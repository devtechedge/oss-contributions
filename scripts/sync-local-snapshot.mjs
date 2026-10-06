#!/usr/bin/env node
/**
 * sync-local-snapshot.mjs — pull merged-PR facts from the ledger into a local career-ops checkout.
 *
 * Why this exists (30 Sep 2026): the GitHub publication targets already refresh themselves on every
 * merge (scripts/sync-merged-oss.mjs, hourly cron + dispatch). The local career-ops user layer is a
 * separate copy that nothing refreshed, so `cv.md`, `config/profile.yml`, `modes/_brief.md`,
 * `modes/_profile.md`, `article-digest.md`, and `documents/devayan-all-details.txt` drifted to an
 * old merged count and an old ledger list.
 *
 * Design rules:
 *   - PATCH, never overwrite. Every file here is in career-ops' own USER_PATHS list, so
 *     `node update-system.mjs` never reverts these edits. Prose stays Dev's; only machine-known
 *     tokens move.
 *   - One in-memory buffer per file, written once. Two rules on one file must never each read
 *     from disk, or the second write clobbers the first.
 *   - Replace callbacks receive (match, ...groups, offset, whole). They rebuild from the GROUPS,
 *     never from indexing the match string.
 *   - Every rule must be a fixed point: running twice changes nothing.
 *   - The merged list is spliced between the LEDGER markers. A local file with no markers is
 *     reported as a problem and left alone rather than guessed at.
 *   - Two API calls per run (ledger + private details). Cheap enough to run hourly.
 *
 * Usage:
 *   node sync-local-snapshot.mjs --target DIR [--check] [--quiet]
 *
 *   --target DIR  career-ops checkout root (required)
 *   --check       report what would change, write nothing, exit 1 if drift exists
 *   --quiet       suppress the per-file change list
 */

import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";

const LEDGER_REPO = "devtechedge/oss-contributions";
const PRIVATE_REPO = "devtechedge/jobsearch-private";
const PUBS_PATH = "docs/triage/publications.json";
const DETAILS_PATH = "devayan-all-details.txt";

const LEDGER_START = "<<<LEDGER:MERGED_LIST>>>";
const LEDGER_END = "<<<END:LEDGER:MERGED_LIST>>>";

const LONG_MONTHS = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December",
];

function parseArgs(argv) {
  const args = { target: null, check: false, quiet: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--target") args.target = argv[++i];
    else if (a === "--check") args.check = true;
    else if (a === "--quiet") args.quiet = true;
    else if (a === "--help" || a === "-h") {
      console.log("Usage: node sync-local-snapshot.mjs --target DIR [--check] [--quiet]");
      process.exit(0);
    } else {
      throw new Error(`Unknown argument '${a}'`);
    }
  }
  if (!args.target) throw new Error("--target DIR is required");
  return args;
}

function run(cmd, argv) {
  const r = spawnSync(cmd, argv, { encoding: "utf8" });
  if (r.error) throw r.error;
  if (r.status !== 0) {
    throw new Error(`${cmd} ${argv.join(" ")} exited ${r.status}: ${(r.stderr || "").trim()}`);
  }
  return r.stdout;
}

function ghRaw(repo, p) {
  const out = run("gh", ["api", `repos/${repo}/contents/${p}`, "--jq", ".content"]);
  return Buffer.from(out.replace(/\s+/g, ""), "base64").toString("utf8");
}

function countFrom(pubs) {
  // Authored merges only: co-authored PRs live in pubs.co_authored and never
  // count; the role filter guards against one landing in records.
  const recs = (pubs.records || []).filter((r) => (r.role || "author") !== "co-author");
  return { merged: recs.length, repos: new Set(recs.map((r) => r.repo)).size };
}

function longDate(iso) {
  const [y, m, d] = iso.split("-").map(Number);
  return `${d} ${LONG_MONTHS[m - 1]} ${y}`;
}

// Every rule captures the surrounding text and rebuilds the match from its GROUPS plus the new
// number. `(\d+)` is never rewritten in place, and nothing is ever derived from indexing the match.
function buildRules(merged, asOf, profileDate, bullets) {
  const n = String(merged);

  // "28 merged upstream pull requests" -> "30 merged upstream pull requests".
  // The old number is captured only so the regex can find it; it is never re-emitted.
  const countPhrase = [
    /\b\d+( merged upstream pull requests)\b/g,
    (m, g1) => `${n}${g1}`,
  ];

  return [
    { file: "cv.md", rules: [countPhrase] },
    { file: "modes/_brief.md", rules: [countPhrase] },
    {
      file: "modes/_profile.md",
      rules: [
        countPhrase,
        [
          /(as recorded in the canonical ledger on )\d{1,2} ([A-Z][a-z]+) (\d{4})/g,
          (m, g1) => `${g1}${profileDate}`,
        ],
      ],
    },
    { file: "article-digest.md", rules: [countPhrase] },
    {
      file: "config/profile.yml",
      rules: [
        [
          /(hero_metric:\s*")\d+( merged upstream pull requests)(")/g,
          (m, g1, g2, g3) => `${g1}${n}${g2}${g3}`,
        ],
      ],
    },
    {
      file: "documents/devayan-all-details.txt",
      requiresMarkers: true,
      list: bullets,
      rules: [
        [
          /(Merged )\d+( upstream pull requests)/g,
          (m, g1, g2) => `${g1}${n}${g2}`,
        ],
        [
          /(records )\d+( merged upstream pull requests)/g,
          (m, g1, g2) => `${g1}${n}${g2}`,
        ],
        [
          /(Tracks )\d+( merged pull requests across [^.\n]* as of )(\d{1,2}) ([A-Z][a-z]+) (\d{4})(\.)/g,
          (m, g1, g2, day, mon, yr, dot) => `${g1}${n}${g2}${day} ${mon} ${yr}${dot}`,
        ],
      ],
    },
  ];
}

function spliceList(text, inner) {
  const s = text.indexOf(LEDGER_START);
  const e = text.indexOf(LEDGER_END);
  if (s === -1 || e === -1 || e <= s) return null;
  return text.slice(0, s) + LEDGER_START + "\n" + inner + "\n" + LEDGER_END + text.slice(e + LEDGER_END.length);
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  const root = path.resolve(args.target);
  if (!fs.existsSync(root)) throw new Error(`target not found: ${root}`);

  const { merged, repos } = countFrom(JSON.parse(ghRaw(LEDGER_REPO, PUBS_PATH)));
  const details = ghRaw(PRIVATE_REPO, DETAILS_PATH);

  const esc = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const listMatch = details.match(new RegExp(`${esc(LEDGER_START)}\\n([\\s\\S]*?)\\n${esc(LEDGER_END)}`));
  if (!listMatch) throw new Error("private details file has no ledger block");

  const asOf = (details.match(/Tracks \d+ merged pull requests across [^.\n]* as of (\d{1,2} [A-Z][a-z]+ \d{4})\./) || [])[1];
  if (!asOf) throw new Error("private details file has no as-of date to mirror");
  // Parse without a Date round trip: `new Date("30 Sep 2026")` is UTC midnight and shifts a day
  // in some local zones.
  const dm = asOf.match(/^(\d{1,2}) ([A-Z][a-z]+) (\d{4})$/);
  if (!dm) throw new Error(`could not parse as-of date '${asOf}'`);
  const mi = LONG_MONTHS.findIndex((m) => m.toLowerCase().startsWith(dm[2].toLowerCase()));
  if (mi === -1) throw new Error(`unknown month '${dm[2]}' in as-of date '${asOf}'`);
  // Long form, because modes/_profile.md is prose and reads better than "30 Sep 2026".
  const profileDate = `${dm[1]} ${LONG_MONTHS[mi]} ${dm[3]}`;

  const changes = [];
  const problems = [];

  for (const spec of buildRules(merged, asOf, profileDate, listMatch[1])) {
    const file = path.join(root, spec.file);
    const prev = fs.existsSync(file) ? fs.readFileSync(file, "utf8") : null;
    if (prev === null) {
      problems.push(`${spec.file} not found under target`);
      continue;
    }
    if (spec.requiresMarkers && !(prev.includes(LEDGER_START) && prev.includes(LEDGER_END))) {
      problems.push(`${spec.file} has no ledger markers; refusing to guess, update by hand`);
      continue;
    }
    let next = prev;
    for (const [re, fix] of spec.rules) next = next.replace(re, fix);
    if (spec.list) {
      const spliced = spliceList(next, spec.list);
      if (spliced === null) {
        problems.push(`${spec.file} ledger block vanished mid-run, skipped`);
        continue;
      }
      next = spliced;
    }
    // Fixed-point guard: a rule that is not idempotent would silently chew the text on run 2.
    let probe = next;
    for (const [re, fix] of spec.rules) probe = probe.replace(re, fix);
    if (probe !== next) {
      problems.push(`${spec.file} rule set is not idempotent, refused to write`);
      continue;
    }
    if (next === prev) continue;
    changes.push(spec.file);
    if (!args.check) fs.writeFileSync(file, next, "utf8");
  }

  console.log(
    JSON.stringify(
      { merged, repos, as_of: asOf, changed: changes, problems, checked: args.check },
      null,
      2,
    ),
  );

  if (problems.length) {
    console.error("Local snapshot incomplete:\n" + problems.map((p) => ` - ${p}`).join("\n"));
    process.exit(1);
  }
  if (args.check && changes.length) process.exit(1);
}

try {
  main();
} catch (err) {
  console.error(err.stack || err.message || String(err));
  process.exit(1);
}

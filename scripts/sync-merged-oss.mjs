#!/usr/bin/env node
/**
 * Unified OSS merge reconciler + publisher.
 *
 * Source of truth: docs/triage/triage.json (operational state)
 * Publication copy: docs/triage/publications.json (curated prose, never overwritten)
 *
 * Idempotent: running once or ten times yields the same files.
 * Commits are the caller's job; this script only writes when content changes.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const DEFAULT_ROOT = path.resolve(__dirname, "..");

const AUTHOR = "devtechedge";
const LEDGER_OWNER = "devtechedge";
const LEDGER_REPO = "oss-contributions";
const PROFILE_REPO = "devtechedge";
const TODAY = new Date().toISOString().slice(0, 10);

const MARK = {
  tableStart: "<!-- ledger:merged-table:start -->",
  tableEnd: "<!-- ledger:merged-table:end -->",
  profileStart: "<!-- ledger:profile-merged:start -->",
  profileEnd: "<!-- ledger:profile-merged:end -->",
  resumeStart: "<<<LEDGER:MERGED_LIST>>>",
  resumeEnd: "<<<END:LEDGER:MERGED_LIST>>>",
  linkedinRepStart: "<<<LEDGER:LINKEDIN_REP>>>",
  linkedinRepEnd: "<<<END:LEDGER:LINKEDIN_REP>>>",
};

function parseArgs(argv) {
  const args = {
    root: DEFAULT_ROOT,
    publishOnly: false,
    dryRun: false,
    prs: [],
    summary: "",
    updateAbout: false,
  };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--root") args.root = path.resolve(argv[++i]);
    else if (a === "--publish-only") args.publishOnly = true;
    else if (a === "--dry-run") args.dryRun = true;
    else if (a === "--update-about") args.updateAbout = true;
    else if (a === "--pr") args.prs.push(argv[++i]);
    else if (a === "--summary") args.summary = argv[++i] ?? "";
    else if (a === "--help" || a === "-h") {
      console.log(`Usage: node scripts/sync-merged-oss.mjs [options]
  --root DIR          Ledger checkout (default: repo root)
  --pr owner/repo#N   Force-reconcile a specific PR (repeatable)
  --summary TEXT      Curated summary for a newly created publication record
  --publish-only      Skip GitHub reconcile; regenerate publication targets
  --update-about      PATCH the GitHub repository description
  --dry-run           Print the plan; write nothing`);
      process.exit(0);
    }
  }
  return args;
}

function readJson(file) {
  return JSON.parse(fs.readFileSync(file, "utf8"));
}

function writeJson(file, value) {
  const text = JSON.stringify(value, null, 2) + "\n";
  return writeIfChanged(file, text);
}

function writeIfChanged(file, next) {
  const prev = fs.existsSync(file) ? fs.readFileSync(file, "utf8") : null;
  if (prev === next) return false;
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, next);
  return true;
}

function prKey(repo, number) {
  return `${repo}#${number}`;
}

function parsePrRef(ref) {
  const m = String(ref).trim().match(/^([^/#]+)\/([^#]+)#(\d+)$/);
  if (!m) throw new Error(`Invalid PR ref '${ref}'. Expected owner/repo#number`);
  return { owner: m[1], repoName: m[2], repo: `${m[1]}/${m[2]}`, number: Number(m[3]) };
}

function formatDisplayDate(iso) {
  if (!iso) return "";
  const d = new Date(iso.includes("T") ? iso : `${iso}T00:00:00Z`);
  const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  return `${d.getUTCDate()} ${months[d.getUTCMonth()]} ${d.getUTCFullYear()}`;
}

function formatMonthYear(iso) {
  if (!iso) return "";
  const d = new Date(iso.includes("T") ? iso : `${iso}T00:00:00Z`);
  const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  return `${months[d.getUTCMonth()]} ${d.getUTCFullYear()}`;
}

function token() {
  return process.env.GITHUB_TOKEN || process.env.GH_TOKEN || process.env.LEDGER_SYNC_TOKEN || "";
}

async function gh(pathname, { method = "GET", body, accept, token: tokenOverride } = {}) {
  const headers = {
    Accept: accept || "application/vnd.github+json",
    "User-Agent": "devtechedge-oss-ledger-sync",
    "X-GitHub-Api-Version": "2022-11-28",
  };
  const t = tokenOverride || token();
  if (t) headers.Authorization = `Bearer ${t}`;
  if (body) headers["Content-Type"] = "application/json";
  const res = await fetch(`https://api.github.com${pathname}`, {
    method,
    headers,
    body: body ? JSON.stringify(body) : undefined,
  });
  const text = await res.text();
  let data = null;
  try {
    data = text ? JSON.parse(text) : null;
  } catch {
    data = text;
  }
  if (!res.ok) {
    const msg = data?.message || text || res.statusText;
    const err = new Error(`GitHub ${method} ${pathname} → ${res.status} ${msg}`);
    err.status = res.status;
    throw err;
  }
  return data;
}

async function ghGraphql(query, variables = {}) {
  return gh("/graphql", { method: "POST", body: { query, variables } });
}

async function fetchPull(owner, repo, number) {
  const p = await gh(`/repos/${owner}/${repo}/pulls/${number}`);
  return {
    repo: `${owner}/${repo}`,
    number: p.number,
    title: p.title,
    body: p.body || "",
    state: p.merged_at ? "merged" : p.state,
    merged: Boolean(p.merged_at),
    merged_at: p.merged_at,
    closed_at: p.closed_at,
    merge_commit: p.merge_commit_sha,
    html_url: p.html_url,
    author: p.user?.login,
    issue: extractIssueNumber(p.body || "", p.title || ""),
  };
}

function extractIssueNumber(body, title) {
  const m = `${body}\n${title}`.match(/\b(?:Fixes|Closes|Resolves)\s+#(\d+)/i);
  return m ? Number(m[1]) : null;
}

function orgOf(repo) {
  return repo.split("/")[0];
}

function defaultDisplayName(repo) {
  const known = {
    "anza-xyz/kit": "Anza Kit",
    "better-auth/better-auth": "Better Auth",
    "biomejs/biome": "Biome",
    "brianc/node-postgres": "node-postgres",
    "pnpm/pnpm": "pnpm",
    "recharts/recharts": "Recharts",
    "web-infra-dev/rspress": "Rspress",
    "SQLMesh/sqlmesh": "SQLMesh",
    "thirdweb-dev/js": "thirdweb JS",
    "pytest-dev/pytest-env": "pytest-env",
  };
  return known[repo] || repo.split("/")[1];
}

function mergedRecords(triage) {
  return (triage.pull_requests || []).filter((p) => p.status === "merged");
}

function sortLedger(a, b) {
  const ta = a.merged_at || a.merged || "";
  const tb = b.merged_at || b.merged || "";
  if (ta !== tb) return ta < tb ? 1 : -1;
  const ra = a.repo.toLowerCase();
  const rb = b.repo.toLowerCase();
  if (ra !== rb) return ra < rb ? -1 : 1;
  return b.number - a.number;
}

function sortProfile(a, b) {
  const na = (a.display_name || defaultDisplayName(a.repo)).toLowerCase();
  const nb = (b.display_name || defaultDisplayName(b.repo)).toLowerCase();
  if (na !== nb) return na < nb ? -1 : 1;
  return a.number - b.number;
}

function findPub(pubs, repo, number) {
  return (pubs.records || []).find((r) => r.repo === repo && r.number === number);
}

function ensurePublication(pubs, facts, { summary, curated } = {}) {
  const existing = findPub(pubs, facts.repo, facts.number);
  if (existing) {
    if (!existing.merged && facts.merged) existing.merged = facts.merged;
    if (!existing.merged_at && facts.merged_at) existing.merged_at = facts.merged_at;
    if (!existing.merge_commit && facts.merge_commit) existing.merge_commit = facts.merge_commit;
    if (existing.issue == null && facts.issue != null) existing.issue = facts.issue;
    return { record: existing, created: false };
  }
  const display = defaultDisplayName(facts.repo);
  const org = orgOf(facts.repo);
  const impact =
    summary ||
    humanizeTitle(facts.title) ||
    `Merged upstream pull request ${facts.repo} #${facts.number}.`;
  const langs = facts.languages || [];
  const langLabel = langs.length ? langs.join("/") : "TypeScript";
  const mergedDay = facts.merged || (facts.merged_at || "").slice(0, 10);
  const monthYear = formatMonthYear(facts.merged_at || mergedDay);
  const record = {
    id: prKey(facts.repo, facts.number),
    repo: facts.repo,
    number: facts.number,
    merged: mergedDay,
    merged_at: facts.merged_at || (mergedDay ? `${mergedDay}T00:00:00Z` : null),
    merge_commit: facts.merge_commit || null,
    issue: facts.issue ?? null,
    url: facts.html_url || `https://github.com/${facts.repo}/pull/${facts.number}`,
    languages: langs,
    org,
    display_name: display,
    profile_title: `${display} #${facts.number}`,
    ledger_logo: `https://github.com/${org}.png?size=40`,
    profile_logo: `https://github.com/${org}.png?size=48`,
    profile_logo_alt: display,
    ledger_what: impact,
    resume_bullet: `${facts.repo} #${facts.number} (${langLabel}) - ${uncap(impact)} Merged ${monthYear}. github.com/${facts.repo}/pull/${facts.number}`,
    linkedin_bullet: `${facts.repo} #${facts.number} - ${uncap(impact)}`,
    profile_line: uncap(impact),
    curated: Boolean(curated || summary),
  };
  pubs.records.push(record);
  return { record, created: true };
}

function humanizeTitle(title) {
  if (!title) return "";
  return title
    .replace(/^(fix|feat|docs|chore|refactor|test|perf)(\([^)]+\))?:\s*/i, "")
    .replace(/\s+/g, " ")
    .trim()
    .replace(/^./, (c) => c.toUpperCase());
}

function uncap(s) {
  if (!s) return s;
  return s.charAt(0).toLowerCase() + s.slice(1);
}

function cap(s) {
  if (!s) return s;
  return s.charAt(0).toUpperCase() + s.slice(1);
}

function joinPubs(triage, pubs) {
  const out = [];
  for (const pr of mergedRecords(triage)) {
    const rec = findPub(pubs, pr.repo, pr.number);
    if (!rec) {
      throw new Error(`Missing publication record for ${pr.repo}#${pr.number}`);
    }
    out.push({
      ...rec,
      merged: rec.merged || pr.merged,
      merged_at: rec.merged_at || pr.merged_at || (pr.merged ? `${pr.merged}T00:00:00Z` : null),
      merge_commit: rec.merge_commit || pr.merge_commit || null,
    });
  }
  return out;
}

function splice(haystack, startMark, endMark, inner, { fallback } = {}) {
  const start = haystack.indexOf(startMark);
  const end = haystack.indexOf(endMark);
  if (start !== -1 && end !== -1 && end > start) {
    return haystack.slice(0, start) + startMark + "\n" + inner + "\n" + endMark + haystack.slice(end + endMark.length);
  }
  if (fallback) return fallback(haystack, inner);
  throw new Error(`Missing markers ${startMark} / ${endMark}`);
}

function rewriteCounts(text, n) {
  return text
    .replace(/Merged \d+ upstream pull requests/g, `Merged ${n} upstream pull requests`)
    .replace(/records \d+ merged upstream pull requests/g, `records ${n} merged upstream pull requests`)
    .replace(/\d+ merged upstream pull requests across/g, `${n} merged upstream pull requests across`)
    .replace(/\d+ merged upstream pull requests span/g, `${n} merged upstream pull requests span`)
    .replace(/merged-\d+/g, `merged-${n}`);
}

function renderLedgerRow(rec) {
  if (rec.ledger_row) return rec.ledger_row;
  const logo = rec.ledger_logo || `https://github.com/${orgOf(rec.repo)}.png?size=40`;
  const date = formatDisplayDate(rec.merged_at || rec.merged);
  return `| <img src="${logo}" width="18" /> [${rec.repo}](https://github.com/${rec.repo}) | [#${rec.number}](${rec.url}) | ${rec.ledger_what} | ${date} |`;
}

function renderProfileBlock(rec) {
  if (rec.profile_block) return rec.profile_block;
  const logo = rec.profile_logo || `https://github.com/${orgOf(rec.repo)}.png?size=48`;
  const alt = rec.profile_logo_alt || rec.display_name || defaultDisplayName(rec.repo);
  const title = rec.profile_title || `${defaultDisplayName(rec.repo)} #${rec.number}`;
  const align = rec.profile_align === false ? "" : ' align="left"';
  return `<img src="${logo}" width="32" height="32" alt="${alt}"${align} /> **[${title}](${rec.url})** - ${rec.profile_line}`;
}

function renderResumeBullet(rec) {
  return rec.resume_bullet.startsWith("- ") ? rec.resume_bullet : `- ${rec.resume_bullet}`;
}

function uniqueRepos(recs) {
  const names = [];
  const seen = new Set();
  for (const rec of [...recs].sort(sortProfile)) {
    const name = rec.display_name || defaultDisplayName(rec.repo);
    if (seen.has(name)) continue;
    seen.add(name);
    names.push(name);
  }
  return names;
}

function oxford(list) {
  if (list.length === 0) return "";
  if (list.length === 1) return list[0];
  if (list.length === 2) return `${list[0]} and ${list[1]}`;
  return `${list.slice(0, -1).join(", ")}, and ${list[list.length - 1]}`;
}

const ABOUT_HARD_CAP = 340;

function aboutDescription(n, recs) {
  const names = uniqueRepos(recs);
  const covering = ", covering SDKs, tooling, frameworks, databases, docs and concurrency fixes";
  const prefix = `Public ledger of upstream open-source contributions: ${n} merged pull requests across TypeScript, Rust and Python. Merged into `;
  const commaAnd = (list) => {
    if (list.length === 0) return "";
    if (list.length === 1) return list[0];
    return `${list.slice(0, -1).join(", ")} and ${list[list.length - 1]}`;
  };
  const candidates = [
    `${prefix}${oxford(names)}${covering}.`,
    `${prefix}${oxford(names)}.`,
  ];
  for (let k = names.length - 1; k >= 1; k--) {
    candidates.push(`${prefix}${commaAnd(names.slice(0, k))} and more.`);
  }
  for (const c of candidates) {
    if (c.length <= ABOUT_HARD_CAP) return c;
  }
  throw new Error(`aboutDescription overflow: even minimal form is ${candidates[candidates.length - 1].length} chars (cap ${ABOUT_HARD_CAP})`);
}

function publishReadme(root, recs, n, dryRun) {
  const file = path.join(root, "README.md");
  let text = fs.readFileSync(file, "utf8");
  text = rewriteCounts(text, n);
  text = text.replace(/\*\*Latest update:\*\* [^\n]+/, `**Latest update:** ${formatDisplayDate(TODAY)}`);
  const rows = [...recs].sort(sortLedger).map(renderLedgerRow).join("\n");
  const table = `| Repo | PR | What | Merged |\n| --- | --- | --- | --- |\n${rows}`;
  try {
    text = splice(text, MARK.tableStart, MARK.tableEnd, table);
  } catch {
    text = text.replace(
      /(## ✅ Merged pull requests\n\n)([\s\S]*?)(\n## 🔀 Open pull requests)/,
      `$1${MARK.tableStart}\n${table}\n${MARK.tableEnd}$3`,
    );
  }
  if (dryRun) return { file, changed: text !== fs.readFileSync(file, "utf8") };
  return { file, changed: writeIfChanged(file, text.endsWith("\n") ? text : text + "\n") };
}

function publishResume(root, recs, n, dryRun) {
  const file = path.join(root, "docs/Devayan_Mandal-resume.txt");
  let text = fs.readFileSync(file, "utf8");
  text = rewriteCounts(text, n);
  const bullets = [...recs].sort(sortLedger).map(renderResumeBullet).join("\n");
  try {
    text = splice(text, MARK.resumeStart, MARK.resumeEnd, bullets);
  } catch {
    text = text.replace(
      /(Merged upstream:\n)([\s\S]*?)(\n\nActive upstream engineering spans)/,
      `$1${MARK.resumeStart}\n${bullets}\n${MARK.resumeEnd}$3`,
    );
  }
  if (dryRun) return { file, changed: text !== fs.readFileSync(file, "utf8") };
  return { file, changed: writeIfChanged(file, text.endsWith("\n") ? text : text + "\n") };
}

function defaultLinkedinRep(rec) {
  return `${rec.display_name || defaultDisplayName(rec.repo)} - ${uncap(rec.ledger_what)}`;
}

function publishLinkedin(root, recs, n, pubs, dryRun) {
  const file = path.join(root, "docs/linkedin-all-details.txt");
  let text = fs.readFileSync(file, "utf8");
  text = rewriteCounts(text, n);

  const grouped = [];
  const seen = new Set();
  const byRepo = new Map();
  for (const rec of recs) {
    if (!byRepo.has(rec.repo)) byRepo.set(rec.repo, []);
    byRepo.get(rec.repo).push(rec);
  }
  const repoOrder = [...byRepo.keys()].sort((a, b) => {
    const aa = [...byRepo.get(a)].sort(sortLedger)[0];
    const bb = [...byRepo.get(b)].sort(sortLedger)[0];
    return sortLedger(aa, bb);
  });
  for (const repo of repoOrder) {
    if (seen.has(repo)) continue;
    seen.add(repo);
    const override = pubs.repos?.[repo]?.linkedin_representative;
    if (override) grouped.push(`• ${override.replace(/^•\s*/, "")}`);
    else grouped.push(`• ${defaultLinkedinRep(byRepo.get(repo)[0])}`);
  }

  try {
    text = splice(text, MARK.linkedinRepStart, MARK.linkedinRepEnd, grouped.join("\n\n"));
  } catch {
    text = text.replace(
      /(Representative work:\n\n)([\s\S]*?)(\n\nActive contribution areas include)/,
      `$1${MARK.linkedinRepStart}\n${grouped.join("\n\n")}\n${MARK.linkedinRepEnd}$3`,
    );
  }

  if (dryRun) return { file, changed: text !== fs.readFileSync(file, "utf8") };
  return { file, changed: writeIfChanged(file, text.endsWith("\n") ? text : text + "\n") };
}

function publishExperiencePaste(root, dryRun) {
  const src = path.join(root, "docs/linkedin-all-details.txt");
  const text = fs.readFileSync(src, "utf8");
  const expHead = text.indexOf("2. Open-Source Software Contributor");
  const descHead = expHead === -1 ? -1 : text.indexOf("DESCRIPTION", expHead);
  const bodyHead = descHead === -1 ? -1 : text.indexOf("\n", descHead) + 1;
  const skillsHead = bodyHead <= 0 ? -1 : text.indexOf("KEY SKILLS", bodyHead);
  if (skillsHead === -1) throw new Error("experience paste: Experience block not found");
  const paste = text
    .slice(bodyHead, skillsHead)
    .split("\n")
    .filter((l) => !l.includes("<<<LEDGER") && !l.includes("<<<END:LEDGER"))
    .join("\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
  const file = path.join(root, "docs/generated/linkedin-experience-paste.txt");
  const next = paste + "\n";
  if (dryRun) return { file, changed: !fs.existsSync(file) || fs.readFileSync(file, "utf8") !== next };
  return { file, changed: writeIfChanged(file, next) };
}

function publishProfileFragment(root, recs, dryRun) {
  const blocks = [...recs].sort(sortProfile).map(renderProfileBlock).join("\n\n");
  const inner = `${MARK.profileStart}\n${blocks}\n${MARK.profileEnd}`;
  const file = path.join(root, "docs/generated/profile-merged.md");
  if (dryRun) {
    const prev = fs.existsSync(file) ? fs.readFileSync(file, "utf8") : "";
    return { file, changed: prev !== inner + "\n", content: inner };
  }
  return { file, changed: writeIfChanged(file, inner + "\n"), content: inner };
}

function publishProfileReadme(root, recs, dryRun) {
  const fragment = publishProfileFragment(root, recs, dryRun);
  const file = path.join(root, "docs/generated/profile-README.md");
  if (!fs.existsSync(file)) return fragment;
  let text = fs.readFileSync(file, "utf8");
  const blocks = [...recs].sort(sortProfile).map(renderProfileBlock).join("\n\n");
  try {
    text = splice(text, MARK.profileStart, MARK.profileEnd, blocks);
  } catch {
    text = text.replace(
      /(### Merged:\n\n)([\s\S]*?)(\n---\n)/,
      `$1${MARK.profileStart}\n${blocks}\n${MARK.profileEnd}$3`,
    );
  }
  if (dryRun) return { file, changed: text !== fs.readFileSync(file, "utf8"), fragment };
  return { file, changed: writeIfChanged(file, text.endsWith("\n") ? text : text + "\n"), fragment };
}

function publishResumeHtml(root, recs, n, dryRun) {
  const file = path.join(root, "docs/generated/Devayan_Mandal-resume.html");
  const bullets = [...recs]
    .sort(sortLedger)
    .map((r) => `<li>${escapeHtml(r.resume_bullet.replace(/^- /, ""))}</li>`)
    .join("\n");
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Devayan Mandal - Resume</title>
  <style>
    :root { color-scheme: light; }
    body { font: 11.5pt/1.45 "Source Sans 3", "Segoe UI", sans-serif; max-width: 800px; margin: 32px auto; color: #1a1c1f; }
    h1 { font-size: 22pt; letter-spacing: -0.03em; margin: 0 0 4px; }
    h2 { font-size: 11pt; text-transform: uppercase; letter-spacing: 0.08em; margin: 22px 0 8px; border-bottom: 1px solid #d5d8dd; padding-bottom: 4px; }
    .sub { color: #4b5563; margin-bottom: 16px; }
    ul { padding-left: 18px; }
    li { margin: 0 0 6px; }
    @media print { body { margin: 16px 20px; } }
  </style>
</head>
<body>
  <h1>Devayan Mandal</h1>
  <p class="sub">Full Stack AI Native / Forward Deployed AI Engineer & Open Source Contributor</p>
  <h2>Open source</h2>
  <p>Merged ${n} upstream pull requests. Canonical ledger: github.com/devtechedge/oss-contributions</p>
  <ul>
${bullets}
  </ul>
</body>
</html>
`;
  if (dryRun) return { file, changed: !fs.existsSync(file) || fs.readFileSync(file, "utf8") !== html };
  return { file, changed: writeIfChanged(file, html) };
}

function escapeHtml(s) {
  const map = {
    "&": "&" + "amp;",
    "<": "&" + "lt;",
    ">": "&" + "gt;",
    '"': "&" + "quot;",
  };
  return String(s).replace(/[&<>"]/g, (ch) => map[ch]);
}

function countIn(text) {
  const m = text.match(/merged-(\d+)/) || text.match(/Merged (\d+) upstream/) || text.match(/(\d+) merged upstream pull requests/);
  return m ? Number(m[1]) : null;
}

function validate(triage, recs, files) {
  const n = recs.length;
  const triageN = mergedRecords(triage).length;
  const problems = [];
  if (triageN !== n) problems.push(`triage merged=${triageN} publications=${n}`);
  // linkedin-all-details.txt no longer carries the per-PR LEDGER list (removed Sep 2026),
  // so only its merged count is checked here, not individual PR numbers.
  const NUMBER_CHECKED = new Set(["README", "resume", "profile-fragment"]);
  for (const [label, text] of files) {
    const c = countIn(text);
    if (c != null && c !== n) problems.push(`${label} count=${c} expected=${n}`);
    if (!NUMBER_CHECKED.has(label)) continue;
    for (const rec of recs) {
      if (!text.includes(`#${rec.number}`)) {
        problems.push(`${label} missing ${rec.repo}#${rec.number}`);
      }
    }
  }
  const liText = (files.find(([label]) => label === "linkedin") || [])[1] || "";
  const expHead = liText.indexOf("2. Open-Source Software Contributor");
  const descHead = expHead === -1 ? -1 : liText.indexOf("DESCRIPTION", expHead);
  const bodyHead = descHead === -1 ? -1 : liText.indexOf("\n", descHead) + 1;
  const skillsHead = bodyHead <= 0 ? -1 : liText.indexOf("KEY SKILLS", bodyHead);
  if (skillsHead !== -1) {
    const paste = liText
      .slice(bodyHead, skillsHead)
      .split("\n")
      .filter((l) => !l.includes("<<<LEDGER") && !l.includes("<<<END:LEDGER"))
      .join("\n")
      .replace(/\n{3,}/g, "\n\n")
      .trim();
    if (paste.length > 1990 || paste.length < 1980) problems.push(`linkedin Experience paste=${paste.length} outside 1980-1990 window`);
  }
  return problems;
}

function upsertPr(triage, facts) {
  const list = triage.pull_requests || (triage.pull_requests = []);
  let rec = list.find((p) => p.repo === facts.repo && p.number === facts.number);
  const created = !rec;
  if (!rec) {
    rec = { repo: facts.repo, number: facts.number };
    list.unshift(rec);
  }
  rec.status = facts.merged ? "merged" : facts.state === "closed" ? "closed" : "open";
  rec.last_checked = TODAY;
  rec.do_not_duplicate = true;
  if (facts.merged) {
    rec.merged = (facts.merged_at || TODAY).slice(0, 10);
    rec.merge_commit = facts.merge_commit || rec.merge_commit || null;
    rec.merged_at = facts.merged_at || rec.merged_at;
    delete rec.mergeable;
    delete rec.opened;
  }
  if (facts.issue != null) rec.issue = facts.issue;
  else if (rec.issue === undefined) rec.issue = null;
  if (!rec.summary && facts.summary) rec.summary = facts.summary;
  return { rec, created };
}

function upsertIssue(triage, { repo, number, status, related, note }) {
  const list = triage.issues || (triage.issues = []);
  let rec = list.find((i) => i.repo === repo && i.number === number);
  if (!rec) {
    rec = { repo, number };
    list.unshift(rec);
  }
  rec.status = status;
  rec.attempted = true;
  rec.do_not_duplicate = true;
  rec.last_checked = TODAY;
  if (related) rec.related_prs = Array.from(new Set([...(rec.related_prs || []), related]));
  if (note) rec.note = note;
  return rec;
}

function addRepoContribution(triage, repo, number) {
  const repos = triage.repositories || (triage.repositories = {});
  const entry = repos[repo] || (repos[repo] = { contributions: [], focus: "" });
  if (!Array.isArray(entry.contributions)) entry.contributions = [];
  if (!entry.contributions.includes(number)) entry.contributions.push(number);
}

async function reconcileOne(triage, pubs, ref, { summary } = {}) {
  const { owner, repoName, repo, number } = typeof ref === "string" ? parsePrRef(ref) : ref;
  if (owner === AUTHOR) {
    return { facts: { repo, number, merged: false, author: AUTHOR }, created: false, skipped: "own-repo" };
  }
  const facts = await fetchPull(owner, repoName, number);
  if (facts.author && facts.author !== AUTHOR) {
    throw new Error(`${repo}#${number} author is @${facts.author}, not @${AUTHOR}`);
  }
  const { rec } = upsertPr(triage, facts);
  if (facts.merged && !rec.summary) {
    rec.summary = summary || `${facts.title}. Merge commit ${(facts.merge_commit || "").slice(0, 7)}.`;
  }
  if (facts.issue) {
    upsertIssue(triage, {
      repo,
      number: facts.issue,
      status: facts.merged ? "closed" : "open",
      related: number,
      note: facts.merged
        ? `Closed by merged PR #${number} (${(facts.merge_commit || "").slice(0, 7)}).`
        : `Tracked by PR #${number}.`,
    });
  }
  if (facts.merged) addRepoContribution(triage, repo, number);
  const pubFacts = { ...facts, languages: findPub(pubs, repo, number)?.languages };
  const { created } = ensurePublication(pubs, pubFacts, {
    summary,
    curated: Boolean(summary),
  });
  return { facts, created };
}

async function reconcileTrackedOpen(triage, pubs) {
  const open = (triage.pull_requests || []).filter((p) => p.status === "open" || p.status === "draft");
  if (open.length === 0) return { checked: 0, merged: [] };
  if (!token()) {
    console.warn("No GITHUB_TOKEN; skipping tracked-open reconcile");
    return { checked: 0, merged: [] };
  }
  const merged = [];
  const chunkSize = 12;
  for (let i = 0; i < open.length; i += chunkSize) {
    const chunk = open.slice(i, i + chunkSize);
    const fields = chunk
      .map((p, idx) => {
        const [owner, name] = p.repo.split("/");
        return `p${idx}: repository(owner: "${owner}", name: "${name}") { pullRequest(number: ${p.number}) { number title state merged mergedAt mergeCommit { oid } url author { login } body } }`;
      })
      .join("\n");
    const data = await ghGraphql(`query { ${fields} }`);
    if (data.errors) throw new Error(data.errors.map((e) => e.message).join("; "));
    for (let idx = 0; idx < chunk.length; idx++) {
      const node = data.data[`p${idx}`]?.pullRequest;
      const tracked = chunk[idx];
      tracked.last_checked = TODAY;
      if (!node) continue;
      if (node.merged) {
        const facts = {
          repo: tracked.repo,
          number: tracked.number,
          title: node.title,
          body: node.body || "",
          state: "merged",
          merged: true,
          merged_at: node.mergedAt,
          merge_commit: node.mergeCommit?.oid,
          html_url: node.url,
          author: node.author?.login,
          issue: tracked.issue ?? extractIssueNumber(node.body || "", node.title || ""),
        };
        upsertPr(triage, facts);
        if (facts.issue) {
          upsertIssue(triage, {
            repo: tracked.repo,
            number: facts.issue,
            status: "closed",
            related: tracked.number,
            note: `Closed by merged PR #${tracked.number}.`,
          });
        }
        addRepoContribution(triage, tracked.repo, tracked.number);
        ensurePublication(pubs, facts);
        merged.push(prKey(tracked.repo, tracked.number));
      } else if (node.state === "CLOSED") {
        tracked.status = "closed";
      }
    }
  }
  return { checked: open.length, merged };
}

async function discoverRecentMerged(triage, pubs) {
  if (!token()) return [];
  const since = new Date(Date.now() - 14 * 24 * 3600 * 1000).toISOString().slice(0, 10);
  const q = encodeURIComponent(`author:${AUTHOR} is:pr is:merged updated:>=${since} -user:${AUTHOR}`);
  let data;
  try {
    data = await gh(`/search/issues?q=${q}&per_page=20`);
  } catch (err) {
    console.warn("search skipped:", err.message);
    return [];
  }
  const found = [];
  for (const item of data.items || []) {
    const repo = item.repository_url.replace("https://api.github.com/repos/", "");
    const number = item.number;
    const already = (triage.pull_requests || []).find((p) => p.repo === repo && p.number === number && p.status === "merged");
    if (already) continue;
    if (repo.startsWith(`${AUTHOR}/`)) continue;
    const [owner, repoName] = repo.split("/");
    await reconcileOne(triage, pubs, { owner, repoName, repo, number });
    found.push(prKey(repo, number));
  }
  return found;
}

// The repository description is an admin-level PATCH. secrets.GITHUB_TOKEN
// cannot do it even with `permissions: contents: write` (GitHub answers 403
// "Resource not accessible by integration"), which is why the About text went
// stale while every other publication target kept syncing. LEDGER_SYNC_TOKEN is
// the PAT that unblocks it; the fallback keeps local runs working unchanged.
function adminToken() {
  return process.env.LEDGER_SYNC_TOKEN || "";
}

async function updateAbout(n, recs) {
  const description = aboutDescription(n, recs);
  await gh(`/repos/${LEDGER_OWNER}/${LEDGER_REPO}`, {
    method: "PATCH",
    body: { description },
    token: adminToken() || token(),
  });
  return description;
}

// The profile repo is a different repository, so secrets.GITHUB_TOKEN (which is
// scoped to the ledger repo) cannot write to it. LEDGER_SYNC_TOKEN is an
// optional PAT with contents:write on the profile repo. Without it the profile
// README is left untouched rather than failing the run.
function profileToken() {
  return process.env.LEDGER_SYNC_TOKEN || "";
}

async function publishProfileReadmeRemote(recs) {
  const t = profileToken();
  if (!t) return { skipped: "LEDGER_SYNC_TOKEN not set" };
  const p = `/repos/${AUTHOR}/${PROFILE_REPO}/contents/README.md`;
  const cur = await gh(p, { token: t });
  if (!cur || typeof cur.content !== "string" || !cur.sha) {
    return { skipped: "could not read profile README" };
  }
  const branch = cur.branch || "main";
  const text = Buffer.from(cur.content, "base64").toString("utf8");
  const blocks = [...recs].sort(sortProfile).map(renderProfileBlock).join("\n\n");
  let next;
  try {
    next = splice(text, MARK.profileStart, MARK.profileEnd, blocks);
  } catch {
    return { skipped: "profile README missing ledger:profile-merged markers" };
  }
  if (next === text) return { changed: false };
  await gh(p, {
    token: t,
    method: "PUT",
    body: {
      message: `chore(ledger): sync merged OSS to profile README (${recs.length} merged)`,
      content: Buffer.from(next, "utf8").toString("base64"),
      sha: cur.sha,
      branch,
    },
  });
  return { changed: true };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const root = args.root;
  const triagePath = path.join(root, "docs/triage/triage.json");
  const pubsPath = path.join(root, "docs/triage/publications.json");
  const triage = readJson(triagePath);
  const pubs = fs.existsSync(pubsPath)
    ? readJson(pubsPath)
    : { schema_version: 1, records: [], repos: {} };
  if (!Array.isArray(pubs.records)) pubs.records = [];
  if (!pubs.repos) pubs.repos = {};

  const report = { merged: [], createdPubs: [], files: [], about: null, problems: [] };

  if (!args.publishOnly) {
    for (const ref of args.prs) {
      const result = await reconcileOne(triage, pubs, ref, { summary: args.summary });
      if (result.skipped) continue;
      report.merged.push(prKey(result.facts.repo, result.facts.number));
      if (result.created) report.createdPubs.push(prKey(result.facts.repo, result.facts.number));
    }
    const tracked = await reconcileTrackedOpen(triage, pubs);
    report.merged.push(...tracked.merged);
    const discovered = await discoverRecentMerged(triage, pubs);
    report.merged.push(...discovered);
    triage.last_updated = TODAY;
  }

  const recs = joinPubs(triage, pubs);
  const n = recs.length;
  pubs.last_updated = TODAY;
  pubs.merged_count = n;

  const writes = [];
  writes.push(publishReadme(root, recs, n, args.dryRun));
  writes.push(publishResume(root, recs, n, args.dryRun));
  writes.push(publishLinkedin(root, recs, n, pubs, args.dryRun));
  writes.push(publishExperiencePaste(root, args.dryRun));
  writes.push(publishProfileReadme(root, recs, args.dryRun));
  writes.push(publishResumeHtml(root, recs, n, args.dryRun));

  if (!args.dryRun) {
    const py = path.join(root, "scripts/render-resume-artifacts.py");
    if (fs.existsSync(py)) {
      const rendered = spawnSync("python3", [py, root], { encoding: "utf8" });
      if (rendered.status !== 0) {
        console.warn("resume artifact render skipped:", rendered.stderr || rendered.stdout);
      } else {
        // The renderer only writes when the bytes changed, so trust its
        // "wrote <path>" lines instead of assuming every artifact moved.
        const wrote = new Set(
          String(rendered.stdout || "")
            .split("\n")
            .filter((line) => line.startsWith("wrote "))
            .map((line) => line.slice("wrote ".length).split(" (")[0].trim()),
        );
        const docx = path.join(root, "docs/generated/Devayan_Mandal-resume.docx");
        const pdf = path.join(root, "docs/generated/Devayan_Mandal-resume.pdf");
        if (fs.existsSync(docx)) writes.push({ file: docx, changed: wrote.has(docx) });
        if (fs.existsSync(pdf)) writes.push({ file: pdf, changed: wrote.has(pdf) });
      }
    }
  }

  if (!args.dryRun) {
    const masterPy = path.join(root, "scripts/render-resume-docx.py");
    const masterDocx = path.join(root, "docs/Devayan_Mandal.docx");
    if (fs.existsSync(masterPy) && fs.existsSync(masterDocx)) {
      const before = fs.readFileSync(masterDocx);
      const rendered = spawnSync("python3", [masterPy, root], { encoding: "utf8" });
      if (rendered.status !== 0) {
        console.warn("::warning::master resume DOCX not updated:", rendered.stderr || rendered.stdout);
      } else {
        const after = fs.readFileSync(masterDocx);
        writes.push({ file: masterDocx, changed: !before.equals(after) });
      }
    }
  }

  if (!args.dryRun) {
    writes.push({ file: triagePath, changed: writeJson(triagePath, triage) });
    writes.push({ file: pubsPath, changed: writeJson(pubsPath, pubs) });
  }

  const fileTexts = [
    ["README", fs.readFileSync(path.join(root, "README.md"), "utf8")],
    ["resume", fs.readFileSync(path.join(root, "docs/Devayan_Mandal-resume.txt"), "utf8")],
    ["linkedin", fs.readFileSync(path.join(root, "docs/linkedin-all-details.txt"), "utf8")],
    ["profile-fragment", fs.existsSync(path.join(root, "docs/generated/profile-merged.md"))
      ? fs.readFileSync(path.join(root, "docs/generated/profile-merged.md"), "utf8")
      : fs.existsSync(path.join(root, "docs/generated/profile-README.md"))
        ? fs.readFileSync(path.join(root, "docs/generated/profile-README.md"), "utf8")
        : ""],
  ];
  report.problems = args.dryRun ? [] : validate(triage, recs, fileTexts);
  report.files = writes.filter((w) => w.changed).map((w) => path.relative(root, w.file));
  report.merged_count = n;
  report.about_preview = aboutDescription(n, recs);

  if (args.updateAbout && token() && !args.dryRun) {
    try {
      report.about = await updateAbout(n, recs);
    } catch (err) {
      report.about_error = err.message;
      console.warn("About update skipped:", err.message);
    }
  }

  if (!args.dryRun) {
    try {
      report.profile_readme = await publishProfileReadmeRemote(recs);
    } catch (err) {
      report.profile_readme_error = err.message;
      console.warn("Profile README sync skipped:", err.message);
    }
  }

  console.log(JSON.stringify({ ok: report.problems.length === 0, ...report }, null, 2));
  if (report.problems.length) {
    console.error("Invariant failed:\n" + report.problems.map((p) => ` - ${p}`).join("\n"));
    process.exit(1);
  }
}

main().catch((err) => {
  console.error(err.stack || err.message || err);
  process.exit(1);
});

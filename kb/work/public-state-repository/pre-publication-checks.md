# Pre-publication checks for the state tree

## Scope and provenance

Commissioned by the operator on 2026-11-11 as a read-only audit for the
[public state repository](./README.md) workshop. It covers items 2 to 6 of
"Before anything is published", the "Links" open question and the
cross-machine open question. Nothing under `kb/reports/state/` was changed.

The audited tree is `kb/reports/state/` on 2026-11-11: 281 files, 18 MB.
Its subdirectories are `fixes/` (55 files), `ingest/` (empty),
`meta-analyser-pilot-20261021/` (33 files, 14 MB), `review/` (89 files),
`revise-autoreason/` (57 files), `tag-placement/` (36 files) and `x-likes/`
(9 files). `README.md` and `.commonplace-validation-ignore` are tracked by the
main repository.

The tree is ignored, so every `rg` command below uses `--no-ignore`. Commands
run from `kb/reports/state/` unless they name another directory.

## Summary for the decision

- No real credential was found.
- `x-likes/` must not be published. It holds the operator's private like
  history and the full text of 142 third-party posts.
- Review continuation is not portable. A review run directory refuses to open
  under a different checkout path. Review results are portable, but this
  checkout holds none.
- The meta-analyser pilot traces carry about 2.5 MB of MIT-licensed
  OpenResearch source excerpts without the licence notice.
- The state README is out of date in five places.
- No tracked file links to a live file in the state tree. Six tracked files
  name a live file by path.

## 2. Secrets

**Verdict: no real credential found. The 10 key-pattern files are false
positives: 2 contain provider-encrypted reasoning blobs and 8 contain note
slugs that start with `sk-`.**

### Evidence

Strict credential patterns:

```bash
P='sk-[A-Za-z0-9_-]{16,}|sk-ant-|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{20,}|github_pat_|gho_|xox[abprs]-|-----BEGIN [A-Z ]*PRIVATE KEY|Bearer [A-Za-z0-9._-]{10,}|AIza[0-9A-Za-z_-]{30,}'
rg --no-ignore --hidden -l -e "$P" .
```

This matched 10 files, the same 10 the workshop README reports after item 1.

- 8 files in `tag-placement/2026-09-26/` (`aggregate.json`,
  `assigned-tags.json`, `finalize-8795.json`, `finalize-8799.json`,
  `finalize-8807.json`, `jobs.json`, `run.json`, `selector.json`). Every match
  is the tail of a note slug such as `...-sk-success-does-not-establish-intended-path-health`.
  Not a credential.
- `meta-analyser-pilot-20261021/openresearch-claim-first/stdout.log` and
  `meta-analyser-pilot-20261021/import-case-trace-first/stdout.log`. Every
  `sk-` match sits inside a 557- to 1371-character run that starts
  hundreds of characters earlier, after `"encrypted_content":"`. These are
  OpenAI encrypted reasoning blobs that the Pi harness logged. The `sk-` is
  a coincidental substring. Not a credential.

Broad keyword patterns, each counted with
`rg --no-ignore --hidden -i -l -e '<pattern>' . | wc -l`:

| Pattern | Files | Disposition |
|---|---|---|
| `api[_-]?key` | 0 | none |
| `(access\|auth\|refresh\|bearer\|session)[_-]?token` | 1 | quoted Rust source (`set_up_auth_token`) in a pilot trace |
| `secret` | 4 | prose ("secrets or services") in 3 pilot traces; "Secret Service" in a post in `x-likes/zby/sync.json` |
| `password\|passwd` | 0 | none |
| `Bearer ` | 0 | none |
| `[A-Z_]*(KEY\|TOKEN\|SECRET)[A-Z_]*=` | 0 | none |
| `ANTHROPIC_\|OPENAI_\|GITHUB_TOKEN\|GH_TOKEN\|AWS_` (case-insensitive) | 2 | quoted Rust source (`openai_base_url`); case-sensitive count is 0 |
| `-----BEGIN [A-Z ]*PRIVATE KEY` (case-sensitive) | 0 | none |
| `ssh-(rsa\|ed25519) AAAA` | 0 | none |
| `cookie\|ct0\|auth_token` | 3 | `ct0` inside a tool-call id; quoted source |

Long runs: `rg --no-ignore --hidden -l '[A-Za-z0-9+/_-]{60,}' .` and a Python
classifier over each hit. 37 files hold 40+ character lowercase hex runs; these
are SHA-256 hashes and commit ids. Mixed-case runs occur in 16 files, all in
`meta-analyser-pilot-20261021/` and `x-likes/2026-09-24-literature-batch/`.
They are absolute paths, reasoning and tool-call ids, and `encrypted_content`
blobs (3 to 42 per pilot `stdout.log`). None is a credential.

Email addresses:
`rg --no-ignore --hidden -l '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' .`
matched 0 files.

Account identifiers:
`rg --no-ignore -l '"user_id"' .` matched only `x-likes/zby/sync.json`, which
holds the operator's numeric X user id. The pilot and review logs hold 26
`session_id` and 6 `thread_id` values. These are harness session identifiers,
not credentials.

Third-party personal data: `x-likes/zby/sync.json` holds 142 posts with
author id, display name and handle for 97 distinct authors. See item 4.

### For the operator

- The encrypted reasoning blobs are opaque provider data. They are not
  secrets, but they add nothing for a reader. Excluding the pilot traces
  removes them; see item 4.
- These patterns must be rerun before every later push. Pilot-style harness
  logs (`stdout.log` from Pi or Codex JSON mode) are the likeliest place for a
  future leak, because they record whole tool results.

## 3. Machine-specific paths

**Verdict: two files are operational references that break on another
machine: the review runs' `calls/run.json`. The other 40 `/home/zby` files
are historical records with no consumer in `src/`.**

### Evidence

`rg --no-ignore --hidden -l '/home/zby' . | wc -l` gives 42 files: 26 in
`meta-analyser-pilot-20261021/`, 14 in `review/`, 1 in `tag-placement/`, 1 in
`x-likes/`. Occurrences by prefix (from `rg --no-ignore -o '/home/zby/[^"\\ ]{0,60}'`):
4,453 under `/home/zby/llm/commonplace/.commonplace` (analysis worktrees), 805
under `/home/zby/llm/commonplace/kb`, 69 under `/home/zby/.pi/agent/install`,
22 at the checkout root.

| Files | Class | Consumer and effect elsewhere |
|---|---|---|
| `review/runs/revise/*/*/calls/run.json` (2) | (a) operational | `headless.jobs` opens it through `workjig.Run` (workjig 0.3.1). Its top-level `workdir` is `/home/zby/llm/commonplace`. `workjig/run.py` `_load_or_create` raises `RecordError("run workdir differs from recorded workdir")` when the checkout path differs. Repeating the workflow command, which continues the run by replay, fails. `dismiss` and `approve` take only the lock (`workjig.hold`) and do not hit this check. Each attempt's absolute `launch_dir` is also read by `headless.jobs.describe()` for a stderr tail; that read degrades silently. |
| `review/runs/revise/*/*/calls/launches/*/prompt.txt` (6) and `stdout.log` (6) | (b) historical | Workjig writes them per launch for the worker. Replay reads outputs from `run.json`, not these files. |
| `tag-placement/2026-09-26/run.json` | (b) historical | Producer was the SQLite review pipeline, deleted in `3562ca982`. Also names `library_override: /tmp/commonplace-tag-placement-catalogue-f01io9q3`, which no longer exists. |
| `meta-analyser-pilot-20261021/**` (26) | (b) historical | Launched by an ad hoc launcher that is not in `src/` or `scripts/` (`rg -l "launcher.log\|complete.json" scripts src` matched nothing). No code reads these files. The retained prompts name 4 of them by absolute path (see Links). |
| `x-likes/2026-09-24-literature-batch/handoffs.md` | (b) historical | Prose links to run directories under `agentic-system-analysis/`, which moved to the archive. The links are already broken. |

Other markers:

| Pattern | Files | What |
|---|---|---|
| `/tmp/` | 3 | Pi's `/tmp/pi-bash-*.log` overflow paths in 2 pilot traces; the `library_override` above |
| `/usr/`, `/opt/`, `/mnt/`, `/var/`, `/etc/`, `/Users/`, `C:\\` | 0 | none |
| `/root`, `.local/share` | 1 | quoted Rust source and prose in one pilot trace |
| `related-systems/` | 8 | all in the pilot; paths into the OpenResearch analysis worktree |
| hostname `zby-Z4` | 0 | none |
| word `zby` outside `/home/zby` | review 7 files, x-likes 3 | the article's GitHub Discussions URL `github.com/zby/commonplace`; the `x-likes/zby/` handle directory |

Commands: `rg --no-ignore --hidden -l -e '<pattern>' . | wc -l` per pattern,
and `rg --no-ignore --hidden -l -F "$(hostname)" .`.

Review result files are clean. In the worktree that holds results (see the
cross-machine section), `grep -rl /home/zby` over `results/` and `packets/`
matched 0 files.

### For the operator

- Decide whether the two review run directories should be published at all.
  They are revision runs from 2026-11-10. Another machine can read them but
  cannot continue them unless its checkout is also at `/home/zby/llm/commonplace`.
- Making runs portable is a workjig or headless change: record `workdir`
  relative to the run, or allow an explicit rebinding. That is out of scope
  here; record it as a gap if continuation across machines is wanted.
- Leave historical paths unrewritten, as the workshop README directs.

## 4. Redistribution

**Verdict: `x-likes/` is not publishable. The pilot traces need a licence
decision. `fixes/`, `review/`, `revise-autoreason/` and `tag-placement/`
quote only Commonplace's own text, plus one attributed two-line quotation.**

### Evidence

Fenced and quoted blocks per directory, from
`rg --no-ignore -l '^\s*```' <dir>` and `rg --no-ignore -l '^> ' <dir>`:

| Directory | Files with fences | Files with `>` quotes | Origin |
|---|---|---|---|
| `fixes/` | 0 | 0 | Commonplace notes |
| `revise-autoreason/` | 0 | 16 | Commonplace notes; one two-line Karpathy quotation with attribution and link |
| `review/` | 6 | 7 | Commonplace criteria and the article under revision |
| `tag-placement/` | 0 | 0 | Commonplace notes and tag heads |
| `x-likes/` | 0 | 0 | see below |
| `meta-analyser-pilot-20261021/` | 0 | 0 | quotes sit inside JSON tool results, see below |

**`x-likes/`** holds:

- `zby/sync.json` (346 KB, file mode 600). State for `scripts/sync_x_likes.py`,
  which still exists and still reads it. It contains the operator's X user id,
  142 seen post ids with first-observed times, and 142 active payloads. Each
  payload has the full post text, expanded links and the author's id, name
  and handle; there are 97 distinct authors. The 21-day expiry only runs during
  a sync, and the last sync was 2026-09-24, so all 142 payloads are still
  present. X stopped showing likes publicly in 2024, so this file discloses
  private reading history.
- `2026-09-24-literature-batch/`: a Codex batch record from 2026-09-24
  (`report.md`, `handoffs.md`, `papers.json`, `systems.json`, `discovery.json`,
  `tweet-provenance.json`). It lists 50 arXiv ingests and the liked post URLs
  that led to them. Its producer was a one-off agent batch, not a command.
- `evidence/2101345320957300772-cognitive-load.png`: a screenshot of a page of
  the book "The Math Academy Way", taken from a post. It quotes Anderson (1987)
  and Chase and Ericsson (1982). This is third-party copyrighted material.
- `.sync.lock`: an empty lock file.

I did not check X's developer terms for redistributing post content. The
privacy problem is enough to exclude the directory.

**`tag-placement/2026-09-26/`** is a tag-placement review of 388 notes and 848
tag assignments, run as jobs 8790 to 8810 of the SQLite review pipeline with
`gpt-6-sol` workers. That pipeline was deleted in `3562ca982`. The run
reviewed `kb/notes/`, which no longer exists. Its operator report is in
`kb/reports/cache/tag-placement/`. Its README says thirteen parent conflicts
"require disposition before retagging". The data is Commonplace's own.

**`meta-analyser-pilot-20261021/`** is the raw state of the Pi meta-analyser
prompt pilot. The tracked record is
`kb/reports/retained/meta-analyser-pilot-20261021/README.md`, which already
records a decision. The pilot launcher is not in the repository. The
instruction it tested survives as
`kb/agentic-system-analyses/instructions/analyse-agentic-system/meta-analyser.md`
and is used by `src/commonplace/lib/agentic_analysis/audit.py`. The retained
README warned that these logs "may contain private source/trace material".

The traces quote external source. A JSON pass over each `stdout.log`
(summing `tool_execution_end` results) gives these tool-result sizes:

| Trace | Tool results | Characters | OpenResearch files read |
|---|---|---|---|
| `openresearch-trace-first` | 15 | 1,026,690 | 3 |
| `openresearch-claim-first` | 27 | 834,820 | 5 |
| `openresearch-compact` | 23 | 614,368 | 10 |
| `import-case-*` (2) | 10 each | about 15,000 each | 0 (synthetic fixture) |

Most of those characters are the analysed run's own worker traces, which in
turn contain OpenResearch source reads. OpenResearch is
`https://github.com/alphaXiv/OpenResearch`. Its licence file in the analysis
worktree (`.commonplace/worktrees/openresearch-62725ad1cd0a/related-systems/alphaXiv--OpenResearch/LICENSE`)
is MIT, "Copyright (c) 2026 alphaXiv". MIT permits redistribution if the
notice accompanies substantial portions. The traces do not carry the notice.
The traces also embed the Pi harness system prompt and its install paths.

**`fixes/`** holds 55 fix reports written by the
[fix system](../../instructions/FIX-SYSTEM.md), dated 2026-04-13 to
2026-08-18. They quote review warnings about Commonplace notes.

**`revise-autoreason/`** holds two runs from 2026-04-13. The skill now writes
runs to `kb/work/revise-autoreason/` and deletes them, so these are
leftovers.

### For the operator

- Exclude `x-likes/` from the public repository, for example with a
  `.gitignore` inside it. `scripts/sync_x_likes.py` writes there, so the
  exclusion must be permanent, not a one-time omission.
- For the pilot traces, choose one: exclude them (the retained report already
  holds the prompts and final reports); or publish them with an MIT notice for
  OpenResearch. Excluding them also removes 14 of the 18 MB.
- The pilot's evidence role looks finished, because the retained README records
  a decision. Whether it may be deleted is the operator's call.

## 5. Copied snapshots

**Verdict: no copied snapshot remains in the tree.**

### Evidence

Real snapshots use `type: types/snapshot.md` with `source:`, `captured:` and
`capture:` fields (checked on
`kb/sources/.snapshots/01-what-did-ilya-see.md`).

- `rg --no-ignore --hidden -l 'types/snapshot\.md' .` matched 0 files.
- `rg --no-ignore --hidden -l '^(captured|capture|source|source_url|snapshot):' .`
  matched 0 files.
- `rg --no-ignore -l 'captured: ' .` matched 0 files, so no snapshot is
  embedded inside a JSON string either.
- `rg --no-ignore --hidden -il '<html|<!doctype' .` matched 0 files.
- `rg --no-ignore --hidden -l 'sources/\.snapshots/' .` matched 1 file,
  `x-likes/2026-09-24-literature-batch/papers.json`. It names 50 snapshot
  paths and hashes; it copies no content.

The two snapshot-like files the workshop README counted were presumably in
the trees moved to the archive. I did not verify that, because the archive is
out of scope.

The only full external page is the PNG screenshot in `x-likes/` (item 4).

### For the operator

Nothing to decide here beyond item 4.

## 6. Reader-facing status

**Verdict: the state README needs rewriting before publication. Draft text
and the discrepancies follow.**

### Draft paragraph for a public reader

> This repository holds operational state from Commonplace workflows. It is
> unreviewed model output kept so that work can continue and be inspected; it
> is not endorsed by inclusion. Expect failed candidates, abandoned runs and
> records from methods that have since changed. `review/` belongs to
> `commonplace-review`. Its `results/` hold the current review coverage, one
> judgment per note and criterion. Its `packets/` hold each note's latest
> full-pass disposition. Its `runs/` hold replay records that only open in a
> checkout at the original path. `fixes/` holds warning dispositions from the
> fix system. `ingest/` holds ingest drafting runs while they are open. The
> other directories are leftovers: `revise-autoreason/` from an earlier version
> of that skill and `tag-placement/` from the retired SQLite review pipeline.
> Library files in the main repository do not depend on anything here. A
> state commit does not record which main-repository commit it belongs to.

The last sentence should change if the operator records the pairing.

### Current state README against the tree

| README says | Tree has |
|---|---|
| `review/` holds `results/`, `packets/` and `runs/` | only `review/runs/revise/` (2 runs); no results, no packets |
| `agentic-system-transfer/` | does not exist |
| analysis "now owns working runs under `kb/agentic-systems/reports/state/`" | code places runs in each worktree's `kb/agentic-system-analyses/state/` (`STATE_ROOT` in `src/commonplace/lib/agentic_analysis/worktree.py`) |
| (not mentioned) | `meta-analyser-pilot-20261021/`, `tag-placement/`, `x-likes/` |
| `ingest/` described as holding runs | empty |
| lists deletable abandoned data (SQLite, `review-jobs/` and others) | those moved to the archive in item 1 |

### `kb/agentic-systems/reports/state/`

That tree does not need to join the public repository for collaborators to run
analyses. The
[analysis skill](../../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md)
prepares a dedicated worktree per analysis. The code keeps each run directly
under that worktree's `kb/agentic-system-analyses/state/`, and controllers
under `.commonplace/worktrees/controllers/`, with absolute paths checked on
reload (`automation.py`: `record.get("controller") != str(state)`). Accepted
publications integrate into tracked `retained/` sets. `kb/agentic-systems/reports/state/`
holds 8 instinctual-memory runs from 2026-10-01 and 2026-10-02 under an earlier
method. Their own README says they cannot resume under the current method,
and 108 of their files contain `/home/zby`. Collaborators need neither tree.
Continuing someone else's in-flight analysis would need the worktree itself,
which no state repository provides.

## Links

**Verdict: no tracked file links to a live file in the state tree. Six
tracked files name a live file by path; one is a test fixture path.**

### Evidence

A Python pass over `git ls-files` (excluding `kb/reports/state/`) found
Markdown links whose target resolves into a `reports/state/` path:

- `kb/work/public-state-repository/README.md` links `../../reports/state/README.md`.
  That file is tracked, so this is not a dependency on state.
- `kb/reports/retained/agentic-analysis-output-documents-20261002/captures/batch-01-rerun-2026-09-28.md`
  has 3 absolute links into another worktree's
  `kb/reports/state/agentic-system-analysis/`. They are already dead.

The same pass found concrete file paths (`kb/reports/state/...` ending in a
file extension) in tracked text. Those that exist today:

| Live file named | Tracked files naming it |
|---|---|
| `kb/reports/state/README.md` | `src/commonplace/scaffold_manifest.py`, `kb/agentic-systems/reports/retained/layout-migration-2026-10-01/package-probe.json` |
| `meta-analyser-pilot-20261021/openresearch-input/attempts.json` and `scanner.json` | `kb/reports/retained/meta-analyser-pilot-20261021/openresearch-trace-first-prompt.txt`, `openresearch-claim-first-prompt.txt` |
| `meta-analyser-pilot-20261021/openresearch-compact/attempts.json` and `scanner.json` | `kb/reports/retained/meta-analyser-pilot-20261021/openresearch-compact-prompt.txt` |
| `x-likes/zby/sync.json` | `tests/commonplace/sources/test_sync_x_likes_script.py` (path under a temporary root) |

105 tracked files name state files that no longer exist. By top directory:
`agentic-system-analysis/` 1,250 mentions, `review-jobs/` 520, `full-pass/`
74, `reviews/` 32, the SQLite stores 18, others 10. Most are in
`kb/reports/retained/`. They are historical mentions, not links.

### For the operator

The retained pilot prompts are exact records of what workers received. Their
input maps name state files by absolute path. That is evidence, not a
dependency. If the pilot traces are excluded or deleted, those paths dangle,
which is acceptable for a historical prompt.

## Cross-machine reuse of review results

**Verdict: a collaborator needs `review/results/**`, plus `review/packets/**`
for unresolved full-pass work. Result files are repository-relative and
portable. This checkout has no results to share.**

### What a collaborator needs

From `results.py` and `gates.py`:

- `review/results/<note-path>/<criterion-id>.md`. `gates._fresh()` and
  `results.freshness()` decide whether a pair needs review from the result's
  two hashes and the current note and criterion files. Nothing else is read.
- `review/packets/<note-path>`, only for a full pass with a pending hand-back.
  `full_pass.py` reads the current packet from there.
- `review/runs/` is not needed for freshness or status. It is needed only to
  continue a run, which fails on another checkout path (item 3).

Freshness also needs the same note and criterion text. A collaborator on a
different main commit sees stale pairs. In an installed project, criteria
named `commonplace:<path>` hash the installed library's text, so a
different Commonplace version also stales them.

### Are paths repository-relative in the actual files?

This checkout has no `review/results/` or `review/packets/`:
`ls kb/reports/state/review` shows only `runs/`. The only result files found
on this machine are in the agent worktree
`.claude/worktrees/agent-ad870d0e81ccb2af4/` (branch
`worktree-agent-ad870d0e81ccb2af4`, commit `be81ed972`): 37 results and 1
packet, all for `kb/theory/definitions/storage-substrate.md`.

Three sampled results (`complexity/could-be-a-paragraph.md`,
`prose/mannered-prose.md`, `structural/general-before-specific.md`) have:

- `note: kb/theory/definitions/storage-substrate.md` (repository-relative);
- `criterion: kb/instructions/review-gates/...` (repository-relative);
- `run: kb/reports/state/review/runs/20261109T235356Z` (repository-relative,
  informational only).

`grep -rl /home/zby` over that worktree's `results/` and `packets/` matched
0 files. `results._posix()` refuses absolute paths and `..`, so the code
enforces this.

### For the operator

- If current review coverage should be shared, it has to come from wherever
  results are produced. Either the main checkout's sweeps have not written
  results yet, or they were lost. The worktree's 37 results are a test run.
- The review architecture page names `kb/reports/state/review/` as fixed
  paths in `results.RESULTS` and `gates.STATE`. A nested checkout at
  `kb/reports/state/` keeps them valid.

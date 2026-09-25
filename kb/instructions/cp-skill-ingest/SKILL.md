---
name: cp-skill-ingest
description: Use when asked to ingest one URL or local snapshot into a tracked .ingest.md source analysis, or to execute a bounded re-ingest request. Retaining quotes in an existing ingest is cp-skill-ground's job, not this skill's.
type: types/instruction.md
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Skill, Task
context: fork
model: opus
argument-hint: "[url-or-file | re_ingest_request] — URL, snapshot path, or structured re-ingest request. No argument lists recent snapshots."
---

# Ingest source

Preserve a faithful, reusable account of what a source contributes to the
installed KB and what its evidence supports.

Ingest one URL-backed primary source into a tracked
`kb/sources/*.ingest.md` report. The reading copy may already exist as a
Markdown snapshot under `kb/sources/.snapshots/`.

## Contract

**Target:** `$ARGUMENTS`

The direct output is the `.ingest.md` report in `kb/sources/`, with the local
snapshot's slug. URL snapshotting and connection discovery may write their own
local or generated artifacts. The parent may also shorten an unpaired local
snapshot's filename under Step 1 without changing its bytes. Do not directly
write any other library artifacts.

The parent agent owns target resolution, snapshotting, checksum guards,
connection discovery, drafting-worker dispatch, handoff verification, final
validation, and user reporting. One primary fresh drafting worker owns the
ingest analysis and writes the `.ingest.md` report; at most one fresh
replacement worker may repair that report after a failed handoff. Use only a
harness-provided sub-agent or worker mechanism; never launch `codex`, `codex
exec`, `claude`, or another agent CLI from the shell. If the harness cannot
launch a fresh worker without carrying the parent's conversation history, stop
after connection discovery and report that isolated drafting is unavailable.
Do not draft locally unless the user explicitly authorizes a local fallback
for that run. If authorized, execute the same standalone drafting instruction
with the same fixed inputs and report `drafting was local, not delegated` as a
workflow exception.

The drafting worker executes the standalone `draft-ingest-report.md`
instruction. That instruction owns report analysis, writing, and worker-side
verification; this skill owns only the surrounding orchestration.

The caller may supply an **occasion**: the question or job that brought the
source in. It is the one task-specific input the worker receives beyond the
fixed paths. It must be stated before the source is read and must not carry
the parent's reading of the source; the worker records it and lets it govern
only the report's selection sections. An occasion that is already an exact
source-side claim is `cp-skill-ground`'s job once the ingest exists; pass the
broader question here, or none.

The canonical empty Quotes block is the following complete Markdown section,
including the blank line after its sentence:

```markdown
## Quotes

No source quotes have been retained yet.

```

A re-ingest caller supplies this structured request instead of an ordinary
URL-or-file target:

```yaml
re_ingest_request:
  ingest_path: <exact ingest path>
  snapshot_path: <name-paired snapshot path>
  occasion: <optional; omitted keeps the incumbent's occasion field>
```

## Steps

1. **Resolve the target and replacement policy.**
   - If the target is a `re_ingest_request`, require exactly one existing
     `kb/sources/<slug>.ingest.md` and its exact name-paired
     `kb/sources/.snapshots/<slug>.md`. Reject a different `snapshot_path`; do
     not search for a snapshot by checksum. Read the ingest's `source` and
     `snapshot_sha256`, reject the retired `source_snapshot` and
     `code_revisions` fields, and require the snapshot's frontmatter `source`
     to equal the ingest's canonical `source`. Compute lowercase SHA-256 from
     the exact snapshot bytes.
     - Require zero or one incumbent Quotes block; stop before mutation if more
       than one exists. The block starts at the exact `## Quotes` heading and
       includes every byte through the byte immediately before the next
       level-two heading. If the section is absent, use the canonical empty
       Quotes block; do not infer quotes from any other section. Treat Quotes as
       empty only when the section is absent or is exactly the canonical empty
       block. Any other present Quotes block is populated.
     - If the snapshot checksum equals the incumbent `snapshot_sha256`, set
       `retained_quotes` to the extracted block and continue. Do not rewrite,
       normalize, or reformat it.
     - If the checksums differ, stop before connection discovery, backup
       creation, worker dispatch, or output mutation. Report both checksums,
       both paired paths, and the canonical source. An ingest's
       `snapshot_sha256` is immutable because a note marked `(snapshot
       required)` may depend on those exact bytes even when Quotes is empty. A
       changed observation requires a distinct snapshot basename and ingest;
       re-ingest never changes the incumbent observation.
     - Set `occasion` to the request's value when supplied, else to the
       incumbent's frontmatter `occasion` verbatim, else `none`.
     - Set `output_path` to the supplied `ingest_path`, retain whether it existed
       at the start of the run, and skip the remaining Step 1 bullets.
   - If `$ARGUMENTS` is empty, list recent
     `kb/sources/.snapshots/*.md` files, then ask which one to ingest.
   - For an ordinary `arxivb.org/abs/<paper-id>` URL, resolve the paper before
     searching for an existing ingest. arXivBangers is a discovery site with
     abstracts and automated editorial commentary; the default ingest target
     is the full paper it links to. Use `https://arxiv.org/abs/<paper-id>` as
     the canonical target, preserving an explicit version suffix and dropping
     query strings and fragments. Use that URL for duplicate lookup and
     `source` metadata, then let `cp-skill-snapshot-web` fetch the full PDF
     through its arXiv route. Report this resolution to the user. Do not fall
     back to the arXivBangers abstract if paper capture fails. An explicit
     request to analyze the arXivBangers page itself keeps the supplied URL;
     local-snapshot targets and structured re-ingest requests retain their
     existing source identity. Never repurpose an existing arXivBangers ingest
     or change its checksum to represent the full paper.
   - For a URL target, first search tracked `kb/sources/*.ingest.md` files for
     an exact frontmatter `source` match. If several match, stop and report the
     duplicate ingests. If one matches, resolve only its name-paired snapshot.
     If that file is missing, capture the ingest's canonical `source` and
     continue only if the adapter returns that exact name-paired path. Do not
     search other snapshots for the incumbent checksum.
   - If the target is a `paperswithcode.co/paper/` URL, or it is an arXiv paper
     and the user explicitly requested code grounding, read and follow the
     conditional procedure [ingest-paper-with-code](../ingest-paper-with-code.md),
     resolved from this skill's real location.
     Use the paper snapshot and code-grounding context it returns. Skip the next
     two target-input bullets, then resume with the snapshot-frontmatter bullet
     so the common output, Quotes, and checksum guards still run.
   - If no snapshot has been resolved and the target starts with `http://` or
     `https://`, invoke
     `cp-skill-snapshot-web` on the URL. Parse the `Snapshot saved:` or
     `Already snapshotted:` line from its output; that path is the source
     snapshot for the next step.
   - For a non-URL target, require one Markdown file under
     `kb/sources/.snapshots/`. A directory is not a v1 primary source.
   - Read the snapshot frontmatter. Retain `source`, `captured`, `capture`,
     optional `capture_scope` and `doi`, and flat capture-adapter fields such
     as `status_id`, `conversation_id`, `post_count`, or `api_url`. Do not
     copy snapshot `type`, `description`, or `tags`.
   - Compute lowercase SHA-256 from the exact Markdown file bytes after capture
     completes. Do not hash a JSON, PDF, image, or other companion.
   - Derive `kb/sources/<slug>.ingest.md`. Before connection discovery, require
     the snapshot basename to be at most 63 characters and the derived path's
     stem (`<slug>.ingest`) to be at most 70 characters. If either is overlong
     and no ingest exists at the derived path or was resolved for this source,
     choose a shorter descriptive slug automatically. Require both the new
     snapshot path and new ingest path to be unused; on a collision, choose
     another short slug. Rename only the local Markdown snapshot, verify its
     SHA-256 is unchanged, update the resolved paths, and continue without
     asking the user. Do not stop merely because the initial name is overlong.
     Never rename an existing ingest or its paired snapshot through this
     recovery; report overlong existing pairs for explicit relocation. If URL
     resolution already found an ingest, require this derived path to equal it. For every
     existing output, require the snapshot to be its exact name-paired path,
     require exact frontmatter `source` equality, and require its
     `snapshot_sha256` to equal the snapshot checksum. On a mismatch, stop and
     report the permanent `re-ingest.md` route; an ordinary target never
     authorizes a changed observation. Extract `retained_quotes` exactly as
     defined above, using the canonical empty block when the incumbent section
     is absent. For a new output, set `retained_quotes` to the canonical empty
     block.

     On an ordinary-target checksum mismatch, report one permanent route with
     the exact ingest path filled in: `Read and execute the Commonplace library
     instruction re-ingest with Target: <path>.`

2. **Run connection discovery.**
   Invoke `cp-skill-connect` on the source snapshot path. Wait for it to finish.
   For a source snapshot, require the completed report at
   `kb/reports/cache/connect/sources/<snapshot-name>.connect.md`. Verify that it
   exists and is non-empty. The parent does not extract connections, classify
   the source, or begin value judgments; those belong to the fresh drafting
   worker.

3. **Prepare the drafting handoff.**
   Resolve these exact inputs without writing a brief file:
   - `draft_instruction_path`: the absolute path of
     [draft-ingest-report](../draft-ingest-report.md), resolved from this
     skill's real location, so the worker can open it
   - `snapshot_path`: the Markdown snapshot from Step 1
   - `connect_report_path`: the generated report from Step 2
   - `output_path`: `kb/sources/<snapshot-slug>.ingest.md`
   - `snapshot_sha256`: the checksum already computed from `snapshot_path`
   - `retained_quotes`: the complete Quotes block resolved in Step 1
   - `code_grounding_context`: only when returned by the paper-with-code branch;
     include its secondary-source commit URLs, claim classifications, pinned
     citations, evidence boundaries, and execution status; retain paper version,
     checkout paths, and reviewed commits only in the parent for final reporting
   - `occasion`: the caller's pre-reading question or job, verbatim, or `none`;
     for a re-ingest, the value resolved in Step 1

   Require the instruction, snapshot, and connect report to exist and be
   non-empty. Recompute the snapshot checksum immediately before dispatch and
   require it to equal `snapshot_sha256`. Do not pass the parent conversation,
   any part of an existing ingest other than `retained_quotes`, the backup path,
   or the parent's interpretations to the worker.

   If `output_path` existed when Step 1 began, create a unique backup in the
   platform's temporary directory, outside `kb/`, before dispatch. Hash the
   incumbent's exact bytes, copy it with the platform's native byte-copy
   operation (for example, `cp` on POSIX or `Copy-Item -LiteralPath` in
   PowerShell), and require the backup's SHA-256 to equal that incumbent hash.
   Do not use a text read/write cycle. Stop before dispatch if creating,
   hashing, or verifying the backup fails. Retain the verified backup path and
   incumbent hash in the parent through the primary attempt and the one
   permitted repair attempt.

4. **Draft through one primary fresh worker.**
   Launch one newly isolated sub-agent or worker with only the dispatch below
   as task context. Use a clean-context launch; do not fork or attach the
   parent's conversation history. If the harness cannot provide that
   isolation, follow the fail-closed rule in the contract. Use the harness
   worker mechanism only.

   Give the worker this dispatch with every placeholder filled in. The warning
   against orchestration skills is load-bearing: skill discovery can re-fire in
   a worker context and would otherwise recurse. Substitute `retained_quotes`
   as an unquoted, unindented multiline value without changing any of its bytes.

   ```text
   Execute {draft_instruction_path} as the delegated ingest-report drafting
   worker. That instruction and the fixed inputs below are your complete brief.
   Do not invoke or follow any auto-loaded skill, including cp-skill-ingest,
   cp-skill-connect, or cp-skill-snapshot-web. Their orchestration work is
   already complete. Do not spawn another agent.

   Fixed inputs:
   - mode: create
   - snapshot_path: {snapshot_path}
   - connect_report_path: {connect_report_path}
   - output_path: {output_path}
   - snapshot_sha256: {snapshot_sha256}
   - retained_quotes: {retained_quotes_exact_multiline_value}
   - code_grounding_context: {code_grounding_context_or_none}
   - occasion: {occasion_or_none}
   - validation_failures: none
   ```

5. **Verify the drafting handoff.**
   Wait for the primary worker to finish, collect its response, then close,
   terminate, or release it before continuing. Require `output_path` to exist
   and be non-empty. Recompute the snapshot checksum and require it still to
   equal both the pre-dispatch checksum and the ingest's `snapshot_sha256`.
   Require exactly one Quotes block, immediately before `## Connections Found`,
   whose bytes equal `retained_quotes`. Verify that the ingest retained the
   snapshot's capture metadata, including `capture_scope` and `doi` when present,
   contains no `source_snapshot` or `code_revisions`, and does not link to
   `.snapshots/`, cite a `related-systems/` checkout, or name the generated
   connect report. For a code-grounded ingest, verify its `secondary_sources`
   and `Code Grounding` section against the supplied context. When an occasion
   was supplied, require frontmatter `occasion` to equal it; when none was,
   require the field to be absent. Run full validation:

   ```bash
   commonplace-validate kb/sources/some-article.ingest.md
   ```

   If this run created the source snapshot, validate that snapshot explicitly.
   A candidate is clean only when the checksum check, exact Quotes comparison,
   every other handoff check, and full validation all pass.

   If the primary worker did not produce a clean report, launch at most one new
   fresh replacement worker with the same clean-context boundary. Dispatch the
   same standalone instruction and fixed inputs, including the identical
   `retained_quotes`, but set `mode: repair` and supply the exact handoff or
   validation failures in `validation_failures`. Leave the failed primary
   candidate at `output_path` for that repair worker. Do not add parent
   interpretations or a rewritten analysis brief. Wait for the replacement,
   collect its response, close, terminate, or release it, then repeat every
   checksum, Quotes, handoff, and full-validation check. Do not retain either
   single-use worker for another task.

6. **Accept or restore.**
   Any handled failure after the backup is verified and before acceptance,
   including a worker-launch failure, follows the existing-output restoration
   branch below.

   - After a clean primary or repair candidate, accept the replacement. If a
     verified backup exists, delete it only now. Report any backup-cleanup
     failure and retain its path without changing the validated ingest.
   - After handled final failure for an existing output, copy the verified
     backup over `output_path` with the same platform-native byte-copy operation.
     Hash the restored file and require it to equal the retained incumbent hash.
     After successful verification, delete the backup and report both the failed
     refresh and successful restoration. If restoration or its verification
     fails, retain the backup and report its path and both failures.
   - After handled final failure for a new output, stop and report the blocker;
     there is no incumbent to restore. Never draft or repair the analysis in the
     parent context.

7. **Discover connections for the accepted ingest.**
   Run this step only after Step 6 accepts a clean primary or repair candidate,
   including a same-checksum refresh. Invoke `cp-skill-connect` on `output_path`
   and wait for completion. This is a separate pass from snapshot discovery;
   keep its report at
   `kb/reports/cache/connect/sources/<snapshot-slug>.ingest.connect.md`.
   Require a non-empty report whose `source` is `output_path` and run
   `commonplace-validate` on that report. Read its `Bidirectional Candidates`
   and `Reverse-edge Candidates`, including an explicit `None` when there
   are no candidates. Each proposed inbound link must independently serve a
   reader need under the linking artifact's collection contract; an outbound
   ingest link alone does not justify a return link.

   Do not author these candidates into the ingest or other library artifacts.
   If discovery or report validation fails, keep the accepted ingest, report
   connection discovery as incomplete, and give `cp-skill-connect <output_path>`
   as the retry. Do not restore an incumbent or repeat drafting for this failure.

8. **Report the result.**
   - On success, tell the user where the ingest report was saved, that drafting
     was delegated, and the report's recommended next action. For a
     paper-with-code ingest, also report the paper version, checkout paths,
     reviewed commits, execution status, and validation result.
   - For an accepted ingest, also give the post-ingest connect report path and
     summarize its inbound-link candidates, or state that none were found.
     Distinguish a validated ingest from incomplete connection discovery when
     Step 7 fails; do not report that links were authored.
   - On handled final failure for an existing output, report that the refresh
     failed and the incumbent was restored with its verified SHA-256. Do not
     present the failed candidate as saved output.
   - On a restore failure or a failed new ingest, report the blocker and any
     retained backup path exactly as required by Step 6.

## Constraints

- Run `cp-skill-connect` before classification or value extraction.
- Draft through one primary fresh harness worker using the source snapshot and
  generated connect report; on failure, allow at most one fresh replacement.
  Never pass the parent's full orchestration context.
- Do not draft locally when worker delegation is unavailable unless the user
  explicitly authorizes that fallback for the current run.
- The drafting worker writes only the `.ingest.md` report. Outside an explicitly
  authorized local-fallback run, the parent owns no substantive report drafting
  or repair.
- Write only the `.ingest.md` report directly.
- Accept exactly one URL-backed primary source; reject directory primaries.
- Pair an ingest only with its name-derived snapshot. A checksum verifies that
  named file; it never discovers a substitute.
- Never update an existing ingest's `snapshot_sha256`. Changed source bytes are
  a new observation with a distinct snapshot basename and ingest path.
- Do not add staging, atomic rename, locks, compare-and-swap, crash recovery, or
  concurrent-writer coordination. This procedure covers handled failures only.

---
name: cp-skill-ingest
description: Use when asked to ingest one URL or an existing local snapshot into a tracked .ingest.md source analysis.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Skill, Task
context: fork
model: opus
argument-hint: "[url-or-file] — URL (https://...) or path to .md file in kb/sources/.snapshots/. No argument lists recent snapshots."
---

# Ingest source

Ingest one URL-backed primary source into a tracked
`kb/sources/*.ingest.md` report. The reading copy may already exist as a
Markdown snapshot under `kb/sources/.snapshots/`.

## Contract

**Target:** `$ARGUMENTS`

The direct output is the `.ingest.md` report in `kb/sources/`, with the local
snapshot's slug. URL snapshotting and connection discovery may write their own
local or generated artifacts. Do not directly write any other library
artifacts.

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

## Steps

1. **Resolve the target.**
   - If `$ARGUMENTS` is empty, list recent
     `kb/sources/.snapshots/*.md` files, then ask which one to ingest.
   - For a URL target, first search tracked `kb/sources/*.ingest.md` files for
     an exact frontmatter `source` match. If several match, stop and report the
     duplicate ingests. If one matches, read its `snapshot_sha256` and resolve
     the local input by checksum before considering a URL duplicate:
     - use the sole exact checksum match;
     - stop and report every path if several local files match;
     - if none matches, capture the ingest's `source` and compare the returned
       file's checksum;
     - continue only when recapture is exact;
     - on adapter failure, report the source as unavailable;
     - on different bytes, report both checksums and stop without changing the
       ingest. Changing the durable observation requires explicit re-ingestion
       after the analysis is reconsidered.
   - If the target is a `paperswithcode.co/paper/` URL, or it is an arXiv paper
     and the user explicitly requested code grounding, read and follow the
     conditional procedure `ingest-paper-with-code.md`. In an installed project
     use `kb/commonplace/instructions/ingest-paper-with-code.md`; in the
     Commonplace source checkout use `kb/instructions/ingest-paper-with-code.md`.
     Skip the remaining Step 1 bullets, then continue at Step 2 with the paper
     snapshot and code-grounding context returned by that procedure.
   - If the target starts with `http://` or `https://`, invoke
     `cp-skill-snapshot-web` on the URL. Parse the `Snapshot saved:` or
     `Already snapshotted:` line from its output; that path is the source
     snapshot for the next step.
   - Otherwise, require one Markdown file under
     `kb/sources/.snapshots/`. A directory is not a v1 primary source.
   - Read the snapshot frontmatter. Retain `source`, `captured`, `capture`, and
     flat capture-adapter fields such as `status_id`, `conversation_id`,
     `post_count`, or `api_url`. Do not copy snapshot `type`, `description`, or
     `tags`.
   - Compute lowercase SHA-256 from the exact Markdown file bytes after capture
     completes. Do not hash a JSON, PDF, image, or other companion.
   - Derive `kb/sources/<slug>.ingest.md`. If it already exists, require its
     `snapshot_sha256` to equal the input file's checksum before overwriting its
     analysis. A filename or canonical-URL match never overrides a checksum
     mismatch.

2. **Run connection discovery.**
   Invoke `cp-skill-connect` on the source snapshot path. Wait for it to finish.
   For a source snapshot, require the completed report at
   `kb/reports/connect/sources/<snapshot-name>.connect.md`. Verify that it
   exists and is non-empty. The parent does not extract connections, classify
   the source, or begin value judgments; those belong to the fresh drafting
   worker.

3. **Prepare the drafting handoff.**
   Resolve these exact inputs without writing a brief file:
   - `draft_instruction_path`: use
     `kb/commonplace/instructions/draft-ingest-report.md` in an installed
     project or `kb/instructions/draft-ingest-report.md` in the Commonplace
     source checkout
   - `snapshot_path`: the Markdown snapshot from Step 1
   - `connect_report_path`: the generated report from Step 2
   - `output_path`: `kb/sources/<snapshot-slug>.ingest.md`
   - `snapshot_sha256`: the checksum already computed from `snapshot_path`
   - `code_grounding_context`: only when returned by the paper-with-code branch;
     include its secondary-source commit URLs, claim classifications, pinned
     citations, evidence boundaries, and execution status; retain paper version,
     checkout paths, and reviewed commits only in the parent for final reporting

   Require the instruction, snapshot, and connect report to exist and be
   non-empty. Recompute the snapshot checksum immediately before dispatch and
   require it to equal `snapshot_sha256`. Do not pass the parent conversation,
   the body of an existing ingest, or the parent's interpretations to the
   worker.

4. **Draft through one primary fresh worker.**
   Launch one newly isolated sub-agent or worker with only the dispatch below
   as task context. Use a clean-context launch; do not fork or attach the
   parent's conversation history. If the harness cannot provide that
   isolation, follow the fail-closed rule in the contract. Use the harness
   worker mechanism only.

   Give the worker this dispatch with every placeholder filled in. The warning
   against orchestration skills is load-bearing: skill discovery can re-fire in
   a worker context and would otherwise recurse.

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
   - code_grounding_context: {code_grounding_context_or_none}
   - validation_failures: none
   ```

5. **Verify the drafting handoff.**
   Wait for the primary worker to finish, collect its response, then close,
   terminate, or release it before continuing. Require `output_path` to exist
   and be non-empty. Recompute the snapshot checksum and require it still to
   equal both the pre-dispatch checksum and the ingest's `snapshot_sha256`.
   Verify that the ingest retained the snapshot's capture metadata, contains no
   `source_snapshot` or `code_revisions`, and does not link to `.snapshots/`,
   cite a `related-systems/` checkout, or name the generated connect report.
   For a code-grounded ingest, verify its `secondary_sources` and `Code
   Grounding` section against the supplied context.

   If the primary worker did not produce a clean report, launch at most one new
   fresh replacement worker with the same clean-context boundary. Dispatch the
   same standalone instruction and fixed inputs, but set `mode: repair` and
   supply the exact handoff or validation failures in `validation_failures`.
   Do not add parent interpretations or a rewritten analysis brief. Wait for
   the replacement, collect its response, then close, terminate, or release it
   before evaluating the result. If that attempt also fails, stop and report
   the blocker; do not draft or repair the analysis in the parent context. Do
   not retain either single-use worker for another task.

6. **Validate.**
   Run:

   ```bash
   commonplace-validate kb/sources/some-article.ingest.md
   ```

   If this run created the source snapshot, validate that snapshot explicitly.
   If final ingest validation fails and the replacement attempt has not already
   been used, use the one fresh replacement-worker path from Step 5. Otherwise,
   stop and report the blocker. Do not make substantive report edits in the
   parent context.

7. **Report the result.**
   Tell the user where the ingest report was saved, that drafting was delegated,
   and the report's recommended next action. For a paper-with-code ingest, also
   report the paper version, checkout paths, reviewed commits, execution status,
   and validation result.

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
- Never update an existing ingest's `snapshot_sha256` merely because a
  recapture produced different bytes.

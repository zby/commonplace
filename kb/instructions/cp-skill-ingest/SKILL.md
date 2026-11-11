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
snapshot's slug. It is drafted as a candidate in an ignored working directory,
`kb/reports/state/ingest/<slug>/`, and copied to `kb/sources/` only after it
passes the handoff check; until then an existing ingest stays unchanged. URL
snapshotting and connection discovery may write their own local or generated
artifacts. The parent may also shorten an unpaired local
snapshot's filename under Step 1 without changing its bytes. Do not directly
write any other library artifacts.

The parent agent owns target resolution, snapshotting, checksum guards,
connection discovery, drafting-worker dispatch, handoff verification, final
validation, and user reporting. One primary fresh drafting worker owns the
ingest analysis and writes the candidate; at most one fresh replacement
worker may repair that candidate after a failed handoff. The parent publishes
the accepted candidate. Use only a
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
For scientific papers, its experimental contribution assessment draws on the
worker's pretrained NeurIPS reviewing methodology, interpreted through
Commonplace's Popperian approach to problem solving and criticism. The
standalone drafting instruction carries this cue into the fresh worker.

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
     to equal the ingest's canonical `source`.
     - Set `occasion` to the request's value when supplied, else to the
       incumbent's frontmatter `occasion` verbatim, else `none`.
     - Set `output_path` to the supplied `ingest_path` and skip to the final
       Step 1 bullet, which opens the handoff. Its guards enforce the checksum
       and Quotes rules: an ingest's `snapshot_sha256` is immutable because a
       note marked `(snapshot required)` may depend on those exact bytes even
       when Quotes is empty. A changed observation gets a new date-named
       capture and a new ingest (re-ingest's **New observation**); re-ingest
       never changes the incumbent observation.
   - If no target was given, list recent
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
     an exact frontmatter `source` match. Several matches are separate
     observations of one source: list them with their `captured` dates and
     stop for the user to name one ingest path, or to request a new
     observation through re-ingest. If one matches, resolve only its
     name-paired snapshot. If that file is missing, stop and report `snapshot
     not available on this machine`; do not recapture, because a new capture
     cannot reproduce the pinned bytes. Do not search other snapshots for the
     incumbent checksum.
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
     resolution already found an ingest, require this derived path to equal it.
   - Open the handoff once `output_path` is final and capture has completed:

     ```bash
     commonplace-ingest-handoff prepare <output_path>
     ```

     Add `--occasion '<occasion>'` when an occasion was supplied,
     `--code-grounded` when the paper-with-code branch returned context, and
     `--created-snapshot` when this run created the source snapshot.

     The command requires the name-paired snapshot and hashes its exact
     Markdown bytes. For an existing output it also requires the snapshot's
     `source` to equal the ingest's, the ingest's `snapshot_sha256` to equal
     the snapshot checksum, and zero or one Quotes block. It then creates the
     working directory and writes the handoff record there. It does not write
     to `kb/sources/`. Do not compute or extract any of this by hand.

     If the command refuses, nothing was written. Stop before connection
     discovery and report its message, both paired paths, and the canonical
     source. A checksum refusal names the permanent `re-ingest` route with the
     exact ingest path; an ordinary target never authorizes a changed
     observation. A refusal for an unfinished run means an earlier ingest of
     this source stopped midway: report the working directory and let the
     user decide before closing it.

     On success, retain the printed `handoff_record`, `candidate_path`,
     `retained_quotes_path`, and `snapshot_sha256`.

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
   - `output_path`: `kb/sources/<snapshot-slug>.ingest.md`, where the report
     will be published; the worker does not write it
   - `candidate_path`: the file printed in Step 1, which the worker writes
   - `snapshot_sha256`: the checksum printed when Step 1 opened the handoff
   - `retained_quotes_path`: the file printed in Step 1, which holds the exact
     Quotes block the report must contain
   - `handoff_record`: the record printed in Step 1
   - `code_grounding_context`: only when returned by the paper-with-code branch;
     include its secondary-source commit URLs, claim classifications, pinned
     citations, evidence boundaries, and execution status; retain paper version,
     checkout paths, and reviewed commits only in the parent for final reporting
   - `occasion`: the caller's pre-reading question or job, verbatim, or `none`;
     for a re-ingest, the value resolved in Step 1

   Require the instruction, snapshot, and connect report to exist and be
   non-empty. The worker checks the snapshot against `snapshot_sha256` before
   analysis, and Step 5 checks it again. Do not pass the parent conversation,
   any part of an existing ingest other than the retained Quotes file, or the
   parent's interpretations to the worker.

4. **Draft through one primary fresh worker.**
   Start one new sub-agent or worker that receives only the dispatch below.
   Do not use a launch mode that copies the parent's conversation into the
   worker, such as a fork. If the harness has no launch mode without that
   copy, follow the fail-closed rule in the contract. Use the harness worker
   mechanism only.

   Give the worker this dispatch with every placeholder filled in. The warning
   against orchestration skills is load-bearing: skill discovery can re-fire in
   a worker context and would otherwise recurse.

   ```text
   Execute {draft_instruction_path} as the delegated ingest-report drafting
   worker. That instruction and the fixed inputs below are your complete brief.
   Do not invoke or follow any auto-loaded skill, including cp-skill-ingest,
   cp-skill-connect, or cp-skill-snapshot-web. Their orchestration work is
   already complete. Do not spawn another agent.

   Work from the repository root, {repo_root}. Every path below is relative
   to it, and commands run from there.

   Fixed inputs:
   - mode: create
   - snapshot_path: {snapshot_path}
   - connect_report_path: {connect_report_path}
   - output_path: {output_path}
   - candidate_path: {candidate_path}
   - snapshot_sha256: {snapshot_sha256}
   - retained_quotes_path: {retained_quotes_path}
   - handoff_record: {handoff_record}
   - code_grounding_context: {code_grounding_context_or_none}
   - occasion: {occasion_or_none}
   - validation_failures: none
   ```

5. **Verify the drafting handoff.**
   Wait for the primary worker to finish and collect its response. If the
   harness keeps a finished worker open, end it before continuing; a worker
   that ended on its own needs no action. Run the handoff check:

   ```bash
   commonplace-validate <candidate_path> --handoff <handoff_record>
   ```

   It validates the candidate as if it were already at `output_path`, so its
   links and snapshot pairing resolve from there, and checks it against the
   record and the unchanged incumbent: the snapshot still hashes to the pinned
   checksum and the candidate records that checksum; exactly one Quotes block
   equals the incumbent's block, or the canonical empty block, byte for byte;
   `occasion` and code grounding match what the run supplied; and full
   validation passes, with dead links and ingest-contract warnings (Quotes
   position, local-only references, uncopied capture metadata) counted as
   failures. Do not repeat these checks by hand.

   For a code-grounded ingest, also verify the content of `secondary_sources`
   and the `Code Grounding` section against the supplied context; the command
   checks only that both are present. A candidate is clean only when the
   command prints `HANDOFF CLEAN` and, where it applies, this content check
   passes.

   If the primary worker did not produce a clean report, launch at most one new
   fresh replacement worker under the same launch rule. Dispatch the
   same standalone instruction and fixed inputs, including the same
   `candidate_path` and `handoff_record`, but set `mode: repair` and supply
   the command's failure lines, plus any code-grounding content failure, in
   `validation_failures`. Leave the failed primary candidate at
   `candidate_path` for that repair worker. Do not add parent interpretations
   or a rewritten analysis brief. Wait for the replacement, collect its
   response, end it if the harness keeps it open, then repeat the handoff check.
   Do not retain either single-use worker for another task.

6. **Publish or close.**
   - After a clean primary or repair candidate, publish it:

     ```bash
     commonplace-ingest-handoff publish <handoff_record>
     ```

     The command repeats the handoff check, copies the candidate to
     `output_path` only if the incumbent is still the one the handoff opened
     with, and records the run as published. If it refuses, `output_path` is
     unchanged; report its message.
   - After handled final failure, including a worker-launch failure, run
     `commonplace-ingest-handoff close <handoff_record>` and report the
     blocker. The command records the run as closed and keeps the failed
     candidate for inspection. An existing ingest was never changed, so there
     is nothing to restore. Never draft or repair the analysis in the parent context.

7. **Discover connections for the accepted ingest.**
   Run this step only after Step 6 accepts a clean primary or repair candidate,
   including a same-checksum refresh. Invoke `cp-skill-connect` on `output_path`
   and wait for completion. This is a separate pass from snapshot discovery;
   keep its report at
   `kb/reports/cache/connect/sources/<snapshot-slug>.ingest.connect.md`.
   Require a non-empty report whose `source` is `output_path` and run
   `commonplace-validate` on that report; the command takes one path per
   run. Read its `Bidirectional Candidates` and `Reverse-edge Candidates` in
   the report file itself, including an explicit `None` when there are no
   candidates. The connect run's summary does not replace that read. Each proposed inbound link must independently serve a
   reader need under the linking artifact's collection contract; an outbound
   ingest link alone does not justify a return link.

   Do not author these candidates into the ingest or other library artifacts.
   If discovery or report validation fails, keep the accepted ingest, report
   connection discovery as incomplete, and give `cp-skill-connect <output_path>`
   as the retry. Do not repeat drafting for this failure.

8. **Report the result.**
   - On success, tell the user where the ingest report was saved, that drafting
     was delegated, and the report's recommended next action. For a
     paper-with-code ingest, also report the paper version, checkout paths,
     reviewed commits, execution status, and validation result.
   - For an accepted ingest, also give the post-ingest connect report path and
     summarize its inbound-link candidates, or state that none were found.
     Distinguish a validated ingest from incomplete connection discovery when
     Step 7 fails; do not report that links were authored.
   - On handled final failure, report the blocker and, for an existing output,
     that the refresh failed and the ingest is unchanged. Do not present the
     failed candidate as saved output.

## Constraints

- Run `cp-skill-connect` before classification or value extraction.
- Draft through one primary fresh harness worker using the source snapshot and
  generated connect report; on failure, allow at most one fresh replacement.
  Never pass the parent's full orchestration context.
- Do not draft locally when worker delegation is unavailable unless the user
  explicitly authorizes that fallback for the current run.
- The drafting worker writes only the candidate. Outside an explicitly
  authorized local-fallback run, the parent owns no substantive report drafting
  or repair.
- Write `kb/sources/` only through `commonplace-ingest-handoff publish`.
- Accept exactly one URL-backed primary source; reject directory primaries.
- Pair an ingest only with its name-derived snapshot. A checksum verifies that
  named file; it never discovers a substitute.
- Never update an existing ingest's `snapshot_sha256`. Changed source bytes are
  a new observation with a distinct snapshot basename and ingest path.
- The working directory and the publish guard are the only staging. Do not add
  atomic rename, locks, crash recovery, or concurrent-writer coordination. A
  run that stops without `publish` or `close` stays open; the next `prepare`
  for that source refuses until it is closed.
- Do not delete a working directory. It stays after the run as the record of
  its handoff checks; the next `prepare` for the same source replaces it.

# Investigation: harness-orchestrated-review engineering gaps (`kb/log.md` line 22)

Source log item (2026-06-12, FIX category): first harness-orchestrated review run via Claude Code dynamic workflows (selector -> two prepared batches -> one reviewer agent per batch, parallel -> ingest). Four frictions recorded: (1) workflow `args` didn't reach the script, (2) no shell in the script sandbox forces deterministic sweeps into the parent conversation, (3) no per-run token telemetry, (4) the recorded model partition is the orchestrator's unverified assertion. The log also flagged the `structured-output-codec-for-review-protocol.md` proposal's trigger as "arguably met" for the workflow medium.

## What was read

- `kb/reference/adr/030-harness-facing-seams-batch-endpoints-and-runner-adapters.md` — the ADR the log item cites. **Now superseded** by ADR 034, itself superseded by ADR 035 (accepted, 2026-07-01). Both postdate the 2026-06-12 log entry.
- `kb/reference/adr/034-queued-review-jobs-and-execution-provenance.md` (2026-06-30) and `035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md` (2026-07-01, accepted/current).
- `kb/agentic-systems/claude-code-dynamic-workflows.md` — the harness analysis note; last touched 2026-06-03 (`5da75274`, `eb109cce`), i.e. before the friction-generating run and with no update since.
- `kb/reference/proposals/structured-output-codec-for-review-protocol.md` in full, including its adoption criteria.
- `kb/work/monthly-improvement-triage/README.md`'s "Deprioritized" section.
- Current code: `src/commonplace/cli/review/finalize_review_job.py`, `src/commonplace/cli/review/create_review_jobs.py`, `src/commonplace/review/finalization.py`.
- `kb/reference/README-REVIEW-SYSTEM.md` and `kb/reference/review-architecture.md` for current documented behavior.
- `git log --since=2026-06-12` on the finalize/create-jobs code and the two ADRs, confirming the relevant commits (`40c34e5c` job runner, `2925b2f3` job-owned finalization, `85496362` "Validate review runner provenance", `a529ce3e` "Simplify review job finalization surface", `cd7a9ba7` 2026-07-01 "Simplify review finalization") all postdate the log entry.

## Status of each friction

1. **Workflow `args` didn't reach the script.** Still open. This is a Claude Code (harness/product) bug, not Commonplace code — nothing in `src/commonplace/` touches workflow-script argument passing. The workaround (inline the data) already exists and is the only lever available from this side. No related commits found; `claude-code-dynamic-workflows.md` hasn't been updated since 2026-06-03 and doesn't document this bug. Not actionable as a Commonplace design proposal.

2. **No shell in the script sandbox forces deterministic sweeps into the parent conversation.** Still open, but this is an accepted, already-documented harness constraint, not a bug: `claude-code-dynamic-workflows.md`'s "What the runtime withholds" section (point 1, "Guest language, not host language") already names exactly this — no filesystem/shell access, so a deterministic sweep loop needs either an agent spent on enumeration or the parent conversation supplying the work-list via `args`. ADR 030's "harder / accepted costs" also anticipated a version of this ("Commonplace cannot enforce worker-level retries or concurrency; the parent harness owns them"). Nothing to design on Commonplace's side — the constraint lives entirely in the harness.

3. **No per-run token telemetry; ingest accepted none.** **Fixed since the log entry.** ADR 034 (2026-06-30) added a nullable `telemetry_json` column on `review_jobs`; ADR 035 (2026-07-01) and the current `finalize_review_job.py` expose `--telemetry-json` — "Opaque per-harness execution telemetry blob, stored verbatim and never interpreted." `review-architecture.md` documents it ("Missing telemetry is normal. Review identity is `(note_path, gate_path, model_partition)`, not worker-provided execution metadata."). Ingest now accepts telemetry; the remaining limitation (harness reports usage per-workflow, not per-run) is harness-side, not Commonplace's.

4. **Recorded model partition was the orchestrator's unverified assertion.** **Fixed since the log entry.** `finalize_review_job.py --model [--effort]` now validates `build_model_partition(model, effort)` against the job's stored `model_partition` before any state mutation (`finalization.py` lines ~139-144); a mismatch fails finalization rather than silently recording an unverified value. This is exactly the gap the log entry named.

Both fixes shipped through ADR 034/035 and the "Validate review runner provenance" / "Simplify review job finalization surface" / "Simplify review finalization" commits, all dated 2026-06-30 through 2026-07-01 — after the 2026-06-12 log entry and independent of this triage pass.

## The structured-output-codec proposal's deprioritization

Re-checked against `README-REVIEW-SYSTEM.md`'s current documented workflow: it describes one medium-agnostic worker contract — "a worker (typically a sub-agent) reads a job's prompt and writes a single sentinel-delimited `bundle-output.md`" — with no distinction between a live-agent invocation and a dynamic-workflow `agent()` call. The markdown-sentinel codec is the only one the shipped system's docs and code — the "live-agent file-artifact path" — actually exercise; the schema-validated `agent({schema})` call from the log entry was a one-off experimental capability of one harness feature (dynamic workflows), not the path the project's documented review procedure (`run-review-batches.md`) uses.

This confirms, rather than overturns, the triage README's framing: the adoption criteria's literal wording is met by one medium, but that medium isn't the project's actual review-execution focus. Nothing found in this investigation changes that call.

## Verdicts

- **Friction 1 (workflow `args`):** DISMISS-STILL-OPEN-NO-ACTION. Harness bug, not Commonplace's system; existing workaround suffices; no proposal possible since the fix would live in Claude Code itself, not this repo.
- **Friction 2 (no shell forces parent-side sweeps):** DISMISS-STILL-OPEN-NO-ACTION. Already-documented, accepted harness constraint (`claude-code-dynamic-workflows.md`, ADR 030's accepted costs); no Commonplace-side design gap to close.
- **Friction 3 (no token telemetry):** DISMISS — already fixed (ADR 034/035, `--telemetry-json`). No write needed.
- **Friction 4 (unverified model partition):** DISMISS — already fixed (ADR 034/035, `--model`/`--effort` validation in `finalize_review_job.py`). No write needed.
- **Structured-output-codec proposal:** DISMISS-STILL-OPEN-NO-ACTION — the triage README's deprioritization is confirmed correct as written; no factual correction needed in `structured-output-codec-for-review-protocol.md` (its "Current state" section already accurately reflects the current `commonplace-create-review-jobs` CLI and correctly scopes the trigger to output-encoding, which is orthogonal to the provenance fixes in frictions 3-4).

No design proposal, proposal update, or theory note is warranted from this investigation. The log entry's four frictions have already resolved into: two harness-side constraints with no Commonplace-side action available, and two gaps that shipped as part of the review system's own evolution (ADR 034/035) independent of this triage. This item can be closed as fully addressed/dismissed.

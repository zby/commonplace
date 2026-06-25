---
description: "Proposal: add an operator-facing review run status command so agents can inspect review ingestion state without direct SQLite queries"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
status: seedling
---

# Review run status command

The review system should expose a small read-only status command for review runs. The immediate problem is operational: after creating live-agent review runs, an agent sometimes needs to reconcile which runs are still pending, completed, failed, or partly ingested. Today that check falls through to direct SQLite inspection, which is accurate but bypasses the review system's operator API.

## Current state (as of 2026-06-25)

The shipped live-agent path is documented in [review system](../REVIEW-SYSTEM.md):

1. `commonplace-create-review-runs` creates one or more run records and writes prompt, manifest, and bundle output paths.
2. The agent writes each `bundle-output.md`.
3. `commonplace-ingest-bundle-output` parses the bundle output, completes review pairs, writes result artifacts, and appends acceptance events.

The command surface documented in [commands](../commands.md) has selectors for stale review work and warning fixes:

- `commonplace-review-target-selector` answers which note/gate pairs need attention.
- `commonplace-warn-selector` answers which accepted warning findings remain actionable.
- `commonplace-ingest-bundle-output` reports completion for one ingestion call.

What is missing is a read-only command that answers "what happened to these review runs?" after a multi-run operation is interrupted, compacted, or resumed. Operators can inspect `MANIFEST.json` files or query `kb/reports/review-store.sqlite` directly, but neither is the intended stable API for routine agent work.

## Proposed shape

Add a read-only review-run inspection command. Candidate names:

- `commonplace-review-run-status`
- `commonplace-review-runs`

The command should accept one or more run IDs and optionally a note path, recent-run limit, or JSON output flag. The first implementation can stay narrow:

```bash
commonplace-review-run-status 4855 4856 4857 --json
commonplace-review-run-status --note kb/notes/example.md --recent 20 --json
```

For each run it should report:

- run ID, status, runner, model partition, packing mode, note scope, prompt path, bundle output path, manifest path
- pair counts by pair status and decision
- missing or failed pairs, including gate path and result path when available
- whether the bundle output path exists on disk
- whether every completed pair has an acceptance event

The JSON shape should be stable enough for agents to resume interrupted review work without reading schema internals.

## Forces

- Review state intentionally lives in SQLite, so a status command should use the review storage layer rather than scrape markdown reports.
- Operators need a compact recovery view after interrupted multi-run work; the stale-work selector is the wrong abstraction because it answers freshness, not ingestion state.
- Direct SQL is a useful debugging escape hatch, but normal agent procedures should not depend on table names, grouping queries, or schema details.
- A status command should stay read-only. Fixing, ingesting, failing, or acknowledging runs remains the job of existing write commands.

## Non-goals

- Do not add a second freshness selector.
- Do not expose arbitrary SQL or a general database browser.
- Do not make report artifacts canonical. The command should describe canonical DB state and only check artifact paths for operator recovery.

## Open choices

- Command name: singular `review-run-status` is explicit; plural `review-runs` may fit better if it also supports list/recent modes.
- Whether recent-run lookup belongs in this command or a separate listing command.
- Whether a failed run should include debug-log excerpts or only paths to debug artifacts.
- Whether the command should validate manifest consistency or merely report manifest path and DB state.

## Adoption criteria

This proposal is ready to become an implementation task when the review workflow needs another direct DB status query during normal operation. The acceptance test should cover the interrupted-run case: create multiple review runs, ingest only some, then verify the command reports completed, pending, failed, missing-output, and pair-count state without requiring raw SQLite access.

---

Relevant Notes:

- [review system](../REVIEW-SYSTEM.md) — part-of: the runtime workflow and storage model this command would inspect
- [commands](../commands.md) — part-of: the operator command surface that would gain the status command
- [review architecture](../review-architecture.md) — implemented-by: the SQLite storage layer the command should read through

# Implementation Plan

This plan sequences the rewrite in small, reversible slices. The architecture target lives in [target-structure.md](./target-structure.md); this file should not restate it. Use this only when doing implementation work.

## Principles

1. Preserve CLI names, flags, database schema, and review output format.
2. Prefer extraction over behavior change.
3. Keep tests passing after each slice.
4. Stop after each slice if the code is simpler enough; do not create target modules just because the target structure names them.
5. Keep review downstream of core. `commonplace.lib` must not import `commonplace.review`.

## Slice 1: Protocol Ownership

Move prompt and output-format ownership into a review protocol module.

Scope:
- Extract sentinel constants, bundle parsing, gate-sweep parsing, decision extraction, and prompt rendering into a small protocol area.
- Keep link resolution and filesystem reads outside the protocol module; protocol receives already-loaded note, gate, and link-table inputs.
- Keep the parser best-effort; return `unknown` rather than making LLM output strict.
- Keep legacy decision patterns only where they are still needed at runtime.

Acceptance checks:
- Existing bundle and gate-sweep tests pass.
- `run_review_bundle` and `gate_sweep_format` no longer independently own incompatible output-format pieces.
- No prompt/output-format behavior change unless tests explicitly capture it.

Stop point:
- Stop before touching runners or DB finalization.

## Slice 2: Snapshot and Staleness Values

Introduce small value objects for note, gate, and acceptance freshness inputs.

Scope:
- Add `NoteSnapshot`, `GateSnapshot`, and `AcceptanceSnapshot`.
- Add one staleness classifier used by review target selection and warn filtering.
- Keep git loading simple; batching `git cat-file` is optional and should wait for profiling.

Acceptance checks:
- `review_target_selector` and `warn_selector` share freshness semantics.
- Domain code does not import persistence row classes.
- Existing selector tests pass, including model partition and gate-SHA freshness cases.

Stop point:
- Stop before widening scope into full provenance package or loader caching unless duplication remains painful.

## Slice 3: Finalization Out of `review_db.py`

Move business rules out of persistence while preserving the four-table schema.

Scope:
- Keep SQL CRUD thin.
- Move coverage validation, actual-model rekeying, and acceptance-event decisions into a finalization/orchestration function.
- Keep `review_run_gates` as the captured expected-gate contract for ingest/finalization.

Acceptance checks:
- Review rows and acceptance events are committed atomically.
- Parse or coverage failure marks the existing run failed without partial acceptance state.
- Live-agent ingest still finalizes the original run id.
- Existing DB migration and review-run lifecycle tests pass.

Stop point:
- Stop before broad repository-class layering if simple functions are enough.

## Slice 4: Live-Agent Resume Boundary

Make live-agent explicit as a suspended pipeline.

Scope:
- Represent "prompt written, waiting for ingest" with a small prompt artifact or run-id value.
- Make ingest call the same parse/finalize tail used by subprocess execution.
- Do not split runner modules as part of this slice.

Acceptance checks:
- Create-run, prompt-writing, and ingest still use the captured note/gate SHA contract.
- Ingest does not create a second review run.
- Subprocess execution still returns the same output/telemetry behavior as before.

Stop point:
- Stop before changing subprocess telemetry extraction.

## Slice 5: Runner Containment

Only do this if runner code is still blocking tests or changes.

Scope:
- Define a narrow `RunnerResult` shape: output text, telemetry, actual model id.
- Keep Claude/Codex subprocess details in the existing runner module unless there is concrete pressure to split.
- Do not introduce per-runner packages just for symmetry.

Acceptance checks:
- Orchestration depends on `RunnerResult`, not session-log internals.
- Runner telemetry tests still pass.
- No new runner abstraction beyond what current call sites need.

Stop point:
- Stop here unless a third runner or repeated telemetry bugs make a split worthwhile.

## Slice 6: Relocation Integration Cleanup

Adapt review-owned relocation behavior to the new persistence shape.

Scope:
- Keep `ReviewRelocationHook` downstream of core relocation.
- Move DB note-path rekeying behind the review persistence boundary if that boundary now exists.
- Keep review export metadata handling quarantined as legacy export support.

Acceptance checks:
- Core relocation still imports no review modules.
- Review export directories move with notes.
- Review DB note paths rekey correctly.
- Hook preflight failures still abort before core file mutation.

## Do Not Do Yet

- Do not force LLM output into JSON.
- Do not change the database schema.
- Do not rename public CLI commands or flags.
- Do not rewrite all review modules in one pass.
- Do not split runners into `subprocess_claude.py` / `subprocess_codex.py` unless a concrete maintenance problem justifies it.

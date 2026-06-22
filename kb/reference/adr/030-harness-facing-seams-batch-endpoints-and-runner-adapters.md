---
description: "Batch prepare/ingest CLIs expose review pair execution to external orchestrators, and runner adapters put subprocess harness CLIs behind one registry-backed interface"
type: ../types/adr.md
tags: []
status: accepted
---

# 030-Harness-facing seams: batch prepare/ingest endpoints and runner adapters

**Status:** accepted
**Date:** 2026-06-12

## Context

Review execution runs through interchangeable media: a subprocess runner, a live agent following a rendered prompt, and a Python thread pool over the subprocess path. Harness-orchestrated execution (e.g. Claude Code dynamic workflows, where a script fans batches out to sub-agents and Python is reduced to deterministic endpoints) is a fourth medium the system should admit without restructuring. Two obstacles stood in the way after [ADR 029](./029-review-execution-unified-on-note-gate-pairs.md):

1. The live-agent surface was single-note (`create-review-run`) and single-run all-or-nothing (`ingest-bundle-output`), while the batch machinery (run preparation, pair prompt rendering, salvage finalization) existed only as library internals with no CLI.
2. `review_runners.py` was a 774-line module in which two vendor CLIs interleaved — command construction, stream decoding, session-log telemetry scraping — dispatched by `if runner == ...`, with the runner names also hardcoded in three argparse `choices` lists. Adding a harness CLI meant editing four files.

## Decision

1. **Batch-granular endpoints.** `commonplace.review.batch` plus two CLIs expose the executor's batch machinery to external executors:
   - `commonplace-prepare-review-batch <note-path>::<gate-id>... --runner <label> --model <id>` — creates one review run for a note-packed or gate-packed pair set (inapplicable gates are skipped and reported; missing notes/gates and dirty gates are fatal), renders the canonical pair prompt in file mode, and returns `review_run_id`, pair metadata, skipped pairs, `prompt_path`, `bundle_output_path`, and `manifest_path` as JSON. Batch artifacts live under `kb/reports/bundle-reviews/review-run-{review_run_id}/`.
   - `commonplace-ingest-batch-output --review-run-id <id> --input-file <path>` — parses the pair output and finalizes with the executor's salvage policy: completed pairs are retained, missing pairs are marked `missing`, and structural parse errors fail the run. Returns completed/failed pair status as JSON; exit 1 if the run failed.
   The salvage finalization is shared code (`executor.finalize_runs_from_parsed`), so subprocess and external execution cannot drift. The single-note live-agent flow (`create-review-run`/`ingest-bundle-output`) remains all-or-nothing per its prior decision, but uses the same pair parser and artifact manifest contract.
2. **Runner adapters.** `commonplace.review.runners` replaces `review_runners.py`: a `RunnerAdapter` interface (`base.py` — build_command, optional stdout-stream decoding, best-effort telemetry collection), one module per vendor (`claude_code.py`, `codex.py`), and a registry from which `run_prompt` dispatches and the CLIs derive `--runner` choices. Adapters are instantiated per invocation so streaming state feeds telemetry collection. Session-log scraping is explicitly per-adapter and best-effort: returning no telemetry never fails a run. The reviewer-facing system prompt moves to `protocol/prompt.py`.

Adding a harness CLI is now one adapter module plus one registry entry; adding a harness *orchestrator* needs no Python change at all — it consumes the selector, prepare, and ingest endpoints.

## Consequences

Easier:
- Harness-orchestrated review (workflow scripts, parallel sub-agent fan-out) composes from existing endpoints: selector → prepare-batch per group → agent per batch → ingest-batch. Parallelism, budgets, and retries belong to the orchestrator.
- A new subprocess harness is one self-contained module; vendor log-format breakage is isolated to its adapter.
- The `--runner` choice lists can no longer drift from what the code supports.

Harder / accepted costs:
- Batch preparation accepts only pair sets with one shared axis (`note` or `gate`) until a mixed-packing caller needs a stronger manifest and naming contract.
- The live-agent path still treats one note-packed run as all-or-nothing; pair-level salvage is reserved for the batch ingest path.
- `review_sweep`'s thread-pool fan-out remains, now redundant in principle with orchestrator-owned parallelism; it is kept as the working subprocess sweep and is expected to shrink rather than grow.

---

Relevant Notes:

- [review architecture](../review-architecture.md) — part-of: the subsystem these seams expose
- [029-review execution unified on (note, gate) pairs](./029-review-execution-unified-on-note-gate-pairs.md) — see-also: the pair protocol and salvage policy these endpoints surface to external executors
- [Claude Code dynamic workflows](../../agentic-systems/claude-code-dynamic-workflows.md) — derived-from: the harness orchestration model (script coordinates, agents execute, deterministic endpoints at the edges) these seams are shaped for

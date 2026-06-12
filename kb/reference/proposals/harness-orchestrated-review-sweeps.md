---
description: "Proposal: run review sweeps through a harness's sub-agent orchestration feature (workflow scripts) instead of the Python thread pool — wiring validated by one Claude Code experiment, adoption deferred until comparable orchestration surfaces exist in more than one harness"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
status: seedling
---

# Harness-orchestrated review sweeps

Review sweeps need fan-out: many (note, gate) pairs, packed into batches, executed in parallel, with per-batch failure isolation. Today the package supplies that fan-out itself (`review_sweep`'s thread pool over subprocess runners). Harnesses are beginning to ship sub-agent orchestration as a first-class feature — Claude Code's dynamic workflows expose `agent()`/`parallel()` under a model-authored script — which does the same job with native progress display, concurrency caps, isolation, and budgets, and without the fragile half of the subprocess path (session-log scraping, stream decoding, usage-exhaustion string matching). This proposal holds the sweep-orchestration design for that medium. It is deliberately unadopted: the feature is single-vendor, and committing the framework's operating procedure to one harness's proprietary surface contradicts the portability goal that motivates it.

## Current state (as of 2026-06-12)

- The execution seams exist and are validated. [ADR 030](../adr/030-harness-facing-seams-batch-endpoints-and-runner-adapters.md) shipped `commonplace-prepare-review-batch` and `commonplace-ingest-batch-output`; one experiment ran a real slice end-to-end (selector → two prepared batches → a 12-line workflow script with one reviewer agent per batch in parallel → ingest; 4 pairs recorded, zero Python changes; observations in `kb/log.md`, 2026-06-12).
- The orchestration feature is Claude Code-only ([dynamic workflows](../../agentic-systems/claude-code-dynamic-workflows.md)). No comparable scriptable sub-agent surface is known in the other harness this project runs (codex CLI).
- The workflow script sandbox has no shell or filesystem, so it cannot invoke `commonplace-*` commands; only the parent conversation or sub-agents can.
- Frictions observed in the experiment: workflow `args` input did not reach the script (data had to be inlined); no token telemetry lands on the review runs (the harness reports usage per workflow, ingest accepts none); the recorded model partition is the orchestrator's unverified assertion, where the subprocess path rekeys from scraped telemetry.

## The design

Five roles, with the harness owning exactly one:

1. **Work-list** — `commonplace-review-target-selector --json` emits stale pairs (deterministic, Python).
2. **Packing** — group pairs into batches (share-note or share-gate); trivial in any language, owned by the orchestrator.
3. **Prepare** — `commonplace-prepare-review-batch` per batch: run creation, provenance, canonical prompt (deterministic, Python).
4. **Fan-out** — the harness feature: one reviewer agent per batch, in parallel. Reviewers are hermetic: they read the batch's `prompt.md`, write its `bundle-output.md`, and are forbidden from running `commonplace-*` commands — judgment only, no bookkeeping.
5. **Ingest** — `commonplace-ingest-batch-output` per batch: parse, salvage, finalize (deterministic, Python).

The interface between the worlds is files and JSON, never calls: prepare's JSON output feeds the script as data; agents and Python meet at the artifact directory; ingest reads files. The Python endpoints are the fixed point across execution media — a review recorded this way is indistinguishable in the ledger from one recorded by the subprocess runner.

## Free choices

- **Wiring of the deterministic steps.** Parent-interleaved (the conversation runs select/prepare/ingest between workflows — the validated shape) versus coordinator-agent (a sub-agent runs the commands via shell, enabling a self-contained loop-until-no-stale-pairs script). The first keeps agents judgment-only; the second buys script-driven multi-round control flow at the cost of spending LLM calls on deterministic work and blurring the hermetic-reviewer boundary.
- **Promotion form.** An instruction in `kb/instructions/` describing the procedure (harness-neutral prose, the orchestrator re-derives the script each time) versus a saved workflow script (executable, but vendor-locked and dependent on the `args` mechanism working). The instruction form survives harness churn; the script form is faster to invoke.
- **Execution metadata on ingest.** Extend `commonplace-ingest-batch-output` with optional model-id and usage arguments so external executors can attribute what they know, versus leaving external runs telemetry-less. Interacts with the packing-provenance follow-up in [ADR 029](../adr/029-review-execution-unified-on-note-gate-pairs.md).
- **Output codec.** Sentinel files (today) versus schema-validated agent returns — the trigger question lives in [structured-output codec for the review protocol](./structured-output-codec-for-review-protocol.md); this proposal's medium is the first where that trigger is arguably met.

## Adoption criteria

Adopt as framework methodology when a second harness ships a comparable scriptable sub-agent orchestration surface, so the procedure can be written against the *pattern* (returning bounded calls under host-language control flow) rather than one vendor's API. Repo-local use before then is cheap and harmless — the experiment's recipe works today — but it should stay an operator convenience, not a documented operating procedure.

## Risks

- **Vendor coupling by stealth.** If the convenient path is workflow-only, sweep practice drifts to one harness even without a documented commitment; the subprocess path must remain the reference implementation until the adoption trigger fires.
- **Attribution decay.** Telemetry-less external runs weaken per-gate cost statistics; trusted-assertion model partitions weaken partition semantics. Both are acceptable for occasional use and corrosive at scale — the execution-metadata free choice should be resolved before this becomes the default sweep path.
- **Orchestration recipes are unversioned.** A thread pool in the package is tested code; a workflow script re-derived per run is not. Parse failures still land safely (salvage policy), but recipe drift is invisible until a run misbehaves.

---

Relevant Notes:

- [Claude Code dynamic workflows](../../agentic-systems/claude-code-dynamic-workflows.md) — derived-from: the single shipped instance of the orchestration surface this design targets
- [030-harness-facing seams: batch endpoints and runner adapters](../adr/030-harness-facing-seams-batch-endpoints-and-runner-adapters.md) — see-also: the shipped endpoints this design composes; the experiment validating them
- [structured-output codec for the review protocol](./structured-output-codec-for-review-protocol.md) — see-also: the output-encoding decision this medium puts on the table

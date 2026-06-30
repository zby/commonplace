---
description: "Proposal: run review sweeps through harness sub-agent orchestration once comparable surfaces exist in more than one harness"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
status: seedling
---

# Harness-orchestrated review sweeps

Review sweeps need fan-out: many (note, gate) pairs, packed into batches, executed in parallel, with per-batch failure isolation. Commonplace now leaves fan-out to the parent agent or harness: the package creates queued jobs, records claims, and finalizes worker output, while the parent owns model calls, concurrency caps, budgets, and retries. Harnesses are beginning to ship sub-agent orchestration as a first-class feature — Claude Code's dynamic workflows expose `agent()`/`parallel()` under a model-authored script — which can perform that parent role with native progress display and isolation. This proposal holds the sweep-orchestration design for that medium. It is deliberately unadopted as a framework-specific script: the feature is single-vendor, and committing the framework's operating procedure to one harness's proprietary surface contradicts the portability goal that motivates it.

## Current state (as of 2026-06-30)

- The execution seams exist and are validated. [ADR 034](../adr/034-queued-review-jobs-and-execution-provenance.md) defines queued jobs: selector JSON -> `commonplace-create-review-jobs --input ... --grouping {note,gate}` -> `commonplace-claim-review-job` -> worker output -> `commonplace-finalize-review-job`. One experiment ran a real slice end-to-end on an older seam (selector -> two prepared batches -> a 12-line workflow script with one reviewer agent per batch in parallel -> ingest; 4 pairs recorded, zero Python changes; observations in `kb/log.md`, 2026-06-12). The experiment remains evidence for the orchestration pattern, not for current command names.
- The orchestration feature is Claude Code-only ([dynamic workflows](../../agentic-systems/claude-code-dynamic-workflows.md)). No comparable scriptable sub-agent surface is known in the other harness this project runs (codex CLI).
- The workflow script sandbox has no shell or filesystem, so it cannot invoke `commonplace-*` commands; only the parent conversation or sub-agents can.
- Frictions observed in the experiment: workflow `args` input did not reach the script (data had to be inlined); no token telemetry landed on the review records (the harness reports usage per workflow); the recorded model partition was the orchestrator's assertion. ADR 034 now treats telemetry as optional execution evidence, not review identity.

## The design

Five roles, with the harness owning exactly one:

1. **Work-list** — `commonplace-review-target-selector --json` emits stale pairs (deterministic, Python).
2. **Packing** — group pairs into batches (share-note or share-gate); trivial in any language, owned by the orchestrator.
3. **Prepare** — `commonplace-create-review-jobs --input ... --grouping {note,gate}` per selector payload or batch group: job creation, canonical prompt, and pending pair rows (deterministic, Python).
4. **Fan-out** — the harness feature: one reviewer agent per batch, in parallel. Reviewers are hermetic: they read the batch's `prompt.md`, write its `bundle-output.md`, and are forbidden from running `commonplace-*` commands — judgment only, no bookkeeping.
5. **Finalize** — `commonplace-finalize-review-job --review-job-id ...` per job: parse, salvage, persist pair results, append acceptance events, and refresh inspection artifacts (deterministic, Python).

The interface between the worlds is files and JSON, never calls: creation/listing JSON feeds the script as data; agents and Python meet at the artifact directory; finalization reads job-owned files. The Python endpoints are the fixed point across execution media — a review recorded this way is indistinguishable in the ledger from one recorded by the subprocess runner.

## Free choices

- **Wiring of the deterministic steps.** Parent-interleaved (the conversation runs select/prepare/ingest between workflows — the validated shape) versus coordinator-agent (a sub-agent runs the commands via shell, enabling a self-contained loop-until-no-stale-pairs script). The first keeps agents judgment-only; the second buys script-driven multi-round control flow at the cost of spending LLM calls on deterministic work and blurring the hermetic-reviewer boundary.
- **Promotion form.** An instruction in `kb/instructions/` describing the procedure (harness-neutral prose, the orchestrator re-derives the script each time) versus a saved workflow script (executable, but vendor-locked and dependent on the `args` mechanism working). The instruction form survives harness churn; the script form is faster to invoke.
- **Execution metadata at claim/finalize.** `commonplace-claim-review-job` records known runner/model/effort provenance before dispatch; finalization can later attach optional telemetry when a harness exposes it. The open choice is how much parent-orchestrator evidence to collect and how to present telemetry gaps.
- **Output codec.** Sentinel files (today) versus schema-validated agent returns — the trigger question lives in [structured-output codec for the review protocol](./structured-output-codec-for-review-protocol.md); this proposal's medium is the first where that trigger is arguably met.

## Adoption criteria

Adopt as framework methodology when a second harness ships a comparable scriptable sub-agent orchestration surface, so the procedure can be written against the *pattern* (returning bounded calls under host-language control flow) rather than one vendor's API. Repo-local use before then is cheap and harmless — the experiment's recipe works today — but it should stay an operator convenience, not a documented operating procedure.

## Risks

- **Vendor coupling by stealth.** If the convenient path is workflow-only, sweep practice drifts to one harness even without a documented commitment; the parent-dispatched CLI workflow must remain the reference implementation until the adoption trigger fires.
- **Attribution decay.** Telemetry-less external runs weaken per-gate cost statistics; trusted-assertion model partitions weaken partition semantics. Both are acceptable for occasional use and corrosive at scale — the execution-metadata free choice should be resolved before this becomes the default sweep path.
- **Orchestration recipes are unversioned.** A thread pool in the package is tested code; a workflow script re-derived per run is not. Parse failures still land safely (salvage policy), but recipe drift is invisible until a run misbehaves.

---

Relevant Notes:

- [Claude Code dynamic workflows](../../agentic-systems/claude-code-dynamic-workflows.md) — derived-from: the single shipped instance of the orchestration surface this design targets
- [030-harness-facing seams: batch endpoints and runner adapters](../adr/030-harness-facing-seams-batch-endpoints-and-runner-adapters.md) — see-also: the shipped endpoints this design composes; the experiment validating them
- [structured-output codec for the review protocol](./structured-output-codec-for-review-protocol.md) — see-also: the output-encoding decision this medium puts on the table

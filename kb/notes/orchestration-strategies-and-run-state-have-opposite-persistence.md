---
description: Inside a host-language scheduler, run-state K is task-specific so it has near-zero cross-task reuse value and should stay ephemeral, while select-strategies recur and are expensive to rediscover so they are the high-value promotion target — RLM discards both, losing the valuable half
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model, learning-theory, tool-loop, artifact-analysis]
status: seedling
---

# Orchestration strategies and run-state have opposite persistence economics

A scheduler over bounded LLM calls has two symbolic parts: the [accumulated state `K`](./bounded-context-orchestration-model.md) and the `select` logic that decides what the next call sees and does. When the [host language plays both roles](./the-practical-scheduler-is-the-host-language.md), it is tempting to treat them as one substrate with one lifecycle. It is the wrong instinct. Measured by **cross-task reuse value** — how much a later, different task gains from keeping the part around — `K` and `select` sit at opposite poles, so a system that promotes them symmetrically gets one of them wrong.

The axis here is *cross-task* persistence: whether a part is worth lifting into a durable library so later tasks reuse it. That is distinct from *within-run* survival — whether `K` outlives its process or fits in memory — which the [companion note](./the-practical-scheduler-is-the-host-language.md) treats separately and which can force `K` to be reified even when it has no cross-task value.

- **Run-state `K`** is the answer to *this* task — source artifacts plus the relevance labels, summaries, and partial syntheses prior calls produced for it. Some of that is expensive to recompute, but recomputing it does not help the next task, because the next task asks something else. Its cross-task reuse value is near zero, so it should stay **ephemeral across tasks**: it may be checkpointed within a run for durability or capacity, but it is not promoted into the library.
- **`select`-strategies** — the decomposition, partitioning, and aggregation patterns the scheduler applies — recur across tasks and are **expensive to rediscover**. Each is a small piece of control logic that took search to find, and the same shape pays off on the next task. These are the **high-value promotion target**, worth lifting into durable, tested library code.

[RLM](./rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) discards *both* halves after every query. Discarding `K` is correct: it is query-specific, so even when rebuilding it is costly, the cost buys nothing for the next, different query. Discarding the `select`-strategy with it is the loss. A decomposition the model searched for and got right is gone before the next query arrives, so the same search is paid again. The fix is not the opposite symmetry — reify everything, the durable-execution pole. It is to **split the cross-task lifecycles: let `K` stay ephemeral, promote the recurring `select`-fragments.**

## The control structure: a test-gated orchestrator cache

Splitting the lifecycles turns the scheduler into an **orchestrator cache with a test-gated write-back**, run reuse-first rather than generate-first:

1. On a task, search the library for a fitting tested orchestrator.
2. **Hit** → reuse the verified code: cheap, deterministic, no re-derivation.
3. **Miss** → generate the orchestration fresh (RLM-style); if it clears the promotion gate below and passes tests, write it back to the library.

Two distinct gates run here, and conflating them is the trap. *Fit* (step 1) is a selection judgment — does this stored strategy apply to the task at hand — and it does not get easier just because a fragment is tested. *Trust* (step 2) is what the *tested* qualifier buys: a cache of merely retained code is memoization, whereas a cache of *verified* code is what lets a later run rely on a fitting fragment without re-deriving and re-checking it. Tests certify that the fragment still does what it did, not that it suits a given task; selecting a fitting one remains a separate cost (see the retrieval problem below). Promotion is therefore movement up the [verifiability gradient](./verifiability-gradient.md) — from loose, model-authored REPL code toward deterministic library functions. That is the general shape of [codification](./definitions/codification.md), and the loop it closes is [deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) through the repo.

## What this costs, and why promotion must be selective

The asymmetry does not make accumulation free; it tells you *which* half is worth paying for. Promoting `select`-fragments takes back, for those fragments, the governance burden that [discarding everything avoids](./ephemeral-computation-prevents-accumulation.md): provenance, approval, staleness, retirement, dependency drift, and a **retrieval problem** — once the library is large, finding the right orchestrator becomes its own selection cost, and naming noise grows. Keeping `K` ephemeral keeps the corresponding state-management burden off the table, so the bill is paid only on the reusable half, not on everything.

So the promotion gate cannot be "anything that worked." Passing tests is necessary — it is the trust gate above — but not sufficient: the gate must also admit only patterns that are stable, frequently recurring, and expensive to rederive, because [codifying what the model will soon do better unaided](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) is a net-negative trade. The persistence asymmetry justifies *having* a promotion path; the bitter-lesson boundary governs *what crosses it*. Run-state never crosses — not because it is cheap, but because it never recurs; only the costly, recurring control strategies do.

## Where it lands

This is a third mode on the authorship axis. Two poles already exist: the model re-authoring `select` from scratch every run (RLM), and a programmer authoring it once up front (a hand-written host-language scheduler). The third is distinct from both because authorship is *split across time* — the model authors a fragment during a run, and a promotion step turns the recurring, tested ones into library code that later runs reuse. It is neither purely per-run nor purely up-front: the corpus of `select`-functions grows from execution. So it is the [host-language scheduler](./the-practical-scheduler-is-the-host-language.md) made **self-populating** — built bottom-up from exploration rather than top-down by design — and the concrete form of the combined system the [persistence-boundary comparison](./rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md) sketches.

A shipped instance partially confirms the prediction. Claude Code's [dynamic workflows](../sources/claude-code-dynamic-workflows-docs.md) have the model author an ephemeral orchestrator script per task and let a completed run be saved as a reusable `/<name>` command — the promotion path, in the wild. But the shipped form is **coarse and manual**: it promotes the *whole* script by hand, with no test gate and no fragment-level split, so the *fit* and *trust* gates above collapse into a single human decision. The promotion *pole* therefore exists while the machinery this note specifies — the two gates and `select`-fragment granularity — remains unbuilt. The direction is corroborated; the mechanism is not yet.

---

Relevant Notes:

- [the practical scheduler is the host language](./the-practical-scheduler-is-the-host-language.md) — extends: that note keeps `select`/`K` un-reified; this one splits their lifecycles, promoting recurring `select`-fragments while `K` stays ephemeral
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — grounds: the `select`/`K` decomposition whose two halves this note assigns opposite persistence economics
- [RLM has the model write ephemeral orchestrators over sub-agents](./rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) — contrasts: the system that discards both halves, losing the valuable `select`-strategies along with the task-specific state
- [ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — mechanism: the accumulation cost RLM avoids and that selective promotion deliberately takes back on the promoted half
- [deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — mechanism: the repo-mediated learning loop that test-gated promotion closes
- [codification](./definitions/codification.md) — mechanism: promoting a verified `select`-fragment to library code is codification of a control strategy
- [the verifiability gradient](./verifiability-gradient.md) — mechanism: the loose→deterministic movement the "tested" promotion gate enforces
- [codification and relaxing navigate the bitter-lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — caveat: governs which strategies are worth promoting versus left for the model to rederive
- [RLM, Tendril, and llm-do place symbolic work at different persistence boundaries](./rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md) — context: the combined exploration-plus-promotion system this control structure concretises
- [Claude Code dynamic workflows](../sources/claude-code-dynamic-workflows-docs.md) — evidence: shipped instance of the predicted promotion path — model-authored ephemeral orchestrator, saveable as a `/command` — but coarse and manual, with no test gate or fragment-level split ([practitioner report](../sources/a-harness-for-every-task-dynamic-workflows.md))

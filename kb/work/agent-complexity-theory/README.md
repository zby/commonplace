# Agent complexity theory workshop

Working out formal consequences of the [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) and its [universality lemma](../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md). The model is a deliberately simple normal form — a symbolic scheduler over bounded LLM calls — and the lemma means results proved on it transfer to all clean symbolic programs with LLM calls.

The goal is theorem sketches and proof outlines suitable for academic collaboration, not KB design notes. Artifacts here are consumed when they mature into a paper or get pitched to collaborators.

## Candidate result families

1. **Semantic retrieval lower bounds** — orchestration cannot replace semantic inspection without a pre-built index
2. **No universal distillation** — no bounded summary preserves all task-relevant structure for a rich query family
3. **Interaction-width lower bounds** — tasks with dense cross-item dependencies force wide prompts or repeated re-opening
4. **Adaptivity / round lower bounds** — step-dependent discovery and pointer-chasing structures require sequential depth regardless of parallelism
5. **Calls-width-compression tradeoff frontiers** — fewer calls require wider prompts or more aggressive compression
6. **Verification / reliability lower bounds** — long noisy call chains require explicit verifier stages

## Proof template

1. Fix a task family
2. State what symbolic code gets for free vs what requires a bounded call
3. Define per-call bound M and output bandwidth
4. Use adversary or fooling-set argument to maintain indistinguishable worlds
5. Show insufficient calls/rounds/summary-space leaves worlds unseparated
6. Conclude failure in the simple model
7. Lift to all clean bounded-call programs via the universality lemma

## Current sketches

- [Exact retrieval over semantically opaque items requires linear inspection](./exact-retrieval-over-semantically-opaque-items-requires-linear-inspection.md)
- [No universal distillation preserves all task-relevant structure](./no-universal-distillation-preserves-all-task-relevant-structure.md)
- [Adaptive dependencies force width, reopening, or sequential rounds](./adaptive-dependencies-force-width-reopening-or-sequential-rounds.md)
- [Few calls require width and long chains require verification](./few-calls-require-width-and-long-chains-require-verification.md)

## Sketch abstracts

### Interaction / adaptivity lower bounds

Target statement shape: if solving a task requires combining information distributed across many items with important cross-item dependencies, or if the identity of the next item to inspect depends on semantic content discovered in the current step, then bounded-call orchestration must pay somewhere: either wider per-call context, repeated reopening of previously seen sources, or more sequential rounds. Parallel width alone does not remove this cost because the dependency graph is not known in advance.

Practical consequence: some workflows are inherently serial. When the task has real step-dependent discovery, "better planning" cannot collapse it into a shallow one-shot pipeline; the scheduler must budget for iterative loading and intermediate state updates.

### Tradeoff and reliability theorems

Target statement shape: reducing call count pushes burden onto prompt width or onto more lossy intermediate summaries, while increasing chain depth compounds error and omission risk. So decomposition should be analyzable as an explicit cost/reliability frontier rather than a vague engineering heuristic.

Practical consequence: there is no free decomposition. Short pipelines need broad context windows or stronger compression artifacts; long pipelines need verification stages, redundancy, or local re-checks. In practice this means planner designs should expose the cost/reliability trade explicitly and insert verifier passes where the chain would otherwise accumulate unbounded drift.

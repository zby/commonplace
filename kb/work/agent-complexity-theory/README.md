# Agent complexity theory workshop

Working out formal consequences of the [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) and its [universality lemma](../../notes/any-symbolic-program-with-bounded-calls-is-a-select-call-program.md). The model is a deliberately simple normal form — a symbolic scheduler over bounded LLM calls — and the lemma means results proved on it transfer to all clean bounded-call symbolic programs.

The goal is theorem sketches and proof outlines suitable for academic collaboration, not KB design notes. Artifacts here are consumed when they mature into a paper or get pitched to collaborators.

## Candidate result families

1. **Semantic retrieval lower bounds** — orchestration cannot replace semantic inspection without a pre-built index
2. **No universal distillation** — no bounded summary preserves all task-relevant structure for a rich query family
3. **Interaction-width lower bounds** — tasks with dense cross-item dependencies force wide prompts or repeated re-opening
4. **Adaptivity / round lower bounds** — pointer-chasing task structures require sequential depth regardless of parallelism
5. **Calls–width–compression tradeoff frontiers** — decomposition heuristics as costed theorems
6. **Verification lower bounds** — long noisy call chains require explicit verifier stages

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

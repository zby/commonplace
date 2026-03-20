---
description: Some semantic subgoals exceed one context window, so they must be partitioned into smaller semantic judgments with symbolic collection, filtering, and staged summarization between them
type: note
traits: []
tags: [computational-model, context-engineering, tool-loop]
status: seedling
---

# Semantic sub-goals that exceed one context window become scheduling problems

When the material a sub-goal must reason over — files, candidates, examples, or generated comparison cases — exceeds what one **bounded call** can hold, the sub-goal becomes a scheduling problem. The parent task is still semantic, but executing it requires a **symbolic loop**: partition the working set, run smaller semantic judgments, aggregate results in code, then resume the parent.

Collection work is the standard case. An agent decides it needs to analyze a large set before continuing. Relevance filtering, extraction, ranking, and synthesis all require model judgment, but the set does not fit in one prompt. So the system partitions, judges pieces, and collects results deterministically. If even the collected results are too large to synthesize in one call, aggregation itself becomes another decomposed sub-goal — the pattern recurses.

The same structure appears when the relevant cases are not all given in advance. Suppose the agent needs to find contradictions across a large corpus. Even the list of candidate note pairs may not fit in one prompt, so the system cannot start from a complete in-context enumeration of cases. It must generate, prune, and aggregate candidate cases symbolically, then spend bounded calls on the semantic judgments that survive.

These decompositions typically arise *mid-task* — the agent is already in its tool loop when it discovers the set is too large. A framework-owned tool loop becomes awkward here: it assumes the model decides what comes next at each step, but inside this sub-goal the control flow is largely deterministic. Asking the model to simulate that control wastes context; hiding it inside a tool turns the tool into a [hidden scheduler](./stateful-tools-recover-control-by-becoming-hidden-schedulers.md); bypassing the framework reveals that the lower-level primitive was needed all along.

The canonical response is a runtime component that can spawn another tool loop — a sub-agent — for the decomposed sub-goal. That makes the program recursive in the same way the problem is: each level gets a goal, keeps the deterministic parts in code, and delegates the remaining semantic work to the LLM.

---

Relevant Notes:

- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: this note is a direct instance of symbolic scheduling — code deciding what happens next — over bounded semantic calls under a context limit
- [subtasks that need different tools force loop exposure in agent frameworks](./subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md) — related consequence: some fresh calls are needed because child tasks need different tool surfaces
- [stateful tools recover control by becoming hidden schedulers](./stateful-tools-recover-control-by-becoming-hidden-schedulers.md) — counterposition: grants the strongest hidden-runtime recovery before locating this remaining problem
- [codified scheduling patterns can turn tools into hidden schedulers](./codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md) — parallel case: scheduling forced by codified experience rather than structural overflow; same architectural consequence, different cause

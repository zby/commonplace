=== SEMANTIC REVIEW: semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems.md ===

Claims identified: 9

1. [P1, title/opening] When the material a sub-goal must reason over exceeds what one bounded call can hold, the sub-goal becomes a scheduling problem.
2. [P1] Executing it requires a symbolic loop: partition the working set, run smaller semantic judgments, aggregate results in code, then resume the parent.
3. [P2] Collection work is the standard case of this pattern.
4. [P2] If even the collected results are too large to synthesize in one call, aggregation itself becomes another decomposed sub-goal -- the pattern recurses.
5. [P3] The same structure appears when relevant cases are not all given in advance (contradiction-finding across a large corpus).
6. [P4] These decompositions typically arise mid-task.
7. [P4] A framework-owned tool loop becomes awkward here because inside this sub-goal the control flow is largely deterministic.
8. [P4] Hiding it inside a tool turns the tool into a hidden scheduler.
9. [P5] The canonical response is a runtime component that can spawn another tool loop -- a sub-agent -- for the decomposed sub-goal.

---

WARN:
- [Completeness] The note claims "collection work is the standard case" (P2) but only develops two instances: filtering/ranking a pre-existing large set (P2) and generating candidate pairs from a corpus (P3). A third common case -- iterative refinement where the *output* of one bounded call feeds back as input that itself exceeds the window (e.g., multi-draft revision with accumulated feedback, or progressive enrichment of a knowledge graph) -- is neither clearly collection work nor candidate generation. The note's framing implies the space is covered by "given in advance" vs. "not given in advance," but iterative expansion of the working set from the agent's own outputs sits awkwardly between these two.

- [Completeness] The note asserts that the canonical response is a sub-agent (P5), presenting it as the single architectural answer. However, an alternative response is *not* to spawn a sub-agent but to have the outer scheduler itself run the decomposed loop directly in application code without delegating to a child agent. The bounded-context orchestration model note describes exactly this: the symbolic scheduler loops over filter sub-goals itself (the note-selection example, lines 81-88). The sub-agent framing implies recursive agent spawning, but flat scheduler-driven iteration over bounded calls is arguably more canonical in practice. The note could be read as equating these two, but the word "spawn" and the phrase "makes the program recursive" suggest genuine hierarchical delegation rather than a flat loop.

INFO:
- [Completeness] The note identifies two triggers for this pattern: (a) set too large for one prompt and (b) candidate space not enumerable in advance. A boundary case worth noting: what about sub-goals where the material *does* fit in one window but the reasoning itself is too complex -- where the bottleneck is cognitive complexity rather than volume? The note's framing ("material a sub-goal must reason over... exceeds what one bounded call can hold") could be read to include complexity, since the bounded-context orchestration model defines effective context as task-relative, but the examples and language all emphasize volume/set size. If complexity-driven decomposition is intended to be in scope, the note is silent on it; if out of scope, the boundary is not drawn.

- [Grounding] The note links to stateful-tools-recover-control-by-becoming-hidden-schedulers.md with the phrase "hiding it inside a tool turns the tool into a hidden scheduler." The link relationship annotation says "counterposition: grants the strongest hidden-runtime recovery before locating this remaining problem." The linked note does say that hidden schedulers can "recover substantial control" and that context-window overflow is one of the limits. However, the linked note frames the overflow case as a *consequence* ("where a hidden scheduler starts to buckle"), not as a counterposition. The "counterposition" label suggests the linked note argues against this note's claim, but it actually supports it by conceding limits. This is a labeling ambiguity rather than a factual error.

- [Completeness] The simplest possible instance of the concept: a sub-goal that requires reasoning over, say, 2 context windows worth of material, where a single partition-judge-aggregate cycle suffices. The note handles this implicitly (the non-recursive base case of P2), but the recursive case gets more development than the base case. The simplest instance is well-covered.

PASS:
- [Grounding] The link to bounded-context-orchestration-model.md is accurate. The note claims to be "a direct instance of symbolic scheduling -- code deciding what happens next -- over bounded semantic calls under a context limit." The orchestration model note explicitly describes this pattern: a symbolic scheduler partitions work, runs bounded LLM calls for semantic judgment, and aggregates results in code (the canonical note-selection example, lines 68-101). The claim is well-grounded.

- [Grounding] The link to subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md is accurate. That note explicitly cross-references back: "the child task may itself exceed one context window, requiring its own symbolic orchestration internally" (line 19). The two notes complement each other as claimed.

- [Grounding] The link to codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md with the annotation "parallel case: scheduling forced by codified experience rather than structural overflow; same architectural consequence, different cause" is accurate. The codified-scheduling note mirrors this exactly in its own link back: "scheduling forced by structural overflow rather than codified experience; same architectural consequence, different cause" (line 35).

- [Internal consistency] The note is internally consistent. The progression from "becomes a scheduling problem" (title) to "requires a symbolic loop" (P1) to "framework loop is awkward" (P4) to "sub-agent is the canonical response" (P5) follows a coherent logical chain. No definition drift detected -- "scheduling problem," "symbolic loop," "bounded call," and "hidden scheduler" are each used consistently throughout.

- [Internal consistency] The description field ("Some semantic subgoals exceed one context window, so they must be partitioned into smaller semantic judgments with symbolic collection, filtering, and staged summarization between them") faithfully represents the body. It captures the partition-judge-aggregate structure without overclaiming.

Overall: 2 warnings, 2 info
===

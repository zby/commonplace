The note uses the formal notation `M` (the per-call bound) and `m=1` (maximal decomposition) without defining either in the note itself.

- "the per-call bound `M`" — `M` is introduced in the optimization statement with a brief inline label ("respecting the per-call bound `M`"), which provides minimal grounding. However, `M` is never defined in this note — its full semantics come from the linked [symbolic scheduling model](./bounded-context-orchestration-model.md). The sentence reads as if `M` is already known vocabulary, not as a self-contained definition.

- "maximal decomposition to m=1 (one step per bounded call)" — `m=1` notation is used with a parenthetical gloss ("one step per bounded call"), which is adequate. No flag.

- "O(s ln s) cost scaling" — the variable `s` appears without definition. The sentence says "achieves O(s ln s) cost scaling and solves a 1,048,575-step task," from which `s` can be inferred as step count, but it is never named. This requires the reader to reconstruct the variable meaning from context.

Recommendation: Either define `M` inline on first use ("the per-call token bound `M`") or replace it with plain language in prose. Define `s` inline as "number of steps `s`" on first use.

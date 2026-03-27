WARN

All three Relevant Notes bullets begin with lowercase link text that reads as prose, not identifiers.

**Failing bullets:**

```
- [tool loop](./tool-loop-index.md) — context: the index whose argument this convention grounds...
- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: each agent is one iteration...
- [subtasks that need different tools force loop exposure in agent frameworks](...) — motivates: sub-agents are needed precisely...
```

Unlike notes that use hyphenated slug-style identifiers in their link text, this note uses space-separated, human-readable phrases: "tool loop", "bounded-context orchestration model", "subtasks that need different tools force loop exposure in agent frameworks." These read as prose sentence fragments, not code tokens or identifiers.

`[tool loop]` (two words, generic phrase) and `[bounded-context orchestration model]` (mixed, noun phrase) should be "Tool loop" and "Bounded-context orchestration model" to match normal sentence-fragment capitalization. `[subtasks that need different tools...]` is a full lowercase sentence that should start with "Subtasks".

**Recommendation:** Capitalize the first word of each Relevant Notes link text: `[Tool loop]`, `[Bounded-context orchestration model]`, `[Subtasks that need different tools force loop exposure in agent frameworks]`.

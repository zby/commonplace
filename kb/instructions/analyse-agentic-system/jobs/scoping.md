---
description: "Job of an analyse-agentic-system run: write the scoping records of the memory/context and epistemic lenses"
type: types/instruction.md
---

# Scope both lenses

Write `scoping.md` with the two scoping records the [overview type](../../../types/agentic-system-analysis-overview.md)'s Lens scoping section requires, under exactly these headings:

```markdown
### Memory/context scope

### Epistemic scope
```

For each lens choose `brief` or `full` depth from the trigger evidence in `boundary.md` and `runtime-draft.md`, name those trigger records, and state the depth in the record. Memory/context is `full` when the runtime draft shows a route that writes retained content (facts, notes, embeddings, summaries, logs read back later) or a route that assembles retained content into a model's context; otherwise `brief`. Epistemic is `full` when the system claims to produce, check, or grant reliance on truth-apt content, or a route admits content into retained knowledge through a check; otherwise `brief`. Both lenses always run; thin evidence produces a bounded brief result, not a skipped lens. The memory record also states the exclusions and the question the memory report must answer; it becomes part of the memory specialist's frozen input.

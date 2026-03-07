---
description: Distilled artifacts should not link back to sources (focus), but sources should link forward to distilled targets ("Distilled into:") so that source changes trigger staleness review of downstream artifacts
type: note
areas: [links]
status: seedling
---

# Distilled artifacts need source tracking at the source

Distillation produces artifacts optimized for a single goal — an instruction guides an agent, a skill body executes a workflow, a focused note makes one argument. Inline links to the methodology notes, conversations, and earlier drafts that informed the artifact would dilute that focus. The reader of the instruction doesn't need to follow a link to understand why a convention exists; they need to follow the convention.

But the maintainer needs to know the dependency structure. When a source note changes — a methodology claim is revised, a convention is updated, an architectural decision is reversed — every artifact distilled from that source is potentially stale. Without a record of what went into the distillation, there's no way to know which artifacts to review.

## Source-side tracking

The dependency link belongs at the source, not the target. A distillation typically draws from multiple source notes. Each source gets a "Distilled into:" entry in its footer:

```markdown
Distilled into:
- [WRITING.md](../WRITING.md) — the area assignment checklist
```

This optimizes for the primary maintenance scenario: you're editing a methodology note, you see "Distilled into: WRITING.md", you know to check whether WRITING.md needs updating. No reverse lookup needed. The reverse query ("what informed this instruction?") is cheap: `rg "WRITING.md" kb/notes/` finds all notes linking to the target. The KB is small enough that grep is the query engine.

## Two audiences, one link direction

| | Distilled artifact | Source note |
|---|---|---|
| **Reader** | Agent executing a task | Maintainer updating methodology |
| **Links** | Only to things the reader needs | Forward to distilled targets via "Distilled into:" |
| **Staleness signal** | None — it doesn't know its sources | Visible — "I changed, and these downstream artifacts may be stale" |

The distilled artifact stays focused. The source note carries the forward pointer. Staleness detection flows in the direction of change: source changes → maintainer sees downstream targets → reviews them.

---

Relevant Notes:
- [skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) — foundation: the distillation process that produces artifacts needing source tracking
- [link graph plus timestamps enables make-like staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — extends: "Distilled into:" links provide the dependency edges that distilled artifacts deliberately omit
- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — motivates: why distilled artifacts shouldn't carry links back to sources
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — motivates: distillation is a form of frontloading; source-side tracking preserves the pre-frontloaded dependency structure

Distilled into:
- [WRITING.md](../WRITING.md) — the distillation tracking rule

Topics:
- [links](./links.md)

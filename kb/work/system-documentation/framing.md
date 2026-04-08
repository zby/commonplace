# System Documentation Workshop

## The problem

The KB mixes three kinds of notes without explicit separation:

1. **General theory** (~35%) — claims about any agent system ("context efficiency is the central design concern")
2. **Agentic KB design principles** (~35%) — claims about building agent-operated KBs, validated against this system but transferable ("title-as-claim enables traversal-as-reasoning")
3. **Commonplace-specific design** (~30%) — how *this* system works ("directory-scoped types are cheaper than global types")

ADRs document *decisions* — why we chose X over Y at a specific point. But they're deliberately high-level and don't compose into a picture of the current system. If you want to understand how commonplace works today, you'd have to:

- Read CLAUDE.md (router, not documentation)
- Walk through 12 ADRs (decisions, not current state)
- Find and read ~30 system-specific notes scattered across `kb/notes/`
- Read instruction files in `kb/instructions/`

Nobody can build a mental model of the system this way. The general theory is well-indexed (learning-theory-index, computational-model-index, foundations-index). The system-specific knowledge has no equivalent entry point.

## What's needed

A way to document the current system that is:

- **Navigable** — someone (human or agent) can find "how does the type system work?" without knowing which notes, ADRs, and instructions to read
- **Current** — reflects the system *as it is*, not the history of decisions that got it here
- **Composable with theory** — system-specific docs should link to the general theory they instantiate, and vice versa
- **Maintainable** — doesn't create a parallel documentation burden that drifts from the actual system

## What we already have

- **CLAUDE.md** — routing table, vocabulary, conventions. Deliberately minimal — a "map, not a manual." Not documentation of how things work, just where to go.
- **ADRs** (12) — high-level decisions with context, alternatives, consequences. Good for "why did we choose X?" but not for "how does X work now?"
- **Instruction files** (`kb/instructions/`) — imperative procedures for specific operations. Good for "how do I do X?" but not for "how does the system hang together?"
- **Type templates** (`kb/notes/types/`, `kb/sources/types/`) — structural specs for document types. Good for "what fields does a note need?" but not for "why do we have these types?"
- **System-specific notes** scattered in `kb/notes/` — arguments for specific design choices. Good for "why is this a good idea?" but not indexed as a collection.
- **The methodology itself** — commonplace's distinctive property: the methodology IS the content. The system documents itself by using itself. But this is also the source of the mixing problem.

## Open questions

### What form should system documentation take?

1. **A curated index** — `commonplace-system-index.md` that lists system-specific notes, ADRs, instructions, and type templates with context phrases. Lightweight, uses existing infrastructure, no new documents. But an index is a directory, not documentation.

2. **A system guide** — a narrative document (or set of documents) that explains how commonplace works, structured by topic (type system, linking, validation, review, skills, workshop layer). Links to notes and ADRs as supporting material. More useful than an index but harder to maintain.

3. **Annotated architecture** — a document that maps the system's components and their relationships, with links into the relevant notes. Like a system diagram in prose. Good for the "how does it hang together?" question.

4. **Something else?** The workshop-layer note suggests temporal documents that consume value. System documentation isn't temporal — it accumulates. But it also goes stale faster than theory notes.

### How does system documentation relate to the existing note types?

- Should system-specific notes get a tag? A trait? A directory?
- Should they stay mixed with theory notes (the methodology-is-content principle) or be separated?
- If separated, what happens to the straddling notes that validate theory against practice?

### What's the right granularity?

- One big document? (Easy to find, hard to maintain)
- One per subsystem? (Type system, linking, validation, review, skills, workshop)
- Layered? (Overview → subsystem guides → individual notes/ADRs)

### How does this relate to the theory/practice split?

The straddling notes (~35%) are doing valuable work: they validate general claims against this system's practice. Separating theory from practice might break this validation loop. The question is whether you can have separation *in navigation* without separation *in production* — i.e., different indexes into the same notes, not different locations.

## Related notes

- [CLAUDE.md](../../CLAUDE.md) — current routing table
- [a-good-agentic-kb-maximizes-contextual-competence](../notes/a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — the theory this system instantiates
- [agent-statelessness-makes-routing-architectural-not-learned](../notes/agent-statelessness-makes-routing-architectural-not-learned.md) — why good routing/documentation matters: every session is day one
- [a-functioning-kb-needs-a-workshop-layer](../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — library vs workshop distinction applies to documentation too
- [instruction-specificity-should-match-loading-frequency](../notes/instruction-specificity-should-match-loading-frequency.md) — system-specific note that exemplifies the straddling problem
- [skills-derive-from-methodology-through-distillation](../notes/skills-derive-from-methodology-through-distillation.md) — the methodology-is-content principle that makes separation tricky

# System Documentation Workshop

## The real problem

This KB is meant to be used by people building their own agentic KBs. It contains:

1. **General theory** (~35%) — claims about any agent system ("context efficiency is the central design concern," "knowledge storage does not imply contextual activation"). A practitioner needs this to understand *why* certain designs work.

2. **Transferable design patterns** (~35%) — claims about building agent-operated KBs, validated here but applicable elsewhere ("title-as-claim enables traversal-as-reasoning," "progressive disclosure matches instruction specificity to loading frequency"). A practitioner needs this to know *what* to implement.

3. **Commonplace-specific implementation** (~30%) — how *this* system instantiates the patterns ("directory-scoped types," "the `/connect` skill," "review gates with SQLite storage"). A practitioner needs this as *one example* of how to make the patterns concrete — but they'll make different choices.

Right now a practitioner building their own KB would have to read everything and figure out which notes transfer and which are our specific choices. There's no signal saying "this is a general principle you should adopt" vs "this is how we happened to implement it."

### What practitioners actually need

A practitioner building an agentic KB needs to answer, roughly in this order:

1. **Why does this matter?** — The theory. Why context efficiency forces certain architectural choices. Why storage is solved but activation isn't. Why learning requires durable artifacts.

2. **What should I build?** — The design patterns. Progressive disclosure. Claim titles. Typed links with semantic relationships. The library/workshop split. File-first with progressive formalization.

3. **How did someone else do it?** — A reference implementation. Commonplace as a worked example. Not to copy, but to see what the patterns look like when instantiated — and what tradeoffs were made.

4. **How do I build skills?** — The skill system. How skills are structured, how they're loaded, how they interact with the agent harness, what makes a good skill. Our skills (`/ingest`, `/connect`, `/snapshot-web`, `/review-related-system`, etc.) are working examples — but a practitioner building their own KB needs to understand the skill architecture, not just read our skill implementations. This includes: how skills are discovered and activated, how they compose with always-loaded context, how methodology distills into skills, and how to write new ones.

5. **What should I do differently?** — The ADRs and system-specific notes, read critically. Where our choices reflect the theory, and where they reflect our particular constraints (single user, methodology-is-content, no external consumers until recently).

### What's blocking this

- **No layered navigation.** The theory notes, design patterns, and implementation details are mixed in the same indexes. A practitioner can't "zoom in" from principle to pattern to implementation.

- **ADRs document decisions, not current state.** Walking through 12 ADRs tells you why certain choices were made, not how the system works today. And ADRs are deliberately high-level — they don't show the implementation.

- **CLAUDE.md is a router, not documentation.** It tells the agent where to go, not the practitioner how things work or why.

- **The methodology-is-content property cuts both ways.** It means the system documents itself by using itself, which is powerful for internal consistency. But it also means an external reader can't distinguish "this note is about how to build KBs in general" from "this note is about how this particular KB works."

- **Skills have theory and implementations but no architecture guide.** The theory notes explain *why* skills work (methodology distillation, typed callables, progressive disclosure). The skill files show *what* specific skills do. Missing: a document explaining the skill architecture — how the harness discovers and loads skills, how activation triggers work, how skills compose with always-loaded context, and how to write a new skill from scratch. A practitioner building their own system needs this more than they need to read our `/ingest` skill.

## What we already have

- **CLAUDE.md** — routing table, vocabulary, conventions. Deliberately minimal.
- **ADRs** (12) — high-level decisions with context, alternatives, consequences. Good for "why did we choose X?" Not for "how does X work now?"
- **Instruction files** (`kb/instructions/`) — imperative procedures for specific operations.
- **Type templates** (`kb/notes/types/`, `kb/sources/types/`) — structural specs for document types.
- **Theory indexes** — learning-theory-index, computational-model-index, foundations-index. Well-curated entry points into general theory.
- **Related-systems index** — 70+ external systems as comparative evidence.
- **Skills** (`kb/instructions/` and harness-injected) — executable operations like `/ingest`, `/connect`, `/snapshot-web`, `/review-related-system`. Each skill is a working example of methodology-to-procedure distillation, but there's no guide explaining the skill architecture itself — how skills are discovered, loaded, activated, and how to write new ones.
- **Skill theory notes** — [skills derive from methodology through distillation](../notes/skills-derive-from-methodology-through-distillation.md), [instructions are typed callables](../notes/instructions-are-typed-callables.md), [generate instructions at build time](../notes/generate-instructions-at-build-time.md). These explain the theory behind skills but don't document how to build one.
- **System-specific notes** scattered in `kb/notes/` — arguments for specific design choices, not indexed as a collection.

## Options to explore

### Option 1: Layered indexes (lightest touch)

Create three curated indexes that slice the same notes differently:

- **Theory index** (already exists, mostly) — general claims about agent systems
- **Pattern catalog** (new) — transferable design patterns for building agentic KBs, with links to theory notes that ground them and implementation notes that exemplify them
- **Implementation guide** (new) — how commonplace works, organized by subsystem, with links to ADRs that explain why and patterns that it instantiates

Straddling notes appear in multiple indexes with different context phrases. No notes move. No new frontmatter fields.

**Pros:** Cheap, reversible, composable with existing structure.
**Cons:** Three indexes don't compose into a narrative. A practitioner still has to construct the story themselves.

### Option 2: A practitioner's guide (narrative document)

Write a guide aimed at "someone building their own agentic KB." Structure:

1. Start with the theory (why context efficiency matters, what the activation gap means)
2. Derive the design patterns (what follows from the theory)
3. Show the implementation (how commonplace instantiates each pattern)
4. Note the alternatives (what we chose and what you might choose differently)

Each section links deeply into the existing notes. The guide is a reading path through the KB, not a replacement for it.

**Pros:** Gives practitioners what they actually need — a narrative with progressive depth. The synthesis might reveal gaps in the theory.
**Cons:** Maintenance burden. A narrative document drifts from the underlying notes. Someone has to keep it current.

### Option 3: Scope markers on notes (per-note annotation)

Add a frontmatter field or trait indicating transferability:

- `scope: theory` — general claim about agent systems
- `scope: pattern` — transferable design pattern for agentic KBs
- `scope: implementation` — commonplace-specific instantiation

Enables filtering: "show me only the transferable patterns." Makes the layered indexes generatable rather than manually curated.

**Pros:** Per-note, precise, enables automated index generation and filtering.
**Cons:** Requires touching ~100 notes. The straddling notes need judgment calls. Creates a new maintenance obligation (new notes need scope tagging).

### Option 4: Combination

The options aren't mutually exclusive. A practical path:

1. Start with **Option 1** (layered indexes) to discover the right categorization through manual curation
2. If the categorization stabilizes, codify it as **Option 3** (scope markers) so it's maintainable
3. Use the indexes as the skeleton for **Option 2** (practitioner's guide) when the theory is mature enough

This follows the KB's own progressive formalization principle: start with loose structure, tighten as understanding develops.

## Open questions

1. **Is three layers right, or is it really two?** The "transferable design patterns" layer might not be distinct from theory — a pattern IS a theory applied to a domain. Maybe it's just "general theory" (transfers to any agent system) and "this system" (how commonplace works).

2. **What about the synthesis article from the memory workshop?** The `synthesis-ideal-memory-system.md` is already structured as a practitioner-facing article. Is that the model for how theory should be packaged? If so, each major theory cluster might need its own synthesis document.

3. **Does the methodology-is-content property survive external readers?** The system's distinctive claim is that methodology and content aren't separate. But an external reader specifically needs them separated — they want the methodology (how to build KBs) without the content (what this KB contains about learning theory, context engineering, etc.). Or do they want both?

4. **How does this relate to the MkDocs site?** ADR-011 committed the KB to external accessibility via GitHub Pages. The site is a rendering of the notes. If we add layered navigation, it should be reflected in the site structure.

5. **What's the minimum viable version?** Probably: one index page titled "Building an Agentic KB" that curates the 15-20 most important notes in reading order, with context phrases that tell the practitioner what each note gives them and whether it's theory, pattern, or implementation example.

## Related notes

- [CLAUDE.md](../../CLAUDE.md) — current routing table
- [ADR-011: notes must be accessible to external readers](../notes/adr/011-notes-must-be-accessible-to-external-readers.md) — the commitment to external readership that makes this workshop load-bearing
- [a-good-agentic-kb-maximizes-contextual-competence](../notes/a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — the theory this system instantiates
- [agent-statelessness-makes-routing-architectural-not-learned](../notes/agent-statelessness-makes-routing-architectural-not-learned.md) — why good routing/documentation matters: every session is day one
- [skills-derive-from-methodology-through-distillation](../notes/skills-derive-from-methodology-through-distillation.md) — the methodology-is-content principle
- [instruction-specificity-should-match-loading-frequency](../notes/instruction-specificity-should-match-loading-frequency.md) — exemplifies the straddling problem (general principle, specific instantiation)
- [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — the note that prompted this workshop: general theory that should be extractable for practitioners
- [synthesis-ideal-memory-system](./agent-memory-design/synthesis-ideal-memory-system.md) — possible model for practitioner-facing synthesis documents

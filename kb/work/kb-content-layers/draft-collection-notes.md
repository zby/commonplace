# Draft: COLLECTION.md for kb/notes/ (theoretical register)

> Draft for review. Target location: `kb/notes/COLLECTION.md`.

---
register: theoretical
quality_goal: reach
context_strategy: "One claim covers many situations — compress across contexts"
title_convention: claim
---

## Register

This collection operates in the **theoretical register**. Documents here make transferable claims about what is true — mechanisms, principles, and general arguments that should hold across systems, not just in this one.

The quality goal is **reach**: the most general formulation the argument supports, with boundaries mapped explicitly. A note with reach compresses many situations into one explanation, making bounded context work harder.

## Title conventions

**Claim titles by default.** Name the note like a claim, not a topic: "structure enables navigation without reading everything" rather than "thoughts on structure." The title should be something that could be true or false.

Composability test: the title should work as prose when linked — `since [title](./title.md)` or `because [title](./title.md)` should read naturally.

Claim strength test: the claim should be contestable. "Continuous learning is substrate-independent" fails — nobody would push back. "Continuous learning can happen outside of weights" names the thing people actually doubt.

**Exceptions.** Don't force a claim title when it feels strained. Common exceptions:
- Multi-claim specs and frameworks (no single claim subsumes the content)
- Definitional notes (the title is the term being defined)
- Indexes (navigation hubs)
- Seedlings not ready to assert a clear claim

If using a claim title, add the `title-as-claim` trait so review gates can check the promise.

## Description conventions

Descriptions are **retrieval filters, not summaries**. The test: if an agent searched for this note's main concept and got 5 results, would this description help pick THIS one? Descriptions that paraphrase the title add zero retrieval value. Keep under 200 characters; 50–200 is the intended range. Double-quote in frontmatter.

## Reach as quality discipline

Aim for notes that explain *why*, not just record *what works*. Quick tests:
- If you changed one premise, could you predict what changes in the conclusion?
- Would the insight still apply in a different domain?
- Could someone say exactly how the explanation is wrong, not just that it's incomplete?

Notes that only record "X works" are adaptive — useful but brittle. Notes that explain why X works have reach. Reach is a goal to move toward, not a gate every note must clear.

## Outbound linking conventions

When linking FROM this collection:

| To register | Appropriate relationships | Notes |
|---|---|---|
| Theoretical (same register) | since / because / contradicts / extends / qualifies | The claim-traversal graph. These are the argumentative links that make traversal-as-reasoning work. |
| Descriptive (reference, related-systems) | evidence / derived-from / exemplifies | Theories cite descriptions as observations and evidence. The theory must stand without any single description — if it can't, it's still a description, not yet a theory. |
| Prescriptive (instructions) | evidence (rare) | Theories rarely need to cite procedures. When they do, it's usually to note that a practice exists, not to depend on it. |

**Formulation constraint.** The theory's claim — title and opening argument — must be statable in general terms, even when derived from a specific system. If you can't state it without referencing a particular system, it's not yet a theory.

## KB vocabulary on first mention

Terms like [distillation](./definitions/distillation.md), [constraining](./definitions/constraining.md), [codification](./definitions/codification.md), and [context engineering](./definitions/context-engineering.md) have definitions in `definitions/`. On first mention, provide an inline gloss and a link: `[distillation](./definitions/distillation.md) (directed context compression)`.

## Default template

```markdown
---
description: ""
type: note
traits: []
tags: []
status: current
---

# {Claim title}

{Opening paragraph: state the claim and why it matters.}

{Body: argument, evidence, mechanism.}

## Open Questions

- {Question}

---

Relevant Notes:

- [related-note](./related-note.md) — {relationship: extends / grounds / contradicts / enables / exemplifies}
```

## Frontmatter

Frontmatter makes notes queryable via ripgrep. Its presence determines the note's base type:

- **No frontmatter** → `text` — raw capture, no structural expectations
- **Has frontmatter** → `note` or more specific type — full quality checks apply

| Field | Required | Constraints |
|-------|----------|------------|
| `description` | Yes | Must discriminate this note from similar ones |
| `type` | No | Base type: `note` (default) or a specialized type |
| `traits` | No | Review-routing properties: `title-as-claim`, `definition`, `has-comparison`, `has-external-sources`, `has-implementation` |
| `tags` | No | Freeform tags for navigation |
| `status` | No | `seedling`, `current`, `speculative`, `outdated`; some types override this vocabulary |

Write `description` as a double-quoted string. This avoids YAML coercion and parse breaks from characters like `: `.

## Links

Internal documents connect via standard markdown links with relative paths from the source file's directory.

- `[note title](./note-title.md)` — same directory
- `[note title](../note-title.md)` or `[note title](./subdir/note-title.md)` — cross-directory
- Links work as prose: "Since [structure enables navigation](./structure-enables-navigation.md), we chose..."
- Link text doesn't have to match the target's title — use whatever best informs the reader

**Inline vs footer.** Prefer inline links — they carry more information. Footer links are for connections that don't fit naturally into prose:

```markdown
---
Relevant Notes:

- [related note](./related-note.md) — extends this by adding the temporal dimension
```

**Link semantics.** Every connection must articulate the relationship:
- **extends** — builds on an idea by adding a new dimension
- **foundation** — provides the evidence or reasoning this depends on
- **contradicts** — conflicts with this claim
- **enables** — makes this possible or practical
- **example** — illustrates this concept in practice

Bad: `[note](./note.md) — related`
Good: `[note](./note.md) — extends this by adding the runtime perspective`

**Target maturity.** Foundation/grounds links are load-bearing — if the target changes, the linking note's argument weakens. When using foundation links to `status: seedling` or `status: speculative` notes, acknowledge the instability.

**Dangling link policy.** Every link must point to a real file. Before creating a link, verify the target exists with `ls`.

## Filenames

Use lowercase, hyphens for spaces, and the `.md` extension. Derive the filename from the `# Title` heading. Filename slugs are capped at 100 characters.

## Distillation tracking

When you distill content from notes into a focused artifact (instruction, skill body, COLLECTION.md section), add a "Distilled into:" entry in each source note's footer:

```markdown
Distilled into:

- [COLLECTION.md](./COLLECTION.md) — the reach checklist
```

Each source gets its own link so that when it changes, the maintainer sees the downstream artifact that may need review. The distilled artifact itself should NOT link back to its sources.

## Safe rename

Never rename a note manually — it breaks links. Use `commonplace-relocate-note`, which renames or moves the note and updates backlinks across the KB.

## Indexes

There are two kinds of indexes in this collection:

- **Directory indexes** (`index.md`) — auto-generated flat listings of all files with title, description, and type. Use `type: index` with `index_source: directory`.
- **Generated-tail indexes** (e.g. `learning-theory-index.md`, `tags-index.md`) — navigation hubs with an optional curated section plus a generated listing. Use `type: index` with `index_source` describing what the generated section lists.

Rebuild with `commonplace-refresh-indexes`.

**Generated-tail index structure:**

- **Curated section** (optional, hand-written): editorial groupings with context phrases. Curated entries MUST have context phrases — a bare link list is an address book, not a map.
- **Generated section** (automatic): complete listing below the `<!-- generated -->` marker, rebuilt by `commonplace-sync-generated-index`.

**Index lifecycle:** Create when 5+ related notes accumulate under a tag. Curate when the generated listing alone isn't enough. Merge when both indexes are small with significant overlap.

## What does NOT belong here

- Descriptions of how a specific system works → descriptive register (`kb/reference/` or `kb/related-systems/`)
- Procedures, conventions, how-to guidance → prescriptive register (`kb/instructions/`)
- Raw captures without frontmatter → `text` type, any collection
- Work in progress → `kb/work/` (workshops)

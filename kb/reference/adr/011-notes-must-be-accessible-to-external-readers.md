---
description: GitHub Pages commits the KB to external readers who lack CLAUDE.md context — KB vocabulary needs inline glosses and definition links on first mention
type: kb/reference/types/adr.md
tags: []
status: accepted
---

# 011-Notes must be accessible to external readers

**Status:** accepted
**Date:** 2026-04-06

## Context

The KB has always had two internal audiences: agents (who get CLAUDE.md and on-demand methodology loaded into context) and the human operator (who has accumulated familiarity with the vocabulary and conventions). When we added GitHub Pages rendering via MkDocs, we implicitly committed to a third audience: external readers arriving at the rendered HTML with no prior context.

This audience has neither the agent's loaded definitions (CLAUDE.md Vocabulary section, definition notes loaded on demand) nor the operator's background. A sentence like "the skill is produced by distillation from the methodology notes" is clear to both internal audiences but opaque to an external reader who doesn't know that "distillation" has a specific technical meaning in this KB.

The [undefined-terms review gate](../../instructions/review-gates/accessibility/undefined-terms.md) previously exempted KB vocabulary terms (distillation, constraining, codification, context engineering) on the grounds that they were "established KB vocabulary." This exemption optimized for the internal audiences at the expense of the external one.

## Decision

Notes must be written so that an external reader can follow the argument without leaving the page. Specifically:

1. **KB vocabulary terms require an inline gloss and a definition pointer on first mention.** The gloss orients the reader enough to keep reading; the pointer provides depth. Example: `distillation (directed context compression)`.
2. **The undefined-terms gate no longer exempts KB vocabulary.** These terms are now subject to the same first-mention test as any other technical term.
3. **The WRITING.md checklist includes a KB vocabulary item** reminding authors that external readers lack CLAUDE.md context.

The general principle: authors write with full KB context loaded; readers arrive with none. Every note must bridge that gap on its own.

## Consequences

### Easier

- **External readers** can follow notes without chasing definition links or guessing at private vocabulary.
- **New contributors** (human or agent) get oriented faster — the gloss pattern teaches the vocabulary incrementally.
- **Notes are more composable** — a note that defines its terms inline can be excerpted or linked from outside the KB without losing meaning.

### Harder

- **Authoring cost increases** — every first mention of a KB term needs a gloss. This is intentional friction, like the link-relationship requirement ([ADR 009](./009-link-relationship-semantics.md)).
- **Glosses may drift** from definitions — if the definition of "distillation" evolves, glosses scattered across notes may become stale. The definition notes remain authoritative; glosses are approximations.
- **Existing notes are non-compliant.** Retrofitting glosses across the KB is a gradual process, not a bulk operation. The review gate will surface violations as notes are reviewed.

---

Relevant Notes:

- [009-link-relationship-semantics](./009-link-relationship-semantics.md) — parallel: another intentional-friction authoring requirement that improves navigation at the cost of writing speed
- [undefined-terms gate](../../instructions/review-gates/accessibility/undefined-terms.md) — implements: the updated gate that enforces first-mention glosses
- [notes COLLECTION.md](../../notes/COLLECTION.md) — implements: checklist item 5 (KB vocabulary on first mention)

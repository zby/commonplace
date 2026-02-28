---
description: Decision to inline note and structured-claim templates into WRITING.md so the agent gets type structure and writing conventions in a single hop — eliminates one read for the two most common note types
type: adr
areas: [document-system]
status: accepted
---

# 002-inline-global-types-in-writing-guide

**Status:** accepted
**Date:** 2026-02-28

## Context

When writing a note, the agent needs two things: the type template (what sections and frontmatter fields to include) and the writing conventions (title-as-claim, description quality, composability). These lived in separate files:

- Type templates in `kb/notes/types/note.md` and `kb/notes/types/structured-claim.md`
- Writing conventions in `kb/WRITING.md`

The agent's workflow was: read WRITING.md for conventions (1 hop), then read the type template for structure (1 hop). Since [CLAUDE.md is a router, not a manual](../context-loading-strategy.md), it points to WRITING.md for writing guidance — but WRITING.md then pointed elsewhere for the actual templates. Two hops for every write.

The [scenario decomposition](../scenario-decomposition-drives-architecture.md) confirmed this: the "know the structure" and "know how to write well" steps are adjacent in every write scenario. They always load together. Separating them costs a hop with no benefit.

The two global types — `note` and `structured-claim` — account for ~80% of note creation. The remaining types (`adr`, `index`, `related-system`) are directory-local and used less frequently.

## Decision

Inline the `note` and `structured-claim` templates directly into `kb/WRITING.md`, in a Templates section. The canonical type files in `kb/notes/types/` remain unchanged — they're still the authoritative definitions and are used by `/validate`. WRITING.md duplicates their content for loading efficiency.

Directory-local types (`adr`, `index`, `related-system`, `source-review`, task types) are NOT inlined. They stay in their respective `types/` subdirectories. WRITING.md lists where to find them but doesn't reproduce them. These types are less common, and inlining them would bloat a file that loads for every write, not just the writes that need those types.

## Consequences

**Easier:**
- The common write path drops from 2 hops to 1 at the "know the structure" step. The agent reads WRITING.md and has both conventions and the template for `note` or `structured-claim`.
- The [scenario cost evaluation](../../scenarios/write-a-note.md) confirms: step 4 (know the structure) and step 5 (know how to write well) now reference the same file with 0 additional hops.

**Harder:**
- Two sources of truth for the global type templates. If the template changes in `kb/notes/types/note.md`, it must also change in `kb/WRITING.md`. This is a maintenance burden, but the templates are stable — they change rarely.
- WRITING.md is ~1,100 bytes larger (the two inlined templates). Since it loads for every write scenario, this adds ~1,100 bytes to every write. The hop savings (avoiding a ~400-700 byte file read plus tool call overhead) outweigh this.

**Unchanged:**
- Directory-local types still require an additional hop when needed. This adds 1 hop for ~20% of writes (adr, index, related-system creation). Acceptable because these types are less common and the alternative (inlining everything) would make WRITING.md too large.
- `/validate` still reads from `kb/notes/types/` — it validates against the canonical type files, not WRITING.md.

---

Relevant Notes:
- [context-loading-strategy](../context-loading-strategy.md) — foundation: the loading hierarchy principle (match instruction specificity to loading frequency) motivates combining two always-together loads into one
- [scenario-decomposition-drives-architecture](../scenario-decomposition-drives-architecture.md) — grounds: the step decomposition shows "know the structure" and "know how to write well" are adjacent in every write scenario, confirming they belong in the same file

Topics:
- [document-system](../document-system.md)

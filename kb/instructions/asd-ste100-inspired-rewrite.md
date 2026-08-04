---
description: "Use when explicitly asked to experiment with rewriting one KB note in language inspired by ASD-STE100 while preserving its knowledge content"
type: kb/types/instruction.md
---

# Rewrite a note with ASD-STE100-inspired language

Experimental. Use this instruction only with an explicit note path. It is inspired by ASD-STE100; it is not a compliance procedure.

## Rewrite

1. Read the note, its collection's `COLLECTION.md`, and its type specification.
2. Rewrite the prose with these preferences:
   - Give each sentence one main point.
   - Prefer short, direct sentences and active voice.
   - When splitting, restate any definition, condition, qualification, cause, contrast, or appositive relation carried by the original syntax.
   - Keep items in a list grammatically parallel.
   - Name the actor when the actor matters.
   - Use one term consistently for one concept.
   - Make necessary logical connections explicit.
3. Preserve the note's claim, reasoning, evidence, scope, frontmatter, title, headings, links, code, quotations, and registered identifiers. If a preference would change the meaning, preserve the original wording.
4. Run `commonplace-validate <note-path>`.
5. Append departures, observed effects, and new ideas to `kb/reports/asd-ste100-inspired-rewrite.md`.

## Verify

- Compare every split with the original. Check definitional force, modifier attachment, shared qualifiers, appositive identity, logical connections, and list parallelism.
- Read the complete diff for lost qualifiers, changed causal direction, or broadened or narrowed scope.
- Confirm that validation passes.

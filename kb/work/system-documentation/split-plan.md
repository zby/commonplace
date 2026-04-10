# Reference Split Plan

Plan for the notes that should not move wholesale from `kb/notes/` to `kb/reference/`, but instead need to be split into:

- a retained theory note in `kb/notes/`
- a new current-state reference note in `kb/reference/`

This is separate from [move-plan.md](./move-plan.md) because the work is editorial, not mechanical. A relocate pass can move a file and rewrite links. It cannot decide which claims are transferable theory, which passages are local implementation detail, and how to reframe both halves so each stands on its own.

## Goal

After this split batch lands:

- `kb/notes/` contains only the transferable claim, argument, or design principle
- `kb/reference/` contains the commonplace-specific implementation, subsystem description, or operational boundary
- each pair links to the other explicitly
- indexes and entry points can point readers to either theory or current-state documentation without mixing the two

## Split contract

Every split in this plan should satisfy the same contract:

1. The `kb/notes/` file remains the canonical statement of the transferable idea.
2. The new `kb/reference/` file describes how commonplace currently instantiates that idea.
3. The theory note should not depend on current repo paths, current scaffold contents, or current implementation details to make sense.
4. The reference note should not pretend to be universal theory; it should be explicit that it describes commonplace as it exists today.
5. Each side should link to the other in a short "Relevant Notes" or equivalent section.
6. Validation runs after each landed split, not only at the end of the whole batch.

## Work queue

| Source note | New reference note | Theory to keep in `kb/notes/` | Local material to extract into `kb/reference/` | Status |
|---|---|---|---|---|
| `kb/notes/directory-scoped-types-are-cheaper-than-global-types.md` | `kb/reference/type-loading.md` | The economic argument for directory-scoped type loading and thin global types | Current commonplace type layout, path-specific loading behavior, and where global versus collection-local types currently live | done |
| `kb/notes/generate-instructions-at-build-time.md` | `kb/reference/instruction-generation.md` | The general argument for build-time generation over runtime prompt assembly | Current commonplace generation pipeline, scaffold/template sources, and concrete generated artifacts | done |
| `kb/notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md` | `kb/reference/control-plane-goals.md` | The claim that KB goals belong in always-loaded control-plane context | Current `AGENTS.md`/template/install contract and what commonplace presently keeps in always-loaded context | done |
| `kb/notes/scenario-decomposition-drives-architecture.md` | `kb/reference/scenario-architecture.md` | The method: derive architecture from scenario decomposition and context transitions | Current commonplace-vs-installed-project split, concrete scenario surfaces, and the present architecture they justify | done |
| `kb/notes/files-not-database.md` | `kb/reference/storage-architecture.md` | The general files-versus-database argument | Commonplace's current storage boundary: authored files, generated indexes, review-state SQLite exception, and operational rationale | done |

## Landing strategy

Each split should land as its own small batch:

1. Read the source note and mark the paragraphs that are still true if commonplace changed shape tomorrow.
2. Mark the paragraphs that would need rewriting after a path, scaffold, or subsystem change.
3. Create the new `kb/reference/` note first, using only the local/current-state material.
4. Rewrite the original `kb/notes/` note so it reads cleanly without the extracted local detail.
5. Add reciprocal links between the theory note and the reference note.
6. Update any index or navigation pages that should now point at the reference note rather than the theory note.
7. Run `commonplace-validate-notes` after the split lands.

The split should not be done by copying the note wholesale and trimming later. That tends to preserve mixed framing on both sides. The target is two clean documents with different jobs.

## Recommended order

Recommended execution order:

1. `files-not-database` → `storage-architecture`
2. `kb-goals-in-always-loaded-context-guide-inclusion-decisions` → `control-plane-goals`
3. `generate-instructions-at-build-time` → `instruction-generation`
4. `directory-scoped-types-are-cheaper-than-global-types` → `type-loading`
5. `scenario-decomposition-drives-architecture` → `scenario-architecture`

Why this order:

- `files-not-database` and `kb-goals...` are the clearest seams and unblock the architecture/reference entry points.
- `generate-instructions...` and `directory-scoped-types...` are tightly coupled to current scaffold/type-loading explanations and benefit from the earlier control-plane/storage language.
- `scenario-decomposition...` is the broadest and most synthesised split, so it should come last after the narrower subsystem reference notes exist.

## Per-note risks

### `files-not-database.md`

Risk: the note currently mixes a general substrate argument with the specific review-state exception. If split badly, the theory note will become too abstract or the reference note will silently redefine the rule.

Expected seam:

- theory note: why files are usually the right primary substrate for KB knowledge
- reference note: why commonplace still uses SQLite for review state and where that boundary sits

### `kb-goals-in-always-loaded-context-guide-inclusion-decisions.md`

Risk: the present note may be carrying both a general routing principle and a concrete statement about commonplace install-time files. The split must preserve the principle without baking in today's file names.

Expected seam:

- theory note: goals belong in always-loaded control-plane context
- reference note: how commonplace currently realises that in `AGENTS.md` and scaffolded installs

### `generate-instructions-at-build-time.md`

Risk: the note may rely on current Commonplace examples to make the general point legible. If those examples are removed without replacement, the theory side may lose force.

Expected seam:

- theory note: frontload interpretation and generation work when possible
- reference note: the concrete commonplace generation and packaging flow

### `directory-scoped-types-are-cheaper-than-global-types.md`

Risk: the current implementation section may be doing too much of the explanatory work. The theory note must still defend the claim without the current directory tree as its only evidence.

Expected seam:

- theory note: loading and routing economics favor local type directories
- reference note: current commonplace type lookup shape and global-type boundary

### `scenario-decomposition-drives-architecture.md`

Risk: this is the most likely note to need heavy rewriting rather than clean extraction. The method and the current commonplace architecture are interleaved.

Expected seam:

- theory note: architecture should be derived from decomposed use scenarios
- reference note: the concrete commonplace scenarios and the architecture they currently support

## Definition of done

A split candidate is done when:

- both the theory note and the reference note read cleanly on their own
- the theory note no longer makes path- or implementation-specific claims
- the reference note is clearly current-state documentation
- links and indexes are updated
- `commonplace-validate-notes` passes

## Not part of this plan

- Inventing a new `system-doc` type
- Adding a per-note `scope` field or trait
- Reclassifying unrelated notes beyond the five candidates listed above

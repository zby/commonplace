# Experiment plan: per-collection registers

## Goal

Test whether per-collection `COLLECTION.md` files improve writing and connecting quality, and whether the [three-register framework](../../notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with-asymmetric-linking.md) (theoretical / descriptive / prescriptive) holds up in practice.

All convention docs are deploy-time learning artifacts — iterate from use, don't design to completion upfront.

## Two orthogonal axes

- **Register** (per-collection, declared in COLLECTION.md) — theoretical / descriptive / prescriptive. Determines quality goal, title conventions, linking conventions, context-efficiency strategy.
- **Operational role** (usually per-type, sometimes per-collection) — library knowledge, executable instruction, generated report, routing surface, decision record, vocabulary anchor. Determines structural contract and lifecycle. Some roles are type-encoded (`adr`, `definition`, `connect-report`, `index`), but others emerge from collection context — `kb/instructions/` has no specialized instruction type; a plain `note` there takes on an executable role that the same type wouldn't have in `kb/notes/`.

A `note` in `kb/notes/` is theoretical library knowledge. A `note` in `kb/reference/` is descriptive library knowledge. Same type (same structural contract), different register (different quality goal). An `adr` in `kb/reference/` is descriptive decision-record. Register × type gives you the full picture; neither axis alone is sufficient.

## Phase 0: Make tags per-collection

Tags are index-routing metadata. Indexes are per-collection. Tags must match.

- [x] Update `sync_generated_index.py` to be collection-aware — tags scoped per collection, indexes scan only their own collection
- [x] Update `refresh_indexes.py` to discover collections dynamically
- [x] Update tests
- [ ] Remove dead tags from `kb/reference/` docs (tags route nowhere without reference-local indexes)
- [ ] Remove dead tags from `kb/instructions/` docs (same)
- [ ] Revert the `type-system` → `types` tag rename in `kb/notes/` (see [revert-instructions.md](./revert-instructions.md))

Code is done. Tag cleanup remains — runs in a separate session per revert-instructions.md.

## Phase 1: Draft the three COLLECTION.md files

No infrastructure changes. Write the files in the workshop and test them manually (load into context when writing or connecting, see if the guidance helps).

- [x] `kb/notes/` (theoretical register) — [draft-collection-notes.md](./draft-collection-notes.md)
- [ ] `kb/reference/` (descriptive register) — draft as `draft-collection-reference.md`
- [ ] `kb/instructions/` (prescriptive register) — draft as `draft-collection-instructions.md`

Each COLLECTION.md has:
- **Structured fields** (register, quality goal, title/description conventions, outbound linking conventions, default template) — what the compile step extracts and tools consume
- **Free-form prose** describing the collection's purpose, character, operational role, typical workflows, and edge cases — what the writing agent reads to understand context. This is where collection-specific nuance lives, including things like the instruction duality ("these documents are part of the working system, not just documentation")
- **"What does NOT belong here"** — helps agents route content to the right collection

COLLECTION.md lives at the collection root (e.g. `kb/notes/COLLECTION.md`), visible to humans and agents. Not hidden — it's navigational documentation, not config.

**No testing in Phase 1.** Drafting only — write the three COLLECTION.md files and review them for completeness by hand. Testing happens after the WRITING.md split (Phase 2), when the old guidance is gone and the agent has no choice but to use the new path.

## Phase 2: Split WRITING.md

Not retire — split. Universal mechanics still need an authored source of truth, even if the writing skill bakes a distilled copy into its body. The skill body is a *distillation* of the mechanics source, not the source itself. Keeping the separation follows the same distillation chain the theory note describes.

Split into:
- **Register-specific conventions** (title-as-claim, reach, linking rules, economy, precision) → already in each collection's COLLECTION.md
- **Universal framework mechanics** (frontmatter format, link syntax, filename rules, distillation tracking) → slim mechanics document (source of truth); skill distills from it
- **Useful commands** (relocate-note, validate, refresh-indexes) → `kb/reference/` as a description of available tools
- **Index conventions** → COLLECTION.md for collections that manage indexes, or index skill
- **Common pitfalls** → distribute: register-specific ones into COLLECTION.md, procedural ones into the skill

Note: **distillation tracking is cross-register**, not mainly theoretical. Theory→instruction, report→note, workshop→ADR, source→source-review, procedure→skill are all distillation edges. It belongs in the universal mechanics, available to any collection that can be a distillation source.

The loading hierarchy for writing: just `COLLECTION.md` for global types (`note`, `text`, `index`, `definition` — templates baked into the skill), plus `types/{type}.template.md` only for collection-local types. The common case is one document.

**No testing in Phase 2.** The split is a refactoring step. Testing happens after deploy (Phase 3).

## Phase 3: Deploy and test

Deploy:
- Place COLLECTION.md files at collection roots (visible, not hidden)
- Decide on types/ location: keep where they are, or move to `.collection/types/` (hidden is fine for schemas and templates — they're config, not documentation)
- Update type resolution if types/ moves
- Update `commonplace-init` to create COLLECTION.md files for new collections
- Slim WRITING.md to the mechanics source document
- Update CLAUDE.md to point to COLLECTION.md files instead of WRITING.md

Verify: `uv run pytest` — all tests pass. Validation still works. Skills still find type templates.

**Integration test (manual, three roles):**

1. **Agent prepares** — copies the environment to `/tmp/commonplace-test/` with all changes applied (COLLECTION.md files deployed, WRITING.md split, CLAUDE.md updated). Verifies the copy is clean.
2. **User runs** — `cd /tmp/commonplace-test/ && claude -p 'write a note about ...'` (one-shot, fresh session, no prior context).
3. **Agent checks** — inspects what the test agent read (tool call log, any file reads outside the designed path). The success criterion: did the agent read only COLLECTION.md + type template + related-note searches? If it reached for anything else, what was it and what's missing?

**Test cases:**
- Write a theory note in `kb/notes/`.
- Write a reference doc in `kb/reference/`.
- **Instruction duality test:** Write an instruction in `kb/instructions/`. Does the register × type model handle "prescription as implementation" without a fourth register?

## Phase 4: Adapt skills

Only if Phase 3 testing passes — the agent stays within the designed loading path.

### Writing skill

- Parameterize `cp-skill-write` with a target collection (default: `kb/notes/`)
- Skill reads `{collection}/COLLECTION.md` for conventions
- Skill has universal mechanics baked in (distilled from the mechanics source)
- Skill reads `types/{type}.template.md` if using a collection-local type
- Per-collection skill wrappers (e.g. `cp-skill-write-reference`) are thin: set the collection parameter, delegate

### Connect skill

- Build `commonplace-compile-collections` command — reads all COLLECTION.md files, produces a compiled topology document with all registers and cross-register linking rules
- Update `cp-skill-connect` to read the compiled topology
- When connecting: determine source and target registers from their respective collections, suggest relationship types appropriate for that register pair

### Validate

- Consider a validation check for the formulation constraint (theory notes stating claims in general terms). May be too subjective for deterministic validation — could be a review gate instead.

**Test:** Write a note using the adapted skill. Run connect. Are the relationship suggestions register-appropriate? Does the writing skill produce output consistent with the COLLECTION.md conventions?

## Phase 5: Collection moves (separate tasks, after framework is working)

These are consequences of the framework, not prerequisites:

- [ ] Move `kb/notes/related-systems/` to `kb/related-systems/` — create its own COLLECTION.md (descriptive register, landscape variant)
- [ ] Audit `kb/notes/` for description notes that belong in `kb/reference/` (e.g. `why-notes-have-types.md`)
- [ ] Consider renaming `kb/notes/` to `kb/theory/` — clearer register signal, but breaks many paths. Only if the framework proves itself.

## Success criteria

The experiment succeeds if:

1. **COLLECTION.md is self-contained for writing.** The agent stays within the designed loading path (COLLECTION.md + type template + related-note search) without reaching for WRITING.md or other guidance.
2. **The three registers hold up.** No fourth register needed. Straddling cases (like instruction duality) are handled by register × type without stretching.
3. **Practitioners can add collections.** A new collection with a COLLECTION.md is picked up by the compile step. No central file edits required.

## What we're NOT doing

- Not redesigning the type system — types often encode operational role through structural contracts, registers encode content kind through quality goals. They're orthogonal but not perfectly aligned — some operational roles emerge from collection context rather than type.
- Not building a full validation framework for register correctness — formulation constraint checking is a future review gate.
- Not moving all misplaced notes immediately — the audit is a separate task after the framework is proven.
- Not committing to "registers" as permanent terminology — if it doesn't stick in practice, we rename.

## Dependencies

- Phase 0 has no dependencies — do it now.
- Phase 1 depends on Phase 0 (clean tag state).
- Phase 2 depends on Phase 1 drafts being complete.
- Phase 3 depends on Phase 2. This is where the real test happens — deploy to `/tmp/` copy, run `claude -p`, check loading path.
- Phase 4 depends on Phase 3 tests passing (register-specific guidance actually works without the old WRITING.md).
- Phase 5 depends on Phase 4 (moves need the adapted skills).

Phases 1–3 are the experiment. Phases 4–5 are rollout, contingent on the experiment succeeding.

## Relation to other workshops

- `system-documentation/` — the commonplace-specific instance. That workshop produced `kb/reference/` as a descriptive collection. This workshop generalizes the pattern.
- `philosophy-borrowing/` — evaluating speech-act theory as a candidate borrowing. The three-register frame is a speech-act-style decomposition (assertive / representative / directive). Worth cross-pollinating.
- `type-system-rationalization/` — types encode operational role; registers encode content kind. Orthogonal axes, but decisions in one workshop affect the other.

## Decision: tags and indexes are per-collection

Tags are index-routing metadata, not vocabulary. Indexes are per-collection. Therefore tags are per-collection.

- Each collection has its own tags that route into its own indexes.
- A `types` tag in `kb/notes/` routes to the notes `types-index.md`. A `types` tag in `kb/reference/` would route to a reference-local index (if one exists). Same string, different scope — no global namespace.
- Tags on reference docs that have no corresponding reference-local index are dead metadata and should be removed in Phase 0 cleanup.
- Cross-register discovery uses grep (`rg "^tags:.*types" kb/`), not indexes.

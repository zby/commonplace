# Migration plan

Ordered implementation steps for the type-system rationalization. Each step is independently committable and testable.

## Phase 1: Type definitions (YAML)

### 1.1 Write base type YAML files

Create `types/text.yaml` and `types/note.yaml` with the schema from [type-resolver.md](./type-resolver.md).

### 1.2 Write collection type YAML files

Create `.yaml` companions for each current collection-scoped note type:
- `structured-claim.yaml`
- `adr.yaml`
- `index.yaml`
- `spec.yaml`
- `review.yaml`
- `related-system.yaml`
- `source-review.yaml`

Scope notes:

- `structured-claim`, `adr`, `index`, and `related-system` live in `kb/notes/types/`
- `source-review` lives in `kb/sources/types/`
- `spec` and `review` are currently validator-supported legacy `kb/notes/` types without prose templates; add YAML definitions for them so the resolver preserves existing validator behavior instead of silently degrading to base `note`

### 1.3 Fix `related-system` template

Change `kb/notes/types/related-system.md` frontmatter from `type: note` to `type: related-system`.

### 1.4 Update existing related-system notes

Change frontmatter in `kb/notes/related-systems/*.md` from `type: note` to `type: related-system`.

## Phase 2: Type resolver

### 2.1 Implement resolver

Python module: given a file path and parsed frontmatter, return a structural profile (required headings, required fields, allowed status). Scoped lookup: workshop → collection → root.

### 2.2 Tests for resolver

Cover: bare names, scoped fallback, base inheritance, missing YAML graceful degradation, workshop-scoped types.

### 2.3 Integrate resolver into validator

Replace the hard-coded `TYPE_HEADINGS` map and the three special-case checks with resolver-driven profiles:

- `TYPE_HEADINGS` → `required_headings` from YAML
- `spec` any-of logic → `any_headings` from YAML
- `review` date check → `requires_date` from YAML
- `index` link density → `min_links` from YAML

The validator reads the resolved profile and runs the appropriate check for each field present. Validator scope stays `kb/notes/`.

### 2.4 Verify validator output

Run validator on all `kb/notes/` files before and after. Verify by type:

- unchanged types: `note`, `structured-claim`, `adr`, `index`, `spec`, `review`
  For these types, output should be equivalent before and after. Any differences are bugs in the resolver or YAML definitions.
- newly retyped notes: `related-system`
  New warnings are expected and desirable here. These are migration findings (for example missing required sections), not regressions. Review them and fix or acknowledge.
- out of validator scope: `source-review`
  `source-review` does not participate in `kb/notes/` validator parity because the validator still scopes to `kb/notes/`. Cover it in resolver unit tests instead: scoped lookup, YAML loading, and graceful fallback.

Verification procedure:

1. Run the validator on all `kb/notes/` before any type retyping and save the output.
2. Implement resolver + validator integration.
3. Run the validator again before Phase 1.4 retyping and compare outputs for unchanged types.
4. Apply Phase 1.4 (`related-system` retyping).
5. Run the validator a third time and review only the `related-system` diffs as migration findings.

## Phase 3: Traits

### 3.1 Add `title-as-claim` trait to `structured-claim` notes

Bulk-edit all existing `type: structured-claim` notes to include `title-as-claim` in frontmatter `traits:`.

Migration rule:

- merge into the existing `traits:` list rather than replacing it
- de-duplicate traits if the note already carries `title-as-claim`
- preserve unrelated existing traits (`has-comparison`, `has-external-sources`, etc.)

Do **not** rely on implied traits in tooling yet. The current migration keeps trait computation simple: the review system reads explicit `traits:` from frontmatter.

### 3.2 Add `title-as-claim` trait to claim-shaped `note` titles

Scan `kb/notes/` for plain `note` files whose titles are already claim-shaped. Add `title-as-claim` to their existing `traits:` list (or create the list if absent).

Migration rule:

- only consider files with `type: note`
- exclude directories and note kinds that are not supposed to make this promise: `kb/notes/definitions/**`, `kb/notes/related-systems/**`, `kb/notes/adr/**`, `index.md`, `*-index.md`
- generate the candidate list using the current validator's claim-title heuristic (`CLAIMISH_MARKERS`) so the migration uses the same approximation already present in tooling
- manually review the candidate list before editing; only keep notes whose titles are truth-apt propositions, not topic labels or artifact names
- when editing, merge into existing `traits:` lists and de-duplicate rather than replacing the list

This is a corpus migration, not a semantic inference in tooling. The goal is to make the existing title-as-claim convention explicit in frontmatter before review gating depends on it.

### 3.3 Add `definition` trait to definition notes

Add `definition` to `traits:` for every note in `kb/notes/definitions/`.

Migration rule:

- merge into the existing `traits:` list rather than replacing it
- de-duplicate if `definition` is already present

### 3.4 Add `has-comparison`, `has-external-sources` traits

Make this a deterministic corpus migration:

- preserve all existing occurrences of `has-comparison` and `has-external-sources`
- for every `kb/notes/related-systems/*.md` note, add `has-comparison`
- for every `kb/notes/related-systems/*.md` note, add `has-external-sources`
- do not remove `has-implementation`; preserve it where already present
- merge into existing `traits:` lists and de-duplicate rather than replacing the list

Rationale: related-system reviews are structurally comparative and are grounded in external repositories, docs, papers, or products by definition. The migration should encode that invariant directly instead of relying on per-note judgment calls.

## Phase 4: Review integration

### 4.1 Add a shared note-aware gate applicability helper

Do **not** put note-aware filtering directly into the current `resolve_to_gate_ids(args, gates_dir)` interface. That function only expands requested gate ids/bundles and does not know which note is under review.

Instead, split gate resolution into two steps:

- requested gate expansion: bundle name → gate ids
- note-aware applicability filtering: `(note_path, gate_ids)` → applicable gate ids

Implement the second step in a shared helper in `resolve_gates.py` that:

- reads gate frontmatter for `requires_trait`
- reads note frontmatter for `traits`
- excludes non-applicable trait-gated gates

Use this helper from both:

- `create_review_run.py` / `run_review_bundle.py` for direct note-local bundle runs
- `review_target_selector.py` inside its per-note selection loop for sweeps

This keeps one applicability rule for both execution paths while preserving note-dependent filtering.

### 4.2 Expand review sweep note discovery to recurse under `kb/notes/**`

Update `review_target_selector.py` to discover frontmatter-bearing notes recursively, not just top-level `kb/notes/*.md`.

Without this, trait-gating parity checks for definitions and related-system reviews are misleading because those notes are currently outside sweep scope.

### 4.3 Write `frontmatter/title-as-claim` gate

New gate: checks that the title is a proposition (not a topic label). Requires trait: `title-as-claim`.

### 4.4 Update existing gates

Add `requires_trait: title-as-claim` to:
- `frontmatter/claim-strength`
- `frontmatter/title-composability`
- `semantic/explanatory-reach`

### 4.5 Verify review parity

Run selector on a representative set of notes. Check that trait-gated gates no longer fire for notes without the trait (indexes, definitions, related-system reviews), and that direct note-local bundle runs resolve the same applicable gates as sweeps for the same note.

## Phase 5: Cleanup

### 5.1 Remove semantic checks from `/validate` skill

If `/validate` still has soft-oracle checks (description quality, composability), remove them. Validation is purely structural.

### 5.2 Update documentation

- `AGENTS.md` — update type routing table, type routing section
- `kb/instructions/WRITING.md` — update type/trait guidance
- `kb/notes/document-classification.md` — update taxonomy
- `types/note.md` — update traits section with new trait vocabulary
- Move `012-types-for-structure-traits-for-review.md` to `kb/notes/adr/`, set status to `accepted`

### 5.3 Update workshop notes that this contradicts

Per [design.md](./design.md), this design revises:
- `document-types-should-be-verifiable.md` — types are now purely structural (strengthened)
- `directory-scoped-types-are-cheaper-than-global-types.md` — directories scope lookup, not identity
- `deterministic-validation-should-be-a-script.md` — soft-oracle tier removed

## Order dependencies

```
1.1 ─→ 1.2 ─→ 2.1 ─→ 2.2 ─→ 2.3 ─→ 2.4
1.3 ─→ 1.4                    ↓
                              3.1 ─→ 3.2 ─→ 4.1 ─→ 4.2 ─→ 4.3 ─→ 4.4 ─→ 4.5
                              3.3 ───────────────↗                                   ↓
                              3.4 ───────────────↗                             5.1 ─→ 5.2 ─→ 5.3
```

Phase 3 (traits) depends on phase 2 (resolver) because the validator has a hard-coded `VALID_TRAITS` set — adding new traits before the validator accepts them would cause warnings. Phase 2.3 (integrate resolver) should also update `VALID_TRAITS` or replace it with dynamic trait discovery. Phase 4 (review integration) depends on phase 3 because review applicability should operate on the migrated explicit frontmatter traits, not on implied traits that do not exist in tooling yet. Phase 5 (cleanup) comes last.

---

Workshop context:

- [design.md](./design.md) — the design this plan implements
- [type-resolver.md](./type-resolver.md) — resolver algorithm and YAML schema
- [review-integration.md](./review-integration.md) — gate applicability and selector changes
- [decision-criteria.md](./decision-criteria.md) — type vs trait boundary test

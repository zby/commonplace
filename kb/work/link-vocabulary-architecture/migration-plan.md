# Migration plan: land the link-vocabulary-architecture workshop

> Workshop draft. Concrete steps for folding this workshop into the library as one coordinated bundle.

## Scope

Fold:
- Two new ADRs (architecture; theoretical-default additions).
- `links-as-possibility.md` → `kb/notes/` with a claim-shaped title.
- `link-vocabulary.md` → `kb/reference/link-vocabulary.md`.
- Four `*-COLLECTION.md` drafts → replace existing library `COLLECTION.md` files.
- `cp-skill-connect/SKILL.md` rewritten per `connect-skill-design.md`.
- `cp-skill-write/SKILL.md` updated per `write-skill-design.md`.

Retire:
- `kb/reports/collection-topology.md` (compiled matrix, obsolete under per-destination).
- `kb/instructions/cp-skill-compile-collections/` (its only consumer retires).
- Corresponding entries in `src/commonplace/cli/init_project.py` (scaffold + promoted-skills lists) and the matching assertion in `test/commonplace/cli/test_init_project.py`.

Retain:
- `kb/reports/link-vocabulary.md` — frozen audit snapshot, evidence for ADR 020.
- `kb/notes/definitions/register.md` — already extended in place, stays.

## Phase 0 — Pre-flight

1. Confirm workshop is in the target shape (README.md, link-vocabulary.md, four COLLECTION.md drafts, connect-skill-design.md, write-skill-design.md, adr-018-draft.md, label-audit.md, links-as-possibility.md, findings.md).
2. Check remaining consumers of the artifacts scheduled for retirement. Scope is the **whole repo**, not just `kb/`:
   ```
   rg -l "collection-topology|cp-skill-compile-collections" . \
     --glob '!kb/work/link-vocabulary-architecture/**' \
     --glob '!related-systems/**'
   ```
   Expected active consumers/current-behaviour docs (all updated during Phase 7):
   - `kb/instructions/cp-skill-connect/SKILL.md`
   - `kb/instructions/cp-skill-compile-collections/SKILL.md`
   - `kb/reference/collections-and-types.md`
   - `kb/instructions/example-onboard-second-brain.md`
   - `src/commonplace/cli/init_project.py` (SCAFFOLD_FILES, PROMOTED_SKILLS)
   - `test/commonplace/cli/test_init_project.py`
   Expected generated or historical matches:
   - generated indexes such as `kb/reference/dir-index.md` and `kb/instructions/dir-index.md` (regenerated in Phase 9)
   - historical ADR context such as `kb/reference/adr/018-types-are-path-references-to-instruction-docs.md` (check for misleading wording; no rewrite required if clearly historical)
   - workshop inventories such as `kb/work/write-type-resolver/inventory.md` (leave as historical inventory unless the workshop is otherwise being revised)
3. Branch for the fold: `git checkout -b link-vocabulary-fold`.

## Phase 1 — ADRs

Two new ADRs land together. Neither supersedes an existing ADR, though both extend ADR 009 and ADR 017.

**ADR 019: Collection-owned link vocabulary with per-destination outbound rules.**

- File: `kb/reference/adr/019-collection-owned-link-vocabulary.md` (slug TBD).
- Source material: workshop README.md key moves (1–5), links-as-possibility.md (theoretical grounding), label-audit.md (reader-need justifications), connect-skill-design.md and write-skill-design.md (consumer implications).
- Status on land: `proposed`; flip to `accepted` when all phases land and validation passes.
- Extends ADR 017 (`collection-md-is-the-register-convention-boundary`) by specifying the internal structure of the outbound linking conventions COLLECTION.md owns.

**ADR 020: Theoretical-default additions — contrasts and mechanism; directional asymmetry.**

- File: `kb/reference/adr/020-theoretical-default-contrasts-mechanism.md` (slug TBD).
- Source: `adr-018-draft.md` verbatim, renumbered from 018 → 020, with internal paths updated from workshop-relative to library-relative.
- Extends ADR 009; depends on ADR 019's architecture for scoping.

After ADR creation, delete `adr-018-draft.md` from the workshop.

## Phase 2 — Promote `links-as-possibility.md` to `kb/notes/`

Mandatory before Phase 3 so `link-vocabulary.md` can reference its final library path directly.

- New path: `kb/notes/links-encode-conditional-possibilities-not-obligations.md` (or similarly claim-shaped).
- Add frontmatter: `description` (≥50 chars, retrieval-oriented), `type: kb/types/note.md`, `traits: [title-as-claim]`, `tags: [learning-theory]` (candidate), `status: current`.
- Path rewrites inside:
  - `../../notes/definitions/register.md` → `./definitions/register.md`
  - `./label-audit.md` → drop the reference; the label-audit content is absorbed into ADR 019.
- Add a Relevant Notes section with at least: `register` definition, ADR 019.

Delete `links-as-possibility.md` from the workshop after promotion.

## Phase 3 — Land `link-vocabulary.md`

Move `kb/work/link-vocabulary-architecture/link-vocabulary.md` → `kb/reference/link-vocabulary.md`.

**Mechanism:** write the new library file with the workshop content, then delete the workshop copy (rather than `git mv` onto a non-existent target — this is simpler). Add descriptive-register frontmatter: `description`, `type: kb/types/note.md`, `status: current`.

**Path rewrites inside `link-vocabulary.md`:**

| workshop path | library path |
|---|---|
| `../../notes/definitions/register.md` | `../notes/definitions/register.md` |
| `../../instructions/cp-skill-connect/SKILL.md` | `../instructions/cp-skill-connect/SKILL.md` |
| `../../reference/adr/009-link-relationship-semantics.md` | `./adr/009-link-relationship-semantics.md` |
| `./adr-018-draft.md` / `../link-label-audit/adr-018-draft.md` (any mention) | `./adr/020-theoretical-default-contrasts-mechanism.md` |
| `./links-as-possibility.md` | `../notes/links-encode-conditional-possibilities-not-obligations.md` (new path from Phase 2) |

## Phase 4 — Replace COLLECTION.md files

For each of the four proposed COLLECTION.md drafts, replace the existing library COLLECTION.md's contents rather than `git mv` over it — this keeps the library file's git blame/history clean and avoids overwrite awkwardness.

Mechanism per file:

1. Copy draft contents into the library file:
   ```
   cp kb/work/link-vocabulary-architecture/<name>-COLLECTION.md kb/<collection>/COLLECTION.md
   ```
2. Strip the delta-note blockquote at the top (workshop meta-commentary, not for the library).
3. Update the `register` gloss link path:
   - `kb/notes/COLLECTION.md`: `../../notes/definitions/register.md` → `./definitions/register.md`
   - `kb/reference/COLLECTION.md`: `../../notes/definitions/register.md` → `../notes/definitions/register.md`
   - `kb/instructions/COLLECTION.md`: `../../notes/definitions/register.md` → `../notes/definitions/register.md`
   - `kb/agent-memory-systems/COLLECTION.md`: `../../notes/definitions/register.md` → `../notes/definitions/register.md`
4. Delete the workshop draft:
   ```
   rm kb/work/link-vocabulary-architecture/<name>-COLLECTION.md
   ```

No other paths inside the COLLECTION.md files should need updating — by design, they're internally self-contained (no outbound pointers to `link-vocabulary.md` or other workshop docs after the earlier cleanup).

## Phase 5 — Rewrite `cp-skill-connect/SKILL.md`

Follow [`connect-skill-design.md`](./connect-skill-design.md). Key changes:

- Remove the read of `kb/reports/collection-topology.md`.
- Add: read source `COLLECTION.md`; enumerate outbound destination blocks.
- Per destination: apply search guidance, prospect, articulation test, label from authorised set.
- Add **Reverse-edge candidates** and **Off-authorisation candidates** as first-class report sections.
- Honour `kb/instructions/COLLECTION.md`'s frontloading posture when the source is an instruction (narrow outbound; no `see-also` sprays to other collections).

Verify: run the skill on a pilot note (suggest: `kb/notes/axes-of-artifact-analysis.md`) and inspect the report.

## Phase 6 — Update `cp-skill-write/SKILL.md`

Follow [`write-skill-design.md`](./write-skill-design.md). Targeted edits:

1. Step 2 (Load Collection Conventions) — reframe: COLLECTION.md now owns per-destination outbound rules; no other linking doc to consult.
2. Step 4 (Search Before Writing) — extend: apply each destination block's search guidance when prospecting for outbound links.
3. Universal Mechanics → Links — rewrite: keep position guidance and articulation test; remove the embedded five-label list; point at `COLLECTION.md` for authorised labels + reader-needs per destination.

Verify: write a pilot note and confirm writer path consults only `COLLECTION.md`.

## Phase 7 — Retire obsolete artifacts (library + package)

### 7a. Library artifacts

1. Delete `kb/reports/collection-topology.md`.
2. Delete `kb/instructions/cp-skill-compile-collections/` (directory and `SKILL.md`).

### 7b. Package + tests

3. `src/commonplace/cli/init_project.py`:
   - Remove `kb/reports/collection-topology.md` from `SCAFFOLD_FILES`.
   - Remove `cp-skill-compile-collections` from `PROMOTED_SKILLS`.
4. `test/commonplace/cli/test_init_project.py`: update the assertion that expects the topology report to be installed.
5. Run tests: `uv run pytest test/commonplace/cli/test_init_project.py` — expect green.

### 7c. Reference sweep

6. Update active reference docs that describe the retired topology/compile path as current behaviour:
   - `kb/reference/collections-and-types.md`: replace the compiled topology / compile skill model with the new live `COLLECTION.md` per-destination model used by write/connect.
   - `kb/instructions/example-onboard-second-brain.md`: remove the `/cp-skill-compile-collections` step; new collection setup should say that `COLLECTION.md` destination blocks are consumed directly by write/connect.

7. Search for lingering references in active code/docs:
```
rg -l "collection-topology|cp-skill-compile-collections" . \
  --glob '!kb/work/link-vocabulary-architecture/**' \
  --glob '!related-systems/**'
```

Expected after deletion: **no active references**. ADRs (019, 020, 009/017, or 018-types) that mention the retired artifacts in a Context, Scope, or Consequences section are acceptable historical references; update them only if the narrative becomes misleading. Generated indexes are refreshed in Phase 9. Workshop inventories may retain historical paths. If any file outside ADRs, generated indexes, or historical workshop inventories still has an active reference (imports, docstrings, instructions, or reference docs describing current behaviour), update it in the same commit as the deletion.

## Phase 8 — Close workshop

Delete workshop-only files:
- `README.md`, `connect-skill-design.md`, `write-skill-design.md`, `label-audit.md`, `migration-plan.md` (this file), `findings.md`.

Files that should already be gone by this point: `link-vocabulary.md` (moved in Phase 3), four `*-COLLECTION.md` drafts (replaced in Phase 4), `adr-018-draft.md` (renumbered and moved in Phase 1), `links-as-possibility.md` (promoted in Phase 2), `linking-conventions.md` + `extract_labels.py` (deleted earlier in workshop lifecycle).

When empty, remove the workshop directory:
```
rm -rf kb/work/link-vocabulary-architecture/
```

Remove the entry from `kb/work/README.md` "Active Workshops" list.

## Phase 9 — Validation

1. `commonplace-refresh-indexes` — regenerate `dir-index.md` files, tag indexes.
2. `commonplace-validate kb/notes/ kb/reference/ kb/instructions/ kb/agent-memory-systems/` — structural checks.
3. `uv run pytest` — full test suite (covers `test_init_project.py` and any other affected tests).
4. Spot-check link-following: open each migrated `COLLECTION.md` and `kb/reference/link-vocabulary.md`; verify the `register` gloss link resolves and the promoted `links-encode-...` note is reachable.
5. Pilot the rewritten skills:
   - `cp-skill-connect` on a note from each of the four collections; verify reports render all expected sections (Connections Found, Bidirectional Candidates, Reverse-edge candidates, Off-authorisation candidates).
   - `cp-skill-write` on a new note in `kb/notes/`; verify the writer consults only `COLLECTION.md` (not `link-vocabulary.md`).

## Commit strategy

Single branch (`link-vocabulary-fold`), logical commits for reviewability:

1. `add: ADR 019 collection-owned link vocabulary architecture`
2. `add: ADR 020 theoretical-default additions (contrasts, mechanism)` — renumber from workshop draft.
3. `promote: links-as-possibility to kb/notes/ claim-shaped note`
4. `add: kb/reference/link-vocabulary.md authoring catalogue` — from workshop.
5. `replace: per-destination COLLECTION.md for notes/reference/instructions/agent-memory-systems` — one commit per file or combined.
6. `rewrite: cp-skill-connect for per-destination discovery`
7. `update: cp-skill-write to defer linking to COLLECTION.md`
8. `retire: collection-topology report, compile-collections skill, scaffold/promoted-skills entries, test assertion`
9. `close: link-vocabulary-architecture workshop` — deletes workshop directory, updates `kb/work/README.md`.

Each commit should ideally pass `commonplace-validate` and `uv run pytest`; combined validation runs at the end (Phase 9). If a mid-bundle commit can't pass independently (e.g., the skill rewrites before the underlying COLLECTION.md lands), sequence them so the dependency order in the plan is also the commit order.

## Rollback

Single-branch strategy makes rollback straightforward: `git checkout main` without merging. Individual phases can be reverted by reverting their commits in reverse order.

## Post-fold follow-ups (not part of the bundle)

- Audit other skills (`cp-skill-revise`, review skills) for embedded linking vocabulary that should also defer to `COLLECTION.md`.
- Consider whether the connect skill's Reverse-edge candidates section needs tooling support beyond what model interpretation handles.
- Revisit open questions flagged in `link-vocabulary.md` after a period of real use (derived-from vs evidence, supersedes scoping, catalogue organisation).

## What this plan does not cover

- Migration of existing link labels in the corpus. Backward-compatibility for pre-revision labels (e.g., `foundation` as alias of `grounds`, pre-revision cross-register labels) is out of scope; a corpus sweep would be a separate workshop if needed.
- Review-system, validation-rule, or other skill changes beyond the two skills named.

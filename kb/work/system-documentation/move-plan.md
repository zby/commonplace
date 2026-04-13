# Collection move plan

**Status: complete.** All sub-efforts have landed. The `kb/reference/` collection exists, ADRs have moved, the two wholesale system-doc candidates are in place, the five splits are tracked in [split-plan.md](./split-plan.md), entry-point and navigation changes are live, install scaffolding ships the collection, and hardcoded path fixups are done. The tooling prerequisite was resolved by extracting the logic into `commonplace.lib.relocation` with cross-collection support.

Concrete plan for moving system-specific content out of `kb/notes/` into a new `kb/reference/` collection. Follows on from [framing.md](./framing.md), which explored the problem space; this plan records the decisions made and lays out the sub-efforts.

## Decisions

1. **New collection `kb/reference/`** — sibling of `kb/notes/`, `kb/sources/`, `kb/tasks/`, `kb/work/`, `kb/instructions/`. Holds content that describes this specific commonplace system: current state, architecture, and decision history.

2. **Name is `reference/`, not `system/` or `docs/`.** `reference/` names the genre (information-oriented, descriptive, lookup-shaped) rather than the subject, which transfers better to installed projects and contrasts cleanly with `notes/` (theory) and `instructions/` (how-to). `docs/` is redundant with the mkdocs site as a whole; `system/` is overloaded in this KB.

3. **Uses the existing `note` type** — no new `system-doc` type at first (YAGNI). If review or staleness pressures later justify a dedicated type with its own schema and gates, it can be added then.

4. **ADRs move with the collection** — `kb/notes/adr/` → `kb/reference/adr/`. ADRs are system-specific by nature (they record decisions about *this* system), so they belong in `reference/` rather than `notes/`. The `adr` type template, instructions, and schema move to `kb/reference/types/`.

5. **`kb/notes/` collapses toward theory-only** — after the move, the rule is: *"if we renamed a type or restructured a directory tomorrow, would this file need to change?"* Yes → belongs in `reference/`. No → stays in `notes/`.

6. **Per-note scope signal is deferred** — the question of whether individual notes carry `scope: general | pattern | local` (see framing.md options A–D) is a separable sub-effort. Moving the clearly system-specific content first doesn't commit either way.

## Target layout

```
kb/reference/
    README.md              ← entry point: "how commonplace works today"
    architecture.md        ← from kb/notes/commonplace-architecture.md
    type-system.md         ← from kb/notes/document-classification.md
    …                      ← more as the audit finds them
    adr/                   ← moved wholesale from kb/notes/adr/
        002-…md  …  016-…md
    types/
        adr.template.md        ← from kb/notes/types/
        adr.instructions.md
        adr.schema.yaml
```

Three-way contract between top-level collections:

| Collection | Genre | Question it answers |
|---|---|---|
| `kb/notes/` | Claims and theory | *Is this true? Does it transfer?* |
| `kb/reference/` | Current-state description + decision history | *How does our system work, and why?* |
| `kb/instructions/` | Imperative how-to (skills, procedures) | *How do I do X?* |

## Tooling prerequisite: extend `commonplace-relocate-note` — done

All per-file moves in this plan use `commonplace-relocate-note` (`src/commonplace/cli/relocate_note.py`). The script handles git mv, rewriting inbound links across the repo, rebasing outbound links from the moved file, and updating mkdocs redirects — everything the earlier "update inbound/outbound links" bullets would otherwise have had to do manually.

**Resolved**: the logic was extracted into `commonplace.lib.relocation` (commit `458d971`) with `kb_root` parameterised instead of a hardcoded `NOTES_ROOT`. A note can now be moved from any path under `kb/` to any other path under `kb/`, including cross-collection moves like `kb/notes/foo.md → kb/reference/foo.md`. The CLI wrapper accepts the same `--to` syntax with no additional flags. A dedicated test (`test_relocate_note_apply_moves_note_across_kb_collections`) exercises the cross-collection scenario and passes alongside the rest of the relocate-note test suite.

## Sub-efforts

These are decoupled — each can land independently.

### 1. Create the collection and move ADRs (mechanical)

Almost entirely find-replace. Can land first.

**Directory and ADR move:**

ADRs move one at a time via `commonplace-relocate-note` once the prerequisite extension lands. Each invocation handles the git mv, inbound link rewrites across the repo, outbound link rebase, and mkdocs redirect in one pass.

- [x] `mkdir -p kb/reference` and `mkdir -p kb/reference/types` (the script handles parent dirs on move, but the collection root should exist before the first invocation)
- [x] Move each ADR into `kb/reference/adr/` (landed manually with `git mv` plus repo-wide link rewrites and index refresh; the planned `commonplace-relocate-note` extension is still open as tooling cleanup)
- [x] Move the `adr` type files (these aren't notes, so they're a plain `git mv` — the script only handles files under a collection root):
      `git mv kb/notes/types/adr.template.md kb/reference/types/adr.template.md` (and `.instructions.md`, `.schema.yaml`)
- [x] Manually check workshop docs referenced by the script (it updates `*.md` under the repo root, so `framing.md` and `practitioner-contract.md` should already be covered, but verify)
- [x] Rebuild indexes that cite ADRs (`document-system-index.md`, `architecture-index.md`) — inline link rewrites should be handled by the script, but index prose referring to "ADRs in `kb/notes/adr/`" needs manual update
- [x] Verify `git log --follow kb/reference/adr/NNN-…` preserves history per file

**Declare the collection to tooling and docs:**

- [x] Add `reference` collection to live `qmd-collections.yml` (same shape as `notes`, pointing at `kb/reference`)
- [x] Add `reference` collection to `src/commonplace/assets/qmd-collections.yml` (the template that ships with the package)
- [x] Update live `AGENTS.md`:
  - [x] Add `kb/reference/` to the `rg` examples under `## Using the KB`
  - [x] Add an entry for `kb/reference/README.md` (once written) to `## Key Indexes`
  - [x] Short prose paragraph or table row distinguishing `notes/` (theory) from `reference/` (current-state + decisions) from `instructions/` (how-to), mirroring the three-way contract in this plan
- [x] Update `AGENTS.md.template` (the resolved decision is that the framework **does** ship `kb/reference/` as an installed collection, serving as the practitioner's system-documentation collection):
  - [x] Add `kb/reference/` to the `rg` examples under `## Using the KB`
  - [x] Add a placeholder entry in `Key entry points` for `kb/reference/README.md`
  - [x] Add a short three-way-contract paragraph mirroring the live `AGENTS.md`: `kb/notes/` for transferable claims, `kb/reference/` for current-state + decision history of the practitioner's own system, `kb/instructions/` for how-to
- [x] Update install scaffolding so `commonplace-init` creates `kb/reference/` in practitioner projects:
  - [x] Add `Path("kb/reference")` and `Path("kb/reference/types")` to `DEFAULT_DIRS` in `src/commonplace/cli/init_project.py`
  - [x] Add `("kb/reference", "kb/reference")` to `SCAFFOLD_TREES` so scaffold content under `kb/reference/` gets copied
  - [x] Create `src/commonplace/scaffold/kb/reference/types/adr.{template.md,instructions.md,schema.yaml}` by pointing the scaffold at the live `kb/reference/types/` files (so practitioners get the current ADR type preloaded and scaffold packaging stays in sync)
  - [x] Create a starter `src/commonplace/scaffold/kb/reference/README.md` — a short placeholder the practitioner fills in (*"Current-state documentation for this project's system. Describe how your KB is organized, which conventions you've chosen, and link to ADRs."*). Not to be confused with the commonplace-specific `kb/reference/README.md` written in sub-effort 5, which describes commonplace itself.
  - [x] Add a test under `test/` that runs `init_project` against a temp root and asserts `kb/reference/`, `kb/reference/types/`, and the scaffold files are present
- [x] Update mkdocs nav — add `reference/adr/` to `Browse` or a new `Reference` group
- [x] Run `commonplace-validate` to catch missed links

**Deferred**: auditing hardcoded ADR paths in skills, scripts, and `src/commonplace/` beyond the files listed above (see sub-effort 6).

### 2. System-doc audit (judgment)

Apply the restructuring test to `kb/notes/*.md`:

> *If we renamed a type or restructured a directory tomorrow, would this file need to change?*

Yes → candidate for `kb/reference/`. No → stays in `notes/`.

Candidate list:

| Source | Target | Justification | Status |
|---|---|---|---|
| `kb/notes/document-classification.md` | `kb/reference/type-system.md` | Describes the current type inventory and migration state; would need rewriting if types or schemas change | done |
| `kb/notes/commonplace-architecture.md` | `kb/reference/architecture.md` | Describes the repo's current directory layout and operational surface | done |
| `kb/notes/directory-scoped-types-are-cheaper-than-global-types.md` | `kb/reference/type-loading.md` (split) | The economic argument for directory-scoped loading transfers, but the current-implementation section and concrete path claims are specific to Commonplace's present type layout | proposed-split |
| `kb/notes/generate-instructions-at-build-time.md` | `kb/reference/instruction-generation.md` (split) | The build-time-vs-runtime-parameterisation principle transfers, but the current Commonplace skill/task generation scheme and path examples are local | proposed-split |
| `kb/notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md` | `kb/reference/control-plane-goals.md` (split) | The control-plane argument for always-loaded KB goals transfers, but the AGENTS template contract and install-time guidance are specific to the current Commonplace scaffold | proposed-split |
| `kb/notes/scenario-decomposition-drives-architecture.md` | `kb/reference/scenario-architecture.md` (split) | The scenario-decomposition method transfers, but the commonplace-vs-installed-project split, escalation path, and current test-scenario artifacts are local | proposed-split |
| `kb/notes/files-not-database.md` | `kb/reference/storage-architecture.md` (split) | The general files-vs-database argument transfers, but the current commonplace storage boundary, qmd-derived indexes, and SQLite review exception are system-specific and should be split into reference | proposed-split |

Borderline cases to weigh during the audit:

- `files-not-database.md` — general principle, or current-state (we chose files)?
- `backlinks.md` — needs reading
- `linking-theory.md` — needs reading
- Index files (`document-system-index.md`, `architecture-index.md`, `document-system-index.md`) — these point at both theory and ADRs; may need rewriting rather than moving
- Any note whose title is descriptive-not-claim is a mild hint it's reference-shaped rather than theory-shaped

Audit output: extend the table above with the full candidate list before sub-effort 3 starts.

Current judgment on the explicit borderline set:

- `files-not-database.md` should be split — keep the transferable files-vs-database argument in `kb/notes/`, and extract the current commonplace storage boundary and scoped SQLite review exception into `kb/reference/storage-architecture.md`.
- `backlinks.md` stays in `kb/notes/` — it is a general design-space note about inbound-link visibility, not a description of a current commonplace subsystem.
- `linking-theory.md` stays in `kb/notes/` — it is explicitly trying to ground link practices under a transferable theory, not document current state.
- `architecture-index.md` and `document-system-index.md` stay in `kb/notes/` and should be rewritten in place as mixed navigation pages linking theory notes to reference docs/ADRs.

Split judgment on the current candidate set:

- `document-classification.md` should move wholesale — it is already a current-state taxonomy and migration summary rather than a theory note.
- `commonplace-architecture.md` should move wholesale — it is a repo-layout snapshot with no real transferable core once the local paths are removed.
- `directory-scoped-types-are-cheaper-than-global-types.md` should split — keep the general loading-economy argument in `kb/notes/`, extract the "Current implementation" path-specific material into `kb/reference/type-loading.md`.
- `generate-instructions-at-build-time.md` should split — keep the general frontloading/build-time-generation argument in `kb/notes/`, extract the current Commonplace generation/config pattern into `kb/reference/instruction-generation.md`.
- `kb-goals-in-always-loaded-context-guide-inclusion-decisions.md` should split — keep the general claim that goals belong in always-loaded control-plane context in `kb/notes/`, extract the current scaffold/template/install contract into `kb/reference/control-plane-goals.md`.
- `scenario-decomposition-drives-architecture.md` should split — keep the general method of deriving architecture from user-story decomposition in `kb/notes/`, extract the current commonplace-vs-installed-project architecture and scenario measurement surface into `kb/reference/scenario-architecture.md`.

### 3. Candidate list review gate (hard stop) — done

Before any system-doc moves happen, the agent produces the full candidate list from sub-effort 2 — the complete set of notes proposed for moving, with target path and one-line justification per row — and presents it to the user for revision. No `git mv` runs until the user approves the list.

The user may:

- Approve rows as-is
- Edit target paths or names
- Reject rows (they stay in `kb/notes/`)
- Add rows the audit missed
- Split the list into batches to land separately

The approved list is frozen into the table in sub-effort 2 with `approved` in the status column, and becomes the work queue for sub-effort 4.

This gate is a hard stop because each row is a judgment call: "is this system-specific, or general theory?" The agent's audit is a starting proposal, not a decision. The gate also applies to any later additions — if the audit misses notes that turn up during a move, they get added to the list and re-approved, not silently moved.

**Resolved**: the review gate was exercised when the sub-effort 2 candidate list was reviewed, splits were separated out into their own plan, and the two wholesale candidates (`document-classification.md` and `commonplace-architecture.md`) were approved for direct move. The five split candidates landed via the approved [split-plan.md](./split-plan.md).

### 4. System-doc moves (after approval) — done

For each approved candidate:

- [x] Run `commonplace-relocate-note kb/notes/OLD.md --to kb/reference/NEW.md` (dry-run, then `--apply`) — handles git mv, inbound/outbound link rewrites, and mkdocs redirect in one pass
- [x] Update frontmatter if needed (remove `title-as-claim` trait; keep `type: note`; adjust title if the file was renamed to a descriptive form)
- [x] Verify the script's reported link updates look right in the dry-run output before applying
- [x] Run `commonplace-validate` as a belt-and-braces check
- [x] Mark the row `done` in the sub-effort 2 table

The wholesale moves (`document-classification.md → type-system.md`, `commonplace-architecture.md → architecture.md`) landed via the relocation library, and the five split candidates landed via [split-plan.md](./split-plan.md). All rows in the sub-effort 2 candidate table are marked `done`.

### 5. Entry point and navigation

- [x] Write `kb/reference/README.md` — one-page tour of what's in the collection; links to `architecture.md`, `type-system.md`, ADR index
- [x] Add a `Reference` group to mkdocs nav with the key pages and the ADR index
- [x] Update `kb/notes/tags-index.md` to cross-link `reference/` where appropriate, or note that `reference/` has its own entry point

### 6. Hardcoded path fixups (deferred cleanup)

After the directory move is stable, audit for hardcoded paths:

- [x] Search for `notes/adr` across `src/`, `skills/`, `kb/instructions/`, and agent-facing docs
- [x] Search for `kb/notes/adr` across the whole repo
- [x] Fix any live tooling/docs that still assumed ADRs live under `notes/`

This can wait until after #1 lands and smoke-test reveals any broken tooling.

## Sequencing

0. **Tooling prerequisite**: extend `commonplace-relocate-note` to accept collection roots other than `kb/notes/`, with a dry-run test against one ADR
1. **Create the collection and move ADRs** (sub-effort 1, mechanical, low risk, high clarity win) — ship next, including qmd and AGENTS.md updates
2. **System-doc audit** (sub-effort 2) — agent proposes the full candidate list in one sitting
3. **Review gate** (sub-effort 3) — user revises and approves the candidate list; hard stop before any moves
4. **Entry point `kb/reference/README.md` + starter system-docs** (`architecture.md`, `type-system.md`) — ship as a small batch once those two rows are approved
5. **Remaining system-doc moves** (sub-effort 4) — batch by theme from the approved list
6. **Hardcoded path fixups** (sub-effort 6) — after everything lands

## Deferred / out of scope for this plan

- Per-note scope signal (framing.md options A–D)
- Broader practitioner-contract decisions about what gets installed vs. what stays in `commonplace/` (covered in `practitioner-contract.md`); this plan only resolves two specific questions: (1) `kb/reference/` ships as an installed collection, and (2) the `adr` type is therefore effectively promoted from "local (ours)" to "core" status, since it ships with the installed scaffold
- A dedicated `system-doc` type with its own schema and review gates
- Whether `kb/instructions/` itself should be renamed or reorganized

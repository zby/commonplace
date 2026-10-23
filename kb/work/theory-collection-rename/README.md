# Rename the notes collection to Theory

Posed by the operator on 2026-10-22, after the site menu was trimmed to
Agentic Systems, Reference and the other collections.

## Current execution status

The full source/library rename is implemented under
[ADR 123](../../reference/adr/123-theory-names-the-commonplace-library-collection.md).
This KB and the shipped library use Theory; consuming projects keep their soft
Notes scaffold and customized collections. The complete 1,437-test suite, site
redirect acceptance and all six isolated installed-project stages pass. The
[execution record](./execution.md) names commits, preservation checks and the
remaining residual audit and closeout. Do not release before that closeout.

The original framing, inventories and questions below are planning history,
not unresolved authority gates. In particular, their original suggestion to
scaffold Theory was superseded: init keeps Notes. Actual execution counts and
operator decisions are in the execution record and ADR, not the pre-sort counts.

## Goal

Rename the collection now at `kb/notes/` to **Theory**, so its name states its
role beside Reference (Commonplace's selections and their state) and
Instructions (procedures). Its README already calls it "the theory collection",
and [content routing](../../reference/content-routing.md) already routes
"theory: the reader reasons with it" there. The `note` type keeps its name:
the collection is the theory, its members are notes.

## Operator decisions

- Rename the collection to Theory (2026-10-22). Depth (label only or the
  directory too) is decided here, not yet.
- The operator is inclined toward a full rename and requested a complete
  implementation inventory before deciding. Preparation does not authorize
  the rename or settle migration and frozen-record policy.
- Leaning towards the full rename (2026-10-22); see [plan](./plan.md).
- **Runtime code must be collection-independent.** The operator approved
  revising the plan to remove unnecessary Notes-specific runtime assumptions,
  not replace them with Theory-specific ones. Build/scaffold manifests still
  declare the shipped layout. Operation scope and eligibility need explicit
  decisions; discovering a collection does not make it eligible for every
  operation.
- The operator confirmed collection-type work was complete and authorized
  runtime hardwiring removal. Track 1 now uses explicit scopes; the
  [execution status](./hardwired-collections-plan.md#execution-status) records
  interfaces, verification and retained policy exceptions. Track 1 is committed
  as `43a98d836`. This does not authorize the collection rename.
- The unquoted-source bound is collection-owned, through
  `unquoted-source-limit` ([ADR 122](../../reference/adr/122-collections-set-the-unquoted-source-limit.md),
  commit `daed61d59`). It moves with the contract and needs no type-registration
  update. The [special collection definition](../../reference/definitions/special-collection.md)
  records intentional fixed-name roles; no root configuration is commissioned.
  Work/Tasks/proposal lifecycle design stays out of scope. Existing lifecycle
  checks remain provisional, not a compatibility contract.
- **Evidence splits by scope of inference, as a prerequisite** (2026-10-22).
  Evidence whose bounded inference keeps a free variable (a design-space
  claim, including an existence claim Commonplace witnesses) stays with the
  theory. Evidence whose inference, once Commonplace's choices are scoped,
  concerns only those fixed choices or their effects goes to
  `kb/reports/retained/`, beside the raw evidence it interprets; no new
  `kb/reference/evidence/` is created. Retained starts flat for these;
  structure comes later if the population needs it. This is the existing
  placement test of `kb/notes/COLLECTION.md` applied to evidence. Sort and
  move these before the rename.

## Implementation clarifications (2026-10-23)

- The operator authorized implementation after the plan update. The scaffold
  keeps its soft project `kb/notes/` collection; this KB and the shipped library
  become Theory.
- Inspect what a frozen record actually protects. ADRs are semantically frozen,
  not byte-frozen: repair navigational links while preserving the decision.
  Identify exact-capture and hash-pinned obligations separately rather than
  assuming all historical prose is immutable.
- Review/freshness continuity is not required. The reviews are already old and
  the operator expects a new system. Leave historical state intact without
  migrating keys or baselines; designing the replacement is separate work.

## Constraint

[ADR 116](../../reference/adr/116-one-word-per-concept-across-prose-and-code.md)
gives one concept one word on every surface and renames code first when
surfaces disagree. A "Theory" label over a `kb/notes/` path is therefore
allowed only as a recorded, temporary step of a full rename, not as an end
state.

## Starting evidence (2026-10-22)

- **Contents:** 429 Markdown files; 366 at the root. Subdirectories:
  `definitions/` (27, vocabulary), `evidence/` (17, episode records that
  support or test claims), `agent-memory-requirements/` (13), `proposals/` (3,
  "finished but unadopted theory"), `types/` (2), `research/` (1).
- **Live inbound links:** about 200 files across `kb/notes`, `kb/tags`,
  `kb/reference`, `kb/instructions`, `kb/index.md` and `AGENTS.md`.
- **Frozen inbound links:** the Agent Memory Systems reviews (159 files),
  ADRs (49), retained reports (52), reference proposals (37) and several
  workshops. Local `kb/reports/state` and `cache` hold about 18,600 more; they
  are not published.
- **Code naming the path:** `lib/project_status.py`, `lib/project_paths.py`,
  `lib/promotion.py` and `cli/promotion_candidates.py`, `cli/validate_notes.py`
  (the `notes` target), `review/review_target_selector.py` (`NOTES_ROOT`),
  `review/collection_conformance.py`; relocate command examples.
- **Scaffold:** `scaffold_manifest.py` creates `kb/notes/` and
  `kb/notes/types/` in every new KB, from `templates/user-notes-COLLECTION.md`
  and `user-notes-README.md`; other user templates mention `notes/`.
- **Declarations:** `kb/tags/COLLECTION.md` lists `notes` as a participating
  collection; `AGENTS.md`, content routing and `CLAUDE.md`'s collection table
  name `kb/notes/`; `properdocs.yml` holds 215 redirect entries from
  `notes/` paths.

## Prepared implementation inventory (historical baseline)

Read the [implementation plan](./implementation-plan.md) before executing.
It provides the decision gates, runtime/build/scaffold changes, exact file
inventories, redirect-map changes, preservation risks, consumer migration
requirements and verification coverage.

The separate [hardwired-collections removal plan](./hardwired-collections-plan.md)
owns runtime independence. It extends the Notes findings to source handling,
workshop/archive policies and tag roots; distinguishes intentional layout and
state paths; and fixes coordination with the agent typing collection specs.
Use it for the completed runtime work and its verification status; this
workshop's other plans retain the rename/migration worklist. The generic scope
refactor and collection-owned source bound were implemented at this planning
checkpoint, before the collection rename. These inventories remain pinned to
their recorded pre-sort HEAD.

The dry run moves 431 files (429 Markdown and two schemas) and would rewrite
2,119 Markdown paths, including 997 untracked local report files. It does not
repair code literals, local type pointers, schema constants or the complete
redirect map. The plan separates these from command-produced backlinks.

These are pre-sort baseline counts. The concurrently recorded evidence-sort
prerequisite above takes precedence; reconcile the move, backlink and redirect
inventories after it. The detailed implementation plan distinguishes that
recorded decision from recommendations still awaiting approval, including
consumer handling, protected records and review-state migration.

## Original decision questions

These were the initial questions. ADR 123 and the execution record supersede
their unresolved framing; they are retained to explain the preparation.

1. **Depth.** Label only (menu and README heading), or rename the directory to
   `kb/theory/` with code, scaffold and declarations. ADR 116 favours the full
   rename.
2. **`evidence/`.** Decided as above; open parts:
   - the per-file sort (which of the 17 move, which split into a local
     finding plus a general claim);
   - contracts: `kb/reports/COLLECTION.md` lists "experiment reports,
     measurements, and exact records cited by later work" under `retained/`
     but forbids broadening it into "a second notes, reference,
     instructions, or workshop collection". Local evidence moved there is
     an experiment report, not a reference description; state that in the
     reports contract, and change Reference's and the notes contract's
     routing lines to match. Moved notes need a report form (type, or plain
     text with the retained-record conventions) and their identity rules;
   - links: local evidence bears on an ADR or design document
     (`is-evidence-for` from reports), which cites it back; a later theory
     note cites it `abstracted-from`, not as corroboration;
   - existing evidence-shaped files already in `kb/reference/`
     (`harness-sub-agent-model-selection-regression.md`,
     `tag-readme-trace-as-self-improving-loop.md`) move there too or stay;
   - coupling with [decision-lifecycle-evidence](../decision-lifecycle-evidence/README.md),
     whose outcome evidence for decisions would land in the same place.
3. **`definitions/`.** Vocabulary as theory's terms: state it in the contract,
   or leave as is.
4. **Installed projects.** New KBs get Theory from the scaffold. Existing
   consumers may retain their collection names through generic runtime
   support, without a dual-name shim. Decide the library-reference upgrade
   procedure and how init refresh avoids an unwanted second collection;
   consumer-owned directory migration is optional.
5. **Frozen history.** Rewrite links in frozen collections and retained
   reports through relocation, or leave them and rely on site redirects.
6. **Decision record.** A full rename changes what ships to consuming KBs and
   needs an ADR.
7. **Runtime scope: resolved.** Status and `today`/`recent` validation require
   `--collection`; promotion takes an explicit collection; review requires
   `--note`, with `--user-verified` only a filter. The generic `notes_validation`
   status field reports its scope. ADR 122 attaches the source bound to the
   governing collection contract, not a type path. Verify these behaviors
   through the rename; do not reopen them as implicit-scope design questions.

## Boundaries

- Commit any `commonplace-relocate-*` result alone, without content edits.
- Do not edit retained analysis sets or frozen collections except through the
  relocation command's backlink rewrite, if question 5 chooses that.
- The note type, its schema and `type: types/note.md` values stay unchanged
  unless a separate decision renames them.

## What closes this workshop

The collection has one name on every surface, or a recorded decision keeps
`notes`; the ADR (if any) is accepted; the scaffold, code, declarations and
site agree; installed-project handling is decided and documented. Then remove
this directory and its Active Workshops entry.

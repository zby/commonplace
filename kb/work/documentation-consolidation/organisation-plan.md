# Organisation plan for the reference documents

Proposed by an agent (claude-fable-5-2) on 2026-11-19, from the [analysis](./reference-analysis.md) and the operator's positions recorded in [routes and skills](./routes-and-skills.md). Not adopted. Nothing here is done. The plan covers the 30 documents directly under `kb/reference/`. The subdirectories `adr/`, `proposals/`, `definitions/` and `types/` stay, by the operator's decision.

## Principle

Place each piece of content by how it reaches its reader.

1. **A rule an agent must apply** goes on a route: a skill body, a collection contract, a type spec, `AGENTS.md`, or a tool's output (`--help`, a validator message, a test).
2. **Name only the tool needed for the operation.** For example, the write instruction names `commonplace-validate` when the agent checks the document it just wrote. Command usage belongs in `--help`.
3. **What a person needs to decide whether to run something** goes in a short overview: what it does, what it may publish, what it costs, when it needs a decision.
4. **The current state that several decisions compose**, and invariants that cross components, go in a small set of architecture documents.
5. **Claims about Commonplace itself**, read by people and found by search, go in one directory of their own.

A document that serves none of these is removed, after anything unique in it has a home.

## Target layout

Thirty documents become fourteen at the top level and five in one new directory. One moves to theory evidence. Ten are merged or removed.

### Stay at the top level (14)

| Document | Change |
|---|---|
| `architecture.md` | becomes the one high-level document. It absorbs `workflow-architecture.md`, the delegation invariant and the per-installation table from `control-plane-goals.md`, and the unique lines of `instruction-generation.md`. It gains a "decision chains" section: for each area, the ADRs in force and which clauses were amended |
| `storage-architecture.md` | kept. A code error message cites one of its headings, so that heading stays |
| `review-architecture.md` | shrunk to about 100 lines: ownership rules, the state table, the freshness boundary, the guard's claim, and which clauses of ADR 127 survive. The components table and the behaviour specification go; docstrings and help own them |
| `review-and-editing-system.md` | the renamed review guide, rewritten as a person's overview of about 80 lines |
| `validation-contract.md` | kept in place; code and the analysis plan pin its path. Stale statements fixed |
| `documentation-site.md` | kept as a publishing checklist; the collection list replaced by the rule |
| `link-vocabulary.md` | shrunk to the approach and the label catalogue, for a maintainer. Its rules move to routes (below) |
| `content-routing.md` | kept; missing collections added |
| `navigation.md` | shrunk to the recipes and the source-lookup rule; future ideas removed |
| `collections-and-types.md` | absorbs `collection-prototypes.md` and `collections-never-own-frontmatter-semantics.md` as sections |
| `vocabulary-collision-ledger.md` | kept as the register; its decisions also go on a route |
| `vocabulary-unification-ledger.md` | kept |
| `design-rationale-management.md` | kept |
| `agent-memory-coverage.md` | kept and refreshed; two of its claims are out of date |

### New directory `kb/reference/worked-case/` (5)

Claims about this repository, for a human reader. The index already has a section of this name.

| Document | Kind |
|---|---|
| `commonplace-declared-frame.md` | a declaration other notes cite |
| `epistemic-stance.md` | a declaration; `AGENTS.md` names it |
| `source-adoption-policy.md` | a declared policy |
| `commonplace-as-an-instrument.md` | an assessment against the theory |
| `where-change-candidates-come-from-in-commonplace.md` | an assessment against the theory |

### Move to `kb/theory/evidence/` (1)

`tag-readme-trace-as-self-improving-loop.md`. Its two sibling notes are already there.

### Merged or removed (10)

| Document | What happens first |
|---|---|
| `commands.md` | its unique 3 to 4 kB moves into `--help`; consumers repointed (below) |
| `instruction-generation.md` | two unique points move to `architecture.md`; one claim moves to the theory note that links it |
| `control-plane-goals.md` | the delegation invariant and one table move to `architecture.md` |
| `scenario-architecture.md` | the step table moves into the theory note it instantiates |
| `workflow-architecture.md` | merged into `architecture.md` |
| `collection-prototypes.md` | merged into `collections-and-types.md` |
| `collections-never-own-frontmatter-semantics.md` | merged into `collections-and-types.md` |
| `agentic-system-analysis-design-brief.md` | its evaluation priorities move into `maintain-analysis-method.md`, which requires reading it; six links retargeted |
| `commonplace-agent-memory-gap-plan.md` | removed. This loses the eleven-step order and the done-when criteria, which nothing else records |
| `harness-sub-agent-model-selection-regression.md` | removed; ADR 067's link retargeted to the retained audit that states the lesson |

## New and changed routes

| Content | Route |
|---|---|
| running a review | new skill `cp-skill-review`, about 45 lines; it never writes a note |
| revising a note | new skill `cp-skill-revise`, about 60 lines; it may write the note |
| the review pointer in `AGENTS.md` and in `AGENTS.md.template` | removed; the skills replace it |
| stop kinds; sweep stops | merged into `continue-a-revise-pass.md` and `run-review-batches.md` |
| setting up a Pi reviewer | its own instruction |
| what each command does | `--help`: the review module's long docstring shown as help; a description on each `commonplace-analysis` subcommand; the unique points for `status`, `validate`, `promotion-candidates`, `ingest-handoff`, `task` and relocation |
| the CLI pointer in `AGENTS.md` | reads: use `--help`; `uv tool list` lists the commands |
| the lineage test | `cp-skill-write`, in its link mechanics |
| how to write a contract's outbound-links section | `kb/types/collection-contract.md` |
| the collision-ledger decisions | one line in `cp-skill-write`'s vocabulary step naming the terms to check |
| keep tags inline | `cp-skill-write` |
| editing the root delegation rule opens a search of the commissioning instructions | one clause in `AGENTS.md`, beside the rule |

## Order of work

Each phase stands alone and can be committed and stopped after. Relocations are committed alone, as the repository's git rules require.

1. **Fix the stale statements.** About 20 are listed in the analysis. No structure changes. This is useful even if nothing else is adopted.
2. **Make help carry what the command reference carries.** Add the missing descriptions. Check: for each unique item the analysis lists, the help shows it.
3. **Write the two skills** and move the guide's unique operating content into the instructions they link. Remove the `AGENTS.md` pointer. Check: a fresh agent asked to review a note, and one asked to improve a note, reach the right command and stop for the operator at the right points, without being told the skill's name.
4. **Rewrite the guide as the overview and rename it.** Check: the operator can tell from it what a run may publish, what it costs and when it needs a decision.
5. **Remove `commands.md`.** Repoint the catalogue test at the published entry points and their help. Retarget the analysis skill's two anchors to subcommand help. Give `cp-skill-health-check` another smoke-test file.
6. **Consolidate architecture.** Write the decision chains first; they are the part no other artifact holds.
7. **Put the orphan rules on routes**, then shrink `link-vocabulary.md` and `navigation.md` and do the merges into `collections-and-types.md`.
8. **Create `worked-case/`**, move the evidence note, merge the design brief, remove the plan and the incident record.
9. **Rebuild the reference index** to match, and update `properdocs.yml` redirects for the published pages that moved.

Phases 1 to 5 change what agents load and are the ones the workshop's closure test can measure. Phases 6 to 9 are tidying with a smaller effect on agents.

## How this meets the workshop's closure test

The framing asks whether an agent can find a consequential dependency without being told its name, and whether an operator can decide from the overview.

- An agent asked to review or revise a note loads a skill of about 50 lines where it loaded a 61 kB guide.
- The rules the analysis found off-route get a route.
- The operator's overview is written for the decision, not as a copy of behaviour.
- The framing's own continuation case, an editing restriction that must survive two routes, belongs in the "coordination between runs" section of `architecture.md` and in a comment beside each route in code. The plan does not otherwise test it.

Untested: whether agents doing writing tasks apply the authoring rules once they are on a route. No session trace was examined.

## Decisions for the operator

1. **How do ADRs stay usable** when later ADRs amend them: a decision-chains section in `architecture.md`, as planned, or amending the old ADR texts?
2. **One `worked-case/` directory, or two**, with the three declarations in a `declarations/` directory of their own? The plan assumes one, because five files do not need two directories.
3. **The gap plan.** Removal loses its ordering and done-when criteria. Is that accepted?
4. **The incident record.** Remove, or move to `kb/reports/retained/` to keep the job numbers?
5. **The name.** ADR 139 and the documents say "review and editing system". The operator later said "Review and Edit System". One has to be chosen before the guide is renamed.
6. **No further subdirectories.** With fourteen documents left, `architecture/` and `authoring/` directories would group four or five files each and add no route. The plan does not create them.

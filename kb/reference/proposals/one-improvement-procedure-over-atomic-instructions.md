---
description: "Proposal: replace the full pass, fix procedure and simplification passes with one improvement procedure that is mostly LLM instructions, composed as variants from typed atomic instructions, with each run a typed directory the validator checks"
type: reference/types/design-proposal.md
tags: [review-system]
---

# One improvement procedure over atomic instructions

Commonplace has three ways to improve one note after review: the full improvement pass, the fix procedure for review warnings, and the simplification passes. All three do the same thing. They review the note with some operations, choose edit operations from what the review found, apply them within bounds, review again, and stop for an operator where authority requires it. They do it from the same ingredients, atomic instructions of three kinds:

- **Review operations**: the gate criteria, and the full pass's method families (critique, compression, composition friction, premise decomposition, connect).
- **Edit operations**: the simplification passes, and the fix strategies keyed to warning kinds.
- **Stops**: strike lists, the publication approval, the hand-back dispositions.

The goal is one procedure in their place. It is flexible because it is mostly LLM instructions. It is held in shape by the infrastructure every other artifact already uses: types, schemas and `commonplace-validate`. Code stays only where batching needs it, in review.

## Current state (as of 2026-11-13)

The three procedures, as the operator meets them:

| | Full pass | Fix procedure | Simplification passes |
|---|---|---|---|
| Entry | `commonplace-review run full-pass` | agent follows [fix review warnings](../../instructions/fix-warnings/fix-review-warnings.md); no workflow command | `commonplace-review run revise` with `--assess` or `--plan` |
| Review operations used | all six method families, before editing and again at closing | the gate catalog, as fresh `warn` and `fail` results, before and after | none; code checks on each text |
| Edit operations used | the packet's body edits under `keep`, then a copyedit | the fix strategies, chosen per finding | the passes a plan names, in order |
| Stops used | hand-back dispositions; `--direction` for an undetermined update; exact publication approval | `deferred` items; the agent edits the checkout directly, so no publication boundary | strike lists for plain-wording and abstractions; exact publication approval |
| Where the operator's answer is kept | packet resolution fields with rationale, under [resolve a full-pass disposition](../../instructions/resolve-full-pass-disposition.md) | the agent's `rejected` and `deferred` statuses in the free-form fix report | the proposed list and each strike with the operator's required reason, in the run's operator record |

The atomic instructions, where they live and who uses them:

| Kind | Atom | Lives at | Used by |
|---|---|---|---|
| Review | gate criteria, in seven bundles | [review-gates/](../../instructions/review-gates/) | full pass, fix procedure, gate sweeps |
| Review | compression bundle | [compression-bundle/](../../instructions/compression-bundle/) | full pass |
| Review | critique | [critique-note](../../instructions/critique-note.md) | full pass |
| Review | composition friction, with premise decomposition | [composition-friction-gate](../../instructions/composition-friction-gate.md), [premise-decomposition-gate](../../instructions/premise-decomposition-gate.md) | full pass |
| Review | connect | [cp-skill-connect](../../instructions/cp-skill-connect/SKILL.md) | full pass |
| Edit | simplification passes, each with `effort` and preserve rules | [simplification-passes/](../../instructions/simplification-passes/README.md) | revise workflow |
| Edit | fix strategies, keyed to finding kinds | [fix strategy taxonomy](../../instructions/fix-warnings/fix-strategy-taxonomy.md) | fix procedure |
| Edit | packet body edits and copyedit under `keep` | [run a full improvement pass](../../instructions/run-full-improvement-pass-on-note.md) | full pass |
| Stop | strike list, with the operator's reason per strike | [resolve a strike list](../../instructions/simplification-passes/resolve-a-strike-list.md) | revise workflow |
| Stop | exact publication approval | revise and full-pass workflows | both workflow commands |
| Stop | hand-back disposition with a packet | [resolve a full-pass disposition](../../instructions/resolve-full-pass-disposition.md) | full pass |
| Stop | `deferred` item | [fix review warnings](../../instructions/fix-warnings/fix-review-warnings.md) | fix procedure |

Shipped constraints this proposal must respect:

- [ADR 080](../adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md) keeps every claim-level change with the author. No edit operation changes a title, thesis or title-as-claim.
- The [review system](../README-REVIEW-SYSTEM.md) asks that each operation be evaluated alone before its composition is trusted.
- The operator-decision record is `commonplace-review decisions` under [ADR 130](../adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md). It reads what runs leave in the state tree.
- A strike carries the operator's required reason since 2026-11-13, enforced today by revise workflow code.
- Directory types ([ADR 111](../adr/111-directory-types-declare-their-layout.md), [directory artifact](../definitions/directory-artifact.md)) are shipped and still experimental; one workflow family uses them.
- The revise workflow is 661 lines and the full pass 603. Both fix composition in Python: the assessment and plan grammar, which passes stop for strikes, the method order, the closing cycle.

## The problem

The same atoms are wired three ways, and the wiring is where the differences and the failures are. The full pass runs every review operation and then edits once. The fix procedure runs one kind of review operation and edits per finding, with no run record. The simplification passes run edit operations in a planned order with no review after. Nothing names the wiring, so two wirings cannot be compared on the same note.

Two of the three wirings are code. How the atoms are combined is the part that matters most and will change most, and today each change to it is a change to a Python workflow.

## The design

One constraint is set, by the operator on 2026-11-13: review needs code, fixing does not. Review is many pairs over many notes with freshness, results and cost to track, a batching problem. Fixing is one note, one agent, a diff and an operator, a conversation problem. So review operations run through `commonplace-review` as they do now, and everything else is instruction.

The procedure has two layers. The atoms are the stable layer. The composition is the variable layer and exists as variants. Structure comes from three typed artifacts.

**An atom is a typed instruction file.** One review operation, edit operation or stop, with its contract: what it reads, what it may change, what it must preserve, what it returns. Review gates already have a type. Edit operations get one; the simplification passes nearly fit it already, and each fix strategy becomes a file of that type. 
**Every atom is individually testable.** This is a design requirement, not a hope. An atom can be run by itself on one note, and a review operation can be run by itself across a whole collection through the batch machinery, so that it can be calibrated before any variant relies on it: the split check on every note in `kb/theory/`, for instance, with its rate of proposals, its hits on known cases and an operator-judged sample. An atom that only works inside a composition, because it needs the variant's context or another atom's unrecorded output, does not meet the contract. Its inputs are therefore files, and its output is a typed result the batch run can store.

**A variant is an instruction that composes atoms.** It states its entry evidence, the review operations it runs, how it selects edit operations from their findings, the order, how far it re-reviews after editing, where it stops for the operator, and which checks it runs on what it produced. `commonplace-validate` is the default check; a cheap variant runs little more and an expensive one runs more. An agent follows the variant in a session, delegating atoms to workers where isolation matters. The operator answers in the session, and the commit is the publication. Variants are expected to change often and to coexist, each retained with the runs it was tried on.

**A run is a typed directory.** Each run of a variant leaves one directory in the state tree, a directory artifact whose type declares its roles: a report that carries the run's identity and ending, the findings the variant read, the edit chain, and the operator's answers with their reasons. The start text and the candidate are not members, because a directory member must be a Markdown file of one declared type: the start text is a commit and a hash, the candidate is the note in the working tree, and intermediate texts are stored by hash beside the members. `commonplace-validate` on the directory checks that the required members exist, that they name the same note and start text, and that the answers satisfy their schema, such as a reason on every strike, rejection and deferral. This is where strictness lives. The rules are schema and layout, so tightening or loosening one is an edit to a type, not to a workflow. The schemas are part of what is being designed and will change with the variants.

An output is filed by what it is about, never by who asked for it. The two kinds of operation differ here. A review operation is a function of the note's text, so its result goes to the shared result store, keyed by note and atom, at the same path whether a standalone batch or an improvement run produced it; the run names itself in the result as provenance. The run's findings member cites the results it acted on, with their hashes, and does not hold them. An edit operation is a function of a text chain: its output is a candidate that means something only relative to the text it was given. It always lives in a run. Running one edit operation alone is therefore not a special case with its own directory but a run of a one-atom variant, which is also how an edit operation is unit-tested.

The record follows from the run type. Decisions key to the atom, never to the variant, so evidence about an atom survives recomposition, and the variant's name on the run says which composition produced it. The decisions command reads the answers member of each run and should be thin enough that a schema revision is not a code change.

### The default composition

Variants differ, but one ordering rule holds for the default one, set by the operator on 2026-11-13: higher-order concerns before lower-order concerns. The wording is the composition field's. A higher-order concern is about what the note is: its claim, its boundary, whether it should exist, where it belongs. A lower-order concern is about how the note says it: framing, flow, wording. Work on a lower-order concern is wasted when a higher-order one is unsettled, because the text it improves may not survive. The simplification passes already order themselves this way through their `depth` field; the rule here extends that order upward to the note's existence and boundary.

1. **Check higher-order concerns first.** Some review operations can propose a change to what the note is: a split, a merge, a rehome, a rejection, a different claim. These checks always run before any edit. The expected result, in most runs, is that they propose nothing and the run goes on. That rarity is a working assumption the design rests on, not a measured fact: the [higher-order check evaluation workshop](../../work/higher-order-check-evaluation/README.md) exists to test it and to keep the check calibrated, and it is expected to stay open, since the check will be recalibrated many times as wordings, models and the collection change. If the check proves to propose often, the default composition is what has to change. A proposal carries a force:
   - **Strong:** the run stops there and puts the proposal before the operator. Lower-order edits are not run, because they would be spent on text that may not survive.
   - **Weak:** the change might be beneficial but the note stands as it is. The run records the proposal as a pending item and goes on to the edits.
2. **Otherwise apply what is automated.** Edit operations that need no operator decision run and are applied, up to the exceptions their atoms name. They normally run first among the edits, since nothing waits on them.
3. **Save the rest for the operator.** Edits that need a decision are not applied and do not block step 2. They are written to the run's answers member as pending items, each with its context, and the run ends with some changes applied and some pending.

So a run has three ordinary endings: stopped on a strong proposal with nothing edited, fully applied, or partly applied with pending items, which may include a weak proposal. A later session resolves the pending items by the same present, ask and record step, and the decisions command lists what is still pending per note. Which edit operations count as automated is the grade question, which the [second proposal](./authority-grades-and-learning-from-operator-decisions.md) owns; a variant only needs each atom to say which of the two it is today.

What this gives up is stated plainly. Code no longer refuses a text that changed the title or H1; that becomes a diff the agent reads and the operator sees. Approvals are no longer bound to exact text with later edits detected, and a stopped run does not resume without paying again; both become the session itself.

## Options

**A. Run as a directory type.** As described above: roles for report, findings, edit chain and answers, validated as one unit. A [workshop draft](../../work/decision-lifecycle-evidence/improvement-run-type.md) gives the layout and what validation can and cannot check.
Operativity: the variant's agent writes the members; `commonplace-validate` and the decisions command consume them. Force against: directory types are experimental, and a second workflow will find their rough edges.

**B. Run as one typed file.** A single run report whose frontmatter holds the decision list, schema-checked like the full-pass packet; the texts stay in git.
Operativity: the same two consumers. Force against: one file cannot check that its parts agree with each other or that a member is missing, and the candidate and findings are then recoverable only from the session and the commit.

The retired code is the same under both: the revise workflow and the full pass's editor, packet, closing cycle and repair, each retired only when a variant has run its cases on retained examples. The six method families stay as review operations.

**Candidate selection** (2026-11-13): A, with B as the fallback if the directory-type machinery costs more than the run structure is worth. No decision is taken here.

## Free choices

- How many notes a one-atom variant can be run over at once, since the batch machinery today runs review operations only.
- How results from different wordings of one review operation are kept apart during calibration: the store keeps one result per note and criterion, so a rerun overwrites.
- The edit-operation type's fields, and whether fix strategies and method families are rewritten to their types or wrapped.
- Whether a variant has a type of its own, so the validator can check that every atom it names exists.
- Whether the run type keeps four member types or folds the findings and the edit chain into the report.
- The answers schema: its fields, and which decisions require a reason.
- Where variants and atoms live under `kb/instructions/`, and how a variant is named and retired.
- Which review operations are the higher-order checks, and how each states the force of what it proposes. They always run first, so their cost is paid on every run; the full pass's method families cost far more than a gate sweep, which argues for a small dedicated check over the whole method suite.
- What makes a proposal strong: the check's own judgment, a stated criterion such as the note having no claim its neighbours do not own, or the operator's threshold recorded from earlier answers.
- Whether pending items expire when the note's text changes under them, as review results go stale.
- Which checks a variant names beyond `commonplace-validate`.
- The interface for operator answers. A session in which the agent presents each item in context, asks, and records the answer is the candidate; [resolve a strike list](../../instructions/simplification-passes/resolve-a-strike-list.md) is that step for one stop.

## Adoption criteria

- **The higher-order check:** the build does not wait on it. The procedure is built on the assumption that higher-order proposals are rare, and the standing [higher-order check evaluation workshop](../../work/higher-order-check-evaluation/README.md) reports when the assumption fails.
- **First build:** the operator commissions the run type, the edit-operation type and the first variant. The fix case is the candidate first variant, since the fix procedure is the one with no run record today. Its first run on a note with fresh warnings is the first retained example.
- **Retirement of an editing path:** a variant has run that path's cases on retained examples and the operator accepts the results.
- **Fallback to option B:** the first run type needs validator changes that the run structure does not justify.

What to do with the runs once they exist, which authority each atom carries and what evidence may move it toward automation, is a separate proposal: [authority grades and learning from operator decisions](./authority-grades-and-learning-from-operator-decisions.md).

---

Relevant Notes:

- [Authority grades and learning from operator decisions](./authority-grades-and-learning-from-operator-decisions.md) — enables: the run records this procedure leaves are the evidence that proposal grades and learns from
- [Review architecture](../review-architecture.md) — part-of: the review workflows that keep running the review operations
- [Run a full improvement pass on one note](../../instructions/run-full-improvement-pass-on-note.md) — procedure: the variant that runs every review operation
- [Fix system](../../instructions/FIX-SYSTEM.md) — procedure: the variant that edits per finding, and the candidate first case
- [Simplification passes](../../instructions/simplification-passes/README.md) — procedure: the variant that runs edit operations from a plan, and the smallest example of a composition separated from its atoms
- [ADR 111](../adr/111-directory-types-declare-their-layout.md) — decided-by: directory types and their layouts, which the run type would use
- [ADR 127](../adr/127-review-runs-as-workflows-over-result-files.md) — decided-by: review as workflows over result files, the part that stays in code
- [ADR 130](../adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md) — decided-by: the operator-decision record that reads what runs leave

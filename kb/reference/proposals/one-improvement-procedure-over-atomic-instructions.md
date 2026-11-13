---
description: "Proposal: replace the full pass, fix procedure and simplification passes with one procedure composed as variants from atomic instructions of three kinds (review operations, edit operations, stops), with authority grades on the atoms"
type: reference/types/design-proposal.md
tags: [review-system, warranted-autonomy]
---

# One improvement procedure over atomic instructions

Commonplace has three ways to improve one note after review: the full improvement pass, the fix procedure for review warnings, and the simplification passes. All three do the same thing. They review the note with some operations, choose edit operations from what the review found, apply them within bounds, review again, and stop for an operator where authority requires it. They do it from the same ingredients: atomic instructions of three kinds.

- **Review operations**: the gate criteria, and the full pass's method families (critique, compression, composition friction, premise decomposition, connect).
- **Edit operations**: the simplification passes, and the fix strategies keyed to warning kinds.
- **Stops**: strike lists, the publication approval, the hand-back dispositions.

What differs is the composition: how each procedure enters the loop, which operations it selects and in what order, how far it re-reviews, and where it stops. This proposal replaces the three procedures with one procedure that has two layers. The atomic instructions are the stable layer. The composition is the variable layer, and it will exist as variants, because how the atoms are combined is the part that matters most and will change most. Authority grades attach to the atoms. The evidence for moving a grade comes from the operator-decision record, which shipped under [ADR 130](../adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md) and keys to the atoms. A learning loop would calibrate atoms and compare variants.

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

- **Adopted:** the operator-decision record, as the read-only query `commonplace-review decisions` over run operator records, full-pass packets and fix reports under `kb/reports/state/`, under [ADR 130](../adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md); recorded here rather than proposed below. It tells operator from agent judgment and item from bundle decisions, and computes no statistic. Procedures for reading it are deferred to the [unresolved frontier](../definitions/unresolved-frontier.md) work.
- [ADR 080](../adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md) keeps every claim-level change with the author. No edit operation changes a title, thesis or title-as-claim.
- The strike-list stops are declared temporary procedure-development points. The planning instruction asks the operator to retain proposed, accepted and rejected choices with their reasons, and to evaluate rule changes on retained and fresh examples before a stop is removed. Since 2026-11-13 the revise workflow requires a reason with every strike and blocks deleted, edited or added entries. The record lists them across runs; no procedure reads that listing yet.
- [Full improvement pass closure](../full-improvement-pass-closure.md) states as policy: do not build trust-dial automation or reduced audit sampling from the closing calibration.
- The [review system](../README-REVIEW-SYSTEM.md) asks that each operation be evaluated alone before its composition is trusted. Reliable replay does not establish reliable selection or editing judgment.
- One full pass on one short note cost 27 launches and $4.47. A fix on one warning is a single agent edit.

## The problem

The same atoms are wired three ways, and the wiring is where the differences and the failures are. The full pass runs every review operation and then edits once. The fix procedure runs one kind of review operation and edits per finding, outside any run directory. The simplification passes run edit operations in a planned order with no review after. Nothing names the wiring, so nothing can compare two wirings on the same note, and a failure in one procedure is repaired in that procedure alone.

Evidence about an atom is split the same way. A fix strategy's rejections live in fix reports, a pass's strikes in revise runs, a disposition in packets. The record now lists all three, but an atom used by two procedures still has its evidence under two names, and no stop has a grade that evidence could move.

## The two layers

The atomic instructions are the stable layer. Each is one review operation, edit operation or stop, with its own contract: what it reads, what it may change, what it returns, and what it must preserve. Each is evaluated alone, as the review system already requires. Each is an action class, and a grade attaches to it. The gate criteria and the simplification passes already have this shape; the method families, the fix strategies and the full pass's editor do the same work without the same contract.

The composition is the variable layer. A variant of the one procedure is a named composition: its entry evidence, the review operations it runs, how it selects edit operations from their findings, the order, how far it re-reviews after editing, and which stops it includes where. The three procedures today are three variants that were never named as such. Variants are expected to change often and to coexist. Each is retained with the evidence it was tried on, and the simplification passes already show the shape at the smallest scale: a planning instruction separate from its passes.

Two rules connect the layers. The record's action class keys to the atom, never to the variant, so evidence about an atom survives recomposition; the procedure version an entry lacks today is the variant's name. And a variant is what gets compared, while an atom is what gets calibrated: a variant that does worse than another on the same notes says something about the composition, not about the atoms it shares with the better one.

## Authority grades on the atoms

An edit operation's grade says how far the procedure goes with its output before an operator decides. Authority is set on two axes that today's procedures mix.

Per item, within a run:

1. **Apply.** The edit lands in the run's text, and later atoms work on it. Settled simplification passes and the full pass's body edits under `keep` run this way.
2. **Propose, then wait.** A stop puts the proposed items before the operator, who selects before any is applied. The strike list is this stop.
3. **Hand back.** A stop ends the procedure on this item, and the author decides. This is a change of author, not a smaller permission: the hand-back dispositions and the fix procedure's `deferred` items do this today. A variant must keep it an ownership boundary and never encode it as a stricter step on the same scale as the other two, since no evidence about an atom can move an item across it.

Per run, at the boundary:

- **Approve publication.** The variant produces a candidate, and the operator approves the exact final text. Both workflow commands do this for every changed text, so an applied item never reaches the checkout on its grade alone. A change on this axis is a change to a variant's publication boundary, a different decision from lowering an atom's grade.

The grade of an item is not fixed by its atom alone. The drift section names a signal from the note's history across runs that routes an otherwise applicable item to hand back.

A review operation's output can be declined before any edit: the fix agent rejects a finding with evidence, the packet reconciles findings and drops some, the revision assessment may not recommend a pass. Whether declining is a graded action is left free below, but declines must be recorded in any case: a record holding only what reached the operator cannot show a wrongly declined finding, which the learning section needs.

Claim-level changes stay at **hand back** in every variant, because ADR 080 decided that from six episodes of in-pass repair drifting toward defensible emptiness ([narrowing bought to survive review is paid for in content](../../theory/narrowing-bought-to-survive-review-is-paid-for-in-content.md)). Learning applies only to atoms below that ceiling.

## An observed drift, read as a composition failure

ADR 080 stopped the pass from changing a claim, but it did not stop the drift that [narrowing bought to survive review](../../theory/narrowing-bought-to-survive-review-is-paid-for-in-content.md) describes; it moved the drift across runs. Under `keep`, and under the fix procedure, each run answers its findings with a scope section, a qualifier, a historical reframing or a narrower description. Each edit is justified by a finding. The note grows longer and more conditional, the warning count barely moves, and the accumulated result hides the deeper problem: the claim is wrong as titled, or the note has no contribution its neighbours do not own.

Two episodes on 2026-11-12 show the shape. Two fix passes on `kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md` added a scope section, qualifiers and a historical framing; the pair count stayed at 36 pass and 8 warn across both; the operator's answer was a generalization and a retitle, with claim-level decisions still open. One full pass on the former `kb/theory/types-give-agents-structural-hints-before-opening-documents.md` proposed `revise` with three candidate claims, each narrower than the title; the operator's answer was `delete`, because every sentence of the warranted update was owned elsewhere.

In the two-layer reading the drift is a composition failure, not an atom failure. The fix strategies are local repairs: restore a qualifier, widen an attribution to the source, add framing, mark an extension as the note's own, acknowledge a boundary case. Several widen rather than narrow, and none is wrong on its own. What the variant lacks is a stop between repeated edit operations on one claim: nothing reopens whether the claim should be retained, reformulated or deleted when a repair lands on a claim that earlier repairs already qualified. The mechanism is repeated local repair without escalation.

The designed antidote exists and no variant can reach it. [ADR 066](../adr/066-claims-declare-modality-in-text-and-passes-repair-mode-mismatch.md) added the ideal-type mode: keep the general first-order claim, concede its exceptions, and carry an adequacy record (declared use, omitted mechanism, consequence bound, explanatory dominance) that review attacks as content ([domain pricing routes an exception to idealization assessment](../../theory/domain-pricing-routes-an-exception-to-idealization-assessment.md)). It is the repair that answers a counterexample without shrinking the subject. ADR 080 moved every mode conversion to the author, so it is reachable only through a hand-back, and the revise brief that hand-back produces is not required to consider it: the 2026-11-12 packet offered two universal candidates and one statistical, none ideal-type. The validation series behind ADR 066 is the caution on the other side: mode conversion proved rare because an ideal-type landing needs its own warrant, and a claim whose first-order model has no explanatory dominance, as the structural-hints note's did not, cannot take it.

Two consequences bind the design. First, the record must be readable per note across runs, so accumulated narrowing is visible where a single run's diff cannot show it. The shipped record groups entries by note; the fix procedure's entries remain whole reports, not items. Second, growth in qualifiers, scope sections or length while the warning count holds is a candidate signal that routes the next item to **hand back** rather than **apply**; it is a signal, not a rule, until retained examples test it. The procedures for both are deliberately unspecified: the two episodes are the whole evidence base, and good procedures need more examples than that.

### Three atoms that stand apart from the options

Three cheap changes follow from the drift and the antidote. Each is an atom or a change to one, so any variant can include it, and none should wait on the larger design:

- **A revise brief considers the ideal-type mode** whenever its diagnosis concerns exceptions or claim modality, and states what warrant for it is present or missing. It is not required to disprove idealization first: deletion, merger or a narrower claim is sometimes the right answer, and a brief that must argue past idealization every time would carry a preservation bias of its own. This changes the hand-back stop's content.
- **An escalation stop.** When an edit operation lands on a claim that earlier repairs already qualified, the worker reports it for the operator instead of applying it. It supplies what the drift lacks, a point at which local repair stops and someone asks whether the claim survives. It is an operator check, not an automatic stop: the "already qualified" condition is firmer than the untested signal above, so at this stage the worker's report and the operator's answer are the evidence that would later warrant a rule.
- **A reflection field** in the fix report and the packet: the editing worker, as the first observer of the drift, states whether the edits it made suggest a problem with the claim that the edits do not address. Reflections are evidence for the record, never a disposition.

Their adoption criterion is in the last section.

## Learning: calibrate atoms, compare variants

What the record can warrant is narrow, [since an accepted edit verifies the change, not the rule](../../theory/an-accepted-edit-verifies-the-change-not-the-rule.md). Each approval verifies one instance. A grade change is a claim about an atom, and it needs its own verification. A publication approval is one bundle decision, never an approval of each edit behind it; the record keeps that distinction, and a loop must not undo it.

The record does not lower a grade by itself. A grade change is an operator decision, and the record supplies its evidence. Five forces shape what evidence counts.

- **Approval rate is the wrong statistic.** An atom the operator approves nine times in ten is fine under a stop and unsafe without one. Lowering the grade needs a way to tell, per instance, which proposals the operator would reject, [since the augmentation-automation boundary is discrimination, not accuracy](../../theory/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md). In practice the record should yield one of two things: a check that catches the rejected kind, or a narrower atom definition that excludes it. Either is then tested on retained and fresh examples, as the strike-list instruction already requires. [Warranted autonomy is bounded by oracle domain](../../theory/warranted-autonomy-is-bounded-by-oracle-domain.md), so a lowered grade covers only the narrowed atom that the check or definition can assess.
- **Local justification does not check cumulative damage.** In the drift above each edit is justified by its finding, and the defect lies in the accumulation. A check that reads an edit only against its finding therefore cannot discriminate for the edit operations that add a qualifier, scope section or framing. The route in the first point stays open to those atoms only if the check also reads the note's history, which makes the per-note record a possible requirement for lowering their grade. Whether such a trajectory-aware check can be stated is a question for the first retained examples, not for this proposal.
- **Evidence belongs to the atom, comparison to the variant.** An atom's evidence is pooled across every variant that used it, which is why the record keys to atoms. A variant is judged against another variant on the same notes, and that judgement never lowers an atom's grade by itself.
- **The remaining decisions get harder.** As predictable atoms move down, the decisions left with the operator concentrate the harder cases ([warranted transfer leaves people the hardest-to-warrant decisions](../../theory/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md)). Rates computed over all decisions then drift for reasons unrelated to any atom. Evidence must be read per atom.
- **Success is measured per judgment, not per hour.** Operator time may not fall, because attention moves to harder work ([increasing computational autonomy relocates human effort](../../theory/increasing-computational-autonomy-relocates-human-effort.md)). The measure of progress is how much accepted improvement each operator decision supports.

A grade that moved down needs a way back up. The [audit-a-prior-pass](../../instructions/simplification-passes/audit-a-prior-pass.md) procedure already traces a weakened passage to the finding that caused it. Sampled audits of lowered atoms, with an audit failure raising the grade again, would close that loop.

The closure policy is narrower than a ban. It prohibits trust-dial automation and reduced audit sampling "from this calibration": the closing-cycle evidence of the shipped full pass. It does not foreclose automation warranted by different evidence, and this record is different evidence. Three obligations still need separate treatment in any adopting decision: removing an operator selection stop, changing the final-text closing review, and introducing retrospective audits. The audits add checking where none exists, and removing a strike-list stop leaves the closing review and the publication boundary as they are. The clause the loop does touch is the trust dial: a grade that evidence moves down and audits move up is one, even when each move is an operator decision. The adopting decision should say which of the three obligations it preserves and which it revises, and on what evidence.

## Options

The options are two ways to run a variant. They are stages more than rivals: the first needs no code, and the second is where the first's steps go as they settle.

**A. Variants as instructions over the review commands.** A variant is an instruction an agent follows, in a session or headless, as the full-pass instruction is today. It uses the review workflow commands internally rather than a new command: `run gates` for review operations, `run revise` with a plan for edit passes, and the packet with [resolve a full-pass disposition](../../instructions/resolve-full-pass-disposition.md) for hand-backs. The first variant replaces one of the three procedures on its own cases. Lowest cost, and every atom stays where it lives.
Operativity: the instruction is consumed by an agent with binding force over the commands it calls; the record reads the runs those commands leave. Force against: the steps the instruction holds in prose, selection above all, are the steps that are hardest to evaluate alone.

**B. Variants as plans the revise workflow runs.** The revise workflow is the base, because it already has the loop's pieces in order: an assessment that produces a plan, atoms that each run as one bounded worker ask on the text the previous one left, strike stops, and exact publication from captured inputs. A variant is then a plan, and the composition is data. Four widenings, in build order:

1. Assessment takes any evidence: a purpose, fresh review results, or the method families' outputs. There are no intake profiles; a fix run is an assessment over warnings and a full pass is an assessment over the method outputs.
2. Fix strategies become passes. As passes they get the run directory, the text chain, code checks and the publication boundary the fix procedure lacks, and their rejected and deferred items become plan decisions the record reads as items.
3. Dispositions become plan stops. The plan's `stop` already reports a rewrite and stops; revise, delete, merge and rehome are that stop with a packet, where ADR 080's hand-back lives.
4. Review after editing scales with the edit: a one-finding fix re-reviews the pairs the edit staled, a full pass reruns its method families. This is a selection rule inside the variant, not a reason to keep three procedures.

Operativity: the review command consumes each widening as it lands and retires the path it replaces. Forces against: composing stages hides which stage is unreliable unless each stays separately evaluable, which single fixed-pass runs preserve and every variant must keep; and the entry cases must keep their cost shape, which the fourth widening is for.

The learning loop is orthogonal to the choice. It requires grades that a decision can change and a decision on the closure policy's three obligations.

**Sequence.** A review on 2026-11-12 proposed building the record first, as a bounded evidence-gathering step. That step shipped under [ADR 130](../adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md). The record is a surface of the [unresolved frontier](../definitions/unresolved-frontier.md). Procedures for reading it come later with the frontier work; two candidate occasions are already visible, before any decision to remove a strike-list stop, and whenever repeated repairs on one note prompt another intervention. Any such reading keeps two questions apart: per note, whether repeated repairs are obscuring a claim-level problem; per atom, whether safe applications can be told from cases that need operator judgment.

**Candidate selection** (2026-11-13): the operator's direction is one procedure whose variants share the same atoms. Option A is the candidate for the first variant, with option B as where its steps go once they have run on retained examples. No decision is taken here.

Oracle warrant for a lowered grade: the operator's decision, backed by a discriminating check or narrowed atom tested on retained and fresh examples. That warrant stops at the atom's boundary as defined when the decision was made, and at the conditions of the examples. It never extends to claim-level changes.

## Free choices

- The atom's contract: the fields every atom declares (kind, inputs, bound, what it preserves, what it returns, default grade, cost), and whether the method families and fix strategies are rewritten to it or wrapped.
- Whether a method family is one atom or several: critique, compression and connect each return findings of more than one kind.
- The grade set on the per-item axis: the three above, fewer, or a split of apply between per-edit and per-run approval.
- Whether reasons are required at every stop. For strikes the operator decided on 2026-11-13 that they are, accepting the cost per decision for the most learning input. Whether packet resolutions and publication approvals carry the same requirement is open.
- The interface for operator answers: direct edits to the proposed file, or a session in which an agent presents each item in context, asks the operator, and records the answer in the same file, approving on the operator's word. The strike list has the session procedure ([resolve a strike list](../../instructions/simplification-passes/resolve-a-strike-list.md)); the packet resolution and the publication approval could take the same shape, since each is a proposed file and an answer.
- The retention of operator answers in the state tree, where [ADR 130](../adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md) keeps the record. The record is as durable as the state repository's commit cadence, which the [public state repository workshop](../../work/public-state-repository/README.md) still owns. One force remains open against that default: operator answers, unlike run bundles, cannot be regenerated by rerunning a workflow, so their retention bar is higher than the tree's. Whether a reading promotes read entries into the tracked record is deferred with the reading procedures to the frontier work named under the sequence.
- Whether declining a finding is a graded action or stays with the variant that met it. Recording the decline is not free: without it the record is censored to what reached the operator.
- How variants are named, where their compositions are kept, and what evidence retires one.
- Under option B, the order in which steps move from the instruction into the review command; the four widenings are the candidate order, each after the instruction's step it replaces has run on retained examples.

## Adoption criteria

- **The three atoms:** the next revise hand-back or fix pass on a note that already carries one pass's qualifiers; the brief, escalation and reflection changes cost one instruction edit each and need no other trigger.
- **Option A:** the operator commissions the first variant as an instruction; it needs no new code. The procedure it replaces retires only when the variant has run that procedure's cases on retained examples.
- **Option B:** a widening lands when the instruction's step it replaces has run on retained examples, built on the revise workflow rather than as a fourth path.
- **Learning loop:** one atom has enough recorded decisions that a discriminating check or narrowed definition can be stated and tested on fresh examples, and a decision has revisited the closure policy's trust-dial clause.

---

Relevant Notes:

- [Review architecture](../review-architecture.md) — part-of: the review workflows and run directories every variant runs in
- [Gate learning from accepted edits](./gate-learning-from-accepted-edits.md) — compares-with: mines new gates from accepted edits, where this proposal moves authority grades on existing atoms; both rest on the same instance-versus-rule oracle limit
- [Run a full improvement pass on one note](../../instructions/run-full-improvement-pass-on-note.md) — procedure: the variant that runs every review operation, with its dispositions, closing cycle and publication boundary
- [Fix system](../../instructions/FIX-SYSTEM.md) — procedure: the variant that edits per finding, whose deferred items have no reader today
- [Simplification passes](../../instructions/simplification-passes/README.md) — procedure: the variant that runs edit operations from a plan, and the smallest example of a composition separated from its atoms
- [ADR 127](../adr/127-review-runs-as-workflows-over-result-files.md) — decided-by: run directories and result files, where per-run decision entries live
- [ADR 130](../adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md) — decided-by: the operator-decision record whose entries a grade decision would read

---
description: "Proposal: put authority grades on the atomic instructions of the improvement procedure, expose cross-run narrowing as a composition failure, and move grades toward automation only on discriminating evidence from recorded operator decisions"
type: reference/types/design-proposal.md
tags: [review-system, warranted-autonomy]
---

# Authority grades and learning from operator decisions

The [one improvement procedure](./one-improvement-procedure-over-atomic-instructions.md) composes review operations, edit operations and stops into variants, and each run leaves typed records of what the operator decided. This proposal is about what to do with those records: which authority each atom carries, how a known drift shows up across runs, and what evidence may move an atom toward automation. It depends on the procedure proposal and adds nothing to what that proposal needs in order to be built.

## Current state (as of 2026-11-13)

- The operator-decision record is shipped as `commonplace-review decisions` under [ADR 130](../adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md). It tells operator from agent judgment and item from bundle decisions, and computes no statistic. Procedures for reading it are deferred to the [unresolved frontier](../definitions/unresolved-frontier.md) work.
- [ADR 080](../adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md) keeps every claim-level change with the author. No edit operation changes a title, thesis or title-as-claim.
- A strike on a plain-wording or abstractions list carries the operator's required reason since 2026-11-13. The stops are declared temporary procedure-development points whose removal needs rule changes evaluated on retained and fresh examples.
- [Full improvement pass closure](../full-improvement-pass-closure.md) states as policy: do not build trust-dial automation or reduced audit sampling from the closing calibration.
- The [review system](../README-REVIEW-SYSTEM.md) asks that each operation be evaluated alone before its composition is trusted.
- The procedure proposal is not adopted. Until it is, the atoms here are the existing gate criteria, method families, simplification passes, fix strategies and stops, and the variants are the three procedures that use them.

## The problem

No stop has a grade that evidence could move. The operator's decisions are the strongest evidence the system gets about which edits are wanted, and they are now recorded, but nothing says which class of action a decision belongs to or what would warrant removing the stop that produced it. Without that, the strike-list stops cannot finish their declared development path, and every variant keeps the operator at every boundary indefinitely.

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

Two episodes on 2026-11-12 show the shape. Two fix passes on the since-retired `kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md` added a scope section, qualifiers and a historical framing; the pair count stayed at 36 pass and 8 warn across both; the operator's answer was a generalization and a retitle, with claim-level decisions still open. One full pass on the former `kb/theory/types-give-agents-structural-hints-before-opening-documents.md` proposed `revise` with three candidate claims, each narrower than the title; the operator's answer was `delete`, because every sentence of the warranted update was owned elsewhere.

In the two-layer reading the drift is a composition failure, not an atom failure. The fix strategies are local repairs: restore a qualifier, widen an attribution to the source, add framing, mark an extension as the note's own, acknowledge a boundary case. Several widen rather than narrow, and none is wrong on its own. What the variant lacks is a stop between repeated edit operations on one claim: nothing reopens whether the claim should be retained, reformulated or deleted when a repair lands on a claim that earlier repairs already qualified. The mechanism is repeated local repair without escalation.

The designed antidote exists and no variant can reach it. [ADR 066](../adr/066-claims-declare-modality-in-text-and-passes-repair-mode-mismatch.md) added the ideal-type mode: keep the general first-order claim, concede its exceptions, and carry an adequacy record (declared use, omitted mechanism, consequence bound, explanatory dominance) that review attacks as content ([domain pricing routes an exception to idealization assessment](../../theory/domain-pricing-routes-an-exception-to-idealization-assessment.md)). It is the repair that answers a counterexample without shrinking the subject. ADR 080 moved every mode conversion to the author, so it is reachable only through a hand-back, and the revise brief that hand-back produces is not required to consider it: the 2026-11-12 packet offered two universal candidates and one statistical, none ideal-type. The validation series behind ADR 066 is the caution on the other side: mode conversion proved rare because an ideal-type landing needs its own warrant, and a claim whose first-order model has no explanatory dominance, as the structural-hints note's did not, cannot take it.

Two consequences bind the design. First, the record must be readable per note across runs, so accumulated narrowing is visible where a single run's diff cannot show it. The shipped record groups entries by note; the fix procedure's entries remain whole reports, not items. Second, growth in qualifiers, scope sections or length while the warning count holds is a candidate signal that routes the next item to **hand back** rather than **apply**; it is a signal, not a rule, until retained examples test it. The procedures for both are deliberately unspecified: the two episodes are the whole evidence base, and good procedures need more examples than that.

### Three atoms that stand apart from the options

Three cheap changes follow from the drift and the antidote. Each is an atom or a change to one, so any variant can include it, and none should wait on the larger design:

- **A revise brief considers the ideal-type mode** whenever its diagnosis concerns exceptions or claim modality, and states what warrant for it is present or missing. It is not required to disprove idealization first: deletion, merger or a narrower claim is sometimes the right answer, and a brief that must argue past idealization every time would carry a preservation bias of its own. This changes the hand-back stop's content.
- **An escalation stop.** When an edit operation lands on a claim that earlier repairs already qualified, the worker reports it for the operator instead of applying it. It supplies what the drift lacks, a point at which local repair stops and someone asks whether the claim survives. It is an operator check, not an automatic stop: the "already qualified" condition is firmer than the untested signal above, so at this stage the worker's report and the operator's answer are the evidence that would later warrant a rule.
- **A reflection field** in the run report, and in the packet while it exists: the editing worker, as the first observer of the drift, states whether the edits it made suggest a problem with the claim that the edits do not address. Reflections are evidence for the record, never a disposition.

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

**A. Grades named in the variants.** Each variant states, per atom it uses, whether the atom's output is applied, proposed or handed back, and each run's records carry the atom and the variant's name. No code. Grades are then visible and comparable across variants, and a grade change is an edit to a variant with the evidence cited.
Operativity: the variant instruction is consumed by the agent running it; the grade is read by the operator deciding a change. Force against: a grade stated only in prose can drift between variants that share an atom.

**B. Grades declared on the atoms.** Each atom's file declares its default grade, and a variant may only raise it. One declaration per atom, checked by the validator where the atom's type allows.
Operativity: `commonplace-validate` and the variant consume the declaration. Force against: it fixes a field on every atom before any grade has moved, which the first evidence may show to be the wrong unit.

The learning loop is orthogonal to the choice. It requires grades that a decision can change and a decision on the closure policy's three obligations.

Oracle warrant for a lowered grade: the operator's decision, backed by a discriminating check or narrowed atom tested on retained and fresh examples. That warrant stops at the atom's boundary as defined when the decision was made, and at the conditions of the examples. It never extends to claim-level changes.

## Free choices

- The grade set on the per-item axis: the three above, fewer, or a split of apply between per-edit and per-run approval.
- Whether reasons are required at every stop. For strikes the operator decided on 2026-11-13 that they are, accepting the cost per decision for the most learning input. Whether hand-back resolutions and publication approvals carry the same requirement is open.
- Whether declining a finding is a graded action or stays with the variant that met it. Recording the decline is not free: without it the record is censored to what reached the operator.
- The retention of operator answers in the state tree. They cannot be regenerated by rerunning anything, so their retention bar is higher than the tree's default, which the [public state repository workshop](../../work/public-state-repository/README.md) still owns. Whether a reading promotes read entries into the tracked record is deferred with the reading procedures.

## Adoption criteria

- **The three atoms:** the next hand-back or fix on a note that already carries one pass's qualifiers; the brief, escalation and reflection changes cost one instruction edit each and need no other trigger.
- **Option A:** the first variant of the procedure is written; it names its grades from the start.
- **Option B:** two variants disagree on the grade of an atom they share.
- **Learning loop:** one atom has enough recorded decisions that a discriminating check or narrowed definition can be stated and tested on fresh examples, and a decision has revisited the closure policy's trust-dial clause.

---

Relevant Notes:

- [One improvement procedure over atomic instructions](./one-improvement-procedure-over-atomic-instructions.md) — rests-on: the atoms, variants and run records this proposal grades and learns from
- [Gate learning from accepted edits](./gate-learning-from-accepted-edits.md) — compares-with: mines new gates from accepted edits, where this proposal moves authority grades on existing atoms; both rest on the same instance-versus-rule oracle limit
- [ADR 130](../adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md) — decided-by: the operator-decision record whose entries a grade decision would read
- [ADR 080](../adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md) — decided-by: the hand-back ceiling no grade can cross

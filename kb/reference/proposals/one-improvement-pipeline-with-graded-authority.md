---
description: "Proposal: give the full pass, fix procedure and simplification passes shared authority grades per action class, as three procedures or one pipeline, moved toward automation on evidence from the operator-decision record"
type: reference/types/design-proposal.md
tags: [review-system, warranted-autonomy]
---

# One improvement pipeline with graded authority

Commonplace has three ways to improve one note after review: the full improvement pass, the fix procedure for review warnings, and the simplification passes. Each turns findings into bounded edits, and each stops somewhere for an operator. They draw that operator boundary in different places and name it differently. Their answers can now be read across runs, but no stop has a grade that evidence could move.

This proposal gives the three procedures a shared authority vocabulary: each class of action carries a grade that says how far the pipeline may go before an operator decides. The evidence a grade change needs comes from the operator-decision record, which shipped under [ADR 130](../adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md). Option A adds the vocabulary to the three procedures as they are; option B also makes them one pipeline in code. A learning loop would move grades on that evidence. Three small changes that answer an observed drift stand apart from the choice between A and B and have their own adoption criterion.

## Current state (as of 2026-11-13)

| | Full pass | Fix procedure | Simplification passes |
|---|---|---|---|
| Entry | `commonplace-review run full-pass` | agent follows [fix review warnings](../../instructions/fix-warnings/fix-review-warnings.md); no workflow command | `commonplace-review run revise` with `--assess` or `--plan` |
| Finding source | six method families over the note, reconciled into a packet | fresh `warn`/`fail` review results | an assessment, or a fixed plan |
| Edit bound | body edits that keep the claim; copyedit | framing, accuracy and attribution; no argument change | per-pass preserve rules; `defend` claims |
| Review after editing | closing cycle; at most one repair | re-run the gate sweep | none beyond code checks on each text |
| Operator stops | hand-back dispositions; `--direction` for an undetermined update; exact publication approval | `deferred` items | strike lists for plain-wording and abstractions; exact publication approval |
| Where the operator's answer is kept | packet resolution fields with rationale, under [resolve a full-pass disposition](../../instructions/resolve-full-pass-disposition.md) | the agent's own `rejected` and `deferred` statuses in the free-form fix report; nothing consumes deferred items | the proposed list and each strike with the operator's required reason, in the run's operator record |
| Read across runs by | `commonplace-review decisions`: disposition as agent judgment, resolution as the deciding authority's | `commonplace-review decisions`: the report listed once, by path; no run binds it | `commonplace-review decisions`: one entry per proposed entry, with the strike reason |

Shipped constraints this proposal must respect:

- **Adopted:** the operator-decision record, as the read-only query `commonplace-review decisions` over run operator records, full-pass packets and fix reports under `kb/reports/state/`, under [ADR 130](../adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md); recorded here rather than proposed below. It tells operator from agent judgment and item from bundle decisions, and computes no statistic. Procedures for reading it are deferred to the [unresolved frontier](../definitions/unresolved-frontier.md) work.
- [ADR 080](../adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md) keeps every claim-level change with the author. The pass never changes a title, thesis or title-as-claim.
- The strike-list stops are declared temporary procedure-development points. The planning instruction asks the operator to retain proposed, accepted and rejected choices with their reasons, and to evaluate rule changes on retained and fresh examples before a stop is removed. Since 2026-11-13 the revise workflow requires a reason with every strike and blocks deleted, edited or added entries, so each run holds its proposed list and its strikes with reasons. The record lists them across runs; no procedure reads that listing yet.
- [Full improvement pass closure](../full-improvement-pass-closure.md) states as policy: do not build trust-dial automation or reduced audit sampling from the closing calibration.
- The [review system](../README-REVIEW-SYSTEM.md) asks that each operation be evaluated alone before its composition is trusted. Reliable replay does not establish reliable selection or editing judgment.
- One full pass on one short note cost 27 launches and $4.47. A fix on one warning is a single agent edit.

## The problem

The three procedures share a structure but not a vocabulary. A finding arrives. Something decides whether it applies. An editor changes text within a bound. Something re-reviews, and an operator approves, strikes or takes over. Today a `deferred` fix item, a `revise` hand-back and a struck plain-wording entry are three names for related decisions. They live in three record shapes. One query now lists all three, but only as decisions; nothing says which grade each stop holds.

That costs two things. The same kind of finding can get different handling depending on which procedure meets it. And the operator's decisions, which are the strongest evidence the system gets about which edits are wanted, have no class whose grade they could move. Without that, no stop can be removed on warrant, and the strike-list stops cannot finish their declared development path.

## Authority grades

An action class is a kind of action the pipeline can take: one pass's edits, one fix strategy, one disposition. Its grade says how far the pipeline goes before an operator decides. Authority is set on two axes that today's procedures mix, so the candidate grades are listed by axis.

Per item, within a run:

1. **Apply.** The edit lands in the run's text, and later stages work on it. Settled intermediate passes and full-pass body edits under `keep` already run this way.
2. **Propose, then wait.** The operator selects among proposed items before any is applied. The strike lists do this today.
3. **Hand back.** The pipeline stops on this item, and the author decides. This is a change of author, not a smaller permission: the full-pass dispositions other than `keep` and the fix procedure's `deferred` items do this today. An implementation must keep it an ownership boundary and not encode it as a stricter step on the same scale as the other two, since no evidence about a class can move an item across it.

Per run, at the boundary:

- **Approve publication.** The run produces a candidate, and the operator approves the exact final text. Both workflow commands do this today for every changed text, so an applied item never reaches the checkout on its grade alone. A grade change on this axis is a change to the publication boundary, which is a different decision from lowering an item class.

The grade of an item is not fixed by its class alone. The drift section below names a signal from the note's history across runs that routes an otherwise applicable item to hand back.

A separate authority question is who may decline a finding. The fix agent may reject a finding with recorded evidence. The full-pass packet reconciles findings and drops some. The revision assessment may simply not recommend a pass. Whether declining is a graded action is left free below, but declines must be recorded in any case: a record holding only what reached the operator cannot show a wrongly declined finding, which the learning section needs.

Claim-level changes stay at **hand back** under every option here, because ADR 080 decided that from six episodes of in-pass repair drifting toward defensible emptiness ([narrowing bought to survive review is paid for in content](../../theory/narrowing-bought-to-survive-review-is-paid-for-in-content.md)). Learning applies only to classes below that ceiling.

## An observed drift the grades must expose

ADR 080 stopped the pass from changing a claim, but it did not stop the drift that [narrowing bought to survive review](../../theory/narrowing-bought-to-survive-review-is-paid-for-in-content.md) describes; it moved the drift across runs. Under `keep`, and under the fix procedure, each run answers its findings with a scope section, a qualifier, a historical reframing or a narrower description. Each edit is justified by a finding. The note grows longer and more conditional, the warning count barely moves, and the accumulated result hides the deeper problem: the claim is wrong as titled, or the note has no contribution its neighbours do not own.

Two episodes on 2026-11-12 show the shape. Two fix passes on `kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md` added a scope section, qualifiers and a historical framing; the pair count stayed at 36 pass and 8 warn across both; the operator's answer was a generalization and a retitle, with claim-level decisions still open. One full pass on the former `kb/theory/types-give-agents-structural-hints-before-opening-documents.md` proposed `revise` with three candidate claims, each narrower than the title; the operator's answer was `delete`, because every sentence of the warranted update was owned elsewhere.

The designed antidote exists and is out of the pipeline's reach. [ADR 066](../adr/066-claims-declare-modality-in-text-and-passes-repair-mode-mismatch.md) added the ideal-type mode: keep the general first-order claim, concede its exceptions, and carry an adequacy record (declared use, omitted mechanism, consequence bound, explanatory dominance) that review attacks as content ([domain pricing routes an exception to idealization assessment](../../theory/domain-pricing-routes-an-exception-to-idealization-assessment.md)). It is the repair that answers a counterexample without shrinking the subject. ADR 080 then moved every mode conversion to the author, so the pass can only name it in a revise brief, and the brief is not required to consider it: the 2026-11-12 packet offered two universal candidates and one statistical, none ideal-type. The fix procedure cannot reach it either, for a different reason. Its [strategy taxonomy](../../instructions/fix-warnings/fix-strategy-taxonomy.md) is a set of local repairs: restore a qualifier, widen an attribution to the source, add framing, mark an extension as the note's own, acknowledge a boundary case. Several of them widen rather than narrow. What none of them does is reopen whether the claim should be retained, reformulated or deleted, and the procedure has no step that escalates when a repair lands on a claim that earlier repairs already qualified. The mechanism of the drift is therefore repeated local repair without escalation, not a taxonomy that only narrows. The validation series behind ADR 066 is the caution on the other side: mode conversion proved rare because an ideal-type landing needs its own warrant, and a claim whose first-order model has no explanatory dominance, as the structural-hints note's did not, cannot take it.

Two consequences bind the design. First, the record must be readable per note across runs, so accumulated narrowing is visible where a single run's diff cannot show it. The shipped record groups entries by note; the fix procedure's entries remain whole reports, not items. Second, growth in qualifiers, scope sections or length while the warning count holds is a candidate signal that routes the next action to **hand back** rather than **apply**; it is a signal, not a rule, until retained examples test it. The procedures for both are deliberately unspecified: the two episodes are the whole evidence base, and good procedures need more examples than that.

### Changes that stand apart from the options

Three cheap changes follow from the drift and the antidote. None needs a grade or a record, so none should wait on the larger design:

- A revise brief considers the ideal-type mode whenever its diagnosis concerns exceptions or claim modality, and states what warrant for it is present or missing. It is not required to disprove idealization first: deletion, merger or a narrower claim is sometimes the right answer, and a brief that must argue past idealization every time would carry a preservation bias of its own.
- The fix procedure gains an escalation step: when a repair lands on a claim that earlier repairs already qualified, the worker reports it for the operator instead of applying it. The step supplies what the drift lacks, a point at which local repair stops and someone asks whether the claim survives. It is an operator check, not an automatic stop: the "already qualified" condition is firmer than the untested signal above, so at this stage the worker's report and the operator's answer are the evidence that would later warrant a rule.
- The fix report and the packet gain a reflection field: the editing worker, as the first observer of the drift, states whether the edits it made suggest a problem with the claim that the edits do not address. Reflections are evidence for the record, never a disposition.

Their adoption criterion is in the last section.

## Learning toward automation

What the record can warrant is narrow, [since an accepted edit verifies the change, not the rule](../../theory/an-accepted-edit-verifies-the-change-not-the-rule.md). Each approval verifies one instance. A grade change is a claim about a class, and it needs its own verification. A publication approval is one bundle decision, never an approval of each edit behind it; the record keeps that distinction, and a loop must not undo it.

The record does not lower a grade by itself. A grade change is an operator decision, and the record supplies its evidence. Four forces shape what evidence counts.

- **Approval rate is the wrong statistic.** A class the operator approves nine times in ten is fine under a stop and unsafe without one. Lowering the grade needs a way to tell, per instance, which proposals the operator would reject, [since the augmentation-automation boundary is discrimination, not accuracy](../../theory/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md). In practice the record should yield one of two things: a check that catches the rejected kind, or a narrower class definition that excludes it. Either is then tested on retained and fresh examples, as the strike-list instruction already requires. [Warranted autonomy is bounded by oracle domain](../../theory/warranted-autonomy-is-bounded-by-oracle-domain.md), so a lowered grade covers only the narrowed class that the check or definition can assess.
- **Local justification does not check cumulative damage.** In the drift above each edit is justified by its finding, and the defect lies in the accumulation. A check that reads an edit only against its finding therefore cannot discriminate for the local repairs that add a qualifier, scope section or framing, or for `keep` edits that do the same. The route in the first point stays open to those classes only if the check also reads the note's history, which makes the per-note record a possible requirement for lowering their grade. Whether such a trajectory-aware check can be stated is a question for the first retained examples, not for this proposal.
- **The remaining decisions get harder.** As predictable classes move down, the decisions left with the operator concentrate the harder cases ([warranted transfer leaves people the hardest-to-warrant decisions](../../theory/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md)). Rates computed over all decisions then drift for reasons unrelated to any class. Evidence must be read per class.
- **Success is measured per judgment, not per hour.** Operator time may not fall, because attention moves to harder work ([increasing computational autonomy relocates human effort](../../theory/increasing-computational-autonomy-relocates-human-effort.md)). The measure of progress is how much accepted improvement each operator decision supports.

A grade that moved down needs a way back up. The [audit-a-prior-pass](../../instructions/simplification-passes/audit-a-prior-pass.md) procedure already traces a weakened passage to the finding that caused it. Sampled audits of lowered classes, with an audit failure raising the grade again, would close that loop.

The closure policy is narrower than a ban. It prohibits trust-dial automation and reduced audit sampling "from this calibration": the closing-cycle evidence of the shipped full pass. It does not foreclose automation warranted by different evidence, and this record is different evidence. Three obligations still need separate treatment in any adopting decision: removing an operator selection stop, changing the final-text closing review, and introducing retrospective audits. The audits add checking where none exists, and removing a strike-list stop leaves the closing review and the publication boundary as they are. The clause the loop does touch is the trust dial: a grade that evidence moves down and audits move up is one, even when each move is an operator decision. The adopting decision should say which of the three obligations it preserves and which it revises, and on what evidence.

## Options

**A. Shared grades over the record; the three procedures stay.** Each procedure names its stops by grade, and each record entry carries the grade and the procedure version it was taken under; the shipped entries carry neither. The full pass and the revise workflow already have the stop points; the fix procedure gains item-level entries for its `rejected` and `deferred` items, which the record now lists only as whole reports. Lowest cost, and no new composition to evaluate.
Operativity: grades are consumed where stops are decided today: the workflow code for its stops and the fix instruction for the agent. The record's reader exists; a grade decision still needs a reading procedure, at least a report an operator reads before deciding.

**B. One pipeline with three intake profiles.** Intake differs: the full method suite, fresh review warnings, or an assessment or plan. Everything after intake is shared: triage into action classes, editing at each class's grade, review after editing, and exact publication approval. The fix procedure then gains the run directory, code checks and publication boundary it now lacks, instead of editing the checkout directly.
Operativity: the review command consumes it and replaces three paths. Forces against: composing the stages hides which stage is unreliable unless each stays separately evaluable; and review after editing must scale with the edit, or a one-warning fix inherits full-pass cost.

The learning loop is orthogonal to the choice between A and B. It requires the record and grades that a decision can change, and it requires a decision on the closure policy's three obligations.

**Sequence.** A review on 2026-11-12 proposed building the record first, as a bounded evidence-gathering step, before either option. That step shipped under [ADR 130](../adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md). The record is a surface of the [unresolved frontier](../definitions/unresolved-frontier.md). Procedures for reading it come later with the frontier work; two candidate occasions are already visible, before any decision to remove a strike-list stop, and whenever repeated repairs on one note prompt another intervention. Any such reading keeps two questions apart: per note, whether repeated repairs are obscuring a claim-level problem; per action class, whether safe applications can be told from cases that need operator judgment. A moves only if that evidence shows the shared grade vocabulary earning its keep. B stays contingent on its rebuild trigger. The shared record was the motivated part; the single pipeline in code remains a hypothesis.

Oracle warrant for a lowered grade: the operator's decision, backed by a discriminating check or narrowed class tested on retained and fresh examples. That warrant stops at the class boundary as defined when the decision was made, and at the conditions of the examples. It never extends to claim-level changes.

## Free choices

- The unit of an action class: a pass, a fix strategy, a gate, a finding kind, or a combination.
- The grade set on the per-item axis: the three above, fewer, or a split of apply between per-edit and per-run approval.
- Whether reasons are required at every stop. For strikes the operator decided on 2026-11-13 that they are, accepting the cost per decision for the most learning input. Whether packet resolutions and publication approvals carry the same requirement is open.
- The interface for operator answers: direct edits to the proposed file, or a session in which an agent presents each item in context, asks the operator, and records the answer in the same file, approving on the operator's word. The strike list has the session procedure ([resolve a strike list](../../instructions/simplification-passes/resolve-a-strike-list.md)); the packet resolution and the publication approval could take the same shape, since each is a proposed file and an answer.
- The retention of operator answers in the state tree, where [ADR 130](../adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md) keeps the record. The record is as durable as the state repository's commit cadence, which the [public state repository workshop](../../work/public-state-repository/README.md) still owns. One force remains open against that default: operator answers, unlike run bundles, cannot be regenerated by rerunning a workflow, so their retention bar is higher than the tree's. Whether a reading promotes read entries into the tracked record is deferred with the reading procedures to the frontier work named under the sequence.
- Whether declining a finding is a graded action or stays with the procedure that met it. Recording the decline is not free: without it the record is censored to what reached the operator.
- Whether the fix procedure becomes a workflow command under option B or stays agent-run under option A.

## Adoption criteria

- **Drift changes:** the next revise hand-back or fix pass on a note that already carries one pass's qualifiers; the brief, escalation and reflection changes cost one instruction edit each and need no other trigger.
- **Option A:** a strike-list stop is to be removed, or a logged case in `kb/log.md` shows the same finding kind handled inconsistently across two procedures.
- **Option B:** one of the three procedures needs its editing, review or publication path rebuilt, or the fix procedure is to become headless. Build on a shared path then rather than adding a fourth.
- **Learning loop:** one class has enough recorded decisions that a discriminating check or narrowed definition can be stated and tested on fresh examples, and a decision has revisited the closure policy's trust-dial clause.

---

Relevant Notes:

- [Review architecture](../review-architecture.md) — part-of: the review workflows and run directories every option extends
- [Gate learning from accepted edits](./gate-learning-from-accepted-edits.md) — compares-with: mines new gates from accepted edits, where this proposal moves authority grades on existing action classes; both rest on the same instance-versus-rule oracle limit
- [Run a full improvement pass on one note](../../instructions/run-full-improvement-pass-on-note.md) — procedure: the full pass's dispositions, closing cycle and publication boundary
- [Fix system](../../instructions/FIX-SYSTEM.md) — procedure: the fix pipeline whose deferred items have no reader today
- [Simplification passes](../../instructions/simplification-passes/README.md) — procedure: the revision workflow and its temporary strike-list stops
- [ADR 127](../adr/127-review-runs-as-workflows-over-result-files.md) — decided-by: run directories and result files, where per-run decision entries live
- [ADR 130](../adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md) — decided-by: the operator-decision record whose entries a grade decision would read

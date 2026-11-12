---
description: "Proposal: treat the full pass, the fix procedure and the simplification passes as one improvement pipeline whose action classes carry graded operator authority, with one operator-decision record as evidence for moving a class toward automation"
type: reference/types/design-proposal.md
tags: [review-system, warranted-autonomy]
---

# One improvement pipeline with graded authority

Commonplace has three ways to improve one note after review: the full improvement pass, the fix procedure for review warnings, and the simplification passes. Each turns findings into bounded edits, and each stops somewhere for an operator. They draw that operator boundary in different places, name it differently, and record the operator's answer in different places or not at all. So nothing can tell which kinds of edit the operator reliably accepts, and no stop can move with evidence.

This proposal has two parts. The first is one pipeline in which each class of action carries an authority grade: how far the pipeline may go before an operator decides. The second is one operator-decision record that keeps every decision taken at those grades, as the evidence a later grade change needs. Both are options; no choice is made here.

## Current state (as of 2026-11-12)

| | Full pass | Fix procedure | Simplification passes |
|---|---|---|---|
| Entry | `commonplace-review run full-pass` | agent follows [fix review warnings](../../instructions/fix-warnings/fix-review-warnings.md); no workflow command | `commonplace-review run revise` with `--assess` or `--plan` |
| Finding source | six method families over the note, reconciled into a packet | fresh `warn`/`fail` review results | an assessment, or a fixed plan |
| Edit bound | body edits that keep the claim; copyedit | framing, accuracy and attribution; no argument change | per-pass preserve rules; `defend` claims |
| Review after editing | closing cycle; at most one repair | re-run the gate sweep | none beyond code checks on each text |
| Operator stops | hand-back dispositions; `--direction` for an undetermined update; exact publication approval | `deferred` items | strike lists for plain-wording and abstractions; exact publication approval |
| Where the operator's answer is kept | packet resolution fields with rationale, under [resolve a full-pass disposition](../../instructions/resolve-full-pass-disposition.md) | the agent's own `rejected` and `deferred` statuses in the fix report; nothing consumes deferred items | the proposed and approved strike list inside the run directory, with no reason |

Shipped constraints this proposal must respect:

- [ADR 080](../adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md) keeps every claim-level change with the author. The pass never changes a title, thesis or title-as-claim.
- The strike-list stops are declared temporary procedure-development points. The instruction already asks for proposed, accepted and rejected choices with their reasons, and for evaluation on retained and fresh examples before a stop is removed. The code records proposed and approved lists per run. It captures no reasons, and nothing aggregates across runs.
- [Full improvement pass closure](../full-improvement-pass-closure.md) states as policy: do not build trust-dial automation or reduced audit sampling from the closing calibration.
- The [review system](../README-REVIEW-SYSTEM.md) asks that each operation be evaluated alone before its composition is trusted. Reliable replay does not establish reliable selection or editing judgment.
- One full pass on one short note cost 27 launches and $4.47. A fix on one warning is a single agent edit.

## The problem

The three procedures share a structure but not a vocabulary. A finding arrives. Something decides whether it applies. An editor changes text within a bound. Something re-reviews, and an operator approves, strikes or takes over. Today a `deferred` fix item, a `revise` hand-back and a struck plain-wording entry are three names for related decisions. They live in three record shapes, and one of them has no reader.

That costs two things. The same kind of finding can get different handling depending on which procedure meets it. And the operator's decisions, which are the strongest evidence the system gets about which edits are wanted, are scattered or discarded. Without that evidence, no stop can be removed on warrant, and the strike-list stops cannot finish their declared development path.

## Authority grades

An action class is a kind of action the pipeline can take: one pass's edits, one fix strategy, one disposition. Its grade says how far the pipeline goes before an operator decides. A candidate set of grades, ordered from most to least autonomous:

1. **Apply.** The edit lands in the run's text, and later stages work on it. Settled intermediate passes and full-pass body edits under `keep` already run this way.
2. **Apply, then approve publication.** The run produces a candidate, and the operator approves the exact final text. Both workflow commands do this today for changed text.
3. **Propose, then wait.** The operator selects among proposed items before any is applied. The strike lists do this today.
4. **Hand back.** The pipeline stops, and the author decides. The full-pass dispositions other than `keep` and the fix procedure's `deferred` items do this today.

A separate authority question is who may decline a finding. The fix agent may reject a finding with recorded evidence. The full-pass packet reconciles findings and drops some. The revision assessment may simply not recommend a pass. A unified design has to say whether declining is itself a graded action.

Claim-level changes stay at **hand back** under every option here, because ADR 080 decided that from six episodes of in-pass repair drifting toward defensible emptiness ([narrowing bought to survive review is paid for in content](../../theory/narrowing-bought-to-survive-review-is-paid-for-in-content.md)). Learning applies only to classes below that ceiling.

## An observed drift the grades must expose

ADR 080 stopped the pass from changing a claim, but it did not stop the drift that [narrowing bought to survive review](../../theory/narrowing-bought-to-survive-review-is-paid-for-in-content.md) describes; it moved the drift across runs. Under `keep`, and under the fix procedure, each run answers its findings with a scope section, a qualifier, a historical reframing or a narrower description. Each edit is justified by a finding. The note grows longer and more conditional, the warning count barely moves, and the accumulated result hides the deeper problem: the claim is wrong as titled, or the note has no contribution its neighbours do not own.

Two episodes on 2026-11-12 show the shape. Two fix passes on `kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md` added a scope section, qualifiers and a historical framing; the pair count stayed at 36 pass and 8 warn across both; the operator's answer was a generalization and a retitle, with claim-level decisions still open. One full pass on the former `kb/theory/types-give-agents-structural-hints-before-opening-documents.md` proposed `revise` with three candidate claims, each narrower than the title; the operator's answer was `delete`, because every sentence of the warranted update was owned elsewhere.

The designed antidote exists and is out of the pipeline's reach. [ADR 066](../adr/066-claims-declare-modality-in-text-and-passes-repair-mode-mismatch.md) added the ideal-type mode: keep the general first-order claim, concede its exceptions, and carry an adequacy record (declared use, omitted mechanism, consequence bound, explanatory dominance) that review attacks as content ([domain pricing routes an exception to idealization assessment](../../theory/domain-pricing-routes-an-exception-to-idealization-assessment.md)). It is the repair that answers a counterexample without shrinking the subject. ADR 080 then moved every mode conversion to the author, so the pass can only name it in a revise brief, and the brief is not required to consider it: the 2026-11-12 packet offered two universal candidates and one statistical, none ideal-type. The fix procedure cannot reach it at all. Its [strategy taxonomy](../../instructions/fix-warnings/fix-strategy-taxonomy.md) holds scope-narrowed, qualifier-dropped, hedge and boundary-case-acknowledged: every move narrows, so a fix pass drifts by construction. The validation series behind ADR 066 is the caution on the other side: mode conversion proved rare because an ideal-type landing needs its own warrant, and a claim whose first-order model has no explanatory dominance, as the structural-hints note's did not, cannot take it.

Three consequences for this design, plus one from the antidote: a revise brief should state why the general claim cannot be kept as an idealization before it offers narrower candidates, and the fix taxonomy should either gain a route to that question or declare that it only narrows. First, the record must be readable per note across runs, so accumulated narrowing is visible where a single run's diff cannot show it. Second, growth in qualifiers, scope sections or length while the warning count holds is a candidate signal that routes the next action to **hand back** rather than **apply**; it is a signal, not a rule, until retained examples test it. Third, the editing worker is the first observer of this drift and should say so: a reflection field in the fix report and the packet, stating whether the edits it made suggest a problem with the claim that the edits do not address. Reflections are evidence for the record, never a disposition. The procedures here are deliberately unspecified: the two episodes are the whole evidence base, and good procedures need more examples than that.

## The operator-decision record

Each decision at a grade boundary becomes one entry. The entry holds what was proposed, the operator's answer (approve, strike, reject, take over or apply an alternative), any reason given, and enough identity to replay the case: the action class, the finding, and the texts involved. The packet resolution fields and the strike lists already hold parts of this. The record unifies their shape and makes them readable across runs.

What the record can warrant is narrow, [since an accepted edit verifies the change, not the rule](../../theory/an-accepted-edit-verifies-the-change-not-the-rule.md). Each approval verifies one instance. A grade change is a claim about a class, and it needs its own verification.

## Learning toward automation

The record does not lower a grade by itself. A grade change is an operator decision, and the record supplies its evidence. Three forces shape what evidence counts.

- **Approval rate is the wrong statistic.** A class the operator approves nine times in ten is fine under a stop and unsafe without one. Lowering the grade needs a way to tell, per instance, which proposals the operator would reject, [since the augmentation-automation boundary is discrimination, not accuracy](../../theory/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md). In practice the record should yield one of two things: a check that catches the rejected kind, or a narrower class definition that excludes it. Either is then tested on retained and fresh examples, as the strike-list instruction already requires. [Warranted autonomy is bounded by oracle domain](../../theory/warranted-autonomy-is-bounded-by-oracle-domain.md), so a lowered grade covers only the narrowed class that the check or definition can assess.
- **The remaining decisions get harder.** As predictable classes move down, the decisions left with the operator concentrate the harder cases ([warranted transfer leaves people the hardest-to-warrant decisions](../../theory/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md)). Rates computed over all decisions then drift for reasons unrelated to any class. Evidence must be read per class.
- **Success is measured per judgment, not per hour.** Operator time may not fall, because attention moves to harder work ([increasing computational autonomy relocates human effort](../../theory/increasing-computational-autonomy-relocates-human-effort.md)). The measure of progress is how much accepted improvement each operator decision supports.

A grade that moved down needs a way back up. The [audit-a-prior-pass](../../instructions/simplification-passes/audit-a-prior-pass.md) procedure already traces a weakened passage to the finding that caused it. Sampled audits of lowered classes, with an audit failure raising the grade again, would close that loop. That meets the closure document's policy against reduced audit sampling head-on: adopting it needs a decision that revisits that policy for authority grades.

## Options

**A. Shared grades and one record; the three procedures stay.** Each procedure names its stops by grade and writes the same record. The full pass and the revise workflow already have the stop points; the fix procedure gains a record of its `rejected` and `deferred` items that someone reads. Lowest cost, and no new composition to evaluate.
Operativity: grades are consumed where stops are decided today: the workflow code for its stops and the fix instruction for the agent. The record has no consumer yet; one must be built, at least a report an operator reads before a grade decision.

**B. One pipeline with three intake profiles.** Intake differs: the full method suite, fresh review warnings, or an assessment or plan. Everything after intake is shared: triage into action classes, editing at each class's grade, review after editing, and exact publication approval. The fix procedure then gains the run directory, code checks and publication boundary it now lacks, instead of editing the checkout directly.
Operativity: the review command consumes it and replaces three paths. Forces against: composing the stages hides which stage is unreliable unless each stays separately evaluable; and review after editing must scale with the edit, or a one-warning fix inherits full-pass cost.

**C. Record only.** Keep every procedure as it is and build only the cross-run record, as a research instrument for a later grade decision.
Operativity: its only consumer is the operator's periodic reading. A record with no named reading occasion changes nothing, so adoption must name one.

The learning loop is orthogonal to the choice among A, B and C. It requires the record and grades that a decision can change, and it requires a revisit of the closure policy for its audit half.

Oracle warrant for a lowered grade: the operator's decision, backed by a discriminating check or narrowed class tested on retained and fresh examples. That warrant stops at the class boundary as defined when the decision was made, and at the conditions of the examples. It never extends to claim-level changes.

## Free choices

- The unit of an action class: a pass, a fix strategy, a gate, a finding kind, or a combination.
- The grade set: the four above, fewer, or a split of grade 2 between per-edit and per-run approval.
- Whether reasons are optional. A required reason on every strike raises the cost per operator decision that this design is meant to lower.
- Where the record lives: entries kept in each run directory and aggregated by a query, or one append-only record under `kb/reports/`.
- Whether declining a finding is a graded action or stays with the procedure that met it.
- Whether the fix procedure becomes a workflow command under option B or stays agent-run under option A.

## Adoption criteria

- **Option A or C:** the operator moves to remove a strike-list stop, since the instruction already requires the evidence a record would hold; or a recorded case shows the same finding kind handled inconsistently across two procedures.
- **Option B:** one of the three procedures needs its editing, review or publication path rebuilt, or the fix procedure is to become headless. Build on a shared path then rather than adding a fourth.
- **Learning loop:** one class has enough recorded decisions that a discriminating check or narrowed definition can be stated and tested on fresh examples, and a decision has revisited the closure policy on audit sampling.

---

Relevant Notes:

- [Review architecture](../review-architecture.md) — part-of: the review workflows and run directories every option extends
- [Gate learning from accepted edits](./gate-learning-from-accepted-edits.md) — compares-with: mines new gates from accepted edits, where this proposal moves authority grades on existing action classes; both rest on the same instance-versus-rule oracle limit
- [Run a full improvement pass on one note](../../instructions/run-full-improvement-pass-on-note.md) — procedure: the full pass's dispositions, closing cycle and publication boundary
- [Fix system](../../instructions/FIX-SYSTEM.md) — procedure: the fix pipeline whose deferred items have no reader today
- [Simplification passes](../../instructions/simplification-passes/README.md) — procedure: the revision workflow and its temporary strike-list stops
- [ADR 127](../adr/127-review-runs-as-workflows-over-result-files.md) — decided-by: run directories and result files, where per-run decision entries would live

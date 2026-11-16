---
type: reference/types/design-proposal.md
description: "Proposal: revise a note's write brief through a recorded operator decision instead of an unrecorded hand edit, so that changes to what a note must keep leave the same record as changes to the note"
tags: [review-system]
---

# Recorded revision of write briefs

A note's [write brief](../../types/write-brief.md) states what the note must do, keep and exclude. The improvement procedures and the rewrite workflow treat it as binding. A change to the note goes through a candidate, a diff and the operator's recorded approval of the exact text. A change to the brief goes through none of these: a session agent edits the file after the operator agrees in conversation, and the commit is the only record.

The outcome sought is that a change to what a note must keep is proposed, decided and recorded in the way a change to the note is. The explanatory conjecture is that the brief will be amended more often now that every procedure reads it, and that an amendment decides more than one edit does, because it binds every later write. If that holds, the brief is the place where an unrecorded change costs most.

This proposal holds the options. The operator's direction on 2026-11-16 is to keep the hand edit for now and to decide after the procedures have produced more cases.

## Current state (as of 2026-11-16)

- **The brief binds.** Ordinary writing (`cp-skill-write`), the four improvement procedures on `commonplace-review run revise` and the rewrite workflow (`commonplace-review run rewrite`, [ADR 136](../adr/136-note-rewrites-run-as-a-workflow-that-ends-at-operator-approval.md)) give a note's brief to their workers as retained intent. A run captures the brief at its start and does not publish when the brief file has changed since.
- **A run adds to the brief and does not restate it.** A revise plan's `must-keep` lists only what the run adds to the brief's Must keep, and the assessor stops the plan when the purpose conflicts with the brief. A rewrite commission for a note with a brief holds the sources, the current direction and any additions, and names a brief item the operator amended.
- **A brief is amended by hand.** The write-brief type says a brief binds "until a user amends it". The writing skill has the agent update the brief in the same write when a request conflicts with it. The multistage skill has the session agent amend the brief with the operator before a rewrite run, and write or update it afterwards from the commission. No code writes a brief.
- **Nothing records the amendment.** `commonplace-review decisions` lists decisions on proposed edits, on findings and on publication. An agreement to change a brief is not among them.
- **Editing a brief has no review or freshness consequence**, by the type's own statement. Nothing checks the current note against a changed brief.
- **Briefs are few.** Nine files in the repository declare a brief.
- **Three things can prompt an amendment, and none does so systematically.** A role report can show that other notes rely on a term or claim the brief does not keep. The skill and the review-system guide tell the session agent to offer such an addition to the operator. A rewrite commission can add to or amend the brief. An operator's rejection of a proposed edit can state a rule that applies to later writes ("the metaphor is easy - don't change").

## What is uncertain

Whether the problem is large enough to build for. On 2026-11-16 the three notes that went through improvement runs had no brief, and the one rewrite ran on a note without one. No brief amendment has yet been lost, disputed or regretted. The case for a recorded revision is an expectation, not an observation.

## Options and consumers

The options differ in what records the decision and what applies it. All keep the rule that an agent never changes a brief on its own judgment.

**A. Keep the hand edit.** The session agent proposes, the operator agrees in conversation, the agent edits the brief, and the commit records it. Consumers: the session agent, through the writing and multistage skills. This is current behaviour and costs nothing. It leaves the operator's reason only in the conversation, and it cannot be listed.

**B. A brief amendment is a set of decided items.** A proposed amendment is a list of items, each one addition, removal or change of one brief entry, with its source: a role report, a commission, an earlier decision or the operator's request. The operator decides each item in an [answers](../../types/answers.md) file, as for proposed edits. Approved items are applied to the brief. Consumers: the session agent through the item-decision instruction, the validator through the answers type, and the decision record. It needs a new kind of question for the answers type, and something that applies an approved item to a brief: code for a fixed item format, or an agent for free-form items.

**C. A brief amendment is a candidate text.** The amended brief is produced as a whole candidate, with a diff against the current brief, and goes through the publication stop the note workflows use: the operator approves the exact text, or accepts it with a revision. Consumers: the publication code and the text-approval instruction, both existing. It needs the runner to accept a brief as the artifact, which today it does not: a brief has no brief, and the candidate checks assume a note. It records one decision per amendment, not one per entry.

**D. Do not revise the brief; pass the decisions.** The brief stays as first written. What the operator decides later reaches workers as earlier decisions and as the role report, which the procedures already pass. Consumers: the workers, through inputs that exist. It needs nothing built. It leaves the brief incomplete as a statement of intent, and it loses anything decided outside a run.

B and C can combine: items for what is proposed, one approved text for what is written.

**A rival decomposition.** The options above treat the brief as one file with one revision route. The alternative is to split it by who may change each part. Intent and reserved decisions would change only by the operator's direct word. Must keep and must exclude would be maintained from recorded decisions and role reports through B. Nothing yet shows that the parts are amended at different rates or by different routes, so this stays an open region.

## Forces and choices left open

- **A brief must stay short.** The type forbids restating the document. If each rejected wording becomes a "must keep" entry, the brief grows into a list of sentences. Options B and D differ here: D keeps such decisions out of the brief, B needs a rule for which decisions rise to a brief entry.
- **Creating a brief and amending one may be one act or two.** Most notes have no brief. A recorded route that covers only amendment would leave the first brief, the more consequential write, unrecorded.
- **Whether a changed brief should prompt a check of the note.** A new "must keep" entry can already be violated by the current text. Today nothing looks. A check would be a review operation with the brief as its criterion; none exists.
- **Whether an amendment may happen inside a run.** Today a changed brief stops a run. A rewrite whose commission amends the brief has the agent amend it before the run. Allowing an amendment as a step of a plan would let one run carry both, and would need the run to rebind to the new brief.
- **Who proposes.** A role report, a commission and a rejection reason are three sources with different reliability. A design can accept proposals from all three or only from the operator.

## Adoption criteria

The choice returns to decision when the procedures have run on notes that have briefs. The records to read are the run directories and the decision record. What would change the selection:

- Amendments that were agreed in conversation and later could not be reconstructed, or were made without the operator's word, argue for B or C over A.
- Runs stopped or restarted because a brief changed underneath them argue for allowing an amendment inside a run.
- Role reports that repeatedly list relied-on terms missing from briefs argue for a systematic source of proposals, which only B gives.
- Earlier decisions that workers follow without any brief entry argue for D, and against building a route.
- Briefs that grow with each run argue for a rule on what rises to a brief entry before any route is built.

Until then option A stays in force. It remains feasible however the others are decided, and switching from it costs no migration, because a brief amended by hand is an ordinary brief.

## Commitment

Adopting B or C would commit session agents to a stop for every brief change and the answers type or the runner to a new artifact kind. Either is reversible at the cost of the code and instruction changes, since the briefs themselves keep their format.

---

Relevant Notes:

- [Full write briefs cut edit drift; one-line briefs did not](../../theory/evidence/full-write-briefs-cut-edit-drift-one-line-briefs-did-not.md) — rests-on: why the brief's keep and exclude entries carry its value, and so why changes to them matter
- [Authority grades and learning from operator decisions](./authority-grades-and-learning-from-operator-decisions.md) — see-also: the proposal that owns what recorded operator decisions are used for

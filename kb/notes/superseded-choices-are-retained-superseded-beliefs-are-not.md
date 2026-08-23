---
description: "Retention after supersession follows remaining truth role rather than maintenance operation: preserve a witness to the choice event, while a refuted belief loses subject-matter standing"
type: kb/types/note.md
traits: [title-as-claim]
tags: [kb-maintenance, artifact-analysis, foundations]
---

# Superseded choices need a historical witness; refuted beliefs lose subject-matter standing

When a system refutes a belief about some subject matter, the displaced
assertion loses standing. It was wrong, and the fact that the system once held
it makes nothing about the subject true. When a system supersedes a residual
choice, the earlier prescription stops governing, but the choice event remains
true: the system committed to X at t. At least one reliable witness to that
event must survive when no other retained artifact can reconstruct it.

The asymmetry comes from the role that remains after displacement. A belief
answers to evidence independent of what the system once thought. A choice event
answers to the act of choosing. Supersession does not keep the old prescription
current, but it cannot undo that act. Destroying every reliable witness does
not make the past event false; it only makes the event unavailable to a later
bounded reader.

## What "no standing" rules out

"The system held B at time t" is itself truth-apt and can be worth retaining.
That is a historical observation about the system, not the refuted assertion
about B. It earns retention on evidence about the past, like any other belief.
A time-indexed subject-matter claim that remains true also falls outside the
refuted case. Replacing current guidance does not falsify a claim about an
earlier time.

The choice side also contains two roles. "The system committed to X at t"
remains the same true event-fact after supersession. "Do X now" may be the old
choice's expired prescription and has no current authority. The obligation is to
keep the event checkable, not to keep treating the displaced prescription as
operative. A refuted belief must therefore re-earn retention in some other
role, while a genuine choice event keeps historical standing.

## Production relation selects the operation, not what must survive

[Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md)
draws the production boundary at whether source material plus the consumer goal
determines the retained content. A change to determining inputs calls for
refresh or re-derivation. Changing an addition the inputs did not determine
calls for a later commitment or supersession.

That production relation selects the maintenance operation. It does not settle
what, if anything, must survive displacement. An ampliative conjecture is a
committed addition because its sources do not determine it, but what it asserts
remains a belief. If later evidence refutes it, the current theory should be
rewritten. Preserving the old wording as history is a separate retention
decision. A residual choice is also committed, but its event-fact remains true
after supersession and therefore needs a reliable witness.

Timing makes that witness load-bearing. Since
[history has one chance to become checkable](./history-has-one-chance-to-become-checkable.md),
an unrecorded choice is often not reconstructable from the artifacts it shaped.
Those artifacts may show the winning option without showing that a decision was
taken, which alternatives remained live, or which forces were weighed. Other
contemporaneous records can satisfy the obligation when they preserve those
facts. The requirement is at least one reliable witness, not every duplicate.

## Two maintenance regimes follow

A record of choices grows by appending: each supersession adds a link in a chain
whose earlier events stay readable and true. A body of beliefs is reworked
holistically: when evidence changes the understanding, the current text states
what is now believed. Prior wording remains only when a separate historical use
earns its retention.

Commonplace shows that both regimes can coexist. Decision records carry
lifecycle status, `supersedes`/`superseded-by` edges, and the alternatives that
lost. Theoretical notes instead rewrite refuted claims, leaving version control
to retain bytes without granting them standing. Its
[proposal archiving decision](../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md)
also shows that a superseded choice can leave the active frontier while its
historical witness survives. This instance establishes feasibility, not unique
correctness.

## Scope

Where applicable requirements, constraints, and beliefs determine a selection
uniquely, no residual choice was made. The apparent choice is a derivation
recoverable from its determining inputs. Dropping its record costs
recomputation, not the history of a free selection.

Where a belief's subject matter is the system's own commitments, the historical
proposition may remain true. The same is possible for a subject-matter claim
whose explicit time index remains true after current guidance changes. Neither
case is a refuted belief retaining standing it lost.

Mixed artifacts require region-level treatment. An ADR can contain a choice
event, an expired prescription, and truth-apt rationale. Retaining the artifact
keeps a witness to the first without granting equal standing to every region.
A belief that was responsibly warranted at t may likewise deserve preservation
as evidence of a past knowledge state, but that historical use must earn its own
place.

The obligation is against losing every reliable witness, not against deleting a
duplicate or demoting history from active attention. Which maintenance
operation applies remains keyed to production relation by
[artifact classification](./artifact-classification-separates-content-kind-lineage-and-authority.md).

---

Relevant Notes:

- [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — extends: splits its commitment column by remaining content role, so supersession does not itself decide which historical witness must survive
- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md) — grounds: why an unrecorded choice is not reconstructable later, which is what makes the retention obligation bite
- [Artifact classification separates content kind, lineage, and authority](./artifact-classification-separates-content-kind-lineage-and-authority.md) — contrasts: assigns the maintenance operation to production relation, where this note asks which truth role and witness survive that operation
- [A compact, refreshable whole-picture narrative can replace infeasible fragment reconciliation](./evolving-understanding-needs-holistic-rewrite-not-composition.md) — mechanism: describes the holistic-rewrite regime this note assigns to beliefs, including why appended pivot logs are the wrong shape for it
- [Retire, redact, supersede, and relax memory](./agent-memory-requirements/retire-redact-supersede-relax.md) — contrasts: lifecycle states answer "what is current?" while temporal memory answers "what was true then?", a second reason to retain history that is orthogonal to the standing question here
- [ADR type specification](../reference/types/adr.md) — evidenced-by: the append-only decision-record contract preserves the choice event and alternatives even after its prescription loses current authority

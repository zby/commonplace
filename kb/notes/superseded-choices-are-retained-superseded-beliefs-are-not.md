---
description: "Retention obligations follow content kind rather than the commitment boundary: a displaced belief keeps no standing in its own role, while a superseded choice stays the only record of what the system committed to"
type: kb/types/note.md
traits: [title-as-claim]
tags: [kb-maintenance, artifact-analysis, foundations]
---

# Superseded choices are retained; superseded beliefs are not

When a system revises a belief, the version it displaces keeps no standing.
It was wrong, and the system's having held it makes no claim about the subject
matter true. When a system supersedes a choice, the choice it displaces stays a
fact about what that system committed to, and after the fact the record is the
only thing carrying it.

The asymmetry follows from what each is answerable to. A belief answers to
evidence, and evidence is indifferent to what anyone previously thought — the
displaced version was already false while it was held, so discarding it removes
no truth about its subject. A choice answers to nothing outside the act of
choosing. The act is the only thing that ever made it true, so deleting the
record deletes the fact.

## What "no standing" rules out

"The system held B at time t" is itself truth-apt and can be worth retaining.
The asymmetry is not that a displaced belief disappears while a displaced choice
persists. It is that the two persist in different roles, when they persist at
all.

A displaced belief survives, if it survives, as a *different* proposition: a
historical observation about the system, answerable to evidence about the past,
and earning its retention on that evidence like any other belief. What it stops
being is something the system asserts about the subject matter. A superseded
choice survives as *itself* — the same proposition, that this system committed
to X at t, stays true after supersession, because supersession is a later act
rather than a discovery that the earlier act did not happen. So a displaced
belief has to re-earn its place, while a superseded choice does not lose the
standing it already had.

## The obligation attaches to the choice, not to the commitment

[Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md)
puts supersession, and irrecoverable loss on deletion, on the commitment side of
the production boundary. That boundary settles which artifact a consumer should
treat as authoritative. It does not by itself settle whether the displaced
version has to survive, and the two questions come apart because commitment and
residual choice are different categories: an ampliative conjecture adds content
its sources do not determine, so producing it is a commitment, while what it
asserts remains a belief.

A conjecture later found wrong is therefore rewritten in place rather than
displaced by a record naming it. No free selection had the old text as its only
witness — the conjecture was answerable to evidence throughout, and evidence
still supplies the answer. Within committed content, the retention obligation
tracks content kind, and the residual-choice part is what carries it.

The obligation bites because of timing. Since
[history has one chance to become checkable](./history-has-one-chance-to-become-checkable.md),
a choice not recorded when it was made is generally not reconstructable
afterwards from the artifacts it shaped: those artifacts show the option that
won, not that a decision was taken or which alternatives were live. This is what
makes the record load-bearing — a later reader needs it to tell a deliberate
reversal from an accident, and to know which forces a revisit would have to
re-weigh.

## Two maintenance regimes follow

A record of choices grows by appending: each supersession adds a link in a chain
whose earlier entries stay readable and stay true. A body of beliefs is reworked
holistically: when understanding changes, the current text is rewritten to state
what is now believed, and no residue of the prior wording is preserved as a
record of anything.

Commonplace is one system where both regimes are visible and separated. Its
decision records carry a lifecycle status, `supersedes`/`superseded-by` edges,
and a requirement to state the alternatives that lost, so a superseded decision
remains readable in place. Its theoretical notes have no supersession label in
their link vocabulary at all: a note whose claim stops holding is rewritten, and
the displaced text is left to version control, which retains bytes without
granting them standing. The instance is a witness that the two regimes can be
run side by side in one retention system, not evidence that this arrangement is
uniquely correct.

Retention is also not the same as frontier attention. A superseded choice can be
archived out of the actively-consulted set while keeping its standing — which is
what Commonplace's
[proposal archiving decision](../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md)
chose. The obligation this note states is against destruction, not against
demotion.

## Scope

Vary the premise and the conclusion moves with it. Where applicable
requirements, constraints, and beliefs determine a selection uniquely, no
residual choice was made: the apparent "choice" is a derivation, recoverable
from its determining inputs, and dropping its record costs a recomputation
rather than a fact. The retention obligation appears exactly when the inputs
leave options live.

The reverse case is not an exception either. Where a belief's subject matter is
the system's own commitments, the historical proposition is retained — but it
was a belief about a particular all along, not a displaced belief clinging to
standing it lost.

This note says what happens to displaced *content*. Which maintenance
*operation* applies — refresh, re-derivation, or supersession — is keyed on the
production relation by
[artifact classification](./artifact-classification-separates-content-kind-lineage-and-authority.md),
and that operation does not determine the fate of what it displaces.

## Open Questions

- Does a recorded retraction sit on the choice side? Retracting is an act, so a
  record of it looks like a fact about what the system did rather than a
  displaced belief — which would make retraction a commitment rather than the
  bare removal of one.
- Where does a belief that was warranted on the evidence available then, and is
  wrong now, belong? It looks like a belief with a retained past. Reading its
  warrant-at-t as a gated acceptance would move that part to the choice side
  without any new evidence arriving.

---

Relevant Notes:

- [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — extends: splits its commitment column by content kind, so supersession-and-retain applies to the residual choice rather than to every committed addition
- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md) — grounds: why an unrecorded choice is not reconstructable later, which is what makes the retention obligation bite
- [Artifact classification separates content kind, lineage, and authority](./artifact-classification-separates-content-kind-lineage-and-authority.md) — contrasts: assigns the maintenance operation to the production relation, where this note asks what becomes of the content that operation displaces
- [A compact, refreshable whole-picture narrative can replace infeasible fragment reconciliation](./evolving-understanding-needs-holistic-rewrite-not-composition.md) — mechanism: describes the holistic-rewrite regime this note assigns to beliefs, including why appended pivot logs are the wrong shape for it
- [Retire, redact, supersede, and relax memory](./agent-memory-requirements/retire-redact-supersede-relax.md) — contrasts: lifecycle states answer "what is current?" while temporal memory answers "what was true then?", a second reason to retain history that is orthogonal to the standing question here
- [ADR type specification](../reference/types/adr.md) — evidenced-by: the append-only decision-record contract — supersession status plus a required record of the alternatives that lost — as the choice-side regime in operation

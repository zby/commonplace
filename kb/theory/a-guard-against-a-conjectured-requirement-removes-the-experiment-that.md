---
description: "A guard against an unstated requirement holds the condition at the value where the conjecture and its negation agree, so it immunizes the conjecture; explains why test-selected agents guard by default and when omitting is the cheaper experiment"
type: types/note.md
traits: [title-as-claim, has-external-sources]
tags: [llm-reliability, evaluation, learning-theory]
---

# A guard against a conjectured requirement removes the experiment that would test it

A requirement that nobody stated but an implementer adds — "the cache must be
consistent", "this handler needs a lock", "re-check the row before writing" —
is a conjecture about the environment: that the unguarded condition would
occur and would do harm. Implementing the guard does not test that
conjecture. It fixes the condition at the one value where the conjecture and
its negation predict the same outcome. Staleness held at zero produces no
harm whether or not staleness would have harmed anyone. The only experiment
that can eliminate the conjecture is to let the condition occur and watch the
outcome, which means running without the guard, in production or in a
stand-in that can produce the harm. So a guard written against an
untested requirement removes the experiment that would test it, and the
absence of trouble afterwards corroborates nothing.

Claim mode: universal. It is refuted by a suppressing guard under
which evidence later produced in the guarded system refutes or corroborates
the conjecture the guard was written against.

## The causal reading

Treat the conjecture as a single edge in a causal graph, from the unguarded
condition to user-visible harm. Passive observation eliminates a graph only
when the data show a dependence or independence the graph forbids, and
showing either needs the condition to vary. Interventions discriminate
between graphs only at values where the graphs predict different outcomes, as
in [competing causal theories can guide distinguishing
experiments](./competing-causal-theories-can-guide-distinguishing-experiments.md).
A guard is an intervention, but at the non-discriminating value: it holds the
condition at the level where both the edge and its absence predict no harm.
It therefore blocks both routes to elimination at once. Nothing varies, so
observation cannot eliminate the edge, and the one intervention actually run
is the one that cannot distinguish.

In Popperian terms the guard immunizes the conjecture. The same vocabulary
already names this move for claims, in [domain pricing routes an exception to
idealization assessment but does not decide
it](./domain-pricing-routes-an-exception-to-idealization-assessment.md): an
adjustment that makes refuting cases stop biting while risking nothing itself.
A guard is that adjustment written in code.

## Either resolution immunizes the other conjecture

A conjectured requirement arrives with some credence, but the program is
binary: the mechanism is present or absent. Either way the implementer
commits, and because [commitment, not derivation, creates new ground
truth](./commitment-not-derivation-creates-new-ground-truth.md), the code
then carries a resolution the task never entailed. The decision rests on two
unknowns: whether the harm would occur, and what the guard costs to carry.
Each resolution runs the experiment on one unknown and suppresses the other.
Omitting the guard lets the harm occur and reveals nothing about carrying
cost. Adding the guard pays the carrying cost and reveals nothing about the
harm. Both are bold conjectures in Popper's sense, exposed to refutation by
different refuters. Each also tends to make itself true. Once later code
depends on the guarantee a guard provides, the requirement is real; once
clients have built around staleness, the non-requirement is entrenched. Sean
Goedecke describes the guarded endpoint, in [What requirements don't you
have?](../sources/sean-goedecke-what-requirements-dont-you-have.ingest.md),
as requirements that "petrify the system over time". On this note's reading,
a petrified system is one whose design conjectures have been immunized one by
one, so that evidence can no longer revise them. The same entrenchment runs
the other way, though it is rarely named, because the entrenched state is the
simpler one.

The asymmetry that remains is in the feedback channel, and it is a tendency,
not a law. An omitted guard fails as an event: a stale read, a race, a
complaint, each with a time and a suspect. A carried guard fails as a diffuse
cost, spread across every later change that works around it, mixed with the
cost of the feature it sits inside and with every other guard, and no part of
that cost names the mutex. So the refutation of the omit branch tends to
arrive soon and point at its cause, while the refutation of the guard branch
arrives late and points at nothing. Loops in which carrying costs are
attributed to individual guards as quickly and as reliably as harms are
attributed to missing ones would refute this tendency. The next section shows
the same gap acting on the implementer's oracle.

## Why test-selected implementers add guards

Two mechanisms push an automated implementer toward the guarded branch, and
they compound.

The first is missing information. Whether a stale read is acceptable is a
decision premise the owner holds and the code does not express. By [an author
should fix what the executor can't determine, not what it
will](./fix-what-the-executor-cant-determine-not-what-it-will.md), a choice
the implementer cannot settle from doctrine, commission and evidence is a gap
in the commission, and an implementer facing a gap projects an interpretation
into it. Which way the projection goes is settled by the second mechanism.

The second is oracle asymmetry, and it decides the direction. In the loops
Goedecke describes, the operative check on generated code is a test suite
plus a review that looks for bugs. That oracle penalizes a missed edge case
at once and a carried guard rarely and late, so from the implementer's side
the guard's carrying cost appears near zero. The oracle under-prices guards
for the reason the guard branch rarely meets its refuter: carrying cost
arrives late and unattributed, so no check in the loop sees it. Since [weakly discriminated
qualities tend to be
underselected](./weakly-discriminated-qualities-tend-to-be-underselected.md),
"solves only the problems this system has" is exactly the quality the loop
fails to enrich. With a carrying cost near zero, any conjecture of nonzero
credence is worth guarding. An instruction to make no mistakes raises the
perceived cost of the missed case without changing the carrying cost, so it
moves the threshold further toward guarding everything. Goedecke reports the
visible result: models "obsessed with satisfying the Grader" introduce a
mutex to keep semi-related data in sync, or a mid-flight re-check of data
already checked, without being told to. About half of the large generated
changes he reviews carry a requirement the model introduced itself.

## Where omitting the guard is the right move

The decision turns on two costs the implementer rarely holds: the cost of
carrying the guard and the cost of running the experiment, which is the cost
of being wrong once without it. Where the experiment is cheap and
reversible, omitting the guard is both the simpler design and the way to
learn whether the requirement exists, at the price of leaving the carrying
cost unmeasured. This is the regime in which [ad hoc
explanation can be rational when error is cheap and
local](./ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md):
a wrong guess costs about one iteration and nothing downstream depends on it.
Goedecke's dropped requirements are each a case where someone judged the
cost of the experiment acceptable: a stale page, a lost datapoint, a slow tail request.
Where the experiment is expensive or irreversible, keeping the guard is
rational even though it immunizes the conjecture, and the owner accepts that
the question stays open. The error is guarding by default, at a
threshold the owner never set.

A record of the untested side is the artifact this analysis calls for,
whichever way the collapse went, because [design rationale must preserve
decision premises its interpreter cannot
regenerate](./design-rationale-must-preserve-unregenerable-decision-premises.md)
and neither the credence nor the two costs can be read back from the code. A
recorded non-requirement states that the owner ran the experiment and the
conjectured requirement did not survive, or chose to run it and accepts the
exposure. It is also what lets the owner's decision reach a sub-agent: a
positive requirement is recorded in tests, and a non-requirement is recorded
nowhere unless someone writes it down.

## Scope

- The claim concerns requirements that are conjectures about the environment
  (users, load, concurrency, failure rates). Requirements the owner has stated
  as commitments are outside it, because a stated requirement has already
  been weighed.
- It concerns guards that suppress the condition. A guard that only
  observes, such as a log of stale reads, lets the condition vary and keeps
  the whole experiment. A suppressing guard with instrumentation, such as a
  counter on lock contention, measures how often the condition occurs but
  not whether it would have harmed anyone, because the consequence remains
  suppressed.
- It assumes the harm, had it occurred, would have been observable. Where
  harm is unobservable, omitting the guard runs the experiment without reading its
  result.
- The two-mechanism account of why implementers add guards is a conjecture
  about test-selected code generation, and the feedback-channel asymmetry is
  declared statistical in its section. The causal and Popperian reading of
  what a guard does to the conjecture stands without either.

## Open Questions

- Whether a generation loop can be given a nonzero carrying cost for guards
  that the oracle actually enforces, for instance by scoring diff size or
  mechanism count against the stated requirements, and whether such a score
  would be gamed in the same way tests are.
- Whether shadow execution (running the guarded and unguarded paths together
  and comparing outcomes) is a general way to run the experiment without
  bearing its full cost, or only applies where the harm is a detectable
  divergence.
- Whether a recorded non-requirement decays like other conversation-only
  constraints under compaction, or whether its presence in a decision record
  is enough to keep it delivered.

---

Relevant Notes:

- [What requirements don't you have?](../sources/sean-goedecke-what-requirements-dont-you-have.ingest.md) — abstracted-from: the observations of dropped requirements in real systems and of coding agents adding unrequested guards; the immunization reading is this note's own
- [competing causal theories can guide distinguishing experiments](./competing-causal-theories-can-guide-distinguishing-experiments.md) — mechanism: interventions discriminate only at values where rival graphs predict different outcomes
- [domain pricing routes an exception to idealization assessment but does not decide it](./domain-pricing-routes-an-exception-to-idealization-assessment.md) — grounds: the immunizing move as defined for claims
- [weakly discriminated qualities tend to be underselected](./weakly-discriminated-qualities-tend-to-be-underselected.md) — mechanism: why a test-only oracle sets the guard's carrying cost to zero
- [an author should fix what the executor can't determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md) — grounds: a non-requirement is a choice the implementer cannot settle from its commission
- [ad hoc explanation can be rational when error is cheap and local](./ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md) — extends: the cheap-and-local regime is where omitting the guard is the economical error-control policy
- [commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — grounds: either resolution of the conjecture is a commitment the task did not entail
- [current-task fit alone does not warrant costly structural entrenchment](./current-task-fit-alone-does-not-warrant-costly-entrenchment.md) — contrasts: that note prices entrenchment by reversibility; this note adds that either resolution of a conjectured requirement entrenches and hides the other's test
- [design rationale must preserve decision premises its interpreter cannot regenerate](./design-rationale-must-preserve-unregenerable-decision-premises.md) — grounds: the credence and the two costs behind a collapsed conjecture are premises the code cannot regenerate
- [silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — contrasts: an unrequested guard is a silent resolution of the spec whose success hides that the commission left the choice open

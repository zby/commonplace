---
description: "A guard against an unstated requirement fixes the cause at the value where the conjecture and its negation agree, so it immunizes the conjecture; explains why test-selected agents guard by default and when omitting is the learning move"
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
that can eliminate the conjecture is to let the condition vary, which in
software means shipping without the guard. So a guard written against an
untested requirement removes the experiment that would test it, and the
absence of trouble afterwards corroborates nothing.

The claim is universal in mode. It is refuted by a prevention guard under
which evidence later produced in the guarded system refutes or corroborates
the conjecture the guard was written against.

## The causal reading

Treat the conjecture as a single edge in a causal graph, from the unguarded
condition to user-visible harm. Passive observation eliminates a graph only
when the data show an independence the graph forbids, and that needs the
cause to vary. Interventions discriminate between graphs only at values where
the graphs predict different outcomes, as in [competing causal theories can
guide distinguishing
experiments](./competing-causal-theories-can-guide-distinguishing-experiments.md).
A guard is an intervention, but at the non-discriminating value: it sets the
cause to the level at which both the edge and its absence predict no harm.
It therefore blocks both routes to elimination at once. Nothing varies, so
observation cannot eliminate the edge, and the one intervention actually run
is the one that cannot distinguish.

In Popperian terms the guard immunizes the conjecture. The same vocabulary
already names this move for claims, in [domain pricing routes an exception to
idealization assessment but does not decide
it](./domain-pricing-routes-an-exception-to-idealization-assessment.md): an
adjustment that makes refuting cases stop biting while risking nothing itself.
A guard is that adjustment written in code.

## The two discrete outcomes are not symmetric

A conjectured requirement arrives with some credence, but the program is
binary: the mechanism is present or absent. Either way the implementer
commits, and because [commitment, not derivation, creates new ground
truth](./commitment-not-derivation-creates-new-ground-truth.md), the code
then carries a resolution the task never entailed. The two resolutions differ
in what they can teach. Omitting the guard is the bold conjecture: it exposes
the implementer to refutation by the world, and the refutation, when it
comes, is informative. Adding the guard is a commitment that cannot be
refuted from inside the running system. One branch learns and the other does
not.

Accumulation follows. Each guard freezes one open question for as long as it stands, and
later code can come to depend on the guarantee the guard provides, so the
experiment grows more expensive the longer the guard stands. Sean Goedecke
describes the endpoint, in [What requirements don't you
have?](../sources/sean-goedecke-what-requirements-dont-you-have.ingest.md), as requirements
that "petrify the system over time". On this note's reading, a petrified
system is one whose design conjectures have all been immunized, so that none
can be revised on evidence.

## Why test-selected implementers add guards

Two mechanisms push an automated implementer toward the guarded branch, and
they compound.

The first is missing information. Whether a stale read is acceptable is a
decision premise the owner holds and the code does not express. By [an author
should fix what the executor can't determine, not what it
will](./fix-what-the-executor-cant-determine-not-what-it-will.md), a choice
the executor cannot settle from doctrine, commission and evidence is a gap in
the commission, and an executor facing a gap projects an interpretation into
it. The projection lands on the safe side.

The second is oracle asymmetry, and it decides the direction. The operative
check on generated code is usually a test suite plus a review that looks for
bugs. That oracle penalizes a missed edge case and does not penalize a
carried guard, so from the implementer's side the guard's carrying cost reads
as zero. Since [weakly discriminated qualities tend to be
underselected](./weakly-discriminated-qualities-tend-to-be-underselected.md),
"solves only the problems this system has" is exactly the quality the loop
fails to enrich. With a zero carrying cost, any conjecture of nonzero
credence is worth guarding, and an instruction to make no mistakes raises the
perceived cost of the missed case without touching the carrying cost, so it
moves the threshold further toward guarding everything. Goedecke reports the
visible result: models "obsessed with satisfying the Grader" that introduce
a mutex to keep semi-related data in sync, or a mid-flight re-check of data
already checked, without being told to, and about half of the large generated
changes he reviews carrying a requirement the model introduced itself.

## Where omitting the guard is the right move

The decision turns on two costs the implementer rarely holds: the cost of
carrying the guard, and the cost of running the experiment, which is the
cost of being wrong once without it. Where the experiment is cheap and
reversible, omitting the guard is both the simpler design and the only way to
learn whether the requirement exists. This is the regime in which [ad hoc
explanation can be rational when error is cheap and
local](./ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md):
a wrong guess costs about one iteration and nothing downstream depends on it.
Goedecke's dropped requirements are each a case where someone judged the
experiment survivable: a stale page, a lost datapoint, a slow tail request.
Where the experiment is expensive or irreversible, keeping the guard is
rational even though it immunizes the conjecture, and the owner accepts that
the question stays open. The error is not guarding as such. It is guarding by
default, at a threshold the owner never set.

A recorded non-requirement is the artifact this analysis calls for. It states
that the owner ran the experiment, or chose to run it, and the conjectured
requirement did not survive. It is also the one form of the ruling that can
travel to a sub-agent, because a positive requirement leaves tests behind and
a non-requirement leaves nothing unless someone writes it down.

## Scope

- The claim concerns requirements that are conjectures about the environment
  (users, load, concurrency, failure rates), not requirements the owner has
  stated as commitments. A stated requirement has already been weighed.
- It concerns guards that suppress the condition. A guard that observes
  instead, such as a counter on lock contention or a log of stale reads,
  preserves variance in the cause and keeps part of the experiment. It can
  establish how often the condition occurs; it still cannot establish whether
  the condition would have harmed anyone, because the consequence remains
  suppressed.
- It assumes the harm, had it occurred, would have been observable. Where
  harm is silent, omitting the guard runs the experiment without reading its
  result.
- The two-mechanism account of why implementers add guards is a conjecture
  about test-selected code generation. The causal and Popperian reading of
  what a guard does to the conjecture stands without it.

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
- [an author should fix what the executor can't determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md) — grounds: a non-requirement is a choice the executor cannot settle from its commission
- [ad hoc explanation can be rational when error is cheap and local](./ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md) — extends: the cheap-and-local regime is where omitting the guard is the economical error-control policy
- [commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — grounds: either resolution of the conjecture is a commitment the task did not entail
- [current-task fit alone does not warrant costly structural entrenchment](./current-task-fit-alone-does-not-warrant-costly-entrenchment.md) — contrasts: that note prices entrenchment by reversibility; this note adds that an entrenched guard also forecloses learning
- [silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — contrasts: an unrequested guard is a silent resolution of the spec whose success hides that the commission left the choice open

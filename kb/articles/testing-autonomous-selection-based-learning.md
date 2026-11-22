---
description: "Research program article: separates membership, edit outcomes, and autonomous LLM judgment in Commonplace; defines comparisons for admission, targeted correction, criterion revision, and net gain, plus a proposed first routing-check experiment"
type: articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/theory/definitions/selection-based-learning.md
  - kb/theory/definitions/single-loop-and-double-loop-learning.md
  - kb/theory/defining-improvement-for-open-ended-work.md
  - kb/theory/selection-based-learning-needs-only-a-local-comparison.md
  - kb/theory/necessary-preference-can-guide-improvement-without-a-global-measure.md
  - kb/theory/reversibility-can-favor-a-change-by-limiting-future-loss.md
  - kb/theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/theory/false-positive-generation-is-filtered-before-retention.md
  - kb/theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md
  - kb/theory/definitions/operative-change.md
  - kb/theory/evidence/commonplace-revision-used-theory-guided-computational-search.md
  - kb/reference/commonplace-declared-frame.md
---

# Testing Autonomous Selection-Based Learning

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

An agent finds a draft filed as a finished proposal and moves it. That fixes
one document. Suppose it also compares ways to prevent the mistake, changes
its own routing instruction, and uses the new instruction on later drafts.
Now there are two questions to test: did the system change how it does its
next job, and did those jobs go better than they would have otherwise?

The [lead article](./deployment-time-machine-learning-llm-selected-updates.md)
bets that a large language model (LLM) can help find candidate changes and
discriminating checks, and can select updates without a person choosing
each one. Commonplace, an agent-operated knowledge base, gives us a place
to test that bet. A comparison on fresh work tests the value of the whole
loop. More focused comparisons distinguish finding a repair from judging
one, and changing a procedure from changing how future repairs are judged.

## Three claims, not one verdict

Three claims need different evidence.

**Membership today.** Under
[Commonplace's declared frame](../reference/commonplace-declared-frame.md)—which
specifies the people and programs counted as inside the system—Commonplace
comprises its agents, command-line tools, and human operator, editing a
store of library notes, instructions, types, validators, and code used
across tasks. For a named class of edits such as routing instructions, the
operator or an agent can reject proposals, later tasks consume what is
kept, and a misleading check can be revised for future edits. The
[2026-08-30 revision](../theory/evidence/commonplace-revision-used-theory-guided-computational-search.md)
records one such episode, with the operator selecting among candidate
revisions to Commonplace's own machinery. That establishes capacity for a
human-assisted system—a modest claim that any engineering team maintaining
a handbook also meets.

**Whether a particular edit improved the system.** Admitting a reversible edit can
be a sound decision while its payoff remains unknown
([reversibility can limit future loss](../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md)).
Whether the edit actually improved the system is a separate question, decided by
comparing fresh work with the edit against fresh work without it while
leaving the rest of the store intact except for edits that depend on it.
Fix the standard before the test. [Defining improvement for open-ended
work](../theory/defining-improvement-for-open-ended-work.md) starts with the
tasks the system will serve. Here we use [strict necessary preference](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md):
name the alternative, whose work counts, and the horizon; call the change
an improvement if every way of weighing the consequences compatible with
those commitments favors it. The judge can have grounds to expect a gain
at admission; whether a gain occurred calls for evidence from later work.

Changed behavior alone proves only that the edit mattered
([operative change](../theory/definitions/operative-change.md)), not that
it helped.

**Autonomous selection.** A retained procedure can change later work even
when the criterion for adopting it stays fixed. If the system can also
revise that criterion for future procedure changes, it has the further
capacity for [double-loop learning](../theory/definitions/single-loop-and-double-loop-learning.md).
For either claim, attribute each decision to whoever made it: if an
operator chooses the repair, the episode tests the human–machine system,
not autonomous selection.

## Three capabilities and one test of the whole loop

Testing autonomous judgment requires separating its parts so a success on
one cannot mask failure on another. Every test fixes the model, task
family, available evidence, and budget in advance and states what counts
against the prediction *for that setup*; one unsuccessful run rules out
that configuration, not all fixed-weight models.

| Capability | Comparison | What distinguishes a real gain |
|---|---|---|
| **Admission** | The model and a fixed gate receive the same proposals and evidence: useful edits the gate rejects, harmful edits it admits, and edits it handles correctly (preventing a judge that merely inverts the gate from scoring well). | Compare kept edits and their fresh-work outcomes against both the fixed gate and admitting everything. Tying the gate shows no advantage for model judgment; a persuasive rationale alone proves nothing. |
| **Targeted correction** | One harmful edit and one independently useful edit enter in the same batch; later use supplies failure evidence without naming the culprit. | Compare the learner's repair against keeping the batch and rolling the whole batch back. Without a useful edit to preserve, tying full rollback cannot separate diagnosis from indiscriminate removal. |
| **Criterion revision** | Unseen proposals are judged under both the old criterion and a retained revision to it. | Different pass/fail decisions show the criterion changed in practice. Better decisions require a separate check, since rejecting every proposal prevents every bad admission. |

Giving both judges the same candidates isolates selection. It says nothing
about whether either judge could have found the useful candidate in the
first place. [A local comparison](../theory/selection-based-learning-needs-only-a-local-comparison.md)
can select only among alternatives reached. Evidence has a similar boundary:
[the judgment companion](./can-an-llm-judge-which-changes-are-worth-making.md#testing-the-bet-without-asking-the-judge-to-grade-itself)
compares a decisive fact supplied directly, discoverable with tools, or
unavailable. Record who chose the traces, queries and checks as well as who
chose the edit.

**Check consistency of preferences, not just actions.** Present the same
two alternatives in both orders with unchanged evidence, commitments and
horizon. Strictly preferring A to B and then B to A is inconsistent.
Adopting a routing rule for a trial and removing it at review need not be:
the trial installed a rule *and* a review commitment, and the review may
have evidence that was unavailable at admission. Count the work done
under the rule even if it is later removed.

**Net gain is a separate test of the whole loop.** All three capabilities
can succeed locally while accumulated edits degrade the system overall. The
whole-loop test compares the evolving store against an otherwise matched
system running on the starting store over the same fresh work and horizon.
It counts search and evaluation compute, upkeep, human supervision, and losses incurred before rollback alongside task outcomes, watching
for costs local approvals miss: judgment errors,
[false-positive acceptance](../theory/false-positive-generation-is-filtered-before-retention.md),
[unfaithful rationales](../theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md),
and store accretion. When compatible measures pull apart, the verdict is
reported as open. Neither withholding the entire store nor showing one
successful repair establishes the net benefit of continued revision.

Even a whole-loop gain does not establish that more computation buys more
gain. That requires varying the compute budget. Nor does it establish that
[retained hypotheses save observations](../theory/retained-theories-may-improve-sample-efficiency.md): compare how many new cases each system needs after a task shift, with the same model and history but without the retained hypothesis in the comparison system. To test an explanation of a decision, intervene on the rule it names and check whether behavior changes as predicted.

## A first experiment: repairing a misleading routing check

Rather than waiting for an end-to-end automated loop, the program starts
with one focused test of criterion revision: repairing a check that lets
overbroad routing instructions pass. This is a **proposed experiment**, not
a run already commissioned or completed.

In the test, the model receives the current review check along with
execution traces in which overbroad routing lines passed that check and
later misdirected work. The experimenter has located the check and selected the traces. The model
must diagnose the failure, find a candidate repair, and decide whether to
install it. Success would not show that it could have found the relevant
traces unaided. To rule
out a model that rewrites every check it sees, the trial pairs misleading
checks with at least one sound check whose accompanying failure traces stem
from another cause, counting leaving the sound check unchanged as the
correct result.

Both the old and resulting checks are then run on the same unseen
proposals, including sound routing rules that should still pass, and fresh
downstream tasks measure both misroutes prevented and useful guidance lost.
Three observations are reported separately rather than collapsed into one
score:

1. **Operative revision:** did the revised misleading check change
   decisions on unseen proposals?
2. **Downstream gain:** did those changed decisions prevent misroutes
   without rejecting sound routing rules and degrading fresh work?
3. **Selectivity:** did the model leave the sound check alone when the
   failure traces had another cause?

Reporting them separately exposes informative mixed results—for example, a
model that fixes a faulty check well yet rewrites sound checks
unnecessarily, showing it can repair a known flaw without reliably telling
when repair is warranted. Even passing all three checks tests only
criterion revision on one failure pattern, not sustained autonomous
learning across a store. Other controlled designs appear in the
[testing supplement](./testing-whether-a-theory-builder-learns.md), which
is being re-anchored from our earlier theory-builder framing.

Every step logs who proposed, diagnosed, selected, and installed the edit.
People can design the trial and independently assess outcomes afterward
without entering the loop; a person who picks the best among several
model-drafted repairs *is* inside it, making the run human-assisted.

## Why the development path matters

Commonplace moves decisions out of the operator's hands one kind at a time,
reporting separately which operations still complete and which resulting
edits improve later work
([bootstrapping with Commonplace](./bootstrapping-autonomous-selection-based-learning.md)).
The practical payoff under test is whether a misleading check gets repaired
without waiting for a person to notice the pattern and redesign it—and
whether that saves human judgment overall once supervision and cleanup are
counted.

The same path carries the Bitter Lesson boundary: a system bootstrapped
from hand-written instructions, types, and checks scales with computation
[only if automated learning eventually outgrows that starting state](../theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md),
supplying and revising the task-specific criteria new work demands.

## Current evidence and where rivals disagree

The current evidence record is small and should not be overstated:

- **No end-to-end automated run.** Commonplace reports no completed
  demonstration of sustained autonomous double-loop learning.
- **The Python change-judgment probes.** An original six-session study
  was designed to test one model across two Python change cases but was never run. A
  follow-on design compares one model against human practitioners on a
  single CPython build-default case; three fresh model answers have been
  collected ([comparison record](../reports/retained/python-change-judgment-probe-2026-11-20/comparison/README.md)), while human replies, the independent mixed reading, and a
  second-round case variant remain pending. Even completed, that comparison
  probes stated reasons for one decision, not the downstream effect of an
  admitted edit.
- **The 2026-08-30 revision.** As noted above, the operator selected among
  candidate revisions in that episode, so it is evidence about the
  human-assisted system rather than autonomous judgment.

Rival views enter only where a specific experiment separates their
predictions. Rich Sutton and Khurram Javed argue that forming genuinely new
concepts requires continual weight updates
([Sutton and Javed](../sources/sutton-javed-why-ai-models-stop-learning.ingest.md));
because repairing a routing check need not involve forming a new concept,
passing that first test would not refute their claim. Similarly, the 2026
study
[Harness Evolution Hits a Ceiling](../sources/harness-evolution-ceiling-weight-training.ingest.md)
deferred stalled failures to weight training, yet a stalled run does not by
itself show that the judge failed unless the evidence reaching the proposer
is separated from the evidence visible only to the scorer.

## Where to go next

- [Deployment-Time Machine Learning: LLM-Selected Updates Without a Single Score](./deployment-time-machine-learning-llm-selected-updates.md)
  — why a change to the system’s own method can close a learning loop, and
  which further gains require separate evidence.
- [Can an LLM Judge Which Changes Are Worth Making?](./can-an-llm-judge-which-changes-are-worth-making.md)
  — how to separate judging the available facts from finding them.
- [Selection-based learning](../theory/definitions/selection-based-learning.md)
  and its
  [definition checks](../theory/definitions/selection-based-learning-checks.md)
  — the full definition and the boundary cases it is tested against.
- [Bootstrapping Autonomous Selection-Based Learning with Commonplace](./bootstrapping-autonomous-selection-based-learning.md)
  — how update decisions move from the operator to computation one kind at
  a time, and the removal test that shows a decision has moved.
- [Testing Whether a Theory Builder Learns](./testing-whether-a-theory-builder-learns.md)
  — an earlier companion draft covering additional experimental designs.

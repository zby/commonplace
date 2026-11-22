---
description: "Research program article: separates membership, edit outcomes, and autonomous LLM judgment in Commonplace; defines comparisons for admission, targeted correction, criterion revision, and net gain, plus a proposed first routing-check experiment"
type: articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/theory/definitions/selection-based-learning.md
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

In [selection-based learning](../theory/definitions/selection-based-learning.md),
a system learns by changes that are each proposed, judged inside the loop,
and can be rejected. In Commonplace those changes are edits to a readable,
addressable store—prose, structured text, and code consumed by its later
work. The
[lead article](./deployment-time-machine-learning-llm-selected-updates.md)
argues that a fixed-weight language model could serve as that judge where
no fixed test is adequate, using a robust comparison in place of a single
value function.

This article sets out the research program behind that bet. Its question is
narrow: **which comparisons would distinguish autonomous model judgment
from what Commonplace already does with a human operator?** For each
comparison, it states what a positive result would establish and what it
would leave open.

## Three claims, not one verdict

Commonplace, our agent-operated knowledge-base framework, serves as the
testbed. Evaluating it requires separating three claims rather than
collapsing them into a single verdict.

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
Once those dependencies, the parties whose gains and losses count, and the
horizon across tasks are declared, the edit improved the system only if the
system is **robustly better**—meaning every compatible measure of the declared
work favors keeping it
([necessary preference](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md)).
Changed behavior alone proves only that the edit mattered
([operative change](../theory/definitions/operative-change.md)), not that
it helped.

**Autonomous judgment.** The conjecture under test is that a fixed-weight
language model can make the admission, correction, and criterion-revision
decisions without a person making them. Any episode in which the operator
selects among candidate edits is evidence about the human–machine system,
not a test the autonomous model passed or failed.

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

**Consistency comes before all three.** A judge supplies a comparison only
if its answers do not contradict each other. The check is cheap: give the
model the same change and its reversal on the same evidence, and the same
pair of versions in both orders and in different wordings. Approving a
change and its reversal, or a chain of changes that returns to where it
started, is a contradiction, and so is an answer that flips with order or
wording. The consistency need not cover every possible change. It has to
hold for the changes the loop actually compares.

**Net gain is a separate test of the whole loop.** All three capabilities
can succeed locally while accumulated edits degrade the system overall. The
whole-loop test compares the evolving store against an otherwise matched
system running on the starting store over the same fresh work and horizon.
It counts upkeep and human supervision alongside task outcomes, watching
for costs local approvals miss: judgment errors,
[false-positive acceptance](../theory/false-positive-generation-is-filtered-before-retention.md),
[unfaithful rationales](../theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md),
and store accretion. When compatible measures pull apart, the verdict is
reported as open. Neither withholding the entire store nor showing one
successful repair establishes the net benefit of continued revision.

## A first experiment: repairing a misleading routing check

Rather than waiting for an end-to-end automated loop, the program starts
with one focused test of criterion revision: repairing a check that lets
overbroad routing instructions pass. This is a **proposed experiment**, not
a run already commissioned or completed.

In the test, the model receives the current review check along with
execution traces in which overbroad routing lines passed that check and
later misdirected work. It receives only the evidence—no diagnosis and no
replacement rule—and decides whether and how to revise the check. To rule
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
([bootstrapping with Commonplace](./bootstrapping-an-autonomous-theory-builder.md)).
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
- **The Python change-judgment probes.** An original six-session design
  tested one model across two Python change cases and was never run. A
  follow-on design compares one model against human practitioners on a
  single CPython build-default case; three fresh model answers have been
  collected, while human replies, the independent mixed reading, and a
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
  — the lead article stating the paradigm, the weight-training contrast,
  and the Bitter Lesson argument.
- [Selection-based learning](../theory/definitions/selection-based-learning.md)
  and its
  [definition checks](../theory/definitions/selection-based-learning-checks.md)
  — the full definition and the boundary cases it is tested against.
- [Testing Whether a Theory Builder Learns](./testing-whether-a-theory-builder-learns.md)
  and
  [Bootstrapping an Autonomous Theory Builder with Commonplace](./bootstrapping-an-autonomous-theory-builder.md)
  — earlier companion drafts covering additional experimental designs and
  the incremental automation path.

---
description: "Research program article: separates membership, learned edits, and autonomous LLM judgment in Commonplace; defines comparisons for admission, targeted correction, criterion revision, and net gain, plus a proposed first routing-check experiment"
type: articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/theory/definitions/deliberative-learning.md
  - kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  - kb/theory/reversibility-can-favor-a-change-by-limiting-future-loss.md
  - kb/theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/theory/false-positive-generation-is-filtered-before-retention.md
  - kb/theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md
  - kb/theory/definitions/operative-change.md
  - kb/theory/evidence/commonplace-revision-used-theory-guided-computational-search.md
  - kb/reference/commonplace-declared-frame.md
---

# Testing Autonomous Deliberative Learning

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

In [deliberative learning](../theory/definitions/deliberative-learning.md),
a system learns by making proposed, rejectable edits to its own readable,
addressable store—prose, structured text, and code consumed by its later
work—with a judgment inside the loop deciding which edits stay. The
[lead article](./deliberative-learning-judgment-in-place-of-a-value-function.md)
argues that a fixed-weight language model could serve as that judge where
no fixed test is adequate, using on-balance judgment in place of a single
value function.

This article sets out the research program behind that bet. Its question is
narrow: **which comparisons would distinguish autonomous model judgment
from what Commonplace already does with a human operator?** For each
comparison, it states what a positive result would establish and what it
would leave open.

## Three claims, not one verdict

Commonplace is an agent-operated knowledge-base framework that serves as
our testbed. Assessing it requires keeping three separate claims apart,
rather than collapsing them into a single yes-or-no verdict.

**Membership today.** Under
[Commonplace's declared frame](../reference/commonplace-declared-frame.md)—which
names the people and programs counted as inside the system—the system
includes the agents, the command-line tools, and the human operator. Its
store holds library notes, instructions, types, validators, and code used
across tasks. For a named class of edits, such as changes to routing
instructions, the operator or an agent can reject a proposed edit, later
tasks load what is kept, and a misleading review check can itself be
revised for future edits of that class. That establishes capacity for a
human-assisted system—a weak claim that any engineering team maintaining a
handbook also meets.

**Whether a particular edit was learned.** Admitting a reversible edit can
be a sound decision while its payoff is still unknown
([reversibility can limit future loss](../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md)).
Whether that edit was actually **learned** is a separate verdict: compare
fresh work with the edit against fresh work without it, leaving the rest of
the store intact except for later edits that depend on it. Name those
dependencies, whose gains and losses count, and the horizon across tasks.
Showing that later behavior changed proves only that the edit mattered
([operative change](../theory/definitions/operative-change.md)); it does
not show that the change was for the better.

**Autonomous judgment.** The conjecture under test is that a fixed-weight
language model can make the admission, correction, and criterion-revision
decisions without a person making them. An episode in which the operator
selects among candidate edits is evidence about the human–machine system,
not a test the autonomous model either passed or failed.

## Four comparisons that separate the capabilities

To test autonomous judgment without conflating its parts, fix the model,
task family, available evidence, and compute budget before a run, and state
what outcome counts against the prediction *for that setup*. One failed run
counts against that configuration, not against all fixed-weight models.

| Capability | Comparison and interpretation |
|---|---|
| **Admission** | Give the model and a fixed gate the same proposals and evidence, including useful edits the gate rejects, harmful edits it admits, and edits it handles correctly (without the third group, a judge that merely inverts the gate would score well). Compare which edits each admits and their consequences on fresh work, alongside admitting every proposal. If the fixed gate matches the model, no advantage for model judgment is shown; a persuasive rationale alone proves nothing. |
| **Targeted correction** | Place one harmful edit and one independently useful edit in the same batch, and supply evidence from later use without naming the culprit. Compare the learner's repair against leaving the batch intact and against rolling the whole batch back. If nothing useful sits in the batch to preserve, tying full rollback cannot distinguish accurate diagnosis from indiscriminate removal. |
| **Criterion revision** | Compare later decisions on the same unseen proposals under the old and revised criteria. A retained revision that changes which proposals pass shows that the criterion actually changed in practice. Whether those decisions improved is a separate check: a check that rejects everything prevents every bad admission. |

**Net gain is a separate test of the whole loop.** All three capabilities
can pass locally while accumulated edits make the system worse overall.
Compare the evolving store against an otherwise matched system running on
the starting store over the same fresh work and horizon. Count upkeep and
human supervision alongside task outcomes, checking specifically for costs
local approvals miss—judgment errors,
[false-positive acceptance](../theory/false-positive-generation-is-filtered-before-retention.md),
[unfaithful rationales](../theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md),
and store accretion. When reasonable measures disagree, report the
disagreement as open
([on-balance judgments](../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md)).
Neither withholding the entire store nor demonstrating one successful
repair establishes the net benefit of continued revision.

## A first experiment: repairing a misleading routing check

As a proposed first experiment—**not a run already commissioned or
completed**—test criterion revision on one concrete failure mode: an
existing check that lets overbroad routing instructions pass.

Give the model the current review check together with execution traces in
which overbroad routing lines passed that check and later misdirected work.
Supply the evidence only, not a diagnosis or a replacement rule, and let
the model decide whether and how to revise the check. Then run both the old
and revised checks on the same set of unseen proposals, including sound
routing rules that should still pass. On fresh downstream tasks, record
both misroutes prevented and useful guidance lost.

The comparison separates three outcomes:

1. **No operative revision:** later decisions on unseen proposals do not
   change.
2. **Changed decisions without demonstrated gain:** misroutes drop only by
   rejecting sound rules, or overall task outcomes do not improve.
3. **Improved criterion:** the revised check prevents misroutes while
   preserving sound guidance on fresh work.

Even outcome 3 tests only one capability—criterion revision on a single
failure pattern—not sustained autonomous learning across a whole store.
Other controlled designs live in the
[testing supplement](./testing-whether-a-theory-builder-learns.md), which
is being re-anchored from our earlier theory-builder framing.

Record for every step who proposed, diagnosed, selected, and installed the
change. People may design the trial and independently assess outcomes
afterward without entering the learning loop; a person who picks the best
among several model-drafted repairs *is* inside the loop, turning the run
into a human-assisted trial.

## Why the development path matters

Commonplace moves decisions out of the operator's hands one kind at a time,
reporting separately which operations still complete and which resulting
edits improve later work
([bootstrapping with Commonplace](./bootstrapping-an-autonomous-theory-builder.md)).
The practical payoff under test is whether a misleading check gets repaired
without waiting for a person to spot the recurring pattern and redesign it.
Whether that saves human judgment overall depends on supervision and
cleanup costs as much as on the repair itself.

This path also carries the Bitter Lesson boundary: a system starting from
hand-written instructions, types, and checks scales with computation
[only if automated learning eventually outgrows that starting state](../theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md),
supplying and revising the task-specific criteria new work requires.

## Current evidence and where rivals disagree

The current evidence record is small and should not be overstated:

- **No end-to-end automated run.** Commonplace reports no completed
  demonstration of sustained autonomous double-loop learning.
- **The Python change-judgment probe.** We designed a six-session probe
  comparing how models and practitioners reason about one change; that
  first design was not run. A follow-on comparison on a CPython build
  default collected three model answers from fresh sessions, while human
  practitioner replies, the independent mixed reading, and a second-round
  case variant remain pending. Even completed, that comparison probes
  stated reasons for a single decision, not the downstream effect of an
  admitted edit.
- **The 2026-08-30 revision.** One observed episode in Commonplace
  ([theory-guided computational search](../theory/evidence/commonplace-revision-used-theory-guided-computational-search.md))
  used retained theory to guide search while the operator selected among
  candidate revisions. That is evidence about the human-assisted system,
  not autonomous judgment.

State rival predictions only where an experiment actually separates them.
Rich Sutton and Khurram Javed argue that forming genuinely new concepts
requires continual weight updates
([Sutton and Javed](../sources/sutton-javed-why-ai-models-stop-learning.ingest.md));
a successful routing-check repair need not involve forming a new concept,
so passing that first test would not refute their claim. Similarly, the
2026 study
[Harness Evolution Hits a Ceiling](../sources/harness-evolution-ceiling-weight-training.ingest.md)
deferred stalled failures to weight training, yet a stalled run does not by
itself show that the judge failed unless the evidence reaching the proposer
is separated from the evidence visible only to the scorer.

## Where to go next

- [Deliberative Learning: Judgment in Place of a Value Function](./deliberative-learning-judgment-in-place-of-a-value-function.md)
  — the lead article stating the paradigm, the weight-training contrast,
  and the Bitter Lesson argument.
- [Deliberative learning](../theory/definitions/deliberative-learning.md) —
  the full definition and boundary cases.
- [Testing Whether a Theory Builder Learns](./testing-whether-a-theory-builder-learns.md)
  and
  [Bootstrapping an Autonomous Theory Builder with Commonplace](./bootstrapping-an-autonomous-theory-builder.md)
  — earlier companion drafts covering additional experimental designs and
  the incremental automation path.

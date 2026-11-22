---
description: "Lead article: how a deployed agent system for open-ended knowledge work can learn at deployment time by LLM-selected updates without a single score, when that loop fits the Bitter Lesson, and how retained hypotheses may help"
type: articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/theory/definitions/self-improving-system.md
  - kb/theory/definitions/reflective-system.md
  - kb/theory/definitions/selection-based-learning.md
  - kb/theory/selection-based-learning-needs-only-a-local-comparison.md
  - kb/theory/necessary-preference-can-guide-improvement-without-a-global-measure.md
  - kb/theory/reversibility-can-favor-a-change-by-limiting-future-loss.md
  - kb/theory/definitions/single-loop-and-double-loop-learning.md
  - kb/theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md
  - kb/theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/theory/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/theory/retained-theories-may-improve-sample-efficiency.md
  - kb/theory/definitions/addressable-theory.md
  - kb/theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md
---

# Deployment-Time Machine Learning: LLM-Selected Updates Without a Single Score

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

Standard machine learning updates opaque numerical weights during training,
driven directly by a scalar loss or reward. Open-ended knowledge work
rarely comes with a single score that captures what matters, because gains
and losses fall on different tasks and different people—whether the work is
research synthesis, curating a knowledge base, reviewing technical
documents, applying operational policies, or maintaining software.

Yet a deployed agent system can still learn after training while its model
weights stay fixed
([deployment-time learning with fixed weights](../theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md)).
Between tasks, it updates what it retains—procedures, routing rules, review
criteria, explanatory notes, and scripts—by proposing changes, evaluating
whether they make later work better, and rejecting weak ones. Because
proposing updates is costly, evaluation needs only a local comparison among
the few candidates at hand rather than a global score ranking every
possible state
([local comparison suffices](../theory/selection-based-learning-needs-only-a-local-comparison.md)).

This article makes one empirical bet and two conditional arguments about
such a deployment-time learning loop for open-ended knowledge work. The bet
is that a large language model (LLM) can help find candidates and
discriminating checks, and select among them well enough that later work
improves without a person judging each update. If the bet holds, a fully
automated loop can sit on the compute side of the Bitter Lesson. A stronger
design that retains testable hypotheses alongside its winning updates may
also need fewer new observations after structured shifts and supply
bounded, testable explanations of what it learned.

## One failure, two repairs

To see the loop clearly, start with a concrete build-maintenance case—where
diffs and replay tests make every causal step easy to inspect—and then look
at the exact same pattern in prose knowledge work.

Take a hypothetical deployed agent system that maintains build pipelines
across several repositories. Its test-selection workflow skips build tests
for edits it classifies as documentation-only. One such edit changes a
repository's README, and the build breaks: the packaging step reads that
README to generate the package description.

**The first repair fixes the work product.** The agent diagnoses the
failure, adds a test that builds the package, ships the fix, and closes the
report. That repository's pipeline is better. The agent system is not: its
own test-selection rule is unchanged, so the same kind of edit in another
repository will skip the same tests. Fixing an external output is not by
itself evidence that the system learned.

**The second repair updates the system's own method.** The failure is now
evidence about the agent's own workflow, and the same diagnostic capability
goes to work on it. Search produces candidate updates:

- run every test on every edit;
- add an exception for this one file;
- before classifying an edit, inspect which files the build reads, and
  treat any file it reads as code;
- leave the workflow unchanged.

Search also produces checks that discriminate among these candidates. For
example, the system can replay last quarter's edits under each rule and
count which failures each would have caught.

Selection then compares the four candidates on missed failures against
cost. Running every test avoids misses caused by skipping a relevant test,
but uses more compute and delays feedback. The single-file exception is
cheap but catches nothing new. Dependency inspection costs one analysis per
edit. The judge can investigate the facts these trade-offs depend on: how
often documentation files feed builds across repositories, and what a full
test run costs. It can reject every candidate, or install dependency
inspection on a bounded trial with a scheduled review
([reversibility limits future loss](../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md)).
Suppose it installs dependency inspection on trial.

No single score was needed: missed failures and compute fall on different
jobs, and the comparison only had to decide among the four candidates
reached. Under
[strict necessary preference](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md),
a change counts as an improvement when every compatible way of weighing
consequences favors it, while an open comparison still permits a bounded
trial. Choosing a candidate is not proof that it helps; it is a decision
made on current evidence.

Weeks later, in another repository, an edit changes a changelog that the
release script includes in its archive. The old rule would have classified
the edit as documentation and skipped the build tests. The retained method
finds the dependency, runs the tests, and catches a broken release. The
later job was causally changed by the selected update, not merely
accompanied by a log of the earlier failure. The check is to rerun the same
job with and without the retained method and see whether the outcome
differs. No model weights changed; what the deployed system retains for
later work did.

**The same loop runs in non-code knowledge work, where the lack of a single
score is even clearer.** Suppose an agent maintaining a research knowledge
base repeatedly files unfinished working drafts into the collection
reserved for finished design proposals. Moving one misplaced draft fixes
the document, not the agent. Updating the agent's own routing instructions
triggers the same four-way choice: leave the instructions alone, add a
one-off exception, add a rule distinguishing finished proposals from
in-flight drafts, or add a review check before filing. Here the trade-off
is between prevented misfilings and diffuse reading or context cost on
every unrelated task. Again, the test of learning is whether withholding
the retained update changes how fresh drafts get filed later.

## What closes the loop

The second repair in both cases has the structure of
[selection-based learning](../theory/definitions/selection-based-learning.md):
a change to what the system retains for its later work is proposed,
evaluated on whether it makes that work better, and can be rejected. Unlike
a direct gradient update—where a scalar loss determines the next weights
without proposing or rejecting a candidate—selection admits or rejects
discrete updates to the system's retained store of instructions, policies,
notes, or scripts. Because the deployed system does the selecting itself, routes each update
through inspectable instructions or scripts that govern its later work
([reflection](../theory/definitions/reflective-system.md)), and can reject
weak proposals, the process is **reflective self-improvement by
selection**—making the system a
[self-improving system](../theory/definitions/self-improving-system.md) for
this class of updates.

The boundary matters for the claim of automation. User requests, bug
reports, reader objections, and external acceptance decisions come from
outside the deployed system; depending on them does not make the learning
loop human-assisted. The loop is human-assisted only when people make the
internal update decisions at issue: which remedies to consider, how to
diagnose the failure, or which candidate to install.

Two criteria must be kept apart. An object-level rule governs the work
itself—which tests an edit gets, or where a document is filed. An adoption
criterion governs revisions to those rules, such as "adopt a workflow
change if replay shows it catches the observed failure at acceptable added
cost," or "admit a new instruction line only if it stays brief." Editing a
procedure under a fixed adoption criterion is a single-loop self-edit.

Suppose instead that several revisions pass that adoption criterion and
still degrade work: workflow edits that pass replay but prove too costly
across projects, or brief routing lines that keep misdirecting adjacent
document types. If the system changes the adoption criterion itself—
requiring cross-project cost estimates, or requiring every new routing rule
to state what it excludes—it has revised how it judges future updates. That
is
[double-loop learning](../theory/definitions/single-loop-and-double-loop-learning.md),
a further capability rather than a requirement for the basic loop.

Whether the loop helps is an empirical question. Compare the learning
system with a credible baseline—such as its starting instructions or an
existing fixed check—over fresh work it has not yet seen. Count compute,
review time, and the cost of rolling back bad revisions alongside gains on
the work itself.
[Testing Autonomous Selection-Based Learning](./testing-autonomous-selection-based-learning.md)
sets out those comparisons.

## The bet

The empirical bet is that a fixed-weight LLM can run that loop for
open-ended knowledge work without per-update human judgment: helping
generate candidate updates and discriminating checks, locating the facts
that decide between them, and rejecting weak candidates reliably enough
that later work improves.
[Can an LLM Judge Which Changes Are Worth Making?](./can-an-llm-judge-which-changes-are-worth-making.md)
develops the judgment side: where the decisive evidence comes from, what
packet curation hides, and how to test a judge without asking it to grade
itself. The two arguments below are conditional on the bet.

## First argument: the loop can sit on the compute side of the Bitter Lesson

Rich Sutton's Bitter Lesson is that general methods using computation beat
methods built on researchers' domain knowledge: "The two methods that seem
to scale arbitrarily in this way are search and learning"
([Sutton](../sources/sutton-the-bitter-lesson-original-essay.ingest.md),
verbatim). An immediate objection is that a system editing its own prose
instructions, rubrics, and scripts looks like hand-crafted knowledge.

The lesson contrasts how knowledge is produced, not
[how it is represented](../theory/the-bitter-lesson-selects-production-methods-not-representational.md).
Computation can produce prose procedures, structured criteria, and code as
well as floating-point weights. Reading the lesson this way is an
interpretation; Sutton's own essay does not address representation, and in
later work he argues for continual weight updates.

The deployment-time loop is compatible with the lesson only on one
condition: additional computation does the domain-specific discovery and
selection. Computation must diagnose the recurring failure, generate
candidate methods and discriminating checks, and reach the verdict, rather
than a person supplying each decisive step. Unattended scripts do not meet
that condition by themselves; a script that runs unattended while encoding
a person's diagnosis of each failure mode is still hand-supplied knowledge.
A system bootstrapped from hand-written instructions and checks fits the
lesson
[only if its learning outgrows that starting point](../theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).

Even then, scaling is not automatic. The decisive open bottleneck is
**credit assignment without a chain rule**: as a store of instructions,
notes, checks, and scripts grows interdependent, a later failure rarely
points straight to which retained entry should change. Whether results
improve as more compute is spent has to be measured.

## Second argument: retained hypotheses may buy sample efficiency and explanation

The basic loop needs only winning updates: the system keeps "inspect build
dependencies" or "exclude unfinished drafts from design proposals" because
it won. A stronger design also retains a revisable hypothesis with its
predictions, evidence, and checks. In the build case: "a file the build
reads behaves as code for testing purposes; the build's configured input
list names every such file." That hypothesis predicts which future edits
need build tests, cites the README failure as evidence, and names the
replay test that checks it.

The hypothesis changes the next inquiry. Suppose a later failure comes from
a snippet that the build reaches through an include and that the configured
input list does not name. A system that kept only the patch might add
another exception or rediscover the dependency from scratch. The retained
hypothesis gives the system a specific premise to test: does the input list
name every dependency, or only the entry points? If it names only entry
points, the system can revise that single premise—updating predictions for
other included files that have never failed yet.

The same mechanism applies in any knowledge base or policy store: revising
the shared premise behind a family of review rules or research procedures
updates every downstream case that rests on that premise rather than
patching failures one by one. This works because the hypothesis is
[addressable](../theory/definitions/addressable-theory.md): its assumptions
and scope can be inspected and revised one at a time.

The conditional payoff is
[sample efficiency](../theory/retained-theories-may-improve-sample-efficiency.md).
Under a task shift that preserves structure, a system with retained
hypotheses may need fewer new target observations to reach comparable
performance than the same model working from the same history kept only as
case records. This is not a claim of lower compute; maintaining and
checking hypotheses costs compute too.

The second payoff is a bounded kind of explanation. A retained hypothesis
claims that a particular rule governs the system's behavior. That claim can
be tested by intervention: run the next task with and without the
hypothesis, or edit the premise it states and check whether behavior moves
as predicted. Readable text is legible, but
[legibility is not faithfulness](../theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md):
plausible prose need not be what drove the behavior. Even a faithful rule
explains the deployed system's operative method, not the model's weights.

## Mixed results and current evidence

The claims can come apart. A loop could beat its baseline on fresh work
while gains stop growing with added compute; that supports the bet but not
the scaling argument. Systems with and without retained hypotheses could
need the same number of new observations; that would leave the base loop's
value intact while counting against the sample-efficiency conjecture in
that setting. Intervening on a retained hypothesis could fail to change
behavior, making its explanations unfaithful even where learning occurred.

Commonplace, the agent-operated knowledge-base framework behind this
article, is a live human-assisted setting for developing these ideas on
knowledge work: human maintainers still sit inside the boundary for both
search and selection—noticing recurring problems, diagnosing failures,
shaping candidate revisions, and accepting updates. No end-to-end
autonomous loop has been demonstrated. The bet and both arguments remain
untested.

## Where to go next

- [Can an LLM Judge Which Changes Are Worth Making?](./can-an-llm-judge-which-changes-are-worth-making.md)
  — develops the judgment bet in detail: packet curation versus tool-using
  inquiry, a three-arm diagnostic test, and separating working definition,
  judge competence, and framework prompting.
- [Testing Autonomous Selection-Based Learning](./testing-autonomous-selection-based-learning.md)
  — sets out the wider experimental program: admission, targeted
  correction, criterion revision, whole-loop net gain, and the current
  evidence record.
- [Selection-based learning](../theory/definitions/selection-based-learning.md)
  and
  [Selection-based learning needs only a local comparison](../theory/selection-based-learning-needs-only-a-local-comparison.md)
  — the definition of the learning process and why costly search means
  evaluation compares only the candidates reached.
- [Defining Improvement for Open-Ended Work](../theory/defining-improvement-for-open-ended-work.md)
  and
  [Necessary preference can guide improvement without a global measure](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md)
  — what a usable definition of improvement needs to handle and strict
  necessary preference as one working definition.

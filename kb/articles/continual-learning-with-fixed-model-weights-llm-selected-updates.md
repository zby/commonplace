---
description: "Lead article: the bet that autonomous selection-based learning over text, hypotheses, and code can clear four continual-learning bars with fixed weights without a single score, plus its base-model floor, Bitter Lesson scaling, and hypothesis payoffs"
type: articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/theory/definitions/self-improving-system.md
  - kb/theory/definitions/reflective-system.md
  - kb/theory/definitions/selection-based-learning.md
  - kb/theory/selection-based-learning-needs-only-a-local-comparison.md
  - kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  - kb/theory/credit-assignment-without-a-chain-rule-is-a-debugging-problem.md
  - kb/theory/defining-improvement-for-open-ended-work.md
  - kb/theory/on-balance-judgment-with-an-llm.md
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

# Continual Learning with Fixed Model Weights: LLM-Selected Updates Without a Single Score

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

Showing that a fixed-weight agent can learn *something* across tasks is easy.
Existing agent memory systems already save notes, append reminders to prompt
files, or patch scripts and perform better on the next few runs. The hard
question is why those systems plateau so quickly. As local patches pile up,
rules contradict each other, context windows fill, retrieval misses the right
entry, and the system stalls or degrades unless a person cleans it up. Because
of that low ceiling, many researchers assume that real continual
learning—growing steadily more capable across months of work on a codebase,
organization, or research domain—requires updating model weights.

This article states a stronger empirical bet and two conditional arguments
about [learning with fixed model weights](../theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md).
The bet is that this low ceiling is a failure of weak memory and selection
loops, not an inherent limit of fixed weights. On top of a capable
fixed-weight large language model (LLM), autonomous
[selection-based learning](../theory/definitions/selection-based-learning.md)
over an inspectable store of procedures, hypotheses, and code can deliver
sustained, compounding continual learning for open-ended knowledge and
software work without per-update human judgment and without a single scalar
score—clearing four bars that ordinary agent memory misses:

1. **Sustained long-horizon growth without an accretion plateau**—pruning,
   refactoring, and synthesizing retained artifacts across long streams of
   work and shifting requirements rather than endlessly appending patches.
2. **New methods, abstractions, and executable tools**—acquiring reusable
   workflows, domain concepts, checks, and software that handle whole classes
   of work the starting system could not reliably do, rather than only saving
   facts or tips.
3. **Targeted credit assignment and criterion revision without a scalar
   reward**—tracing later failures back to specific retained entries, undoing
   bad changes, and revising working checks when those checks mislead.
4. **Outgrowing its hand-crafted bootstrap as experience and compute
   grow**—rather than remaining capped by the failure modes and rules a human
   initially wrote into the harness.

This is not a claim that fixed-weight selection can learn anything; it depends
on a frozen base model already above the
[competence floor needed to operate the loop](../theory/base-llm-competences-for-autonomous-selection-based-learning.md),
detailed below. If the bet holds above that floor, a fully automated loop can
sit on the compute side of the Bitter Lesson, and retaining testable
hypotheses alongside winning updates may buy sample efficiency under
structured shifts plus bounded, testable explanations of what the system
learned.

## One failure, two repairs

To see the difference between fixing a task, saving a reminder, and updating a
method, follow one concrete failure. Suppose an agent maintaining pipelines
across repositories misses a build failure because its instructions tell it to
skip tests on documentation edits, and a documentation edit changes a README
that the packaging step reads to generate the package description. Consider
two ways the agent could respond.

**The first repair fixes the work product.** The agent diagnoses the failure,
adds a test that builds the package, ships the fix, and closes the report.
That repository's pipeline is better. The agent system is not: its own
test-selection rule is unchanged, so the same kind of edit in another
repository will skip the same tests. Fixing an external output is not by
itself evidence that the system learned.

**The second repair updates the system's own method.** The failure is now
evidence about the agent's own workflow, and the same diagnostic capability
goes to work on it. Search produces candidate updates:

- run every test on every edit;
- add an exception for this one file;
- before classifying an edit, inspect which files the build reads, and treat
  any file it reads as code;
- leave the workflow unchanged.

Search also produces checks that discriminate among these candidates—for
example, replaying last quarter's edits under each rule and counting which
failures each would have caught.

Selection then compares the four candidates on missed failures against cost.
Running every test avoids misses caused by skipping a relevant test, but uses
more compute and delays feedback. The single-file exception is cheap but
catches nothing new. Dependency inspection costs one analysis per edit. The
judge can check the facts these trade-offs depend on: how often documentation
files feed builds across repositories, and what a full test run costs. Because
search reaches only these few alternatives, selection needs a
[local comparison among the candidates at hand](../theory/selection-based-learning-needs-only-a-local-comparison.md),
not a global score ranking every possible workflow.

In [on-balance judgment](../theory/on-balance-judgment-with-an-llm.md)—formalized
in one way by
[necessary preference](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md)—a
change counts as an improvement when no compatible way of weighing
consequences opposes it and at least one strictly favors it. Where compatible
weightings still disagree or evidence is incomplete, the comparison stays
open, and the judge can install dependency inspection on a bounded trial with
a scheduled review
([reversibility limits future loss](../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md)).
Choosing a candidate is a decision on current evidence, not proof that the
edit helps.

Weeks later, in another repository, an edit changes a changelog that the
release script includes in its archive. The old rule would have classified the
edit as documentation and skipped the build tests. The retained method finds
the dependency, runs the tests, and catches a broken release. The later job
was causally changed by the selected update, not merely accompanied by a log
of the earlier failure. The check is to rerun the same job with and without
the retained method and see whether the outcome differs. No model weights
changed; what the deployed system retains for later work did.

**The same loop runs in non-code knowledge work, where the lack of a single
score is even clearer.** Suppose an agent maintaining a research knowledge
base repeatedly files unfinished working drafts into the collection reserved
for finished design proposals. Moving one misplaced draft fixes the document,
not the agent. Updating the agent's own routing instructions triggers the same
four-way choice: leave the instructions alone, add a one-off exception, add a
rule distinguishing finished proposals from in-flight drafts, or add a review
check before filing. Here the trade-off is between prevented misfilings and
diffuse reading or context cost on every unrelated task. Again, the test of
learning is whether withholding the retained update changes how fresh drafts
get filed later.

Notice where ordinary agent memory stops in both cases—and where the four bars
begin. An append-only memory system adds a reminder (*"remember README can
affect builds"* or *"watch out for drafts in proposals"*) and moves on. Over
hundreds of tasks, dozens of such reminders accumulate, overlap, and bloat
every prompt. Sustained continual learning requires turning recurring checks
into reusable procedures or code, pruning and merging redundant rules, tracing
a later regression back to the specific earlier edit that caused it, and
revising the admission check itself when bad edits keep slipping past it.

## What closes the loop

The second repair in both cases has the structure of
[selection-based learning](../theory/definitions/selection-based-learning.md):
a change to what the system retains for its later work is proposed, evaluated
on whether it makes that work better, and can be rejected. Unlike a gradient
step that adjusts weights to reduce a training loss, the loop admits or
rejects discrete updates to the system's retained store of instructions,
policies, notes, or scripts. Because the deployed system does the selecting
itself, routes each update through inspectable instructions or scripts that
govern its later work
([reflection](../theory/definitions/reflective-system.md)), and can reject
weak proposals, the process is **reflective self-improvement by
selection**—making the system a
[self-improving system](../theory/definitions/self-improving-system.md) for
this class of updates.

The boundary matters for the claim of automation. User requests, bug reports,
reader objections, and external acceptance decisions come from outside the
deployed system; depending on them does not make the learning loop
human-assisted. The loop is human-assisted only when people make the internal
update decisions at issue: which remedies to consider, how to diagnose the
failure, or which candidate to install.

Two criteria must be kept apart. An object-level rule governs the work
itself—which tests an edit gets, or where a document is filed. An adoption
criterion governs revisions to those rules, such as "adopt a workflow change
if replay shows it catches the observed failure at acceptable added cost," or
"admit a new instruction line only if it stays brief." Editing a procedure under
a fixed adoption criterion is a single-loop self-edit.

Suppose instead that several revisions pass that adoption criterion and still
degrade work: workflow edits that pass replay but prove too costly across
projects, or brief routing lines that keep misdirecting adjacent document
types. If the system changes the adoption criterion itself—requiring
cross-project cost estimates, or requiring every new routing rule to state
what it excludes—it has revised how it judges future updates. That is
[double-loop learning](../theory/definitions/single-loop-and-double-loop-learning.md),
the capability required whenever a fixed check starts misleading the loop.

## Testing the bet and its base-model floor

Testing the four bars does not require a benchmark against hypothetical
continual weight training for open-ended work. Each bar is directly testable
against concrete baselines on fresh streams of work:

- **Static starting system:** shows whether the loop delivers net gain over
  time once search, inquiry, upkeep, and rollback costs are counted.
- **Append-only agent memory:** isolates whether selection, pruning,
  refactoring, and tool or code creation avoid the accretion plateau.
- **Fixed-gate or score-only loop:** tests whether LLM on-balance judgment and
  criterion revision outperform a fixed check when trade-offs are non-scalar
  or the check misleads.
- **Human-assisted bootstrap:** tests how many update decisions actually move
  to computation without losing quality as operator involvement is withheld.

[Can an LLM Judge Which Changes Are Worth Making?](./can-an-llm-judge-which-changes-are-worth-making.md)
develops the judgment side—packet curation versus tool-using inquiry and a
three-arm diagnostic test—while
[Testing Autonomous Selection-Based Learning](./testing-autonomous-selection-based-learning.md)
sets out the comparisons for admission, targeted correction, criterion
revision, and whole-loop net gain.

Closing this loop autonomously still depends on what the frozen weights supply
up front. Harness code can handle much of the loop's machinery—enforcing
codified validators, capturing traces, replaying past cases, tracking bloat,
and executing rollbacks—but our working hypothesis is that
[three irreducible semantic competences remain on the frozen base LLM](../theory/base-llm-competences-for-autonomous-selection-based-learning.md):
interpreting unformalized text into action, diagnosing novel failures and
synthesizing candidate fixes in text or code, and judging unformalized
trade-offs while recognizing missing evidence. Below that competence floor,
edits to prompts or tools cannot substitute for capabilities the loop itself
needs; weight training still builds the base learner. Above that floor, the
two arguments below are conditional on the bet holding.

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

This loop fits the lesson only if additional computation does the
domain-specific discovery and selection: diagnosing recurring failures,
generating candidate methods and discriminating checks, and reaching verdicts,
rather than a person supplying each decisive step. Unattended scripts do not
meet that condition by themselves; a script that runs unattended while
encoding a person's diagnosis of each failure mode is still hand-supplied
knowledge. A system bootstrapped from hand-written instructions and checks
fits the lesson
[only if its learning outgrows that starting point](../theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).

Even then, scaling is not automatic. A key open challenge is
[**credit assignment without a chain rule**](../theory/credit-assignment-without-a-chain-rule-is-a-debugging-problem.md):
credit assignment by debugging is far less scalable than backpropagation
across billions of coupled weights, yet coding agents already automate much of
that debugging on large deterministic codebases. The open question is whether
automated debugging remains reliable when the store mixes code with
natural-language instructions whose traces, coupling, and failures are softer.

## Second argument: retained hypotheses may buy sample efficiency and explanation

Keeping only winning updates—such as "inspect build dependencies" or "exclude
unfinished drafts from design proposals"—leaves the system to rediscover why a
rule worked whenever a new failure appears. A stronger design also retains a
revisable hypothesis with its predictions, evidence, and checks. In the build
case: "a file the build reads behaves as code for testing purposes; the
build's configured input list names every such file." That hypothesis predicts
which future edits need build tests, cites the README failure as evidence, and
names the replay test that checks it.

The hypothesis narrows the next inquiry and helps with credit assignment.
Suppose a later failure comes from a snippet that the build reaches through an
include and that the configured input list does not name. A system that kept
only the patch might add another exception or rediscover the dependency from
scratch. The retained hypothesis gives the system a specific premise to test:
does the input list name every dependency, or only the entry points? If it
names only entry points, the system can revise that single premise—updating
predictions for other included files that have never failed yet.

The same mechanism applies in any knowledge base or policy store: revising the
shared premise behind a family of review rules or research procedures updates
every downstream case that rests on that premise rather than patching failures
one by one. This works because the hypothesis is
[addressable](../theory/definitions/addressable-theory.md): its assumptions
and scope can be inspected and revised one at a time.

The conditional payoff is
[sample efficiency](../theory/retained-theories-may-improve-sample-efficiency.md).
Under a task shift that preserves structure, a system with retained hypotheses
may need fewer new target observations to reach comparable performance than
the same model working from the same history kept only as case records. This
is not a claim of lower compute; maintaining and checking hypotheses costs
compute too.

The second payoff is a bounded kind of explanation. A retained hypothesis
claims that a particular rule governs the system's behavior. That claim can be
tested by intervention: run the next task with and without the hypothesis, or
edit the premise it states and check whether behavior moves as predicted.
Readable text is legible, but
[legibility is not faithfulness](../theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md):
plausible prose need not be what drove the behavior. Even a faithful rule
explains the deployed system's operative method, not the model's weights.

## What would refute the bet, and current evidence

Once human curation is removed across capable base models and clean evidence
interfaces, the bet fails if any of four ceilings holds: the store plateaus or
degrades because credit assignment, pruning, and refactoring break down under
accretion; the loop stays confined to narrow exceptions instead of
synthesizing reusable methods or executable tools; model judgments and
criterion revisions introduce more rework and silent regressions than a fixed
check; or additional experience and compute stop improving retained methods
beyond the hand-crafted bootstrap.

The conditional claims can also come apart from the base bet. A loop could
beat its static and append-only baselines on fresh work while gains stop
growing with added compute; that supports bounded selection-based learning but
not the Bitter Lesson scaling argument. Systems with and without retained
hypotheses could need the same number of new observations, leaving the base
loop intact while counting against the sample-efficiency conjecture in that
setting. Intervening on a retained hypothesis could fail to change behavior,
making its explanations unfaithful even where learning occurred.

Commonplace, the agent-operated knowledge-base framework behind this article,
is a live human-assisted setting for developing these ideas on knowledge work:
human maintainers still sit inside the boundary for both search and
selection—noticing recurring problems, diagnosing failures, shaping candidate
revisions, and accepting updates. No end-to-end autonomous loop has cleared
these four bars yet. The bet and both conditional arguments remain untested.

## Where to go next

- [Can an LLM Judge Which Changes Are Worth Making?](./can-an-llm-judge-which-changes-are-worth-making.md)
  — develops the judgment bet in detail: packet curation versus tool-using
  inquiry, a three-arm diagnostic test, and separating working definition,
  judge competence, and framework prompting.
- [Testing Autonomous Selection-Based Learning](./testing-autonomous-selection-based-learning.md)
  — sets out the wider experimental program: admission, targeted correction,
  criterion revision, whole-loop net gain, and the current evidence record.
- [Bootstrapping Autonomous Selection-Based Learning](./bootstrapping-autonomous-selection-based-learning.md)
  — explains how Commonplace moves update decisions from the human operator
  to computation one kind at a time, tested by withholding the operator.
- [Selection-based learning](../theory/definitions/selection-based-learning.md)
  and
  [Selection-based learning needs only a local comparison](../theory/selection-based-learning-needs-only-a-local-comparison.md)
  — the definition of the learning process and why costly search means
  evaluation compares only the candidates reached.
- [Harness code may offload much of a selection loop, leaving three base LLM competences](../theory/base-llm-competences-for-autonomous-selection-based-learning.md)
  and
  [Credit assignment without a chain rule is a debugging problem over an interdependent store](../theory/credit-assignment-without-a-chain-rule-is-a-debugging-problem.md)
  — our working hypothesis on the base-model floor and how debugging governs credit assignment as the store grows.
- [Defining Improvement for Open-Ended Work](../theory/defining-improvement-for-open-ended-work.md),
  [On-balance judgment with an LLM](../theory/on-balance-judgment-with-an-llm.md),
  and
  [Necessary preference can guide improvement without a global measure](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md)
  — what a usable improvement standard needs to handle, how an LLM compares
  remedies, and asymmetric necessary preference as one formalization.

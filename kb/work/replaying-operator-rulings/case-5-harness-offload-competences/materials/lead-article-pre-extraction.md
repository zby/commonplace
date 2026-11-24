# Continual Learning with Fixed Model Weights: LLM-Selected Updates Without a Single Score

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
about learning with fixed model weights. The bet is that this low ceiling is a
failure of weak memory and selection loops, not an inherent limit of fixed
weights. On top of a capable fixed-weight large language model (LLM),
autonomous selection-based learning over an inspectable store of procedures,
hypotheses, and code can deliver sustained, compounding continual learning for
open-ended knowledge and software work without per-update human judgment and
without a single scalar score—clearing four bars that ordinary agent memory
misses:

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

This is not a claim that fixed-weight selection can learn anything: it assumes
a base model strong enough to support the loop. If the bet holds, a fully
automated loop can sit on the compute side of the Bitter Lesson, and retaining
testable hypotheses alongside winning updates may buy sample efficiency under
structured shifts plus bounded, testable explanations of what the system
learned.

## One failure, two repairs

An agent can finish a task with its model weights unchanged and still be
better prepared for the next one. Suppose it misses a build failure because
its instructions tell it to skip tests on documentation edits, and a
documentation edit changes a README that the packaging step reads to generate
the package description. Consider two ways an agent maintaining pipelines
across repositories could respond.

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

Search also produces checks that discriminate among these candidates. For
example, the system can replay last quarter's edits under each rule and count
which failures each would have caught.

Selection then compares the four candidates on missed failures against cost.
Running every test avoids misses caused by skipping a relevant test, but uses
more compute and delays feedback. The single-file exception is cheap but
catches nothing new. Dependency inspection costs one analysis per edit. The
judge can investigate the facts these trade-offs depend on: how often
documentation files feed builds across repositories, and what a full test run
costs. Because search reaches only these few alternatives, selection needs a
local comparison among the candidates at hand, not a global score ranking
every possible workflow. In on-balance judgment—formalized in one way by
necessary preference—a change counts as an improvement when no compatible way
of weighing consequences opposes it and at least one strictly favors it, while
an open comparison still permits installing dependency inspection on a bounded
trial with a scheduled review. Choosing a candidate is not proof that it
helps; it is a decision made on current evidence.

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

The second repair in both cases has the structure of selection-based learning:
a change to what the system retains for its later work is proposed, evaluated
on whether it makes that work better, and can be rejected. Unlike a gradient
step that adjusts weights to reduce a training loss, the loop here admits or
rejects discrete updates to the system's retained store of instructions,
policies, notes, or scripts. Because the deployed system does the selecting
itself, routes each update through inspectable instructions or scripts that
govern its later work (reflection), and can reject weak proposals, the process
is **reflective self-improvement by selection**—making the system a
self-improving system for this class of updates.

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
double-loop learning.

## Testing the bet

Testing the four bars does not require an elusive head-to-head benchmark
against hypothetical continual weight training for open-ended work. Each bar
is directly testable against concrete baselines on fresh streams of work:

- **Static starting system:** shows whether the loop delivers net gain over
  time once search, inquiry, upkeep, and rollback costs are counted.
- **Append-only agent memory:** isolates whether selection, pruning,
  refactoring, and code/tool creation avoid the accretion plateau.
- **Fixed-gate or score-only loop:** tests whether LLM on-balance judgment and
  criterion revision outperform a fixed check when trade-offs are non-scalar
  or the check itself misleads.
- **Human-assisted bootstrap:** tests how many update decisions actually move
  to computation without losing quality as operator involvement is withheld.

## First argument: the loop can sit on the compute side of the Bitter Lesson

Rich Sutton's Bitter Lesson is that general methods using computation beat
methods built on researchers' domain knowledge: "The two methods that seem
to scale arbitrarily in this way are search and learning." An immediate
objection is that a system editing its own prose instructions, rubrics, and
scripts looks like hand-crafted knowledge.

The lesson contrasts how knowledge is produced, not how it is represented.
Computation can produce prose procedures, structured criteria, and code as
well as floating-point weights. This proposed loop fits the lesson only if
additional computation does the domain-specific discovery and selection:
diagnosing the recurring failure, generating candidate methods and
discriminating checks, and reaching the verdict, rather than a person
supplying each decisive step. A system bootstrapped from hand-written
instructions and checks fits the lesson only if its learning outgrows that
starting point.

Even then, scaling is not automatic. The decisive open bottleneck is **credit
assignment without a chain rule**: as a store of instructions, notes, checks,
and scripts grows interdependent, a later failure rarely points straight to
which retained entry should change.

## Second argument: retained hypotheses may buy sample efficiency and explanation

The basic loop needs only winning updates: the system keeps "inspect build
dependencies" or "exclude unfinished drafts from design proposals" because it
won. A stronger design also retains a revisable hypothesis with its
predictions, evidence, and checks. In the build case: "a file the build reads
behaves as code for testing purposes; the build's configured input list names
every such file." If a later failure comes from an included snippet not listed
in the build inputs, the retained hypothesis gives the system a specific
premise to test and revise—updating predictions for other included files that
have never failed yet.

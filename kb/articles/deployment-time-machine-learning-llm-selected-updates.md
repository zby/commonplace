---
description: "Lead article: how a deployed agent can select edits to its instructions without a single score; the bet that a fixed-weight LLM can build the preference model and make the robust comparison; weight-training contrast, Bitter Lesson, empirical test"
type: articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/theory/definitions/selection-based-learning.md
  - kb/theory/definitions/single-loop-and-double-loop-learning.md
  - kb/theory/necessary-preference-can-guide-improvement-without-a-global-measure.md
  - kb/theory/reversibility-can-favor-a-change-by-limiting-future-loss.md
  - kb/theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/theory/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md
  - kb/theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md
  - kb/theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md
  - kb/theory/false-positive-generation-is-filtered-before-retention.md
  - kb/theory/definitions/operative-change.md
  - kb/theory/definitions/addressable-theory.md
  - kb/theory/definitions/self-improving-system.md
  - kb/theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
  - kb/theory/revising-an-improvement-objective-is-licensed-from-outside-it.md
  - kb/theory/the-deployed-system-not-the-model-is-the-unit-of-learning.md
  - kb/theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md
---

# Deployment-Time Machine Learning: LLM-Selected Updates Without a Single Score

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

A deployed agent can learn by changing what it retains between tasks: an
instruction its next run will read, or a criterion it uses to judge its own
edits, while the model's weights stay as they are. The question is which
revisions to keep. If a new instruction prevents routing errors but adds
reading time to every task, can a large language model (LLM) select an
update without reducing both effects to one score?

First, **selection-based learning**—learning through proposed changes
that are evaluated and can be rejected—needs a comparison, not a single
score. The alternative denied here is that selecting an update first
requires collapsing every gain and loss into one number. The judge that
evaluates a proposed change need only compare the candidates at hand,
including leaving the system unchanged. One scoring function can supply the
comparison when it captures what matters. Often the stated purpose
permits several ways to weigh the gains and losses. Decision analysis calls
the set of those weightings a **preference model**, and the comparison is
**robust** when every weighting in the set gives the same answer. A robust
comparison can select changes without anyone choosing one scalar weighting.
The case argued here is the one where the changes are edits to the system's
own retained instructions and criteria, kept as a readable,
[addressable](../theory/definitions/addressable-theory.md) **store**: text
whose parts can be inspected and revised one at a time. The process itself
is not new: software teams do it when they maintain handbooks and linters,
and symbolic learners such as PRODIGY ran a fixed-formula version of it in
the 1980s. Like reinforcement learning, selection-based learning names a
process with no built-in guarantee of improvement.

Second, and this is our empirical bet: **a fixed-weight language model can
supply what the selection step needs. It can build the preference model
from a stated purpose and make the robust comparison.** The bet is that the
model can identify which trade-offs the purpose permits, trace later
failures to specific edits, and revise the criteria it uses to judge future
edits. Whether spending more computation on that work yields better
decisions is a further test.

## One change followed through

Before stating the paradigm abstractly, follow a single edit through a
deployed agent system that maintains its own knowledge base and instruction
files.

Suppose agents repeatedly misfile design proposals in the wrong directory.
A change is proposed: add one routing line to the main instruction file
loaded on every task, directing design proposals to the right folder and to
the spec that says how a design proposal must be written. A judge evaluates
the proposed edit before it enters the store. It weighs the expected routing
fix against a diffuse cost. Every unrelated task also loads that extra line.
On a task already near the model's effective context limit, extra prompt
text can tip a correct answer into rework. The judge compares leaving the
file alone, adding the line as proposed, and adding it on trial. It selects
the trial: it installs the line and schedules a review of the next
maintenance run. The reviewer will inspect where the line sent each task and
decide whether to keep, narrow, or remove it. The line takes effect now
under either form of adoption; only the trial also changes what the reviewer
will do.

On later tasks, the new line directs proposal writes accurately. Then a
longer maintenance run fails: the rule matched a migration plan that
belonged instead in a
[workshop](../theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md),
the system's temporary area for unfinished work. At the scheduled review,
the reviewer traces the misfiling to the new line and narrows its scope to
finished design proposals while leaving the rest of the instruction file
intact. Later still, three similar over-broad rules pass the system's
existing brevity check. A third change then revises the review check itself:
every new routing rule must declare what it excludes before acceptance.

This constructed illustration shows three things. First, a system can adapt
across tasks at deployment time without changing a single model weight: the
unit of learning is [the deployed system, not the model alone](../theory/the-deployed-system-not-the-model-is-the-unit-of-learning.md).
Second, the judge selected the line with a review commitment, not the line
as originally proposed. The review costs time but gives the system a chance
to catch misrouting. That makes the trial a different proposal, not one that
every compatible measure must favor. Selecting it does not show that later
work was better than if the file had stayed unchanged. Third, no
single scalar metric had to be invented to compare saved misfilings against
diffuse context load.

## Selection-based learning versus direct gradient training

Our knowledge base defines
[selection-based learning](../theory/definitions/selection-based-learning.md) by
one condition: a change to what the system retains for its later work is
proposed, evaluated, and can be rejected. Evaluation need not be a separate
stage or actor. Its result decides whether the change is made or undone,
and a rejection is its own event. It can apply one fixed measure, such as a
validator or a utility formula, or a comparison across several.

[AlphaGo Zero](https://www.nature.com/articles/nature24270) is a well-known
case. Each newly trained network played the current best one and replaced
it only if it won by a margin of 55%. Its successor
[AlphaZero](../sources/alphazero-chess-shogi-self-play.ingest.md) dropped that step and updated
a single network continually, so it no longer selected among networks.

The gradient steps that trained each network were not selected in either
system. They are direct updates: the evidence determines the change, and
nothing is proposed or rejected. A plain gradient step in pre-training
works the same way. It is told the right output for each input, and the
error fixes the update. A training run that also keeps or discards
checkpoints adds selection on top of those steps. Automatic trace logging
and triggers that write on a count are direct updates too.

The definition does not say where the retained information is held or who does the
selecting. A deployed checkpoint, a team's working habits, and an
instruction file all qualify. Naming a system adds two questions. The
system is a
[self-improving system](../theory/definitions/self-improving-system.md)
when the selecting is done inside it, and it is double-loop when it can
also revise what it selects by. A model whose checkpoint is picked by its
engineers learns by selection without being self-improving. Commonplace,
our agent-operated knowledge-base framework, does all three today only with
people inside the system. The bet of this article is that the software
alone can, given a stated purpose.

This article treats one case: a readable store, edited by selected changes.
Writing rules down does not change the kind of learning. It gives rules
that an evaluator can read and a later edit can correct one at a time. The
table compares that case with gradient training.

| Axis | Direct gradient training | Selection-based learning over a readable store |
|---|---|---|
| **Modifiable substrate** | Opaque numerical parameters | Readable, [addressable](../theory/definitions/addressable-theory.md) store (prose, structured text, code) |
| **Role of the value / loss function** | Scalar loss, reward, or value function | Rejectable judgment in the loop—from one fixed measure up to a robust comparison across a preference model |
| **When updates happen** | Training or fine-tuning runs | Deployment time, taking effect on the next task that reads the store |
| **Credit assignment and correction** | Backpropagation or policy gradients across parameters | Inspecting traces to edit, narrow, or revert specific entries while keeping the rest |
| **Inspectability** | Requires interpretability probes over weights | Direct reading, diffing, testing, and version control by people or agents |

The last three rows are payoffs of a readable store, and two carry limits.
"Deployment time" places a change in the lifecycle, not its speed:
proposing, evaluating, and safely installing it still take time
([persistent deployment-time adaptation](../theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md)).
Direct reading—by people or by other agents at volumes people could not
read—works only while each rule stays readable at an affordable cost. Large
or obscure artifacts can block it
([inspection needs an affordable route, not just readable form](../theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md)).

Those payoffs carry real costs that belong on the ledger of any comparison
with weight training. Explicit artifacts need retrieval, applicability
checks, validation, and ongoing upkeep. A false abstraction in a shared
instruction can misdirect many tasks, while a right rule that retrieval
misses does nothing. Worse, legibility does not guarantee faithfulness:
a plausible written rule need not be what actually drove the model's
behavior, so a rationale read from it can send repair to the wrong rule
([revision guided by rationale needs faithfulness, not just legibility](../theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md)).
Keeping episode records alongside distilled rules preserves a path to
re-examine a rule that goes stale
([retaining episode evidence](../theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md)),
at the cost of storing and managing more state.

## Proof, formula, judgment: where the bet enters

If selection-based learning over readable stores is not new, why did earlier
AI systems not turn it into a general machine learning paradigm? The three
precedents below raise the same question: how does a system decide whether
a proposed change is worth keeping?

**Formal proof.** Jürgen Schmidhuber's
[Gödel machine](../theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md)
is the strictest case, where a change is admitted only by formal proof. Its entire software, including its proof
searcher and utility representation, is readable, modifiable code, and live
observations enter proofs on the fly. Yet a self-rewrite takes effect only
through a formal proof that switching has higher expected utility than
continuing the current search, under axioms describing the hardware,
environment, and utility. That buys an optimality guarantee conditional on
those axioms and that utility, at a steep price. The machine must ignore
every useful improvement it cannot prove. A valid proof also does not
establish that the axioms adequately describe the real-world domain. Under
an inadequate formalization, a proved switch need not deliver what its user
wanted. Within these limits the machine can rewrite even its own utility
function, when it proves the rewrite better under the current one.

**Fixed formula.** Steven Minton's
[PRODIGY](../sources/minton-utility-of-ebl-aaai88.ingest.md) built a
working symbolic selection-based learner in 1988. It kept search-control rules
only while a fixed utility formula estimated positive time saved, updated
each rule's estimate from later use, and dropped rules whose estimate
turned negative. That is genuine **targeted correction**—pinning a loss on
one retained rule and removing it while keeping the rest. What PRODIGY
could not do was question whether its single formula in one unit (time
saved) captured what mattered; it was **single-loop**, needing Minton
outside the system to revise the formula.

**Changing heuristics.** Douglas Lenat's
[EURISKO](../sources/eurisko-learns-new-heuristics-and-domain-concepts.ingest.md),
an early-1980s symbolic program that discovered new heuristics and domain
concepts,
demonstrated the next step—**double-loop** criterion revision. In one
reported episode, after a badly generalized heuristic wasted effort,
EURISKO did not merely drop that heuristic; it also retained a restriction
penalizing future generalizations of that shape before they ran. Changing
what governs later decisions of a class revises the working criterion.
EURISKO could revise its own heuristics, but it still needed Lenat to
correct some judgments of worth. A heuristic could gain credit by
influencing how credit was awarded, not by helping solve the task. Lenat
could reject it on that ground without having to specify a better scoring
formula.

**Robust comparison.** In real engineering and knowledge work, gains and
losses fall on different tasks, and many different scalar value functions
can be defended from the same declared goal. The rule for this case is old and
standard: rank two options only where every admissible value function
agrees. Stochastic dominance is a familiar instance. One gamble dominates
another when every increasing utility function prefers it, and restricting
the set to risk-averse utilities orders more pairs. Multiple-criteria
decision analysis states the rule in the terms used here
([Greco, Mousseau and Słowiński](../sources/greco-ordinal-regression-revisited.ingest.md)).
It keeps every value function compatible with the preferences a person has
stated, and calls that set the preference model. A preference for one
option over another is *necessary* when every function in the set gives it,
and *possible* when at least one does. With no stated preferences, an option
is necessarily preferred only when it is at least as good on every
criterion, which leaves most real changes unordered. When stated preferences
leave one function, the method is ordinary selection by a value function.

The analogy has a limit. In that method the criteria are fixed, so each
stated preference can only narrow the set. In open-ended work an objection
can introduce a criterion nobody had listed. That widens the set and can
overturn an earlier verdict.

A
[robust comparison](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md)
applies this to a change. Once the alternative, the parties whose costs
count, and the horizon are fixed, the change is an improvement when every
compatible value function favors it. This is stricter than the method's
own relation, which asks only that an option be at least as good. When
compatible value functions pull in opposite directions or evidence has not
yet arrived, the comparison stays open. The system can still act on it as a
bounded decision, using
[reversibility to limit future loss](../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md),
as in the routing-line example above.

In the decision-analysis method, a person states the preferences. **We bet
that a fixed-weight language model can do that work autonomously: derive
the preference model from the declared purpose of the work, make the robust
comparison, and decide the cases it leaves open.** This is double-loop
selection-based learning with targeted correction, for work where no fixed
criterion is adequate. It requires the model to compare proposed edits and
to diagnose which retained edit caused a later failure. It also requires the
model to recognize when an existing gate, validator, or review criterion is
misleading and to revise it, while the declared objective the criteria serve
stays fixed
([revising an improvement objective](../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md)).

The bet is not that the model writes down value functions and computes
which option wins under all of them, as the decision-analysis method does.
Nor need the procedure assign every version a number: for the pair at hand,
the judge can favor either version or leave the comparison open. The bet is
that the model can give reasons that do the same work: which work changed,
whose costs count, and which weighting or observation would reverse the
choice. This says what the judge must do, not how its weights produce an
answer. The factual parts of those reasons, such as which work changed, can
be checked one at a time. The weighing of whose costs count cannot be
checked independently. It can only be challenged. Some open comparisons
close when the alternative is changed. Keeping the routing line for good may
be open, while trying it with a cheap way back can be better under every
compatible measure. What still remains is taken as a decision with its
reasons, not reported as an improvement, and later evidence can reverse it.

Consistency is part of the bet. A model that strictly prefers a change and
then, on the same evidence, strictly prefers its reversal matches no fixed
set of value functions. A test can look for such cycles. Even consistent
answers can neglect a cost the stated purpose requires the judge to count.

## Compatible with the Bitter Lesson

For many machine learning researchers, the immediate objection is Rich
Sutton's
[Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html):
general methods that leverage computation through search and learning
eventually beat methods built on human domain knowledge. A common folk
reading compresses that into *structure loses to weights*, treating any
system that learns by editing prose or code as a throwback to hand-crafted
symbolic AI.

That folk reading confuses **production method** with **representational
form**
([the Bitter Lesson selects production methods, not representational forms](../theory/the-bitter-lesson-selects-production-methods-not-representational.md)).
The Bitter Lesson contrasts human-supplied knowledge with knowledge
produced by computation through search and learning. It says nothing about
whether the retained result must live in floating-point weights. Scale
displaced hand-tuned weights as well as hand-written features. The losers
spanned both forms, because how the content was made decided the outcome.

Sutton himself leans toward the weights-only view: in a 2026
[interview](https://sequoiacap.com/podcast/rich-sutton-and-khurram-javed-why-ai-models-stop-learning-and-how-to-start-it-again),
he and Khurram Javed argue that forming new concepts requires continual
weight updating. That is a substantive rival hypothesis, not a corollary of
the Bitter Lesson essay. A 2026 empirical study,
[Harness Evolution Hits a Ceiling](../sources/harness-evolution-ceiling-weight-training.ingest.md),
reached a similar conclusion after an automated harness-evolution loop
stalled and deferred hard failures to weight training. Yet the authors'
own diagnosis attributed the stall to what the proposer was not shown (its
scorer saw a failure mode in a quarter of runs that never reached the
proposer), though their single remedy run stayed within noise. On one model
line the whole harness gain came from editing a natural-language lessons
file.

Once a language model supplies the comparison inside an automated
selection loop, the system sits on the computation side of the Bitter
Lesson if its results improve as more computation is spent. Additional
compute can be spent on more candidate proposals,
richer execution traces, independent criticism, targeted revisions, and
revised working criteria—all automatically generated and tested rather
than hand-authored. Whether that spending pays as the store grows is open.
The hard problem is credit assignment without a chain rule: when entries
depend on each other, a later failure rarely identifies which entry should
change.

One strict condition attaches. A system bootstrapped from hand-written
instructions, types, and review gates—as Commonplace currently is—fits the
Bitter Lesson
[only if automated learning outgrows that starting point](../theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).

## Whether a change improved the system, current evidence, and limits

A change is an event, and what the store keeps is
content. So the comparison is between two states of the system that differ
only in what the change did: added, revised or removed content. Entries
that depend on the changed content are adjusted to match. The change
improved the system when the state that has its effect is robustly better at
its later work: better under every compatible measure of the declared work
over the declared horizon.

For a recent edit—like our routing line on the day it is added—the verdict
is normally **open** until later episodes arrive. Passing the check that
admitted an edit does not show that later work is better.
Letting a change stand while its verdict is open is a decision, not a
demonstrated gain.

Testing the bet therefore requires a two-part empirical check on fresh
tasks outside the episode that prompted the edit:

1. **Operative dependence.** Withholding or altering the retained entry
   must change later behavior
   ([operative change](../theory/definitions/operative-change.md)). Loading
   a memory file on every run proves nothing if the model ignores it.
   For a change that removed content, no retained entry is left to
   withhold; the counterpart test is restoring the removed entry.
2. **Robust improvement.** The changed behavior must score higher under
   every compatible measure of the declared work, not merely pass the
   check that admitted it.

Realistic sets of compatible measures leave many trade-offs open. A test
therefore reports an open comparison as open, and is built around contrasts
clean enough to resolve.
[Testing Autonomous Selection-Based Learning](./testing-autonomous-selection-based-learning.md)
sets those comparisons out.

**Current state of evidence.** Commonplace is an active, human-assisted
bootstrap developing the store, review machinery, and judgment probes. We
report **no completed end-to-end automated run** demonstrating sustained
autonomous double-loop learning yet.

**Material limits and failure modes.** Even if the loop runs without human
intervention, five hazards can defeat it:

- *Judgment reliability.* Language-model judges can miss diffuse costs,
  hallucinate causal links in traces, or approve plausible-sounding edits
  that fail in practice.
- *False-positive retention.* A proof gate admits a switch only when it is
  proved better under stated axioms; empirical admission certifies only
  that a change passed the checks it faced. A harmful change that passes
  those checks is admitted, and
  [false-positive acceptance becomes operative](../theory/false-positive-generation-is-filtered-before-retention.md)
  until later evidence catches it.
- *Unfaithful rationales.* Legible prose can diverge from what actually
  steers the model's outputs, masking the real cause of gains or losses.
- *Accretion and maintenance drag.* Local gains are salient while context
  load and rule interactions are diffuse, so a chain of locally plausible
  edits can degrade aggregate performance unless whole-store comparisons
  and pruning counteract it.
- *Weak proposals.* A comparison selects only among the candidates that
  search reaches. A sound judge over poor proposals still learns little,
  and the bet stated here is about the comparison, not about how good the
  proposals are.

If controlled runs show that automated language-model judgment cannot keep
false-positive acceptance, unfaithful rationales, and accretion below the
gains it finds, the bet fails—and those domains stay with weights-only
continual learning or with engineering governed by people.

## Where to go next

- [Testing Autonomous Selection-Based Learning](./testing-autonomous-selection-based-learning.md)
  — the comparisons that would test the bet, and a proposed first
  experiment.
- [The definition](../theory/definitions/selection-based-learning.md) —
  the full definition, including what a claim must name and boundary cases
  such as triggers and direct updates. A companion definition covers
  [single-loop and double-loop learning](../theory/definitions/single-loop-and-double-loop-learning.md).
- [Necessary preference can guide improvement without a global measure](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md)
  — what a claim of improvement asserts, how to decide when the comparison
  is open, and Commonplace's declared objective.
- [Reversibility can favor a change by limiting future loss](../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md)
  — the companion to the previous note.
- Companion drafts in this collection—written before this framing
  was adopted and currently being re-anchored from the narrower *theory
  builder* special case (where the store holds explicit, criticized
  theories):
  [Testing Whether a Theory Builder Learns](./testing-whether-a-theory-builder-learns.md),
  [Bootstrapping an Autonomous Theory Builder with Commonplace](./bootstrapping-an-autonomous-theory-builder.md),
  and
  [Which Existing Self-Improving Systems Are Theory Builders](./which-existing-self-improving-systems-are-theory-builders.md).

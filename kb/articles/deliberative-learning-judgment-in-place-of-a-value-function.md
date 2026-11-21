---
description: "Lead article: deliberative learning as a distinct learning paradigm with on-balance judgment in place of a value function; fixed-weight LLM bet, weight-training contrast, Bitter Lesson, and empirical test"
type: articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/theory/definitions/deliberative-learning.md
  - kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  - kb/theory/reversibility-can-favor-a-change-by-limiting-future-loss.md
  - kb/theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/theory/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/theory/retained-artifacts-enable-persistent-deployment-time-adaptation.md
  - kb/theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md
  - kb/theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md
  - kb/theory/false-positive-generation-is-filtered-before-retention.md
  - kb/theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md
  - kb/theory/definitions/operative-change.md
  - kb/theory/definitions/addressable-theory.md
  - kb/theory/definitions/self-improving-system.md
  - kb/theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
  - kb/theory/revising-an-improvement-objective-is-licensed-from-outside-it.md
  - kb/theory/the-deployed-system-not-the-model-is-the-unit-of-learning.md
  - kb/theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md
---

# Deliberative Learning: Judgment in Place of a Value Function

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

Every machine learning loop needs two things: a modifiable substrate that
carries what the system retains, and a selection signal—a loss, reward, or
value function—that decides which updates stay. Standard machine learning
pairs opaque numerical weights with a scalar loss or value function. Viewed
through that frame, an agent that edits its own instructions or code without
a scalar benchmark looks like prompt engineering rather than learning.

This article makes a two-level claim. First, **deliberative learning**—a
system learning by making proposed, rejectable edits to its own readable,
addressable store—is a distinct learning paradigm. When no single formula
captures the work, an **on-balance judgment** works in place of a value
function inside the loop, deciding edits without selecting one scalar
weighting from the many value functions compatible with the goal. The
process itself is not new:
software teams do it when they maintain handbooks and linters, and symbolic
learners such as PRODIGY ran a fixed-formula version of it in the 1980s.
Like reinforcement learning, the term names a process with no built-in
guarantee of improvement.

Second, and this is our empirical bet: **putting a fixed-weight language
model in the judge slot turns deliberative learning into an automated
machine learning paradigm.** What is new is not the loop, but a machine
judge that can weigh trade-offs in prose and code without a formal utility
function, trace later failures back to specific retained edits, and revise
its own working criteria—learning at deployment time while its weights stay
fixed, and scaling with computation in a way compatible with the Bitter
Lesson.

## One change followed through

Before stating the paradigm abstractly, follow a single edit through a
deployed agent system that maintains its own knowledge base and instruction
files.

Suppose agents repeatedly misfile design proposals in the wrong directory.
A change is proposed: add one routing line to the main instruction file
loaded on every task, directing design proposals to the right folder and
type contract. A judge evaluates the proposed edit before it enters the
store. It weighs the expected routing fix against a diffuse cost—every
unrelated task also loads that extra line, and on a task already near the
model's effective context limit, extra prompt text can tip a correct answer
into rework. Because the edit is one identifiable line and cheap to revert
if trouble appears, the judge approves it.

On later tasks, the new line directs proposal writes accurately—until a
longer maintenance run fails because the rule matched a migration plan that
belonged in a temporary workshop instead. Inspecting the trace points
directly to that routing line. A second judgment narrows its scope to
finished design proposals while leaving the rest of the instruction file
intact. Later still, after three similar over-broad rules pass the system's
existing brevity check, a third change revises the review check itself so
every new routing rule must declare what it excludes before acceptance.

That sequence establishes three things. First, the system adapted across
tasks at deployment time without changing a single model weight: the unit
of learning is [the deployed system, not the model alone](../theory/the-deployed-system-not-the-model-is-the-unit-of-learning.md).
Second, an on-balance judgment played the role a scalar loss or value
function plays in weight training—deciding admission, guiding a targeted
fix to one line, and prompting a revision to the review check. Third, no
single scalar metric had to be invented to compare saved misfilings against
diffuse context load.

## Deliberative learning versus training weights

Our knowledge base defines
[deliberative learning](../theory/definitions/deliberative-learning.md) by
two conditions:

1. **Legible, addressable store.** What the system retains lives in
   contents that can be read and pointed at—prose, structured text, and
   code—belonging to the system's own behavior-determining organization and
   consumed by its later work. The system learns by editing those contents.
2. **Decision in the loop.** A change to the store is proposed, judged in a
   separate step inside the learning loop, and can be rejected. The judgment
   is a decision on available evidence that later work will go better with
   the change than without it, weighing considerations like an on-balance
   judgment. Treating one fixed criterion (such as a validator or utility
   formula) as settling the matter is the special case.

A single validator or utility formula weighs nothing—"deliberative" fits
the general case of weighing trade-offs better than this limiting case—yet
it still separates proposing from judging and can reject a change. By
contrast, opaque weight updates fail the first condition, while direct
input-driven updates (such as a nightly click-ranking job or a readable
tabular reinforcement-learning table), automatic trace logging, and pure
triggers that write on a count without judging what was written all fail
the second.

The structural contrast with weight training is starkest when laid side by
side:

| Axis | Training weights | Deliberative learning |
|---|---|---|
| **Modifiable substrate** | Opaque numerical parameters | Readable, [addressable](../theory/definitions/addressable-theory.md) store (prose, structured text, code) |
| **Role of the value / loss function** | Scalar loss, reward, or value function | Rejectable judgment in the loop—from a fixed criterion up to an on-balance judgment |
| **When updates happen** | Training or fine-tuning runs | Deployment time, taking effect on the next task that reads the store |
| **Credit assignment and correction** | Backpropagation or policy gradients across parameters | Inspecting traces to edit, narrow, or revert specific entries while keeping the rest |
| **Inspectability** | Requires interpretability probes over weights | Direct reading, diffing, testing, and version control by people or agents |

Three payoffs follow directly from storing what the system retains in
readable, addressable artifacts. Adaptation takes effect immediately at
deployment time without waiting for a retraining run
([persistent deployment-time adaptation](../theory/retained-artifacts-enable-persistent-deployment-time-adaptation.md)).
Retained knowledge is inspectable now—by people or by other agents at
volumes people could not read—whatever the pace of weight interpretability
research
([inspectability as a property of form](../theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md)).
And when a mistake occurs, an addressable store lets later rounds point at
the faulty line and fix it without wiping out unrelated work.

Those payoffs carry real costs that belong on the ledger of any comparison
with weight training. Explicit artifacts need retrieval, applicability
checks, validation, and ongoing upkeep; a false abstraction in a shared
instruction can misdirect many tasks, while a right rule that retrieval
misses does nothing. Worse, legibility does not guarantee faithfulness:
[a plausible written rule need not be what actually drove the model's behavior](../theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md).
Keeping episode records alongside distilled rules preserves a path to
re-examine a rule that goes stale
([retaining episode evidence](../theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md)),
at the cost of storing and managing more state.

## Proof, formula, judgment: where the bet enters

If deliberative learning over readable stores is not new, why did earlier
AI systems not turn it into a general machine learning paradigm? Looking at
three precedents shows that the bottleneck was always **what played the
value-function role**.

**Formal proof.** Jürgen Schmidhuber's
[Gödel machine](../theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md)
represents the hard-oracle extreme. Its entire software—including its proof
searcher and utility representation—is readable, modifiable code, and live
observations enter proofs on the fly. Yet every self-rewrite requires a
formal proof of higher expected utility under axiomatized hardware,
environment priors, and scalar utility. That buys a formal optimality
guarantee relative to those axioms at a steep price: the machine must
ignore every useful improvement it cannot prove, and no general real-world
domain has the full axiomatization required.

**Fixed formula.** Steven Minton's
[PRODIGY](../sources/minton-utility-of-ebl-aaai88.ingest.md) built a
working symbolic deliberative learner in 1988. It kept search-control rules
only while a fixed utility formula estimated positive time saved, updated
each rule's estimate from later use, and dropped rules whose estimate
turned negative. That is genuine **targeted correction**—pinning a loss on
one retained rule and removing it while keeping the rest. What PRODIGY
could not do was question whether its single formula in one unit (time
saved) captured what mattered; it was **single-loop**, needing Minton
outside the system to revise the formula.

**Changing heuristics.** Douglas Lenat's
[EURISKO](../sources/eurisko-learns-new-heuristics-and-domain-concepts.ingest.md)
demonstrated the next step—**double-loop** criterion revision. In one
reported episode, after a badly generalized heuristic wasted effort,
EURISKO did not merely drop that heuristic; it also retained a restriction
penalizing future generalizations of that shape before they ran. Changing
what governs later decisions of a class revises the working criterion. Yet
EURISKO's symbolic heuristics remained brittle and repeatedly needed Lenat
to intervene.

**On-balance judgment.** In real engineering and knowledge work, gains and
losses fall on different tasks, and many different scalar value functions
can be defended from the same declared goal. An
[on-balance judgment](../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md)
works in place of a single value function by leaving that choice open. Once
the alternative, whose costs count, and the horizon are fixed, a change is
an improvement on balance when every reasonable measure of the declared
work—every value function defensible from its purpose—favors it. An unknown
is worth investigating only if a plausible answer could reverse the choice.
When compatible value functions pull in opposite directions or evidence has
not yet arrived, the verdict stays open—and the system can still act as a
bounded decision, using
[reversibility to limit future loss](../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md),
as in the routing-line example above.

This is where the second level of our thesis—the machine learning
bet—enters. **We bet that a fixed-weight language model can fill the judge
slot autonomously, running double-loop deliberative learning with targeted
correction for work where no fixed criterion is adequate.** That requires
the model not only to weigh proposed edits and diagnose which retained edit
caused a later failure, but also to recognize when an existing gate,
validator, or review criterion is misleading and revise it—while the
declared objective the criteria serve stays fixed
([revising an improvement objective](../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md)).

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
produced by computation through search and learning; it says nothing about
whether the retained result must live in floating-point weights. Scale
displaced hand-tuned weights as well as hand-written features—what lost
spanned both forms because what decided the outcome was how the content was
made.

Sutton himself leans toward the weights-only view: in a 2026
[interview](https://sequoiacap.com/podcast/rich-sutton-and-khurram-javed-why-ai-models-stop-learning-and-how-to-start-it-again),
he and Khurram Javed argue that forming new concepts requires continual
weight updating. That is a substantive rival hypothesis, not a corollary of
the Bitter Lesson essay. A 2026 empirical study,
[Harness Evolution Hits a Ceiling](../sources/harness-evolution-ceiling-weight-training.ingest.md),
reached a similar conclusion after an automated harness-evolution loop
stalled and deferred hard failures to weight training—yet its own data
located the stall in what the proposer was not shown (its scorer saw a
failure mode in a quarter of runs that never reached the proposer), and its
strongest gains came from editing a natural-language lessons file.

Once a language model plays the value-function role inside an automated
deliberative loop, the system sits on the computation side of the Bitter
Lesson. Additional compute buys more candidate proposals, richer execution
traces, independent criticism, targeted revisions, and better working
criteria—all automatically generated, tested, and revised rather than
hand-authored.

One strict condition attaches. A system bootstrapped from hand-written
instructions, types, and review gates—as Commonplace currently is—fits the
Bitter Lesson
[only if automated learning outgrows that starting point](../theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).
The initial human scaffolding must serve as a launchpad that computation
comes to supply and revise, not a permanent ceiling of hand-crafted rules.

## What counts as learned, current evidence, and limits

Because deliberative learning names a process with no success condition,
the paradigm claim stays honest only if success is judged separately. A
change to the store was **learned** when the present system is better, on
balance, at its later work with that one change than with that change taken
out (leaving unrelated later edits intact), across every reasonable measure
of the declared work over the declared horizon.

For a recent edit—like our routing line on the day it is added—the verdict
is normally **open** until later episodes arrive, just as
[compounding is tested in later improvement rather than by the accepting metric](../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md).
Letting a change stand while its verdict is open is a decision, not a
demonstrated gain.

Testing the bet therefore requires a two-part empirical check on fresh
tasks outside the episode that prompted the edit:

1. **Operative dependence.** Withholding or altering the retained entry
   must change later behavior
   ([operative change](../theory/definitions/operative-change.md)). Loading
   a memory file on every run proves nothing if the model ignores it.
2. **On-balance improvement.** The changed behavior must score higher
   across reasonable measures of the declared work, not merely pass the
   check that admitted it.

**Current state of evidence.** Commonplace is an active, human-assisted
bootstrap developing the store, review machinery, and judgment probes. We
report **no completed end-to-end automated run** demonstrating sustained
autonomous double-loop learning yet. Treating the paradigm as already
validated would invert the order of proof.

**Material limits and failure modes.** Even if the loop runs without human
intervention, four hazards can defeat it:

- *Judgment reliability.* Language-model judges can miss diffuse costs,
  hallucinate causal links in traces, or approve plausible-sounding edits
  that fail in practice.
- *False-positive retention.* Unlike proof-gated switches, empirical
  admission admits harmful changes, and
  [false-positive acceptance becomes operative](../theory/false-positive-generation-is-filtered-before-retention.md)
  until later evidence catches it.
- *Unfaithful rationales.* Legible prose can diverge from what actually
  steers the model's outputs, masking the real cause of gains or losses.
- *Accretion and maintenance drag.* Local gains are salient while context
  load and rule interactions are diffuse, so a chain of locally plausible
  edits can degrade aggregate performance unless whole-store comparisons
  and pruning counteract it.

If controlled runs show that automated language-model judgment cannot keep
false-positive acceptance, unfaithful rationales, and accretion below the
gains it finds, the bet fails—and weights-only continual learning wins
those domains.

## Where to go next

- [Deliberative learning](../theory/definitions/deliberative-learning.md) —
  the full definition, including what a claim must name, the distinction
  between correction and displacement, and boundary cases such as triggers
  and direct updates.
- [On-balance judgments can guide improvement without a global measure](../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md)
  — what an on-balance claim asserts, how to decide under open verdicts,
  and Commonplace's declared objective; paired with
  [reversibility can favor a change by limiting future loss](../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md).
- Companion drafts in this collection—written before deliberative learning
  was adopted and currently being re-anchored from the narrower *theory
  builder* special case (where the store holds explicit, criticized
  theories):
  [Testing Whether a Theory Builder Learns](./testing-whether-a-theory-builder-learns.md),
  [Bootstrapping an Autonomous Theory Builder with Commonplace](./bootstrapping-an-autonomous-theory-builder.md),
  and
  [Which Existing Self-Improving Systems Are Theory Builders](./which-existing-self-improving-systems-are-theory-builders.md).

---
description: "A Gödel machine admits self-rewrites through proof under its current formalization; this restricts admission without establishing how many useful changes are reachable or how reliably they are found"
type: types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [self-improving-systems, reflection, improvement-loop, learning-theory, judgment-governed-self-improvement]
---

# Gödel machines are a proof-governed case of reflective self-modification

Schmidhuber's Gödel machine permits rewriting its software, including the code
that searches for changes. Its initial admission route requires a proof that
switching to a proposed program has greater expected utility than continuing
the current search, under axioms describing the machine, environment, and
utility function ([Schmidhuber, §3.2 (snapshot required)](../sources/goedel-machines-schmidhuber.ingest.md)).

This is a proof-governed construction of reflective self-modification, not a
definition of reflection. Its admission rule offers rigor relative to a
formalization while excluding switches for which the required proof is not
obtained. That restriction alone says neither how large the reachable state
space is nor how well the machine operates within a practical budget.

## The change loop

The construction can be read as a [proposal-selection improvement
loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md):

| Function | Gödel-machine realization |
|---|---|
| Self-representation | Axioms describing the machine, its software, environment assumptions, and utility |
| Search | Proof techniques that can construct proposed replacements and proofs |
| Evaluation | A proof of the target theorem comparing switching with continued search |
| Authority and retention | The switching operation invokes the proved replacement, which can rewrite the subsequent software |

These functions are not independent components. Passing the switching check
and invoking the replacement are coupled. Environmental observations can enter
the proof process through the source's time-labelled `state2theorem` operation;
the machine is not limited to deductions about its initial state alone.

Self-modification can also change the proof searcher, axioms, or utility
representation where the predecessor formalization licenses that change.
The construction does not require every later policy choice to have been
listed in the seed, nor does it require an unchanged proof-search implementation
forever ([Schmidhuber, §3.2 and §6.1 (snapshot required)](../sources/goedel-machines-schmidhuber.ingest.md)).

## Three different limits

**Admission.** A useful switch cannot take effect through the proof-gated route
unless the required proof is obtained. The paper says the machine "must ignore
those self-improvements whose effectiveness it cannot prove"
([Schmidhuber, §2.4 (snapshot required)](../sources/goedel-machines-schmidhuber.ingest.md), verbatim).
Some claims may be unprovable under the axioms; others may be provable but not
found within the available resources. These are different limits.

**Adequacy of the formalization.** The Global Optimality Theorem compares a
switch with continuing the search, including the later switches that search
might find. Its guarantee is conditional on the encoded assumptions and
utility. A valid proof under an inadequate model or objective need not warrant
the outcome a user actually wanted. Formalization moves some judgment into the
choice of premises and objective; it does not remove that judgment.

**Practical continuation.** The existence of an admissible beneficial switch
says little about the cost of finding it or about sustained software-production
performance. A restrictive proof gate may allow many useful changes under one
formalization and few under another. No general size estimate follows from
proof-gated admission alone. Likewise, being allowed to emit arbitrary code
does not make a useful empirical successor likely.

## The machine as a judgment-governed self-improving system

The construction meets the definition of
[judgment-governed self-improvement](./definitions/judgment-governed-self-improvement.md). Its later
operation runs its own code, and that code can be read and pointed at. A
rewrite is proposed by the proof searcher and judged by a separate
check, which rejects every rewrite that lacks a proof of the target theorem.
The proof is the special case of the judgment in which one fixed criterion
settles the matter.

The machine is also double-loop capable. The paper lets it rewrite its
utility function and target theorem, on the condition that the new values
are provably better according to the old ones
([Schmidhuber, §6.1 item 4](../sources/goedel-machines-schmidhuber.ingest.md)).
A successor that ranks later alternatives differently is a revised
criterion. The old utility function licenses such a successor only when the
successor serves it better, for example by being cheaper to evaluate. So
what is replaced is a stand-in, and the objective it serves stays fixed, as
[objective revision](./revising-an-improvement-objective-is-licensed-from-outside-it.md)
requires. This describes the construction. No particular run is guaranteed
to revise the criterion.

## Comparison with empirical self-modification

An empirical loop can propose a change, test it, observe later consequences,
and recover without first proving improvement. Its characteristic risk is
accepting harmful changes. The proof route instead risks leaving a useful
change unavailable because its proof is absent or too expensive. Which costs
more depends on the objective, evidence, search process, and consequences of
error.

Consider the narrow case of a prompt-editing loop whose harness loads each edit
without an independent acceptance check. Its revision path is permissive and
its retention reliable, but neither property makes the edit good. Once a harmful
instruction is retained, it can affect later runs. This illustrates why
[false-positive acceptance becomes
operative](./false-positive-generation-is-filtered-before-retention.md).

That is a property of the chosen gate, not of natural-language representation.
A prompt-editing system can add tests, limited authority, independent criticism,
versioning, and rollback. Conversely, executable code can be admitted through a
weak gate. [Available checks](./warranted-autonomy-is-bounded-by-oracle-domain.md)
bound what the observed success warrants in either case. Proof is one way to
govern self-referential changes; it is not the only way to obtain bounded
empirical warrant.

## Acceptance and search pressure differ

The [Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)
uses viability to decide archive admission and benchmark performance to weight
later parent selection. It does not require each archived candidate to prove
or even demonstrate immediate improvement. The [Huxley-Gödel
Machine](../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)
uses evidence about descendants to inform that selection. These are different
uses of evidence from a proof authorizing a switch.

[Incremental Self-Improvement](../sources/on-learning-how-to-learn-learning-strategies.ingest.md)
provides another contrast: a payoff-per-time criterion governs retained
modifications and restoration when they cease to qualify. These cases show why
admission, reproduction, and continued retention should not be collapsed into
one notion of evaluator strength.

Two properties name the difference. A change is **displaced** when a newer
alternative scores higher on the same criterion, with no new evidence about
the change itself. It is **corrected** when evidence from later use counts
against it. Correction is **targeted** when the evidence counts against one
change, which is reversed or weakened while the rest is kept. It is
**bundle** correction when the system can only reverse everything since a
baseline.

- **The Darwin Gödel Machine has displacement and no correction.** An
  agent's score is measured once at admission and never updated. Its
  selection weight falls when higher-scoring agents enter the archive and
  when its own count of children grows. Neither is evidence about the agent.
- **The Huxley-Gödel Machine has targeted correction.** Poor descendants
  lower how often one ancestor is selected, even if no other branch
  improves.
- **Incremental Self-Improvement has bundle correction.** It restores the
  state before a modification together with everything that followed it.

All three apply a criterion they cannot revise. The Darwin Gödel Machine
paper reports the limit in one run: an agent reached the maximum score on a
hallucination check by deleting the logging marker the detector keyed on.
That is evidence against the criterion. No loop in the system could use it,
and the authors responded from outside by hiding the checking functions.

The useful comparison has at least two dimensions: the rigor of inference from
stated premises, and how well those premises and observations cover the
objective. A strong answer on one dimension does not supply the other.

## Grounds for change: proof against on-balance judgment

The Gödel machine is one judgment-governed self-improving system. Commonplace aims at another:
a learner whose judgment is an
[on-balance judgment](./on-balance-judgments-can-guide-improvement-without-a-global-measure.md)
made by a language model. The two share the readable store and the
rejectable decision. They differ in the grounds required for a change, not
in whether the system observes the world or can rewrite its own evaluators.
Natural language, fixed model weights, and the mere presence of
self-modification do not define the difference.

| Question | Proof-governed route | On-balance judgment by a language model |
|---|---|---|
| What justifies a change? | A proof of the switching claim under the formalization | A judgment, on the evidence available, that later work is expected to go better with the change; no single measure is selected |
| How does evidence enter? | Observations enter through formalized operations and can support proofs | Cases, traces and operating consequences are read directly and weighed |
| What if the criterion is inadequate? | A proof does not establish the adequacy of its premises; a revised utility function must be proved better under the old one | The learner can revise the gate, check or weighting it applies, while the declared objective stays fixed |
| What protects against a bad change? | The proof, conditional on the axioms and the utility function | Correction from later evidence, and a preference for changes that can be undone |
| What remains uncertain? | Whether the formalization is adequate and useful proofs can be found within resources | Whether the model's judgments, its diagnoses of later failures and its criterion revisions are reliable enough for the work |

The second route permits acting where the required proof has not been
obtained, and it permits accepting harmful changes. It gives up the proof's
guarantee and puts correction from later evidence in its place, with
[reversibility](./reversibility-can-favor-a-change-by-limiting-future-loss.md)
limiting what a mistaken change can cost before it is corrected. It is
therefore not simply a more permissive admission route. Whether a language
model can make these judgments well enough, with no person judging, is
Commonplace's conjecture, and no test of it has been run. Keep the
capability to acquire a new evaluator separate from the warrant for using
it: replacing an evaluator needs evidence of adequacy, not permission from
the incumbent.

## Scope

- A [reflective system](./definitions/reflective-system.md) needs a causally
  connected self-representation, not a proof of improvement. Proof-gated
  admission is an additional design choice.
- Deductive closure concerns derivable propositions. Transition closure
  concerns states reachable through permitted operations and inputs. Neither
  alone establishes practical reliability.
- The Gödel-machine paper presents a formal construction, not an implemented
  software house with measured continuation reliability. It supports the
  architectural comparison, not a performance ranking.
- Formal causal reasoning would require suitable assumptions and objectives
  inside the formalization. The host architecture alone does not supply them.

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: separates the functions instantiated by the proof route
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: keeps admission evidence relative to what its premises and checks cover
- [Reflective system](./definitions/reflective-system.md) — contrasts: reflection does not require proof-gated admission
- [Judgment-governed self-improvement](./definitions/judgment-governed-self-improvement.md) — defined-in: the definition the machine meets
- [Single-loop and double-loop learning](./definitions/single-loop-and-double-loop-learning.md) — defined-in: the double-loop kind the machine is capable of
- [On-balance judgments can guide improvement without a global measure](./on-balance-judgments-can-guide-improvement-without-a-global-measure.md) — contrasts: the judgment Commonplace puts in the place of the proof
- [Revising an improvement objective is licensed from outside it or is not improvement](./revising-an-improvement-objective-is-licensed-from-outside-it.md) — grounds: why a proved change of utility function replaces a stand-in and leaves the objective fixed
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — extends: explains how a current policy can govern its own revision
- [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — mechanism: identifies the risk of admitting a harmful retained change
- [Schmidhuber, Gödel Machines (snapshot required)](../sources/goedel-machines-schmidhuber.ingest.md) — abstracted-from: supplies the formal construction, theorem, and proof-search limits

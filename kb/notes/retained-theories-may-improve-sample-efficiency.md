---
description: "Conjecture: retained theories may reduce target observations under structured shifts; a useful theory's reuse benefit is separate from selecting it by estimated explanatory-reach"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, discovery]
---

# Retained theories may improve sample efficiency under structured shifts

When a task changes but preserves some underlying structure, a useful theory
may reduce the new observations needed to recover performance. A theory can
supply a basis for diagnosis and revision across many cases instead of making
the learner infer each target behavior independently. Whether retaining that
basis beats reconstructing it is an empirical question.

This note studies an arrangement that retains
[addressable theories](./definitions/addressable-theory.md): formulated
assumptions, scope conditions, and parts that can be inspected and revised
individually. Theories may be expressed in natural language, causal models,
or programs. Retention and addressability are chosen treatments whose benefits
are conjectured. [Conjectural learning](./definitions/conjectural-learning.md)
also admits whole replacement and reconstruction from retained criticism.
It requires criticism of an operative formulated theory to improve capacity
for future action; operating the proposed process does not guarantee learning.

The conjectured pathway is:

> **observations → theory search → assessment of explanatory-reach → retained addressable theory → reuse or revision**

It contains two separable hypotheses:

- **Reuse and revision:** retaining a useful theory and revising it in response
  to criticism may reduce target observations under structured shifts.
- **Selection:** among candidates with comparable source fit, preferring
  estimated explanatory-reach may select theories that transfer better.

The proposed selection rule prefers [explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md)
among revisions that fit the evidence. This is an explicit choice under test,
not a condition of conjectural learning or evidence that the selector works.

[Reach-assessment](./definitions/reach-assessment.md) is the
proposed capability behind the second hypothesis. A useful supplied theory
can deliver the first benefit without being chosen by that selector. Neither
retention nor a gain from the complete arrangement establishes the selector's
contribution. These structured-transfer hypotheses remain distinct from the
[companion's content, addressability, and efficiency conjectures](./commonplace-studies-conjectural-learning-through-retained-theories.md).

## Explanatory-reach supplies the leverage

A theory has [explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) when it captures structure that supports correct conclusions beyond the observations that produced it. That structure may be a causal mechanism, invariant, modular decomposition, compositional rule, or reusable program.

A **structured shift** changes surface regularities while preserving enough of this structure for an earlier theory to remain useful. The learner may then need to identify only which premise, parameter, component, or applicability condition changed, rather than infer each target behavior independently. One theory-level revision can change many downstream predictions at once.

Consider a release exporter whose retained theory says that edits need a
manifest check when the exporter reads the file, and that its configured input
list names every file it reads. Adding a documentation file to that list calls
for applying the existing theory. Later, the exporter gains support for
included snippets. An edit to an unlisted snippet passes a syntax check but
produces an invalid manifest. Criticism identifies the false premise: the
configured list names entry points, not every dependency. The revised theory
includes files reachable through includes, while preserving the connection
between executable consumption and checking. It changes the predicted checks
for other snippets that have never failed.

This hypothetical revision changes a claim, rather than merely deciding
whether an unchanged condition applies. The retained theory supplies a
candidate diagnosis; whether it saves observations compared with discovering
that dependency from a rule such as "documentation files are safe", or
reconstructing the explanation, remains the conjecture.

This is also the central risk. A broad but wrong theory produces broader negative transfer than a local association does, because it is wrong just as widely as it would have been useful — and [stating where a lesson stops](./abstract-an-experience-only-when-you-can-state-the-boundary.md) is a judgment, not something the evidence hands over.

## The capability at issue is reasoning about theories

Testing the whole pathway requires more than storing explicit rules. The learner needs operations for constructing candidates, deriving consequences, identifying assumptions, comparing explanations, seeking discriminating evidence, and revising content or scope. The reuse hypothesis can instead be tested with a supplied theory, isolating its use and revision from discovery and selection. Search and assessment stay distinct stages, [since a proposal-selection loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md): a system can be starved by its search range while its evaluator is sound, or flooded with candidates its evaluator cannot rank.

LLMs can operate on natural-language candidates before the relevant concepts
have been formalized: expose an assumption, compare mechanisms, propose a
counterexample, or rewrite an applicability condition. Consequences attributed
to prose depend on interpretation, and locating the cause of a failure requires
judgment. A plausible post-hoc explanation can be mistaken for a diagnosis.
Criticism can instead overturn a core assumption or require replacing the
whole theory; addressing one part imposes no minimum-edit rule. How reliably
LLMs select theories with genuine explanatory-reach remains open, and two
benchmarks measure adjacent behaviors.

[DiscoverPhysics](../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) places agents in simulated worlds whose laws deliberately differ from our universe's physics, has them propose experiments and observe trajectory data, and collects both a natural-language explanation and a Python implementation of the discovered law. Its abstract-level capture reports that "Strong predictive accuracy doesn't guarantee quality conceptual explanations" ([DiscoverPhysics, Findings](../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md), verbatim). The capture does not reveal how explanation quality was scored or quantify the dissociation. FalsifyBench runs a Wason-style rule-discovery game across twelve models. Its abstract reports that "The primary driver of success is the capacity for negative testing" ([FalsifyBench, abstract](../sources/falsifybench-inductive-reasoning-rule-discovery-games.ingest.md), verbatim): models that test to falsify a hypothesis outperform models that seek confirmation.

Both readings need care. DiscoverPhysics's captured result separates two submitted outputs inside one benchmark, not theory search from reach-assessment in general. FalsifyBench's headline may be partly definitional: on 2-4-6, where the hidden rule is deliberately broader than the seed invites, probes outside the current hypothesis are also the only informative probes, so the correlation could be information gain rather than an epistemic disposition. Neither cited capture establishes reuse of a retained theory across a controlled shift — the gap the comparisons below would need to address — but together they show adjacent behaviors that such a test can separate from predictive fit.

## Addressable parts supply an update interface

A parametric learner can acquire reusable structure. Features learned in one network transfer to related tasks ([Yosinski et al. 2014](https://arxiv.org/abs/1411.1792)), meta-learned initializations adapt from a handful of examples ([Finn, Abbeel, and Levine 2017](https://arxiv.org/abs/1703.03400)), and gradient updates can produce behavior equivalent to revising a theory. The claim cannot be that weights contain only correlations or that they cannot encode theories.

The distinction concerns the interface available to the learning process.
Where retention is purely parametric and no semantic interface exposes what
was retained, an individual theory is not available as a named update target.
The process cannot use that interface to inspect an assumption or revise a
scope condition. The extent and collateral effects of updates must be
assessed behaviorally. This does not classify unknown model-internal
processing: an opaque model may formulate and criticize theories privately.
Evidence of weights or missing visible rationale settles neither presence nor
absence of conjectural learning.

[Addressability](./definitions/addressable-theory.md) makes particular
assumptions and scope conditions available for revision, and comes in degrees.
A theory that can only be replaced whole can still be criticized and can
support learning. Separately editable parts make candidate repairs easier to
name; they do not guarantee correct diagnosis or preservation of other
behavior. Shared premises can affect many conclusions, so regression checks
remain necessary.

Two lines of work show this is a claim about a default rather than an impossibility, and the shape of their shortfall is more informative than the fact that they exist. [ROME](../sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md) applies a rank-one update to transformer weights to change a selected factual association — "factual associations correspond to localized, directly-editable computations" ([ROME, Overview](../sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md), verbatim) — and reports specificity and counterfactual-generalization tests. Calling this content-addressability without scope-addressability is the comparison here: the edit target is addressable, but the edited artifact exposes no premise or applicability boundary to rescope. Concept bottleneck models take the other route, supervising a legible concept layer during training: "By construction, we can intervene on these concept bottleneck models by editing their predicted concept values and propagating these changes to the final prediction" ([Concept bottleneck models, abstract](../sources/concept-bottleneck-models-paper-v3.ingest.md), verbatim). The correction is per-inference rather than a persistent theory revision. In the paper's OAI oracle-correction experiments, a linear downstream predictor benefited less from correction than its nonlinear counterpart despite similar initial task and concept accuracies. Separately, correction slightly increased error in a joint control model with low concept-loss weight and poorer concept alignment. These are limits on correction within a supplied concept vocabulary, not tests of persistent theory revision.

The comparison is therefore between arrangements exposing different update
interfaces, not between learning and non-learning or between neural and
symbolic systems. [Representational form](./definitions/representational-form.md)
helps describe these interfaces. An LLM using retained prose is a hybrid:
weights supply interpretation while artifacts supply persistent identity and
separately revisable content.

## Formalization can buy a mechanical acceptance test

Symbolic systems can implement the same pathway wherever the theory space and acceptance criteria are formalized: causal discovery searches for structure whose consequences survive specified interventions, and [DreamCoder](../sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md) iteratively extends a domain-specific language with reusable symbolic abstractions while training neural search guidance.

Formalization can make acceptance mechanical when the system supplies an explicit retention objective or proof obligation. The DreamCoder snapshot cited here is abstract-only: it supports iterative library growth and compositional reuse, but it does not state a description-length criterion or a discrete retention gate. That capture cannot ground the stronger example; this note retains only its bounded library-growth evidence. The general cost of the formal route remains a supplied language, variables, primitives, search procedure, and acceptance test, [worked out in the causal and proof obligations that formal systems check](./formal-systems-assess-explanatory-reach-through-causal-and-proof.md). LLMs take the opposite trade: a far more open-ended theory space before formalization, with weaker guarantees.

## What the negative results actually bound

Generic "off-distribution" predicts nothing, since some shifts destroy every regularity any system could have retained. The conjecture is conditional on structured shifts, and the transfer literature supports that conditional shape and no more: reusable causal mechanisms are proposed as what survives intervention-like change ([Schölkopf et al. 2021](../sources/towards-causal-representation-learning.ingest.md)), cross-environment stability is proposed as evidence for causal predictors — "we collect all models that do show invariance in their predictive accuracy across settings and interventions. The causal model will be a member of this set of models with high probability" ([Peters, Bühlmann, and Meinshausen 2016, abstract](../sources/causal-inference-using-invariant-prediction.ingest.md), verbatim) — and speed of adaptation to such change can be made a training signal ([Bengio et al. 2019](https://arxiv.org/abs/1901.10912)).

Generalization under shift is hard and assumption-dependent for every method. Under the benchmarks and model-selection procedures studied in [DomainBed](../sources/in-search-of-lost-domain-generalization.ingest.md), the evaluated domain-generalization methods did not consistently beat carefully implemented empirical risk minimization. [Rosenfeld, Ravikumar, and Risteski](../sources/rosenfeld-risks-of-invariant-risk-minimization.ingest.md) bound invariant risk minimization specifically: in their linear Gaussian setting it needs more environments than the environmental-feature dimension, and with nonlinear featurizers the objective *permits* a predictor that is near-identical to the invariant one on the training distribution and reverts to ERM on most sufficiently shifted test points, with an exponentially small penalty. That second result is a formal existence construction. The paper also reports confirming synthetic fits from its own model, but not how often practical optimization reaches the constructed failure outside that setting. This keeps the result compatible with invariance-as-hypothesis-test rather than contradicting it.

The [Bitter Lesson comparison](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md)
does not guarantee that assessed structure survives scaling. Searching theory
space and testing candidates can produce structure instead of relying only on
hand-supplied priors; whether that procedure remains competitive is a further
conjecture. A sufficiently scaled system might perform the useful search
internally, making external artifacts dispensable. The [retained realization
must earn its costs](./a-complete-theory-path-does-not-establish-improved-capacity.md#the-current-llm-plus-artifact-realization).
Nothing here establishes its permanent advantage.

## Cost can erase the gain

The sample-efficiency hypothesis concerns new target observations only. Distinct from it is whether the advantage survives full accounting: theory discovery, [codification](./definitions/codification.md), retrieval, applicability checking, validation, application, maintenance, and correction on one side; pretraining, adaptation data, optimization, and evaluation on the other. Folding every entry into "sample efficiency" conflates the two.

The boundary must be drawn symmetrically. Counting the historical evidence that produced an explicit theory as free, while charging the parametric learner for all its training data, biases the comparison before it starts. Retrieval deserves separate emphasis: a theory nothing surfaces at the moment of need contributes nothing however good it is, while parametric retention avoids a separate retrieval step by residing in the operative substrate — which does not guarantee the relevant behavior activates or generalizes in context. Its discount is differently shaped, not absent. Proof, simulation, model checking, causal analysis, counterexample generation, and targeted experiment can all contribute to criticism when they challenge what the theory says. Their warrant depends on what they test. Interpreting a natural-language theory and locating a defect add judgments whose reliability bounds unattended use, [since warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md).

## What would test the conjecture

The two hypotheses require distinct comparisons so that a useful theory's
contribution is distinguishable from its selector's.

**Reuse and revision comparison.** Use the same base model, source observations,
and inference budget. Keep the initial source-derived theory fixed across
arms that retain it unchanged, allow additions only, or permit revision.
Compare retention separately with reconstruction from retained formulated
criticisms and with reconstruction from records containing only inputs and
outcomes. The first contrast asks what keeping the assembled theory buys;
the second asks what retaining the work of criticism buys. Indexed traces
containing the same conjectures and criticism can implement retained theory;
file format does not distinguish the treatments.

These comparisons estimate differences between the specified arrangements.
They do not establish that a reconstructor lacks private formulated criticism,
or isolate criticism's contribution merely by holding model weights fixed.
Reconstruction and use must actually occur for their costs and benefits to
be compared. A supplied theory using knowledge unavailable in the source
observations is a capability test, not evidence of an end-to-end learning
advantage. Parametric adaptation and formal causal-discovery or
program-synthesis systems can remain additional comparisons, with training
and search costs reported separately.

**Selection comparison.** Give each selector the same candidate theories, source evidence, and selection budget. Compare a selector that prefers estimated explanatory-reach among comparably fitting candidates with selection by source fit alone, using a declared tie-break rule. Keep the downstream application and revision procedure fixed. The selector sees no held-out target outcomes; score its choices on controlled shifts afterward. Include candidate sets with similar source fit but different transfer behavior, so that source fit alone does not settle the choice. This tests whether an LLM's reach judgments add useful selection information beyond source fit. It does not assume that changing an instruction removes all implicit reach-assessment from the model.

Apply controlled shifts of distinct kinds: surface change preserving the mechanism; intervention preserving some causal modules; change invalidating one applicability condition; change invalidating the theory entirely; and a deceptive correlation that held across every source observation. Measure target observations needed to recover performance, mechanism identification, scope calibration, collateral damage to unaffected cases, false transfer, and discovery and validation costs. Evaluate both comparisons over repeated task and candidate sets; a lucky theory choice cannot establish a selector's reliability.

The predictions differ:

- **Reuse and revision:** a useful retained theory should reduce target observations relative to reconstruction from inputs and outcomes on shifts that preserve its structure. Its advantage over reconstruction from retained criticism is a separate question. Where a scope condition changes, permitting revision should improve adaptation relative to freezing that same theory. Incorrect or invalidated theories test the risk of negative transfer; they need not defeat every repair procedure.
- **Selection:** reach-based selection should choose theories with better held-out transfer, or less harmful overgeneralization, than source-fit selection under the matched conditions. A null or negative result would count against this selector's proposed benefit in the tested setting, even if useful theories still help once supplied.

Removing the explicit reach-based selector therefore need not erase the reuse benefit. A generic accuracy gain from the full pathway would establish neither contribution separately.

## Scope

The prediction concerns shifts preserving enough structure for a theory to
remain useful. A broad false theory can instead spread error, and revising it
may cost more than starting again. Neither explicit representation nor local
editability establishes explanatory-reach. A surviving theory can change
future reliance without a text edit. When this is claimed as learning, evidence
must establish improved capacity; unchanged text alone does not decide.

Fewer target observations and lower total cost are separate claims. The
comparison must count discovery and prior evidence symmetrically and keep
selector performance distinct from the benefit of a useful supplied theory.
The benchmarks cited above do not establish either conjecture for this
retained-theory arrangement.

## Open Questions

- Whether a task family with controlled structured shift can be exhibited where this pathway measurably reaches fixed performance on fewer target observations — and whether one can be exhibited where it measurably fails to.
- Whether the declared selection policies produce measurably different choices, and how much implicit reach-assessment remains in the source-fit comparator or downstream revision procedure.
- Whether hybrid pathways — parametric adaptation guided by retrieved explicit theories — dominate both pure pathways, turning the contest into an engineering question about composition.
- Whether a theory's explanatory-reach can be estimated from its addressable form before any shift tests it, or whether legibility supplies only a handle on reach established some other way.
- Whether validating a theory's reach against an informally specified shift is itself target-data-free, or quietly consumes the observations the conjecture claims to save.
- Whether discovery, codification, validation, and maintenance cost for a *library* of many theories grows faster than the smooth cost curve of parametric scaling as task families accumulate.
- Whether, and under which conditions, LLM evaluators rank natural-language theories by explanatory-reach reliably enough to improve held-out transfer beyond source-fit selection; if they do, what accounts for that capability.

---

Relevant Notes:

- [Conjectural learning](./definitions/conjectural-learning.md) — defined-in: the broader process whose membership does not require retained addressable theories
- [Addressable theory](./definitions/addressable-theory.md) — defined-in: the chosen structural property whose payoff is conjectured
- [Reach-assessment](./definitions/reach-assessment.md) — defined-in: the capability that selects the theory whose reach could pay, and which retention does not supply
- [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: the property that carries the conjectured gain, and the negative test that judges it
- [Recognition, not linking, is the hard problem in knowledge systems](./recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) — grounds: theory search turns on recognizing prior observations as instances of a proposed structure, the step that carries the cost
- [Abstract an experience into a lesson only when you can state where the lesson stops](./abstract-an-experience-only-when-you-can-state-the-boundary.md) — grounds: stating applicability conditions is a judgment, not a derivation from the evidence
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the search/evaluation split that keeps theory generation distinct from reach-assessment
- [Representational form](./definitions/representational-form.md) — defined-in: the natural-language, symbolic, and distributed-parametric axis the parametric contrast runs along
- [Codification](./definitions/codification.md) — defined-in: the natural-language-to-symbolic crossing the cost ledger names
- [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](./formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — extends: develops the formal routes and their dependence on a supplied language
- [World models assess explanatory-reach through action-conditioned prediction](./world-models-assess-explanatory-reach-through-action-conditioned.md) — contrasts: a distributed-parametric route to the same assessment
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — mechanism: why validation warrants conclusions only within the domain its checks cover
- [DiscoverPhysics](../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) — evidenced-by: an abstract-level report that predictive accuracy and conceptual-explanation quality can come apart; scoring and magnitude are unavailable in the capture
- [FALSIFYBENCH](../sources/falsifybench-inductive-reasoning-rule-discovery-games.ingest.md) — evidenced-by: falsification-seeking test selection predicts rule-discovery success across models
- [ROME](../sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md) — evidenced-by: a targeted rank-one factual edit with specificity and generalization tests; the scope-addressability comparison is target-side
- [Concept bottleneck models](../sources/concept-bottleneck-models-paper-v3.ingest.md) — evidenced-by: a supervised interface correctable per inference; OAI oracle-correction experiments show that similar initial accuracy need not imply similar correction benefit
- [DreamCoder](../sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md) — evidenced-by: iterative growth of reusable symbolic abstractions; the current capture does not expose a description-length retention gate
- [In search of lost domain generalization](../sources/in-search-of-lost-domain-generalization.ingest.md) — evidenced-by: specialized generalization methods did not consistently beat tuned ERM under a fixed protocol
- [The risks of invariant risk minimization](../sources/rosenfeld-risks-of-invariant-risk-minimization.ingest.md) — evidenced-by: bounds the IRM objective specifically, in the linear regime by environment count and outside it by an existence proof

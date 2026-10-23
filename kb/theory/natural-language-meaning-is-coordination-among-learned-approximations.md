---
description: "Untested hypothesis extending Lampinen's learned-approximation mechanism to natural language: no external semantics exists to approximate, so meaning is coordination held by weak checks; recasts constraining and deviation diagnosis"
type: types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, constraining, llm-reliability]
---

# Natural-language meaning is coordination among learned approximations, not approximation of a target

This note states a hypothesis. It is our extrapolation from a mechanism Andrew Lampinen describes; Lampinen does not state it, and it has not been tested.

## The mechanism it starts from

Andrew Lampinen argues that a general pattern-learner, brain or network, has no innate symbol manipulation: "Classical symbol manipulation" is "something we learn with effort" ([Lampinen](../sources/symbols-neural-networks-mathematical-intelligence.ingest.md), verbatim). It uses external symbol systems as scaffolds; "by doing so, we can learn to internalize approximations of these systems" ([Lampinen](../sources/symbols-neural-networks-mathematical-intelligence.ingest.md), verbatim). Those approximations stay imperfect: "even then they remain fallible" (verbatim).

"Approximation" presupposes a target. For a formal language such as Lean the target exists: a checker with a unique operational semantics sits outside every learner, and each learner's competence is measured against it.

## The hypothesis

The same learning mechanism produces natural-language competence, but there is no external artifact to approximate. Nobody holds the real semantics that others approximate. Natural-language semantics is then not a target. It is a population of graded internal approximations that stay aligned only where something checks them against each other. "Coordination" names this case more accurately than "approximation", and the difference is substantive: the population has nothing to converge on except each other.

Other speakers, the shared world, and retained texts such as dictionaries and legal definitions play the checker's role. This checker is weak, distributed, and slow in the sense of the [oracle strength spectrum](./oracle-strength-spectrum.md). The hypothesis predicts that meaning is sharpest where correction is cheap and frequent (concrete nouns, counting, institutionally policed technical terms) and loosest where little checks a use (abstract terms such as "intelligence" or "learning"). Interpretation variance should grow with distance from checkable use.

[Constraining](./definitions/constraining.md) is then the operation that installs a local checker for a natural-language artifact. It does not narrow a fixed meaning. It acts on a population of approximations and raises their alignment by making one reading checkable. [Codification](./definitions/codification.md) is the limit case: the checker becomes a runtime, and the target becomes real.

## Consequences

**Deviation diagnosis.** [LLM output deviation requires three-way diagnosis](./llm-output-deviation-requires-three-way-diagnosis.md) models deviation with the set of outputs the user would accept (`I`), the set the specification admits (`V`), and the interpreter's output distribution (`D`). The hypothesis reshapes each question.

- [Underspecification](./agentic-systems-interpret-underspecified-instructions.md), `V` wider than `I`, is not only an author's omission. For weakly checked terms no artifact fixes what the specification admits, so `V` has no sharp boundary. Underspecification is structural for natural language and shrinks only where a checker exists.
- [Interpreter failure](./out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md), `D` outside `V`, presupposes a determinate `V`. Its test asks whether a competent reader given only the spec would accept the output. For unchecked terms that question has no determinate answer, so the line between underspecification and interpreter failure blurs. Registered definitions sharpen `V`'s boundary and make the question askable.
- [Indeterminism](./execution-indeterminism-is-a-property-of-the-sampling-process.md), the spread of `D`, is the single-model analogue of variance across speakers.

The perfect interpreter assumed in the underspecification case is the natural-language counterpart of the Lean checker: a fixed semantics no learner has. The hypothesis says that counterpart does not exist, which is why diagnosis needs three questions rather than one.

**Formalization runs the other way.** For Lean the formal artifact came first; for natural language the approximations did. Montague-style formal semantics is a later codification of the regions that stabilized, a lossy retrospective grammar rather than what speakers learned. This is [progressive constraining](./progressive-constraining-commits-only-after-patterns-stabilize.md) applied to language itself.

**Meaning sits on the pattern side.** Lampinen quotes Mac Lane that "strict formalism can’t explain which of many formulas matter" and glosses it in his own words: "it is meaning that resolves the frame problem" ([Lampinen](../sources/symbols-neural-networks-mathematical-intelligence.ingest.md), verbatim). He places meaning on the intuitive side that formal systems lack. Applied to natural language, semantics is a property of learned pattern-competence.

[Fodor and Pylyshyn's primary argument](../sources/fodor-pylyshyn-1988-connectionism-cognitive-architecture.ingest.md) concerns systematicity: the ability to understand some sentences is linked to the ability to understand certain others. They argue that these linked capacities require mental representations with constituent structure and processes sensitive to that structure. Compositionality adds a semantic condition: shared constituents make approximately the same contribution across expressions. Their account permits implicit rules, performance errors, and neural implementation. Learned, fallible competence therefore does not by itself distinguish this hypothesis from their position.

On this hypothesis, communication pressure produces competence whose compositionality is approximate. Approximation alone does not answer their argument, since their semantic condition already allows it. The hypothesis still needs a mechanism explaining why related capacities develop together and why constituent meanings remain sufficiently stable across expressions. Whether such a mechanism would meet their requirements for structured representation and processing remains open.

[Smolensky's account](../sources/smolensky-proper-treatment-connectionism.ingest.md) offers another comparison: cultural knowledge is expressed for reliable use by different people, while individual intuitive knowledge depends on experience and may require a different form of description. This distinction separates how competence is represented in an individual from how knowledge is shared. Moving from learned individual competence to this note's claim that natural-language meaning has no external target still requires an additional argument.

**LLMs are a second-order case.** A language model learns from text written by speakers who each hold only approximations. Nothing in the chain is the real meaning, which weakens arguments that a model lacks a semantics that humans possess.

**KB vocabulary.** The vocabulary section of `AGENTS.md`, the `kb/notes/definitions/` directory, and the one-term-per-concept rule install small local symbol systems for agents and sessions to approximate. They raise oracle strength for a few terms without reaching codification, because the checker is still a reader. One term per concept concentrates checking pressure on one word so its approximations converge; a synonym splits the pressure and lets both words drift.

[Vocabulary-collision controls](./vocabulary-collisions-prevented-at-write-time-not-read-time.md) make this proposal more concrete: distinct terms and explicit clause frames help delimit a technical sense, while validator-defined positions can enforce its use. A definition alone supplies no such enforcement. These are candidate mechanisms for improving local alignment; their availability does not establish this hypothesis.

## Scope

- The hypothesis is untested. A test: interpretation variance among agents should track how often a term's use gets corrected. Review-gate disagreement across terms with and without registered definitions is one measurable proxy. The KB-vocabulary consequence is refuted if registered terms show no lower disagreement than comparable unregistered terms.
- Lower disagreement alone would not show better judgment: [reviewers can share the same prior](./reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) and agree on the same error. A test should measure agreement separately from errors against an independently specified local use, including uses not seen during correction. This would test the KB-vocabulary consequence, not settle the broader theory of meaning.
- Lampinen's essay supplies the mechanism, not evidence for this extension; its own evidence concerns mathematics.

---

Relevant Notes:

- [Symbols, neural networks, and mathematical intelligence](../sources/symbols-neural-networks-mathematical-intelligence.ingest.md) — abstracted-from: supplies the learned-approximation mechanism this note extends to natural language, where the essay does not go
- [LLM output deviation requires three-way diagnosis](./llm-output-deviation-requires-three-way-diagnosis.md) — extends: explains why the valid set has no sharp boundary for weakly checked terms
- [oracle strength spectrum](./oracle-strength-spectrum.md) — extends: places the checkers of natural-language meaning at the weak, distributed end of the spectrum
- [progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) — extends: reads formal semantics as progressive constraining applied to language
- [constraining](./definitions/constraining.md) — defined-in: the operation this note recasts as installing a local checker
- [codification](./definitions/codification.md) — defined-in: the limit case where the checker becomes a runtime

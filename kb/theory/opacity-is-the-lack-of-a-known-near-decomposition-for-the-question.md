---
description: "Proposes one mechanism behind the three sources of opacity, no known decomposition that puts the inspection question inside an affordable block, and reads the inspection cost as description length over a chosen vocabulary of units."
type: types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, artifact-analysis]
---

# Opacity is the lack of a known near-decomposition for the question

An artifact is [opaque](./opacity-depends-on-the-inspection-question-and-budget.md) for a question when no known decomposition of it puts the question's units inside a block the inspector can afford to read, with the rest of the artifact entering through a few aggregates. This note proposes that condition as the mechanism behind the three sources of opacity that [representational form](./definitions/representational-form.md) names: the artifact's scale, the reference's form, and deliberate obfuscation. It also gives the inspection cost a reading: the description length of the cheapest known explanation of the behavior in question, over a chosen vocabulary of units. The transfer from Simon's dynamic systems to dependency structure in artifacts is this note's conjecture, not Simon's claim.

## The condition

Simon's [Architecture of Complexity](../sources/herbert-simon-architecture-of-complexity.ingest.md) introduces the condition as a second approximation after perfectly separable systems: a theory of nearly decomposable systems, in which the interactions, verbatim, "among the subsystems are weak, but not negligible." Two propositions follow, quoted verbatim with the capture's typography: "( a ) in a nearly decomposable system, the shortrun behavior of each of the component subsystems is approximately independent of the short-run behavior of the other components; ( b ) in the long run, the behavior of any one of the components depends in only an aggregate way on the behavior of the other components."

Read interaction as dependency between the units of an artifact: a call, a citation, a shared variable, a weight that two computations use. A question about a unit's behavior on a short horizon then needs only the block the unit sits in. Other blocks enter through a few aggregate quantities, which is what an interface is. The cost of the question is the size of the block that contains its units plus the number of aggregates crossing the block's boundary, for the question's horizon and tolerance. It is not the artifact's total size. Dense coupling, or a hub every block depends on, defeats local reading while each unit stays readable.

The condition is relative to the question in two ways Simon already names. The horizon decides whether a block is independent: short-run questions localize, long-run questions reach every block through aggregates. The tolerance decides which interactions count as weak. Both belong beside an opacity judgment, as the opacity note's question and acceptable cost.

## The measure

The reading of inspection cost as a description length follows [Grünwald's](../sources/grunwald-mdl-tutorial.ingest.md) crude two-part form of the minimum description length principle, verbatim: "The best point hypothesis H ∈ H(1) ∪ H(2) ∪ . . . to explain the data D is the one which minimizes the sum L(H) + L(D|H), where • L(H) is the length, in bits, of the description of the hypothesis; and • L(D|H) is the length, in bits, of the description of the data when encoded with the help of the hypothesis."

Mapped to inspection, the hypothesis is the block and its rules, and the residual is what the aggregates and the exceptions add. Three properties of the measure follow from Grünwald's own qualifications, and each matches a qualification the opacity note already carries.

The measure is relative to a description method. [Grünwald](../sources/grunwald-mdl-tutorial.ingest.md) requires one that is, verbatim, "restrictive enough" that the shortest description is computable, chosen by prior knowledge of the domain. For inspection the description method is the vocabulary of units the consumption path exposes, so the same artifact has different costs under different paths, which is why opacity is path-relative.

A found explanation is an upper bound. The shortest description is uncomputable, so the cheapest explanation known today bounds the cost from above, and a better decomposition found later lowers it without changing the artifact.

The hypothesis side can be gamed. [Grünwald](../sources/grunwald-mdl-tutorial.ingest.md) notes, verbatim, that the length of a hypothesis "can be very large under one code, but quite short under another", so a crude code for hypotheses is "in danger of becoming arbitrary". A comparison of inspection costs is honest only when the vocabulary of units is fixed before the comparison. The KB does not compute these lengths; the measure fixes what a cost comparison has to hold constant.

## One failure, three sources

The three sources of opacity differ in what has happened to the decomposition, not in the kind of obstacle.

- **Scale.** A decomposition is known, and the block containing the question is too large to read, or a hub couples it to everything. Each unit is readable; the question is not affordable.
- **The reference's form.** No decomposition aligned with the question is known under the path on which the question is asked. Kernels and tensor operands are a near-decomposition of a model's weights for runtime questions. For the question of what the model does with an instruction, no block of parameters is known to be the block. Superposition is the specific form of the failure: many concepts share the same units, so the blocks the question wants do not exist as blocks of parameters.
- **Deliberate obfuscation.** A decomposition is destroyed on purpose. The transformation makes every unit depend on every other for the inspector's questions while preserving the function. The cryptographic results the opacity note cites bound how completely this can be done.

Known but expensive, unknown, and destroyed are three states of one condition. This is why the modifier is one word.

## Finding a decomposition lowers opacity without changing the artifact

Mechanistic interpretability is the search for a decomposition where none is exposed. [Templeton and co-authors](../sources/scaling-monosemanticity-claude-3-sonnet.ingest.md) train sparse autoencoders on a production model's activations and test the found units by intervention. Clamping the Golden Gate Bridge feature to ten times its maximum activation changes behavior as the feature's interpretation predicts; verbatim, "In this example, the model starts to self-identify as the Golden Gate Bridge!"

Under the path that addresses features, the activations are localized for the behaviors the found features cover, and [the authors](../sources/scaling-monosemanticity-claude-3-sonnet.ingest.md) are explicit that the coverage is partial. Verbatim, they "could only find features corresponding to about 60% of the boroughs" of London in their largest dictionary, and call the found set "an incomplete description of the model's internal representations". So localization under an interpretability path is graded by coverage, and the form under the path on which a system runs the model is unchanged.

[ROME](../sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md) is the same move on weights: a factual association is located, edited, and the edit's effect checked.

Both cases give content-addressability without scope-addressability, and Simon's condition says what that means structurally. The found block is strongly coupled inside: clamping one feature moves everything the feature covers. Its links to the rest are not weak: the clamp leaks into the model's self-identification, and [the authors](../sources/scaling-monosemanticity-claude-3-sonnet.ingest.md) report, verbatim, that useful steering "typically requires clamping feature activations to values outside their observed range", which they attribute to perturbing one feature when "several correlated features with related meanings" are co-active. A block whose cross-block interactions are not negligible is not yet a nearly decomposable unit, so the edit cannot be confined to the behavior it targets.

## Consequence for addressability

The two propositions map onto repair. Short-run independence is what lets a failure be blamed on a part and fixed there. Long-run dependence through aggregates is holism in structural terms: on a long enough horizon every part answers to every other, which is why a test can bear on a large part of a system. So a located part is a sound candidate for repair, in the sense of [addressable theory](./definitions/addressable-theory.md), only where its interactions with the other parts are weak on the horizon of the test.

## Scope

- Simon's result is a theorem about linear dynamic systems described by a nearly decomposable interaction matrix. Reading interaction as dependency between an artifact's units is this note's transfer. It needs a worked case on a real codebase or KB dependency graph before it can enter a definition as more than a mechanism.
- Decomposability is a structure. Opacity is a cost judgment on top of it, relative to the question, to the decompositions known, and to the budget. Composability of a construction is neither necessary nor sufficient: a model is composed of operations that are fully understood and is not decomposable for instruction-level questions.
- Simon flags a selection effect: a world may look hierarchic because its non-hierarchic parts elude understanding. The mechanism explains the affordable cases without showing that they predominate.
- The measure fixes what a cost comparison must hold constant. It yields no number the KB can compute.

## Open Questions

- Compression. Simon ties near-decomposability to the redundancy that makes a compact description of a system possible, and the [epiplexity](../sources/from-entropy-to-epiplexity-rethinking-information-computational.ingest.md) ingest's time-bounded description length is the nearest formal neighbor. Whether inspection cost and compressibility are one quantity or two is a separate task.
- Whether obfuscation is exactly the destruction of near-decomposability, or only one route to it.
- The worked case named under Scope.

---

Relevant Notes:

- [Opacity depends on the inspection question and budget](./opacity-depends-on-the-inspection-question-and-budget.md) — extends: the three sources of opacity and their evidence; this note proposes the condition they share
- [Representational form](./definitions/representational-form.md) — defined-in: the opaque modifier and path-relative localization
- [Addressable theory](./definitions/addressable-theory.md) — defined-in: the graded property whose structural precondition the last section states
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](./localized-retention-pays-where-change-is-sparse-in-a-matching.md) — contrasts: change locality after Parnas against interaction locality after Simon; its impact closure is an interaction condition stated in change terms
- [Simon, The Architecture of Complexity](../sources/herbert-simon-architecture-of-complexity.ingest.md) — evidenced-by: the definition of near-decomposability and its two propositions; the theorem is cited there, not stated
- [Grünwald, A tutorial introduction to the minimum description length principle](../sources/grunwald-mdl-tutorial.ingest.md) — evidenced-by: the two-part code and its relativity to a description method
- [Templeton et al., Scaling Monosemanticity](../sources/scaling-monosemanticity-claude-3-sonnet.ingest.md) — evidenced-by: a found decomposition tested by intervention, with partial coverage and leakage across the found blocks
- [ROME](../sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md) — evidenced-by: the same move on weights, giving content-addressability without scope-addressability

---
description: "Conjectures near-decomposability as a mechanism for affordable inspection; explores description length as a cost proxy and separates locating a faulty part from containing a repair."
type: types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, artifact-analysis]
---

# Near-decomposability may make local inspection affordable

A known near-decomposition may make local inspection affordable when it captures the dependencies relevant to the question. This note proposes that mechanism for the three sources of [opacity](./opacity-depends-on-the-inspection-question-and-budget.md): scale, the reference's form, and deliberate obfuscation. Whether it explains every affordable inspection route remains open. Description length is explored as a proxy for the amount to explain; finding and checking that explanation also cost work. The transfer from Simon's dynamic systems to dependency structure in artifacts is this note's conjecture, not Simon's claim.

## The condition

Simon's [Architecture of Complexity](../sources/herbert-simon-architecture-of-complexity.ingest.md) introduces the condition as a second approximation after perfectly separable systems: a theory of nearly decomposable systems, in which the interactions, verbatim, "among the subsystems are weak, but not negligible." Two propositions follow, quoted verbatim with the capture's typography: "( a ) in a nearly decomposable system, the shortrun behavior of each of the component subsystems is approximately independent of the short-run behavior of the other components; ( b ) in the long run, the behavior of any one of the components depends in only an aggregate way on the behavior of the other components."

The proposed transfer reads interaction as dependency between the units of an artifact: a call, a citation, a shared variable, a weight that two computations use. If the question's relevant dependencies fit inside one block and the remaining effects can be captured by interface summaries, local inspection need not read the whole artifact. The block and those summaries determine how much material must be examined. Whether that material is affordable to understand and check is a further question. Dense coupling, or a hub every block depends on, can defeat local reading while each unit stays readable.

In this transfer, the horizon and tolerance determine which interactions may be ignored or summarized. A decomposition useful for one question need not support another. The analogy does not establish that every artifact has a short horizon on which questions localize, or that every long-horizon question reaches every block.

## A proposed description-length proxy

The reading of inspection cost as a description length follows [Grünwald's](../sources/grunwald-mdl-tutorial.ingest.md) crude two-part form of the minimum description length principle, verbatim: "The best point hypothesis H ∈ H(1) ∪ H(2) ∪ . . . to explain the data D is the one which minimizes the sum L(H) + L(D|H), where • L(H) is the length, in bits, of the description of the hypothesis; and • L(D|H) is the length, in bits, of the description of the data when encoded with the help of the hypothesis."

Mapped to inspection, the hypothesis is the block and its rules, and the residual is what the aggregates and the exceptions add. In the [prompt case](./english-can-approximate-a-model-defined-prompt-language.md), the hypothesis is the coarse English account and the residual describes observed behavior left unexplained by it. The proposed empirical test probes that residual; a description-length score additionally requires a specified encoding. This mapping proposes a description-length proxy; it does not establish that description length measures inspection effort. The following qualifications constrain the proposal.

The measure is relative to a description method. [Grünwald](../sources/grunwald-mdl-tutorial.ingest.md) requires one that is, verbatim, "restrictive enough" that the shortest description is computable, chosen by prior knowledge of the domain. For inspection the description method is the vocabulary of units the consumption path exposes, so the same artifact has different costs under different paths, which is why opacity is path-relative.

A found explanation and its residual supply an upper bound on the shortest description available in the chosen description method. The restriction quoted above makes the minimum computable in practical MDL; a search that merely retains the shortest explanation found so far need not have reached it. Neither quantity bounds the effort of finding or checking that explanation without a further cost model.

The hypothesis side can be gamed. [Grünwald](../sources/grunwald-mdl-tutorial.ingest.md) notes, verbatim, that the length of a hypothesis "can be very large under one code, but quite short under another", so a crude code for hypotheses is "in danger of becoming arbitrary". A comparison of inspection costs is honest only when the vocabulary of units is fixed before the comparison. The KB does not compute these lengths; the measure fixes what a cost comparison has to hold constant.

## One failure, three sources

The conjecture reads the three sources of opacity as different obstacles to local decomposition:

- **Scale.** A decomposition is known, and the block containing the question is too large to read, or a hub couples it to everything. Each unit is readable; the question is not affordable.
- **The reference's form.** The units exposed by the reference may not align with the question. Kernels and tensor operands expose runtime operations without supplying a readable instruction-level rule. A coarse semantic description of the prompt may still answer the question, as [the English approximation account](./english-can-approximate-a-model-defined-prompt-language.md) explains. Opacity remains where that description is insufficient and the relevant detail cannot be established affordably; the absence of a separate parameter block alone does not establish it.
- **Deliberate obfuscation.** A transformation may hide or disrupt a decomposition while preserving the function. Whether this explains the inspection obstacle must be established for the transformation and question. The cryptographic results summarized in the opacity note do not by themselves establish this structural account.

Known but expensive, unknown, and disrupted would then be three states of one obstacle. Opacity's definition does not depend on this unification succeeding.

## Finding a decomposition lowers opacity without changing the artifact

Mechanistic interpretability is the search for a decomposition where none is exposed. [Templeton and co-authors](../sources/scaling-monosemanticity-claude-3-sonnet.ingest.md) train sparse autoencoders on a production model's activations and test the found units by intervention. Clamping the Golden Gate Bridge feature to ten times its maximum activation changes behavior as the feature's interpretation predicts; verbatim, "In this example, the model starts to self-identify as the Golden Gate Bridge!"

Under the path that addresses features, the activations are localized for the behaviors the found features cover, and [the authors](../sources/scaling-monosemanticity-claude-3-sonnet.ingest.md) are explicit that the coverage is partial. Verbatim, they "could only find features corresponding to about 60% of the boroughs" of London in their largest dictionary, and call the found set "an incomplete description of the model's internal representations". So localization under an interpretability path is graded by coverage, and the form under the path on which a system runs the model is unchanged.

[ROME](../sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md) is the same move on weights: a factual association is located, edited, and the edit's effect checked.

Both cases offer handles on content without establishing independently controllable scope. The proposed transfer of Simon's condition asks whether the relevant interactions are weak enough for the intended intervention. The found block is strongly coupled inside: clamping one feature moves everything the feature covers. Its links to the rest are not weak: the clamp leaks into the model's self-identification, and [the authors](../sources/scaling-monosemanticity-claude-3-sonnet.ingest.md) report, verbatim, that useful steering "typically requires clamping feature activations to values outside their observed range", which they attribute to perturbing one feature when "several correlated features with related meanings" are co-active. These observations do not establish that cross-block effects stay within a chosen tolerance. Near-decomposability allows weak nonzero interactions; whether a particular intervention is contained needs its own check.

## Consequence for addressability

The proposed transfer to repair concerns how much must be checked after an edit. If a decomposition captures the dependencies relevant to the test, weak interactions across its blocks may let the inspector assess the edit within one block and its interfaces. Establishing that the decomposition captures those dependencies is part of the work.

That is separate from locating a repair candidate in an [addressable theory](./definitions/addressable-theory.md), whose parts can be inspected and revised individually. Consider a shared conversion routine that adds one where its stated rule requires adding two. A trace through that operation can identify a candidate fault even when many callers depend on the routine. Repairing it still requires checking the affected callers. Many callers establish a broad dependency footprint, not by themselves strong interaction between blocks. For a direct coupled case, consider the explicitly stated equations `x = y + 1` and `y = 2x`: each equation is separately editable although changing either can change both variables. Separate editability does not require independent consequences.

## Scope

- Simon's result is a theorem about linear dynamic systems described by a nearly decomposable interaction matrix. Reading interaction as dependency between an artifact's units is this note's transfer. It needs a worked case on a real codebase or KB dependency graph before it can enter a definition as more than a mechanism.
- Decomposability is a structure. Opacity is a cost judgment on top of it, relative to the question, to the decompositions known, and to the budget. Composing a model from understood numerical operations does not by itself supply an affordable instruction-level description. A coarse semantic decomposition may supply one without locating separate parameter blocks.
- Simon flags a selection effect: a world may look hierarchic because its non-hierarchic parts elude understanding. The mechanism explains the affordable cases without showing that they predominate.
- Description length is a proposed proxy for the amount to explain, not a measure of the work of finding or checking the explanation. No calibrated relation between these costs is established here. The KB computes neither quantity.

## Open Questions

- Compression. Simon ties near-decomposability to the redundancy that makes a compact description of a system possible, and the [epiplexity](../sources/from-entropy-to-epiplexity-rethinking-information-computational.ingest.md) ingest's time-bounded description length is the nearest formal neighbor. Whether inspection cost and compressibility are one quantity or two is a separate task.
- Whether obfuscation is exactly the destruction of near-decomposability, or only one route to it.
- Whether affordable abstraction or certificate checking can answer a question without the near-decomposition proposed here. Such a case would limit the mechanism to local reading rather than opacity in general.
- The worked case named under Scope.

---

Relevant Notes:

- [Opacity depends on the inspection question and budget](./opacity-depends-on-the-inspection-question-and-budget.md) — extends: the three sources of opacity and their evidence; this note proposes the condition they share
- [Representational form](./definitions/representational-form.md) — defined-in: the opaque modifier and path-relative localization
- [Addressable theory](./definitions/addressable-theory.md) — defined-in: the graded property that exposes repair candidates, separately from the cost of checking their effects
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](./localized-retention-pays-where-change-is-sparse-in-a-matching.md) — contrasts: change locality after Parnas against interaction locality after Simon; its impact closure is an interaction condition stated in change terms
- [Simon, The Architecture of Complexity](../sources/herbert-simon-architecture-of-complexity.ingest.md) — evidenced-by: the definition of near-decomposability and its two propositions; the theorem is cited there, not stated
- [Grünwald, A tutorial introduction to the minimum description length principle](../sources/grunwald-mdl-tutorial.ingest.md) — evidenced-by: the two-part code and its relativity to a description method
- [Templeton et al., Scaling Monosemanticity](../sources/scaling-monosemanticity-claude-3-sonnet.ingest.md) — evidenced-by: a found decomposition tested by intervention, with partial coverage and leakage across the found blocks
- [ROME](../sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md) — evidenced-by: the same move on weights, giving content-addressability without scope-addressability

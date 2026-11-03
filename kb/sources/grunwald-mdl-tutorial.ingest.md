---
description: "Grünwald's MDL tutorial: description length relative to a restricted, computable code class, crude two-part vs refined MDL, and why that measure is not Kolmogorov complexity"
source: https://arxiv.org/abs/math/0406077
captured: "2026-11-03"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 667ec67af72404f9ee9fca80005a1d0c11014895991ad04f6f3f301e367c05de
ingested: "2026-11-03"
occasion: "whether MDL supplies a measure for the length of the cheapest known explanation of an artifact's behavior over a given vocabulary of units, as distinct from the Kolmogorov complexity of the artifact."
type: types/ingest-report.md
learning_claims: true
domains: [minimum-description-length, model-selection, kolmogorov-complexity, inductive-inference]
tags: [learning-theory]
---

# Ingest: A Tutorial Introduction to the Minimum Description Length Principle

## Classification

This is a technical tutorial and survey rather than a paper with new results. Chapter 1 gives a non-technical account of the principle. Chapter 2 makes it precise through prefix codes, the Kraft inequality, universal codes, normalized maximum likelihood (NML), four interpretations of parametric complexity, and a section on known problems. The captured version is arXiv v1 (2004), prepared as the opening chapters of an MIT Press edited collection. The analysis is worked out from [arXiv math/0406077](https://arxiv.org/abs/math/0406077).
Author: Peter Grünwald (CWI Amsterdam), a leading MDL researcher. He writes as an advocate. He defends MDL against its critics, but he also gives a section to its real failures (§2.10.2), and a footnote says his own views are milder than Rissanen's.

## Summary

The tutorial presents MDL as inductive inference by compression: any regularity in data can be used to describe it in fewer symbols, so the hypothesis or model that compresses the data most has captured the most regularity. Grünwald first sets aside "ideal" MDL, which is based on Kolmogorov complexity, because it is uncomputable and depends on the syntax of the chosen language at small sample sizes (§1.2.1). Practical MDL instead fixes a description method C that is restrictive enough that the shortest description attainable with C can always be computed, and accepts that some regular sequences will then not be compressible (§1.2.2). Crude two-part MDL minimizes L(H) + L(D|H). L(D|H) is fixed as −log P(D|H). L(H) needs a code for hypotheses, and an ad hoc code makes the procedure "in danger of becoming arbitrary" (§1.4, §2.4.2). Refined MDL replaces the two-part code with a universal one-part code per model, the NML code, whose length is stochastic complexity = fit + parametric complexity COMP(M). It argues that this removes the arbitrariness for finite sets of well-behaved parametric models, and that COMP is invariant under reparameterization (§1.4, §2.6, §2.10.1). Rissanen's philosophy treats models as languages, defines noise as the residual bits under the chosen model rather than as a random variable, and treats the simplicity preference as a strategy, not a claim that the world is simple (§1.5, §1.6). Grünwald concedes that carving infinite model classes involves unavoidable arbitrariness, and that MDL can fail under misspecification even though it was designed not to assume a true distribution (§2.10).

## Contribution assessment (our opinion)

The problem, model selection from limited data without assuming that a candidate model is true, is central to statistics and learning theory. The tutorial's contribution is clarification and synthesis rather than new theorems. It sharply separates the uncomputable Kolmogorov ideal, the vocabulary-dependent crude two-part criterion, and the minimax-justified refined criterion. It also collects four independent rationales (compression, counting distinguishable distributions, Bayes with Jeffreys' prior, prequential prediction) under one quantity. Grünwald says the crude/refined terminology is his own pedagogical coinage (note 4). As far as background knowledge goes, it has since become a standard way of explaining the field. This judgment does not rest on a literature survey. The account survives criticism mainly because the author states its limits himself: refined MDL is fully specified only for a restricted class of parametric models, and misspecification failures are acknowledged rather than explained. The demonstrated value is conceptual precision. Claims about practical performance rest on cited work that this ingest did not check.

## Quotes

> Let H(1) , H(2) , . . . be a list of candidate models (e.g., H(k) is the set of k-th degree
> polynomials), each containing a set of point hypotheses (e.g., individual polynomials). The best point hypothesis H ∈ H(1) ∪ H(2) ∪ . . . to explain the data D is the
> one which minimizes the sum L(H) + L(D|H), where
> • L(H) is the length, in bits, of the description of the hypothesis; and
> • L(D|H) is the length, in bits, of the description of the data when encoded
> with the help of the hypothesis.
> --- `kb/sources/.snapshots/grunwald-mdl-tutorial.md` @ `sha256:667ec67af72404f9ee9fca80005a1d0c11014895991ad04f6f3f301e367c05de` — §1.3, crude two-part version of the MDL principle

> 1. uncomputability It can be shown that there exists no computer program that,
> for every set of data D, when given D as input, returns the shortest program that
> prints D [Li and Vitányi 1997].
> 2. arbitrariness/dependence on syntax In practice we are confronted with small
> data samples for which the invariance theorem does not say much. Then the
> hypothesis chosen by idealized MDL may depend on arbitrary details of the syntax
> of the programming language under consideration.
> --- `kb/sources/.snapshots/grunwald-mdl-tutorial.md` @ `sha256:667ec67af72404f9ee9fca80005a1d0c11014895991ad04f6f3f301e367c05de` — §1.2.1, why idealized (Kolmogorov) MDL is not practically applicable

> Such description methods C should be restrictive enough so that
> for any data sequence D, we can always compute the length of the shortest description
> of D that is attainable using method C; but they should be general enough to allow us
> to compress many of the intuitively ‘regular’ sequences. The price we pay is that, using
> the ‘practical’ MDL Principle, there will always be some regular sequences which we
> will not be able to compress. But we already know that there can be no method for
> inductive inference at all which will always give us all the regularity there is — simply
> because there can be no automated method which for any sequence D finds the shortest
> computer program that prints D and then halts. Moreover, it will often be possible to
> guide a suitable choice of C by a priori knowledge we have about our problem domain.
> --- `kb/sources/.snapshots/grunwald-mdl-tutorial.md` @ `sha256:667ec67af72404f9ee9fca80005a1d0c11014895991ad04f6f3f301e367c05de` — §1.2.2, practical MDL uses a restricted description method C

> Definition of L(H): A Problem for Crude MDL It is more problematic to find
> a good code for hypotheses H. Some authors have simply used ‘intuitively reasonable’
> codes in the past, but this is not satisfactory: since the description length L(H) of
> any fixed point hypothesis H can be very large under one code, but quite short under
> another, our procedure is in danger of becoming arbitrary.
> --- `kb/sources/.snapshots/grunwald-mdl-tutorial.md` @ `sha256:667ec67af72404f9ee9fca80005a1d0c11014895991ad04f6f3f301e367c05de` — §1.4, the L(H) problem for crude MDL

## Connections Found

For the occasion, this source serves as the **technical basis**. It is the KB's first primary MDL source. It states the distinction the occasion needs: Kolmogorov complexity uses a universal language and is uncomputable, while practical MDL uses a chosen, restricted description method whose minimum is computable by construction. It also says where choosing that description method remains arbitrary.

Within the theory collection it bears on three notes. It is evidence for [learning inside a fixed decomposition inherits its mistakes](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). A restricted code class C is a hypothesis class fixed in advance, so "there will always be some regular sequences which we will not be able to compress" (§1.2.2), and carving a hypothesis space into nested models is arbitrariness that every combined model/parameter selection method has to accept (§2.10.1). It is also evidence for [information value is observer-relative](../theory/information-value-is-observer-relative.md), but it qualifies that note. The note says classical information theory abstracts away the observer. The MDL branch of the Kolmogorov lineage makes regularity relative to a chosen description method, and noise relative to the current model (§1.5). Only the invariance theorem, for long sequences under universal machines, removes that dependence. Whether this qualifies the note's claim or only narrows its scope is a decision for the note's author. Finally, it compares with [epiplexity by example](../theory/epiplexity-by-example-what-entropy-and-complexity-miss.md) on how a measure fixes the observer. That note's table moves from Kolmogorov (a fixed universal machine) straight to epiplexity (a time-bounded learner). Practical MDL, with a restricted and computable code class, is the missing middle rung, and it is the rung the occasion asks about.

It also compares with [first-principles reasoning selects for explanatory-reach over adaptive fit](../theory/first-principles-reasoning-selects-for-explanatory-reach-over.md). MDL is the most disciplined formal version of selection by fit penalized by complexity. It is justified by prediction and consistency, and it explicitly declines to claim that the selected model is true. That gives the adaptive-fit pole of the note a well-specified form.

Among sources, it is the canonical statement of the baseline that [Bennett's weakness paper](./optimal-choice-of-hypothesis-is-the-weakest-not-the-shortest.ingest.md) argues against. Refined MDL's complexity is not plain syntactic length, so that comparison should name which MDL it means. It supplies the crude-versus-refined distinction behind [DreamCoder](./dreamcoder-wake-sleep-bayesian-program-learning.ingest.md)'s library-growth gate, which costs a library plus programs given the library. That is a two-part criterion whose L(H) code is chosen ad hoc. It answers part of the [08 simplicity ingest](./08-simplicity-hidden-in-complexity.ingest.md)'s representation-dependence critique: Grünwald concedes the critique for crude MDL and claims refined MDL avoids it only inside a restricted model class. It also supplies the two-part and prequential machinery that [epiplexity's time-bounded MDL](./from-entropy-to-epiplexity-rethinking-information-computational.ingest.md) adapts.

It sits beside [Popper's *Logic of Scientific Discovery*](./popper-logic-of-scientific-discovery.ingest.md) as a rival answer to what simplicity is. Popper identifies it with degree of falsifiability, tied to parameter dimension. Grünwald identifies it with the ability to fit random data, and shows that two models with equal parameter counts can differ in complexity (Example 1.4). It reads together with [No Free Lunch](./no-free-lunch-theorem-no-universal-learning-algorithm.ingest.md) on whether a simplicity preference can be justified without assumptions about the problem distribution. Grünwald's guarantees are consistency results that assume a true distribution lies in the model class.

## Learning Claims (our opinion)

**Mechanism on its own terms.** MDL learns by selecting, from a candidate set fixed in advance, the hypothesis or model that gives the shortest lossless code for the observed data. "Learning" is equated with finding regularity, and regularity with compressibility (§1.1, §1.3). The procedure is a single selection over fixed data. When the sample grows, the selected model can become more complex (Example 1.6), but nothing from an earlier selection is carried into the next one except the data.

**Mapping onto Commonplace concepts.** The code class C, or the model family, corresponds to the hypothesis-class part of a fixed decomposition. The source states plainly that improvement happens only within it (§1.2.2). It also admits that choosing it, including how to carve an infinite class into nested models, is not fixed by MDL (§2.10.1). Rissanen's "models as languages" view is close to Commonplace's view that what can be explained depends on the representational vocabulary. The mapping is partial: Rissanen uses "language" to mean a universal code over data, not a medium in which theories are stated.

**Theory-builder conditions.**
- *Localized content* is met for the hypotheses. Each is a formal, identifiable object, such as a polynomial or a Markov chain of stated order.
- *Consumption* is met in the ordinary sense: the selected model is used for prediction.
- *Criticism* is only partly met. Rivals are compared by a fixed scoring rule over fixed data. That is comparison with rivals, but the criterion cannot be criticized from inside the procedure, and a failure cannot be blamed on the code class or the data.
- *Iteration* is not met by the procedure itself.

Persistence: none within the method. Results persist only as the chosen model. The theory-builder loop lives one level up, in the research program. Grünwald's own history is an example: crude two-part codes were criticized for arbitrary L(H) and replaced by refined MDL, and misspecification failures are recorded as open problems (§1.7, §2.10.2). That loop is human scientific work, not an MDL mechanism.

**Learning judgment.** The evidence for improved future capacity is conditional. Consistency and good convergence rates hold when some distribution in the model class generates the data (§1.5, §2.10.1). Empirical failures are reported under misspecification (§2.10.2). So the source supports "MDL selects well inside a well-specified class". It does not support "compression-based selection improves predictions in general". It adds nothing about revising the decomposition itself.

## Extractable Value

1. **Practical MDL supplies a vocabulary-relative measure, but its computability condition does not cover "cheapest known".** For the occasion, the closest MDL quantity is the shortest description of the data attainable with a chosen description method C. Grünwald requires C to be restrictive enough that this minimum can always be computed (§1.2.2). The quantity is therefore defined relative to the vocabulary, and it differs from Kolmogorov complexity in two stated ways: it is computable, and it has no invariance theorem that makes the choice of language irrelevant. A "cheapest known" explanation found by search over an expressive vocabulary of units is a different quantity. It is an upper bound on the C-relative minimum, and it equals that minimum only when the search is exhaustive over C, which is the condition MDL's restriction is designed to secure. A KB note using MDL for this purpose should name which quantity it means. [quick-win]

2. **The explanation's length is not the measure: MDL scores the explanation plus the residual.** Two-part MDL minimizes L(H) + L(D|H). Refined MDL scores fit + COMP(M). In both, a cheap explanation that leaves much behavior unexplained pays for it in residual bits, which the MDL view calls noise relative to the model (§1.5). A measure of "cheapest explanation of an artifact's behavior" that counts only the explanation's units corresponds to L(H) alone, and it rewards under-explaining. The Kolmogorov structure-function variant (§2.9.4) is the source's account of separating a structure part from noise, if only the structural part is wanted. [quick-win]

3. **A vocabulary of units makes this crude MDL, with the arbitrariness that implies.** Costing explanations by counting units in a chosen vocabulary is an "intuitively reasonable" code for hypotheses. Grünwald says such codes make the procedure "in danger of becoming arbitrary", because the same hypothesis can be long under one code and short under another (§1.4, §2.4.2). Refined MDL removes this only for finite sets of parametric models with a defined NML distribution. Discrete, compositional vocabularies (grammars, programs, libraries) fall outside that case. Grünwald names context-free grammars only as an exotic application of MDL in the broad sense (§2.9.1). He says a "definite" MDL approach has not yet been formulated for tasks beyond parametric model selection (§2.8), and that some arbitrariness in carving the class remains unavoidable (§2.10.1). The prescription for such vocabularies is our inference, not his. Comparisons across vocabularies therefore inherit the code choice. Comparisons within one vocabulary are sound only relative to it. [deep-dive]

4. **Practical MDL is the middle rung between Kolmogorov and epiplexity.** It fixes the observer as a restricted, computable code class chosen with domain knowledge. Kolmogorov fixes a universal machine. Epiplexity fixes a time-bounded learner. Adding this rung to [epiplexity by example](../theory/epiplexity-by-example-what-entropy-and-complexity-miss.md) would let the KB say which kind of observer-relativity a vocabulary-relative measure has. [quick-win]

5. **Noise relative to the model qualifies the observer-relative note.** "These data are noisy" means only that the data are incompressible under the current model (§1.5). This is a classical-lineage instance of observer-relative structure, and it bears on the framing in [information value is observer-relative](../theory/information-value-is-observer-relative.md). [quick-win]

6. **Complexity is the ability to fit random data, not a parameter count.** Stevens' and Fechner's models both have two parameters, yet Stevens' fits more data patterns. It fit better in 67% of samples that Fechner's model generated (Example 1.4). This is a concrete reason why counting parameters or units can misstate flexibility. It is relevant to any simplicity comparison involving Popper or Bennett. [just-a-reference]

7. **A simplicity preference is a strategy, not a claim about the world.** "a strategy cannot be true or false, it is 'clever' or 'stupid'" (§1.6). Its justification is conditional on consistency results. This is a usable framing for the KB's own preference for sharp, high-content claims. That preference has a different justification, Popperian content. [just-a-reference]

## Limitations (our opinion)

This is an advocate's tutorial. Its practical-performance claims ("in many cases, the methods described here perform very well") rest on cited studies that the tutorial does not reproduce, and this ingest did not check them. The theoretical guarantees it emphasizes, consistency and minimax-optimal rates, hold when a true distribution lies in the model class. That is exactly the assumption the MDL philosophy says it does not need, and Grünwald concedes that MDL can fail when the assumption is violated (§2.10.2). So the philosophy's independence from truth assumptions is better supported for MDL's interpretation than for its performance.

The non-arbitrariness claim for refined MDL is narrow. It covers finite sets of parametric models with finite parametric complexity and a defined NML distribution. Beyond those, the tutorial offers "extensions in the same spirit" and explicitly incomplete treatments of prediction, classification and non-parametric settings (§2.7, §2.8). It says loss-based MDL for classification without probabilistic assumptions is "still in their infancy". So the tutorial gives no settled MDL measure for deterministic artifacts described in discrete, compositional vocabularies, which is the case nearest the occasion. Applying MDL there means using crude two-part codes with a chosen code for units, along with the arbitrariness the source warns about.

The framework measures descriptions of data, meaning observed outcomes, not artifacts as such. Using it for "an artifact's behavior" first requires deciding which observations count as the data and what precision they are recorded at. The tutorial does not address that representation step. Its examples use fixed numeric or binary samples. Finally, this is a 2004 snapshot. It predates later work by Grünwald and others on misspecification, so its account of open problems may be out of date.

## Recommended Next Action

Write a theory note titled "Description length over a chosen vocabulary is MDL's crude two-part code, not Kolmogorov complexity". It should use this ingest to state three things. First, the C-relative shortest description is computable when C is restricted, and a search-found "cheapest known" explanation is only an upper bound on it. Second, the measure must include residual unexplained behavior, L(D|H), as well as explanation length, L(H). Third, the code for units carries crude MDL's arbitrariness unless a refined construction is available. The note should place this quantity as the middle rung in [epiplexity by example](../theory/epiplexity-by-example-what-entropy-and-complexity-miss.md).

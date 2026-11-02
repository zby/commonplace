---
description: "Barak et al. prove virtual-black-box obfuscation impossible via contrived unobfuscatable circuit families, define indistinguishability obfuscation; bounds claims that code is opaque or readable by form"
source: https://www.boazbarak.org/Papers/obfuscate.pdf
captured: "2026-11-01"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 5d3d6d902b0c89e5f07469cbaf87d427cb7169dd452d038aec24ab88cf309f43
ingested: "2026-11-01"
occasion: "What does the virtual black-box impossibility result establish, for which function families, how is indistinguishability obfuscation defined, and what does the paper say about reading versus running a program? What scope limits must accompany its use as evidence about opacity of symbolic form? The source is the author-hosted copy; the ePrint 2001/069 PDF returned 403 at capture. The work appeared at CRYPTO 2001 and in JACM 2012."
type: types/ingest-report.md
domains: [program-obfuscation, virtual-black-box, indistinguishability-obfuscation, rice-theorem]
tags: [artifact-analysis]
---

# Ingest: On the (Im)possibility of Obfuscating Programs

## Classification

A theoretical cryptography and complexity paper: definitions, theorems and
proofs, with no experiments. The captured copy is the author-hosted full
version dated July 18, 2010. It states that a preliminary version appeared at
CRYPTO '01 and thanks the J.ACM reviewers. The caller records the journal
version as JACM 2012 and the IACR ePrint copy as
[eprint.iacr.org/2001/069](https://eprint.iacr.org/2001/069.pdf); that copy
returned 403 at capture time, so this ingest analyses the author-hosted copy
only.
Author: Boaz Barak, Oded Goldreich, Russell Impagliazzo, Steven Rudich, Amit
Sahai, Salil Vadhan and Ke Yang, a group of leading theoretical
cryptographers. The paper is the standard foundational reference for the
theory of program obfuscation.

## Summary

The paper formalizes an obfuscator as an efficient compiler whose output
computes the same function as the input program, is at most polynomially
larger, and satisfies the "virtual black box" (VBB) property: anything an
efficient adversary can compute from the obfuscated program it could also
compute from oracle (input-output) access to the original. It takes the
weakest version of that property, hiding a single predicate (Definitions 2.1
and 2.2), and proves it unachievable. Assuming one-way functions, it
constructs an unobfuscatable circuit ensemble (Definition 3.1, Theorem 3.11):
from any circuit computing the same function, the original "source code" can
be reconstructed efficiently, yet with oracle access alone a hidden string
stays pseudorandom. Efficient circuit obfuscators therefore do not exist
unconditionally (Corollary 3.10). The result holds even when the obfuscator
has unbounded running time, needs to hide only one fixed bit from one fixed
adversary, or only approximately preserves functionality (Theorem 4.3). Under
a factoring assumption the counterexample family lies in TC0
(Theorem 4.12). The authors attribute the impossibility to "a fundamental
difference between getting black-box access to a function and getting a
program that computes it". In their words, "a program is a succinct
description of the function, on which one can perform computations". The
difference vanishes exactly for function classes that are learnable from
queries. The same construction refutes a promise-problem version of a
"scaled-down Rice's theorem" (Conjecture 5.2, Theorem 5.3). That conjecture
would have formalized the intuition, which the introduction calls "highly
speculative", that the only useful thing to do with a program is to run it.
The plain conjecture (5.1) stays open. Section 7 proposes weaker notions that
escape the impossibility proof. The main one is indistinguishability
obfuscation (Definition 7.1): for any two same-size circuits computing the
same function, no efficient adversary can distinguish their obfuscations. An
inefficient one exists trivially by outputting the lexicographically first
equivalent circuit (Proposition 7.2), and an efficient one is "as good" as any
obfuscator (Proposition 7.3). The paper does not construct an efficient one.

## Contribution assessment (our opinion)

The problem is foundational: obfuscation would yield software protection,
public-key encryption from private-key encryption, and homomorphic
encryption. Before this paper, the field had only heuristics and informal
intuitions. The paper's main contribution is a sharp refutation. It states the
weakest reasonable form of the folk conjecture, a hiding-one-predicate VBB, and
gives a counterexample robust to every natural relaxation the authors try. It
also isolates the mechanism: code is a succinct description that can be run on
itself or on other code, which oracle access cannot match. The
counterexamples are explicitly contrived, so the result does not show that
any particular useful program cannot be obfuscated. Our background knowledge,
not the capture, says the iO definition introduced almost in passing in
Section 7 later became central once candidate efficient constructions
appeared, from 2013 onward. If so, the paper's lasting significance is double:
it closed the VBB paradigm in general and named the notion that replaced it.
This is a tentative judgment about later history; the paper itself
demonstrates only the negative result and the definitions.

## Quotes

> Definition 2.2 (circuit obfuscator) A probabilistic algorithm O is a (circuit) obfuscator for the
> collection F of circuits if the following three conditions hold:
> • (functionality) For every circuit C ∈ F, the string O(C) describes a circuit that computes the
> same function as C.
> • (polynomial slowdown) There is a polynomial p such that for every circuit C ∈ F, we have
> that |O(C)| ≤ p(|C|).
> • (“virtual black box” property) For any PPT A, there is a PPT S and a negligible function α
> such that for all circuits C ∈ F
> h
> i
> Pr [A(O(C)) = 1] − Pr S C (1|C| ) = 1 ≤ α(|C|).
> We say that O is efficient if it runs in polynomial time.
> --- `kb/sources/.snapshots/on-the-impossibility-of-obfuscating-programs.md` @ `sha256:5d3d6d902b0c89e5f07469cbaf87d427cb7169dd452d038aec24ab88cf309f43` — Definition 2.2, virtual black-box obfuscation (pdftotext dropped the inequality brackets)

> Definition 3.1 An unobfuscatable circuit ensemble6 is an ensemble {Hk }k∈N of distributions Hk
> on circuits (from, say, {0, 1}lin (k) to {0, 1}lout (k) ) satisfying:
> --- `kb/sources/.snapshots/on-the-impossibility-of-obfuscating-programs.md` @ `sha256:5d3d6d902b0c89e5f07469cbaf87d427cb7169dd452d038aec24ab88cf309f43` — Definition 3.1, opening

> • (efficient computability) Every circuit C ∈ Supp(Hk ) is of size poly(k). Moreover, C ← Hk
> can be sampled uniformly in time poly(k).
> --- `kb/sources/.snapshots/on-the-impossibility-of-obfuscating-programs.md` @ `sha256:5d3d6d902b0c89e5f07469cbaf87d427cb7169dd452d038aec24ab88cf309f43` — Definition 3.1, efficient computability

> • (reverse-engineerability) C is easy to reconstruct givenSany equivalent circuit: There exists a
> polynomial-time algorithm A such that for every C ∈ k Supp(Hk ) and every circuit C 0 that
> computes the same function as C it holds that A(C 0 ) = C.
> The reverse-engineerability condition says that the source code C can be completely reverseengineered given any program computing the same function. On the other hand the unlearnability
> condition implies that it is infeasible to reverse-engineer the source code given only black-box access
> to C. We note that for the purpose of the main impossibility result, it would have sufficed for the
> function π to have a single bit output. (We will make use of the longer pseudorandom output of π
> in later results.) Putting the two items together, it follows that, when given only black-box access
> to C, it is hard to find any circuit computing the same function as C. In the language of learning
> theory (see [KV]), this says that an unobfuscatable circuit ensemble constitutes a concept class
> that is hard to exactly learn with queries. Indeed, any concept class that can be exactly learned
> with queries is trivially obfuscatable (according to even the strongest definitions of obfuscation),
> because we can view the output of the learning algorithm when given oracle access to a function
> C in the class as an obfuscation of C.
> --- `kb/sources/.snapshots/on-the-impossibility-of-obfuscating-programs.md` @ `sha256:5d3d6d902b0c89e5f07469cbaf87d427cb7169dd452d038aec24ab88cf309f43` — Definition 3.1, reverse-engineerability, with the authors' gloss on both conditions and query learnability

> Theorem 3.11 (unobfuscatable programs) If one-way functions exist, then there exists an unobfuscatable circuit ensemble.
> --- `kb/sources/.snapshots/on-the-impossibility-of-obfuscating-programs.md` @ `sha256:5d3d6d902b0c89e5f07469cbaf87d427cb7169dd452d038aec24ab88cf309f43` — Theorem 3.11

> We prove in Theorem 3.11 that, assuming one-way functions exist, there exists an unobfuscatable circuit ensemble. This implies that, under the same assumption, there is no obfuscator
> that satisfies Definition 2.2 (actually we prove the latter fact directly in Theorem 3.8).
> --- `kb/sources/.snapshots/on-the-impossibility-of-obfuscating-programs.md` @ `sha256:5d3d6d902b0c89e5f07469cbaf87d427cb7169dd452d038aec24ab88cf309f43` — consequence for Definition 2.2

> Corollary 3.10 Efficient circuit obfuscators do not exist (unconditionally).
> --- `kb/sources/.snapshots/on-the-impossibility-of-obfuscating-programs.md` @ `sha256:5d3d6d902b0c89e5f07469cbaf87d427cb7169dd452d038aec24ab88cf309f43` — Corollary 3.10

> The essence of this proof, and in fact of all
> the impossibility proofs in this paper, is that there is a fundamental difference between getting
> black-box access to a function and getting a program that computes it, no matter how obfuscated:
> A program is a succinct description of the function, on which one can perform computations (or
> run other programs). Of course, if the function is (exactly) learnable via oracle queries (i.e., one
> can acquire a program that computes the function by querying it at a few locations), then this
> difference disappears.
> --- `kb/sources/.snapshots/on-the-impossibility-of-obfuscating-programs.md` @ `sha256:5d3d6d902b0c89e5f07469cbaf87d427cb7169dd452d038aec24ab88cf309f43` — proof of Proposition 3.4, stated as the essence of all the impossibility proofs

> The hope that some form of obfuscation is possible arises from the fact that analyzing programs
> expressed in rich enough formalisms is hard. Indeed, any programmer knows that total unintelligibility is the natural state of computer programs (and one must work hard in order to keep a
> program from deteriorating into this state). Theoretically, results such as Rice’s Theorem and the
> hardness of the Halting Problem and Satisfiability all seem to imply that the only useful
> thing that one can do with a program or circuit is to run it (on inputs of one’s choice). However,
> this informal statement is, of course, highly speculative, and the existence of obfuscators requires
> its own investigation.
> --- `kb/sources/.snapshots/on-the-impossibility-of-obfuscating-programs.md` @ `sha256:5d3d6d902b0c89e5f07469cbaf87d427cb7169dd452d038aec24ab88cf309f43` — Section 1, introduction

> simulator, which we use to formalize the interpretation of Rice’s Theorem as “the only useful thing
> you can do with a machine is run it.”
> --- `kb/sources/.snapshots/on-the-impossibility-of-obfuscating-programs.md` @ `sha256:5d3d6d902b0c89e5f07469cbaf87d427cb7169dd452d038aec24ab88cf309f43` — Appendix A, Rice's Theorem generalizations

> Definition 7.1 (indistinguishability obfuscator) An indistinguishability obfuscator is defined
> in the same way as a circuit obfuscator, except that the “virtual black box” property is replaced with
> the following:
> • (indistinguishability) For any PPT A, there is a negligible function α such that for any two
> circuits C1 , C2 that compute the same function and are of the same size k,
> |Pr [A(O(C1 ))] − Pr [A(O(C2 ))]| ≤ α(k).
> Some (very slight) hope that this definition is achievable comes from the following observation.
> Proposition 7.2 (Inefficient) indistinguishability obfuscators exist.
> --- `kb/sources/.snapshots/on-the-impossibility-of-obfuscating-programs.md` @ `sha256:5d3d6d902b0c89e5f07469cbaf87d427cb7169dd452d038aec24ab88cf309f43` — Definition 7.1 and Proposition 7.2

> Let O(C) be the lexicographically first circuit of size |C| that computes the same function
> --- `kb/sources/.snapshots/on-the-impossibility-of-obfuscating-programs.md` @ `sha256:5d3d6d902b0c89e5f07469cbaf87d427cb7169dd452d038aec24ab88cf309f43` — proof of Proposition 7.2 (pdftotext split the sentence; it ends "as C.")

> As is usually the case with impossibility results and lower bounds, we show that obfuscators
> (in the “virtual black box” sense) do not exist by presenting a somewhat contrived counterexample
> of a function ensemble that cannot be obfuscated. It is interesting whether obfuscation is possible
> for a restricted class of algorithms, which nonetheless contains some “useful” algorithms. This
> restriction should not be confined to the computational complexity of the algorithms: if we try to
> restrict the algorithms by their computational complexity, then there’s not much hope for obfuscation. Indeed, as mentioned above, we show that (under widely believed complexity assumptions)
> our counterexample can be placed in TC0 . In general, the complexity of our counterexample is
> essentially the same as the complexity of pseudorandom functions, and so a complexity class that
> does not contain our example will also not contain many cryptographically useful algorithms.
> --- `kb/sources/.snapshots/on-the-impossibility-of-obfuscating-programs.md` @ `sha256:5d3d6d902b0c89e5f07469cbaf87d427cb7169dd452d038aec24ab88cf309f43` — Section 1.3, Discussion

## Connections Found

The source's role in this KB is a formal counterpoint to an account of
opacity in the theory layer. [Opacity is a scale
threshold](../theory/opacity-is-a-scale-threshold.md), the opacity misuse case
and inspection rule in [representational
form](../theory/definitions/representational-form.md), and the "inherently
inspectable at useful scales" claim in [inspectable artifact, not supervision,
defeats the blackbox
problem](../theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md)
together treat opacity as a scale effect. On that account, symbolic code is
readable by default. The paper bears on this account in two opposite
directions, and a transfer must keep both:

- Against "readable by default": the paper treats making a program
  unintelligible while preserving its function as a coherent goal. It
  defines what success would mean (VBB, and the weaker iO) independently of
  program size. The introduction also states that total unintelligibility is
  the natural state of programs unless someone works to prevent it.
  Unintelligibility is therefore a property of a particular program, not of
  its form. This is a qualification of the scale account, not support for it.
- Against "opaque by construction" in its strong sense: VBB impossibility
  shows that for some function families, any program computing the function
  reveals its source. Reading can therefore strictly exceed running. A
  deliberately obscured symbolic artifact cannot in general be made as
  uninformative as black-box probing. The paper establishes this for
  contrived cryptographic families. Whether the gap matters for ordinary code
  it leaves open.

The paper defines iO and proves only an inefficient instance. That instance
canonicalizes rather than scrambles: it outputs the lexicographically first
equivalent circuit. Efficient constructions are outside this source. The
paper therefore supports "deliberate obfuscation is a definable, non-scale
source of opacity". It does not support "efficient opacity-by-construction is
achievable".

The paper also gives a cryptographic formalization of [information value is
observer-relative](../theory/information-value-is-observer-relative.md) for
computational capacity. An obfuscated program contains all of the original's
information, yet the VBB ideal asks that a polynomial-time observer extract no
more than from queries. It compares with [statecharts and programs differ in
what they show, not in what they can
compute](../theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md)
on one axis: function-equivalent representations differ in what a reader can
recover. Obfuscation is the limiting case where an equivalence-preserving
transformation is chosen to show as little as possible.

All transfers from the paper are by analogy across one gap. The paper's
"reader" is a probabilistic polynomial-time adversary with negligible-advantage
criteria. A transfer to an agent or human reading code must name which part
carries over.

## Extractable Value

1. **VBB impossibility as a bound on the opaque modifier** -- for the
   unobfuscatable ensembles of Definition 3.1 (constructed from any one-way
   function, in TC0 under factoring), every functionally equivalent program
   leaks the source. Opacity-by-construction therefore cannot in general match
   oracle-only access. The scope is existential and contrived: it rules out a
   general-purpose obfuscator, not obfuscation of specific useful programs.
   This scope must travel with any use of the result. [quick-win]
2. **Indistinguishability obfuscation as the achievable-notion candidate** --
   Definition 7.1 hides which of several equivalent same-size implementations
   was used, not what the function is. The trivial inefficient iO is
   canonicalization. This gives the opaque modifier a precise weak sense: the
   artifact shows the function but not the authoring choices. It also
   separates that sense from VBB-style hiding of the function itself. The
   paper does not establish efficient existence. [quick-win]
3. **Reading versus running, stated precisely** -- the paper rejects the
   informal Rice-style slogan "the only useful thing to do with a program is
   run it" for a promise-problem version (Theorem 5.3). It locates the gap in
   code being a succinct description that can be computed on. The gap closes
   exactly when the function class is learnable from queries. This sharpens
   the representational-form inspection rule. Reading code can beat testing
   it only for function classes not learnable from queries, and the paper
   shows the advantage is real for some of those classes. It does not show the
   advantage holds for every unlearnable class. [experiment]
4. **Opacity has a non-scale source** -- deliberate, function-preserving
   transformation is a source of practical unreadability independent of size.
   This is evidence for revising the universal reading of the opacity note's
   title and the matching misuse case in representational form. The paper
   defines the goal; it does not show the goal is efficiently met. Heuristic
   obfuscation, such as the paper's IOCCC figure, is the practical evidence
   that it is often met against human readers. [deep-dive]
5. **Observer-bounded extraction as a formal model** -- the simulator-based
   VBB definition is a reusable template for saying "this artifact yields an
   observer no more than that access path", with the observer's resources
   explicit. It could formalize comparisons between consumption paths, such
   as reading versus probing, in KB theory. [just-a-reference]

## Limitations (our opinion)

The impossibility is existential: it exhibits contrived function families
built from cryptographic primitives. The authors call it "a somewhat contrived
counterexample". It says nothing about whether a particular useful program can
be obfuscated, and the paper names restricted or syntactically defined classes
as open. Every result is asymptotic and stated against probabilistic
polynomial-time adversaries with negligible advantage. "Readable", "opaque"
and "can reconstruct" therefore have meanings that do not map directly onto an
agent or human reading a finite program. Many results assume one-way
functions; Corollary 3.10 is unconditional only for efficient obfuscators. The
scaled-down Rice conjecture itself (5.1) remains open, and Appendix A reports
the computability-side intuition as inconclusive. The paper therefore does not
settle whether every semantic property decidable from code is decidable from
queries, outside the promise setting. On the positive side, the paper defines
iO and proves only an inefficient instance. Any claim that obfuscated code is
efficiently and provably opaque rests on later work outside this capture. This
ingest also analyses the 2010 author-hosted full version. It has not compared
that copy against the ePrint or the JACM text.

## Recommended Next Action

Revise [Opacity is a scale threshold, not a class
property](../theory/opacity-is-a-scale-threshold.md) to recognize deliberate
obfuscation as a non-scale source of opacity while preserving the VBB
impossibility limit: reading can exceed probing for some contrived function
families. Distinguish the inefficient iO instance here from the conditional
efficient construction in the [Jain–Lin–Sahai
ingest](./indistinguishability-obfuscation-well-founded-assumptions.ingest.md).

---

Relevant Notes:

- [On the (Im)possibility of Obfuscating Programs](https://www.boazbarak.org/Papers/obfuscate.pdf) — derived-from: author-hosted full version analysed here
- [Opacity is a scale threshold, not a class property](../theory/opacity-is-a-scale-threshold.md) — is-evidence-for: deliberate obfuscation is a definable non-scale source of opacity, qualifying the scale-only reading
- [Representational form](../theory/definitions/representational-form.md) — is-evidence-for: qualifies the symbolic inspection rule and the opacity misuse case; reading can exceed probing for some families
- [Inspectable artifact, not supervision, defeats the blackbox problem](../theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — is-evidence-for: code's inspectability is a property of the particular artifact, not guaranteed by its form
- [Information value is observer-relative](../theory/information-value-is-observer-relative.md) — is-evidence-for: VBB formalizes extraction bounded by the observer's computational resources
- [Statecharts and programs differ in what they show, not in what they can compute](../theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md) — compares-with: function-equivalent representations differ in what a reader can recover
- [Indistinguishability Obfuscation from Well-Founded Assumptions](./indistinguishability-obfuscation-well-founded-assumptions.ingest.md) — compares-with: an efficient construction of the notion Section 7 defines, under four standard assumptions

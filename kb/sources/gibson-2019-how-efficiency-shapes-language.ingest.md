---
description: "Gibson et al. 2019 review: efficiency and learnability shape language; dependency locality grounds keep-related-words-close writing rules for human readers, with LLM transfer untested"
source: https://socsci.uci.edu/~rfutrell/papers/gibson2019efficiency.pdf
captured: "2026-10-26"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 9eba04eaf9629542e7d65017ba39d7932a0ec7329f2f3ddfc376af9f4be02641
ingested: "2026-10-26"
occasion: "Commonplace is considering adding dependency-length-minimization guidance to its writing instructions for natural-language output (KB notes, instructions, operator messages) that is read by humans inside and outside the project and also by LLM agents. What does this source establish about the relation between syntactic dependency distance and processing cost, what operational word-ordering rules for writers does it support, and what are the limits of its evidence?"
type: types/ingest-report.md
domains: [writing-style, information-theory, psycholinguistics, context-engineering]
learning_claims: true
---

# Ingest: How Efficiency Shapes Human Language

## Classification

This is a scientific review article, not a primary study. It synthesizes
corpus analyses, behavioral experiments, artificial-language learning studies
and computational models under one information-theoretic framework, and it
reports no new data. One figure presents a replication of an earlier corpus
result on 50 languages without methods detail. The capture is the authors'
manuscript PDF. From background knowledge, the published version appeared in
*Trends in Cognitive Sciences* in 2019; the snapshot does not state the venue.

Author: Edward Gibson, Richard Futrell, Steven T. Piantadosi, Isabelle
Dautriche, Kyle Mahowald, Leon Bergen and Roger Levy (MIT, UC Irvine, UC
Berkeley, Edinburgh, UC San Diego). Gibson, Futrell and Levy authored much of
the cited dependency-locality and information-locality work, so the review
summarizes the authors' own research program as well as others'.

## Summary

The review argues that pressure for communicative efficiency, balanced against
learnability and complexity, explains recurring properties of human languages
from the lexicon to syntax. Efficiency means successful transmission with
minimal average sender and receiver effort, usually measured as message
length. Ambiguity out of context is presented as efficient, because context
usually resolves it and conversation partners can cheaply ask for
clarification. Word length tracks predictability in context more closely than
raw frequency. Kinship and color vocabularies sit near an
informativeness–complexity tradeoff. For syntax, *dependency length* is the
linear distance in words between two words linked by a syntactic dependency.
*Dependency locality* is the claim that this distance should be as short as
possible, because each long dependency costs a working-memory retrieval
during incremental comprehension and production. The review cites
comprehension experiments for measurable difficulty and corpus studies
showing that real sentences in 37 (replicated: 50) languages have shorter
dependencies than random reorderings. That corpus evidence shows a
population-level tendency against chosen random baselines, not processing cost
directly. *Information locality* generalizes the principle: under noisy
memory, any two words with high mutual information should sit close.
Dependency locality is the special case where those words are a syntactic
head and its dependent. Word order and morphology are alternative encodings of
the same dependency tree and trade off. Compositionality may arise from the
cultural-transmission bottleneck. The closing challenges concede that
counterfactual baselines are often the hardest part of an efficiency claim and
that information theory idealizes communication.

## Contribution assessment (our opinion)

The problem is central to cognitive science: whether language universals have
a functional explanation, as opposed to an innate-grammar one. The review's
contribution is integrative. It places word length, lexical partitions, word
order, morphology and compositionality under one source-coding and
channel-coding vocabulary. It turns Chomsky's ambiguity objection into a
prediction of the framework. It states the framework's open problems
candidly: complexity metrics, null hypotheses, estimation from data and
non-informational utility. It adds no new test. Its strength depends on the
cited primary studies, which the review summarizes without effect sizes. My
tentative judgment is that the framework is progressive in the Popperian
sense. Its claims are falsifiable against explicit counterfactual baselines,
and the dependency-locality strand has survived large cross-linguistic
corpus tests. Several other strands are flagged by the authors as
speculative, such as gender as useful redundancy and the usefulness account of
color terms. From background knowledge the review is widely cited, but that
does not establish the priority of its individual ideas, most of which
originate in the cited work.

## Quotes

> Under the assumption that comprehenders’ memory for linguistic context is noisy, a
> principle of information locality can be derived, such that all words with high
> mutual information should be close for processing efficiency, where mutual
> information is a measure of how strongly the distribution of two words is constrained
> [107]. Under this hypothesis, linguistic heads and dependents are word pairs that have
> especially high mutual information, meaning that dependency locality becomes a special
> case of information locality. Information locality extends the theoretical reach of
> dependency locality from strictly syntactic dependencies to all statistical dependencies.
> Information locality might thus potentially explain word order phenomena that go
> beyond traditional dependency locality, such as preferences in the relative order of
> adjectives [108, 109].
> --- `kb/sources/.snapshots/gibson-2019-how-efficiency-shapes-language.md` @ `sha256:9eba04eaf9629542e7d65017ba39d7932a0ec7329f2f3ddfc376af9f4be02641` — Syntax section, information locality

> To show that an aspect of language is
> efficient in terms of communication and learnability, it is often necessary to contrast the
> observed language data with some counterfactual baseline indicating what a language
> might look like without a pressure for efficiency.
> --- `kb/sources/.snapshots/gibson-2019-how-efficiency-shapes-language.md` @ `sha256:9eba04eaf9629542e7d65017ba39d7932a0ec7329f2f3ddfc376af9f4be02641` — Specification of null hypotheses

> Specification of these counterfactual baselines is often the most
> challenging part of making an efficiency claim.
> --- `kb/sources/.snapshots/gibson-2019-how-efficiency-shapes-language.md` @ `sha256:9eba04eaf9629542e7d65017ba39d7932a0ec7329f2f3ddfc376af9f4be02641` — Specification of null hypotheses

## Connections Found

For this occasion, the source's role is the review-level technical basis for
locality as a reading-cost mechanism. The KB has no prior treatment of
dependency or information locality. Its closest artifact is
[Two rewrites exposed a syntax-or-repetition tradeoff](../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md).
That note records a simplification pass that "moved a temporal qualifier away
from the definition it limited". In this source's terms, the pass lengthened a
dependency. Its finding that restating relations added 4.9% more words matches
the source's statement that dependency length is an effort component
separate from utterance length. Locality and length can trade against each
other.

Beyond the occasion, the source explains why ambiguity persists in natural
language. This bears on
[Agentic systems interpret underspecified instructions](../theory/agentic-systems-interpret-underspecified-instructions.md)
and on
[Legal drafting solves the same problem as context engineering](../theory/legal-drafting-solves-the-same-problem-as-context-engineering.md),
whose premise matches the source's example of legal contracts and programming
languages becoming wordy when they pursue zero ambiguity. The efficiency
argument assumes cheap clarification. That assumption names the condition that
fails in
[Silent disambiguation is the semantic analogue of tool fallback](../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md):
an executing agent often has no repair channel. The rule "omit what context
supplies" parallels
[An author should fix what the executor can't determine, not what it will](../theory/fix-what-the-executor-cant-determine-not-what-it-will.md).
The source grounds the rule in source coding over shared context. The note
grounds it in what the executor can and cannot determine. The admission that
information theory idealizes communication and must be constrained by the
processor's limits supports
[Information value is observer-relative](../theory/information-value-is-observer-relative.md).
The transmission-bottleneck account of compositionality is a hedged candidate
for the mechanism gap that
[Natural-language meaning is coordination among learned approximations](../theory/natural-language-meaning-is-coordination-among-learned-approximations.md)
leaves open. The source offers it beside an innate-bias alternative, and it
does not answer the systematicity condition in
[Fodor and Pylyshyn](./fodor-pylyshyn-1988-connectionism-cognitive-architecture.ingest.md).
The source's account of counterfactual baselines is an observational instance
of
[An experiment identifies only the contrast it actually runs](../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md).

## Learning Claims (our opinion)

The source's adaptation mechanism has two parts. First, languages change over
generations, and learners favor simpler, more learnable systems. Second, a
cultural-transmission bottleneck means that each learner sees only a sparse
sample. That sparsity selects for compositional and systematic form–meaning
mappings, because a non-compositional system "could not survive over
generations". Supporting evidence named in the review comes from
iterated-learning laboratory experiments, in which arbitrary signals become
systematic, and from artificial-language learning, in which a
dependency-locality bias and a morphology–word-order tradeoff emerge. The
review treats the cultural-selection account as one possibility beside an
innate inductive bias. It does not claim to have discriminated between them.

Mapped onto Commonplace concepts, the language-change process is not a
[theory builder](../theory/definitions/theory-builder.md), judged condition by
condition:

- **Localized content.** Partly met. Words and constructions are identifiable
  units, but they are forms in a code, not stated theories about the world.
- **Consumption.** Met in a weak sense. Speakers use the code in every
  utterance.
- **Criticism.** Not met. Selection works on learnability and usage outcomes,
  with no stated reason aimed at what a unit says. This is the trial-and-error
  side of the theory-builder boundary, comparable to black-box selection.
- **Iteration.** Met. Each generation's output becomes the next generation's
  input.

Persistence is high, spanning centuries, but persistence is not a condition.
The research program that the review describes, on the other hand, fits the
community case of a theory builder. It states conjectures, tests them against
counterfactual baselines and records open problems.

Whether languages learn, in the sense of improving capacity for future
communication, is not established by this source. The corpus results show that
present languages are more efficient than chosen baselines. They do not trace
an improvement history or isolate the transmission bottleneck as its cause.
In the terms of
[Learning inside a fixed decomposition inherits its mistakes](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md),
learners' working memory and inductive biases are fixed outside the update
space of cultural change. Cultural change can optimize word order within
them, but it cannot revise them. This interpretation is ours. Its consequence
for the occasion is that dependency locality reflects the constraints of
human processors. Whether a language model reader shares the constraint is a
separate question.

## Extractable Value

1. **What the source establishes about dependency distance and processing
   cost.** The causal claim is that long dependencies cost working-memory
   retrievals in incremental comprehension and production. The review asserts
   this and supports it by citing comprehension experiments (refs. 91, 92)
   without effect sizes. The stronger evidence is indirect: corpus studies
   show that dependency lengths across dozens of languages fall below random
   baselines that respect other word-order constraints, and learners show the
   bias in artificial-language experiments. For Commonplace guidance, this
   licenses "long dependencies raise human reading cost" as a
   well-supported psycholinguistic claim at review grain. It does not license
   a quantified cost or an optimal ordering. [quick-win]
2. **Operational ordering rules the source supports for English prose read by
   humans.** Keep a head and its dependents adjacent, for example a verb with
   its particle or object and a noun with its modifier. The source's example
   is the awkwardness of separating "threw" from "out". In English, place
   short constituents before long ones, so that the heavy phrase comes last.
   The source notes that head-final languages such as Japanese prefer the
   reverse, so this rule is English-specific rather than universal. Avoid
   crossing dependencies; the source says locality only "possibly" explains
   their rarity. The rules are well grounded as tendencies of fluent
   production. Their benefit as deliberate editing rules for technical prose
   is an inference the source does not test. [quick-win]
3. **Information locality grounds "keep necessary conditions next to their
   claims".** By generalizing locality from syntactic links to any
   high-mutual-information pair, the source supplies a mechanism for the
   AGENTS.md writing rule. It also explains the qualifier-displacement failure
   in the two-rewrites evidence note. The source presents information locality
   as derived under a noisy-memory assumption and as a hypothesis that
   "might" explain phenomena beyond syntax. A KB theory note should keep that
   status. [experiment]
4. **Locality and length are separate costs.** The source treats dependency
   length as effort "beyond utterance length". Together with the 4.9% word
   increase in the two-rewrites note, this means a locality rule needs a
   stated tie-break against brevity. Splitting a sentence to shorten
   dependencies can add words and restated relations. Guidance that
   minimizes only one cost is likely to degrade the other. [experiment]
5. **Efficiency claims need a counterfactual baseline.** The authors say that
   specifying baselines is "often the most challenging part" of an efficiency
   claim, and that no general method exists for generating the alternative
   utterances a speaker could have produced. Any Commonplace evaluation of
   locality guidance must therefore name its comparison: original prose
   versus rewrite, measured by a stated reader task. [quick-win]
6. **Out-of-context ambiguity is efficient only with shared context and cheap
   repair.** This explains why natural-language specifications keep residual
   ambiguity. It also names the assumption that agent handoffs break: the
   receiver often cannot ask for clarification. The bound matters for operator
   messages and instructions read by agents. [deep-dive]
7. **Word order and morphology as redundant encodings of one dependency
   tree.** Redundant marking acts like parity bits, making the signal robust
   to noise. For writers, explicit relation markers such as "which limits X"
   can substitute for adjacency when adjacency is impossible. This transfer
   is ours. [just-a-reference]
8. **Compositionality from a transmission bottleneck.** This is a candidate
   mechanism for the meaning note's open gap, hedged as one of two
   possibilities. [just-a-reference]

## Limitations (our opinion)

- **A review, not a test.** Every processing-cost claim is relayed from cited
  studies. The review gives no effect sizes, no reading-time magnitudes and no
  account of when locality effects fail to appear. One cited title, Bartek et
  al., "In search of on-line locality effects", suggests that the online
  evidence is more mixed than the summary sentence implies. The ingest cannot
  check this without the primary studies.
- **Corpus minimization is not reader benefit.** The strongest evidence shows
  that producers' sentences are shorter in dependency length than random
  reorderings. That is consistent with a processing pressure. It is also
  compatible with production-side planning ease or grammatical conventions
  shaped by other forces. It does not show that a reader of edited technical
  prose comprehends faster or more accurately after dependencies are
  shortened.
- **Human-processor mechanism.** The mechanism is working-memory retrieval
  and noisy memory of context in humans. A transformer reader attends to all
  prior tokens without decaying memory, so the mechanism does not transfer by
  identity. A degradation with distance in long contexts may exist for other
  reasons, but this source offers no evidence for language models. Per
  [Human writing structures transfer to LLMs because failure modes overlap](../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md),
  the LLM half of the occasion needs a shown shared failure mode, not this
  analogy.
- **Units and grain.** Dependency length is counted in words within single
  sentences. The source says nothing about distance across sentences or
  paragraphs, about tokens, or about document structure such as headings and
  lists. Extending "keep related things close" to a document level goes
  beyond its evidence. Information locality reaches beyond syntax but is
  explicitly hypothetical there.
- **Language-specific direction.** Short-before-long is reported for English
  and reversed for Japanese. Rules derived from it apply to English-language
  KB output only.
- **Idealization conceded.** The authors state that information theory
  "assumes an idealized version of communication" and that complexity and
  utility metrics are not settled. Efficiency arguments in the other strands,
  such as gender as redundancy and color usefulness, are flagged by the
  authors themselves as speculative or partial.
- **Minor exposition error.** The dependency-syntax example describes the
  link between "red" and "car" with head and dependent reversed. This does
  not affect the argument, but it shows that the illustrative passages need
  checking before reuse.

## Recommended Next Action

Write a `kb/theory/` note claiming that locality of related words lowers
reading cost for human readers. Ground it in this ingest and in
[Two rewrites exposed a syntax-or-repetition tradeoff](../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md).
State the three supported rules: head–dependent adjacency, short-before-long
in English, and conditions adjacent to the claims they limit. State the
length–locality tie-break. Leave transfer to LLM readers as an explicit open
question under the per-convention test. Gate any change to the writing
instructions on that note.

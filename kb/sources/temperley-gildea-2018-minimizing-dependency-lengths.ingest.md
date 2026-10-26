---
description: "Temperley & Gildea 2018 review of dependency length minimization: rival tests (EIC, end-weight, predictability), contested comprehension evidence, and bounds on writer word-order rules"
source: https://doi.org/10.1146/annurev-linguistics-011817-045617
captured: "2026-10-26"
capture: pdftotext
capture_scope: full-source
capture_note: "Publisher PDF supplied by the user; 14 per-page download-watermark lines removed. Body text was checked word by word against the publisher HTML page: all substantive differences were hyphenation, ligatures, numbered example sentences absent from the HTML, and reference-list formatting."
doi: "10.1146/annurev-linguistics-011817-045617"
genre: scientific-paper
snapshot_sha256: b15306c4abf6234c5789a18263c447c396ffe82f9c24053cee5910c3f6030617
ingested: "2026-10-26"
occasion: "Commonplace is considering adding dependency-length-minimization guidance to its writing instructions for natural-language output (KB notes, instructions, operator messages) that is read by humans inside and outside the project and also by LLM agents. What does this source establish about the relation between syntactic dependency distance and processing cost, what operational word-ordering rules for writers does it support, and what are the limits of its evidence?"
type: types/ingest-report.md
domains: [writing-conventions, psycholinguistics, dependency-length, word-order]
---

# Ingest: Minimizing Syntactic Dependency Lengths (Temperley & Gildea 2018)

## Classification

This is a narrative review article in the *Annual Review of Linguistics*
4:67-80. It reports no new data. It organizes prior typological, corpus,
computational and experimental work under one hypothesis, dependency length
minimization (DLM). DLM is the preference for placing a head and its dependent
close together.

Author: David Temperley (Eastman School of Music) and Daniel Gildea (computer
science), both at the University of Rochester. Both are principal contributors
to the DLM literature. Several of the reviewed studies are their own
(Temperley 2007, 2008; Gildea & Temperley 2007, 2010; Temperley & Gildea 2010),
so the review is written by proponents.

## Summary

The review argues that DLM is "an important factor in language structure and
cognition". It groups the evidence by method. Typology shows consistent
branching and short-near-head ordering rules across languages. Corpus studies
of syntactic choice show that English writers prefer orders with shorter
dependencies, for example short-before-long post-verbal phrases and inverted
quotation verbs after long subjects. Computational simulations show that real
English sentences average 47.5 words of total dependency length. Random
projective orders of the same trees average 82.7, and the projective optimum is
33.5. Across 20 and 37 languages, observed lengths are below chance. The
review also reports two contrasts that separate DLM from rivals. In
three-adjunct English constructions, the first adjunct is shorter than the
second, which DLM predicts and Hawkins's Early Immediate Constituents (EIC)
theory does not. In head-final Japanese, long-before-short ordering is
preferred, which DLM predicts and production end-weight does not. On
comprehension, it presents Gibson's Dependency Locality Theory (DLT) with its
critiques. Demberg & Keller found DLT a small predictor of reading times.
Levy & Keller found antilocality effects, where added intervening material
made a verb easier to read. ACT-R models decay in time and add interference
from similar intervening structures. Gildea & Jaeger found that observed
grammars trade dependency length against n-gram predictability. The authors
leave open whether DLM is caused by production or comprehension pressure. They
note that expectation may explain part of the comprehension benefit, because
frequent orders are easier to process. Corpus figures depend on the tested
decomposition: projective dependency trees under one headhood convention, held
fixed while word order varies.

## Contribution assessment (our opinion)

The problem matters: whether one locality principle explains word-order
regularities across grammar, production and comprehension. The review's
contribution is synthesis and criticism, not new evidence. It sets DLM against
named rivals and reports which observed contrasts separate them. It marks one
English case as indecisive, and it states the comprehension evidence's limits
openly. That is useful Popperian work: the strongest support it reports comes
from cases where rivals make opposite predictions, not from agreement alone.
Its likely significance is as a compact, citable entry point to the
literature. Its weaknesses are typical of a short narrative review. Coverage is
selective, the authors' own studies are prominent, and no effect sizes are
pooled. The causal question is explicitly left open. These narrow the
conclusions rather than undermine them. Originality cannot be judged against
other reviews from the material in hand; the overlapping Futrell, Levy and
Gibson review is one comparison point.

## Quotes

> In one study, Demberg & Keller (2008) tested the theory’s ability to predict data from the Dundee corpus, a collection of reading time measurements on newspaper text. The study found the DLT to be limited as a predictor of reading times in general because it generates predictions only for nouns and verbs. When nouns and verbs were analyzed separately, the DLT was a significant though fairly small predictor of reading times.
> --- `kb/sources/.snapshots/temperley-gildea-2018-minimizing-dependency-lengths.md` @ `sha256:b15306c4abf6234c5789a18263c447c396ffe82f9c24053cee5910c3f6030617` — §5, Demberg & Keller (2008)

> A challenge for the DLT is the phenomenon of so-called antilocality effects. In some cases, the processing difficulty of a word (measured by reading time) seems to decrease, not increase, as it gets further from its dependents.
> --- `kb/sources/.snapshots/temperley-gildea-2018-minimizing-dependency-lengths.md` @ `sha256:b15306c4abf6234c5789a18263c447c396ffe82f9c24053cee5910c3f6030617` — §5, antilocality

> This additional argument inserts a discourse referent between the object den Fußball and the verb versteckt, which should increase the processing difficulty of the verb, according to the DLT. However, the verb was read more quickly when the dative argument was included. Levy & Keller (2013) argue (following Konieczny 2000 and others) that this is because the additional argument makes the verb more predictable. The more arguments have occurred, the more likely it is that the verb will follow, and the more information we have as to what it will be. However, a second experiment showed evidence for locality effects:
> --- `kb/sources/.snapshots/temperley-gildea-2018-minimizing-dependency-lengths.md` @ `sha256:b15306c4abf6234c5789a18263c447c396ffe82f9c24053cee5910c3f6030617` — §5, Levy & Keller (2013), sentences 11–12

> The authors find that optimizing one criterion does not generally lead to good performance on the other, but that the observed languages are generally closer to some optimal frontier that trades off dependency length against average log probability. This finding provides evidence that both of these measures of processing difficulty have independently contributed to the development of the languages studied.
> --- `kb/sources/.snapshots/temperley-gildea-2018-minimizing-dependency-lengths.md` @ `sha256:b15306c4abf6234c5789a18263c447c396ffe82f9c24053cee5910c3f6030617` — §4, Gildea & Jaeger (2015)

> An issue not addressed above is the ultimate cause of DLM. Two possibilities, not mutually exclusive, are that it arises from constraints on either production or comprehension.
> --- `kb/sources/.snapshots/temperley-gildea-2018-minimizing-dependency-lengths.md` @ `sha256:b15306c4abf6234c5789a18263c447c396ffe82f9c24053cee5910c3f6030617` — conclusion

> However, evidence has also shown that comprehension difficulty is greatly affected by expectation, which in turn is shaped by the statistics of the linguistic input—the frequency of different syntactic structures and configurations (Levy 2008). If (for example) language production favors a short–long ordering of adjuncts, then it would not be surprising if this ordering was easier to process, simply because it is more often encountered and therefore more expected. Perhaps the most likely possibility is that DLM is inherently advantageous for both production and comprehension, and that each one is further shaped by the other in a mutually reinforcing process.
> --- `kb/sources/.snapshots/temperley-gildea-2018-minimizing-dependency-lengths.md` @ `sha256:b15306c4abf6234c5789a18263c447c396ffe82f9c24053cee5910c3f6030617` — conclusion

## Connections Found

For the occasion, this source is the **bounding review** among the
dependency-locality captures. The sibling ingests supply the primary evidence:
Gibson's DLT as the comprehension mechanism, Temperley 2007 for English writer
choices and Futrell 2015 for the cross-language baseline. This review supplies
the rivals and failures that any writing rule built on them must state.

It compares with the [Gibson DLT
ingest](./gibson-dependency-locality-theory.ingest.md) on distance as the
human comprehension-cost mechanism. That ingest names the rivals as
underweighted from background knowledge. This review provides them from a
citable source: the small reading-time effect, antilocality, ACT-R time decay
with interference, and the Gibson & Warren and Alexopoulou & Keller cost
modifications.

It compares with the [Temperley 2007
ingest](./temperley-2007-dependency-length-written-english.ingest.md) on
evidence for writer ordering choices. Cite the 2007 paper for the
constructions. Cite this review for how those constructions discriminate DLM
from EIC and end-weight, and for the estimate that writers' choices, not
grammar alone, shorten English dependencies (51.4 under a corpus-matched fixed
grammar against 47.5 observed).

It compares with the [Futrell 2015
ingest](./futrell-dependency-length-minimization.ingest.md) on observed
dependency length against random and optimal baselines. That ingest reads
locality as a pressure, not a target, without naming the competing pressure.
This review names one, n-gram predictability, and reports that observed
grammars lie near a tradeoff frontier between the two.

It is evidence for the human half of [Human writing structures transfer to
LLMs because failure modes
overlap](../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md).
Typological, corpus and experimental evidence converge on locality, with
stated limits. The LLM half remains untested.

It compares with [Two rewrites exposed a syntax-or-repetition
tradeoff](../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md)
on lowering attachment cost while preserving syntactic relations. The review
adds reordering under a fixed tree, and extraposition, which can shorten
dependencies at the price of crossing them. Both findings concern human
readers at word scale.

It is evidence for [An experiment identifies only the contrast it actually
runs](../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md)
as an independent illustration from outside agent evaluation. The review
credits DLM over EIC and end-weight only where their predictions diverge, and
it calls the English premodifier case, where they are not separated,
indecisive.

## Extractable Value

1. **Writer rules this review supports, with evidence type** -- each rule
   should carry its evidence class, because the classes differ in what they
   show:
   - *Put the longer of two post-head phrases last in English* (heavy-NP
     shift, short-before-long adjuncts, the shorter of three adjuncts first).
     Support: corpus evidence of writer choice, plus a DLM-over-EIC contrast.
     This shows what writers do, not measured reading ease.
   - *Keep a subject short when a verb or quoted clause depends across it*
     (quotation inversion with long subjects; objects longer than subjects;
     shorter subjects after a fronted adjunct). Support: corpus evidence of
     writer choice.
   - *Avoid object relatives with full-noun subjects and nested
     center-embedding; prefer subject relatives or a pronoun subject.*
     Support: comprehension experiments under DLT (sentences 7 to 10 in the
     review). This is the strongest direct cost evidence in the review.
   - *Place a late modifier next to the head it modifies.* Readers prefer to
     attach a sentence-final modifier to the most recent eligible head
     (sentence 21). A modifier meant for an earlier verb is likely to be
     misattached. Support: ambiguity-resolution evidence, with the authors'
     doubts about the parsing mechanism.

   The ordering direction is language-specific. DLM predicts long-before-short
   for pre-head dependents, and Japanese shows it. The English pre-head case
   is indecisive, so the review supports no rule for fronted material.
   [experiment]
2. **The distance-cost link is contested, so guidance should state it as a
   pressure** -- the review shows that dependency distance predicts human
   processing difficulty in targeted constructions. The effect on naturalistic
   reading is small. It can reverse when added material makes the verb more
   predictable. It may partly reflect frequency-based expectation rather than
   distance itself. A writing instruction should present locality as one
   pressure that a writer weighs against predictability and clarity, not as a
   quantity to minimize. [quick-win]
3. **The competing pressure is named and measured** -- observed grammars sit
   near a frontier that trades dependency length against next-word
   predictability, and optimizing either one alone performs poorly on the
   other. This explains why the observed length stays above the optimum, and
   it is the reason a rule should not push sentences toward the computed
   minimum. [just-a-reference]
4. **Extraposition is a bounded exception** -- moving a long relative clause
   after a verb modifier can shorten dependencies and improves acceptability
   when the clause is long. A separate study found added difficulty even with
   length controlled. Guidance can permit it for long modifiers but should not
   recommend it as a general move. [just-a-reference]
5. **Distance has several metrics** -- word count, intervening new discourse
   referents (DLT), elapsed time with similarity-based interference (ACT-R)
   and intervening syntactic heads (Alexopoulou & Keller). The interference
   result yields one further candidate rule: avoid placing a similar clause,
   such as another subject-verb pair, between a subject and its verb. A lint
   check or rule must choose a metric, and the choices can rank sentences
   differently. [just-a-reference]

## Limitations (our opinion)

- **Narrative review by proponents.** Selection is not systematic, and the
  authors' own studies supply most of the computational evidence. The
  disclosure statement reports no conflicts, but the framing favours DLM. The
  review does present rivals and failures, which reduces this concern without
  removing it.
- **Corpus figures depend on the analysis held fixed.** All dependency-length
  numbers assume one headhood convention, and the review itself says headhood
  for noun phrases and coordination is controversial. The simulations also
  hold the dependency tree fixed and vary only order. They cannot compare
  alternative ways of structuring the content, such as splitting a sentence or
  restating a referent, which are the alternatives the KB's own rewrite
  evidence tested.
- **Production evidence is not comprehension evidence.** The writer-choice
  rules rest on what edited English writers produced, mostly in *Wall Street
  Journal* news prose. The review's own conclusion leaves the cause open, and
  the expectation account predicts that frequent orders feel easier whether or
  not distance matters. For the occasion, those rules are skilled practice,
  not measured readability gains.
- **Weak naturalistic comprehension effect.** The strongest cost evidence
  comes from constructed sentences with object relatives and center
  embedding, which are rare in KB prose. Demberg & Keller report DLT as a
  significant but small predictor on newspaper reading. The gain from
  reordering ordinary technical prose may therefore be small.
- **No evidence about LLM readers.** Every proposed mechanism is human memory:
  activation decay, storage cost or retrieval interference. Nothing here
  shows a transformer paying a cost that grows with intervening words. Under
  [Human writing structures transfer to LLMs because failure modes
  overlap](../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md),
  each convention still needs an LLM-side check.
- **Capture gaps.** The extraction omits the branching diagrams for
  structures 1 to 4, and some interlinear German glosses are broken up. The
  prose explains those cases enough to follow them. Coverage ends in 2017.

## Recommended Next Action

When the theory note that the sibling ingests recommend is written in
`kb/theory/` (keeping dependents near their heads lowers human parse cost),
cite this ingest for its bounds section. The section should state four points:
the cost link is contested (small naturalistic effect, antilocality,
expectation); locality trades against predictability; the ordering direction
depends on head direction, and English fronted material has no supported rule;
and only the relative-clause and center-embedding rules have direct
comprehension evidence.

---

Relevant Notes:

- [Minimizing Syntactic Dependency Lengths: Typological/Cognitive Universal? (Annual Review of Linguistics, 2018)](https://doi.org/10.1146/annurev-linguistics-011817-045617) — derived-from: the ingest analysis is worked out from the published review
- [Gibson's Dependency Locality Theory ingest](./gibson-dependency-locality-theory.ingest.md) — compares-with: distance as the human comprehension-cost mechanism; this review supplies DLT's rivals and failures
- [Temperley 2007 dependency-length ingest](./temperley-2007-dependency-length-written-english.ingest.md) — compares-with: evidence for writer ordering choices; 2007 for constructions, this review for rival discrimination and the grammar-versus-choice split
- [Futrell 2015 dependency length minimization ingest](./futrell-dependency-length-minimization.ingest.md) — compares-with: observed length against random and optimal baselines; this review names predictability as the competing pressure
- [Human writing structures transfer to LLMs because failure modes overlap](../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) — is-evidence-for: human side only, with the contested comprehension evidence stated
- [Two rewrites exposed a syntax-or-repetition tradeoff](../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) — compares-with: lowering attachment cost while preserving relations; reordering and extraposition as human-reader levers
- [An experiment identifies only the contrast it actually runs](../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — is-evidence-for: independent illustration; DLM is credited over rivals only where predictions diverge

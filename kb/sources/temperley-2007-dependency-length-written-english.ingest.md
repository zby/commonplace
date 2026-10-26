---
description: "Temperley 2007 corpus study: English writers' syntactic choices shorten dependencies (short subjects, heavy-last, short-before-long adjuncts); evidence for writer word-order rules, human-only"
source: https://doi.org/10.1016/j.cognition.2006.09.011
captured: "2026-10-26"
capture: pdftotext
capture_scope: full-source
doi: "10.1016/j.cognition.2006.09.011"
genre: scientific-paper
snapshot_sha256: f6ae5fff8a98c76918267cfafe3f9b27f7a7cd87745a8d1535e0e886a1c7da9a
ingested: "2026-10-26"
occasion: "Commonplace is considering adding dependency-length-minimization guidance to its writing instructions for natural-language output (KB notes, instructions, operator messages) that is read by humans inside and outside the project and also by LLM agents. What does this source establish about the relation between syntactic dependency distance and processing cost, what operational word-ordering rules for writers does it support, and what are the limits of its evidence?"
type: types/ingest-report.md
domains: [writing-conventions, psycholinguistics, dependency-length, word-order]
---

# Ingest: Minimization of dependency length in written English (Temperley 2007)

## Classification

This is a peer-reviewed empirical paper in *Cognition* 105:300-333. It derives
predictions from a processing theory and tests them with eleven statistical
comparisons over an annotated corpus. It is a production-side corpus study.
It runs no reading-time, comprehension, or rewrite experiment.
Author: David Temperley, Eastman School of Music, University of Rochester. He
is known for computational models of music and language cognition. The paper
was accepted under Jacques Mehler's editorship.

## Summary

Temperley asks whether written English shows the preference that Gibson's
Dependency Locality Theory (DLT) predicts. DLT holds that integrating a word
with its head costs more as the distance between them grows. Temperley
measures distance in words and treats a phrase's complexity as the sum of all
its head-dependent distances. From this he derives four Dependency Length
Minimization Rules (DLMRs):

1. Branch consistently.
2. Keep left-branching constituents short in a mainly right-branching
   language.
3. When the order is free, put shorter dependents closer to the head.
4. When the order is fixed, keep the closer dependents short.

He tests them on the Wall Street Journal portion of the Penn Treebank, about
1 million words from 1989, and reruns the tests on the roughly 400,000-word
Brown portion. Most predictions hold in the WSJ data:

- Subjects are much longer when quotation verbs are inverted (9.47 vs 2.16
  words).
- Direct objects are longer than subjects (5.80 vs 3.13). The gap survives a
  hand-coded check limited to new-entity indefinites (8.95 vs 5.95).
- Adverbial clauses after the main clause are longer than those before it
  (11.41 vs 9.76).
- Subjects of relative clauses are shorter inside subject NPs than inside
  object NPs (1.41 vs 1.61).
- Of two post-verbal adjuncts, the second is longer (5.96 vs 3.04). The same
  holds for the first two of three adjuncts, a case that separates DLT from
  Hawkins's EIC theory.
- Subjects are shorter after a fronted adjunct, but objects are not. This
  rules out a simple general avoidance of long sentences.

One prediction fails. Two fronted adjuncts show a small, non-significant
short-long order where DLT predicts long-short. The same pattern appears more
strongly in the Brown data. The paper concludes that DLT and a rival
"short-first" principle together cover the data. It argues that written word
order more plausibly serves comprehension than production, but it does not
test that attribution.

## Contribution assessment (our opinion)

When it was published, the question was important. Comprehension evidence
for distance-based processing cost was strong, but production evidence was
mostly Hawkins's constituent-recognition work. This paper turned a
comprehension theory into specific, refutable predictions about free
syntactic choices. Tests 9 and 10 are a good control design: the predicted
effect appears for subjects and is absent for objects in the same contexts.
Test 11 is a well-chosen test that separates DLT from EIC. The method is
simple, though. It compares mean constituent lengths with one-way F-tests and
has no multivariate control for discourse status, semantic class, or genre.
Only one effect has a hand-coded given/new control, and that control covers
100 cases per group. My tentative judgment is that the paper's lasting value
is to show that dependency-length minimization is a measurable pressure on
production. It also shows plainly where that pressure fails to predict
orderings (fronted adjuncts, left-branching conjuncts, Turkish). From
background knowledge, it was an early step toward later multilingual
dependency-length studies. I cannot verify its priority or literature
coverage from this capture.

## Quotes

> Test 1: Subject NPs in quotation sentences, in S–V order and V–S order
> Result: Average length of subject NP: in S–V order, 2.16 words; in V–S order,
> 9.47 words.
> --- `kb/sources/.snapshots/temperley-2007-dependency-length-written-english.md` @ `sha256:f6ae5fff8a98c76918267cfafe3f9b27f7a7cd87745a8d1535e0e886a1c7da9a` — Test 1, quotation-verb inversion

> Test 7: Clauses with two postmodifying adjuncts
> Result: Average length of first adjunct = 3.04; average length of second
> adjunct = 5.96. (F(1, 5226) = 675.6, p < .0005)
> The prediction is confirmed; in clauses with two postmodifying adjuncts, the second
> adjunct tends to be significantly longer than the first.
> --- `kb/sources/.snapshots/temperley-2007-dependency-length-written-english.md` @ `sha256:f6ae5fff8a98c76918267cfafe3f9b27f7a7cd87745a8d1535e0e886a1c7da9a` — Test 7, two post-verbal adjuncts

> Test 8: Clauses with two premodifying adjuncts
> Result: Average length of first adjunct = 3.15, average length of second
> adjunct = 3.48. (F(1, 1224) = 3.4, p = .06, n.s.)
> In this case, the prediction—that the first adjunct will be longer than the second—is
> not confirmed; on average, the second adjunct is slightly longer.
> --- `kb/sources/.snapshots/temperley-2007-dependency-length-written-english.md` @ `sha256:f6ae5fff8a98c76918267cfafe3f9b27f7a7cd87745a8d1535e0e886a1c7da9a` — Test 8, two fronted adjuncts

> The dependency-length view predicts a long-short ordering here,
> but this was not found; rather, a short-long preference was found (though it is small and
> statistically non-significant), as would be predicted by the short-first principle.
> --- `kb/sources/.snapshots/temperley-2007-dependency-length-written-english.md` @ `sha256:f6ae5fff8a98c76918267cfafe3f9b27f7a7cd87745a8d1535e0e886a1c7da9a` — Discussion of Test 8

> Would we expect to find dependency-length minimization effects in speech?
> --- `kb/sources/.snapshots/temperley-2007-dependency-length-written-english.md` @ `sha256:f6ae5fff8a98c76918267cfafe3f9b27f7a7cd87745a8d1535e0e886a1c7da9a` — Discussion; the habit suggestion below is framed for speech production

> it may be that strategies for dependency-length minimization such as those discussed above—the avoidance of long subject NPs, for
> example—are acquired by speakers as general habits, so that elaborate length calculations are not required on every occasion.
> --- `kb/sources/.snapshots/temperley-2007-dependency-length-written-english.md` @ `sha256:f6ae5fff8a98c76918267cfafe3f9b27f7a7cd87745a8d1535e0e886a1c7da9a` — Discussion, speech production

## Connections Found

For the occasion, this source is the **operational anchor** among the
dependency-locality captures. It names specific constructions where skilled
writers shorten dependencies, so it is the closest available material to
word-order rules a writer could apply. It does not directly support the claim
that distance causes processing cost. That link is imported from Gibson's
comprehension work, which the paper cites but does not test.

It bounds [Two rewrites exposed a syntax-or-repetition
tradeoff](../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md).
That note found two ways to lower parsing load in mature prose: splitting,
which lost relations, and restating, which added 4.9% more words. Temperley
documents a third move in human writing. Reordering constituents keeps the
syntactic relations and shortens dependencies without adding words. The
paper measures what writers chose, not whether the result was easier to
understand. Reordering is therefore an untested candidate for the note's
tradeoff, not a refutation of it.

It is evidence for the human side of [Human writing structures transfer to
LLMs because failure modes
overlap](../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md).
At sentence scale, a writing convention (dependency-shortening order) tracks
a named human processing cost (activation decay over intervening words). The
note's per-convention transfer test then needs an LLM-side check that this
source cannot supply.

It compares with [Local materialization should outperform distant
natural-language
declarations](../theory/local-materialization-should-outperform-distant-declarations.md)
on one axis only: distance between a dependent element and what it depends on
as a cost. Temperley gives a human mechanism at sentence scale. The note is a
document-scale conjecture about LLM readers and explicitly does not assume a
monotonic decline with distance. The comparison keeps the scales and the
readers apart. It does not support the note.

No other tracked KB note addresses sentence-level syntactic processing cost.

## Extractable Value

1. **Candidate word-order rules with their corpus support** -- the
   writer-facing rules the paper supports, each as "skilled writers do this",
   not "this improves reading":
   - put the heavier of two post-head phrases last (Tests 7 and 11; the
     heavy-NP and dative cases are discussed but not tested here);
   - keep pre-verbal subjects short, and move elaboration such as appositives
     and non-restrictive relative clauses to object position or a later
     mention (Tests 2 and 3, and the Ortega example);
   - put long adverbial clauses after the main clause (Tests 4 and 5; the
     effect is modest, about 1.5 words);
   - keep the subject short after a fronted adjunct (Test 9);
   - avoid relative clauses nested inside subjects, which create
     center-embedding (Test 6, which does not replicate in Brown).

   These rules preserve relations, so they fit the gap that the
   syntax-or-repetition note leaves open better than splitting does. Their
   comprehension benefit is inferred from DLT, and their benefit for LLM
   readers is untested. [experiment]
2. **What the source establishes about distance and cost** -- it establishes
   a production correlation. Written English shows the constituent-length
   asymmetries that a distance-cost theory predicts, at very large N, and the
   Brown data mostly agree. It does not establish that distance causes
   processing cost. Guidance written from this paper should cite comprehension
   evidence, such as Gibson's DLT studies, for the cost claim and cite this
   paper only for "writers already do this". [just-a-reference]
3. **A rule the evidence does not support: "long before short" for fronted
   material** -- DLT predicts that the longer of two fronted adjuncts should
   come first. Writers do the reverse, weakly in the WSJ data and strongly in
   Brown. Guidance that follows dependency-length arithmetic mechanically
   would recommend an order skilled writers avoid. A "short-first" default
   plus the DLT-specific rules for subject length covers the observed
   choices better. [quick-win]
4. **Two separable metrics** -- dependency length can be counted in words or
   in new discourse referents. Complexity can be the sum of distances or the
   peak integration cost. The paper uses words and the sum, while Gibson uses
   referents and the peak. A writing rule or lint check must choose one, and
   the choices can rank sentences differently. [just-a-reference]
5. **Habit as the production mechanism** -- the paper suggests that speakers
   acquire dependency-minimizing strategies as habits, for example avoiding
   long subjects, instead of calculating lengths. The suggestion is framed
   for speech production; applying it to writing is an extension. This
   matches how guidance
   could be stated: as a few construction-level heuristics, not as an
   instruction to compute dependency lengths. [just-a-reference]

## Limitations (our opinion)

- **Production evidence, not processing evidence.** The tests count what
  writers produced. The step from "writers prefer shorter dependencies" to
  "shorter dependencies are easier to read" rests on cited comprehension work
  and on the author's argument that writing lacks speech's time pressure. No
  reader was measured, and the paper says the production-versus-comprehension
  question is unresolved. For the occasion, this means the paper can justify a
  rule as conventional skilled practice but not as a measured readability
  gain.
- **No evidence about LLM readers.** The proposed cost mechanism is
  activation decay in human working memory. Nothing here shows that a
  transformer pays a cost that grows with intervening words.
  [Human writing structures transfer to LLMs because failure modes
  overlap](../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md)
  requires that check for each convention. Guidance for mixed human and agent
  readers can rely on the human side only.
- **Simple statistics and partial confound control.** Each test compares mean
  lengths between two groups. There is no regression on discourse status,
  definiteness, semantic type, or genre. Given/new is controlled only in
  Test 3, on 100 hand-classified cases per group coded by one person.
  Argument versus adjunct is approximated from Treebank function tags. The
  author names discourse factors as an open alternative. Very large N makes
  small differences significant. Test 6's 0.2-word difference has p < .05,
  and statistical significance does not show that a rule is worth stating.
- **Narrow, edited genre.** The WSJ data is 1989 house-edited news prose. The
  Brown rerun widens the genre, but the paper does not give its significance
  tests. Brown fails to replicate Test 6. As extracted from the table, Brown
  object NPs in Test 10 are longer with a fronted adjunct (5.09 vs 4.54),
  which the text does not discuss. Commonplace's technical, list-heavy,
  heavily qualified prose is not represented.
- **The rival explanation is not ruled out.** A short-first principle
  explains the adjunct and conjunct orderings and the failed fronted-adjunct
  prediction. DLT is needed only for short left-branching constituents and
  for the Test 9 and 10 asymmetry. The DLT-versus-EIC comparison is "far
  from resolved" in the author's words, and the Turkish test rests on 87
  cases.
- **Heavy-NP shift and the dative alternation are not tested here.** The
  paper explains them as predicted by DLMR 3 and cites other authors for the
  data. Do not cite this paper as corpus evidence for those two
  constructions.

## Recommended Next Action

Record one entry in the "Ideas to test later" section of
`kb/reports/retained/asd-ste100-inspired-rewrite.md`. The entry would propose
a constituent-reordering pass over one KB note. The pass would apply heavy
phrases last, short subjects, long adverbial clauses after the main clause,
and short subjects after fronted adjuncts, and it would measure meaning
preservation and word count against the two earlier rewrites. Do this before
any dependency-length rule enters a writing instruction. This source supports
the rules only as observed human practice, and their value for agent readers
has no test yet.

---

Relevant Notes:

- [Minimization of dependency length in written English (Cognition, 2007)](https://doi.org/10.1016/j.cognition.2006.09.011) — derived-from: the ingest analysis is worked out from the published paper
- [Two rewrites exposed a syntax-or-repetition tradeoff](../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) — compares-with: ways to lower parsing load while preserving relations carried by syntax; reordering is the untested third route
- [Human writing structures transfer to LLMs because failure modes overlap](../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) — is-evidence-for: human side only; a word-order convention tracks a named human processing cost
- [Local materialization should outperform distant natural-language declarations](../theory/local-materialization-should-outperform-distant-declarations.md) — compares-with: distance as cost, contrasting sentence-scale human evidence with a document-scale LLM conjecture

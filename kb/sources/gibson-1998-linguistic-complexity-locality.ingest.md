---
description: "Gibson's 1998 SPLT: human sentence difficulty tracks peak load from long-held predicted heads and distant attachments, saturating per item; supports nesting and heavy-last rules, human-only"
source: https://doi.org/10.1016/S0010-0277(98)00034-1
captured: "2026-10-26"
capture: pdftotext
capture_scope: full-source
doi: "10.1016/S0010-0277(98)00034-1"
genre: scientific-paper
snapshot_sha256: b77b8a7a5be43ddf817e9ea2c41618960a19164b2a954b9d0b2f7d0d9b02e07d
ingested: "2026-10-26"
occasion: "Commonplace is considering adding dependency-length-minimization guidance to its writing instructions for natural-language output (KB notes, instructions, operator messages) that is read by humans inside and outside the project and also by LLM agents. What does this source establish about the relation between syntactic dependency distance and processing cost, what operational word-ordering rules for writers does it support, and what are the limits of its evidence?"
type: types/ingest-report.md
domains: [writing-conventions, psycholinguistics, dependency-length, sentence-processing]
---

# Ingest: Linguistic complexity: locality of syntactic dependencies (Gibson 1998)

## Classification

This is a long theoretical journal article (Cognition 68, 1998, 76 pages). It
proposes a formal resource model of sentence comprehension and argues for it
against named rival theories. Its evidence is mixed. Two self-paced reading
datasets are compared with predicted costs: King and Just (1991) and an
experiment by Gibson and Ko that was still in progress, with 48 participants at
the time of writing. One rating questionnaire is reported (Gibson and Warren).
Most contrasts rest on published acceptability findings or on the author's
intuitive judgments. It is therefore a scientific paper whose tests are mostly
consistency checks against known contrasts.
Author: Edward Gibson (MIT Brain and Cognitive Sciences), a leading
sentence-processing researcher. This paper introduces the Syntactic Prediction
Locality Theory (SPLT), the precursor of his later Dependency Locality Theory.
He is an advocate of the theory he presents.

## Summary

Gibson proposes that comprehension draws on one limited pool of working-memory
resources with two kinds of cost. **Integration cost** is paid when a new word
attaches to an earlier head or dependent. It grows with the number of new
discourse referents (new noun phrases and tensed verbs as events) processed
since that head was last activated. **Memory cost** is paid for every
obligatory syntactic head the sentence still needs. Each predicted head costs
more the longer it has been held, again counted in new referents; the
prediction of the top-level clause's verb is free. Reading time is integration
cost divided by the resources left over after storage. Judged difficulty is set
by the **maximal** memory load at any parse state, not by length or average
load. Two same-length, same-meaning sentences differ from easy to
unprocessable, and adding right-branching clauses to a hard sentence does not
make it harder (examples 13 to 15). Gibson argues that per-item memory cost
saturates (a sigmoid, section 2.6.7): one dependency stretched by many
modifiers stays processable. He concludes that overload needs at least two long
unresolved predictions held at once, putting capacity near 2M(3) memory units
(section 3.5). From this he derives the subject- versus object-extracted
relative clause contrast, overload in doubly center-embedded clauses, the
SC/RC versus RC/SC asymmetry, easier embeddings with an indexical pronoun as
the innermost subject, Japanese stacking effects, easier Dutch cross-serial
than German nested verbs, and **heaviness**: putting the longer of two
dependents last lowers peak integration and memory cost (section 4). He
conjectures that the same costs drive speakers' heavy-last choices, on the
condition that production plans little right-hand structure ahead (footnote
25). Section 6 states a weakness in the model itself. In an activation model,
if storage cost grows with distance then integration should not, so Gibson
sketches a variant with fixed storage cost. That variant became the later DLT.

## Contribution assessment (our opinion)

The problem, which limited resource makes some unambiguous sentences hard, is
central to psycholinguistics, and the paper's value is a bold, quantified
conjecture that unifies phenomena earlier theories explained piecemeal. Its
best tests are discriminating contrasts that rivals get wrong: the SC/RC
asymmetry, the pronoun effect that incomplete-dependency counts cannot
predict, and two-clause sentences that become unprocessable. These are real
error-eliminating moves. The empirical base is weaker than the scope. The
reading-time support is two small datasets fitted region by region with
correlations described as high, and one of them was unfinished. Most overload
and heaviness claims are intuitions or prior ratings, and the cost functions
and the capacity of about 2M(3) are fitted to the same contrasts they explain.
Gibson's own section 6 concedes that the dual-distance design is weakly
motivated, which is to the paper's credit as criticism. From background
knowledge, the SPLT and its DLT successor became standard reference theories,
so its significance as a framework is likely high. The specific SPLT memory
function is best read as a superseded stage rather than a settled result.
Originality against the rivals it reviews is clear; I cannot assess priority
beyond that review.

## Quotes

> it is assumed that the relative intuitive acceptability of
> two unambiguous sentences which are controlled for plausibility is determined by the
> maximal quantity of memory resources that are required at any point during the parse
> of each sentence
> --- `kb/sources/.snapshots/gibson-1998-linguistic-complexity-locality.md` @ `sha256:b77b8a7a5be43ddf817e9ea2c41618960a19164b2a954b9d0b2f7d0d9b02e07d` — §2.5, difficulty hypothesis

> If sentence length were a major factor in determining intuitive sentence complexity, then
> (14) should be judged roughly as complex as (13), since the two sentences are of
> the same length and have the same meaning. However, (13) is much more complex
> than (14).
> --- `kb/sources/.snapshots/gibson-1998-linguistic-complexity-locality.md` @ `sha256:b77b8a7a5be43ddf817e9ea2c41618960a19164b2a954b9d0b2f7d0d9b02e07d` — §2.5, examples 13 vs 14

> Thus intuitive complexity is not determined by the average memory complexity
> over a sentence. We therefore assume that the intuitive complexity of a sentence is
> determined by the maximal memory complexity reached during the processing of
> the sentence.
> --- `kb/sources/.snapshots/gibson-1998-linguistic-complexity-locality.md` @ `sha256:b77b8a7a5be43ddf817e9ea2c41618960a19164b2a954b9d0b2f7d0d9b02e07d` — §2.5, after examples 15a-b

> One prediction of a
> linear memory cost function is that it is steadily increasing, even in the limit. Thus,
> given a single syntactic prediction whose cost is determined by the function, there
> should be some distance such that the total cost associated with maintaining this
> prediction exceeds the processor’s available computational resources. For example,
> the prediction of the second object of a ditransitive verb can be delayed indefinitely
> by adding modifiers to the first object. If the memory cost function M(n) is linear,
> then there should be some number of modifiers (e.g. prepositional phrases or relative
> clauses) such that the addition of one further modifier causes processing breakdown.
> Intuitive judgments suggest that this prediction is not borne out:
> --- `kb/sources/.snapshots/gibson-1998-linguistic-complexity-locality.md` @ `sha256:b77b8a7a5be43ddf817e9ea2c41618960a19164b2a954b9d0b2f7d0d9b02e07d` — §2.6.7, linear-cost prediction

> Once past a certain distance, there is no noticeable complexity difference between
> different distance predicted category realizations, and this point occurs well before
> memory overload.
> --- `kb/sources/.snapshots/gibson-1998-linguistic-complexity-locality.md` @ `sha256:b77b8a7a5be43ddf817e9ea2c41618960a19164b2a954b9d0b2f7d0d9b02e07d` — §2.6.7, after examples 30-31

> This evidence suggests that the memory cost function heads asymptotically
> toward a maximal complexity.
> --- `kb/sources/.snapshots/gibson-1998-linguistic-complexity-locality.md` @ `sha256:b77b8a7a5be43ddf817e9ea2c41618960a19164b2a954b9d0b2f7d0d9b02e07d` — §2.6.7, sigmoid motivation

> A generalization that presents itself from the SPLT analysis is that structures
> which include a parse state with at least two long unresolved predicted categories
> in addition to the top-level verb are unacceptable, and those without such a state are
> usually acceptable. Under the memory cost function assumed here, a ‘long’ unresolved prediction is one spanning at least three intervening new discourse referents.
> --- `kb/sources/.snapshots/gibson-1998-linguistic-complexity-locality.md` @ `sha256:b77b8a7a5be43ddf817e9ea2c41618960a19164b2a954b9d0b2f7d0d9b02e07d` — §3.5, overload generalization

> if a verb is followed by two arguments or modifiers, and if one of the two
> phrases is much longer than the other, then the structure is easier to understand if the
> heavy phrase is ordered second, even if there is a grammatical reason to put it first.
> --- `kb/sources/.snapshots/gibson-1998-linguistic-complexity-locality.md` @ `sha256:b77b8a7a5be43ddf817e9ea2c41618960a19164b2a954b9d0b2f7d0d9b02e07d` — §4, heaviness preference

> Indeed, the SPLT directly accounts
> for the ordering preference. In particular, the ordering complexity effects follow
> from the integration cost component of the SPLT which dictates that longer distance
> attachments are more expensive to make than shorter distance ones. In particular, the
> reason that the structures in (55) are harder to process than the structures in (56) is
> that the maximal integration cost is higher in the examples in (55) than it is in the
> examples (56), due to a long-distance integration that is required in the processing of
> (55), but not in the processing of (56).
> --- `kb/sources/.snapshots/gibson-1998-linguistic-complexity-locality.md` @ `sha256:b77b8a7a5be43ddf817e9ea2c41618960a19164b2a954b9d0b2f7d0d9b02e07d` — §4, integration-cost account of 55 vs 56

> Hence less memory cost is needed in processing structures with obligatory heavy-shifted phrases.
> --- `kb/sources/.snapshots/gibson-1998-linguistic-complexity-locality.md` @ `sha256:b77b8a7a5be43ddf817e9ea2c41618960a19164b2a954b9d0b2f7d0d9b02e07d` — §4, memory-cost account of 55a vs 56a

## Connections Found

For the occasion, this source is the **peak-and-saturation anchor** of the
dependency-locality batch. Its siblings supply the fixed-storage revision and
the production evidence. It compares with
[The Dependency Locality Theory](./gibson-dependency-locality-theory.ingest.md)
on the storage-cost function. SPLT makes a held prediction's cost grow with
distance and saturate. DLT, motivated by SPLT's own section 6 critique, fixes
it per predicted head. The two predict different costs for one long held
expectation, so a writing rule citing "Gibson" must say which model it
assumes. It compares with
[Temperley 2007](./temperley-2007-dependency-length-written-english.ingest.md)
on how dependency cost is aggregated. Temperley sums word distances. SPLT
section 2.5 is the primary argument that judged difficulty tracks the peak
load, not the total, so it settles that open choice on the Gibson side for
human comprehension. It compares with
[Futrell, Levy and Gibson](./futrell-levy-gibson-dependency-locality.ingest.md)
on production versus comprehension. That paper shows writers minimize
dependency length without testing reader cost. SPLT section 4 is where the
comprehension model is conjectured to drive production, under a stated
planning condition, so the link from "writers do this" to "readers benefit" is
asserted here rather than tested.

On the KB side, the source is evidence for
[Two rewrites exposed a syntax-or-repetition tradeoff](../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md),
for human readers only. It adds two points to that note's undifferentiated
"parsing load". A rewrite only needs to lower the sentence's heaviest point.
Reordering nested material into right-branching form removes overload while
keeping every word and relation (13 versus 14), which is a third option beside
splitting or repeating. It is likewise evidence for the human half of
[Human writing structures transfer to LLMs because failure modes overlap](../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md).
It names the human failure that "no nested clauses" and "heavy constituent
last" prevent, namely peak load from several simultaneously held
predictions. The LLM half remains untested. It compares with
[Soft degradation can bind before the hard cap](../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md)
on load that length does not predict. Structure, not word count, decides
difficulty, and footnote 7 names similarity-based interference as a further
cost. This is an analogy from a human processor, not evidence about models. It
compares with
[Soft-bound traditions as sources for context engineering strategies](../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md)
on the shape of a working-memory bound. SPLT gives a saturating per-item cost
where overload comes from how many long predictions are held at once, not
from one very long one.

## Extractable Value

1. **What the source establishes about distance and cost** -- for human
   readers of unambiguous sentences, cost rises with the number of new
   discourse referents between a word and its attachment site, and with how
   long obligatory heads are held open. Judged difficulty follows the worst
   parse state, and per-item cost levels off after two or three intervening
   referents. The support is two small reading-time fits on relative clauses
   plus many rating and intuition contrasts on extreme constructions, in
   English, Japanese, Dutch and German. Guidance should cite it as a human
   comprehension model of long and stacked dependencies, not as a measured
   cost function for ordinary technical prose. Human-reader reach is high;
   LLM-reader reach is not established. [quick-win]
2. **Writer rules the source directly supports** -- each rule maps to a named
   contrast, so each can be tested and dropped on its own:
   - never hold two long open dependencies at once, such as a clause nested
     inside a clause before either verb arrives (13, 34, 40b);
   - prefer the right-branching paraphrase of a nested sentence; it keeps the
     same words and meaning at far lower peak cost (13 versus 14);
   - when a head has two dependents, put the longer one last (55 versus 56);
   - extrapose a clausal subject behind its verb ("It bothered the intern
     that ..." over "That ... bothered the intern", 57);
   - inside an unavoidable embedding, use given referents (pronouns,
     established terms) rather than new entities (16, 17);
   - prefer subject-extracted to object-extracted relative clauses (1).
   [quick-win]
3. **Target the peak, not sentence length** -- SPLT predicts that appending
   right-branching clauses does not raise judged difficulty, while one nested
   point can make a sentence unprocessable. A rewrite or lint check should
   look for the sentence's worst state (several open heads, a long-distance
   attachment), not for word count. This conflicts with summed-distance
   metrics such as Temperley's, and a check must choose one. [experiment]
4. **Saturation limits over-correction** -- one long dependency, such as a
   heavily modified object before a second argument (30, 31), stays
   processable, and overload needs two long predictions held together. A
   guideline that flags every long dependency would over-fire; flagging
   overlapping long dependencies matches the source. This conclusion rests on
   intuitive judgments only. [experiment]
5. **Storage-model choice is a live disagreement** -- section 6 shows that
   SPLT's distance-based storage is weakly motivated and sketches the
   fixed-storage variant that became DLT. Rules 2 to 4 above survive under
   either model, but the exact cost of one long held prediction does not. A
   theory note should state the rules without SPLT's memory-unit arithmetic.
   [just-a-reference]
6. **Production conjecture with its condition** -- heavy-last ordering is
   predicted to also ease production, but only if the producer does not plan
   right-hand structure in detail (footnote 25). For LLM writers, which
   generate left to right, the condition's analogue is open. The conjecture
   does not show that reader benefit and writer habit coincide.
   [just-a-reference]

## Limitations (our opinion)

The central claim is bounded in five ways. First, every test concerns human
readers. Nothing here measures LLM comprehension. The model's mechanism is
activation decay over intervening material in a fixed resource pool, which a
transformer reader does not share by construction, so benefit to agent readers
needs its own test. Second, the evidence is thin relative to the theory's
scope. The only on-line data are relative-clause reading times from two
small studies, one unfinished, with correlations reported only as "high" and
no per-condition statistics. Most overload, heaviness and saturation claims
rest on intuitive judgments, sometimes the author's own, about extreme
constructions such as doubly nested relative clauses that rarely occur in KB
prose. The source therefore gives no effect sizes for the milder dependencies
of ordinary technical writing. Third, the cost functions are fitted, not
independently measured. "Almost any monotonically increasing function"
reproduces the contrasts, the sigmoid's parameters and the capacity near
2M(3) are set from the same examples they explain, and the text states B = 1
while Figure 5's formula implies a centre at n = 2. Precise unit counts in a
writer rule would claim more than the source has. Fourth, the model carries
stipulations that Gibson himself questions: the cost-free top-level predicate,
the clause-closure principle, and distance-based storage. Section 6 offers a
variant that removes them, so the SPLT memory function is not the author's
settled view. Fifth, rivals are mostly older memory-count, stack and
perspective theories. Semantic-similarity interference is set aside as
orthogonal (footnote 4), and expectation-based accounts are engaged only for
ambiguity resolution, so they remain alternative explanations for some
contrasts. The section 4 heaviness account explains a known preference but is
not tested against those alternatives.

## Recommended Next Action

When writing the planned `kb/theory/` note on dependency-locality writing rules
(the note the DLT and Futrell-Levy-Gibson ingests recommend), cite this ingest
for three bounded points: target the sentence's peak load rather than its
length; flag overlapping long dependencies rather than every long one; and
prefer relation-preserving right-branching reorderings. State the rules without
SPLT's unit arithmetic or a committed storage model, and mark LLM-reader
benefit as an untested conjecture.

---

Relevant Notes:

- [Linguistic complexity: locality of syntactic dependencies](https://doi.org/10.1016/S0010-0277(98)00034-1) — derived-from: the analysed paper
- [Two rewrites exposed a syntax-or-repetition tradeoff](../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) — is-evidence-for: peak parse load and right-branching reordering as a relation-preserving alternative, human readers only
- [Human writing structures transfer to LLMs because failure modes overlap](../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) — is-evidence-for: names the human failure behind no-nesting and heavy-last conventions; LLM half untested
- [Soft degradation can bind before the hard cap even when required evidence fits](../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) — compares-with: load set by structure rather than length, in a human processor
- [Soft-bound traditions as sources for context engineering strategies](../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) — compares-with: saturating per-item cost versus a count bound on working memory
- [The Dependency Locality Theory](./gibson-dependency-locality-theory.ingest.md) — compares-with: distance-based versus fixed storage cost for held predictions
- [Temperley 2007](./temperley-2007-dependency-length-written-english.ingest.md) — compares-with: peak load versus summed dependency length as the cost aggregate
- [Futrell, Levy and Gibson](./futrell-levy-gibson-dependency-locality.ingest.md) — compares-with: conjectured comprehension-to-production link versus measured production minimization

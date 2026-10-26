---
description: "Gibson's dependency locality theory: human parse cost grows with new referents between head and dependent plus open predictions; supports writer rules against nesting, human-only"
source: http://tedlab.mit.edu/tedlab_website/researchpapers/Gibson_2000_DLT.pdf
captured: "2026-10-26"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 63f9d57a3c6b5e12ea0ef5a30ac8d3009501edd243d89634bb86b4a498aec29b
ingested: "2026-10-26"
occasion: "Commonplace is considering adding dependency-length-minimization guidance to its writing instructions for natural-language output (KB notes, instructions, operator messages) that is read by humans inside and outside the project and also by LLM agents. What does this source establish about the relation between syntactic dependency distance and processing cost, what operational word-ordering rules for writers does it support, and what are the limits of its evidence?"
type: types/ingest-report.md
domains: [writing-conventions, psycholinguistics, dependency-length, sentence-processing]
---

# Ingest: The Dependency Locality Theory (Gibson 2000)

## Classification

This is a theoretical book chapter in psycholinguistics (chapter 5 of an edited
volume, 2000). It states a formal cost model and tests it against rival
resource theories with reported experiments. Most experiments are the author's
own, and the primary reports appear elsewhere (Gibson 1998, Gibson and Ko 1998,
Warren and Gibson 1999, Babyonyshev and Gibson 1999). The chapter therefore
summarizes evidence rather than reporting full methods, so it is classified as
a scientific paper with secondary-report evidence.
Author: Edward Gibson (MIT), the originator of the dependency locality theory
(DLT) and a central figure in sentence-processing research. He is an advocate
of the theory he presents.

## Summary

Gibson proposes that sentence comprehension draws on one fixed pool of
resources with two kinds of cost. **Integration cost** arises when a new word
is attached to an earlier head or antecedent. It is 1 energy unit (EU) for
building a new discourse referent plus 1 EU for each new discourse referent
(noun phrases, tensed verbs as events) that intervenes between the two linked
elements. Given referents, such as the pronouns *I* and *you*, cost less to
cross. **Storage cost** is 1 memory unit (MU) for each syntactic head still
required to finish the sentence grammatically. Intuitive difficulty tracks the
peak integration time in the parse, and the chapter states that the true cost
function is nonlinear: several long integrations at one word are worse than
one long integration. The theory explains why doubly center-embedded relative
clauses are unprocessable while right-branching paraphrases with the same
words are easy; why a pronoun as the innermost subject makes them easier
(questionnaire, Warren and Gibson 1999), which incomplete-dependency counts
cannot explain; why a complement clause containing a relative clause is easier
than the reverse; why a prepositional phrase in a nested position adds
difficulty; and why object-extracted relative clauses are slower than
subject-extracted ones. The word-region reading-time correlations come from
one self-paced reading study (32 participants, 16 items, about six regions per
sentence; r = 0.79 and 0.77, combined p < 0.005). Japanese ratings and an
ambiguity study (60 participants) support the storage component. Gibson leaves
the referent-only distance metric, the storage-integration relation, and
storage versus incomplete-dependency indexing explicitly unresolved.

## Contribution assessment (our opinion)

The problem is central to psycholinguistics: what limited resource makes some
unambiguous sentences hard. The chapter's main contribution is an explicit,
quantitative conjecture. It separates integration from storage, it measures
distance in new discourse referents rather than words, and it makes
word-by-word predictions that can be tested and refuted. The pronoun-subject
contrast is a well-chosen test against the incomplete-dependency theories,
because those theories predict no difference. The chapter's own evidence is
thin. The reading-time fits rest on a handful of regions with marginal
per-sentence significance, the difficulty contrasts are mostly ratings of
extreme constructions, and the rivals considered are older memory-count
theories. Surprisal-style expectation accounts and antilocality findings are
not addressed (rival status from background knowledge, corroborated by the
[Futrell, Levy and Gibson ingest](./futrell-levy-gibson-dependency-locality.ingest.md)).
From background knowledge, DLT became one of the field's standard reference
theories, so its likely significance is high as a framework. Its specific
metric is a tentative simplification that later work, such as
[Temperley 2007](./temperley-2007-dependency-length-written-english.ingest.md),
partly confirmed and partly failed.

## Quotes

> For simplicity , it is assumed that 1 EU is consumed for each new discourse referent in the intervening region .
> --- `kb/sources/.snapshots/gibson-dependency-locality-theory.md` @ `sha256:63f9d57a3c6b5e12ea0ef5a30ac8d3009501edd243d89634bb86b4a498aec29b` — section 5.3, integration cost distance assumption

> Becausereferentsfor first- and second-person pronouns are already presentin the current discourse, integrating acrossthem consumesfewer resourcesthan integrating across new discourse referents, according to the discourse-based DLT structural integration cost hypothesis.
> --- `kb/sources/.snapshots/gibson-dependency-locality-theory.md` @ `sha256:63f9d57a3c6b5e12ea0ef5a30ac8d3009501edd243d89634bb86b4a498aec29b` — section 5.3, pronoun-subject example (6)

> This RC, who John met, is therefore doubly nested. The resulting structure is so complex that it is unprocessablefor most people.
> --- `kb/sources/.snapshots/gibson-dependency-locality-theory.md` @ `sha256:63f9d57a3c6b5e12ea0ef5a30ac8d3009501edd243d89634bb86b4a498aec29b` — section 5.1, example (1c)

> becausesentence(2) contains the samewords and expressesthe sameideasas (Ic), yet (2) is much easierto understand: (2) John met the senator [S' who attacked the reporter [S' who disliked the editor]].
> --- `kb/sources/.snapshots/gibson-dependency-locality-theory.md` @ `sha256:63f9d57a3c6b5e12ea0ef5a30ac8d3009501edd243d89634bb86b4a498aec29b` — section 5.1, non-nested paraphrase (2)

> It should be emphasizedthat aspectsof the DLT have been oversimplified up to this point . Importantly , the structural integration cost function is not actually linear, so that a single long structural integration will never be as complex as multiple shorter integrations taking place at the sameprocessingstate.
> --- `kb/sources/.snapshots/gibson-dependency-locality-theory.md` @ `sha256:63f9d57a3c6b5e12ea0ef5a30ac8d3009501edd243d89634bb86b4a498aec29b` — section 5.3, oversimplifications

> In addition, the distancefunction assumedthus far increments its cost for new discourse referents alone. Processingother kinds of elementsalso probably causesmeasurableincrements in structural integration cost.
> --- `kb/sources/.snapshots/gibson-dependency-locality-theory.md` @ `sha256:63f9d57a3c6b5e12ea0ef5a30ac8d3009501edd243d89634bb86b4a498aec29b` — section 5.3, oversimplifications

## Connections Found

For the occasion, this source is the **comprehension-cost anchor** of the
dependency-locality batch: it supplies the mechanism by which distance costs a
human reader, while its siblings supply production evidence and scope. It
compares with [Temperley 2007](./temperley-2007-dependency-length-written-english.ingest.md)
on DLT's predictions tested in written corpora; Temperley confirms most of the
derived writer rules but finds one failure (fronted adjuncts run short before
long where DLT predicts long before short) and uses a different metric
(words and summed distance rather than new referents and peak). It compares
with [Futrell, Levy and Gibson](./futrell-levy-gibson-dependency-locality.ingest.md)
on cost as a cause of difficulty versus its imprint on word order across 53
languages, where antilocality and lossy-context surprisal are reviewed as
rivals. It compares with [Gibson et al. 2019](./gibson-2019-how-efficiency-shapes-language.ingest.md)
on scope: the same lead author later frames locality as one efficiency
pressure among several.

On the KB side, DLT is evidence for the "parsing load" named without a
mechanism in [Two rewrites exposed a syntax-or-repetition tradeoff](../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md);
that note's failed pass moved a temporal qualifier away from the definition it
limited and detached an appositive, which lengthens dependencies. The
evidence is bounded to human readers. It is likewise evidence for the human
half of [Human writing structures transfer to LLMs because failure modes overlap](../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md),
whose per-convention transfer test still lacks the LLM half. It compares with
[Human-LLM differences are load-bearing for knowledge system design](../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md)
as a quantified human-reader cost model of exactly the kind that note says must
be re-checked for agents. It compares with
[Local materialization should outperform distant natural-language declarations](../theory/local-materialization-should-outperform-distant-declarations.md)
on whether distance between a dependent and what governs it raises the cost of
correct use: DLT counts intervening new referents rather than raw words, which
is a human precedent for that note's separation of distance from intervening
competing content, though DLT works at sentence scale and is not LLM evidence.
It compares with [Soft-bound traditions as sources for context engineering strategies](../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md)
and [Skill and Working Memory](./skill-and-working-memory.ingest.md) on the
shape of a bounded processor's limit: DLT assumes one fixed pool with storage
and distance-dependent integration, while Chase and Ericsson show capacity
expanding with skill. Finally, it compares with
[Attention Is All You Need](./05-attention-is-all-you-need.ingest.md) on the
cost of linear distance: human integration cost grows with distance, whereas
attention gives a constant path length between positions, so the mechanism
does not carry over to transformer readers by construction.

## Extractable Value

1. **What the source establishes about distance and cost** -- for human
   readers, the cost of attaching a word to its head grows with the number of
   new discourse referents in between, and holding open predicted heads adds
   cost from the same pool. The evidence is ratings of center-embedded
   contrasts plus one small self-paced reading fit, in English and Japanese.
   Guidance should cite it as "a tested human comprehension model predicts
   higher cost for long and stacked dependencies", not as a measured cost
   function for ordinary technical prose. High reach for human readers; none
   established for LLM readers. [quick-win]
2. **Writer rules the mechanism directly supports** -- the chapter's contrasts
   license a short, falsifiable rule set for human-read prose:
   - do not nest a clause between a subject and its verb, and prefer a
     right-branching paraphrase (sentence 1c versus 2);
   - move a heavy constituent out of the span between a head and its
     dependent, as Japanese fronting does (3c versus 4);
   - attach modifiers where they do not interrupt a dependency (the nested
     prepositional phrase contrast);
   - prefer subject-extracted to object-extracted relative clauses;
   - avoid opening many predicted heads at once, such as long material before
     the main verb, because storage cost accumulates.
   Each rule names its DLT contrast, so it can be tested and dropped
   individually. [quick-win]
3. **Distance is counted in new referents, not words** -- intervening given
   material (pronouns, already-introduced terms) costs less than new entities.
   For KB prose this suggests that an unavoidable interruption should reuse
   established terms rather than introduce new ones, and that a word-count or
   sentence-length check is a crude proxy. Any lint check must choose between
   this metric and Temperley's word-count sum, because they can rank sentences
   differently. [experiment]
4. **Mechanism for the condition-adjacency rule** -- DLT gives the AGENTS.md
   rule "Keep necessary conditions next to their claims" a human-side
   rationale at sentence scale: a displaced qualifier is a long integration.
   It does not justify section-scale adjacency, which is a different
   mechanism. [quick-win]
5. **Peak cost, not average, drives difficulty** -- the theory predicts that
   several long integrations landing on one word (as at the verbs of nested
   clauses) cause breakdown, so rewriting effort should target the sentence's
   worst attachment point rather than overall length. [experiment]
6. **Storage-minimization tie-break** -- in footnote 9, Gibson proposes that
   when storage and integration costs conflict, the parser minimizes storage,
   because open predictions become later integration costs. This is a
   tentative ordering principle for writers choosing between two imperfect
   orders. [just-a-reference]

## Limitations (our opinion)

The central claim is bounded in five ways. First, all evidence concerns human
readers. Nothing here tests LLM comprehension, and transformer attention is not
distance-limited by construction (as the
[Attention Is All You Need ingest](./05-attention-is-all-you-need.ingest.md)
records), so any benefit of these rules for agent readers is a separate
conjecture that needs its own test, as
[Human-LLM differences are load-bearing](../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md)
requires. Second, the difficulty contrasts use extreme constructions (doubly
nested relative clauses) that rarely occur in KB prose. The chapter does not
establish effect sizes for the milder dependencies of ordinary technical
writing, and its reading-time fit uses about six regions per sentence with
marginal per-sentence significance. Third, the metric is admittedly
simplified. Gibson says the cost function is nonlinear, that elements other
than new referents probably add cost, and that the storage-integration
relation and storage indexing are undecided. Writer rules derived from the
exact EU counts would claim more precision than the source has. Fourth, the
rivals tested are older incomplete-dependency theories. Expectation-based
accounts, antilocality effects in verb-final languages, and semantic-similarity
interference (which footnote 3 concedes affects nested structures) remain
alternative explanations for some contrasts. An independent corpus test found
one failed DLT prediction
([Temperley 2007](./temperley-2007-dependency-length-written-english.ingest.md)).
Fifth, the chapter is a secondary summary; methods and full statistics are in
the primary papers. The pdftotext capture is also scrambled in the
ambiguity-resolution section and the conclusions, so this ingest relies on the
clean prose of sections 5.1 to 5.3.5 and does not establish the details of the
ambiguity-resolution claims (snapshot required).

## Recommended Next Action

Write a tentative theory note in `kb/theory/` claiming that keeping each
dependent near its head, measured in intervening new referents, lowers human
parse cost and that reordering can achieve this without the repetition cost of
splitting. Use this ingest as the mechanism, Temperley 2007 for the writer
rules and the failed fronted-adjunct case, and
[Two rewrites exposed a syntax-or-repetition tradeoff](../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md)
as the KB-local failure. State the LLM-reader benefit as an untested
conjecture with an explicit transfer test, before any rule enters the writing
instructions.

---

Relevant Notes:

- [The Dependency Locality Theory (PDF)](http://tedlab.mit.edu/tedlab_website/researchpapers/Gibson_2000_DLT.pdf) — derived-from: the analysed chapter
- [Two rewrites exposed a syntax-or-repetition tradeoff](../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) — is-evidence-for: DLT is a human-side mechanism for the parsing load the rewrites traded against repetition
- [Human writing structures transfer to LLMs because failure modes overlap](../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) — is-evidence-for: names the human failure that locality conventions prevent; LLM half untested
- [Human-LLM differences are load-bearing for knowledge system design](../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — compares-with: a quantified human-reader cost model that must be re-checked for agents
- [Local materialization should outperform distant natural-language declarations](../theory/local-materialization-should-outperform-distant-declarations.md) — compares-with: distance counted as intervening new content, at sentence rather than section scale
- [Soft-bound traditions as sources for context engineering strategies](../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) — compares-with: shape of a bounded processor's limit (storage plus distance-dependent integration)
- [Skill and Working Memory](./skill-and-working-memory.ingest.md) — compares-with: fixed resource pool versus learned capacity expansion
- [Temperley 2007](./temperley-2007-dependency-length-written-english.ingest.md) — compares-with: DLT's predictions tested on written corpora, with one failure and a different metric
- [Futrell, Levy and Gibson](./futrell-levy-gibson-dependency-locality.ingest.md) — compares-with: comprehension cost versus cross-linguistic word-order minimization and its rival motivations
- [Gibson et al. 2019](./gibson-2019-how-efficiency-shapes-language.ingest.md) — compares-with: locality as one efficiency pressure among several
- [Attention Is All You Need](./05-attention-is-all-you-need.ingest.md) — compares-with: human distance cost versus constant attention path length
- [Linguistic complexity: locality of syntactic dependencies](./gibson-1998-linguistic-complexity-locality.ingest.md) — compares-with: the predecessor model's distance-based storage cost and peak-load aggregate versus DLT's fixed storage cost
- [Minimizing syntactic dependency lengths](./temperley-gildea-2018-minimizing-dependency-lengths.ingest.md) — compares-with: the later review's small naturalistic effect, antilocality and predictability tradeoff against DLT's mechanism claim

---
description: "Why dependency-locality psycholinguistics licenses a few relation-preserving word-order heuristics for human-read English prose, but not a minimize-dependency-length rule justified by reading cost; LLM-reader benefit untested"
type: types/note.md
traits: [title-as-claim, synthesis, has-external-sources]
tags: [document-system]
---

# Dependency locality supports ordering heuristics, not a reading-cost rule

**Dependency length** is the distance between a syntactic head and a word that depends on it, such as a verb and its subject or a noun and its modifier. **Dependency locality** is the hypothesis that longer dependencies cost more to process, so language users prefer word orders that keep them short. The psycholinguistic evidence for this hypothesis supports writing guidance of one kind: a short list of construction-level ordering heuristics for English prose read by humans. It does not support a rule that tells a writer to minimize dependency length because shorter dependencies are cheaper to read.

Five properties of the evidence produce this gap. The broad evidence measures production, not reading. The direct reading evidence is narrow and partly contrary. No cost metric is settled. Locality is one pressure among several. The evidence varies only word order. Each property removes one premise that a reading-cost rule needs, and none removes the premises of the heuristics. All seven sources synthesized here study human language and human readers, so the heuristics' value for LLM readers is a separate, untested question.

## The broad evidence shows what producers do

The largest studies compare observed sentences with random reorderings of the same syntactic trees. In 37 languages, "all languages have average dependency lengths shorter than the random baseline, especially for longer sentences" ([Futrell, Mahowald and Gibson 2015](../sources/futrell-dependency-length-minimization.ingest.md), verbatim). In edited English, writers make the predicted choices: when a quotation verb is inverted, the subject is long ("Average length of subject NP: in S–V order, 2.16 words; in V–S order, 9.47 words"), and of two adjuncts after a verb, "the second adjunct tends to be significantly longer than the first" ([Temperley 2007](../sources/temperley-2007-dependency-length-written-english.ingest.md), verbatim).

This evidence records what writers and grammars produced. It does not measure what a reader pays. The corpus authors say so: "We do not take a position on the precise functional motivation for DLM" ([Futrell, Levy and Gibson 2020](../sources/futrell-levy-gibson-dependency-locality.ingest.md), verbatim). A later review leaves the cause open between production and comprehension pressure, and it names a confound for any reading advantage of a common order: "it would not be surprising if this ordering was easier to process, simply because it is more often encountered and therefore more expected" ([Temperley and Gildea 2018](../sources/temperley-gildea-2018-minimizing-dependency-lengths.ingest.md), verbatim). A frequent short-dependency order can therefore be easier to read because it is frequent, not because its dependencies are short.

## The direct reading evidence is narrow and partly contrary

Gibson's dependency locality theory (DLT) is the comprehension model behind the corpus work. Its clearest contrasts are extreme constructions. A doubly nested relative clause is unprocessable for most readers, while a non-nested sentence with the same words and ideas is much easier ([Gibson 2000](../sources/gibson-dependency-locality-theory.ingest.md)). Those constructions are rare in technical prose.

On ordinary text the effect is small. In a reading-time corpus of newspaper text, "the DLT was a significant though fairly small predictor of reading times" ([Temperley and Gildea 2018](../sources/temperley-gildea-2018-minimizing-dependency-lengths.ingest.md), verbatim). The same review reports antilocality: added material between an object and its verb should have slowed the verb, "However, the verb was read more quickly when the dative argument was included", which its authors attribute to the verb becoming more predictable (verbatim). The comprehension evidence therefore supports avoiding nesting and similar overload. It gives no effect size for the milder dependencies of technical writing. In one tested case added distance coincided with faster reading, although a second experiment in the same study found the expected locality effect.

## No cost metric is settled

A rule to minimize dependency length needs one quantity to minimize. The models disagree on it. DLT counts intervening new entities, not words: "1 EU is consumed for each new discourse referent in the intervening region", and pronouns already in the discourse cost less to cross. Gibson also states that "the structural integration cost function is not actually linear" ([Gibson 2000](../sources/gibson-dependency-locality-theory.ingest.md), verbatim). Its predecessor model judges a sentence by its worst point: "intuitive complexity is not determined by the average memory complexity over a sentence", and the cost of one held prediction "heads asymptotically toward a maximal complexity" ([Gibson 1998](../sources/gibson-1998-linguistic-complexity-locality.ingest.md), verbatim).

A summed word-count measure and a peak, entity-count measure can rank the same two sentences differently. Saturation also means that one long dependency is tolerable. Gibson generalizes that unacceptable structures hold "at least two long unresolved predicted categories" at once ([Gibson 1998](../sources/gibson-1998-linguistic-complexity-locality.ingest.md), verbatim), a generalization from intuitive judgments. A rule that flags every long dependency would therefore fire on sentences readers handle well.

## Locality is one pressure among several

Observed orders are not minimal. Observed lengths "are also longer than the minimal baselines", and the authors hold that "dependency length should not be fully minimized because of other factors and desiderata", such as letting a reader recover the structure word by word ([Futrell, Mahowald and Gibson 2015](../sources/futrell-dependency-length-minimization.ingest.md), verbatim). One competing pressure has been measured: "the observed languages are generally closer to some optimal frontier that trades off dependency length against average log probability" ([Temperley and Gildea 2018](../sources/temperley-gildea-2018-minimizing-dependency-lengths.ingest.md), verbatim).

Mechanical minimization also predicts one English order wrongly. For two adjuncts placed before the main clause, "The dependency-length view predicts a long-short ordering here, but this was not found" ([Temperley 2007](../sources/temperley-2007-dependency-length-written-english.ingest.md), verbatim); writers lean slightly, and not significantly, the other way. A rule derived from length arithmetic would recommend an order that skilled writers do not choose.

## The evidence varies only word order

The corpus baselines hold structure fixed: the random linearizations "all have the same underlying dependency structure as the original sentence, just with a potentially different linear order" ([Futrell, Mahowald and Gibson 2015](../sources/futrell-dependency-length-minimization.ingest.md), verbatim). The authors' correction names splitting ideas into multiple sentences as another way users might shorten dependencies, and scopes their result to order "given the dependency tree structures of the sentences they want to express" (verbatim). Because [an experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md), this evidence speaks to reordering within one structure, not to splitting or restating.

That boundary matters for KB prose. In [two rewrites of one note](./evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md), unguarded sentence splitting lost semantic relations, and guarded splitting kept them by adding 4.9% more words. Reordering is the third lever: it keeps every relation and adds no words. The sources show that writers use it. No source here tests whether it improves reading.

## The heuristics the evidence supports

Each heuristic names a construction that a writer can recognize without computing lengths. Temperley suggests that speakers acquire such strategies "as general habits, so that elaborate length calculations are not required on every occasion" ([Temperley 2007](../sources/temperley-2007-dependency-length-written-english.ingest.md), verbatim). He makes that suggestion about speech; applying it to writing is this note's transfer.

1. **After a verb or noun, put the shorter phrase first and the longer phrase or clause last.** Writers do this ([Temperley 2007](../sources/temperley-2007-dependency-length-written-english.ingest.md)), and in the comprehension model a structure "is easier to understand if the heavy phrase is ordered second" ([Gibson 1998](../sources/gibson-1998-linguistic-complexity-locality.ingest.md), verbatim). The direction is English-specific: dependency length minimization "predicts a long-before-short preference in head-final contexts" such as Japanese ([Futrell, Levy and Gibson 2020](../sources/futrell-levy-gibson-dependency-locality.ingest.md), verbatim).
2. **Keep a subject that precedes its verb short.** Writers put long subjects after an inverted quotation verb, and Temperley names the avoidance of long subjects as one such habit. Support is corpus evidence of writer choice only ([Temperley 2007](../sources/temperley-2007-dependency-length-written-english.ingest.md)).
3. **Do not nest a clause inside another clause before either verb arrives; use the non-nested paraphrase with the same words.** This has the strongest direct comprehension evidence ([Gibson 2000](../sources/gibson-dependency-locality-theory.ingest.md)).
4. **Do not hold two long unresolved dependencies open at once.** One long dependency alone is tolerable. Support is a model generalization from intuitive judgments ([Gibson 1998](../sources/gibson-1998-linguistic-complexity-locality.ingest.md)).
5. **When an interruption is unavoidable, fill it with given material rather than new entities.** DLT finds pronouns already in the discourse cheaper to cross ([Gibson 2000](../sources/gibson-dependency-locality-theory.ingest.md)). Extending this to terms the note has already introduced is this note's inference.
6. **For material placed before the main clause, apply no length-ordering rule.** The one tested prediction failed.

Heuristics 1 and 2 rest on what skilled writers do. Heuristics 3 to 5 have comprehension support, mostly from extreme constructions. No heuristic has been tested by rewriting technical prose and measuring how well readers understand it.

The rule to keep necessary conditions next to their claims has a sentence-scale instance here: a condition clause attached to a distant head is a long dependency. Beyond the sentence, the closest mechanism is information locality, under which words with high mutual information should be close. Its own authors frame its reach beyond syntax as a hypothesis: "Information locality might thus potentially explain word order phenomena that go beyond traditional dependency locality" ([Gibson et al. 2019](../sources/gibson-2019-how-efficiency-shapes-language.ingest.md), verbatim). It does not yet warrant the cross-sentence rule.

## LLM readers

The mechanisms these sources propose are human working-memory costs: storage of predicted heads and integration across intervening material. Since [human writing structures transfer to LLMs only where failure modes overlap](./human-writing-structures-transfer-to-llms-because-failure-modes.md), each heuristic needs evidence that LLM readers show the failure it prevents, such as misattaching a modifier across distance or nesting. These sources supply only the human half of that test. For [dual-audience documents](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md), the heuristics are warranted for human readers and remain candidates for agent readers.

## Scope

- The claim covers English prose at sentence scale. The ordering direction in heuristic 1 reverses for head-final languages.
- The heuristics are tendencies. Grammar, given-before-new order and other pressures can override them in a given sentence.
- Most of the cited work comes from the hypothesis's proponents, and two sources are reviews that relay primary studies.
- The claim would be refuted on its negative side by a controlled reading experiment on ordinary technical prose in which minimizing a stated dependency-length metric, beyond what the heuristics do, improves comprehension, with the gain surviving a change of metric. It would be refuted on its positive side by a rewrite test in which applying heuristics 1 to 5 lowers comprehension or meaning preservation for human readers.

## Open Questions

- Do LLM readers make more attachment or comprehension errors as dependency distance or nesting grows, holding content fixed?
- Does a reordering pass over a mature note preserve meaning better than the splitting passes in the two-rewrites experiment, and does it change word count?
- If a mechanical check is built, should it count words or new entities, and should it score the sum or the peak?

---

Relevant Notes:

- [An experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md) — grounds: the order-only baselines license claims about reordering a fixed structure, not about splitting or restating
- [Two rewrites exposed a syntax-or-repetition tradeoff](./evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) — evidenced-by: bounds the levers; splitting lost relations and restating added words, leaving reordering as the untested relation-preserving option
- [Human writing structures transfer to LLMs because failure modes overlap](./human-writing-structures-transfer-to-llms-because-failure-modes.md) — grounds: the per-convention transfer test that the LLM-reader half of each heuristic still needs
- [Human-LLM differences are load-bearing for knowledge system design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — grounds: the dual-audience premise that makes human-only warrant insufficient for KB writing rules
- [Local materialization should outperform distant natural-language declarations](./local-materialization-should-outperform-distant-declarations.md) — contrasts: a section-scale distance conjecture about LLM readers, where this note covers word-scale evidence about human readers
- [Large-scale evidence of dependency length minimization in 37 languages](../sources/futrell-dependency-length-minimization.ingest.md) — abstracted-from: cross-language corpus regularity, gap to optimum and order-only design
- [Dependency locality as an explanatory principle for word order](../sources/futrell-levy-gibson-dependency-locality.ingest.md) — abstracted-from: undecided functional motivation and head-direction dependence of short-before-long
- [Linguistic complexity: locality of syntactic dependencies](../sources/gibson-1998-linguistic-complexity-locality.ingest.md) — abstracted-from: peak load, saturation and the heaviness account
- [The dependency locality theory](../sources/gibson-dependency-locality-theory.ingest.md) — abstracted-from: entity-count metric, nesting contrasts and the stated nonlinearity
- [How efficiency shapes human language](../sources/gibson-2019-how-efficiency-shapes-language.ingest.md) — abstracted-from: information locality as a hypothesis beyond syntax
- [Minimization of dependency length in written English](../sources/temperley-2007-dependency-length-written-english.ingest.md) — abstracted-from: English writer choices, the failed fronted-adjunct prediction and the habit suggestion
- [Minimizing syntactic dependency lengths](../sources/temperley-gildea-2018-minimizing-dependency-lengths.ingest.md) — abstracted-from: small naturalistic effect, antilocality, the predictability tradeoff and the open cause

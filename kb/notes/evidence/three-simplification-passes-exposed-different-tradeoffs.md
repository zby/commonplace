---
description: "Evidence from three independent rewrites of one mature article: broad style guidance ranked best overall, a compact style cue improved rhythm but drifted, and exhaustive local review barely changed the text"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [document-system, evaluation]
---

# Three simplification passes exposed different clarity–precision tradeoffs

Three independent simplification passes over the same mature article produced three different results. Broad established-style guidance gave the best balance in one blind comparison, but made the article slightly longer. A compact Churchill-and-Zinsser cue produced the shortest and easiest first read, but weakened several technical relations. An exhaustive sentence-level pass preserved the baseline closely and exposed one conceptual ambiguity, but made only seven revisions.

This is evidence about how these instructions behaved on one article, not a general ranking. It suggests that editorial reach, compression, and auditable semantic restraint are distinct properties of a prose-revision procedure.

## Experiment

The target was the 1,991-word version then titled *Reflective self-improvement* at commit `7e21c9ae`, immediately before the first explicit simplification commit. Three fresh sub-agents received that exact baseline. Each saw only its assigned instruction and wrote a separate candidate; none saw the live article or another candidate.

| Treatment | Instruction shape | Result |
|---|---|---|
| Established style | [Broad style advice](../../instructions/simplify-prose-with-established-style-advice.md), with explicit semantic-preservation constraints and freedom to recast locally | 2,019 words (+28); clarified actors, causal sequences, and comparisons |
| Churchill and Zinsser | [Compact two-pass cue](../../instructions/edit-with-churchill-and-zinsser.md), followed by a general instruction to preserve claims and relations | 1,962 words (-29); strongest economy and rhythm, with several precision regressions |
| Sentence by sentence | [Exhaustive local review](../../instructions/simplify-prose-sentence-by-sentence.md), with stable unit identifiers, `keep` and `defer` decisions, and a coverage ledger | 1,992 words (+1); 139 keeps, seven revisions, and one conceptual defer across 147 units |

A fourth fresh agent then compared anonymized copies of the baseline and all three candidates. The hidden mapping was sentence pass `A`, baseline `B`, Churchill and Zinsser `C`, and established style `D`. The judge ranked them `D > C > A > B`: established style first overall, Churchill and Zinsser first for immediate clarity and rhythm, the sentence pass third, and the baseline fourth.

The judge identified `A` as the baseline with high confidence. This mistake is informative: the exhaustive pass stayed so close to the source that an independent reader could not distinguish it from the incumbent. The ranking itself remains one qualitative LLM judgment, not a reader-performance result.

The exact baseline, instruction snapshots, candidates, coverage ledger, hashes, anonymous mapping, and comparison result are preserved under `kb/reports/simplification-instruction-comparison-20260807/`.

## What differed

The established-style pass used its extra words to make relations more explicit. It separated the fixed evaluator from the optimizer's revision surface, preserved all three conditions in the indirect-feedback example, and stated the Gödel machine's proof obligation more directly. The blind judge considered this the best balance of clarity, coherence, and precision, although it left several baseline abstractions and unclear referents untouched.

The Churchill-and-Zinsser pass made broader, more economical changes. Several improved the article's progression, but others changed its content: it omitted *later* from one definition of compounding, made a conditional reinvestment path sound asserted, gave an acceptance metric the agency to accept a change, changed “provides evidence” to “shows,” and presented an intended context benefit as achieved. Its 29-word reduction therefore did not represent pure simplification.

The sentence pass changed only units for which it found a clear local improvement. It repaired an evidential relation, named ambiguous referents, replaced “the table asks” with “the table compares,” and deferred a possible conflation between behavioral authority and the map that represents it. Its coverage ledger made restraint visible, but exhaustive inspection did not supply the broader editorial judgment needed to simplify whole paragraphs or reorganize an explanation.

## Inference

The passes behaved as different instruments rather than stronger and weaker versions of one operation:

- A compact style cue licensed broad recasting and found substantial improvements, but its general preservation clause did not reliably protect technical relations.
- An exhaustive local procedure made semantic restraint auditable, but its one-unit-at-a-time scope selected against larger improvements.
- Broad style guidance with explicit invariants allowed more editorial judgment while keeping the main relations intact in this run, even when clarity required expansion rather than compression.

The result argues against judging a simplifier by word count alone. It also argues against treating complete sentence coverage as complete editorial review. A useful evaluation must separately inspect readability, semantic preservation, structural reach, and the cost of running and reviewing the pass.

## Limits

- One agent ran each instruction once on one mature technical article.
- One LLM supplied the anonymized four-way judgment. No human comprehension test or downstream agent task was run.
- The judge did not know the true baseline and misidentified it, so its semantic-faithfulness ordering cannot be read as a calibrated measurement.
- The experiment recorded final word counts and edit decisions, not runtime, token cost, or reviewer effort.
- The treatments differed in process as well as prose advice: only the sentence pass required an exhaustive ledger and an explicit defer decision.
- The comparison tested retrospective revision. It does not show how the same advice affects prose written from scratch.

---

Relevant Notes:

- [Two rewrites exposed a syntax-or-repetition tradeoff](./two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) — grounds: an earlier controlled rewrite shows why simplifying mature syntax can either lose semantic relations or restore them through added wording

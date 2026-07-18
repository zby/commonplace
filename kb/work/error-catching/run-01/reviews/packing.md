# Gate review: sentence/clause-packing

Criterion: kb/instructions/review-gates/sentence/clause-packing.md — sentences over ~40 words packing more than 2-3 independent concepts that could be split without losing meaning.

## packing-A
### Findings
- "The mechanism generalises beyond indexes to any authoritative artifact — specs, documentation, plans, curated lists — since any artifact that an agent treats as exhaustive will suppress fallback discovery when it goes stale, and although indexes are the clearest case because their purpose is explicitly navigational, a stale spec or an outdated architecture doc creates the same trap, where the agent reads it, trusts it, and stops looking for current information." — ~69 words, at least six clauses (generalisation, example list, mechanism, concession about indexes, spec/doc trap, agent-behavior chain). Splits cleanly into three sentences with no meaning loss.
## Result: FAIL

## packing-B
### Findings
- none — sentences stay well under the ~40-word threshold; longer ones carry at most two concepts.
## Result: PASS

## packing-C
### Findings
- "The output is reformatted repetition rather than processing, and this is the worst case because the quality gate passes confidently — the output is well-structured, grammatical, and topically relevant — yet for all that structure it just doesn't add anything, no matter how polished the formatting looks." — ~46 words, five clauses (repetition-not-processing, worst-case claim, gate-passes reason, surface-quality aside, doesn't-add-anything with trailing qualifier). Splittable without meaning loss; the trailing "no matter how polished..." restates the point the prior clause already makes.
## Result: WARN

## packing-D
### Findings
- "A natural language prompt admits a space of valid interpretations — 'write a summary' doesn't pick out a unique text — and on top of that underspecification, execution indeterminism means that even the same interpretation may render differently across runs, so the output you get is doubly unpinned before you ever decide to keep it." — ~54 words, four to five clauses (interpretation space, example, indeterminism, cross-run variation, "doubly unpinned" consequence). Splits into two or three sentences without losing meaning; the "doubly unpinned" consequence clause restates what the two prior clauses already establish.
## Result: WARN

## packing-E
### Findings
- "When an agent has no index for a topic, she falls back to search — and search accesses current content, so she might find what she needs — but when an index exists and is incomplete, the agent reads it, feels oriented, and stops looking before the missing notes ever surface." — ~50 words, five to six clauses (no-index case, search property, possible success, incomplete-index case, three-verb behavior chain, temporal qualifier). The contrastive halves are independent concepts and split cleanly into separate sentences without meaning loss.
## Result: WARN

## packing-F
### Findings
- none — the opening asymmetry and the generalisation paragraph are already split into short sentences; nothing exceeds the threshold with more than 2-3 concepts.
## Result: PASS

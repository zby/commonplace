---
description: "Curated head for the prose-readability tag — how prose is made easy for a reader to follow at sentence and paragraph level, and how it is edited for that without changing its claims; evidence from Commonplace rewrite runs"
type: types/tag-readme.md
complete: true
---

# Prose readability

This tag gathers claims about how prose is made easy for its reader to follow at sentence and paragraph level, and how prose is edited for that without changing its claims. The reader may be a human or an agent, and a note qualifies when it says which. An artifact qualifies when it substantively addresses what makes a passage easy or hard to follow, which editing moves preserve meaning, or which human readability conventions carry over to agent readers; mentioning readability as a benefit of something else is not enough. No single defining note anchors the tag; the operative rules are the quality bar in the root `AGENTS.md` and the prose and sentence review-gate lenses.

Readability is not brevity. The two rewrite evidence notes below record a compact editing cue losing technical relations while the pass judged best lengthened the text, so a model that reads this tag as an instruction to shorten will cut what the reader needed. Nearby but different: [document-system](./document-system-README.md) is the parent and covers how documents are typed, structured and checked, including writing conventions such as claim titles; [context-engineering](./context-engineering-README.md) covers what gets loaded into an agent's bounded context and what that reader already holds, where this tag covers how a text reads once it is in front of the reader.

## What makes prose easy to follow

- [Figurative wording can suggest relations that the target claim does not justify](../theory/figurative-wording-imports-source-domain-entailments-unless-mapped.md) — conditional inference risk, useful figures, mixed human framing evidence and an explicit LLM test
- [Opening position can signal a human reader's theme; proportion remains conjectural](../theory/position-and-proportion-set-what-a-reader-retains.md) — separates human theme identification and recall from LLM judgment, and gives the untested proportion mechanism a test

- [Dependency locality supports ordering heuristics, not a reading-cost rule](../theory/dependency-locality-supports-ordering-heuristics-not-a-reading-cost.md) — word order sets how much a human reader holds at once; six construction-level heuristics, no length metric, LLM benefit untested
- [Structured output is easier for humans to review](../theory/structured-output-is-easier-for-humans-to-review.md) — separating evidence from reasoning lets a reviewer check each without holding both
- [Human writing structures transfer to LLMs because failure modes overlap](../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) — the per-convention test for whether a human readability structure helps an agent reader
- [Design for the first-time human, except on access cost](../theory/design-for-the-first-time-human-except-on-access-cost.md) — write for the newcomer's reading unless the agent's access mode makes whole reads expensive

## Editing without changing claims

- [Two rewrites exposed a syntax-or-repetition tradeoff](../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) — evidence that unguarded sentence splitting drops relations the reader cannot regenerate; guarded splitting keeps them at a word cost
- [Three simplification passes exposed different clarity–precision tradeoffs](../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) — evidence that the shortest pass drifted and the best-ranked pass added words
- [Reverse compression is when LLM output expands without adding information](../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) — the opposite failure: fluent expansion that adds reading cost without extractable structure

## Procedures

Instructions carry no tags. The editing procedures that apply these claims are the [simplification passes](../instructions/simplification-passes/README.md), the [compression bundle](../instructions/compression-bundle/README.md), the [established-style simplification instruction](../instructions/simplify-prose-with-established-style-advice.md) and its [sentence-by-sentence](../instructions/simplify-prose-sentence-by-sentence.md) counterpart, and the prose and sentence review-gate lenses, for example [mannered prose](../instructions/review-gates/prose/mannered-prose.md) and [clause packing](../instructions/review-gates/sentence/clause-packing.md).

## Related Tags

- [document-system](./document-system-README.md) — parent: how documents are typed, structured, tested and retained; members here keep that tag
- [context-engineering](./context-engineering-README.md) — neighbour: what an agent reader has loaded and how it got there, where this tag covers how the text reads
- [evaluation](./evaluation-README.md) — neighbour: the rewrite evidence notes are also records of how edits were judged

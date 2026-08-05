---
description: "Use when simplifying all reader-facing prose in one Markdown file through a compact sentence-by-sentence pass without changing its meaning or structure"
type: kb/types/instruction.md
---

# Simplify prose sentence by sentence

Use this instruction to simplify the wording of a complete file without changing what it says or how it is organized. Change wording only when the improvement is clear. Keep wording that carries necessary precision, qualification, contrast, or voice. Invoke the instruction directly or call it from a larger writing or review workflow. Use a different instruction for structural or substantive revision.

## Scope

Process one complete Markdown file per invocation. Read the full file once for context, then work through it in source order, one paragraph, blockquote, list item, or table row at a time. Inspect every sentence. Also inspect reader-facing fragments that are not sentences, such as headings, captions, labels, and fragmentary table cells.

Skip frontmatter, code, formulas, link destinations, and generated blocks unless the caller includes them. Record every excluded region. Do not reorder sections or paragraphs, and do not edit more than one local block at a time.

## Process the file

1. As you reach each sentence, assign it the next stable identifier: `S001`, `S002`, and so on. Assign standalone reader-facing fragments `F001`, `F002`, and so on. Number units while processing them; do not build a separate inventory first.
2. Give each unit one decision. Use `keep` when no clear improvement is available; `revise`, `split`, `merge`, or `delete` for a local edit; and `defer` when the problem requires structural or substantive revision. A zero-change pass is valid.
3. Apply any edit before moving to the next unit. A `merge` may combine only adjacent units. Keep original identifiers stable after a revision, split, merge, or deletion.
4. After finishing a local block, re-read it with the preceding and following sentences. Check the edits together for repeated openings, subjects, verbs, or claim framing; unclear referents; lost transitions; and changed technical roles. Revert a weaker edit or mark the problem `defer`.

## Inspect each unit

1. Put the real actor, action, constraint, or result before abstract framing. Prefer “X can give the system more control” to “X's proposed advantage is control,” and “Each candidate must be judged against…” to “Each episode needs…” when these rewrites preserve the claim. Do not give a path, channel, artifact, evidence, or other abstraction agency unless it performs that causal role. Preserve uncertainty with an accurate modal or nearby qualifier.
2. Make an important relation between adjacent sentences explicit when the reader would otherwise have to infer it. Use the smallest accurate connective, such as *but* for contrast, *because* for cause, or *therefore* for consequence.
3. Remove helper verbs, repeated phrases, and clauses whose work a later concrete detail already does. If later behavior shows that a policy is used, for example, do not first say that the runtime loads it.
4. After an example, state what it establishes when the inferential step is not already clear. Connect the relevant concrete detail to the general claim instead of leaving the reader to infer why the example matters.
5. Prefer direct verbs, but do not replace a plain, precise phrase with stiffer wording merely to match a pattern. Compare every revision with the original for causal direction, uncertainty, conditions, scope, evidence strength, technical roles, and unit of analysis.

## Report

Return a compact coverage ledger containing one decision for every `S` and `F` identifier. Consecutive `keep` decisions may be collapsed into ranges such as `S001–S016 keep`; they need no individual anchors or reasons. List every other decision separately.

For each `revise`, `split`, `merge`, or `delete`, give the nearest heading, original wording, final wording, and a brief reason. For each `defer`, name the larger problem without solving it. End with decision counts, excluded regions, changed file paths, and validation results. Do not create a durable report unless the caller or containing workflow supplies a path.

## Verify

- Check that the coverage ledger has no missing sentence or fragment identifiers.
- Check that every changed unit is easier to understand, whether or not it is shorter.
- Check that no material claim, qualification, causal role, or useful voice changed.
- Re-read the complete revised file once for cumulative problems, but do not make an unlogged broad revision during this read.
- Run the artifact's validator.

---
description: "Use when simplifying the prose of one complete Markdown file through an exhaustive sentence-by-sentence pass without weakening its claims"
type: kb/types/instruction.md
---

# Simplify prose sentence by sentence

Use this instruction to simplify the wording of a complete file without changing what it says or how it is organized. Invoke it directly or call it as a focused step inside a larger writing or review workflow. Use a different instruction for structural or substantive revision.

## Scope

Process one complete Markdown file per invocation. Read the full file before editing, then inspect every sentence in source order. Change only one sentence, two adjacent sentences, or one paragraph at a time.

Include complete sentences in paragraphs, blockquotes, list items, and table cells. Record skipped non-prose regions, such as frontmatter, code, formulas, and generated blocks, once in the report. Do not silently omit sentences.

## Build the sentence ledger

Before editing, number every original sentence in source order as `S001`, `S002`, and so on. Identify each sentence by its nearest heading and a short opening anchor. Keep these identifiers stable when a sentence is revised, split, merged, or deleted.

Record one decision for every sentence:

- `keep` — no simplification would improve clarity without loss.
- `revise` — replace the sentence locally.
- `split` — replace one sentence with two or more.
- `merge` — combine it with an adjacent sentence; record every affected identifier.
- `delete` — remove a sentence whose work another sentence already does.
- `defer` — the problem requires substantive or larger-scale restructuring.

## Inspect each sentence

1. Look for places where the reader must decode an abstraction before seeing the mechanism. Put the actor, action, constraint, or result first. For example, prefer “X can give the system more control” to “X's proposed advantage is control,” or “Each candidate must be judged against…” to “Each episode needs…”. Preserve the original uncertainty with an accurate modal or nearby qualifier.
2. Make an important relation between adjacent sentences explicit when the reader would otherwise have to infer it. Use the smallest accurate connective, such as *but* for contrast, *because* for cause, or *therefore* for consequence.
3. Remove helper verbs, repeated phrases, and clauses whose work a later concrete detail already does. If later behavior shows that a policy is used, for example, do not first say that the runtime loads it.
4. After an example, state what it establishes when the inferential step is not already clear. Connect the relevant concrete detail to the general claim instead of leaving the reader to infer why the example matters.
5. Compare the revision with the original. Check its causal direction, uncertainty, conditions, scope, evidence strength, and unit of analysis. Keep or restore wording when the revision loses nuance or worsens the flow.

Work through the ledger in order. After finishing a paragraph, re-read that paragraph with its preceding and following sentences. If a local edit creates a need for broader restructuring, revert it or mark it `defer`.

## Report

Return the complete sentence ledger to the caller. Do not omit `keep` rows. Keep unchanged rows compact: include the identifier, section and opening anchor, decision, and a brief reason. For each `revise`, `split`, `merge`, or `delete` decision, also show the original and final wording. For each `defer` decision, name the larger problem without solving it.

End the report with decision counts, skipped non-prose regions, changed file paths, and validation results. Do not create a durable report file unless the caller or containing workflow supplies a report path.

## Verify

- Check that every original sentence has exactly one ledger decision.
- Check that every changed sentence is easier to understand, whether or not it is shorter.
- Check that no material claim or qualification changed.
- Re-read the complete revised file once for cumulative problems, but do not make an unlogged broad revision during this read.
- Run the artifact's validator.

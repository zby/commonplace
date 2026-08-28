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

1. As you reach each sentence, assign it the next stable identifier: `S001`, `S002`, and so on. Assign standalone reader-facing fragments `F001`, `F002`, and so on. A run-in label belongs to the sentence or fragment it introduces. Treat a grammatical sentence that spans Markdown blocks as one `S` unit; do not number its syntactic pieces again as fragments. Number a list item or table cell as `F` only when it stands independently rather than completing a surrounding sentence. Do not assign identifiers to excluded material. Number units while processing them; do not build a separate inventory first.
2. Give each unit one decision. Use `keep` when no clear improvement is available; `revise`, `split`, `merge`, or `delete` for a local edit; and `defer` when the problem requires structural or substantive revision. A zero-change pass is valid.
3. Apply any edit before moving to the next unit. A `merge` may combine only adjacent units. Keep original identifiers stable after a revision, split, merge, or deletion.
4. After finishing a local block, re-read it with the preceding and following sentences. Check the edits together for repeated openings, subjects, verbs, or claim framing; unclear referents; lost transitions; and changed technical roles. Revert a weaker edit or mark the problem `defer`.

## Inspect each unit

1. Put the real actor, action, constraint, or result before abstract framing. Prefer “X can give the system more control” to “X's proposed advantage is control,” and “Each candidate must be judged against…” to “Each episode needs…” when these rewrites preserve the claim. Do not give a path, channel, artifact, evidence, or other abstraction agency unless it performs that causal role. Preserve uncertainty with an accurate modal or nearby qualifier.
2. When clarity depends on deciding whether a phrase denotes a term, the concept it names, a source account, the current artifact's explication, or the object to which the concept applies, mark the unit `defer`; do not polish its existing frame. Name the possibly conflated roles in the report and route the artifact through the [conceptual-role conflation review gate](./review-gates/semantic/conceptual-role-conflation.md).
3. Make an important relation between adjacent sentences explicit when the reader would otherwise have to infer it. Use the smallest accurate connective, such as *but* for contrast, *because* for cause, or *therefore* for consequence.
4. Remove helper verbs, repeated phrases, and clauses whose work a later concrete detail already does. If later behavior shows that a policy is used, for example, do not first say that the runtime loads it.
5. After an example, state what it establishes when the inferential step is not already clear. Connect the relevant concrete detail to the general claim instead of leaving the reader to infer why the example matters.
6. Prefer direct verbs, but do not replace a plain, precise phrase with stiffer wording merely to match a pattern. Compare every revision with the original for causal direction, uncertainty, conditions, scope, evidence strength, technical roles, and unit of analysis.
7. Preserve formal relational wording — such as `is a function of`, quantifiers, invariants, equivalence claims, and `by construction` — unless the replacement states the same relation at least as explicitly. Do not trade a formal relation for looser causal prose merely to foreground an actor.

## Report

Keep a compact coverage ledger containing one decision for every `S` and `F` identifier while working. By default, report every non-`keep` decision and summarize the number of `keep` decisions. Include the full ledger or collapsed `keep` ranges only when the caller or containing workflow asks for auditable coverage.

For each `revise`, `split`, `merge`, or `delete`, give the nearest heading, original wording, final wording, and a brief reason. For each `defer`, name the exact author-owned choice or missing evidence, the affected units, the next procedure or recipient, and the condition for resuming; do not solve it in this pass. End with decision counts, excluded regions, changed file paths, and validation results. Do not create a durable report unless the caller or containing workflow supplies a path.

## Verify

- Check that the coverage ledger has no missing sentence or fragment identifiers.
- Check that every changed unit is easier to understand, whether or not it is shorter.
- Check that no material claim, qualification, causal role, or useful voice changed.
- Re-read the complete revised file once for cumulative problems, but do not make an unlogged broad revision during this read.
- Run the artifact's validator.

## Provenance

The sentence-level heuristics draw on Gopen and Swan's reader-expectation approach, Joseph Williams's character-and-action analysis, and Richard Lanham's Paramedic Method. Commonplace adds exhaustive sentence and fragment coverage, block-local editing, explicit semantic-invariant checks, and artifact validation for agent execution.

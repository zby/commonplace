---
description: "Use when running the blind EX/OP reclassification test that the mechanism direction review named as its reversal evidence, before maintainer adjudication of the explained-by/operates-through split"
type: kb/types/instruction.md
---

# Blind mechanism reclassification test

## Purpose

The [mechanism direction review](./mechanism-label-direction-review.md) recommends splitting the 128-row mechanism surface into `explained-by` (EX, 41 rows) and `operates-through` (OP, 72 rows), and pre-registered its own reversal criterion:

> Reverse the split if a blind second classification cannot distinguish "the target is the explanatory account" from "the target is the process/component through which the effect occurs" without source-specific prose.

That test has never been run. This instruction runs it. The outcome is the last evidence input before maintainer adjudication of the split; it decides nothing by itself and migrates nothing.

## Governing context (orchestrator only)

Read the [mechanism direction review](./mechanism-label-direction-review.md) (the ledger is the sample frame), [ADR 020](../../reference/adr/020-theoretical-default-contrasts-mechanism.md) ("by what operation?"), and the foundations workshop's [retrodiction run](../linking-foundations/generator-retrodiction-run.md) — specifically the A/B section's methodological lesson: **single-run classifications mislead; classify with k independent samples per row.**

Classifier subagents must NOT read any of these files, any workshop file, the link-vocabulary catalogue, or the collection contracts. Their entire input is defined below.

## Sample (deterministic, pre-registered)

From the review's exact disposition ledger, in the order the rows are listed there:

- **EX rows:** positions 1, 3, 5, … (every 2nd) → 21 rows.
- **OP rows:** positions 1, 5, 9, … (every 4th) → 18 rows.
- **EN rows:** all 10 (boundary probes — scored separately, see below).

49 rows total. Do not resample, substitute, or drop rows for convenience. Before classifying, verify each sampled row still exists at (or near) its recorded source line; a moved-but-present edge stays in the sample with its new line, a deleted edge is recorded as attrition and excluded from denominators. Report attrition.

## Classification protocol

**k = 3 fresh classifier subagents per row**, each in its own context. Bulk classification may run on a cheaper model than the orchestrating session (Sonnet is fine); record the models actually used. Each classifier receives, in its prompt or via a scratchpad file it alone reads:

1. The full text of the source artifact and the target artifact (or generous excerpts centered on the edge if an artifact is very long — include the footer line and its surrounding section either way).
2. The row under test: source path:line → target path. Do not reveal the origin label's history, the review's disposition, or that a prior review exists.
3. Exactly these class definitions, verbatim, and nothing more:

> - **EX** — the target is an explanatory account or general principle answering why or how the source claim/phenomenon occurs. Rejecting or revising the target prompts re-reading the source's causal argument, not automatically changing an implementation.
> - **OP** — the target is a process, component, control path, artifact, or operational rule through which the source effect is literally produced. A target change prompts an interface, behavior, or operational fit review.
> - **EN** — the target is a condition that must be available, true, or completed for the source claim/process to work, rather than the explanation or the operating path itself.
> - **OTHER** — none of the above fits; say what the relation is in one line.

Each classifier returns: one class, a one-line justification, and a confidence (low/medium/high). Classifiers must not see each other's answers.

## Scoring (orchestrator)

Per row: the k votes, the majority class (2/3 or better; no majority = UNSTABLE), and agreement with the review's disposition. Aggregate, with EX/OP rows and EN rows reported **separately**:

- inter-classifier stability: share of rows with a majority; share unanimous;
- majority-vs-review agreement on the 39 EX/OP rows;
- the confusion structure: how many disagreements are EX↔OP (the split-threatening kind) versus EX/OP↔EN or ↔OTHER (boundary kinds).

## Pre-registered decision reading

- **Split survives** if ≥90% of EX/OP rows have a stable majority AND the majority agrees with the review's EX/OP disposition on ≥80% of them AND EX↔OP confusion accounts for <15% of EX/OP rows.
- **Reversal evidence** (per the review's own criterion) if EX↔OP confusion is the dominant failure — report it plainly and recommend either one broad successor or redesigned boundary tests; do not soften the result.
- **EN rows count for the prerequisite boundary, not the split.** High disagreement or EX/OP votes on EN rows informs the pending `enables`/`precondition` review; it neither saves nor sinks the EX/OP split.
- Anything between the clean outcomes: report the numbers against the thresholds and stop; interpretation belongs to the maintainer.

## Output

Write `kb/work/linking-contract-consistency/blind-mechanism-reclassification-results.md` containing: the sampled row list with per-row votes, majority, review disposition, and match; the aggregate table; the confusion structure; attrition; models used (requested and actual, without inventing provenance); and a one-paragraph verdict phrased against the pre-registered thresholds. Validate the file, run `git diff --check`, and report changed paths.

Do not edit corpus edges, collection contracts, the catalogue, ADRs, durable instructions, or prior workshop results. The result feeds maintainer adjudication of the mechanism split; per standing practice, any subsequent migration needs its own approved plan.

---
description: Complexity review adapted for review-revise experiment. Reads baseline.md, writes output to run directory.
---

# Complexity Review (experiment)

**Target: kb/work/review-revise/baseline.md**

## What this is

A read-only review that asks: is this note more complex than its idea warrants? A note can have clean prose, correct content, and valid structure while still be inflated — too many sections, too many framings, too many connections for what is fundamentally a simple insight.

This is distinct from prose review (which catches representational failures) and semantic review (which catches content errors). Complexity review catches **the failure mode where a simple idea is presented as if it were a complex one**.

The underlying test: compression that preserves all non-obvious claims should be possible. If compressing the note to half its length loses nothing the reader needs, the note was over-complex.

## Prerequisites

Read the target note in full. Before running checks, write down in one sentence: **what is the core non-obvious claim?** This anchors all subsequent checks.

## Checks

### 1. Claim-to-section ratio

**Failure mode:** The note has more sections than distinct non-obvious claims. Sections restate the same insight in different framings rather than developing new ones.

**Test:** List the distinct non-obvious claims the note makes (not restatements, not background). Count them. Count the sections. If sections outnumber distinct claims, identify which sections are restating rather than extending.

### 2. Framework decoration

**Failure mode:** A table, taxonomy, or enumerated framework that doesn't add precision beyond what a paragraph of prose would convey. The structure looks rigorous but the content is the same with or without it.

**Test:** Read the table or taxonomy. Can you delete it and replace it with one sentence without losing information? If yes, it's decorative. Tables earn their space when they enable comparison across dimensions that prose would obscure.

### 3. Connection inflation

**Failure mode:** Relevant Notes entries that don't add navigational value — links to notes whose connection is obvious from the content, or links with relationship phrases that restate what the body already says.

**Test:** For each Relevant Notes entry, ask: would an agent reading this note be surprised to learn this connection exists? If the body already explains the relationship in full, the footer entry adds nothing.

### 4. Could-be-a-paragraph

**Failure mode:** The entire note, after removing background and connections, reduces to a single insight that could be expressed in one paragraph — but is presented as a multi-section analysis.

**Test:** Write the note's content as a single paragraph. If nothing is lost that a reader would miss, the note is over-complex. This is the strongest signal — it means the note doesn't need sections at all, just a claim and its justification.

## Output

Write the review to `kb/work/review-revise/run-01/complexity-review.md` using this format:

```
=== COMPLEXITY REVIEW: baseline.md ===

Core claim (one sentence): {the non-obvious claim}

Checks applied: 4

WARN:
- [{check-name}] {finding with specific evidence from the note}
  Recommendation: {what to change}

INFO:
- [{check-name}] {finding}

CLEAN:
- [{check-name}] {what was checked and why it held}

Overall: {CLEAN / {N} warnings, {M} info}
===
```

Report every check — WARN, INFO, or CLEAN.

## Do NOT

- Do not modify the target note. This is read-only analysis.
- Do not report prose quality, content correctness, or structural issues — those belong to other reviews.
- Do not penalize genuinely complex notes. A multi-part argument with independent evidence at each step earns its length.

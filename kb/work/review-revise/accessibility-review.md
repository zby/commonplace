---
description: Accessibility review — checks whether a note can be understood by a reader who has not read the rest of the KB. Catches undefined terms, opaque notation, unidentified references, and jargon that persists beyond its grounding point.
---

# Accessibility Review (experiment)

**Target: kb/work/review-revise/baseline.md**

## What this is

A read-only review that asks: could a reader who has not read the rest of this KB follow this note? The other reviews (semantic, prose, complexity) assume an insider audience. This one does not.

The target reader is someone technically competent who has not read the linked notes. They can follow an argument, but they should not need to click a link or know a prior convention to understand the sentence they are reading.

Report findings as WARN (likely blocks comprehension) or INFO (mildly opaque), never FAIL.

## Prerequisites

Read the target note in full. Note: this note originally lived at `kb/notes/session-history-should-not-be-the-default-next-context.md`. Do NOT read linked notes before running the checks — the point is to evaluate the note as a standalone artifact.

## Checks

### 1. Undefined terms

**Failure mode:** A technical term or concept is used as if the reader already knows it, with no inline definition or gloss.

**Test:** On first encounter of each technical term, ask: does the surrounding sentence define it, paraphrase it, or give enough context to infer its meaning? A link is not a definition — the reader should not have to follow a link to understand the sentence.

**Examples of failure:** "An execution boundary usually creates two different questions" (what is an execution boundary?). "Storage in K is cheap" (what is K?).

**Examples of passing:** "An execution boundary — any point where one LLM call ends and another begins — creates two distinct decisions" (inline gloss).

### 2. Notation opacity

**Failure mode:** Formal notation or variable names from another note are used in prose without being defined in this note. The reader must read the linked note to decode the sentence.

**Test:** For each piece of notation (`K`, `select(K)`, `P`, `||P||_t`, etc.), check: is it defined in this note, or does the sentence only make sense if you already know the notation from elsewhere? A brief gloss ("the scheduler's accumulated state `K`") suffices; a bare variable does not.

### 3. Unidentified references

**Failure mode:** A named system, tool, person, or organization is introduced without enough context for the reader to know what it is.

**Test:** For each proper noun (system name, product name, person name), check: does the note say what it is on first mention? "Slate is the main tension case" fails — the reader doesn't know what Slate is. "Random Labs' Slate agent system is the main tension case" passes.

### 4. Jargon persistence

**Failure mode:** A KB-internal term is defined or linked once (typically in the opening) but then reused throughout the body without context. By the third or fourth use, the reader has lost the grounding.

**Test:** Track KB-specific vocabulary through the note. If a term appears more than twice after its definition point, check whether later uses still make sense without scrolling back to the definition. Terms that have become common in the field (e.g., "context window," "prompt") are fine. Terms specific to this KB's framework (e.g., "bounded call," "select(K)," "clean model") need ongoing context or should be replaced with plain language after the first grounded use.

## Output

Write the review to `kb/work/review-revise/run-01/accessibility-review.md` using this format:

```
=== ACCESSIBILITY REVIEW: baseline.md ===

Checks applied: 4

WARN:
- [{check-name}] {finding with specific quote from the note}
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
- Do not read linked notes before running checks — evaluate standalone comprehension.
- Do not penalize standard technical vocabulary (LLM, context window, prompt, token, API).
- Do not penalize terms that are defined inline on first use.

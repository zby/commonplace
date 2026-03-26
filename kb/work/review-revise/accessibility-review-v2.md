---
description: "Accessibility review v2 — checks standalone readability. Key change from v1: recommends replacing notation with plain language, not just glossing it."
---

# Accessibility Review v2 (experiment)

**Target: kb/work/review-revise/baseline.md**

## What this is

A read-only review that asks: could a reader who has not read the rest of this KB follow this note? The other reviews (semantic, prose, complexity) assume an insider audience. This one does not.

The target reader is someone technically competent who has not read the linked notes. They can follow an argument, but they should not need to click a link or know a prior convention to understand the sentence they are reading.

Report findings as WARN (likely blocks comprehension) or INFO (mildly opaque), never FAIL.

## Prerequisites

Read the target note in full. Note: this note originally lived at `kb/notes/session-history-should-not-be-the-default-next-context.md`. Do NOT read linked notes before running checks — evaluate standalone comprehension.

## Checks

### 1. Undefined terms

**Failure mode:** A technical term or concept is used as if the reader already knows it, with no inline definition or gloss.

**Test:** On first encounter of each technical term, ask: does the surrounding sentence define it, paraphrase it, or give enough context to infer its meaning? A link is not a definition — the reader should not have to follow a link to understand the sentence.

### 2. Notation opacity

**Failure mode:** Formal notation or variable names from another note are used in prose. The reader must read the linked note to decode the sentence.

**Test:** For each piece of notation (`K`, `select(K)`, `P`, `||P||_t`, etc.), check: is it defined in this note, or does the sentence only make sense if you already know the notation from elsewhere?

**Recommendation principle:** Prefer replacing notation with plain language over glossing it. "The scheduler's accumulated state" is better than "the scheduler's accumulated state `K`" — the backtick notation adds nothing for a reader who doesn't know the source model, and it signals "you should already know this symbol." Only keep notation if the note uses it as a variable in a formal argument (equations, pseudocode). If notation appears only in prose sentences, replace it entirely.

### 3. Unidentified references

**Failure mode:** A named system, tool, person, or organization is introduced without enough context for the reader to know what it is.

**Test:** For each proper noun (system name, product name, person name), check: does the note say what it is on first mention? "Slate is the main tension case" fails. "Random Labs' Slate, an agent orchestration system, is the main tension case" passes.

**Important:** Only recommend identification if the information is stated in the note itself or its linked sources. Do NOT guess or fabricate attributions. If the note doesn't say who made a system, recommend that the author add the identification — do not supply it yourself.

### 4. Jargon persistence

**Failure mode:** A KB-internal term is defined or linked once but then reused throughout the body without context. By the third or fourth use, the reader has lost the grounding.

**Test:** Track KB-specific vocabulary through the note. If a term appears more than twice after its definition point, check whether later uses still make sense without scrolling back.

**Recommendation principle:** After grounding a term once in the opening, prefer plain language in the body. "The next call should see a representation chosen for its task" is better than "the next bounded call should see a representation chosen for its task" — "bounded" adds nothing once the concept is established. Reserve the full technical term for the opening definition and the Relevant Notes section.

## Output

Write the review to the run directory using this format:

```
=== ACCESSIBILITY REVIEW v2: baseline.md ===

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
- Do not fabricate identifications for named systems — recommend the author add them.

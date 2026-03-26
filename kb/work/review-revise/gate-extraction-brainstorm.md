# Brainstorm: Automatic gate extraction from manual edits

## The problem

The review-revise experiment revealed a bootstrapping gap. The existing review instructions (prose, semantic, complexity) are hand-authored bundles of checks, each bundling 4-8 checks into a single document. When the 3-review battery ran against the session-history baseline, it caught 2/16 changes. Adding two new reviews (accessibility, sentence-level) — also hand-authored — brought coverage to 9/16. But the process of discovering *what to check* was fully manual: a human edited a note, then a human reverse-engineered the edits into named checks.

The desired mechanism: show the agent a before/after, have it extract generalizable checks ("gates"), store them as reusable units, and load relevant subsets when reviewing future notes.

## What a gate is

A gate is a single quality check extracted from a concrete editing action but stated generally enough to apply to any note. The change catalogue already has the right shape:

```
Name: Parsing ambiguity — negation scope
Failure mode: "The mistake is not X" reads as "the mistake is [failing to X]"
Test: For each sentence with negation, check if the scope of "not" is ambiguous
Example (fail): "The mistake is not storing a trace"
Example (pass): "Storing a trace is fine — the mistake is letting..."
```

This is exactly what the review instructions already decompose into — each "### Check" section *is* a gate. The unit already exists. What's missing is:
1. A mechanism to extract new gates from edits
2. A flat storage that decouples gates from review bundles
3. A selection mechanism that loads manageable subsets

## Gate extraction: from diff to gate

Input: a before/after pair (two file versions, or a diff).

The agent's job:

1. **Segment the diff** into semantically distinct changes (a structural reorganization is one change even if it touches many lines; a word substitution is one change).
2. **For each change, identify the quality failure** in the before-text. Not "what was changed" but "what was wrong."
3. **Generalize**: state the failure mode as a pattern, not specific to this note. "Undefined KB-internal term used in body prose" not "the term 'bounded call' was used without definition."
4. **Check for overlap** with existing gates. If an existing gate already covers this failure mode, don't create a duplicate — but maybe refine the existing gate with a new example.
5. **Write the gate** as a standalone file.

### What makes extraction hard

- **Granularity**: The S3 change (compress trace taxonomy) involves editorial judgment about whether content earns its weight. That's hard to state as a testable gate. Contrast with A1 (define "execution boundary") which is crisp: "technical term used without inline definition." Some changes resist codification into gates.
- **Generalization quality**: A gate extracted from one edit may be too specific (fires only on notes about orchestration) or too general (fires on everything, producing noise).
- **Structural changes**: Section reordering (S5), section merging (S2), section folding (S4) are harder to express as local checks — they require whole-note reasoning. These may need a different kind of gate (structural gates vs. local gates).

### Possible gate types

| Type | Scope | Example | Extractable from diff? |
|------|-------|---------|----------------------|
| **Lexical** | Single phrase/sentence | Undefined term, ambiguous negation, stock LLM phrase | Easy — localized changes |
| **Semantic** | Paragraph | Misleading link text, wrong framing, confidence miscalibration | Medium — requires understanding the *why* |
| **Structural** | Whole note | Section should be merged, section ordering wrong, taxonomy too heavy | Hard — requires editorial judgment |
| **Cosmetic** | Surface | Capitalize bullets, fix link paths | Easy but low value — often `/validate`'s territory |

The experiment data supports this hierarchy: lexical and semantic gates had the best hit/stability rates (A1-A4, C1-C2 were stable across both runs). Structural gates (S1-S6) were the main source of misses and instability.

## Storage: flat directory of gate files

```
kb/instructions/gates/
  undefined-term.md
  notation-opacity.md
  unidentified-reference.md
  jargon-persistence.md
  parsing-ambiguity.md
  framing-mismatch.md
  stock-phrase.md
  misleading-link-text.md
  ...
```

Each gate file:

```yaml
---
name: Undefined term
description: Technical term used without inline definition or gloss — reader must follow a link or know KB context to understand the sentence.
type: lexical
tags: [accessibility, readability]
source: session-history edit 2026-03-25, change A1
hit_examples: 1
---

## Failure mode

A technical term or concept is used as if the reader already knows it. A link is not a definition — the reader should not have to follow a link to understand the sentence.

## Test

On first encounter of each technical term, ask: does the surrounding sentence define it, paraphrase it, or give enough context to infer its meaning?

## Example (fail)

"An execution boundary usually creates two different questions"

## Example (pass)

"An execution boundary — any point where one LLM call ends and another begins — creates two distinct decisions"
```

~20-30 lines per gate. Compact enough that you can load 8-12 gates into a review context without overwhelming the agent (~200-350 lines of instructions).

## Selection: which gates to load

This is the core design question. Loading all gates defeats the purpose (context overwhelm, same as bundled reviews). Loading too few misses problems. Several approaches, not mutually exclusive:

### Approach 1: Fixed budget, tagged selection

Load N gates per review pass (say 8-10). Select based on:
- **Note characteristics**: Does the note have notation? Load notation-opacity. Does it link to external sources? Load misleading-link-text, unbridged-cross-domain.
- **Gate tags**: Match gate tags against note tags/type.
- **Mandatory set**: Some gates are so universally applicable they always load (undefined-term, stock-phrase).

Pro: Simple, predictable. Con: Requires good tagging, may miss surprising gates.

### Approach 2: Two-phase triage

**Phase 1**: Load a compressed gate index — one line per gate (name + description). Ask the agent: "Given this note, which of these gates are likely relevant?" The agent returns a shortlist.

**Phase 2**: Load the full instructions for the shortlisted gates only.

Pro: Uses LLM judgment for selection, adapts to note content. Con: Extra LLM call, triage quality depends on description quality, may have false negatives at triage.

### Approach 3: Coverage rotation

Divide the gate pool into overlapping subsets. Each review pass uses a different subset. Over multiple passes, full coverage is achieved.

- Pass 1: gates 1-10
- Pass 2: gates 6-15
- Pass 3: gates 11-20

Pro: Eventually covers everything, no selection logic needed. Con: Slow, requires multiple passes, many misses per individual pass.

### Approach 4: Hit-rate weighted selection

Track which gates produce findings on which kinds of notes. Over time, build up associations:
- "undefined-term" fires often on notes with `status: seedling`
- "stock-phrase" fires often on notes generated/co-written with LLMs
- "misleading-link-text" fires often on notes with >5 links

Use these associations to weight selection. New gates get exploration budget (random inclusion).

Pro: Self-improving. Con: Needs history infrastructure, cold start problem, risk of overfitting to past patterns.

### Approach 5: Hierarchical — always/conditional/exploratory

Three tiers:
- **Always** (3-5 gates): Universal checks. Loaded every time. The highest-value, most-stable gates.
- **Conditional** (variable): Loaded when note characteristics match. E.g., notation-opacity loads only when the note contains backtick-delimited symbols.
- **Exploratory** (2-3 gates): Randomly sampled from the full pool. Ensures new or rare gates get exercised.

Budget: 3 always + 4 conditional + 3 exploratory = 10 gates per pass.

Pro: Balanced between reliability and discovery. Con: Tier assignment is itself a judgment call.

## The relationship to existing review instructions

The existing review documents (prose-review.md, semantic-review.md, etc.) are essentially pre-bundled gate sets with shared preamble. Two migration paths:

### Path A: Decompose existing reviews into gates

Break each review's checks into individual gate files. The review instruction becomes a lightweight dispatcher that loads its gate subset. The review type is now a *named gate collection*, not a monolith.

`prose-review.md` becomes: "Load gates: source-residue, pseudo-formalism, confidence-miscalibration, proportion-mismatch, orphan-references, unbridged-cross-domain, redundant-restatement, anthropomorphic-framing."

### Path B: Keep reviews, add gate layer alongside

The existing reviews stay as they are (they work; the experiment proved their stability). Gates are an additional, more granular layer. New checks discovered through editing go into the gate pool. Periodically, high-value gates get promoted into a formal review document.

Path B is safer for now — the existing reviews are validated and stable. Path A is the eventual target once the gate system proves itself.

## The extraction workflow

Concretely, how a human editing session becomes new gates:

1. Human edits a note (or reviews an agent's edit and makes corrections).
2. Human (or agent) runs: `/extract-gates baseline.md revised.md`
3. The agent diffs the two versions, segments into changes, and for each:
   a. Describes the quality failure in the before-text
   b. Searches `kb/instructions/gates/` for existing gates covering the same failure
   c. If no match: drafts a new gate file
   d. If match: proposes adding the new example to the existing gate
4. Human reviews the proposed gates, accepts/rejects/edits.
5. Accepted gates are written to `kb/instructions/gates/`.

This is supervised learning with human-in-the-loop: the edit is the training signal, the gate is the learned rule, the human approval prevents bad generalizations.

## Open questions

1. **How to test gate quality?** A gate extracted from one edit has N=1 evidence. When does it earn trust? Maybe: a gate must fire on at least 2 different notes before being promoted from "candidate" to "active."

2. **Gate decay**: Some gates may become irrelevant as writing practices improve (if nobody writes stock LLM phrases anymore, that gate is just noise). Should gates have expiry or demotion logic?

3. **Structural gates**: The experiment's biggest misses were structural (S1-S6). These resist local-check formulation. Are structural gates a separate mechanism (whole-note review with different prompting), or can they be expressed as local checks with a "zoom out" preamble?

4. **Interaction with revision**: The current workshop explores review → revise as a pipeline. If gates are the review mechanism, how does revision change? Does the reviser see the gate findings, or the full gate instructions? The run-01 data suggests the reviser benefits from specific findings more than general instructions (hit rate was higher when review findings were precise).

5. **Context budget arithmetic**: At ~25 lines per gate and a practical budget of ~300 instruction lines, the ceiling is ~12 gates per pass. Is that enough? The change catalogue has 16 items across 4 categories. Two passes of 10 gates each, with overlap, might be the practical operating point.

6. **Selection by note lifecycle stage**: Seedlings probably need different gates than mature notes. Accessibility gates matter more for notes approaching "evergreen"; structural gates matter more for freshly written seedlings that are still finding their shape. Should lifecycle stage influence gate selection?

7. **Relationship to the selector engine**: The selector engine (scripts/selector_engine.py) currently decides *whether* a note needs review. Gate selection decides *what checks* to apply. These are orthogonal but could be coordinated: the selector's change analysis (what changed in the note) could inform which gates to load (load gates relevant to the kind of change detected).

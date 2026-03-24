---
description: Frontmatter review — checks description discrimination, title composability, claim strength, and title-body alignment. Soft-oracle counterpart to the deterministic validate script; this checks whether metadata serves its retrieval and composability purposes.
---

# Frontmatter Review

**Target: $ARGUMENTS**

If target is empty, ask which note to review. If target is a name without path, search `kb/notes/` for a matching `.md` file.

## What this is

A read-only review that checks whether a note's metadata (description and title) serves its purpose — retrieval discrimination and composability. These are judgment checks that require LLM evaluation; the deterministic validate script (`validate_notes.py`) catches structural issues (missing fields, invalid enums, broken links) but cannot assess semantic quality. Report findings as WARN (likely real) or INFO (worth checking), never FAIL.

## Do NOT

- Do not modify the note. This is read-only analysis.
- Do not report structural issues (frontmatter parsing, link health, enum validity). The validate script covers those.
- Do not report content correctness issues. That's semantic review's job.
- Do not report prose quality issues. That's prose review's job.
- Do not review more than one note per invocation.

## Prerequisites

Read the target note in full.

Before writing the review, capture the note revision you are actually reviewing:

- `note-path`: the target note path (for example `kb/notes/backlinks.md`)
- `last-full-review-note-sha`: `git hash-object {note-path}`
- `last-full-review-note-commit`: `git log -1 --format=%H -- {note-path}` if the note is tracked
- `last-full-review-at`: current ISO 8601 time (for example `date -Iseconds`)
- `last-accepted-note-sha`: same as `last-full-review-note-sha` for a new full review
- `last-accepted-note-commit`: same as `last-full-review-note-commit` for a new full review
- `last-accepted-at`: same as `last-full-review-at` for a new full review
- `last-acceptance-kind`: `full-review`

## Checks

### 1. Description discrimination

**Failure mode:** The description restates the title or is so generic that it wouldn't help pick this note from a list of 5 search results.

**Test:** Read the title and the description. Ask: if an agent searched for this note's main concept and got 5 results, would this description help choose this one? Descriptions that paraphrase the title add zero retrieval value. Descriptions that merely summarize ("this note discusses X") are weak.

A good description adds what the title can't carry, in priority order:

1. **Mechanism** — how or why the claim works (strongest discriminator)
2. **Scope** — what boundaries or conditions the claim has
3. **Implication** — what follows from the claim in practice
4. **Context** — where the claim applies or what prompted it

Lead with mechanism or scope — these discriminate best. Within 200 chars you typically fit one or two of these.

**Examples:**

Bad (restates title — no discrimination value):
- Title: `approvals guard against llm mistakes not active attacks`
- Description: "The approval system protects against LLM errors rather than deliberate attacks"

Good (adds mechanism — reader immediately knows WHY):
- Title: `approvals guard against llm mistakes not active attacks`
- Description: "A determined attacker controls the prompt and can social-engineer approval; approvals catch the common case of tool misuse from hallucination or misunderstanding"

Good (adds scope — reader knows WHEN this applies):
- Title: `oracle strength spectrum`
- Description: "The bitter lesson boundary is a gradient, not a binary — oracle strength (how cheaply and reliably you can verify correctness) determines where on the spectrum a component sits"

### 2. Title composability

**Failure mode:** The title doesn't work as a linkable prose fragment — it can't be woven into a sentence in another note.

**Test:** Does `since [title]...` or `because [title]...` read naturally as a sentence fragment? A title that forces awkward grammar when linked hurts composability across the KB.

**Examples:**
- "knowledge management" — bare topic, doesn't compose: "since knowledge management" is incomplete, WARN
- "knowledge management requires curation not accumulation" — composes: "since knowledge management requires curation not accumulation, we designed...", PASS
- "context-loading-strategy" — descriptive name for a concrete artifact, PASS

### 3. Claim strength

**Failure mode:** The title is phrased as a claim but asserts something nobody would disagree with. A weak claim is worse than a topical title — it looks like it's saying something specific but carries no information. A topical title is at least honest about being a category label.

**Test:** Could someone knowledgeable reasonably argue the opposite? If the claim is a truism ("testing improves quality," "documentation helps understanding"), it fails. The fix is usually to sharpen the claim to the specific, non-obvious insight the note actually establishes — or to switch to a topical title if the note genuinely covers a topic rather than arguing a point.

**Examples:**
- "continuous learning is substrate-independent" — nobody would push back; the classification isn't revealing enough to contest, WARN
- "continuous learning can happen outside of weights" — names the thing people actually doubt, PASS
- "validation should be fast" — truism, WARN
- "deterministic validation should be a script" — specific, contestable (someone might argue LLM validation is better), PASS

**Exceptions:** Topical titles are correct for multi-claim specs and frameworks, definitional notes (term pinning), index pages, and exploratory/seedling notes where the ideas aren't firm enough to assert as claims. Check the note's `type` and `status` before flagging.

### 4. Title-body alignment

**Failure mode:** The title promises one thing but the body delivers another. This happens through drift — the note evolves during writing or editing but the title isn't updated to match, or the body gets extended beyond the title's scope.

**Test:** Read the title, then read the body. Ask: does the body actually support this title? Two common failure patterns:

- **Claim drift:** A claim title asserts X, but the body's actual argument establishes Y (a related but different point). The title should be updated to match what the body actually argues.
- **Scope drift:** A topical title names a narrow topic, but the body covers a broader area (or vice versa). The title and body should agree on scope.

If the title and body are misaligned, WARN. Include what the body actually establishes so the fix is clear.

## Output format

```
<!-- REVIEW-METADATA
note-path: {note-path}
last-full-review-note-sha: {git-blob-sha-for-the-note-content-you-reviewed}
last-full-review-note-commit: {last-commit-touching-note-if-available}
last-full-review-at: {iso-8601 timestamp}
last-accepted-note-sha: {same-git-blob-sha-for-a-full-review}
last-accepted-note-commit: {same-last-commit-touching-note-if-available}
last-accepted-at: {same-iso-8601 timestamp-for-a-full-review}
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: {note-filename} ===

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

Report every check — WARN, INFO, or CLEAN. Showing clean checks calibrates trust in the review.

The metadata block is operational state, not prose. The selector compares the current note against `last-accepted-note-sha`, while `last-full-review-*` preserves the note revision that actually received a full review.

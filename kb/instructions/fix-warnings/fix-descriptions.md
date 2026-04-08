---
description: Fix description warnings from /validate. Rewrites descriptions that are too long, multi-sentence, terminal-punctuated, or title-restating. Can be used standalone, in a sweep, or called by the fix-review-warnings agent when it encounters description issues.
---

# Fix Description Warnings

**Target: $ARGUMENTS**

If target is empty, ask which note to fix. If target is a name without path, search `kb/notes/` for a matching `.md` file.

## What this is

A focused editing pass that fixes description-field warnings from `/validate`. Descriptions are the most important frontmatter field — they're retrieval filters that help agents decide whether to load the full note. Getting them right requires reading the note, not just compressing the existing description.

## Prerequisites

1. Run `/validate {note-path}` or read a prior validate output to identify description warnings.
2. Read the target note in full — title, opening paragraphs, and conclusion at minimum.

## The rules

From `/validate`:
- **Length:** 50–200 characters
- **Single statement:** no sentence-ending punctuation mid-description
- **No terminal punctuation:** don't end with `.` `!` `?`
- **Discrimination:** must help pick THIS note over similar ones — not restate the title

## How to write a good description

The description answers "why THIS note?" not "what is this note about?" The title already states the claim; the description adds what the title can't carry.

**Priority order** (from the validate instruction):
1. **Mechanism** — how or why the claim works (strongest discriminator)
2. **Scope** — what domain or boundary the claim operates within
3. **Implication** — what follows from the claim, or what it enables

**Process:**
1. Read the title. It states the claim.
2. Read the note body. Identify what's distinctive — the mechanism, the key evidence, the architectural implication, or the contrast with related notes.
3. Write one phrase or clause (not a sentence) that captures the distinctive element.
4. Check: if an agent got 5 search results including this note, would the description help pick this one? If not, sharpen.

**Common failure modes:**
- **Summary creep:** trying to compress the whole note into 200 chars. Pick ONE discriminating element instead.
- **Title paraphrase:** "This note argues that [title restated]." Zero retrieval value — the title already says this.
- **Grammatical damage:** forcing two ideas into one clause with "and" or "but" that doesn't parse. If two ideas don't fit, pick the more discriminating one.
- **Hedging in the description:** descriptions are retrieval filters, not epistemic claims. "Context is the scarce resource" is fine in a description even if the note hedges the claim in the body.

## Procedure

1. Identify which validate warnings apply (too long, multi-sentence, terminal punctuation, title restatement).
2. Read the note to find the discriminating element.
3. Write the new description. Check length (aim for 100–180 chars as a sweet spot).
4. Verify against the rules.
5. Apply the edit.

## Sweep mode

To fix descriptions across many notes:

```bash
commonplace-validate-notes all 2>/dev/null | grep "description:"
```

This produces a list of all notes with description warnings. Process each note using the procedure above.

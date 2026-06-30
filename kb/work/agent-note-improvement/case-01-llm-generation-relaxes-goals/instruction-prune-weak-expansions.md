# Instruction: prune weak expansions

Use this instruction to review a note that is plausible but bloated. The goal is not to attack the central claim equally everywhere. The goal is to find the strongest retained point, then identify which parts make that point weaker.

## Task

Given a note, write an improvement report. Do not edit the note.

## Procedure

1. State the note's strongest load-bearing claim in one sentence.
2. List the sections or paragraphs that directly support that claim.
3. List the sections or paragraphs that are interesting but underbuilt, speculative, redundant, or only loosely connected.
4. For each weak expansion, decide one action:
   - **remove** — the material weakens the note and does not deserve preservation here;
   - **compress** — the idea is useful only as a qualifier, caveat, or open question;
   - **split** — the idea may deserve its own note because it has a distinct central claim;
   - **keep** — the material is necessary for the main note's argument.
5. Explain how the note would become harder to attack after those actions.

Prefer deletion or compression when the expansion is plausible but unsupported. Do not recommend adding qualifications merely because an opponent could object; additions must earn their space by strengthening the central claim.

## Output

Write a Markdown report with:

```markdown
# Prune Weak Expansions: <note title>

**Target:** <path>
**Strongest retained claim:** <one sentence>

## Core support
- <section/paragraph and why it supports the claim>

## Weak expansions
| Location | Problem | Action | Rationale |
|---|---|---|---|
| ... | ... | remove/compress/split/keep | ... |

## Proposed shape
<short outline of the note after pruning>

## Candidate splits
- <new note title or none> — <what claim it would carry and what evidence it needs>

## Net effect
<why this makes the note stronger>
```

---
gate_id: structural/general-before-specific
name: General before specific
lens: structural
watches: [body]
staleness: changed
---

## Failure mode

A section about a specific case, exception, or tension appears before the section that states the general pattern it exemplifies.

## Test

For each pair of adjacent sections, ask whether section N is a specific case and section N+1 states the general rule. If so, they should be reordered so the reader learns the rule before the exception. Report all such pairs, not just the first.

Signals that a section is more specific include case-study framing, proper nouns, or explicit tension wording.

**Tiebreaker:** If the specific section *qualifies* or *tensions* the general rule (counterexample, exception), specific-before-general is defensible — flag as INFO. If the specific section *exemplifies* the general rule (one instance of a pattern), general should come first — flag as WARN.

## Example (fail)

```markdown
## Tension: Slate's episodes sit between traces and artifacts
[specific system discussion]

## Execution-boundary compression is a recurring design move
[general pattern with multiple examples]
```

## Example (pass)

```markdown
## Execution-boundary compression is a recurring design move
[general pattern with multiple examples]

## Tension: Slate's episodes sit between traces and artifacts
[specific system discussion]
```

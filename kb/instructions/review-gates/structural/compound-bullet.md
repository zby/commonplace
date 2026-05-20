---
gate_id: structural/compound-bullet
name: Compound bullet
description: 'A bullet item packs two distinct ideas into one item, usually joined by a dash, semicolon, or `but`, so the second idea gets buried during scanning.'
type: kb/types/review-gate.md
lens: structural
watches: [body]
staleness: changed
---

## Failure mode

A bullet item packs two distinct ideas into one item, usually joined by a dash, semicolon, or `but`, so the second idea gets buried during scanning.

## Test

For each bullet item longer than about 30 words, ask whether it contains two independent claims that could stand as separate bullets without losing meaning.

Do not flag bullets that develop one idea with supporting detail. The signal is two separable points, not one point with elaboration.

## Example (fail)

```markdown
- move toward **artifact-first loading** once the caller's real consumption pattern is understood — but "artifact-first" does not mean "minimal"; a compressed episode that also serves memory and learning is still an artifact, not a transcript
```

## Example (pass)

```markdown
- Move toward **artifact-first loading** once the caller's real consumption pattern is understood
- "Artifact-first" does not mean "minimal" — a compressed episode that also serves memory and learning is still an artifact, not a transcript
```

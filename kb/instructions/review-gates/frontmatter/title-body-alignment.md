---
gate_id: frontmatter/title-body-alignment
name: Title-body alignment
description: 'The title promises one thing but the body now establishes something else because the note drifted during writing or later edits.'
type: kb/types/instruction.md
lens: frontmatter
watches: [title, body]
staleness: rewrite(0.5)
---

## Failure mode

The title promises one thing but the body now establishes something else because the note drifted during writing or later edits.

## Test

Read the title, then read the body. Ask whether the body actually supports the title's claim or scope.

Look for two common patterns:

- claim drift: the title asserts X but the body really establishes related claim Y
- scope drift: the title names a narrower or broader scope than the body actually covers

Report what the body now establishes so the title can be corrected precisely.

---
type: kb/types/instruction.md
description: Workshop review gate for checking broken link path during review-revise experiments
gate_id: structural/broken-link-path
name: Broken link path
lens: structural
watches: [body]
staleness: changed
---

## Failure mode

A relative markdown link target does not resolve to an existing file. Common causes: the target note was moved to a subdirectory, renamed, or deleted.

## Test

For each relative markdown link in the note, resolve the path from the note's directory and check whether the target file exists. Report any links whose targets are missing.

This check overlaps with `/validate`'s link-health check. The value of including it in review is that it catches broken links before they reach validation, and it can flag the likely cause rather than only the break.

## Example (fail)

```markdown
the shared move is [compression at the execution boundary](./distillation.md)
```

## Example (pass)

```markdown
the shared move is [compression at the execution boundary](./definitions/distillation.md)
```

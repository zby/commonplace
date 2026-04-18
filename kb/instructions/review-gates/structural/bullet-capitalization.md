---
gate_id: structural/bullet-capitalization
name: Bullet capitalization
description: 'Bullet items begin with lowercase prose where a normal sentence fragment should start with a capital letter.'
type: instruction
lens: structural
watches: [body]
staleness: changed
---

## Failure mode

Bullet items begin with lowercase prose where a normal sentence fragment should start with a capital letter.

## Test

Scan bullet lists and check whether the first word starts with a lowercase letter. Skip items that intentionally begin with code tokens, identifiers, or other deliberately lowercase forms.

## Example (fail)

```markdown
- the caller receives more than it needs
- local tactical debris survives beyond the stage where it mattered
```

## Example (pass)

```markdown
- The caller receives more than it needs
- Local tactical debris survives beyond the stage where it mattered
```

---
type: types/type-spec.md
name: vocabulary-ledger
description: "Compact lookup table that routes a vocabulary question to a record of competing uses or a proposed unification."
schema: ./vocabulary-ledger.schema.yaml
---

# Vocabulary ledger

Use this type for an index of active vocabulary collisions or candidate unifications. Each row links the term or terms to one record and gives the reader enough context to recognise the case.

A collision record gives the writing decision, its rationale and provenance, and the conditions for reconsideration. A unification record names the current definitions, proposed common account, distinctions still to test, current writing decision, and resolution test. Pending candidates leave the current definitions in force.

## Template

```markdown
---
type: types/vocabulary-ledger.md
description: "{What a reader can look up here}"
---

# Vocabulary {collision or unification} ledger

| Terms | Question |
|---|---|
| [terms](./{record-directory}/{record}.md) | {Uses to distinguish or common account to test} |
```

---
gate_id: frontmatter/title-as-claim
name: Title as claim
lens: frontmatter
watches: [title]
staleness: changed
requires_trait: title-as-claim
---

## Failure mode

The note carries the `title-as-claim` trait, but the title is not actually a proposition.

## Test

Ask whether the title states something that could be true or false.

Topic labels, category names, bare artifact names, and navigation headings fail this gate even if they are useful titles in other contexts. This gate only checks whether the title fulfills the promise made by the trait.

WARN when the title reads like a topic or label rather than an assertion. PASS when the title makes a concrete claim, even if the claim still needs refinement from other frontmatter or semantic gates.

## Example (fail)

- `knowledge management`
- `LACP`
- `learning theory index`

## Example (pass)

- `deterministic validation should be a script`
- `context efficiency is the central design concern in agent systems`

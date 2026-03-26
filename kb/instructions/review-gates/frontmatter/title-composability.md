---
gate_id: frontmatter/title-composability
name: Title composability
lens: frontmatter
watches: [title]
staleness: changed
---

## Failure mode

The title does not work as a linkable prose fragment inside other notes.

## Test

Read the title inside sentence frames such as `since [title]...` or `because [title]...`.

If the title forces awkward grammar and is not a concrete artifact name, it is not composable enough for KB linking.

## Example (fail)

- `knowledge management`

## Example (pass)

- `knowledge management requires curation not accumulation`
- `context-loading-strategy`

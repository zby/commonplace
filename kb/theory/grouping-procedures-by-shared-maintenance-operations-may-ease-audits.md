---
description: "Skeleton conjecture: whether persistent procedure groupings reduce audit effort beyond assembling the relevant set on demand remains untested."
type: types/note.md
traits: [title-as-claim]
tags: []
brief: grouping-procedures-by-shared-maintenance-operations-may-ease-audits.brief.md
---

# Grouping procedures by shared maintenance operations may ease audits

Conjecture: keeping procedures that need the same maintenance checks in a
persistent group may reduce audit effort compared with assembling that group
on demand.

## Concrete example

Commonplace groups reusable procedures such as writing and connection discovery
under `kb/instructions/`. A maintenance pass could inspect that group for
procedures that have drifted from their supporting theory or duplicate one
another. If those procedures were scattered among theory notes, the pass would
first have to distinguish executable procedures from explanations. This
illustrates the proposed saving; no comparison has measured it.

## Open Questions

- When does the saved selection effort outweigh maintaining the grouping?
- Does this add anything beyond [operation-relative grouping](./areas-exist-because-useful-operations-require-reading-notes-together.md) and [directory locality](./directory-placement-is-total-frontmatter-classification-is-partial.md)?

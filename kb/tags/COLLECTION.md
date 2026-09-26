---
participating: [notes, reference, instructions, agent-memory-systems, agentic-systems]
---

# Tag heads for kb/tags/

## Purpose and scope

One head per tag: `kb/tags/<tag>-README.md`, type
[`types/tag-readme.md`](../types/tag-readme.md). The filename names the tag
([ADR 089](../reference/adr/089-tags-are-one-namespace-per-kb-with-heads-in-kb-tags.md)).
A head introduces what the tag gathers, in the words a reader would search
for, names the defining note when the tag has one, and picks entries with a
phrase saying why each matters. It is the page a tag link leads to on the
published site, where the build appends the full member listing
([ADR 025](../reference/adr/025-complete-generated-indexes-are-build-time-only.md)).

Every tag in use has a head. Validation reports a tag on an artifact in a
participating collection whose head does not exist; write the head or drop the
tag. A tag not worth a head is not worth assigning. A head is not a note: it
makes no claim and is judged on whether a reader can tell from it what the tag
means and where to go next.

## Participating collections

The `participating:` list in this file's frontmatter names the collections
whose `tags:` lines are membership claims. Every `complete`
mark, the generated listing on the site, and the head requirement range over
exactly those collections, through one collector. Tags on artifacts elsewhere
(`work`, `sources`, `reports`, `types`, and the proposal archive under
`reference/proposals/archive/`) are not read. Nothing is inferred from the
directory tree: a collection joins the tag space by being listed here.

Within the participating collections, tags are carried by notes, by the
system analyses in `agent-memory-systems` and `agentic-systems`, and by
reference proposals. Instructions, ADRs, and the other reference pages route
through their own indexes and carry no tags; that is a rule, not a gap
(operator decision, 2026-09-26).

## Tag assignment

Before assigning a tag, read its head. Assign it only when the artifact
substantively addresses the head's stated subject, question, or mechanism;
mention or background use is insufficient. When the head leaves placement
ambiguous, clarify its inclusion condition before assigning the tag. An
artifact may carry neighboring tags when it meets each condition.

## Quality goal

A head is good when its opening lets a reader decide whether the tag is what
they are looking for and lets a writer justify or challenge an assignment.
State the inclusion condition and, where neighboring tags could be confused,
the boundary. The picks then let readers find the load-bearing entries
without the full listing. Keep heads small: the type warns past 8 KB
and fails past 16 KB. Prefer splitting a large tag into child tags, each with
its own head, over grouping inside one head.

## Marks

`complete: true` is a validated cache of membership, enforced or omitted: every
member is linked from the head or carries a tag whose head is linked from it,
so the head reaches every member in one hop ([ADR 090](../reference/adr/090-one-completeness-mark-reaches-members-in-one-hop.md)).
Children are the heads the body links; no list names them. Drop the mark
rather than force a weak child tag or a tag created to hold a few notes;
listing those members by hand also satisfies it. The [`tag-readme` type](../types/tag-readme.md) carries the
maintenance procedure; [`maintain-curated-indexes`](../instructions/maintain-curated-indexes.md)
carries the audit workflow.

## Outbound links

Link members by relative path (`../notes/<file>.md`) with a context phrase.
Link other heads under `## Related Tags` with a phrase saying how the tags
connect. Do not link into `kb/work/`. Heads carry no `tags:` of their own.

## Type eligibility

Heads use the global `types/tag-readme.md`. `README.md` is this collection's
landing and carries no type. No other artifact belongs here.

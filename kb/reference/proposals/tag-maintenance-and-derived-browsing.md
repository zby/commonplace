---
description: "Proposal: test temporary topic groupings and reviewed tag-maintenance suggestions before changing Commonplace’s canonical tag structure."
type: ../types/design-proposal.md
tags: [kb-maintenance, context-engineering]
traits: [has-external-sources]
---

# Tag maintenance and derived browsing

Commonplace could make large tags easier to browse and maintain by generating
temporary topic groupings, then letting maintainers promote useful groupings
into deliberate tag changes. The candidate priority is to test that view before
adopting a deeper hierarchy or automatic membership assignment. This proposal
records an option space and an evaluation target; it adopts no new behavior.

## Current state (as of 2026-09-22)

Commonplace already has curated tag introductions, selective links with context
phrases, and complete generated listings for published pages. Agents use
curated heads and scoped queries. The [navigation contract](../navigation.md)
keeps generated inventories off the default agent read path.

The [tag-readme contract](../../types/tag-readme.md) supplies checked
completeness and coverage marks. Splitting a tag keeps the parent tag on child
members. The current collector groups explicitly assigned strings within a
collection; it excludes tag-head artifacts from ordinary membership.
`collect_collection_tag_index` in `src/commonplace/lib/index_generated.py` and
`validate_tag_readme` in `src/commonplace/lib/validation.py` are the inspected
implementation surfaces.

The [semantic-contract proposal](./semantic-contract-for-tags-and-tag-heads.md)
and [tag-scope proposal](./tag-scope-is-declared-where-membership-claims-are-made.md)
already own tag meaning, head identity, membership scope, and resolver changes.
This proposal adds browsing and maintenance options without choosing those
contracts. Any trial must state the existing collection scope it actually uses.

## External design and evidence boundary

[Gwern’s design article (snapshot required)](../../sources/gwern-design-of-this-website.ingest.md)
describes URL-based annotations, hierarchical tag paths, tag pages with
introductions, non-recursive tag cross-references, and lazy previews. A tag can
also supply an automatically updated bibliography inside another page. Its
future-work discussion proposes classifier-assisted assignment, splitting large
tags, and finding members for sparse tags. Footnote 21 distinguishes an untagged
item from one explicitly judged not to belong.

The inspected implementation goes further than the future-work heading might
suggest. At commit `de5a6016ef3d9359b9214747a2e0b684ab7c2c81`, the
[directory generator](https://github.com/gwern/gwern.net/blob/de5a6016ef3d9359b9214747a2e0b684ab7c2c81/build/app/generateDirectory.hs#L139)
invokes semantic ordering for sufficiently large ordinary tags and renders a
separate “Sort By Magic” view. The
[grouping implementation](https://github.com/gwern/gwern.net/blob/de5a6016ef3d9359b9214747a2e0b684ab7c2c81/build/GenerateSimilar.hs#L1204)
orders entries, splits the sequence at large adjacent distances, and obtains
cached labels through a
[title-based label generator](https://github.com/gwern/gwern.net/blob/de5a6016ef3d9359b9214747a2e0b684ab7c2c81/build/tagguesser.py).
These are browsing groups; this path does not establish an automatic rewrite of
canonical memberships. The article’s broader interactive maintenance workflow
must not be reported as implemented on this evidence.

The public source files were read on 2026-09-22 and their Git blob hashes matched
the named commit. No Gwern build, model call, or usability test was run. The
source establishes a concrete implementation option, not its benefit for
Commonplace agents.

## Forces and incompatible assumptions

- Browsing improvements should preserve exact membership and the inexpensive
  fallback query. A generated group must not acquire a completeness promise
  that only the whole tag can support.
- Grouping by topic may help exploration but obscure a task that needs date
  order, a known title, or an authored argumentative sequence. Multiple views
  remain an option.
- Gwern’s filesystem-derived hierarchy does not map directly to Commonplace,
  where directories primarily encode collection contracts. Moving notes to
  express topics would conflate those two purposes.
- Gwern’s [tag normalization](https://github.com/gwern/gwern.net/blob/de5a6016ef3d9359b9214747a2e0b684ab7c2c81/build/Tags.hs#L108)
  removes a parent when a more specific path is present. Copying that rule
  would conflict with Commonplace’s explicit parent-membership split rule.
- Gwern permits tag pages to carry tags as cross-references. Commonplace’s
  proposed semantics separate tag heads from ordinary members. A related-topic
  link need not become a subtype or membership assertion.
- Embedding and model infrastructure has an ongoing cost. A useful grouping
  may be obtainable by an agent reading titles and descriptions, without a
  persistent embedding service.

## Options and their consumers

| Option | What would consume it and with what force | Main choice or limit |
|---|---|---|
| Keep current curated heads and scoped queries | Existing readers follow authored routes; current validation checks marks | Baseline with no additional machinery; maintenance remains manual or agent-assisted through existing procedures. |
| Temporary grouped view of one tag | A maintainer or reader inspects generated groups and opens selected members; groups advise navigation only | Candidate first trial. Compare an agent-produced grouping with the existing head and title/description listing before deciding whether embeddings are needed. A product view or command does not yet exist. |
| Suggested additions, removals, splits, and merges | A maintenance worker proposes a reviewable change; an accepted edit changes canonical tags and reruns existing membership checks | Candidate next step if browsing groups expose useful repeated edits. Semantic acceptance needs editorial judgment; structural checks cannot establish that an item belongs. |
| Remember rejected suggestions | A suggestion producer suppresses or revisits previously judged item–tag pairs | Consider only after repeated false suggestions are observed. Absence must remain distinct from rejection; changed note content or tag meaning must permit reconsideration. No consumer exists yet. |
| Aliases and readable tag labels | Authoring tools resolve input names; readers see a compact label while canonical identity stays inspectable | Useful if vocabulary lookup causes observed friction. Ambiguous input needs an explicit resolution policy; fuzzy matching is not evidence of semantic identity. |
| Reusable generated tag views inside pages | The documentation build derives a bibliography or related-material section from canonical membership | Useful where the same membership is now maintained twice. Keep editorial role phrases authored, and keep bulk generated output out of committed agent-facing files. |

The distinctions above rest on [index completeness not determining editorial
orientation](../../notes/index-completeness-does-not-determine-editorial-orientation.md).
Generated labels are candidate interpretations, not a semantic oracle. A model
agreeing with its own grouping supplies no independent warrant for the grouping.
The consumer split follows [access-path cost](../../notes/design-for-the-first-time-human-except-on-access-cost.md):
a browser preview and an agent’s bounded result can expose the same members
without requiring the same interface.

## Candidate selection and adoption criteria

Prefer a bounded comparison on one tag with a concrete browsing or maintenance
problem. Give it both the existing curated/query view and a temporary grouped
view. Keep canonical membership fixed during the comparison. Use real tasks:
find a known relevant item, identify useful readings for a question, and propose
a justified split. Include relevant items outside the tag when judging the
question-answering task; membership recall alone cannot establish task recall.

Before adoption, the grouped view must demonstrate a useful reduction in
reader effort or maintenance effort without hiding relevant members. Record
which items were missed, what material was loaded, and what corrections were
needed. The maintainer must judge whether the groups answer the stated tasks;
that judgment is bounded to those tasks and that corpus. Structural validation
must independently confirm that grouping preserves the exact input set.

If the view only looks coherent but does not improve those tasks, retain the
baseline. If it helps, decide whether it belongs in a maintenance report, an
agent query, the published site, or several surfaces. Only demonstrated repeated
use would justify a permanent command, an embedding dependency, or a retained
rejection store. Canonical taxonomy changes remain separate editorial decisions
and must reconcile with the two existing tag proposals.

## Remaining choices

The first trial still needs a tag and a concrete operator task. Other free
choices are the grouping method, whether groupings are task-conditioned, how
ambiguous aliases are handled, and what would invalidate a rejected suggestion.
None requires choosing new fields, a schema, a clustering threshold, or a
repository-wide migration now.

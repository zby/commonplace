---
description: "Separates the curated introduction to a tag from exact enumeration; a head no longer authorizes readers to skip a search or obliges authors to cover every member."
type: reference/types/adr.md
tags: []
status: accepted
---

# 140-Tag heads are selective

**Status:** accepted
**Date:** 2026-11-23
**Supersedes:** [ADR 090](./090-one-completeness-mark-reaches-members-in-one-hop.md). Amends the completeness rules of [ADR 026](./026-tag-readme-type-with-completeness-and-coverage-marks.md) and [ADR 089](./089-tags-are-one-namespace-per-kb-with-heads-in-kb-tags.md).

## Context

A tag head introduces a topic and recommends where to start. ADR 090 also let it promise that its links reached every member, directly or through a linked head. That promise gave an agent a reason to skip a membership lookup. In the operator's experience agents checked membership anyway. Maintaining links when membership changed therefore imposed work without reliably saving a search. The membership collector already answers the exact question without relying on editorial picks.

## Decision

A tag head is selective. It states what qualifies for the tag and recommends useful reading. Its links make no coverage claim, even when they happen to include every member. The tag-readme schema rejects `complete` for either boolean value. There is no replacement field. Readers who need every member use the collector or the published listing; connection discovery does not stop at a head.

## Considered alternatives

Keeping the optional one-hop mark would preserve a machine-checked shortcut. A historical case showed the check catching an omission, but that does not show readers rely on the shortcut now. Keeping the mark for individual collections would still require maintaining coverage alongside curation without an identified reader who would skip the lookup. A `selective` field would repeat the same rule on every head.

## Consequences

Authors choose links for their value to readers, not to satisfy a coverage test. Validating a tagged note still checks whether its tags have heads; it no longer revalidates a head because the note might have invalidated its coverage. Head identity, link health and size remain checked. Existing projects remove the retired field from their heads; rerunning init does not rewrite project-owned contracts.

This decision changes neither which collections participate in membership nor how generated lists are grouped. A text search for useful reading need not use the same scope as an exact membership query.

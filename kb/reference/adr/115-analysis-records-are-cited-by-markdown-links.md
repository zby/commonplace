---
description: "Analysis records are cited by Markdown links to the declaring member's heading anchor; a bare record ID is literal text, so code resolves each citation by destination instead of scanning prose for ID tokens"
type: reference/types/adr.md
status: accepted
---

# 115 — Analysis records are cited by Markdown links

**Status:** accepted
**Date:** 2026-10-09
**Amends:** [ADR 104](./104-name-analysis-records-with-stable-short-handles.md): record names stay; written grouping prose and token scanning are retired. [ADR 096](./096-analysis-passes-declare-their-own-records-under-lens-prefixes.md): declaration prefixes stay; the prefix still names the declaring analyst.

## Context

An analysis member cited a record by writing its ID in prose. Validation
had to decide which tokens were citations. It scanned every
record-shaped token outside quotations and code, then matched each against
the declarations in the members the role may cite. Three rules existed only
to keep that scan sound: a refusal of declared names where one was a token
prefix of another, a refusal of declaration headings missing their prefix,
and close-match suggestions for unresolved tokens. Grouping prose such as
`RT-OBJ-a through RT-OBJ-c` needed a stated rule that only the written
endpoints resolve. A mention of a record that the author
did not mean as a citation still had to resolve.

The citing text also did not say where the record lives. A reader followed
an ID by searching the set, and the rendered pages had no link to follow.

## Decision

A record declaration is a level-four heading that is exactly the record ID,
`#### RT-OBJ-store`. Its label moves to the first line of the body,
`Label: Short label`. Python-Markdown's default heading slug gives the
stable anchor, the lowercase ID (`#rt-obj-store`).

A record citation is a Markdown link whose text is the full ID and whose
destination is the declaring member and that anchor:
`[RT-OBJ-store](runtime.md#rt-obj-store)`, or `[RT-OBJ-store](#rt-obj-store)`
inside the declaring member. Validation resolves each citation by its
destination. The destination must be a member the citing role's layout
`cites`, the member must declare the record exactly once, and the link text
must be the ID the anchor addresses. A bare record ID is literal text and is
not checked. Links inside quotations, fenced excerpts and inline code are
excluded. Links that are not record citations stay ordinary links.

Structured fields use the same form. An annotation heading is
`#### On [ID](member.md#anchor)`. `Part of:` and `Amendment:` carry
record citations. A memory profile's `records` lists hold the link
destination, `memory.md#mem-rte-update-path`, and the comparison matrix
resolves each entry against the member it names.

`SRC-*` sources stay bare IDs resolved against the Source register within
the citing role's scope. They live in one table, so a link would add a
destination without adding information, and their range refusal stays.

## Consequences

- The token-prefix collision check, unprefixed-declaration check and
  close-match suggestions are removed. Grouping prose needs no rule: its
  bare IDs are literal, and a writer who means a citation links each record.
  Identity checks stay: declaration prefixes, unique declarations,
  annotation and `Part of:` targets, supersession form and the predecessor's
  declared IDs.
- A rendered member links each citation to its declaration.
- Analysts write the declaring member in every citation. The prefix
  already names it, so the cost is the link syntax, not a new fact.
- The retained-archive Dynamic Cheatsheet set keeps its bare-ID grammar as
  frozen history. It already failed the current contract on earlier
  changes, and nothing validates it as current. Revision-1 profiles keep
  bare-ID `records` lists under the existing BACKCOMPAT branch.
- An analysis run started before this change has members in the old
  grammar and fails validation on resume; it must restart.

## Alternatives

- **A raw HTML anchor before a labelled heading**, `<a id="rt-obj-store"></a>`,
  would keep the label in the heading. It adds markup the writer must keep
  in step with the heading, and Python-Markdown already provides the slug.
  Rejected.
- **The `attr_list` extension** (`#### RT-OBJ-store — Label {#rt-obj-store}`)
  would also keep the label, but the site build does not enable it and the
  anchor would again be written twice.
- **Keeping bare-ID citations** keeps the scan and its three special rules.

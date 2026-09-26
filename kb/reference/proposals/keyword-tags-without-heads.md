---
description: "Proposal: a second, weaker kind of tag — a keyword with no head, no page, and no marks, for scoped search only — declared per collection; set aside by ADR 089 on YAGNI grounds until search-only tagging shows a need"
type: reference/types/design-proposal.md
tags: [kb-maintenance, curation]
---

# Keyword tags without heads

A tag today is a membership claim: the artifact belongs to a topic that has a head, a page on the published site, and possibly marks that a validator checks. Some tagging wants less than that. A workshop file may carry a provisional label before anyone knows whether the topic is worth a head; a survey collection may want a facet that is only ever used in scoped search. This proposal records the option of a second kind of tag for those uses, and why it was set aside.

## Current state (as of 2026-09-25)

[ADR 089](../adr/089-tags-are-one-namespace-per-kb-with-heads-in-kb-tags.md) decides that every tag in use within the KB's tag space has a head, that membership ranges over one fixed set of participating collections, and that no consumer reads tags outside that set. It records this proposal's idea under its considered alternatives and rejects it for now on YAGNI grounds: the headless tags that prompted it were mistakes under the existing rules, and were given heads or retagged in the same change rather than legalized by a new mechanism. `kb/work/` and `kb/sources/` artifacts may carry `tags:` lines; nothing reads them, so they are neither keywords nor memberships but inert text.

## Problem

Under the one-mechanism rule, assigning a tag costs a head, or the assignment is refused. That is right for a topic. It is heavy for three recurring cases:

- **Provisional vocabulary.** A workshop groups its files with a label it may never promote. Today that label is inert; if it were read, it would demand a head for a topic that may not exist.
- **Search facets.** A collection wants a label that only ever narrows a scoped `rg`, such as a mechanism family across a hundred system reviews. A head adds a page nobody reads and a maintenance obligation.
- **Host projects starting out.** A host that adopts tags has no heads and may want to label before it curates.

## Option space

- **Keywords by absence of a head.** A tag with no head in `kb/tags/` is a keyword: searchable and listed in generated tails, but with no page and no marks. Nothing is declared. Its cost is that the kind of a tag changes when someone writes or deletes a head, and a reader of a `tags:` line cannot tell which kind they are looking at.
- **Keywords by collection declaration.** Each collection's contract states whether its tags are memberships or keywords, beside its linking rules, with one machine-read field the collector consumes. Its cost is that the same string means different things depending on where it is read, and every consumer carries the distinction. This is the form ADR 089 rejected.
- **A separate field.** `keywords:` beside `tags:`, so the two kinds never share a field. Its cost is a second frontmatter field on every type and a second scan recipe; its benefit is that a reader always knows which kind they see.
- **No keywords; provisional labels live elsewhere.** A workshop groups files by directory; a survey facet is a typed field on the review, as the agent-memory-system review type already does for lineage. This is the current state.

## Forces

- One mechanism is easier to explain, validate, and read. Two kinds of tag in one field is the failure the tag-scope work spent a month untangling.
- A head can be minimal. The cost the keyword idea saves is one short introduction per tag, which is small unless tags are assigned freely.
- Search never needed the distinction: a scoped `rg` over a string works whether or not a head exists.
- The published site is where a headless tag hurts: a tag link with no page behind it, or a page with no introduction.

## Operativity

Any option changes the collector, the validator's head requirement, and the site build's tag routing. No consumer needs keywords today. A separate field would add a schema change on every typed artifact.

## Adoption criteria

Reopen this proposal when tagging under the one-mechanism rule is observed to be refused or deferred because the head cost is too high for a recurring label, or when a host project asks for search-only labels. Until then the current state stands.

## Remaining choices

Which of the three keyword forms to adopt if the trigger arrives; whether generated tails list keywords at all; whether a keyword can be promoted to a topic by writing its head, and what that does to existing assignments.

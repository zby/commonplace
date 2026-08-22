---
description: "Accepted decision to retire text-contract profiles and keep reusable collection contracts only as clone-once prototypes with no inheritance or synchronization"
type: ../types/adr.md
tags: []
status: accepted
---

# 069-Collection contract bundles become one-time prototypes

**Status:** accepted
**Date:** 2026-08-22

## Context

Commonplace described theoretical, descriptive, prescriptive, editorial, and
dialectical/evidential **profiles** as named bundles that a collection could
adopt, extend, or replace. That wording implied a relationship between the
shared bundle and each adopting collection. No implemented path supplied one.

Collection discovery resolves the nearest `COLLECTION.md`. Writing and
connection skills read that file directly. Collection-conformance review uses
the local file itself as the gate. Deterministic validation parses no profile
declaration and has no profile fallback, inheritance, or conformance rule.
Every live collection already restated its operative contract in full. A
profile name inside that contract was therefore only a family-resemblance
label; removing it changed no binding rule.

The reusable abstraction still had one concrete consumer. The three
`COLLECTION.md` package templates seed standard collections during
`commonplace-init`. A worked dialectical/evidential contract could likewise
save a future collection author from re-deriving its attribution rules. These
bundles act at creation time, not while an installed collection is written or
reviewed.

The mismatch imposed an always-loaded cost. `AGENTS.md` defined profile as
registered vocabulary and repeated profile names in a `Role` column even
though routing depended on the adjacent `Use when` text. The profile catalogue
also claimed cross-collection coordination that independently evolving local
contracts could not guarantee.

## Decision

Retire **profile** as text-contract vocabulary. A collection does not adopt,
extend, conform to, or remain under a shared contract bundle. Its own
`COLLECTION.md` is complete and authoritative.

Keep genuinely reusable bundles as **collection prototypes** in
[`collection-prototypes.md`](../collection-prototypes.md). A collection
prototype is optional creation-time text that may be copied and adapted into a
new local contract. Copying ends the relationship: the destination project
owns and maintains its `COLLECTION.md`; Commonplace does not synchronize the
copy, apply later prototype changes to it, or claim that the collection still
conforms to the prototype. Catalogue changes affect future copies only.

The three standard package templates are the shipped notes, reference, and
instructions prototypes. The dialectical/evidential template is available as
an opt-in **experimental** prototype: it has one worked case but has not been
tested across independently maintained collections, and `commonplace-init`
does not install it automatically. Editorial/expository conventions remain
only in `kb/articles/COLLECTION.md`; one local realization with no
collection-creation consumer does not justify a prototype.

The prototype definition lives at the start of its catalogue rather than in a
separate definition artifact. Creation-only vocabulary does not belong in the
always-loaded root glossary. `AGENTS.md` keeps the text-contract gloss, drops
its profile half, and removes the routing table's `Role` column. Live collection
contracts state their purpose and quality goal directly. The profile material
is removed from `kb/notes/definitions/text-contract.md` in place, leaving its
text-contract definition for the separate decision about that term's eventual
home.

This decision partially supersedes [ADR 042](./042-register-becomes-a-default-profile-under-open-ended-text-contracts.md):
the closed register taxonomy remains retired, but its open set of adopted
profiles and worked-case promotion model is replaced by clone-once prototypes.
It also supersedes the profile-catalogue part of [ADR 057](./057-articles-use-an-editorial-profile-and-excluded-drafts.md)
without changing the articles collection, article lifecycle, or draft
circulation decisions.

## Considered alternatives

**Keep profiles as nonbinding shared labels.** This preserved compact names and
historical continuity. Rejected because the names carried no independently
consumed rules, while “adopt” and “under” continued to imply a relationship the
system did not implement. Similar local contracts can be described directly
when that comparison matters.

**Make profiles authoritative and update installed collections from them.**
This would make adoption real through inheritance, compilation, or
synchronization. Rejected because a local `COLLECTION.md` is intentionally the
complete, inspectable authority for its subtree. Shared updates would introduce
precedence, compatibility, migration, and freshness machinery with no observed
need.

**Delete reusable bundles entirely.** This would leave only local contracts.
Rejected because `commonplace-init` already needs creation-time contract text,
and the dialectical/evidential worked case provides a useful opt-in starting
point. Calling those files prototypes states their actual lifecycle.

**Create a separate collection-prototype definition.** Rejected because the
term is needed only when selecting creation material. Defining it in the
catalogue keeps its semantics beside the available copies and avoids another
canonical surface.

**Keep editorial/expository as a prototype.** Rejected because only
`kb/articles/` realizes it and no workflow copies it. Its local contract remains
operative; prototype status would advertise unsupported reuse.

## Consequences

**Operativity path.** `commonplace-init` consumes the three standard package
templates once when destination contracts do not yet exist. It preserves
existing contracts. The experimental template is selected manually and is not
on the default initialization path. After creation, agents and conformance
review consume only the destination `COLLECTION.md`, with that file's existing
contract force. No runtime or authoring consumer reads the prototype catalogue
to determine an installed collection's rules.

This makes the documentation match the implementation: a maintainer can tell
which artifact binds now and which text merely helps create it. Existing
collection contracts lose a label but none of their substantive clauses.
Future prototype improvements can be made without implying migration work for
installed projects.

The accepted cost is weaker name-based coordination across collections.
Similar collections may diverge after copying, and the catalogue no longer
claims that a common name guarantees compatible conventions. A reader who
needs to compare them must inspect their local contracts. That was already the
only reliable comparison.

Historical ADR titles and archived deliberation keep the term “profile” where
it records the vocabulary in use at the time. Supersession notes prevent those
records from being mistaken for current guidance. Ordinary uses of “profile”
for unrelated concepts, such as execution or system profiles, are unaffected.

---

Relevant Notes:

- [Text contract](../../notes/definitions/text-contract.md) — defined-in: the binding local declaration that prototypes may help an author create but never replace
- [Collection prototypes](../collection-prototypes.md) — implemented-by: catalogues the actual creation-time starting contracts
- [ADR 042: Register becomes a default profile under open-ended text contracts](./042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) — supersedes: replaces its adopted-profile model while preserving retirement of the closed register taxonomy
- [ADR 057: Articles use an editorial profile and excluded drafts](./057-articles-use-an-editorial-profile-and-excluded-drafts.md) — supersedes: retires the shared editorial-profile claim while preserving the local article contract and lifecycle

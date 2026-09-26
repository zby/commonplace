---
description: "Tags form one namespace per KB; membership claims range over the KB's participating collections; every tag has a head, and every head lives in a scaffolded kb/tags/ collection; no cross-KB membership and no exact resolver"
type: reference/types/adr.md
tags: []
status: accepted
---

# 089-Tags are one namespace per KB with heads in kb/tags

**Status:** accepted
**Date:** 2026-09-25
**Refines:** [ADR 026](./026-tag-readme-type-with-completeness-and-coverage-marks.md) (keeps the `tag-readme` type, weight gates, and marks; retires its hub binding and fixes the scope its marks range over)

## Context

A tag string is used across collections, but every surface that makes a claim about a tag's membership scans one collection. The validator checks a head's `complete` and `covered_by` marks over the head's own collection. The generated tail on the published site enumerates that same collection, while a rendered note's tag link routes across collection boundaries to that page. A reader who follows a tag from a reference document therefore lands on a tag page whose authored content plus generated listing omits the document they came from. ADR 026 made the marks enforced-or-omitted so that a claim telling exhaustive consumers to stop looking is never silently false; at repository scope the claims are false, because their scope was never named.

Heads sit in `kb/notes/`. A head is not a note by that collection's contract: it introduces and routes a topic rather than making a claim with explanatory reach, and it has its own type and rules. Its members span collections, so no member collection is its natural home. Head identity is declared twice, by filename and by `index_key`, with no invariant between the copies.

Under [ADR 086](./086-projects-read-the-library-from-the-installed-package.md) a host project reads the library from the installed package and cannot write to it. What a host's tags are, where their heads would go, and whether a host note can belong to a library tag were undecided. No host project uses tags today.

Usage evidence bounds how much machinery the decision may carry. A survey of about 6,800 agent sessions found tag search near one percent of KB search, description and content search the rest; tag pages were read mostly by work on the tag system itself. The operator's own finding failures, checked against their examples, were vocabulary misses and stale head text, not missing members or page shape. Tags earn their keep as human-readable topic pages on the published site and as a cheap keyword facet, and the design must cost accordingly.

## Decision

1. **One namespace per KB.** A tag string has one sense everywhere within one KB. Commonplace's `kb/` is one KB; each host project's `kb/` is another.

2. **Membership ranges over the KB's participating collections.** Every membership claim, mark check, and generated listing for a tag ranges over one set of collections, the same for every tag, declared once as the `participating:` list in the frontmatter of `kb/tags/COLLECTION.md` and never inferred from the directory tree. In this checkout: `notes`, `reference`, `instructions`, `agent-memory-systems`, and `agentic-systems`. `work`, `sources`, `reports`, `types`, and the proposal archive are outside the tag space, and no tag consumer reads them. Tags mean one thing wherever they are read; there is no second, weaker kind of tag (see Considered alternatives).

3. **Heads live in `kb/tags/`.** Every tag head is `kb/tags/<tag>-README.md`, type `tag-readme`, in every KB. The filename is the head's identity; the `index_source` and `index_key` fields are retired from the type. The collection's own `README.md` is the hub, an ordinary collection landing, replacing the special `tags-README.md` and its `tag-indexes` binding. `commonplace-init` scaffolds `kb/tags/` with its contract and landing; it scaffolds no heads.

4. **Every tag has a head.** A tag string in use within the tag space has a head, and the validator reports a tag without one. A head may be minimal: an introduction saying what the tag gathers and a few picks. A tag not worth a head is not worth assigning; the assignment is retagged or dropped.

5. **No cross-KB membership.** A host artifact cannot be a member of a library tag, because the library is read-only. A host may reuse a library tag string; it is then the host's own tag, with the host's own head or none. A query that unions two KBs' sweeps is an explicit query and asserts nothing about either KB's marks.

6. **Marks keep ADR 026's semantics at the declared scope, and are never forced.** `complete` and `covered_by` remain validated caches of exact membership, enforced-or-omitted. (*Amended by [ADR 090](./090-one-completeness-mark-reaches-members-in-one-hop.md): one mark, `complete`, meaning one-hop reach; `covered_by` retired.*) When a mark cannot be made true without a weak child tag or a tag created to hold a few notes, the mark is dropped and the head lists the uncovered members by hand.

7. **No exact resolver and no new tag relations.** The collector that scans participating collections, and the validator and site build that consume it, are the whole membership machinery. `covered_by` remains the only typed tag-to-tag relation.

## Considered alternatives

Two proposals worked out this option space and are archived on adoption: "Tag scope is declared where membership claims are made" and "Semantic contract for tags and tag heads".

**Collection-local tags.** Each collection keeps its own tag space; marks are reworded to "every note in this collection"; the site stops linking tags across collections. Cheapest, and it matches the current code. It lost because the cross-collection topic page is the one thing a human reader gets from a tag, and because the same string meaning different things in two collections of one KB is the confusion the namespace decision exists to remove.

**Heads stay in `kb/notes/`.** Considered first, to avoid relocating twenty-one heads. It lost when the host case was examined: a host has nothing to relocate, so the migration cost was the only reason, and two conventions are worse than one relocation. It also leaves heads as a standing exception to the notes contract.

**A dormant exact resolver first, then activation.** The workshop's earlier program: build a resolver over declared participation, keep it dormant, switch every consumer, then activate. It lost to the usage evidence. Agents do not use tags to find things, so a resolver has no consumer beyond the collector, validator, and site build, which a scoped scan already serves.

**A finding trial before any contract work.** Four presentations of the same members, judged on the operator's real tasks, to decide whether tags deserve a contract. Not run: the operator's examples showed vocabulary misses on notes that were present and tagged, which no presentation addresses. Its transcript survey stands as evidence.

**Generated topic groups for large tags** (Gwern's "Sort By Magic"). Redundant with child tags and `covered_by`, which give durable, addressable groups that an agent-written KB can afford to curate. Left open only as a split-candidate generator for tags over about a hundred members, untriggered.

**Scaffold heads or a starter vocabulary for hosts.** Rejected: no host uses tags, and a head for a tag nobody uses is the stale-index failure by construction.

**Keywords as a second kind of tag.** A tag without a head, or a tag on an artifact in a non-participating collection, would be a keyword: searchable and listed but making no claim. Each collection would declare whether its tags are memberships or keywords. Rejected by the operator (2026-09-25) on YAGNI grounds. The headless tags that motivated it were mistakes under the existing rules, which already expected a head per tag; the right response to a mistake in the data is to fix the data, not to adjust the new architecture so the mistake becomes legal. They were fixed in the implementing change. The same point from the consumer side: a second kind of tag makes every reader and every consumer carry a distinction that nothing yet needs. The idea is retained as a proposal, [Keyword tags without heads](../proposals/keyword-tags-without-heads.md), for the case where search-only tagging earns a mechanism of its own.

**Cross-KB membership by reading the library's heads as the host's.** Rejected: the library is read-only, its marks are validated only in the source checkout, and a host member would make them false there.

**Where the participating set is recorded** was left open in the first draft and resolved at implementation: the tag collection's own contract, since the set is a property of the tag space rather than of any member collection, and a collection contract already carries the collection's other cross-collection rules, its linking grammar. A per-collection field was rejected with the keyword option: it is the same distinction carried by every consumer.

**Left open.** Whether a host's site build should offer a union view over library tags.

## Consequences

**Operativity path.** The changed organization reaches behavior through four consumers. The collector in `index_generated` scans the participating set and reads heads from `kb/tags/`; the validator's mark checks use the collector's membership and fail a false mark, which is the force that keeps the claims honest; the site build's generated tail enumerates the same set, so a published tag page lists every participating member; and `commonplace-init` scaffolds the collection and its contract. Navigation entry points in the doctrine and in the init-written routing file name `kb/tags/README.md` as the hub. `cp-skill-connect` reads heads at the new path and keeps its `complete` skip rule. Implementation lands in commits carrying `Decision: ADR 089`.

**Easier.** A tag's page on the site is complete at the scope it claims. "Where is the head for X" has one answer in every KB. A host that wants tags needs no new mechanism. Heads stop being an exception the notes contract tolerates. The hub is an ordinary landing checked like every other.

**Harder or riskier.** Twenty-one heads and every link to them move, covered by redirects. A mark can now be falsified by an artifact in another collection, so a clean single-collection validation no longer clears a head; sweeps must validate `kb/tags/`. Reference and instruction authors who tag an artifact now change a published listing and may falsify a mark, which the validator reports on the head, not on the artifact they wrote.

**No longer possible.** A tag page that silently omits members from other participating collections. A head outside `kb/tags/`. A tag in use with no head. Two heads for one tag. A mark that is true in one collection and false in the KB.

**Limits.** This decision covers topical tags on library artifacts in one KB and the surfaces named above. It has not been tested with a host project that uses tags, with more than one participating collection contributing a large share of a tag's members, or with a site build that serves more than one KB. It does not decide what assigning a tag asserts beyond membership in a named set, which the retired semantic-contract proposal explored; that question returns only if a consumer needs more than membership.

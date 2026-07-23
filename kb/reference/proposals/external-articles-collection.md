---
description: "Proposal: an outward-facing articles collection — landing pages and blog posts distilled from the KB, each an entry point leading an outside reader into the KB; option space, forces, no decision"
type: kb/types/note.md
traits: [design-proposal]
tags: [document-system, context-engineering]
---

# External articles collection

Every writable collection Commonplace ships is inward-facing: its artifacts are consumed in-context by an LLM agent operating on the KB. There is no place to author an artifact meant for a human reader *outside* the project — a landing page, a blog post, a methodology write-up drawn from the KB's own notes. This proposal describes what such a collection would have to declare and the choices it leaves open. One orientation constraint is fixed by operator intent: every artifact in the collection is an **entry point into the KB** — it works for a reader with no KB context, and its job is to lead that reader into the KB, not to replace it. Within that constraint the proposal decides nothing.

## Current state (as of 2026-07-22)

- Writable collections are `kb/notes/` (theoretical profile), `kb/reference/` (descriptive), `kb/instructions/` (prescriptive), `kb/agent-memory-systems/` and `kb/agentic-systems/` (descriptive external-system coverage), `kb/sources/` (captured material), and `kb/work/` (workshop). Each is authored for, and loaded into, an agent's bounded context while it operates on the KB.
- The three default [profiles](../text-contract-profiles.md) — theoretical, descriptive, prescriptive — plus one promoted profile (dialectical/evidential, proven in the sibling `epistack-casebooks` project) all assume that in-project consumer. The profile set is open-ended, and new profiles are promoted only after a worked case ([ADR 042](../adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md)).
- Agent-facing conventions run through every collection: descriptions are retrieval filters rather than reader abstracts, links are relative-path graph edges, frontmatter and footer link tables are structural, vocabulary is glossed on first use for a reader who can traverse the graph. Commonplace has a [ProperDocs documentation site](../documentation-site.md) that renders `kb/` and supplies reader landing pages, but it publishes the agent-facing source largely as-is. There is no enforced transform from KB markdown to a self-standing article that strips structural metadata and rewrites internal links for an off-site channel.
- Scope rules push application-specific KB content to consuming projects. Commonplace's own scope covers KB methodology; a consuming KB covers its domain. Neither has an authoring home for content addressed to an outside reader.
- Outward-facing writing already happens in this repo: the [Where It Lives Is Not What It Is ingest](../../sources/where-it-lives-architectural-vocabulary-retained-adaptation.ingest.md) records a position paper worked from this KB's notes, while the `epistack-submission` and `epistack-competition` workshops under `kb/work/` draft external submission material. Workshops close and are deleted, so the finished outward artifact has no library home — the deliverable either evaporates or the workshop lingers past its lifecycle.

## Problem

An outward-facing article is a document a human reads without prior KB context — and, under the entry-point orientation, its job is to hand that reader a way in. It synthesises what several notes established into continuous prose for an audience that will not read a footer link table or a retrieval-filter description, and it must earn the reader's next click into the KB rather than assume it. None of the shipped profiles fit: their quality goals (reach, fidelity + economy, executability) are calibrated for a consumer who can traverse the graph and load adjacent artifacts on demand.

Today an author who needs to publish from the KB has two bad options. Misuse `kb/notes/`: wrong contract (claim-as-title and reach, not audience-facing self-contained prose), and the note's agent-facing links and glosses leak into anything derived from it. Or leave the KB entirely: the published piece loses its lineage back to the notes it distils, so nothing records which claims it rests on or signals the article for revision when those claims change.

## Option space

**Where it lives.** A new top-level `kb/articles/` collection (`articles` is the working name); an area inside an existing collection; or a sibling publish tree outside `kb/` (a `content/` or `site/` root with its own tooling) that links *back into* `kb/` for lineage. Placement inside `kb/` buys the [collection contract and type model](../collections-and-types.md), validation, and a [general freshness substrate](../freshness-architecture.md), though article target kinds and transitions would still have to be defined; placement outside avoids forcing agent-facing tooling onto reader-facing artifacts.

**Artifact modes.** The entry-point orientation is shared, but two maintenance shapes are in play. A *landing page* is a living document — a curated doorway into a region of the KB, maintained in place, expected to track the KB as it evolves. A *blog post* is a dated publication — a record of what was said, conventionally not silently rewritten after publication; when it drifts from the KB the remedy is a follow-up post or a banner, not an in-place edit. One collection can host both modes if the contract names them and gives each its maintenance rule, or the collection can commit to one mode and leave the other out of scope.

**[Text contract](../../notes/definitions/text-contract.md) / profile.** A new editorial (expository) profile. Orientation: lead an external human reader into the KB. Quality goal: clarity for a reader with no KB context, plus *funnel effectiveness* — the piece must stand on its own yet leave the reader knowing where in the KB to go next; self-containment is a floor, not the ceiling, which distinguishes this from a plain essay profile. Title convention: headline or topical. Attribution: an article carries a byline and is a first-person-committed *public* statement, so the stakes of the "first-person-committed" property that the internal profiles treat as low-ceremony change outside the project. Maintenance: split by artifact mode — landing pages track the KB like a description tracks its referent; blog posts are dated records whose staleness means "would we still say this", remedied by re-publishing rather than in-place edits.

**Link grammar — the internal/published boundary.** Two edge classes that must not be confused. *[Lineage](../../notes/definitions/lineage.md) edges* record which notes an article distils, for maintenance and backlink; they belong in frontmatter or a footer and must never render into published output. *Published references* are the links inside the prose a human follows — and under the entry-point orientation the most important of these point *into the KB*: they are the funnel, deliberate invitations to go deeper, not leakage to strip. Whether they survive publication depends on the channel. A reader arriving on GitHub can follow relative links into `kb/` directly; an off-site channel (a blog, a submission venue) breaks relative paths, so publishing there needs a render step that rewrites KB links to stable public URLs — and strips lineage footers, frontmatter, and agent-facing glosses. The hard design object is this channel-dependent transform: raw KB markdown is the published artifact on at most one channel.

**Type.** Reuse `note` with an `article` trait, or introduce a collection-local `article` type spec whose schema carries a byline, publish date, canonical URL, and an explicit source-notes list.

## Forces

- **Boundary leakage.** Frontmatter, footer link tables, first-use vocabulary glosses, and relative links are all agent-facing. Without an enforced render step they leak into published output. This is the load-bearing risk: the collection is only coherent if the internal→published transform is specified, not left to per-article discipline.
- **Two consumers, one artifact.** An article is both a graph node (maintained, linked from the notes it distils) and a published document (self-standing, human-read). The retrieval-filter description and the human-facing abstract are different texts; the maintenance-facing and reader-facing shapes pull the same artifact in opposite directions.
- **Attribution inversion.** The internal profiles make attribution optional because first-person commitment is cheap inside the project. A byline on a public article is not cheap — the same property carries different weight the moment the audience is external.
- **Lineage versus drift.** An article distils notes that keep evolving, and the two artifact modes want different freshness semantics from the same substrate. A landing page tracks the KB — source-note changes mean "update me". A blog post is a record — the same changes mean only "a follow-up may be warranted", never an automatic rewrite. Neither matches the description-tracks-referent model of any registered target kind exactly, and conflating the two modes would give one of them the wrong staleness remedy.
- **Scope and YAGNI.** This may be a consuming-project concern rather than a Commonplace default. The editorial profile could be proven in one consuming KB's worked case first, per the worked-case-first promotion guard, before earning a shared profile entry — the same path the dialectical/evidential profile took.

## Free choices

- Whether articles live inside `kb/` at all, or in a sibling publish tree that links back into `kb/` for lineage.
- Whether the collection hosts both artifact modes (living landing pages and dated blog posts) under one contract, or commits to one mode.
- Whether a blog is a distinct channel generated *from* the collection (the collection is canonical, posts render out) or the collection simply archives what was published elsewhere.
- Whether to introduce an `article` type spec or reuse `note` plus an `article` trait; if a spec, whether mode (landing page vs post), byline, publish date, and canonical URL are schema fields.
- The render pipeline: none (raw markdown as published, GitHub-only channel), a dedicated rewrite/export command, or a static-site-generator boundary that owns the transform.
- Whether note→article lineage uses the current [`adapted-from`](../adr/054-add-adapted-from-and-operationalized-from-lineage-relations.md) relation with a source-side `Adapted into:` footer, which needs the source collection's authorization, or lives only on the article side as a source-notes list.

## Adoption criteria

- A real need to publish from a Commonplace KB — this repo publishing its own methodology, or a consuming project publishing domain findings — rather than a speculative feature. The `epistack-submission` workshop material is a candidate first case.
- An editorial/expository profile written and exercised in a single worked case — plausibly a `kb/work/` workshop drafting the candidate `COLLECTION.md` plus one or two real articles before the collection is created — then promoted to the [profile catalogue](../text-contract-profiles.md) under the ADR 042 guard.
- The internal→published render boundary specified and enforced, so no agent-facing convention reaches published output.
- Freshness semantics chosen for the "revision-may-be-warranted" signal, distinct from the description-tracks-referent model, if lineage is registered at all.

## Rationale

- [Human-LLM differences are load-bearing for knowledge-system design](../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — rationale: the dual-audience problem this collection makes explicit; an outward-facing article is the extreme case where the human reader, not the agent, is the sole consumer.
- [Design for the first-time human, except on access cost](../../notes/design-for-the-first-time-human-except-on-access-cost.md) — rationale: supports separate human-facing and agent-facing materializations over one source of truth when their access modes diverge.
- [Source changes should surface downstream review targets, while reverse lineage can remain searchable](../../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) — rationale: a source-note change must surface the dependent article even when maintenance lineage is hidden from the published reader.
- [Keep lineage and compiled views from drifting](../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) — rationale: a rendered publication needs an authoritative source, regeneration rule, and stale-view handling rather than becoming an independent source of truth.
- [Links encode conditional possibilities, not obligations](../../notes/links-encode-conditional-possibilities-not-obligations.md) — rationale: published KB links should be deliberate invitations serving a reader need, which is what makes them a funnel rather than graph leakage.
- [Text contract](../../notes/definitions/text-contract.md) — defined-in: the contract vocabulary this proposal would extend with an editorial profile.
- [Text contract profiles](../text-contract-profiles.md) — see-also: the open, worked-case-gated catalogue a new editorial profile would be promoted into.

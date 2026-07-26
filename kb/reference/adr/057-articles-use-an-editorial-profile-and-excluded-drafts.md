---
description: "Articles use a promoted editorial profile, keep drafts under a site-excluded collection subtree, and publish immutable dated bodies through ProperDocs"
type: ../types/adr.md
tags: []
status: accepted
---

# 057-Articles use an editorial profile and excluded drafts

**Status:** accepted
**Date:** 2026-07-26

## Context

Commonplace had no durable home for outward-facing writing. Its library collections are optimized for agents that can traverse the graph, while a technical reader arriving from outside needs a self-standing body and a deliberate onward path into the KB. The public ProperDocs site already renders every ordinary file under `kb/`, so a committed draft in a rendered path is public before an editorial publication decision exists.

The worked case established the missing shape. `kb/articles/` now has an editorial collection contract, a deliberately minimal local type, and a near-complete first article distilled from the self-improving-systems cluster. The proposal **External articles collection** left draft placement, publication, profile promotion, and lifecycle presentation open until that case existed.

## Decision

**`kb/articles/` adopts the editorial/expository profile.** Its audience is a highly technical reader with no project context. Bodies are reader-only prose: headlines rather than claim-titles, no agent-facing footer grammar, and in-prose links that deliberately lead into the KB. Articles carry a byline, lifecycle status, and source-note lineage. The exercised profile is promoted to the shared [profile catalogue](../text-contract-profiles.md).

**Drafts live under `kb/articles/drafts/`.** This subtree remains inside the article collection, so the collection contract, article type, write path, validation, and conformance review apply from the first commit. ProperDocs excludes `articles/drafts/**`, keeping drafts out of the published site and search index. Publication relocates the article to the collection root, sets `status: published` and a `published` date, and lists it in `kb/articles/README.md`.

**Published bodies are dated records.** Publication freezes the substantive body. Later corrections use a dated annotation, a superseding article, or `status: withdrawn`; they are never silent rewrites. ProperDocs already renders article status in the metadata line under the title, so `published`, `superseded`, and `withdrawn` remain visible on the page without a second committed banner.

**The article type stays minimal.** `source_notes` paths are structurally constrained and resolved by validation. Byline, lifecycle, publication date, reader-only prose, and freeze semantics remain binding collection-contract clauses, enforced through authoring and collection-conformance review. They move into schema only after a mechanical failure demonstrates that prose enforcement is insufficient.

**Lineage remains searchable, not freshness-registered.** A dated article tolerates later divergence from its source notes; a source change prompts the editorial question “follow up or leave as history,” not an automatic rewrite obligation. Living landing pages and off-site publication remain outside this decision.

Operativity path: `cp-skill-write` and collection-conformance review consume `kb/articles/COLLECTION.md` with binding force; that contract routes an approved draft into the prescriptive [publication procedure](../../instructions/publish-an-article.md); `properdocs.yml` removes the draft subtree from site generation; the collection README controls published navigation; and the ProperDocs hook renders lifecycle status to readers. The pre-decision worked draft, “Reflective self-improvement,” remains in the collection root through its imminent first publication; later drafts start in the excluded subtree.

## Considered alternatives

**Draft in `kb/work/`.** Rejected because the article contract and type would bind only at promotion, after the drafting decisions they are meant to shape. Workshop files are also temporary work products, while an article draft needs stable editorial identity before publication.

**Draft in the collection root, rendered but unlisted.** This was sufficient for the first worked draft while no published article existed, but not as a standing procedure. Site search still discovers an unlisted page; a visible `draft` label does not undo accidental publication.

**Exclude by frontmatter status in a build hook.** Rejected for the first version. A path glob is inspectable configuration with no custom filtering code, and placement plus frontmatter gives two visible signals during operation. A status-driven hook can return only if relocation becomes recurring friction.

**Require byline, status, and publication date in schema immediately.** Rejected under the worked-failure rule used by the article type. These fields bind now through the collection contract and conformance review; schema should gain only constraints whose absence produces a demonstrated mechanical failure. `source_notes` resolution already crossed that threshold.

**A separate publishing tree or export command.** Rejected because ProperDocs already supplies rendering, stable path-derived URLs, link resolution, search, navigation, and redirects. Adding another canonical tree would create synchronization work without a second publication channel.

Free choices left open: whether a later living-page article mode deserves freshness registration; whether source-side lineage ever becomes useful; and whether off-site republication requires a fail-closed public-link audit.

## Consequences

Easier:

- Authors work under the final editorial contract without exposing unfinished pages.
- Publication is a small, reviewable transition: relocate, set status/date, and list.
- The shared profile catalogue now has an in-repo exercised editorial case.
- Readers see lifecycle state on every rendered article, while the Markdown body stays reader-only.

Harder / accepted costs:

- Publishing changes the article path, so the relocation tool and redirect integrity remain part of the operation.
- Editorial requirements are judgment-enforced rather than schema-enforced until failure evidence warrants stricter machinery.
- Searchable lineage does not proactively surface source drift; maintainers must ask the follow-up-or-history question deliberately.

---

Relevant Notes:

- [Text contract profiles](../text-contract-profiles.md) — implemented-by: catalogue containing the promoted editorial/expository profile
- [Documentation site](../documentation-site.md) — part-of: rendering and publication channel used by articles
- [Publish an article](../../instructions/publish-an-article.md) — implemented-by: executable transition from approved draft to dated public artifact
- [ADR 042 — Register becomes a default profile under open-ended text contracts](./042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) — extends: worked-case-first rule under which the editorial profile is promoted
- [Document types should be verifiable](../../notes/document-types-should-be-verifiable.md) — rationale: why article schema constraints are added from observed mechanical failure rather than speculative completeness

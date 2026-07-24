---
description: "Proposal: outward-facing kb/articles/ — dated posts distilled from the KB for technical readers, published via the existing ProperDocs Pages pipeline; open: the draft-to-published procedure"
type: kb/types/note.md
traits: [design-proposal]
tags: [document-system, context-engineering]
---

# External articles collection

Every writable collection Commonplace ships is inward-facing: its artifacts are consumed in-context by an LLM agent operating on the KB. There is no place to author an artifact meant for a human reader *outside* the project — a blog post or methodology write-up drawn from the KB's own notes. This proposal describes such a collection. Four constraints are now fixed by operator intent:

- **Entry point into the KB.** Every article works for a reader with no KB context, and its job is to lead that reader into the KB, not to replace it.
- **Audience: highly technical.** Researchers and builders of agent and knowledge systems. Self-contained means "no KB context assumed", never "simplified" — the pieces carry full technical weight.
- **Channel: the existing ProperDocs site.** Articles publish through the pipeline the KB already has — `.github/workflows/pages.yml` builds `kb/` with ProperDocs and deploys to GitHub Pages on every push to `main`. The KB artifact is canonical; the site is a derived render; off-site republication is out of scope.
- **Lineage stays simple.** An article records the notes it distils as a plain, searchable list. No freshness registration, no automated drift surfacing in the first iteration.

What remains genuinely open — and is the main design question below — is the **publication procedure**: on this channel there is no publish step, because every file under `kb/` is live at its URL as soon as the push deploys. "Published" must therefore be constructed editorially, and the option space for that (directory placement, index listing, rendered status cues) is laid out under [Publication procedure](#publication-procedure-the-open-question).

## Current state (as of 2026-07-23)

- Writable collections are `kb/notes/` (theoretical profile), `kb/reference/` (descriptive), `kb/instructions/` (prescriptive), `kb/agent-memory-systems/` and `kb/agentic-systems/` (descriptive external-system coverage), `kb/sources/` (captured material), and `kb/work/` (workshop). Each is authored for an agent's bounded context. The three default [profiles](../text-contract-profiles.md) plus one promoted profile all assume that in-project consumer; new profiles are promoted only after a worked case ([ADR 042](../adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md)).
- The [ProperDocs documentation site](../documentation-site.md) is already a working outward channel: `docs_dir: kb`, so every file under `kb/` not matched by `exclude_docs` renders and is publicly reachable at a stable URL derived from its path, minutes after a push to `main`. Relative links between KB files render as working site links; frontmatter is consumed as page metadata, not displayed; `redirect_maps` preserves external URLs across renames. The nav is generated from collection `README.md` files, so a `kb/articles/README.md` becomes a top-nav entry with no configuration. The site's hooks already render a **metadata badge** under each page's first heading (`src/commonplace/docs/properdocs_hooks.py:on_page_markdown`): type, `status`, and tag links — so a status field on an article is already reader-visible today, without new machinery.
- The repository is public. Nothing under `kb/` is ever access-restricted; the site search plugin indexes every rendered page. "Publication" on this channel can only mean editorial status — what the KB presents as finished, listed, and citable — never secrecy.
- Outward-facing writing has already happened here and left no library trace: the [Where It Lives Is Not What It Is ingest](../../sources/where-it-lives-architectural-vocabulary-retained-adaptation.ingest.md) records a position paper worked from this KB's notes, and the epistack submission workshops drafted competition material and were closed and deleted (2026-07-23) after the deadline passed. Workshops close and are deleted by design, so the finished outward deliverable either evaporates or the workshop lingers past its lifecycle — exactly the gap this proposal names.

## Problem

An outward-facing article is a document a technical reader — a researcher or builder — reads without prior KB context, and whose job is to hand that reader a way in. It synthesises what several notes established into continuous prose for an audience that will not read a footer link table or a retrieval-filter description, and it must provide a clear, worthwhile onward path into the KB. None of the shipped profiles fit: their quality goals (explanatory-reach, fidelity + economy, executability) are calibrated for a consumer who can traverse the graph and load adjacent artifacts on demand.

Today an author who needs to publish from the KB has two bad options. Misuse `kb/notes/`: wrong contract (claim-as-title and explanatory-reach, not audience-facing self-contained prose), and the note's agent-facing conventions leak into anything derived from it. Or draft in a workshop and publish nowhere durable: the piece loses its lineage back to the notes it distils, and the workshop lifecycle guarantees the deliverable has no home.

## Design

**Where it lives.** `kb/articles/`, inside `docs_dir`, so the existing pipeline renders it with no new tooling. Placement inside `kb/` buys the [collection contract and type model](../collections-and-types.md) and validation. The old alternatives — a sibling publish tree, a dedicated export command, a static-site-generator boundary to build — are dissolved by the channel decision: ProperDocs already owns the transform, strips frontmatter, resolves relative links, and preserves URLs across renames.

**What the render boundary reduces to.** ProperDocs handles the structural transform, so boundary discipline narrows to an authoring rule the contract must state: *all agent-facing structure lives in frontmatter; the article body is reader-only prose.* No footer link tables, no first-use glosses aimed at graph traversal, no retrieval-filter phrasing. In-prose links into `kb/` are not leakage — under the entry-point orientation they are the point: deliberate invitations to go deeper, which render as working site links on this channel.

**Lineage.** A `source_notes` frontmatter list of repo-relative paths, validated to resolve. Discovery of affected articles after a note changes is a search (`rg "source_notes" kb/articles/`), and that is all v1 claims. The [general freshness substrate](../freshness-architecture.md) exists if automated drift surfacing ever earns its cost, but a dated post tolerates drift by design — "would we still say this" is answered by a follow-up post, not a rewrite — so the cheap cut is safe for this mode. The deferred obligation is on record in the rationale below.

**Artifact mode: dated posts first.** A *blog post* is a dated publication — a record of what was said, not silently rewritten after publication; when it drifts from the KB the remedy is a follow-up post or a status annotation. The other mode — a *living landing page*, maintained in place to track the KB — stays out of scope until the dated-post contract has been exercised. (The site already has de facto landing pages: `kb/index.md` and the collection READMEs. Whether they should ever adopt the article contract is a later question.)

**Type.** A collection-local `article` type spec: `status`, byline, publish date (required once published), `source_notes`. The canonical URL is derivable from the path on this channel and `redirect_maps` preserves it across renames, so it is not a schema field until an off-site channel exists. Lineage lives article-side only; no source-side `Adapted into:` footers in v1 (the [`adapted-from`](../adr/054-add-adapted-from-and-operationalized-from-lineage-relations.md) relation remains available if source-side visibility is ever wanted).

**Publication lifecycle.** At minimum `draft`, `published`, `superseded`, `withdrawn`. Publication freezes the dated body: corrections become an explicit status annotation, a superseding post, or a withdrawal — never a silent rewrite. The rendered status surface (below) is where these states become visible to the reader.

## Publication procedure (the open question)

Push equals live: the moment an article file lands on `main`, it renders at its URL. So the procedure that makes an article "published" is editorial, and the options — not mutually exclusive — are:

1. **Directory as status.** Drafts live in a `kb/work/` workshop and move into `kb/articles/` only at publication. The collection contains only published (and later superseded/withdrawn) articles; presence in the directory *is* the status. Reuses the existing workshop convention for in-flight work, but has a structural flaw for this collection: `kb/work/` enforces no quality goals. A workshop draft is written outside the article type and the editorial contract, so everything the collection exists to enforce — schema, reader-only body, review — binds only retroactively, at promotion. The draft also still renders at its workshop URL.
2. **Draft in place, excluded from the build.** Drafts sit inside the collection under a path listed in `exclude_docs` — e.g. `kb/articles/drafts/` with one `articles/drafts/**` glob. The collection contract, article type, and validation bind from the first commit, because a `drafts/` subdirectory is still inside the `COLLECTION.md` subtree; the draft is visible in the repo but absent from the site and its search index until moved to the collection root.
3. **Draft in place, rendered but unlisted.** The collection README lists only `status: published` articles. Weakest as a lone mechanism: the search plugin indexes drafts, and nothing on the page itself marks them — it only works combined with option 4.
4. **Status rendered on the page.** The metadata badge already renders `status` under the title; the remaining work is presentation — CSS in the site's existing `extra_css` to color-code it (e.g. draft amber, superseded/withdrawn flagged with a pointer to the successor), or a hook extension that promotes non-`published` states from a badge line to a banner. Some form of this is needed in *any* design, because a superseded or withdrawn dated page must say so on the page itself, not only in an index.

The real choice is between 1 and 2 for draft handling (3 alone is leaky), with 4 required regardless. The decisive criterion rules out option 1: drafting must happen where the quality goals are enforced, and only the collection enforces them — a draft that spends its life outside the contract meets the contract by accident. For the first article the worked case simplifies past option 2 as well: the collection starts empty, so there is no published face for a rendered draft to pollute, and the draft sits directly in the collection root with its `draft` status shown by the existing badge (3 + 4). The exclusion mechanism is deferred until the collection has published content to protect.

## Forces

- **Boundary leakage.** Narrowed but not gone: ProperDocs strips frontmatter and resolves links, so what can still leak is body-level habit — footer link tables, agent-facing glosses, retrieval-filter prose. The reader-only-body rule must be in the collection contract and checked by review, not left to per-article discipline.
- **Publicability is a channel property.** On this repo's public site the publication step reduces to editorial status. A consuming project that is not wholly public gets no such reduction: there, publishing needs the full fail-closed check (unresolved public routes, links into non-public artifacts, human approval boundaries). The contract should state this so the simplification is not silently copied into a setting where it is wrong.
- **Two consumers, one artifact.** An article is both a graph node (validated, lineage-tracked, findable by agents) and a published document (self-standing, human-read). The retrieval-filter description and the reader-facing opening are different texts; the type must give each its place rather than letting one impersonate the other.
- **Attribution inversion.** The internal profiles treat first-person commitment as low-ceremony. A byline on a public dated post is a different commitment — the same property carries different weight the moment the audience is external, which is why byline and date are schema fields, not conventions.
- **Lineage versus drift.** Searchable-only lineage means nothing *surfaces* an article when its source notes move on; someone has to look. For dated posts this is acceptable — drift produces a follow-up, not an obligation to rewrite — but it is one more reason living landing pages stay out of scope: they would need the surfacing machinery this proposal deliberately defers.
- **Scope and YAGNI.** The editorial profile is proven here first in one worked case, per the worked-case-first promotion guard, before earning a shared profile entry — the same path the dialectical/evidential profile took.

## Free choices

- Draft handling once the collection has published content: an excluded `drafts/` path in `exclude_docs`, a build hook that excludes any article with `status: draft`, or drafts that keep rendering with the badge.
- Status presentation: badge coloring versus banner promotion, the color semantics, and whether draft state ever renders at all.
- Whether the collection README lists superseded and withdrawn articles or only published ones.
- Whether living landing pages later join the collection under the same contract, and whether the site's existing landing pages adopt it.
- Whether `mode` is a schema field from day one or added only when a second mode exists.
- Whether source-side lineage footers (`Adapted into:`) ever ship, or lineage stays article-side permanently.
- Whether freshness registration is ever added for articles, and for which mode.

## Adoption criteria

- A real first article published: this repo publishing its own methodology (named below), not a speculative feature.
- An editorial/expository profile written and exercised in the worked case, then promoted to the [profile catalogue](../text-contract-profiles.md) under the ADR 042 guard.
- The reader-only-body rule stated in the collection contract and holding in practice: the rendered page shows no agent-facing structure beyond the standard metadata badge.
- Lifecycle exercised at least through `draft` and `published`, with the status surface rendered well enough that supersession or withdrawal could be represented without silently rewriting the dated body.
- Lineage recorded as validated `source_notes` on the published article. (Freshness integration is explicitly deferred, not forgotten — it returns only if drift becomes a real cost.)

## Recommended worked case

A test configuration, not a shipped-system decision:

- Create `kb/articles/` first, with a `COLLECTION.md` (editorial profile draft) and a collection-local `article` type requiring `status`, byline, publish date, and `source_notes` with resolving paths.
- **First post: reflective self-improving systems** — the KB's home territory. Distil what the [self-improving-systems cluster](../../notes/self-improving-systems-README.md) establishes into one dated post for researchers and builders: what it means for a system to operate on its own methodology, and what Commonplace's worked experience says about making that loop governable. Draft it directly in the collection root with `status: draft` — the contract, type, and validation bind from the first commit, and the rendered badge marks the state.
- Publish by setting `status: published` and the date, and listing the article in the collection README (which also puts `Articles` in the site nav). The post is live at its Pages URL when the push deploys.
- Render status visibly. The v1 floor is the existing metadata badge showing `status`; color-coding via `extra_css` is polish that can land with the same change or after.
- Treat the published body as frozen: any correction in the exercise is made as a status annotation or a superseding note, to prove the mechanism.

The case succeeds when the post is live at its URL with a reader-only body, a visible status, a working onward path into the KB, and validated `source_notes` — and when a deliberate edit to one source note is discoverable by search and triaged into "follow-up or leave" without anyone proposing to rewrite the dated body. Only after that should the design decide the standing draft-handling rule once published content exists (an excluded `drafts/` path, a status-driven exclusion hook, or drafts that render with the badge), whether landing pages join, and whether the profile merits promotion.

## Rationale

- [Human-LLM differences are load-bearing for knowledge-system design](../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — rationale: the dual-audience problem this collection makes explicit; an outward-facing article is the extreme case where the human reader, not the agent, is the sole consumer of the body.
- [Design for the first-time human, except on access cost](../../notes/design-for-the-first-time-human-except-on-access-cost.md) — rationale: supports separate human-facing and agent-facing materializations over one source of truth when their access modes diverge.
- [Source changes should surface downstream review targets, while reverse lineage can remain searchable](../../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) — rationale: names the obligation this proposal deliberately defers; v1 accepts searchable-only lineage because the dated-post mode tolerates drift.
- [Keep lineage and compiled views from drifting](../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) — rationale: the rendered site is a derived view with an authoritative source and a regeneration rule (the Pages build), which is what makes KB-canonical publication safe.
- [Links encode conditional possibilities, not obligations](../../notes/links-encode-conditional-possibilities-not-obligations.md) — rationale: published KB links should be deliberate invitations serving a reader need, which is what makes them an onward path rather than graph leakage.
- [Document types should be verifiable](../../notes/document-types-should-be-verifiable.md) — rationale: the `article` type makes publication identity, lifecycle, and source-note obligations mechanically checkable rather than prose convention.
- [Text contract](../../notes/definitions/text-contract.md) — defined-in: the contract vocabulary this proposal would extend with an editorial profile.
- [Text contract profiles](../text-contract-profiles.md) — see-also: the open, worked-case-gated catalogue a new editorial profile would be promoted into.
- [Documentation site](../documentation-site.md) — see-also: the channel this proposal fixes — build pipeline, README-vs-index rule, nav generation, metadata badge, and landing-page inventory.

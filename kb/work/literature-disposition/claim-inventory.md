# Claim inventory for the cohort

Built 2026-08-24, deliberately **before** reading any external source, so the
literature's vocabulary does not decide what counts as a claim — the ordering the
[first worked case](../source-grounding/worked-case-agents-navigate.md) followed.

**Epistemic status of the attributions.** Every `established-elsewhere` row below
is a *recalled* placement, not a read one. That is precisely the status this
workshop exists to distrust, so each row is a hypothesis with a named target for
the sibling workshop to adjudicate, and confidence is recorded honestly including
where it is low. A row is a reading assignment, not a verdict.

## Part 1: the navigation and pointer notes

### link-following-and-search-impose-different-metadata-requirements

| # | Claim | Class | Candidate tradition | Conf |
|---|---|---|---|---|
| C1 | Two movement modes: local link-following with rich context, long-range search with none | established-elsewhere | browse vs analytical search (Marchionini 1995); orienteering vs teleporting (Teevan et al. 2004) | med-high |
| C2 | Pointer context is graded: inline prose > index entry > one-line description | local-transferable | adjacent to scent cue quality, but foraging ranks cue-content correlation, not cue *types* | low |
| C3 | Without local context the pointer must be self-sufficient, so descriptions carry the decision | established-elsewhere | document-surrogate literature; query-biased vs static summaries (Tombros & Sanderson 1998) | medium |
| C4 | Indexes are hybrid — jumped to like search, browsed like links — so they need both | local-transferable | none placed | — |
| C5 | Each mode has its own metadata lever | local-commonplace | — | — |

Attribution present: **none**. Strongest dependent: `kb/reference/navigation.md:92`,
which takes it as the rationale for the shipped navigation model.
**Error found:** skill descriptions are filed under "link-following: local
navigation with rich context," but they load at session start with no surrounding
argument — by the note's own criterion they belong on the search side. The
section's summary sentence is false for one of its three members.

### a-knowledge-base-should-support-fluid-resolution-switching

Five claims; one recalled as established (Shneiderman's "overview first, zoom and
filter, details on demand," low-medium), four local. C2 and C4 are a Commonplace
mechanism inventory that survives any literature finding untouched.

**Attribution defect, independent of disposition.** The note declares
`traits: [has-external-sources]` on the strength of `Source: - Adapted from a
social media post on "The Art of Good Thinking: Moving Between Levels"` — no
author, no URL. A trait is asserted against an unidentifiable reference.
**Error found:** the title says KB quality "should be measured by" fluidity while
the body defers all measurement to open questions.

### index-curation-adds-orientation-that-generation-cannot-produce

| # | Claim | Class | Candidate tradition | Conf |
|---|---|---|---|---|
| C1 | A complete generated listing gives completeness but not orientation | established-elsewhere | LIS pathfinders / subject guides / annotated bibliographies | medium |
| C2 | Curation adds groupings, role-stating phrases, cross-index links | established-elsewhere | same, plus PKM Maps of Content | med-high |
| C3 | The context phrase states a note's *role in the topic*, which a description cannot | established-elsewhere | annotation in annotated bibliographies; thesaurus scope notes (ISO 25964) | medium |
| C4 | Generated-tail architecture confines staleness to the curated head | local-commonplace | — | — |
| C5 | Curation has diminishing returns below ~5 notes | local-commonplace | — | — |

**This is the second case where the error matters more than the overlap — and
this one is operative.**

"Generation cannot produce" is false as stated. An LLM can generate groupings and
role annotations; what *deterministic build-time* generation from a note's own
description cannot do is produce them **verifiably**. The note's only evidence is
a design preference recorded in the OpenViking review — that "auto-aggregation
would lose" editorial context phrases — plus the assertion that "orientation
resists automation." Auto-aggregation there means bottom-up summary aggregation,
which is deterministic. So the evidence supports the scoped claim and the title
asserts the unscoped one.

Two ADRs `rests-on` it: [ADR 025](../../reference/adr/025-complete-generated-indexes-are-build-time-only.md)
line 69 ("why curated heads stay committed while generated listings move to build
time") and [ADR 026](../../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md)
line 69 ("the groupings and phrases are the durable value that survives a mark's
drop").

**The good news is that scoping it does not destabilize either ADR.** Both are
about deterministic build-time generation, so the scoped claim is all they
require. The note overclaims past what its own dependents need. Correcting the
scope makes the dependency honest rather than breaking it.

Attribution present: none — **but the lineage already exists one hop away.**
`an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract` names Luhmann's
hub notes and Milo's LYT/MOC and says the tag-README "inherits the tradition's
core commitment," linking back here. The attribution may need moving one hop, not
inventing.

### human-llm-differences-are-load-bearing-for-knowledge-system-design

Five claims, **zero** placed in an outside tradition. Best-attributed note of the
six: it cites *Context Engineering for AI Agents in OSS* (arXiv 2510.21413) for
the dual-audience split and Lopopolo's *Harness Engineering* as the endpoint.
Zettelkasten, PKM, library science, and Toulmin are named in prose but uncited —
mention, not attribution.

**Candidate cohort correction:** almost no foraging content. Its only
navigation-adjacent material is one table row, and that row has already been
split off into `design-for-the-first-time-human-except-on-access-cost`. It
probably does not belong in this cohort.

### pointer-design-tradeoffs-in-progressive-disclosure

C1 (a pointer is a lower-resolution representation supporting a load/skip
decision) is recalled as the IR/LIS **document surrogate**, high confidence. C3
(fixed / query-time / link-site, cut by *when the pointer learns about the
consumer*) is medium — the fixed-vs-query-time split is Tombros & Sanderson 1998
and per-link characterization is typed hypertext links, though the three-way
composition may be local. C4 is a real bounded-context delta with no
human-subjects analogue: a stateless agent's routing failure is a cliff, not a
slowdown, which defeats "compute the most specific pointer you can afford."

**Error found:** the reliability column conflates *availability* with *accuracy*.
Table 1 scores fixed pointers "Highest — always present, deterministic"; Table 2
gives them the failure mode "Stale if source changes." A stale description is
confidently wrong, which is worse than an absent one — as the KB's own
`stale-indexes-reduce-discovery-when-they-suppress-fallback-search` argues.

### charting-the-knowledge-access-problem-beyond-rag

Self-labelled brainstorming, which discounts any disposition applied to it. Six
claims, three recalled as established — the RAG critique (Bates berrypicking
1989; Belkin's ASK), the navigation-mode taxonomy (long jump vs local traversal
is near-literally teleporting vs orienteering), and multiple precomputed views
per corpus (LIS surrogate hierarchies, which the note's own "Historical analogy"
names without citing).

The most literature-exposed of the six and also the one already gesturing at the
right tradition. **The deficiency is missing citations, not missing awareness.**

## Cross-cutting findings

**1. Attribution is the sharper defect, not overlap.** Four of six cite nothing
external for claims placed in an outside tradition. Of the remaining two, one
names traditions in prose with zero works or authors, and one carries a
`has-external-sources` trait backed by an unnamed social-media post.

**2. The delta is real and concentrated.** The reliability axis, the degradation
cliff, and the dual-audience tension are claims about bounded-context stateless
consumers with no human-subjects analogue. **A disposition that counted only
overlap would strip these notes at exactly the points where they carry the
transfer argument** — the failure mode the workshop was built to avoid.

**3. Two candidate cohort corrections.** `human-llm-differences` probably does not
belong. `index-curation` does, but its literature is LIS reference work and PKM
Maps of Content, not information foraging — and the lineage is already drawn in a
sibling note.

**4. Four errors worth acting on whatever the literature says.** All survive any
ingest: the unscoped "generation cannot produce" that two ADRs rest on; the
availability/accuracy conflation in the reliability column; the skill-description
misfiling; and the `has-external-sources` trait on an unidentifiable source.

These keep landing. Across the cohort so far, **the defects found are worth more
than the rediscoveries** — which is a finding about the method, not just about
these notes: reading a note against a source surfaces errors that neither
in-corpus review nor the source ingest alone would reach.

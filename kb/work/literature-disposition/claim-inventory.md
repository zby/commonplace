# Claim inventory for the cohort

Built 2026-08-24, deliberately **before** reading any external source, so the
literature's vocabulary does not decide what counts as a claim — the ordering the
[first worked case](../source-grounding/worked-case-agents-navigate.md) followed.

**Epistemic status of the attributions.** Every `established-elsewhere` row below
is a *recalled* placement, not a read one. That is precisely the status this
workshop exists to distrust, so each row is a hypothesis with a named target for
the sibling workshop to adjudicate, and confidence is recorded honestly including
where it is low. A row is a reading assignment, not a verdict.

## Post-inventory update — 2026-08-26

The tables below remain the source-blind 2026-08-24 inventory. They are retained
as evidence of what the notes and model recall suggested before source reading;
later evidence should adjudicate those assignments, not be written backward
into them.

The claim-grounding rollout subsequently produced sixteen `literature handoff`
uses across ten notes. Only KSA-1, in
`knowledge-storage-does-not-imply-contextual-activation`, belongs to this
inventory's starting cohort. Its handoff remains open: Gao and Chen now provide
a bounded agent-documentation case that separates explicit consultation from
behavioral uptake, but they do not supply the primary
availability/accessibility or spontaneous-transfer evidence assigned here. The
other fifteen uses are new intake whose cohort membership must be decided; their
current source states are recorded in the [workshop
README](./README.md#received-claim-grounding-rollout-handoffs).

The operative source route has also changed since this inventory was built.
Current work grounds a use directly in retained exact `## Quotes` or in an exact
name-paired snapshot through a `(snapshot required)` link and the standard
`semantic/grounding-alignment` gate. References below to the rollout's former
normalized-Claims machinery are historical.

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

### index-completeness-does-not-determine-editorial-orientation

Formerly `index-curation-adds-orientation-that-generation-cannot-produce`.

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
`indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more` argues.

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

## Part 2: the remaining five

### The scoping finding, which outranks the per-note results

Of these five notes, **only one falls in the information-foraging / LIS cluster
both workshops scoped.** The traditions the claims actually place into:

| Note | Nearest tradition | In scope? |
|---|---|---|
| `knowledge-storage-does-not-imply-contextual-activation` | cognitive psychology of memory and transfer — Tulving & Pearlstone 1966 availability vs accessibility; Gick & Holyoak spontaneous-transfer failure | no |
| `an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract` | PKM / Zettelkasten — Luhmann hub notes, Milo LYT | **yes** |
| `indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more` | human-factors automation bias, omission errors — Skitka, Mosier & Burdick 1999; Parasuraman & Riley 1997; plus materialized-view maintenance | adjacent |
| `design-for-the-first-time-human-except-on-access-cost` | single-source publishing (DITA, docs-as-code); materialized views | no |
| `addressability-grain-sets-a-matched-selective-read-floor` | storage-systems **read amplification** and the DB **access path** (Selinger et al. 1979); IR passage retrieval | no |

**This falsifies a shared premise.** Both workshops were framed around a
"navigation cluster" needing a foraging/LIS corpus. The cohort was assembled from
note titles by an outside reader, and the titles misled: the actual literature
these claims need is wider and mostly elsewhere. A sibling workshop briefed only
on foraging, scent, berrypicking, exploratory search, and faceted classification
**could not adjudicate four of these five notes.**

Note the shape of the miss on `addressability-grain`. Connect rejected it from
the Pirolli tradition, correctly — "the source assumes the target is unknown,
which is the premise the note discharges." But rejection from the scoped
tradition read as *no external tradition*, when its mechanism is read
amplification: you pay for the smallest addressable unit regardless of record
size, in the same byte currency. Scoping a disposition to the wrong cluster does
not merely fail to find the source; it produces false confidence that the claim
is local.

### knowledge-storage-does-not-imply-contextual-activation — the 218 inbound edges, resolved

Measured, not estimated: **158 of 158** reviews in `kb/agent-memory-systems/`
cite it — 100%. All 158 citations sit in the `Relevant Notes:` tail; **zero**
appear in review body prose. All 158 reviews carry the required `## Read-back`
section. Dominant annotation labels: `distinguishes` (88), `applies` (17),
`contrasts` (8).

So the inbound count overstates the coupling in one direction and understates it
in another.

**Cheap to rewire.** The 158 are uniform, tail-position, mechanically greppable,
and carry no argument — no review argues *from* the note, quotes it, or disagrees
with it. A retarget is a scripted edit.

**But the real dependency is three files, not 163.**
`kb/agent-memory-systems/types/agent-memory-system-review.md:134` states:
"**Read-back is defined in [knowledge storage does not imply contextual
activation]** — including what does and does not count as it (retained memory
that accumulates from use, not shipped baseline documentation), and how it
differs from activation." The type spec delegates a *definition*; break it and
every review's required section loses its contract. `README.md` and
`review-framework-design.md` are the other two.

**The decisive structural fact: the established half and the depended-on half are
disjoint.** C1 and C2 — knowledge can be present without affecting the next
action — are recalled as Tulving's availability/accessibility distinction and the
inert-knowledge literature, uncited. C3, the operational definition of
**read-back**, is wholly local and is what 158 reviews and a type spec consume.
No external source supplies C3.

Therefore **thinning this note toward a pointer because its famous half restates
Tulving would destroy the half the system actually runs on.** If anything is
retired here it is the first two sections, and the read-back paragraph would need
promoting — most plausibly into `kb/notes/definitions/`, where the collection can
cite it directly.

### an-enforced-tag-readme — the advertised model, assessed

The critique called this the model of the right structure. **The form deserves
the praise; the evidence does not.**

The form is genuinely the best in the cohort — "A tag-README is a Map of Content
wearing a validator," an explicit novelty disclaimer heading the inherited
section, the delta stated as "old plus new," and a closing boundary saying which
sub-claim the machinery covers and what "stays editorial, un-contracted, and
inherited wholesale."

**But its attribution is named-but-unrouted**: "Luhmann" and "Nick Milo's LYT"
with no dated work, no URL, no `kb/sources/` ingest. That is exactly the recalled
background this workshop distrusts, dressed in citation clothing — which makes it
a *more* dangerous model than an openly uncited note, because copying the form
without fixing the evidence propagates the problem in a more convincing package.
Its pivotal claim is also an unsurveyed universal negative: "no Zettelkasten or
LYT practitioner writes 'this map lists every note on the topic' as an enforced
promise." The whole "the silence was not an oversight" move rests on it.

**The pattern, stated for reuse** — seven moves, in order:

1. Name the inherited artifact in the tradition's own vocabulary in the first
   sentence — an identification ("X *is* a Y wearing a Z"), not a gesture at a
   related tradition.
2. State the delta as an "old plus new" formula in the opening paragraph, so a
   reader who stops there already has the disposition answer.
3. Give the inherited half its own section that opens by disclaiming novelty.
4. Explain why the tradition lacked the added part **in terms of the tradition's
   own operating conditions**, as a correct choice under those conditions. This
   is the load-bearing move: it converts "we noticed what they missed" into
   "their conditions differed" — a claim about mechanism rather than about credit.
5. Flip those same named conditions one-to-one for the new consumer, same count
   and same order, so the correspondence is checkable.
6. Argue joint necessity: show what each condition alone would produce.
7. Draw the contract boundary explicitly — which sub-claim the machinery covers,
   and what remains inherited and uncontracted.

Plus an eighth this note does not do: **route the tradition claim to a dated
source**, and supply evidence for any negative claim about the tradition rather
than asserting it.

### Further errors found

- **`stale-indexes` C1 may be analytic rather than empirical.** It stipulates the
  stopping behaviour into the comparison — the consumer "would search current
  content if no index existed but accepts the index's result and stops when one
  does" — so the conclusion holds by construction and the claim cannot fail. But
  [ADR 026](../../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md)
  treats it as a finding, calling it "the problem in [this note] in its sharpest
  form." The empirical claim the ADR needs — that agents in fact stop on an
  apparently complete head — is assumed, not argued anywhere in the note.
- `design-for-the-first-time-human` C4 restates single-source publishing without
  saying so; its real delta is C3, that the divider is access *mode* rather than
  consumer identity.

## Running tally

Across all eleven notes inventoried, the source-blind count stood at **three
defects** — two operative ones, the unscoped "generation cannot produce" under
ADRs 025/026 and the possibly-analytic `stale-indexes` C1 under ADR 026; plus the
prose-only pointer-context monotone — against **zero clean rediscoveries that a
retirement would tidily remove**. The method keeps returning errors where it was
pointed at redundancy.

**Execution update, 2026-08-24.** The pointer-context monotone was subsequently
removed from `agents-navigate-by-deciding-what-to-read-next` and its sole
inheritor, `linking-theory`, during the claim-pull rollout. The categorical
`index-curation` claim was renamed and scoped to distinguish complete membership
from editorial orientation; the revised claim was propagated through ADR 025,
ADR 026, and its dependent MOC note. At that date the possibly-analytic
`stale-indexes` defect remained open; the zero-clean-rediscoveries finding was
unchanged.

**Intake update, 2026-08-25.** Neither the Gao–Chen source nor the sixteen
rollout handoffs changes that tally or supplies a final artifact disposition.
They add bounded evidence and a triaged source/target queue. The first
keep, merge, thin, or retire decision remains to be made and executed end to
end.

**Execution update, 2026-08-26.** Re-checking the current note and ADR 026 found
that the conditional control-flow mechanism did not need prevalence evidence,
but its title omitted a necessary condition: the suppressed retrieval must
produce greater realized task-relevant coverage. The note is now
`indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more`; its
title, thesis, scope, and dependent summaries carry that condition. ADR 026
still rests on it because Commonplace explicitly tells exhaustive consumers to
skip the by-tag sweep under `complete: true`.

The same pass separated pointer availability from accuracy, moved skill
descriptions out of source-local link-following, narrowed resolution fluidity to
a qualitative criterion, repaired the superseded dual-audience navigation row,
and dropped the false external-source trait. All three defects in the running
tally are now repaired. The zero-clean-rediscoveries finding and the absence of
a first artifact disposition are unchanged.

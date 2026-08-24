# Disposition of notes whose content is established outside Commonplace

## Governing question

For each note whose substance is already established in external literature,
should it be retired into a source route, thinned to a normalized claim node,
rewritten around the part Commonplace actually adds, or left as it is — and is
there a general rule, or only per-note judgments?

The upstream half — which sources are authoritative, what an ingest must
extract, and whether the graph needs a thin claim node at all — belongs to
[source-grounding](../source-grounding/README.md). This workshop owns what
happens to the notes.

## Current status — 2026-08-24

**Open.** The starting cohort has twelve candidates. The first was inventoried
and checked against an actual source in the worked case; the other eleven have
claim inventories and candidate reading assignments. No candidate yet has a
final dated disposition.

| Closure condition | State | What remains |
|---|---|---|
| Source-grounded disposition for every settled cohort member | Open | Settle cohort membership, capture the claim-selected corpus, and adjudicate the eleven unworked candidates. The worked candidate's final artifact disposition is also open. |
| One disposition executed end to end | Open | The first case produced and executed a claim correction, not a final keep, merge, thin, or retire decision. |
| General disposition rule | Open | The evidence supports claim-level, source-grounded judgment, but no rule or no-general-rule finding has been promoted. |
| Write-time check decision | Partial | ADR 073 guards explicit new or changed source dependencies. It cannot discover unattributed prior art, which is the check this closure condition still needs decided. |

The claim-side repair and source-grounding machinery no longer block progress.
The operative `index-curation` claim has been scoped without destabilizing its
dependent ADRs. The next unblocked work in
[Channel 2](./three-channels.md#channel-2--claims-to-change) is to re-check
`stale-indexes` before deciding whether to change it. Most final dispositions
still wait on the wider source corpus.

## The parallel worth exploiting, and where it breaks

[The seven-case documentation disposition
evidence](../../notes/evidence/seven-documentation-cases-left-routing-and-synthesis.md)
asks the same shape of question about a different recovery authority: should a
description of shipped-system state exist when the code can regenerate it? Its
method is transferable and should be borrowed rather than reinvented:

- recoverability attaches to **units of content, not to artifacts**, so an
  artifact can be part retire and part keep;
- disposition is determined **by search, not by reading**. That workshop
  recorded a load-bearing error — asserting recoverability as settled
  background licensed judging passages by reading them, which produced two wrong
  calls in the first worked case before the search caught them;
- dispositions carry **a date and the basis they were decided on**, because the
  mixture drifts;
- **worked cases before general rules**, and "no general rule" is a finding.

Where the parallel breaks, and it breaks in a way that should change the answer:

**Recovery from code is cheap; recovery from literature is not.** Re-reading
`src/` costs a file read. "See Pirolli and Card" costs obtaining a paper that
may be paywalled, long, and about human subjects. The ingest stands in for the
source, so **the ingest's fidelity is load-bearing here in a way live source
never was there.** A retirement into a source route is only as good as the
ingest it routes to — which is why this workshop depends on the sibling one.

**Code recovery preserves the conclusion; literature recovery does not.** The
code *is* the system being described, so a recovered description is about the
same object. A human information-seeking result is about a different consumer.
Whatever survives must still carry the argument that the mechanism transfers.
That argument is Commonplace's own, is recoverable from nothing, and is the
thing most likely to be lost by a disposition that only counts overlap.

## What is already settled

**The literature was not ingested at workshop opening.** Measured 2026-08-24:
no source ingest in
`kb/sources/` covered information foraging, scent, berrypicking, exploratory
search, orienteering, faceted classification, or generated navigation, so the
cluster's claims were written from recalled background. One ingest has since
landed (`pirolli-proximal-information-scent-distal-content`); the rest of the
gap stands. The [claim inventory](./claim-inventory.md) found that the corpus
needed is wider than this list, and the sibling workshop has not yet decided it.
[`links-README.md`](../../notes/links-README.md) says so in its own words:
"**TODO:** This survey is from the agent's training data, not systematic."

**Prospective source grounding is operative; prior-art discovery is not.**
[ADR 073](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md)
adds immutable Claims entries to tracked ingests, a guard in the two promoted
writing skills for explicit new or materially changed source dependencies, and
source review pairs over artifact-to-ingest uses. That machinery starts only
when the candidate already names the dependency. It does not ask whether an
uncited claim is established elsewhere. Every novelty and economy test remains
KB-internal. The novelty battery in
[`evaluate-log-entry-for-note-creation.md`](../../instructions/evaluate-log-entry-for-note-creation.md)
compares a candidate against existing *Commonplace* notes. `cp-skill-write`'s
duplicate guard is a targeted `rg` in the target collection. The attribution
gates audit already-cited targets; none searches for a missing source. The gap
the critique names in its step 8 therefore remains, but it is now narrower than
"no write-time check."

**Retirement is a defined nine-step procedure with a human stop.**
[`retire-artifact.md`](../../instructions/retire-artifact.md) requires: extract
surviving content first, one piece per commit, never bundled into the
retirement; **inventory inbound references and stop for user approval before
editing anything**; retarget by reader need; `git rm`; add a one-hop published
redirect to `redirect_maps` in `properdocs.yml`; and retire freshness baselines
via `commonplace-freshness-status --missing` piped into
`commonplace-freshness-retire`. There is no `commonplace-retire`, and
`commonplace-relocate-note` does not re-key or retire baselines. Nothing in this
workshop bypasses that procedure.

## What a later session should not assume

**That the cluster is rediscovery.** The [input critique](./chatgpt-critique.md)
asserts that several of these notes are information-foraging theory in local
vocabulary. Establishing that means reading the sources; treating the diagnosis
as settled background is the exact error the documentation disposition sweep
already paid for once. **One note has now been checked and the diagnosis came
back only half right** — see the received findings below. Extrapolating from it
to the other eleven would repeat the error at one remove.

**That the four dispositions are a menu to allocate across.** Retire / thin
node / rewrite around the delta / leave operative documentation alone are
candidates. A fifth may fit better, and one note may need different dispositions
for different regions.

**That the per-note table in the critique is a plan.** It was produced without
reading the sources it appeals to and without reading the notes' downstream
dependents. Its rows are hypotheses with a proposer, not assignments.

**That overlap counts decide anything.** A note can restate an established
result and still be load-bearing because it is where the transfer argument
lives, because many notes cite it as a normalized premise, or because it holds a
local boundary the literature does not draw. Overlap is an input to the
judgment, not the judgment.

**That a stub is the cheap default.** The critique's opening point is that
reducing every note to a one-paragraph pointer preserves the duplication in a
cheaper form while adding a navigation hop. Separately,
`kb/notes/COLLECTION.md`'s theory-independence constraint may not even permit a
pure pointer. Both cut against reflexive thinning.

## Starting cohort

The notes the critique names, with library inbound-reference counts measured
2026-08-24 by `rg -l "<slug>.md"` across `notes reference instructions types
agent-memory-systems agentic-systems articles sources`. Counts are a rewiring
cost estimate, not a disposition signal.

| Note | Tags | Inbound |
|---|---|---|
| `agents-navigate-by-deciding-what-to-read-next` | links | 19 |
| `stale-indexes-reduce-discovery-when-they-suppress-fallback-search` | kb-maintenance | 26 |
| `human-llm-differences-are-load-bearing-for-knowledge-system-design` | document-system | 13 |
| `design-for-the-first-time-human-except-on-access-cost` | document-system, context-engineering | 10 |
| `link-following-and-search-impose-different-metadata-requirements` | links | 7 |
| `a-knowledge-base-should-support-fluid-resolution-switching` | foundations | 7 |
| `pointer-design-tradeoffs-in-progressive-disclosure` | links, computational-model | 7 |
| `index-curation-adds-orientation-that-generation-cannot-produce` | kb-maintenance | 6 |
| `charting-the-knowledge-access-problem-beyond-rag` | foundations | 5 |
| `addressability-grain-sets-a-matched-selective-read-floor` | document-system, context-engineering | 4 |
| `an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract` | kb-maintenance, document-system | 3 |
| `knowledge-storage-does-not-imply-contextual-activation` | llm-reliability, failure-modes, evaluation | 217 |

Two things the table already shows. The last row is 163 citations from
`kb/agent-memory-systems/` reviews alone — that note is infrastructure for a
whole collection, and any disposition touching it is a different scale of
change. And the cohort spans five tags, so a tag-README restructure is not one
README.

Membership is a finding to re-test, not a fixed list. The cohort was assembled
by an outside reader from note titles; notes elsewhere in the KB may have the
same problem, and some of these may not have it at all.

**Re-tested 2026-08-24, and the framing was wrong in a way that matters.** This
is not one cluster with one literature. The [claim inventory](./claim-inventory.md)
placed the cohort's claims into cognitive psychology of memory and transfer,
human-factors automation bias, materialized-view maintenance, single-source
publishing, storage read amplification, and PKM — with information foraging
covering only part of it. "Navigation cluster" was a reading of the titles, not
of the claims. Any disposition scoped to a foraging corpus would fail to
adjudicate most of these notes, and — the sharper risk — would read *rejection
from foraging* as *no external tradition*, producing false confidence that a
claim is local.

## Received: the first source-grounding case

`agents-navigate-by-deciding-what-to-read-next` was taken through the full chain
against a captured, read source (Pirolli on proximal information scent) on
2026-08-24. Recorded here rather than only in the sibling workshop, because that
workshop closes and is deleted while this one still needs the result.

**The critique's diagnosis was half right, and the half it missed matters more.**
At first examination, three uncited claims overlapped the source — the
follow/skip unit, the probabilistic judgment under uncertainty, and the proximal
cue that lets a reader judge without loading the target. **A stricter blind
re-run found that overlap is not subsumption**: the source does not establish
the "fundamental unit" wording, does not compose its two separate results into a
pointer-level tradeoff, and supports only the proximal/distal core of the third.
All three needed narrowing rather than deletion. A fourth claim, "the more
context a pointer carries, the cheaper the navigation decision," was **not** in
the source and was wrong by the source's own lights: it merged estimate quality
with interaction cost where the source separates them, and the source's nearest
test fixed cue size rather than varying it. Three further claims were local and
absent from the source. See the [worked
case](../source-grounding/worked-case-agents-navigate.md).

So the note is **not** the clean rediscovery case the critique proposed. A note
whose central design claim is wrong is not obviously a retirement candidate — it
may be a correction candidate, and retiring it would delete the error without
correcting anything that inherited it.

**The correction landed later on 2026-08-24.** The note now links the Pirolli
ingest, narrows the source-side claims, states the human-to-LLM transfer boundary,
and replaces the monotone with uncertainty reduction per unit of context.
`linking-theory` received the same source route and correction. Source review
pairs passed for both artifacts with no stale pair. This executes the claim
repair and its one known propagation edge; it does **not** settle whether the
first note should ultimately survive, merge, thin, or retire.

**The critique's per-note table was contradicted where it was checked.** Connect
rejected three cohort notes as belonging to this tradition, with reasons:
`index-curation` ("nothing that discriminates *curated* from *generated*
listings, which is the note's entire claim"), `addressability-grain` ("the source
assumes the target is unknown, which is the premise the note discharges"), and
`a-knowledge-base-should-support-fluid-resolution-switching` ("the source's
switching is lateral, not vertical"). The critique had proposed retiring or
partly retiring two of those three into the literature route.

**One batch found in passing.** Three artifacts carry standing "survey is from
training data" TODOs inside this tradition — `links-README.md`,
`title-as-claim-enables-traversal-as-reasoning.md`, and
`information-value-is-observer-relative.md`. They are one batch, not three, and
only the first is in the current cohort.

## Boundaries

In scope:

- notes in `kb/notes/` whose substance may be established externally
- link rewiring, retirement execution, and the tag-README consequences
- whether a write-time check belongs in `kb/notes/COLLECTION.md`, in the
  log-entry novelty battery, in a review gate, or nowhere

Out of scope as artifacts:

- ADRs, type specs, and current-state reference documentation. They define what
  Commonplace does; their job is not theoretical novelty, and they should not be
  shrunk because their rationale rests on established theory. They may need
  *added* source routes while staying self-sufficient to operate the system.
- Source selection and the ingest contract — [source-grounding](../source-grounding/README.md)
- Link-label semantics — [linking-foundations](../linking-foundations/README.md)
  and [linking-contract-consistency](../linking-contract-consistency/README.md)

## Dependency

Dispositioning depends on the sibling workshop's ingests: you cannot find that a
note restates a source you have not read. But the left-hand side of the
subsumption record — which claims each note actually makes, and which downstream
artifacts depend on each claim — is independent of any ingest and can start now.
Doing that first also makes the ingests better, because it tells the sibling
workshop which claims the corpus has to adjudicate.

## What closes this workshop

1. Every note in the settled cohort has a **dated** disposition with a reason
   grounded in an actual source, not in a resemblance.
2. At least one disposition executed end to end as a worked case — including
   inbound rewiring and, if it is a retirement, the full `retire-artifact.md`
   procedure with its approval stop.
3. The general rule promoted, or the finding recorded that disposition is
   per-note with no general rule.
4. A decision on the write-time check: promoted to wherever it belongs, or the
   recorded finding that the existing intra-KB novelty tests should not grow an
   external-literature arm, with the reason.

## Files

- [Grounding cleanup procedure](./cleanup-procedure.md) — restored after the
  claim-pull workshop deleted it on closure with 66 of 68 citing notes still
  ungrounded; carries the corpus state at freeze
- [Cleanup cohort 01 — reconstructed](./cleanup-cohort-01.md) — the claim-pull
  rollout's own run, rebuilt from diffs after being deleted with all eight
  completion rows still `pending`: six narrowed, two contradicted, zero grounded
  as written
- [Cleanup cohorts 03–07](./cleanup-cohort-03.md) — 24 notes in five manifests,
  mutually disjoint from each other and from cohort 02 on both notes and ingests,
  so all six run in parallel without coordination
- [Cleanup cohort 02](./cleanup-cohort-02.md) — first cohort under the restored
  procedure: five targets, 16 pairs, frozen at `6cdb3c10`, with a predicted
  disposition distribution to judge the run against
- [Three channels: migration, claims, machinery](./three-channels.md) — every
  finding sorted by kind of change, with verification status per row and a
  sequencing argument against migrating first
- [Claim inventory for the cohort](./claim-inventory.md) — per-note load-bearing
  claims with recalled tradition placements as reading assignments, not verdicts;
  the cross-cutting finding is that attribution defects and outright errors
  outnumber clean rediscoveries
- [How far the pointer-context monotone actually spread](./c4-propagation-sweep.md)
  — 2026-08-24 sweep of all 20 citing artifacts: one inheritor by verbatim copy,
  zero operative reach, and the shipped description band already set on the
  corrected rationale by a July retrieval assay
- [External critique of the navigation cluster](./chatgpt-critique.md) — the
  pasted 2026-08-24 input that opened this work; unedited, and its diagnosis,
  disposition table, and migration order are all candidate proposals

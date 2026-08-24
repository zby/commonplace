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

## The parallel worth exploiting, and where it breaks

[documentation-disposition](../documentation-disposition/README.md) asks the
same shape of question about a different recovery authority: should a
description of shipped-system state exist when the code can regenerate it? Four
worked cases in, its method is transferable and should be borrowed rather than
reinvented:

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

**The literature is not ingested.** Measured 2026-08-24: no source ingest in
`kb/sources/` covers information foraging, scent, berrypicking, exploratory
search, orienteering, faceted classification, or generated navigation. So the
cluster's claims were written from recalled background.
[`links-README.md`](../../notes/links-README.md) says so in its own words:
"**TODO:** This survey is from the agent's training data, not systematic."

**No write-time check anywhere asks whether the literature already settles a
claim.** Every novelty and economy test in the corpus is KB-internal. The
novelty battery in
[`evaluate-log-entry-for-note-creation.md`](../../instructions/evaluate-log-entry-for-note-creation.md)
compares a candidate against existing *Commonplace* notes. `cp-skill-write`'s
duplicate guard is a targeted `rg` in the target collection. The attribution
gates (`grounding-alignment`, `concept-attribution`, `conceptual-role-conflation`,
`unidentified-references`) all audit attribution to *already-cited* targets;
none requires that a source exist. `explication-quality` asks a definition to
name its explicandum, but is type-gated to definitions. So the gap the critique
names in its step 8 is real and measured, not conjectured.

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
vocabulary. That is plausible — `agents-navigate-by-deciding-what-to-read-next`
states the scent mechanism almost in its canonical form and cites nobody for it
— but plausible is not established, and establishing it means reading the
sources. Treating the diagnosis as settled background is the exact error
`documentation-disposition` already paid for once.

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

- [External critique of the navigation cluster](./chatgpt-critique.md) — the
  pasted 2026-08-24 input that opened this work; unedited, and its diagnosis,
  disposition table, and migration order are all candidate proposals

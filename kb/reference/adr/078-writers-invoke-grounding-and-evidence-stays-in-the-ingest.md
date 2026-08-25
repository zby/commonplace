---
description: "Accepted decision that the promoted writers invoke cp-skill-ground automatically and report every quotes-added append, that creating a missing ingest stays manual, and that bounded evidence stays in the ingest Quotes pool"
type: ../types/adr.md
tags: []
status: accepted
---

# 078-Writers invoke grounding and evidence stays in the ingest

**Status:** accepted
**Date:** 2026-08-25

## Context

[ADR 076](./076-source-claim-grounding-is-a-promoted-skill.md) gave grounding a
routable entry — `cp-skill-ground`, the sole writer of an ingest's `## Quotes`
section — but deliberately left the writers stopping. A note whose source
evidence was insufficient could not be finished in one run: the writer reported
a skill call and the operator invoked it, then restarted the write. The reason
for the stop was mutation authority, not ergonomics. A request to write one
artifact would cause a second artifact to be edited, and that footprint had not
been weighed.

Two things bound that footprint. The append is append-only and byte-preserving,
and `commonplace-validate` resolves every `Source extract (verbatim)` against
the name-paired pinned snapshot, so no agent certifies its own transcription
([ADR 073](./073-untracked-source-snapshots-require-ingest-grounding.md)). And
the writers already stop at exactly the guard that would trigger the call, so
automatic invocation adds no new detection surface — only a continuation.

The proposal *Source-claim grounding skill and evidence-retention boundary*
carried this question together with a second one it left open: whether bounded
source evidence should live in the ingest Quotes pool, in a companion artifact,
in the target, or nowhere. Both are settled here, and the proposal is
archived.

## Decision

**The promoted writers invoke `cp-skill-ground` automatically.** When a guarded
source dependency's ingest exists and its Quotes are insufficient,
`cp-skill-write` and `cp-skill-write-multistage` invoke `cp-skill-ground` with
`Target` and `Claim needed` and act on the returned route: `quotes sufficient`
or `quotes added` — re-read the Quotes section and apply the
`semantic/grounding-alignment` gate against it; `snapshot required` — take the
snapshot route; a blocker — stop before saving, or record the blocker in the
workshop and leave the live target untouched.

**Every `quotes added` result is reported with its ingest path** in the writer's
final report, and in the workshop `README.md` for multistage. An ingest
mutation caused by a request to write a note is never a silent side effect.

**Creating a missing ingest stays manual.** A dependency naming a URL with no
tracked ingest is a stop or blocker that names the exact URL for a separate
`cp-skill-ingest` run. The writers never create source records and never edit
an ingest themselves. The two mutations differ in kind: the append is
append-only, exact-byte verified against pinned bytes, and visible in the diff,
so its authority footprint is small; creating an ingest is a network capture
plus a drafting worker, a different order of side effect.

**Bounded evidence stays in the ingest Quotes pool; ADR 073 stands.** No
comparison experiment is run first. The only force offered against the current
design was a design smell — a shared, demand-grown mutation surface inside an
artifact that also owns source identity and analysis — with no observed
failure. Reopen on a recorded concrete force: evidence-reuse contention, an
ingest made unreadable by quote volume, or a portability failure.

## Considered alternatives

**Keep the stop.** Writers keep reporting the skill call and waiting, which
holds ingest mutation behind a separate operator invocation and preserves a
manual retry point. Rejected: the retry costs a full re-entry into the write for
a mutation whose correctness is already checked by code, and the operator's
decision at that point is not informed by anything the writer does not already
have.

**Let grounding also create a missing ingest automatically.** Rejected on the
boundary above — an automatic write would then add a source artifact, not just
extend one, and would pull a network capture and a drafting worker inside a
request to write a note.

**Evidence in a separate grounding artifact.** A companion would separate
source analysis from retained evidence, pooled per source or owned per target
use. Rejected for lack of a force: it requires a new type, a declared relation,
validator support, a retargeted writer, and a gate route, and nothing observed
so far says the ingest is the wrong owner.

**Evidence in the target artifact.** Claim and quote would change together, so
no source artifact would be mutated and ordinary target freshness would cover
both. Rejected: it duplicates common quotations across targets and imposes an
evidence convention on every target type.

**Nowhere: always require the snapshot.** This removes bounded-evidence writes
entirely, but makes every source-dependent use non-portable and potentially
expensive to review. Rejected; the marker route stays available for the
exceptional case where quotes genuinely cannot carry the check.

**Run a prospective comparison before deciding.** The proposal's own candidate:
compare the ingest pool against at least one non-ingest route on live writes,
observing reuse, extra mutation, portability, and drift into target repair.
Rejected as an experiment with no motivating failure; the trigger conditions
above replace it.

Free choices from the proposal, resolved: automatic invocation begins in
ordinary writing and multistage together, not in one first; missing-ingest
creation is not automatic; there is no separate evidence artifact, so the
pooled-versus-per-use question does not arise; and persistence follows
successful evidence selection automatically, since the append is the grounding
run's normal completion rather than a separately authorized effect. Left open:
whether review-repair workflows should invoke grounding the same way.

## Consequences

A note write can complete in one run when the source is already ingested, which
removes the grounding-and-retry round trip ADR 073 accepted as a cost. The
writer's final report becomes the place where an ingest mutation is visible, so
a report that omits a `quotes added` line hides a real change — the convention
carries weight it did not carry when the writer mutated nothing.

The proposal's stated risk — automatic grounding becoming automatic
confirmation — is bounded rather than removed. `cp-skill-ground` returns
non-support as a blocker instead of a weak pass, and `semantic/grounding-alignment`
remains an independent retrospective check that reads the retained extracts.
What automation adds is the mechanical, exact-byte-verified half; the semantic
half stays outside the writer.

Operativity path: `kb/instructions/cp-skill-write/SKILL.md` and
`kb/instructions/cp-skill-write-multistage/SKILL.md` carry the invocation,
route handling, and reporting rules, and `kb/instructions/cp-skill-ground/SKILL.md`
carries the result protocol they consume. All three are promoted skills loaded
by harness skill selection; the force is the skill body, not a validator.

Where the decision stops applying: it binds the two promoted writers and no
others — an agent writing a note outside `cp-skill-write` or
`cp-skill-write-multistage` is not covered, and neither are review-repair
workflows, which stay an open question. Installed projects inherit the same
skills through scaffolding, so the boundary travels with them unchanged. The
evidence-location half is scoped to bounded verbatim extracts under ADR 073's
mutation contract; it says nothing about evidence forms that contract does not
support, such as rewritten or removed incumbent quotes.

The alternatives above are the frontier record of the option space; the
archived proposal keeps the dated current-state anchor and the rollout
measurement (44 of 59 uses grounded as written) for a decision audit.

---

Relevant Notes:

- [ADR 076 — Source-claim grounding is a promoted skill](./076-source-claim-grounding-is-a-promoted-skill.md) — extends: closes the automatic-invocation question that promotion deliberately deferred
- [ADR 073 — Untracked source snapshots require ingest grounding](./073-untracked-source-snapshots-require-ingest-grounding.md) — extends: keeps its ingest Quotes pool and snapshot marker as the evidence design and removes the grounding-and-retry round trip it accepted
- [Ground a source-dependent claim](../../instructions/cp-skill-ground/SKILL.md) — implemented-by: the skill whose result protocol the writers now consume in-run
- [Write a KB note](../../instructions/cp-skill-write/SKILL.md) — implemented-by: the writer that invokes grounding and reports every append
- [The boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — rests-on: exact-byte verification licenses the mechanical append while leaving semantic support outside the automated step

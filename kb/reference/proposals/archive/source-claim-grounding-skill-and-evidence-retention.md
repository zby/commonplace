---
description: "Proposal (adopted by ADR 076 and ADR 078): let writers invoke the grounding skill automatically while deciding whether retained evidence belongs in an ingest, beside it, in the target, or only in the pinned snapshot"
type: ../../types/design-proposal.md
tags: []
---

# Source-claim grounding skill and evidence-retention boundary

Commonplace has a promoted grounding skill, but promoted writers do not invoke
it and continue. They stop and hand the operator a skill call. Letting writers
invoke it in-run would compose grounding into a single write.

The grounding skill may also append quotations to an ingest itself. Automatic
invocation would therefore make a request to write one artifact capable of
mutating another. Whether writers should invoke grounding automatically and
where its evidence should persist are separate design choices.

## Current state (as of 2026-08-25)

- [`cp-skill-ground`](../../../instructions/cp-skill-ground/SKILL.md) is a
  promoted, user-invocable skill since
  [ADR 076](../../adr/076-source-claim-grounding-is-a-promoted-skill.md), adopted
  2026-08-25 from this proposal's "promote for explicit use" option. It takes
  one source identity and one source-side need, reads exact retained Quotes or
  the checksum-matched snapshot, and does not edit the target.
- [`cp-skill-write`](../../../instructions/cp-skill-write/SKILL.md) and
  [`cp-skill-write-multistage`](../../../instructions/cp-skill-write-multistage/SKILL.md)
  detect insufficient source evidence but stop and report the skill invocation
  instead of running it.
- Under [ADR 073](../../adr/073-untracked-source-snapshots-require-ingest-grounding.md),
  an ordinary ingest link declares its Quotes sufficient. A link marked
  `(snapshot required)` declares that semantic checking needs the exact local
  snapshot.
- [`cp-skill-ingest`](../../../instructions/cp-skill-ingest/SKILL.md) creates and
  re-ingests source records only; it has no quote-append path.
  `cp-skill-ground` performs the append itself and is the sole writer of an
  ingest's `## Quotes` section, under name-paired snapshot, source-identity,
  checksum, splice-scope, byte-preservation, and restore-on-failure guards.
- Exact-quote verification is deterministic in `commonplace-validate`: it
  resolves every `Source extract (verbatim)` against the name-paired snapshot
  and fails on one that does not occur. No agent verifies its own
  transcription.
- In the direct Quotes/snapshot rollout, 44 of 59 source-dependent uses were
  grounded as written. The remainder needed narrowing, repair, retained local
  reasoning, or literature handoff. Evidence preparation is reusable; target
  disposition is not mechanical.

## The two decisions

### Should writers invoke the grounding skill automatically?

**Keep the stop.** Writers continue to report the skill call and wait. This
keeps mutation behind a separate invocation but preserves the manual retry.
The writer instruction remains the operative routing surface.

**Let writers invoke it automatically.** The existing named-source guard
becomes the trigger. The grounding result controls whether the caller can
continue, while target repair remains with the writer and semantic assurance
remains with
[`semantic/grounding-alignment`](../../../instructions/review-gates/semantic/grounding-alignment.md).
The promoted writers and the skill invocation channel together make the change
operative.

Automatic invocation is the candidate direction. It does not itself decide
whether the grounding run may persist evidence.

### Where should bounded source evidence persist?

**In the ingest Quotes pool (current design).** Exact passages are shared across
uses and available in a fresh checkout. The cost is a shared, demand-grown
mutation surface inside an artifact that also owns source identity and analysis.
The source contract, ingest type, `cp-skill-ground`, validator, and grounding
gate already make this route operative.

**In a separate grounding artifact.** A companion could separate source
analysis from retained evidence. It could be pooled per source or owned by one
target use; that finer choice should follow evidence about reuse, contention,
and artifact count. A new type, declared relation, validator, writer, and gate
route would be required before such an artifact had authority.

**In the target artifact.** Claim and exact evidence would change together, so
no source artifact would be mutated and ordinary target freshness would cover
both. The cost is duplicated quotations and an evidence convention imposed on
different target types. Target contracts, exact-source validation, and the
grounding gate would have to consume the retained form.

**Nowhere: always require the snapshot.** This removes bounded-evidence writes
but makes every source-dependent use non-portable and potentially expensive to
review. The existing marker and grounding gate already implement this route.

An ephemeral skill result is not durable grounding. If no bounded evidence is
retained, the target must declare its snapshot dependency so a later reviewer
can fail closed rather than trust a prior agent's conclusion.

## Where the append role lives

The case for a separate mechanical append owner is closed. `cp-skill-ground`
now selects the passages and writes them, and the independent check that the
split used to supply comes from `commonplace-validate` instead: a skill that
merges selection with persistence no longer certifies its own transcription,
because no agent's reading is the verification.

What remains open is downstream of the retention choice. The append role
belongs wherever the evidence lands. If evidence moves out of the ingest,
`cp-skill-ground` keeps the role and retargets it — writing the new evidence
artifact under the same exactness, preservation, and rollback guards, with the
validator resolving extracts against the pinned source — and the ingest stops
being a mutation target at all.

`cp-skill-ingest` retains only its separate role of creating a missing source
record. Whether an automatic grounding run may invoke it to create one is a
distinct mutation-authority choice: it decides whether an automatic write may
add a source artifact, not where evidence lives.

## Forces

- **Composition versus hidden mutation.** One uninterrupted write is cheaper,
  but its side effects must match the authority implied by the request.
- **Fresh context versus target fidelity.** Source isolation limits
  confirmation from thematic overlap, but skill packaging does not deliver it:
  a `context: fork` skill inherits the invoking conversation, so isolation
  would require a fresh sub-agent with a minimal brief. The caller must still
  preserve the claim it intends to test.
- **Reuse versus ownership.** Pooled evidence avoids duplication. Per-use or
  target-owned evidence gives clearer mutation and freshness boundaries.
- **Portability versus completeness.** Small tracked extracts make ordinary
  review portable; full snapshots preserve context but are ignored local state.
- **Mechanical verification versus semantic warrant.** Exact-byte checking can
  verify transcription. It cannot establish that a source supports the target
  claim or its transfer.
- **Current implementation versus artifact fit.** The append machinery inside
  `cp-skill-ground`, together with the validator's exact-quote resolution
  against the name-paired snapshot, lowers the cost of keeping the current
  design but does not settle whether the ingest is the right evidence owner.

## Candidate direction

Let writers invoke the grounding skill automatically after they have fixed the
source-side need. Keep the grounding skill separate
from target repair and from the independent semantic gate.

Do not yet select the persistence path. First compare the current ingest pool
with at least one non-ingest route on prospective writes. The comparison should
observe evidence reuse, extra artifact mutation, review portability, and how
often a supposedly grounding run instead changes the target claim.

## Free choices

- Whether automatic invocation begins with ordinary writing only or also enters
  multistage and review-repair workflows.
- Whether a missing ingest may be created automatically from an exact supplied
  URL.
- Whether a separate evidence artifact is pooled per source or owned per target
  use.
- Whether persistence follows successful evidence selection automatically or
  remains a separately authorized effect.

## Adoption criteria

- The promoted operation has a small composable result that distinguishes usable
  evidence, snapshot dependence, non-support, and a blocker without becoming a
  new source-authority layer.
- Exact retained passages are checked independently against the pinned source;
  the grounding skill does not certify its own transcription or semantic
  conclusion. For the current ingest route the transcription half is already
  met by `commonplace-validate`; the semantic half remains with
  `semantic/grounding-alignment`. A non-ingest retention route must carry both
  halves over.
- The chosen retention route gives the grounding gate direct source text,
  declares fresh-checkout behavior, and has one visible mutation owner.
- Automatic composition removes the current retry without silently absorbing
  target repair, semantic review, or corpus-wide evidence extraction.
- Adoption changes the selected retention contract, its writer, validation,
  gate routing, and promoted-skill consumers together.

## Risks

- Automatic invocation can hide a wider mutation footprint behind convenient
  routing.
- A companion can become a second ingest; per-use records can turn citations
  into excessive maintenance state.
- Target-owned quotations can distort prose and duplicate common evidence.
- Automatic grounding can become automatic confirmation unless non-support and
  contradiction remain normal outcomes.

---

Relevant Notes:

- [Skills are instructions plus routing and execution policy](../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) — rests-on: promotion adds a structured invocation channel a caller can compose against
- [An author should fix what the executor cannot determine, not what it will](../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) — rests-on: this proposal selects architecture boundaries rather than prewriting the eventual skill
- [The boundary of automation is the boundary of verification](../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — rests-on: exact-byte verification licenses mechanical persistence but not semantic support
- [ADR 073: Untracked source snapshots require ingest grounding](../../adr/073-untracked-source-snapshots-require-ingest-grounding.md) — compares-with: the current ingest-Quotes and snapshot-marker design whose retention boundary remains open here
- [ADR 076: Source-claim grounding is a promoted skill](../../adr/076-source-claim-grounding-is-a-promoted-skill.md) — compares-with: the explicit-use promotion already adopted from this proposal, leaving automatic invocation open
- [`cp-skill-ground`](../../../instructions/cp-skill-ground/SKILL.md) — procedure: the promoted operation whose automatic invocation this proposal argues for

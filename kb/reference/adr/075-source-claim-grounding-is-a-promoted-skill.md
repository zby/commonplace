---
description: "Accepted decision that source-claim grounding is the promoted skill cp-skill-ground, the single advertised entry for deciding which quotes an ingest retains, with cp-skill-ingest reduced to its mechanical callee"
type: ../types/adr.md
tags: []
status: accepted
---

# 075-Source-claim grounding is a promoted skill

**Status:** accepted
**Date:** 2026-08-25

## Context

[ADR 073](./073-untracked-source-snapshots-require-ingest-grounding.md) made one
procedure responsible for deciding what source evidence a claim needs: read the
ingest's `## Quotes`, then either declare them sufficient, retain the minimum
verbatim excerpts through `cp-skill-ingest`'s `quote_append_request`, or declare
`snapshot required`. That procedure was a plain instruction addressed by file
path.

Its only inbound routes were the stop-and-report handoff inside `cp-skill-write`
and `cp-skill-write-multistage`, ADR 073 itself, and the rollout workshop. A
request that does not start inside a writer — an operator asking to retain a
quote that supports a discussion — had no route at all. Because instructions are
addressed by path, the writers' handoff also had to carry two literal routes,
one for the source checkout and one for an installed project.

The unrouted request did not stay unrouted; it matched the wrong surface.
`cp-skill-ingest` advertised "mechanically append verified verbatim quotes", so
an agent holding that request matched the ingest skill, invoked it with a
natural-language target, and the skill selected quotes anchored to no claim.
That happened on 2026-08-25 and forced the choice: one request had two
advertised surfaces, and the one it reached did not own the decision.

Two standing claims decide where the procedure belongs.
[Capability placement should follow autonomy readiness](../../notes/capability-placement-should-follow-autonomy-readiness.md):
a bounded procedure that has already run repeatedly and autonomously — the
rollout cohorts — is promotion-ready.
[Skills are instructions plus routing and execution policy](../../notes/skills-are-instructions-plus-routing-and-execution-policy.md):
promotion changes discovery and invocation, not the procedure itself.

## Decision

**Grounding is the promoted skill `cp-skill-ground`.** It lives at
`kb/instructions/cp-skill-ground/SKILL.md`, is installed by `commonplace-init`,
and is user-invocable with arguments `Target` and `Claim needed`. Its body and
result protocol — `quotes sufficient`, `quotes added`, `snapshot required` — are
unchanged from the instruction it replaces.

**`cp-skill-ground` is the single advertised entry** for deciding which quotes
an ingest retains. `cp-skill-ingest`'s description now presents its quote-append
path as the mechanical callee of a `quote_append_request` from
`cp-skill-ground`, not as a capability to match requests against. One request,
one matching surface.

**Writers still stop when Quotes are insufficient.** Their handoff becomes a
single route addressed by skill name — invoke `cp-skill-ground` with `Target`
and `Claim needed` — instead of a path branched on install layout.

## Considered alternatives

**Keep the instruction and add routing pointers.** An `AGENTS.md` pointer, or a
broader `cp-skill-ingest` description, would make the procedure findable without
promoting it. Rejected: it leaves two advertised surfaces for one request, which
is the failure that motivated the decision. The capability-placement rule puts
an autonomy-ready procedure on the skill surface rather than in a control-plane
inventory.

**Promote it and let writers invoke it automatically.** This is the candidate
direction of the proposal *Source-claim grounding skill and evidence-retention
boundary*. Deferred, not rejected: a request to write one artifact would then
mutate a second, and that mutation authority is a separate decision. Promotion
for explicit use carries no new mutation footprint, so it need not wait on that
question.

**Fold quote selection into `cp-skill-ingest`.** One skill would then own both
selection and append. Rejected: it merges evidence selection with persistence,
so the skill choosing quotes would certify its own transcription. The split
keeps one mechanical mutation owner whose checks are independent of who selected
the passages.

**Move retained evidence out of the ingest first.** The same proposal leaves the
evidence-retention boundary open. Left open here: the skill's result protocol
does not change if the append target later moves, so promoting now forecloses
nothing.

## Consequences

Operativity path: grounding and quote-retention requests reach
`cp-skill-ground` through harness skill discovery, with no competing match on
`cp-skill-ingest`; the force is routing, not validation. Writers report one
route, and installed projects need no path-branched handoff.

The proposal retains only its undecided parts — automatic invocation from
writers, and the evidence-retention boundary.

Caveat on the expected benefit: on this harness a `context: fork` skill inherits
the invoking conversation, so promotion does not by itself isolate source
reading from target prose. Any later claim that grounding runs in a fresh
context must name the launch mode that actually provides it.

---

Relevant Notes:

- [Capability placement should follow autonomy readiness](../../notes/capability-placement-should-follow-autonomy-readiness.md) — rests-on: the readiness criterion under which a repeatedly-run bounded procedure belongs on the skill surface
- [Skills are instructions plus routing and execution policy](../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) — rests-on: why promotion changes discovery and invocation while leaving the procedure intact
- [ADR 073 — Untracked source snapshots require ingest grounding](./073-untracked-source-snapshots-require-ingest-grounding.md) — extends: gives the grounding procedure it defined a routable entry point without altering its result protocol
- [Ground a source-dependent claim](../../instructions/cp-skill-ground/SKILL.md) — implemented-by: the promoted skill this decision installs

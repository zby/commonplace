# Maintenance form for shipped-system descriptions

## Governing question

For each description of what the shipped system currently does, should
Commonplace generate it, register it for staleness against the code it
describes, author only the part no recovery reaches, or minimize it?

## What is already settled

**Placement is not the question.** These artifacts belong in `kb/reference/`,
which owns the state Commonplace's choices produced. An earlier framing had
them homeless; that was an artifact of a placement test since replaced.

**They are recoverable.** The running system can regenerate their content, so
[the recovery test](../../notes/documentation-generates-the-system-rather-than-describing-it.md)
marks them cache rather than generator. Deleting one costs a bounded
recomputation, never a fact.

**Recoverable does not mean deletable.** For a model reader the recompute is
the expensive step, so
[a materialized derived value is often worth keeping](../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md)
exactly where ordinary software would call it premature denormalization. The
decision is economic, not a cleanup.

**An unchecked cache is the hazard.** Hand-maintained-and-trusted is the state
[the enforce-or-omit rule](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)
forbids, because a false copy suppresses the read that would have exposed it.
Most of these artifacts are currently in exactly that state.

## Scope

The class, as identified by two independent criteria converging:
`architecture.md`, `lib-modules.md`, `commands.md`, `storage-architecture.md`,
`freshness-schemas.md`, and the code-architecture halves of
`review-architecture.md` and `freshness-architecture.md`.

Membership is a finding to re-test, not a fixed list. Some of these are mixed —
partly a recoverable compression of code, partly level-native vocabulary that
no implementation determines. The mixed ones are where the work is.

Out of scope: ADRs, proposals, purpose and frame documents, and anything else
whose content the system cannot regenerate.

## What a later session should not assume

The four dispositions are candidates, not a menu to allocate across. A fifth
may fit better, and one artifact may need different dispositions for different
regions. `commands.md` and `freshness-schemas.md` look mechanically derivable
and `lib-modules.md` looks like a judgment-dependent summary, but neither
impression has been tested.

## Dependency worth exploiting

[The ADR routing workshop](../adr-routing/README.md) is building, or deciding
not to build, a change-target-keyed routing surface. If it lands, it answers
this workshop's hardest question empirically: a description that the routing
surface never serves is one nobody consults, which settles minimize-versus-
register without argument. Sequencing this workshop after or alongside that one
trades waiting for evidence.

## What closes this workshop

Every artifact in the class has a disposition with a reason, at least one is
executed as a worked case, and the general rule — if one exists — is promoted.
If the answer turns out to be per-artifact with no general rule, say so; that
is a finding, not a failure to conclude.

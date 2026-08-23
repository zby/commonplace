# Maintenance form for shipped-system descriptions

## Governing question

For each description of what the shipped system currently does, should
Commonplace generate it, register it for staleness against the code it
describes, author only the part no recovery reaches, or minimize it?

## What is already settled

**Placement is not the question.** These artifacts belong in `kb/reference/`,
which owns the state Commonplace's choices produced. An earlier framing had
them homeless; that was an artifact of a placement test since replaced.

**They are predominantly, not wholly, recoverable — and that is a result, not a
premise.** An earlier version of this section asserted that the running system
can regenerate their content, full stop. That was wrong three ways, and the
error was load-bearing: it licensed judging passages by reading them instead of
searching for their other homes, which produced two wrong calls in the first
worked case.

Recoverability attaches to **units of content, not to artifacts** — the central
move of [the recovery test](../../notes/documentation-generates-the-system-rather-than-describing-it.md)
this workshop rests on. A file is a mixture, and the mixture is the whole
problem. `lib-modules.md` returned one irrecoverable passage in six rule-shaped
candidates; a blanket claim would have deleted it.

It is also not a property of documentation, or of `kb/reference/`. **ADRs are
the counterexample**: they live in the same collection, and no running system
regenerates a decision, its rejected alternatives, or the reason a boundary
sits where it does. What distinguishes the artifacts in scope here is that most
of their content happens to describe current state, which is recoverable — a
contingent fact about this class, established per unit by search, never assumed.

Where a unit *is* recoverable, deleting it costs a bounded recomputation and
never a fact. Where it is not, deletion is unbounded loss. Which one applies is
what the procedure determines.

**Recoverable does not mean deletable, and the reader decides.** The value of a
description is per-read recompute cost times recomputes avoided, minus
maintenance, and [human and agent readers invert on both terms](../../notes/human-recompute-is-dear-and-rare-agent-recompute-is-cheap-and-constant.md)
— dear and rare against cheap and constant. That model is the workshop's basis;
the local work is supplying Commonplace's magnitudes and reading the disposition
off them. Relatedly, [in-context recompute is dear next to a CPU's](../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md),
which is why materializing can pay at all — a different comparison class, not a
competing claim.

**The hazard is real in principle but is not what is happening here.**
Hand-maintained-and-trusted is the state
[the enforce-or-omit rule](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)
forbids. These artifacts are formally in it — no validator checks them — but
[measurement](./staleness-baseline.md) shows they are not drifting: lag runs
0–3 commits and they are largely updated in the same commit as the code.

So the operative problem is **cost, not rot**. They stay current because a
co-maintenance tax is paid on every code change that touches them. The question
is which disposition reduces that tax without losing what the descriptions
provide.

## Scope

The class, as identified by two independent criteria converging:
`architecture.md`, `lib-modules.md`, `commands.md`, `storage-architecture.md`,
`freshness-schemas.md`, and the code-architecture halves of
`review-architecture.md` and `freshness-architecture.md`.

Membership is a finding to re-test, not a fixed list. Some of these are mixed —
partly a recoverable compression of code, partly level-native vocabulary that
no implementation determines. The mixed ones are where the work is.

Out of scope as artifacts: ADRs, proposals, purpose and frame documents. Their
content is overwhelmingly irrecoverable, so the disposition question does not
arise for them — but that is a judgment about where the work is worth doing,
not a claim that every unit inside them is unique.

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

## Current draft

- [Decide What Documentation an LLM Needs](./decide-what-documentation-an-llm-needs.md) — turns the workshop's recovery, addressability, value, placement, and maintenance findings into an executable disposition procedure. **Deliberately not promoted to `kb/instructions/`**: its write-time half is folded into [`kb/reference/COLLECTION.md`](../../reference/COLLECTION.md)'s economy tests, and its audit half fires only on a corpus sweep, which is one-off migration work. Promotion condition and reasoning are recorded on the draft itself.
- [Worked case: `lib-modules.md`](./worked-case-lib-modules.md) — the first artifact through the full procedure; one survivor in six rule-shaped candidates, and a docstring relocation that shrank from 37 functions to one on inspection

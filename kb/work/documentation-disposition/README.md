# Maintenance form for shipped-system descriptions

## Governing question

For each description of what the shipped system currently does, should
Commonplace generate it, register it for staleness against the code it
describes, author only the part no recovery reaches, or minimize it?

## What is already settled

**Placement is not the question.** These artifacts belong in `kb/reference/`,
which owns the state Commonplace's choices produced. An earlier framing had
them homeless; that was an artifact of a placement test since replaced.

**Every artifact is a mixture, and the split is the operative thing.**
Recoverability attaches to **units of content, not to artifacts** — the central
move of [the recovery test](../../notes/documentation-generates-the-system-rather-than-describing-it.md)
this workshop rests on. Where a unit is recoverable, deleting it costs a bounded
recomputation and never a fact; where it is not, deletion is unbounded loss.
Which one applies is what the procedure determines, per unit, by search.

An earlier version of this section asserted the artifacts in scope are
recoverable, as settled background. The error was load-bearing: it licensed
judging passages by reading them instead of searching for their other homes,
which produced two wrong calls in the first worked case before the search caught
them. `lib-modules.md` returned one irrecoverable passage in six rule-shaped
candidates; a blanket claim would have deleted it.

**Do not state a ratio.** Any proportion is a measurement of one moment, and it
is not stable. **ADRs are the counterexample that shows recoverability is not a
property of documentation, or of `kb/reference/`**: they sit in the same
collection, and no running system regenerates a decision, its rejected
alternatives, or the reason a boundary sits where it is.

**And the mixture drifts one way.** Irrecoverable content accretes: every
recorded rationale, rejected option, or warning to a future changer adds some,
while recoverable content is cheap to regenerate or correct. The sharpened
economy tests now in [`kb/reference/COLLECTION.md`](../../reference/COLLECTION.md)
push the same direction by construction, since they filter recoverable additions
at write time and let irrecoverable ones through. So an artifact dispositioned
today can accumulate a generator core and need re-examination. This audit is not
once-and-done, and a disposition should record the date and the basis it was
decided on rather than reading as permanent.

**Recoverable does not mean deletable, and the reader decides.** The value of a
description is per-read recompute savings times recomputes avoided, minus
maintenance. [Opposed factor directions do not order that cache
value](../../notes/opposed-recompute-factors-do-not-decide-documentation-segmentation.md),
and cache value alone does not decide whether a second audience-specific content
layer pays. The local work must therefore supply Commonplace's magnitudes and
specialization tradeoff rather than infer a disposition from reader identity.
Relatedly, [in-context recompute is dear next to a CPU's](../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md),
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
regions. The first two worked cases showed why appearance is not a disposition:
`lib-modules.md` was retired after live source proved the better routing surface,
while `commands.md` retained a small checked catalogue because command-local
help cannot discover an unknown command. `freshness-schemas.md` remains
untested.

## Dependency worth exploiting

[The ADR routing workshop](../adr-routing/README.md) is building, or deciding
not to build, a change-target-keyed routing surface. If it lands, it answers
this workshop's hardest question empirically: a description that the routing
surface never serves is one nobody consults, which settles minimize-versus-
register without argument. Sequencing this workshop after or alongside that one
trades waiting for evidence.

## What closes this workshop

Every artifact in the class has a disposition with a reason **and a date**, at
least one is executed as a worked case, and the general rule — if one exists —
is promoted. If the answer turns out to be per-artifact with no general rule,
say so; that is a finding, not a failure to conclude.

Dates matter because the mixture drifts. A disposition is a judgment about an
artifact's composition at a time, not a permanent property, so a later session
needs to know when it was made and against what.

## Current draft

- [Decide What Documentation an LLM Needs](./decide-what-documentation-an-llm-needs.md) — turns the workshop's recovery, addressability, value, placement, and maintenance findings into an executable disposition procedure. **Deliberately not promoted to `kb/instructions/`**: its write-time half is folded into [`kb/reference/COLLECTION.md`](../../reference/COLLECTION.md)'s economy tests, and its audit half fires only on a corpus sweep, which is one-off migration work. Promotion condition and reasoning are recorded on the draft itself.
- [Worked case: `lib-modules.md`](./worked-case-lib-modules.md) — the first artifact through the full procedure, completed 2026-08-24 by retiring the reference after task-vocabulary searches reached a more complete live-source surface
- [Worked case: `commands.md`](./worked-case-commands.md) — the second artifact through the procedure; retained the complete 22-name catalogue as checked routing, removed repeated manuals, and made side-effect-free live help a tested command-wide contract

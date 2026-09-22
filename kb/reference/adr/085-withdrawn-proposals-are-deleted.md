---
description: "Decision that a design proposal whose problem or adoption trigger has lapsed, with no decision foreclosing it, is withdrawn by deletion rather than archived or kept"
type: ../types/adr.md
tags: []
status: accepted
---

# 085-Withdrawn proposals are deleted

**Status:** accepted
**Date:** 2026-09-22
**Amends:** [ADR 056](./056-adopted-and-retired-proposals-archive-out-of-the-frontier.md) (adds a third exit from the frontier)

## Context

ADR 056 gives a proposal two exits: adoption, when its choice ships as an
ADR, and retirement, when a later decision forecloses it. Both end in the
archive. A proposal can also stop mattering with no decision at all: the
workflow it was designed for is removed, or the problem it addresses goes
away, or its adoption trigger plainly never arrives. The 2026-09-22 review of
the frontier found two such proposals. One had lost its only worked case when
the workflow it targeted was retired without an ADR. The other said of itself
that a different approach would likely dominate.

With no exit, such a proposal stays in the frontier, and listing the
directory stops answering "what is still open". Forcing an exit through an
ADR is also wrong: an ADR records an implemented decision, and withdrawing a
proposal implements nothing.

The archive is justified by what an adopted or retired proposal retains: the
dated measurements a live commitment rested on, which a decision audit may
need and nobody can re-derive. A withdrawn proposal warranted no commitment,
so nothing has a claim on its measurements. That is the same reason
workshops are deleted rather than archived.

## Decision

**A live design proposal may be withdrawn** when its problem no longer exists
in the system, or its adoption trigger has lapsed, and no decision forecloses
it. The operator decides; the withdrawing commit's body names which condition
holds and the evidence for it. No ADR records a withdrawal.

**A withdrawn proposal is deleted.** Before deletion, anything still current
is extracted as for any retirement: a transferable claim becomes a note, and a
fact the system still depends on moves to the reference doc that owns it.
Inbound links are retargeted or removed, and the published path redirects to
the nearest page that carries the proposal's subject. Git keeps the text.

The `design-proposal` type spec states the withdrawn exit beside the
archived state, and [retire an artifact](../../instructions/retire-artifact.md)
reads it to choose the delete destination.

## Considered alternatives

**Require a retiring ADR for every lapsed proposal.** Keeps a single rule:
every exit has a decision record. Rejected because an ADR records an
implemented decision, and a withdrawal implements nothing. The commit body
already carries change narrative under
[ADR 074](./074-git-is-the-change-history-layer.md).

**Archive withdrawn proposals.** Keeps the text for clones without history.
Rejected because the archive's warrant is evidence behind a live commitment,
and a withdrawn proposal has none. Archiving it would grow the archive with
designs that no audit needs.

**Keep lapsed proposals in the frontier.** No operation needed. Rejected
because the frontier's value is that every file in it is open, and each
lapsed file taxes every sweep of the directory.

**Mark lapsed proposals in place.** A banner or status field. Rejected for the
reason ADR 056 rejected in-place archiving: the file stays in every default
listing, and a lifecycle field nothing validates is a cache that goes stale.

**Free choices left open.** No staleness signal routes a proposal to
withdrawal. A refresh of its current state is where a lapsed trigger is
usually noticed.

## Consequences

The frontier can shrink without a decision record, so its listing stays
accurate. The cost is that a withdrawn proposal is visible only in git
history, and a shallow clone cannot see it. That is acceptable because
nothing live rests on it.

Withdrawal is the operator's judgment, so a proposal can be withdrawn
wrongly. Recovery is a new proposal, written from git history if needed.

**Operativity path.** The `design-proposal` type spec states the withdrawn
exit and names the procedure. `retire-artifact` reads the type spec at its
first step to choose the destination, and the agent running it follows its
extraction and inbound-link steps with procedural force. The
[refresh procedure](../../instructions/refresh-a-proposal-current-state.md)
routes a lapsed trigger to the operator. Nothing enforces that a deletion
under `proposals/` was a withdrawal rather than an unrecorded retirement; the
commit body is the only record.

---

Relevant Notes:

- [ADR 056: adopted and retired proposals archive out of the frontier](./056-adopted-and-retired-proposals-archive-out-of-the-frontier.md) — see-also: the two exits and the archive-versus-delete test this decision extends
- [Design proposal](../types/design-proposal.md) — implemented-by: the type spec that states the withdrawn exit
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — rests-on: the deletion rule for residue that warranted no commitment

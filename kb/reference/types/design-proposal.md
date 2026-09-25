---
type: type-spec
name: design-proposal
description: Finished but unadopted design for the Commonplace system — problem, option space, forces, free choices, no decision
schema: ./design-proposal.schema.yaml
---

# Design proposal

## Authoring Instructions

Use a design proposal for a finished but unadopted design: the problem, the option space, the forces, and the free choices — without deciding. A design still being worked out stays in the workshop layer (`kb/work/`); a decided and implemented choice becomes an ADR (`../adr/`). Where proposals may live is a placement rule in [`kb/reference/COLLECTION.md`](../COLLECTION.md); everything a proposal must be is stated here ([ADR 084](../adr/084-kind-rules-live-in-type-specs-and-operations-in-instructions.md)).

- **No decision.** A proposal may hold several options and unresolved forces. When it converges on one choice that ships, the choice becomes an ADR and the proposal leaves the frontier (see Lifecycle).
- **First version stays conceptual.** A new proposal records the problem, the option space, the forces, and the candidate selections — not implementation detail. Field names, schemas, thresholds, and step-by-step procedures invented before the design space is understood are authoring-time snapshots that constrain later design without warrant — the same mistake [an instruction author makes by fixing details the executor could determine](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md), landed one layer earlier. Add detail in revisions, when a named force or an adoption decision demands it; a first version that reads like an implementation plan has skipped its own option space.
- **Transferable theory stays in notes.** A requirement or rationale that forms an independently transferable truth-apt claim belongs in `kb/notes/` and is cited from here via a `rests-on` edge. A proposal to change adopted theory vocabulary belongs in `kb/notes/proposals/`. The design proposal inlines system-specific constraints, candidate options, and the context needed to evaluate them.
- **Dated current-state anchor.** State the system facts the proposal rests on under a `## Current state (as of YYYY-MM-DD)` heading. Going stale against later ADRs is an expected lifecycle event, not a defect: refresh or retire.
- **Operativity and warrant** (proposals authored 2026-07-24 or later). For each option that changes behavior-determining organization, state its operativity path — what would consume the change, through which channel, with what force ([operative change](../../notes/definitions/operative-change.md)). "No consumer yet; one must be built" is a valid answer and exactly what the adoption decision needs to see. If an option adds or strengthens automated evaluation, also name what warrants the oracle and where that warrant stops.
- **Adoption criteria.** Name what would have to be observed, built, or decided for an option to be adopted, so a later reader can tell whether the trigger has arrived.
- **Unmistakably proposed.** The description leads with "Proposal:". Readers of `kb/reference/` are usually trying to act on the shipped system, so a proposal never presents shipped behavior as open, or proposed behavior as shipped.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `description` | Yes | Leads with `Proposal:`; an archived adopted proposal may use `Proposal (adopted):`. |
| `type` | Yes | `../types/design-proposal.md` for proposals under `kb/reference/proposals/`; `../../types/design-proposal.md` once archived. |
| `tags` | No | Navigation tags. |
| `traits` | No | Review-routing traits, e.g. `has-external-sources`. |

- The schema enforces the `Proposal` lead and the dated current-state heading; the other clauses are checked by type-conformance review.
- Review separates the artifact's regions. Truth-apt statements remain contestable. Candidate options and selections are reviewed against requirements, constraints, consequences, and trade-offs. The artifact as a whole is also reviewed for proposal-process fitness — problem stated, forces stated, candidate selections marked, adoption criteria named — and claim-title expectations do not apply.

## Lifecycle

A proposal is in one of three states, or has been withdrawn. Each transition has one procedure.

| State | What must hold | Enters by |
|---|---|---|
| **Live** (`kb/reference/proposals/`) | Every clause above. Nothing it contains has shipped. | Promotion from a workshop, or a new proposal written directly |
| **Partially adopted** (still live) | The shipped part is gone from the proposal: shipped behavior is described in reference docs and recorded in an ADR or its implementing commit, and the current-state anchor notes the adoption. A proposal that silently retains shipped content has become a false description. | [Extract the adopted part of a proposal](../../instructions/extract-adopted-part-of-a-proposal.md) |
| **Archived** (`kb/reference/proposals/archive/`) | Fully adopted, or retired by a later decision that forecloses it. Nothing still current remains: shipped behavior, decision-relevant reasoning, and transferable requirements have left, and what stays is the irreproducible remainder — dated current-state anchors and the measurements the design rested on. An ADR names it by title in prose, with no path and no link. The file is frozen: correct it only for link integrity when something it points at moves. | [Retire an artifact](../../instructions/retire-artifact.md) |

**Withdrawn** is the exit for a live proposal whose problem no longer exists in the system, or whose adoption trigger has lapsed, when no decision forecloses it. The operator decides; the withdrawing commit's body names which condition holds and its evidence. Anything still current is extracted first ([ADR 085](../adr/085-withdrawn-proposals-are-deleted.md)).

When a live proposal's current-state anchor may have gone stale, [refresh the proposal's current state](../../instructions/refresh-a-proposal-current-state.md); a refresh routes shipped or foreclosed content to the procedures above and reports a lapsed trigger to the operator.

**Retirement destination: archive to `kb/reference/proposals/archive/` when the proposal is adopted or retired by a decision; delete when it is withdrawn.** Archived files keep this type ([ADR 056](../adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md)). [Retire an artifact](../../instructions/retire-artifact.md) reads this line to pick its destination.

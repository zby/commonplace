---
type: kb/types/type-spec.md
name: design-proposal
description: Finished but unadopted design for the Commonplace system — problem, option space, forces, free choices, no decision
schema: ./design-proposal.schema.yaml
---

# Design proposal

## Authoring Instructions

Use a design proposal for a finished but unadopted design: the problem, the option space, the forces, and the free choices — without deciding. A design still being worked out stays in the workshop layer (`kb/work/`); a decided and implemented choice becomes an ADR (`../adr/`).

Proposals live under `kb/reference/proposals/`. Once adopted or retired, a proposal is extracted and moved to `proposals/archive/`, which nothing outside it links into ([ADR 056](../adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md)); archived files keep this type. This spec enforces only the mechanical core; the full authoring contract — including the judgment clauses no schema checks — is [proposals/README.md](../proposals/README.md).

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `description` | Yes | Leads with `Proposal` (`Proposal:`, or `Proposal (adopted):` after adoption) so a reader of `kb/reference/` never mistakes proposed for shipped. |
| `type` | Yes | `../types/design-proposal.md` for proposals under `kb/reference/proposals/`. |
| `tags` | No | Navigation tags. |
| `traits` | No | Review-routing traits, e.g. `has-external-sources`. The type replaces the former `design-proposal` trait. |

- The body must carry a dated current-state anchor — a `## Current state (as of YYYY-MM-DD)` section stating the system facts the proposal rests on. Going stale against later ADRs is lifecycle, not defect: refresh or retire.
- Reviewed for design quality — problem stated, forces stated, free choices marked, adoption criteria named — not contestability; claim-title expectations do not apply.

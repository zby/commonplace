---
description: "Unadopted system designs live in kb/reference/proposals/ as notes with the design-proposal trait; the proposed ADR status is removed so ADRs record only implemented decisions; the YAGNI gap rule routes system gaps to proposals and transferable insights to notes"
type: ../types/adr.md
tags: []
status: accepted
---

# 028-Design proposals live in kb/reference/proposals; ADRs record implemented decisions only

**Status:** accepted
**Date:** 2026-06-12

## Context

Design proposals — finished but unadopted designs — had no home. The theory register (`kb/notes/`) demands contestable claims, and a proposal's free parameters make it evaluable by usefulness rather than truth, so proposals squatted there under `status: speculative` with hedged titles. The workshop layer was wrong (workshops close; proposals wait), and the prescriptive surface admitted only adopted artifacts: instructions are operative, and although the ADR type nominally allowed `Status: proposed`, in practice all five `proposed` ADRs (004, 005, 007, 019, 020) were long implemented — stale markers, not pending decisions. Meanwhile the AGENTS.md YAGNI rule routed every identified gap to `kb/notes/`, reinforcing the squatting.

## Decision

1. **ADRs record implemented decisions only.** The `proposed` status is removed from the ADR type spec and schema (`accepted | superseded | deprecated` remain); the five stale `proposed` ADRs are flipped to `accepted`. A decision still under consideration is not an ADR.
2. **Unadopted system designs live in `kb/reference/proposals/`** as plain `note`-typed artifacts carrying the `design-proposal` trait — trait rather than type because nothing is automatically checkable yet (types for structure, traits for review, per [ADR 012](./012-types-for-structure-traits-for-review.md)).
3. **The proposal contract** (in `proposals/README.md`): no decision — a proposal may hold multiple options and unresolved forces; transferable requirements live in `kb/notes/` and are cited via `rationale`, with only system-specific constraints inlined; a dated current-state anchor, with staleness against later ADRs an expected lifecycle event; descriptions lead with "Proposal:" so reference readers never mistake proposed for shipped. When part of a proposal ships, that content moves out to reference docs and an ADR.
4. **The YAGNI gap rule reroutes:** system feature or design gaps → `kb/reference/proposals/`; transferable insights → `kb/notes/`.
5. **The theory register keeps a recast option:** a design whose requirements are substantive may stay in `kb/notes/` as an existential claim with the construction presented as a witness, free choices marked, rather than moving to `proposals/`.

Lifecycle: workshop (active, closes) → proposal (finished, undecided, waits) → ADR (decided and implemented) or retirement.

## Consequences

Easier:
- The theory register's claim contract stays undiluted; review gates stop applying contestability tests to non-truth-apt artifacts.
- Proposals become first-class and findable instead of squatting as hedged speculative notes; partial adoption becomes visible because shipped content must leave the proposal.
- The decision record sharpens: `Status: proposed` can no longer go stale, because it no longer exists.

Harder / accepted costs:
- Two homes for design-shaped content (recast claim in notes vs proposal in reference) require a judgment call on whether requirements are substantive.
- `kb/reference/` readers must respect the `proposals/` boundary; the "Proposal:" description prefix and directory segregation carry that load.
- No template or schema enforces the proposal contract yet; review relies on the trait until structure earns codification.

---

Relevant Notes:

- [design proposals differ from claims in kind, not confidence](../../notes/design-proposals-differ-from-claims-in-kind-not-confidence.md) — rationale: the category distinction and existential recast this decision implements

---
description: "An artifact's production history is convertible to later-checkable form only at production time, via records/attestation or re-derivability; after that a bounded reviewer sees only carried state"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [context-engineering]
status: seedling
---

# History has one chance to become checkable

An artifact's history — how it was produced, what was consulted, who or what made it — can be converted into later-checkable form only at production time. There are two conversion routes:

1. **Records / attestation.** Capture the facts while they are still available: provenance fields, citations, quote anchors. W3C PROV and in-toto attestations are the systems exemplars; science's methods sections and pre-registration are the institutional ones.
2. **Re-derivability.** Pin the inputs and fix a deterministic process, so history can be re-checked from state at any later time. Reproducible builds do this. It is usually unavailable for nondeterministic LLM production, where the same prompt need not yield the same output.

After production, the option is gone. A later reviewer sees only the artifact's *state* — its text plus whatever witnesses it carries or names — and cannot recover unrecorded history.

## Boundaries

Stated so the claim is neither tautology nor overclaim:

- **Leakage is real but unreliable.** Processes do leave unintended traces in state — stylometry and statistical forensics read them. But leakage is noisy and adversarially fragile, so a review contract cannot bind on it.
- **Verifiability can decay gradually, not vanish at once.** A snapshot stays re-checkable against its source URL until that source changes. Recording is insurance against decay, so it is not always an *immediate* necessity — but the window only closes.
- **The claim is relative to a bounded reviewer** — no world access, no re-execution, no memory of production. That is precisely what KB review deliberately is.

## Design consequence

Recording is the one feature YAGNI cannot defer. Every other verification mechanism can be built later; a record not made at production time is unrecoverable.

Corollary for contracts: a review-facing contract can bind only what the artifact carries. Process requirements must be enforced at production time or converted into carried state — there is no third option a downstream reviewer can reach for.

The philosophy-of-science anchor is Reichenbach's distinction between the context of discovery and the context of justification: the methods section (and pre-registration) is the institutional mechanism for dragging discovery facts into the justificatory record.

---

Relevant Notes:

- [The verifiability gradient](./verifiability-gradient.md) — contrasts: an orthogonal axis — how *cheaply* something can be checked, versus whether and when it can be checked at all
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — extends: the recomputable special case; provenance records are the non-recomputable complement, trusted precisely because they cannot be recomputed
- [W3C PROV overview](../sources/prov-overview.ingest.md) — evidence: the canonical records/attestation exemplar for capturing provenance at production time
- [in-toto farm-to-table guarantees](../sources/in-toto-farm-to-table-guarantees.ingest.md) — evidence: cryptographic whole-chain attestation as the systems exemplar for the records route

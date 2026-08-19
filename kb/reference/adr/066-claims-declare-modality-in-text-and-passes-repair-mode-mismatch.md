---
description: "Claims assert in one of three modes — universal, statistical, ideal-type — declared in the claim text; the full pass detects mode mismatch via counterexample shape and repairs it through mode-guarded reframes in both directions"
type: ../types/adr.md
tags: []
status: accepted
---

# 066-Claims declare modality in text, and passes repair mode mismatch

**Status:** accepted
**Date:** 2026-08-19

## Context

Review defeats claims with counterexamples, and every repair the pipeline offered weakened the claim: qualify, narrow, reframe down, or delete. Author-side guidance sweeps drafts for absolutes before review, so both pressures point the same way. Three worked episodes in 2026-08 (recorded in the popperian-maintenance-episode workshop) showed the cost: crisp claims with genuine unification were walked into hedged or checklist forms with no step where anyone asked whether the strong claim was the more useful artifact, and a full corpus survey found 22 modality-mismatched notes — statistical claims stated as universals with the modality leaking into body hedges, tendency claims hedged past refutability, and ideal-type reasoning practiced without a label (the "clean model / degraded variant" cluster).

The counter-machinery was tested before adoption. The two-stage idealization criterion (pricing routes an exception to assessment; adequacy decides) survived a full pass on its own note, and pass `20260819T105132Z-2a6408` ran the first in-pass adequacy assessment against a partially open record: the gate attacked the declared commitment on its merits, treated open dimensions as open rather than as defeats, and refused acceptance on pricing evidence alone — with no new verdict, trait, or gate, because the declared commitments were ordinary note content.

This adopts the corresponding parts of the design proposal "Repair dispositions for defeated claims are an epistemic policy with an option space"; the proposal retains its undecided remainder.

## Decision

1. **Three claim modes, refuter-defined.** Universal (one genuine counterexample refutes), statistical (only prevalence evidence refutes; the claim must state what prevalence would refute it), ideal-type (a declared first-order model; refuted by unpriced-ordinary exceptions or dominance failure). Declared in `kb/notes/COLLECTION.md` under "Claim modality" — the binding surface the full pass reads.
2. **Modality lives in the claim text, not frontmatter.** Title, thesis, or a named section carries the mode; an ideal-type claim carries its adequacy record (declared use, omitted mechanism, consequence bound, explanatory dominance) in the body. Undeclared text reads as universal. Rationale: the premise-decomposition gate quotes premises verbatim, so in-text modality is tested automatically — pass `2a6408` demonstrated this end to end — while a frontmatter field would be a second copy of claim semantics that can drift. Mode is orthogonal to lifecycle stage (a status-conjecture note declares both when both apply).
3. **The premise-decomposition gate reads premises at their stated modality** and annotates every non-HOLDS premise's counterexample shape — `instance`, `prevalence`, or `priced-exception` — as routed attention, never a verdict.
4. **The full pass repairs mode mismatch through the existing keep-reframe, mode-guarded and bidirectional.** Counterexample shapes route the target mode. Guards: a statistical retitle must state its refuter or the reframe fails as vacuous; an ideal-type conversion must write the adequacy record into the body, where the closing cycle's premise rerun attacks it — that closing attack is the conversion's required resistance. A claim hedged below its warrant is the same finding in reverse, reframed up.
5. **Conversions outside a pass remain permitted**; the mode guards bind whoever converts, and the next full pass supplies the deferred attack, since the record is content the premise gate tests by default.

## Consequences

- The 22 surveyed candidates (workshop file `statistical-mode-candidates.md`) are repairable by ordinary full passes; no migration or batch operation is needed. Recommended first conversions are recorded there.
- The narrowing-direction guards gain mode-specific companions: the refuter test already polices analytic narrowing; the stated-refuter guard polices vacuous statistical landings; the adequacy record polices immunized ideal-type landings.
- No frontmatter modality field ships. If corpus sweeps later need to enumerate declared ideal-type or statistical claims mechanically, addressability can be added then, under the derived-copy rule (checked or absent).
- Partially adopted from the proposal named above, which keeps its undecided remainder: profile-level repair-policy declaration (no second installation demands it) and freshness-store drift tracking for pricing attestations (requires factored dependency pairs, themselves an open proposal).

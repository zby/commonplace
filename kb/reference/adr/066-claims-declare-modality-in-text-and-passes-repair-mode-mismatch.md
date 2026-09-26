---
description: "Claims assert in one of three modes — universal, statistical, ideal-type — declared in the claim text; the full pass detects mode mismatch via counterexample shape and repairs it through mode-guarded reframes in both directions"
type: reference/types/adr.md
tags: []
status: accepted
---

# 066-Claims declare modality in text, and passes repair mode mismatch

**Status:** accepted — decision 4 amended by [ADR 080](./080-full-passes-hand-claim-changes-back-as-a-pending-revise.md) (2026-08-26): the full pass no longer converts mode in-pass; a mode mismatch is a pending `revise` whose brief names the target mode and its guard; decision 1 amended by [ADR 091](./091-refutation-needs-a-checkable-counterexample-corroboration-a-test.md) (2026-09-26): the universal refuter is a counterexample others can check again, not one unrepeated report
**Date:** 2026-08-19

## Context

Review defeats claims with counterexamples, and every repair the pipeline offered weakened the claim: qualify, narrow, reframe down, or delete. Author-side guidance sweeps drafts for absolutes before review, so both pressures point the same way. Three worked episodes showed the cost: crisp claims with genuine unification were walked into hedged or checklist forms with no step where anyone asked whether the strong claim was the more useful artifact, and a full corpus survey found 22 modality-mismatched notes — statistical claims stated as universals with the modality leaking into body hedges, tendency claims hedged past refutability, and ideal-type reasoning practiced without a label (the "clean model / degraded variant" cluster).

The counter-machinery was tested before adoption. The two-stage idealization criterion (pricing routes an exception to assessment; adequacy decides) survived a full pass on its own note, and the first in-pass adequacy assessment ran against a partially open record: the gate attacked the declared commitment on its merits, treated open dimensions as open rather than as defeats, and refused acceptance on pricing evidence alone — with no new verdict, trait, or gate, because the declared commitments were ordinary note content.

## Decision

1. **Three claim modes, refuter-defined.** Universal (one genuine counterexample refutes), statistical (only prevalence evidence refutes; the claim must state what prevalence would refute it), ideal-type (a declared first-order model; refuted by unpriced-ordinary exceptions or dominance failure). Declared in `kb/notes/COLLECTION.md` under "Claim modality" — the binding surface the full pass reads.
2. **Modality lives in the claim text, not frontmatter.** Title, thesis, or a named section carries the mode; an ideal-type claim carries its adequacy record (declared use, omitted mechanism, consequence bound, explanatory dominance) in the body. Undeclared text reads as universal. Rationale: the premise-decomposition gate quotes premises verbatim, so in-text modality is tested automatically, as the in-pass assessment demonstrated, while a frontmatter field would be a second copy of claim semantics that can drift. Mode is orthogonal to lifecycle stage (a status-conjecture note declares both when both apply).
3. **The premise-decomposition gate reads premises at their stated modality** and annotates every non-HOLDS premise's counterexample shape — `instance`, `prevalence`, or `priced-exception` — as routed attention, never a verdict.
4. **The full pass repairs mode mismatch through the existing keep-reframe, mode-guarded and bidirectional.** Counterexample shapes route the target mode. Guards: a statistical retitle must state its refuter or the reframe fails as vacuous; an ideal-type conversion must write the adequacy record into the body, where the closing cycle's premise rerun attacks it — that closing attack is the conversion's required resistance. A claim hedged below its warrant is the same finding in reverse, reframed up.
5. **Conversions outside a pass remain permitted**; the mode guards bind whoever converts, and the next full pass supplies the deferred attack, since the record is content the premise gate tests by default.

## Considered alternatives

The option space was developed in the design proposal "Repair dispositions for defeated claims are an epistemic policy with an option space", in its version before this ADR trimmed it. The proposal framed repair of defeated claims as an epistemic policy and offered three options.

**Option 1: document reframe-to-warranted as the universal policy.** Name the existing weaken-only repair set as this installation's policy in `kb/notes/COLLECTION.md` or the pass instruction, with no new mechanism. It lost as a complete answer because the idealization question stays unposable: a claim whose crisp form is refuted in detail but whose unification is worth keeping has no survivable declared form. Its core point, that the repair policy must be stated where it binds, survives in the "Claim modality" contract.

**Option 2 as proposed: a modality trait or frontmatter field, plus a new keep-as-idealization disposition.** The adopted decision takes this option's modes, reading rule (undeclared reads as universal), and two-stage adequacy assessment, but changes two parts. Modality moved into the claim text, because the premise-decomposition gate quotes premises verbatim, so in-text modality is attacked without extra machinery, while a field would be a second copy of claim semantics that can drift. The new disposition variant became a mode-guarded use of the existing keep-reframe, because the in-pass assessment ran with no new verdict, trait, or gate.

**Option 3: profile-level repair policy.** Each text-contract profile would declare which repair dispositions review may take. Deferred, not rejected: no second installation or episode demands it, and building profile machinery ahead of that need is the plan-first risk the proposal itself named. It stays in the proposal as undecided remainder.

**A dedicated pricing gate beside the premise gate.** The proposal left open whether the premise gate learns modality-conditional reading or a separate gate runs the honesty test. Resolved for the premise gate: it reads premises at stated modality and annotates counterexample shape as routing information. Drift tracking for pricing attestations needs factored `(note, attestation)` review pairs, which are themselves an open proposal, so it stays deferred.

**Deciding forces.** Every repair the pipeline offered weakened the claim; three worked episodes and the 22-note survey showed the cost; the first in-pass adequacy assessment showed that declared commitments can be attacked as ordinary content; and an idealization form must not become an immunizing stratagem, hence the adequacy record and the stated-refuter guard.

**Free choices.** Resolved: all three conversion paths the proposal named (write-time declaration, in-pass reframe, direct revision outside a pass) remain permitted under the same guards (decision 5). The proposal flagged "idealization" as a naming risk (praise-adjacent readings) and listed "first-order model" and "declared-ideal" as alternatives; the decision names the mode "ideal-type", the term the proposal's option 2 already used, and the record gives no further reason for that choice. Left open: profile-level policy declaration and attestation drift tracking. ADR 080 later removed in-pass mode conversion from the full pass (see Status).

## Consequences

- The 22 surveyed candidates are repairable by ordinary full passes; no migration or batch operation is needed.
- The narrowing-direction guards gain mode-specific companions: the refuter test already polices analytic narrowing; the stated-refuter guard polices vacuous statistical landings; the adequacy record polices immunized ideal-type landings.
- No frontmatter modality field ships. If corpus sweeps later need to enumerate declared ideal-type or statistical claims mechanically, addressability can be added then, under the derived-copy rule (checked or absent).
- Adopted in part from the design proposal "Repair dispositions for defeated claims are an epistemic policy with an option space", which keeps its undecided remainder: profile-level repair-policy declaration and freshness-store drift tracking for pricing attestations.

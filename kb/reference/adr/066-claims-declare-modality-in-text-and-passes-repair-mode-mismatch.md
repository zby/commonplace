---
description: "Claim modes and their refuters remain active in text and premise review; ADR 080 replaced in-pass mode conversion with author hand-back, and ADR 091 tightened the universal refuter"
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

1. **Three claim modes, refuter-defined.** Universal (a counterexample others can check again refutes, as amended by ADR 091), statistical (only prevalence evidence refutes; the claim must state what prevalence would refute it), ideal-type (a declared first-order model; refuted by unpriced-ordinary exceptions or dominance failure). Declared in [the theory collection contract](../../theory/COLLECTION.md) under "Claim modality" — the binding surface the full pass reads.
2. **Modality lives in the claim text, not frontmatter.** Title, thesis, or a named section carries the mode; an ideal-type claim carries its adequacy record (declared use, omitted mechanism, consequence bound, explanatory dominance) in the body. Undeclared text reads as universal. Rationale: the premise-decomposition gate quotes premises verbatim, so in-text modality is tested automatically, as the in-pass assessment demonstrated, while a frontmatter field would be a second copy of claim semantics that can drift. Mode is orthogonal to lifecycle stage (a status-conjecture note declares both when both apply).
3. **The premise-decomposition gate reads premises at their stated modality** and annotates every non-HOLDS premise's counterexample shape — `instance`, `prevalence`, or `priced-exception` — as routed attention, never a verdict.
4. **In-pass mode conversion is superseded by ADR 080.** The original decision let counterexample shapes route a bidirectional, mode-guarded keep-reframe. The full pass now hands mode mismatch back as a pending `revise`: its brief names candidate claims, target modes and their guards, but applies no claim change. A claim hedged below its warrant also routes to the author rather than being reframed in-pass.
5. **Author-applied conversions remain permitted under the mode guards.** A statistical claim must state its refuter; an ideal-type conversion must carry its adequacy record in the body. The next full pass supplies the deferred attack on those commitments as ordinary content. This permission does not restore in-pass conversion.

## Considered alternatives

The option space was developed in the design proposal "Repair dispositions for defeated claims are an epistemic policy with an option space", in its version before this ADR trimmed it. The proposal framed repair of defeated claims as an epistemic policy and offered three options.

**Option 1: document reframe-to-warranted as the universal policy.** Name the existing weaken-only repair set as this installation's policy in `kb/notes/COLLECTION.md` or the pass instruction, with no new mechanism. It lost as a complete answer because the idealization question stays unposable: a claim whose crisp form is refuted in detail but whose unification is worth keeping has no survivable declared form. Its core point, that the repair policy must be stated where it binds, survives in the "Claim modality" contract.

**Option 2 as proposed: a modality trait or frontmatter field, plus a new keep-as-idealization disposition.** The adopted decision takes this option's modes, reading rule (undeclared reads as universal), and two-stage adequacy assessment, but changes two parts. Modality moved into the claim text, because the premise-decomposition gate quotes premises verbatim, so in-text modality is attacked without extra machinery, while a field would be a second copy of claim semantics that can drift. The new disposition variant became a mode-guarded use of the existing keep-reframe, because the in-pass assessment ran with no new verdict, trait, or gate.

**Option 3: profile-level repair policy.** Each text-contract profile would declare which repair dispositions review may take. Deferred, not rejected: no second installation or episode demands it, and building profile machinery ahead of that need is the plan-first risk the proposal itself named. It stays in the proposal as undecided remainder.

**A dedicated pricing gate beside the premise gate.** The proposal left open whether the premise gate learns modality-conditional reading or a separate gate runs the honesty test. Resolved for the premise gate: it reads premises at stated modality and annotates counterexample shape as routing information. Drift tracking for pricing attestations needs factored `(note, attestation)` review pairs, which are themselves an open proposal, so it stays deferred.

**Deciding forces.** Every repair the pipeline offered weakened the claim; three worked episodes and the 22-note survey showed the cost; the first in-pass adequacy assessment showed that declared commitments can be attacked as ordinary content; and an idealization form must not become an immunizing stratagem, hence the adequacy record and the stated-refuter guard.

**Free choices.** At adoption, all three conversion paths the proposal named (write-time declaration, in-pass reframe, direct revision outside a pass) were permitted under the same guards. Write-time declaration and author-applied revision remain available; in-pass reframe does not. The proposal flagged "idealization" as a naming risk (praise-adjacent readings) and listed "first-order model" and "declared-ideal" as alternatives; the decision names the mode "ideal-type", the term the proposal's option 2 already used, and the record gives no further reason for that choice. Left open: profile-level policy declaration and attestation drift tracking. ADR 080 later removed in-pass mode conversion from the full pass (see Status).

## Consequences

- A full pass can identify a mode mismatch and produce a revision brief, but the author must make the claim-level repair. The original survey is not a current automatic-repair queue.
- The stated-refuter guard constrains statistical landings; the adequacy record constrains ideal-type landings. Premise review attacks the resulting commitments at their declared mode, whether the author introduced them at write time or through revision.
- No frontmatter modality field ships. If corpus sweeps later need to enumerate declared ideal-type or statistical claims mechanically, addressability can be added then, under the derived-copy rule (checked or absent).
- Adopted in part from the design proposal "Repair dispositions for defeated claims are an epistemic policy with an option space", which keeps its undecided remainder: profile-level repair-policy declaration and freshness-store drift tracking for pricing attestations.

**Limits.** The retained policy governs claim declaration and review in this KB; it does not authorize automatic claim conversion. The original 23-pass validation series accepted no in-pass conversion. Its missing positive conversion cases remain limits of that historical evidence, not a reason to exercise the retired path. The active consumers are the theory collection contract, premise-decomposition method and full-pass revision brief.

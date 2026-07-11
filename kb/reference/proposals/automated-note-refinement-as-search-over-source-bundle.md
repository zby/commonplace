---
description: "Proposal: build the automated note-refinement loop on a source bundle that emits a set of notes, not a single identity-stable note — reframing non-convergence (split, drift, kill) as search outcomes"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
---

# Automated note refinement as a search over a fixed source bundle

We already have the pieces of an automated note-refinement loop — critique gates, focused single-aspect passes, the autoreason tournament — and the obvious next step is to wire them into one procedure that runs unattended. The blocker is conceptual, not mechanical: **the process is not convergent.** Refining a note can drift it into a different note, split it into two, or establish that it should not exist at all. An optimization loop assumes a fixed object descending a fixed objective toward a fixed point; note-writing is a *search*, and the good output can sit arbitrarily far from the seed. This proposal holds the design that makes that acceptable: make the object of refinement a **source bundle** that emits a *set* of notes, not a single note the loop must keep identity-stable. Non-convergence then stops being a defect to suppress and becomes the expected shape of the work — not every starting idea is a good note, and the loop should be free to say so.

## Current state (as of 2026-06-15)

The single-note version is already prototyped; the bundle version is not.

- **`cp-skill-revise-autoreason`** is the working loop: keep the **incumbent** (do-nothing) as a first-class candidate, generate a critique-driven revision (B) and a synthesis (AB), rank the three blind with three judges by Borda count, and **stop after the incumbent survives two consecutive challenges**. This is already a non-convergence-aware stopping rule — "stop when challenges stop beating best-so-far," not "stop when the object stabilizes." But its object is **one note**, identity-preserving: it forbids semantic content loss, preserves link targets, and **cannot split** (`Preserve all semantic content, claims, evidence, caveats, qualifiers, and link targets from the incumbent A`).
- **The critique layer it would call** is itself proposed but partly shipped: [gate learning from accepted edits](./gate-learning-from-accepted-edits.md) (the human-accept oracle and gate lifecycle, plus a folded-in alternative stance — marginal-value stopping over an open-ended, ad-hoc lens catalogue). Atomic gates, the selector, and bundle loading have shipped under the review subsystem.
- **The workshop primitive already exists.** `kb/work/<workshop-name>/` is a mutable working set whose value is *consumed*: it produces library artifacts and is deleted ([a functioning KB needs a workshop layer](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md)). Crucially, the COLLECTION rules **forbid linking into `kb/work/`** — nothing in the library imports from a workshop. The promotion path (`cp-skill-write` then `cp-skill-connect`) is what confers graph identity on a finished note.

## The design

Make the object a **bundle**: a workshop directory holding the **fixed source material** plus zero-or-more draft notes. The procedure is a function, not an in-place edit:

```
refine : bundle (sources + 0..n drafts) → set of library notes
```

The invariant the search is anchored to is the **sources plus the KB's scope and quality bar** — never any particular draft. This dissolves all three non-convergence cases into ordinary outcomes:

- **Split** — the bundle emits 2 notes instead of 1. No longer a special case the loop must detect and refuse; just a larger output set.
- **Drift** — the bundle's claims move while the sources stay fixed. Legitimate, because identity was never pinned to a draft.
- **Kill** — the bundle emits 0 notes. A *good* outcome (the seed was not a note), not a failure to recover from.

**Graph identity is conferred only at promotion.** While refinement runs inside `kb/work/`, no backlink, `derived-from` edge, or description is committed, so splitting and drifting break nothing — there is nothing yet to break. The final step runs `cp-skill-write`/`cp-skill-connect` on each emitted note to wire it into the library. This is also why the bundle, not the note, is the safe object: a note carries graph identity that a non-convergent loop would have to forge; a workshop carries none until it closes.

**The incumbent safeguard generalizes from note to set.** Autoreason's defense against silently refining a good note into a worse different one — the incumbent never loses by default; a challenger must *win* — lifts directly: the incumbent is the **current emitted set**, and a challenger set (which may have a different cardinality) must beat it. The stopping rule is unchanged in spirit: budget exhaustion, or the incumbent set surviving K consecutive challenges.

## Free choices

- **Granularity of the object.** Source bundle (this proposal's lead) versus **claim-set** — extract atomic claims, refine each, re-bundle into notes at the end, making split the *default* rather than an operation. The claim-set framing aligns with the one-claim-per-note body-composability convention but needs a claim store the workshop does not yet have. Bundle is the cheaper first cut; claim-set is the more principled endpoint.
- **Set-valued judging — the one genuinely new mechanism.** Autoreason's judges score a single packet. Comparing a 1-note incumbent against a 2-note challenger needs a judge that scores **coverage and non-redundancy of the set**, not per-note quality summed — otherwise splitting always wins (more notes, more surface) or never wins (each fragment weaker than the whole). Options: a holistic set judge; per-note judging plus an explicit redundancy/coverage penalty; or decorrelated judges each owning one axis (coverage, non-redundancy, per-note reach) aggregated — the [decorrelated-checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) move. This is the part worth designing carefully; the rest is plumbing.
- **How far drift may run.** Unbounded (the loop may walk arbitrarily far from the seed, judged only on output quality) versus tethered (a drift penalty or a hard requirement that every emitted note still be supported by the bundle's sources). Tethering trades reach for provenance safety.
- **Where the incumbent set and intermediate drafts live.** A dedicated `kb/work/<refine-run>/` workshop per run (consistent with the workshop lifecycle, auto-discarded) versus an ephemeral scratch area outside `kb/`. The workshop choice buys inspectability and resumability at the cost of `kb/work/` churn.
- **Promotion trigger.** Auto-promote the winning set when the loop stops, versus emit the set into the workshop and require a human accept before `cp-skill-connect` wires it in. The human-accept gate aligns with [an accepted edit verifies the change, not the rule](../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) — the strongest oracle stays "did a human accept this set."

## Adoption criteria

Adopt as a framework procedure when, measured against running `cp-skill-revise-autoreason` per note:

- the bundle loop produces **split outcomes that a human accepts** at a rate that justifies the machinery — if it never usefully splits, the single-note loop is sufficient and simpler;
- **kill outcomes are trusted** — operators act on "this seed is not a note" rather than overriding it, evidence the anti-convergence stance pays;
- set-valued judging ranks split/merge/drift challengers against the incumbent set without a systematic bias toward larger or smaller sets;
- promoted notes pass `cp-skill-validate` and survive `cp-skill-connect` with no more orphaning or stale-edge debt than hand-written notes.

## Risks

- **Runaway drift / non-termination.** With no fixed point, the loop can wander or churn indefinitely; the budget bound and the incumbent-set survival counter are load-bearing, not optional — the same backstop autoreason already relies on.
- **Set judging is harder to get right than note judging.** A miscalibrated coverage/redundancy score silently biases every run toward over-splitting or never-splitting; this is the most likely place the design fails quietly.
- **Provenance loss under drift.** A note that has drifted far from its sources may no longer be grounded by them while still claiming a `derived-from` edge — the tether choice exists precisely to bound this, and an untethered loop must re-verify grounding at promotion.
- **Losing a good incumbent to a confident-but-worse challenger** — the [fluency-smoothing](../../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md) failure the judges themselves are subject to. Blind judging and a default-win incumbent mitigate but do not eliminate it; the recovery is a separate check with teeth, not the generator volunteering quality.
- **`kb/work/` churn.** A workshop per run accumulates if runs are not closed; the workshop lifecycle already prescribes deletion, but an automated loop must actually perform it.

## Open questions

- The convergence-vs-search reframing is a transferable claim, not a system-specific constraint — per the proposals contract it should be **promoted to a theory note in `kb/notes/`** (something like *"automated refinement is a search over a fixed source bundle, not convergence of a single artifact"*) and cited here via `rationale`, rather than living only in this proposal's opening.
- Does the bundle object subsume re-distillation? [Evolving understanding needs re-distillation, not composition](../../notes/evolving-understanding-needs-re-distillation-not-composition.md) already argues that updating a settled note means re-running distillation from sources — which is exactly `refine : bundle → noteset` applied to an existing note plus new sources. Is automated refinement just re-distillation with a tournament bolted on?
- Minimal set-judge: can per-note Borda plus a single scalar redundancy penalty match a holistic set judge, or does coverage need its own decorrelated judge?
- Where do sources that *enter mid-run* attach (a refinement that pulls in a new source while running)? Does that re-open the "fixed" bundle, and does the incumbent set reset?

---

Relevant Notes:

- [a functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — rationale: the workshop is the bundle object — a consumed working set that emits library artifacts and carries no graph identity until it closes
- [distillation](../../notes/definitions/distillation.md) — rationale: `bundle → note set` is a distillation; the loop is an automated, tournament-judged distiller
- [evolving understanding needs re-distillation, not composition](../../notes/evolving-understanding-needs-re-distillation-not-composition.md) — rationale: updating a settled note is re-distilling from sources — the same bundle→noteset operation applied to an existing note
- [an accepted edit verifies the change, not the rule](../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) — rationale: the human-accept oracle that the promotion gate and incumbent-set comparison rest on
- [error correction works above chance with decorrelated checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — rationale: set-valued judging can use decorrelated per-axis judges (coverage, non-redundancy, reach) instead of one holistic score
- [LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on](../../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md) — rationale: the judges are subject to the fluency-smoothing they police; recovery needs a separate check with teeth, not the generator's own confidence
- [the boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — rationale: the loop can only be trusted as far as its stopping oracle verifies; prose is the oracle-poor register where this bites hardest
- [gate learning from accepted edits](./gate-learning-from-accepted-edits.md) — see-also: the gate lifecycle, accepted-edit oracle, and open-ended-lens alternative stance this loop would feed and draw from

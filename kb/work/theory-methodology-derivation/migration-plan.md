# Migration plan: replace distillation with derivation

Goal (operator-set): **replace "distillation" with "derivation" as the KB's term.** Prerequisite: clean up the KB so the current usages are cleanly separated — some usages split into their components, some replaced by a different term entirely. This file sequences that work against the [usage audit](./distillation-usage-audit.md)'s evidence.

## End state

- `derivation` is a defined term (graded entailment: output inside the source's claim closure, given the consumer's goal; verification by matching, cache/staleness semantics). `selection` is defined lightly (consumer-directed choosing — of source material and of which consequences to derive; it carries the targeting that the old definition called "use-shaping").
- `discovery` owns all ampliative traffic, graded by the [polation axis](./polation-structure-of-generalization.md): routine induction (extrapolation) at the shallow end, generative insight (hyperpolation) at the deep end.
- Mixed artifacts carry an explicit dominance **bet** (see the [vocabulary thread](./derivation-selection-vocabulary.md)'s bet doctrine) instead of a hybrid category.
- "Distillation" survives only in: external systems' own command names, the ML-knowledge-distillation sense in sources, and historical ADR text.

## Waves

Ordered so each wave makes the next one mechanical. Validate (`cp-skill-validate`) after each wave; commit waves separately.

### Wave 0 — receiving vocabulary (blocks everything)

No usage can be re-worded until the target terms exist and are constrained.

1. Draft `kb/notes/definitions/derivation.md` — the entailment subtype, explicitly graded (checkability degrades with source coherence; even derived artifacts are re-verified by judgment per `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`). Decide whether `selection` gets its own definition file or a section inside derivation's.
2. Amend `kb/notes/definitions/../discovery-is-seeing-the-particular-as-an-instance-of-the-general.md` (and/or a new short discovery definition note if the claim note shouldn't carry definitional load) to own the routine-induction end, using the polation grading.
3. Write the bet doctrine down where it can be cited (likely a section of the derivation definition, or a small note) — mixed artifacts are classified by dominant regime as a falsifiable commitment with stated detection signatures.

Output check: the three terms must jointly cover every non-META instance class in the audit, with the authored-judgment residue explicitly assigned (accumulation/constraining) or explicitly deferred.

### Wave 1 — split the entangled usages (the cleanup the rename needs)

The audit's AMP and MIX instances, ~30 in the library. These are *semantic* edits — each one re-words a passage to name the actual operation, not a token swap:

- The definition's own instance list (`definitions/distillation.md:23,25`): move "repeated failures → gate instruction" and "notice patterns" to discovery examples.
- The trace→rule ladder cluster: relabel the "Distill" rung (`trace-derived-memory-earns-authority...`, `an-outcome-check-licenses-replay...`, `an-accepted-edit-verifies-the-change...`, `abstract-an-experience...`) to induction/discovery vocabulary; their oracle theory transfers unchanged.
- `distillation-is-transformation-not-selection.md`: split its argument — anti-mere-selection (kept, becomes an argument *for* derivation over selection) vs its ampliative evidence (re-filed as discovery). Likely outcome: retitle and rewrite, since both the title's subject and its evidence change vocabulary.
- `write-instruction.md`: resolve the internal tension — its "repeated manual operations → stable procedure" framing is discovery (extrapolative), its "distilled from methodology" step is derivation; say both, correctly.
- `spec-mining-as-codification.md:19` and similar: one-line re-words (mined regularities are extrapolations, then codified).
- Two-stage pipeline descriptions (mostly agent-memory-systems prose, but a few library instances): name the stages separately where separable; where entangled, apply the bet and record it.

### Wave 2 — the mechanical rename (DER and SEL instances)

~120 instances that are already derivation- or selection-shaped: token-level re-wording, low risk, batched by collection. Includes `skills-derive-from-methodology-through-distillation.md` → title simplifies to its own first clause.

### Wave 3 — META surfaces (the infrastructure)

- `AGENTS.md` vocabulary entry: distillation → derivation (+ selection), discovery entry updated.
- `definitions/distillation.md`: rewrite as a stub/redirect defining the old term in terms of the new ones, or delete with backlink fixes — per repo norms (no backcompat) probably delete once nothing links to it.
- Tag migration: `distillation` tag → `derivation` (learning-theory `covered_by`, tag-README with its marks, per-note tag fields) — one sweep, validator-checked.
- `Distilled into:` footer: per the audit these span SEL/DER/AMP, so each footer gets classified during Wave 1/2 passes; the label itself becomes `Derived into:` where derivation, or a discovery-side label otherwise. Update `link-vocabulary.md` and `cp-skill-write`.
- Filename renames (5 notes) with backlink rewrites — use the relocation tooling if the move-map engine workshop has landed anything usable.
- ADR: record the whole decision as an ADR once Waves 0–1 prove the scheme (worked-case-first). ADR 011's hardcoded gloss and the review-gate examples get updated here.

### Deferred / out of scope

- `kb/agent-memory-systems` type-spec (`Distilled form:` field, "raw → distilled loop" contract) — self-contained surface, ~100 boilerplate instances; migrate on its own schedule after the library settles, with the field's replacement name drawn from the discovery side (the field's content is usually ampliative).
- `kb/sources/` and external command names — never touched.
- The crystallized-reasoning note's coinage — separate decision, out of this workshop's scope.

## Best next step (analysis)

The single highest-leverage step is **Wave 0, item 1: draft the derivation definition.** Reasons:

- Everything downstream cites it; nothing upstream blocks it — the routing question is settled (extend discovery, polation grading) and the audit supplies the definition's worked examples and its required caveats (gradedness, the authored-judgment gap, the selection collision in `memory-management-policy...`).
- It is the cheapest way to stress-test the whole scheme: if the definition can classify the audit's hard cases (trace→rule ladder, ad-hoc distillation, skill-creator loop) cleanly on paper, the waves are safe; if it can't, better to find out in one file than mid-sweep.
- Per repo norms it should be drafted here in the workshop, run against the audit's hard cases as its Misuse/Exclusions material, then promoted via `cp-skill-write` together with the discovery amendment — the pair is one atomic vocabulary change.

Risk to watch: Wave 1 rewrites load-bearing theory notes (the trace→rule oracle cluster). Those edits should go through review gates, not just token edits — the semantic-review machinery exists for exactly this.

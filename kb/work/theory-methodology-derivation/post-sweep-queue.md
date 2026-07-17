# Post-sweep queue

Edits parked while the final Wave 1 review sweep runs (its baselines key on the swept files' current content; editing mid-sweep orphans them). Apply after the sweep's fixes are committed.

## 1. Structure note: two physics additions (operator-approved 2026-07-17)

Target: `kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md`. Both keep the note's hedged register (illustration, not evidence). Re-gate after applying.

**(a) Effective-theory instance** — replace the current intro sentence of the effective-field-theory paragraph ("Effective field theory offers two useful analogies, not grounds for this model.") with:

> Physics already operates this architecture. An effective theory — thermodynamics over statistical mechanics, ray optics over wave optics — is worked out from a deeper theory, dramatically cheaper to apply, and strictly less general, with a known breakdown boundary at which one drops back to the fundamental layer; physics retains both layers permanently because the domain of application is open-ended. This is an illustration from another discipline, not evidence for the maintenance model.

Then the Penco citation and the matching/cutoff/correspondence bullets continue unchanged. Optional clause: **UV completion** (methodology first, theory reconstructed afterward) as the physics name for the spec-mining direction the note already links.

**(b) Physics–chemistry mixed case** — append to the mixed-artifact caveat section (after the Batterman paragraph):

> The physics–chemistry pair shows the mix at discipline scale. Chemistry is in principle grounded in quantum mechanics, and computational quantum chemistry serves as a live fallback for cases chemical rules do not cover, with recurrent results promoted into chemical practice. Yet chemistry's organizing vocabulary — bonds, electronegativity, aromaticity — is native to its own level of description and resists smooth derivation from the deeper theory; revising the physics does not invalidate it. A chemist's working theory is a mixed artifact: partly recomputable from the deeper layer, partly level-native structure maintained on its own terms.

Reference if wanted: Eric Scerri on the periodic table and reduction (philosophy of chemistry; would need an ingest to cite properly).

## 2. Vocabulary-collisions note: corpus-evidence decision

The sweep's fix pass generalized away the concrete corpus check from the clausal-binding section (the 36-occurrence grep of `actionable`, its reproducible command, and the "not one predicates it of a methodology" finding — full version in commit `9f8bd753`). Operator decision needed: restore date-stamped (the way the audit's 464 figure is handled) or accept the generalized wording.

## 3. Wave 3 prep (inventory computed 2026-07-17, pre-deletion)

- **`definitions/distillation.md` deletion**: 28 files link to it — AGENTS.md, 2 instruction files (`example-onboard-second-brain.md`, review gate `undefined-terms.md` — the gate uses it as its worked example), 5 sibling definitions (codification, constraining, context-engineering, directed-reading, text-contract), `distillation-README.md`, `learning-theory-README.md`, `tags-README.md`/`README.md` navigation, and ~16 content notes. Salvage map is in `wave-1-worksheet.md`; the Faithful-Self-Evolvers caveat still needs a target (candidates: `knowledge-storage-does-not-imply-contextual-activation`, `claw-learning-loops…`).
- **Filename renames remaining** (4): `distillation-README.md` (retires with the tag), `distillation-status-determines-directory-placement.md`, `maintenance-operations-catalogue-should-stage-distillation-into.md`, `skills-derive-from-methodology-through-distillation.md` (entangled — held back in obvious-cases, needs its rewrite first). Use `commonplace-relocate-note`; rename before gating.
- **Tag retirement**: `distillation` out of learning-theory's `covered_by`; retire `distillation-README.md`; redistribute member notes.
- **AGENTS.md vocabulary**: remove the Distillation entry; `discovery lifecycle` already has its definition note — check whether it gets a vocabulary line (net 0) or not (net −1).
- **ADR**: draft in this workshop (next step), promote once Wave 1 fixes are committed.

## 4. Carried from closed threads

- Polation thread open questions, dropped unless someone picks them up: (a) polation distance as a review-time gate signal ("are this note's claims entailed / extrapolated / off-manifold relative to its cited sources?") — would make the dominance bet checkable; (b) Ord's flexible-vs-strict polation as a frame for quote-fidelity vs gloss in source handling.

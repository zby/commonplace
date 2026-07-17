# Post-sweep queue

Edits parked while the final Wave 1 review sweep runs (its baselines key on the swept files' current content; editing mid-sweep orphans them). Apply after the sweep's fixes are committed.

## 1. Structure note: two physics additions (operator-approved 2026-07-17) — DONE 2026-07-18

Both applied after the sweep landed, adapted to the note's post-fix hedged register (effective-theory instance into the analogy paragraph; physics–chemistry pair as a second illustration in the mixed-artifact caveat). Validation clean. Re-gating happens with the next sweep. Original drafts kept below for reference.

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

## 4. Reframe the insight note as the conjecture phase (operator direction 2026-07-17) — DONE 2026-07-18

Executed: renamed to `conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md` (34 files' links rewritten, properdocs redirect added); body reframed with the co-arising claim explicitly depth-graded (recognition precedes positing at the shallow end, full co-arising only at the generative-model end — avoiding the overclaim a bare title swap would have inherited); three-depths table tied to the lifecycle's polation axis; Darwin/Fleming examples recast in lifecycle phases; the `Distilled into:` footer classified as `Derived into:`; the lifecycle note's routing rule now hands off to this note for the conjecture phase's internal structure (its old "degenerate case" section had already been replaced by the sweep's compatible "Compressed cases do not skip testing"). Nineteen inbound anchor texts updated from the old title; the `kb/index.md` / tag-README "discovery as operation" framing sentences left for Wave 3 (entangled with the `distillation` vocabulary entry). Validation clean on the note, the lifecycle definition, and both tag heads. Original plan kept below.

`discovery-is-seeing-the-particular-as-an-instance-of-the-general.md` should be just the abduction part — its content (dual structure, three depths, recognition cost, examples) is conjecture-phase material, not a characterization of discovery as a whole, and its current title binds bare "discovery" to the insight act, which the lifecycle definition forbids.

- **Retitle**: "Conjecture is seeing the particular as an instance of the general"; rename via `commonplace-relocate-note` (~31 inbound links incl. `kb/index.md`, `discovery-README.md`, `learning-theory-README.md`, nine source ingests). Rename before gating.
- **Body**: reframe opening around the conjecture phase of the [discovery lifecycle](../../notes/definitions/discovery-lifecycle.md); the three-depths table is the conjecture's internal grading (aligns with the polation table: shared structure ≈ extrapolation, generative model ≈ hyperpolation); Fleming becomes the clean lifecycle case (conjecture opens, test/acceptance stabilizes) instead of a "boundary of the claim". Widens the claim to routine conjecture (failures→gate) at shallow depth — deliberate.
- **Lifecycle note** (in-sweep, so blocked): rewrite its "degenerate case" section — instant insight = a conjecture whose evidence is pre-accumulated so the test collapses, not a telescoped whole lifecycle; repoint its Relevant Notes link to the retitled note as the conjecture-phase description.
- The note's legacy `Distilled into:` footer (cp-skill-connect) is one of the pending footer classifications — classify during the same edit.

## 5. Carried from closed threads

- Polation thread open questions, dropped unless someone picks them up: (a) polation distance as a review-time gate signal ("are this note's claims entailed / extrapolated / off-manifold relative to its cited sources?") — would make the dominance bet checkable; (b) Ord's flexible-vs-strict polation as a frame for quote-fidelity vs gloss in source handling.

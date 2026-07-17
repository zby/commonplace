# Migration plan: replace distillation with derivation

Goal (operator-set; revised 2026-07-17): **retire "distillation" without a successor technical term.** "Derive" stays ordinary English everywhere — no definition note, no vocabulary entry. The theory that backed the old term moves into citable notes and the link grammar. Prerequisite unchanged: clean up the KB so the current usages are cleanly separated — some split into their components, some replaced by plain language or routed to discovery. This file sequences that work against the [usage audit](./distillation-usage-audit.md)'s evidence.

## End state

- No successor term. The theory of entailment-preserving reshaping (graded entailment, matching, fallback, cache/staleness semantics) lives in the two-layer structure note as canonical citable claims. A note that needs the strong sense cites the structure note or states the specific support inline — the same way any claim cites its grounds.
- The link grammar carries the boundary: `Derived from:` / `Derived into:` semantics are specified in `link-vocabulary.md` — the label asserts the artifact adds no substantive claims beyond the source; ampliative lineage takes a discovery-side label. Labels and review gates police the DER/AMP boundary; prose never did (the audit shows `distillation` drifted with a definition in place).
- The **discovery lifecycle** owns all ampliative traffic, graded by the [polation axis](./polation-structure-of-generalization.md): routine induction (extrapolation) at the shallow end, generative insight (hyperpolation) at the deep end. The compound is the technical term (decided 2026-07-17, per the naming rule in [prose-has-no-scope](../vocabulary-governance/prose-has-no-scope.md)); bare "discovery" stays ordinary English.
- Mixed artifacts carry an explicit dominance **bet** (see the [vocabulary thread](./derivation-selection-vocabulary.md)'s bet doctrine) instead of a hybrid category.
- "Distillation" survives only in: external systems' own command names, the ML-knowledge-distillation sense in sources, and historical ADR text.
- Net vocabulary diff: 0, with a quality upgrade. `distillation` leaves the AGENTS.md vocabulary; `discovery lifecycle` enters (there is no existing `discovery` entry to amend). The incoming term is a greppable multi-word coinage, not a captured common word — the exposure class that produced the migration.

## Execution status (2026-07-17)

- **First semantic wave applied and committed** (`80f47b41`): the trace→rule ladder cluster renamed to abstraction vocabulary (the six notes plus `agent-memory-README.md`), with the note renames `trace-derived-memory-earns-authority…` → `trace-extracted-…` and `use-trace-derived-extraction` → `use-trace-extraction-as-meta-learning` and corpus-wide backlink fixes. Validation clean. Residues — and the lesson that sweep patterns must match single-l `distil` — recorded in [obvious-distillation-cases.md](./obvious-distillation-cases.md).
- **Adjacent infrastructure committed** (`ca1ea328`, `5ed02f6a`): `trace-derived` retired in favor of the coined compounds `trace-extracted` (lineage) and `trace-learning` (loop tag, type-spec sections) across agent-memory-systems, `systems.csv`, the renderer, and tests — the naming rule applied to infrastructure vocabulary.
- **Workshop self-references cleaned** (`8dd16304`): the threads no longer use "distillate"/"distillation" as operator vocabulary while arguing for its retirement.
- **Theory promoted** (`e429e82e`): the scope/collision reflection is now the library note `vocabulary-collisions-prevented-at-write-time-not-read-time.md` — the uniqueness invariant and the multi-word-coinage rule are citable claims the remaining waves build on.
- **Ordering note**: these Wave 1-shaped edits deliberately ran ahead of Wave 0, under the staging rule in [obvious-distillation-cases.md](./obvious-distillation-cases.md) — only cases whose replacement follows from the note's own argument, needing no receiving vocabulary.
- **Wave 0 item 1 done** (`7e9a63c8`): the structure note is promoted as `kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md` — one note, one claim; open-endedness argument folded in as grounds; promotion criterion kept in the note (no separate gate artifact); maintenance semantics stated as citable claims; physics terms cited as loans. Stress test passed: all ten hard-case rows in [receiving-vocabulary-draft.md](./receiving-vocabulary-draft.md) classify using the note plus plain language, confirming the later waves are expressible as prose + label + citation. The two-layer thread in this workshop is now source material with a durable home; a review-gate pass over the promoted note is still worth scheduling before Wave 1 leans on it.
- **Wave 0 item 2 done** (`0dc7fb4c`): `link-vocabulary.md` now defines the two lineage regimes — `derived-from`/`Derived into:` (no added claims; recomputable-copy maintenance, citing the structure note) vs `abstracted-from`/`Abstracted into:` (claims exceed the instances; authority earned by testing) — with the classifying question, the dominant-regime call for mixed artifacts, and `Distilled into:` retired for new writing. The edit also fixed a latent collision in the catalogue itself: the old `derived-from` row defined the label as "abstraction provenance". 15 existing `Distilled into:` footers plus the pre-existing `derived-from` edges are flagged as unclassified lineage pending the Wave 1/2 passes. `cp-skill-write`'s footer prescription updated to match.
- **Wave 0 item 3 done** (`7ac83249`) — **Wave 0 complete.** `kb/notes/definitions/discovery-lifecycle.md` defines the compound (phases with Peircean analogues, polation grading with the no-geometry caveat, ampliative traffic entering at the conjecture stage, bare "discovery" ordinary English); the co-arising insight note links in as the degenerate case; the `discovery` tag-README (`complete: true`) lists it. The draft's six pre-Wave-1 acceptance tests all pass: every non-META audit class has a receiving home (derived/abstracted labels, conjecture stage, accumulation/constraining for authored judgment), the trace→rule ladder already rewrote without a bridge term, conjecture and accepted status are distinguishable, consumer-directedness and the coverage bet live in the structure note's region choice, form-vs-content distance is stated, and every rewrite names its control regime via label or citation.
- **Next**: Wave 1 — the entangled semantic cases, now unblocked: the distillation definition's instance list, the `distillation-is-transformation-not-selection` split, `write-instruction.md`'s two provenance stories, two-stage pipeline descriptions, and classification of the 15 legacy `Distilled into:` footers and pre-existing `derived-from` edges against the new label semantics. Load-bearing rewrites go through review gates. Then the re-scoped Wave 2 and the Wave 3 META surfaces.

## Waves

Ordered so each wave makes the next one mechanical. Validate (`cp-skill-validate`) after each wave; commit waves separately.

### Wave 0 — receiving vocabulary (blocks everything)

No usage can be re-worded until the target terms exist and are constrained.

**Minimality constraint** (operator, 2026-07-17): technical terms that are also ordinary English words are inherently confusing — marker-scoping localizes the ambiguity but does not remove it, and every dual-sense word taxes every future reader with a which-sense resolution. The mitigation is a minimal technical vocabulary (this is `minimum-viable-vocabulary-is-the-naming-set-that-most-reduces` applied to the framework's own reflective terms): a word earns a definition note only when its operational consequences — verification and maintenance semantics — differ enough from plain prose that inline support can't carry them. Applied strictly (operator, same day), `derivation` itself fails the bar: the natural meaning of "derive" is close enough, and a note that needs the strong sense can cite the theory directly. So Wave 0 promotes theory and label grammar, not definitions. The physics loans (matching, cutoff, correspondence) stay cited-in-passing, not coined; the authored-judgment residue reuses accumulation/constraining; polation stays a source citation grading discovery internally. The constraint also ratifies the routing decision — the ampliative operation gets no separate captured word; its technical handle is the compound `discovery lifecycle` (naming decision of 2026-07-17), with bare "discovery" staying ordinary English.

1. Promote the two-layer structure note with the theory stated as citable claims: graded entailment-preservation (checkability degrades with source coherence, per `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`), matching, fallback, cache/staleness semantics. This note is the canonical home a rewritten usage points at when it needs the strong sense; the selection material (consumer-directedness, the coverage bet) folds in here too.
2. Specify the link-label semantics in `kb/reference/link-vocabulary.md` (moved up from Wave 3 — the labels are now the only surface where the entailment claim is formally made): `Derived from:` / `Derived into:` asserts the artifact adds no substantive claims beyond the source; ampliative lineage takes a discovery-side label. Update `cp-skill-write` to match.
3. Amend `discovery-is-seeing-the-particular-as-an-instance-of-the-general.md` (and/or a new short definition note if the claim note shouldn't carry definitional load) to own the routine-induction end, using the polation grading. The technical term the amendment introduces is **discovery lifecycle**; bare "discovery" stays ordinary English. The compound needing a citable home strengthens the separate-note option — a definition note titled by the compound, leaving the existing title-as-claim note's insight claim untouched.
4. Write the bet doctrine down where it can be cited (a section of the structure note, or a small companion note) — mixed artifacts are classified by dominant regime as a falsifiable commitment with stated detection signatures.

Output check: every non-META instance class in the audit must have a receiving home — plain prose plus structure-note citation (DER/SEL), the discovery lifecycle (AMP), or accumulation/constraining (authored judgment) — with none left implicitly bridged by an undefined strong sense of "derive".

### Wave 1 — split the entangled usages (the cleanup the rename needs)

The audit's AMP and MIX instances, ~30 in the library. These are *semantic* edits — each one re-words a passage to name the actual operation, not a token swap:

- The definition's own instance list (`definitions/distillation.md:23,25`): move "repeated failures → gate instruction" and "notice patterns" to discovery examples.
- The trace→rule ladder cluster: relabel the "Distill" rung (`trace-extracted-memory-earns-authority...`, `an-outcome-check-licenses-replay...`, `an-accepted-edit-verifies-the-change...`, `abstract-an-experience...`) to induction/discovery vocabulary; their oracle theory transfers unchanged.
- `distillation-is-transformation-not-selection.md`: split its argument — anti-mere-selection (kept, becomes an argument *for* derivation over selection) vs its ampliative evidence (re-filed as discovery). Likely outcome: retitle and rewrite, since both the title's subject and its evidence change vocabulary.
- `write-instruction.md`: resolve the internal tension — its "repeated manual operations → stable procedure" framing is discovery (extrapolative), its "distilled from methodology" step is derivation; say both, correctly.
- `spec-mining-as-codification.md:19` and similar: one-line re-words (mined regularities are extrapolations, then codified).
- Two-stage pipeline descriptions (mostly agent-memory-systems prose, but a few library instances): name the stages separately where separable; where entangled, apply the bet and record it.

### Wave 1.5 — dissolved (2026-07-17)

An incoming-term audit was planned here while the direction was still "make `derivation` a defined term": ~518 loose `deriv*` occurrences across 166 library files would have become ambiguous against a strict technical sense. With no successor term, prose "derive" cannot be a false signal, and the audit collapses to the labeled edges only — the ~27 existing `Derived from:`/`derived-from` link labels, each of which gets classified against the Wave 0 label semantics during the Wave 1/2 passes that already touch every footer. Kept as a record of why the wave existed and why it went away.

### Wave 2 — the mechanical rename (DER and SEL instances)

~120 instances that are already derivation- or selection-shaped: token-level re-wording, low risk, batched by collection. Includes `skills-derive-from-methodology-through-distillation.md` → title simplifies to its own first clause.

### Wave 3 — META surfaces (the infrastructure)

- `AGENTS.md` vocabulary entry: remove `distillation`, amend `discovery`; nothing enters (net −1).
- `definitions/distillation.md`: delete with backlink fixes once nothing links to it (no successor to redirect to — per repo norms, no backcompat stub); its salvageable material routes to the structure note and the discovery amendment.
- Tag retirement: the `distillation` tag has no successor tag — remove it from learning-theory's `covered_by`, retire its tag-README, and redistribute member notes to the tags matching their post-migration classification (discovery-side or existing learning-theory children) — one sweep, validator-checked.
- `Distilled into:` footer: per the audit these span SEL/DER/AMP, so each footer gets classified during Wave 1/2 passes against the label semantics fixed in Wave 0 — `Derived into:` where no-added-claims holds, a discovery-side label otherwise.
- Filename renames (5 notes) with backlink rewrites — use the relocation tooling if the move-map engine workshop has landed anything usable.
- ADR: record the whole decision as an ADR once Waves 0–1 prove the scheme (worked-case-first). ADR 011's hardcoded gloss and the review-gate examples get updated here.

### Deferred / out of scope

- `kb/agent-memory-systems` type-spec (`Distilled form:` field, "raw → distilled loop" contract) — self-contained surface, ~100 boilerplate instances; migrate on its own schedule after the library settles, with the field's replacement name drawn from the discovery side (the field's content is usually ampliative).
- `kb/sources/` and external command names — never touched.
- The crystallized-reasoning note's coinage — separate decision, out of this workshop's scope.

## Best next step (analysis)

The single highest-leverage step is **Wave 0, items 1–2 together: promote the structure note and fix the label semantics.** Reasons:

- The structure note is now the canonical home everything downstream cites, and the label grammar is the only surface where the entailment claim is formally made — nothing in Wave 1 can be reworded safely until both exist.
- The stress-test survives the direction change: the [receiving-vocabulary draft](./receiving-vocabulary-draft.md)'s hard-case table still has to classify cleanly — but the classifications now decide which label or citation each case gets, not which defined term. If the trace→rule ladder, ad-hoc distillation, and the skill-creator loop can be expressed as plain prose + label + citation on paper, the waves are safe.
- The discovery amendment promotes together with the structure note — the pair is one atomic change (AMP traffic needs its receiving lifecycle the moment the old term stops covering it).

Risk to watch: Wave 1 rewrites load-bearing theory notes (the trace→rule oracle cluster). Those edits should go through review gates, not just token edits — the semantic-review machinery exists for exactly this.

Working draft: [receiving-vocabulary-draft.md](./receiving-vocabulary-draft.md) holds the former candidate definitions; its derivation/selection material is now source text for the structure note's theory section and the link-vocabulary spec, and its discovery amendment and hard-case table remain live as written.

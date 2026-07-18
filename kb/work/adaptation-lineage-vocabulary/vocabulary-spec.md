# Vocabulary spec (locked)

The output of §1 of [execution-plan.md](./execution-plan.md). Sections 3 and 4 of the plan execute against this without further judgment calls; §5's collection-adoption sweep and the AGENTS.md wording (the one remaining item from the README's "Decisions to finish") still need drafting.

## `adapted-from` (general relation)

**Truth condition.** Asserts the target's specific content — its selection, structure, or wording — was substantially worked up from the source's specific content for a use the source didn't natively serve, without asserting that content is complete, entailed, or generalizes beyond the source.

**Test.** If the source were removed or materially changed, would the target's actual content need rewriting (not just its motivation)? Yes → material input, `adapted-from`. If the target would be unchanged because the source only justified or inspired the work → background influence; use `rationale`, `evidence`, `grounds`, or `see-also` instead.

**Maintenance consequence.** Source change flags the target for a judgment recheck of fit — not automatic recomputation (unlike `derived-from`: there is no single correct adaptation to re-derive and compare against), and not a fresh-evidence retest (unlike `abstracted-from`: there is no generalization claim to falsify).

**Footer.** `Adapted into:` — a third registered footer section, recorded at the source only, same forward-pointer-only convention as `Derived into:` / `Abstracted into:`.

## `operationalized-from` (minted alternative, not a stacked child)

**Truth condition (portable, not pairing-defined).** Narrows `adapted-from`'s test: the target adds ordering, defaults, or stopping conditions the source doesn't fix, while adding no substantive claims beyond it. The test itself names no collections — it applies wherever a source is worked into an executable/operational shape, not only methodology → procedure. (This is what `skills-derive-from-methodology.md` already argues about itself in its second half — "a different person would produce a meaningfully different skill" — the note's reasoning was right, the label was wrong.)

**Current authorization (pairing-scoped, evidence-gated, not a definitional limit).** Today only `kb/notes/` methodology notes → `kb/instructions/` procedures, skills, checklists, and gates is authorized in `COLLECTION.md`, because that's the only pairing with live corpus evidence (Finding 3 and its ~15 citing notes). An authoring-time *alternative* to `adapted-from` for this pairing — never record both edges for the same relationship. If a structurally identical case shows up in a different pairing later, the truth condition already covers it; extending authorization needs only a new `COLLECTION.md` entry, not a new relation name — same architecture as `derived-from`'s per-pairing authorization below, not a special case.

**Maintenance consequence.** Same as `adapted-from` — flag for recheck, not recompute.

**Footer.** `Operationalized into:` — a fourth registered footer section, same recording convention.

## Recording direction and collection authorization

Resolves the tension between a target-side identifier (`adapted-from`) and a source-side footer (`Adapted into:`).

**Relation hierarchy is flat, not a taxonomy tree.** `operationalized-from` is a narrower authoring-time *alternative* to `adapted-from` for exactly one pairing (methodology → procedure) — never record both edges for the same relationship, and don't nest further sub-relations under either without a new live case forcing it (same minimality bar that keeps `generated-from` deferred).

**The persisted edge is the source-side footer, not a target-side link.** Per the existing convention (unchanged): "the produced artifact does not link back" — there is no target-side `adapted-from` inline link recorded by default. The hyphenated relation names (`adapted-from`, `operationalized-from`, `derived-from`, `abstracted-from`) are used in two places only: (a) as the authorized-label token inside a `COLLECTION.md`'s outbound-linking declaration, and (b) in prose discussion of the vocabulary. The graph edge a reader actually encounters is always the footer heading (`Adapted into:`, `Operationalized into:`, etc.) at the source.

**Authorization sits with the source collection, not the shared catalogue.** Because the footer is written at the source and points forward to the target, it is an outbound link from the source's perspective — per [ADR 019](../../reference/adr/019-collection-owned-link-vocabulary.md) and [collections-and-types.md](../../reference/collections-and-types.md), the *source* collection's `COLLECTION.md` is the sole authoritative contract; `link-vocabulary.md` is a palette that "note writers and the connect skill do not read." No artifact may emit a new lineage footer for a pairing its own collection's `COLLECTION.md` hasn't explicitly authorized with a reader-need context phrase. This must land in `COLLECTION.md` **before** `cp-skill-write` or any corpus-correction pass emits a new `Adapted into:` / `Operationalized into:` footer — a sequencing constraint on execution-plan §3, not just a documentation task.

## `derived-from` — tested per pairing, not banned by register

`derived-from`'s authorization is decided per source→destination pairing against its entailment test (*"could another agent reconstruct the target's substantive claims from the source plus stated premises?"*), declared in the source collection's `COLLECTION.md` — not a blanket register ban. No collection is categorically excluded; a descriptive or generated-projection pairing remains eligible wherever a genuine case is a mechanically reconstructible copy.

**What the corpus evidence actually shows:** the methodology → procedure pairing isn't banned from `derived-from` in principle, but every audited real case fails the entailment test on its own admitted evidence — `skills-derive-from-methodology.md` states "a different person reading the same methodology would produce a meaningfully different skill" two paragraphs after claiming no added claims (Finding 3). So `kb/notes/ → kb/instructions/` is authorized in `COLLECTION.md` for `operationalized-from` as its default label; `derived-from` stays theoretically available for that pairing only as an exception requiring explicit justification (a specific procedure that genuinely adds zero ordering/defaults judgment), not the assumed case.

Repository/source material → descriptive review, session state/trace → handoff, and attributed sources → dialectical map resolve to `adapted-from` for the same evidence-based reason — not a rule that those destinations can never hold a recomputable copy.

## Deferred

- **`generated-from`** (canonical artifacts → mechanically-reproducible projection) — no confirmed live case of a *persisted* artifact needing this edge. Ephemeral regenerated projections (e.g. connect's on-demand titles listing) don't need a lineage edge at all — they retain nothing, so nothing can go stale. Revisit if a stored, non-regenerated projection turns up.
- **Workshop investigation → ADR** — not a lineage edge in this vocabulary. An ADR's relationship to its grounding notes is already covered by `rationale`/`grounds`/`evidence` citations; it isn't "worked up from" the notes the way an adapted or operationalized artifact is.

## Evaluation-boundary table, resolved

| source → target | relation |
|---|---|
| theory → methodology | `derived-from` / `abstracted-from`, existing case-by-case test, unchanged (stays within `kb/notes/`) |
| methodology → skill, checklist, or gate | `operationalized-from` |
| repository or source material → descriptive review | `adapted-from` |
| attributed sources → dialectical map | `adapted-from` |
| session state or trace → summary or handoff | `adapted-from` |
| canonical artifacts → index or runtime projection | deferred (no edge for ephemeral/regenerated cases; `generated-from` candidate if a persisted case appears) |
| workshop investigation → ADR | not a lineage edge; use `rationale`/`grounds`/`evidence` |

These rows are corpus-evidence defaults for `COLLECTION.md` to authorize, not register-level bans — see the `derived-from` section above.

## Corpus consequences (feeds execution-plan §4)

Evidence recording for the four still-unaudited commits (`b35ea92c`, `c7cc78f4`, `4c0c3cf8`, `b0b775c7`) uses the multi-axis method now, not a DER/AMP binary: for each changed passage, record source/target artifact contracts, the operation performed (selection, compression, synthesis, operationalization, generation), and the epistemic relation (reconstructible / generalized / authored / mixed) — assign a candidate label against this spec only after those axes are recorded. This is a correction to execution-plan §2's original instructions, not a re-audit of the five already-completed commits (those findings stand as evidence of mismatches under the pre-existing binary vocabulary).

**Single coherent pass, not independent edits:**
- `kb/notes/skills-derive-from-methodology.md` and `kb/instructions/write-instruction.md:42` describe the same pairing rule and must stay mutually consistent — reclassify both together, from `derived-from` to `operationalized-from`. Neither note's content needs rewriting, only the lineage label and footer heading.

**Semantic judgment required, not mechanical find-replace:**
- `kb/work/lineage-mechanisms/`'s "ad-hoc distillation" passages explicitly package judgment about which term fits — resolve each passage to `adapted-from` or `operationalized-from` (methodology → procedure cases) individually, not by a blanket substitution.

**Corpus-wide sweep** (broadened from the two originally flagged sites): any existing `Derived into:` footer in `kb/notes/` whose target is a `kb/instructions/` procedure, skill, gate, or checklist is a candidate for the same conversion — grep for the pattern and check each target's collection, don't assume only the two named cases exist.

**From the migration audit's Finding 1 and Finding 2** (previously identified, not yet scheduled):
- The four files using "condense"/"condensing" as an unacknowledged peer operator (`raw-accumulation-does-not-create-usable-memory.md:20`, `readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md:35`, `treat-continual-learning-as-substrate-coevolution.md:55`, `deploy-time-learning-is-the-missing-middle.md:34`) — replace with the settled `adapt`/`adaptation` prose term.
- The 70+ generated "Extraction" backlink footers coined in `f7aac9e6` — this is systemic, not 70 manual edits: locate the generator (likely a connect-skill or note-generation script) and fix at the source. If the generator is out of this workshop's scope, defer explicitly with a filed proposal reference rather than leaving it silently unscheduled.
- The re-derivation/re-abstraction inconsistency for trace re-extraction language (`preserve-evidence-without-loading-history.md:305,311,320`, `serve-multiple-consumers.md:333` vs. `commonplace-agent-memory-gap-plan.md:1822`) and the "Distill updates"/"Condense updates" vs. "abstract" inconsistency (`elicitation-requires-maintained-question-generation-systems.md:1016` vs. `open-domain-memory-retention-needs-a-declared-output-spec.md:1261`) — reconcile both against this spec.

**Two additional flagged sites, not previously scheduled:**
- `kb/notes/definitions/constraining.md:45` — "carried by the `derived-from` / `abstracted-from` labels" is now an incomplete list; update it, and reconsider the "Relationship to use-shaping" table's "Use-shaped (worked out from a source)" column, since that description is now closer to `adapted-from`'s truth condition than to `derived-from`'s.
- `kb/notes/definitions/context-engineering.md:27` — "producing derived views, summaries, and handoff artifacts" should read "producing adapted or derived views, summaries, and handoff artifacts" — most of what follows (summaries, handoff artifacts) resolves to `adapted-from` per the evaluation-boundary table, not `derived-from`.
- `kb/instructions/cp-skill-write/SKILL.md`'s "Lineage tracking" bullet (~line 94) states the binary `Derived into:` / `Abstracted into:` test directly in the skill body — needs expansion to the four-way test, kept as terse as the existing bullet.

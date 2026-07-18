# Migration audit findings

Corpus evidence for the workshop's [migration audit](./README.md#migration-audit), gathered by two independent sub-agent passes over the distillation-retirement commit range. Anchors are commit + path; classify, don't mechanically revert.

## Finding 1 — "condense/condensing" reintroduced as an unacknowledged 4th operator

Commit `593c60af` mechanically swapped `distill(ation)` → `condense/condensing` in several places where the surrounding sentence lists it as a **peer operator** to Constrain/Discover/Prune — i.e., exactly the general "conversion" slot the old term held, now under a new label with no citation, no definition, and no review tracking:

- `kb/notes/raw-accumulation-does-not-create-usable-memory.md:20` — "**Constraining** ... **Condensing** reshapes diffuse material ... **Discovery** ... **Pruning** ..."
- `kb/notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md:35` — "the operators (codify, relax, constrain, condense)"
- `kb/notes/treat-continual-learning-as-substrate-coevolution.md:55` — same operator-list pattern
- `kb/notes/deploy-time-learning-is-the-missing-middle.md:34` — "Two operators drive the updates: constraining ... and condensing"

This is the exact recurrence ADR 053's Consequences section warned about ("the control trap can recur under any future attractive label") — it happened inside the same migration, unreviewed, because "condense" reads as ordinary English and slipped past the write-time uniqueness check.

Related: the audit report attributed to commit `f7aac9e6` a separate **"Extraction"** successor term (own comparison-table row) for the SEL-dominant sense of old distillation, plus a corpus-wide backlink propagation. The §4 investigation below could not reproduce a corresponding 70+ generated footer surface. The confirmed part is the same underlying gap — a real operation lost its name and informal replacements filled the slot — and neither "extraction" nor "condense" is in ADR 053, the migration plan's four-part decision, or AGENTS.md's vocabulary list.

## Finding 2 — the same operation classified inconsistently across files

Two cases where structurally identical content got opposite DER/AMP treatment because no single classification pass reconciled cross-file references:

1. **Trace re-extraction language.** `kb/notes/agent-memory-requirements/preserve-evidence-without-loading-history.md:305,311,320` and `serve-multiple-consumers.md:333`: "redistillation" of raw session traces into reusable artifacts → **"re-derivation"** (asserts strong entailment-preservation). But `kb/reference/commonplace-agent-memory-gap-plan.md:1822`, same concept → **"re-abstraction"** (correctly ampliative).
2. **Probe-generation from logged failures.** `kb/notes/elicitation-requires-maintained-question-generation-systems.md:1016`, checklist step "Distill updates" → **"Condense updates"** — but the step is instance→rule generalization (AMP), not compression. The cross-reference to the identical lifecycle step in `kb/notes/open-domain-memory-retention-needs-a-declared-output-spec.md:1261` → "...log-misses/**abstract**/prune..." (correct AMP treatment).

### Finding 2 disposition

The long-form anchors cited above were already shortened or moved by the subsequent migration, so the live corpus did not contain the literal `redistillation` passages at those line numbers. The remaining live uses in `preserve-evidence-without-loading-history.md` and `serve-multiple-consumers.md` describe reconstructing summaries or other use-shaped trace products, not generalizing a verified instance into a rule; they now use **reconstruction**. The reference gap plan already reserves **re-abstraction** for trace-to-rule generalization, and the live probe checklist now says **Abstract updates**, matching the existing `abstract` wording in the parallel output-spec note.

## Finding 3 — the migration's flagship "derive" case may itself be judgment, not derivation

`kb/notes/skills-derive-from-methodology.md` (replacing `skills-derive-from-methodology-through-distillation.md`) is cited from ~15 other notes as the paradigm case of entailment-preserving reshaping. Its own body states the skill "adds no substantive claims the methodology does not already support" (the derivation bar) — then two paragraphs later: "A different person reading the same methodology would produce a meaningfully different skill... the process requires judgment." Output that varies meaningfully by author is the third, ungoverned case (selects sources, packages judgment) — see Finding 4 — not strict derivation. This note argues itself into the DER bucket while its own evidence sits closer to the third case.

## Finding 4 — the original "ad-hoc distillation" term survives untouched and untracked

`kb/work/lineage-mechanisms/` (README.md, current-practices-and-theory.md, model-provenance.md, storage-weight-across-cases.md, general-lineage-refresh-state-design.md) defined and used "ad-hoc distillation" as a stable term meaning "selects sources, packages judgment" — this was exactly the third operation this workshop needed to name. The six corpus sites are now classified as `adapted-from` artifacts or source shaping. It was never migrated, renamed, or flagged in ADR 053's Consequences/deferred list (which only names the agent-memory-systems type-spec, kb/sources, and the crystallized-reasoning coinage as deferred); the §4 pass closes that untracked deferral.

### Extraction-backlink investigation

The reported 70+ generated "Extraction" backlink footers could not be reproduced in the current corpus. A search for footer-shaped `Extraction:`, `Extracted from:`, and extraction-labelled backlink lines under `kb/` found no such authored footer surface. The only current `Extraction` occurrences are ordinary prose headings or descriptions in notes, source analyses, and agent-memory-system reviews; none is a registered lineage footer.

The cited commit `f7aac9e6` is also not evidence of a hidden generator: its stat is 40 changed files, and its additions are rename/backlink maintenance around the `constraining-and-extraction-both-trade-generality-for-reliability.md` note, not a generated `Extraction` footer batch. No emitter for that footer pattern exists in `scripts/`, `src/`, or `kb/instructions/`. The current `cp-skill-connect` contract explicitly writes only a gitignored connect report and does not author links or footers. There is therefore no generator fix to make in this workshop's scope; retain the claim as an unreproduced historical report rather than adding a speculative cleanup or a new vocabulary surface.

## Lower-confidence, worth a second look

- `kb/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md:204` — "**Derivation** and implementation often connect the profiles" — capitalized, unlinked, uncited on first use; reads like a proper-noun successor term rather than ordinary English.
- `kb/notes/definitions/context-engineering.md:757` — "Reshaping recorded knowledge ... producing derived views, summaries, and handoff artifacts — is the main operation" — dilutes "derived" to cover the whole context-engineering operational core, most of which is authored summarization judgment, not entailment-preservation.

## Confirmed clean (no mislabeling found)

- The 16 `derived-from` → `abstracted-from` lineage-edge flips in `4175dbb3` — each genuinely marks a claim generalizing beyond a single cited source, matching the commit's stated reasoning.
- `757d6daa`'s retirement of `distillation-is-transformation-not-selection.md` — its load-bearing claim (trace→rule adds a condition clause and rationale, i.e. ampliative not derivation) was correctly preserved into `abstract-an-experience-only-when-you-can-state-the-boundary.md`.
- `9e252b41`'s derived-from/abstracted-from gloss fix in both COLLECTION.md files — correct, matches link-vocabulary semantics.

## What this evidences for the workshop's evaluation boundary

Findings 1–4 together are direct evidence for the `methodology → skill/checklist/gate` and `session state/trace → summary/handoff` rows of the [evaluation boundary table](./README.md#evaluation-boundary): both rows predicted judgment/selection pressure that "derive" doesn't cover, and the corpus shows writers reaching for ad hoc, uncoordinated fixes ("condense," "extraction," "re-abstraction," lingering "ad-hoc distillation") instead of a named third relation.

## Multi-axis audit of the four remaining commits

This pass records evidence before assigning any candidate relation label. The source and target columns name the artifact contracts involved; the operation column describes what the changed passage does; the epistemic-relation column records whether the target content is reconstructible, generalized, authored, or mixed. A pointer-maintenance change is recorded as maintenance, not as a new source-to-target lineage edge.

### `b35ea92c` — scope the derived-copy framing to lineage regimes

| Changed passage | Source contract | Target contract | Operation | Epistemic relation |
|---|---|---|---|---|
| `kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:20` | Theoretical notes on derived copies, abstracted rules, lineage, and staleness | Theoretical note stating the managed-staleness rule | Generalizes the subject from every distilled artifact to any dependent artifact, then decomposes the repair into derived-copy rechecking versus abstracted-rule support re-examination | Mixed: the derived-copy branch is reconstructible from the stated mechanical check; the universal staleness claim and the abstracted branch are a synthesis and boundary judgment |
| Same note, `Relevant Notes` link at the end | Retitled source note | Existing theoretical note's navigation | Renames a local pointer after the source note's title migration | No epistemic transformation; referential maintenance |

The commit therefore changes the theory's scope and maintenance semantics, not merely its vocabulary. It is evidence for a source-to-theory synthesis that combines a reconstructible subcase with an authored generalization; it does not itself establish a new footer relation.

### `b0b775c7` — correct the worksheet's treatment of derived copies

| Changed passage | Source contract | Target contract | Operation | Epistemic relation |
|---|---|---|---|---|
| `kb/work/theory-methodology-derivation/wave-1-worksheet.md:12` | The corrected derived-copy note and the migration review that exposed the error | Workshop worksheet / execution plan | Reclassifies the planned fix: keeps lineage and staleness detection universal, while making copy identity and re-derive-and-compare regime-specific | Mixed, with an authored planning judgment over already-reviewed evidence |

This is a workshop decision record, not a durable theory artifact and not a lineage edge. The worksheet preserves the distinction between evidence inherited from the note and the operator's decision about how the next edit should be performed.

### `4c0c3cf8` — separate abstraction, context-shaping, and operational procedure work

| Changed passage | Source contract | Target contract | Operation | Epistemic relation |
|---|---|---|---|---|
| `kb/instructions/write-instruction.md` description, opening, and prerequisites | Repeated manual task instances plus any companion methodology notes | Prescriptive instruction for writing a procedure | Splits instruction creation into abstracting a stable core from repetitions and working the procedure body out from methodology; makes recurrence evidence and boundaries explicit | Mixed: the stable core is generalized from repeated cases; the procedure's ordering, defaults, and boundary choices remain authored, while the methodology-backed body is intended to be recoverable with the task |
| `kb/instructions/write-instruction.md:42` | Companion methodology note | Prescriptive instruction's maintenance/linking step | Turns the provenance story into an explicit forward link requirement | Mixed: the need for a link is authored operational policy, while the intended procedure content remains tied to its methodology |
| `kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md:28,40,54` | AgeMem's external behavior plus the KB's learning-theory vocabulary | Theoretical/descriptive note about memory-management mechanisms | Replaces an overloaded operator with context-shaping language and synthesizes the STM/LTM contrast for the KB's two-layer execution model | Mixed: the external system description is source-answerable; the cross-register comparison and context-shaping interpretation are authored synthesis |
| `kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md:88` | Existing two-layer execution note | Theoretical/descriptive note's related-notes navigation | Adds a grounding pointer for the newly stated session-scale analogy | No epistemic transformation; authored navigation |
| `kb/work/theory-methodology-derivation/obvious-distillation-cases.md` third and fourth batch tables | Wave-1 audit, changed notes, and the migration execution contract | Workshop ledger / queue | Records proposed rewordings and footer checks for later execution | Authored classification of mixed evidence; the table is a plan, not a claim-preserving or operational target artifact |

The commit contains two distinct provenance stories in `write-instruction.md`, which should remain distinct in the later mapping pass: repeated practice supplies a generalization, while methodology supplies material for an operational procedure. The commit itself does not prove that either story is a mechanically reconstructible copy.

### `c7cc78f4` — reframe the insight note as the conjecture phase

| Changed passage | Source contract | Target contract | Operation | Epistemic relation |
|---|---|---|---|---|
| Rename and body of `kb/notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md` | The prior theoretical note plus `definitions/discovery-lifecycle.md` and the existing three-depth argument | Theoretical note describing the conjecture phase | Retitles and narrows the concept, grades co-arising by abstraction depth, connects the examples to lifecycle phases, and adds lifecycle/constraining cross-references | Mixed: the old three-depth material is retained and reorganized; the lifecycle boundary, depth qualification, and Darwin/Fleming phase assignments are authored synthesis |
| `conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md:64-66` | Theoretical note's mechanism of naming a structure | `kb/instructions/cp-skill-connect/SKILL.md`'s Phase 5 logging procedure | States that the insight is operationalized as abstraction-opportunity logging in a prescriptive skill | Mixed: the note supplies the mechanism and rationale, while the phase, logging format, and execution behavior are operational additions; the existing `Derived into:` footer is evidence to classify later, not a decision made here |
| `kb/notes/definitions/discovery-lifecycle.md`, `kb/notes/discovery-README.md`, and `kb/index.md` | The renamed theoretical note and the learning/discovery vocabulary | Theoretical definition plus curated indexes | Updates lifecycle routing and navigation, while retaining some broader "discovery as operation" wording for the later vocabulary wave | Mixed for the routing sentence; authored/navigation maintenance for the index changes |
| Inbound references in the changed `kb/notes/` files | The renamed theoretical note | Existing theoretical notes with `grounds`, `extends`, `contrasts`, `parallels`, or `mechanism` prose | Rewrites the target path and displayed title; no cited claim is re-derived | No epistemic transformation; existing relation prose is preserved and only its referent is maintained |
| Inbound references in the ten changed `kb/sources/*.ingest.md` reports | Captured external source plus the ingest report's analysis | Theoretical note used as a connection or recommended landing surface | Repairs local analysis pointers after the note rename | No new lineage: source reports remain descriptive evidence, and their existing evidence/grounding language is unchanged |
| `kb/work/philosophy-borrowing/peirce-abduction.md` and `post-sweep-queue.md` | Workshop reasoning and migration execution history | Workshop planning/recordkeeping artifacts | Updates a workshop pointer and records the completed rename, validation, and deferred Wave 3 work | Authored workshop bookkeeping; not a durable source-to-target transformation |
| `properdocs.yml` redirect | Old note path | New note path in the documentation site | Adds a deterministic compatibility redirect for the rename | Reconstructible mechanical mapping, with no epistemic relation |

The broad `c7cc78f4` diff is therefore mostly referential maintenance around one substantive theoretical reframe. Its many changed files must not be counted as many independent lineage cases. The one formal footer case points from a theoretical note into a prescriptive skill and carries operationalization language; its eventual label is deliberately deferred to the locked-spec mapping pass.

### Audit result before final mapping

The four commits now have multi-axis evidence recorded. The audit supports three distinctions that the later mapping must preserve:

1. A theoretical note can combine reconstructible content with an authored scope generalization (`b35ea92c`).
2. Repeated practice and methodology are different inputs to a procedure, even when one instruction describes both (`4c0c3cf8`).
3. A large rename commit can contain one substantive adaptation/operationalization case surrounded by pointer maintenance (`c7cc78f4`).

No `adapted-from`, `operationalized-from`, `derived-from`, or `abstracted-from` candidate labels are assigned in this section.

## Coverage note

Two sub-agent passes covered: `f7aac9e6`, `4175dbb3`, `757d6daa`, `9e252b41` (read in full) and `593c60af` (the large Wave 2/3 commit). The primary multi-axis pass above now covers the remaining `b35ea92c`, `c7cc78f4`, `4c0c3cf8`, and `b0b775c7` commits. Candidate relation mapping remains gated on the locked vocabulary spec and is intentionally not part of this evidence record.

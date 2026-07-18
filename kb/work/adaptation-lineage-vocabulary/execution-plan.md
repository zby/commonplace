# Execution plan
Revised after Codex review of the first version, then folded so each run of consecutive `[Delegatable]` items is one task description dispatchable with a single command, not one command per bullet. Folding stops at any non-delegatable gate — items on either side of a gate never merge, since the gate is there because ordering matters. Sections capped at roughly three tasks running concurrently alongside the primary agent, not unlimited. Tasks flagged **semantic, not mechanical** need an agent capable of a real judgment call, not find-replace, and should not be folded with purely mechanical tasks even when adjacent.
## 1. Multi-axis evidence audit and core vocabulary design (parallel)
**[Delegatable — one command]** Evidence recording for the four still-unaudited commits (`b35ea92c`, `c7cc78f4`, `4c0c3cf8`, `b0b775c7`): for each changed passage, record source/target artifact contracts, the operation performed (selection, compression, synthesis, operationalization, generation, etc.), and the epistemic relation (reconstructible / generalized / authored / mixed). Do not assign a DER/AMP or any other candidate label at this stage — that mapping happens in §2, after the spec is locked. Append to `migration-audit-findings.md` in this structure; the five already-completed commits' findings stand as-is (valid evidence against the old binary vocabulary, not something to redo).

**Not delegatable — done.** Core design decisions are locked in [vocabulary-spec.md](./vocabulary-spec.md): `adapted-from`'s truth condition and maintenance consequence, `operationalized-from` minted as a flat authoring-time alternative for methodology→procedure (not a taxonomy child; `generated-from` still deferred), `derived-from` tested per source→destination pairing rather than banned by register, and the recording-direction resolution: the persisted edge is always the source-side footer, and the _source_ collection's `COLLECTION.md` is the sole authorizing contract, not the shared catalogue.
## 2. Lock the spec
Checkpoint, not new work: `vocabulary-spec.md` is final as of this revision, including recording direction and the flat relation hierarchy. Once §1's multi-axis evidence for the four remaining commits is in hand, map each recorded case to a candidate label against the locked spec — this mapping is the "final reclassification" that cannot run before the spec exists.
## 3. Update the shared catalogue, `COLLECTION.md` contracts, `AGENTS.md`, template disposition, and `cp-skill-write`
**Not delegatable, do first — this is the gate.** Identify and update every source `COLLECTION.md` whose collection will emit `adapted-from` / `operationalized-from` footers — at minimum `kb/notes/COLLECTION.md`, which needs new authorized-label entries for its `kb/instructions/` destination (`Operationalized into:`, methodology→procedure default) and for whichever destinations host descriptive-review, handoff, and dialectical-map targets (`Adapted into:`). Declare each with a reader-need context phrase, per the existing per-destination convention. No task in §4 may write a new footer before its pairing is authorized here.

**[Delegatable — one command, once the gate above lands]** All three of the following are independent of each other and only gated on `COLLECTION.md` authorization, so dispatch together:

- Update `kb/reference/link-vocabulary.md`: two catalogue rows, a new subsection alongside "Lineage semantics" giving both relations' truth conditions and maintenance consequences, `Adapted into:` / `Operationalized into:` footer conventions, and an update to the Migration status paragraph noting `derived-from`'s pairing-tested (not register-banned) scope.
  
- Update `kb/instructions/cp-skill-write/SKILL.md`'s "Lineage tracking" bullet (~line 94) from the binary `Derived into:` / `Abstracted into:` test to the four-way test, kept as terse as the existing bullet.
  
- Add the semi-technical-prose-vs-registered-identifier convention to `AGENTS.md` (currently absent), and resolve `AGENTS.md.template`'s disposition — the one item carried over from the workshop's original decisions list.
  
## 4. Correct all classified corpus sites
Gated on §3 landing (each fix applies now-authorized vocabulary, not vocabulary nobody may write yet). Four dispatchable units, not one per site — but keep the semantic/mechanical split, since it's information the delegate command needs, not just plan bookkeeping.

**[Delegatable — one command]** Single coherent pass: `kb/notes/skills-derive-from-methodology.md` + `kb/instructions/write-instruction.md:42` describe the same pairing rule and must stay mutually consistent — reclassify both together from `derived-from` to `operationalized-from`. Neither note's content needs rewriting, only the label and footer heading.

**[Delegatable — one command, semantic, not mechanical]** Fold together since both need the same kind of real judgment, not find-replace:

- `kb/work/lineage-mechanisms/` (README.md, automatic-derivation-rules.md, general-lineage-refresh-state-design.md, storage-weight-across-cases.md, current-practices-and-theory.md, model-provenance.md) — each "ad-hoc distillation" passage packages a real judgment call about which term fits; resolve individually to `adapted-from` or `operationalized-from`.
  
- Finding 2's reconciliations: "re-derivation" vs. "re-abstraction" for trace re-extraction language (`preserve-evidence-without-loading-history.md`, `serve-multiple-consumers.md` vs. `commonplace-agent-memory-gap-plan.md`), and "Distill/Condense updates" vs. "abstract" for the probe-generation checklist step (`elicitation-requires-maintained-question-generation-systems.md` vs. `open-domain-memory-retention-needs-a-declared-output-spec.md`).
  

**[Delegatable — one command, mechanical-ish, known-shape]** Fold together — lower-judgment corrections, all well-specified by the spec or an existing diagnosis:

- Corpus-wide sweep: grep for `Derived into:` footers in `kb/notes/` targeting a `kb/instructions/` procedure, skill, gate, or checklist — convert each to `Operationalized into:`.
  
- `kb/notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md:66` — the stale "Phase 5 abstraction-opportunity logging" claim, already diagnosed in `kb/work/theory-methodology-derivation/obvious-distillation-cases.md:102`.
  
- Finding 1's four-file "condense"/"condensing" peer-operator replacement with `adapt`/`adaptation` (`raw-accumulation-does-not-create-usable-memory.md`, `readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md`, `treat-continual-learning-as-substrate-coevolution.md`, `deploy-time-learning-is-the-missing-middle.md`).
  
- `kb/notes/definitions/constraining.md:45` — expand the incomplete `derived-from`/`abstracted-from` label list, and reconsider the "Relationship to use-shaping" table's column description against `adapted-from`'s truth condition.
  
- `kb/notes/definitions/context-engineering.md:27` — "producing derived views" → "producing adapted or derived views."
  

**[Delegatable — one command, investigate and report, not execute]** The 70+ generated "Extraction" backlink footers coined in `f7aac9e6` are not 70 manual edits — dispatch a task to locate the generator and report back whether a source-level fix is feasible in scope; the fix-vs-defer call comes back to the primary agent, this task doesn't decide it.
## 5. Promote the new ADR after implementation
Not delegatable, and not before §3–4 land — an ADR describes an implemented decision, not one still under consideration in the workshop layer. Once the catalogue, `COLLECTION.md` authorizations, and corpus corrections are in, draft a new ADR (not an in-place edit to ADR 053) amending its "no successor term" bullet: names `adapted-from` and `operationalized-from` as the successor relations, describes what was actually built, and leaves ADR 053's other three bullets untouched.

Decided: no dedicated write-time gate against future vocabulary drift (considered and rejected — see below). The ADR's Consequences section should name this risk explicitly, the same way ADR 053 named it and was right that it would recur: the hyphenated-identifier discipline is already trivially greppable and isn't what failed in Finding 1; the actual failure was ordinary-English peer-operator words with no formal term, which can't be caught prospectively by any fixed word list. Enforcement stays with the existing periodic audit, which is what caught it this time.
## 6. Validation, semantic review, lexical checks, pytest
**[Delegatable — one command, mechanical]** Fold together — all three are verification, not judgment: run `commonplace-validate` across all touched files; run a final lexical audit (grep for leftover "ad-hoc distillation," ungoverned "condense"/"Extraction" peer-operator usage, and any remaining `Derived into:` footer pointing at a `kb/instructions/` procedure, to confirm the corpus-wide sweep is actually complete); run the full `pytest` suite. Report all three results back.

**[Delegatable — one command, semantic, kept separate]** Targeted semantic review on the judgment-heavy corrections from §4 (the merged skills-derive-from-methodology.md/write-instruction.md pass, `lineage-mechanisms/`, the Finding 2 reconciliations) — a review pass, not a fix pass, so it stays separate from the mechanical verification above even though both are "delegatable, one command."
## 7. Close and delete the workshop
Not delegatable — closeout judgment calls.

- Confirm no other `COLLECTION.md` beyond `kb/notes/` needs authorization updates, per the evaluation-boundary table's resolved rows.
  
- Decide the transferable-theory-note question per the workshop's own non-goal (skip unless the orthogonality claim earns its own note).
  
- Check all six "What closes the workshop" criteria in `README.md`.
  
- Remove the workshop directory and its already-deferred active-workshop index entry.

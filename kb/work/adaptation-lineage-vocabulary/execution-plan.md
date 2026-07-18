# Execution plan
Revised after Codex review of the first version, then folded so each run of consecutive `[Delegatable]` items is one task description dispatchable with a single command, not one command per bullet. Folding stops at any non-delegatable gate — items on either side of a gate never merge, since the gate is there because ordering matters. Sections capped at roughly three tasks running concurrently alongside the primary agent, not unlimited. Tasks flagged **semantic, not mechanical** need an agent capable of a real judgment call, not find-replace, and should not be folded with purely mechanical tasks even when adjacent.
## 1. Multi-axis evidence audit and core vocabulary design (parallel) — done
All nine commits now have evidence recorded in `migration-audit-findings.md`: five from the original passes, four from the multi-axis pass covering `b35ea92c`, `c7cc78f4`, `4c0c3cf8`, `b0b775c7`. Mapping that evidence against the locked spec is recorded in `vocabulary-spec.md`'s Corpus consequences section.

**Not delegatable — done.** Core design decisions are locked in [vocabulary-spec.md](./vocabulary-spec.md): `adapted-from`'s truth condition and maintenance consequence, `operationalized-from` minted as a flat authoring-time alternative for methodology→procedure (not a taxonomy child; `generated-from` still deferred), `derived-from` tested per source→destination pairing rather than banned by register, and the recording-direction resolution: the persisted edge is always the source-side footer, and the _source_ collection's `COLLECTION.md` is the sole authorizing contract, not the shared catalogue.
## 2. Lock the spec — done
Checkpoint, not new work: `vocabulary-spec.md` is final, including recording direction, the flat relation hierarchy, and the mapping of all nine audited commits' evidence to candidate labels (or "no action," where the case is out of this workshop's scope).
## 3. Update the shared catalogue, `COLLECTION.md` contracts, `AGENTS.md`, template disposition, and `cp-skill-write`
**Not delegatable, do first — this is the gate. Done for the one live pairing.** `kb/notes/COLLECTION.md` now authorizes `operationalized-from` (destination: `instructions`, reader-need context phrase included) and its prose exception for the otherwise-rare `kb/notes/` → `kb/instructions/` outbound direction. `adapted-from` was deliberately **not** added anywhere yet: on inspection, `kb/notes/` isn't actually the source collection for the evaluation-boundary table's other rows (repository/source material → descriptive review and session state/trace → handoff both source from `kb/sources/` or `kb/work/`, not `kb/notes/`; dialectical map has no collection to authorize). Authorize `adapted-from` in whichever collection turns out to be the real source once a live corpus case in §4 needs it — don't authorize speculatively. No task in §4 may write a new footer before its pairing is authorized here.

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
  
- `kb/notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md:66` — a double issue, confirmed by the `c7cc78f4` audit: the "Phase 5 abstraction-opportunity logging" claim is both factually stale (cp-skill-connect has no Phase 5 anymore, per `kb/work/theory-methodology-derivation/obvious-distillation-cases.md:102`) and carries operationalization language with an existing `Derived into:` footer that needs reclassifying to `Operationalized into:` if any claim survives the staleness fix.
  
- Finding 1's four-file "condense"/"condensing" peer-operator replacement with `adapt`/`adaptation` (`raw-accumulation-does-not-create-usable-memory.md`, `readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md`, `treat-continual-learning-as-substrate-coevolution.md`, `deploy-time-learning-is-the-missing-middle.md`).
  
- `kb/notes/definitions/constraining.md:45` — expand the incomplete `derived-from`/`abstracted-from` label list, and reconsider the "Relationship to use-shaping" table's column description against `adapted-from`'s truth condition.
  
- `kb/notes/definitions/context-engineering.md:27` — "producing derived views" → "producing adapted or derived views."
  

**[Delegatable — one command, investigate and report, not execute]** The 70+ generated "Extraction" backlink footers coined in `f7aac9e6` are not 70 manual edits — dispatch a task to locate the generator and report back whether a source-level fix is feasible in scope; the fix-vs-defer call comes back to the primary agent, this task doesn't decide it.
## 5. Promote the new ADR after implementation
Drafted in parallel with §4 as [adr-draft.md](./adr-draft.md), since everything the ADR needs to describe — the vocabulary, its authorization, the skill/AGENTS.md changes — is already implemented in §1–3; §4 is corpus cleanup applying that vocabulary, not changing it (same shape as ADR 053 itself shipping with "remaining churn, tracked not blocking"). Not delegatable. Promotion to `kb/reference/adr/054-...md` still waits for §4 and §6 to close — the draft's own header says not to file it before then. Promotion is then a `git mv` plus dating the Status/Date fields, not a rewrite: amends ADR 053's "no successor term" bullet, describes what was actually built, leaves ADR 053's other three bullets untouched.

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

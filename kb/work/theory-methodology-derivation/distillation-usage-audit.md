# Distillation usage audit

Evidence for the [vocabulary thread](./derivation-selection-vocabulary.md)'s decision: can "distillation" be decomposed into consumer-directed **selection** + **derivation** (entailment-preserving transformation), with the ampliative residue routed to **discovery**?

## Method

Sweep run 2026-07-17 on this branch. Corpus: every `distill*` occurrence in `kb/notes/`, `kb/reference/`, `kb/instructions/`, `kb/agentic-systems/`, `kb/work/` (excluding this workshop), `kb/agent-memory-systems/`, and `AGENTS.md`. Excluded: `kb/sources/` (external captured text) and `kb/reports/` (generated). Five parallel classification agents; per-instance granularity everywhere except `kb/agent-memory-systems/` (per-file, 1–3 sense lines each, ~130 files). Occurrences referring to the same operation were grouped into one instance; counts are therefore judgment-dependent and approximate.

Categories: **META** (the term/concept itself — definitions, tag names, link labels, field names, external command names; migration = renaming only), **SEL** (predominantly selection), **DER** (predominantly derivation — output entailed by / recomputable from source given the consumer's goal), **AMP** (ampliative — output asserts claims not entailed: instances→rule, traces→lesson, posited patterns), **MIX** (both, non-trivially).

## Tallies

| Corpus | META | SEL | DER | AMP | MIX | UNCLEAR | instances |
|---|---|---|---|---|---|---|---|
| kb/notes A–L | 45 | 4 | 22 | 14 | 6 | 1 | 92 |
| kb/notes M–Z | 21 | 6 | 15 | 7 | 1 | 0 | 50 |
| kb/reference + kb/instructions + kb/agentic-systems + AGENTS.md | 13 | 2 | 11 | 3 | 0 | 0 | 29 |
| kb/work | 29 | 7 | 16 | 2 | 5 | 2 | 61 |
| kb/agent-memory-systems | 104 | 4 | 39 | 62 | 17 | 2 | 232 |
| **Total** | **212** | **23** | **103** | **88** | **29** | **5** | **464** |

Reading the substantive (non-META) 248 instances:

- **Library usage (notes/reference/instructions) is derivation-dominant**: DER 48, AMP 24, SEL 12, MIX 7. The economy proposal's direction holds there — most working uses of the word denote entailment-shaped reshaping (methodology→skill, source→summary, trace→consumer-shaped return, catalogue→instruction).
- **External-system description is ampliative-dominant**: in `kb/agent-memory-systems`, when the word describes what a system actually does, AMP leads 62 to 39 (56 AMP-dominant files vs 39 DER-dominant). The trace-learning loop the collection reviews — trajectories → rules, lessons, skills, playbooks, weights — is generalization, and the collection's own qualifying test ("does it distill traces into lessons/rules?") is phrased in the ampliative sense.
- **Pure selection is rare and almost never alone** (23 instances, mostly one workshop's "ad-hoc distillation" term). "Selection is simple" holds; selection alone rarely earned the word.

## Key findings

1. **The definition's own canonical instance list already spans DER and AMP.** `kb/notes/definitions/distillation.md` lists methodology→skill and article→summary (DER) alongside "repeated review failures → gate instruction" and "notice patterns, then write an artifact" (AMP). The decomposition splits the definition itself, not just downstream usage.

2. **The ampliative usages are the KB's most theoretically load-bearing.** The trace→rule ladder — `trace-extracted-memory-earns-authority-per-operation-not-at-capture.md` ("**Distill** — generalize the verified fact into a rule", citing the distillation definition as `defined-in`), `an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md`, `an-accepted-edit-verifies-the-change-not-the-rule.md`, `abstract-an-experience-only-when-you-can-state-the-boundary.md` — is an oracle theory *about* licensing instance→rule generalization, all under the word "distill". These are exactly the cases the proposal routes to discovery.

3. **`distillation-is-transformation-not-selection.md` is the pivotal note and it conflates two things.** Its title-as-claim rejects the selection framing; its evidence (trace → universally-quantified preference rule, "a condition clause and a rationale the trace never contained") is entirely ampliative. Under the decomposition its argument splits: anti-*mere*-selection (correct, and the reason the proposal needs derivation, not just selection) and shape-change-that-adds-claims (discovery, not derivation). Its "substrate must persist / losing a distillate means redistilling" section already runs on cache/re-derivation semantics.

4. **Two direct term collisions.** `memory-management-policy-is-learnable-but-oracle-dependent.md:54` already uses "selection and distillation" as a *contrasting pair* (LTM=selection, STM=distillation). And the lineage-mechanisms workshop's stable term "ad-hoc distillation" self-defines as "selects sources, **packages judgment**" — selection plus *authored* additions, which are neither entailed nor generalized from the source. The two-primitive decomposition has no slot for authored commitment; nearest existing homes are accumulation (new authored claims) or constraining (commitment), and the gap should be named in the definition work.

5. **Derivation must be defined as graded.** Even clear DER cases are re-verified by judgment, not mechanical recomputation: `distilled-artifacts-need-source-tracking.md` treats staleness review as judgment, and `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` explicitly separates mechanically-recomputable copies from judgment-checked ones. The entailment ideal (and its matching/cache payoffs) degrades with source coherence — consistent with the [vocabulary thread](./derivation-selection-vocabulary.md)'s caveat.

6. **Prescriptive-side tension already visible.** `kb/instructions/write-instruction.md` defines instruction-writing as distillation of "repeated manual operations → stable procedure" (AMP: "you can't distill what you haven't done") while its own step 6 frames the instruction as distilled *from methodology notes* (DER). The two provenance stories coexist under one word. Similarly, `kb/work/review-revise-gated/run-08/gate-noise-audit.md` records reviewers disputing whether execution-boundary compression counts as distillation at all — live boundary friction with the current term.

7. **Two-stage pipelines are the common hybrid.** Many described systems (and some KB procedures) run a DER stage (deterministic stats, compaction, summaries) feeding an AMP stage (rules, insights, harness edits): `agentic-harness-engineering`, `g-memory`, `clawvault`, `MemoryOS`, `signetai`; also `skill-creator-distillation`'s "re-distillation from a mixed evidence base". One word currently spans both stages; the decomposition names them differently — arguably the point.

8. **A formal result survives untouched.** `kb/work/agent-complexity-theory/no-universal-distillation-preserves-all-task-relevant-structure.md` models distillation as a bounded summary map — pure DER; renaming is mechanical there.

## Migration mechanics inventory

Renaming is not find-and-replace:

- **Five library filenames** contain `distill*` (`distillation-README`, `distillation-is-transformation-not-selection`, `distillation-status-determines-directory-placement`, `distilled-artifacts-need-source-tracking`, `evolving-understanding-needs-re-distillation-not-composition`), some cited by path in ADRs 021 and a proposal.
- **Tag infrastructure**: `distillation` is in learning-theory's `covered_by` (validator-enforced), with a tag-README carrying `complete: true`.
- **Shipped link grammar**: the `Distilled into:` footer (defined in `kb/reference/link-vocabulary.md`, prescribed in `cp-skill-write`) — audited instances span SEL (definition split-outs), DER (principle→checklist), and AMP (cross-system syntheses), so each footer needs classification, not substitution. DER cases could become `Derived into:`.
- **Review type-spec boilerplate**: `kb/agent-memory-systems/types/agent-memory-system-review.md` hard-codes the mandatory `**Distilled form:**` field and the "raw → distilled loop" contract — the source of ~100 META instances (one per review). A rename here is one type-spec edit plus a bulk sweep, but note the field's *content* is usually ampliative, so its new name should come from the discovery side.
- **Canonical gloss**: "directed context compression" is hardcoded in ADR 011 and the `undefined-terms` review gate example.
- **Unrenameable**: external systems' own command names (`memex distill`, `/learning-redistill`, `finetune --distill`, "SFT distillation") stay; the ML-knowledge-distillation sense remains in sources.

## What the evidence says about the decision

- The **decomposition is real**: the word demonstrably covers three operations with different verification semantics (selection / derivation / ampliative generalization), the definition itself leaks across the boundary, and the friction is already surfacing in reviews and internal tensions. Explication is warranted.
- The **economy replacement is supported for the library, with a routing job attached**: DER dominates library usage, so "replace most usage with derivation" is accurate there — but ~a quarter of substantive library usage and the *majority* sense in agent-memory-systems is ampliative and must be routed to discovery (or a named sub-operation of it, e.g. the existing abstraction/rule-extraction ladder), which is a semantic migration, not a rename.
- **Discovery's definition needs a check**: it's currently "positing a general concept and *recognizing particulars as instances*"; trace→rule promotion is positing the general from a particular. Compatible, but the definition should confirm it owns this case before AMP traffic is routed to it.
- **Whether "distillation" survives as the composite's name** is now a smaller question: if it survives, its definition must explicitly *exclude* ampliative steps (fixing finding 1); if retired, the inventory above is the work list. The agent-memory-systems type-spec can migrate on its own schedule either way — it is a self-contained surface.

## Status

Sweep complete. Next: reconcile with `discovery`'s definition, decide the composite-name question, then draft the `derivation` (and `selection`) definition notes against this evidence.

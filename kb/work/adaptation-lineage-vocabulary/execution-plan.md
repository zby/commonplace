# Execution plan

Two independent-judgment threads, then three delegatable execution passes gated on them, then closeout. Sections marked **[Delegatable]** are big, simple, low-judgment chunks suited to a lightweight/fast agent; the unmarked sections need continuity of reasoning and stay with the primary agent or operator.

## 1. Core design decisions (not delegatable)

Resolve the workshop's "Decisions to finish" list into a single locked spec:

- `adapted-from` truth conditions — what makes a source a *material input* vs background influence.
- Whether `operationalized-from` / `generated-from` are named subrelations, alternatives, or not yet warranted (the audit's methodology→skill and canonical→projection cases are the test data).
- The maintenance consequence of `adapted-from`, kept weaker than `derived-from`'s recomputation regime.
- Where `derived-from` is *not* authorized (descriptive/prescriptive/dialectical collections whose correctness condition isn't claim-closure) — this directly decides whether `skills-derive-from-methodology.md` and `write-instruction.md:42` get reclassified as `adapted-from`/`operationalized-from` or stay `derived-from` with a narrower argument.
- Source-side inverse: does `Derived into:` get a new `Adapted into:` sibling, and do these become registered identifiers or stay reader-facing phrases.

Output: a short written spec (in the workshop README or a new `vocabulary-spec.md`) that sections 3 and 4 below execute against without further judgment calls. Any genuinely open call goes to the user rather than being decided silently.

## 2. Finish the migration audit — **[Delegatable]**

Independent of §1 — can run in parallel. Apply the same method the first two passes used (read `git show` in full, grep touched files for distill/derive/abstract/condense, classify DER vs AMP by the two-layer theory's test) to the four remaining commits: `b35ea92c`, `c7cc78f4`, `4c0c3cf8`, `b0b775c7`. Append findings to `migration-audit-findings.md` in the existing format.

`b35ea92c` and `b0b775c7` are small single-file wording fixes and likely clean; `c7cc78f4`'s `Distilled into:`→`Derived into:` reclassification and `4c0c3cf8`'s `write-instruction.md` edit are the ones worth real scrutiny.

## 3. Formalize the vocabulary (gated on §1's locked spec)

- **[Delegatable]** Add `adapted-from` to `kb/reference/link-vocabulary.md`: a catalogue row, a new subsection alongside "Lineage semantics (derived vs abstracted)" giving its truth conditions, an `Adapted into:` footer convention matching the existing pattern, and an update to the Migration status paragraph. Purely mechanical once §1's spec exists.
- **[Delegatable]** Add the semi-technical-prose-vs-registered-identifier convention to `AGENTS.md` (currently absent entirely — confirmed no adaptation/lineage convention exists there yet).
- **Not delegatable:** draft the ADR amending ADR 053 — add one decision bullet naming `adapted-from` as the successor relation for the composite selection-plus-reshaping operation the "no successor term" line left unfilled, leaving the other three ADR 053 bullets (ordinary-English "derive", discovery-lifecycle routing for ampliative traffic, `distillation` surviving only in non-KB senses) untouched. Small, but it's a decision record — keep it with the operator/primary agent, drafted straight from §1's spec.

## 4. Fix the confirmed flagged sites — **[Delegatable, one agent per site]**

Gated on §3 (each fix applies the now-settled vocabulary, not invents it):

- `kb/notes/skills-derive-from-methodology.md` — reconcile the self-contradiction (line 30 claims no new claims added; line 36 says a different person would produce a different skill) by applying §1's derived-from/adapted-from boundary decision.
- `kb/instructions/write-instruction.md:42` — same reclassification applied to the methodology→procedure `derived-from` claim.
- `kb/notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md:66` — fix the stale "Phase 5 abstraction-opportunity logging" claim; already diagnosed (not fixed) in `kb/work/theory-methodology-derivation/obvious-distillation-cases.md:102`, so this is a known-shape correction.
- `kb/work/lineage-mechanisms/` (README.md, automatic-derivation-rules.md, general-lineage-refresh-state-design.md, storage-weight-across-cases.md, current-practices-and-theory.md, model-provenance.md) — replace the untouched "ad-hoc distillation" term with the settled vocabulary.

These four are independent of each other — good candidates to run as four parallel lightweight-agent tasks once §3 lands.

## 5. Closeout (primary agent)

- Determine which collections' `COLLECTION.md` outbound-link rules need updating to authorize `adapted-from` (theory, dialectical-map, and generated-projection collections are the live cases from the evaluation-boundary table) and update them.
- Run `commonplace-validate` across touched files.
- Decide the transferable-theory-note question per the workshop's own non-goal (skip unless the orthogonality claim earns its own note beyond the vocabulary decision).
- Check all six "What closes the workshop" criteria, then remove the workshop directory and its (already-deferred) active-workshop index entry per the Bookkeeping note.

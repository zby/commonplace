# Reflective-systems coherence repairs

## Goal

Resolve the four live defects remaining after triage of the [2026-07-14 reflective-systems coherence report](../../reports/reflective-systems-coherence-report.md), without replaying recommendations already absorbed by later revisions.

## Evidence boundary

The report is evidence about repository snapshot `32ce89e6`, not current truth. Each repair must be checked against the live library before editing. The triage against `c41c7155` found four remaining defects; everything else in the report is either already resolved or deferred under YAGNI.

## Repair queue

1. **Complete — external-model boundary.** Keep provider and weights outside the declared Commonplace frame. Treat editable model-binding requests as internal localized configuration that may select an external dependency when realized, not as reflective coverage of the dependency's distributed-parametric form; assess requested-to-realized binding separately.
2. **Complete — closure semantics.** Naming a decider closes routing only. Decision-content closure requires explicitly retained criteria, supplied directly or imported by reference; tacit criteria held by the decider do not count.
3. **Complete — natural-language/symbolic crossing.** Recast the claim around changes that move the interpretation–enforcement boundary; do not generalize from those crossings to every reliability improvement.
4. **Pending — retrieval locality.** State failure at the unit it breaks: the represented aspect, constraint, or reflective path whose retrieval wire missed it, not the whole system's reflectivity.

## Item 1 decision and acceptance boundary

The operative distinction is:

- **Reflective coverage** applies only to represented aspects of the same bounded system. Its operation profile records what internal processes can do to those covered aspects or components.
- **Dependency control** records the cross-boundary effect an internal binding requests. Editing the binding changes localized Commonplace configuration; if the request is realized, it selects an external model without covering that model or its weights. Request addressability and operative realization are separate findings.

Item 1 is complete when:

- the coverage theory states the boundary condition and no longer uses Commonplace's external provider model as an example of a covered component;
- the declared frame and Commonplace case classify the binding as internal and modifiable, and the provider/weights as external and uncovered;
- every live consumer of `selection-grade` or `selection-only` parametric coverage either adopts dependency-control wording or is shown to describe a genuinely in-boundary component;
- affected artifacts pass deterministic validation, and a final search finds no live statement granting reflective coverage to Commonplace's external weights.

## Item 1 completion evidence

Completed 2026-08-10. The repair changed these library artifacts:

- `kb/notes/reflective-coverage-is-graded-across-representational-forms.md`
- `kb/reference/commonplace-declared-frame.md`
- `kb/reference/commonplace-as-a-reflective-system.md`
- `kb/notes/methodological-and-computational-closure-track-different-changes.md`
- `kb/notes/only-explicit-retention-is-durable-writable-and-addressable.md`
- `kb/notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md`
- `kb/notes/improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md`
- `kb/notes/evidence/six-commonplace-paths-establish-broad-addressability-not-completeness.md`
- `kb/articles/what-makes-human-inclusive-self-revision-non-trivial.md`
- `kb/work/self-improvement-cluster-operationalization/README.md`

The coverage theory now confines reflective operations to represented in-boundary aspects. The Commonplace frame and case identify the writable object as a localized binding request, leave provider weights outside the system, and treat any realized model selection as dependency control. They also state that request addressability does not establish realization or a reflective causal path. A focused semantic re-review found no remaining blocker.

Each changed artifact, this workshop README, and `kb/work/README.md` passed an individual `commonplace-validate` run. A live-library search found no remaining claim that Commonplace has `selection-grade` or `selection-only` reflective coverage of external provider weights; matches in the snapshot report and frozen evidence packets remain historical evidence. `git diff --check` was clean, and `uv run pytest` passed all 479 tests.

## Item 2 decision and acceptance boundary

Methodological closure is assessed from retained methodology relative to a named pathway and its consequential decision set. The presence of capable actors, tools, or authority procedures can make the methodology actionable, but does not supply decision content that its retained materials leave open.

Naming a decider closes routing only. Decision-content closure requires the methodology to supply a criterion, explicitly import a retained criterion or decision procedure that constrains the result, or determine the result itself. An imported criterion need not be duplicated, but the pathway must operatively use it. Tacit criteria held by a decider remain actor capability rather than retained methodology. A choice may be declared outside the consequential decision set when its divergence is tolerable; that narrows the assessment instead of closing the choice.

Item 2 is complete when the canonical closure note and its live summaries use this distinction consistently, no dependent artifact relies on the tacit-criteria exception, and the affected artifacts pass deterministic validation.

## Item 2 completion evidence

Completed 2026-08-10. The repair changed:

- `kb/notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md`
- `kb/notes/self-improving-systems-README.md`

The canonical note now separates routing from decision-content closure, treats direct and explicitly imported criteria alike, bounds closure by how far those criteria constrain the answer, and excludes tacit actor criteria. The tag head no longer presents closure as an intrinsic property of methodology-as-input. A backlink audit found no other live dependent that needed editing, and a focused semantic re-review found no remaining blocker. Both changed artifacts passed individual `commonplace-validate` runs without warnings. A live-library search found none of the superseded exception phrases, and `git diff --check` was clean. The historical report and frozen replication packet remain unchanged.

## Item 3 decision and acceptance boundary

The interpretation–enforcement boundary records which form bears responsibility for a behavior: natural-language content leaves consequences to model or human interpretation, while a symbolic artifact has consequences assigned by a formal consumer. A change moves the boundary only when it transfers that responsibility. Codification is the observed natural-language-to-symbolic direction; retiring formal enforcement would be the reverse direction.

Two related changes must remain separate. Re-grounding a symbolic rule against revised retained natural-language criteria changes the mapping between forms without reallocating responsibility. Symbolic execution that exposes a faulty natural-language instruction is cross-form feedback; if the enforcement stays fixed, it changes neither the allocation nor the enforcement rule. Same-form bug fixes, retry corrections, atomicity repairs, resource bounds, and guidance revisions can materially improve reliability without any crossing.

Item 3 is complete when the canonical claim, title, description, evidence reading, and reflective-coverage consequence use this boundary; the Commonplace trace is no longer presented as evidence of a reverse boundary movement or re-grounded enforcement; live consumers stop equating crossings with reliability improvement generally; the obsolete claim no longer survives as the live note identifier; and the affected artifacts and redirect map pass deterministic validation.

## Item 3 completion evidence

Completed 2026-08-10. The repair changed:

- `kb/notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md` (relocated from `kb/notes/improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md`)
- `kb/notes/reflective-coverage-is-graded-across-representational-forms.md`
- `kb/sources/knowledge-centric-self-improvement-2607.19592.ingest.md`
- `kb/sources/jdegoes-recursive-agent-architecture-2081854216264392934.ingest.md`
- `properdocs.yml`

The canonical note now makes boundary movement, rather than improvement generally, the event that requires modification-grade coverage of both localized forms and their mapping. It treats re-grounding and symbolic-to-natural-language feedback as distinct mechanisms, states that the reference trace demonstrates only codification and feedback, and names same-form reliability improvements as counterexamples to the former generalization. The Knowledge-Centric Self-Improvement case is now a boundary-stable comparison rather than purported evidence that gains concentrate at crossings. The live theory backlink and both ingest link labels use the narrowed claim, and the relocation removes the superseded claim from the note's live identifier while preserving its published URL through the generated redirect.

A focused semantic pass against grounding alignment, internal consistency, explanatory-reach, load-bearing qualifiers, underspecification, and unearned generality found no remaining blocker after making the retained-natural-language condition on re-grounding explicit. All four changed library artifacts and this workshop README passed individual `commonplace-validate` runs without warnings. Redirect validation found all 103 targets resolvable, no key shadowing a live page, and a flat redirect topology. A live-library search found none of the superseded claim formulations. `git diff --check` was clean, and `uv run pytest` passed all 479 tests. The snapshot report and historical workshop evidence remain unchanged.

## Next-session routing

Resume at the first `Pending` queue item. Re-read the cited live artifacts before editing because this workshop records decisions and status, not frozen replacement text. Complete one item fully, update its status and evidence here, then stop unless the maintainer asks to continue.

## What closes the workshop

All four defects are repaired in the library, the queue records their validation evidence, and no unresolved finding remains. Then delete this workshop and remove its entry from `kb/work/README.md`; the durable value belongs in the repaired library artifacts.

## Bookkeeping

Keep repair decisions and validation evidence here. Do not copy full library drafts into the workshop, and do not edit the snapshot report to make it describe later repository states.

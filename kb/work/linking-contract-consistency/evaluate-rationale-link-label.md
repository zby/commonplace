---
description: "Use when deciding whether rationale needs a distinct source-as-subject successor, should merge with grounds, or should cease to be a formal link relation"
type: kb/types/instruction.md
---

# Evaluate the rationale link label

## Outcome

Produce `kb/work/linking-contract-consistency/rationale-label-direction-review.md` with an evidence-backed decision among these live hypotheses:

1. **Distinct successor:** the cross-register reader journey is real and `rests-on` is an honest source-as-subject replacement for `rationale`.
2. **Merge:** `rationale` and `grounds` encode the same reader need once the source artifact is known, so they need one jointly reviewed successor rather than separate migrations.
3. **Retire:** the useful information belongs in connective prose and context phrases; no formal successor earns its authoring cost.
4. **Split or reclassify:** the corpus contains more than one relation and no single replacement covers it.

Do not edit the catalogue, collection contracts, ADRs, instructions outside this workshop, or corpus edges. Evaluation may create the review and update the pending rationale retrospective with surprises. The parent agent or maintainer owns the migration decision.

## Governing semantics

Read before classifying:

- [ADR 058](../../reference/adr/058-directional-identifiers-use-source-as-subject.md) for the source-as-subject invariant;
- [ADR 020](../../reference/adr/020-theoretical-default-contrasts-mechanism.md), especially its stated `grounds` / `rationale` boundary;
- [link vocabulary](../../reference/link-vocabulary.md) and every live collection authorization containing either label;
- the [evidence migration retrospective](./evidence-label-migration-retrospective.md) and [rationale migration plan](./rationale-label-migration-plan.md).

Treat current declarations as hypotheses to test against authored edges, not as the answer. The current intended distinction is:

- `rationale`: a design, description, procedure, or rule points to the theoretical claim explaining why it exists;
- `grounds`: a theoretical assertion points to a premise a reader follows to evaluate it.

Both current identifiers fail the source-as-subject grammar as presently defined: the target supplies the rationale or grounds for the source.

## Build the evaluation corpus

Recompute live counts. Do not reuse the preliminary counts in conversation or the historical authorization matrix.

Create a temporary TSV with one row per registered edge and these fields: label, source path, source collection, target as authored, resolved target, destination class, link title, context phrase, exclusion bucket, and semantic disposition. Define the positive mutable surface and mutually exclusive exclusions before classification. Preserve generated reports, immutable snapshots, frozen experiments/calibration artifacts, archived proposals, historical quotations, and inactive workshop history as evidence rather than migration candidates.

Review:

- every active `rationale` footer edge;
- every active file that authors both `rationale` and `grounds`;
- every active `grounds` edge outside the intended note→note theoretical cohort;
- a varied sample of note→note `grounds` edges covering definitions, mechanisms, empirical support, dependencies, and argumentative premises;
- current recommendation, example, and procedure prose that teaches either identifier.

Resolve local targets before assigning source→destination classes. Record authorization gaps separately from semantic ambiguity.

## Classify by assertion, not spelling

For each `rationale` edge, choose exactly one provisional disposition:

- **R — rationale dependency:** `source rests-on target` honestly states that the source's design, rule, interpretation, or existence depends on the target claim.
- **G — premise dependency:** the source is itself an assertion whose truth is argued from the target premise; compare with the intended `grounds` cohort.
- **E — evidence:** the target is an observation, source, or case bearing empirically on the source; test `evidenced-by`.
- **L — lineage:** the target materially generated or was transformed into the source; test the registered lineage relations without changing them.
- **N — navigation or another relation:** the edge is comparison, definition, implementation, history, or weak adjacency rather than rationale.
- **X — remove:** the edge has no independent reader need beyond nearby prose.
- **A — ambiguous:** full local context still supports multiple dispositions.

Use these tests:

1. **Assertion test:** Can a reader truthfully say “source rests on target” without reversing endpoints or overstating dependence?
2. **Reader-need test:** What concrete question causes a reader to follow the edge—“why does this design/rule exist?” or “which premise should I verify?”
3. **Counterfactual test:** If the target changed or were rejected, would the source need design reconsideration, truth reassessment, evidential updating, or merely a citation edit?
4. **Substitution test:** Would the intended successor to `grounds` communicate the same useful action? Would `rests-on` conceal a distinction the reader needs before following?
5. **Context-removal test:** Is the distinction carried only by knowing the source collection, and is that information reliably available to the reader? Do not preserve two labels merely to restate recoverable source type.
6. **Authoring-cost test:** Does the formal label outperform a direct connective phrase such as “because,” “motivated by,” or “implements” often enough to justify remaining vocabulary?

Pay special attention to off-contract pairings and same-file use of both labels. They are high-information cases: they may expose a real distinction, uncontrolled synonymy, or classification drift.

## Compare candidate outcomes

Evaluate at least these candidates:

| candidate | question |
|---|---|
| `rests-on` for `rationale` only | Does it preserve the cross-register reader journey without claiming conclusive justification? |
| one successor for `rationale` + `grounds` | Does one dependency label preserve every reader action, with collection/context supplying the rest? |
| no successor | Would connective prose and more specific existing labels serve the reader better? |
| split/reclassification | Do recurring semantic cohorts require different existing or new identifiers? |

Do not select by name elegance or migration size. Prefer the smallest vocabulary that preserves distinct, repeatedly useful reader actions.

## Required review

The review must contain:

- inventory and exclusion counts by source→destination pair;
- a disposition table reconciling every active `rationale` edge;
- comparison samples from the `grounds` cohort, including every off-pattern pairing and every file using both labels;
- the strongest evidence for and against each candidate outcome;
- the recommended assertion template, reader need, direction kind, and neighboring-label boundaries—or a clear recommendation to retire;
- authorization and migration consequences without performing them;
- ambiguous cases quoted minimally with file/line pointers;
- confidence and the specific evidence that could reverse the decision.

Update [the rationale retrospective](./rationale-label-migration-retrospective.md) immediately when the evaluation finds a reusable surprise. Validate the review and retrospective, check `git diff`, and report changed paths.

## Execution provenance

This evaluation is model-agnostic. If a specific model or partition is requested, record the actual executing model from runtime evidence. Do not substitute another model while labeling the result as the requested one. If the requested model cannot be dispatched, return that limitation to the parent instead of fabricating model-specific provenance.

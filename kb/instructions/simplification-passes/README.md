# Simplification passes

Passes that simplify one article or note whose claims are settled but whose
text is not. The caller can fix the work in advance, or explicitly commission
an assessment to choose it. Ordinary passes run without a selection stop;
plain-wording and abstractions retain their selection-approval stops. Each pass is a short worker packet: it states
what the pass exists to make true, what it must preserve, and what it returns.
Workers follow [execute a revision pass](./execute-a-revision-pass.md).
The planning procedure is [revise an article or note](./revise-an-article-or-note.md);
the workflow publishes what needs no decision, ends at its first stop and
leaves a continuation record, which a session agent takes up with the
operator by [continue a revise pass](../continue-a-revise-pass.md). A per-item
pass's answers file is decided with [decide items](../decide-items.md);
[approve a text](../approve-a-text.md) says what to tell the operator after a
publication, and how to publish a held candidate.

For a generic editorial pass with no assessment, use
[revise-note](../revise-note.md) instead. To review the artifact before the
assessor plans, use the full procedure, `--full` (see
[ways to make a plan](#ways-to-make-a-plan)). The
[audit pass](./audit-a-prior-pass.md) here is for checking what an earlier
automated pass did.

## Passes

Every pass except split-out-a-treatment is an
[edit operation](../../types/edit-operation.md): it takes one text of the
note and returns an [edit result](../../types/edit-result.md). Each runs
alone with `commonplace-revise try OPERATION NOTE`, which writes nothing
to the checkout, and the revise workflow runs each pass through the same
route. Split-out-a-treatment writes a second file, so it stays a plain
instruction for a session.

Each pass declares `effort: simple` or `effort: judgment` in its frontmatter.
Simple passes run in a fresh worker on a cheaper model or lower effort;
judgment passes run on the stronger profile. Each edit operation declares
`decision`: `none` when it applies its changes, `per-item` when it first
returns proposals for the operator to decide in an
[answers](../../types/answers.md) file. The passes in the depth order
of the orchestrating procedure also declare `depth` (1 runs first); a pass
without `depth` may run at any point.

- [audit-a-prior-pass](./audit-a-prior-pass.md) (simple) — trace each passage an automated pass weakened to the finding that caused it, and restore what the finding did not justify.
- [narrow-overclaims](./narrow-overclaims.md) (judgment) — move claims from what cannot be observed to what can, and mark gaps instead of inventing precision.
- [opening-and-title](./opening-and-title.md) (judgment) — make the TL;DR read with only its own words and the title state the central contrast literally.
- [readability-and-flow](./readability-and-flow.md) (judgment) — structural moves, tightening, and sentences rewritten to parse on first reading, with no change of claim.
- [plain-wording](./plain-wording.md) (simple) — replace decorative figures with literal statements and unusual words with common ones, and cut exclusions that deny what the sentence already ruled out, after the operator approves the list.
- [abstractions](./abstractions.md) (judgment) — per term, either keep a coined or registered abstraction everywhere because one sentence needs its distinction, or replace it with the ordinary word everywhere.
- [split-out-a-treatment](./split-out-a-treatment.md) (simple) — keep the artifact's passage minimal and put the full argument in a separate file that later passes do not load.
- [place-external-systems](./place-external-systems.md) (simple) — position named systems against the artifact's criteria by reading generated main-review files, with source ingests identified separately.

## Ways to make a plan

`commonplace-revise` runs a plan: a list of passes in depth
order. The procedures differ only in how the plan is made.

- **Focused.** The operator names one pass or one review finding.
  `--pass NAME` runs a one-entry plan for that pass on the whole artifact.
  `--finding RESULT` runs a one-entry plan for
  [fix a finding by a named strategy](../fix-warnings/fix-strategy-taxonomy.md),
  with that review result of the artifact as its `finding` input. Nothing
  is assessed and nothing is reviewed. `--purpose` and `--must-keep` go into
  the plan; without `--purpose`, the plan states that the operator named
  no other purpose. `--plan FILE` supplies any other fixed plan.
- **Triage.** `commonplace-revise triage` asks the operator about the artifact's fresh stored
  `warn` and `fail` review results. It writes one answers file per result,
  whose items are the result's `warn` and `fail` findings, and ends. In a
  session, follow [decide items](../decide-items.md): the operator approves
  a finding that is right, rejects one that is wrong, with a reason, or
  defers it. On the operator's word, `commonplace-revise apply FILE FILE ...`, naming every decided
  file, starts a new run whose plan holds one entry for
  [fix a finding by a named strategy](../fix-warnings/fix-strategy-taxonomy.md)
  per result with an approved finding, in depth order. The fix receives the
  approved answers as `finding-answers` and fixes only the approved
  findings. Nothing is reviewed and nothing is assessed.
- **Quick.** `--quick` asks one assessor to choose the passes. It reads the
  artifact and the artifact's fresh stored `warn` and `fail` review
  results, when any exist. It launches no review.
- **Full.** `--full` first runs every review operation that declares a
  `depth` on the artifact: the catalog gates, the compression checks and
  their synthesis, critique, composition friction, premise
  decomposition and the [role report](../role-in-the-kb-gate.md). Fresh
  results are reused and new ones go to the shared store. The assessor
  then reads the `warn` and `fail` results, the depth 1 reports, the
  compression synthesis report and the role report. If a depth 1 report
  proposes changing what the artifact is, the plan stops and nothing is
  edited. The role report shows which dependents rely on the artifact's
  terms and claims; the stop names those a change would reach. Each pass
  receives the report's `## Role` section as its `kb-role` input and leaves
  the terms and claims it lists as relied on. The edited text is not
  reviewed again.

## Fixed-plan execution: the simple baseline

Use one pass to evaluate an editing operation independently of planning.
Supply a YAML plan whose purpose, scope and must-keep claims are settled.
`must-keep` lists only what this run keeps beyond the note's write brief;
every pass receives the brief and keeps its Must keep:

```yaml
purpose: "Make the experiment description easier for KB maintainers to follow."
must-keep:
  - "The proposed experiment is a prediction, not an established result."
passes:
  - pass: readability-and-flow
    scope: "The experiment-design section only; preserve its predictions and measures."
stop: null
```

Replace these example values with the actual commission, save the plan outside
the run's generated `artifact/` directory, and run:

```bash
commonplace-revise ARTIFACT --plan PLAN.yaml
```

For one pass with no scope, `--pass NAME` writes this plan for you.

This route makes no assessment call and does not choose or add passes. The
worker still exercises judgment within the assigned operation. The plan owns
`purpose` and `must-keep`; do not also supply their CLI options. Multiple fixed
passes are supported, but do not treat their composition as evidence that an
individual pass is reliable. A missing scope covers the whole artifact; use
an explicit scope for a bounded trial. An empty `must-keep` list does not license
changing claims.

The command writes the changed text to the artifact without a stop and
records the publication: the report's `publications` names the published
text and its diff under `artifact/publications/`. Nothing is committed;
`git diff` shows the change, and git reverses it. Tell the operator what was
published, with the path of the note and of the diff
([approve a text](../approve-a-text.md)). A text that adds a validation
warning the artifact does not have is held instead: the run keeps
`artifact/final.md` and `artifact/final.diff`, the original remains
unchanged, and the report's `held` names the command that publishes it.
On the operator's word, `commonplace-revise publish RUN` publishes that
exact candidate, and `commonplace-revise publish RUN --revised FILE` the operator's revision of
it, a full text outside `artifact/` ([approve a text](../approve-a-text.md)).
Candidate files are outputs, not editable inputs. Use `--plan` for a changed
commission. No-change runs write nothing. A wording-selection pass that
proposes anything ends the run after the earlier passes' work is published;
its proposals wait in `artifact/<pass>-answers.md`, and later passes wait in
the continuation record.

Every invocation is a new run: choose a mode each time. No run is repeated
or resumed; a later command names the answers file or the run it acts on.

For an independent report-only operation, use one artifact and one gate id:

```bash
commonplace-review ARTIFACT --criteria GATE-ID --grouping pair
```

Use a gate id, not a bundle name or the default criteria. A finding does not trigger
an edit or choose more review work. Fresh pairs are skipped; use `--force`
only when deliberately requesting a new judgment. Artifact validation belongs
in these note workflows; Python tests belong to development of the machinery.

## Planning-containing workflows

`commonplace-revise ARTIFACT --quick --purpose TEXT [--must-keep CLAIM ...]`
commissions assessment and pass selection, then runs the validated plan without
a routine plan-approval stop. The assessor also receives the artifact's fresh
`warn` and `fail` review results. The planning instruction's "Run it as a workflow"
section describes its additional behavior. `--full` adds a review step
before the same assessment. Evaluate the assessor's choices separately from
individual review and editing operations before relying on their composition.

The procedure in a conversation remains the right tool when passes are chosen
as the conversation goes or a pass needs the conversation as evidence.

---

Relevant Notes:

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) — rests-on: why every pass states what it must preserve: unguarded splitting lost relations
- [Three simplification passes exposed different clarity–precision tradeoffs](../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) — rests-on: why passes are separate instruments rather than stronger and weaker versions of one edit

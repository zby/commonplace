# Simplification passes

Passes that simplify one article or note whose claims are settled but whose
text is not. The caller can fix the work in advance, or explicitly commission
an assessment to choose it. Ordinary passes run without a selection stop;
plain-wording and abstractions retain their selection-approval stops. Each pass is a short worker packet: it states
what the pass exists to make true, what it must preserve, and what it returns.
Workers follow [execute a revision pass](./execute-a-revision-pass.md).
The planning procedure is [revise an article or note](./revise-an-article-or-note.md).

For a generic editorial pass with no assessment, use
[revise-note](../revise-note.md) instead. For a full automated review pass,
use [run-full-improvement-pass-on-note](../run-full-improvement-pass-on-note.md);
the [audit pass](./audit-a-prior-pass.md) here is for checking what such a
pass did.

## Passes

Each pass declares `effort: simple` or `effort: judgment` in its frontmatter.
Simple passes run in a fresh worker on a cheaper model or lower effort;
judgment passes stay on the session model. The six passes in the depth order
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

## Fixed-plan execution: the simple baseline

Use one pass to evaluate an editing operation independently of planning.
Supply a YAML plan whose purpose, scope and protected claims are settled:

```yaml
purpose: "Make the experiment description easier for KB maintainers to follow."
defend:
  - "The proposed experiment is a prediction, not an established result."
passes:
  - pass: readability-and-flow
    scope: "The experiment-design section only; preserve its predictions and measures."
stop: null
```

Replace these example values with the actual commission, save the plan outside
the run's generated `artifact/` directory, and run:

```bash
commonplace-review run revise ARTIFACT --plan PLAN.yaml
```

This route makes no assessment call and does not choose or add passes. The
worker still exercises judgment within the assigned operation. The plan owns
`purpose` and `defend`; do not also supply their CLI options. Multiple fixed
passes are supported, but do not treat their composition as evidence that an
individual pass is reliable. A missing scope covers the whole artifact; use
an explicit scope for a bounded trial. An empty `defend` list does not license
changing claims.

Inspect the returned report, `artifact/final.md` and `artifact/final.diff`.
The original remains unchanged until the operator approves the exact
`artifact/publication.json` with the report's `approve-command`. Repeat the
reported command to publish from captured inputs. Repeating alone never
approves. Candidate and manifest files are outputs, not editable inputs.
Use `--plan` for a changed commission. No-change runs need no publication
approval. Wording-selection passes stop earlier for their own approvals.

An unchanged repeat retains the mode and captured plan, even if the supplied
plan file is later removed. Changed artifact text starts a new run: choose
`--plan` or `--assess` again. Older runs without a recorded mode also require
that explicit choice; their retained files are not migrated or deleted.

For an independent report-only operation, use one artifact and one gate id:

```bash
commonplace-review run gates ARTIFACT --criteria GATE-ID --grouping pair
```

Use a gate id, not a bundle name or `--all-gates`. A finding does not trigger
an edit or choose more review work. Fresh pairs are skipped; use `--force`
only when deliberately requesting a new judgment. Artifact validation belongs
in these note workflows; Python tests belong to development of the machinery.

## Planning-containing workflows

`commonplace-review run revise ARTIFACT --assess --purpose TEXT [--defend CLAIM ...]`
commissions assessment and pass selection, then runs the validated plan without
a routine plan-approval stop. The planning instruction's "Run it as a workflow"
section describes its additional behavior. `run full-pass` also contains
planning and disposition choices. Evaluate those choices separately from
individual review and editing operations before relying on their composition.

The procedure in a conversation remains the right tool when passes are chosen
as the conversation goes or a pass needs the conversation as evidence.

---

Relevant Notes:

- [Two rewrites exposed a syntax-or-repetition tradeoff](../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) — rests-on: why every pass states what it must preserve: unguarded splitting lost relations
- [Three simplification passes exposed different clarity–precision tradeoffs](../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) — rests-on: why passes are separate instruments rather than stronger and weaker versions of one edit

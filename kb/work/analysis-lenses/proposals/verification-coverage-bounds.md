# Proposal: verification coverage bounds

Operator proposal, 2026-10-11, refined in discussion. Status: option for the
[first deliverable](../first-deliverable.md) to compare. Not adopted, not
authorized for implementation.

## Problem

`verify-reports.md` tells the single verification role to judge coverage
against the frozen repository tree for every record. On a large repository
that is a second exhaustive analysis, and the method states no stopping rule
for it. The duty also falls equally on the general layer and on lenses whose
questions touch a fraction of the tree.

## Proposal

Concentrate the exhaustive coverage duty at the general layer and make the
runtime record the coverage bound for everything downstream. Memory already
scopes itself from runtime routes, so this follows the existing grain.

1. **Runtime coverage is checked against the whole tree, at module and
   entry-point granularity.** Every top-level package, shipped entry path (CLI
   dispatch, hooks, registered tools, service and library operations) and
   packaging manifest in the frozen tree is either placed in Components or
   Routes, or declared immaterial with a reason. Depth checks follow the
   runtime record's anchors. This bounds the exhaustive duty by the tree's
   structure rather than its size.

2. **Lens omission checks are bounded to runtime-located paths plus the
   lens's own anchors.** Correctness checking follows a lens's anchors wherever
   they go. Omission checking, the expensive part, searches only the
   runtime-located paths relevant to the lens's question. A mechanism found
   outside both sets is routed as a runtime coverage finding, not a lens
   finding. Lens discovery stays unbounded; only the search for what a lens
   missed is bounded.

3. **The bound is stated as a limit.** The verification record says that
   omission judgment for memory and epistemic was bounded to runtime-located
   paths, so synthesis carries it and unknown does not read as absence.

"Runtime-located paths" is the union of source anchors in the runtime record's
shared records. No new contract surface is needed.

## Placement options

**Same verifier, two coverage rules.** Rewrite the tree-coverage sentence in
`verify-reports.md` into rules 1 and 2, add rule 3 to the verification
record's limits, and add one line to `trace-runtime.md` saying that its anchors
define the located paths later roles depend on, so material components it did
not trace must be declared. No new role, schema or engine change: rung one or
two on the ladder in [design direction](../design-direction.md). Risk: a
runtime coverage gap is found after lenses scoped from it. That risk exists
today unchanged, since nothing verifies runtime before memory reads it.

**Separate runtime verification before the lenses.** Lenses start from a
verified map and lens verification gets cheaper, at the cost of a new role and
one sequential stage. Rung three. A runtime correction would then need to
re-run lenses, which the current order-only input does not do.

Recommendation under examination: take the first, and let evidence decide the
second.

## Discriminating measurement

Across the retained runs, from the records and frozen worktrees:

- Share of memory and epistemic anchors outside runtime-located paths. If
  small, the bound is tight and lenses rarely need paths runtime missed.
- Runtime coverage findings raised by the verifier, by materiality. If rare,
  the single-verifier placement is enough; if common, early runtime
  verification earns its stage.

Both are deterministic over retained records and are within the workshop's
scope. Neither distinguishes good runtime coverage from lens anchoring on the
map; only a coverage audit of the source does.

## What would count against adoption

- A coverage audit finds material mechanisms outside runtime-located paths
  that lenses reached and the bounded verifier would not have checked.
- Module-granularity tree checks still exceed the verifier's budget on the
  largest retained repositories.
- The declared-immaterial list grows into the product inventory the runtime
  instruction forbids.

## Change footprint by layer

Checked on 2026-10-11 against the live plan, set type, analysis library and
engine. Four layers, from least to most disruptive: analysis instructions and
type prose; analysis plan and layout data; analysis-specific code and tests
under `src/commonplace/lib/agentic_analysis/` and
`tests/commonplace/agentic_analysis/`; the generic engine under
`src/commonplace/artifactrun/`. Nothing below was run; these are readings of
the code, to be confirmed by the analysis test suite when a change is
authorized.

### Placement one: same verifier, two coverage rules

Instructions and type prose only.

- `verify-reports.md`: replace the tree-coverage sentence with rules 1 and 2.
- `trace-runtime.md`: one line that its anchors define the located paths later
  roles depend on.
- The verification type already says completeness is "relative to the
  required analysis questions and declared evidence boundary, not exhaustive
  inspection of repository contents". The instruction currently reaches
  further than its type; placement one brings it back. The type's Limits
  section carries rule 3 unchanged, and the existing rule in `rules.py` that
  every declared limit is carried into the synthesis's Limitations propagates
  it for free. The schema checks section headings only, so no schema change.

### Lens reruns on runtime correction

Plan data only. Changing memory and epistemic from `runtime: order-only` to
`runtime: required` in `plan.yaml` makes an accepted runtime correction lapse
their judgments and re-run them. The engine already does this: a judgment holds
while every non-order-only input resolves to its pinned version
(`artifactrun/run.py`, `holds`). The compact-plan tests already exercise this
toggle. The cost is a design trade-off, two lens reruns per accepted runtime
correction, not machinery.

### Placement two: separate runtime verification before the lenses

Plan and layout data, plus small analysis-code and test changes. No engine
change.

Data:

- Set type layout: add a `runtime-verification` role of the verification type
  with `verifies: [runtime]`; narrow `report-verification.verifies` to memory,
  epistemic and reconciliation; add the role to the boundary's `complete` list.
- `plan.yaml`: a `runtime-check` artifact-check job over runtime (the generic
  handler), the role entry reading boundary, runtime and the check findings,
  `verified-by: [runtime-verification]` on memory and epistemic so they wait
  for an accepted verdict, and the role among the assemble inputs. The engine
  derives `apply-runtime-verification`, judgment gating and the `verifies`
  relation from the layout; `verified-by` and verifying roles are generic in
  `artifactrun/compact.py`.

Analysis code:

- `verification.py`: `report_check_gate` reads the handed check under the
  fixed name `report-check-handed`. A second verifier with its own check job
  needs the gate parametrized by the handed input's name, or a second
  function. `cited_records` iterates the layout and needs nothing.
- Possibly the overview template and `records.py` navigation line, if the
  overview is to link the new verification.
- `worker-profiles.yaml` needs no change; profiles are keyed by harness, not
  role.

Tests: `test_declaration.py` pins the verifier set and asserts the
`report-verification:verifies:<role>` relation for every report role;
`test_compact_plan.py` expects the hook set `{boundary, report-verification}`.
Both are analysis tests and would be updated with the plan.

### Generic engine

No change under any option. Verifying roles, `verifies` and `verified-by`
gating, order-only versus required inputs and the artifact-check handler are
already generic and in use.

### Measurements

The discriminating measurements are read-only tooling over retained records
and frozen worktrees. They belong in `scripts/` if kept, and touch no layer of
the method.

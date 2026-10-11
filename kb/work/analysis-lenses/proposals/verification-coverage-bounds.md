# Proposal: verification coverage bounds

Operator proposal, 2026-10-11, refined in discussion and tightened after a
reviewer's reading the same day. Status: one option for the
[first deliverable](../first-deliverable.md) to compare, alongside clarifying
the existing materiality rule and a question-driven omission budget. Not
adopted, not authorized for implementation.

## Problem

The method already limits coverage by materiality. The verification type
says completeness is relative to the required questions and the declared
boundary, not exhaustive inspection of repository contents, and
`verify-reports.md` invokes that threshold. What neither states is how the
verifier should select and stop an omission search: which parts of the frozen
tree to look in for mechanisms the records missed, and when looking further is
no longer warranted. The instruction's wording, "judge coverage against the
frozen repository tree", leans exhaustive without saying how far. The gap is a
missing operational stopping rule, not an exhaustive duty to remove, and it
falls equally on the general layer and on lenses whose questions touch a
fraction of the tree.

## Proposal

Concentrate the exhaustive coverage duty at the general layer and make the
runtime record the coverage bound for everything downstream. Memory already
scopes itself from runtime routes, so this follows the existing grain.

1. **Runtime coverage is checked against the whole tree, at module and
   entry-point granularity.** Every top-level package, shipped entry path (CLI
   dispatch, hooks, registered tools, service and library operations) and
   packaging manifest in the frozen tree is either placed in Components or
   Routes, or declared immaterial with a reason. Depth checks follow the
   runtime record's anchors. The structural inventory can be enumerated
   mechanically from package layout, manifests and registration points, but
   judging each item's materiality is worker effort, and the count of entry
   paths grows with the repository. This check therefore needs its own
   prioritization or stopping rule, or it moves the unbounded obligation
   rather than resolving it.

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
shared records. No new contract surface is needed, but file anchors are an
imprecise bound: one anchor in a large file admits a large search space, a
relevant helper in an unanchored file falls outside it, and an anchored file
does not show which mechanisms were investigated. The comparison should test
whether the existing anchors are a useful proxy against a question- or
mechanism-based stopping rule before making them authoritative.

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

- Share of memory and epistemic anchors outside runtime-located paths. A
  small share is consistent with a tight bound; it is also consistent with
  lenses anchoring on the map and sharing its omissions.
- Runtime coverage findings raised by the verifier, by materiality. A low
  count is consistent with an adequate map; it is also consistent with a
  verifier that rarely searches for omissions.

Both are deterministic over retained records and are within the workshop's
scope. Neither establishes sufficiency. Only a bounded coverage audit of the
frozen source, independent of the existing records, can challenge the shared
blind spots; it does not need to be exhaustive.

## What would count against adoption

- A coverage audit finds a material mechanism outside both runtime-located
  paths and the lens's own anchors, so bounded omission checking would not
  have looked there, and its omission makes a central conclusion misleading.
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

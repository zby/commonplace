# Faster collection validation

Make full collection validation materially faster while preserving its complete
observable results. This reduces the cost of a routine Commonplace operation.
The contribution is a bounded implementation patch plus a reproducible
correctness and timing comparison. Follow the [shared handoff](./README.md).

## Inputs and baseline

Read the [validation contract](../../reference/validation-contract.md),
[validation-run decision](../../reference/adr/050-validation-runs-share-parsed-artifacts-and-collection-indexes.md),
[validator implementation](../../../src/commonplace/lib/validation.py), and
[CLI](../../../src/commonplace/cli/validate_notes.py). Parsing and some collection
indexes are already shared within a run: establish the remaining bottleneck
with profiling rather than assuming that caching has not been implemented.

```bash
python -m pytest
commonplace-validate kb/notes --json
commonplace-validate kb/reference --json
commonplace-validate kb/instructions --json
```

Existing validation warnings or failures are baseline output to preserve, not
permission to omit checks. Record command exit codes as well as output.

## Search commission

Profile the pinned checkout, choose an observed bottleneck, and try alternative
implementations. Restrict production edits to validation and directly necessary
helpers; explain each changed helper's callers. Do not introduce a persistent
cache, schema change, broad graph-loader redesign, or reduced validation scope.

Build a reusable comparison runner that executes baseline and candidate against
the same immutable input tree, with separate installations and fresh processes.
First capture reference results before optimizing. Compare parsed JSON exactly,
including diagnostic order, reasons, severities, subjects, and analysed artifact
lists, and compare exit codes. Normalize only installation-dependent absolute
root prefixes if required; list that normalization explicitly. Do not discard
fields to obtain agreement.

Exercise the three real collections above and generated small/medium/large
collections with varied linking density, shared types, tag membership, and
deliberately invalid inputs. Include single-file validation and successive runs
after changing notes, linked files, type specs, and collection contracts. These
cases check that reused work has not hidden a dependency or stale result.
Freeze a portion of generated cases before optimizing and reserve it for the
final comparison. Make the generator accept a maintainer-chosen seed.

Time complete CLI runs separately from fixture construction and profiling.
Alternate baseline and candidate on the same machine, use at least five measured
runs per workload, and report every timing plus the median. Distinguish a fresh
process from a cold filesystem cache; do not claim the latter without measuring
it. Report peak memory and relevant environment details as well.

## Acceptance

The target is at least a 2x median speedup on the pinned `kb/notes` collection,
unchanged results on every comparison case, and no material slowdown elsewhere
(investigate median regressions over 10% that exceed timing noise). Report
absolute times so a negligible baseline cost cannot masquerade as a useful win.
The speed target is a commission goal, not a claim that this improvement exists.

Supply one command to rerun equivalence checks and a bounded timing comparison
on baseline and candidate. Include the full-suite result and a concise account
of the bottleneck and why the change removes work without removing checks.
Keep the patch focused enough to review separately from the benchmark runner.

If profiling shows that a material gain needs a redesign or semantic change,
stop and return the profile and measured attempts. A smaller demonstrated gain
may be submitted with its actual numbers, but is not automatically accepted.
Passing the finite comparison set establishes measured equivalence, not proof
for every possible KB; the maintainer still reviews the patch and can rerun
with a fresh seed.

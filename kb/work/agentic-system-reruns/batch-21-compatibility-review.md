# Batch 21 compatibility review: result and release work

**No reset regression was found in the reviewed two-file change. Batch 21 is
not released: its code guard correctly refuses the changed package, and the
current-reset-to-frozen-command bridge still needs disposable verification.**
This review does not authorize implementation, binding refresh, environment
preparation, same-run recovery or analytical dispatch. The existing helper,
active plan, nine feedback packets and old workspaces remain unchanged.

## Decision for the operator

A new analysis method is not needed for these nine targeted corrections. Keep
each run's original method, sources, accepted upstream records and remaining
attempt limits. The batch-22 coverage clarification does not automatically
upgrade those methods or resolve a contradiction encountered in their old
validators. Such a stop must remain a stop, not prompt a frozen-code patch.

The recommended next release work is:

1. Verify a disposable bridge from the selected origin reset implementation to
   the actual frozen judgment/scheduling implementations in separate interpreters.
   Cover both confirmed core-code families and the intended correction shapes.
2. Prepare a reset/refusal-only helper entry point and parent-held harness
   packets. Preserve all reset, closure, archive, feedback and completion checks.
   Dispatch analytical coordinators only through the exposed project tool.
3. If the bridge passes, explicitly approve the exact reviewed current package
   tree at `5af51ae1f09f9f903701d9ff11348c201182c950` for **external reset only**.
   Retain a package/dependency-wide equality guard against that approved tree;
   do not replace the pin with arbitrary HEAD or ignore validation files.
   Record the old baseline, exact reviewed diff, tests and release decision.
4. Commit that reviewed release, then obtain execution and same-run writer
   clearance before any withdrawal or operator refusal. Recheck all live
   bindings, source/publication state, budget and runtime capability at admission.

Step 3 is a conditional recommendation, **not a binding change made by this
review**. The independent code reviewer instead prefers an unchanged `f12f9a746`
reset runtime in a separate immutable code environment. That alternative would
avoid approving new imports, but needs environment preparation and helper
rebinding while preserving the true publication origin. The parent recommends
first testing the exact current tree: the reset implementation is byte-identical,
static paths and the scoped probe show no changed comparison call, and this
avoids an additional code environment. If bridge evidence contradicts that
argument, stop and reconsider the original-runtime alternative rather than
weakening a guard or forcing success. Both independent reports are retained.

## What was reviewed

Origin HEAD: `67482d6cf903522dd6313f51c56eeeba26c3fd1d`.
Original reset baseline: `f12f9a7467f4b01a5777bf8f65f109560b05e848`.
The source/dependency diff contains only `systems_matrix.py` and
`agentic_analysis/rules.py`; `pyproject.toml` and `uv.lock` are unchanged.

- [Independent code-path review](./batch-21-current-code-review.md): imports,
  conditional handler resolution, effect withdrawal, rematerialization, library
  versus Python-package binding, later frozen validation and inherited corpus.
- [Independent test/release review](./batch-21-current-release-review.md): actual
  test assertions and gaps, frozen bindings, both budget families and the
  proposed harness-native release ordering.
- Parent read both reports completely, reviewed the full helper and reset/
  publication/materialization paths, checked bound-file hashes and performed
  the scoped disposable probe below.

All **138 checked file bindings** matched: the five runtime files, base inventory,
prior integration proof, launcher and each case's preparation, run definition,
evidence, native files and feedback payloads. The independent review also
confirmed all nine recorded worktree HEADs and native command bindings. These
checks do not prove that no prior writer can resume, that every possible file is
covered, or that the complete live preflight will pass.

A parent hash grouping of six frozen core modules (`artifactrun/run.py`,
`engine.py`, `store.py`, `checks.py`, `plan.py` and `cli/run.py`) found exactly
two source families:

- Supermemory, ContextPilot, OpenRSI, ModularRSI, JAZ, Autogenesis and AREX-Skill.
- MehmetGoekce LLM Wiki and ClawVault.

This supports two bridge representatives for those modules. It is not proof
that every other handler, type or dependency is identical. Check the rest of
the exercised closure while constructing the bridge. The old family retains
original author counters; only the two batch-20 cases consume the reset floor.
Do not manufacture new headroom.

## Why the current code block is not an observed reset failure

The broad guard requires equality with `f12f9a746` before the helper's case
preflight. Committed changes still violate that equality. Its refusal is
therefore expected and remains correct until a new release deliberately
approves another exact implementation. Matching five runtime hashes alone is
not enough to bypass a transitive package guard.

Both changed modules are imported through the helper's publication/validation
imports and dynamic handler loading. However, the standard external reset calls
reset hooks, not ordinary candidate checks, assembly or publication handlers.
The publication reset hook checks opening identity, journals and byte maps,
returns replacements, and does not validate profile coverage. Rematerialization
copies preserved member bytes and a working manifest without invoking the
changed comparison rules.

Later `judge`, advancement, checks and publication use each frozen prepared
package. Cwd, an old library directory or in-memory criterion bytes do not
switch an already loaded Python implementation. Runtime code bindings must be
checked before reset, and frozen prefixes must remain in use afterward.

Full inherited-corpus validation still matters during later publication.
Both batch-20 worktrees inherit the two historical profiles affected by the
current coverage-reader exception. Their original validators accept the old
convention. Backporting only the strict half of the new rule could break that
corpus; no such backport or historical relabeling is proposed.

## Tests actually run

The independent release reviewer ran existing disposable tests offline with
`uv run --no-sync`:

- Feedback reentry, reset, reset-publication and publication files:
  **54 passed in 17.98 seconds**, including all 16 feedback cases.
- Selected synthetic historical-coverage and profile consumers:
  **18 passed, 23 deselected in 3.87 seconds**.

These are **72 selected passes**, not a new full-suite release claim. The
1,684-test batch-22 run is prior evidence, not a rerun in this review.

The parent additionally reran all eight existing publication-reset tests with
review-only instrumentation in `/tmp/batch21_reset_reachability_probe.py`.
While each external reset call was active, traps failed on calls to
`systems_matrix.validate_comparison`, the artifact rule's comparison adapter,
or publication's pinned-artifact validation adapter. Traps were inactive during
fixture construction and later republication, so they did not disable validation
elsewhere. No production or test file was edited.

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="/tmp:$PWD" uv run --no-sync pytest -p batch21_reset_reachability_probe tests/commonplace/agentic_analysis/test_reset_publication.py -m '' --tb=short
8 passed in 1.23 seconds
```

The probe recorded 12 reset invocations: four completed, two fixture-injected
interruptions and six expected guarded refusals. No trapped validation call
occurred. Raw results: `/tmp/batch21-reset-reachability-results.json`; log:
`/tmp/batch21-reset-reachability-tests.txt`. These eight tests overlap the
54-test selection; do not count them as eight additional distinct tests.
The fixtures script publication validation and do not exercise old packages,
so this probe strengthens reset reachability evidence without closing the
mixed-package bridge or proving substantive report validity.

## Work still required before release

The bridge should cover one/two upstream authors, the profile author and the
preserved synthesis author. All refusals must be installed before any advance;
assert no stale acceptance replay, no opening/acquisition rerun, preserved
upstream identities, fresh dependent verification, and matching archive/new
publication bytes. A retained-counter exhaustion must stop. Keep the rejected
verifier self-correction route rejected; AREX remains synthesis-only with its
accepted-record constraint.

The harness route must acquire exclusive one-shot ownership, record assignments
before effects, verify reset/archive/upstream preservation, install and verify
**all** exact-version refusals, then hand the existing run/prefix to a fresh
`commonplace-coordinator`. It must explicitly forbid prepare/start/acquire and
additional operator judgments. Test partial-feedback failure, ledger collision,
interrupted waits and coordinator/verification failure before using it on real
runs. A case cannot advance before complete feedback or overlap the next case.
There is no assistant Bash-agent-CLI fallback. Batch-22 fresh-start packets
cannot be reused: their no-feedback/new-workspace policy is a different commission.

Neither metadata nor process absence establishes writer exclusion for a reused
run. Current bindings, headroom, external fencing for old commands, pending-reset
absence and runtime/profile availability remain live launch gates. New completed
bytes still need independent exact-byte/operational audits and separate integration
authority; nothing here clears old incidents or unselected publications.

## Preservation and review records

No real reset, judge, advance, acquisition, worktree installation, analytical
coordinator launch, publication, integration, guard/seal refresh or commit was
performed. The future `outputs/batch-21-corrections/` one-shot directory remains
absent. Unrelated concurrent workshop/ingest changes were left untouched.

The project-worker launch diagnostic succeeded (`COMMONPLACE_WORKER_OK`); depth
and nesting limits were unknown. Review assignments were disjoint:

- `c9dbb4c0-3809-4473-ad45-7452c289fe1a`: code-path report, completed and read.
- `447b2942-cfc1-4a87-9397-743db354ba0e`: test/release report, completed and read.

These are coding/review workers, not batch-21 correction coordinators. This
report and the two independent reports retain the review; they are not native
analytical workflow inputs or launch authority.

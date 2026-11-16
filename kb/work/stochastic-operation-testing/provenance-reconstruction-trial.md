# Trial: reconstruct a review fixture from a commit and retained note

Authorized by the operator on 2026-11-14: “run the trial”, following the proposal to use current tools rather than implement shared machinery.

## Question and acceptance

Can a KB commit plus retained uncommitted target text construct independent, useful review fixtures using existing tools? Success means both fixtures restore the captured note at its original path, use the same committed context and criterion, start without operational state, and produce new independently retained calls whose captured inputs match the intended fixture. A failure to construct or execute the fixture is recorded, not repaired by silently changing the experiment.

This is an integration and reconstruction exercise, not a test of verdict correctness or an estimate of stability. Two results cannot establish a failure rate.

## Fixed scope

- Target: `kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md`, captured from the dirty live checkout before fixture preparation.
- Operation: `prose/proportion-mismatch`, one gate that needs no ignored source snapshot or previous report as an explicit input.
- Baseline: the main checkout's HEAD at capture; record its full commit in the retained manifest. Overlay only the target, not other dirty files.
- Two detached worktrees outside the main checkout, with empty operational state. Use explicit `--profile opus`, pair grouping, one worker, `--force`, no resume, and a 180-second launch timeout.
- Two sequential command invocations. Each has the existing command's maximum of three launch attempts, so at most six paid launches. Expected cost is below a few dollars, not a hard monetary cap. Stop after an infrastructure failure or unexpected fixture mutation; do not replace failed trials or expand the gate set.
- Use the current bare `commonplace-review` command from the editable installation. Record executable/code identity separately from the KB fixture; inspect source cleanliness and hashes before and after. This does not test historical executable installation.

## Retention and controls

Raw evidence belongs under `kb/reports/state/stochastic-operation-testing/provenance-reconstruction-20261114/`. Keep the captured target, its diff from the commit, a machine-readable manifest, command output/error/status, complete review state and per-trial input/output checks. Keep a compressed archive of the committed repository tree so the fixture content does not depend solely on future Git reachability. The main checkout and its review results are not trial output locations.

The CLI resolves its library from the worktree. Its profile file is the committed one; the explicitly named opus entry is checked against the current configuration. User-level harness configuration and provider internals are not isolated; record configuration fingerprints where safe, not credential contents. Existing command records retain prompts and launch traces. Check observed file reads for out-of-fixture access. Prompt restrictions and the checkout guard are not a filesystem sandbox.

The project startup hook is inert outside Claude cloud sessions; require the cloud-session environment flag not to be true. No source snapshot or prior review state is copied into the fixtures. Missing inputs, uncontrolled settings and any deviation must appear in the result summary.

## Interpretation

A successful exercise supports this reconstruction path for one gate. It does not establish that all review operations need only a commit and note, that the original live environment was recreated, or that the method works after code/provider changes. Practical gaps become requirements for shared provenance/fixture support rather than reasons to build a general runner immediately.

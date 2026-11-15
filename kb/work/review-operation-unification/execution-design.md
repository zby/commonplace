# Shared execution for review operations

Selected direction, 2026-11-14. This file owns the common requirements for the [review-only subset](./README.md); storage fields and command syntax are not adopted by implication.

## Execution and recording

Every admitted review operation runs through the existing Commonplace headless runtime as a Workjig workflow. A simple workflow can be one worker call applying an instruction. Instructions own judgment; shared support owns capture, provenance, result recording, deterministic validation and recovery.

```text
select requested work using its freshness policy, if any
  → capture declared inputs and provenance
  → execute the instruction through Workjig
  → retain and validate the output
  → expose completion and the current result
```

There is no parallel native-agent execution path or public prepare/accept lifecycle. Validation checks the output contract, not correctness of the judgment. Retain failed attempts and distinguish them from completed results. Keep the replaceable current-result view separate from per-execution evidence, especially repeated trial outputs. Reuse existing run records and storage where practical.

## Ordinary provenance

Record the KB commit, original target path and exact target bytes supplied to the reviewer, including uncommitted text. Capture at dispatch and give the worker that capture. Record operation/instruction identity, request/profile, observed model and executable identity separately from the KB revision.

Surrounding KB context may remain live. Qualify the record rather than claiming an immutable snapshot. An uncommitted criterion or wrapper needs an explicit identity/capture policy; do not attribute its bytes to HEAD. Preserve artifacts already produced without requiring comprehensive ordinary-run environment capture.

Freshness consumes provenance. Initially preserve existing gate hash behavior unless separately changed. Define other operations' policies from their needs; a recorded Git commit does not automatically stale every result after every commit. No policy means freshness is unassessed, not that the result is fresh.

## Operational-input boundary

The launcher may select explicitly requested inputs from shared `kb/reports/state/`. Before execution, copy them into the run and record their original identities, hashes and roles. Use retained copies, not symlinks to mutable state.

The instruction reads only these run-local operational inputs and writes run-owned outputs. It does not browse shared state or other runs. Workflow machinery handles publication to the current-result view.

**Operational inputs must be self-contained.** Provenance links do not grant access to other runs. Missing information requires a contract repair or another explicitly supplied input, not recursive discovery or dependency copying. A second state repository is optional preservation infrastructure, not a requirement.

Authored KB links are separate: ordinary reviews may read authorized live content; trials read the fixture. Necessary ignored source snapshots must be supplied explicitly. This is an access contract, not proof that current harness permissions enforce filesystem isolation.

## Controlled reconstruction

Restore the recorded KB commit in a worktree, overlay the retained target at its original path, and supply the captured operational inputs. Record the selected executable and effective harness configuration. Missing content must stop preparation or require an explicitly documented substitute baseline. Reconstruction need not recreate every circumstance of the original live incident.

Ordinary runs and trials execute the same operation implementation. Each trial gets independent mutable state, bypasses freshness skips and cross-trial answer replay, and retains its own evidence. Within-trial retries and resumes are not new observations.

Retain accessible fixture content and execution evidence comprehensively, with explicit gaps for provider internals and unretained configuration. Do not retain secrets or publish private source copies. A worktree alone neither pins an editable installation nor fixes MCP readiness.

The [reconstruction exercise](../stochastic-operation-testing/provenance-reconstruction-results.md) demonstrated exact commit-plus-uncommitted-note reconstruction with current tools, but not equivalent effective tool availability. It supports the content path, not a claim of complete isolation. Ordinary runs need not use worktrees.

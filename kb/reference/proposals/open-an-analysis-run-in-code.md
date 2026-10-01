---
description: "Proposal: open an agentic-system analysis run with one command that allocates the run ID, writes run-state, runs the publication preconditions early, and settles where the expected incumbent digest lives"
type: reference/types/design-proposal.md
---

# Open an analysis run in code

Opening a run for [`analyse-agentic-system`](../../agentic-systems/instructions/analyse-agentic-system/SKILL.md) is prose the agent carries out by hand: pick a run ID, write run-state from the template, record the method commit, and run destination inspection before reading sources. The agent copies inspection's `expected_incumbent_sha256` into the run's `## Run` prose so two publication commands can be given the same value. Inspection already checks the worktree, but the running package is first checked against the method commit at prepare or publish. This proposal records the option space for moving run opening into code and, in particular, for where the method commit and incumbent digest should live. Publication-time checks remain necessary because the worktree, method and destination can change during analysis.

## Current state (as of 2026-09-29)

- The three preconditions are functions in `src/commonplace/lib/agentic_publication.py`: `require_publishable_worktree`, `require_method_unchanged`, `require_running_package_unchanged`. Destination inspection runs only the worktree check; prepare and publish run all three.
- No opening command allocates a run ID or creates initial run-state. The ID format is checked by the `RUN_ID` pattern (`src/commonplace/lib/agentic_set.py`).
- `commonplace-agentic-analysis-publication inspect-destination` prints JSON and stores nothing. The run-state schema is closed (`additionalProperties: false`) and has no field for the digest; the run-state type says the digest is recorded in `## Run` prose.
- The digest guards against replacing an incumbent that changed since inspection. Publication checks it during validation and checks the incumbent bytes again before replacement, but no lock spans the check and replacement; simultaneous publishers can still race.
- The method commit is recorded manually for the overview's `inputs-commit`; run-state has no field for it.
- Run IDs are allocated as `AAS-<date>-<system-slug>-<nn>` in a checkout that several sessions can write to.

## The problem

1. **Late package mismatch.** The running package can differ from the opening method commit, with the mismatch first found at prepare or publish. Dirty trees are already checked before source analysis; later worktree or method changes still need publication-time checks.
2. **Hand-carried values.** The incumbent digest passes through agent prose and two later command lines. Copying a later incumbent's digest would let the run replace bytes it did not inspect at opening. The method commit also passes manually from opening to the overview, with no stored opening value against which to check it.
3. **Manual allocation.** The next `<nn>` for a system is chosen by looking at existing run directories, which can collide between concurrent sessions.

## Options

All options add an `open` command that allocates the ID, creates initial run-state, and records current HEAD as the method commit in structured run-state. That stored commit is authoritative: the overview must copy it, and publication must reject a mismatch. This common change extends the run-state contract. `open` checks worktree eligibility and running package equality before analysis; publication retains those checks and checks method drift from the stored commit. At opening, the method baseline is HEAD itself, so there is no earlier method baseline against which to reject committed changes.

The options below differ in how they retain the destination inspection result.

### A. An `open` command that also records the digest in run-state

`open` also runs destination inspection and stores its digest or explicit absence in structured run-state, bound to the inspected destination and source identity. `prepare` and `publish` read that expectation from run-state, reject a different destination or source identity, and the `--expected-incumbent-sha256` flag goes away.

- Extends the run-state contract beyond the common method-commit addition to retain the publication expectation.
- Keeps the opening-time incumbent expectation fixed; does not make check-and-replacement atomic.
- Puts the digest where the publication code already loads state (`load_run_state` validates it).

### B. An `open` command that leaves the digest in prose

`open` prints destination inspection's digest, which stays a hand-copied value in prose and later command arguments. Moves the package check earlier and automates allocation and method-commit recording; leaves the hand-carried digest.

### C. An `open` command that writes the digest into `## Run` prose in a fixed line, read back by code

No additional schema change for the digest, but publication would parse a machine-consumed value from prose alongside the structured state fields. The fixed line would become part of the run-state contract.

### D. Drop the stored digest and re-inspect inside `prepare` and `publish`

`open` checks destination eligibility but retains no digest. `prepare` and `publish` inspect the current incumbent independently. This needs no additional digest field, but permits replacement of an incumbent published since opening, including between prepare and publish. Checks within publication remain subject to the existing check-and-replacement race. Adoption would require deciding that replacing an eligible newer incumbent is acceptable; the frequency of sibling publications informs that choice, but no recorded evidence establishes it.

## Forces

- **Run-state is deliberately minimal.** The type says it proves only which run, which boundary, which bytes completed it, and which report finalized the memory member. Retaining the method commit and, under A, the publication expectation extends that scope to opening inputs; neither needs a recovery log.
- **Inspection needs a clean tree, and so does opening.** Running inspection inside `open` is consistent, because both require the same worktree state.
- **The guard's purpose and limit.** A sibling analysis can publish a review after this run opened. Retaining the opening digest detects a changed incumbent at later checks. It does not serialize concurrent publishers; a strict atomic replacement guarantee would require a separate publication change.
- **Editable-install coupling.** The package check compares the running command's source bytes with the method commit. Opening and publication may execute from different installed checkouts if both satisfy that check; checkout identity itself is not the requirement.
- **Concurrent allocation.** Two sessions opening runs for the same system need distinct `<nn>` values. Creating the run directory atomically as part of allocation is a candidate mechanism; file locking is another.

## Free choices

- Names and representation of the structured opening inputs, including how an inspected absence is distinguished from a missing expectation.
- Whether `open` also prints the paste-ready frontmatter (type, run, source identity, method commit, system name) for the overview and members.
- How `open` chooses the slug: from the caller's argument only, or normalized from the source identity.

## Operativity and warrant

For all options, `open` consumes the existing worktree and package checks before analysis. Run-state loading validates the stored method commit; `prepare` and `publish` require the overview to agree with it and retain the worktree, method-drift and package checks. A mismatch stops publication.

Under A, publication reads the incumbent expectation from structured state; under B, from command arguments copied from prose; under C, from the fixed prose line. Each rejects an incumbent mismatch. Under D, publication checks only the current incumbent's eligibility and subsequent byte stability within the command; it no longer enforces an opening-time expectation. These are identity checks, not new semantic evaluations. Byte equality says nothing about whether the incumbent was worth replacing and does not warrant an atomic concurrency guarantee.

## Adoption criteria

- An option is chosen by the operator, with its storage and overwrite-policy trade-offs named in the decision.
- For every option, tests show that `open` rejects a worktree that violates publication eligibility and a running package that differs from the opening method commit.
- Tests show that publication rejects a changed method after opening, a later worktree or package violation, and an overview method commit that differs from the stored opening value.
- Concurrent openings for the same system receive distinct run IDs without overwriting either run's state.
- For A, tests show that changing the incumbent after `open` makes publication fail, including when an initially absent destination becomes occupied; changing the destination or source identity also fails. For B and C, tests preserve the retained-expectation behavior through their respective input channels. For D, tests demonstrate and the decision accepts replacement of an eligible newer incumbent.
- The skill's step 1, items 1–2 are revised to call `open` in the same commit that ships it. Preserve obligations the command does not implement, including prior-analysis isolation and blocker handling. Scope classification and step 2's source-freezing and citation rules remain.

## Related

- [Run-state type](../../agentic-systems/types/agentic-system-analysis-run-state.md) — the contract this proposal would extend under option A.

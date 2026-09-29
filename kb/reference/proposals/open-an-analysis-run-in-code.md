---
description: "Proposal: open an agentic-system analysis run with one command that allocates the run ID, writes run-state, runs the publication preconditions early, and settles where the expected incumbent digest lives"
type: reference/types/design-proposal.md
---

# Open an analysis run in code

Opening a run for [`analyse-agentic-system`](../../instructions/analyse-agentic-system/SKILL.md) is prose the agent carries out by hand: pick a run ID, write run-state from the template, record the method commit, and later run destination inspection and copy its `expected_incumbent_sha256` into the run's `## Run` prose so two publication commands can be given the same value. The publication preconditions (clean worktree, method paths unchanged, running package equal to the method commit) already exist as code, but they first run at destination inspection and at prepare or publish, so a run that could never publish is discovered late. This proposal records the option space for moving run opening into code and, in particular, for where the incumbent digest should live.

## Current state (as of 2026-09-29)

- The three preconditions are functions in `src/commonplace/lib/agentic_publication.py`: `require_publishable_worktree`, `require_method_unchanged`, `require_running_package_unchanged`. Destination inspection runs only the worktree check; prepare and publish run all three.
- Nothing allocates a run ID or writes run-state. Only the `RUN_ID` pattern exists (`src/commonplace/lib/agentic_set.py`).
- `commonplace-agentic-analysis-publication inspect-destination` prints JSON and stores nothing. The run-state schema is closed (`additionalProperties: false`) and has no field for the digest; the run-state type says the digest is recorded in `## Run` prose.
- The digest is used as a compare-and-swap: publication proceeds only if the incumbent review still has the bytes the run assumed when it was opened.
- Run IDs are allocated as `AAS-<date>-<system-slug>-<nn>` in a checkout that several sessions can write to.

## The problem

1. **Late failure.** A dirty tree, a changed method path or a stale package install is found at publication, after the analysis work is done.
2. **Hand-carried value.** The incumbent digest passes through agent prose and two later command lines. A transcription error fails publication at best and, if it names a different real digest, defeats the compare-and-swap.
3. **Manual allocation.** The next `<nn>` for a system is chosen by looking at existing run directories, which can collide between concurrent sessions.

## Options

### A. An `open` command that also records the digest in run-state

`open` allocates the ID, creates run-state, records HEAD as the method commit, runs the three preconditions, runs destination inspection, and stores the digest in a new nullable run-state frontmatter field. `prepare` and `publish` read it from run-state, and the `--expected-incumbent-sha256` flag goes away.

- Changes the run-state contract: a new field, a schema change, and a type-spec edit.
- Keeps the compare-and-swap meaning: the digest is fixed at open time.
- Puts the digest where the publication code already loads state (`load_run_state` validates it).

### B. An `open` command that leaves the digest in prose

`open` does everything except the digest, which stays a hand-copied value. Fixes the late failure and the allocation; leaves the hand-carried value.

### C. An `open` command that writes the digest into `## Run` prose in a fixed line, read back by code

No schema change, but publication would parse prose, which the run-state type deliberately avoids (`It is not a recovery log`; state fields are frontmatter).

### D. Drop the stored digest and re-inspect inside `prepare` and `publish`

Simplest contract, no new field. The digest is then computed at publication time, so the compare-and-swap disappears: it would only detect changes between inspection and replacement inside one command, not changes since the run started. Whether the weaker guard is enough depends on how often a sibling run publishes to the same destination between open and publish, which no recorded evidence answers.

## Forces

- **Run-state is deliberately minimal.** The type says it proves only which run, which boundary, which bytes completed it, and which report finalized the memory member. A field that stores an input to publication is a small extension of that scope; it is not a recovery record.
- **Inspection needs a clean tree, and so does opening.** Running inspection inside `open` is consistent, because both require the same worktree state.
- **The guard's purpose.** A concurrent analysis of the same system can publish a review after this run opened. Only a digest fixed at open time detects that.
- **Editable-install coupling.** The package-equals-method-commit check reads the running command's source, so `open` and publication must run from the same installed checkout.
- **Concurrent allocation.** Two sessions opening runs for the same system need distinct `<nn>` values. Creating the run directory atomically as part of allocation is a candidate mechanism; file locking is another.

## Free choices

- Field name and whether `absent` is stored as a string or as null with a separate marker.
- Whether `open` also prints the paste-ready frontmatter (type, run, source identity, method commit, system name) for the overview and members.
- How `open` chooses the slug: from the caller's argument only, or normalized from the source identity.

## Operativity and warrant

Consumer: the publication commands (`prepare`, `publish`) and, under option A, `load_run_state`. Channel: code reading run-state. Force: a failed precondition or a digest mismatch stops publication. The `open` command is a new consumer of the existing preconditions, moving their force from publication time to run start. No new automated evaluation is added; the warrant for the digest check is byte equality, which stops at incumbent bytes and says nothing about whether the incumbent was worth replacing.

## Adoption criteria

- Option A or D is chosen by the operator, with the trade-off in the Forces section (a stored digest and its extra schema field, against a weaker guard) named in the decision.
- For any option, a test shows that a dirty tree, a changed method path and a stale package are each rejected by `open`, not first by publication.
- For A, a test shows that an incumbent change after `open` makes `publish` fail with the stored digest.
- The skill's step 1 and step 2 text is reduced to the command call in the same commit that ships the command.

## Related

- [Run-state type](../../types/agentic-system-analysis-run-state.md) — the contract this proposal would extend under option A.

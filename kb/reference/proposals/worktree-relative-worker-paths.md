---
description: "Proposal: shorten analysis worker command paths by using the prepared worktree as their explicit base, while retaining both validation stages."
type: reference/types/design-proposal.md
---

# Worktree-relative worker paths

Consider supplying worktree-relative paths in analysis worker commands instead
of repeating the absolute worktree prefix. The intended benefit is fewer path
reconstruction errors without changing run storage or validation ownership.
This is an unadopted proposal, not authorization to implement it.

## Current state (as of 2026-10-12)

The Pi dispatch instructions specify the current worktree's absolute root as
the worker's working directory. The handout generator in
`src/commonplace/artifactrun/handouts.py` nevertheless supplies absolute run,
artifact and file-input paths.

In three audited worker episodes, the prompt supplied a correct absolute
artifact path and a complete validation command. The worker substituted a
nonexistent worktree-like directory for the artifact directory nested under
the run. Validation failed before checking the draft. These observations
establish incorrect path reconstruction, not that path length caused it.

A six-run audit found no passing worker preflight followed by a deterministic
engine refusal. Its sole deterministic refusal followed a failed preflight
invocation; a fresh worker repaired the content. Preflight therefore remains
useful for repair within the original worker session, while the engine check
protects acceptance when preflight is not completed successfully.

## Options and consumers

**Worktree-relative commands — leading candidate.** Keep the prepared worktree
root as the explicit base for generated worker command paths. This removes the
repeated absolute prefix without relocating runs. The initial prompt locator
can remain absolute so opening the handoff does not depend on interpreting its
contents first. The generator would supply the shorter commands through the
worker prompt; the launcher would establish the working directory, and worker
instructions would require running those commands from that base. This is a
launch-and-instruction contract, not enforcement of model behavior.

**Keep absolute commands.** Leave generation and launch behavior unchanged.
Absolute paths remain independent of the shell's current directory, but the
observed reconstruction failure remains possible despite complete command
supply. This option needs no new consumer.

**Generate a bound validation command.** A per-handout command could hide the
machine-known validator arguments from the worker. The generator and launcher
would need to deliver an executable entry point that workers invoke, preserving
the existing validator's diagnostics and exit status. No such entry point is
proposed for implementation now. It adds machinery that relative commands may
make unnecessary.

## Forces and boundaries

Relative paths are shorter but depend on a stable base. A worker changing its
shell directory could make an otherwise correct command target the wrong
location. Paths outside the worktree also need an explicit policy; not every
input should automatically become a relative path.

The frozen worktree's validator must remain the executable used. Shortening a
command must not accidentally select the origin checkout or a different
installed version. Run identity and output ownership must remain unchanged.

Retain mandatory worker preflight and the independent engine check. This
proposal neither changes acceptance nor adds validation receipts, retries,
new evaluation rules, or a new storage layout. It does not claim that shorter
paths guarantee copying accuracy or that the two validation contexts are
equivalent.

## Adoption criteria and open choices

Before adoption, confirm actual worker launches use the intended worktree root,
not merely that the instructions request it. Establish how commands retain
that base after source exploration. Verify that shortened paths still select
the assigned candidate, correct run artifact, and frozen validator, including
when the coordinator starts outside that worktree.

Decide which worker-facing paths become relative and how outside-worktree
inputs are represented. Keep these choices open until the affected launch and
handout consumers are inspected. If a stable base cannot be assured, retain
absolute paths or reconsider the bound-command option.

Adoption requires a separate implementation decision and tests of path
resolution and command delivery. Subsequent runs would need to show whether
path reconstruction errors decrease; the current observations do not establish
that benefit. No implementation is commissioned by retaining this proposal.

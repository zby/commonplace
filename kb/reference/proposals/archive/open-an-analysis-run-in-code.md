---
description: "Proposal (adopted): Historical opening preflight and incumbent-digest handling before workflow start became the analysis entry point under ADR 101."
type: reference/types/design-proposal.md
---

# Open an analysis run in code

> **Archived** (see [archive README](./README.md)). Adopted through the existing
> workflow start by [ADR 101](../../adr/101-open-analysis-runs-through-workflow-start.md).
> The analysis workflow and skill carry the live operation. The dated opening
> conditions below remain a historical anchor.

## Current state (as of 2026-09-29)

The original proposal recorded three precondition functions in
`src/commonplace/lib/agentic_publication.py`: publication-worktree checks,
method-unchanged checks and running-package checks. Destination inspection
ran only the worktree check; prepare and publish ran all three.

No command allocated an analysis run ID, wrote initial run state or recorded
HEAD. The skill instructed the agent to perform these operations manually.
The expected incumbent digest appeared in the run's prose and was copied
into the publication command's `--expected-incumbent-sha256` argument.

## Retained boundary

This is the pre-adoption opening path described by the proposal, not the
current command contract. ADR 101 records the implemented workflow-owned
opening, its publication expectation, considered alternatives and remaining
limits. The proposed separate command and authored state layout were not
adopted. There is no remaining implementation commission in this archive entry.

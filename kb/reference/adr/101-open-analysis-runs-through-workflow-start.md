---
description: Open code-scheduled analyses with early publication preflight, a method pin and destination expectation before handing work to analysts
type: reference/types/adr.md
status: accepted
---

# 101 — Open analysis runs through workflow start

**Status:** accepted
**Date:** 2026-10-02

## Context

Starting expensive analysis before checking its publication conditions can
produce a result that cannot be published. The analysis also needs one frozen
method identity and an expectation of the review it may replace.

## Decision

The existing workflow start allocates the analysis run and invokes code-owned
opening before worker handouts. Opening checks the publication worktree and
running package against the method commit, pins that commit, fixes the date
and review destination, and records the expected incumbent digest. Later
publication uses that same expectation rather than inspecting a new baseline.

Use the workflow's opening state as authority. Do not add a separate analysis
opening command or require an agent to copy an incumbent digest into prose.
The analysis skill supplies the workflow-start invocation.

## Considered alternatives

**Add a dedicated open command.** This would duplicate the start operation
already owned by the generic engine and analysis definition. Allocation and
opening belong on that existing entry path.

**Carry the incumbent digest in authored run prose.** This adds a copy operation
and makes a mechanical publication expectation depend on text authorship.
Code-owned state preserves its identity without analytical interpretation.

**Inspect a fresh baseline at publication.** This would permit a run to replace
a review changed after it opened. The recorded expectation intentionally
blocks that replacement; concurrent trials need distinct destinations.

## Consequences

The agent orchestrator consumes the start command as its entry operation.
The workflow engine invokes the analysis definition's opening checks before
launching workers. Publication consumes the stored method and destination
expectations as binding preconditions. Handoffs and later consumers retain
the resulting run and manifest identity.

Opening establishes conditions at that time, not a guarantee they remain true.
Publication repeats its checks and may still refuse a stale destination or
changed method. This records the deployed opening design and adopts the
mechanical obligations of *Open an analysis run in code* without its proposed
separate command or authored state layout.

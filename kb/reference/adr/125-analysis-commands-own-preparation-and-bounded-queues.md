---
description: "Analysis commands own isolated preparation, durable allocation bindings and bounded queues while the pinned workflow and Workjig retain role and worker-launch authority"
type: reference/types/adr.md
status: accepted
---

# 125 — Analysis commands own preparation and bounded queues

**Status:** accepted
**Date:** 2026-11-07
**Amends:** [ADR 118](./118-analyses-run-as-a-workflow-over-headless-harnesses.md):
the shell-loop batch and worktree-only preparation policy. Workflow roles,
budgets, checks and publication remain unchanged.

## Context

An unattended analysis needs an explicit target, a committed method, a prepared
command environment and an operator-visible result. A shell loop cannot retain
which effects belong to which input across interruption without supplying those
bindings itself. Replacing an uncertain allocation can duplicate expensive work;
seeing no controller PID cannot establish that its workers stopped.

The implementation commission requires command-owned preparation and reporting,
one bounded queue, and the startup-file and branch-freshness checks stated by
the skill. ADR 118 deliberately removed origin-side checks because headless
workers do not inherit the caller's loaded context. These new origin checks are
an intake policy requested by this commission, not proof that origin context
reaches a worker. Unrelated dirty content may still be excluded.

## Decision

`analyse` and `batch` own the outer lifecycle. One target uses the same lifecycle
as a queue item. The coordinator records the input, selected committed method,
profile and worktree destination before preparation, then invokes only that
worktree's installed command with explicit cwd and environment. It does not
import a second workflow version into its process. The skill selects explicit
targets, invokes the command and reports unresolved operator decisions.

The pinned child owns idempotent allocation by key. It journals the run binding
before creating its directory. Reentry either discovers that exact allocation
or stops; it never allocates a replacement on uncertainty. The workflow remains
ordinary Python over Workjig-backed workers. Integration and evidence cleanup
remain separately authorized.

A controller lock excludes another controller. Per-target POSIX leases survive
into child commands, including an orphan child. SIGINT/SIGTERM stop claims and
drain children rather than attempting cancellation across Workjig's independent
worker process groups. Restart reconciles leases and pinned-child records
before claims. Unsettled worker reservations, uncertain effects and interrupted
audits require operator attention. Explicit target resume keeps the original
run, method and profile and performs no automatic acknowledgement or retry.
Ordinary analysis stops permit independent queued work; preparation failures,
command failures and uncertain ownership pause new claims.

Preparation checks origin startup files against the selected commit. Default
revision selection refuses a HEAD behind or diverging from the locally known
default branch, without fetching. Another revision is an operator choice.
The prepared worktree's existing code, cleanliness and method guards remain
mandatory. Local paths and explicit document inputs retain their source route;
remote plausibility validation performs no acquisition probes.

## Considered alternatives

**An outer Workjig call.** Rejected: it would classify workflow-command failures
and missing result files as another launch protocol around the same workers.
Ordinary subprocess ownership plus durable target/allocation bindings supplies
the needed queue recovery without another launch/retry authority.

**Four fixed sublists or shell loops.** Rejected: fixed partitions leave slots
idle behind slow targets, while independent loops do not share one durable
ownership/reconciliation boundary. A queue releases each completed analysis's
slot immediately, including after an ordinary stop.

**Terminate every process on a signal.** Rejected: Workjig workers own independent
process groups, and controller termination alone does not establish descendant
settlement. Draining is slower but retains existing ownership and completion
records. Abrupt death remains an explicit recovery case.

**One production profile per role.** Unneeded: role/attempt-specific fixture
responses use one executable harness and one recorded profile. Production model
routing is not part of queue automation.

## Consequences

The CLI consumes explicit intake and returns controller JSON and summaries.
Preparation enforces method selection; pinned-child allocation and inspection
commands supply durable bindings and results; the workflow and headless layer
supply worker truth. The canonical skill consumes the high-level invocation
surface, while low-level commands remain the separately authorized repair path.
Publication, integration and cleanup gain no authority from a queue receipt.

Limits: deterministic local fixtures exercise real workflow checks and simulated
workers, not analytical quality or live-provider behavior. The outer leases
require POSIX local-filesystem locking; network filesystem semantics are not
established. Four analyses with three role workers permit twelve role workers,
with advisory auditors occupying their analysis slots afterward. Provider
capacity, disk/inodes, worktree placement and a committed method require
operator preflight before substantial live execution. No live pilot, campaign,
integration or cleanup is implied by this decision.

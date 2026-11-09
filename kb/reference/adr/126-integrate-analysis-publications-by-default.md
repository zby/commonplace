---
description: "New high-level analysis invocations authorize guarded integration, with publication retained separately from delivery into main and replay-safe integration evidence"
type: reference/types/adr.md
status: accepted
---

# 126 — Integrate analysis publications by default

**Status:** accepted
**Date:** 2026-11-09
**Amends:** [ADR 106](./106-merge-analysis-publications-from-isolated-worktrees.md)
and [ADR 125](./125-analysis-commands-own-preparation-and-bounded-queues.md):
new high-level invocations include integration authority. Acceptance, advisory
audit independence and separately authorized cleanup remain unchanged.

## Context

The operator wants an analysis request to deliver accepted results into `main`,
not leave a second routine integration decision for each publication. Publication
and delivery can nevertheless fail independently. A dirty origin, competing
publication or interrupted Git command must not turn an accepted analysis into
a reason to repeat expensive workers or overwrite another result.

Several analyses can finish together. A worktree-local publication lock does
not serialize their changes to a shared origin. Reentry also needs evidence
that distinguishes this operation's branch or merge from an unrelated branch
with the same name.

## Decision

New `analyse` and `batch` invocations authorize guarded integration as their
final phase. After analysis children drain, the controller integrates complete
publications serially through their prepared commands and environments.
Low-level `prepare` and `run` remain the publication-only route. Existing
controllers retain their recorded policy and pinned code; a new outer command
does not grant old runs automatic commit authority. New controllers refuse a
method without the required integration protocol before allocating work.

Record publication and integration independently. Integration refusal preserves
the accepted bytes, receipt, audit evidence and worktree. It does not withdraw
acceptance, run another analyst, copy outputs into `main`, choose a conflict
side or authorize cleanup. A local blocked or out-of-scope result has no
publication to integrate.

The integration command retains clean-origin, `main`, method ancestry,
publication binding and affected-path guards. Exact-byte checks extend through
Git staging and transfer. All cooperating integrations into one Git repository
share a lock covering inspection and mutation. Durable intent and result
records bind the effect to its run, method, publication and origin. Resume
recognizes proven committed or merged effects without duplicating them;
ambiguous partial effects require operator repair. Non-cooperating Git writers
must still be excluded.

A published but unintegrated result is unfinished delivery and returns nonzero.
Advisory audit findings are not an integration veto; unsettled process ownership
remains a reason to stop new effects. Explicit initiating-agent attribution may
supply a model trailer. A tool-only call does not infer it from the analyst's
profile.

## Considered alternatives

**Keep a separate routine authorization.** Rejected for new high-level calls:
the operator explicitly wants delivery into `main` to finish the request.
Separate authority remains appropriate for old publications and cleanup.

**Append an unrecorded merge command.** Rejected: interruption after a commit
or merge would leave replay unable to distinguish completion from a pending
effect. A deterministic branch name alone does not prove ownership.

**Integrate concurrently as workers finish.** Unneeded. Serial finalization
after the analysis pool drains avoids mixing this controller's preparation and
origin changes. A repository-wide lock is still needed for other controllers
and manual integrations.

**Repair conflicts or dirty state automatically.** Rejected: stashing,
resetting, rebasing or choosing a side would exceed the accepted publication
transfer and could conceal competing work. Preserve evidence instead.

## Consequences

The high-level CLI and durable controller enforce the default and report
publication separately from integration. Prepared integration commands enforce
Git ownership, byte and recovery guards. The canonical analysis skill,
publication instruction and command reference teach invoking agents and
operators the same authority boundary. Worker packets and accepted member
contracts do not change.

Analyses can now finish routine delivery unattended when origin state permits
it. Origin dirt or competing publications can still require operator action;
that action does not require repeating analysis. Cross-system comparisons and
landscape synthesis still need their own commission after integration.

Limits: local deterministic tests establish lifecycle and Git behavior, not
analytical quality or provider performance. POSIX local-filesystem locks do not
establish safety against arbitrary Git writers or network-filesystem locking.
The change does not rewrite existing method checkouts or receipts, and a clean
merge does not certify validity under newer analysis contracts.

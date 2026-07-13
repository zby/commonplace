---
description: Full-pass packets retain guarded start-state captures and authoritative asynchronous disposition resolution
type: ../types/adr.md
tags: []
status: accepted
---

# 051-Full-pass packets own guarded captures and resolutions

**Status:** accepted
**Date:** 2026-07-13

## Context

A full improvement pass may recommend deleting or merging a note without authority to perform that operation immediately. The recommendation can remain pending while its source or proposed merge target continues to change. Applying the old recommendation later would operate on characters the pass did not assess. A hash alone can refuse stale work but cannot show what changed, and review-database snapshots have evidence-owned pruning semantics rather than the packet's retention lifetime.

The pass's assessment methods still reopen logical paths. Threading captured content through review selection, direct methods, connection discovery, and agent instructions would add a broad pinned-input seam before concurrency demonstrated the need. A cooperative no-edit rule is sufficient during the active pass, but the later asynchronous transition needs a deterministic, inspectable precondition.

## Decision

Each full-pass packet owns immutable UTF-8 `.txt` captures of the artifacts its disposition guards.

- The source is captured at pass start. A merge target is captured when the provisional merge recommendation is finalized.
- Logical repository paths remain method inputs and state keys. Packet-relative capture paths are used only for hash verification and capture-to-current diffs.
- `full-pass-report.md` uses `kb/reports/types/full-pass-report.md`. Its frontmatter is canonical for disposition and resolution; its rendered `Resolution` section is a validated projection.
- `keep` reports begin `not-required`; delete and merge reports begin `pending`. Explicit user authority may accept, reject, or apply an alternative. A readable changed input may deterministically supersede a report. Missing inputs and corrupted captures require reconciliation.
- `commonplace-guard-full-pass-report` verifies every capture, compares every current logical artifact, emits machine-readable per-input results and diffs, and exits successfully only when all inputs match. It never mutates reports or live artifacts.
- Capture paths are normalized, packet-relative `.txt` paths confined to regular non-symlink files inside the packet. Type-owned validation re-verifies capture hashes and the rendered resolution projection.
- Resolution remains instruction-driven while report volume is small. Every packet-driven keep, delete, merge, rejection, or alternative operation runs the deterministic guard immediately before its first mutation or decision record.
- Reports and captures are one retention unit. Pending packets are never pruned; resolution-aware cleanup may remove the unit only after its state is no longer load-bearing.

The first implementation adds no review-DB state, captured-input override, general capture store, lock, automatic rebase, or general artifact-version API. Hashing is shared in `commonplace.lib`; the rest remains full-pass-specific until a second consumer proves an extraction boundary.

## Consequences

Easier:

- An asynchronous recommendation can be refused against changed text and can show the operator exactly what changed.
- Review snapshot retention remains independent from full-pass decision retention.
- Logical identity cannot accidentally collapse into the report-local capture path.
- Corrupted packets, changed inputs, and missing inputs have distinct deterministic outcomes.
- Pending and rejected decisions are discoverable without markers in authored notes.

Harder:

- Gitignored report packets now contain non-regenerable resolution state and require resolution-aware cleanup.
- Active passes depend on cooperative no-edit ownership because methods are not pinned to the capture.
- The guard is optimistic; a residual comparison-to-mutation race remains.
- Merge execution remains a semantic editing operation with explicit postcondition verification, not a generic relocation command.

## Links

- [Available types](../available-types.md) — implemented-by: catalogs the `kb/reports/types/full-pass-report.md` structured state contract
- [Run a full improvement pass](../../instructions/run-full-improvement-pass-on-note.md) — procedure: creates captures and typed packets and guards keep application
- [Resolve a full-pass disposition](../../instructions/resolve-full-pass-disposition.md) — procedure: inspects, guards, and records asynchronous outcomes
- [Commonplace CLI commands](../commands.md) — implemented-by: documents the deterministic guard command
- [ADR 036 — Review acceptance is current state](./036-review-acceptance-is-current-state-not-append-only-history.md) — contrasts: review evidence retention remains separate from packet-owned decision retention

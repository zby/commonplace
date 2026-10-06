---
description: "Ingest extracts and analysis quotations resolve through one resolver against a declared pin; bytes absent from this machine are unverified information in standing validation and a refusal where a run holds the source"
type: reference/types/adr.md
status: accepted
---

# 112 — One quote resolver for grounding and analysis evidence

**Status:** accepted
**Date:** 2026-10-06
**Extends:** [ADR 072](./072-ingests-own-source-authority-and-snapshots-are-local.md) and [ADR 073](./073-untracked-source-snapshots-require-ingest-grounding.md), whose local-bytes policy now also governs analysis evidence; [ADR 111](./111-directory-types-declare-their-layout.md), whose boundary member supplies the analysis pin.

## Context

Two paths resolved the same kind of citation: a blockquote with a `> ---`
attribution, matched once within its range. Ingest validation resolved
`## Quotes` extracts against the name-paired snapshot pinned by
`snapshot_sha256`, and reported missing bytes as unverified. Analysis code
resolved member quotations against the frozen source recorded in run state,
only during a run and at run-state completion. Standing validation of an
analysis set checked quotation form and nothing else, because the frozen
checkout lives outside the KB on the machine that ran the analysis.

ADR 111 made the boundary a member whose `source` declares the frozen
checkout or capture, so the set itself now carries its pin.

## Decision

One resolver, `resolve_citations` in `commonplace.lib.quote_grounding`,
resolves citations against a pinned source with three implementations: an
ingest snapshot pinned by checksum, a Git checkout pinned at a commit, and a
capture file pinned by digest. Each citation resolves to `match`, `mismatch`
(the attribution does not name the pin, or the quote is absent, ambiguous or
outside its range) or `unverified` (the pinned bytes are not here).

The analysis set rule resolves every member's quotations against the
boundary's `source`. Standing validation reports unverified quotations once
per member as information, as it does for ingest extracts. The analysis
workflow holds the source, so its acceptance treats the same finding as a
refusal; it no longer reads run state to resolve quotations, and run-state
completion relies on set validation for them. Run state still requires its
frozen source to be present.

## Considered alternatives

**Fail standing validation when the frozen checkout is missing.** Retained
sets would fail on every machine but the one that ran them, which ADR 072
already rejected for ingest snapshots.

**Store analysis sources as KB ingests with snapshots.** A checkout at a
commit is many files, not one snapshot; one resolver interface over distinct
pins keeps both shapes without converting either.

**Keep a run-state path for analysis quotations.** It would leave standing
validation and draft feedback without quotation checks, and two resolvers
whose messages and policies drift.

## Consequences

`commonplace-validate` on an analysis set reports quotation mismatches by
member wherever the frozen source is present, and validating a working
`output/` gives analysts the same quotation findings acceptance does.
Reconciliation and overview quotations are now resolved at acceptance and in
standing validation, not only at completion. Messages share one wording, and
ambiguity advice proposing candidate ranges is available to ingest extracts.
A set without a boundary cannot resolve its quotations and fails.

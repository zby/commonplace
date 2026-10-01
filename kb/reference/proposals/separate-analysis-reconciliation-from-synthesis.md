---
type: reference/types/design-proposal.md
description: "Proposal: settle and independently verify analysis records before writing and checking the public synthesis"
---

# Separate analysis reconciliation from synthesis

## Problem

Reconciliation resolves disagreements between analyst records and writes the
public synthesis in the same job. A record correction therefore asks the next
round to write public text again, before independent verification has accepted
the records that support it. Each job also loads both record and overview
contracts, although these govern different writing tasks.

## Current state (as of 2026-10-01)

The analysis workflow runs three analysts, then bounded rounds of
reconciliation and verification. The overview holds reconciliation,
synthesis, limitations and verification. Runtime and epistemic reports remain
unchanged; reconciliation can return findings to the memory analyst.

In the local Instinctual Memory run ending in `03`, reconciliation ran three
times. Its reconciliation section grew from 3,314 to 6,406 bytes; synthesis
stayed between 4,695 and 4,775 bytes. The inspected verification blockers
concerned records and the memory profile. This is evidence from one run,
not an estimate of how often rewriting occurs. The two published member sets
have been archived unchanged in preparation for replacement runs.

## Forces

Preserve independent verification and the existing memory correction route.
Give each author one writing task. Keep public text grounded in settled
records, and keep amendments discoverable without rewriting analyst reports.
Bound correction work and preserve an exact, independently readable retained
set. Extra verification jobs cost model calls even when no correction occurs.

## Options and operative paths

### Separate reconciliation, record verification, synthesis and synthesis verification

Reconciliation becomes a retained member. The workflow consumes record
verification blockers to repeat reconciliation or stop. Once records pass,
a separate author consumes the members and reconciliation to write public
text. A second independent judge checks that text against its cited records;
its blockers permit one synthesis correction, then stop. Code renders the
overview and public review from the accepted text and both verifications.

Reconciliation and record verification load member contracts. The synthesis
jobs load the overview contract and shared evidence and record meanings.
They still read the reports as evidence. A trial must check whether a missing
member-type definition prevents a supported synthesis judgment.

Both judges are model judgments warranted by inspection of the supplied
sources and records. Structural checks establish shape, identity and reference
resolution, not semantic support or complete source coverage. No judge supplies
an independent experimental oracle. A record fault found during synthesis
checking is stated as a limitation; if this would make the synthesis
misleading, the run stops rather than reopening the record loop.

### Keep reconciliation inside the overview

The workflow could delay synthesis while still rendering reconciliation into
an overview. This keeps four retained members, but preserves a contract shared
by two authors and requires a provisional overview or extraction boundary.
Code would consume that provisional document as intermediate state.

### Reopen reconciliation for record faults found during synthesis verification

The synthesis judge could route record blockers back to the record loop. The
workflow would consume those blockers as renewed mutation authority. This
permits deeper repair but makes the correction budget and settled-record
boundary harder to understand. The present design instead stops on a fault
that cannot be represented faithfully as a limitation.

### Put verification in the reconciliation member

Code could append the judge's text to the reconciliation member. Readers would
find record amendments and their verification together. This gives the member
two author roles and makes the overview's account of completion less direct.
Keeping both verifications in the overview preserves one entry point.

## Adoption criteria

The workflow must publish a five-member set after record verification and
synthesis verification pass. Tests must exercise memory returns, both bounded
correction loops, refusal of unsupported references, and replay. The two fresh
system runs must validate and publish, with synthesis handed out once plus at
most one correction. Their traces must show the intended contract separation
and record any missing definition or late record fault. No current retained
set may fail its contract while the change lands.

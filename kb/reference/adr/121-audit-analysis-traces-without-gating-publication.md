---
description: "Why post-run analysis trace audits use failures as investigation leads but cannot gate publication or authorize corrections; pilot results and limits."
type: reference/types/adr.md
status: accepted
---

# 121 — Audit analysis traces without gating publication

**Status:** accepted
**Date:** 2026-10-21

## Context

Successful publication hides recovered command failures. Those failures can
identify weakly inspected claims, but neither a failed command nor a missing
read proves that the accepted analysis is wrong.

## Decision

Save an explicit-failure scan of every recorded attempt, including failed and
superseded attempts. After a completed Pi analysis, launch a fresh, read-only
meta-analyser to investigate at most three consequential questions within
30 tool calls. Use failures as leads; distinguish supported content defects
from claims that a process failure caused them. No findings is valid.

Keep the audit advisory. Findings, timeout and incomplete coverage do not alter
publication, the receipt or analysis exit status. Corrections require separate
authority. Preserve audit outputs as local run evidence; before worktree removal,
extract useful evidence or obtain an explicit decision not to retain it.

## Considered alternatives

**Claim-first investigation:** the pilot reached the same bounded outcomes but
used more calls on the real case; retain it as a comparison, not the default.
**Automatic correction or publication gating:** not justified by the small pilot;
a suspicious process event is not sufficient evidence for either.
**Manual audits only:** leave recovery inspection dependent on a separate commission.

## Consequences

The analysis runner supplies saved traces and accepted outputs through the
[meta-analyser instruction](../../agentic-system-analyses/instructions/analyse-agentic-system/meta-analyser.md).
The operator consumes its report as advice, not an acceptance verdict. Read-only
and investigation budgets are prompt-enforced, not an operating-system sandbox.

The [retained pilot](../../reports/retained/meta-analyser-pilot-20261021/README.md)
compared trace-first and claim-first on OpenResearch and a constructed import
case: four fresh Pi invocations using `gpt-6.1-sol`, medium reasoning. Both found
the constructed defect, recognized the repaired validator failure, and established
no failure-linked residual defect in OpenResearch. A fifth, compact trace-first
invocation checked three OpenResearch questions and established no material defect
in those paths. Exact prompts, reports, metrics and the constructed fixture remain
retained independently of the deleted audit workshop.

Limits: one real case and one constructed case establish feasibility, not detection
rates, general superiority or cost effectiveness. The compact prompt has no positive
constructed-case test. Status scanning misses masked errors; empty findings do not
certify correctness. The meta-analyser currently runs only for Pi analyses.

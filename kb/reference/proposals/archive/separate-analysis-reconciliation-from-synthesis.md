---
type: reference/types/design-proposal.md
description: "Proposal (adopted): dated analysis-workflow state and section-size observations behind the reconciliation/synthesis split"
---

# Separate analysis reconciliation from synthesis

> **Archived** (see [archive README](./README.md)). Adopted by [ADR 098](../../adr/098-separate-analysis-reconciliation-from-synthesis.md), which carries the selected design and alternatives. The pre-adoption workflow and one run's section-size observations remain here — design texture only.

## Current state (as of 2026-10-01)

Before adoption, the analysis workflow ran three analysts, then bounded rounds
of reconciliation and verification. The overview held reconciliation,
synthesis, limitations and verification. Runtime and epistemic reports remained
unchanged; reconciliation could return findings to the memory analyst.

In the local Instinctual Memory run ending in `03`, reconciliation ran three
times. Its reconciliation section grew from 3,314 to 6,406 bytes; synthesis
stayed between 4,695 and 4,775 bytes. The inspected verification blockers
concerned records and the memory profile. This is evidence from one run,
not an estimate of how often rewriting occurs. The two published member sets
were archived unchanged in preparation for replacement runs.

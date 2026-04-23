---
description: "Source-only coverage note for Trajectory-Informed Memory Generation, a trajectory-to-tip learning pipeline without local code-inspected review coverage"
type: kb/types/note.md
traits: [has-external-sources]
tags: [related-systems, trace-derived]
status: current
---

# Trajectory-Informed Memory Generation

Trajectory-Informed Memory Generation is tracked here as source-only related-system coverage, not as an `agent-memory-system-review`. The KB coverage comes from the [trajectory-informed ingest](https://arxiv.org/html/2603.10600v1), which records the paper's method and limitations. The ingest says no public source code was found as of 2026-03-13, so this belongs outside `../reviews/` until code is available and inspected.

## Trace-derived placement

The system analyzes completed execution trajectories into strategy, recovery, and optimization tips, consolidates them, and retrieves relevant tips at runtime. Its promotion target is inspectable natural-language artifacts rather than model weights. In the trace-derived survey it is the source-only counterpart to AgeMem: both learn from trajectories under task-completion-style oracles, but they choose different learning substrates.

## Review boundary

Do not create `kb/agent-memory-systems/reviews/trajectory-informed-memory-generation.md` unless a reachable repository is found and inspected. The review type in `../types/agent-memory-system-review.md` requires code access; this note keeps the system visible without overclaiming implementation evidence.

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — cross-system placement: uses the system as a source-ingested trajectory-to-artifact case
- [Trajectory-Informed Memory Generation ingest](https://arxiv.org/html/2603.10600v1) — source coverage: paper snapshot analysis and limitations
- [memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — contrast: same trajectory/oracle family as AgeMem, different promotion substrate

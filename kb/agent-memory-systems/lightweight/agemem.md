---
description: "Lightweight coverage note for AgeMem, an RL-trained LTM/STM memory-management policy covered through paper ingest rather than local code review"
type: kb/types/note.md
traits: [has-external-sources]
tags: [trace-derived]
status: current
---

# AgeMem

AgeMem is tracked here as lightweight related-system coverage, not as an `agent-memory-system-review`. The KB coverage comes from the [AgeMem ingest](https://arxiv.org/html/2601.01885v1) and the analysis note [memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md). There is no local repo-backed review for this system.

## Trace-derived placement

AgeMem learns a memory-management policy from task trajectories. The policy operates over fixed long-term and short-term memory actions: `Add`, `Update`, `Delete`, `Retrieve`, `Summary`, and `Filter`. Its promotion target is model weights, while stored facts remain in a memory store. This makes it a clean trajectory-to-weights case for the trace-derived survey, but lower-confidence as implementation evidence because the concrete runtime and storage implementation have not been inspected locally.

## Review boundary

Do not create `kb/agent-memory-systems/reviews/agemem.md` unless a reachable repository is found and inspected. The review type in `../types/agent-memory-system-review.md` requires code access; this note exists to keep the system visible without pretending the KB has repo-grounded coverage.

---

Relevant Notes:

- [memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — primary analysis note: interprets AgeMem as learnable policy under a task-completion oracle
- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — cross-system placement: uses AgeMem as a lower-confidence source-ingested trajectory-to-weights case
- [AgeMem ingest](https://arxiv.org/html/2601.01885v1) — source coverage: paper snapshot analysis and limitations

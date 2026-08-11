---
description: "A rule-based selector can target one case only when a signal already distinguishes it from the other live candidates; lacking that, the system must wait, load a bounded superset, or infer relevance from content"
type: kb/types/note.md
traits: [title-as-claim]
tags: [context-engineering, agent-memory]
---

# Rule-based context selection needs a pre-existing signal

A rule-based selector can load context for a specific case only when a signal — a feature that already distinguishes that case from the other live candidates — is available to it. The signal can be a path, type, tag, tool, event payload, or workflow mode; it need not name the target, only separate it from the alternatives. The limit is structural: a rule cannot select on a distinction that none of its inputs encode. [Codification](./definitions/codification.md) makes such selection cheap, deterministic, and reviewable, but it cannot manufacture the distinguishing signal.

When no signal is available yet, the selector has three moves instead: wait for or ask for one, [load a bounded superset](./always-loaded-context-mechanisms-in-agent-harnesses.md) so the case is present without being singled out, or infer relevance from the candidates' content — lexically or semantically. Only inference produces a targeted result without a pre-existing signal, and it does so by reading content rather than matching a feature: a different mechanism, not a variant of the same one.

Push and pull do not change this. Pull arrives with a request — a query, path, or tool call — that already carries the signal. Push must fire before the agent asks, so it needs the signal from upstream: a task identifier, the current object, a workflow mode, an event payload. A coarse always-on trigger such as session start or a bare `Write` event carries no such signal, so it can deliver generic context but never the item this case needs. Push names a delivery direction, not a way of knowing what to deliver.

The bound is on selection, not presence: a bounded superset can hold the right item without any signal picking it out. Rule-based routing is reliable exactly when the signal already exists; producing it for a case still in flight is the part outside its reach.

## Relevant Notes

- [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — grounds: the activation gap this sharpens into a constraint on rule-based selection

- [agent statelessness means the context engine should inject context](./agent-statelessness-means-the-context-engine-should-inject-context.md) — contrasts: its open “how to identify what to inject” question; exact push needs an upstream signal

- [codification](./definitions/codification.md) — defined-in: rule-based selection is the codified regime whose reach this bounds

- [frontloading spares execution context](./frontloading-spares-execution-context.md) — contrasts: frontloading uses inputs known upstream of the call; this note characterizes when the required signal is upstream

- [agentic memory systems comparative review](../agent-memory-systems/agentic-memory-systems-comparative-review.md) — evidenced-by: the cross-system push/pull split this mechanism explains

- [Activate Behavior-Changing Memory Before The Mistake](./agent-memory-requirements/activate-behavior-changing-memory.md) — extends: applies the bound to pre-action activation and separates typed from inferred cues

- [Promotion selects for unreliable activation, and the regress ends only at an external trigger](./promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md) — extends: develops the bound into a trigger-feasibility limit for activation packages

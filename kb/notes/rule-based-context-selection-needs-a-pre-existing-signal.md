---
description: "A rule-based selector can target one case only when a rule-ready signal already distinguishes it; otherwise the system must wait, load broadly, or infer relevance from task and candidate content"
type: kb/types/note.md
traits: [title-as-claim]
tags: [context-engineering, agent-memory]
---

# Rule-based context selection needs a pre-existing signal

A rule-based selector can load context for a specific case only when a rule-ready signal — a codified feature that already distinguishes that case from the other live candidates — is available to it. The signal can be a path, type, tag, tool argument, event payload, or workflow mode; it need not name the target, only separate it from the alternatives. The limit is structural: a rule cannot select on a distinction that none of its inputs encode. [Codification](./definitions/codification.md) makes such selection cheap, deterministic, and reviewable, but it cannot manufacture the distinguishing signal.

When no rule-ready signal is available yet, the system has three moves instead: wait for or ask for one, [load a bounded superset](./always-loaded-context-mechanisms-in-agent-harnesses.md) so the case is present without being singled out, or infer relevance from the current task and candidate content — lexically or semantically. Inference can produce a targeted result without a predeclared route, but not without selection input: it derives a relevance relation from content instead of matching a distinction already encoded for the rule.

Push and pull do not change this. Pull supplies selection input directly through a query, path, or tool call. A path may itself be rule-ready; a natural-language query may instead supply content from which relevance is inferred. Push must obtain equivalent input upstream through a task identifier, current object, workflow mode, event payload, or input to a relevance classifier. A coarse trigger such as session start or a bare `Write` event can deliver generic context, but by itself cannot choose among multiple live candidates. Push names a delivery direction, not a way of knowing what to deliver.

The practical consequence inverts where the difficulty seems to lie. Storing a memory and injecting it are the easy parts; **the hard part is the selector — deciding which sessions are the relevant ones** — and that is exactly what needs the selection input. Having stored the `curl` lesson tells the system nothing about which sessions are about to run `curl`.

The bound is on selection, not presence: a bounded superset can hold the right item without any signal picking it out. Rule-based routing is reliable exactly when the rule-ready signal already exists; deriving relevance for a case still in flight belongs to inference rather than rule matching.

## Relevant Notes

- [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — grounds: the activation gap this sharpens into a constraint on rule-based selection

- [agent statelessness means the context engine should inject context](./agent-statelessness-means-the-context-engine-should-inject-context.md) — contrasts: its open “how to identify what to inject” question; exact push needs an upstream signal

- [codification](./definitions/codification.md) — defined-in: rule-based selection is the codified regime whose reach this bounds

- [frontloading spares execution context](./frontloading-spares-execution-context.md) — contrasts: frontloading uses inputs known upstream of the call; this note characterizes when the required signal is upstream

- [agentic memory systems comparative review](../agent-memory-systems/agentic-memory-systems-comparative-review.md) — evidenced-by: the cross-system push/pull split this mechanism explains

- [Activate Behavior-Changing Memory Before The Mistake](./agent-memory-requirements/activate-behavior-changing-memory.md) — extends: applies the bound to pre-action activation and separates typed from inferred cues

- [Promotion selects for unreliable activation, and the regress ends only at an external trigger](./promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md) — extends: develops the bound into a trigger-feasibility limit for activation packages

---
description: "Identifies operator functions concealed by successful interactive work, so unattended workflows can replace those dependencies or narrow their scope."
type: types/note.md
traits: [title-as-claim]
tags: [warranted-autonomy, goal-prioritization]
---

# Unattended work needs the functions that interaction supplied

Successful interactive work can conceal dependencies on the operator. Removing the operator removes part of the working system wherever their contributions were necessary. Preserving its capacity requires another way to perform those functions, or a narrower scope in which they are unnecessary. The unit of analysis is the human–agent process: success after intervention does not establish that the opening request was sufficient.

## What interaction supplies

An operator can perform five overlapping functions:

- **Purpose:** determine which result would be useful and resolve competing interpretations.
- **Context:** supply missing facts, prior decisions, boundaries, or sources.
- **Correction:** challenge an inference or redirect work after an intermediate result.
- **Evaluation:** judge whether the result answers the intended question.
- **Stopping:** decide whether to continue, accept a partial result, abandon a direction, or return an unresolved problem.

These are functions, not separate roles or stages. Evaluation can trigger correction or stopping. Some contributions become identifiable only after execution exposes the need; [a bare writing prompt does not determine its intended contribution](./a-bare-writing-prompt-does-not-determine-its-intended-contribution.md).

## What this adds

[Intent-framed delegation](./intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) explains the governing controls; [fix what the executor cannot determine](./fix-what-the-executor-cant-determine-not-what-it-will.md) allocates choices; [the augmentation–automation boundary](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) addresses detecting incorrect outputs. This inventory helps identify which human contributions a successful conversation concealed before choosing how to replace them.

The delegation note records a 2026-09-27 regression rerun: the handoff omitted that coverage breadth would be compared with withheld baselines, and two of three coordinators chose narrower boundaries. This illustrates a missing purpose contribution; it does not test whether this inventory would prevent the omission.

Commonplace's `AGENTS.md` Delegation rule already implements parts of the inventory through purpose, inputs, acceptance, verification, and stop conditions. A task can package known contributions, but still needs a response to conditions discovered during execution.

Agent design and environment design are alternative places to provide that response. For example, a [workshop layer that retains work in progress](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) can preserve unresolved decisions between runs. When only the operator can supply a missing decision, stopping preserves their authority but leaves the work incomplete.

Recurring interventions therefore identify candidate dependencies to investigate. This complements [measuring improvements per human judgment](./increasing-computational-autonomy-relocates-human-effort.md): first identify what the judgment supplied, then test whether later runs can supply it adequately.

## Scope

The inventory is not exhaustive. Unnecessary interventions need no replacement, and an agent's existing judgment may already supply a function. Identifying a dependency does not establish that its proposed replacement is reliable.

A function can also be lost on the delegate's side rather than the operator's. In Norman's autopilot case the automated delegate held the delegated function and dropped the anomaly reporting that a human delegate had supplied, because the task written for the autopilot named only what the autopilot consumed ([Norman 1989](../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md)). That dependency falls outside the five functions above, which interaction supplies from the operator's side.

## Open Questions

Does supplying a way to detect and handle one recurring intervention improve unattended outcomes beyond fuller initial instructions? Compare the same work class, acceptance criterion, and total resource budget. No improvement would challenge the dependency diagnosis or its proposed replacement.

---

Relevant Notes:

- [Norman, The problem of automation: inappropriate feedback and interaction](../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md) — evidenced-by: qualifies the inventory; the lost function is supplied by the delegate, not the operator, and the evidence is incident narratives rather than a test

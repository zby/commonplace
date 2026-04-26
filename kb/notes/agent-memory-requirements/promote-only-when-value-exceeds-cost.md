---
description: "Candidate memory should become durable only when future retrieval or activation value exceeds review and maintenance cost"
type: kb/types/note.md
tags: [agent-memory, context-engineering]
status: current
---

# Promote Only When Future Value Exceeds Maintenance Cost

Promotion from candidate memory to durable artifacts creates obligations: review, update, invalidation, connection, retirement, and consistency with sources. System-definition promotions add risk because they change behavior. Candidate observations should therefore remain cheaper and less authoritative than library notes, policies, instructions, tests, or scripts until future retrieval or activation value exceeds review and maintenance cost.

An observation inbox can be the lightest candidate stage. Its job is to record a noticed pattern, bug, missing link, possible synthesis, or improvement opportunity before the mechanism is understood. It should be cheap enough to use during unrelated work, but it needs later triage so it does not become a second untrusted library.

## Promotion Destinations

- Knowledge notes, decision records, source reviews, indexes, and negative-result records for material whose value is explanatory.
- Procedures, skills, runbooks, checklists, and instructions for recurring work patterns.
- Schemas, type contracts, review gates, tests, validators, linters, scripts, plugins, runtime extensions, and guardrails when the learned rule is deterministic enough for [codification](../definitions/codification.md).
- Always-loaded policy only when the rule is stable, high-frequency, and cheap enough to spend context on every session.
- Existing domain work surfaces when those are the actual source of authority.

For behavior-changing material, promotion should usually update an authoritative source artifact first. Assistant-facing cues, prompt excerpts, checklists, generated indexes, and other compiled surfaces should normally be rendered from that source unless they are explicitly governed as the source themselves.

This promotion path is a [constraining](../definitions/constraining.md) gradient: prose candidate, curated note, instruction, checklist, test, script, guardrail. [Spec mining is codification's operational mechanism](../spec-mining-as-codification.md) gives the practical loop for moving repeated failures or procedures toward executable checks.

## Evaluation Questions

- Is the candidate cheaper and less authoritative than promoted memory?
- Does promotion create an explicit maintenance obligation?
- Does promotion strength depend on signal type, role, and consequence?
- Are compiled cues and prompt files render targets rather than accidental source artifacts?

---

Relevant Notes:

- [Spec mining is codification's operational mechanism](../spec-mining-as-codification.md) - explains how repeated failures move toward executable checks
- [Constraining](../definitions/constraining.md) - defines the gradient from prose to stricter symbolic forms

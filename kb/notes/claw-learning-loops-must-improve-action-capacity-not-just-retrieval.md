---
description: A Claw learning loop must target contextual competence (execution, classification, planning, communication), not just retrieval accuracy — question-answering is one mode among many
type: kb/types/note.md
traits: [title-as-claim]
tags: []
---

# Claw learning loops must improve action capacity, not just retrieval

A [Claw](../sources/simon-willison-karpathy-claws.ingest.md) accumulates context and acts on a user's behalf. Its system-level learning objective is therefore **contextual competence**: the capacity to act appropriately given what it has retained about the domain, user, and project. Retrieval remains an essential subsystem objective, but it is not a sufficient success criterion for the Claw as a whole.

This distinction separates action capacity from action outcome. Retained knowledge can expand the range of actions a system is equipped to perform without guaranteeing that any particular action will succeed. Execution, classification, communication, planning, and precedent recognition all depend on accumulated context, but their outcomes also depend on the model, prompt, tools, permissions, and environment.

## Action capacity needs action-guiding artifacts

Reference facts and relationships are not the only retained material that can improve future work. A Claw may also need preferences about how work should be done, procedures learned from successful executions, and precedents that preserve earlier judgments and their rationale. Voice guides and domain models are further examples of action-guiding artifacts, not evidence that the document type system itself must change.

[Koylanai's Personal Brain OS](../sources/koylanai-personal-brain-os.ingest.md) provides one anecdotal example: its self-reported design stores preferences, procedures, precedents, and voice material separately. This establishes that such a design exists, not that practitioner-built Claws converge on it.

## Existing mutations can learn different content

The [KB learning loop](./automating-kb-learning-is-an-open-problem.md) proposes extracting, synthesising, reformulating, regrouping, and retiring artifacts. Those operations can already express preference codification, procedure capture, and precedent consolidation. What changes is not necessarily the mutation vocabulary, but which candidates are proposed and what evidence licenses their promotion.

For example, repeated user choices may suggest a preference, while successful traces may suggest a procedure. Neither should become authoritative merely because it appeared once or correlated with success: [choosing what to learn requires both validity and learning-value gates](./choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md).

## Evaluation needs contribution attribution

At the Claw level, the relevant question is whether behavior became more contextually competent. At the KB-subsystem level, the questions are narrower: Did the needed artifact exist? Did it represent the lesson faithfully, reach the relevant context, and causally affect the action? These questions preserve a modular diagnostic boundary. An action failure licenses a KB mutation only when the failure can be attributed to missing, misleading, unavailable, or behaviorally inert retained knowledge rather than to the model, prompt, tools, permissions, or environment.

Existing systems illustrate both sides of this boundary. [Agent Workflow Memory](../agent-memory-systems/reviews/agent-workflow-memory.md) distils successful traces into workflow prose for later tasks, while [Voyager](../agent-memory-systems/reviews/voyager.md) promotes successful programs into a reusable skill library. Yet retained experience can be present without affecting behavior. Storage and retrieval alone therefore do not establish learning impact, as the [behavioral-faithfulness evidence](../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) shows.

Retrieval learning is therefore a valid layer, not a rival objective. It can measure artifact availability, fidelity, and selection. The broader action outcome indicates whether the Claw's competence improved; attribution tells its learning loop which subsystem, if any, should change.

## Open Questions

- What practical intervention or counterfactual can establish that a retained artifact caused an action improvement rather than merely co-occurred with it?
- Which end-to-end failures can be attributed cheaply enough to license a KB mutation rather than a model, prompt, tool, permission, or environment change?

---

Relevant Notes:

- [Agent memory needs discoverable, composable, trusted knowledge under bounded context](./agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) — extends: develops contextual competence into minimum properties of useful retained knowledge
- [Memory design adds operational axes to artifact analysis](./memory-design-adds-operational-axes-to-artifact-analysis.md) — extends: maps capture, activation, authority, lifecycle, and evaluation around retained artifacts
- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — grounds: durable readable artifacts can change system behavior during deployment

---
description: "Behavior-changing memory must activate before relevant actions rather than waiting for explicit retrospective search"
type: kb/types/note.md
traits: [has-external-sources]
tags: [agent-memory, context-engineering, learning-theory]
---

# Activate Behavior-Changing Memory Before The Mistake

The system must not merely answer "what do we know?" It must sometimes answer an unasked question: "what past lesson applies to the action I am about to take?"

[Continual learning's open problem is behaviour, not knowledge](../continual-learning-open-problem-is-behaviour-not-knowledge.md): adding retrievable facts is easier than changing future action. A stored correction only matters operationally if it fires before the agent repeats the corrected behavior.

## Methods

- Always-loaded instructions for stable, high-frequency, low-cost constraints.
- On-reference loading when a document, source, issue, or artifact is explicitly mentioned.
- On-invoke loading through skills, tools, or workflows that carry their own instructions.
- On-situation loading through typed cues that match proposed actions, task domains, risk markers, or decision spaces.
- Checklists, tests, scripts, lint rules, approval gates, or runtime guardrails when the lesson can be moved from prose toward symbolic enforcement.

Typed cue indexes provide the on-situation loading form of this family. A cue can carry a trigger condition, lesson, source pointer, behavioral authority, consequence weight, and placement target. Matching can use rules, embeddings, action classifiers, or LLM relevance judgments. The choice depends on consequence, false-positive tolerance, and cost.

## Behavioral Faithfulness

A cue that fires and enters context has not succeeded unless it changes downstream action in the intended direction. High-authority behavior-shaping material needs evidence that it earns its context budget: WITH/WITHOUT comparisons, perturbation tests, post-action trace audits, or other checks against behavior. [Large Language Model Agents are not Always Faithful Self-Evolvers](../../sources/llm-agents-are-not-always-faithful-self-evolvers.md) is the cautionary example: written or compressed memories can improve measured behavior without being used in the way their designers assume.

[Synapptic](../../agent-memory-systems/reviews/synapptic.md) is the clearest reviewed system that treats activation as something to test rather than assume. It extracts behavioral guards from Claude Code sessions, runs WITH/WITHOUT ablations with an LLM judge, records per-model verdicts, and excludes guards marked redundant or harmful before compiling them into assistant-facing memory surfaces.

## Evaluation Questions

- Does relevant behavior-changing memory activate before the risky action?
- Is activation scoped enough to avoid wasting context?
- Does the system test whether fired memory actually changes behavior?
- Are high-priority cues demoted when they are redundant, harmful, stale, or too noisy?

---

Relevant Notes:

- [Continual learning's open problem is behaviour, not knowledge](../continual-learning-open-problem-is-behaviour-not-knowledge.md) - grounds the behavior-change test
- [Knowledge storage does not imply contextual activation](../knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes storage from effective activation
- [Large Language Model Agents are not Always Faithful Self-Evolvers](../../sources/llm-agents-are-not-always-faithful-self-evolvers.md) - evidence: causal-intervention warning that visible memory can fail to drive behavior

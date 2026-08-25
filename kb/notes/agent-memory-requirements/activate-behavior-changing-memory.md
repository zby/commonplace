---
description: "Behavior-changing memory must activate before relevant actions rather than waiting for explicit retrospective search"
type: kb/types/note.md
traits: [has-external-sources]
tags: [agent-memory, context-engineering, learning-theory]
---

# Activate Behavior-Changing Memory Before The Mistake

The system must not merely answer "what do we know?" It must sometimes answer an unasked question: "what past lesson applies to the action I am about to take?"

[Continual learning requires governing behaviour-changing writes, not just storing content](../continual-learning-requires-governing-behaviour-changing-writes.md): adding retrievable facts is easier than changing future action. A stored correction only matters operationally if it fires before the agent repeats the corrected behavior.

## Methods

- Always-loaded instructions for stable, high-frequency, low-cost constraints.
- On-reference loading when a document, source, issue, or artifact is explicitly mentioned.
- On-invoke loading through skills, tools, or workflows that carry their own instructions.
- On-situation loading through typed cues that match proposed actions, task domains, risk markers, or decision spaces.
- Checklists, tests, scripts, lint rules, approval gates, or runtime guardrails when the lesson can be moved from natural-language toward symbolic enforcement.

Typed cue indexes provide the on-situation loading form of this family. A cue can carry a trigger condition, lesson, source pointer, behavioral authority, consequence weight, and placement target. Matching can use rules, embeddings, action classifiers, or LLM relevance judgments. The choice depends on consequence, false-positive tolerance, and cost.

## Documentation-specific candidates remain hypotheses

System documentation that arrives with the system rather than accumulating from its use is not read-back under this KB's [memory boundary](../knowledge-storage-does-not-imply-contextual-activation.md), but documentation intended to change agent behavior faces the same delivery and uptake gates. Gao and Chen's [coding-agent trace study](../../sources/from-agent-behaviour-to-agent-friendly-documentation.ingest.md) motivates two candidates. Self-contained documents with locally retrievable structure may reduce dependence on cross-document navigation. Runnable examples, doctests, and schema contracts may turn a prose expectation into an executable specification or check.

Neither candidate is a demonstrated activation technique. The first targets delivery: the study observed repeated reading but no `Follow-reference` event under its trace definition. The second targets verification and measurement: the authors explicitly present executable documentation as a hypothesis for intervention studies after observing no explicit documentation-based validation sequence. Both still require a comparison showing that the implemented documentation-and-delivery package changes behavior in the intended direction.

## Behavioral Faithfulness

A cue that fires and enters context has not succeeded unless it changes downstream action in the intended direction. High-authority behavior-shaping material needs evidence that it earns its context budget: WITH/WITHOUT comparisons, perturbation tests, post-action trace audits, or other checks against behavior. [Large Language Model Agents are not Always Faithful Self-Evolvers](https://arxiv.org/html/2601.22436v3) is the cautionary example: written or compressed memories can improve measured behavior without being used in the way their designers assume.

[Synapptic](../../agent-memory-systems/reviews/synapptic.md) is the clearest reviewed system that treats activation as something to test rather than assume. It extracts behavioral guards from Claude Code sessions, runs WITH/WITHOUT ablations with an LLM judge, records per-model verdicts, and excludes guards marked redundant or harmful before compiling them into assistant-facing memory surfaces.

## Evaluation Questions

- Does relevant behavior-changing memory activate before the risky action?
- Is activation scoped enough to avoid wasting context?
- Does the system test whether fired memory actually changes behavior?
- Are high-priority cues demoted when they are redundant, harmful, stale, or too noisy?

---

Relevant Notes:

- [Continual learning requires governing behaviour-changing writes, not just storing content](../continual-learning-requires-governing-behaviour-changing-writes.md) - grounds the behavior-change test
- [Knowledge storage does not imply contextual activation](../knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes storage from effective activation
- [Large Language Model Agents are not Always Faithful Self-Evolvers](https://arxiv.org/html/2601.22436v3) - evidence: causal-intervention warning that visible memory can fail to drive behavior

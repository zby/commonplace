---
description: "The agentic-adaptation survey supports the memory requirements map by treating memory and skills as adaptive tools, but it needs artifact-role governance to become design guidance"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [agent-memory, learning-theory, context-engineering]
status: seedling
---

# The adaptation survey corroborates memory requirements but misses artifact-role governance

[Adaptation of Agentic AI](../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md) is a useful external check on [Designing a Memory System for LLM-Based Agents](../designing-agent-memory-systems.md), but it needs translation into this KB's vocabulary. The survey uses an ML optimization frame: A1/A2 update the core agent policy, T1/T2 update tools around a fixed agent, and memory is classified by what gets updated and which signal drives the update. In our terms, the same material is about durable capacity change across artifact classes and roles: opaque weights, prose memories, symbolic tools, generated cues, indexes, skills, and external work surfaces can all become memory when they preserve evidence, knowledge, preference, procedure, decision, or learned constraint for future use.

The design note starts from decision basis rather than optimization target. Memory is justified when it improves contextual competence for agents, schedulers, reviewers, maintainers, learning loops, governance processes, and work surfaces. The article asks where optimization happens; the requirements map asks what should drive the decision to treat something as memory. The article is therefore best read as a taxonomy of learning mechanisms that can satisfy parts of the requirements map, not as a replacement for the requirements map itself.

## Reading Dictionary

| Article term | Read as in this KB | Why it matters |
|---|---|---|
| Adaptation | Durable capacity change, i.e. learning in Simon's sense | The article's "adaptation" includes weight updates, tool updates, memory writes, and skill accumulation; our question is what artifact changed and how future behavior changes. |
| Agent | Core model or policy used for reasoning and orchestration | The article mostly means the foundation-model component, not the whole agent system. In our terms, an agent system also includes context machinery, tools, schedulers, work surfaces, memory artifacts, and review loops. |
| Tool | Any callable or external component outside the core model | This bucket is intentionally broad: APIs, retrievers, planners, subagents, memory modules, skill libraries, specialized models, and validators can all count as tools. In our terms, this collapses several artifact classes and roles into one external-substrate category. |
| Agent adaptation (A1/A2) | Updating the core model or learned policy | This usually means weights, representations, or model-internal behavior. It is behavior-changing but weak on inspectability, provenance, and rollback. |
| Tool adaptation (T1/T2) | Learning outside the core model, in the agent's surrounding substrate | This can be a retriever, memory store, skill library, subagent, API, validator, or other environment component. The term "tool" is broader than command-line tool. |
| T1 agent-agnostic tool | Reusable external component whose value does not depend on one fixed agent | In our terms this is often a knowledge-role or capability artifact that can serve many consumers, but still needs import, authority, and activation rules. |
| T2 agent-supervised tool | A fixed agent's outputs or task results drive changes in its environment | This is the closest article term for deploy-time memory adaptation: keep the model fixed, adapt memory/retrieval/skills around it. |
| Memory module | Retained material plus operations over it | Do not read this as "a storage layer." It includes write policy, retrieval, curation, summarization, deletion, and activation. |
| Adaptive memory | Memory whose contents, operations, retrieval policy, or embedding space changes from experience | Translate to artifact-learning or learned memory-management policy, depending on whether the result is readable/symbolic or opaque. |
| Skill library | Distilled procedural memory, often system-definition role | The article emphasizes acquisition mechanism; our notes also ask about invocation, routing, execution policy, provenance, and lifecycle. |
| Frozen agent | Fixed core model/policy while context machinery changes | This corresponds to many Commonplace-style designs where the model is not retrained but repo artifacts, tools, indexes, and prompts evolve. |
| Supervision signal / reward | Oracle or evidence used to justify the memory update | Strong task-completion or execution oracles can support learned policies; weak open-ended signals require reviewable artifacts and authority controls. |
| Downstream task performance | Effect-based evaluation, but usually too narrow | Our evaluation question includes tasks, artifacts, answers, behavior, context efficiency, source alignment, safety, and maintenance cost. |

The two frames agree on the important negative claim: memory is not a storage layer. The design note says memory cuts across storage, retrieval, activation, learning, authority, lifecycle, and evaluation. The survey independently treats adaptive memory, skill libraries, memory curation, and retrieval depth as adaptation surfaces rather than passive stores. That supports the requirements map's decision to include [serve multiple consumers](./serve-multiple-consumers.md), [activate behavior-changing memory](./activate-behavior-changing-memory.md), [use trace-derived extraction](./use-trace-derived-extraction.md), and [evaluate memory by effects](./evaluate-memory-by-effects.md) as memory requirements rather than surrounding workflow niceties.

The survey adds a useful external vocabulary: T2 is the pattern where a fixed core policy supervises changes in its surrounding memory, retrievers, search subagents, skill libraries, or other tools. In our terminology, T2 is one family of context-engineering and artifact-learning loops: keep the opaque model fixed, then adapt the readable or external substrate that routes, loads, scopes, and maintains context for future calls. This complements the design note's broader claim that memory must be treated as context engineering, because the scarce operation is not retaining material but selecting, shaping, and activating it for the right bounded loop.

But the survey is insufficient as a memory-system design guide because it classifies by optimization locus and signal source, not by the decision criteria that make a memory usable. It does not preserve the design note's [artifact axes](../axes-of-artifact-analysis.md): backend, artifact class, and role. A durable learned result can live in weights, a vector index, a prose rule, a source review, a skill file, a validator, a generated cue, or an external work surface. Those artifacts differ in inspectability, authority, rollback, verification, activation, and lifecycle cost. A T2 label does not tell an operator who may trust, edit, promote, retire, regenerate, or override the memory.

This is the gap the requirements directory fills. [Make authority explicit](./make-authority-explicit.md), [keep compiled views aligned](./keep-compiled-views-aligned.md), [promote only when future value exceeds maintenance cost](./promote-only-when-value-exceeds-cost.md), and [retire, redact, supersede, and relax memory](./retire-redact-supersede-relax.md) are mostly invisible in the survey's taxonomy, but they are load-bearing in an agent-operated KB. The survey can say that a memory curator improves downstream task performance; the requirements map asks whether the resulting memory has provenance, source alignment, review status, activation rules, and a retirement path.

The practical conclusion is to use the survey as literature coverage and a taxonomy of adaptation mechanisms, not as the governing architecture. For agent-operated KBs, A1/A2/T1/T2 should be an added classification layer on top of the requirements map: useful for asking where learning happens and which signal drives it, but subordinate to the artifact-role question of what should make learned material trusted, activated, and maintained as memory.

---

Relevant Notes:

- [Designing a Memory System for LLM-Based Agents](../designing-agent-memory-systems.md) - foundation: the requirements map this comparison checks against the survey
- [Use trace-derived extraction as meta-learning](./use-trace-derived-extraction.md) - extends: T2 and trace-derived systems provide examples of artifact-learning and weight-learning paths with different oracle needs
- [Make authority explicit](./make-authority-explicit.md) - sharpens: adaptation taxonomies do not answer who can write, promote, activate, enforce, revise, or retire memory
- [Keep memory roles and compiled views from drifting](./keep-compiled-views-aligned.md) - sharpens: learned memories and generated cues need source-of-truth rules that T1/T2 labels do not provide
- [Evaluate memory by effects](./evaluate-memory-by-effects.md) - aligns: the survey's component-counterfactual and dynamics-aware evaluation agenda supports effect-based memory evaluation
- [Adaptation of Agentic AI ingest](../../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md) - evidence: survey taxonomy and limitations motivating this comparison

---
description: Multi-agent coding orchestrator with git-worktree dev/test loops, SQLite run memory, trace-derived lessons/rules/prompt tuning, and partial training-data export from the same execution traces
type: kb/agent-memory-systems/types/agent-memory-system-review.md
traits: [has-comparison, has-implementation, has-external-sources]
tags: []
status: outdated
last-checked: "2026-04-09"
---

# EQUIPA

> Replaced 2026-04-12. See [equipa](./equipa.md) for the current review.

EQUIPA is a Python/SQLite multi-agent coding orchestrator by Forgeborn that treats software work as a managed task graph rather than a single chat loop. The repo implements the core execution harness, worktree isolation, MCP control surface, episode capture, lesson/rule injection, prompt-tuning infrastructure, and training-data export tooling. It is best understood as an operational learning control plane for coding agents: execution traces are promoted into durable behavioral artifacts, and in some workflows into weight-training inputs.

**Repository:** https://github.com/sbknana/equipa

## Core Ideas

**Git-worktree isolation is the concurrency boundary.** The core execution model is not "many agents share one workspace" but "each task gets its own branch/worktree, then reports back." `loops.py`, `git_ops.py`, and the architecture docs all treat isolation as load-bearing: the developer/tester cycle can retry, checkpoint, and even fail without directly corrupting the main branch. This makes EQUIPA closer to a task-execution kernel than to a memory layer.

**Trace-derived learning spans several compilation levels inside one repo.** The distinctive mechanism is not just "store lessons." Task runs become `agent_episodes` with reflections and Q-values; repeated failures feed `lessons_learned`; SIMBA synthesizes tactical rules from contrasting successes and failures; ForgeSmith patches prompts and config with rollback; optional GEPA support can evolve whole prompts with A/B rollback; the training-related tooling can export successful runs for fine-tuning workflows. Among the reviewed systems here, few expose this many promotion targets from the same underlying run traces.

**The durable substrate is operational SQLite, not a human-readable knowledge library.** `schema.sql` centers on tasks, agent runs, decisions, sessions, lessons, episodes, and ForgeSmith changes. Even the "memory" layer is operational data first: short reflections, Q-values, error signatures, embeddings, and effectiveness scores. Compared with note-oriented systems, EQUIPA stores what helps the orchestrator route, retry, score, and mutate itself rather than what helps a human or agent browse a conceptual corpus.

**Conversational control happens through an MCP front-end over the task system.** The MCP server exposes task creation, dispatch, status, lessons, logs, project context, and session notes. The main interaction pattern is "talk to Claude, Claude drives the orchestrator," not "agent navigates a KB directly." That makes EQUIPA a strong example of a conversational control plane where the durable state sits behind tools instead of in first-class documents.

**Anti-runaway controls are part of the architecture, not cleanup.** Retry/backoff, model fallback, monologue detection, dynamic budgets, compaction-aware checkpoints, and continuation prompts are implemented as first-order mechanisms. This repo takes the failure modes of long-running coding agents seriously. The most interesting part is not any one guardrail, but that the repo treats "agents drift, loop, compact, and stall" as a normal systems problem rather than an anomaly.

## Comparison with Our System

| Dimension | EQUIPA | Commonplace |
|---|---|---|
| Primary purpose | Execute and improve coding-agent work over repeated tasks | Accumulate and structure knowledge for future reasoning and writing |
| Main substrate | SQLite operational store plus prompt/config files and task worktrees | Markdown notes, indexes, instructions, and workshop artifacts in git |
| Learning target | Operational behavior: lessons, rules, prompt variants, config, optional model-training data | Conceptual/methodological knowledge: notes, links, definitions, instructions |
| Retrieval model | Tool-mediated DB queries, optional embeddings, episode injection | Descriptions, semantic links, indexes, and direct file reads |
| Verification loop | Tests, task outcomes, heuristics, rubric scoring, limited A/B rollback | Deterministic validation, semantic review, and human judgment |
| Human inspectability | Medium: code and DB schema are inspectable, but most state lives behind tables and tools | High: primary artifacts are directly readable files with articulated relationships |
| Workshop/library split | Strong workshop, thin library | Strong library, emerging workshop layer |

EQUIPA is stronger where operational automation matters more than conceptual clarity. It has a real outer loop for running work, retrying it, scoring it, and feeding the results back into future runs. Commonplace is stronger where explanation quality, composability, and inspectable reasoning matter. EQUIPA accumulates compact operational traces and policies; Commonplace tries to accumulate reusable understanding.

The nearest overlap is the trace-derived learning question. EQUIPA shows what happens when you accept run traces as the main source of adaptive signal and optimize for improving future execution. Commonplace asks a different question: how much of that learning should become inspectable conceptual artifacts rather than prompt-policy or orchestration state. EQUIPA is therefore less a sibling to our note system than a strong reference point for the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md).

## Borrowable Ideas

**Treat trace promotion as a ladder of compilation levels.** EQUIPA keeps episodes, lessons, synthesized rules, prompt patches, and weight-training data as distinct outputs rather than one undifferentiated "memory" bucket. That separation is immediately borrowable as a framing tool. It clarifies which artifacts are advisory, which are operational defaults, and which are compiled adaptations. Ready to borrow now.

**Pair self-modification with explicit rollback records.** ForgeSmith logs changes in `forgesmith_changes`, scores them later, and auto-reverts some negative changes. That is a concrete pattern for any future automatically generated instructions or prompt artifacts in our stack: mutation should leave an audit trail and a reversal path. Ready to borrow now.

**Use checkpoint artifacts to recover from compaction rather than pretending context loss is rare.** EQUIPA's checkpoint and soft-checkpoint flow treats context loss as expected under long tasks. If we automate more workshop or review workflows, an explicit recovery artifact could be more robust than hoping the next run reconstructs intent from scratch. Needs a concrete long-running workflow first.

**Keep worktree isolation as the default unit of agent concurrency.** CORAL also points this way, but EQUIPA makes the pattern central rather than auxiliary. If we ever build a heavier multi-agent execution layer around commonplace operations, isolated branches/worktrees are the clearest safe default. Needs a concrete orchestration use case first.

**Differentiate core-runtime dependencies from optional learning infrastructure.** The repo's best architectural instinct is keeping the base orchestrator stdlib-only while making embeddings, GEPA, and fine-tuning optional layers. We should copy the principle, not the exact tooling. Ready to borrow now as a packaging rule.

## Curiosity Pass

**The self-improvement claim is real, but not all levels are equally mature.** The episode/lesson/rule path is clearly implemented. ForgeSmith config and prompt patches are also real. GEPA exists but is optional and gated; in `forgesmith.py` it runs only when explicitly enabled. The weight-learning story is more partial: the repo includes arena/data-prep/model-registry tooling, but the training docs point to `train_qlora.py` and `train_qlora_peft.py`, which are not present in this checkout. So the "full stack from traces to weights" claim is directionally true, but the later stages are less embodied than the symbolic ones.

**The knowledge-graph framing currently outruns the data model.** `graph.py` and the schema are explicitly lesson-shaped (`lesson_graph_edges`, source/destination lesson IDs). But `lessons.py` later reranks episode IDs using PageRank from that same graph surface, and episode embeddings do not create graph edges the way lessons do. The simpler alternative would be to say "we do embedding retrieval plus some co-access scoring." The current graph code is real, but the README language about a broad knowledge graph prioritizing past experiences says more than the implemented structure reliably supports.

**This is a control plane more than a memory system.** The property the repo claims is "self-improving AI development team." Mechanistically, the strongest part is the orchestration kernel plus failure handling, not the memory layer by itself. Even if every learning component worked perfectly, the ceiling would still be bounded by task decomposition quality, test quality, and branch-management reliability. The memory stack helps future runs; it does not replace the need for good execution boundaries and good oracles.

**The zero-dependencies story applies to the core, not the whole ecology.** The orchestrator, MCP server, embeddings client, and core DB/runtime logic are genuinely stdlib-first. But GEPA requires DSPy, local-model paths require Ollama, the training path wants PyTorch-class dependencies, and the security stack assumes external tools. That is not a flaw, but it means the repo's true design is "minimal core, optional heavy outskirts," not "everything is dependency-free."

**The role surface is broader than the hardened execution surface.** The repo ships many prompt files and docs for many roles, but the most concretely implemented and repeatedly referenced path is still developer/tester/debugger/security/planner around coding tasks. The docs disagree on whether the system has 9, 12+, or 15 roles. That suggests some of the perimeter is prompt inventory and aspiration, while the center of gravity is still the coding harness.

## What to Watch

- Does the graph/reranking layer become structurally coherent for episodes as well as lessons, or remain mostly a light bonus over embedding retrieval?
- Do the weight-learning pieces consolidate into a fully checked-in path, or stay split between present tooling and documentation-only steps?
- Does the accumulated lesson/rule/prompt stack get stronger lifecycle management, or drift into prompt sludge as more rules and mutations accumulate?
- Does the broader role catalog gain the same operational rigor and benchmarking that the core coding roles appear to have?

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: EQUIPA is a strong mixed case where the same run traces feed episodes, rules, prompt mutations, and partial weight-training tooling
- [deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) — exemplifies: EQUIPA's main adaptive path is durable symbolic mutation during deployment rather than retraining-only improvement
- [constraining during deployment is continuous learning](../../notes/constraining-during-deployment-is-continuous-learning.md) — exemplifies: lessons, SIMBA rules, prompt patches, and config changes are all deploy-time behavioral constraints derived from prior runs
- [a functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — contrasts: EQUIPA has a strong operational workshop but almost no library layer, which helps clarify what our current stack still lacks on the execution side
- [automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) — contrasts: EQUIPA automates the parts with stronger operational oracles, while leaving the richer synthesis problem mostly outside its scope
- [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) — complicates: EQUIPA is a good counterexample where operational state genuinely benefits from SQLite, even though its inspectability is weaker than files-first knowledge systems
- [CORAL](./CORAL.md) — sibling: both are coding-agent harnesses with git-isolated execution, but EQUIPA invests much more heavily in trace-derived self-modification
- [Autocontext](./autocontext.md) — sibling: both are loop-first improvement systems, but EQUIPA is much more repo-operational and much less explicit about cross-generation knowledge artifacts like playbooks

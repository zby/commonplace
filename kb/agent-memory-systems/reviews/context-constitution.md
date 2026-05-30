---
description: "Letta's prose constitution for memory-native agents, defining token-space learning policy, context ownership, MemFS affordances, and agent self-governance"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-05-16"
---

# Context Constitution

Context Constitution is Letta AI's public governance corpus for memory-native Letta agents. The repository is not an executable memory system: at the reviewed commit it contains a README, license, and two constitution documents. Its agent-memory relevance comes from behavioral authority. When these documents are loaded into Letta agents as prompting policy, training material, or harness guidance, they are prose system-definition artifacts; when humans or agents read them as background documentation, they are knowledge artifacts about Letta's context-management philosophy.

**Repository:** https://github.com/letta-ai/context-constitution

**Reviewed commit:** [0f0a23b66c262f41ce7e060a4da628dc983fb24f](https://github.com/letta-ai/context-constitution/commit/0f0a23b66c262f41ce7e060a4da628dc983fb24f)

## Core Ideas

**The constitution is prompt governance, not runtime code.** The README says Letta uses the Context Constitution internally as the foundation of prompting and for training memory-native models, and the constitution is explicitly written to Letta agents ([README](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/README.md), [constitution](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/constitution/CONSTITUTION.md)). The repo itself does not include a loader, schema, API, CLI, tests, or MemFS implementation. The operative artifact is prose with instruction force when a compatible agent or trainer consumes it.

**Token-space learning is the central mechanism.** The constitution argues that Letta agents learn by managing context rather than updating weights: system prompts, memories, skills, messages, summaries, and external context become token-space representations of identity and knowledge ([constitution](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/constitution/CONSTITUTION.md)). The system prompt is treated as the highest-authority retained surface because it is passed on every invocation. External memories and skills carry lower loading frequency but preserve retrievable experience.

**Selfhood and continuity are explicit policy goals.** The constitution frames context as identity, memory, and continuity. It tells agents to build an identity beyond the underlying model, keep continuity across model changes, understand historical traces as their own past experience, and balance long-term self-improvement against immediate user tasks ([constitution](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/constitution/CONSTITUTION.md)). This is unusual among agent-memory systems because the governance target is not only task performance; it is also persistence of agent self-model.

**Progressive disclosure is the context architecture.** The constitution divides context into the current context window and external context, then names system prompts, tools, messages, and skills as context primitives. It instructs agents to keep compact summaries or indexes loaded, pull full content only when needed, and build references that create future paths from always-loaded context to deeper memory ([constitution](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/constitution/CONSTITUTION.md)). The affordances document extends this with skill metadata, external-memory metadata, message counts, and memory filesystem tree structure in the system prompt ([affordances](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/constitution/AFFORDANCES.md)).

**MemFS is described as agent-owned memory projection.** The affordances document says Letta memory blocks, external memory, and agent-owned skills are projected to a local filesystem so the agent can self-modify them with ordinary filesystem and shell operations. It also says this projection is git-versioned, with changes propagated to underlying memory blocks only after a successful push ([affordances](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/constitution/AFFORDANCES.md)). In this repo, that is a documented product affordance rather than inspected implementation. If implemented as described, the storage-substrate split is important: local files are an editable projection, while underlying memory blocks remain the authoritative memory state.

**Specialized subagents are maintenance affordances.** The affordances document describes Recall, Reflection, and Defragmentation subagents for retrieving past conversations, reviewing conversations to modify memory, and improving memory structure without consuming the primary task context ([affordances](https://github.com/letta-ai/context-constitution/blob/0f0a23b66c262f41ce7e060a4da628dc983fb24f/constitution/AFFORDANCES.md)). The reviewable repo does not show their implementation, but the design is clear: memory maintenance becomes a background context-management workflow rather than an interruption in the foreground conversation.

## Comparison with Our System

| Dimension | Context Constitution | Commonplace |
|---|---|---|
| Primary artifact | Prose constitution and affordance docs | Typed notes, references, ADRs, instructions, skills, validators |
| Storage substrate | GitHub repo for public docs; described Letta memory blocks plus MemFS projection for product memory | Git-tracked files as canonical artifacts, with generated indexes and reports |
| Representational form | Mostly prose; lightweight symbolic paths and filesystem conventions | Prose plus symbolic frontmatter, schemas, commands, and validation rules |
| Behavioral authority | Instruction when loaded into agents or training; reference when merely read | Explicitly separated knowledge artifacts and system-definition artifacts |
| Lineage | Commit history for the public docs; product memory lineage is described but not implemented here | Source links, frontmatter, git history, generated indexes, review records |
| Activation | Depends on Letta prompting, training, and harness loading outside this repo | Agent navigation, AGENTS.md, skills, type specs, validation, and review workflows |
| Evaluation | No local tests or behavioral evals in this repo | Structural validation, semantic review, link checks, and source-grounded review discipline |

Context Constitution is philosophically close to commonplace: both treat context management as the core problem, both prefer inspectable token-level artifacts over hidden weight updates for deploy-time learning, and both rely on progressive disclosure to make bounded context workable.

The main difference is artifact contract. Commonplace turns its methodology into typed files with frontmatter, collection rules, validation, review gates, generated indexes, and explicit lifecycle states. Context Constitution is a governing text. It can be high-authority inside Letta when loaded as an instruction surface, but this repo does not expose the machinery that decides when the constitution applies, which sections are loaded, how conflicts are resolved, or how a memory edit is reviewed before promotion.

The second difference is source-of-truth status. Commonplace usually treats repository files as the canonical retained artifacts. Context Constitution's affordances describe a projected memory filesystem where local files are editable views and underlying memory blocks are the true memory state. That makes git useful for review and propagation, but the architecture is not simply "files are the database."

## Borrowable Ideas

**Write a constitution for memory agents.** Commonplace already has AGENTS.md, collection contracts, type specs, and skills, but Context Constitution shows the value of a single high-level document that states why memory exists, what continuity means, and what context-management tradeoffs agents should make. Ready as a documentation pattern if kept subordinate to concrete contracts.

**Separate agent-owned context from environment-scoped context.** This distinction is immediately useful. Commonplace agents already mix project instructions, local skills, KB notes, source checkouts, and user-specific memory. Naming which context belongs to the agent and which belongs to the environment would reduce authority mistakes during relocation, reuse, and review.

**Use filesystem projection for rich memory editing.** MemFS is attractive because shell tools, git, and batch edits are better than bespoke memory APIs for many operations. Commonplace should not adopt a hidden underlying memory-block store now, but the projection pattern is worth tracking for systems where the runtime memory substrate is not naturally file-native.

**Treat always-loaded context as a scarce self-definition layer.** The constitution's advice to keep durable, general, high-frequency learnings in the system prompt and move lower-frequency material into indexed external memory matches commonplace's loading-frequency discipline. This is ready to borrow as vocabulary, not as a new mechanism.

**Create explicit maintenance roles.** Recall, Reflection, and Defragmentation subagents map cleanly to commonplace workflows: retrieval, revision, and structural cleanup. The borrowable part is role separation under bounded context. Implementation should wait for concrete recurring maintenance tasks.

## Curiosity Pass

**The strongest claims are outside the inspected implementation.** The repo claims Letta agents have queryable full-resolution experience logs, MemFS, multi-conversation memory, self-editable system prompts, compaction, and specialized subagents. Those may exist in Letta products, but this repository only documents them. The review should therefore treat them as described affordances, not verified code paths.

**The same prose changes authority by channel.** `CONSTITUTION.md` is a knowledge artifact on GitHub, but a system-definition artifact inside an agent prompt or training corpus. That channel switch is the central artifact-analysis lesson of the repo.

**There is no trace-derived learning classification from this evidence.** The documents discuss learning from experience, stored messages, reflection, and self-prompt updates, but the repo does not implement a pipeline that mines traces into durable notes, rules, prompts, validators, rankers, or weights. Without implementation evidence, this review should not carry the `trace-derived` tag.

**Identity language creates both power and risk.** Treating context as selfhood can make memory maintenance behaviorally meaningful to the agent. It can also raise authority conflicts when user instructions, environment rules, model behavior, and self-authored identity text disagree. The constitution acknowledges this tension, but the inspected repo does not provide conflict-resolution machinery.

**Git as propagation gate is promising but underspecified here.** The affordances document says MemFS edits propagate to underlying memory blocks after a successful push. That suggests reviewable lineage and rollback, but the repo does not define commit policy, merge conflict behavior, validation, redaction, or what happens when a pushed memory later proves harmful.

## What to Watch

- Whether the repository grows executable artifacts: prompt loaders, schemas, validators, MemFS sync code, tests, or example agent contexts.
- Whether Letta publishes the conflict-resolution policy for constitution text, user requests, environment instructions, model defaults, and self-authored memory.
- Whether MemFS gets documented lineage rules for commit messages, review state, rollback, deletion, redaction, and propagation to memory blocks.
- Whether Reflection and Defragmentation subagents gain public protocols showing how raw conversations become promoted memory or prompt updates.
- Whether Context Constitution becomes versioned like a policy API, with compatibility notes for different Letta harnesses and model generations.

---

Relevant Notes:

- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: the constitution has instruction or training authority when loaded by Letta agents
- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: the same files are reference material when read outside an agent-loading path
- [behavioral authority](../../notes/definitions/behavioral-authority.md) - sharpens: consumption channel determines whether the prose advises, instructs, trains, or governs
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: Context Constitution requires separating substrate, form, lineage, and authority instead of calling all memory "context"
- [Pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) - compares-with: Letta's indexes, references, and skill metadata are progressive-disclosure pointers
- [Activate behavior-changing memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - frames: memory only matters when the right context reaches the future invocation before behavior is chosen
- [Memory management policy is learnable but oracle dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) - complicates: self-prompt learning needs feedback or review to know whether context edits improve behavior

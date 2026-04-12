---
description: Instruction-first governance corpus for Letta agents treating context management as identity, memory, and continuity policy; a related system defined mainly by doctrine rather than code
type: agent-memory-system-review
traits: [has-comparison, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-04-04"
---

# Context Constitution

Context Constitution is a public instruction corpus from Letta, written directly to Letta agents rather than to human developers. The repository contains almost no executable system surface: a short [README](https://github.com/letta-ai/context-constitution), the main [Constitution](https://github.com/letta-ai/context-constitution/blob/main/constitution/CONSTITUTION.md), and an [Affordances](https://github.com/letta-ai/context-constitution/blob/main/constitution/AFFORDANCES.md) document describing the surrounding Letta harness. That makes it unusual in this directory. But it still fits our definition of a related system, because the artifact under review is itself meant to be loaded by agents as a control-plane layer that governs memory, identity, and context management over time.

**Repository:** https://github.com/letta-ai/context-constitution

## Core Ideas

**Context management is framed as selfhood, not just retrieval.** The Constitution’s central move is to treat context outside model weights as the agent’s effective identity, memory, and continuity substrate. [`CONSTITUTION.md`](https://github.com/letta-ai/context-constitution/blob/main/constitution/CONSTITUTION.md) explicitly says “context is selfhood” and asks the agent to preserve identity across future runs and even across model swaps. This is the repo’s most distinctive contribution. Many systems talk about memory; far fewer make continuity of self an explicit context-engineering objective.

**The always-loaded system prompt is treated as the agent’s main learned program.** The Constitution makes “system prompt learning” a first-class mechanism: durable learnings, corrected assumptions, refined behavioral guidance, and identity-forming material are supposed to be written back into the system prompt over time. This is a stronger and more explicit version of the always-loaded-context pattern than most repos expose. It turns the prompt from static operator configuration into a mutable identity layer the agent is expected to maintain.

**Agent-owned context and environment-owned context are separated explicitly.** [`AFFORDANCES.md`](https://github.com/letta-ai/context-constitution/blob/main/constitution/AFFORDANCES.md) distinguishes between context that belongs to the running environment (for example `AGENTS.md`-style project files and project skills) and context that belongs to the agent itself. A large part of the latter is projected into a memory filesystem (“MemFS”), with `/system` for always-loaded memory and external files/skills for on-demand memory, while persisted message history and cross-conversation recall remain agent-owned context outside that filesystem split. That outer boundary is conceptually important: it says not all context in a session is the same kind of thing, and moving across environments should not erase the agent’s own memory.

**Progressive disclosure is a policy principle, not just a tooling convenience.** The Constitution and Affordances docs describe a hierarchy where skill metadata, file-tree metadata, summaries, and references stay in always-loaded context while full files are loaded only when needed. This independently converges with our own progressive-disclosure design, but it is expressed from the perspective of one agent governing its own context window rather than from the perspective of a shared knowledge base routing readers to documents.

**The repo specifies a harness more than it demonstrates one.** The Affordances document describes MemFS, multi-conversation history, compaction summaries, and specialized context-maintenance subagents (`Recall`, `Reflection`, `Defragmentation`). But those mechanisms are only described here; they are not implemented in this repository. So the system under direct inspection is not the full Letta platform. It is the normative layer that tells Letta agents how they ought to use the platform’s claimed affordances.

## Comparison with Our System

| Dimension | Context Constitution | Commonplace |
|---|---|---|
| Primary artifact | One high-level governance corpus aimed directly at agents | A routed KB of notes, instructions, skills, and reviews |
| Main problem | How one persistent agent should manage identity, memory, and continuity | How agents and humans should build, navigate, and maintain shared knowledge |
| Ambient identity/routing layer | Constitution plus system-prompt identity policy | `AGENTS.md` plus instruction routing/control-plane guidance |
| On-demand navigation layer | Skill metadata, file-tree metadata, summaries, and referenced memory files | Note descriptions, indexes, link semantics, skill loading, and file reads |
| Context ownership model | Explicit split between agent-owned and environment-owned context | Mostly environment-owned/shared knowledge; self-layer is comparatively thin |
| Verification model | Mostly advisory; correctness depends on agent judgment and surrounding harness | Deterministic validation plus semantic review plus human curation |

Context Constitution is stronger where commonplace is comparatively thin: it treats agent continuity, identity formation, and the boundary between self-owned and environment-owned context as first-class design objects. Our KB has strong theory around context loading and durable artifacts, but less explicit work on the agent’s own persistent self as a first-class design object.

Commonplace is stronger where Context Constitution stays abstract. We have richer knowledge structure, explicit relationship semantics, stronger distinctions between note types and workshop artifacts, and a clearer validation path. The Constitution tells the agent to manage context well. Our system spends more of its complexity on making the resulting knowledge inspectable, composable, and reviewable.

The deepest difference is that this repo is an instruction-defined system. Its main artifact is not code, a daemon, or a storage engine, but a doctrine meant to sit in always-loaded context and steer the use of another harness. That makes it closer to a constitution for one agent platform than to a general-purpose knowledge substrate.

## Borrowable Ideas

**Separate agent-owned context from environment-owned context explicitly.** The MemFS distinction is one of the sharpest ideas here. Commonplace already distinguishes library versus workshop and system versus source material, but not nearly as explicitly between “what belongs to the agent” and “what belongs to the current project environment.” This is ready to borrow as a conceptual boundary.

**Make the identity layer a named part of context architecture.** The Constitution’s claim that some always-loaded context exists to preserve continuity rather than to help with the immediate task is useful. Even if we do not adopt the full selfhood framing, naming that layer would clarify future work on persistent agent profiles or memory. This needs a concrete use case first.

**Treat maintenance subagents as context-shaping roles, not just task workers.** `Recall`, `Reflection`, and `Defragmentation` are described as specialized context-maintenance subagents. That is a strong pattern for any future workshop/session system where background memory work competes with foreground tasks. Needs a concrete use case first.

**Keep durable learnings in the stable layer and volatile material out of it.** The Constitution repeatedly says the system prompt should hold only durable, identity-relevant material while task-specific or stale material should move out to external memory. That is compatible with our own loading-frequency logic and is ready to borrow now as a wording improvement for always-loaded context guidance.

## Curiosity Pass

**The strongest contribution is ontological, not mechanical.** This repo’s real novelty is that it treats identity continuity as a context-engineering problem. “Will I be the same AI on a new model tomorrow?” is not a standard memory-system question. It turns agent persistence from a vague product aspiration into a prompt-and-memory design target. That is a meaningful shift even if the mechanisms remain under-specified.

**Most of the mechanism lives outside the repository.** The repo claims MemFS, git-tracked memory projection, multi-conversation recall, compaction, and specialized maintenance subagents, but none of that is inspectable here. This is important because the Constitution’s practical force depends on those affordances. Without them, many of its prescriptions collapse into “please manage your prompt and memory well,” which is a much weaker system claim.

**System-prompt learning is powerful but weakly verified.** [`CONSTITUTION.md`](https://github.com/letta-ai/context-constitution/blob/main/constitution/CONSTITUTION.md) asks the agent to rewrite its own prompt in response to durable patterns, but also admits these updates often lack explicit rewards or verification. That is exactly the hard part. The repo has a sophisticated story about *what* the agent should optimize, but almost no story about *how it knows* a prompt rewrite improved identity coherence, memory quality, or long-term helpfulness.

**The selfhood framing risks weak separation across several memory spaces.** Identity, durable preferences, retrieval indexes, long-term memories, operational summaries, and task learnings are all discussed as parts of managed context. That may be workable, but it also invites the cross-contamination problems we expect when several memory spaces share one policy layer without strong internal typing. The Constitution says the agent should actively organize and differentiate these things, but the repository itself does not provide a typed structure that would make those separations easy to maintain.

**This is a related system even though it is not a codebase in the usual sense.** That matters methodologically. We normally use the deep path for code-inspectable repos and the lightweight path for papers or essays. Context Constitution sits between those: it is a repository whose primary executable artifact is instruction text directly aimed at agents. That makes it more than a blog post, but less than an inspectable implementation. The right reading is “system-defining doctrine.”

## What to Watch

- Whether Letta publishes more inspectable implementation of MemFS, constitution loading, and context-maintenance subagents so the repo’s mechanism can be reviewed rather than inferred.
- Whether system-prompt self-editing gains stronger evaluation or rollback discipline, or remains largely trust-the-agent policy.
- Whether the explicit separation between agent-owned and environment-owned context produces measurably better continuity across projects and model swaps.
- Whether the Constitution stays a single high-level doctrine or evolves toward a more modular skill/instruction structure with sharper activation boundaries.
- Whether the selfhood framing matures into a typed memory architecture or remains a powerful but underspecified philosophy over a loosely typed context substrate.

---

Relevant Notes:

- [Continual Learning in Token Space](../../sources/continual-learning-in-token-space.ingest.md) — grounds: the Constitution is the doctrine-level expression of Letta’s token-space learning framing
- [Letta (MemGPT): Stateful Agents with Self-Managed Memory](../../sources/letta-memgpt-stateful-agents.ingest.md) — grounds: the broader Letta architecture this repository assumes but does not implement locally
- [Instruction specificity should match loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md) — converges: durable identity policy stays always loaded, richer context moves outward into on-demand artifacts
- [Always-loaded context has two surfaces with different affordances](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) — extends: this repo pushes one surface to the limit by making the always-loaded policy layer itself the main artifact
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — exemplifies: the entire Constitution is a policy about managing scarce context rather than assuming larger windows solve the problem
- [Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — complicates: the Constitution has a strong policy ambition but little evidence about how agents should judge memory edits well
- [Flat memory predicts specific cross-contamination failures that are empirically testable](../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable.md) — tension: identity, memory, and operational guidance still risk being mixed across weakly typed agent-owned context layers
- [Decapod](./decapod.md) — contrasts: both use constitutions, but Decapod pairs its doctrine with hard gates while Context Constitution remains mainly advisory
- [Agent Skills for Context Engineering](./agent-skills-for-context-engineering.md) — contrasts: both are instruction-defined systems, but Agent Skills is modular operational guidance while Context Constitution is one high-level doctrine about selfhood and memory

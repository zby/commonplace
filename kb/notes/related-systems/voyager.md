---
description: Embodied lifelong-learning agent that turns successful Minecraft trajectories into reusable JavaScript skills with vector retrieval, automatic curriculum, and critic-gated refinement
type: note
tags: [related-systems]
status: current
last-checked: 2026-03-20
---

# Voyager

Voyager is a research codebase for open-ended embodied learning in Minecraft. The loop is explicit in the source: propose a task, retrieve relevant prior skills, have an action agent generate code, execute it in the environment, let a critic judge success, then promote successful programs into a reusable skill library. Built by Guanzhi Wang and collaborators as the open-source implementation of the Voyager paper.

**Repository:** https://github.com/MineDojo/Voyager

## Core Ideas

**Successful trajectories are promoted into executable code artifacts.** In `voyager/voyager.py`, successful rollouts return `program_code` and `program_name`; `learn()` then calls `self.skill_manager.add_new_skill(info)`. Promotion is not "store a reflection" but "store a reusable JavaScript function plus retrieval metadata." That makes Voyager one of the clearest trace-derived code-learning systems in this queue.

**The skill library is inspectable and retrieval-backed.** `SkillManager` persists code under `skill/code/`, generated description stubs under `skill/description/`, a `skills.json` manifest, and a Chroma vector store in `skill/vectordb/`. Retrieval is semantic over the generated descriptions, but reinjection is actual code: `retrieve_skills()` returns the stored program bodies, which are then injected into the action-agent system prompt.

**Learning is gated by a critic, not by free accumulation.** After execution, `CriticAgent.check_task_success(...)` inspects the environment state, inventory, chest observation, and current task/context, then returns `success` plus critique. Only success triggers promotion into the skill library. Failed attempts still shape the next retry through critique, but they do not become durable skills.

**Curriculum is an active trace-selection mechanism.** `CurriculumAgent` does more than pick the next task. It maintains completed and failed task lists, asks and answers Minecraft-specific QA questions, caches them in a Chroma-backed store, and uses that cache to generate task context. This means Voyager learns not just from rollouts, but also from a growing side memory about the world and task prerequisites.

**The action loop is iterative code repair, not one-shot planning.** `ActionAgent` carries forward execution errors, chat logs, inventory state, nearby entities, chest memory, and critic feedback. On each retry it retrieves skills again with a richer query that includes the latest summarized chat log. The practical loop is therefore: retrieve code, write code, execute, critique, retry, and only then promote.

**The learned substrate is cumulative but structurally shallow.** Voyager accumulates many useful skills, and existing names can be rewritten with versioned files, but there is no richer relation model between skills, no contradiction handling, and no explicit retirement mechanism beyond replacement. The library grows as a bag of callable capabilities rather than a typed knowledge graph.

## Comparison with Our System

Voyager is much closer to deploy-time codification than to note-based memory. It learns from trajectories, but the promoted result is executable code scoped to one embodied domain rather than a cross-domain body of linked explanations.

| Dimension | Voyager | Commonplace |
|---|---|---|
| Trace source | Repeated embodied task trajectories plus environment observations and execution errors | Human+agent editing traces, notes, links, workshop artifacts |
| Learned substrate | JavaScript skills, generated descriptions, task/QA caches | Notes, links, instructions, workshop artifacts |
| Promotion target | Inspectable executable artifacts only | Inspectable text artifacts only |
| Update style | Critic-gated promotion of successful programs, semantic retrieval, name-level rewrites | Manual curation and targeted file edits |
| Oracle strength | Strong environment oracle: task success judged from world state | Mostly human judgment and local validation |
| Scope | Single embodied domain with compositional skills | Cross-domain KB |

Voyager is stronger than our current system on automatic promotion into reusable artifacts. Once a task succeeds, the repo can turn that success into a callable program and reuse it later without human curation.

Commonplace is stronger on articulation and explanatory reach. Voyager's skills are reusable behaviors, but the system does not explain why those behaviors work, how two skills relate, or when one skill invalidates another. It accumulates capability faster than it accumulates understanding.

Relative to [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md), Voyager sharpens a subtype the current survey only partly names: trace-derived learning into executable artifacts. It belongs with artifact-learning systems, but the artifact is code rather than observations, tips, or notes.

## Borrowable Ideas

**Promote only after a strong local success check.** Ready now as a pattern. Voyager does not durably store every attempt; it stores only successful programs. That gating discipline is useful anywhere we have a hard enough oracle.

**Store retrieval text separately from the executable artifact.** Ready now as a design pattern. The split between `code/`, `description/`, `skills.json`, and vector index is simple but effective: retrieval works on descriptions, execution works on code.

**Use context-building side memory distinct from the main artifact library.** Needs a use case first. Voyager's QA cache is not the skill library; it is auxiliary support memory for proposing tasks and filling context gaps. That separation could map well to workshop-side scaffolding around a KB.

**Treat successful outputs as codification candidates, not just memories.** Ready now as a framing. Voyager shows that some trace-derived learnings should become executable tools or scripts directly, rather than intermediate notes.

## Curiosity Pass

Voyager's strongest idea is not just "skill library." It is the end-to-end promotion path from trajectory to code. The repo makes the handoff concrete: success under a critic becomes a reusable program, and later tasks get that program back as in-context capability.

The interesting limitation is that the retrieval abstraction is thinner than the artifact it retrieves. Skill descriptions are generated automatically and stored mainly to support vector search; they do not become a richer semantic layer over the code. So the library can compound behavior without really maturing its knowledge structure.

That makes Voyager a useful counterpoint to note-based systems. It solves a problem we do not solve automatically yet, but only because the domain has a strong oracle and a natural codification target. The ceiling is domain breadth and interpretability: you get callable competence quickly, but not much explicit theory about that competence.

## What to Watch

- Whether later descendants keep the code-artifact promotion path but add stronger lifecycle control such as pruning, dependency tracking, or contradiction detection
- Whether the QA cache remains a sidecar, or evolves into a richer world model that shapes curriculum and retrieval more deeply
- Whether executable-skill accumulation transfers beyond embodied domains with hard environmental feedback
- Whether newer systems keep Voyager's critic-gated promotion discipline while changing the learned substrate from code to weights or richer artifacts

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: Voyager is a clear trajectory-to-executable-artifact case that broadens the artifact-learning side beyond notes, observations, and tips
- [deploy-time learning](../deploy-time-learning-the-missing-middle.md) — sharpens: Voyager uses the same artifact-accumulation mechanism inside a benchmarked embodied loop, without retraining weights, even though the repo is research infrastructure rather than a production deployment system
- [Autocontext](./autocontext.md) — compares: both run repeated improvement loops over trajectories, but Autocontext promotes mostly textual playbooks and optional weights while Voyager promotes executable skills
- [ExpeL](./expel.md) — contrasts: both consolidate across repeated runs, but ExpeL promotes maintained natural-language rules while Voyager promotes callable code
- [codification](../codification.md) — exemplifies: Voyager is one of the clearest cases where successful natural-language-guided behavior is hardened into executable code artifacts

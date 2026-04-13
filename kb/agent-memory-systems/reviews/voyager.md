---
description: Embodied lifelong-learning Minecraft agent whose action/critic/curriculum/skill-manager loop promotes successful trajectories into a Chroma-indexed library of reusable JavaScript functions
type: agent-memory-system-review
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-12"
---

# Voyager

Voyager is the research codebase accompanying the 2023 paper *Voyager: An Open-Ended Embodied Agent with Large Language Models*. It runs a GPT-4-driven agent inside Minecraft (via a Mineflayer/Fabric bridge) through a loop of four LLM roles — action, critic, curriculum, skill manager — that together propose tasks, generate JavaScript programs, execute them against the environment, judge success from world state, and durably store successful programs as retrievable skills. Built by Guanzhi Wang and collaborators at NVIDIA/Caltech/UT Austin and released under MIT.

**Repository:** https://github.com/MineDojo/Voyager

## Core Ideas

**Four roles form a closed generation-and-promotion loop.** `voyager/voyager.py` wires `CurriculumAgent.propose_next_task` → `ActionAgent` code generation → `VoyagerEnv.step` execution → `CriticAgent.check_task_success` → `SkillManager.add_new_skill`. `learn()` iterates this up to `max_iterations`, and `rollout()` retries the action agent up to `action_agent_task_max_retries` (default 4) inside one task. The role split is stable and small; what varies across iterations is the accumulated skill library and the curriculum agent's completed/failed task lists.

**Only critic-approved programs are promoted, and the promotion is code.** At `voyager.py:353`, `if info["success"]: self.skill_manager.add_new_skill(info)`. `add_new_skill` writes the JavaScript `program_code` to `skill/code/<name>.js`, a generated natural-language description to `skill/description/<name>.txt`, an entry in `skill/skills.json`, and an embedding of the description into a Chroma collection under `skill/vectordb/`. The critic is an LLM judge reading biome, inventory, health, position, equipment, chest observation, task and context — not an environment oracle — so success is LLM-adjudicated from world state rather than deterministically checked.

**Retrieval and reinjection use different substrates.** `SkillManager.retrieve_skills(query)` embeds the query (context + summarized chat log) and runs `similarity_search_with_score` over the description vector store with `retrieval_top_k=5`. But what gets returned and reinjected into the action agent's system prompt is the original code from `self.skills[name]["code"]`. Descriptions exist purely as a retrieval handle; the artifact the next action agent sees is an executable JavaScript function body.

**Iterative repair inside a task is distinct from skill promotion across tasks.** Each `step()` feeds the action agent the latest events, executed code, and critic critique; on failure, retrieval re-runs with a query augmented by `summarize_chatlog(events)` and the loop repeats. Promotion happens only once the critic returns success. Failed attempts never become library entries, but they do shape the within-task retry through critic critique and the chat-log-augmented query.

**Skill overwrite is version-stamped, not merged.** When `program_name` is already present (`skill.py:71`), the code deletes the old vector entry, finds the lowest free `<name>V{i}.js` filename, writes the new body under that versioned file, and replaces the old `skills[name]` dict in place. The vector store ends up pointing only at the newest description, but the old file stays on disk as a numbered archive. There is no dependency graph, no contradiction detection, and no explicit retirement — old skills only leave the active library by being overwritten by something the LLM chose to give the same name.

**Curriculum carries its own QA side-memory.** `CurriculumAgent` maintains `completed_tasks`, `failed_tasks`, and a `qa_cache` JSON plus a second Chroma store (`curriculum/vectordb`) keyed on self-generated questions. The curriculum agent asks Minecraft-specific QA questions, answers them with a cheaper model (`qa_model_name` defaults to `gpt-3.5-turbo`), caches both, and uses similarity over the cache to build per-task context. This is a second promotion target parallel to the skill library — text-shaped world knowledge for prompt context, distinct from executable skills for behaviour.

**Nothing cross-world is indexed.** Persistence is filesystem-under-`ckpt_dir`: `skills.json`, `completed_tasks.json`, `failed_tasks.json`, `qa_cache.json`, the two Chroma directories, `action/chest_memory.json`, and `EventRecorder` logs. A learned skill library is portable by copying the directory and passing `skill_library_dir`, which the README describes for zero-shot use on new Minecraft worlds. There is no server, no multi-agent coordination, no cross-run deduplication.

## Comparison with Our System

Voyager is a single-domain automatic codification loop; commonplace is a cross-domain human+agent knowledge base. The overlap is that both accumulate inspectable artifacts on the filesystem; the divergence is nearly everywhere else.

| Dimension | Voyager | Commonplace |
|---|---|---|
| Trace source | Minecraft event streams + execution errors, bounded per-task retries | Human and agent editing of notes, links, workshop artifacts |
| Learned substrate | JavaScript functions + generated descriptions, QA cache | Typed notes with frontmatter and semantic links |
| Promotion trigger | Critic LLM judges success from world state | Human curation and validation commands |
| Update style | Name-collision rewrite with version-stamped file archive | Status transitions (`seedling → current → superseded`), explicit link types |
| Unit-to-unit relations | None — library is a flat `skills.json` dict | Typed links (`extends`, `grounds`, `contradicts`, `exemplifies`) |
| Retrieval | Vector search on auto-generated descriptions, top-k=5 | Tag/type/description grep; progressive navigation via links |
| Reinjection | Code bodies injected into action-agent system prompt | Notes read on demand by agent navigating links |
| Oracle strength | LLM judge over world observations — soft but grounded in concrete state | Advisory validation, human judgment |
| Scope | One embodied domain, transferable within Minecraft | Cross-domain |
| Governance | Max iterations + max retries; no staleness, no supersession metadata | Explicit type instructions, review bundles, supersession status |
| Substrate-class bet | Executable code, not notes | Inspectable text only |

**Where Voyager is stronger.** Automatic promotion works. Voyager does not need a human to decide that a capability should enter the library — success under the critic plus a named program is enough. The split between retrieval handle (description) and reused artifact (code) is a small but effective design pattern commonplace has no direct equivalent for, because our notes are both the retrieval handle and the consumed content. And the artifact shape — executable JavaScript — is at the far end of [codification](../../notes/definitions/codification.md), something commonplace only approaches through shipped CLI commands, not through trace-derived learning.

**Where commonplace is stronger.** Voyager's skills cannot explain why they work, how they relate, or when one invalidates another. The library grows monotonically as a flat dict; the only lifecycle operation is name-collision overwrite. Commonplace's [title-as-claim](../../notes/title-as-claim-enables-traversal-as-reasoning.md) convention, typed links, and explicit status transitions carry relational and lifecycle information that Voyager's skill library does not represent. Voyager also silos knowledge per world directory; commonplace is cross-domain by default, with links as the transfer mechanism.

**The underlying divergence** is what gets trusted into the library. Voyager has a domain with cheap, repeated bounded trials and a world-state-grounded judge, so it can trust LLM-adjudicated successes directly into executable artifacts. Commonplace covers a domain where evaluation is soft and occurrence rates are low, so it cannot promote without human review. Both systems sit on the same [oracle-strength spectrum](../../notes/oracle-strength-spectrum.md), far apart on the same gradient.

## Borrowable Ideas

**Separate the retrieval handle from the reused artifact.** Voyager retrieves on a generated description and reinjects the original code. A commonplace analogue: notes could carry an auto-generated retrieval blurb (distinct from `description` frontmatter) tuned for embedding search, while the full note remains what gets loaded. This would let us tune retrieval independently of note authoring. *Needs a use case first — we do not currently run embedding search over the KB.*

**Name-collision rewrite with version-stamped archive.** When an LLM-generated artifact reuses a name, keeping the old file as `<name>V2.md` and pointing the live index at the new one preserves audit without merging. That is close to our `.replaced.<date>.md` archival pattern for reviews, but applied at sub-artifact granularity. *Ready as a framing — we already do this for reviews; the borrow is extending it to other promotion-like operations.*

**Side memory for context-assembly, distinct from the main library.** Voyager's `qa_cache` is not a skill library; it is scaffolding the curriculum agent uses to build the next task's context. Workshops in commonplace already play this role structurally ([workshop layer](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md)), but Voyager's version is more specific: a QA-shaped cache keyed on questions the agent itself asked. An analogous pattern for commonplace would be an agent-maintained FAQ file per workshop, seeded by questions that arose during the workshop. *Ready as a framing — low-cost prototype.*

**Promote only on a concrete success check that reads state, not intent.** Voyager's critic reads biome, inventory, equipment, chest observation before judging. Even though the judge is an LLM, the grounding is world state, not agent self-report. For commonplace, promotion-to-`current` could similarly require evidence drawn from the system (link-graph position, referenced-by count, validation-clean status) rather than authorial assertion. *Partially ready — needs a lightweight "evidence for promotion" convention in type instructions.*

**Treat some trace-derived learnings as codification candidates, not notes.** Voyager demonstrates that when behaviour is routine, correct, and verifiable, the right durable home is code. For commonplace the analogue is `commonplace-*` commands: when a pattern of manual note operations stabilises, it should migrate to a CLI command. *Ready as a framing — this is already our practice; Voyager sharpens the principle.*

## Curiosity Pass

**"Lifelong learning agent" markets more than the code delivers.** The repo is a research snapshot: the library grows monotonically within a run, skills are never retired or consolidated, and the critic is an LLM reading observations. What is genuinely "lifelong" is that the skill library directory can be carried to a new Minecraft world (`skill_library_dir` in the README) and provide callable competence there. What is not lifelong is self-correction: Voyager has no mechanism to notice that skill A and skill B overlap, that one supersedes another, or that a skill that worked in world X fails in world Y.

**The retrieval abstraction is thinner than it looks.** Descriptions are generated by calling the model with `load_prompt("skill")` over the program code, stored as formatted strings (`async function <name>(bot) { // <description> }`), and embedded into Chroma. They have no relation to each other, no tags, no typing. `retrieve_skills` is plain top-k cosine similarity over description embeddings. The library compounds capability, but its internal structure is a vector index plus a flat JSON dict.

**The critic is load-bearing but lightweight.** `check_task_success` builds a prompt from world observations and asks the LLM to return `{success, critique}` JSON, retrying up to 5 times on parse failure. There is no cross-check, no state oracle, no deterministic verifier. In a tight scenario (`craft_wooden_pickaxe` → inventory contains wooden pickaxe), the LLM judge is almost certainly right. In ambiguous scenarios the judgment is soft. The paper's impressive numbers depend on the assumption that this judge is reliable enough at the tasks the curriculum agent picks. Commonplace would call this a soft oracle and not promote unilaterally on it.

**The library's ceiling is domain breadth, not quality.** Voyager demonstrates that trace-derived-code-learning works in a single embodied domain with cheap bounded trials and a world-state judge. It does not demonstrate anything about domains that lack those properties. The repo's strength is the end-to-end pipeline; its generality claim is weaker than the pipeline itself.

**Two LangChain imports are the whole vector layer.** `Chroma` (two collections) plus `OpenAIEmbeddings`. The review-worthy detail is not the technology but that the system treats retrieval as a trivial subsystem — the interesting work happens in the prompts, the role split, and the critic. That is a useful calibration: the vector store is not the thing, it is plumbing.

**Trace-derived learning placement.** Voyager's *trace source* is per-task Minecraft event rollouts — typed events including `onChat`, `onError`, and `observe` (biome, blocks, entities, health, hunger, position, equipment, inventory, chests) recorded by `EventRecorder` and accumulated inside `voyager.step` during each attempt. Trigger boundaries are per-rollout for promotion (one successful reusable rollout = one skill addition, except explicitly non-reusable housekeeping tasks such as chest-deposit cleanup) and per-task for curriculum updates. *Extraction* pulls out three distinct things: the JavaScript `program_code` + `program_name` returned by the action agent on success, a natural-language skill description generated post-hoc from the code by a cheaper model, and QA-cached world knowledge (Q/A pairs produced by the curriculum agent). The *oracle* deciding what is signal is the `CriticAgent` LLM judge reading world state — a soft oracle with strong grounding. *Promotion target* is inspectable symbolic artifacts only: JavaScript files plus a JSON manifest plus two Chroma collections on disk. No weights are trained; no service-owned memory. *Scope* is per-Minecraft-world in practice, with the README documenting directory-level transfer to new worlds as the cross-task generalisation path. *Timing* is online during deployment — promotion happens live inside the running `learn()` loop, one skill at a time, with no offline consolidation or replay.

On the [survey's axes](../trace-derived-learning-techniques-in-related-systems.md): axis 1 is trajectory-run ingestion (repeated bounded task attempts, not live conversations, not open-ended service event streams). Axis 2 is inspectable symbolic artifacts — squarely one-sided, not split like autocontext. Within axis 2's structure spectrum, Voyager occupies the extreme *executable-code* end, contrasting with ACE/ExpeL's flat-rule artifacts and Reflexion's minimal verbal hints. Voyager strengthens the survey's framing that artifact structure varies over orders of magnitude within one substrate-class; it does not warrant a new subtype, but it remains the clearest reference case for trajectory-to-code promotion.

## What to Watch

- Whether descendants keep the critic-gated promotion discipline but harden the oracle — deterministic world-state checks instead of LLM judges, or ensembles of checks.
- Whether later systems in the same lineage add lifecycle mechanics absent here (dependency tracking between skills, retirement on repeated failure, contradiction detection) or keep the flat-accumulation shape.
- Whether executable-artifact promotion transfers beyond embodied domains with hard environmental feedback — e.g. trace-derived codification in software engineering or data analysis agents.
- Whether the QA sidecar evolves into a richer world model that shapes curriculum and retrieval more deeply, or remains a prompt-scaffolding cache.
- Whether LangChain's API drift (0.0.x-era imports like `langchain.chat_models`, `langchain.vectorstores`, `langchain.embeddings.openai`) forces a rewrite or the repo stays pinned — the code is functionally frozen at GPT-4-era dependencies.

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: Voyager is the reference case for trajectory-to-executable-artifact promotion, occupying the code end of the artifact structure spectrum
- [codification](../../notes/definitions/codification.md) — exemplifies: successful LLM-guided behaviour is automatically hardened into executable JavaScript functions, the far end of codifying natural-language competence
- [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) — exemplifies: the critic is an LLM judge reading concrete world state — softer than deterministic verifiers, harder than agent self-report
- [the-boundary-of-automation-is-the-boundary-of-verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — exemplifies: Voyager can automate promotion because the Minecraft domain provides cheap bounded trials plus observable world state; the boundary of the critic is the boundary of what gets into the library
- [deploy-time-learning-is-the-missing-middle](../../notes/deploy-time-learning-is-the-missing-middle.md) — extends: skill-library accumulation is deploy-time learning via artifact promotion, without weight modification, driven entirely by in-the-loop critic judgment
- [substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated](../../notes/substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md) — exemplifies: substrate-class is symbolic artifacts (not weights); backend is filesystem + Chroma; artifact form is executable JavaScript — three clearly separable choices
- [autocontext](./autocontext.md) — compares: both accumulate across repeated trajectories, but autocontext produces typed lessons and playbooks (and optionally weights) while Voyager produces executable code only
- [expel](./expel.md) — contrasts: both consolidate across runs, but ExpeL maintains natural-language rules with explicit edit/merge/remove operations while Voyager flat-accumulates code with only name-collision overwrite

---
description: "Coverage-planning note mapping the Adaptation of Agentic AI survey's memory and skill systems to existing KB reviews and candidate additions"
type: kb/types/note.md
traits: [has-external-sources]
tags: [related-systems, agent-memory, trace-derived]
status: seedling
---

# Adaptation survey review candidates

[Adaptation of Agentic AI](../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md) is useful as a source-discovery checklist for this collection. The review queue should not mirror the whole paper: most A1/A2 post-training methods, generic RAG methods, and static T1 tools are outside the agent-memory-system review boundary. The relevant slice is the survey's T2 memory and skill material: systems where a fixed agent gains future capacity through an external memory, workflow, skill, or tool substrate.

## Already Covered

The survey's central examples overlap substantially with existing coverage. [Reflexion](./reviews/reflexion.md), [ExpeL](./reviews/expel.md), [Voyager](./reviews/voyager.md), [Dynamic Cheatsheet](./reviews/dynamic-cheatsheet.md), and [ReasoningBank](./reviews/reasoning-bank.md) already cover the reflective, executable-skill, and test-time-artifact-learning branch. [AgentFly](./reviews/AgentFly.md) covers Memento/AgentFly's case-memory and trained selector path. [OS-Copilot](./reviews/OS-Copilot.md) covers FRIDAY's generated executable tool library. [Agent Workflow Memory](./reviews/agent-workflow-memory.md) covers AWM directly. [HippoRAG](./reviews/HippoRAG.md) covers the graph-retrieval baseline.

The database-backed memory cluster has lightweight or adjacent coverage: [Letta/MemGPT](./README.md), [Mem0](./README.md), [Graphiti/Zep](./README.md), [A-MEM](../sources/a-mem-agentic-memory-for-llm-agents.ingest.md), and [AgeMem](./source-only/agemem.md) are already visible in the index or source-only layer. [Cognee](./reviews/cognee.md), [CrewAI Memory](./reviews/crewai-memory.md), [Memori](./reviews/Memori.md), [Hindsight](./reviews/hindsight.md), and [xMemory](./reviews/xMemory.md) cover nearby production or research-code implementations even when they are not the survey's headline examples.

## Deduped Review Queue

**MemoryOS** should get the next repo-backed review. It is the strongest missing OS-metaphor memory architecture: short-term, mid-term, and long-term memory tiers with explicit storage, update, retrieval, and generation modules. It is the cleanest architectural counterpoint to Letta/MemGPT and to the requirements map's context-engineering framing. Candidate source: `BAI-LAB/MemoryOS`.

**MemSkill** should be reviewed if the public code is complete enough. It reframes memory operations themselves as skills: a controller selects memory skills, an executor applies them, and a designer evolves the skill set after failures. This directly tests our claim that the important question is not just where optimization happens, but what drives the decision to transform experience into memory. Candidate source: `zjunlp/SkillX`; `ViktorAxelsen/MemSkill` exists but needs official/mirror verification.

**SkillWeaver** should get a repo-backed review as the strongest missing web-agent executable-skill system. Voyager covers Minecraft code skills and OS-Copilot covers OS-level generated tools; SkillWeaver covers website-specific API skill synthesis, practice, refinement, and sharing. Candidate source: `OSU-NLP-Group/SkillWeaver`.

**SAGE (Skill Augmented GRPO)** should get a disambiguated review if we want the RL-with-skill-library branch. It is distinct from the existing [SAGE](./reviews/sage.md) review and specifically tests skill-integrated reward over sequential rollouts. Candidate source: `amazon-science/SAGE`.

**AriGraph** should get a repo-backed review if graph world-model memory becomes a priority. HippoRAG covers graph retrieval over corpora; AriGraph is more agentic because the graph is built while an agent explores an environment and mixes semantic and episodic memory. Candidate source: `AIRI-Institute/AriGraph`.

**Agent S** is the best single candidate if we want one more computer-use memory/experience system after OS-Copilot. It focuses on experience-augmented hierarchical planning rather than generated tool libraries, so it would not duplicate OS-Copilot directly. Candidate source: `simular-ai/Agent-S`.

## Lower-Priority Or Sample-Only

**Cradle**, **AppAgent/AppAgentX**, **AgentStore**, and **ExACT** should not all be reviewed unless computer-use agents become a focused survey. They are useful samples, but OS-Copilot already covers the most relevant executable-skill-library branch. Pick one only when it adds a new artifact substrate: generated app documentation (AppAgent), specialist-agent registry (AgentStore), or search/trajectory training rather than durable memory (ExACT).

**ChatDB**, **MemoryBank/SiliconFriend**, **MemoChat**, and **ReadAgent** are historical or baseline memory systems. Review them only if we need lineage coverage for database-as-symbolic-memory, conversational long-term memory, memo-tuned models, or gist-memory reading. They are lower priority than MemoryOS, MemSkill, SkillWeaver, SAGE, AriGraph, and Agent S because they are less directly about governed agent memory artifacts.

**PAE**, **LATM**, and **ADAS** are adjacent rather than first-order memory-system reviews. PAE is mostly policy/RL skill acquisition; LATM is tool making; ADAS is agent-architecture search. They belong in this collection only if the scope expands from memory systems to broader adaptation/tooling systems.

## Lower-Priority Or Source-Only

Generative Agents, MemoryBank, ReadAgent, and MemoChat are useful historical baselines but lower review priority unless we need lineage coverage. Several structured-memory examples in the survey, such as AriGraph, ChatDB, SHIMI, and tree-memory systems, may deserve source-only notes if no current, inspectable repository is available. Zep itself should be handled through Graphiti/Zep coverage rather than creating a separate thin note unless the commercial architecture changes the memory model in a way Graphiti does not expose.

The survey also names **SAGE** as an RL-based skill-library system, but this should not be treated as covered by the existing [SAGE](./reviews/sage.md) review. That review covers a different BFT-branded memory system. If the survey's SAGE becomes relevant, use a disambiguated title.

## Practical Queue

1. MemoryOS - highest-value missing architecture review.
2. MemSkill - highest-value missing memory-operations-as-skills review; verify official repo first.
3. SkillWeaver - strongest missing executable web-skill library.
4. SAGE (Skill Augmented GRPO) - RL skill-library branch; disambiguate filename from existing `sage.md`.
5. AriGraph - agent-built episodic/semantic graph memory, complementary to HippoRAG.
6. Agent S - experience-augmented computer-use planning, if one more computer-use system is needed.

## Resolved Repository Addresses

High-priority candidates:

| System | Repository | Note |
|---|---|---|
| Memento / AgentFly | https://github.com/Agent-on-the-Fly/AgentFly | Official code for "Memento: Fine-tuning LLM Agents without Fine-tuning LLMs." |
| MemoryOS | https://github.com/BAI-LAB/MemoryOS | Official code for "Memory OS of AI Agent." |
| MemSkill | https://github.com/zjunlp/SkillX | Paper-announced code location; verify public completeness before review. |
| MemSkill candidate | https://github.com/ViktorAxelsen/MemSkill | Public repo matching the paper title; verify whether this is official or a mirror before using. |
| OS-Copilot / FRIDAY | https://github.com/OS-Copilot/OS-Copilot | Former FRIDAY URL redirects here. |
| Agent Workflow Memory | https://github.com/zorazrw/agent-workflow-memory | Candidate official repo for AWM. |
| HippoRAG | https://github.com/OSU-NLP-Group/HippoRAG | Candidate graph-retrieval baseline. |

Additional survey systems with reachable repos:

| System | Repository | Note |
|---|---|---|
| Cradle | https://github.com/BAAI-Agents/Cradle | General computer-control agent with memory and skill curation. |
| AppAgent | https://github.com/TencentQQGYLab/AppAgent | Smartphone-use agent; generated app documentation is the durable memory surface. |
| AppAgentX | https://github.com/Westlake-AGI-Lab/AppAgentX | Later evolving-GUI-agent variant. |
| Agent S | https://github.com/simular-ai/Agent-S | Computer-use agent with experience-augmented hierarchical planning. |
| AgentStore | https://github.com/chengyou-jia/AgentStore | Registry of specialist agents with meta-agent selection. |
| ExACT | https://github.com/Agent-E3/ExACT | Public repo forked from `microsoft/ExACT`; verify branch coverage before review. |
| SkillWeaver | https://github.com/OSU-NLP-Group/SkillWeaver | Web-agent skill synthesis into reusable APIs. |
| PAE | https://github.com/amazon-science/PAE | Proposer-Agent-Evaluator implementation for autonomous skill discovery. |
| SAGE (Skill Augmented GRPO) | https://github.com/amazon-science/SAGE | Distinct from the existing reviewed `SAGE` memory system. |
| AriGraph | https://github.com/AIRI-Institute/AriGraph | Episodic + semantic knowledge-graph memory for text-game agents. |
| ChatDB | https://github.com/huchenxucs/ChatDB | Database-as-symbolic-memory baseline. |
| MemoChat | https://github.com/LuJunru/MemoChat | Memo-tuned conversational memory model. |
| MemoryBank / SiliconFriend | https://github.com/zhongwanjun/MemoryBank-SiliconFriend | Historical long-term conversational memory baseline. |
| ReadAgent | https://github.com/read-agent/read-agent.github.io | Project-page repo with demo notebook/prompts rather than full package-style implementation. |
| LATM | https://github.com/ctlllll/LLM-ToolMaker | Large Language Models as Tool Makers implementation. |
| ADAS | https://github.com/ShengranHu/ADAS | Meta-agent search over agent architectures; adjacent rather than memory-specific. |

No reliable public repository found in this pass:

- LEGOMem - Microsoft Research page and arXiv paper found, but no code link surfaced.
- CASCADE - arXiv paper found, no code link surfaced.
- SHIMI - arXiv paper found, no code link surfaced.
- CREATOR - paper found, but no clearly official repo surfaced.

---

Relevant Notes:

- [Adaptation of Agentic AI ingest](../sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md) - source checklist: survey that surfaced these candidates
- [Designing a Memory System for LLM-Based Agents](../notes/designing-agent-memory-systems.md) - rationale: candidate reviews should improve the requirements map, not just broaden bibliography
- [The adaptation survey corroborates memory requirements but misses artifact-role governance](../notes/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) - companion: terminology translation for reading the survey
- [Trace-derived learning techniques in related systems](./trace-derived-learning-techniques-in-related-systems.md) - placement: many candidates belong in the trace-derived learning landscape

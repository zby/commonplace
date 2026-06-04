---
description: "Auto-generated sortable comparison table of the code-reviewed agent memory systems across the matrix fields filled reliably enough to compare — storage substrate, read-back direction, engineered push, and trace-derived learning. Rebuild with scripts/render_systems_table.py."
type: kb/types/note.md
traits: [has-comparison]
tags: [agent-memory]
status: current
---

# Agent memory systems comparison table

A sortable view of the code-reviewed systems in this collection, generated from
[`systems.csv`](./systems.csv). Lightweight (doc-only) reviews are excluded — a
comparison table is for *choosing* a system, and that calls for code-grounded
evidence. Click any column header to sort (in the rendered HTML site; on GitHub
the [raw matrix](./systems.csv) is itself a sortable, searchable viewer).

For the architectural deep dive behind these axes, see the
[comparative review](./agentic-memory-systems-comparative-review.md).

## How to read the columns

- **Storage substrate** — where memory physically lives: plain files, a git repo,
  SQLite, an RDBMS, a vector or graph store, key-value, in-memory, or model
  weights. It sets the operational floor — inspectability and diffability at one
  end, scale and query power at the other. Files-family still leads, but a third
  of systems are database-backed, and the most common database is plain SQLite,
  not a vector or graph store.
- **Read-back** — how remembered material reaches the next action: the agent
  *pulls* it with an explicit lookup, the system *pushes* it in unasked, or
  *both*. This is the first question to ask, because it decides whether the agent
  has to remember to look or whether context arrives on its own.
- **Push engineered** — whether the system has actually built a relevance-gated
  path that injects memory *before* the agent acts. Pull-only systems never have
  one by definition; about half of all systems do.
- **Trace-derived** — whether memory is mined automatically from the agent's own
  execution traces rather than authored by hand. It trades throughput for
  reviewability. Most systems are trace-derived — and they overwhelmingly push or
  do both, so automatic learning and automatic activation tend to ship together.

Representational form is omitted from this compact view while the component
one-hot retrofit proceeds. The raw matrix carries `form_prose`, `form_symbolic`,
and `form_parametric` columns.


## The systems (129 code-reviewed)

| System | Storage substrate | Read-back | Push engineered | Trace-derived |
|---|---|---|---|---|
| [A-mem](./reviews/a-mem.md) | vector | pull | no | no |
| [ACE](./reviews/ace.md) | in-memory | push | no | yes |
| [Agent Skills for Context Engineering](./reviews/agent-skills-for-context-engineering.md) | repo | pull | no | yes |
| [Agent Workflow Memory](./reviews/agent-workflow-memory.md) | files | push | yes | yes |
| [Agent-R](./reviews/agent-r.md) | model-weights | push | no | yes |
| [Agent-S](./reviews/Agent-S.md) | files | push | yes | yes |
| [AgentFly](./reviews/AgentFly.md) | files | push | yes | yes |
| [Agentic Harness Engineering](./reviews/agentic-harness-engineering.md) | repo | both | yes | yes |
| [Agentic Local Brain](./reviews/agentic-local-brain.md) | sqlite | both | yes | yes |
| [AI Context OS](./reviews/AI-Context-OS.md) | files | both | yes | yes |
| [ai-memex-cli](./reviews/ai-memex-cli.md) | files | both | no | yes |
| [ai-modules](./reviews/theafh--ai-modules.md) | repo | pull | no | yes |
| [Archie](./reviews/archie.md) | repo | pull | no | no |
| [AriGraph](./reviews/AriGraph.md) | in-memory | push | yes | no |
| [ARIS / Auto-claude-code-research-in-sleep](./reviews/Auto-claude-code-research-in-sleep.md) | files | both | yes | yes |
| [Ars Contexta](./reviews/arscontexta.md) | files | both | yes | yes |
| [Atomic](./reviews/atomic.md) | sqlite | both | yes | no |
| [auto-harness](./reviews/auto-harness.md) | files | both | no | yes |
| [Autocontext](./reviews/autocontext.md) | sqlite | both | yes | yes |
| [Awesome Agent Memory](./reviews/Awesome-Agent-Memory.md) | files | pull | no | no |
| [Basic Memory](./reviews/basic-memory.md) | files | both | yes | yes |
| [beever-atlas](./reviews/beever-atlas.md) | vector | both | yes | yes |
| [Binder](./reviews/binder.md) | sqlite | pull | no | no |
| [browzy.ai](./reviews/browzy-ai.md) | sqlite | push | yes | yes |
| [byterover-cli](./reviews/byterover-cli.md) | files | pull | no | yes |
| [cass_memory_system](./reviews/cass_memory_system.md) | files | both | yes | yes |
| [Claude Context Guard](./reviews/claude-context-guard.md) | repo | both | no | yes |
| [claude-obsidian](./reviews/claude-obsidian.md) | files | both | yes | yes |
| [clawvault](./reviews/clawvault.md) | files | both | yes | yes |
| [Closure-SDK](./reviews/Closure-SDK.md) | in-memory | pull | no | no |
| [Clude](./reviews/cludebot.md) | sqlite | both | yes | yes |
| [CocoIndex](./reviews/cocoindex.md) | files | pull | no | no |
| [Cognee](./reviews/cognee.md) | rdbms | both | yes | yes |
| [compound-engineering-plugin](./reviews/compound-engineering-plugin.md) | repo | both | yes | yes |
| [Context Constitution](./reviews/context-constitution.md) | files | both | no | no |
| [Continuity](./reviews/continuity.md) | sqlite | both | no | yes |
| [CORAL](./reviews/CORAL.md) | files | both | yes | yes |
| [Cortex](./reviews/cortex.md) | graph | pull | no | yes |
| [cq](./reviews/cq.md) | sqlite | pull | no | yes |
| [CrewAI Memory](./reviews/crewai-memory.md) | vector | both | yes | yes |
| [Decapod](./reviews/decapod.md) | files | pull | no | yes |
| [dense-mem](./reviews/dense-mem.md) | graph | pull | no | yes |
| [DocMason](./reviews/docmason.md) | files | both | yes | yes |
| [Dynamic Cheatsheet](./reviews/dynamic-cheatsheet.md) | in-memory | push | yes | yes |
| [Echel](./reviews/echel.md) | files | both | yes | no |
| [Engraph](./reviews/engraph.md) | files | pull | no | no |
| [EQUIPA](./reviews/equipa.md) | sqlite | both | yes | yes |
| [Exocomp](./reviews/exocomp.md) | files | both | no | no |
| [ExpeL](./reviews/expel.md) | files | both | yes | yes |
| [Funes](./reviews/funes.md) | repo | pull | no | no |
| [G-Memory](./reviews/g-memory.md) | vector | push | yes | yes |
| [GBrain](./reviews/gbrain.md) | rdbms | both | yes | yes |
| [getsentry/skills](./reviews/getsentry-skills.md) | files | pull | no | no |
| [Gnosis](./reviews/gnosis.md) | files | pull | no | yes |
| [Graphiti](./reviews/graphiti.md) | graph | pull | no | yes |
| [Halo](./reviews/halo.md) | files | pull | no | yes |
| [Hindsight](./reviews/hindsight.md) | rdbms | both | yes | yes |
| [HippoRAG](./reviews/HippoRAG.md) | files | pull | no | no |
| [hyalo](./reviews/hyalo.md) | files | pull | no | no |
| [HyperAgents](./reviews/hyperagents.md) | files | push | yes | yes |
| [interview-doc-agent](./reviews/interview-doc-agent.md) | files | pull | no | no |
| [KBLaM](./reviews/KBLaM.md) | model-weights | push | yes | no |
| [Kompl](./reviews/Kompl.md) | sqlite | both | yes | yes |
| [LACP](./reviews/lacp.md) | files | both | yes | yes |
| [Letta](./reviews/letta.md) | rdbms | both | yes | yes |
| [LLM Wiki (kenhuangus)](./reviews/kenhuangus--llm-wiki.md) | files | pull | no | yes |
| [LLM Wiki (MehmetGoekce)](./reviews/MehmetGoekce--llm-wiki.md) | files | both | no | no |
| [LLM Wiki (nvk)](./reviews/llm-wiki.md) | files | pull | no | yes |
| [llm-context-base](./reviews/llm-context-base.md) | files | both | no | yes |
| [llm-project-wiki](./reviews/llm-project-wiki.md) | repo | pull | no | no |
| [llm-wiki](./reviews/Pratiyush--llm-wiki.md) | model-weights | pull | no | yes |
| [llm-wiki-coordination](./reviews/llm-wiki-coordination.md) | repo | pull | no | yes |
| [Mem0](./reviews/mem0.md) | vector | both | yes | yes |
| [Memex](./reviews/memex.md) | files | pull | no | no |
| [Memori](./reviews/Memori.md) | service-object | both | yes | yes |
| [MemoryOS](./reviews/MemoryOS.md) | vector | both | yes | yes |
| [MemPalace](./reviews/mempalace.md) | vector | pull | no | yes |
| [MentisDB](./reviews/mentisdb.md) | model-weights | both | no | no |
| [Meta-Harness](./reviews/meta-harness.md) | files | pull | no | yes |
| [MiroShark](./reviews/MiroShark.md) | graph | both | yes | yes |
| [nao](./reviews/nao.md) | repo | both | no | yes |
| [napkin](./reviews/napkin.md) | files | pull | no | no |
| [Nuggets](./reviews/nuggets.md) | files | both | yes | yes |
| [o-o](./reviews/o-o.md) | files | pull | no | no |
| [OpenClerk](./reviews/openclerk.md) | sqlite | pull | no | no |
| [OpenSage](./reviews/OpenSage.md) | files | both | yes | yes |
| [OpenViking](./reviews/openviking.md) | files | both | yes | yes |
| [Operational Ontology Framework](./reviews/operational-ontology-framework.md) | files | pull | no | no |
| [Origin](./reviews/origin.md) | sqlite | both | yes | yes |
| [OS-Copilot](./reviews/OS-Copilot.md) | vector | push | yes | yes |
| [Pal](./reviews/pal.md) | rdbms | both | yes | no |
| [Phantom](./reviews/phantom.md) | vector | both | yes | yes |
| [pi-self-learning](./reviews/pi-self-learning.md) | service-object | both | no | yes |
| [playground](./reviews/playground.md) | files | both | yes | no |
| [Quicky Wiki](./reviews/quicky-wiki.md) | sqlite | pull | no | no |
| [ReasoningBank](./reviews/reasoning-bank.md) | files | both | yes | yes |
| [Reflexion](./reviews/reflexion.md) | in-memory | push | yes | yes |
| [REM](./reviews/REM.md) | graph | both | yes | yes |
| [SAGE](./reviews/amazon-science--SAGE.md) | files | push | yes | yes |
| [sage](./reviews/sage.md) | kv | push | yes | yes |
| [sage-wiki](./reviews/sage-wiki.md) | sqlite | pull | no | yes |
| [Secure LLM-Wiki](./reviews/secure-llm-wiki.md) | repo | push | no | no |
| [Self-Training-LLM](./reviews/Self-Training-LLM.md) | model-weights | push | no | yes |
| [Semiont](./reviews/semiont.md) | files | both | yes | yes |
| [sift-kg](./reviews/sift-kg.md) | files | pull | no | no |
| [Siftly](./reviews/siftly.md) | sqlite | pull | no | no |
| [Signet AI](./reviews/signetai.md) | sqlite | both | yes | yes |
| [SkillNote](./reviews/skillnote.md) | rdbms | both | yes | yes |
| [SkillWeaver](./reviews/SkillWeaver.md) | files | both | yes | yes |
| [SkillX](./reviews/SkillX.md) | in-memory | both | yes | yes |
| [Spacebot](./reviews/spacebot.md) | sqlite | both | yes | yes |
| [Sparks](./reviews/sparks.md) | files | pull | no | no |
| [Stash](./reviews/stash.md) | rdbms | pull | no | yes |
| [supermemory](./reviews/supermemory.md) | service-object | both | yes | yes |
| [Synapptic](./reviews/synapptic.md) | files | push | yes | yes |
| [Synthadoc](./reviews/synthadoc.md) | files | pull | no | no |
| [Tendril](./reviews/tendril.md) | files | pull | no | no |
| [Thalo](./reviews/thalo.md) | files | both | yes | no |
| [TheKnowledge](./reviews/TheKnowledge.md) | files | both | yes | yes |
| [Tolaria](./reviews/tolaria.md) | repo | both | yes | no |
| [tracecraft](./reviews/tracecraft.md) | files | pull | no | no |
| [Virtual Context](./reviews/virtual-context.md) | sqlite | both | yes | yes |
| [VLM-wiki](./reviews/VLM-wiki.md) | files | pull | no | no |
| [Voiden](./reviews/voiden.md) | files | pull | no | no |
| [Voyager](./reviews/voyager.md) | files | push | yes | yes |
| [WeKnora](./reviews/WeKnora.md) | rdbms | both | yes | yes |
| [WUPHF](./reviews/wuphf.md) | repo | both | yes | yes |
| [xMemory](./reviews/xMemory.md) | vector | both | yes | yes |
| [Zikkaron](./reviews/Zikkaron.md) | sqlite | both | yes | yes |

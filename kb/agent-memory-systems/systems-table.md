---
description: "Auto-generated sortable comparison table of the code-reviewed agent memory systems across the matrix fields filled reliably enough to compare — storage substrate, read-back direction, read-back signal (coarse vs instance targeting), trace-derived learning, behavioral authority, and curation operations. Rebuild with scripts/render_systems_table.py."
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
- **Read-back signal** — *how* a push selects what to inject: `coarse` (always-load /
  session-start, generic recall) versus an `instance` signal — an `identifier` match
  or `inferred` relevance (lexical / embedding / judgment). An instance signal *is* a
  targeted push; coarse is not; pull-only shows none. Targeting lives here, in one
  place — there is no separate "engineered push" flag.
- **Trace-derived** — whether memory is mined automatically from the agent's own
  execution traces rather than authored by hand. It trades throughput for
  reviewability. Most systems are trace-derived — and they overwhelmingly push or
  do both, so automatic learning and automatic activation tend to ship together.
- **Authority** — with what force the stored memory acts on the agent, beyond the
  baseline. Every system carries *knowledge* authority and nearly all add
  *instruction* and *routing*, so those are assumed and omitted; the cell shows
  only the discriminating modes: *enforce* (a hard gate the agent can't ignore),
  *validate* (checks writes against rules), *rank* (influences retrieval order),
  and *learn* (feeds back into the system's own behavior). A dash means
  advisory-only — knowledge and instruction, nothing stronger.
- **Curation** — which upkeep operations the system runs over stored memory.
  *Synthesize* and *promote* are near-universal and omitted; the cell shows the
  discriminating ops: *consolidate* (merge related entries), *dedup* (drop
  duplicates), *evolve* (rewrite entries in place), *invalidate* (mark stale),
  and *decay* (age out by time or use). A dash means write-once memory with no
  active upkeep.

Representational form is omitted from this compact view while the component
one-hot retrofit proceeds. The raw matrix carries `form_prose`, `form_symbolic`,
and `form_parametric` columns. The full agency and curation flag sets — including
the near-universal modes assumed away above — also live in the raw matrix.


## The systems (125 code-reviewed)

| System | Storage substrate | Read-back | Read-back signal | Trace-derived | Authority | Curation |
|---|---|---|---|---|---|---|
| [A-mem](./reviews/a-mem.md) | in-memory | pull | — | no | rank+learn | evolve |
| [ACE](./reviews/ace.md) | files | push | coarse | yes | rank+learn | dedup+evolve |
| [Agent Skills for Context Engineering](./reviews/agent-skills-for-context-engineering.md) | files | pull | — | no | validate+rank+learn | — |
| [Agent Workflow Memory](./reviews/agent-workflow-memory.md) | files | push | coarse+identifier | yes | validate+rank+learn | consolidate+dedup |
| [Agent-R](./reviews/agent-r.md) | model-weights | push | coarse | yes | validate+rank+learn | — |
| [Agent-S](./reviews/Agent-S.md) | files | both | coarse+inferred-embedding | yes | validate+rank+learn | — |
| [Agentic Local Brain](./reviews/agentic-local-brain.md) | sqlite | both | coarse+inferred-lexical+inferred-embedding+inferred-judgment | yes | rank+learn | consolidate+dedup+evolve |
| [AI-Context-OS](./reviews/AI-Context-OS.md) | files | both | coarse+identifier+inferred-lexical | yes | validate+rank+learn | — |
| [ai-memex-cli](./reviews/ai-memex-cli.md) | files | both | coarse | yes | validate+rank+learn | consolidate |
| [ai-modules](./reviews/theafh--ai-modules.md) | files | pull | — | yes | enforce+validate+learn | consolidate+dedup+invalidate |
| [Amazon Science SAGE](./reviews/amazon-science--SAGE.md) | files | push | identifier+inferred-lexical+inferred-embedding | no | enforce+validate+rank+learn | dedup |
| [Ars Contexta](./reviews/arscontexta.md) | files | both | coarse | yes | enforce+validate+rank+learn | dedup+evolve+invalidate |
| [Atomic](./reviews/atomic.md) | sqlite | both | identifier+inferred-lexical+inferred-embedding | no | validate+rank+learn | consolidate+dedup+evolve |
| [Auto-claude-code-research-in-sleep](./reviews/Auto-claude-code-research-in-sleep.md) | files | both | coarse | yes | enforce+validate+rank+learn | consolidate+invalidate |
| [auto-harness](./reviews/auto-harness.md) | files | both | coarse+identifier | yes | enforce+validate+learn | consolidate+evolve |
| [Autocontext](./reviews/autocontext.md) | files | both | coarse+identifier+inferred-lexical | yes | enforce+validate+rank+learn | consolidate+dedup+invalidate |
| [Awesome Agent Memory](./reviews/Awesome-Agent-Memory.md) | repo | pull | — | no | rank | — |
| [Basic Memory](./reviews/basic-memory.md) | files | both | coarse+identifier | yes | validate+rank+learn | — |
| [Beever Atlas](./reviews/beever-atlas.md) | vector | pull | — | yes | validate+rank+learn | consolidate+dedup+evolve+invalidate |
| [Binder](./reviews/binder.md) | sqlite | pull | — | no | enforce+validate | consolidate+invalidate |
| [browzy.ai](./reviews/browzy-ai.md) | files | push | coarse+inferred-lexical | yes | validate+rank+learn | consolidate+evolve |
| [byterover-cli](./reviews/byterover-cli.md) | files | both | coarse | yes | validate+rank+learn | decay |
| [cass_memory_system](./reviews/cass_memory_system.md) | files | both | coarse+inferred-lexical | yes | enforce+validate+rank+learn | dedup+evolve+invalidate+decay |
| [Claude Context Guard](./reviews/claude-context-guard.md) | files | both | coarse+identifier | yes | validate | invalidate+decay |
| [claude-obsidian](./reviews/claude-obsidian.md) | files | both | coarse | yes | enforce+validate+rank+learn | consolidate |
| [ClawVault](./reviews/clawvault.md) | files | both | coarse+inferred-lexical+inferred-embedding | yes | enforce+validate+rank+learn | consolidate+dedup+invalidate+decay |
| [Closure-SDK](./reviews/Closure-SDK.md) | files | pull | — | no | enforce+validate+rank+learn | consolidate+evolve+decay |
| [Clude](./reviews/cludebot.md) | sqlite | both | coarse+inferred-lexical+inferred-embedding | yes | enforce+validate+rank+learn | consolidate+dedup+evolve+invalidate+decay |
| [CocoIndex](./reviews/cocoindex.md) | files | pull | — | no | validate+rank | — |
| [Cognee](./reviews/cognee.md) | graph | both | coarse+inferred-lexical+inferred-embedding | yes | validate+rank+learn | consolidate+evolve |
| [Compound Engineering Plugin](./reviews/compound-engineering-plugin.md) | repo | both | coarse+identifier+inferred-lexical | yes | enforce+validate+learn | consolidate+dedup+invalidate |
| [Context Constitution](./reviews/context-constitution.md) | files | pull | — | no | validate | — |
| [Continuity](./reviews/continuity.md) | sqlite | both | coarse | yes | validate+rank+learn | consolidate+evolve |
| [CORAL](./reviews/CORAL.md) | files | both | coarse+identifier | yes | enforce+validate+rank+learn | — |
| [Cortex](./reviews/cortex.md) | graph | pull | — | yes | enforce+validate+rank+learn | evolve+invalidate+decay |
| [cq](./reviews/cq.md) | sqlite | pull | — | yes | enforce+validate+rank+learn | evolve+invalidate |
| [CrewAI Memory](./reviews/crewai-memory.md) | vector | both | inferred-embedding+inferred-judgment | yes | enforce+rank+learn | consolidate+dedup+evolve |
| [Decapod](./reviews/decapod.md) | files | pull | — | yes | enforce+validate+rank+learn | consolidate+dedup+invalidate+decay |
| [dense-mem](./reviews/dense-mem.md) | graph | pull | — | yes | enforce+validate+rank+learn | dedup+invalidate |
| [DocMason](./reviews/docmason.md) | files | both | inferred-lexical | yes | enforce+validate+rank+learn | — |
| [Dynamic Cheatsheet](./reviews/dynamic-cheatsheet.md) | in-memory | push | coarse+inferred-embedding | yes | rank+learn | consolidate+dedup+evolve |
| [Echel](./reviews/echel.md) | files | both | coarse+identifier | no | enforce+validate+rank | consolidate |
| [Engraph](./reviews/engraph.md) | files | pull | — | no | enforce+validate+rank+learn | — |
| [EQUIPA](./reviews/equipa.md) | sqlite | both | identifier+inferred-lexical+inferred-embedding | yes | validate+rank+learn | dedup+evolve+invalidate+decay |
| [Exocomp](./reviews/exocomp.md) | files | both | coarse | no | enforce+validate | — |
| [ExpeL](./reviews/expel.md) | files | both | coarse+identifier+inferred-embedding | yes | validate+rank+learn | dedup+evolve |
| [Funes](./reviews/funes.md) | repo | pull | — | no | validate | consolidate+dedup |
| [G-Memory](./reviews/g-memory.md) | vector | push | inferred-embedding+inferred-judgment | no | rank+learn | consolidate+dedup+evolve |
| [GBrain](./reviews/gbrain.md) | rdbms | both | coarse+identifier+inferred-lexical+inferred-embedding+inferred-judgment | yes | enforce+validate+rank+learn | consolidate+dedup+evolve+invalidate+decay |
| [getsentry/skills](./reviews/getsentry-skills.md) | repo | pull | — | no | enforce+validate | — |
| [Gnosis](./reviews/gnosis.md) | files | pull | — | no | rank | — |
| [Graphiti](./reviews/graphiti.md) | graph | pull | — | yes | validate+rank+learn | consolidate+dedup+evolve+invalidate |
| [HALO](./reviews/halo.md) | sqlite | pull | — | yes | validate+learn | — |
| [Hindsight](./reviews/hindsight.md) | rdbms | both | inferred-lexical+inferred-embedding | yes | validate+rank+learn | consolidate+dedup+evolve |
| [HippoRAG](./reviews/HippoRAG.md) | files | pull | — | no | validate+rank | — |
| [hyalo](./reviews/hyalo.md) | files | pull | — | no | enforce+validate+rank | — |
| [HyperAgents](./reviews/hyperagents.md) | files | push | identifier | yes | enforce+validate+rank+learn | invalidate |
| [interview-doc-agent](./reviews/interview-doc-agent.md) | files | pull | — | no | — | — |
| [KBLaM](./reviews/KBLaM.md) | files | push | coarse+inferred-embedding | no | rank+learn | — |
| [Kompl](./reviews/Kompl.md) | sqlite | both | inferred-lexical+inferred-embedding+inferred-judgment | yes | enforce+validate+rank+learn | dedup+evolve+invalidate |
| [LACP](./reviews/lacp.md) | files | both | coarse+identifier | yes | enforce+validate+rank+learn | consolidate+dedup+evolve+invalidate+decay |
| [Letta](./reviews/letta.md) | rdbms | both | coarse+identifier | yes | enforce+validate+rank+learn | consolidate+evolve |
| [LLM Wiki (kenhuangus)](./reviews/kenhuangus--llm-wiki.md) | repo | both | coarse+inferred-lexical | yes | enforce+validate+rank+learn | evolve+invalidate |
| [LLM Wiki (MehmetGoekce)](./reviews/MehmetGoekce--llm-wiki.md) | files | both | coarse | no | enforce+validate+rank+learn | evolve+invalidate |
| [LLM Wiki (nvk)](./reviews/llm-wiki.md) | files | both | coarse+identifier+inferred-lexical+inferred-judgment | yes | enforce+validate+rank+learn | consolidate+dedup+invalidate |
| [llm-context-base](./reviews/llm-context-base.md) | repo | both | coarse | no | enforce+validate | — |
| [llm-project-wiki](./reviews/llm-project-wiki.md) | files | pull | — | yes | enforce+validate+learn | evolve+invalidate |
| [llm-wiki (Pratiyush)](./reviews/Pratiyush--llm-wiki.md) | files | pull | — | yes | enforce+validate+rank+learn | consolidate |
| [llm-wiki-coordination](./reviews/llm-wiki-coordination.md) | files | pull | — | no | enforce+validate | — |
| [Mem0](./reviews/mem0.md) | vector | both | coarse+identifier+inferred-lexical+inferred-embedding | yes | enforce+validate+rank+learn | consolidate+dedup+decay |
| [Memex](./reviews/memex.md) | files | pull | — | no | enforce+validate | evolve |
| [Memori](./reviews/Memori.md) | rdbms | both | coarse+identifier+inferred-lexical+inferred-embedding | yes | validate+rank+learn | consolidate+dedup |
| [MemoryOS](./reviews/MemoryOS.md) | files | both | coarse+identifier+inferred-embedding | yes | rank+learn | consolidate+evolve+decay |
| [MemPalace](./reviews/mempalace.md) | files | pull | — | yes | validate+rank+learn | dedup+invalidate+decay |
| [MentisDB](./reviews/mentisdb.md) | files | both | coarse+identifier | yes | enforce+validate+rank+learn | dedup |
| [Meta-Harness](./reviews/meta-harness.md) | files | both | coarse+identifier | yes | enforce+validate+rank+learn | — |
| [MiroShark](./reviews/MiroShark.md) | graph | both | identifier+inferred-lexical+inferred-embedding | yes | validate+rank+learn | consolidate+dedup+invalidate |
| [nao](./reviews/nao.md) | files | both | coarse | yes | enforce+validate+rank+learn | evolve+invalidate |
| [napkin](./reviews/napkin.md) | files | pull | — | no | validate+rank | — |
| [Nuggets](./reviews/nuggets.md) | files | both | coarse | yes | rank+learn | decay |
| [o-o](./reviews/o-o.md) | files | pull | — | no | validate | evolve |
| [OpenClerk](./reviews/openclerk.md) | files | pull | — | no | enforce+validate+rank+learn | invalidate |
| [OpenSage](./reviews/OpenSage.md) | files | both | coarse+identifier | yes | enforce+validate+rank+learn | consolidate |
| [OpenViking](./reviews/openviking.md) | files | both | coarse+identifier+inferred-lexical+inferred-embedding | yes | enforce+validate+rank+learn | consolidate+evolve+invalidate |
| [Operational Ontology Framework](./reviews/operational-ontology-framework.md) | repo | pull | — | no | validate | — |
| [Origin](./reviews/origin.md) | sqlite | both | coarse+identifier+inferred-lexical+inferred-embedding | yes | enforce+validate+rank+learn | consolidate+dedup+evolve+invalidate+decay |
| [OS-Copilot](./reviews/OS-Copilot.md) | files | push | inferred-embedding | no | enforce+validate+rank+learn | — |
| [Pal](./reviews/pal.md) | rdbms | both | coarse | no | enforce+validate+rank+learn | consolidate+evolve |
| [Phantom](./reviews/phantom.md) | vector | both | coarse+inferred-lexical+inferred-embedding | yes | enforce+validate+rank+learn | consolidate+evolve+invalidate+decay |
| [pi-self-learning](./reviews/pi-self-learning.md) | files | both | coarse | no | rank+learn | consolidate+dedup+evolve |
| [Playground](./reviews/playground.md) | graph | both | coarse | no | validate | — |
| [Quicky Wiki](./reviews/quicky-wiki.md) | sqlite | pull | — | no | validate+rank+learn | consolidate+evolve+invalidate+decay |
| [ReasoningBank](./reviews/reasoning-bank.md) | files | both | inferred-embedding | no | validate+rank+learn | — |
| [Reflexion](./reviews/reflexion.md) | in-memory | push | identifier | no | validate+learn | — |
| [REM](./reviews/REM.md) | rdbms | both | identifier+inferred-embedding | yes | validate+rank+learn | — |
| [SAGE](./reviews/sage.md) | sqlite | both | coarse+identifier+inferred-lexical+inferred-embedding | no | enforce+validate+rank+learn | dedup+invalidate+decay |
| [sage-wiki](./reviews/sage-wiki.md) | files | pull | — | yes | validate+rank+learn | dedup+evolve+invalidate+decay |
| [Secure LLM-Wiki](./reviews/secure-llm-wiki.md) | repo | push | coarse | no | enforce+validate+rank | dedup+decay |
| [Self-Training-LLM](./reviews/Self-Training-LLM.md) | model-weights | push | coarse | yes | enforce+validate+rank+learn | — |
| [Semiont](./reviews/semiont.md) | files | both | identifier+inferred-embedding+inferred-judgment | yes | validate+rank | dedup+evolve+invalidate+decay |
| [sift-kg](./reviews/sift-kg.md) | files | pull | — | no | validate+rank | consolidate+dedup+invalidate |
| [Siftly](./reviews/siftly.md) | sqlite | pull | — | no | rank | dedup+evolve+invalidate |
| [Signet AI](./reviews/signetai.md) | sqlite | both | coarse+identifier+inferred-lexical+inferred-embedding | yes | enforce+validate+rank+learn | consolidate+dedup+evolve+invalidate+decay |
| [SkillNote](./reviews/skillnote.md) | rdbms | both | coarse+identifier+inferred-judgment | yes | enforce+validate+rank+learn | invalidate+decay |
| [SkillWeaver](./reviews/SkillWeaver.md) | files | both | inferred-judgment | yes | enforce+validate+rank+learn | evolve |
| [SkillX](./reviews/SkillX.md) | in-memory | both | identifier+inferred-embedding+inferred-judgment | yes | enforce+validate+rank+learn | consolidate+dedup |
| [Spacebot](./reviews/spacebot.md) | sqlite | both | coarse+identifier+inferred-lexical+inferred-embedding | yes | enforce+validate+rank+learn | consolidate+dedup+invalidate+decay |
| [Sparks](./reviews/sparks.md) | files | pull | — | no | validate | invalidate+decay |
| [Stash](./reviews/stash.md) | rdbms | pull | — | yes | validate+rank+learn | consolidate+dedup+invalidate+decay |
| [supermemory](./reviews/supermemory.md) | service-object | both | coarse+inferred-lexical+inferred-embedding | yes | rank+learn | dedup+invalidate+decay |
| [Synapptic](./reviews/synapptic.md) | files | push | identifier | yes | enforce+validate+rank+learn | consolidate+dedup+invalidate+decay |
| [Synthadoc](./reviews/synthadoc.md) | files | pull | — | no | enforce+validate+rank | dedup+invalidate+decay |
| [Tendril](./reviews/tendril.md) | files | pull | — | no | enforce+validate | evolve+invalidate+decay |
| [Thalo](./reviews/thalo.md) | files | both | identifier | no | enforce+validate | consolidate+dedup+invalidate+decay |
| [TheKnowledge](./reviews/TheKnowledge.md) | files | both | coarse | yes | enforce+validate+learn | consolidate |
| [Tolaria](./reviews/tolaria.md) | repo | both | identifier+inferred-lexical | no | enforce+rank | consolidate+invalidate+decay |
| [tracecraft](./reviews/tracecraft.md) | files | pull | — | no | enforce | consolidate+dedup+invalidate+decay |
| [Virtual Context](./reviews/virtual-context.md) | sqlite | both | identifier+inferred-lexical+inferred-embedding+inferred-judgment | yes | rank+learn | consolidate+evolve+invalidate+decay |
| [VLM-wiki](./reviews/VLM-wiki.md) | files | pull | — | no | — | consolidate |
| [Voiden](./reviews/voiden.md) | files | pull | — | no | validate | consolidate+decay |
| [Voyager](./reviews/voyager.md) | files | push | coarse+inferred-embedding | yes | enforce+validate+rank+learn | consolidate+invalidate+decay |
| [WeKnora](./reviews/WeKnora.md) | rdbms | both | identifier+inferred-lexical+inferred-embedding+inferred-judgment | yes | enforce+validate+rank+learn | consolidate+evolve |
| [WUPHF](./reviews/wuphf.md) | repo | both | inferred-lexical+inferred-embedding | yes | enforce+validate+rank+learn | consolidate+dedup+invalidate+decay |
| [xMemory](./reviews/xMemory.md) | vector | both | inferred-embedding | yes | rank+learn | consolidate+dedup+invalidate |
| [Zikkaron](./reviews/Zikkaron.md) | sqlite | both | coarse+identifier+inferred-lexical+inferred-embedding | yes | enforce+validate+rank+learn | consolidate+dedup+evolve+decay |

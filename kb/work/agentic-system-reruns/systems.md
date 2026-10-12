# Systems to rerun

Inventory captured on 2026-10-12: **206 targets from 223 records**. See the
[workshop README](./README.md) for scope, deduplication and completion rules.

**Progress: 11 complete with the new engine; 189 pending; 6 blocked or recovery-required; four reserved pipelines in [rolling execution 06](./rolling-06.md), no publications awaiting integration.** [Rolling execution 04](./rolling-04.md) records four API/stream failures and the operator's decision to replace those runs with fresh reruns rather than resume them. [Resume](./resume-2026-10-12.md) records current integration and scheduling disposition; [batch 03](./batch-03.md) retains prior evidence. Checked rows have
published current-engine analysis sets. Completed sets are accepted with recorded limits, not limit-free results.
Historical records are inclusion and identity references, not fresh-run evidence.
The [validation-path maintenance decision](./validation-path-maintenance.md)
resolved the shared producer suspicion. The operator released the dispatch stop;
[rolling execution 05](./rolling-05.md) resumes four fresh source-first pipelines
from the committed validation-output method. All dispatched analyses and audits
have returned. The operator subsequently authorized restart and lifted that
session's overly broad provider pause; resume eligible pending targets after
ownership reconciliation and runtime preflight, as stated in the workshop README.
The six individual holds remain in force; Agent Skills is reserved to its
reported owner.
After assignment, append the run identifier and source boundary. For new runs,
check the box only after publication, audit clearance and verified integration;
append the overview, audit link and integration commit. Record blockers explicitly.

## Rerun checklist

- [ ] **A-mem** (`a-mem`) — pending; [legacy review](../../agent-memory-systems/reviews/a-mem.md).
- [ ] **Academic Research Skills** (`academic-research-skills`) — stopped in [batch 02](./batch-02.md); run `AAS-2026-10-12-academic-research-skills-af879d1883bd-01`; boundary `d1e51716e53fc371727ea6164dd709fc8ea28c97`; runtime worker reported audit-derived findings exposed in upstream source; no publication; unblock requires an operator recovery decision on the source-exposure rule; nested lookup diagnostic now succeeds; [authored account](../../agentic-systems/reviews/academic-research-skills.md).
- [ ] **ACE** (`ace`) — recovery-required in [batch 03](./batch-03.md); fresh run `AAS-2026-10-12-ace-a22ddd59ed57-01`, boundary `82709de050e1db6e6ef2f07bcb0393560b94992a`; coordinator API failure left `000019-reconciliation` open, no publication; unblock requires confirmation of prior worker status and operator recovery direction. Lowercase preparation succeeded under the clarified method; [legacy review](../../agent-memory-systems/reviews/ace.md).
- [x] **AgeMem** (`agemem`) — complete with recorded limits; run `AAS-2026-10-12-2601-01885v1-32274e5bddc1-01`; arXiv v1 HTML boundary SHA-256 `15a7a5f4620aa1b130b4f420a08d8c671aa601f4aad45c101eedfd05d528c7b0`; [overview](../../agentic-system-analyses/retained/2601-01885v1/overview.md); [audit](./audits/batch-03-agemem.md); integration `eedefc2e0e46b8e7a1eaf7581a0386f82f76e151`; [resume](./resume-2026-10-12.md); [lightweight review](../../agent-memory-systems/lightweight/agemem.md).
- [x] **Agent-R** (`agent-r`) — complete with recorded limits; run `AAS-2026-10-12-agent-r-216224d4270a-01`; boundary `82fcc1ca7873b460949ed49022146dd988c32e31`; [overview](../../agentic-system-analyses/retained/agent-r/overview.md); [audit](./audits/batch-03-agent-r.md); integration `04b351bb1c01cb791554cf1281ecd546853723ed`; [resume](./resume-2026-10-12.md); [legacy review](../../agent-memory-systems/reviews/agent-r.md).
- [ ] **Agent-S** (`agent-s`) — pending; [legacy review](../../agent-memory-systems/reviews/Agent-S.md).
- [ ] **Agent Skills for Context Engineering** (`agent-skills-for-context-engineering`) — stopped in [batch 03](./batch-03.md); run `AAS-2026-10-12-agent-skills-for-context-engineering-2423c2f20f83-01`; boundary `9ff0c99108b36d3b886defd825d8ac1f47dba374`; profile-verification API failure and retained epistemic validation-path problem; no publication; reserved to its reported owner; [retrospective](./audits/path-confusion-agent-skills.md) holds the affected draft for an overstated conflict rule, incomplete independent grounding and absent content validation; unblock requires owner coordination and supported recovery; [legacy review](../../agent-memory-systems/reviews/agent-skills-for-context-engineering.md).
- [x] **Agent Workflow Memory** (`agent-workflow-memory`) — complete with recorded limits in [rolling execution 05](./rolling-05.md); run `AAS-2026-10-12-agent-workflow-memory-cb2da079273e-01`, boundary `8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1`; [overview](../../agentic-system-analyses/retained/agent-workflow-memory/overview.md); [audit](./audits/rolling-05-agent-workflow-memory.md); integration `c4ca27c0b366f1f61819af18379dad8cb15b130f`; preserve predecessor stopped run `AAS-2026-10-12-agent-workflow-memory-116175117a61-01` without recovery; [legacy review](../../agent-memory-systems/reviews/agent-workflow-memory.md).
- [x] **AgentFly** (`agentfly`) — complete with recorded limits in [rolling execution 05](./rolling-05.md); run `AAS-2026-10-12-agentfly-bbfc9fb2d5c7-01`, boundary `42fbbcac63dd58ed6856c0761357345a58e4f032`; [overview](../../agentic-system-analyses/retained/agentfly/overview.md); [audit](./audits/rolling-05-agentfly.md); integration `e388725cefffb01c94bc5967cee74a8ccba68120`; preserve predecessor stopped run `AAS-2026-10-12-agentfly-987dd174e8a2-01` without recovery; [legacy review](../../agent-memory-systems/reviews/AgentFly.md).
- [ ] **Agentic Harness Engineering** (`agentic-harness-engineering`) — **fresh rerun required**, by operator decision in [rolling execution 04](./rolling-04.md); preserve stopped run `AAS-2026-10-12-agentic-harness-engineering-49c4f24b03c3-01`, boundary `8b2a55d97590363fe50c3cc6b5e833b020a4bb4c`, report-verification stream failure, no publication; do not resume this run; fresh replacement stopped in [rolling execution 05](./rolling-05.md), run `AAS-2026-10-12-agentic-harness-engineering-b7fb59b2f7bd-01`, acquired HEAD `8b2a55d97590363fe50c3cc6b5e833b020a4bb4c`; boundary worker API 503, no publication or open attempts; recovery requires a supported decision after provider availability is established; [legacy review](../../agent-memory-systems/reviews/agentic-harness-engineering.md).
- [x] **Agentic Local Brain** (`agentic-local-brain`) — complete with recorded limits in [rolling execution 05](./rolling-05.md); run `AAS-2026-10-12-agentic-local-brain-f00cbd577178-01`, boundary `41ea0cb104686eb0d39f32c94c2b84d37cdff0e7`; [overview](../../agentic-system-analyses/retained/agentic-local-brain/overview.md); [audit](./audits/rolling-05-agentic-local-brain.md); integration `0c56e3be1f167ef71fb9711897b89a2f27fe33b6`; preserve predecessor stopped run `AAS-2026-10-12-agentic-local-brain-27587657c512-01` without recovery; [legacy review](../../agent-memory-systems/reviews/agentic-local-brain.md).
- [ ] **Agno AgentOS** (`agno-agentos`) — pending; [authored account](../../agentic-systems/reviews/agno-agentos.md).
- [ ] **AI Agents in Depth** (`ai-agent-book`) — assigned in [rolling execution 06](./rolling-06.md), prepared worktree `ai-agent-book-d56e8121d636`; source acquisition pending; [authored account](../../agentic-systems/reviews/ai-agent-book.md).
- [ ] **AI-Context-OS** (`ai-context-os`) — stopped in [rolling execution 05](./rolling-05.md), run `AAS-2026-10-12-ai-context-os-4f81c8c12f62-01`, frozen source `9ed263080cadf98702bebb42d5260b45bd526f6c`; synthesis worker API 503, no publication or open attempts; recovery requires a supported decision after provider availability is established; [legacy review](../../agent-memory-systems/reviews/AI-Context-OS.md).
- [ ] **ai-memex-cli** (`ai-memex-cli`) — stopped in [rolling execution 05](./rolling-05.md), run `AAS-2026-10-12-ai-memex-cli-8e14b4b6efdc-01`, frozen source `4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f`; epistemic worker stream ended before terminal response, no publication or open attempts; recovery requires a supported decision after provider availability is established; [legacy review](../../agent-memory-systems/reviews/ai-memex-cli.md).
- [ ] **AI Research OS Workshop** (`ai-research-os-workshop`) — assigned in [rolling execution 06](./rolling-06.md), prepared worktree `ai-research-os-workshop-1a93869f8e7f`; source acquisition pending; [legacy review](../../agent-memory-systems/reviews/ai-research-os-workshop.md).
- [ ] **AIDE2** (`aide2`) — pending; [archived review](../../agentic-systems/reviews-archive/aide2.md).
- [ ] **Amazon Science SAGE** (`amazon-science--sage`) — assigned in [rolling execution 06](./rolling-06.md), prepared worktree `amazon-science-sage-8387fc4221ab`; source acquisition pending; [legacy review](../../agent-memory-systems/reviews/amazon-science--SAGE.md).
- [ ] **Apache Maka** (`apache-maka`) — assigned in [rolling execution 06](./rolling-06.md), prepared worktree `apache-maka-c1fa0818ba04`; source acquisition pending; [archived review](../../agentic-systems/reviews-archive/apache-maka.md).
- [ ] **Archie** (`archie`) — pending; [legacy review](../../agent-memory-systems/reviews/archie.md).
- [ ] **AREX-Skill** (`arex-skill`) — pending; [archived review](../../agentic-systems/reviews-archive/arex-skill.md).
- [ ] **AriGraph** (`arigraph`) — pending; [legacy review](../../agent-memory-systems/reviews/AriGraph.md).
- [ ] **Ars Contexta** (`arscontexta`) — pending; [legacy review](../../agent-memory-systems/reviews/arscontexta.md).
- [ ] **arsumbris** (`arsumbris`) — pending; [archived review](../../agentic-systems/reviews-archive/arsumbris.md).
- [ ] **ATLAS** (`atlas`) — pending; [legacy review](../../agent-memory-systems/reviews/atlas.md).
- [ ] **Atomic** (`atomic`) — pending; [legacy review](../../agent-memory-systems/reviews/atomic.md).
- [ ] **Auto-claude-code-research-in-sleep** (`auto-claude-code-research-in-sleep`) — pending; [legacy review](../../agent-memory-systems/reviews/Auto-claude-code-research-in-sleep.md).
- [ ] **auto-harness** (`auto-harness`) — pending; [legacy review](../../agent-memory-systems/reviews/auto-harness.md).
- [ ] **Autocontext** (`autocontext`) — pending; [legacy review](../../agent-memory-systems/reviews/autocontext.md).
- [ ] **Autogenesis** (`autogenesis`) — pending; [authored account](../../agentic-systems/reviews/autogenesis.md).
- [ ] **AutoSci** (`autosci`) — pending; [legacy review](../../agent-memory-systems/reviews/AutoSci.md).
- [ ] **Awesome Agent Memory** (`awesome-agent-memory`) — pending; [legacy review](../../agent-memory-systems/reviews/Awesome-Agent-Memory.md).
- [ ] **Basic Memory** (`basic-memory`) — pending; [legacy review](../../agent-memory-systems/reviews/basic-memory.md).
- [ ] **beads_rust** (`beads-rust`) — pending; [authored account](../../agentic-systems/reviews/beads-rust.md).
- [ ] **Beever Atlas** (`beever-atlas`) — pending; [legacy review](../../agent-memory-systems/reviews/beever-atlas.md).
- [ ] **Binder** (`binder`) — pending; [legacy review](../../agent-memory-systems/reviews/binder.md).
- [ ] **browzy.ai** (`browzy-ai`) — pending; [legacy review](../../agent-memory-systems/reviews/browzy-ai.md).
- [ ] **byterover-cli** (`byterover-cli`) — pending; [legacy review](../../agent-memory-systems/reviews/byterover-cli.md).
- [ ] **cass_memory_system** (`cass_memory_system`) — pending; [legacy review](../../agent-memory-systems/reviews/cass_memory_system.md).
- [ ] **Claude Code dynamic workflows** (`claude-code-dynamic-workflows`) — pending; [authored account](../../agentic-systems/reviews/claude-code-dynamic-workflows.md).
- [ ] **Claude Context Guard** (`claude-context-guard`) — pending; [legacy review](../../agent-memory-systems/reviews/claude-context-guard.md).
- [ ] **claude-obsidian** (`claude-obsidian`) — pending; [legacy review](../../agent-memory-systems/reviews/claude-obsidian.md).
- [ ] **Claude Workstream Kit** (`claude-workstream-kit`) — pending; [legacy review](../../agent-memory-systems/reviews/claude-workstream-kit.md).
- [ ] **ClawVault** (`clawvault`) — pending; [legacy review](../../agent-memory-systems/reviews/clawvault.md).
- [ ] **Closure-SDK** (`closure-sdk`) — pending; [legacy review](../../agent-memory-systems/reviews/Closure-SDK.md).
- [ ] **Clude** (`cludebot`) — pending; [legacy review](../../agent-memory-systems/reviews/cludebot.md).
- [ ] **LLM Wiki (cobusgreyling)** (`cobusgreyling--llm-wiki`) — pending; [legacy review](../../agent-memory-systems/reviews/cobusgreyling--llm-wiki.md).
- [ ] **CocoIndex** (`cocoindex`) — pending; [legacy review](../../agent-memory-systems/reviews/cocoindex.md).
- [ ] **Cognee** (`cognee`) — pending; [legacy review](../../agent-memory-systems/reviews/cognee.md).
- [ ] **Company Brain** (`company-brain`) — pending; [archived review](../../agentic-systems/reviews-archive/company-brain.md).
- [ ] **Compound Engineering Plugin** (`compound-engineering-plugin`) — pending; [legacy review](../../agent-memory-systems/reviews/compound-engineering-plugin.md); [authored account](../../agentic-systems/reviews/compound-engineering-plugin.md).
- [ ] **Context Constitution** (`context-constitution`) — pending; [legacy review](../../agent-memory-systems/reviews/context-constitution.md).
- [ ] **ContextPilot** (`contextpilot`) — pending; [archived review](../../agentic-systems/reviews-archive/contextpilot.md).
- [ ] **Continuity** (`continuity`) — pending; [legacy review](../../agent-memory-systems/reviews/continuity.md).
- [ ] **CORAL** (`coral`) — pending; [legacy review](../../agent-memory-systems/reviews/CORAL.md).
- [ ] **Cortex** (`cortex`) — pending; [legacy review](../../agent-memory-systems/reviews/cortex.md).
- [ ] **cq** (`cq`) — pending; [legacy review](../../agent-memory-systems/reviews/cq.md).
- [ ] **CrewAI Memory** (`crewai-memory`) — pending; [legacy review](../../agent-memory-systems/reviews/crewai-memory.md).
- [ ] **Decapod** (`decapod`) — pending; [legacy review](../../agent-memory-systems/reviews/decapod.md).
- [ ] **deja-vu** (`deja-vu`) — pending; [legacy review](../../agent-memory-systems/reviews/deja-vu.md).
- [ ] **dense-mem** (`dense-mem`) — pending; [legacy review](../../agent-memory-systems/reviews/dense-mem.md).
- [ ] **DocMason** (`docmason`) — pending; [legacy review](../../agent-memory-systems/reviews/docmason.md).
- [ ] **DualGraph** (`dualgraph`) — pending; [archived review](../../agentic-systems/reviews-archive/dualgraph.md).
- [x] **Dynamic Cheatsheet** (`dynamic-cheatsheet`) — complete with new engine; run `AAS-2026-10-12-dynamic-cheatsheet-ca0a0b29d273-01`; boundary `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`; accepted with limits; [legacy review](../../agent-memory-systems/reviews/dynamic-cheatsheet.md); [archived review](../../agentic-systems/reviews-archive/dynamic-cheatsheet.md); [current overview](../../agentic-system-analyses/retained/dynamic-cheatsheet/overview.md).
- [ ] **EAL-bench** (`eal-bench`) — pending; [archived review](../../agentic-systems/reviews-archive/eal-bench.md).
- [ ] **Ecdysis** (`ecdysis`) — pending; [archived review](../../agentic-systems/reviews-archive/ecdysis.md).
- [ ] **Echel** (`echel`) — pending; [legacy review](../../agent-memory-systems/reviews/echel.md).
- [ ] **EchoesVault / echoes-vault-opencode** (`echoes-vault-opencode`) — pending; [legacy review](../../agent-memory-systems/reviews/echoes-vault-opencode.md).
- [ ] **EchoWiki** (`echowiki`) — pending; [legacy review](../../agent-memory-systems/reviews/echowiki.md).
- [ ] **Eidetic** (`eidetic`) — pending; [legacy review](../../agent-memory-systems/reviews/eidetic.md).
- [ ] **Eigenius** (`eigenius`) — pending; [authored account](../../agentic-systems/reviews/eigenius.md).
- [ ] **Engraph** (`engraph`) — pending; [legacy review](../../agent-memory-systems/reviews/engraph.md).
- [ ] **Enoch** (`enoch`) — pending; [archived review](../../agentic-systems/reviews-archive/enoch.md).
- [ ] **EQUIPA** (`equipa`) — pending; [legacy review](../../agent-memory-systems/reviews/equipa.md).
- [ ] **EvoOntology** (`evoontology`) — pending; [archived review](../../agentic-systems/reviews-archive/evoontology.md).
- [ ] **Exo** (`exo`) — pending; [legacy review](../../agent-memory-systems/reviews/exo.md); [authored account](../../agentic-systems/reviews/exo.md).
- [ ] **Exocomp** (`exocomp`) — pending; [legacy review](../../agent-memory-systems/reviews/exocomp.md).
- [ ] **ExpeL** (`expel`) — pending; [legacy review](../../agent-memory-systems/reviews/expel.md).
- [ ] **Fintool** (`fintool`) — pending; [lightweight review](../../agent-memory-systems/lightweight/fintool.md).
- [ ] **Fractal** (`fractal`) — pending; [authored account](../../agentic-systems/reviews/fractal.md).
- [ ] **fragility-grid collection and resume subsystem** (`fragility-grid`) — pending; [archived review](../../agentic-systems/reviews-archive/fragility-grid.md).
- [ ] **Funes** (`funes`) — pending; [legacy review](../../agent-memory-systems/reviews/funes.md).
- [ ] **G-Memory** (`g-memory`) — pending; [legacy review](../../agent-memory-systems/reviews/g-memory.md).
- [x] **GBrain** (`gbrain`) — complete with new engine; run `AAS-2026-10-11-gbrain-9de8e3c225d3-01`; boundary `da434385572e0dc0d825649179aabed4107d6e60`; accepted with limits; [legacy review](../../agent-memory-systems/reviews/gbrain.md); [archived review](../../agentic-systems/reviews-archive/gbrain-garrytan.md); [current overview](../../agentic-system-analyses/retained/gbrain/overview.md).
- [ ] **getsentry/skills** (`getsentry-skills`) — pending; [legacy review](../../agent-memory-systems/reviews/getsentry-skills.md).
- [ ] **Gnosis** (`gnosis`) — pending; [legacy review](../../agent-memory-systems/reviews/gnosis.md).
- [x] **Graphiti** (`graphiti`) — complete with new engine; run `AAS-2026-10-12-graphiti-1d535ca565a4-01`; boundary `964bb11d1e7020e3cc67fab244268b0736b6c219`; accepted with limits; [legacy review](../../agent-memory-systems/reviews/graphiti.md); [current overview](../../agentic-system-analyses/retained/graphiti/overview.md).
- [ ] **HALO** (`halo`) — pending; [legacy review](../../agent-memory-systems/reviews/halo.md).
- [ ] **Hermes Agent** (`hermes-agent`) — pending; [legacy review](../../agent-memory-systems/reviews/hermes-agent.md).
- [ ] **Hindsight** (`hindsight`) — pending; [legacy review](../../agent-memory-systems/reviews/hindsight.md).
- [ ] **HippoRAG** (`hipporag`) — pending; [legacy review](../../agent-memory-systems/reviews/HippoRAG.md).
- [ ] **hyalo** (`hyalo`) — pending; [legacy review](../../agent-memory-systems/reviews/hyalo.md).
- [ ] **HyperAgents** (`hyperagents`) — pending; [legacy review](../../agent-memory-systems/reviews/hyperagents.md).
- [ ] **Incremental Self-Improvement** (`incremental-self-improvement`) — pending; [lightweight review](../../agent-memory-systems/lightweight/incremental-self-improvement.md).
- [x] **Instinctual Memory** (`instinctual-memory`) — complete with new engine; run `AAS-2026-10-12-instinctual-memory-af48437aa60c-01`; boundary `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`; accepted with limits; [archived review](../../agentic-systems/reviews-archive/instinctual-memory-2026-09-30-02.md); [archived review](../../agentic-systems/reviews-archive/instinctual-memory.md); [current overview](../../agentic-system-analyses/retained/instinctual-memory/overview.md).
- [ ] **interview-doc-agent** (`interview-doc-agent`) — pending; [legacy review](../../agent-memory-systems/reviews/interview-doc-agent.md).
- [ ] **Mnemosyne / IsaacCLupus mnemosyn spec** (`isaacclupus_mnemosyn_spec`) — pending; [lightweight review](../../agent-memory-systems/lightweight/IsaacCLupus_mnemosyn_spec.md).
- [ ] **JAZ** (`jaz`) — pending; [archived review](../../agentic-systems/reviews-archive/jaz.md).
- [ ] **jaz-evals** (`jaz-evals`) — pending; [archived review](../../agentic-systems/reviews-archive/jaz-evals.md).
- [ ] **JEPA-Anything** (`jepa-anything`) — pending; [archived review](../../agentic-systems/reviews-archive/jepa-anything.md).
- [ ] **KBLaM** (`kblam`) — pending; [legacy review](../../agent-memory-systems/reviews/KBLaM.md).
- [ ] **LLM Wiki (kenhuangus)** (`kenhuangus--llm-wiki`) — pending; [legacy review](../../agent-memory-systems/reviews/kenhuangus--llm-wiki.md).
- [ ] **kgai** (`kgai`) — pending; [legacy review](../../agent-memory-systems/reviews/kgai.md).
- [ ] **Kompl** (`kompl`) — pending; [legacy review](../../agent-memory-systems/reviews/Kompl.md).
- [ ] **LACP** (`lacp`) — pending; [legacy review](../../agent-memory-systems/reviews/lacp.md).
- [ ] **Letta** (`letta`) — pending; [legacy review](../../agent-memory-systems/reviews/letta.md).
- [x] **Letta Code** (`letta-code`) — complete with new engine; run `AAS-2026-10-12-letta-code-be76afeab9b7-01`; boundary `271f119dcf37d58649a18e6c733386b3c710a456`; accepted with limits; [current overview](../../agentic-system-analyses/retained/letta-code/overview.md).
- [ ] **LHTB bundled continuation mechanism** (`lhtb`) — pending; [archived review](../../agentic-systems/reviews-archive/lhtb.md).
- [ ] **Link** (`link`) — pending; [legacy review](../../agent-memory-systems/reviews/link.md).
- [ ] **llm-context-base** (`llm-context-base`) — pending; [legacy review](../../agent-memory-systems/reviews/llm-context-base.md).
- [ ] **llm-project-wiki** (`llm-project-wiki`) — pending; [legacy review](../../agent-memory-systems/reviews/llm-project-wiki.md).
- [ ] **LLM Wiki (nvk)** (`llm-wiki`) — pending; [legacy review](../../agent-memory-systems/reviews/llm-wiki.md).
- [ ] **llm-wiki-coordination** (`llm-wiki-coordination`) — pending; [legacy review](../../agent-memory-systems/reviews/llm-wiki-coordination.md).
- [ ] **LLM-WIKI-MCP** (`llm-wiki-mcp`) — pending; [legacy review](../../agent-memory-systems/reviews/LLM-WIKI-MCP.md).
- [ ] **LLM-Wiki-v3** (`llm-wiki-v3`) — pending; [legacy review](../../agent-memory-systems/reviews/LLM-Wiki-v3.md).
- [ ] **llmwiki-marimo** (`llmwiki-marimo`) — pending; [legacy review](../../agent-memory-systems/reviews/llmwiki-marimo.md).
- [ ] **LLM Wiki (MehmetGoekce)** (`mehmetgoekce--llm-wiki`) — pending; [legacy review](../../agent-memory-systems/reviews/MehmetGoekce--llm-wiki.md).
- [ ] **Mem0** (`mem0`) — pending; [legacy review](../../agent-memory-systems/reviews/mem0.md); [archived review](../../agentic-systems/reviews-archive/mem0.md).
- [ ] **Memex** (`memex`) — pending; [legacy review](../../agent-memory-systems/reviews/memex.md).
- [ ] **Memori** (`memori`) — pending; [legacy review](../../agent-memory-systems/reviews/Memori.md).
- [ ] **MemoryOS** (`memoryos`) — pending; [legacy review](../../agent-memory-systems/reviews/MemoryOS.md).
- [ ] **MemPalace** (`mempalace`) — pending; [legacy review](../../agent-memory-systems/reviews/mempalace.md).
- [ ] **memwiki** (`memwiki`) — pending; [legacy review](../../agent-memory-systems/reviews/memwiki.md).
- [ ] **MentisDB** (`mentisdb`) — pending; [legacy review](../../agent-memory-systems/reviews/mentisdb.md).
- [ ] **MerchantBench: ReAct and optional persistent notes** (`merchantbench`) — pending; [archived review](../../agentic-systems/reviews-archive/merchantbench.md).
- [ ] **Meta-Harness** (`meta-harness`) — pending; [legacy review](../../agent-memory-systems/reviews/meta-harness.md).
- [ ] **Meta^n** (`meta-n`) — pending; [archived review](../../agentic-systems/reviews-archive/meta-n.md).
- [ ] **MiroShark** (`miroshark`) — pending; [legacy review](../../agent-memory-systems/reviews/MiroShark.md).
- [ ] **ModularRSI** (`modularrsi`) — pending; [archived review](../../agentic-systems/reviews-archive/modularrsi.md).
- [ ] **Neo4j Agent Memory Service (NAMS)** (`nams`) — pending; [lightweight review](../../agent-memory-systems/lightweight/nams.md).
- [ ] **nao** (`nao`) — pending; [legacy review](../../agent-memory-systems/reviews/nao.md).
- [x] **Napkin** (`napkin`) — complete with new engine; run `AAS-2026-10-12-napkin-2b85bef38252-01`; boundary `7582d6a46f5a11995956e60a59c41a5b242109f1`; accepted with limits; [legacy review](../../agent-memory-systems/reviews/napkin.md); [archived review](../../agentic-systems/reviews-archive/napkin.md); [current overview](../../agentic-system-analyses/retained/napkin/overview.md).
- [ ] **Nuggets** (`nuggets`) — pending; [legacy review](../../agent-memory-systems/reviews/nuggets.md).
- [ ] **o-o** (`o-o`) — pending; [legacy review](../../agent-memory-systems/reviews/o-o.md).
- [ ] **oh-my-pi** (`oh-my-pi`) — pending; [archived review](../../agentic-systems/reviews-archive/oh-my-pi.md).
- [ ] **OKF Harness** (`okf-harness`) — pending; [legacy review](../../agent-memory-systems/reviews/okf-harness.md).
- [ ] **OpenClerk** (`openclerk`) — pending; [legacy review](../../agent-memory-systems/reviews/openclerk.md).
- [ ] **OpenRSI: OpenMLE search, experience and training** (`openrsi`) — pending; [archived review](../../agentic-systems/reviews-archive/openrsi.md).
- [ ] **OpenSage** (`opensage`) — pending; [legacy review](../../agent-memory-systems/reviews/OpenSage.md).
- [ ] **OpenViking** (`openviking`) — pending; [legacy review](../../agent-memory-systems/reviews/openviking.md); [archived review](../../agentic-systems/reviews-archive/openviking.md).
- [ ] **OpenWiki** (`openwiki`) — pending; [legacy review](../../agent-memory-systems/reviews/openwiki.md).
- [ ] **Operational Ontology Framework** (`operational-ontology-framework`) — pending; [legacy review](../../agent-memory-systems/reviews/operational-ontology-framework.md).
- [ ] **Origin** (`origin`) — pending; [legacy review](../../agent-memory-systems/reviews/origin.md).
- [ ] **OS-Copilot** (`os-copilot`) — pending; [legacy review](../../agent-memory-systems/reviews/OS-Copilot.md).
- [ ] **PageIndex** (`pageindex`) — pending; [archived review](../../agentic-systems/reviews-archive/pageindex-2026-09-29-02.md).
- [ ] **Pal** (`pal`) — pending; [legacy review](../../agent-memory-systems/reviews/pal.md).
- [ ] **Phantom** (`phantom`) — pending; [legacy review](../../agent-memory-systems/reviews/phantom.md).
- [ ] **pi-posthorse context-window extension** (`pi-posthorse`) — pending; [archived review](../../agentic-systems/reviews-archive/pi-posthorse.md).
- [ ] **pi-self-learning** (`pi-self-learning`) — pending; [legacy review](../../agent-memory-systems/reviews/pi-self-learning.md).
- [ ] **Playground** (`playground`) — pending; [legacy review](../../agent-memory-systems/reviews/playground.md).
- [ ] **Pond** (`pond`) — pending; [legacy review](../../agent-memory-systems/reviews/pond.md); [archived review](../../agentic-systems/reviews-archive/pond.md).
- [ ] **llm-wiki (Pratiyush)** (`pratiyush--llm-wiki`) — pending; [legacy review](../../agent-memory-systems/reviews/Pratiyush--llm-wiki.md).
- [ ] **Prime Agent** (`prime-agent`) — pending; [archived review](../../agentic-systems/reviews-archive/prime-agent.md).
- [ ] **PrimeScientist** (`primescientist`) — pending; [archived review](../../agentic-systems/reviews-archive/primescientist.md).
- [ ] **Prove2Me** (`prove2me`) — pending; [archived review](../../agentic-systems/reviews-archive/prove2me.md).
- [ ] **Quicky Wiki** (`quicky-wiki`) — pending; [legacy review](../../agent-memory-systems/reviews/quicky-wiki.md).
- [ ] **ReasoningBank** (`reasoning-bank`) — pending; [legacy review](../../agent-memory-systems/reviews/reasoning-bank.md).
- [ ] **Reflexion** (`reflexion`) — pending; [legacy review](../../agent-memory-systems/reviews/reflexion.md); [archived review](../../agentic-systems/reviews-archive/reflexion.md).
- [ ] **ReframeWeb** (`reframeweb`) — pending; [legacy review](../../agent-memory-systems/reviews/ReframeWeb.md).
- [ ] **REM** (`rem`) — pending; [legacy review](../../agent-memory-systems/reviews/REM.md).
- [ ] **RSIAgent: verified experience, Actor-owned memory and curriculum search** (`rsiagent`) — pending; [archived review](../../agentic-systems/reviews-archive/rsiagent.md).
- [ ] **SAGE** (`sage`) — pending; [legacy review](../../agent-memory-systems/reviews/sage.md).
- [ ] **sage-wiki** (`sage-wiki`) — pending; [legacy review](../../agent-memory-systems/reviews/sage-wiki.md).
- [ ] **Scroll** (`scroll`) — pending; [legacy review](../../agent-memory-systems/reviews/scroll.md).
- [ ] **Secure LLM-Wiki** (`secure-llm-wiki`) — pending; [legacy review](../../agent-memory-systems/reviews/secure-llm-wiki.md).
- [ ] **Self-Training-LLM** (`self-training-llm`) — pending; [legacy review](../../agent-memory-systems/reviews/Self-Training-LLM.md).
- [ ] **Semantic Engine as ingest infrastructure** (`semantic-engine`) — pending; [authored account](../../agentic-systems/reviews/semantic-engine.md).
- [ ] **Semiont** (`semiont`) — pending; [legacy review](../../agent-memory-systems/reviews/semiont.md).
- [ ] **sift-kg** (`sift-kg`) — pending; [legacy review](../../agent-memory-systems/reviews/sift-kg.md).
- [ ] **Siftly** (`siftly`) — pending; [legacy review](../../agent-memory-systems/reviews/siftly.md).
- [ ] **Sig** (`sig`) — pending; [lightweight review](../../agent-memory-systems/lightweight/sig.md).
- [ ] **Signet AI** (`signetai`) — pending; [legacy review](../../agent-memory-systems/reviews/signetai.md).
- [ ] **SkillLift** (`skilllift`) — pending; [archived review](../../agentic-systems/reviews-archive/skilllift.md).
- [ ] **SkillNote** (`skillnote`) — pending; [legacy review](../../agent-memory-systems/reviews/skillnote.md).
- [ ] **SkillRL** (`skillrl`) — pending; [legacy review](../../agent-memory-systems/reviews/SkillRL.md).
- [ ] **SkillWeaver** (`skillweaver`) — pending; [legacy review](../../agent-memory-systems/reviews/SkillWeaver.md).
- [ ] **SkillX** (`skillx`) — pending; [legacy review](../../agent-memory-systems/reviews/SkillX.md).
- [ ] **Smriti-MCP** (`smriti-mcp`) — pending; [legacy review](../../agent-memory-systems/reviews/smriti-mcp.md).
- [ ] **SoL-Pi** (`sol-pi`) — pending; [archived review](../../agentic-systems/reviews-archive/sol-pi.md).
- [ ] **Spacebot** (`spacebot`) — pending; [legacy review](../../agent-memory-systems/reviews/spacebot.md).
- [ ] **Sparks** (`sparks`) — pending; [legacy review](../../agent-memory-systems/reviews/sparks.md).
- [ ] **Stash** (`stash`) — pending; [legacy review](../../agent-memory-systems/reviews/stash.md).
- [ ] **supermemory** (`supermemory`) — pending; [legacy review](../../agent-memory-systems/reviews/supermemory.md); [archived review](../../agentic-systems/reviews-archive/supermemory.md).
- [ ] **Swamp** (`swamp`) — pending; [legacy review](../../agent-memory-systems/reviews/swamp.md); [authored account](../../agentic-systems/reviews/swamp.md).
- [ ] **SwarmWorld** (`swarmworld`) — pending; [archived review](../../agentic-systems/reviews-archive/swarmworld.md).
- [ ] **Synapptic** (`synapptic`) — pending; [legacy review](../../agent-memory-systems/reviews/synapptic.md).
- [ ] **Synthadoc** (`synthadoc`) — pending; [legacy review](../../agent-memory-systems/reviews/synthadoc.md).
- [ ] **Synto** (`synto`) — pending; [legacy review](../../agent-memory-systems/reviews/synto.md).
- [ ] **Tardigrade inference and compaction** (`tardigrade`) — pending; [archived review](../../agentic-systems/reviews-archive/tardigrade.md).
- [ ] **Tendril** (`tendril`) — pending; [legacy review](../../agent-memory-systems/reviews/tendril.md).
- [ ] **Thalo** (`thalo`) — pending; [legacy review](../../agent-memory-systems/reviews/thalo.md).
- [ ] **ai-modules** (`theafh--ai-modules`) — pending; [legacy review](../../agent-memory-systems/reviews/theafh--ai-modules.md).
- [ ] **TheKnowledge** (`theknowledge`) — pending; [legacy review](../../agent-memory-systems/reviews/TheKnowledge.md).
- [ ] **Tolaria** (`tolaria`) — pending; [legacy review](../../agent-memory-systems/reviews/tolaria.md).
- [ ] **Tracecraft** (`tracecraft`) — pending; [legacy review](../../agent-memory-systems/reviews/tracecraft.md).
- [ ] **Trajectory-Informed Memory Generation** (`trajectory-informed-memory-generation`) — pending; [lightweight review](../../agent-memory-systems/lightweight/trajectory-informed-memory-generation.md).
- [ ] **Virtual Context** (`virtual-context`) — pending; [legacy review](../../agent-memory-systems/reviews/virtual-context.md).
- [ ] **VLM-wiki** (`vlm-wiki`) — pending; [legacy review](../../agent-memory-systems/reviews/VLM-wiki.md).
- [ ] **Voiden** (`voiden`) — pending; [legacy review](../../agent-memory-systems/reviews/voiden.md).
- [ ] **Voyager** (`voyager`) — pending; [legacy review](../../agent-memory-systems/reviews/voyager.md).
- [ ] **WeKnora** (`weknora`) — pending; [legacy review](../../agent-memory-systems/reviews/WeKnora.md).
- [ ] **WikiSkill** (`wikiskill`) — pending; [archived review](../../agentic-systems/reviews-archive/wikiskill.md).
- [ ] **WikiSkill (Stahl-G)** (`wikiskill-stahl-g`) — pending; [archived review](../../agentic-systems/reviews-archive/wikiskill-stahl-g.md).
- [ ] **WUPHF** (`wuphf`) — pending; [legacy review](../../agent-memory-systems/reviews/wuphf.md).
- [ ] **xMemory** (`xmemory`) — pending; [legacy review](../../agent-memory-systems/reviews/xMemory.md).
- [ ] **Zikkaron** (`zikkaron`) — pending; [legacy review](../../agent-memory-systems/reviews/Zikkaron.md).

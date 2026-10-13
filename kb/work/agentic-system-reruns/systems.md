# Systems to rerun

Inventory captured on 2026-10-12: **206 targets from 223 records**. See the
[workshop README](./README.md) for scope, deduplication and completion rules.

**Progress: 17 complete with the new engine; 181 pending; eight held. The operator [released nine targets without substantial accepted analysis](./partial-outcomes-2026-10-13.md) for fresh reruns; six verification-stage holds plus ACE and ai-memex-cli remain held. [Rolling execution 08](./rolling-08.md) owns the queue and has launched four fresh source-first pipelines after reconciliation and preflight. The current workshop commission releases the historical reload dispatch stop; individual holds and preserved failures remain untouched. No integration backlog yet.** [Rolling execution 04](./rolling-04.md) records four API/stream failures and the operator's decision to replace those runs with fresh reruns rather than resume them. [Resume](./resume-2026-10-12.md) records current integration and scheduling disposition; [batch 03](./batch-03.md) retains prior evidence. Checked rows have
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
- [ ] **Academic Research Skills** (`academic-research-skills`) — pending, [released for a fresh rerun](./partial-outcomes-2026-10-13.md); preserve [batch 02](./batch-02.md) run `AAS-2026-10-12-academic-research-skills-af879d1883bd-01`, boundary `d1e51716e53fc371727ea6164dd709fc8ea28c97`; only boundary accepted; runtime worker reported audit-derived findings exposed in upstream source; no publication; fresh execution must respect source-isolation rules and resolve exposure before proceeding; release does not authorize recovery of the preserved run; [authored account](../../agentic-systems/reviews/academic-research-skills.md).
- [ ] **ACE** (`ace`) — recovery-required in [batch 03](./batch-03.md); fresh run `AAS-2026-10-12-ace-a22ddd59ed57-01`, boundary `82709de050e1db6e6ef2f07bcb0393560b94992a`; coordinator API failure left `000019-reconciliation` open, no publication; unblock requires confirmation of prior worker status and operator recovery direction. Lowercase preparation succeeded under the clarified method; [legacy review](../../agent-memory-systems/reviews/ace.md).
- [x] **AgeMem** (`agemem`) — complete with recorded limits; run `AAS-2026-10-12-2601-01885v1-32274e5bddc1-01`; arXiv v1 HTML boundary SHA-256 `15a7a5f4620aa1b130b4f420a08d8c671aa601f4aad45c101eedfd05d528c7b0`; [overview](../../agentic-system-analyses/retained/2601-01885v1/overview.md); [audit](./audits/batch-03-agemem.md); integration `eedefc2e0e46b8e7a1eaf7581a0386f82f76e151`; [resume](./resume-2026-10-12.md); [lightweight review](../../agent-memory-systems/lightweight/agemem.md).
- [x] **Agent-R** (`agent-r`) — complete with recorded limits; run `AAS-2026-10-12-agent-r-216224d4270a-01`; boundary `82fcc1ca7873b460949ed49022146dd988c32e31`; [overview](../../agentic-system-analyses/retained/agent-r/overview.md); [audit](./audits/batch-03-agent-r.md); integration `04b351bb1c01cb791554cf1281ecd546853723ed`; [resume](./resume-2026-10-12.md); [legacy review](../../agent-memory-systems/reviews/agent-r.md).
- [ ] **Agent-S** (`agent-s`) — pending; [legacy review](../../agent-memory-systems/reviews/Agent-S.md).
- [ ] **Agent Skills for Context Engineering** (`agent-skills-for-context-engineering`) — stopped in [batch 03](./batch-03.md); run `AAS-2026-10-12-agent-skills-for-context-engineering-2423c2f20f83-01`; boundary `9ff0c99108b36d3b886defd825d8ac1f47dba374`; profile-verification API failure and retained epistemic validation-path problem; no publication; reserved to its reported owner; [retrospective](./audits/path-confusion-agent-skills.md) holds the affected draft for an overstated conflict rule, incomplete independent grounding and absent content validation; unblock requires owner coordination and supported recovery; [legacy review](../../agent-memory-systems/reviews/agent-skills-for-context-engineering.md).
- [x] **Agent Workflow Memory** (`agent-workflow-memory`) — complete with recorded limits in [rolling execution 05](./rolling-05.md); run `AAS-2026-10-12-agent-workflow-memory-cb2da079273e-01`, boundary `8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1`; [overview](../../agentic-system-analyses/retained/agent-workflow-memory/overview.md); [audit](./audits/rolling-05-agent-workflow-memory.md); integration `c4ca27c0b366f1f61819af18379dad8cb15b130f`; preserve predecessor stopped run `AAS-2026-10-12-agent-workflow-memory-116175117a61-01` without recovery; [legacy review](../../agent-memory-systems/reviews/agent-workflow-memory.md).
- [x] **AgentFly** (`agentfly`) — complete with recorded limits in [rolling execution 05](./rolling-05.md); run `AAS-2026-10-12-agentfly-bbfc9fb2d5c7-01`, boundary `42fbbcac63dd58ed6856c0761357345a58e4f032`; [overview](../../agentic-system-analyses/retained/agentfly/overview.md); [audit](./audits/rolling-05-agentfly.md); integration `e388725cefffb01c94bc5967cee74a8ccba68120`; preserve predecessor stopped run `AAS-2026-10-12-agentfly-987dd174e8a2-01` without recovery; [legacy review](../../agent-memory-systems/reviews/AgentFly.md).
- [ ] **Agentic Harness Engineering** (`agentic-harness-engineering`) — pending, [released for a fresh rerun](./partial-outcomes-2026-10-13.md); latest replacement `AAS-2026-10-12-agentic-harness-engineering-b7fb59b2f7bd-01` stopped in [rolling execution 05](./rolling-05.md) at boundary with API 503, no accepted member/publication/open attempts; acquired HEAD `8b2a55d97590363fe50c3cc6b5e833b020a4bb4c`. Preserve it and predecessor `AAS-2026-10-12-agentic-harness-engineering-49c4f24b03c3-01`, designated for replacement in [rolling execution 04](./rolling-04.md); do not resume either preserved run; [legacy review](../../agent-memory-systems/reviews/agentic-harness-engineering.md).
- [x] **Agentic Local Brain** (`agentic-local-brain`) — complete with recorded limits in [rolling execution 05](./rolling-05.md); run `AAS-2026-10-12-agentic-local-brain-f00cbd577178-01`, boundary `41ea0cb104686eb0d39f32c94c2b84d37cdff0e7`; [overview](../../agentic-system-analyses/retained/agentic-local-brain/overview.md); [audit](./audits/rolling-05-agentic-local-brain.md); integration `0c56e3be1f167ef71fb9711897b89a2f27fe33b6`; preserve predecessor stopped run `AAS-2026-10-12-agentic-local-brain-27587657c512-01` without recovery; [legacy review](../../agent-memory-systems/reviews/agentic-local-brain.md).
- [ ] **Agno AgentOS** (`agno-agentos`) — pending; [authored account](../../agentic-systems/reviews/agno-agentos.md).
- [x] **AI Agents in Depth** (`ai-agent-book`) — complete with recorded limits in [rolling execution 06](./rolling-06.md); run `AAS-2026-10-12-ai-agent-book-d56e8121d636-01`, boundary `dbc046eb896ac4e39aa19c7774c8bf49583b89a6`; selected-workflow coverage, not whole-book replacement; [overview](../../agentic-system-analyses/retained/ai-agent-book/overview.md); [audit](./audits/rolling-06-ai-agent-book.md); integration `3ba7f91dac4bc68f4dee73c9aefabe167271ec4a`; [authored account](../../agentic-systems/reviews/ai-agent-book.md).
- [ ] **AI-Context-OS** (`ai-context-os`) — stopped in [rolling execution 05](./rolling-05.md), run `AAS-2026-10-12-ai-context-os-4f81c8c12f62-01`, frozen source `9ed263080cadf98702bebb42d5260b45bd526f6c`; synthesis worker API 503, no publication or open attempts; recovery requires a supported decision after provider availability is established; [legacy review](../../agent-memory-systems/reviews/AI-Context-OS.md).
- [ ] **ai-memex-cli** (`ai-memex-cli`) — stopped in [rolling execution 05](./rolling-05.md), run `AAS-2026-10-12-ai-memex-cli-8e14b4b6efdc-01`, frozen source `4adb274a33cbb9ff0f03a6aeeb9c8d2525a5ac3f`; epistemic worker stream ended before terminal response, no publication or open attempts; recovery requires a supported decision after provider availability is established; [legacy review](../../agent-memory-systems/reviews/ai-memex-cli.md).
- [x] **AI Research OS Workshop** (`ai-research-os-workshop`) — complete with recorded limits in [rolling execution 06](./rolling-06.md); run `AAS-2026-10-12-ai-research-os-workshop-1a93869f8e7f-01`, boundary `dc6660555266239cd36483cf51b5ab39febacf02`; [overview](../../agentic-system-analyses/retained/ai-research-os-workshop/overview.md); [audit](./audits/rolling-06-ai-research-os-workshop.md); integration `07e73341ad64b4faab06290e9b437ea0c10518b4`; [legacy review](../../agent-memory-systems/reviews/ai-research-os-workshop.md).
- [ ] **AIDE2** (`aide2`) — pending; [archived review](../../agentic-systems/reviews-archive/aide2.md).
- [ ] **Amazon Science SAGE** (`amazon-science--sage`) — pending, [released for a fresh rerun](./partial-outcomes-2026-10-13.md); preserve [rolling execution 06](./rolling-06.md) run `AAS-2026-10-12-sage-8387fc4221ab-01`, acquired revision `3c9244e82244abb1adc5467ee601a03ba0f433a0`; boundary worker stream ended before terminal response; no accepted member/publication/open attempts; [legacy review](../../agent-memory-systems/reviews/amazon-science--SAGE.md).
- [ ] **Apache Maka** (`apache-maka`) — pending, [released for a fresh rerun](./partial-outcomes-2026-10-13.md); preserve [rolling execution 06](./rolling-06.md) run `AAS-2026-10-12-maka-c1fa0818ba04-01`, boundary `a393c5065e56cc083ca3d41943828f80f181f6f6`; only boundary accepted; runtime worker stream ended before terminal response, no publication/open attempts; [archived review](../../agentic-systems/reviews-archive/apache-maka.md).
- [ ] **Archie** (`archie`) — stopped in [rolling execution 06](./rolling-06.md), run `AAS-2026-10-12-archie-aef788232ea1-01`, boundary `76caf94548cf76f2399d9a7446da15e0daa22685`; report-verification worker stream ended before terminal response, no publication or open attempts; unblock requires supported recovery direction; [legacy review](../../agent-memory-systems/reviews/archie.md).
- [ ] **AREX-Skill** (`arex-skill`) — pending; [archived review](../../agentic-systems/reviews-archive/arex-skill.md).
- [x] **AriGraph** (`arigraph`) — complete with recorded limits in [rolling execution 06](./rolling-06.md); run `AAS-2026-10-12-arigraph-fd0f6f1c1383-01`, boundary `e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2`; [overview](../../agentic-system-analyses/retained/arigraph/overview.md); [audit](./audits/rolling-06-arigraph.md); integration `25cf8549f9b2a107d0334acca0ba0a907e442685`; [legacy review](../../agent-memory-systems/reviews/AriGraph.md).
- [x] **Ars Contexta** (`arscontexta`) — complete with recorded limits in [rolling execution 06](./rolling-06.md), run `AAS-2026-10-12-arscontexta-f9e5f2f34166-01`, boundary `2acfd5cc4473c4d06c46be63df748e77e00e2746`; [overview](../../agentic-system-analyses/retained/arscontexta/overview.md); [audit](./audits/rolling-06-arscontexta.md); integration `e4d703463fc5a4443f615abefb8cd222a31c8507`; [legacy review](../../agent-memory-systems/reviews/arscontexta.md).
- [ ] **arsumbris** (`arsumbris`) — stopped in [rolling execution 06](./rolling-06.md), run `AAS-2026-10-12-arsumbris-247284e3101a-01`, boundary `716bb14f2bf50e249d414525c8e07c50478fc786`; report-verification stream failure, no publication/open attempts; unblock requires supported recovery direction; [archived review](../../agentic-systems/reviews-archive/arsumbris.md).
- [x] **ATLAS** (`atlas`) — complete with recorded limits in [rolling execution 06](./rolling-06.md), run `AAS-2026-10-12-atlas-b28ea1ea613f-01`, boundary `65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988`; [overview](../../agentic-system-analyses/retained/atlas/overview.md); [audit](./audits/rolling-06-atlas.md); integration `707e4c8e3099af04ff13035086afb62eb7295134`; [legacy review](../../agent-memory-systems/reviews/atlas.md).
- [x] **Atomic** (`atomic`) — complete with recorded limits in [rolling execution 06](./rolling-06.md), run `AAS-2026-10-12-atomic-f98683232831-01`, boundary `983bea6baf449d060514c94b3b15b5f85f77ba9b`; [overview](../../agentic-system-analyses/retained/atomic/overview.md); [audit](./audits/rolling-06-atomic.md); integration `ad80113c9fb69e7b024f16f1203167c076035936`; [legacy review](../../agent-memory-systems/reviews/atomic.md).
- [ ] **Auto-claude-code-research-in-sleep** (`auto-claude-code-research-in-sleep`) — stopped in [rolling execution 07](./rolling-07.md), run `AAS-2026-10-13-auto-claude-code-research-in-sleep-68f17300f549-01`, source HEAD `26b95cfa0d8747078e9e43b42e20952709e561b8`; coordinator and report-verification provider overload, no publication/open attempts; unblock requires supported recovery direction; [legacy review](../../agent-memory-systems/reviews/Auto-claude-code-research-in-sleep.md).
- [ ] **auto-harness** (`auto-harness`) — stopped in [rolling execution 07](./rolling-07.md), run `AAS-2026-10-13-auto-harness-a6beadfe967c-01`, boundary `52360dbbeb8cea8886d90778e634a145c51da735`; report-verification worker provider overload, no publication/open attempts; unblock requires supported recovery direction; [legacy review](../../agent-memory-systems/reviews/auto-harness.md).
- [ ] **Autocontext** (`autocontext`) — assigned to [rolling execution 08](./rolling-08.md), fresh worktree `autocontext-6f1e750351ab`; source/run boundary pending; previously [released for a fresh rerun](./partial-outcomes-2026-10-13.md); preserve [rolling execution 07](./rolling-07.md) run `AAS-2026-10-13-autocontext-67e5d04eaa52-01`, boundary `f72c154152397f54d55407508b153d28861888a5`; only boundary accepted; runtime worker provider overload, no publication/open attempts; [legacy review](../../agent-memory-systems/reviews/autocontext.md).
- [ ] **Autogenesis** (`autogenesis`) — pending; [authored account](../../agentic-systems/reviews/autogenesis.md).
- [ ] **AutoSci** (`autosci`) — assigned to [rolling execution 08](./rolling-08.md), fresh worktree `autosci-19b6498edffe`; source/run boundary pending; previously [released for a fresh rerun](./partial-outcomes-2026-10-13.md); preserve [rolling execution 07](./rolling-07.md) run `AAS-2026-10-13-autosci-2422fc66dd8d-01`, boundary `f5c2fe009c6683b6aa5b668de759a0610c938aaf`; only boundary accepted; runtime worker stream ended before terminal response, no publication/open attempts; [legacy review](../../agent-memory-systems/reviews/AutoSci.md).
- [ ] **Awesome Agent Memory** (`awesome-agent-memory`) — pending; [legacy review](../../agent-memory-systems/reviews/Awesome-Agent-Memory.md).
- [ ] **Basic Memory** (`basic-memory`) — pending; [legacy review](../../agent-memory-systems/reviews/basic-memory.md).
- [ ] **beads_rust** (`beads-rust`) — pending; [authored account](../../agentic-systems/reviews/beads-rust.md).
- [ ] **Beever Atlas** (`beever-atlas`) — pending, [released for a fresh rerun](./partial-outcomes-2026-10-13.md); preserve [rolling execution 07](./rolling-07.md) run `AAS-2026-10-13-beever-atlas-1a34c0e1615d-01`, source HEAD `7d791af27ef4aa19644cb385c7ca24619bc4f848`; only boundary accepted; coordinator and runtime provider overload, no publication/open attempts; [legacy review](../../agent-memory-systems/reviews/beever-atlas.md).
- [ ] **Binder** (`binder`) — assigned to [rolling execution 08](./rolling-08.md), fresh worktree `binder-15e0514441cf`; source/run boundary pending; previously [released for a fresh rerun](./partial-outcomes-2026-10-13.md); preserve [rolling execution 07](./rolling-07.md) run `AAS-2026-10-13-binder-0ac507351cd6-01`, boundary `e4066d750ac5c6918706f44b12daa261b261106e`; only boundary accepted; runtime worker API 503, no publication/open attempts; [legacy review](../../agent-memory-systems/reviews/binder.md).
- [ ] **browzy.ai** (`browzy-ai`) — assigned to [rolling execution 08](./rolling-08.md), fresh worktree `browzy-ai-289663718f22`; source/run boundary pending; previously [released for a fresh rerun](./partial-outcomes-2026-10-13.md); preserve [rolling execution 07](./rolling-07.md) worktree `browzy-ai-3eb115584672`; coordinator provider overload before any discoverable run/source acquisition; no run identity, accepted member or publication established; [legacy review](../../agent-memory-systems/reviews/browzy-ai.md).
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

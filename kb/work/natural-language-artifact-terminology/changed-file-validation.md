# Changed-file validation

Corpus baseline: `b0147dc4`. Implemented corpus commit: `f5a4230b`.

The final library batch invoked `commonplace-validate` once for each of 259 changed KB Markdown artifacts. Because marked tag indexes are checked as dependents, those invocations emitted 309 validation results; all 309 were `Overall: PASS (clean)`. `AGENTS.md` is not a KB artifact and is covered by diff inspection plus `git diff --check`.

| changed file | row IDs | deterministic validation result |
|---|---|---|
| `AGENTS.md` | SP-0001–SP-0003 | N/A — root instruction; diff inspected and `git diff --check` clean |
| `kb/agent-memory-systems/README.md` | EX-0001–EX-0003 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/lightweight/IsaacCLupus_mnemosyn_spec.md` | EX-0004–EX-0009 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/lightweight/agemem.md` | EX-0010–EX-0012 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/lightweight/fintool.md` | EX-0013–EX-0014 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/lightweight/sig.md` | EX-0015–EX-0016 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/lightweight/trajectory-informed-memory-generation.md` | EX-0017–EX-0020 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/review-framework-design.md` | EX-0021–EX-0025, RS-0153–RS-0154 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/AI-Context-OS.md` | EX-0026–EX-0033 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/Agent-S.md` | EX-0034–EX-0047 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/AgentFly.md` | EX-0048–EX-0053 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/AriGraph.md` | EX-0054–EX-0058 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/Auto-claude-code-research-in-sleep.md` | EX-0059–EX-0068 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/AutoSci.md` | EX-0069–EX-0074 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/Awesome-Agent-Memory.md` | EX-0075–EX-0076 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/CORAL.md` | EX-0077–EX-0086 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/Closure-SDK.md` | EX-0087–EX-0094 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/HippoRAG.md` | EX-0095–EX-0099 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/KBLaM.md` | EX-0100–EX-0104 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/Kompl.md` | EX-0105–EX-0109 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/LLM-WIKI-MCP.md` | EX-0110–EX-0115 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/LLM-Wiki-v3.md` | EX-0116–EX-0118 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/MehmetGoekce--llm-wiki.md` | EX-0119–EX-0125 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/Memori.md` | EX-0126–EX-0131 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/MemoryOS.md` | EX-0132–EX-0136 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/MiroShark.md` | EX-0137–EX-0146 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/OS-Copilot.md` | EX-0147–EX-0150 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/OpenSage.md` | EX-0151–EX-0159 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/Pratiyush--llm-wiki.md` | EX-0160–EX-0164 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/REM.md` | EX-0165–EX-0171 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/ReframeWeb.md` | EX-0172–EX-0174 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/Self-Training-LLM.md` | EX-0175–EX-0179 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/SkillRL.md` | EX-0180–EX-0190 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/SkillWeaver.md` | EX-0191–EX-0200 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/SkillX.md` | EX-0201–EX-0208 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/TheKnowledge.md` | EX-0209–EX-0216 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/VLM-wiki.md` | EX-0217–EX-0227 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/WeKnora.md` | EX-0228–EX-0236 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/Zikkaron.md` | EX-0237–EX-0242 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/a-mem.md` | EX-0243–EX-0248 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/ace.md` | EX-0249–EX-0259 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/agent-r.md` | EX-0260–EX-0265 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/agent-skills-for-context-engineering.md` | EX-0266–EX-0281 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/agent-workflow-memory.md` | EX-0282–EX-0298 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/agentic-harness-engineering.md` | EX-0299–EX-0305 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/agentic-local-brain.md` | EX-0306–EX-0314 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/ai-memex-cli.md` | EX-0315–EX-0322 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/amazon-science--SAGE.md` | EX-0323–EX-0326 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/archie.md` | EX-0327–EX-0331 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/arscontexta.md` | EX-0332–EX-0340 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/atlas.md` | EX-0341–EX-0344 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/atomic.md` | EX-0345–EX-0352 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/auto-harness.md` | EX-0353–EX-0361 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/autocontext.md` | EX-0362–EX-0373 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/basic-memory.md` | EX-0374–EX-0379 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/beever-atlas.md` | EX-0380–EX-0393 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/binder.md` | EX-0394–EX-0399 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/browzy-ai.md` | EX-0400–EX-0406 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/byterover-cli.md` | EX-0407–EX-0414 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/cass_memory_system.md` | EX-0415–EX-0424 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/claude-context-guard.md` | EX-0425–EX-0437 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/claude-obsidian.md` | EX-0438–EX-0445 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/claude-workstream-kit.md` | EX-0446–EX-0454 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/clawvault.md` | EX-0455–EX-0462 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/cludebot.md` | EX-0463–EX-0474 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/cobusgreyling--llm-wiki.md` | EX-0475–EX-0480 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/cocoindex.md` | EX-0481–EX-0484 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/cognee.md` | EX-0485–EX-0492 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/compound-engineering-plugin.md` | EX-0493–EX-0500 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/context-constitution.md` | EX-0501–EX-0506 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/continuity.md` | EX-0507–EX-0516 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/cortex.md` | EX-0517–EX-0525 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/cq.md` | EX-0526–EX-0537 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/crewai-memory.md` | EX-0538–EX-0549 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/decapod.md` | EX-0550–EX-0559 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/deja-vu.md` | EX-0560–EX-0566 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/dense-mem.md` | EX-0567–EX-0576 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/docmason.md` | EX-0577–EX-0581 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/dynamic-cheatsheet.md` | EX-0582–EX-0591 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/echel.md` | EX-0592–EX-0594 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/echoes-vault-opencode.md` | EX-0595–EX-0598 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/echowiki.md` | EX-0599–EX-0601 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/eidetic.md` | EX-0602–EX-0608 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/engraph.md` | EX-0609–EX-0610 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/equipa.md` | EX-0611–EX-0623 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/exo.md` | EX-0624–EX-0633 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/exocomp.md` | EX-0634–EX-0641 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/expel.md` | EX-0642–EX-0645 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/funes.md` | EX-0646–EX-0653 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/g-memory.md` | EX-0654–EX-0659 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/gbrain.md` | EX-0660–EX-0664 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/getsentry-skills.md` | EX-0665–EX-0671 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/gnosis.md` | EX-0672–EX-0674 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/graphiti.md` | EX-0675–EX-0682 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/halo.md` | EX-0683–EX-0686 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/hermes-agent.md` | EX-0687–EX-0697 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/hindsight.md` | EX-0698–EX-0707 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/hyalo.md` | EX-0708–EX-0712 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/hyperagents.md` | EX-0713–EX-0719 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/interview-doc-agent.md` | EX-0720–EX-0726 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/kenhuangus--llm-wiki.md` | EX-0727–EX-0735 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/kgai.md` | EX-0736–EX-0744 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/lacp.md` | EX-0745–EX-0749 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/letta.md` | EX-0750–EX-0755 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/link.md` | EX-0756–EX-0763 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/llm-context-base.md` | EX-0764–EX-0770 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/llm-project-wiki.md` | EX-0771–EX-0774 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/llm-wiki-coordination.md` | EX-0775–EX-0778 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/llm-wiki.md` | EX-0779–EX-0783 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/llmwiki-marimo.md` | EX-0784–EX-0786 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/mem0.md` | EX-0787–EX-0792 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/memex.md` | EX-0793–EX-0798 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/mempalace.md` | EX-0799–EX-0802 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/memwiki.md` | EX-0803–EX-0816 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/mentisdb.md` | EX-0817–EX-0822 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/meta-harness.md` | EX-0823–EX-0826 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/nao.md` | EX-0827–EX-0831 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/napkin.md` | EX-0832–EX-0839 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/nuggets.md` | EX-0840–EX-0847 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/o-o.md` | EX-0848–EX-0850 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/okf-harness.md` | EX-0851–EX-0855 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/openclerk.md` | EX-0856–EX-0858 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/openviking.md` | EX-0859–EX-0863 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/openwiki.md` | EX-0864–EX-0866 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/operational-ontology-framework.md` | EX-0867–EX-0869 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/origin.md` | EX-0870–EX-0880 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/pal.md` | EX-0881–EX-0888 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/phantom.md` | EX-0889–EX-0897 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/pi-self-learning.md` | EX-0898–EX-0908 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/playground.md` | EX-0909–EX-0913 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/quicky-wiki.md` | EX-0914–EX-0918 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/reasoning-bank.md` | EX-0919–EX-0928 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/reflexion.md` | EX-0929–EX-0940 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/sage-wiki.md` | EX-0941–EX-0950 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/sage.md` | EX-0951–EX-0957 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/secure-llm-wiki.md` | EX-0958–EX-0962 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/semiont.md` | EX-0963–EX-0965 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/sift-kg.md` | EX-0966–EX-0969 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/siftly.md` | EX-0970–EX-0974 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/signetai.md` | EX-0975–EX-0979 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/skillnote.md` | EX-0980–EX-0989 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/smriti-mcp.md` | EX-0990–EX-0995 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/spacebot.md` | EX-0996–EX-1001 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/sparks.md` | EX-1002–EX-1009 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/stash.md` | EX-1010–EX-1011 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/supermemory.md` | EX-1012–EX-1017 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/swamp.md` | EX-1018–EX-1022 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/synapptic.md` | EX-1023–EX-1029 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/synthadoc.md` | EX-1030–EX-1034 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/synto.md` | EX-1035–EX-1040 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/tendril.md` | EX-1041–EX-1048 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/thalo.md` | EX-1049–EX-1055 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/theafh--ai-modules.md` | EX-1056–EX-1074 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/tolaria.md` | EX-1075–EX-1076 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/tracecraft.md` | EX-1077–EX-1079 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/virtual-context.md` | EX-1080–EX-1087 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/voiden.md` | EX-1088–EX-1090 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/voyager.md` | EX-1091–EX-1098 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/wuphf.md` | EX-1099–EX-1104 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/reviews/xMemory.md` | EX-1105–EX-1110 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/trace-learning-techniques-in-related-systems.md` | EX-1111–EX-1127 | PASS — `commonplace-validate` (final library batch) |
| `kb/agent-memory-systems/types/agent-memory-system-review.md` | EX-1128–EX-1139 | PASS — `commonplace-validate` (final library batch) |
| `kb/agentic-systems/claude-code-dynamic-workflows.md` | EX-1140 | PASS — `commonplace-validate` (final library batch) |
| `kb/agentic-systems/gbrain.md` | EX-1141–EX-1148 | PASS — `commonplace-validate` (final library batch) |
| `kb/agentic-systems/semantic-engine.md` | EX-1149 | PASS — `commonplace-validate` (final library batch) |
| `kb/instructions/FIX-SYSTEM.md` | RT-0001 | PASS — `commonplace-validate` (final library batch) |
| `kb/instructions/ingest-directory.md` | RT-0002 | PASS — `commonplace-validate` (final library batch) |
| `kb/instructions/migrate-semantics-preserving-gate-changes.md` | RT-0003 | PASS — `commonplace-validate` (final library batch) |
| `kb/instructions/refresh-agent-memory-review-taxonomy.md` | RT-0004–RT-0007 | PASS — `commonplace-validate` (final library batch) |
| `kb/instructions/write-agent-memory-system-review/SKILL.md` | RT-0008 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` | NT-0001–NT-0005, RS-0009 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md` | NT-0006 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/agent-memory-requirements/activate-behavior-changing-memory.md` | NT-0007 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md` | NT-0008–NT-0009 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md` | NT-0010–NT-0011 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/agent-memory-requirements/retire-redact-supersede-relax.md` | NT-0012 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md` | NT-0013–NT-0018 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/agentic-systems-interpret-underspecified-instructions.md` | NT-0019–NT-0020, NT-0270 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/an-action-model-matters-only-through-its-consumption-path.md` | NT-0021–NT-0023 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/artifact-analysis-README.md` | NT-0024–NT-0025, RS-0025 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/axes-of-artifact-analysis.md` | SP-0004–SP-0031 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/changing-requirements-conflate-genuine-change-with-disambiguation.md` | NT-0026 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/commitment-not-derivation-creates-new-ground-truth.md` | NT-0027–NT-0032 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md` | NT-0033 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/computational-model-README.md` | NT-0034–NT-0035, RS-0010 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/definitions/actionable-methodology.md` | NT-0036 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/definitions/behavior-determining-organization.md` | NT-0037 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/definitions/behavioral-authority.md` | NT-0038 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/definitions/codification.md` | SP-0032–SP-0039 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/definitions/constraining.md` | SP-0040 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/definitions/knowledge-artifact.md` | NT-0039 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/definitions/operative-part.md` | NT-0040–NT-0045 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/definitions/reach-assessment.md` | SP-0041–SP-0048 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/definitions/representational-form.md` | SP-0049–SP-0057, RS-0026–RS-0028 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/definitions/storage-substrate.md` | NT-0046–NT-0047 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/definitions/system-definition-artifact.md` | NT-0048–NT-0049 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/deploy-time-learning-README.md` | NT-0050 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/deploy-time-learning-is-the-missing-middle.md` | NT-0051–NT-0058 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/designing-agent-memory-systems.md` | NT-0059–NT-0060 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/enforcement-without-structured-recovery-is-incomplete.md` | NT-0061 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md` | NT-0062–NT-0066 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/frontloading-spares-execution-context.md` | NT-0067 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md` | NT-0068–NT-0070 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md` | NT-0071–NT-0096 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/information-value-is-observer-relative.md` | NT-0097–NT-0098 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/llm-context-is-composed-without-scoping.md` | NT-0099–NT-0106, RS-0001 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/llm-executed-methodologies-are-metacircular-interpreters.md` | NT-0107–NT-0112 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md` | NT-0113–NT-0115 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md` | NT-0116–NT-0117 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/memory-design-adds-operational-axes-to-artifact-analysis.md` | NT-0118–NT-0120 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/only-explicit-retention-is-durable-writable-and-addressable.md` | NT-0121–NT-0123 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/opacity-is-a-scale-threshold.md` | NT-0124 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/orchestration-needs-privilege-quarantine-not-permission-scope.md` | NT-0125–NT-0127 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md` | NT-0128–NT-0138 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md` | NT-0139–NT-0154 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/real-self-improving-systems-occupy-combinations-no-rung-captures.md` | NT-0155 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/reflective-coverage-is-graded-across-representational-forms.md` | NT-0156–NT-0165, RS-0024 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/research/adaptation-agentic-ai-analysis.md` | NT-0166–NT-0173 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/retrieval-failure-is-reflection-failure.md` | NT-0174–NT-0175 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md` | NT-0176–NT-0177 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/specification-level-separation-recovers-scoping-before-it-recovers.md` | NT-0178, RS-0002–RS-0004 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/specification-strategy-should-follow-where-understanding-lives.md` | NT-0179–NT-0182, NT-0271 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md` | NT-0183–NT-0197 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/technical-constraints-make-kb-objective-choice-engineering.md` | NT-0198–NT-0199 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md` | NT-0200–NT-0207 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md` | NT-0208–NT-0213 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md` | NT-0214–NT-0222 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md` | NT-0223–NT-0227 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/treat-continual-learning-as-substrate-coevolution.md` | NT-0228–NT-0237 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/verifiability-gradient.md` | NT-0238–NT-0239 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md` | NT-0240–NT-0251 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md` | NT-0252–NT-0265, NT-0272–NT-0273, RS-0019–RS-0020 | PASS — `commonplace-validate` (final library batch) |
| `kb/notes/world-models-assess-explanatory-reach-through-action-conditioned.md` | NT-0266–NT-0269 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/README-REVIEW-SYSTEM.md` | RT-0009–RT-0010, RS-0029–RS-0030 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md` | RT-0011, RS-0054–RS-0057 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/adr/012-types-for-structure-traits-for-review.md` | RT-0012–RT-0013, RS-0082 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/adr/016-custom-types-use-template-instruction-pairs.md` | RT-0014–RT-0015 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/adr/017-collection-md-is-the-register-convention-boundary.md` | RT-0016 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/adr/018-types-are-path-references-to-instruction-docs.md` | RT-0017–RT-0019, RS-0038–RS-0048 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/adr/021-shipping-model-path-audit-option-e.md` | RT-0020–RT-0021, RS-0083–RS-0089 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md` | RT-0022 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/agent-memory-coverage.md` | RT-0023–RT-0024 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/architecture.md` | RT-0025 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/collections-and-types.md` | RT-0026–RT-0027 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/collections-never-own-frontmatter-semantics.md` | RT-0028–RT-0030 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/commonplace-agent-memory-gap-plan.md` | RT-0031 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/commonplace-as-a-reflective-system.md` | RT-0032–RT-0037 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/lib-modules.md` | RT-0038 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/link-vocabulary.md` | RT-0039–RT-0040 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/proposals/README.md` | RT-0041 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/proposals/a-reader-facing-banner-for-user-verification.md` | RT-0042, RS-0109 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/proposals/channel-compiled-instruction-artifacts.md` | RT-0043–RT-0045 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/proposals/where-subtree-scoped-write-time-contracts-live.md` | RT-0046–RT-0049 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/proposals/write-time-vocabulary-collision-controls.md` | RT-0050, RS-0105 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/review-architecture.md` | RT-0051 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/tag-readme-trace-observed-causal-connection.md` | RT-0052–RT-0056 | PASS — `commonplace-validate` (final library batch) |
| `kb/reference/validation-contract.md` | RT-0057–RT-0060 | PASS — `commonplace-validate` (final library batch) |
| `kb/types/review-gate.md` | RT-0061–RT-0062, RS-0152 | PASS — `commonplace-validate` (final library batch) |
| `kb/types/tag-readme.md` | RT-0063 | PASS — `commonplace-validate` (final library batch) |
| `kb/types/type-spec.md` | RT-0064–RT-0068 | PASS — `commonplace-validate` (final library batch) |

## Handoff control artifacts

These files carry the audit and handoff rather than migrated source occurrences. They are validated as text artifacts in the final handoff batch.

| changed file | row IDs | deterministic validation result |
|---|---|---|
| `kb/work/natural-language-artifact-terminology/migration-ledger.md` | control artifact — no occurrence rows | PASS — `commonplace-validate` (final handoff batch) |
| `kb/work/natural-language-artifact-terminology/migration-rows-spine.md` | control artifact — no occurrence rows | PASS — `commonplace-validate` (final handoff batch) |
| `kb/work/natural-language-artifact-terminology/migration-rows-notes.md` | control artifact — no occurrence rows | PASS — `commonplace-validate` (final handoff batch) |
| `kb/work/natural-language-artifact-terminology/migration-rows-reference-instructions-types.md` | control artifact — no occurrence rows | PASS — `commonplace-validate` (final handoff batch) |
| `kb/work/natural-language-artifact-terminology/migration-rows-external-systems.md` | control artifact — no occurrence rows | PASS — `commonplace-validate` (final handoff batch) |
| `kb/work/natural-language-artifact-terminology/migration-rows-residual-exceptions.md` | control artifact — no occurrence rows | PASS — `commonplace-validate` (final handoff batch) |
| `kb/work/natural-language-artifact-terminology/changed-file-validation.md` | control artifact — no occurrence rows | PASS — `commonplace-validate` (final handoff batch) |
| `kb/work/natural-language-artifact-terminology/lessons-learned.md` | control artifact — no occurrence rows | PASS — `commonplace-validate` (final handoff batch) |

## Verification-remediation addendum

Remediation start: `b2d03311`. Repaired corpus commit: `760bf239`. This addendum covers every file changed by the correction pass; the earlier table remains the audit for the original migration.

### Repaired library Markdown

`commonplace-validate` passed on every file below. The two noted description-length warnings predate the remediation and do not affect the changed body text.

| changed file | reopened row IDs | deterministic validation result |
|---|---|---|
| `kb/notes/axes-of-artifact-analysis.md` | SP-0012 | PASS — 1 pre-existing description-length warning |
| `kb/notes/commitment-not-derivation-creates-new-ground-truth.md` | NT-0029, NT-0030 | PASS — clean |
| `kb/notes/definitions/actionable-methodology.md` | NT-0036 | PASS — clean |
| `kb/notes/deploy-time-learning-is-the-missing-middle.md` | NT-0056 | PASS — clean |
| `kb/notes/improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md` | NT-0091 | PASS — clean |
| `kb/notes/llm-executed-methodologies-are-metacircular-interpreters.md` | NT-0108, NT-0111 | PASS — clean |
| `kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md` | NT-0130, NT-0131, NT-0132 | PASS — clean |
| `kb/notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md` | NT-0189 | PASS — 1 pre-existing description-length warning |
| `kb/notes/technical-constraints-make-kb-objective-choice-engineering.md` | NT-0198, NT-0199 | PASS — clean |
| `kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md` | NT-0218, NT-0220 | PASS — clean |
| `kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md` | NT-0226, NT-0227 | PASS — clean |
| `kb/notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md` | NT-0243, NT-0244 | PASS — clean |
| `kb/notes/world-models-assess-explanatory-reach-through-action-conditioned.md` | NT-0268 | PASS — clean |
| `kb/reference/adr/021-shipping-model-path-audit-option-e.md` | RT-0020, RT-0021 | PASS — clean |
| `kb/reference/collections-never-own-frontmatter-semantics.md` | RT-0028 | PASS — clean |
| `kb/reference/lib-modules.md` | RT-0038 | PASS — clean |
| `kb/reference/validation-contract.md` | RT-0057 | PASS — clean |
| `kb/agent-memory-systems/lightweight/trajectory-informed-memory-generation.md` | EX-0019 | PASS — clean |
| `kb/agent-memory-systems/reviews/AgentFly.md` | EX-0053 | PASS — clean |
| `kb/agent-memory-systems/reviews/OpenSage.md` | EX-0157 | PASS — clean |
| `kb/agent-memory-systems/reviews/agent-skills-for-context-engineering.md` | EX-0278 | PASS — clean |
| `kb/agent-memory-systems/reviews/agentic-local-brain.md` | EX-0308 | PASS — clean |
| `kb/agent-memory-systems/reviews/autocontext.md` | EX-0371 | PASS — clean |
| `kb/agent-memory-systems/reviews/basic-memory.md` | EX-0377 | PASS — clean |
| `kb/agent-memory-systems/reviews/claude-obsidian.md` | EX-0443 | PASS — clean |
| `kb/agent-memory-systems/reviews/context-constitution.md` | EX-0501 | PASS — clean |
| `kb/agent-memory-systems/reviews/cortex.md` | EX-0522 | PASS — clean |
| `kb/agent-memory-systems/reviews/deja-vu.md` | EX-0564 | PASS — clean |
| `kb/agent-memory-systems/reviews/eidetic.md` | EX-0605 | PASS — clean |
| `kb/agent-memory-systems/reviews/equipa.md` | EX-0617, EX-0618, EX-0621, EX-0622 | PASS — clean |
| `kb/agent-memory-systems/reviews/exocomp.md` | EX-0638, EX-0639 | PASS — clean |
| `kb/agent-memory-systems/reviews/hyalo.md` | EX-0710 | PASS — clean |
| `kb/agent-memory-systems/reviews/llm-wiki-coordination.md` | EX-0777 | PASS — clean |
| `kb/agent-memory-systems/reviews/o-o.md` | EX-0850 | PASS — clean |
| `kb/agent-memory-systems/reviews/quicky-wiki.md` | EX-0918 | PASS — clean |
| `kb/agent-memory-systems/reviews/sage-wiki.md` | EX-0941 | PASS — clean |
| `kb/agent-memory-systems/reviews/smriti-mcp.md` | EX-0992, EX-0993 | PASS — clean |
| `kb/agent-memory-systems/reviews/sparks.md` | EX-1006 | PASS — clean |
| `kb/agent-memory-systems/reviews/stash.md` | EX-1010, EX-1011 | PASS — clean |
| `kb/agent-memory-systems/reviews/synthadoc.md` | EX-1032 | PASS — clean |
| `kb/agent-memory-systems/reviews/virtual-context.md` | EX-1085 | PASS — clean |
| `kb/agent-memory-systems/trace-learning-techniques-in-related-systems.md` | EX-1115, EX-1117 | PASS — clean |

### Executable and generated surfaces

| changed file | row IDs | verification result |
|---|---|---|
| `src/commonplace/lib/systems_matrix.py` | ES-0001–ES-0004 | Focused and full tests pass; active-vocabulary search clean |
| `tests/commonplace/lib/test_systems_matrix.py` | ES-0005–ES-0018 | 11 focused tests and 483 full-suite tests pass |
| `tests/commonplace/lib/fixtures/zikkaron_review.md` | ES-0019–ES-0027 | Parsed by focused tests; active-vocabulary search clean |
| `kb/agent-memory-systems/systems.csv` | ES-0028–ES-0181 | Regenerated; component-count audit 152/152 form, 94/94 distilled form, 151/151 mixed |

### Remediation control and evidence files

| changed file | row ownership | deterministic validation result |
|---|---|---|
| `kb/work/natural-language-artifact-terminology/README.md` | control artifact | PASS — clean |
| `kb/work/natural-language-artifact-terminology/remediation-plan.md` | control artifact | PASS — clean |
| `kb/work/natural-language-artifact-terminology/migration-rows-spine.md` | SP-0012 | PASS — clean |
| `kb/work/natural-language-artifact-terminology/migration-rows-notes.md` | NT-0029, NT-0030, NT-0036, NT-0056, NT-0091, NT-0108, NT-0111, NT-0130–NT-0132, NT-0189, NT-0198, NT-0199, NT-0218, NT-0220, NT-0226, NT-0227, NT-0243, NT-0244, NT-0268 | PASS — clean |
| `kb/work/natural-language-artifact-terminology/migration-rows-reference-instructions-types.md` | RT-0020, RT-0021, RT-0028, RT-0038, RT-0057 | PASS — clean |
| `kb/work/natural-language-artifact-terminology/migration-rows-external-systems.md` | 32 reopened EX rows listed in the manifest | PASS — clean |
| `kb/work/natural-language-artifact-terminology/migration-rows-executable-surface.md` | ES-0001–ES-0181 | PASS — clean |
| `kb/work/natural-language-artifact-terminology/migration-ledger.md` | manifest and reconciliation | PASS — clean |
| `kb/work/natural-language-artifact-terminology/changed-file-validation.md` | this mapping | PASS — clean |

The historical captures `kb/sources/where-it-lives-architectural-vocabulary-retained-adaptation.md` and `kb/sources/where-it-lives-retained-adaptation-2026-06-23.md` are unchanged from `b2d03311`. `git diff --check` is clean. All 1,903 semantic and executable occurrence rows remain verification-pending.

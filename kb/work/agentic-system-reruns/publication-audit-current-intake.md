# Current own-publication audit intake

## Result and authority

**169 live own completed publications** are fixed in the [machine intake](./publication-audit-current-intake.json), including **9 completed batch-18 publications**. This is inventory and exact-byte reconciliation only, not a semantic audit or permission to release holds, replace incumbents, accept or integrate.

Observation window: `2026-10-16T22:22:58.512515+00:00` through `2026-10-16T22:23:02.335679+00:00`. Origin HEAD: `0b74fc426143a1f91e83800f00b979271ad84363`; end HEAD: `0b74fc426143a1f91e83800f00b979271ad84363`.

Machine intake SHA-256: `29c5a94a2c926f9c8b895cf5a5f50b0157461fa2a8aff39779131d14ab6d530e`.

## Counts

| Class or check | Count |
| --- | ---: |
| integrated | 98 |
| reusable held | 22 |
| reusable positive | 6 |
| needs fresh audit | 43 |
| discovered-resolved-worktrees | 291 |
| registered-worktrees | 281 |
| live-own-completed-publications | 169 |
| live-publication-files | 2183 |
| canonical-incumbents | 135 |
| archived-prior-integrated-records | 37 |
| archived-current-canonical-byte-matches | 37 |
| incumbent-transfer-stops | 17 |
| unbound-hold-recommendations | 1 |
| completed-batch18-publications | 9 |
| unpublished-or-potentially-active-own-runs-excluded | 87 |
| unpublished-batch18-own-runs-excluded | 7 |
| discovery-gaps | 1 |
| all-live-maps-match-effect | 169 |
| all-manifest-member-pins-match | 169 |
| prior-live-runs-reconciled | 160 |
| new-or-unaudited-excluding-unbound-hold | 42 |
| nonintegrated-live-publications | 71 |
| attributed-hold-recommendations | 23 |

The 43 fresh-audit rows comprise 33 still-unaudited older publications, nine completed batch-18 publications and the historically unbound Dynamic Cheatsheet hold. The six reusable positives are alternatives with incumbent-transfer stops, not ready replacements.

Live classifications are mutually exclusive. Incumbent-transfer stops and unbound holds are separate axes. Integrated means exact run ID and complete recursive current bytes equal a source-matched canonical set, not a fresh audit result. Archived records are historical carry-forward, not live publications.

## Discovery and evidence

Registered worktrees came from `git --no-optional-locks worktree list --porcelain`. Immediate directories under both commissioned roots were added; resolved worktree and run paths were deduplicated. The JSON retains raw registrations, directory discoveries, exact paths, preparation and opening metadata, method/source identities, full recursive publication/effect maps, publish pins, attempt metadata, pending resets, non-completed effects, integration records and canonical maps. Inherited retained files do not establish own publication.

Own-publication membership requires a run definition selected by preparation token (or name-derived fallback), a completed publish effect naming that run, and a destination inside that worktree. Literal publication/run/effect agreement is checked independently. No target source checkout or live trace was opened. Filename leads are not compliance evidence.

The complete prior JSON was parsed and all live and archive structures processed programmatically. Audit reuse requires a bound prior full map and literal source record, not a same-source title. Later coordinator decisions are attributed through the hash-bound intake. Renewed Supermemory has an explicit report-bound canonical JSON map digest. Dynamic Cheatsheet `11e3e77c2265` remains historically unbound; its depth diagnosis is not clearance.

All 160 prior live own runs reconcile. Only AI Memex CLI and Supermemory differ from their prior intake maps, as recorded by the re-entry evidence. AI Memex now exactly matches its integrated qualified publication. Supermemory matches its renewed report-bound hold. All 169 current publication maps equal their completed effects, all assembled member pins match, and all opening records agree on run, source identity and method. No open attempt, pending reset or non-completed current effect was observed among these published rows. These metadata checks do not certify worker compliance.

## Preserved stops and gaps

**23 attributed hold recommendations** remain holds, including the unbound Dynamic Cheatsheet hold. Batch-19 reserved-owner/compliance and four operational holds remain separate from content recovery. Selection does not authorize a reset or release a hold.

**17 nonintegrated candidates have source-matched canonical incumbents.** Every transfer remains stopped, including positive alternatives. The JSON links each incumbent to its complete exact current map. No replacement was selected.

**Explicit discovery gap:** `https://github.com/Versatly/clawvault` is one of the seventeen batch-18 source identities, but no current batch-18 worktree or preparation was found in the registered/immediate discovery roots. A `batch-18/clawvault.output` filename exists; it was not opened. No current run ID, completion or failure is inferred. The older unpublished `d44ad402971c` run is separately excluded. This yields nine completed publications, seven unpublished run IDs and one missing batch-18 worktree identity—not seventeen completed analyses.

Activity cannot safely be inferred from absence of publication. Every unpublished or potentially active own run is excluded and listed in JSON. Batch-18 point-in-time exclusions follow; their attempts, jobs, handouts and logs were not opened:

- `AAS-2026-10-16-cortex-a11f1b1f5b26-01` — no completed own publish effect; activity unverified.
- `AAS-2026-10-16-llm-wiki-0756aa1691c4-01` — no completed own publish effect; activity unverified.
- `AAS-2026-10-16-llm-wiki-38d98e5340c9-01` — no completed own publish effect; activity unverified.
- `AAS-2026-10-16-memori-42d7741038da-01` — no completed own publish effect; activity unverified.
- `AAS-2026-10-16-llm-wiki-e6401f1dede5-01` — no completed own publish effect; activity unverified.
- `AAS-2026-10-16-pal-94ed103de680-01` — no completed own publish effect; activity unverified.
- `AAS-2026-10-16-semantic-engine-35fd15aefe82-01` — no completed own publish effect; activity unverified.

This does not assert all those runs are still executing. No process-liveness check was made. Only completed batch-18 publications enter the queue. Later arrivals require a new inventory. Arbitrary nonstandard state roots and unidentifiable own runs remain discovery limits rather than inferred completeness.

## Fixed live-publication register

New, unbound and uncertain rows have unique proposed report paths under `audits/current-publications/<run-id>.md` in the JSON. These are reservations, not created files or audit assignments. Historical and trace leads are per-row; missing leads remain gaps. Full hashes and exact run/preparation/command paths are in JSON.

| Exact run | Classification | Source identity | Incumbent transfer |
| --- | --- | --- | --- |
| `AAS-2026-10-12-2601-01885v1-32274e5bddc1-01` | integrated | `https://arxiv.org/html/2601.01885v1` | integrated |
| `AAS-2026-10-12-agent-skills-for-context-engineering-2423c2f20f83-01` | reusable held | `https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering` | no incumbent |
| `AAS-2026-10-14-ai-modules-a7044d5627d2-01` | integrated | `https://github.com/TheAFH/ai-modules` | integrated |
| `AAS-2026-10-14-2609-26457-6b3bcd4791cf-01` | integrated | `https://arxiv.org/abs/2609.26457` | integrated |
| `AAS-2026-10-14-workflows-f9c2f80a3a94-01` | integrated | `https://code.claude.com/docs/en/workflows` | integrated |
| `AAS-2026-10-13-contextpilot-30d0d09e6cdc-01` | reusable held | `https://github.com/Tencent/ContextPilot` | no incumbent |
| `AAS-2026-10-14-deja-vu-22137d4d39a5-01` | integrated | `https://github.com/vshulcz/deja-vu` | integrated |
| `AAS-2026-10-10-dynamic-cheatsheet-004374829a63-01` | reusable positive | `https://github.com/suzgunmirac/dynamic-cheatsheet` | STOP |
| `AAS-2026-10-15-dynamic-cheatsheet-11e3e77c2265-01` | needs fresh audit; unbound hold | `https://github.com/suzgunmirac/dynamic-cheatsheet` | STOP |
| `AAS-2026-10-09-dynamic-cheatsheet-2529cdc2795b-01` | reusable held | `https://github.com/suzgunmirac/dynamic-cheatsheet` | STOP |
| `AAS-2026-10-10-dynamic-cheatsheet-41e85fccfcaf-01` | reusable positive | `https://github.com/suzgunmirac/dynamic-cheatsheet` | STOP |
| `AAS-2026-10-10-dynamic-cheatsheet-43cd203254e8-01` | reusable positive | `https://github.com/suzgunmirac/dynamic-cheatsheet` | STOP |
| `AAS-2026-10-14-engraph-0cd4f00695b0-01` | integrated | `https://github.com/devwhodevs/engraph` | integrated |
| `AAS-2026-10-14-fractal-ee03010af4c2-01` | integrated | `https://github.com/trampoline-ai/fractal` | integrated |
| `AAS-2026-10-13-gbrain-ab46e8c48dba-01` | reusable held | `https://github.com/garrytan/gbrain` | STOP |
| `AAS-2026-10-11-graphiti-4896fccada9e-01` | reusable held | `https://github.com/getzep/graphiti` | STOP |
| `AAS-2026-10-10-graphiti-5833fd846841-01` | reusable held | `https://github.com/getzep/graphiti` | STOP |
| `AAS-2026-10-11-graphiti-72c99440b180-01` | reusable held | `https://github.com/getzep/graphiti` | STOP |
| `AAS-2026-10-10-graphiti-85a21a06d35c-01` | reusable held | `https://github.com/getzep/graphiti` | STOP |
| `AAS-2026-10-14-halo-c4ed89d7f99f-01` | integrated | `https://github.com/context-labs/halo` | integrated |
| `AAS-2026-10-14-hermes-agent-bfb4bdc54d37-01` | integrated | `https://github.com/nousresearch/hermes-agent` | integrated |
| `AAS-2026-10-14-hindsight-34c2ca821edf-01` | integrated | `https://github.com/vectorize-io/hindsight` | integrated |
| `AAS-2026-10-14-hyalo-ffe11d6a6d56-01` | integrated | `https://github.com/ractive/hyalo` | integrated |
| `AAS-2026-10-14-hyperagents-dd9d501b160c-01` | integrated | `https://github.com/facebookresearch/Hyperagents` | integrated |
| `AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01` | integrated | `https://people.idsia.ch/~juergen/fki198-94.pdf` | integrated |
| `AAS-2026-10-14-interview-doc-agent-c7597c33f23d-01` | integrated | `https://github.com/Shilren/interview-doc-agent` | integrated |
| `AAS-2026-10-15-jaz-a94bea79c61a-01` | reusable held | `https://github.com/jaz-lang/JAZ` | no incumbent |
| `AAS-2026-10-15-jaz-evals-17ab95f93794-01` | integrated | `https://github.com/jaz-lang/jaz-evals` | integrated |
| `AAS-2026-10-15-jepa-anything-434b01ab7774-01` | integrated | `https://github.com/Gen-Verse/JEPA-Anything` | integrated |
| `AAS-2026-10-14-kgai-54bcae52e039-01` | integrated | `https://github.com/kgaidev/kgai` | integrated |
| `AAS-2026-10-14-kompl-9cffb1e5eb86-01` | integrated | `https://github.com/tuirk/Kompl` | integrated |
| `AAS-2026-10-14-lacp-91efd16f7a35-01` | integrated | `https://github.com/0xNyk/lacp` | integrated |
| `AAS-2026-10-11-letta-code-88afa3263646-01` | reusable positive | `https://github.com/letta-ai/letta-code` | STOP |
| `AAS-2026-10-11-letta-code-9d060e7dab7e-01` | reusable positive | `https://github.com/letta-ai/letta-code` | STOP |
| `AAS-2026-10-13-letta-code-7b0fd36d07f0-01` | reusable positive | `https://github.com/letta-ai/letta-code` | STOP |
| `AAS-2026-10-11-letta-code-f54d2479889e-01` | reusable held | `https://github.com/letta-ai/letta-code` | STOP |
| `AAS-2026-10-15-lhtb-a0548ba4edbf-01` | integrated | `https://github.com/zli12321/lhtb` | integrated |
| `AAS-2026-10-14-link-595f6f9cba36-01` | integrated | `https://github.com/gowtham0992/link` | integrated |
| `AAS-2026-10-14-llm-context-base-f63a7c0fb5f2-01` | integrated | `https://github.com/asakin/llm-context-base` | integrated |
| `AAS-2026-10-14-llm-project-wiki-c6c664168f3e-01` | integrated | `https://github.com/akash-r34/llm-project-wiki` | integrated |
| `AAS-2026-10-14-llm-wiki-coordination-a12f3c7007f2-01` | integrated | `https://github.com/AEVYRA/llm-wiki-coordination` | integrated |
| `AAS-2026-10-14-llm-wiki-v3-3bd68241f463-01` | reusable held | `https://github.com/vvvvvivekkk/LLM-Wiki-v3` | no incumbent |
| `AAS-2026-10-14-llmwiki-marimo-56b2c84667fe-01` | reusable held | `https://github.com/Clod/llmwiki-marimo` | no incumbent |
| `AAS-2026-10-14-mem0-5b642a1731b4-01` | integrated | `https://github.com/mem0ai/mem0` | integrated |
| `AAS-2026-10-14-memex-42ecde52cc05-01` | integrated | `https://github.com/wastedcode/memex` | integrated |
| `AAS-2026-10-14-mempalace-ed71875aea5a-01` | integrated | `https://github.com/milla-jovovich/mempalace` | integrated |
| `AAS-2026-10-14-memwiki-79dcc4d04bcb-01` | integrated | `https://github.com/hereisSwapnil/memwiki` | integrated |
| `AAS-2026-10-14-mentisdb-a8b5903ae3e2-01` | integrated | `https://github.com/cloudllm-ai/mentisdb` | integrated |
| `AAS-2026-10-15-merchantbench-d2f4d78dbe37-01` | needs fresh audit | `https://github.com/khancold/MerchantBench` | no incumbent |
| `AAS-2026-10-14-meta-harness-5e480e270fee-01` | integrated | `https://github.com/stanford-iris-lab/meta-harness` | integrated |
| `AAS-2026-10-14-meta-n-18c23b6f8bb4-01` | integrated | `https://github.com/MinnesotaNLP/Meta-n` | integrated |
| `AAS-2026-10-14-modularrsi-96b89989168e-01` | reusable held | `https://github.com/IQuestLab/ModularRSI` | no incumbent |
| `AAS-2026-10-14-from-agent-memory-to-portable-skills-605887a7f7a0-01` | reusable held | `https://neo4j.com/blog/genai/from-agent-memory-to-portable-skills` | no incumbent |
| `AAS-2026-10-14-nao-f9d36a4b7276-01` | integrated | `https://github.com/getnao/nao` | integrated |
| `AAS-2026-10-11-napkin-1b60c5d21780-01` | reusable held | `https://github.com/Michaelliv/napkin` | STOP |
| `AAS-2026-10-11-napkin-28752ba411ea-01` | reusable held | `https://github.com/Michaelliv/napkin` | STOP |
| `AAS-2026-10-10-napkin-b831630d0978-01` | reusable held | `https://github.com/Michaelliv/napkin` | STOP |
| `AAS-2026-10-14-nuggets-c2e87e6916cc-01` | integrated | `https://github.com/NeoVertex1/nuggets` | integrated |
| `AAS-2026-10-14-oh-my-pi-c0ffc54ff768-01` | integrated | `https://github.com/can1357/oh-my-pi` | integrated |
| `AAS-2026-10-15-okf-harness-6bf5507fbdbf-01` | integrated | `https://github.com/pumblus/okf-harness` | integrated |
| `AAS-2026-10-14-openrsi-c72dec9967a3-01` | reusable held | `https://github.com/FrontisAI/OpenRSI` | no incumbent |
| `AAS-2026-10-14-opensage-291d1ed79d37-01` | integrated | `https://github.com/opensage-agent/OpenSage` | integrated |
| `AAS-2026-10-14-openviking-7b5b57541af5-01` | integrated | `https://github.com/volcengine/OpenViking` | integrated |
| `AAS-2026-10-14-openwiki-8f502f680f75-01` | integrated | `https://github.com/langchain-ai/openwiki` | integrated |
| `AAS-2026-10-15-pageindex-50056ef72767-01` | integrated | `https://github.com/VectifyAI/PageIndex` | integrated |
| `AAS-2026-10-15-phantom-cc566f03ac40-01` | integrated | `https://github.com/ghostwright/phantom` | integrated |
| `AAS-2026-10-14-pi-posthorse-58b9647d2f29-01` | integrated | `https://github.com/fitchmultz/pi-posthorse` | integrated |
| `AAS-2026-10-15-pi-self-learning-1a318610d4b1-01` | integrated | `https://github.com/mcollina/pi-self-learning` | integrated |
| `AAS-2026-10-14-playground-88ee8a292f9b-01` | integrated | `https://github.com/triblespace/playground` | integrated |
| `AAS-2026-10-14-pond-7a589a889ca1-01` | integrated | `https://github.com/tenequm/pond` | integrated |
| `AAS-2026-10-14-prime-agent-8ec59ae12476-01` | integrated | `https://github.com/PrimeIntellect-ai/prime-agent` | integrated |
| `AAS-2026-10-14-primescientist-f880686cf98a-01` | integrated | `https://github.com/henri-xyu02/PrimeScientist` | integrated |
| `AAS-2026-10-14-prove2me-workspace-187ef30582c9-01` | integrated | `https://github.com/prove2me/Prove2Me_workspace` | integrated |
| `AAS-2026-10-15-qwenpaw-e41495d47fc0-01` | integrated | `https://github.com/niceirene/qwenpaw` | integrated |
| `AAS-2026-10-14-reasoning-bank-f0bedcab086c-01` | integrated | `https://github.com/google-research/reasoning-bank` | integrated |
| `AAS-2026-10-14-reflexion-19159b69b712-01` | integrated | `https://github.com/noahshinn/reflexion` | integrated |
| `AAS-2026-10-14-reframeweb-cff918d7eb1e-01` | integrated | `https://github.com/jubjub727/ReframeWeb` | integrated |
| `AAS-2026-10-14-rem-a81fdc774400-01` | integrated | `https://github.com/satyammistari/REM` | integrated |
| `AAS-2026-10-14-rsiagent-b11225763c0b-01` | integrated | `https://github.com/AetherLabsAI/RSIAgent` | integrated |
| `AAS-2026-10-15-sage-d3843de6d2dd-01` | integrated | `https://github.com/l33tdawg/sage` | integrated |
| `AAS-2026-10-15-sage-wiki-cc43456fb833-01` | integrated | `https://github.com/xoai/sage-wiki` | integrated |
| `AAS-2026-10-15-self-training-llm-5b5ee621bde2-01` | integrated | `https://github.com/wj210/Self-Training-LLM` | integrated |
| `AAS-2026-10-15-semiont-d516c7013d8f-01` | integrated | `https://github.com/The-AI-Alliance/semiont` | integrated |
| `AAS-2026-10-15-sift-kg-dca68bc45a2c-01` | needs fresh audit | `https://github.com/juanceresa/sift-kg` | no incumbent |
| `AAS-2026-10-15-siftly-71a1181fbc3d-01` | needs fresh audit | `https://github.com/ViperrCrypto/Siftly` | no incumbent |
| `AAS-2026-10-14-sig-releases-50379145ac31-01` | integrated | `https://github.com/sig-ai-app/sig-releases` | integrated |
| `AAS-2026-10-14-signetai-64f703d83203-01` | integrated | `https://github.com/signet-ai/signetai` | integrated |
| `AAS-2026-10-14-skilllift-0f350bf64418-01` | integrated | `https://github.com/walter-mitty-pro/SkillLift` | integrated |
| `AAS-2026-10-14-skillnote-0ccfe85cda4a-01` | integrated | `https://github.com/luna-prompts/SkillNote` | integrated |
| `AAS-2026-10-14-skillrl-0dba0e1c895e-01` | integrated | `https://github.com/aiming-lab/SkillRL` | integrated |
| `AAS-2026-10-14-skillweaver-c921cc7a5ed0-01` | integrated | `https://github.com/OSU-NLP-Group/SkillWeaver` | integrated |
| `AAS-2026-10-14-skillx-61e3fc8f9aa5-01` | integrated | `https://github.com/zjunlp/SkillX` | integrated |
| `AAS-2026-10-14-smriti-mcp-14f6928f9817-01` | integrated | `https://github.com/Deepak-Bhardwaj-PS/smriti-mcp` | integrated |
| `AAS-2026-10-14-sol-pi-42f04fbbc6bb-01` | integrated | `https://github.com/NVlabs/SoL-Pi` | integrated |
| `AAS-2026-10-14-spacebot-6a954b400f95-01` | integrated | `https://github.com/spacedriveapp/spacebot` | integrated |
| `AAS-2026-10-15-sparks-563865f8b26f-01` | integrated | `https://github.com/YogiRK/sparks` | integrated |
| `AAS-2026-10-15-stash-7ac5612837a0-01` | integrated | `https://github.com/alash3al/stash` | integrated |
| `AAS-2026-10-15-supermemory-ae21530d128d-01` | reusable held | `https://github.com/supermemoryai/supermemory` | no incumbent |
| `AAS-2026-10-15-swamp-440d19cc0bcc-01` | integrated | `https://github.com/swamp-club/swamp` | integrated |
| `AAS-2026-10-15-swarmworld-e39fbc17e3fb-01` | integrated | `https://github.com/lamm-mit/SwarmWorld` | integrated |
| `AAS-2026-10-15-synapptic-9dce97c66546-01` | integrated | `https://github.com/appcuarium/synapptic` | integrated |
| `AAS-2026-10-15-synthadoc-a3cae9152fff-01` | integrated | `https://github.com/axoviq-ai/synthadoc` | integrated |
| `AAS-2026-10-15-synto-eabcdcce3da2-01` | needs fresh audit | `https://github.com/kytmanov/synto` | no incumbent |
| `AAS-2026-10-15-talorys-7bce41ba9401-01` | needs fresh audit | `https://github.com/rociiu/talorys` | no incumbent |
| `AAS-2026-10-15-tardigrade-455e1aaccd4d-01` | needs fresh audit | `https://github.com/clavia-labs/tardigrade` | no incumbent |
| `AAS-2026-10-15-tendril-f560fb299a37-01` | needs fresh audit | `https://github.com/serverless-dna/tendril` | no incumbent |
| `AAS-2026-10-14-thalo-86fcc3efe983-01` | integrated | `https://github.com/rejot-dev/thalo` | integrated |
| `AAS-2026-10-14-theknowledge-319a64927ee3-01` | integrated | `https://github.com/BadWally/TheKnowledge` | integrated |
| `AAS-2026-10-14-tolaria-42ddaf2ee8cd-01` | integrated | `https://github.com/refactoringhq/tolaria` | integrated |
| `AAS-2026-10-14-tracecraft-9c4af961e8e2-01` | integrated | `https://github.com/arrmlet/tracecraft` | integrated |
| `AAS-2026-10-14-2603-10600v1-a956324c9a82-01` | integrated | `https://arxiv.org/html/2603.10600v1` | integrated |
| `AAS-2026-10-14-virtual-context-bbd06cc3ac95-01` | integrated | `https://github.com/virtual-context/virtual-context` | integrated |
| `AAS-2026-10-14-vlm-wiki-311faef777b4-01` | integrated | `https://github.com/veniVeci/VLM-wiki` | integrated |
| `AAS-2026-10-14-voiden-98188b4a2f55-01` | integrated | `https://github.com/voidenhq/voiden` | integrated |
| `AAS-2026-10-14-voyager-f16a44a0cfe3-01` | integrated | `https://github.com/MineDojo/Voyager` | integrated |
| `AAS-2026-10-15-weknora-7adf8a01c381-01` | integrated | `https://github.com/Tencent/WeKnora` | integrated |
| `AAS-2026-10-15-2608-27454-65116a9d0de7-01` | integrated | `https://arxiv.org/abs/2608.27454` | integrated |
| `AAS-2026-10-15-wikiskill-baafad05d35e-01` | integrated | `https://github.com/Stahl-G/WikiSkill` | integrated |
| `AAS-2026-10-15-wuphf-b246722f99c0-01` | integrated | `https://github.com/nex-crm/wuphf` | integrated |
| `AAS-2026-10-15-xmemory-b9a2b9f58eda-01` | integrated | `https://github.com/hu-xiaobai/xMemory` | integrated |
| `AAS-2026-10-15-zikkaron-0102ec63c6e5-01` | integrated | `https://github.com/amanhij/zikkaron` | integrated |
| `AAS-2026-10-15-claude-workstream-kit-103204afa1ab-01` | needs fresh audit | `https://github.com/ChristopherA/claude-workstream-kit` | no incumbent |
| `AAS-2026-10-15-cludebot-cb70d11d215b-01` | needs fresh audit | `https://github.com/sebbsssss/cludebot` | no incumbent |
| `AAS-2026-10-15-cocoindex-3514227a0537-01` | needs fresh audit | `https://github.com/cocoindex-io/cocoindex` | no incumbent |
| `AAS-2026-10-15-context-constitution-7a352d7408f6-01` | needs fresh audit | `https://github.com/letta-ai/context-constitution` | no incumbent |
| `AAS-2026-10-15-coral-25e5fdab9dc4-01` | needs fresh audit | `https://github.com/Human-Agent-Society/CORAL` | no incumbent |
| `AAS-2026-10-15-crewai-62e53db969a7-01` | needs fresh audit | `https://github.com/crewAIInc/crewAI` | no incumbent |
| `AAS-2026-10-15-dense-mem-1a314bed9a5c-01` | needs fresh audit | `https://github.com/markhuangai/dense-mem` | no incumbent |
| `AAS-2026-10-15-eal-bench-f9a76e2fa858-01` | needs fresh audit | `https://github.com/tommasocerruti/eal-bench` | no incumbent |
| `AAS-2026-10-15-echel-08d27848b99a-01` | needs fresh audit | `https://github.com/alirezabbasi/echel` | no incumbent |
| `AAS-2026-10-15-echoes-vault-opencode-239c6738bb9e-01` | needs fresh audit | `https://github.com/psinetron/echoes-vault-opencode` | no incumbent |
| `AAS-2026-10-15-eigenius-fe68ed89519b-01` | needs fresh audit | `https://github.com/eigenius/eigenius` | no incumbent |
| `AAS-2026-10-15-equipa-32016e8dd9ae-01` | needs fresh audit | `https://github.com/sbknana/equipa` | no incumbent |
| `AAS-2026-10-15-exo-f0905e2cf44b-01` | needs fresh audit | `https://github.com/exoharness/exo` | no incumbent |
| `AAS-2026-10-15-funes-a9e6dbb3946a-01` | needs fresh audit | `https://github.com/ulyssestenn/funes` | no incumbent |
| `AAS-2026-10-15-gmemory-a2192cc823f7-01` | needs fresh audit | `https://github.com/bingreeky/GMemory` | no incumbent |
| `AAS-2026-10-15-gnosis-5bfb42422ce3-01` | needs fresh audit | `https://github.com/skorokithakis/gnosis` | no incumbent |
| `AAS-2026-10-15-isaacclupus-mnemosyn-spec-1887e13dcc13-01` | needs fresh audit | `https://github.com/noirblue/IsaacCLupus_mnemosyn_spec` | no incumbent |
| `AAS-2026-10-15-kblam-5a0c2fe96cc1-01` | needs fresh audit | `https://github.com/microsoft/KBLaM` | no incumbent |
| `AAS-2026-10-15-llm-wiki-mcp-5dff0dd0576a-01` | needs fresh audit | `https://github.com/Electro-resonance/LLM-WIKI-MCP` | no incumbent |
| `AAS-2026-10-15-miroshark-b3df0e053a29-01` | needs fresh audit | `https://github.com/aaronjmars/MiroShark` | no incumbent |
| `AAS-2026-10-15-origin-805d03bc599f-01` | needs fresh audit | `https://github.com/7xuanlu/origin` | no incumbent |
| `AAS-2026-10-15-quicky-wiki-628f7d7cc628-01` | needs fresh audit | `https://github.com/anzal1/quicky-wiki` | no incumbent |
| `AAS-2026-10-15-ai-context-os-4a0e34822f96-01` | reusable held | `https://github.com/alexdcd/AI-Context-OS` | no incumbent |
| `AAS-2026-10-15-ai-memex-cli-4324549b4bc0-01` | integrated | `https://github.com/zelixag/ai-memex-cli` | integrated |
| `AAS-2026-10-15-sage-d0de15ae5730-01` | needs fresh audit | `https://github.com/amazon-science/SAGE` | no incumbent |
| `AAS-2026-10-15-maka-4a8b73e41579-01` | needs fresh audit | `https://github.com/apache/maka` | no incumbent |
| `AAS-2026-10-15-archie-1ab3d8b8ff03-01` | integrated | `https://github.com/gchamon/archie` | integrated |
| `AAS-2026-10-15-arex-skill-1871063034b5-01` | reusable held | `https://github.com/VectorSpaceLab/AREX-Skill` | no incumbent |
| `AAS-2026-10-15-arsumbris-a9be6bac297f-01` | integrated | `https://github.com/arsumbris/arsumbris` | integrated |
| `AAS-2026-10-15-auto-claude-code-research-in-sleep-a8abf5f80cbb-01` | integrated | `https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep` | integrated |
| `AAS-2026-10-15-auto-harness-92303e444cb2-01` | integrated | `https://github.com/neosigmaai/auto-harness` | integrated |
| `AAS-2026-10-15-autocontext-b7f59f8405c4-01` | integrated | `https://github.com/greyhaven-ai/autocontext` | integrated |
| `AAS-2026-10-15-autogenesis-9bcfa57fd7c1-01` | reusable held | `https://github.com/DVampire/Autogenesis` | no incumbent |
| `AAS-2026-10-15-autosci-430df584df8f-01` | integrated | `https://github.com/skyllwt/AutoSci` | integrated |
| `AAS-2026-10-15-beever-atlas-10a3512c094c-01` | integrated | `https://github.com/Beever-AI/beever-atlas` | integrated |
| `AAS-2026-10-15-binder-a35c41531d40-01` | integrated | `https://github.com/mpazik/binder` | integrated |
| `AAS-2026-10-15-browzy-ai-0a823a13a7b6-01` | integrated | `https://github.com/VihariKanukollu/browzy.ai` | integrated |
| `AAS-2026-10-15-byterover-cli-71610aaf716b-01` | needs fresh audit | `https://github.com/campfirein/byterover-cli` | no incumbent |
| `AAS-2026-10-15-o-o-b6fd0055e5c1-01` | needs fresh audit | `https://github.com/jahala/o-o` | no incumbent |
| `AAS-2026-10-16-a-mem-sys-eff95cd80440-01` | needs fresh audit | `https://github.com/WujiangXu/A-mem-sys` | no incumbent |
| `AAS-2026-10-16-agent-s-db6fee212353-01` | needs fresh audit | `https://github.com/simular-ai/Agent-S` | no incumbent |
| `AAS-2026-10-16-basic-memory-46fe4c6cfdc3-01` | needs fresh audit | `https://github.com/basicmachines-co/basic-memory` | no incumbent |
| `AAS-2026-10-16-beads-rust-e82d5506d2ff-01` | needs fresh audit | `https://github.com/Dicklesworthstone/beads_rust` | no incumbent |
| `AAS-2026-10-16-hipporag-2b37edfc7ade-01` | needs fresh audit | `https://github.com/OSU-NLP-Group/HippoRAG` | no incumbent |
| `AAS-2026-10-16-memoryos-bb72a1b70e03-01` | needs fresh audit | `https://github.com/BAI-LAB/MemoryOS` | no incumbent |
| `AAS-2026-10-16-openclerk-ec0e00c2bb0a-01` | needs fresh audit | `https://github.com/yazanabuashour/openclerk` | no incumbent |
| `AAS-2026-10-16-os-copilot-7cef03148c53-01` | needs fresh audit | `https://github.com/OS-Copilot/OS-Copilot` | no incumbent |
| `AAS-2026-10-16-llm-wiki-6786c5985cdc-01` | needs fresh audit | `https://github.com/Pratiyush/llm-wiki` | no incumbent |

## Completed batch-18 exact sources

- `AAS-2026-10-16-a-mem-sys-eff95cd80440-01` — `https://github.com/WujiangXu/A-mem-sys` at `f303dfc71e07bdc787f4bc135d4cea328ae30e99`; 13 files; own completed effect matches: `True`.
- `AAS-2026-10-16-agent-s-db6fee212353-01` — `https://github.com/simular-ai/Agent-S` at `15776a8dc659658b1963816ea006f7af1978e595`; 13 files; own completed effect matches: `True`.
- `AAS-2026-10-16-basic-memory-46fe4c6cfdc3-01` — `https://github.com/basicmachines-co/basic-memory` at `a72751c5d626380dedeed30f55f7a80ba3dc710d`; 13 files; own completed effect matches: `True`.
- `AAS-2026-10-16-beads-rust-e82d5506d2ff-01` — `https://github.com/Dicklesworthstone/beads_rust` at `53f7a3d30aca8cab3c3e4abdefeade459e8a3089`; 13 files; own completed effect matches: `True`.
- `AAS-2026-10-16-hipporag-2b37edfc7ade-01` — `https://github.com/OSU-NLP-Group/HippoRAG` at `d5c8329422e0a0b834a15874545cb6a74b4f9b26`; 13 files; own completed effect matches: `True`.
- `AAS-2026-10-16-memoryos-bb72a1b70e03-01` — `https://github.com/BAI-LAB/MemoryOS` at `587ed7755c7aed179965792830ff1b5ad9a6fa92`; 13 files; own completed effect matches: `True`.
- `AAS-2026-10-16-openclerk-ec0e00c2bb0a-01` — `https://github.com/yazanabuashour/openclerk` at `092fb98d243c2d9d95867ad04618ebce88983552`; 13 files; own completed effect matches: `True`.
- `AAS-2026-10-16-os-copilot-7cef03148c53-01` — `https://github.com/OS-Copilot/OS-Copilot` at `f720af8807e49a92dda64572d2c6bc6c0ac7ee7e`; 13 files; own completed effect matches: `True`.
- `AAS-2026-10-16-llm-wiki-6786c5985cdc-01` — `https://github.com/Pratiyush/llm-wiki` at `b1088890ee0743810a92577aecad946c6b3eb2d2`; 13 files; own completed effect matches: `True`.

## Prior evidence references

Current hashes identify present inputs, not fabricated historical audit pins. The JSON preserves prior references and explicitly recorded historical hashes.

| Input | Current SHA-256 |
| --- | --- |
| `/home/zby/llm/commonplace/kb/work/COLLECTION.md` | `cc7986cde1a046a8e9f1149ea0a97aaa7fb83d489a288d47868cdaf88cf9e897` |
| `/home/zby/llm/commonplace/kb/types/text.md` | `67adf7ae1a8d14c68881d13c7ed1b87b79615043ec0efbcb60179d05ef9ec962` |
| `/home/zby/llm/commonplace/kb/work/agentic-system-reruns/audit-a-rerun.md` | `a0cb0028febfc19b82dc2caa832638e13d972b0d2a9e1a143961c887f8b8be48` |
| `/home/zby/llm/commonplace/kb/work/agentic-system-reruns/audit-integration-intake-2026-10-15.json` | `31fabfd2e3a3bdb7046a1e8f4a5ff7af6bea9d3ee43d8afd2529a8dd8fb3ed19` |
| `/home/zby/llm/commonplace/kb/work/agentic-system-reruns/audit-integration-intake-2026-10-15.md` | `acd409f5665ccda3f0c325582e2fb466874d0ce77e089372fa86aea5285471a0` |
| `/home/zby/llm/commonplace/kb/work/agentic-system-reruns/audit-integration-later-46.json` | `09e73b81205a3eb6a79b1e5dd536563f98733fda0d8504a3aad38b557c69949b` |
| `/home/zby/llm/commonplace/kb/work/agentic-system-reruns/reentry-pilots.md` | `f414d60d3bffb2f76cd59eaec392769e7dcda74a79301d7c890274ea9d8c5337` |
| `/home/zby/llm/commonplace/kb/work/agentic-system-reruns/batch-19-depth-results.md` | `b87c71e012141efb07344eeefb7171899d139b996d9e5ee6d59dbcf1aacd3d07` |
| `/home/zby/llm/commonplace/kb/work/agentic-system-reruns/batch-19.json` | `92b7e97bcae57b9c1cf9d8953149eab3035088435164e7f55313aae956367350` |

## Limits and verification

- Point-in-time fixed discovery, not a lock. Runs completing after their individual observation are later arrivals, excluded until a new inventory.
- No semantic audit, source acquisition/verification/execution, acceptance, integration, reset, inspect/advance command, delegation or Git write. Parent owns subsequent acceptance/integration.
- Potentially active runs read only at shallow run-definition/publish-effect identity metadata; no attempts, jobs, handouts or logs opened. No process-liveness inference from absent publication.
- Prior JSON fully parsed; all live/archive row structures processed programmatically. Prior conclusions remain attributed, not freshly semantically reviewed.
- Canonical identity uses boundary source metadata. GitHub owner/project case, terminal slash and .git normalize only for matching; literal metadata retained.
- Archive payloads not opened or rehashed. Historical archive/effect/method assertions are carried forward, not recertified.
- Current report hashes are not invented historical audit bindings. Dynamic Cheatsheet 11e3e77c2265 remains unbound and held; batch-19 depth is diagnosis, not clearance.
- No live trace content scanned. Historical locator assertions inherited as leads only; new discovery examines filenames only.
- Explicit preparation token selects own runs. Unprepared worktrees use name-derived token plus matching completed effect and local destination. Nonmatching/inherited definitions not counted; arbitrary nonstandard state roots remain a discovery limit.
- Open attempts use terminal-state metadata only, not engine execution. Unfamiliar states conservatively uncertain.

Machine guards checked unique run IDs, resolved publication paths and proposed report paths. JSON was serialized and reparsed. Markdown validation is run separately on this owned file; no publication is freshly validated or audited. Only the two commissioned files are written. No staging, commit, cleanup, configuration change or worktree mutation is authorized.

---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "SkillRL epistemic routes: outcome checks, unverified skill admission, search-answer scoring and behavior adaptation."
run-id: AAS-2026-10-14-skillrl-0dba0e1c895e-01
reviewed-boundary: "4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d"
---

# SkillRL epistemic report

## Source-and-claim boundary

The question is whether SkillRL's experience-to-skill and reward-to-policy routes establish knowledge, or instead install behavior-shaping candidates. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence). Frozen evidence: see the [Source register](boundary.md#source-register). All added reads below are SRC-1 implementation at the frozen commit; README claims are doctrine/design or reported operation, not observed runs. No target execution occurred.

The positive routes do not imply a system-complete negative about acceptance. Several included alternatives remain unassessed. Missing execution evidence prevents conclusions about generated content, actual reliance, learning benefit and exercised self-improvement. Missing input provenance prevents authenticating imported experiences; missing provider internals prevents individuating beliefs in remote or actor weights. Missing interventions prevent attributing a benefit to skills rather than policy fitting, input selection or other machinery.

| Entry point or operation | Source path | Coverage and prevented conclusion |
|---|---|---|
| RL launch, policy fitting and resume | SRC-1, `verl/trainer/main_ppo.py`, `verl/trainer/ppo/ray_trainer.py` | Supplied [RT-RTE-policy-update](runtime.md#rt-rte-policy-update), [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout); no independent full worker audit. |
| ALFWorld outcome feedback and action admission | SRC-1, `agent_system/environments/env_package/alfworld/envs.py`, `agent_system/environments/env_package/alfworld/projection.py` | Supplied [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout); format feedback is not an action veto or skill test. |
| Dynamic generation and parser | SRC-1, `agent_system/memory/skill_updater.py` | Direct read; [EPI-RTE-proposal-check](#epi-rte-proposal-check), supplied [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission), [RT-RTE-training-admission](runtime.md#rt-rte-training-admission). |
| Bank rendering, addition, deletion and save | SRC-1, `agent_system/memory/skills_only_memory.py` | Direct rendering/mutation read; [EPI-RTE-skill-withdrawal](#epi-rte-skill-withdrawal); selection internals supplied by runtime. |
| Offline generators | SRC-1, `skill_generation/alfworld.py`, `skill_generation/search.py`, `skill_generation/webshop.py` | Supplied [RT-RTE-offline-production](runtime.md#rt-rte-offline-production); detailed Search/WebShop generation remains uninspected, preventing equivalent semantic-check conclusions. |
| SFT pipeline and aggregation | SRC-1, `examples/sft_data_generation/run_alfworld.sh`, `examples/sft_data_generation/skill_memory/aggregate_skills.py` | Direct driver and aggregation body; supplied [RT-RTE-sft-production](runtime.md#rt-rte-sft-production). Per-trajectory memory generation, final flattening and alternate SFT pipelines not independently audited: no complete preservation or acceptance conclusion. |
| Trajectory cleanup | SRC-1, `examples/sft_data_generation/preprocess/dedupe_repetitions.py` | Direct complete read and source deduction; [EPI-RTE-trajectory-cleanup](#epi-rte-trajectory-cleanup). |
| Search tool and terminal scorer | SRC-1, `agent_system/environments/env_package/search/third_party/skyrl_gym/tools/search.py`, `agent_system/environments/env_package/search/third_party/skyrl_gym/envs/search/env.py`, `agent_system/environments/env_package/search/third_party/skyrl_gym/envs/search/utils.py` | Direct operative paths; [EPI-RTE-search-import](#epi-rte-search-import), [EPI-RTE-answer-check](#epi-rte-answer-check). Retrieval service/index not inspected: no corpus warrant or retrieval quality judgment. |
| WebShop evaluator | SRC-1, `agent_system/environments/env_package/webshop/envs.py` | Scoped search locates perfect-match reward conversion. Full purchase evaluator uninspected: no license beyond attributed benchmark feedback. |
| Environment dispatch alternatives | SRC-1, `agent_system/environments/env_manager.py` | Direct `make_envs` read confirms Search, ALFWorld, WebShop, cards, Sokoban and AppWorld. Last three evaluator/action paths unassessed: no system-wide absence of other checks. |
| Packaging and exposed operations | SRC-1, `setup.py`, `pyproject.toml` | Direct complete reads expose packaging, not console-script/hook dispatch. Shipped shell/module drivers remain covered above. Search registers its tool group in the directly read environment. The exposed deletion method is assessed even though runtime did not trace it. |
| Shipped candidate bank | SRC-1, `memory_data/alfworld/claude_style_skills.json` | Direct initial entries only; [EPI-OBJ-skill-principles](#epi-obj-skill-principles). Artifact availability does not establish generating/checking provenance. Other banks unassessed. |

Claims: [RT-CLM-reusable-patterns](runtime.md#rt-clm-reusable-patterns), [EPI-CLM-recursive-evolution](#epi-clm-recursive-evolution), [EPI-CLM-context-efficiency](#epi-clm-context-efficiency). These do not explicitly promise infallible truths; their transfer, evolution and utility implications still need route-specific assessment.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-skill-principles](#epi-obj-skill-principles) | Conditional strategy effectiveness and task assumptions, distinguishable from imperative prescriptions | see record | SRC-1, `memory_data/alfworld/claude_style_skills.json` | No verified effectiveness or authenticated generation history. |
| [RT-OBJ-trajectory-batch](runtime.md#rt-obj-trajectory-batch) | Task/action/outcome reports; numerical masks and scores are distinct operative parts | see record | SRC-1, `agent_system/multi_turn_rollout/rollout_loop.py` | Reward does not identify the cause of failure or endorse reasoning. |
| [EPI-OBJ-search-content](#epi-obj-search-content) | Imported passages and model answer strings | see record | SRC-1, `agent_system/environments/env_package/search/third_party/skyrl_gym/envs/search/env.py` | Documents, answer and reference remain separate authorities. |
| [RT-CMP-actor-rollout](runtime.md#rt-cmp-actor-rollout) | Not determinable in weights; output text can be truth-apt | see record | SRC-1, `verl/workers/actor/dp_actor.py` | No accessible weight instance or proposition-level training trace. |
| [RT-CMP-skill-updater](runtime.md#rt-cmp-skill-updater) | Not determinable internally; generated principles are candidates | see record | SRC-1, `agent_system/memory/skill_updater.py` | Opaque, unpinned service; inference does not establish semantic checking. |
| [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model) | None individuated in similarity vectors | see record | SRC-1, `agent_system/memory/skills_only_memory.py` | Similarity ranks relevance, not truth or strategy effectiveness. |
| [RT-RTE-sft-production](runtime.md#rt-rte-sft-production) | Generated memories, rules and reasoning; supplied actions/outcome labels | see record | SRC-1, `examples/sft_data_generation/distillation/distill_alfworld.py` | Route cited as mixed-material container, not a second object declaration; reasoning provenance and correctness unverified. |

## Authority-route ledger

Each row is one consequential function. Repeated route citations split checking, admission and retention rather than declaring duplicate routes. Fields owned by supplied records say `see`; relations and bounded epistemic licenses below are this report's assessment. No operation is evidenced as observed.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-offline-production](runtime.md#rt-rte-offline-production) | content transformation | implemented | [EPI-OBJ-skill-principles](#epi-obj-skill-principles) | truth-apt transformation: indeterminate | Experience to rules | see route | see route | see route | see route | Candidate generalizations only; input warrant unknown | see route | see route | SRC-1, `skill_generation/alfworld.py` | [RT-CLM-reusable-patterns](runtime.md#rt-clm-reusable-patterns) | Transfer untested | Actual outputs unavailable; compression versus conjecture cannot be established for generated instances. |
| [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission), [RT-RTE-training-admission](runtime.md#rt-rte-training-admission) | content transformation | implemented | [EPI-OBJ-skill-principles](#epi-obj-skill-principles) | truth-apt transformation: indeterminate | Failure fragments to new rules | see routes | see routes | see routes | see routes | Model proposals, not warranted causal explanations | see routes | see routes | SRC-1, `agent_system/memory/skill_updater.py` | [EPI-CLM-recursive-evolution](#epi-clm-recursive-evolution) | Titles are not full challenged principles | Missing candidate instance prevents classifying its semantic edge. |
| [EPI-RTE-proposal-check](#epi-rte-proposal-check) | check/evidence production | implemented | [EPI-OBJ-skill-principles](#epi-obj-skill-principles) | no content change | see record | see record | see record | see record | see record | JSON/key presence only | see record | see record | SRC-1, `agent_system/memory/skill_updater.py` | none | Structural check, not content acceptance | `when_to_apply` requested but not required by parser. |
| [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission), [RT-RTE-training-admission](runtime.md#rt-rte-training-admission) | disposition/acceptance | implemented | [EPI-OBJ-skill-principles](#epi-obj-skill-principles) | no content change | Returned proposals to live training bank | see routes | see routes | see routes | see routes | Operational admission only; no named effectiveness acceptance criterion | see routes | see routes | SRC-1, `verl/trainer/ppo/ray_trainer.py` | [EPI-CLM-recursive-evolution](#epi-clm-recursive-evolution) | Failure evidence triggers generation, not candidate verification | Existing-ID exclusion is not semantic novelty or truth checking. |
| [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission), [RT-RTE-training-admission](runtime.md#rt-rte-training-admission) | retention | implemented | [EPI-OBJ-skill-principles](#epi-obj-skill-principles) | no content change | Live additions to saved bank | see routes | see routes | see routes | see routes | Retained candidates, not accepted knowledge | see routes | see [RT-BAP-skill-conditioning](runtime.md#rt-bap-skill-conditioning) | SRC-1, `agent_system/memory/skills_only_memory.py` | [EPI-CLM-recursive-evolution](#epi-clm-recursive-evolution) | Retention is not lifecycle integration | No evidence-consuming acceptance followed by integration in these traced paths. |
| [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout) | operational admission/selection/consumption | implemented | [EPI-OBJ-skill-principles](#epi-obj-skill-principles) | truth-apt transformation: non-ampliative reshaping | Bank selection and rendering | see route | see route | see route | see route | Category/similarity licenses relevance only | see route | see [RT-BAP-skill-conditioning](runtime.md#rt-bap-skill-conditioning) | SRC-1, `agent_system/memory/skills_only_memory.py` | [RT-CLM-reusable-patterns](runtime.md#rt-clm-reusable-patterns) | General applicability omitted | Concrete rendering witness in object record; no guaranteed model compliance. |
| [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout) | check/evidence production | implemented | [RT-OBJ-trajectory-batch](runtime.md#rt-obj-trajectory-batch) | no content change | ALFWorld task outcome | see route | see route | see route | see route | Simulator `won` licenses bounded task outcome, not component effectiveness | see route | see route | SRC-1, `agent_system/environments/env_package/alfworld/envs.py` | none | No reasoning/transfer oracle | Simulator/data external contracts unverified. |
| [EPI-RTE-search-import](#epi-rte-search-import) | content transformation | implemented | [EPI-OBJ-search-content](#epi-obj-search-content) | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | Source warrant unknown; local doc numbering is not provenance | see record | see record | SRC-1, `agent_system/environments/env_package/search/third_party/skyrl_gym/tools/search.py` | none | Retrieval success is not truth | Corpus/service lineage unassessed. |
| [EPI-RTE-answer-check](#epi-rte-answer-check) | check/evidence production | implemented | [EPI-OBJ-search-content](#epi-obj-search-content) | no content change | see record | see record | see record | see record | see record | Normalized reference agreement only | see record | see record | SRC-1, `agent_system/environments/env_package/search/third_party/skyrl_gym/envs/search/utils.py` | none | Reference match is not independent world truth | Combined history includes retrieved text; answer tag origin not authenticated. |
| [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | behavior/policy adaptation | implemented | [RT-CMP-actor-rollout](runtime.md#rt-cmp-actor-rollout) | non-truth-apt policy/content update: numerical optimization | Reward/advantage to actor state | see route | see route | see route | see route | No proposition-level license from optimizer | see route | see [RT-BAP-policy-parameters](runtime.md#rt-bap-policy-parameters) | SRC-1, `verl/workers/actor/dp_actor.py` | [EPI-CLM-recursive-evolution](#epi-clm-recursive-evolution) | Numerical guard is not quality veto | Parametric truth-apt content not determinable; better performance unobserved. |
| [EPI-RTE-skill-withdrawal](#epi-rte-skill-withdrawal) | disposition/acceptance | implemented | [EPI-OBJ-skill-principles](#epi-obj-skill-principles) | no content change | see record | see record | see record | see record | see record | Withdrawal by ID gives no falsity finding | see record | see record | SRC-1, `agent_system/memory/skills_only_memory.py` | none | No automatic content-driven caller found | In-memory removal need not revoke cached episode selection or disk copies. |
| [EPI-RTE-trajectory-cleanup](#epi-rte-trajectory-cleanup) | content transformation | implemented | [RT-RTE-sft-production](runtime.md#rt-rte-sft-production) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | Surviving reports unchanged, evidential coverage degraded | see record | see record | SRC-1, `examples/sft_data_generation/preprocess/dedupe_repetitions.py` | [EPI-CLM-context-efficiency](#epi-clm-context-efficiency) | Equal actions need not mean equal observations | Deletion can hide changed state; does not validate surviving strategy. |
| [RT-RTE-sft-production](runtime.md#rt-rte-sft-production) | content transformation | implemented | [EPI-OBJ-skill-principles](#epi-obj-skill-principles) | truth-apt transformation: indeterminate | Planning patterns to skills; actions to reasoning | see route | see route | see route | see route | Candidate reasoning and strategies, not independent explanations | see route | see route | SRC-1, `examples/sft_data_generation/skill_memory/aggregate_skills.py` | [RT-CLM-reusable-patterns](runtime.md#rt-clm-reusable-patterns) | Success label is supplied, not retested | Generated explanations may reshape or add claims; actual outputs absent. |
| [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | lineage/freshness/recovery | implemented | [RT-CMP-actor-rollout](runtime.md#rt-cmp-actor-rollout) | no content change | Checkpoint resume | see route | see route | see route | see route | Restoring parameters establishes no endorsement or truth | see route | see [RT-BAP-policy-parameters](runtime.md#rt-bap-policy-parameters) | SRC-1, `verl/trainer/ppo/ray_trainer.py` | none | Bank/checkpoint restoration decoupled | Exact coupled reproduction not guaranteed. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-reusable-patterns](runtime.md#rt-clm-reusable-patterns) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-offline-production](runtime.md#rt-rte-offline-production), [RT-RTE-sft-production](runtime.md#rt-rte-sft-production), [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout) | None supplied | No controlled transfer comparison | Produces and supplies reusable-form instructions | Reusable form does not establish effective transfer. |
| [EPI-CLM-recursive-evolution](#epi-clm-recursive-evolution) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission), [RT-RTE-training-admission](runtime.md#rt-rte-training-admission), [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | None supplied | Validation feedback can affect training; no isolated skill intervention | Wired failure-responsive additions and numerical fitting | Co-change does not establish correct diagnosis, improvement or full theory criticism. |
| [EPI-CLM-context-efficiency](#epi-clm-context-efficiency) | see record | SRC-1, `README.md`; reported operation | see record | [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout), [EPI-RTE-trajectory-cleanup](#epi-rte-trajectory-cleanup) | None supplied | No measurement denominator, trace comparison or independent utility test | Compact rendering and tail history are implemented | Neither the 10–20% magnitude nor enhanced reasoning utility is established. |

## Bounded conclusion

SkillRL imports experience records and, in Search, retrieval passages with unknown source warrant. It selects and reshapes instructions for policy prompts. Category, similarity and parser checks grant operational relevance or structural admissibility, not truth. The inspected skill-addition paths retain model proposals without an evidence-consuming decision that they work for a stated scope. Thus those paths establish candidate retention and use, not accepted ampliative knowledge or post-acceptance lifecycle integration. They may produce conjectures; absent actual outputs, entailment versus conjecture remains indeterminate rather than presumed ampliative.

ALFWorld outcomes support simulator goal achievement. Search exact match supports normalized agreement with dataset targets. These are consequential evaluators: rewards shape training, continuation ends at terminal conditions, and poor outcomes can trigger skill generation. Neither evaluator warrants the proposed failure mechanism, generated reasoning, replay safety, transfer or skill-specific causality. Search imports and answer scoring are additional material routes beyond the runtime's detailed ALFWorld account. Withdrawal is an exposed API capability, not a wired shipped withdrawal workflow or an exercised semantic rejection/rollback protocol. Its method is implemented, but the bounded caller search locates no invocation.

Policy fitting independently changes distributed parameters. Numerical stability checks can suppress an optimizer step; they do not accept a new policy by a held-out quality criterion. Numerical adaptation is implemented even though internal truth-apt representations are not determinable. Saved banks and checkpoints have distinct recovery paths. Static bank presence proves neither production history nor acceptance.

The online skill route has improvement-directed self-change capacity over later training episodes: outcome evidence triggers proposals; software installs them into training memory; a later reset can deliver them through advisory model guidance. The independently specified objective is benchmark task success. Link 4—later operation causally depending on the change—is unestablished, as are exercised self-improvement and successful improvement. Parameter fitting is a separate implemented adaptation route, not a substitute witness for skill effects. Learning benefit remains uninspected for both.

The rule texts meet localized formulation at a coarse whole-principle level. Their computational consumers are wired, but actual content-dependent decisions remain unobserved. Full content-directed criticism of current principles and iterative retention of such criticism are not established by the title-only updater input and its counts/IDs history. This leaves theory-builder conditions independent rather than deriving all from the presence of a skill bank. Selected task behavior is represented in failure fragments and the resulting instructions can reach later behavior, giving a wired two-direction reflective pathway at that limited aspect; its accuracy and exercised influence remain unobserved. Launch/configuration are human contributions, while proposal and admission on the traced dynamic route are computational. That autonomy does not establish reliability or autonomous theory building. Unassessed alternatives prevent a whole-system negative.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-skill-principles
Label: Skill principles and applicability

Source-native identity: bank `general_skills`, `task_specific_skills`, and common-mistake instruction text. Form: natural-language principles, titles and applicability conditions inside symbolic JSON lists/IDs; substrate: disk JSON and live Python dictionaries. This is the instruction object consumed by [RT-BAP-skill-conditioning](runtime.md#rt-bap-skill-conditioning), not a duplicate of the policy component or [RT-OBJ-trajectory-batch](runtime.md#rt-obj-trajectory-batch). No supplied object declares this bank part.

Imperatives are not themselves propositions. Their task assumptions and statements about strategy consequences can be assessed over household task domains. One visible principle says immediate acquisition avoids losing track/re-searching; this does not authenticate that causal claim. SRC-1, `memory_data/alfworld/claude_style_skills.json`:

> "principle": "As soon as a required object becomes visible and reachable, take it before moving elsewhere to avoid losing track or re-searching.",
> --- `memory_data/alfworld/claude_style_skills.json`

A deterministic rendering deduction uses the inspected general-skill loop: input title `T`, principle `P`, applicability `C` renders `- **T**: P` under General Principles; `C` is omitted. No new proposition is created, but scope information is lost. This qualifies semantic preservation of the whole record, not the surviving text. SRC-1, `agent_system/memory/skills_only_memory.py`:

>         general_skills = retrieved_memories.get('general_skills', [])
>         if general_skills:
>             lines = ["### General Principles"]
>             for skill in general_skills:
>                 title = skill.get('title', '')
>                 principle = skill.get('principle', '')
>                 lines.append(f"- **{title}**: {principle}")
>             sections.append("\n".join(lines))
> --- `agent_system/memory/skills_only_memory.py`

Addressability: individual entries, IDs, principles and conditions are inspectable/editable; this is not fine-grained explicit identification of causal premises. Persistence: live additions can reach later episodes; saved/reconfigured banks can reach later runs, see the admission routes. Provenance of the shipped instance remains unknown.

#### EPI-OBJ-search-content
Label: Search passages and answer content

Source-native identity: tool-return document `contents`, `SearchEnv.chat_history`, `<answer>` text, and `ground_truth["target"]`. Natural-language content is held in symbolic message/dataset structures and live Python strings; tool transport is JSON. These are distinct from the tokenized container [RT-OBJ-trajectory-batch](runtime.md#rt-obj-trajectory-batch): retrieval corpus text and dataset target are not declared parts of that rollout batch. Answer text can later enter the batch; that overlap is a projection, not identity. Imported content, generated answer, and reference each keep separate warrant. SRC-1, `agent_system/environments/env_package/search/third_party/skyrl_gym/envs/search/env.py`:

>         assert "ground_truth" in extras, "ground_truth is required in extras field"
>         self.ground_truth = extras["ground_truth"]
> --- `agent_system/environments/env_package/search/third_party/skyrl_gym/envs/search/env.py`

### Routes

#### EPI-RTE-proposal-check
Label: Proposal structure check

This is the checking subroute spanning [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission) and [RT-RTE-training-admission](runtime.md#rt-rte-training-admission), not either complete admission route. Distinct target: returned JSON/key presence before code admission.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: List of entries with skill_id, title and principle keys, or empty list on parse failure.
- Later read-back: inapplicable — this check itself retains no content; the parent routes admit and persist its outputs.
- Delegated visibility: Parser sees provider response text, not independent task evidence.
- Selection predicate: Extract first `[` through last `]`, JSON-decode, require three keys.
- Invalidation or expiry: inapplicable — each response is checked anew; no stored verdict or expiry.
- Activation or effect: Missing keys/invalid JSON withhold candidates from parent admission; no semantic verification.
- Evidence limits: No actual response or successful check trace supplied; malformed non-JSON types can reach the outer exception catch.

Owner: updater Python. Evaluator domain: parseable response structure. Model proposes; software decides; operator supplies service/run configuration, not per-skill approval. Missing structure can veto a candidate; `when_to_apply` is guidance, not this gate's criterion. Operating mode: bounded failure-driven training update. Oracle: none for principle truth/effectiveness. Recovery: outer exception returns empty; no tested alternative or semantic rollback. Consumer/channel/force/horizon: parent updater/admission code receives filtered list; enforcing structural gate for this update. Epistemic license: three-key presence only. SRC-1, `agent_system/memory/skill_updater.py`:

>                 return [
>                     s for s in skills
>                     if all(k in s for k in ['skill_id', 'title', 'principle'])
>                 ]
> --- `agent_system/memory/skill_updater.py`

The content-directed-criticism limit follows the actual updater inputs, not model opacity alone:

> EXISTING SKILL TITLES (avoid duplicating these):
> {existing_titles}
>
> Generate 1-{self.max_new_skills_per_update} NEW actionable skills that would help avoid these failures.
> Each skill must have: skill_id, title (3-5 words), principle (1-2 sentences), when_to_apply.
> --- `agent_system/memory/skill_updater.py`

Theory-builder conditions 1–4: 1 formulation implementation conclusion status: wired for whole natural-language principles; 2 consumption implementation conclusion status: wired for delivery, operation conclusion status: uninspected for actual dependence on content; 3 content-directed criticism implementation conclusion status: uninspected beyond the bounded prompt/parser account—titles and failures do not expose challenged principle/blame/revision; 4 iteration implementation conclusion status: wired for repeated additions, but criticism-driven iteration conclusion status: uninspected because retained counts/IDs are not a retained criticism. Learning: uninspected benefit. Reflection: wired limited trace-to-instruction-to-prompt pathway, operation uninspected. Autonomous proposal/admission: wired within operator-started updates; autonomous theory builder: uninspected because conditions 3–4 remain unestablished. These are separate assessments, not a single builder verdict.

#### EPI-RTE-skill-withdrawal
Label: Skill withdrawal by identifier

No counterpart after comparison with supplied admission routes. This exposed deletion method can change future bank membership when called, rather than parsing or adding proposals. The supplied refusal's memory fragment assesses the same maintenance capability as afforded; the direct source check agrees. No shipped caller was located, so an integrated withdrawal workflow is not established. The ledger's architectural status remains implemented for the inspected method itself.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Boolean removal result and changed general/task lists; clears embedding cache if removed.
- Later read-back: If a caller invokes removal, later retrieval from the changed live bank can omit the removed ID; a separate save makes the changed bank reloadable. No shipped removal caller was located.
- Delegated visibility: Caller supplies an ID; policy sees later rendered selections, not a falsity decision.
- Selection predicate: Equality to supplied skill_id across general and task-specific skills, not common_mistakes.
- Invalidation or expiry: Embedding cache cleared; existing episode selections and saved copies not automatically revoked.
- Activation or effect: Calling the method enforces live bank membership change; connection to a shipped caller is not established and actual use is unobserved.
- Evidence limits: Search `remove_skill\(` in agent_system, verl, examples and skill_generation at SRC-1 finds only its declaration. No automatic quality-driven invocation established in that boundary.

Endpoint/progression/owner: exposed capability is API caller → bank method → filtered Python lists → possible later retrieval; optional separate save. The caller is unspecified, not an inspected shipped endpoint. No evaluator of principle truth is invented: condition is ID equality. Admission here is withdrawal, with caller decision and no intrinsic human/computational identity. Mode: caller-invoked bank maintenance, no improvement trigger. Rollback requires caller restoration/reload; no built-in comparative test. Guidance: ID argument only. Epistemic authority: none beyond membership. Operational authority: future bank selection cannot choose removed entries from these lists; cached episodes may still carry text. Consumer/channel/force/horizon: retrieval over lists, enforcing membership until re-addition, with later prompts advisory. SRC-1, `agent_system/memory/skills_only_memory.py`:

>         self.skills['general_skills'] = [
>             s for s in self.skills.get('general_skills', [])
>             if s.get('skill_id') != skill_id
>         ]
> --- `agent_system/memory/skills_only_memory.py`

>         if removed:
>             self._skill_embeddings_cache = None
>             print(f"[SkillsOnlyMemory] Removed skill: {skill_id}")
>         return removed
> --- `agent_system/memory/skills_only_memory.py`

#### EPI-RTE-trajectory-cleanup
Label: Trajectory action deduplication
Part of: [RT-RTE-sft-production](runtime.md#rt-rte-sft-production)

This independently inspected deterministic preprocessing part has different checks/consumers from model reasoning distillation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Filtered trajectory lists replacing input lists, then cleaned JSON from CLI.
- Later read-back: Cleaned file feeds memory generation and distillation in the SFT shell pipeline.
- Delegated visibility: Downstream models receive surviving steps, not the removed observations.
- Selection predicate: Equal adjacent action suffix windows; ascending pattern length, first match removes newest window.
- Invalidation or expiry: Output regenerated by CLI; no verdict or removed-step recovery record.
- Activation or effect: Code forces removal before downstream model calls; benefit and downstream behavioral influence unobserved.
- Evidence limits: Action equality does not establish state/observation equality or authentic source records; no runtime fixture executed.

Source deduction: two records with action `look` and observations `empty`, then `object appeared` produce only the first record. On adding the second, n=2 and pattern_len=1 compare equal actions, deleting the second record. This is non-ampliative deletion, not an entailed claim that the environment stayed empty. Evaluator target/domain: duplicate action windows in symbolic lists. Result forces later evidence selection, not acceptance of claims. Owner: Python CLI; consumer/channel/force/horizon: memory/distillation stages read cleaned JSON, enforced input filtering for that batch, potentially persisted as training material. No answer oracle or human content approval; operator selects inputs. Recovery requires original input file, not automatic reconstruction. SRC-1, `examples/sft_data_generation/preprocess/dedupe_repetitions.py`:

>         for pattern_len in range(1, n // 2 + 1):
>             last = [s.get("action") for s in cleaned[-pattern_len:]]
>             prev = [s.get("action") for s in cleaned[-2 * pattern_len : -pattern_len]]
>             if last == prev:
>                 del cleaned[-pattern_len:]
>                 break
> --- `examples/sft_data_generation/preprocess/dedupe_repetitions.py`

The caller gives the transformed data consequential consumers:

> python "${DIR}/skill_memory/generate_memory_alfworld.py" \
>   --input_file "${WORK_DIR}/processed_trajectories_cleaned.json" \
>   --output_file "${WORK_DIR}/generated_memories.json"
> --- `examples/sft_data_generation/run_alfworld.sh`

#### EPI-RTE-search-import
Label: Search passage import

Distinct from the supplied ALFWorld-centered [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout): a dispatched Search tool imports external informational text. Its source chain was only scoped in runtime, not declared with these warrant fields.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON result text wrapped as information in SearchEnv observations, or error/no-result text.
- Later read-back: inapplicable — inspected import holds ordinary current-episode history, not an accumulated durable memory; subsequent history consumption is within the episode.
- Delegated visibility: Policy receives document contents labeled Doc numbers; tool return formatting does not include complete source identity/ranking metadata.
- Selection predicate: Model search-tag query, configured topk, service response `result`; tool registration names SearchToolGroup/search.
- Invalidation or expiry: Episode history resets; request failures retried or surfaced, not treated as evidence of proposition falsity.
- Activation or effect: Informational text enters later policy observation; changed decisions unobserved.
- Evidence limits: Retrieval service/index and content provenance uninspected; transport success cannot license source truth.

Owner/progression: model query → environment parser → registered tool → HTTP service → document formatting → environment user observation → policy. Imported propositions have unknown warrant; no acceptance decision. Consumer/channel/force/horizon: policy observation, advisory model interpretation during episode. Deterministic witness: one retrieved contents string ` X ` formats as `Doc 1: X\n`; this adds a local ordinal, not a citation or verification. SRC-1, `agent_system/environments/env_package/search/third_party/skyrl_gym/tools/search.py`:

> def _passages2string(retrieval_result):
>     format_reference = ""
>     for idx, doc_item in enumerate(retrieval_result):
>         content = doc_item["document"]["contents"].strip()
>         format_reference += f"Doc {idx+1}: {content}\n"
>     return format_reference
> --- `agent_system/environments/env_package/search/third_party/skyrl_gym/tools/search.py`

#### EPI-RTE-answer-check
Label: Search answer reference check

Distinct evaluator route within dispatched Search, compared with [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout)'s ALFWorld simulator outcome. No counterpart declares this exact-match check.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Terminal numeric reward: default 1 for normalized reference match, 0 otherwise or no answer tag.
- Later read-back: inapplicable — check itself does not retain a new claim; reward can enter the supplied policy-update/admission paths.
- Delegated visibility: Scorer receives concatenated chat history and dataset ground_truth target; policy supplies action text, not an authenticated proof.
- Selection predicate: Terminal on answer tags or max turns; extract last complete answer-tag match from combined history.
- Invalidation or expiry: New reset supplies new reference/history; no truth-verdict cache.
- Activation or effect: Enforcing episode completion and consequential reward signal; no semantic approval of reasoning or skill.
- Evidence limits: Reference provenance, actual answers and downstream effects unobserved. History includes retrieved user information, so matched tag origin is not guaranteed to be the final policy answer.

Target/domain: extracted answer string versus dataset target(s), under lowercase, punctuation/article removal and whitespace normalization. Evaluator: deterministic exact-match Python; reference oracle: supplied dataset target, not model judgment or independent world test. Owner: SearchEnv invokes scorer at terminal. Consumer/channel/force/horizon: environment reward and manager success feed trainer metrics/objective, enforcing numerical feedback in bounded episodes; terminal flag stops continuation. Code judges outcome; model proposes answers; humans configure data but do not approve each answer. No epistemic acceptance of the explanation or source passages occurs.

A falsifying case for “score proves semantic equivalence”: normalization maps `a-b` to `ab`; it can agree with target `ab` without preserving the intended token boundary. Exact matching is valid for its explicit normalization domain, not all factual meanings. SRC-1, `agent_system/environments/env_package/search/third_party/skyrl_gym/envs/search/utils.py`:

>     def remove_punc(text):
>         exclude = set(string.punctuation)
>         return "".join(ch for ch in text if ch not in exclude)
> --- `agent_system/environments/env_package/search/third_party/skyrl_gym/envs/search/utils.py`

>         if em_check(answer, ground_truth["target"]):
>             return score
>         else:
>             return format_score
> --- `agent_system/environments/env_package/search/third_party/skyrl_gym/envs/search/utils.py`

Combined history, rather than a proven final answer alone, is the actual target input:

>             chat_history_str = "".join([item["content"] for item in self.chat_history])
>             return compute_score(chat_history_str, self.ground_truth)
> --- `agent_system/environments/env_package/search/third_party/skyrl_gym/envs/search/env.py`

### Claims

#### EPI-CLM-recursive-evolution
Label: Recursive skill evolution claim

Distinct from [RT-CLM-reusable-patterns](runtime.md#rt-clm-reusable-patterns): this names feedback timing and co-evolution, not reusable abstraction alone. SRC-1, `README.md`, doctrine/design:

> - **Recursive Skill Evolution**: A dynamic mechanism where the skill library co-evolves with the agent's policy during RL by analyzing validation failures.
> --- `README.md`

Implementation supports the validation-triggered training-bank path and a separate policy optimizer. It does not establish accepted fixes or actual co-improvement. No observed/causal experiment supplied.

#### EPI-CLM-context-efficiency
Label: Context efficiency claim

Distinct from [RT-CLM-reusable-patterns](runtime.md#rt-clm-reusable-patterns): magnitude and reasoning utility are performance claims, not bank format. SRC-1, `README.md`, reported operation:

> - **Context Efficiency**: Achieves 10-20% token compression compared to raw trajectory storage while enhancing reasoning utility.
> --- `README.md`

No supplied measurement/comparison establishes this magnitude or utility effect. Rendering/cleanup wiring alone cannot supply them.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; supplied [RT-BAP-skill-conditioning](runtime.md#rt-bap-skill-conditioning) and [RT-BAP-policy-parameters](runtime.md#rt-bap-policy-parameters) cover the retained instruction and parameter consumers. Added route records state their distinct immediate consumers and forces.

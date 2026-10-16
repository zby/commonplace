---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "SkillRL memory: persistent textual skill banks, alternate experience retrieval, bounded episode context and failure-fed admission."
run-id: AAS-2026-10-14-skillrl-0dba0e1c895e-01
source-identity: "https://github.com/aiming-lab/SkillRL"
reviewed-boundary: "4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d"
---

# SkillRL memory report

## Boundary and evidence

The subject is SkillRL's memory and context machinery inside the frozen builder/improvement-plane [boundary](boundary.md). SRC-1 is the only source, at commit `4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d`. The supplied runtime is provisional evidence, not the limit of inspection. Direct reads add the complete memory implementations, ALFWorld/Search/WebShop manager branches, SFT memory creation and aggregation portions, distillation selection, repetition cleanup and the WebShop final validation pass. These are implementation evidence; the bank example is shipped content, not an observed execution of its producer.

Included are persistent skill content and metadata, derived experience records, optional dense indexes, episode buffers, offline and failure-fed writes, withdrawal capabilities and later prompt consumers. Numerical policy state and checkpoint separation are retained through supplied runtime records. Provider-internal storage and reasoning are opaque. External rollout provenance and external SFT fitting are outside frozen evidence. General bundled training/framework mechanisms not reached by these paths remain outside the memory account; this prevents framework-wide guarantees, not the specific memory findings below.

| Operation or included part | Source paths in SRC-1 | Coverage and limits |
|---|---|---|
| Load, select, render, append, remove and save skills | `agent_system/memory/skills_only_memory.py` | Direct complete read; [MEM-OBJ-skill-content](#mem-obj-skill-content), [MEM-OBJ-skill-metadata](#mem-obj-skill-metadata), [MEM-RTE-bank-maintenance](#mem-rte-bank-maintenance); supplied [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout). |
| Alternate bank/experience load, goal embedding, FAISS search, budget and display | `agent_system/memory/retrieval_memory.py` | Direct complete read; [MEM-OBJ-experience-records](#mem-obj-experience-records), [MEM-CMP-retrieval-encoder](#mem-cmp-retrieval-encoder), [MEM-OBJ-retrieval-index](#mem-obj-retrieval-index), [MEM-RTE-experience-selection](#mem-rte-experience-selection). |
| Experience save API and unfinished manager save hook | `agent_system/memory/retrieval_memory.py`, `agent_system/environments/env_manager.py` | Direct; [MEM-RTE-experience-save](#mem-rte-experience-save). No shipped caller found in bounded search, and no live-bank append in API. |
| ALFWorld/Search/WebShop reset and observation delivery | `agent_system/environments/env_manager.py` | Direct branches; [MEM-CLM-search-category](#mem-clm-search-category); supplied rollout route plus annotation. WebShop's later length handling and non-skill environment context branches not fully traced: prevents uniform truncation guarantees across managers. |
| Episode history and context filtering | `agent_system/memory/memory.py`, `agent_system/multi_turn_rollout/rollout_loop.py` | Direct complete buffer read and collector scoped search; [MEM-OBJ-episode-history](#mem-obj-episode-history). Other non-skill managers remain available, uninspected in detail; no repository-wide working-context inventory claimed. |
| Failure analysis, key checks, ID assignment, update summary | `agent_system/memory/skill_updater.py` | Direct complete read; annotations on [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission) and [RT-RTE-training-admission](runtime.md#rt-rte-training-admission). Trainer scheduling, reconstruction and checkpoint behavior supplied, not independently audited here. |
| Original offline generators and shipped memory/bank inputs | `skill_generation/alfworld.py`, `skill_generation/search.py`, `skill_generation/webshop.py`, `memory_data/alfworld/claude_style_skills.json`, `memory_data/search/claude_style_skills_search.json` | ALFWorld production supplied by [RT-RTE-offline-production](runtime.md#rt-rte-offline-production); Search/WebShop scoped source search and initial bank portions directly inspected. Full input provenance, all prompt semantics and WebShop generator failure extraction remain uninspected; equivalence of generator semantics is not asserted. |
| SFT trace cleanup, memory creation, bank aggregation, distillation selection | `examples/sft_data_generation/preprocess/dedupe_repetitions.py`, `examples/sft_data_generation/skill_memory/generate_memory_alfworld.py`, `examples/sft_data_generation/skill_memory/aggregate_skills.py`, `examples/sft_data_generation/distillation/skill_retrieval.py` | Direct selected functions; [MEM-RTE-trace-abstraction](#mem-rte-trace-abstraction). Full parsing and Search/WebShop memory generation remain available but not inspected; prevents authentication and cross-environment equivalence claims. |
| Distilled reasoning and final training data | `examples/sft_data_generation/distillation/distill_alfworld.py`, `examples/sft_data_generation/distillation/distill_search.py`, `examples/sft_data_generation/postprocess/sharegpt_to_pairs.py`, `examples/sft_data_generation/postprocess/validate_and_fix_webshop.py` | Supplied [RT-RTE-sft-production](runtime.md#rt-rte-sft-production); Search import directly checked, pair conversion scoped search, WebShop final-pass read. Earlier WebShop repair phases remain uninspected in detail; cannot claim repairs preserve executed trajectories. |
| Policy weights and recovery artifacts | `verl/trainer/ppo/ray_trainer.py`, `verl/workers/fsdp_workers.py` | Supplied [RT-CMP-actor-rollout](runtime.md#rt-cmp-actor-rollout), [RT-RTE-policy-update](runtime.md#rt-rte-policy-update); trainer scoped search. Full optimizer/checkpoint serialization not independently inspected. |

There are no source access gaps for included checkout files. Available-but-uninspected parts above limit conclusions locally. No target code, provider, test or example was executed.

## Core ideas

The principal retained result is a JSON library of textual instructions, not a raw replay buffer. Skills are organized as general principles, category-specific principles and mistakes. Code selects their fields; the policy interprets those fields. Selection metadata and dense vectors are not equivalent to instruction content. See [MEM-OBJ-skill-content](#mem-obj-skill-content) and [MEM-OBJ-skill-metadata](#mem-obj-skill-metadata).

Failure-fed admission appends general instructions; it does not edit the challenged old principle or preserve a causal diagnosis. The updater sees old titles, bounded reconstructed failure excerpts and requested output fields. Later general-skill rendering drops applicability conditions. Thus the producer's requested qualifications need not reach the action consumer. See the annotations on the two admission routes and [RT-BAP-skill-conditioning](runtime.md#rt-bap-skill-conditioning).

Context selection is automatic host supply, not a policy-requested memory tool. Reset performs retrieval, but positive-history observation construction gates delivery. Template mode can grow without a hard general-skill cap because every dynamic skill is included. Embedding mode can instead omit dynamic instructions. Alternate legacy experience retrieval uses similarity thresholds and approximate character budgets; the skill-bearing alternate branch does not enforce its advertised token parameter. See [MEM-RTE-experience-selection](#mem-rte-experience-selection).

Search has a consequential producer/consumer mismatch: shipped query-type skills exist, and offline distillation reads them, but online `SkillsOnlyMemory` reads only `task_specific_skills`. General principles and mistakes still pass. This is a bounded loss of category content, not absence of all Search memory. See [MEM-CLM-search-category](#mem-clm-search-category).

## Shared records

### Components

#### MEM-CMP-retrieval-encoder
Label: RetrievalMemory goal encoder

Source-native identity: `RetrievalMemory.embedding_model_name`, default `Qwen/Qwen3-Embedding-0.6B`. Distributed-parametric SentenceTransformer weights loaded in process, with a global cache keyed by model name and device. The inspected path encodes goals, not parameter training. No immutable version is pinned; a name/path may resolve to changed weights. Distinct from the skills-only instance in [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model): different class, initialization and persistent-cache consumer, although the default model name matches. SRC-1, `agent_system/memory/retrieval_memory.py`.

> self.embedding_model = SentenceTransformer(self.embedding_model_name, device=device)
> --- `agent_system/memory/retrieval_memory.py:147-147`

### Operative objects

#### MEM-OBJ-skill-content
Label: Skill bank instruction content

Source-native identity: `general_skills`, `task_specific_skills` (or Search `query_type_skills`) and `common_mistakes` textual bodies. Natural-language titles, principles, applicability conditions, descriptions and avoidance instructions live in JSON files and loaded Python dictionaries. These are derived behavioral guidance, not raw traces. Shipped bank provenance is not authenticated; online additions derive from selected training/validation failures; offline additions derive from supplied experience. Later policy authority is model-interpreted guidance, not simulator permission. Updater authority differs: existing titles are deduplication hints, not the full principles. SRC-1, `agent_system/memory/skills_only_memory.py`, `agent_system/memory/skill_updater.py`, `memory_data/alfworld/claude_style_skills.json`. This is retained input/output of several supplied routes, not the trajectory batch [RT-OBJ-trajectory-batch](runtime.md#rt-obj-trajectory-batch); no counterpart object was declared in supplied runtime.

> "principle": "Search every plausible surface or container exactly once before revisiting; prioritize unopened or unseen locations to cover the whole room methodically.",
> --- `memory_data/alfworld/claude_style_skills.json`

The displayed general block preserves titles/principles but not applicability, IDs or provenance. Task-specific blocks add applicability; mistake rendering omits any `why_it_happens` reason. SRC-1, `agent_system/memory/skills_only_memory.py`.

> when = skill.get('when_to_apply', '')
> lines.append(f"- **{title}**: {principle}")
> if when:
>     lines.append(f"  _Apply when: {when}_")
> --- `agent_system/memory/skills_only_memory.py`

#### MEM-OBJ-skill-metadata
Label: Skill bank access metadata

Source-native identity: `skill_id`, category dictionary keys and document order. Symbolic metadata in the same JSON/dictionary substrate as [MEM-OBJ-skill-content](#mem-obj-skill-content), but consumed by code for deduplication, category choice and ordering. It is not a justification for skill truth. The updater rewrites IDs; template selection prioritizes the `dyn_` prefix, making an ID behavioral targeting metadata. Existing-ID filtering does not establish semantic novelty or even within-call duplicate filtering: the initial `existing_ids` set is not extended after each append. SRC-1, `agent_system/memory/skills_only_memory.py`, `agent_system/memory/skill_updater.py`. No corresponding supplied operative-object record exists; nearest supplied route is [RT-RTE-training-admission](runtime.md#rt-rte-training-admission).

> existing_ids = self._get_all_skill_ids()
>
> for skill in new_skills:
>     skill_id = skill.get('skill_id')
>     if skill_id in existing_ids:
>         print(f"[SkillsOnlyMemory] Skipping duplicate skill: {skill_id}")
>         continue
> --- `agent_system/memory/skills_only_memory.py`

#### MEM-OBJ-experience-records
Label: Derived experience records

Source-native identity: `RetrievalMemory.memories` and offline `generated_memories` JSON entries. Mixed parts: natural-language goal, description, planning pattern, mistake and refined action text; symbolic IDs, tags, outcome and structured step fields. Substrate: JSON files and Python collections. These are abstractions or heuristic projections of supplied trajectories, not authenticated raw interactions. Offline ALFWorld creation retains original goal/outcome, model-produced description, successful refinement and strategic guidance; heuristic save retains successful input steps but replaces failed steps with mistake descriptions. Different producer controls are separated in [MEM-RTE-experience-save](#mem-rte-experience-save) and [MEM-RTE-trace-abstraction](#mem-rte-trace-abstraction). Later consumers are offline aggregation and alternate retrieval; only selected display fields reach the policy. No counterpart to this durable object exists in supplied runtime; [RT-OBJ-trajectory-batch](runtime.md#rt-obj-trajectory-batch) is current-run source state, not this derivation. SRC-1, `agent_system/memory/retrieval_memory.py`, `examples/sft_data_generation/skill_memory/generate_memory_alfworld.py`.

> "task_meta": {"original_goal": goal},
> "refined_trajectory": refined,
> "strategic_guidelines": strategic,
> --- `examples/sft_data_generation/skill_memory/generate_memory_alfworld.py`

#### MEM-OBJ-retrieval-index
Label: Experience goal embeddings and index

Source-native identity: success/failure embedding arrays, FAISS indexes and `embeddings_cache.pkl`. Distributed dense vectors reside in NumPy arrays/pickle; symbolic index-to-record position maps reside in process. They derive from original goals, not a complete encoding of lesson content. The cache loader checks model-name equality, not memory-content/order identity or immutable encoder revision. This limits correspondence guarantees when a file is edited or replaced under the same directory/model name. It also deserializes host pickle, not policy-interpreted guidance. Distinct from skills-only in-memory cache in [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model). SRC-1, `agent_system/memory/retrieval_memory.py`.

> if cache_data['embedding_model_name'] == self.embedding_model_name:
>     self.success_embeddings = cache_data['success_embeddings']
>     self.failure_embeddings = cache_data['failure_embeddings']
> --- `agent_system/memory/retrieval_memory.py`

#### MEM-OBJ-episode-history
Label: SimpleMemory and SearchMemory episode buffers

Source-native identity: each class's per-environment `_data` list. Mixed natural-language observations/actions/information and symbolic record structure in process. Raw current-episode records, not derived persistent lessons. ALFWorld/WebShop store previous observation plus projected action; Search stores projected search action plus next information. Code exposes a verbatim suffix to later invocations, retaining earlier entries in host memory until reset. No model-facing arbitrary reload tool is established. This is working-context control, not the contract's accumulated-memory read-back. Distinct from full rollout training tensors in [RT-OBJ-trajectory-batch](runtime.md#rt-obj-trajectory-batch). SRC-1, `agent_system/memory/memory.py`, `agent_system/environments/env_manager.py`.

> if self._data is not None:
>     self._data.clear()
> self._data = [[] for _ in range(batch_size)]
> --- `agent_system/memory/memory.py:35-38`

### Routes

#### MEM-RTE-bank-maintenance
Label: Direct bank mutation and withdrawal

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Added count, removal boolean, or JSON file write and console output.
- Later read-back: Live-bank mutation affects future retrieval; saved JSON can be configured for later load. No deployed caller of removal was found in the bounded search.
- Delegated visibility: Direct caller supplies full dictionaries or a skill ID; no model/human approval is built into these methods.
- Selection predicate: Addition targets general or named category; removal matches exact ID across general/task lists, not mistake entries.
- Invalidation or expiry: Successful append/removal invalidates skills-only embedding cache; episode selections are not explicitly cleared by these methods.
- Activation or effect: Changes eligible instruction content; prompt delivery/compliance remains dependent on caller and manager progression.
- Evidence limits: Exposed API capability, not an independently wired automatic cleanup workflow; generic caller's human identity unresolved.

SRC-1, `agent_system/memory/skills_only_memory.py`. Distinct from model-proposal admissions [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission) and [RT-RTE-training-admission](runtime.md#rt-rte-training-admission): these public operations can bypass their parser/ID assignment. Caller proposes/decides; code rejects preexisting IDs for addition, but performs no content-quality test. Caller can withdraw matching entries and persist a changed bank; restoring an earlier file requires external choice/reconfiguration. No outcome oracle or experimental comparison belongs to this direct editing mode. Physical JSON I/O is not human content approval.

> if removed:
>     self._skill_embeddings_cache = None
>     print(f"[SkillsOnlyMemory] Removed skill: {skill_id}")
> return removed
> --- `agent_system/memory/skills_only_memory.py`

Removal replaces lists, while reset-cached selections hold skill dictionaries; therefore withdrawal need not retroactively revoke the already-selected prompt material before reset. An automatic removal caller was not found by `remove_skill\(` search in `agent_system`, `verl`, `examples` at the frozen revision. This search warrants only a bounded caller limit, not repository-wide absence.

#### MEM-RTE-experience-selection
Label: Alternate experience and skill selection

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Retrieved structured selections to ALFWorld/Search manager reset, later rendered observation strings.
- Later read-back: Previously derived experience JSON can be loaded and selected for a later policy invocation; loading static shipped content alone is not evidence of accumulated read-back.
- Delegated visibility: Policy sees extracted patterns, example goals and limited action/observation prefixes or mistakes, not whole stored records or dense vectors.
- Selection predicate: If skills are truthy, first six general skills, all detected-category skills and first five mistakes; optional two successful examples after top-three similarity search at 0.6. Otherwise goal-similarity success and failure search with configurable threshold/top-k and approximate budgets.
- Invalidation or expiry: Loaded memory collections and index remain instance state; save_trajectory does not refresh them. Episode selections reset at next reset.
- Activation or effect: Supplies guidance on noninitial positive-history manager branches; reliable action change remains unobserved.
- Evidence limits: Goal similarity is not demonstrated semantic relevance of lessons; advertised max_tokens is not enforced on the skills branch, nor a tokenizer-exact constraint on legacy branch.

SRC-1, `agent_system/memory/retrieval_memory.py`, `agent_system/environments/env_manager.py`. This is a distinct alternative selector upstream of supplied [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout), not a duplicate complete rollout. Host reset decides selection and automatic supply. Legacy allocation uses 500 estimated tokens for patterns, 300 for mistakes and remainder for examples; `len(json.dumps(item)) // 4` estimates size and stops at first nonfitting item. Rendering then further drops fields: legacy successful examples show at most five steps; skill-style examples show four actions. Storage budget is not identical to consumer context budget.

> if self.skills:
>     return self._retrieve_with_skills(task_description, max_tokens, include_examples)
>
> # Fallback to legacy trajectory-based retrieval
> return self._retrieve_legacy(task_description, top_k, similarity_threshold, max_tokens)
> --- `agent_system/memory/retrieval_memory.py`

#### MEM-RTE-experience-save
Label: Heuristic experience file save

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Appended serialized derived record at caller-provided save_path.
- Later read-back: Reload by a subsequently constructed RetrievalMemory can expose the record; no same-instance memory/index append occurs here and no shipped saver caller was found in the bounded search.
- Delegated visibility: API receives task, steps and caller's success boolean; later policy sees the selection route's display projection.
- Selection predicate: Success selects retained steps and ordered unique heuristic action types; failure selects repetitive-action, wandering, early-stop or generic mistake descriptions instead of steps.
- Invalidation or expiry: File grows; invalid JSON is replaced by an empty list before append. Live memory collections/index are not invalidated.
- Activation or effect: Creates potential behavior-shaping guidance, not an established live online experience-learning loop.
- Evidence limits: Caller-supplied outcome is not independently checked; heuristic diagnoses are not causally verified.

SRC-1, `agent_system/memory/retrieval_memory.py`, `agent_system/environments/env_manager.py`. No supplied counterpart after comparison with [RT-RTE-offline-production](runtime.md#rt-rte-offline-production), which uses model bank generation, not this heuristic save operation. Caller owns admission and supplies outcome; code determines transformation and file replacement. Generic caller identity leaves human control unresolved. No quality veto/rollback is wired. Manager `save_episode_trajectories` ends in a placeholder; search of `save_trajectory\(` and `save_episode_trajectories\(` across `agent_system`, `verl`, `examples` found definitions and documentation, not executable callers.

> pass  # Actual saving logic will be called from trainer
> --- `agent_system/environments/env_manager.py`

#### MEM-RTE-trace-abstraction
Label: SFT trace abstraction stages

Part of: [RT-RTE-sft-production](runtime.md#rt-rte-sft-production)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Cleaned trajectory JSON, per-trajectory derived memory JSON, and aggregated skill bank JSON in shipped batch pipeline.
- Later read-back: Aggregator reads derived patterns/mistakes; distillation loads the bank and includes selected fields in generated conversations. Final pairs are destined for external SFT fitting.
- Delegated visibility: ALFWorld memory model sees goal/outcome and serialized trajectory; aggregator sees planning patterns or mistakes, not necessarily raw records or refinement rationale. Distillation sees rendered bank and recorded steps.
- Selection predicate: Repetition cleanup compares consecutive action sequences; ALFWorld memory generation defaults to first trajectory per entry, outcome from all_success label; aggregation uses successful planning patterns for principles and failure mistakes for avoidance rules.
- Invalidation or expiry: Regenerated files replace outputs; parse/API failure can leave empty/partial model fields or skip entries. No automatic semantic rollback established.
- Activation or effect: Produces textual behavioral guidance and reasoning-enriched training data; downstream fitting and better future behavior are unobserved.
- Evidence limits: Full parsing and environment-specific memory prompts were not audited; source labels and supplied rollout history do not authenticate execution or causal pruning.

SRC-1, `examples/sft_data_generation/preprocess/dedupe_repetitions.py`, `examples/sft_data_generation/skill_memory/generate_memory_alfworld.py`, `examples/sft_data_generation/skill_memory/aggregate_skills.py`, `examples/sft_data_generation/distillation/skill_retrieval.py`. The route is a material stage of the supplied SFT container, not a replacement. Human chooses input/configuration, not each lesson. Models propose abstraction/aggregation; software constructs IDs and files. Recorded outcome labels drive inclusion, without an independent new-outcome oracle. Repetition deletion compares actions alone, so identical commands with changed observations can be removed; this does not establish behavior-preserving cleanup.

> if last == prev:
>     del cleaned[-pattern_len:]
>     break
> --- `examples/sft_data_generation/preprocess/dedupe_repetitions.py`

> general = call_llm(client, model, GENERAL_PRINCIPLES_PROMPT, {"planning_patterns": all_patterns})
> general = _assign_skill_ids(general, prefix="gen")
> --- `examples/sft_data_generation/skill_memory/aggregate_skills.py`

General aggregation retains rules with assigned IDs, not explicit links back to individual trace evidence. The memory records retain selected outcome/goal data, but aggregation's output does not carry their UUID lineage into each skill. Rationale cannot be assumed preserved because the model was asked to refine a trajectory. Distillation selection reads all general rules, chosen-category rules and all mistakes, unlike online fixed slices. Its formatter drops general applicability and mistake reasons as well.

### Claims

#### MEM-CLM-search-category
Label: Search category delivery mismatch

The online Search manager instantiates the shared SkillsOnlyMemory, whose category lookup and embedding cache use `task_specific_skills`. Search's original generator, shipped bank and SFT aggregator instead use `query_type_skills`. Thus those query-type instructions are not selected by either online skills-only mode in the inspected path; general and mistake delivery remains possible. Offline distillation explicitly supports the Search key and therefore falsifies a broader claim that all consumers lose Search categories. SRC-1, `agent_system/environments/env_manager.py`, `agent_system/memory/skills_only_memory.py`, `skill_generation/search.py`, `memory_data/search/claude_style_skills_search.json`, `examples/sft_data_generation/skill_memory/aggregate_skills.py`, `examples/sft_data_generation/distillation/skill_retrieval.py`. This qualifies the Search extension of [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout); no supplied claim declares this mismatch.

> task_specific = self.skills.get('task_specific_skills', {})
> goal = task_description.lower()
> --- `agent_system/memory/skills_only_memory.py`

> "search": "query_type_skills",
> --- `examples/sft_data_generation/distillation/skill_retrieval.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout)

Memory consumers differ by part: code interprets IDs/categories/counts; the actor interprets selected instruction bodies; optional encoders generate ranking vectors. Reset selection caches dictionaries in process. Copying their display text into an observation establishes delivery, not model dependence. Skills-only accepts `max_tokens`, `similarity_threshold` and `include_examples` through ignored `**kwargs`; no per-bank token accounting is implemented there. All dynamic general skills can outgrow top-k in template mode; embedding mode ranks instead. Source trust is operator file selection plus JSON load, not evidence authentication. SRC-1, `agent_system/memory/skills_only_memory.py`, `agent_system/environments/env_manager.py`; supplied runtime retains the minimum dynamic-selection and initial-delivery quotes.

Working context uses episode-local buffers and host suffix selection, not a separate child model. Old turns are omitted preferentially, while host entries remain until reset. Skills are copied by value into each later prompt; there is no policy-controlled pointer/reload mechanism in these inspected methods. The per-environment isolation resembles a task frame, but no child frame's summary or return crosses to a parent. SRC-1, `agent_system/memory/memory.py`, `agent_system/environments/env_manager.py`. Collector token limits are additional left/right/middle/error controls, not source-aware eviction of less useful material, SRC-1, `agent_system/multi_turn_rollout/rollout_loop.py`.

#### On [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission)

The admitted durable part is [MEM-OBJ-skill-content](#mem-obj-skill-content), controlled by software/model admission without per-content human approval in the traced path. Updater prompt requests principle and applicability but parser requires only skill_id/title/principle. It keeps an in-process update history of counts and IDs, not source excerpts, criticism or reasons. History counts include reassigned outputs before the final cap, so the summary is not necessarily admitted-bank size. The trace-to-rule chain runs reconstructed failures → bounded excerpts plus old titles → model array → key filter/ID rewrite → general append/save → future reset/display. SRC-1, `agent_system/memory/skill_updater.py`; trainer's wiring and limitations remain supplied rather than independently re-established.

> self.update_history.append({
>     'num_failures_analyzed': len(failed_trajectories),
>     'num_skills_generated': len(reassigned),
>     'skill_ids': [s.get('skill_id') for s in reassigned],
> })
>
> return reassigned[:self.max_new_skills_per_update]
> --- `agent_system/memory/skill_updater.py`

> if all(k in s for k in ['skill_id', 'title', 'principle'])
> --- `agent_system/memory/skill_updater.py`

Admission persists advice, not a link to the originating failure or an old-principle challenge. Old titles guide avoidance of duplicate topics; they do not provide old claims for content-directed criticism. Later general rendering reads principles, not stored applicability or update history. Raw failures are not retained in the bank by this mechanism. SRC-1, `agent_system/memory/skill_updater.py`, `agent_system/memory/skills_only_memory.py`.

#### On [RT-RTE-training-admission](runtime.md#rt-rte-training-admission)

The same bounded abstraction, key admission, lossy general display and history limits apply. Trace origin differs: reconstructed training batch rows rather than validation inputs/outputs, as supplied in this route. The actual later consumer is training rollout policy after reset, not the updater's current call. Persisted bank JSON is distinct from numerical policy checkpoints; reconfiguration is needed for cross-run bank read-back. SRC-1, `agent_system/memory/skill_updater.py`, `agent_system/memory/skills_only_memory.py`; supplied trainer evidence in the cited route.

#### On [RT-RTE-sft-production](runtime.md#rt-rte-sft-production)

Alternative retained forms matter: intermediate cleaned traces, derived experiences, bank JSON, reasoning-enriched conversations and final instruction/output pairs have different consumers. Model-generated reasoning is a derived display/training body, not authentication of recorded action correctness. WebShop's final validation code removes absent/invalid action formats but counts admissible-action mismatches without dropping those items; its validation label alone is not a universal admissibility veto. Earlier fixes are only partially inspected here. SRC-1, `examples/sft_data_generation/postprocess/validate_and_fix_webshop.py`.

> if action.lower() not in adm_lower:
>     final_issues += 1
>
> final_data.append(item)
> --- `examples/sft_data_generation/postprocess/validate_and_fix_webshop.py`

## Write side

Offline production and SFT processing use externally supplied trace files. Human input/configuration selection is distinct from human approval of generated claims. The original offline generator route writes a bank after model JSON generation, as supplied in [RT-RTE-offline-production](runtime.md#rt-rte-offline-production). Newer SFT stages separate cleanup, model memory creation and model bank aggregation in [MEM-RTE-trace-abstraction](#mem-rte-trace-abstraction). Exact initial trace provenance remains unresolved rather than being attributed to SkillRL's own live collector.

Online failure admission is append-oriented. The two supplied admission routes retain distinct scheduling and failure origins but share the updater and bank-adder. Required-key checks, ID uniqueness against existing state and empty-on-error returns reject some proposals; they do not verify usefulness or causal diagnosis. Direct mutation can bypass that pathway. [MEM-RTE-bank-maintenance](#mem-rte-bank-maintenance) affords withdrawal, but neither a post-admission outcome veto nor automatic expiry/removal is established on these traced paths. Retained advice can express reasons in its natural-language principle, but the code does not ensure or separately retain failure rationale or lineage.

The experience saver is another write surface, not evidence that completed episodes automatically populate retrieval memory. Its unfinished manager hook and lack of live-index refresh prevent that claim. See [MEM-RTE-experience-save](#mem-rte-experience-save). Numerical fitting is separate: [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) changes policy weights, not explicit textual reasons. Separately saved step banks are not a coupled policy/bank recovery transaction.

## Read-back

The principal chain is changed bank → future manager reset → automatic category/ranking selection → cached selected dictionaries → noninitial positive-history observation → policy user-message tokens. This is host-push context supply, although reset requests retrieval internally; there is no demonstrated foreground policy pull. Initial calls and nonpositive history do not receive the selected skills. Static shipped rules follow the same delivery path but are not accumulated read-back. SRC-1, `agent_system/environments/env_manager.py`; [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout).

Changed JSON can cross runs only when the operator configures it for loading. A save method or skill file is not by itself an actual later consumer. The heuristic experience save capability lacks shipped live-loop wiring; alternate retrieval does have manager consumers for configured records. Dense representations select bodies and never substitute for their interpreted content. Approximate memory budgets, dynamic overflow and final collector token limits prevent assuming every newly retained rule reaches a complete prompt. See [MEM-RTE-experience-selection](#mem-rte-experience-selection).

SFT aggregation reads selected model-produced patterns/mistakes; distillation reads bank text and source steps; external fitting would read final pairs. These are successive consumer authorities, not one uniform memory effect. Offline Search category consumption is valid where online consumption fails, as shown in [MEM-CLM-search-category](#mem-clm-search-category). Current episode suffixes are working state, not new persistent lessons; no automatic compaction summary is produced by the inspected buffers.

## Integration issues

1. **Search qualification:** [MEM-CLM-search-category](#mem-clm-search-category) corrects any inference from [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout) that the Search bank's query-type skills traverse the shared online selector. General/mistake guidance remains; offline distillation has a different schema-aware consumer. Consequence: do not extend hierarchical category delivery uniformly across environments.
2. **ID guarantee scope:** [MEM-OBJ-skill-metadata](#mem-obj-skill-metadata) narrows existing-ID checks described in [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission): direct add does not update its initial seen set during one call. Updater-mediated serial proposals still receive reassigned IDs. Consequence: deduplication is pathway-specific, not a bank invariant.
3. **Experience saver:** [MEM-RTE-experience-save](#mem-rte-experience-save) and [MEM-RTE-experience-selection](#mem-rte-experience-selection) must not be joined into automatic online trajectory learning without missing caller/index-refresh evidence. SRC-1 manager hook is a placeholder; bounded caller search found no invocation. Saved files afford future reloading, not same-instance update.
4. **Cache correspondence:** [MEM-OBJ-retrieval-index](#mem-obj-retrieval-index) establishes only a model-name cache check. Memory replacement under the same cache path can break goal-vector correspondence; no run establishes whether that occurred. This limits correctness, not the existence of retrieval.
5. **SFT containment and quality:** [MEM-RTE-trace-abstraction](#mem-rte-trace-abstraction) is a stage of [RT-RTE-sft-production](runtime.md#rt-rte-sft-production), not a duplicate. Cleanup can delete action repetitions despite changed observations; final WebShop validation does not veto every mismatch. Earlier repair phases, exact parsing semantics, Search/WebShop memory-generation semantics and external fitting remain unresolved. These prevent blanket faithful-trace/validated-data claims.
6. **Recovery and source gaps:** Initial shipped/externally supplied experience provenance, exact provider weights and behavior, full WebShop context-length handling, non-skill manager context control and coupled policy/bank recovery remain unestablished. Relevant records are [MEM-OBJ-experience-records](#mem-obj-experience-records), [MEM-CMP-retrieval-encoder](#mem-cmp-retrieval-encoder), [RT-CMP-skill-updater](runtime.md#rt-cmp-skill-updater), [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) and [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout). Available source is not an access gap.

No new declaration intentionally duplicates a supplied referent. The SFT part is explicitly contained; the alternate selector overlaps the rollout's upstream context boundary but is not its full referent. Other closest supplied-record comparisons are retained in declarations.

## Limitations and checks

Source HEAD was rechecked against the full boundary commit. Required member identities and contracts were read in full before source inspection. One guessed distillation helper path did not exist; inspection followed `distill_search.py`'s actual import to `skill_retrieval.py` instead. No outside source, prior analysis, target execution or model-provider call supplied evidence. Implementation supports available/wired retention and delivery, not exercised compliance, reliable lessons, causal learning gains or successful coupled recovery.

Deterministic output validation: passed with the invocation's prepared `commonplace-run validate-output` command after disambiguating the encoder quotation using its validator-supplied source range. The pass establishes structure, citation resolution and quotation occurrence, not analytical correctness or coordinator acceptance.

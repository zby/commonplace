---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "SkillX memory: experience-derived plans and skills, provisional extraction state, checkpoint recovery and retrieval-to-prompt limits."
run-id: AAS-2026-10-14-skillx-61e3fc8f9aa5-01
source-identity: https://github.com/zjunlp/SkillX
reviewed-boundary: b0047c848dbbcf019363d6d56eef8c558f69aefc
---

# SkillX memory report

## Boundary and evidence

SkillX retains reusable task plans, functional implementations and atomic tool-use examples. This account includes their extraction, transformation, admission, persistence, retrieval and formatting; provisional extractor memory; copied feedback summaries; synthetic-task checkpoints; and embedding-derived access state. It follows the whole-system [boundary](boundary.md) at SRC-1, commit `b0047c848dbbcf019363d6d56eef8c558f69aefc`. The supplied [runtime](runtime.md) orders the trace but does not delimit inspection.

Evidence is implementation and source-native doctrine/design, not newly observed execution. Direct reads added here cover complete `core/skill.py`, `data/loaders.py`, `data/exporters.py`, `extraction/tool_summary.py`, `inference/skill_usage.py`, `inference/embedding_service.py` and `inference/prompt_formatters.py`; bounded bodies of `pipeline.py`, `extraction/skill_extractor.py`, `extraction/plan_extractor.py`, `inference/retriever.py`, `expansion/task_manager.py`, `expansion/task_generator.py`, `preprocessing/trajectory_adapter.py` and `config/tool_schemas.py`. Correction-round direct reads also cover complete `data/schemas.py` and recheck complete `data/exporters.py`, establishing the blocked export preflight described below. All are SRC-1 at the frozen revision. Initial iteration-one sample entries are inspected artifact evidence, not proof that this commit produced them. Other iteration payloads and historical reward aggregates were not independently read here. Runtime findings about filters, rollout internals and wrapper stubs are supplied evidence, explicitly distinguished below.

Providers, embedding-server internals, external evaluator implementations and external acquisition directories remain outside the source boundary. Their absence from the capture prevents provenance, semantic-correctness, availability and deployment conclusions. Benchmark wrapper execution stubs and integration defects prevent treating prepared prompts as exercised task-agent memory. Available but uninspected benchmark-specific extraction adapters, optional strategy parsers, individual tool schemas and remaining sample entries limit exhaustive content claims, not the positive mechanisms established below.

| Entry point / operation | SRC-1 source paths | Coverage and records / prevented conclusion |
|---|---|---|
| CLI and direct pipeline construction | `pipeline.py`, `data/loaders.py` | Direct stage/CLI reads; [RT-RTE-library-build](runtime.md#rt-rte-library-build), [MEM-OBJ-skill-library](#mem-obj-skill-library). Direct caller settings can bypass skill filters. |
| Imported/normalized experience | `preprocessing/trajectory_adapter.py`, `data/loaders.py` | Direct adapter conversion reads; [MEM-OBJ-trajectory](#mem-obj-trajectory). Input origin and reward authenticity remain unresolved. CLI loader is not automatic benchmark normalization. |
| Long-feedback replacement | `extraction/tool_summary.py` | Direct complete read; [MEM-RTE-feedback-summary](#mem-rte-feedback-summary). No pointer reload or token-budget guarantee. |
| Plans, including merged-plan alternative | `extraction/plan_extractor.py`, `pipeline.py` | Direct extraction and orchestration, supplied runtime merge account; [MEM-OBJ-plan-skill](#mem-obj-plan-skill), [RT-RTE-library-build](runtime.md#rt-rte-library-build). Plan-combiner internals not fully inspected here; optimality unestablished. |
| Functional, atomic and hybrid extraction | `extraction/skill_extractor.py`, `pipeline.py` | Direct extraction, collection and preparation bodies; [MEM-RTE-proposal-context](#mem-rte-proposal-context). Standalone atomic collection has a type mismatch; admission does not erase provisional state. |
| Filtering and merge maintenance | `filtering/pipeline.py`, `filtering/base.py`, `clustering/merger.py`, `clustering/dbscan.py`, `core/skill.py` | Supplied [RT-CLM-quality-control](runtime.md#rt-clm-quality-control), [RT-RTE-response-eval](runtime.md#rt-rte-response-eval); direct library merge and content cleanup. No semantic validation guarantee. |
| Direct library admission and alternate export/import | `core/skill.py`, `data/exporters.py`, `data/loaders.py`, `data/schemas.py` | Direct complete reads; [MEM-OBJ-skill-library](#mem-obj-skill-library), [MEM-CLM-format-boundary](#mem-clm-format-boundary), supplied [EPI-RTE-export-validation](epistemic.md#epi-rte-export-validation). Standalone structural checks are implemented, but export preflight fails at schema construction before validation. Unchecked export and direct admission remain available; list, plan-only and unified files are not interchangeable. |
| Library loading, retrieval, step query, formatting | `inference/skill_usage.py`, `inference/retriever.py`, `inference/prompt_formatters.py` | Direct reads; [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare), [MEM-OBJ-retrieval-vectors](#mem-obj-retrieval-vectors). Step-query API has no established shipped execution-loop caller. |
| Alternative public plan rewrite | `inference/plan_rewriter.py` | Supplied corrected [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare) covers `PlanRewriteService.get_pseudo_plan`, which passes plural references correctly. No shipped caller found by runtime's name search; no persistence or later delivery established. This prevents a system-wide rewriting-unreachable conclusion without repairing the service mismatch. |
| Alternative public self-filter | `inference/retriever.py` | Direct complete class read; [MEM-RTE-self-filter](#mem-rte-self-filter). Independent `ainvoke`/`invoke` route, not the service's `SkillSelector`. |
| Benchmark-facing consumers | `inference/benchmarks/appworld.py`, `inference/benchmarks/bfcl.py`, `inference/benchmarks/tau2bench.py` | Supplied [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare), [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance); direct formatter check corroborates plan/policy omissions. Actual task-agent use unobserved. |
| Exploration, task generation and recovery | `expansion/env_worker.py`, `expansion/env_explorer.py`, `expansion/explorer.py`, `expansion/strategies/`, `expansion/task_manager.py`, `expansion/task_generator.py` | Supplied rollout/strategy findings; direct manager checkpoint and public generator/synthesizer reads; [RT-RTE-task-synthesis](runtime.md#rt-rte-task-synthesis), [MEM-OBJ-task-checkpoint](#mem-obj-task-checkpoint). Simulated versus real trace provenance remains route-specific. |
| Tool contracts, prompts and acquisition scripts | `config/tool_schemas.py`, `prompts/`, `scripts/` | Direct registry methods; supplied boundary/runtime acquisition and prompt evidence. Static contracts guide admission, not accumulated experience or callable tool installation. Individual schema correctness and external acquisition provenance uninspected. |
| Bundled libraries and historical evaluations | `skillx_db/`, `exp_log/` | Direct iter1 shape samples; supplied boundary historical-result limits; [MEM-CLM-format-boundary](#mem-clm-format-boundary). No inspected automatic historical-log-to-update consumer, complete content census or causal benefit conclusion. |

Repository Python searches covered CLI dispatch, schema/prompt registration, `SkillSelfFilter`, public task generators, library loaders/exporters, source metadata and modification keys. These expose additional APIs, not evidence of deployed hooks or an unsolicited memory-injection agent. No target code, tests, providers or services were executed.

## Core ideas

1. **The reusable result is instructional text, not installed functions.** Plans and skill bodies persist across tasks in JSON. Code uses names, types and tool lists to choose material; later model interpretation gives that material behavioral force. The reference-implementation warning in [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance) prevents equating Python-like skill content with callable tools.
2. **Admission has two different horizons.** Final-library admission occurs after optional filtering and merging, but proposals already enter extractor context before those checks. A later rejection does not necessarily withdraw their influence on subsequent extraction calls. [MEM-RTE-proposal-context](#mem-rte-proposal-context) separates that provisional path from the durable library.
3. **Selection is targeted and request-driven.** Task and plan-step text drive cosine ranking, then optional model selection and benchmark formatting. Counts bound candidates, not total prompt tokens. Plans and metadata can be returned without reaching the downstream prompt. [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare) and its annotation below give the actual consumer boundary.
4. **Persistence is selective about reasons.** Unified serialization preserves skill content and fixed metadata, not the extraction wrapper's modification rationale, input histories or filter discussion. Epoch summaries preserve counts. Tasks can retain expected actions and confidence without verified execution. This is trace-derived instructional memory, not evidence of improved capacity or a fully retained criticism history (SRC-1, `core/skill.py`, `pipeline.py`, `expansion/task_manager.py`).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-skill-library
Label: SkillLibrary persistence container

Source-native identity: `SkillLibrary` in SRC-1, `core/skill.py`. Storage: in-process Python object and JSON file through `save`/`load`; epoch snapshots and final unified output use the same serializer. Symbolic outer structure stores version, benchmark, creation time, planning map, functional/atomic lists and embedding configuration. Its text-bearing parts are declared separately below. The `FAISS-HNSW` configuration label is not an inspected persisted numerical index: serialization writes configuration, while the inspected inference retriever builds NumPy arrays.

> "embeddings": self.embeddings_config,
> --- `core/skill.py`

Compared with supplied [RT-RTE-library-build](runtime.md#rt-rte-library-build), this is its retained output object, not a duplicate route; runtime declares no object counterpart. Consumers are inference loading, tool-coverage queries and in-run expansion. Physical file writing is software I/O; caller identity alone establishes no human approval of individual entries. Direct `add_*` and `merge`, and exporter construction, admit caller-supplied content without the pipeline's model filters. Plans replace by task key; skill merge replaces same-name entries within the expected type list and suppresses incoming atomic skills whose focal name is covered by functional tools. Existing atomic entries are not swept merely because a later functional entry covers them. Cross-type same-name lookup can return an object from the wrong list, making `.index(existing)` fail; replacement is not a total conflict-resolution guarantee (SRC-1, `core/skill.py`, `data/exporters.py`).

> if skill.name in functional_tool_names:
>     dropped_atomic.append(skill.name)
>     continue
> --- `core/skill.py`

There is no tombstone represented by this serializer. This is a statement about this object's fields, not a system-wide absence claim. Removing or replacing a file externally does not automatically invalidate an already-loaded retriever. Recovery requires an explicit caller load of a prior snapshot; `run` starts fresh. Final epoch/statistics files contain summaries, not complete extraction/criticism transcripts (SRC-1, `pipeline.py`).

#### MEM-OBJ-plan-skill
Label: PlanSkill task plans

Source-native identity: `PlanSkill`, task-keyed in `SkillLibrary.planning` (SRC-1, `core/skill.py`, `pipeline.py`, `extraction/plan_extractor.py`). Natural-language steps, often API-named, are stored as `task`/`plan` strings with symbolic map keys and optional metadata. Storage is memory plus unified JSON; plan-only export has a separate shape. Lineage: successful-history extraction, optionally multi-plan combination, or direct caller-provided content. New extracted plans enter before skill filtering. Caller-provided `existing_plans` can guide extraction even when skip-plan mode leaves the saved library's planning map empty.

> for task, plan in new_plans.items():
>     skill_library.add_plan(task, PlanSkill(task=task, plan=plan))
> --- `pipeline.py`

Consumers: skill extraction receives plans by task; inference embeds task plus plan and returns matching plan text; AppWorld formatter can deliver it as reference guidance. BFCL/tau2 formatters omit it. Derivation history is not inherently retained: default pipeline creation supplies only task and plan, with empty metadata. No separate supplied object counterpart; closest supplied records are [RT-RTE-library-build](runtime.md#rt-rte-library-build) and [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare), respectively production and reading routes rather than this object.

#### MEM-OBJ-functional-skill
Label: Functional skill content

Source-native identity: functional `Skill` entries (SRC-1, `core/skill.py`, `extraction/skill_extractor.py`). Storage: list in library and JSON. `document` is natural-language description, parameters, outputs and notes; `content` is Python-like reference implementation. Its consumption by the downstream model is interpretive, not a fixed Python execution rule. Symbolic `name`/`tools`/type have separate access roles; metadata is below. Lineage: selected experience and plan-step prompt, optional supplied prior skills, model proposal, configurable quality/schema gates and cluster merge. Direct caller construction is an alternative lineage. Formatters deliver description/content, with names depending on benchmark; tool names do not confer execution permissions.

> return f"{self.name}\n{self.document}\n{self.content}"
> --- `core/skill.py`

Embedding input includes full content. Cleanup before clustering can change it: functional content is split at the first substring `return`, while the embedding text was assembled before that mutation. Thus the text clustered can differ from the content later saved, and this is not semantic-preserving program normalization (SRC-1, `extraction/skill_extractor.py`).

> if item.get("skill_type") != "atomic" and "return" in skill.get("content", ""):
>     skill["content"] = skill["content"].split("return")[0].strip()
> --- `extraction/skill_extractor.py`

Closest supplied record is the instruction channel [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance); that path is not this stored content. No supplied object counterpart.

#### MEM-OBJ-atomic-skill
Label: Atomic tool-use examples

Source-native identity: atomic `Skill` entries, with tool-centered document and example content, stored in memory/JSON (SRC-1, `core/skill.py`, `extraction/skill_extractor.py`). Natural-language examples can include action sequences; names and tool lists also support fixed coverage/filtering rules. Consumers are later extraction, coverage-based exploration and inference formatting. Pure atomic extraction visits all observed tools; computed missing-tool information does not alone gate its loop. Hybrid omission mode instead chooses uncovered tools after functional extraction. General quality filtering bypasses atomic candidates, while tool filtering remains separately configurable as described by [RT-CLM-quality-control](runtime.md#rt-clm-quality-control).

> for tool in all_tools:
> --- `extraction/skill_extractor.py`

This is distinct from functional content because derivation, bypass behavior and example consumption differ. Closest supplied record is [RT-RTE-library-build](runtime.md#rt-rte-library-build), not an object counterpart. The standalone atomic route's output key is collected as functional by `collect_skills_from_results`; the `skill_type` argument does not correct that branch. Therefore the source-native class label does not guarantee the saved category; see Integration issues. Hybrid `atomic_skill_metadata` has a separate correctly atomic-labelled branch (SRC-1, `extraction/skill_extractor.py`).

#### MEM-OBJ-skill-metadata
Label: Skill access and lineage metadata

Source-native identity: `SkillMetadata` and enclosing skill name/tool fields (SRC-1, `core/skill.py`). Symbolic values in Python/JSON include type, source task list, source tool, cluster ID, extraction epoch and timestamps. Names support matching/replacement and duplicate suppression; tools support eligibility/coverage; type supports partitioning. Source-task fields afford lineage retention but default to empty; their existence does not establish populated provenance. `merge` sets epoch and modified time, not a critique or evaluation reason.

> skill.metadata.extraction_epoch = epoch
> skill.metadata.modified_at = datetime.now().isoformat()
> --- `core/skill.py`

`SkillMetadata.from_dict` accepts a fixed field set, and `Skill.to_dict` serializes only the five skill keys. Outer extraction fields such as `option`, `modified_from`, `filter_result` and `embedding_text` are not the unified saved skill's rationale. Retrieval returns type/similarity and content fields but omits this provenance block. The prompt formatter does not read source tasks or filter reasoning. Distinct operative part from content; closest supplied [RT-RTE-library-build](runtime.md#rt-rte-library-build) covers update decisions rather than this metadata object.

#### MEM-OBJ-trajectory
Label: Raw and normalized experience histories

Source-native identity: caller trajectory dictionaries, normalized `task_history`, reward and optional `raw_data` (SRC-1, `data/loaders.py`, `preprocessing/trajectory_adapter.py`). Storage: loaded JSON/JSONL and in-process dictionaries; actual host state is separate. Messages mix natural-language feedback and code-like actions, with symbolic role/tool-call/reward fields. Adapters preserve the original record as `raw_data`, but pipeline preparation forwards selected history/plan/experience metadata rather than that entire raw record. Reward filtering trusts supplied outcome fields; benchmark labels do not authenticate execution or distinguish genuine from fabricated histories.

> "raw_data": raw,  # Keep original for reference
> --- `preprocessing/trajectory_adapter.py:119-126`

Later consumers: feedback summarizer, plan/skill extraction, and exploration analysis. Raw traces are not themselves the final instruction store: derived plans and skills cross to later tasks; unified serialization does not include the input trace. Real rollout and simulated trajectory origins remain distinct under [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout) and [RT-RTE-task-synthesis](runtime.md#rt-rte-task-synthesis). These are closest supplied routes, not duplicate objects. Original input initialization, human authorship and evaluator provenance remain unresolved for arbitrary caller files.

#### MEM-OBJ-retrieval-vectors
Label: Retrieval vectors and text cache

Source-native identity: retriever `_plan_embeddings`/`_skill_embeddings` and inference embedding service `_cache` (SRC-1, `inference/retriever.py`, `inference/embedding_service.py`). Dense derived numerical representations in NumPy arrays are distributed-parametric access material; text arrays, offsets and cache keys are symbolic mappings, not additional skill claims. They derive from task-plus-plan and name/document/content through an external model. Exact-text keys reuse encodings across requests. No model-version key protects against a mutable endpoint; the component fixity limits are in [RT-CMP-embedding-service](runtime.md#rt-cmp-embedding-service). This object is local result state of that component, not a second backend declaration.

> if use_cache and text in self._cache:
>     embeddings.append(self._cache[text])
> --- `inference/embedding_service.py`

Authority: numerical similarity determines eligible/ranked material, but vectors are not delivered as readable skill evidence. Reload rebuilds text/index state; changing a library object in place does not invoke rebuild automatically. Arrays are not saved by the unified serializer. Request failures produce zero encodings that may be cached; default positive threshold then suppresses matches, not stored skills. Operation remains unobserved.

#### MEM-OBJ-task-checkpoint
Label: Synthetic tasks and recovery checkpoint

Source-native identity: manager generated objectives and checkpoint `{results, processed_indices, tasks_hash, timestamp}` (SRC-1, `expansion/task_manager.py`). Task query/action text is natural language; confidence, IDs, batch indices and seed hash are symbolic control state. Stored as memory and optional JSON. Lineage is seed → simulated or real strategy trace → model objectives → software filters; checkpoint loading reuses results and skips processed batches. A public `TaskSynthesizer` also retains expected action sequence and source-trajectory ID in returned tasks, without itself checkpointing (SRC-1, `expansion/task_generator.py`).

> "results": results,
> "processed_indices": list(processed_indices),
> "tasks_hash": self._compute_tasks_hash(seed_tasks),
> --- `expansion/task_manager.py`

Seed hash covers ID and user task, not all rollout/model/filter settings. Mismatch deletes the checkpoint and starts fresh. Filtered results, not a replayable record of every rejected objective, are saved. Converting tasks preserves confidence/action metadata but produces empty histories and `reward=None`; those are proposed objectives, not successful experience. Closest supplied [RT-RTE-task-synthesis](runtime.md#rt-rte-task-synthesis) is the producer/recovery route, not a duplicate object. Later task execution remains an integration requirement, not an established automatic consumer.

### Routes

#### MEM-RTE-feedback-summary
Label: Long feedback summary substitution
Part of: [RT-RTE-library-build](runtime.md#rt-rte-library-build)

Trigger/owner: pipeline or direct caller invokes `ToolSummary`; code selects over-1,500-character `user`/`tool` messages; a model summarizes the selected feedback using the preceding action. The output replaces that message in a deep-copied trajectory. This is a distinct working-context transformation within the larger build, not a competing build declaration (SRC-1, `extraction/tool_summary.py`, `pipeline.py`).

- Immediate return: Copied history containing extracted `<feedback>` text, or original feedback when extraction fails; batch exceptions keep the original item.
- Later read-back: Subsequent plan/skill invocations receive this derived history; skills/plans can subsequently persist, but summaries are not separately checkpointed by the library serializer.
- Delegated visibility: Summarizer sees methodology, one preceding action and one feedback body; extraction later sees the resulting trajectory rather than a pointer to removed text.
- Selection predicate: Role is user/tool and content character length exceeds `max_len`, default 1500; no ranking or fixed final-length constraint.
- Invalidation or expiry: Copied summary survives in returned value for later calls; caller's original input remains separately available, without a designated reload tool or summary-to-source address.
- Activation or effect: Code substitutes returned text into extraction inputs; information preservation and changed downstream behavior are unobserved.
- Evidence limits: Trigger is character-based, not token occupancy; missing summary tags and batch exceptions preserve raw feedback rather than guarantee compression.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> result = deepcopy(trajectory_item)
> --- `extraction/tool_summary.py`

> return feedback if feedback else environment_feedback
> --- `extraction/tool_summary.py`

Admission: model proposes summary; software tag parsing chooses replacement, without human per-summary approval or an independent correctness oracle. Operating mode is bounded corpus preparation. There is no semantic veto beyond extraction/failure fallback and no source-content authentication. Original object availability is recovery, not automatic restoration in the copied input.

#### MEM-RTE-proposal-context
Label: Provisional extraction proposal reuse
Part of: [RT-RTE-library-build](runtime.md#rt-rte-library-build)

Owner: functional extractor appends proposed add/modify skills to its context list; atomic/hybrid extractors update their persistent instance map. These updates precede pipeline filtering, library conversion and final merge. This narrower part exposes an admission/read-back surface not represented by final-library success (SRC-1, `extraction/skill_extractor.py`, `pipeline.py`).

- Immediate return: Extraction result dictionaries plus changed local/context list or extractor `existing_skills` map.
- Later read-back: Subsequent functional plan-step invocations receive the augmented list; later atomic/hybrid tool invocations can receive the map's prior proposal for that tool, including across items on the same extractor instance.
- Delegated visibility: Models see selected successful history, optional failed history, task, specific step/tool and provisional skill context, not downstream filter reasons.
- Selection predicate: Parsed nonempty proposal list; `option` add/modify and presence of nested skill cause insertion; tool name chooses prior atomic entry.
- Invalidation or expiry: Instance lifetime bounds map reuse; local list lasts through extraction and may alias supplied experience metadata. No downstream rejection-removal call in these update bodies; replacing a map entry uses its skill name.
- Activation or effect: Proposals alter subsequent model-visible context before durable admission. Actual influence on output is unobserved.
- Evidence limits: Functional context originates in `exp_metadata.skills`, not automatically the accumulated functional library; atomic code reads its own map rather than the pipeline-prepared `skill_library` field. Concurrency and caller reuse prevent treating this as an ordered committed-library snapshot.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # Update skill library for next iterations
> for skill_item in skills:
>     if skill_item.get("option") in ["add", "modify"]:
>         if "skill" in skill_item:
>             skill_library.append(skill_item["skill"])
> --- `extraction/skill_extractor.py`

> self.existing_skills[skill_data["name"]] = skill_data
> --- `extraction/skill_extractor.py:373-382`

Admission: model authors and proposes; software admits parsed proposals into context before quality/schema vetoes. Workflow startup is not human content approval. No independent reference answer is checked; supplied rewards and optional failures are evidence inputs of unresolved provenance. Operating mode is bounded extraction. The add/modify/keep guidance and failure exclusion are supplied in [RT-RTE-library-build](runtime.md#rt-rte-library-build); this context retains proposed skill bodies, not necessarily the reasons or later verdict. Retrying/failing final admission does not undo this provisional write.

#### MEM-RTE-self-filter
Label: Alternative skill self-filter

`SkillSelfFilter` in SRC-1, `inference/retriever.py` exposes async/sync model selection over caller-supplied candidates. It is not the `SkillSelector` constructed by `SkillUsageService`; repository reference search found its class declaration but no shipped caller. Thus this is a public capability, not a second wired service path. Closest supplied [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare) has a different selector implementation and interface; [RT-RTE-response-eval](runtime.md#rt-rte-response-eval) covers related parser effects but not this class identity.

- Immediate return: Candidate dictionaries whose names occur in the parsed list; exhausted retries return all candidates.
- Later read-back: inapplicable — this operation does not itself load accumulated state; a caller must supply retained candidates and arrange later delivery.
- Delegated visibility: Task, plan and candidate names/full descriptions, not implementation content or source metadata.
- Selection predicate: Model returns fenced Python list; code evaluates it and matches names. Sync supports `chat` or `invoke`; async uses `ainvoke`.
- Invalidation or expiry: inapplicable — transient selection result; no stored update or cache invalidation.
- Activation or effect: Selection is implemented, including local `eval` parsing; no consumer call or changed task behavior observed.
- Evidence limits: Public API with unspecified caller supports selection capability only, not a retained-memory consumer route. Process permissions and provider outputs unobserved.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

> logger.warning("Failed to filter skills, returning all candidates")
> return skills
> --- `inference/retriever.py:351-354`

Model proposes names and code decides membership; exceptions cannot veto all candidates because fallback is fail-open. No human content approval, answer oracle or improvement comparison. Operating mode is an open selection request, not admission of revised content. Unlike the service selector's interface failure, shared `LLM.ainvoke` can satisfy this class's async call shape; that does not wire it into the service.

### Claims

#### MEM-CLM-format-boundary
Label: Library format compatibility

Claimed operation assessed: reloading retained library artifacts for inference. SRC-1 `core/skill.py` reads `data.get("skills", {})` and nested planning/functional/atomic members; `data/loaders.py` separately offers list and plan-only readers; `data/exporters.py` offers distinct output formats and explicit construction. The first shipped `func_atomic_skills.json` sample is an outer list of extraction wrappers with filter/embedding text; iter1 `plan.json` has top-level `train_epoch` and `plan`. Neither is the unified loader's nested format. A plan-only mapping loaded by `SkillLibrary.from_dict` therefore supplies no nested skills; an outer list cannot provide its `.get`. This is a static shape consequence, not an executed import test.

> skills_data = data.get("skills", {})
> --- `core/skill.py`

> return [data]
> --- `data/loaders.py:162-170`

List loading and `create_library_from_skills` provide explicit conversion ingredients; this is counterevidence to the stronger claim that the samples are unusable by any shipped API. However, `create_skill_service` does not apply those conversions. Plan-only exporter entries are dictionaries containing plan/metadata, whereas sampled plans map directly to strings; normalization remains caller work. Closest supplied [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare) establishes unified loading, not universal format compatibility. No supplied claim counterpart; the boundary already flags this question without declaring a shared record. Scope: sampled iter1 shapes and inspected serializers only; remaining sample contents are not characterized.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-library-build](runtime.md#rt-rte-library-build)

Memory-specific scope: raw histories → copied summaries → plans and candidate skills → filtered/merged instructions → saved unified library. Retention spans epochs and, through explicit inference reload, tasks/processes. `run` creates a new library; caller-provided existing plans and extractor maps are different initialization surfaces. Raw history origin and initial content admission are caller-controlled but not necessarily human-controlled. Software/model transformations need no per-content human approval (SRC-1, `pipeline.py`, `core/skill.py`, `data/loaders.py`).

Reasons and withdrawal: the in-memory epoch result retains candidate/filtered/merged dictionaries, but `save_results` writes epoch and statistics fields only, not those full results. Outer proposal/criticism/verdict fields do not survive fixed `Skill` serialization unless their substance was incorporated into document/content. Same-name replacement, suppression of incoming redundant atomic skills and caller reload are available; they do not retract old text from already-returned prompts or provisional extractor context. A renamed modification removes a candidate from the current collection by `modified_from`, not an old saved-library entry by that key. Final library merge uses the new name, so a renamed successor can coexist with its predecessor (SRC-1, `extraction/skill_extractor.py`, `pipeline.py`, `core/skill.py`).

> summary = {
>     "epoch": epoch_result.get("epoch"),
>     "statistics": epoch_result.get("statistics", {})
> }
> --- `pipeline.py`

#### On [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare)

Read-back is caller-requested pull: factory reloads the unified file; task query selects plans and candidate skills; plan text can drive subsidiary skill queries; formatter returns a prompt. There is no independent background push selector here. Default task plan retrieval is top three at threshold 0.45, then first match; skill retrieval uses four per parsed plan step or twice `max_skills` task candidates, then defaults to ten selected skills. The step API takes step text and defaults to five; it returns content dictionaries, not an installed prompt or execution call (SRC-1, `inference/skill_usage.py`, `inference/retriever.py`).

Budgets are item counts. Full selected documents/content can be arbitrarily long; neither formatter nor service enforces a total prompt-token cap. A truthy available-tools set filters by all listed tools; an empty set is falsy and therefore does not enforce zero available tools. Metadata carries retrieval detail but is not automatically model-visible. Formatters use descriptions and bodies, not source-task or filter rationale. BFCL drops plan and base prompt; tau2 drops plan but retains base policy; AppWorld retains plan as advisory reference. Service rewriting can fail before formatting, as the supplied record documents (SRC-1, `inference/skill_usage.py`, `inference/retriever.py`, `inference/prompt_formatters.py`).

> if tool_filter and not all(t in tool_filter for t in skill.tools):
>     continue
> --- `inference/retriever.py`

#### On [RT-RTE-task-synthesis](runtime.md#rt-rte-task-synthesis)

Retained tasks/checkpoints guide generation recovery, not verified skill adoption. Source traces can be real environment histories or simulated action/observation text; confidence is model output, not an independent evaluator result. Manager checkpoint loading can carry tasks across calls, but duplicate-tracker state is not in its saved fields. Final re-filtering can discard earlier tasks, as supplied runtime establishes and direct manager reads corroborate. Expected action sequence survives conversion as metadata even though execution history remains empty (SRC-1, `expansion/task_manager.py`, `expansion/task_generator.py`).

The public generator/synthesizer variants use `llm.chat` and exact-string query deduplication; full task parser requires query, float confidence and action sequence, attaching source trajectory ID where present. They return proposals, not automatically persisted experience. Shared `LLM` compatibility remains limited by the supplied runtime's missing `chat` finding; substituted callbacks/clients can satisfy it. This is additional public API coverage, not evidence the broken default expansion automatically improves the next epoch.

#### On [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout)

Working-context scope: each task gets an isolated local message frame; returned history/reward crosses back, not a durable conversational pointer. The inspected generic loop's stored tokenizer/model-length fields do not establish trimming. This supplied implementation account supports per-task isolation and caller-returned traces, not summary eviction or persistent worker memory. Real/client evaluator outcomes and generic completion-substring rewards have different trust limits; later extraction's numeric threshold does not repair those differences. Historical raw logs alone establish no trace-fed instruction update (SRC-1, `expansion/env_worker.py`, `expansion/env_explorer.py`; supplied record supplies passages).

## Write side

The main write chain is [RT-RTE-library-build](runtime.md#rt-rte-library-build). Caller files or normalization adapters supply [MEM-OBJ-trajectory](#mem-obj-trajectory); rewards select experience without authenticating its origin. Code selects shortest successful history for skill preparation even when planning uses multi-plan combination. The extractor APIs accept a failed trajectory, but default pipeline preparation searches for reward below 0.5 only among already-successful inputs, so it cannot supply that contrast at the default threshold. Feedback replacement is [MEM-RTE-feedback-summary](#mem-rte-feedback-summary); extraction outputs are instructional plans, descriptions, implementations and examples, not just replay logs. Plan admission occurs earlier and under different checks from skill admission (SRC-1, `pipeline.py`, `extraction/skill_extractor.py`).

Proposal authorship is model-based; physical persistence is code-based; individual human approval is unestablished. Direct library calls/imports are alternative admission mechanisms. Standalone deterministic schema predicates are implemented, but the optional `SkillLibraryExporter.validate_and_export` preflight is blocked: it passes `embeddings_config` to the `SkillLibrarySchema` dataclass, which declares `embeddings`. Construction therefore raises before `schema.validate()` and conditional export. This is a static implementation deduction, not an observed failure. The aggregate validator checks functional and atomic entries for nonempty fields/tools, not planning entries or semantic correctness; caller enforcement of standalone predicates is uninspected. Unchecked `export_json`, library `save` and direct `add_*`/`merge` admission remain separate supported paths, not checked-export gates (SRC-1, `data/exporters.py`, `data/schemas.py`; supplied [EPI-RTE-export-validation](epistemic.md#epi-rte-export-validation)). Quality/schema judgment and cluster merge are best effort with bypasses and fallback described in [RT-CLM-quality-control](runtime.md#rt-clm-quality-control). Pre-merge filtering alone does not validate the generated merged successor. Model parser `eval` is an execution effect, not an admission guarantee.

> functional=[s.to_dict() for s in library.functional],
> atomic=[s.to_dict() for s in library.atomic],
> embeddings_config=library.embeddings_config,
> --- `data/exporters.py`

> atomic: List[Dict] = field(default_factory=list)
> embeddings: Dict[str, Any] = field(default_factory=dict)
> --- `data/schemas.py`

Curation includes summary substitution, plan combination, candidate modification, clustering, model merging, functional `return`-substring cleanup, same-name replacement and incoming-atomic redundancy suppression. These operations request or perform transformations; their labels establish neither semantic improvement nor preserved correctness. `keep` produces no collected replacement. Rejection prevents final admission only on that route: [MEM-RTE-proposal-context](#mem-rte-proposal-context) can retain rejected material for later extraction. No inspected final-library sweep removes old atomic entries merely because new functional coverage appears.

Provenance is selective: fixed source metadata can retain task/tool/epoch fields, but default source lists can remain empty. Unified instruction files do not retain a linked raw history, filter criticism or `modified_from` record. Some rationale may appear in author-supplied prose; no later rationale-specific reader is established. Epoch counts cannot reconstruct rejected proposals. Snapshots allow explicit previous-file selection rather than automatic rollback or atomic update. Task-manager checkpoints are a separate recovery form with seed-hash validation and deletion on mismatch, not a library-resume protocol.

## Read-back

Three distinct implemented later-consumer chains are established. First, provisional proposals are returned to subsequent extraction-model invocations before durable admission. Second, compressed feedback replaces raw feedback for later plan/skill invocation. Third, unified saved library content reaches later retrieval and formatter requests; selected text is prepared for the task model under [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance). The task manager additionally reuses saved generation results/progress across calls. None establishes observed downstream behavioral dependence or benefit.

Selection is query-targeted rather than mere file addressing: task/step semantics drive embeddings and ranking; symbolic type/tool filters and name deduplication narrow candidates; optional selection models see descriptions rather than full provenance. Automatic subsidiary retrieval is triggered by a caller task request, not unsolicited supply. Item budgets and character-triggered summarization are not complete working-context token management. The alternative [MEM-RTE-self-filter](#mem-rte-self-filter) and step API are capabilities without established execution-loop delivery. The supplied corrected [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare) also establishes the public `PlanRewriteService.get_pseudo_plan` helper: it selects reference plans and correctly passes plural references to rewriting, returning pseudo-plan/metadata without saving or establishing later delivery. Its afforded invocation is distinct from the broken service call; actual outputs and behavioral use remain unobserved. Arbitrary get-by-name/get-by-tool accessors likewise establish storage access, not additional deployed memory routes.

The isolated-call mechanism resembles a frame: selected inputs enter each extraction/summary/rollout invocation and only values/results cross back. It does not supply heap-like references to evicted history. Summary text and skill content are copied by value into new messages; original caller inputs or files remain outside the window, without automatic liveness tracking or designated pointer dereference. This limits claims of memory paging or active-session compaction (SRC-1, `extraction/tool_summary.py`, `extraction/skill_extractor.py`; supplied [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout)).

## Integration issues

- **Provisional versus committed read-back:** the supplied corrected runtime now distinguishes the atomic proposal map from committed epoch-library feedback. Direct preparation does insert `item["skill_library"]`, but `AtomicSkillExtractor` reads its instance `existing_skills`; `temp_skill_library` from experience metadata is not consumed in the per-tool prompt. Known recurrence is the proposal map, not guaranteed final epoch-library synchronization. Keep [RT-RTE-library-build](runtime.md#rt-rte-library-build) qualified by [MEM-RTE-proposal-context](#mem-rte-proposal-context); SRC-1, `pipeline.py`, `extraction/skill_extractor.py`.
- **Blocked export preflight:** the earlier write-side description of an optional caller-selected checked export overstated the shipped control. Constructor mismatch prevents validation/export; standalone structural predicates and unchecked export/direct admission remain implemented. This agrees with the supplied [EPI-RTE-export-validation](epistemic.md#epi-rte-export-validation), rather than declaring a duplicate route. It qualifies the admission inventory for [MEM-OBJ-skill-library](#mem-obj-skill-library) and the export coverage row. SRC-1, `data/exporters.py`, `data/schemas.py`; passages retained in Write side.
- **Failure contrast is not automatically supplied:** default pipeline preparation receives only reward-selected successful inputs and searches those for a failed history below 0.5. Direct extractor callers can provide failures, but the default pipeline cannot at threshold 0.999. This narrows contrastive-evidence claims for [RT-RTE-library-build](runtime.md#rt-rte-library-build) and [MEM-RTE-proposal-context](#mem-rte-proposal-context), without denying the optional extractor input. SRC-1, `pipeline.py`, `extraction/skill_extractor.py`.
- **Standalone atomic type mismatch:** `AtomicSkillExtractor` stores output under `plan_step_metadata`; collector labels that branch functional regardless of its `skill_type` argument. Hybrid atomic output uses the separate atomic branch. [MEM-OBJ-atomic-skill](#mem-obj-atomic-skill) therefore cannot be interpreted as guaranteed saved atomic entries for standalone mode. Consequences include filtering partitions, merge suppression, retrieval type eligibility and tool-coverage meaning. SRC-1, `extraction/skill_extractor.py`, `pipeline.py`; affects [RT-RTE-library-build](runtime.md#rt-rte-library-build) and [RT-CLM-quality-control](runtime.md#rt-clm-quality-control).
- **Withdrawal is narrower than modification language:** current-collection `modified_from` removal, library same-name replacement and provisional name-keyed reuse are different mechanisms. Renaming can leave a durable predecessor; final rejection can leave provisional influence; existing redundant atomic entries are not globally purged. SRC-1, `extraction/skill_extractor.py`, `core/skill.py`; concerns [MEM-OBJ-skill-library](#mem-obj-skill-library), [MEM-RTE-proposal-context](#mem-rte-proposal-context), [RT-RTE-library-build](runtime.md#rt-rte-library-build).
- **Alternative selector is not the service selector:** [MEM-RTE-self-filter](#mem-rte-self-filter) adds a public `ainvoke`-based alternative and another response-`eval` site. It does not repair service `generate` mismatch or rewrite signature mismatch. It overlaps the function classes in [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare) and [RT-RTE-response-eval](runtime.md#rt-rte-response-eval), but has distinct source-native identity/call path, not a duplicate declaration. SRC-1, `inference/retriever.py`, `inference/skill_usage.py`.
- **Format and index labels:** [MEM-CLM-format-boundary](#mem-clm-format-boundary) resolves the boundary's sample-format question only for inspected iter1 shapes. Unified loading is not an automatic converter, and `FAISS-HNSW` is configuration rather than demonstrated persisted-index machinery. [MEM-OBJ-skill-library](#mem-obj-skill-library), [MEM-OBJ-retrieval-vectors](#mem-obj-retrieval-vectors), [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare); SRC-1, `core/skill.py`, `data/loaders.py`, `data/exporters.py`, `inference/retriever.py`.
- **Unresolved provenance and deployment:** arbitrary input histories/rewards, initial prior-skill admission, exact backend weights, authenticity/producing revision of bundled results and actual task-agent consumption remain unestablished. These prevent attributed learning, exercised memory authority and causal improvement conclusions, without negating implemented trace-to-instruction writes. Concerns [MEM-OBJ-trajectory](#mem-obj-trajectory), [MEM-OBJ-skill-metadata](#mem-obj-skill-metadata), [MEM-OBJ-task-checkpoint](#mem-obj-task-checkpoint), [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance). Evidence limits are SRC-1 and supplied boundary/runtime; no external investigation was authorized.

No new declaration is identified as the same referent as a supplied record. Contained routes use `Part of`; objects distinguish retained parts from supplied production/access routes. The issues above retain corrections and justified unknowns for reconciliation rather than silently replacing runtime-owned findings.

## Limitations and checks

Frozen checkout HEAD was rechecked as `b0047c848dbbcf019363d6d56eef8c558f69aefc`; `git status --short` showed no changes in that checkout. Source identity remains the registered SRC-1 repository. The analysis used direct source reading/search and supplied runtime findings only, not target execution or prior characterizations. Boundary, report types, collection rules and record contract were read completely. Sample-library coverage is bounded; individual external tool contracts, optional parser variants and historical aggregate outcomes are not exhaustively assessed. No missing execution evidence is treated as evidence of absent architecture.

Deterministic validation: the required `commonplace-run validate-output` check passed: “Member content check passes; invocation residue not checked.” This is not job acceptance or claim support. Structural and quotation validation does not establish analytical correctness, task execution or successful improvement.

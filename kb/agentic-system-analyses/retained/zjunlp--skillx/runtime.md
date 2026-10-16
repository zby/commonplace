---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "SkillX runtime baseline: trajectory-to-library construction, prompt preparation, exploration and change admission at the frozen commit."
run-id: AAS-2026-10-14-skillx-61e3fc8f9aa5-01
reviewed-boundary: b0047c848dbbcf019363d6d56eef8c558f69aefc
---

# SkillX runtime report

## Runtime account

SkillX's consequential work is converting experience into reusable planning, functional and atomic skills and selecting those skills for later model context. The shipped construction path is more complete than the shipped inference deployment: the pipeline writes libraries, while the benchmark agents stop at prompt preparation. Exploration has real environment adapters as well as model-simulated alternatives. These responsibilities all remain inside the [boundary](boundary.md); providers and benchmark implementations remain outside it.

This is an implementation trace, not a target execution. SRC-1 supplies the inspected code and prompts. No provider call, rollout or experiment was performed. The boundary's bundled historical result artifacts do not establish activation of the routes below at this commit. Operation and benefit remain uninspected here. Records below are runtime-owned referents; the supplied boundary declares no peer shared records to duplicate.

### Ordinary construction invocation

A caller supplies an input JSON/JSONL path, output directory, model and benchmark to `run_pipeline`, or equivalent CLI options. The convenience function loads dictionaries, creates `LLM`, constructs `IterativeSkillPipeline`, awaits `run`, and calls `save_results`. Direct callers can instead supply an LLM, schemas, existing plans, extraction modes, filtering timing and expansion objects. This is a Python package/module entry path; inspecting the CLI branch does not establish a successful installed command (SRC-1, `pipeline.py`, `data/loaders.py`).

For the default one-epoch, functional, non-expansion case, code owns progression; the model does not choose pipeline stages. The pipeline creates a fresh library, selects trajectories whose stored reward is strictly greater than 0.999, compresses long feedback, chooses the shortest successful history for each task, requests plans, requests step-specific skills, filters candidates, embeds and clusters them, requests merges, converts surviving dictionaries into `Skill` objects, and merges these into the library. Plans enter the library before skill filtering. A checkpoint is saved after the epoch, including an epoch returning no skills. Final files contain the unified library, epoch statistics and aggregate statistics; the return also contains in-memory results. These are the endpoints and admission decisions of [RT-RTE-library-build](#rt-rte-library-build).

Each extraction call gets a fresh message list: system methodology plus selected task/history/plan/library content, not an enclosing agent conversation. The functional extractor runs plan steps sequentially and can append newly proposed skills to the list shown at the next step. That list starts from the selected trajectory's `exp_metadata.skills`, not the accumulated functional library. Atomic/hybrid extraction instead reads its instance `existing_skills` map and updates it with proposals before filtering or final library admission. These provisional recurrence paths are not synchronized committed-library feedback; see [MEM-RTE-proposal-context](memory.md#mem-rte-proposal-context) (SRC-1, `pipeline.py`, `extraction/skill_extractor.py`). Batch execution uses `asyncio.gather` with a semaphore around batches, so `max_concurrent` bounds batches, not individual calls; each admitted batch can issue `batch_size` concurrent item calls. Failed items can become `None`, filter exceptions become rejection, and unsuccessful merging falls back to the cluster's first skill. These are partial-result policies, not transactional recovery (SRC-1, `extraction/base.py`, `extraction/skill_extractor.py`, `filtering/base.py`, `pipeline.py`).

Long-feedback compression is code-triggered at more than 1,500 characters for `user` or `tool` content. It sends the preceding action and feedback to a separate summarizer invocation and substitutes the extracted feedback in a deep-copied trajectory. The extraction consumers then see that copy. This is selective context replacement, not eviction of an active exploration conversation. The original input object remains available to the caller; no pointer-based reload protocol is created. The local call resembles an isolated frame returning a string, but subsequent windows receive values, not dereferenceable context pointers (SRC-1, `extraction/tool_summary.py`).

> if step.get("role") in ["user", "tool"] and len(step.get("content", "")) > self.max_len:
> --- `extraction/tool_summary.py`

### Later use and the actual delivery boundary

`create_skill_service` loads the saved unified library, creates an embedding client, and builds in-memory indices over task-plus-plan and skill name/document/content. A task request selects plans and skills; optionally a model rewrites the plan or selects names; a benchmark formatter returns a system-prompt string and metadata. The service exposes an additional step-query retrieval API. This is [RT-RTE-prompt-prepare](#rt-rte-prompt-prepare), with the text-authority channel in [RT-BAP-skill-guidance](#rt-bap-skill-guidance). Embeddings and generation are distinct distributed-parametric dependencies, [RT-CMP-llm](#rt-cmp-llm) and [RT-CMP-embedding-service](#rt-cmp-embedding-service).

Several transformations defeat a stronger inference claim. The service calls `rewrite` with `retrieved_plan`, but the method requires `retrieved_plans`; supplying the shared `LLM` also does not satisfy `SkillSelector`'s `generate` interface. The rewrite mismatch raises before successful rewriting; selection catches failures and returns the first candidates. AppWorld and BFCL wrappers request rewriting, while the tau2 wrapper disables it. BFCL's formatter drops both the supplied base prompt and plan; tau2 uses the base prompt as policy but omits the plan. AppWorld adds its static `HUMAN_SKILLS` to metadata only after formatting, not to the already-built prompt. Metadata presence therefore does not establish downstream delivery. All three benchmark `run` and `step` methods are stubs. These are inspected integration limits, not missing external evidence that could be assumed to repair the shipped calls (SRC-1, `inference/skill_usage.py`, `inference/plan_rewriter.py`, `inference/skill_selector.py`, `inference/prompt_formatters.py`, `inference/benchmarks/appworld.py`, `inference/benchmarks/bfcl.py`, `inference/benchmarks/tau2bench.py`).

> plan = await self.rewriter.rewrite(
>     task=task,
>     retrieved_plan=plan
> )
> --- `inference/skill_usage.py`

> async def rewrite(
>     self,
>     task: str,
>     retrieved_plans: List[Dict],
>     context: Optional[Dict] = None,
>     **kwargs
> ) -> Optional[str]:
> --- `inference/plan_rewriter.py`

A separate public helper, `PlanRewriteService.get_pseudo_plan`, retrieves up to its configured number of reference plans and passes the required plural `retrieved_plans` argument to `PlanRewriter.rewrite`. With rewriting disabled it returns the first retrieved plan; with no references it returns metadata and no pseudo-plan. Its return is not a library write or a shipped downstream delivery. A repository-wide Python name search found its declaration but no shipped caller. This afforded alternate invocation prevents a system-wide conclusion that rewriting is unreachable; it does not repair the benchmark/service mismatch above. Actual rewritten output and semantic relation to references remain unobserved (SRC-1, `inference/plan_rewriter.py`; [RT-RTE-prompt-prepare](#rt-rte-prompt-prepare)).

> pseudo_plan = await self.rewriter.rewrite(
>     task=task,
>     retrieved_plans=retrieved_plans,
>     **kwargs
> )
> --- `inference/plan_rewriter.py`

### Four forcing cases and guarantee coverage

1. **Quality admission is not universal validation.** Atomic candidates bypass general filtering; absent usable schemas for the entire batch returns Stage 1 survivors; partial schema coverage supplies only found schemas. The filter verdicts are model-text substring tests, and default pre-merge filtering does not validate the later merged result. Callers can choose `filter_timing="none"` or add library members directly. [RT-CLM-quality-control](#rt-clm-quality-control) bounds the owner, enforcement and strength. Neither an import prohibition in a prompt nor a `tools` list is an execution permission boundary (SRC-1, `filtering/pipeline.py`, `filtering/base.py`, `pipeline.py`, `core/skill.py`).
2. **Model-output parsing itself can execute Python.** The merger's JSON fallback and selector's list parser use `eval` on provider response fragments. This local effect route precedes any downstream environment worker and is not covered by tool schemas or prompt-only guidance. [RT-RTE-response-eval](#rt-rte-response-eval) separates this capability from both an exercised exploit and an actual deployment grant set (SRC-1, `clustering/merger.py`, `inference/skill_selector.py`).
3. **A real rollout is not necessarily a verified success.** Generic workers feed the whole assistant text to a host callback and use completion substrings as reward signals; AppWorld workers extract Python, call `world.execute`, and use the world's evaluator. The client-based real explorer additionally admits provider-native tool calls via `chat(..., tools=...)`, or a text-only `ainvoke` alternative, then forwards assistant messages to `env_client.step`. The `check_list` parameter passed by the experience-guided explorer is not consulted in the two worker execute bodies. It is not an enforced API denylist. [RT-RTE-environment-rollout](#rt-rte-environment-rollout) covers these alternate effect paths; [RT-CLM-rollout-control](#rt-clm-rollout-control) scopes control strength (SRC-1, `expansion/explorer.py`, `expansion/env_worker.py`, `expansion/env_explorer.py`).
4. **Expansion does not close the automatic task-execution cycle.** `run_pipeline` leaves `env_worker` unset even when given `env_url`. The epoch loop invokes `_expand` only when `self.expansion` is non-null, so a task manager alone does not activate that branch. `_expand` prefers a supplied task manager; otherwise it explores and synthesizes, but its original `ExperienceGuidedExplorer.summarize` calls `llm.chat`, which the shared `LLM` does not implement. Both task conversion methods produce empty histories and `reward=None`, with no intervening execution in `run`. Feeding a produced placeholder to the next reward comparison cannot establish successful training experience and can raise a type error. The task manager has another local limit: its stateful duplicate filter is applied to cumulative results repeatedly and finally again, so earlier admitted queries can be removed on a later pass. [RT-RTE-task-synthesis](#rt-rte-task-synthesis) is therefore a bounded generation route, not an established autonomous improvement cycle (SRC-1, `pipeline.py`, `expansion/explorer.py`, `expansion/task_manager.py`, `data/loaders.py`, `llm/client.py`).

These forcing cases inspect both ordinary and bypass paths before assigning guarantees. The capability surface includes host callbacks, environment Python execution, provider-native tool calls, direct model calls and local response evaluation. Current grants depend on the supplied callbacks, world/client object, credentials and Python-process authority. The frozen repository does not establish the deployed sandbox or network/filesystem grants. No global safety or isolation guarantee follows from the step limit or schema checks. No separate remote worker implementation, production shell policy or deployment configuration was established by these inspected paths; those are limits, not claims of system-wide absence.

### Added inspection coverage

Beyond the boundary's initial reads, this member inspected the full LLM invocation/retry body, full two-stage filter and filter implementations, full clustering and embedding clients, full merger and selector, plan extraction and rewriting signatures/bodies, response compression, core state conversion/update, inference formatters and the three wrapper preparation/stub paths. It also inspected real and simulated environment explorer bodies, original experience-guided exploration and summary, task-manager admission/checkpoint/trajectory conversion, and the explore/summarize bodies of random, experience-guided and real-environment strategies. These are SRC-1 implementation passages at the frozen revision, plus extraction prompt doctrine in `prompts/skill_prompts.py`; no new source or evidence layer is introduced. Full schema inventories, all benchmark-specific extraction adapters, every optional strategy formatter/parser, sample-library compatibility and bundled reward aggregates are not assessed here. Those available parts do not warrant negative findings or conclusions about actual benefit.

## Shared records

### Components

#### RT-CMP-llm
Label: LLM provider and callback models

Source-native identity: shared `LLM` wraps `ChatOpenAI`; exploration can instead use supplied `llm_chat_fn`, `chat` or `ainvoke` implementations. Representational form: distributed-parametric provider model, with symbolic client settings and natural-language message inputs kept distinct. Storage substrate: provider-held weights, not present in the checkout; client objects retain model name, URL, token limits and credentials in process (SRC-1, `llm/client.py`, `expansion/env_worker.py`, `expansion/env_explorer.py`).

Parameters changing during operation: no parameter-update operation in these inspected clients; provider-side changes and callback internals are uninspected. Exact version pinned: the default model string `gpt-4.1-2025-04-14` is a requested version label, not a frozen weight digest; caller overrides are accepted. Mutable endpoint resolving another model: possible through configured `base_url`, provider routing or substituted callbacks; resolution is external. Shared retained skills can change without any model-weight change.

> self.client = ChatOpenAI(
>     model=self.model,
>     api_key=self.api_key,
>     base_url=self.base_url if self.base_url else None,
> --- `llm/client.py`

The shared wrapper retries up to ten attempts by default, backs off rate errors and halves output-token allowance for recognized token errors. It does not trim input messages. Success resets the output allowance. Invocation `**kwargs` are accepted but not forwarded to the underlying `client.ainvoke` call. This is best-effort service recovery, not model compliance or delivery assurance; independently supplied callbacks bypass it. Implementation conclusion status: wired. Operation conclusion status: uninspected.

#### RT-CMP-embedding-service
Label: Qwen embedding backend and derived vectors

Source-native identity: clustering and inference each define an `EmbeddingService`, defaulting to `Qwen3-Embedding-8B` at localhost port 7000. Representational form: distributed-parametric embedding model and dense derived representations; symbolic HTTP and cosine-ranking code are separate consumers. Storage substrate: opaque server weights; NumPy arrays in process; inference also caches by exact text. Clustering posts to `/v1/embeddings`, inference to `/encode`; these are different external API contracts, not interchangeable by URL alone (SRC-1, `clustering/embedding.py`, `clustering/dbscan.py`, `inference/embedding_service.py`, `inference/retriever.py`).

Parameters changing during operation: inspected clients only request inference; backend training/update is uninspected. Exact model version pinned: no immutable revision or weights are pinned by the default name. Mutable endpoint resolving another model: possible; the service implementation is external. Corpus changes generate new vectors, not demonstrated weight learning.

> json={"model": self.model, "input": chunk},
> --- `clustering/embedding.py`

> json={"texts": texts, "model": self.model},
> --- `inference/embedding_service.py`

Clustering retries then raises on service failure; inference catches request failures and returns zero vectors of dimension 4096, which can be cached. At the retriever's positive threshold, all-zero cosine similarities do not qualify. This can silently suppress retrieved context; it does not establish an empty knowledge store (SRC-1, `inference/embedding_service.py`, `inference/retriever.py`). Implementation conclusion status: wired. Operation conclusion status: uninspected.

### Operative objects

none declared in this member

### Routes

#### RT-RTE-library-build
Label: Experience-to-library construction and admission

Endpoints and progression: caller-provided trajectory dictionaries enter `IterativeSkillPipeline.run`; reward selection, summarization, plan extraction, skill extraction, optional filters/clustering/merge, object conversion and `SkillLibrary.merge` produce library state, checkpoint files and final JSON. Owner: Python orchestrator controls stages and concurrency; models propose plans/skills/merged content and supply filter verdicts. Policy form: symbolic branch/threshold/merge rules plus natural-language prompts. State: per-epoch dictionaries, task-to-plan map, current library and copied histories (SRC-1, `pipeline.py`, `data/loaders.py`, `extraction/tool_summary.py`, `extraction/skill_extractor.py`, `core/skill.py`).

- Immediate return: In-memory library, epoch results, counts and statistics; `run_pipeline` additionally writes final files before returning.
- Later read-back: Epoch library influences expansion coverage, and saved unified libraries can enter the separate inference load route. Atomic/hybrid extraction reuses its instance proposal map, while functional steps reuse a list seeded from trajectory metadata; neither is an automatic read-back of committed epoch library state. `run` itself starts a fresh library rather than resuming a saved one; this does not reset the extractor instance's proposal map.
- Delegated visibility: Models receive only each stage's assembled messages; filter models see skill content and available schema text, not the full provenance or a guaranteed executable test.
- Selection predicate: Stored reward strictly greater than the caller threshold; default shortest history per task; plan-step parsing; add/modify collection; configurable filter timing; cosine DBSCAN clusters when enabled.
- Invalidation or expiry: Same-name library replacement and atomic redundancy suppression are code rules; no TTL. Checkpoints expose prior epoch snapshots but no automatic transactional restore is implemented in `run`.
- Activation or effect: Software updates library objects and writes JSON. Subsequent behavioral change from these instructions is unobserved.
- Evidence limits: Static wiring, not successful extraction or correct model judgments; direct library APIs and caller-disabled filtering are alternate admission paths. Pipeline preparation supplies atomic `item["skill_library"]`, but the actual atomic prompt consumer reads `self.existing_skills` instead. Downstream filtering/replacement does not synchronize that proposal map in the inspected pipeline and extractor bodies.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller starts/configures the workflow but is not a per-skill approver. Models propose add/modify/keep; collection and enabled filters can veto candidates; dictionary conversion can reject malformed entries; library merge decides insertion/replacement. Plans bypass skill filters. Guidance requests reusable, domain-specific skills, no imported packages, and exclusion of failed/debugging behavior. That text shapes proposals; accepted descriptions, content, tools and metadata persist, not a proof of correctness. Rollback requires caller use of an earlier saved file; in-place updates and file writes are not atomic transactions (SRC-1, `pipeline.py`, `core/skill.py`, `prompts/skill_prompts.py`).

Answer oracle: the input reward is an externally supplied outcome signal with unresolved original evaluator provenance, not a reference answer; quality/schema model judgment alone supplies no answer oracle. Operating mode: bounded offline extraction over a supplied corpus and epoch budget, optionally expanded between epochs. Trigger for change: selected successful experience and model proposals, not demonstrated regressions against an independent improvement objective.

> t for t in trajectories
> if t.get("reward", t.get("after_score", 0)) > threshold
> --- `data/loaders.py`

> - **modify**: revise an existing skill to make it more effective (e.g., improving documents). Only change `content` when necessary, and ensure the resulting skill remains broadly reusable/general-purpose.
> --- `prompts/skill_prompts.py`

> skill_library.merge(skill_objects, epoch=epoch)
> --- `pipeline.py`

The distinction between provisional context admission and final library admission is material: proposals can reach another extraction invocation before quality/schema vetoes. Rejected or subsequently merged library candidates need not be removed from that context. The atomic consumer selects by tool name from its map; concurrent item calls and instance reuse prevent interpreting this as an ordered committed epoch snapshot (SRC-1, `extraction/skill_extractor.py`, `pipeline.py`; [MEM-RTE-proposal-context](memory.md#mem-rte-proposal-context)).

> skill_library = []
> if tool in self.existing_skills:
>     skill_library.append(self.existing_skills[tool])
> --- `extraction/skill_extractor.py:331-335`

This record establishes an instruction-change admission mechanism, not a formulated-theory finding about every generated skill. The actual generated claim content and its criticism are not supplied for this invocation. It establishes neither learned benefit nor exercised self-improvement; later consumers and causal dependence would require additional evidence.

#### RT-RTE-prompt-prepare
Label: Library retrieval to benchmark prompt

Endpoints and owner: `create_skill_service`/`load_library` supplies a unified `SkillLibrary` to `SkillRetriever`; `prepare_prompt` accepts a task/base prompt and returns prompt text plus metadata. Code chooses the usage branch, vector search, optional selector and benchmark formatter. Context includes task, retrieved plan, selected skill descriptions/content and benchmark policy where retained by the formatter. Policy is symbolic ranking/limits plus model interpretation of rewrite and selection prompts (SRC-1, `inference/skill_usage.py`, `inference/retriever.py`, `inference/skill_selector.py`, `inference/prompt_formatters.py`).

- Immediate return: System-prompt string and metadata; wrappers also expose tools where applicable. No benchmark task execution is implemented by the wrappers.
- Later read-back: Saved experience-derived library is reloaded for later tasks; a caller may also request skills per execution step. Prompt rewriting itself is not saved back into the library by this service.
- Delegated visibility: Rewriter is intended to see task/reference plans; selector gets task, plan and truncated candidate descriptions; downstream model would receive formatted selected content, not all candidates or all metadata.
- Selection predicate: Mode gates vanilla/plan-only/skill-only/combined use; default plan top three at cosine threshold 0.45, first plan used; four candidates per parsed plan step or twice `max_skills` for task-only search; optional truthy tool set requires all listed tools; final maximum defaults to ten.
- Invalidation or expiry: Reload rebuilds indices; inference cache is keyed by text, not backend revision. No automatic expiry or endpoint-version invalidation. Each preparation makes a new prompt; it does not compact an existing agent history.
- Activation or effect: Library content is formatted into context where the selected formatter retains it. Delivery is wired, but behavioral use/compliance by a live task agent is unobserved.
- Evidence limits: Default rewrite-enabled skill-usage service with a rewriter has a required-argument mismatch; supplied shared LLM lacks selector's `generate`. BFCL/tau2 omit plan text, and benchmark execution methods are stubs. The separate public `PlanRewriteService.get_pseudo_plan` correctly forwards plural references and returns pseudo-plan/metadata to its caller, without persistence or shipped later delivery. That helper's model call receives task and formatted reference plans; selection uses configured top-k, and its per-request context ends on return. Its internal progression is wired, but no shipped caller was found by Python name search; use and output remain unobserved (SRC-1, `inference/plan_rewriter.py`).
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: code chooses ranks, thresholds and modes; an optional model chooses relevance names, with first-candidate fallback on exceptions. No human content approval occurs in this method. Answer oracle: none in inspected retrieval/selection; no expected task answer is compared. Operating mode: open caller task requests with bounded candidate delivery, not an improvement experiment. No retained-content admission occurs here; it reads rather than revises the library.

> if self.selector and len(raw_skills) > max_skills:
> --- `inference/skill_usage.py`

> response = await self.llm.generate(prompt)
> --- `inference/skill_selector.py`

> raise NotImplementedError("τ²-Bench execution requires environment integration")
> --- `inference/benchmarks/tau2bench.py`

#### RT-RTE-response-eval
Label: Provider-response Python evaluation

Endpoints: model response substrings enter `SkillMerger._extract_skill` or `SkillSelector._extract_skill_names`, then Python `eval`. Owner: local parser code chooses when; provider output determines the expression. Policy form: symbolic regex/JSON attempts followed by Python expression evaluation, not natural-language interpretation. Effect boundary: current Python process and its available builtins/globals; no restricted evaluation environment is passed in these calls (SRC-1, `clustering/merger.py`, `inference/skill_selector.py`).

- Immediate return: Parsed merge object or selected-name list if evaluation and subsequent type checks succeed; exceptions can be swallowed or retried.
- Later read-back: Successful merge values can be admitted through the library-build route; arbitrary evaluation effects are not a designed read-back protocol.
- Delegated visibility: Provider gets candidate skills or selection descriptions; no separate isolated parser worker receives the response.
- Selection predicate: Merger evaluates only after `<skill>` JSON decode failure; selector evaluates fenced Python or a bracketed-list expression when called. Normal valid JSON merging need not take the eval path.
- Invalidation or expiry: inapplicable — this is immediate expression evaluation, not an expiring retained object.
- Activation or effect: Code affords execution of response-controlled expressions before post-eval type checks. No exploit or actual side effect is observed.
- Evidence limits: The shared LLM's selector interface mismatch can prevent reaching selector evaluation; merger fallback remains independently reachable. Actual process permissions and malicious provider response are unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

This is not a declared product-code upgrade mechanism. It is a material alternate execution path whose effects are bounded by process authority, not by the library's tool metadata. There is no per-expression human approval in either inspected parser.

> result = eval(match.group(1).strip())
> --- `clustering/merger.py`

> names = eval(f"[{match.group(1)}]")
> --- `inference/skill_selector.py`

#### RT-RTE-environment-rollout
Label: Model-driven environment rollout variants

Endpoints: exploration guidance enters a worker/explorer, model actions go to callback/world/client execution, observations re-enter messages, and a trajectory/reward returns. Principal: caller-configured environment instance and model credentials; task/instance identity is explicit in the client-based explorer, but generic worker returns no task ID. Owner: code controls maximum steps and stopping; model determines action text or native tool calls. Context/state: local message list and task history, plus externally held world/instance state (SRC-1, `expansion/env_worker.py`, `expansion/env_explorer.py`, `expansion/explorer.py`).

- Immediate return: History, reward and completion fields, or partial history/error; real explorer records per-step actions/observations and releases an acquired instance in `finally`.
- Later read-back: Returned histories can feed exploration summarization and caller-supplied future extraction; the worker itself does not persist a skill library.
- Delegated visibility: A callback sees the whole assistant string; AppWorld sees extracted Python or full fallback text; client `step` receives the most recent assistant message, including `tool_calls` when present. Each task has a separate message frame; only the returned trajectory crosses back.
- Selection predicate: Model response chooses actions within caller-supplied capabilities; code stops at step budget, empty response/error, host done, or worker-specific completion signals.
- Invalidation or expiry: Per-call messages end with the invocation; real client instances are released best effort. World reset is a separate API and is not automatically invoked by each worker `execute` body.
- Activation or effect: Environment callbacks/world/client methods are called by the implementation; externally meaningful state changes and correct completion are unobserved here.
- Evidence limits: Host tool implementations, actual grants and isolation are external; generic completion substrings and AppWorld evaluation are unequal result standards. Merely storing tokenizer/max-model-length fields does not enforce trimming in the generic execute loop.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: model proposes actions; code enforces local stopping; external executor may reject an action under its own contract. No human per-action approval is implemented in the inspected bodies. Answer oracle: generic worker has only a textual completion heuristic; AppWorld supplies external evaluator pass/failure counts; real client supplies done/reward or `evaluate`. Evaluator internals/reference outcomes are uninspected. Operating mode: bounded exploration rollouts, not complete shipped inference wrappers. Recovery returns partial results, logs errors and releases real instances; no local undo of environment effects is established.

> observation = self.env_step_fn(assistant_content)
> --- `expansion/env_worker.py`

> output = self.world.execute(code)
> --- `expansion/env_worker.py`

> response = await self.llm.chat(messages, tools=self.tools)
> --- `expansion/env_explorer.py`

> if "complete_task" in assistant_content.lower():
>     completed = True
>     reward = 1.0
>     break
> --- `expansion/env_worker.py`

#### RT-RTE-task-synthesis
Label: Exploration to synthetic-task admission

Endpoints: seeds/experience enter exploration strategies; model-generated or real histories enter summarization; proposed task dictionaries enter post-filters, optional checkpoint files and trajectory conversion. Owner: original explorer and task-manager APIs are distinct; the manager orchestrates a strategy's `explore(seed_task)` and `summarize(seed_task, trajectory)`, whereas the pipeline's original expansion API takes current library/worker/experience (SRC-1, `pipeline.py`, `expansion/explorer.py`, `expansion/task_manager.py`, `expansion/strategies/random.py`, `expansion/strategies/experience_guided.py`, `expansion/strategies/real_env.py`).

- Immediate return: Proposed task objectives or empty/partial lists; conversion returns placeholder trajectories, not evaluated solutions.
- Later read-back: Task-manager checkpoint reload restores results and processed batch indices when the seed-task hash matches. Converted tasks can be appended to the pipeline pool, but no execution step fills their histories/rewards there.
- Delegated visibility: Each strategy gets a seed task and configured tools/guidance; summarizers receive trajectory text. Random/experience-guided simulated strategies ask a model for actions and observations; real strategies call a real explorer instead.
- Selection predicate: Caller strategy and rollout/thread budgets; model parses task proposals; default manager duplicate normalization is lowercase/strip and confidence threshold is 0.3. Experience guidance prioritizes uncovered/risky APIs or discourages already covered ones.
- Invalidation or expiry: Seed hash mismatch discards a task checkpoint; hash covers task IDs/user-task text, not every strategy/provider setting. Duplicate tracker is mutable across filter calls and can remove prior results on repeated cumulative filtering.
- Activation or effect: Task proposals and checkpoint state are produced by code; automatic later successful extraction from placeholders is not established and has explicit integration breaks.
- Evidence limits: Synthetic observations are model predictions, not execution evidence. Original explorer assumes `chat`; task-manager-only pipeline configuration is not enough to trigger expansion; placeholder rewards are not numeric outcomes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/change account: caller configures seeds, strategy and budgets, not individual objectives; model proposes objectives; software parsing, duplicate/confidence filters and optional custom post-filters can reject. Original experience guidance derives explore/avoid sets from successes, failures and current skill coverage. Task-manager simulated guidance asks for exploration and user-centered tasks, while real strategies summarize environment traces. What persists is tasks and checkpoint progress, not a validated capability or product revision. Recovery uses checkpoint load or fresh generation on mismatch; no demonstrated benchmark feedback comparison validates the new tasks. Answer oracle: none for simulated observations/task confidence; real explorer can supply external reward, but converting an objective resets reward to `None`. Operating mode: bounded seed-based generation, with simulated and real alternatives rather than an open-ended proven self-improvement loop.

> "task_history": [],  # To be filled by agent execution
> "reward": None,  # Not yet evaluated
> --- `expansion/task_manager.py`

> results = self._apply_filters(results)
> 
> self.generated_tasks = results
> --- `expansion/task_manager.py`

### Claims

#### RT-CLM-quality-control
Label: Two-stage quality-control coverage

Claimed operation: the pipeline describes general quality filtering followed by tool-schema validation. Source: SRC-1, `filtering/pipeline.py`, `filtering/base.py`. Owner: filter pipeline, with provider judgment; enforcement points: candidate partition, schema preparation, Boolean verdict collection. Guarantee strength: best effort. Required external contract: available schemas must describe actual tools and model answers must reliably express the requested verdict. The implementation does not establish either contract.

Covered paths: candidates actually sent through enabled stages. Alternate paths: atomic general-stage bypass; no-schema whole-batch return; explicitly skipped stages/filter timing; plans admitted earlier; default post-filter merges; direct `SkillLibrary.add_*`/`merge`. Verdict matching accepts substrings, including strings containing those substrings in a negative formulation. Therefore the code enforces its Boolean tests, not semantic correctness of tools or absence of imports.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not valid_skills:
>     logger.warning("No skills have valid tool schemas for Stage 2")
>     return current_skills  # Return Stage 1 results
> --- `filtering/pipeline.py`

> return "good" in response.lower()
> --- `filtering/base.py`

> return "correct" in answer_part
> --- `filtering/base.py`

#### RT-CLM-rollout-control
Label: Bounded steps and advisory API avoidance

Claimed operation: experience-guided exploration discourages previously explored APIs and runs a bounded rollout. Owner: explorer constructs guidance; worker owns iteration. Enforcement point: `range(max_steps)` covers local worker/client-model steps, not nested callback work or Python-expression execution. Guarantee strength: policy for API avoidance; local symbolic step bound is an invariant only over these loop iterations, not time, tokens or external effects. Required external contract: callbacks and environment operations terminate and enforce their own permissions. Timeout fields alone do not establish enforcement in callbacks (SRC-1, `expansion/explorer.py`, `expansion/env_worker.py`, `expansion/env_explorer.py`).

Covered paths: inspected local loops with a positive caller step budget. Alternate paths: generic/AppWorld callbacks, client/native tools, callable worker extensions and local parser evaluation. The checklist is delivered but not tested in the two concrete worker loops; API avoidance is prompt guidance, not a denylist. Deployment guarantee: uninspected; no actual grant/isolation envelope was supplied.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> check_list=list(apis_to_avoid) if apis_to_avoid else None
> --- `expansion/explorer.py`

> for step in range(max_steps):
>     try:
>         response = self.llm_chat_fn(
>             messages=messages,
>             custom_sampling_params={"temperature": temperature}
>         )
>
>         if response is None or response.get("content", "") == "":
>             if self.verbose:
>                 logger.warning(f"Empty LLM response at step {step}")
>             break
> --- `expansion/env_worker.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-guidance
Label: Retained skills as later model guidance

Consumer: a downstream task model selected by the caller; immediate consumers are retrieval/formatting code and optional rewrite/selection models. Channel: selected descriptions, examples and implementation text in a returned system prompt, not installed callable functions. Force: advisory natural-language/model interpretation, despite code-like content; symbolic retrieval rules decide inclusion, not downstream compliance. Horizon: saved library can cross tasks and process sessions; each returned prompt supplies current-call context. Evidence: SRC-1, `inference/skill_usage.py`, `inference/prompt_formatters.py`, `core/skill.py`.

> 1. The Skill Library provides reference implementations, not callable functions.
> 2. Always verify API documentation before using skills.
> --- `inference/prompt_formatters.py`

The formatter instruction requests checking actual API specifications; it does not prove such checks occur. Delivered library text is capable of shaping future decisions, but the wrapper stubs and missing invocation traces prevent claims of exercised authority or benefit. This path is distinct from local response `eval` and external environment execution.

## Annotations

none

---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "ACE runtime baseline: sequential and batched playbook adaptation, evaluation, reload and optional merging at the frozen main-repository revision."
run-id: AAS-2026-10-18-ace-007571102a54-01
reviewed-boundary: "82709de050e1db6e6ef2f07bcb0393560b94992a"
---

# ACE runtime report

## Runtime account

### Scope and consequential work

ACE's inspected work is answer generation with a text playbook and model-mediated adaptation of that playbook. Python owns progression; the generator, reflector and curator are separate model-call roles, not independently scheduling workers. The target includes its shipped Finance and two Mind2Web callers. AppWorld implementation is unavailable under the [boundary](boundary.md#boundary-and-evidence); this report does not generalize the main-repository loop to that missing integration.

All source findings below use SRC-1 at the reviewed commit. Evidence is inspected implementation or explicitly labelled doctrine/design. No ACE execution, provider request, trace or experiment was supplied or performed. Implementation wiring does not establish activation, reliable compliance, benefit, realized cost or benchmark performance.

Additional inspection beyond the boundary's initial coverage includes the single-sample sequential loop and offline/online drivers in `ace/ace.py`; batch configuration, run dispatch, all three batch phases and offline/online drivers in `ace/ace_batch.py`; generator, reflector, curator proposal/reducer/validation and analyzer implementations in `ace/core/`; generator, reflector and curator prompts in `ace/prompts/`; answer extraction, provider initialization and evaluation in `utils.py`; counter updates, operation application and bullet selection in `playbook_utils.py`; call/error handling in `llm.py`; selected logging functions in `logger.py`; all three caller main paths and the scoring/standardization portions of their `data_processor.py` files. These add implementation and doctrine/design coverage, not an observed-run layer. Dataset contents, preparation algorithms and provider internals were not evaluated; dataset provenance, completeness of benchmark construction and deployed isolation remain unestablished.

### Ordinary shipped invocation

Take the Finance caller in offline mode, batch size one, a nonempty validation set and ordinary positive scheduling intervals. The operator supplies task, save directory, model/provider choices, data configuration and optionally an initial-playbook path. The caller loads and standardizes samples, loads initial text, selects `ACE` rather than `ACEBatch`, constructs three clients, and calls `run`. The same selector is present in both Mind2Web callers (SRC-1, `eval/finance/run.py`, `eval/mind2web/run.py`, `eval/mind2web2/run.py`).

> AceCls = ACEBatch if args.batch_size > 1 else ACE
> --- `eval/finance/run.py`

The orchestrator checks mode and presence of the required sample lists, creates timestamped output directories and saves configuration. Offline mode optionally evaluates test samples before training, then iterates epochs and samples through [RT-RTE-sample-adaptation](#rt-rte-sample-adaptation). A generator call receives the full current playbook, question, context and current reflection as one formatted user message. Its response is text; code extracts the final answer and model-reported bullet IDs. The processor compares the answer with the sample target. Incorrect results trigger up to `max_num_rounds` reflector/regenerator rounds, stopping on processor correctness; correct initial results still get one reflection. Reflector tags update counters. At scheduled steps the curator proposes additions, code applies them, and an enabled analyzer can further rewrite the result. A final generator invocation uses the resulting playbook with an empty reflection. The method returns pre/post answers and tracking data, not a proposed tool action (SRC-1, `ace/ace.py`, `ace/core/generator.py`, `utils.py`).

> prompt = GENERATOR_PROMPT.format(playbook, reflection, question, context)
> --- `ace/core/generator.py`

Offline validation periodically scores the current playbook; a strict improvement over the tracked accuracy selects `best_playbook`. Training continues from the current playbook, not from the best snapshot. The initial playbook remains best if no later snapshot beats the initial tracking threshold of zero, including when no scheduled validation happens. Final and best text files are saved separately. The optional final test uses the best snapshot; consolidated results go to JSON and `run` returns a results dictionary. Selection is [RT-RTE-evaluate-select](#rt-rte-evaluate-select); persistence and explicit cross-run loading are [RT-RTE-playbook-reload](#rt-rte-playbook-reload) (SRC-1, `ace/ace.py`).

> if acc > best_accuracy:
>     best_accuracy = acc
>     self.best_playbook = self.playbook
> --- `ace/ace.py`

### Alternate modes, frames and coordination

`eval_only` runs the generator/scorer path without reflection or curator updates. The public `test` wrapper temporarily replaces `self.playbook`, calls this mode, then restores it on normal return; restoration is not protected by `finally`. Online mode first evaluates the initial playbook on the test split, then tests each window before training on that same window, with one epoch required. Later windows consume the updated playbook. This is a bounded dataset curriculum with labelled targets, not an open-ended environment loop ([RT-RTE-online-windows](#rt-rte-online-windows); SRC-1, `ace/ace.py`, `ace/ace_batch.py`). Both Mind2Web callers can omit offline test samples through `skip_initial_test`; because dispatch tests the presence of those samples at both ends, this omits both initial and final testing. Their answers are scored action descriptions, not browser execution (SRC-1, `eval/mind2web/run.py`, `eval/mind2web2/run.py`, `eval/mind2web/data_processor.py`, `eval/mind2web2/data_processor.py`).

Batch size greater than one selects a different admission route, [RT-RTE-batch-adaptation](#rt-rte-batch-adaptation). A thread per sample works against a shared string snapshot and a local copy. Only results, tags and reflections cross back. Code aggregates these, optionally duplicates and shuffles reflection records, divides them into groups, calls independent curator proposers against the same base, sorts completed proposals by group ID, calls a reducer, and applies its final additions once. Post-curator generation is parallel again. Batch-local frames keep other samples' live reasoning out of each initial generator/reflector context; group concatenation explicitly brings selected results back. There is no persistent provider conversation in `timed_llm_call`: each request sends one user message. This resembles pushing selected values into a frame and returning results, not preserving pointers into a shared model context. The playbook remains outside those frames and is copied in on later calls (SRC-1, `ace/ace_batch.py`, `llm.py`).

The generator gets the whole playbook, while the reflector gets only parsable lines matching generator-reported IDs. No IDs or no matching lines yield explanatory placeholder text. Curator sees the full current playbook, reflection and question context; the batch reducer sees proposal groups, not the original complete per-sample traces. These are material transformations: bullet reporting is not proof of actual use, and aggregation is not complete trace delivery (SRC-1, `ace/core/generator.py`, `playbook_utils.py`, `ace/core/reflector.py`, `ace/core/curator.py`, `ace/ace_batch.py`).

### Controls and forcing cases

1. **Ground-truth withholding is local to prompt construction.** `no_ground_truth` withholds the literal target from reflector input and selects the no-ground-truth curator prompt. It does not remove the answer oracle: sequential and batched code still compare against the target, select the correct/incorrect branch, provide a matching/nonmatching feedback string and stop regeneration on target correctness. The CLI describes withholding ground truth *in reflection*, not removing all supervision. Supported caller configuration reaches these branches. A claim of fully label-free operation for these drivers would be false (SRC-1, `ace/ace.py`, `ace/ace_batch.py`, `ace/core/reflector.py`, `eval/finance/run.py`).

> ground_truth=target if not no_ground_truth else None,
> environment_feedback="Predicted answer does not match ground truth",
> --- `ace/ace.py`

2. **ADD-only operation application is not a system-wide immutability guarantee.** The deterministic operation consumer implements additions and preserves existing lines; sequential validation accepts several other operation names without implementing them, while proposal/reducer paths explicitly filter to ADD. Yet enabled analyzer merging replaces a group with one line and removes other members, including when its merge call fails and it falls back to the first bullet. Initial-playbook loading also replaces the initial state without curator validation. Thus ADD-only describes a particular consumer, not every playbook mutation ([RT-RTE-bulletpoint-merge](#rt-rte-bulletpoint-merge), [RT-RTE-playbook-reload](#rt-rte-playbook-reload); SRC-1, `playbook_utils.py`, `ace/core/curator.py`, `ace/core/bulletpoint_analyzer.py`).

3. **Evaluation is not necessarily a passive text boundary.** The FINER processor evaluates comma-delimited target and prediction fragments with Python `eval`. A prediction fragment reaches `eval` if the preceding target evaluation succeeds; a target-evaluation exception skips prediction evaluation within that `try`. JSON `final_answer` extraction and fallback text extraction do not constrain fragments to numeric literals. The supported FINER caller routes outputs to this consumer, so available source establishes a host-interpreter path, not merely a hypothetical tool API ([RT-RTE-finer-scoring](#rt-rte-finer-scoring); SRC-1, `eval/finance/data_processor.py`, `utils.py`). No exploit was executed and no deployed containment was inspected.

4. **Error rollback is narrower and weaker than its comments suggest.** The batch code intends to exclude phase-one API failures and roll back phase-two playbook/ID changes after phase-three API errors. However, both exception handlers call `is_api_error`, and a bounded search in the batch module and its wildcard-imported project modules found no definition. On an exception reaching either handler in the inspected source, the unresolved name can prevent the intended recovery before even testing `continue_on_llm_error`. Also the transport returns an empty-response sentinel as ordinary text for `train_`/`test_` call IDs, whereas online IDs begin `online_train`; empty online responses can raise instead. A returned sentinel is not the batch's distinct `INCORRECT_DUE_TO_API_ERROR` marker and does not pass through exception-driven exclusion. These branches prevent a universal claim that failed model work never contributes to updates (SRC-1, `ace/ace_batch.py`, `llm.py`).

### Guarantee ownership and effect envelope

| Scoped guarantee | Owner and enforcement | Strength and coverage | Required external contract / alternate path | Conclusion statuses |
|---|---|---|---|---|
| Only supported modes and required list presence enter `run` | Python guards in both orchestrators | invariant at `run`; not a validity check of each sample or interval | Direct component calls bypass dispatch; valid processor/config still required | implementation conclusion status: wired; operation conclusion status: uninspected |
| Curator output has outer structure before application | Curator parser checks reasoning string, operations list, operation dictionaries and ADD required keys | invariant for accepted parser output, not semantic correctness or fully typed ADD values | Direct utility calls bypass it; analyzer uses another parser; model must supply useful content | implementation conclusion status: wired; operation conclusion status: uninspected |
| ADD-only deterministic operation effect | `apply_curator_operations` adds and rebuilds lines; batch filters unsupported names | invariant for this consumer's supported operations, not whole-system preservation | Analyzer can merge/remove; initial input can replace state | implementation conclusion status: wired; operation conclusion status: uninspected |
| Playbook token budget | Operator value is interpolated into curator prompts | policy; not a hard size bound in inspected application/reconstruction code | Requires model compliance; full playbook is still delivered to generator, analyzer can rewrite it | implementation conclusion status: wired; operation conclusion status: uninspected |
| JSON output request | `timed_llm_call` optionally requests provider `json_object`; separate local extraction/validation follows | best effort for useful structured output; not a universal schema guarantee | Provider support required; analyzer direct call does not use this transport or JSON option | implementation conclusion status: wired; operation conclusion status: uninspected |
| Recovery from model errors | Transport retries selected errors; curator can keep prior text; batch contains rollback code | best effort, with batch unresolved-name and sentinel qualifications above | Provider response/usage fields, logger and filesystem must work; not all failures are retried | implementation conclusion status: wired; operation conclusion status: uninspected |

These conclusions follow the cited routes and forcing-case passages, not the class docstrings. In particular, curator ADD validation checks key presence, not the type of content or section. A malformed section can fail later; curation catches failures and returns prior text where its failure logging also succeeds. No quality-score veto governs each sequential addition (SRC-1, `ace/core/curator.py`, `playbook_utils.py`).

The capability surface includes outbound chat requests, local text/JSON writes, supplied Python processor callbacks and optional embeddings/merge calls. The present grant set is caller-selected clients, environment API keys, output paths, processor and initial content; role names confer no separate OS authority. `initialize_clients` builds three clients to the selected provider using one provider key. No deployed sandbox, human approval UI or principal isolation was supplied. The inspected transport supplies no tools to the model, but the FINER scoring path means absence of model tool definitions does not establish absence of host effects. AppWorld, external provider behavior and arbitrary caller callback implementations remain outside the established effect envelope (SRC-1, `utils.py`, `llm.py`, `eval/finance/data_processor.py`).

The optional merge call directly uses `client.chat.completions.create`, temperature 0.3 and `max_tokens`; it bypasses `timed_llm_call` retries, logging, provider-specific token-key selection and JSON mode. Normal role calls use temperature zero, provider-dependent completion-token keys, selected transient-error retries (default limit 1000), and detailed prompt/response/usage logging. Remaining errors raise. Logging retains evidence but does not itself feed a later curator in the inspected loop; the curator receives the current reflection directly (SRC-1, `ace/core/bulletpoint_analyzer.py`, `llm.py`, `logger.py`, `ace/ace.py`, `ace/ace_batch.py`).

## Shared records

### Components

#### RT-CMP-generator
Label: Generator model role

Source-native identity: `Generator.model` and its configured provider client. Representational form: distributed-parametric remote language model; Python stores a model-name string and client, not weights. Generator prompt text is natural language and output parsing is symbolic. Parameters are not updated by inspected ACE code; provider internals are uninspected. Exact weight version is not pinned by the caller's free model string (Finance defaults to `DeepSeek-V3.1`); a provider endpoint/name can resolve differently outside ACE's control. This is a mutability possibility, not observed replacement. SRC-1, `ace/core/generator.py`, `eval/finance/run.py`, `llm.py`.

> self.model = model
> self.max_tokens = max_tokens
> --- `ace/core/generator.py`

#### RT-CMP-reflector
Label: Reflector model role

Source-native identity: `Reflector.model` and its separately instantiated provider client. Representational form: distributed-parametric remote model; substrate is external provider weights, with a Python string/client handle locally. No local parameter-update operation occurs in the inspected role; provider training/state is uninspected. Exact model version is not enforced; its configurable endpoint/name can resolve to changed weights. It is distinct from the generator role even if configured with the same model name. SRC-1, `ace/core/reflector.py`, `utils.py`.

> self.api_client = api_client
> self.api_provider = api_provider
> self.model = model
> --- `ace/core/reflector.py`

#### RT-CMP-curator
Label: Curator model role

Source-native identity: `Curator.model` and its provider client, used for single curation, grouped proposals and reduction. Optional analyzer merge requests reuse the curator client/model configuration, but bypass its transport wrapper. Representational form: distributed-parametric remote model, externally stored parameters; local model string/client and symbolic operation parser. ACE changes playbook text rather than these parameters. No exact immutable weight version is enforced, and endpoint resolution can change externally; internals and actual changes are uninspected. SRC-1, `ace/core/curator.py`, `ace/ace.py`, `ace/core/bulletpoint_analyzer.py`.

> self.curator = Curator(curator_client, api_provider, curator_model, max_tokens)
> --- `ace/ace.py`

#### RT-CMP-embedding-model
Label: Analyzer embedding model

Source-native identity: analyzer `embedding_model`, lazily loaded by name, default `all-mpnet-base-v2`. Representational form: distributed-parametric sentence-transformer weights and dense embeddings; weights live in the external package/model loading substrate and runtime object, embeddings in NumPy arrays. Inspected code calls `encode`, normalizes vectors and computes pairwise dot products; it does not train weights. No revision/hash is pinned in the loading call, so name-based loading may resolve another model artifact; no replacement or training was observed. SRC-1, `ace/core/bulletpoint_analyzer.py`.

> self.embedding_model = SentenceTransformer(self.embedding_model_name)
> --- `ace/core/bulletpoint_analyzer.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-sample-adaptation
Label: Sequential sample adaptation

Endpoints and owner: orchestrator `_train_single_sample` sends task/playbook to generator, prediction/target-derived feedback and selected bullets to reflector, and reflection/playbook/context to curator; Python applies operations to `self.playbook`. Trigger is each training sample. Python decides correctness branches, round limit, stopping and curator frequency; models propose reasoning, tags and additions. Representations are natural-language task/trace/reflection/bullet content plus symbolic IDs, counters, JSON operations and schedule. No per-content human veto is wired. The task processor supplies the answer oracle from dataset targets; model opinion is not the correctness test. Operating mode is offline training or online-window adaptation, not an unbounded user request (SRC-1, `ace/ace.py`, `ace/core/reflector.py`, `ace/core/curator.py`, `playbook_utils.py`).

- Immediate return: Pre-train answer, post-curator answer and tracking dictionary; model calls return response strings and metadata.
- Later read-back: Updated playbook enters regeneration, post-curator generation, later samples and scheduled evaluation; file reload is a separate route.
- Delegated visibility: Generator gets full playbook/context/reflection; reflector gets full response trace and only matching reported bullets; curator gets current playbook, last reflection and question context, not all prior rounds.
- Selection predicate: Processor correctness selects retry versus correct-answer reflection; round limit bounds retries; step modulo curator frequency admits curation; IDs select reflector bullets.
- Invalidation or expiry: Reflection is replaced by the next round and reset to empty for post-curator generation; no automatic playbook expiry is established here.
- Activation or effect: Counters and ADD content are wired into subsequent prompts; actual model dependence or improved answers is unobserved.
- Evidence limits: No sample execution or actual generated insight supplied; zero rounds can leave an incorrect sample with empty reflection, and no-ground-truth mode still uses the target oracle.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/rejection/recovery: curator can return an empty operation list; structure errors and empty sentinels can preserve the current playbook. Parser admission is not an accuracy gate. Existing counters can change before curation; failed additions do not rewind those earlier changes. Optional analyzer admission is independent. Guidance requests new, concise, nonredundant strategies rather than whole-playbook regeneration. Persisting content is bullet text/counters; curator reasoning is in call logs, not automatically reconstructed into the next curator input (SRC-1, `ace/prompts/curator.py`, `ace/ace.py`, `logger.py`).

> - Identify ONLY the NEW insights, strategies, or mistakes that are MISSING from the current playbook
> --- `ace/prompts/curator.py:10-21`

> if step % curator_frequency == 0:
> --- `ace/ace.py`

Theory assessment boundary: the prompt requests diagnosis and reusable principles, but no actual formulated theory instance was supplied. Theory-builder conditions 1–4 are separately limited: (1) operation conclusion status: uninspected — no generated whole explanatory unit inspected; (2) operation conclusion status: uninspected — prompt delivery does not establish content-dependent decisions; (3) operation conclusion status: uninspected — requested diagnosis does not establish claim/result/blame-directed criticism; (4) implementation conclusion status: wired — reflection and updates can reach another round, while iteration of an actual criticized theory is unobserved. Addressability is afforded through individual bullets/IDs, not proof that assumptions and scope are individually exposed. Persistence is wired across samples and explicit reload. Learning and successful improvement are unestablished without capacity/outcome evidence. Reflection has an implemented channel from a representation of prior reasoning to later generation, but actual bidirectional behavior dependence is unobserved. Computation performs the internal proposal, decision and application roles in this bounded driver; this does not establish an autonomous or reflective theory builder. A dispositional improvement-directed self-change pathway is wired through retained context and [RT-BAP-playbook-guidance](#rt-bap-playbook-guidance), with accuracy as an independently specified objective; exercised self-improvement lacks subsequent operation causally depending on the change. These are independent limits, not a bundled negative conclusion.

#### RT-RTE-batch-adaptation
Label: Batch proposals and reduction

Endpoints/progression: `_train_batch` fans out generator/reflector work on a snapshot, joins results, updates shared counters, optionally duplicates/shuffles reflection records, groups them, concurrently proposes additions, reduces nonempty proposal groups, applies once, optionally analyzes, and fans out post-curator generation. Python owns scheduling/state/IDs; curator models propose and reduce. Group count defaults to floor square root of original reflection count, clamped to available records. Batch curation runs per batch rather than using the sequential modulo gate; extracted `curator_frequency` is not consulted in `_train_batch`. Dataset target checks remain the answer oracle; no per-update human approval is wired. SRC-1, `ace/ace_batch.py`, `ace/core/curator.py`.

- Immediate return: Ordered pre/post answer and tracking tuples for batch samples; proposal calls return operation groups rather than installing them.
- Later read-back: Applied result goes to phase-three generation and later batches, validation or online windows.
- Delegated visibility: Per-sample frames receive the snapshot/local counters, not other samples' traces; groups receive combined last reflections and contexts; reducer receives base playbook and proposed operations.
- Selection predicate: Non-marker results enter reflection aggregation; only ADD operations survive proposer/reducer filtering; no proposals skips reducer application.
- Invalidation or expiry: Per-sample reasoning frames end at return; proposal groups are batch-local. Intended phase-three API-error rollback restores pre-phase-two text and next ID, subject to the unresolved handler described below.
- Activation or effect: Code serializes admission to shared state after joins; model use of installed content and gains remain unobserved.
- Evidence limits: No concurrent run supplied; retry and rollback claims are limited by unresolved `is_api_error`, sentinel returns and direct analyzer transport.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission and recovery: proposals can be empty or parser-rejected, reducer can discard proposals, then deterministic ADD application admits its result without an accuracy veto. Instructions request dropping redundant/low-value proposals; this is model policy, not a fixed semantic check. Phase-three rollback cannot undo already returned answers, outbound calls or logs. Its intended exception path is not established as executable recovery because `is_api_error` is not defined by the inspected module/import roots (bounded search: exact identifier in `ace/ace_batch.py`, `utils.py`, `logger.py`, `playbook_utils.py` at the reviewed revision). Even `continue_on_llm_error=True` is after that unresolved call. SRC-1, `ace/ace_batch.py`.

> if is_api_error(e) or config_params.get('continue_on_llm_error', False):
> --- `ace/ace_batch.py:693-693`

> operations = self._add_operations_only(operations_info["operations"], call_id)
> --- `ace/core/curator.py:289-304`

Guidance persists as selected ADD content, not necessarily reducer reasoning. Theory-builder/learning/activation limits are the same as the sequential route, with an additional transformation from reflections to proposals to reducer output; no actual theory or criticism instance was supplied for this route.

#### RT-RTE-evaluate-select
Label: Evaluation and best selection

Endpoints/owner: `_run_test` or periodic offline validation invokes `evaluate_test_set`; worker threads call generator with a fixed supplied playbook, extract answers and invoke the processor. The main thread aggregates successful results and periodic offline code selects `best_playbook` on strictly greater validation accuracy. The processor owns task-specific oracle semantics: FINER per-field matching, formula numeric/string matching, Mind2Web element/operation/value matching. Humans provide datasets and configuration, not per-snapshot approval. Mode is bounded evaluation/validation, with accuracy triggering snapshot selection, not rollback of the current training playbook. SRC-1, `ace/ace.py`, `ace/ace_batch.py`, `utils.py`, `eval/finance/data_processor.py`, `eval/mind2web/data_processor.py`, `eval/mind2web2/data_processor.py`.

- Immediate return: Accuracy/correct/total/no-answer metrics and wrong-answer records; run saves result JSON.
- Later read-back: Selected best text is consumed by final offline testing and may be explicitly reloaded in another run; evaluation metrics are not a curator input here.
- Delegated visibility: Evaluation threads get question/context, shared playbook string and empty reflection; target is used by host scorer, not directly passed to generator by this routine.
- Selection predicate: All supplied samples are scheduled; only successful evaluation results enter aggregate answers/targets; strict validation improvement selects best snapshot.
- Invalidation or expiry: Snapshot stays until a later strict improvement; temporary `test` wrapper restores previous state only on normal return.
- Activation or effect: Selection changes which playbook final testing receives, not the training playbook; realized behavioral differences are unobserved.
- Evidence limits: Exceptions are skipped rather than invariably counted incorrect. All-failed evaluation can reference unassigned `final_results`; metrics do not guarantee full input coverage or benchmark validity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if error:
>     print(error)
>     continue
> --- `utils.py`

The all-failed branch assigns `results` rather than `final_results`, which the final return uses. Mind2Web callers catch `UnboundLocalError` around `run` and print zero results, but this does not complete interrupted persistence or establish successful evaluation (SRC-1, `utils.py`, `eval/mind2web/run.py`, `eval/mind2web2/run.py`).

#### RT-RTE-online-windows
Label: Online test then train

Endpoints/owner: online dispatch performs initial whole-test evaluation, then `_online_train_and_test` partitions test samples into windows, evaluates each window with the current playbook, trains on its samples sequentially or in batches, and saves window/final text. Python owns next steps and carries state between windows. Trigger is online mode; only one epoch is accepted. The oracle is the dataset target/processor, including with `no_ground_truth`; no per-content human veto is wired. SRC-1, `ace/ace.py`, `ace/ace_batch.py`.

- Immediate return: Cumulative pre-window-training accuracy, correct and total counts; files also retain window/training metrics.
- Later read-back: One window's adapted playbook enters later windows and can be reloaded across runs.
- Delegated visibility: Evaluation workers receive current playbook; adaptation frames receive their sample and current/snapshot playbook, with selected reflection records crossing to batch curation.
- Selection predicate: Fixed contiguous window slicing; configured batch size chooses adaptation granularity; target correctness controls within-sample rounds.
- Invalidation or expiry: One-epoch restriction prevents multi-epoch online iteration; no automatic age expiry for retained bullets is wired here.
- Activation or effect: Updates are delivered to later-window generation; observed effects and comparative benefit are unestablished.
- Evidence limits: This is test-then-train on a labelled split, not an independently inspected live environment. Skipped evaluation failures can violate the final total-count assertion; no run evidence supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if num_epochs != 1:
>     raise ValueError(f"online_train_and_test requires num_epochs=1, got {num_epochs}")
> --- `ace/ace.py`

Admission/proposal/rejection/recovery are the sequential or batch route already cited; this route adds window ordering, not a new content gate. Saved final text is current adapted text, not a newly selected best-validation product (SRC-1, `ace/ace.py`, `ace/ace_batch.py`).

#### RT-RTE-playbook-reload
Label: File persistence and reload

Endpoints/owner: offline/online orchestrators write plain-text playbook snapshots; shipped callers' `load_initial_playbook` reads an operator-selected existing path, passes its entire text to the constructor, and later generator calls format it into prompts. Trigger is periodic/end-of-run saving or a new invocation naming an initial file. Filesystem I/O is computational; explicit initial content/path selection belongs to the caller, potentially a human, with authorship otherwise unresolved. No content-specific human approval is required by software. SRC-1, `ace/ace.py`, `ace/ace_batch.py`, `eval/finance/run.py`, `eval/mind2web/run.py`, `eval/mind2web2/run.py`, `ace/core/generator.py`.

- Immediate return: Written snapshot files; loader returns text or None; constructor retains truthy text or initializes standard empty sections.
- Later read-back: Explicit operator/caller path selection reintroduces saved content into a subsequent run and generator prompt; no automatic newest-file discovery is established.
- Delegated visibility: Full loaded text is visible to downstream generator/curator inputs; no provenance or trust header is enforced by the loader.
- Selection predicate: Supplied path exists, then entire file read; constructor truthiness chooses loaded versus empty text.
- Invalidation or expiry: Caller can replace/edit the input file or choose another snapshot; no automatic expiry, version migration or resume transaction is established by this path.
- Activation or effect: Loaded content becomes runtime playbook and is delivered to models; actual behavioral dependence is unobserved.
- Evidence limits: Text persistence is not complete orchestration-state recovery. Constructors set next_global_id to 1 even with initial text, so reload does not itself restore identifier allocation history.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if initial_playbook:
>     self.playbook = initial_playbook
> else:
>     self.playbook = self._initialize_empty_playbook()
> --- `ace/ace.py`

Admission accepts arbitrary truthy file text at this boundary; it does not run curator validation or check that the file was generated by ACE. Caller replacement provides coarse recovery, but no guarantee of replaying counters, best selection, step or ID state. Guidance persists as bullet text/counters, not weights; loaded content may or may not express any theory (SRC-1, `ace/ace.py`, `ace/ace_batch.py`, `eval/finance/run.py`).

#### RT-RTE-bulletpoint-merge
Label: Optional analyzer merge

Endpoints/owner: enabled orchestrator calls `BulletpointAnalyzer.analyze` after curation. Code parses bullets, embeds their content, finds threshold-similar groups and optionally calls the model to merge each group; it reconstructs text with merged first lines and removes processed members. Code chooses candidate groups; model proposes replacement content; a regex admits the line, with fallback to the first bullet. No answer oracle or per-content human veto is wired; mode is optional maintenance during bounded adaptation, triggered by curation and similarity. SRC-1, `ace/core/bulletpoint_analyzer.py`, `ace/ace.py`, `ace/ace_batch.py`.

- Immediate return: Reconstructed playbook string; original string if dependencies, bullets or qualifying groups are unavailable.
- Later read-back: Orchestrator assigns result to current playbook, used by post-curator generation, later samples and snapshots.
- Delegated visibility: Embedding model sees bullet content only; merge model sees group IDs/counters/content, not task correctness records or the full playbook.
- Selection predicate: Parsed bullets and dot-product similarity at configured threshold; unavailable dependencies bypass processing. merge=False deduplicates by keeping the first entry without a model call.
- Invalidation or expiry: Group members can be removed from the reconstructed playbook; no analyzer-specific automatic undo is wired.
- Activation or effect: Text replacement/removal is implemented; preservation of meaning and model behavioral dependence remain unobserved.
- Evidence limits: Merge instructions request first ID and summed counts but parser accepts returned ID/counts without equality checks. Failed merge falls back to first bullet while reconstruction can still remove others.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> except Exception as e:
>     print(f"⚠️  Error merging bullets: {e}, keeping first bullet from group")
>     return bullets_group[0]
> --- `ace/core/bulletpoint_analyzer.py`

Admission/rejection/recovery: regex parsing admits merged content; parse failure or call exception returns the first bullet, not the entire unchanged group. `analyze` marks all group indices processed whenever that returned bullet is truthy. This route can reduce content despite its fallback. Guidance requests a comprehensive concise merge; retained text is not accompanied by a validated preservation proof or task-score gate. SRC-1, `ace/core/bulletpoint_analyzer.py`.

#### RT-RTE-finer-scoring
Label: FINER host evaluation

Endpoints/owner: extracted generator final-answer string reaches `DataProcessor.answer_is_correct`, then `_finer_answer_is_correct`; aggregate FINER scoring calls the same consumer with return_counts. Python splits/lowercases fragments, adjusts prediction length to labels, evaluates each target then prediction in a try block, and compares values. This is a scoring route with dataset ground truth as oracle, not a model-selected tool. The processor owns interpreter execution; caller choice of FINER activates it. SRC-1, `utils.py`, `eval/finance/data_processor.py`, `eval/finance/run.py`.

- Immediate return: Boolean all-fields correctness or matching-field counts; side effects of evaluated expressions, if any, occur before comparison.
- Later read-back: Correctness determines reflection branches, stopping, metrics and best selection; arbitrary expression effects are not characterized as retained memory here.
- Delegated visibility: Host evaluator receives extracted answer fragments and target fragments; this is not provider-native tool delegation.
- Selection predicate: FINER task dispatch; comma splitting and length normalization; successful target eval precedes prediction eval, while exceptions fall back to comparison.
- Invalidation or expiry: inapplicable — the route executes a current scoring expression, not a cache with a freshness lifetime.
- Activation or effect: Python eval is wired to model-derived text without a numeric-literal restriction; actual host effects are unobserved.
- Evidence limits: No exploit or runtime fixture executed. Lowercasing/splitting and target-evaluation preconditions constrain accepted expressions; deployment permissions and containment are unknown.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> try:
>     ground_truth = eval(ground_truth)
>     prediction = eval(prediction.replace(",", "").replace("$", ""))
> except:
>     pass
> --- `eval/finance/data_processor.py`

The consequence is narrower than asserting arbitrary supplied text always executes, and stronger than calling this only a passive numeric parser: supported callers pass model-derived strings to an interpreter when the branch preconditions hold. Formula mode instead attempts float conversion; Mind2Web processors parse element/operation/value descriptions. Those alternatives do not pass through this eval branch (SRC-1, `eval/finance/data_processor.py`, `eval/mind2web/data_processor.py`, `eval/mind2web2/data_processor.py`).

### Claims

#### RT-CLM-context-improvement
Label: Evolving contexts claim

Claimed operation: ACE describes self-improvement through evolving playbooks, incremental updates and natural execution feedback. This is source doctrine/design and reported benefit, not an observed result of this analysis. SRC-1, `README.md`.

> - 🎓 **Self-Supervised Learning**: Adapts effectively without labeled supervision by leveraging natural execution feedback
> --- `README.md`

The inspected callers wire a context-adaptation capacity, but no-ground-truth prompt selection still uses target-derived feedback. Missing AppWorld implementation prevents assessing whether its natural environment feedback realizes a different route. No observed or causal performance conclusion follows from this claim or from context delivery alone.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-playbook-guidance
Label: Playbook behavioral guidance

Consumer: generator model, and separately curator/reducer models deciding future additions. Channel: full playbook text interpolated into role prompts as one user-message body. Force: natural-language guidance interpreted by the model, not a host-enforced obligation to obey any bullet. Horizon: immediate regeneration, later samples/windows, and cross-run operation when a caller explicitly reloads saved text. Code controls delivery; reliable compliance and actual behavior change remain unobserved. SRC-1, `ace/core/generator.py`, `ace/prompts/generator.py`, `ace/core/curator.py`, `ace/ace.py`.

> - Read the playbook carefully and apply relevant strategies, formulas, and insights
> --- `ace/prompts/generator.py`

Updated content can therefore enter the system's behavior-determining inputs without changing weights or source code. This establishes a live-capable instruction channel, not successful learning or exercised self-improvement. Reflector feedback reaches generator through a separate current-round prompt slot; retention of raw logs alone is not this authority path.

## Annotations

none

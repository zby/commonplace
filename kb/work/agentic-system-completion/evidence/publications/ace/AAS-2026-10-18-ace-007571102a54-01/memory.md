---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "ACE memory: whole-playbook delivery, trace-derived additions and counters, optional destructive merging, and explicit snapshot reload."
run-id: AAS-2026-10-18-ace-007571102a54-01
source-identity: "https://github.com/ace-agent/ace"
reviewed-boundary: "82709de050e1db6e6ef2f07bcb0393560b94992a"
---

# ACE memory report

## Boundary and evidence

This report covers the main-repository sequential and batched playbook loops, their component APIs, Finance and both Mind2Web callers, evaluation selection, optional analyzer maintenance, and file reload. It inherits the complete-artifact, partial-loop boundary: AppWorld submodule contents are unavailable, preventing an account of its environment feedback and memory consumers. See the [source register](boundary.md#source-register). All findings use SRC-1 at the frozen commit. No new source is admitted.

Direct reads added or checked `playbook_utils.py` parsing, counts, application, statistics and selected-bullet extraction; `ace/core/generator.py` and `ace/core/reflector.py`; curator admission and reducer sections in `ace/core/curator.py`; `ace/prompts/generator.py` and curator prompts; initialization, single-sample adaptation and offline selection/persistence in `ace/ace.py`; batch aggregation, grouped input construction and reducer application in `ace/ace_batch.py`; analyzer embedding, grouping, merge and reconstruction in `ace/core/bulletpoint_analyzer.py`; logging definitions in `logger.py`; all three caller loaders and orchestrator selection; exports in `ace/__init__.py` and `pyproject.toml`. Searches checked dispatch and persistence entry points in both orchestrators, caller initial-file options, and transport/logging fields in `llm.py` and `utils.py`. These are implementation and doctrine/design evidence, not execution evidence. Other route details below explicitly rely on supplied runtime records.

| Entry point or memory operation | Source paths | Coverage and conclusion limits |
|---|---|---|
| Three CLI loaders and batch selector | `eval/finance/run.py`, `eval/mind2web/run.py`, `eval/mind2web2/run.py` | Direct loader/main reads; [RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload). Full text, not retrieval by question. |
| Public API and dispatch | `ace/__init__.py`, `ace/ace.py`, `ace/ace_batch.py`, `pyproject.toml` | Exports and dispatch searches checked against supplied offline, online and eval-only accounts. No separate tool/hook or console-script registration appears in inspected exports/project metadata; this is not a repository-wide absence claim. |
| Generator delivery and reflector selection | `ace/core/generator.py`, `ace/core/reflector.py`, `playbook_utils.py` | Direct; [MEM-OBJ-playbook-content](#mem-obj-playbook-content), [MEM-OBJ-reflection-content](#mem-obj-reflection-content), annotation on [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation). |
| Tag admission and counter updates | `ace/ace.py`, `ace/ace_batch.py`, `playbook_utils.py` | Direct; [MEM-RTE-counter-update](#mem-rte-counter-update). Multiple tags for one ID collapse to the last tag in one update call. |
| Sequential curation, rejection | `ace/core/curator.py`, `ace/prompts/curator.py`, `playbook_utils.py` | Direct; annotation on [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation). Parser checks are not a content-quality veto. |
| Batch proposals and reduction | `ace/ace_batch.py`, `ace/core/curator.py` | Direct aggregation/reduction reads; [MEM-OBJ-operation-groups](#mem-obj-operation-groups), annotation on [RT-RTE-batch-adaptation](runtime.md#rt-rte-batch-adaptation). Recovery qualifications supplied by runtime. |
| Optional merge and public dedup alternative | `ace/core/bulletpoint_analyzer.py` | Direct; [MEM-OBJ-analyzer-embeddings](#mem-obj-analyzer-embeddings), annotation on [RT-RTE-bulletpoint-merge](runtime.md#rt-rte-bulletpoint-merge). `merge=False` is exposed by API; orchestrators use `merge=True`. |
| Validation, best and final snapshots | `ace/ace.py`, `ace/ace_batch.py`, `utils.py` | Sequential selection directly read; batch/evaluation/window progression supplied by [RT-RTE-evaluate-select](runtime.md#rt-rte-evaluate-select), [RT-RTE-online-windows](runtime.md#rt-rte-online-windows), [RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload). [MEM-OBJ-best-playbook](#mem-obj-best-playbook). |
| Scorer feedback and errors | `eval/finance/data_processor.py`, `eval/mind2web/data_processor.py`, `eval/mind2web2/data_processor.py`, `llm.py` | Supplied runtime findings, including [RT-RTE-finer-scoring](runtime.md#rt-rte-finer-scoring); no independent scorer audit or model execution. |
| Raw logs and shortened usage displays | `logger.py`, `llm.py` | Logger directly read; transport field searches; [MEM-OBJ-call-logs](#mem-obj-call-logs). No wired historical-log consumer established. |
| Provider state and model lineage | `ace/core/generator.py`, `ace/core/reflector.py`, `ace/core/curator.py`, `ace/core/bulletpoint_analyzer.py` | Supplied component records and local calls; opaque provider-side state prevents a complete account of remote retention. |
| Dataset preparation, contents and extension documentation | `eval/`, `EXTENDING_ACE.md`, `tutorials/ExtendingDatasets.md` | Not independently inspected for this report; dataset provenance and alternate custom-caller behavior remain unestablished. These limits do not negate inspected caller routes. |

## Core ideas

1. ACE retains advice as text, not model-weight updates. It delivers the entire current playbook at generation time. The generator is asked to choose relevant advice and report IDs; those reports narrow the reflector's bullet view, not the preceding generator input. This is whole-store delivery plus model interpretation, not a vector retrieval system ([MEM-OBJ-playbook-content](#mem-obj-playbook-content); [RT-BAP-playbook-guidance](runtime.md#rt-bap-playbook-guidance)).
2. Trace-derived content and trace-derived counters are different products. Reflection can generate new advice through curation, while tags increment symbolic counters. Counters accompany the advice into prompts but do not themselves trigger deterministic deletion. In a batch they are not a vote tally: one call keeps the last supplied tag per ID ([MEM-RTE-counter-update](#mem-rte-counter-update)).
3. Retention loses derivational context. The last reflection, grouped reflections and proposed operations are different intermediate views. Only installed bullet text and counters are reconstructed into the playbook. Raw call logs can retain reasoning but are not the inspected curator's historical input ([MEM-OBJ-reflection-content](#mem-obj-reflection-content), [MEM-OBJ-operation-groups](#mem-obj-operation-groups), [MEM-OBJ-call-logs](#mem-obj-call-logs)).
4. ADD-only application does not imply permanent preservation. Analyzer merging can remove group members, even after a failed merge call, and arbitrary loaded text bypasses curation. Validation selects a best snapshot rather than vetoing each current-state update ([RT-RTE-bulletpoint-merge](runtime.md#rt-rte-bulletpoint-merge), [MEM-OBJ-best-playbook](#mem-obj-best-playbook)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-playbook-content
Label: Playbook content

Source-native identity: the `content` part of formatted `self.playbook` bullet lines and any other supplied text delivered as playbook. Representational form: natural-language advice, formulas or code snippets interpreted by generator and curator models; a code snippet's presence is not an executor. Storage substrate: Python strings, then plain-text intermediate/epoch/window/final files. Lineage: constructor-supplied text of unresolved authorship, or standard empty headings followed by model-proposed additions and optional analyzer replacement. Initial-file provenance is not checked. Actual initial content was not supplied. SRC-1, `ace/ace.py`, `playbook_utils.py`, `ace/core/generator.py`.

> return f"[{bullet_id}] helpful={helpful} harmful={harmful} :: {content}"
> --- `playbook_utils.py`

> prompt = GENERATOR_PROMPT.format(playbook, reflection, question, context)
> --- `ace/core/generator.py`

The retained content reaches the generator's later invocations and curator/reducer input. At the generator it has advisory force through model interpretation, not host-enforced compliance. Whole text is passed without a question-dependent deterministic selector or truncation in this formatter. The curator token budget is an instruction, not a size bound. Model completion limits are distinct from retained-input limits. Source trust is not an admission property of the loader: caller-selected arbitrary text receives the same slot as ACE-generated text. SRC-1, `ace/prompts/generator.py`, `ace/prompts/curator.py`, `eval/finance/run.py`.

Distinct identity comparison: [RT-BAP-playbook-guidance](runtime.md#rt-bap-playbook-guidance) is the consumer authority channel; this record is its retained text input, not a duplicate channel. [RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload) is its save/load route, not this object.

#### MEM-OBJ-bullet-metadata
Label: Bullet IDs and counters

Source-native identity: parsed `id`, `helpful`, `harmful` fields attached to playbook lines. Representational form: symbolic identifiers and nonnegative integer counts. Storage substrate: the same strings and text files as [MEM-OBJ-playbook-content](#mem-obj-playbook-content), but separate operative fields. Code assigns IDs on ADD, initializes counts to zero, and derives later counts from reflector tags. The formatter retains the advice content alongside them. IDs select reflector lines and tag updates; counters feed statistics and remain visible in model prompts. They are not access permissions, timestamps or validated causal utility measurements. SRC-1, `playbook_utils.py`, `ace/core/generator.py`, `ace/ace.py`.

> if tag == 'helpful':
>     parsed['helpful'] += 1
> elif tag == 'harmful':
>     parsed['harmful'] += 1
> --- `playbook_utils.py`

The stats routine classifies high-performing/problematic/unused counts for curator input; it does not remove bullets. Duplicate loaded IDs are not ruled out: constructors reset `next_global_id` to 1, even though `get_next_global_id` exists as a utility. ID continuity is therefore not restored by text reload alone. This qualifies targeted selection: matching repeated IDs can return multiple lines. SRC-1, `ace/ace.py`, `playbook_utils.py`; [RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload). No supplied operative-object counterpart exists; the overlapping adaptation routes act on these fields.

#### MEM-OBJ-reflection-content
Label: Reflection content

Source-native identity: `reflection_content`, the full response string returned by `Reflector.reflect`. Natural-language diagnosis with embedded symbolic `bullet_tags` when supplied, held in a Python string and copied into call logs. The tag fields' deterministic effect is separately assessed in [MEM-RTE-counter-update](#mem-rte-counter-update). Lineage combines generator output, question, selected retained bullets, predicted answer, target when enabled, and target-derived correctness feedback. Thus the trace source is both the system's prior response and externally supplied task/oracle material; `no_ground_truth` does not establish label-free feedback. SRC-1, `ace/core/reflector.py`, `ace/ace.py`; [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation).

> return response, bullet_tags, call_info
> --- `ace/core/reflector.py`

Immediate regeneration receives this response in the reflection slot. Sequential curation receives the last reflection, not a concatenation of all error rounds. Post-curator generation resets the slot to `(empty)`. Reflections can shape advice retained for subsequent samples, but the reflection string itself is transient working material unless logged. Diagnosis may carry reasons; neither presence of the response nor the prompt establishes a correct diagnosis or improved capacity. Distinct identity: this is intermediate material carried on [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation) and [RT-RTE-batch-adaptation](runtime.md#rt-rte-batch-adaptation), not either route.

#### MEM-OBJ-operation-groups
Label: Operation groups

Source-native identity: `operation_groups`, dictionaries containing `group_id`, `sample_numbers` and `operations`. Storage substrate: batch-local Python lists/dictionaries, serialized as JSON in reducer input and ordinary call logs. Operative parts: symbolic grouping, section and operation fields determine handling; proposed `content` is natural-language advice evaluated by the reducer model. Lineage: selected last reflections/context are combined by group, each proposer receives the same base playbook, and validated ADD proposals escape the proposal frame. The proposer-level `reasoning` field is not copied into each returned group. SRC-1, `ace/ace_batch.py`, `ace/core/curator.py`.

> return {
>     "group_id": group_idx,
>     "sample_numbers": [record["sample_number"] for record in group_records],
>     "operations": operations,
> }
> --- `ace/ace_batch.py`

> proposed_operations = json.dumps(operation_groups, indent=2, ensure_ascii=False)
> --- `ace/core/curator.py`

The reducer consumes this intermediate representation, not all original generator traces, reflection histories or proposer reasoning. It may synthesize/drop proposals; final ADD content gets new IDs and zero counters. This record is batch-local proposal material, not already adopted memory. Adoption creates [MEM-OBJ-playbook-content](#mem-obj-playbook-content). It may preserve reasons inside content if the model puts them there; no separate reason-to-bullet lineage is enforced. Distinct identity: a material intermediate object of [RT-RTE-batch-adaptation](runtime.md#rt-rte-batch-adaptation), not a second reduction route.

#### MEM-OBJ-best-playbook
Label: Best playbook

Source-native identity: `self.best_playbook`, initialized from the current playbook and replaced on strict validation accuracy improvement. Representational form: the same natural-language content and symbolic metadata as current text, but a distinct snapshot with different admission and consumers. Storage substrate: Python string and offline `best_playbook.txt`; `final_playbook.txt` stores current text instead. Validation selection admits the complete current snapshot, not individual clauses or counters. This snapshot is used by final offline testing and can be explicitly selected for cross-run reload; current training continues without reverting to it. SRC-1, `ace/ace.py`; supplied [RT-RTE-evaluate-select](runtime.md#rt-rte-evaluate-select) and [RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload).

> if acc > best_accuracy:
>     best_accuracy = acc
>     self.best_playbook = self.playbook
> --- `ace/ace.py`

Distinct identity: retained selected product, not the evaluation/selection route. Accuracy labels it best under the supplied scorer and successful evaluations, not universally best advice. Runtime's skipped-error and all-failed evaluation limits apply. No version history or complete resume state is restored by loading this text.

#### MEM-OBJ-call-logs
Label: Call and usage logs

Source-native identity: per-call JSON `call_info` files and bullet-usage JSONL. Storage substrate: filesystem JSON/JSONL; mixed form: natural-language prompts/responses and shortened question/reflection displays, with symbolic IDs, correctness, timing and usage fields. Transport records the full prompt and response fields; usage logging is a different, truncated display surface. These are raw/selected operational records, not the derived playbook. SRC-1, `logger.py`, `llm.py`.

> "sample_context": sample_data.get("context", "")[:500] if sample_data else "",  # First 500 chars
> "sample_question": sample_data.get("question", "")[:200] if sample_data else "",  # First 200 chars
> "reflection_summary": reflection_content[:300] if reflection_content else None,  # First 300 chars
> --- `logger.py`

The logger explicitly describes historical curator lookup as future work:

> TODO: Future curator enhancement - when updating a bullet, the curator can:
> 1. Look up all training samples that used this bullet (via this log)
> 2. Review the reflection content for those samples
> --- `logger.py`

Known consumers in inspected logging/adaptation code are the filesystem writer and current-loop values, not a historical-log reader that automatically rebuilds advice. External inspection is possible but no specified automatic reader was established. Consequently retained curator reasoning is audit material, not established rationale delivery to later model decisions. This is not a claim that every arbitrary caller cannot read logs. Distinct identity from all supplied routes: these artifacts overlap the evidence retained during [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation), not its behavior-shaping output.

#### MEM-OBJ-analyzer-embeddings
Label: Analyzer embeddings

Source-native identity: local normalized `embeddings` NumPy array and dot-product `similarity_matrix`. Representational form: dense numerical, distributed representation of bullet content; storage substrate: temporary arrays during analysis, not a persistent vector database. Lineage: current parsed bullet content encoded by the external sentence-transformer model. Training data/model artifact lineage remains external and uninspected; weight/version limits are in [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model). SRC-1, `ace/core/bulletpoint_analyzer.py`.

> contents = [bullet['content'] for bullet in bullets]
> embeddings = self.embedding_model.encode(contents, convert_to_numpy=True, show_progress_bar=False)
> --- `ace/core/bulletpoint_analyzer.py`

> similarity_matrix = np.dot(embeddings, embeddings.T)
> --- `ace/core/bulletpoint_analyzer.py`

Code consumes similarity scores to group lines at a threshold. The merge model sees the corresponding readable bullet text/IDs/counts, not the opaque embeddings. Neither generator retrieval nor durable embedding persistence follows. Distinct identity from [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model): these arrays are derived data, not model parameters; from [RT-RTE-bulletpoint-merge](runtime.md#rt-rte-bulletpoint-merge): selected numerical intermediate, not maintenance route.

### Routes

#### MEM-RTE-counter-update
Label: Counter update

Owner and endpoints: the orchestrators pass parsed reflector tags to `update_bullet_counts`, which rewrites matching metadata in current playbook text. Trigger: reflection in sequential adaptation, or one aggregated tag call after batch phase one. Model authors tags; code decides matching and increments. There is no per-tag human approval or independent accuracy check on the tag. Dataset correctness guides the reflector upstream, not a deterministic truth oracle for each helpful/harmful judgment. Mode is bounded offline/online adaptation. SRC-1, `ace/ace.py`, `ace/ace_batch.py`, `ace/core/reflector.py`, `playbook_utils.py`.

- Immediate return: Reconstructed playbook text, or original text when no valid tag mapping is obtained.
- Later read-back: Counts remain beside advice in later generator/curator prompts, statistics and saved/reloaded playbooks.
- Delegated visibility: Reflector sees selected reported bullets and current response/feedback; updater sees tag dictionaries and current full text, not the reasoning behind each tag.
- Selection predicate: Valid dictionary with a truthy `id` or legacy `bullet` key; last tag per ID wins within the call; only matching parsed lines increment, and only `helpful` or `harmful` changes counts.
- Invalidation or expiry: No automatic age decay or count-triggered removal in this function; replacing or analyzer-merging the line can supersede its metadata.
- Activation or effect: Symbolic increments are implemented; delivery of revised counts to later models does not establish decisions depend on them.
- Evidence limits: Tags report model judgment, not measured attribution; batch concatenation does not count every tag occurrence for a repeated ID.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if bullet_id:
>     tag_map[bullet_id] = tag_value
> --- `playbook_utils.py`

Advice content is preserved by this updater. Missing/malformed tag entries can be ignored; a neutral or unrecognized final tag gives no increment. There is no semantic curator veto of these writes. Sequential curation rejection does not rewind earlier count changes; batch intended phase-three rollback has runtime's unresolved-handler limitation. For a batch, sample-order concatenation plus assignment means later tags can replace earlier tags before a single increment. This is distinct from adding the number of helpful reports. It narrows what the retained counts measure.

Distinct identity comparison: this sub-operation spans [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation) and [RT-RTE-batch-adaptation](runtime.md#rt-rte-batch-adaptation), so it is not contained in exactly one supplied route. Those routes cover broader proposal/generation progression; neither separately declares this last-tag admission mechanism. No duplicate supplied route is established.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-sample-adaptation](runtime.md#rt-rte-sample-adaptation)

Memory-specific write lineage is response plus task/oracle feedback → last reflection → curator response → structural admission → ADD bullet → current text → post-curator/later-sample generator. This is an automatic trace-fed write route to retained behavior-shaping material, not merely trace storage. The updater and curator are software/model admission mechanisms; initiating training is not approving each bullet. Initial text's authorship/control remains unresolved independently. SRC-1, `ace/ace.py`, `ace/core/curator.py`, `playbook_utils.py`.

> self.playbook, self.next_global_id, operations, _ = self.curator.curate(
> --- `ace/ace.py`

Curation instruction requests missing reusable advice rather than whole-store regeneration. The response must have a reasoning string and operations list, but only operation fields determine installed text; no enforced rationale or task/example pointer is copied into the new bullet. Semantic nonredundancy, correctness and budget compliance remain model policies, not application invariants. ADD required-key checks do not type-check `section`/`content`. Empty operations reject all proposed additions; parse/application failures can preserve prior text subject to successful failure handling. SRC-1, `ace/prompts/curator.py`, `ace/core/curator.py`.

> - Total token budget: {token_budget} tokens
> --- `ace/prompts/curator.py:1-70`

Working context: a generator invocation gets full playbook and one reflection, not an accumulated conversation. Reflector receives only retained lines matching reported IDs; placeholder text handles empty or unmatched selections. Regeneration replaces the reflection rather than appending every earlier round. Post-curator invocation drops reflection entirely but keeps installed advice and counts reachable through current text. These are by-value inputs and returns, not pointers back into a prior model window. SRC-1, `ace/core/generator.py`, `ace/core/reflector.py`, `playbook_utils.py`, `ace/ace.py`; single-user-message transport supplied by runtime.

> if not bullet_ids:
>     return "(No bullets used by generator)"
> --- `playbook_utils.py`

#### On [RT-RTE-batch-adaptation](runtime.md#rt-rte-batch-adaptation)

Memory-specific transformation: local response/feedback frames produce last reflection, context and tags; grouping can duplicate/shuffle reflection records before independent proposals; only proposed operations and group/sample metadata reach reduction. Reflection duplicates do not independently duplicate tag updates, since `all_bullet_tags` is assembled separately before reflection augmentation. The reduced operations are applied once; current text goes to phase-three and later invocations. SRC-1, `ace/ace_batch.py`, `ace/core/curator.py`.

> all_bullet_tags.extend(result["all_bullet_tags"])
> --- `ace/ace_batch.py`

> augmented_records = [
>     record for record in reflection_records for _ in range(augmented_factor)
> ]
> --- `ace/ace_batch.py`

The reducer's policy can reject/drop advice without human review, but its reasoning is not a required part of retained bullet content. No hard input-token cap follows from group sizing or diagnostic token counts. Per-sample frames keep other samples' reasoning out; only selected return values escape. This resembles stack-frame isolation by value, not persistent shared model-context references. Grouping then deliberately combines selected material. No raw conversation checkpoint/host-compaction alternative was established in these inspected functions. Error exclusion/rollback is not assumed reliable beyond runtime's stated handler/sentinel limits. SRC-1, `ace/ace_batch.py`, `ace/prompts/curator.py`.

#### On [RT-RTE-bulletpoint-merge](runtime.md#rt-rte-bulletpoint-merge)

Read-back selector: enabled post-curation maintenance embeds all parsed content, then code selects threshold-similar groups. This is automatic maintenance selection, not question-targeted retrieval. Dense vectors are temporary; selected text/IDs/counts are copied into a separate merge prompt. The model is asked to preserve first ID and combined counts, but regex admission does not enforce those equalities. The replacement line becomes retained advice without a score gate. SRC-1, `ace/core/bulletpoint_analyzer.py`; [MEM-OBJ-analyzer-embeddings](#mem-obj-analyzer-embeddings).

The exposed `merge=False` alternative removes all but the first group member without model synthesis. With merging enabled, failed parsing/call fallback still returns the first bullet; processing marks the group and reconstructs without other members. Therefore rejection of a merge response does not mean preservation of all original advice. No rationale is retained with the resulting line unless included in its content. Superseded members may survive in earlier text snapshots/call evidence, but no automatic analyzer undo or historical reconstruction consumer was established. SRC-1, `ace/core/bulletpoint_analyzer.py`.

> if merged_bullet:
>     first_bullet_idx = indices[0]
>     merge_mapping[first_bullet_idx] = merged_bullet
>     processed_indices.update(indices)
> --- `ace/core/bulletpoint_analyzer.py`

#### On [RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload)

Memory-specific selection is explicit caller path → existence check → full file → truthy constructor input. The reader does not choose bullets by question or automatically select the newest/best filename. Files can hold current, selected-best, epoch or online-window text; none is a complete execution checkpoint. Human content selection/editing is possible through the exposed path, but whether a human or program authored/selected any particular input is unresolved. This is distinct from model-authored in-loop additions. No provenance authentication, rationale recovery or enforced trust distinction is added before delivery to generator/curator. SRC-1, `eval/finance/run.py`, `eval/mind2web/run.py`, `eval/mind2web2/run.py`, `ace/ace.py`.

> if path and os.path.exists(path):
>     with open(path, 'r') as f:
>         return f.read()
> --- `eval/finance/run.py`

## Write side

Acquisition has two independent admission boundaries: arbitrary truthy constructor/loaded input, and in-loop model-derived additions. No initial playbook instance is available, so content authorship and any external approval of initialization stay unknown. Later transformations are known despite that gap. CLI/API callers can replace the entire initial text; the loader is physical I/O, not evidence of a human author or reviewer. See [RT-RTE-playbook-reload](runtime.md#rt-rte-playbook-reload) annotation.

Automatic derivation has two outputs: [MEM-OBJ-bullet-metadata](#mem-obj-bullet-metadata) from tags and [MEM-OBJ-playbook-content](#mem-obj-playbook-content) from curator operations. Tags depend on generator self-reported bullet selection and reflector judgments. Curator additions depend on last or grouped reflections, with syntax checks and optional reducer judgment but no per-addition independent correctness gate. The trace-fed write is wired across samples; raw logs alone are not that mechanism. Requested reusable diagnosis does not establish an actual theory, learning gain or exercised self-improvement. Runtime's separate property limits remain in force.

Maintenance and withdrawal use another boundary: optional analyzer similarity grouping followed by regex-admitted replacement, or first-member deduplication. This can withdraw advice and counters without task evaluation. ADD-only application and unused DELETE names do not supply a deterministic erroneous-advice removal policy. Replacing the input file is another coarse withdrawal mechanism; neither it nor analyzer fallback reconstructs a full prior run. See [RT-RTE-bulletpoint-merge](runtime.md#rt-rte-bulletpoint-merge).

Evaluation selects [MEM-OBJ-best-playbook](#mem-obj-best-playbook), not whether each addition enters current training state. Current and best snapshots have separate later consumers. Rejected additions, failed calls and rejected merge outputs have different effects; no universal transaction covers counters, calls, logs, additions and analyzer removal. Runtime's unresolved batch error handler prevents assuming its intended rollback always executes.

## Read-back

The principal read-back chain is current text → automatic whole-playbook formatter → generator invocation, triggered by another round/sample/window/evaluation. Inputs are current text, task/context and the current reflection slot; the selected retained part is all supplied playbook text. No request for a particular bullet precedes this delivery. Relevant-bullet selection happens within the model and is reported afterward. The authority is advisory model input; observed compliance, content-dependent decisions and benefit are uninspected. See [RT-BAP-playbook-guidance](runtime.md#rt-bap-playbook-guidance).

A second chain is reported IDs → parsed-line filter → reflector prompt. It selects matching content and counters, not a history of past uses. Empty/missing IDs deliver placeholders. A third is whole current text plus last/grouped reflection → curator, and whole current text plus proposed-operation groups → reducer. These are update consumers with a different authority from the generator: their admitted outputs can alter what later generators receive. Token budget is prompt policy; no hard playbook size bound was established in the inspected formatter/application paths.

Cross-run delivery requires naming a file. Standard intermediate/final/best/window files make text reuse wired through shipped loaders, but no scheduler automatically activates a saved artifact. A `test` call or `eval_only` invocation consumes the selected supplied/current text without adaptation as described by [RT-RTE-evaluate-select](runtime.md#rt-rte-evaluate-select). Stored raw log files and transient embeddings lack an established later automatic consumer route. Opaque provider-side memory is not inferred from API calls or role labels.

## Integration issues

- **Counter aggregation refinement:** [MEM-RTE-counter-update](#mem-rte-counter-update) qualifies [RT-RTE-batch-adaptation](runtime.md#rt-rte-batch-adaptation)'s statement that tags are aggregated. Aggregation concatenates them, but `tag_map[bullet_id] = tag_value` collapses duplicates before incrementing. No contradiction with concatenation itself; reconciliation must not describe counters as summed votes or frequencies of all batch judgments. SRC-1, `ace/ace_batch.py`, `playbook_utils.py`.
- **Identity comparison:** no duplicate supplied operative-object declaration exists. The seven new object records are material inputs/intermediates/products of runtime routes rather than replacement route identities; their closest supplied counterparts and distinctions are in each declaration. [MEM-RTE-counter-update](#mem-rte-counter-update) spans two supplied routes, as stated there. No supersession is proposed.
- **Initial and opaque lineage:** actual initial text, authorship/approval, external model training data, endpoint version and provider retention remain unresolved. Consequence: do not assign human approval, trustworthy provenance or fully known remote retention to [MEM-OBJ-playbook-content](#mem-obj-playbook-content), [MEM-OBJ-analyzer-embeddings](#mem-obj-analyzer-embeddings) or runtime model components. Source/API inspection bounds these questions, not an unavailable local file claim.
- **Reason delivery:** [MEM-OBJ-call-logs](#mem-obj-call-logs) can retain reasoning, but [MEM-OBJ-operation-groups](#mem-obj-operation-groups) omits proposer-level reasoning and installed text has no enforced separate rationale link. Consequence: historical rationale retention must not be equated with later rationale consumption. Individual advice might include reasons; no generated instance was supplied to decide that.
- **AppWorld and operation:** the boundary's missing submodule prevents extending these memory routes to AppWorld. No run/experiment establishes actual activation, model compliance, semantic preservation under merging, or improved capacity. These are justified limits, not implementation absences.

## Limitations and checks

The source checkout HEAD was rechecked as `82709de050e1db6e6ef2f07bcb0393560b94992a`; its status was clean during inspection. Supplied run/source/revision fields are preserved. The governing invocation, member types, worker rules and record contract were read completely. Source-only inspection did not execute ACE, its examples/tests, or provider calls. Evidence layers and direct-versus-supplied coverage are distinguished above. No content-dependent theory instance or causal improvement result is asserted.

Deterministic validation: the invocation's `validate-output` command passed after file creation. This checks form, identity, references and quotation occurrence, not analytical correctness or acceptance.

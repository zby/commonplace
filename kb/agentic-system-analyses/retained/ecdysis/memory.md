---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Ecdysis memory: failure compaction, bounded review context, checkpoint reuse, retained harnesses and separately loaded skill artifacts."
run-id: AAS-2026-10-13-ecdysis-bb4c64dbdf60-01
source-identity: "https://github.com/cuiyu-ai/Ecdysis"
reviewed-boundary: cf93866d545b0974dbb0bc83b39c31fbbdeeecb8
---

# Ecdysis memory report

## Boundary and evidence

This report covers memory and working-context control in the shipped improvement plane at the [boundary](boundary.md)'s frozen commit. Included surfaces are result-file ingestion, failure extraction, role-context construction, transcript/checkpoint retention, specification delivery, harness admission and later inference, skill artifact utilities, and result/usage records. The task runtime, real editor, scorer implementation, provider internals and cross-process harness factory are external. Their opaque state is not attributed to Ecdysis. No execution trace was supplied; source tests establish intended consumers, not observed runs.

Direct reads below use SRC-1, implementation unless identified as doctrine/design. I independently read `src/ecdysis/evolution.py`, `src/ecdysis/artifacts.py`, `src/ecdysis/training.py`, `src/ecdysis/inference.py`, `src/ecdysis/benchmark.py`, `src/ecdysis/__main__.py`, `src/ecdysis/__init__.py`, `src/ecdysis/fdcr/review.py`, `src/ecdysis/fdcr/roles.py`, `src/ecdysis/llm_client.py`, `examples/quickstart.py`, `tests/test_artifacts.py`, `tests/test_evolution_checkpoint.py`, `README.md` and `pyproject.toml`. Roles and README also supply doctrine/design. Scoped searches across `src`, `examples` and `tests` checked alternative consumers, convergence/regression helpers, tools, hooks and withdrawal operations. Other test findings remain supplied runtime evidence, not independent reads.

| Entry point or operation | Source path (SRC-1) | Coverage and limits |
|---|---|---|
| `ecdysis` / result-file or directory ingestion | `pyproject.toml`; `src/ecdysis/__main__.py`; `src/ecdysis/evolution.py` | Direct: [MEM-OBJ-trajectories](#mem-obj-trajectories), [RT-RTE-failure-review](runtime.md#rt-rte-failure-review). CLI prints counts, not reusable skill writes. File ingestion explicitly expects JSON object results, not inference JSONL. |
| Failure-only and all-trajectory extraction; grouping/formatting | `src/ecdysis/evolution.py`; `src/ecdysis/__init__.py` | Direct: [MEM-OBJ-trajectories](#mem-obj-trajectories). All-trajectory API keeps successes and missing rewards; its default tail is 20 rather than 80. No shipped subsequent model consumer of that alternative was found. |
| FDCR calls and context reconstruction | `src/ecdysis/fdcr/review.py`; `src/ecdysis/fdcr/roles.py` | Direct: [MEM-OBJ-transcript](#mem-obj-transcript), annotation on [RT-RTE-failure-review](runtime.md#rt-rte-failure-review). Separate two-message calls, metadata-only failure display, twelve-turn history slice. |
| Checkpoint write/reload, interruption and completed reuse | `src/ecdysis/fdcr/review.py`; `tests/test_evolution_checkpoint.py` | Direct: [MEM-OBJ-checkpoint](#mem-obj-checkpoint), [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery). Resume and completed cached spec are different consumers of the same file. |
| Standalone transcript save and specification rendering | `src/ecdysis/fdcr/review.py` | Direct: [MEM-OBJ-transcript](#mem-obj-transcript), annotation on [RT-OBJ-review-spec](runtime.md#rt-obj-review-spec). Save and rendering are capabilities; no shipped standalone saved-transcript reader or coding-agent execution is established. |
| Train, candidate evaluation, rejection and later inference | `src/ecdysis/training.py`; `examples/quickstart.py` | Direct: [MEM-OBJ-round-record](#mem-obj-round-record), annotations on [RT-OBJ-frozen-harness](runtime.md#rt-obj-frozen-harness) and [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission). Real harness encoding and editor behavior remain external. |
| Skill construction, save/load, scope validation and first-ID merge | `src/ecdysis/artifacts.py`; `src/ecdysis/evolution.py`; `tests/test_artifacts.py` | Direct: [MEM-OBJ-evolved-skill](#mem-obj-evolved-skill), [MEM-OBJ-skill-artifact](#mem-obj-skill-artifact), [RT-RTE-artifact-utilities](runtime.md#rt-rte-artifact-utilities). Actual shipped reader is a test comparing round-trip data; no task-agent skill consumer. |
| Inference API, benchmark CLI, JSONL output | `src/ecdysis/inference.py`; `src/ecdysis/benchmark.py`; `pyproject.toml` | Direct: [MEM-OBJ-inference-record](#mem-obj-inference-record), [RT-RTE-harness-inference](runtime.md#rt-rte-harness-inference). Outputs may be opaque until adapter encoding; model-visible task context is external. |
| Usage accounting / model state | `src/ecdysis/llm_client.py`; `src/ecdysis/fdcr/review.py` | Direct: [MEM-OBJ-checkpoint](#mem-obj-checkpoint), [RT-CMP-review-model](runtime.md#rt-cmp-review-model). Usage events are counters, not semantic memory; provider weights/state/version are opaque. |
| Convergence/regression helpers; cleanup, withdrawal, tools/hooks | `src/ecdysis/evolution.py`; `src/ecdysis/training.py`; `src/ecdysis/artifacts.py`; `src/ecdysis/fdcr/review.py` | Direct reads plus scoped search: [MEM-ABS-skill-injection](#mem-abs-skill-injection). Helpers return booleans but trainer does not consult them. No separate skill expiry or deletion protocol is exposed by these APIs; no tool/hook registration adds another memory route in inspected dispatch. External callbacks can do more. |

## Core ideas

1. **Trace evidence reaches two different consumers.** The editor receives compacted messages, task data and failure metadata; review models receive only cluster/sample metadata. The review cannot diagnose a particular action from message evidence it never receives. Tail compaction is a transformation, not a semantic summarizer ([MEM-OBJ-trajectories](#mem-obj-trajectories); [RT-RTE-failure-review](runtime.md#rt-rte-failure-review)).
2. **Review memory is a transcript plus a filtered display.** Full replies persist in process and optionally JSON, while each fresh role request selects the last twelve turns. Older turns remain stored but there is no on-demand model retrieval path. The Moderator's instruction to read the full review does not override this slice ([MEM-OBJ-transcript](#mem-obj-transcript); [RT-RTE-failure-review](runtime.md#rt-rte-failure-review)).
3. **Checkpoint state can acquire direct control authority.** Its progress index chooses calls to skip; completed state returns a cached specification. Matching hashes establish equality of the displayed context and pass count, not unchanged raw evidence, role policy or provider identity ([MEM-OBJ-checkpoint](#mem-obj-checkpoint); [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery)).
4. **Harness retention and skill persistence are separate.** Score admission selects a live harness reference, which reaches later collection/execution. Skill artifacts retain portable instruction text but supply it only to explicit API callers. They neither inherit trainer score admission nor automatically enter inference ([RT-BAP-retained-harness](runtime.md#rt-bap-retained-harness); [MEM-OBJ-evolved-skill](#mem-obj-evolved-skill); [MEM-ABS-skill-injection](#mem-abs-skill-injection)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-trajectories
Label: Extracted trajectory evidence

Identity: dictionaries returned by `collect_failed_trajectories` and `collect_all_trajectories`, held in Python lists in process memory. Their source is caller-supplied `tasks`/`simulations` dictionaries or a JSON object file (`results.json` when a directory is given). Original task/model/tool provenance is unresolved beyond supplied fields. This is trace data, not a newly learned rule. Symbolic reward, trial, termination and tool-call fields use fixed selection/grouping rules; message content and task payloads can contain natural language or arbitrary adapter data. Tool arguments are copied, not interpreted or executed by extraction.

No object counterpart is declared in the supplied runtime. This object is input state of [RT-RTE-failure-review](runtime.md#rt-rte-failure-review), not the normalized review specification. Failed extraction excludes missing rewards and rewards at or above threshold. It keeps the configured message tail and truncates each truthy content string; task payloads and tool arguments have no matching character cap. Compaction drops other message fields. The all-trajectory alternative skips the failure predicate and failure-only diagnostic fields; it is an exposed extraction capability without a shipped later FDCR consumer. Editor delivery is wired through the trainer; models receive a further metadata-only rendering, not these messages. Storage does not itself establish read-back or learning (SRC-1, `src/ecdysis/evolution.py`, `src/ecdysis/training.py`, `src/ecdysis/fdcr/review.py`).

> selected_messages = messages[-max_messages:] if max_messages else []
> --- `src/ecdysis/evolution.py`

> compact["content"] = str(content)[:max_content_chars]
> --- `src/ecdysis/evolution.py`

#### MEM-OBJ-transcript
Label: FDCR review transcript

Identity: `transcript`, a list of role/content dictionaries containing stripped model replies and a final JSON-rendered normalized Moderator spec. Symbolic role keys label turns; non-Moderator bodies are natural-language text. It resides in process memory and optionally checkpoint JSON or a standalone `save_fdcr_transcript` file. Its lineage is model review over formatted failure metadata and earlier selected turns. Replies can carry proposed reasons and criticism, but no supplied transcript establishes that they actually do. Moderator normalization retains four spec fields; extra parsed fields and original response formatting are not retained in its appended turn.

The transcript has no supplied object counterpart; it is retained state of [RT-RTE-failure-review](runtime.md#rt-rte-failure-review) and [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery). Subsequent model invocations consume its last twelve turns through newly constructed user content. A completed checkpoint can return the full stored transcript to the caller; the trainer takes only the spec for its editor. Standalone transcript saving accepts arbitrary payloads and establishes storage, not a subsequent reader. Turns are not individually addressed by a retrieval API (SRC-1, `src/ecdysis/fdcr/review.py`).

> transcript.append({"role": role, "content": content.strip()})
> --- `src/ecdysis/fdcr/review.py`

> def save_fdcr_transcript(payload: dict[str, Any], path: str | Path) -> Path:
>     out = Path(path)
>     out.parent.mkdir(parents=True, exist_ok=True)
>     out.write_text(json.dumps(payload, indent=2))
>     return out
> --- `src/ecdysis/fdcr/review.py`

#### MEM-OBJ-checkpoint
Label: FDCR checkpoint state

Identity: review's `state` dictionary serialized to caller-selected JSON. Symbolic version, status, hash, model name, rounds, index, active-turn/error and usage fields control recovery or describe access/accounting; transcript/spec contain natural-language review content within symbolic containers. These parts are distinguished from raw trajectories: neither raw messages nor original task payloads are serialized into the checkpoint. It retains successful review outputs and progress; completed state additionally retains the normalized spec. Usage segments aggregate completed calls, attempts, duration and token counts, not reasoning or task evidence.

There is no supplied object counterpart; this is the state underlying [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery), containing [MEM-OBJ-transcript](#mem-obj-transcript) and optionally [RT-OBJ-review-spec](runtime.md#rt-obj-review-spec). A running/interrupted consumer uses index and transcript to resume; a completed consumer returns stored outputs without model calls. Its hash lineage is the formatted context plus pass count; model equality checks the string. Caller file control is unresolved as human versus program control; code writes automatically before/after turns. No signature, expiry or role-policy fingerprint is enforced. Temporary-file replacement changes physical write behavior, not semantic approval or concurrency ownership (SRC-1, `src/ecdysis/fdcr/review.py`, `src/ecdysis/llm_client.py`; recovery passages in [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery)).

> pending = path.with_suffix(path.suffix + ".tmp")
> pending.write_text(json.dumps(payload, indent=2, sort_keys=True))
> pending.replace(path)
> --- `src/ecdysis/fdcr/review.py`

#### MEM-OBJ-evolved-skill
Label: EvolvedSkill instruction content

Identity: each `EvolvedSkill` instance's `title`, `pattern` and `tip`, with symbolic `id` addressing the unit. Content resides in dataclasses in memory or a containing artifact's JSON. Pattern/tip are natural-language proposed behavior for an interpreting consumer; identifier comparison is symbolic. Initial authorship can be manual, model-produced or arbitrary caller content. The docstring's “learned” label and default `source="evolution"` do not demonstrate trace derivation or improved capacity. The Moderator's `skills` output can supply compatible dictionaries, but no trainer conversion/save path is wired automatically.

No supplied object counterpart exists; [RT-RTE-artifact-utilities](runtime.md#rt-rte-artifact-utilities) handles these units, whereas [RT-OBJ-review-spec](runtime.md#rt-obj-review-spec) only optionally contains raw skill dictionaries. `from_dict` rejects falsey required values and stringifies content; direct dataclass construction bypasses that check. Neither route semantically vets a tip. Loading and merge deliver units to explicit callers, with first-ID selection rather than contextual relevance. A task-model interpretation path is unestablished. Whole units are inspectable/replacable by caller code; formal theory content is not required (SRC-1, `src/ecdysis/artifacts.py`, `src/ecdysis/evolution.py`, `src/ecdysis/fdcr/roles.py`).

> required = ("id", "title", "pattern", "tip")
> missing = [key for key in required if not data.get(key)]
> --- `src/ecdysis/artifacts.py`

> skill if isinstance(skill, EvolvedSkill) else EvolvedSkill.from_dict(skill)
> --- `src/ecdysis/evolution.py`

#### MEM-OBJ-skill-artifact
Label: SkillArtifact envelope and provenance metadata

Identity: `SkillArtifact`, a symbolic dataclass/JSON envelope carrying experiment, scope, round, mode, skills, timestamp, parent strings, metadata and schema version. Text-bearing skills are separately described in [MEM-OBJ-evolved-skill](#mem-obj-evolved-skill). Metadata is caller-defined and can be opaque. Source task IDs and issue type reside on skills, not as independently checked trace links. A skill's generic metadata could retain reasons, but only pattern/tip/title are mandatory; the normal Moderator skill schema has no rationale field. Thus reason retention and later reason consumption are unresolved for exported skills.

No supplied object counterpart exists. This is the container manipulated by [RT-RTE-artifact-utilities](runtime.md#rt-rte-artifact-utilities). Its version and round labels do not implement historical rollback. Scope gates optional multi-path loads and every parent merge, but direct `load_skill_artifact` has no expected-scope input. Merge keeps original skill objects and concatenates existing parent strings: it does not automatically record each immediate input artifact path or identity, and discards parent envelope metadata unless caller supplies replacement metadata. Save overwrites its path. The inspected test caller saves, reloads and compares full dictionaries; that is a real shipped source consumer, not a task-agent consumer or an observed run (SRC-1, `src/ecdysis/artifacts.py`, `tests/test_artifacts.py`).

> parents.extend(artifact.parent_artifacts)
> --- `src/ecdysis/artifacts.py`

> self.assertEqual(loaded.to_dict(), artifact.to_dict())
> --- `tests/test_artifacts.py`

#### MEM-OBJ-round-record
Label: Training round decision records

Identity: immutable `RoundRecord` dataclass fields retained as `TrainingResult.rounds`, a tuple in process memory. Symbolic records contain baseline/candidate/retained scores, failure/group counts, acceptance flag and status. They derive from the trainer's own round computation, not a full raw trace. They do not retain candidate payload, specification, criticisms, per-task results or rollback snapshots. They are companion audit data to [RT-OBJ-frozen-harness](runtime.md#rt-obj-frozen-harness), not another harness. No supplied object counterpart exists.

Training admission creates these records automatically; a human per-record approval is not wired. The caller can inspect the returned tuple. Neither next-round collection nor `TrainingResult.infer` reads it to decide actions; convergence/regression helpers in `evolution.py` accept separately supplied score dictionaries and are not invoked by the trainer. Records therefore describe acceptance without enforcing future behavior. No automatic durable save/reload is provided (SRC-1, `src/ecdysis/training.py`, `src/ecdysis/evolution.py`; admission quote in [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission)).

> rounds=tuple(records),
> --- `src/ecdysis/training.py`

#### MEM-OBJ-inference-record
Label: Batch inference outcomes

Identity: `InferenceRecord` dataclasses in `InferenceResult.records`, optionally serialized as one JSON object per task; `BenchmarkRun` adds name/version/split. Symbolic indices, IDs, timing and error fields accompany caller task/output payloads. Output form and provenance are external until inspected adapter encoding; readable JSON produced through `default=str` need not preserve an opaque output's full executable structure. A success flag means no caught executor exception, not reward correctness.

No supplied object counterpart exists; this is immediate output of [RT-RTE-harness-inference](runtime.md#rt-rte-harness-inference), not a retained harness. Source consumers render summaries and write JSONL; no package reader converts those rows into the `tasks`/`simulations` reward structure required by failure extraction. Failed task/error data is retained when batch execution continues, but not automatically transformed into learned guidance. There is no model context-selection authority from these records in the inspected runner (SRC-1, `src/ecdysis/inference.py`, `src/ecdysis/benchmark.py`, `src/ecdysis/evolution.py`).

> def succeeded(self) -> bool:
>     return self.error is None
> --- `src/ecdysis/inference.py`

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

#### MEM-ABS-skill-injection
Label: No shipped automatic skill injection into inference

implementation conclusion status: absent

At SRC-1 revision cf93866d545b0974dbb0bc83b39c31fbbdeeecb8, direct reads of `src/ecdysis/training.py`, `src/ecdysis/inference.py`, `src/ecdysis/benchmark.py`, `src/ecdysis/artifacts.py`, `src/ecdysis/evolution.py`, `src/ecdysis/__init__.py`, `src/ecdysis/__main__.py`, `pyproject.toml` and `examples/quickstart.py`, plus `rg` across `src examples tests` for `load_evolved_skills|artifact_from_skills|merge_skill_artifacts|save_fdcr_transcript|format_update_spec|collect_all_trajectories|check_convergence|check_regression|unlink|delete|remove|checkpoint|skill|hook|tool`, found no automatic artifact-to-inference consumer. Trainer returns a harness; runner forwards it unchanged by Ecdysis to executor. The benchmark factory is external and could load skills, so absence is scoped to shipped wiring, not possible integrations. There is no supplied absence counterpart; this bounds [RT-RTE-artifact-utilities](runtime.md#rt-rte-artifact-utilities) and [RT-RTE-harness-inference](runtime.md#rt-rte-harness-inference). It prevents treating JSON skill persistence as demonstrated agent read-back.

> return executor(self.frozen_harness, task)
> --- `src/ecdysis/training.py`

> output = self.executor(self.harness, task)
> --- `src/ecdysis/inference.py`

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-failure-review](runtime.md#rt-rte-failure-review)

Memory-specific selection chain: code extracts reward failures into [MEM-OBJ-trajectories](#mem-obj-trajectories), groups signatures and formats metadata for every role call. Displayed cluster IDs are capped at eight per cluster and failure samples at twelve, but all clusters are retained and no token budget is implemented. Raw messages, task descriptions, current harness, reward-basis/info and tool details never enter this review display. In contrast, editor delivery contains compacted failures and full groups. These different consumer inputs limit the review's trace-grounding, even though the editor has more evidence (SRC-1, `src/ecdysis/evolution.py`, `src/ecdysis/fdcr/review.py`, `src/ecdysis/training.py`).

> for f in failures[:12]:
>     sample.append(
>         f"  task={f.get('task_id')} trial={f.get('trial')} "
>         f"reward={f.get('reward')} term={f.get('termination_reason')} "
>         f"breakdown={f.get('reward_breakdown')}"
>     )
> --- `src/ecdysis/fdcr/review.py`

Fresh calls isolate each role's request to static role policy, reconstructed failure display, history tail and turn instruction. Code selects [MEM-OBJ-transcript](#mem-obj-transcript)'s last twelve turns, not a model-selected summary. No provider conversation handle or pointer is passed; whole text replies escape into transcript. This resembles separate call frames with selected arguments and returns. The analogy stops at textual copies: stored older turns are not dereferenceable heap objects available to the model. Later calls automatically receive a tail; omitted turns have no on-demand reload route. Source storage may preserve reasons that actual role consumption excludes. Context selection is wired; semantic use of retained criticisms and benefit are unobserved. See the supplied route's history quotation and separate theory-condition conclusions rather than equating transcript retention with fulfilled theory building.

#### On [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery)

[MEM-OBJ-checkpoint](#mem-obj-checkpoint) supports two read-back paths. Running/interrupted reentry restores successful replies and next-turn index, then each resumed model call sees only its ordinary history tail. Completed reentry restores the spec directly to the caller; the trainer can deliver it to an editor without fresh review. This is caller-requested file selection followed by automatic status/hash/index selection, not independent unsolicited memory supply. No content relevance search occurs (SRC-1, `src/ecdysis/fdcr/review.py`, `tests/test_evolution_checkpoint.py`).

Same formatted context can result from changed omitted messages, task descriptions or unsampled failure details. Therefore a matching checkpoint may be reused despite changed editor-visible evidence. Static role prompt revisions and endpoint changes also evade the key. The model name/hash check is a bounded freshness control, not a trust guarantee for arbitrary caller-edited JSON. Successful-call usage segments persist as accounting, but resumed `usage` measures the current invocation; retained `usage_segments` carries prior segments separately. Empty failures return before checkpoint loading, so that branch neither reads nor replaces old state. Invalidation raises rather than removing/rebuilding a mismatched file. Error and active-turn fields are cleared after successful progression/completion, not a semantic withdrawal of proposals.

> if not failures:
>     return {
>         "transcript": [],
>         "spec": _parse_moderator_spec(None),
> --- `src/ecdysis/fdcr/review.py`

#### On [RT-OBJ-review-spec](runtime.md#rt-obj-review-spec)

Normalized spec retains patterns, changes, skills and notes. Proposed changes can retain rationales; the editor receives them in the spec dictionary, and `format_update_spec` renders them for an explicit caller. It renders all supplied changes/skills, with no acceptance filter, while appending a minimal/test-safe implementation instruction. That formatter does not execute a coding agent or demonstrate its compliance. Role critique text survives separately in [MEM-OBJ-transcript](#mem-obj-transcript), not necessarily in each final change's rationale. Skill export need not carry those reasons. Malformed parsed output becomes empty fields, not semantic rejection; nonempty failures still cause trainer editing (SRC-1, `src/ecdysis/fdcr/review.py`, `src/ecdysis/training.py`; supplied specification/editor quotations in [RT-OBJ-review-spec](runtime.md#rt-obj-review-spec) and [RT-BAP-review-editor](runtime.md#rt-bap-review-editor)).

> f"- [{ch.get('component', '?')}] {ch.get('description', '')}: "
> f"{ch.get('rationale', '')}"
> --- `src/ecdysis/fdcr/review.py`

#### On [RT-OBJ-frozen-harness](runtime.md#rt-obj-frozen-harness)

Initial harness content, write agency, encoding and storage provenance remain caller-controlled. Known subsequent transformations must not be suppressed by that uncertainty: collector evidence feeds review/editor, editor returns a candidate, and score comparison chooses the later live reference. Quickstart uses symbolic `revision` state with fixed consumers; its editor ignores text, so it supplies a counterexample to automatic review-content-responsive repair. A real harness can contain instructions, code or parameters, but none is established by the generic API. The retained harness is not automatically stored beside FDCR JSON. Later authority reaches collector/executor, as [RT-BAP-retained-harness](runtime.md#rt-bap-retained-harness) establishes; reasons and trace evidence do not automatically travel with that reference (SRC-1, `src/ecdysis/training.py`, `examples/quickstart.py`).

#### On [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission)

Trace-fed update is wired through adapter editing and scalar admission. Acquisition and transformation are automatic after caller setup; no per-content human approval is enforced. The editor proposes organization changes, scorer/collector supply evaluation and trainer decides strict-improvement reference retention. No task-answer oracle is added here; real reference outcomes remain external and quickstart's reward is a fixed revision predicate. Rejected candidates are not returned as retained harness, but their prior review specification/checkpoint can remain on disk. There is no propagated tombstone withdrawing rejected advice from future checkpoint reuse or artifact APIs. Rejection cannot undo callback mutation. [MEM-OBJ-round-record](#mem-obj-round-record) preserves the decision without preserving the candidate or rollback state. Read-back of an accepted reference into later rounds/inference is wired; improved future capacity and exercised content-dependent adaptation are not established by source alone (SRC-1, `src/ecdysis/training.py`, `src/ecdysis/fdcr/review.py`; supplied acceptance and mutation account in the annotated route).

#### On [RT-RTE-artifact-utilities](runtime.md#rt-rte-artifact-utilities)

[MEM-OBJ-evolved-skill](#mem-obj-evolved-skill) and [MEM-OBJ-skill-artifact](#mem-obj-skill-artifact) distinguish instruction content from envelope/source metadata. Explicit path loading is request-directed; path order plus first-ID deduplication determines which version survives. A newer same-ID tip supplied as `new_skills` loses to an earlier parent, so merge is not a semantic revision operation. Direct load has structural validation; expected scope is optional for `load_evolved_skills`, mandatory for parent merge. Typed construction permits bypass of dictionary checks. Save performs physical I/O, not independent admission or human approval. Caller identity and initial authorship remain unresolved; workflow launch is not evidence of human curation of every tip (SRC-1, `src/ecdysis/artifacts.py`, `src/ecdysis/evolution.py`).

Test code is a shipped later reader for structural round-trip comparison, not a later agent interpreting tips. Optional arbitrary metadata can retain reasons or trace links, but source task IDs/default source labels are not verified provenance. Merge keeps only existing parent strings rather than creating a complete ancestry record. No score gate, expiry, retirement propagation or automatic restoration is provided by this utility route. Whether exported content is trace-learned must be traced per caller; the utility accepts manual artifacts too.

> for skill in new_skills or []:
>     if skill.id not in seen_ids:
>         seen_ids.add(skill.id)
>         merged.append(skill)
> --- `src/ecdysis/artifacts.py`

#### On [RT-RTE-harness-inference](runtime.md#rt-rte-harness-inference)

The live harness is the retained behavior-shaping input; [MEM-OBJ-inference-record](#mem-obj-inference-record) is an outcome trace, not a second adaptation store. Inference results and benchmark JSONL retain task/output/error/timing fields with optional encoder conversion. They do not automatically feed failure review, and their schema is not the reward-bearing results schema. A separately supplied harness factory could load durable content, but source does not reveal its selector, provenance or task-model context budget. Inference imposes no model-visible context management itself: that responsibility belongs to the executor. “Without adaptation” concerns Ecdysis scheduling, not deep immutability of the callback's argument (SRC-1, `src/ecdysis/inference.py`, `src/ecdysis/benchmark.py`, `src/ecdysis/training.py`, `src/ecdysis/evolution.py`).

## Write side

| Mechanism | Author / physical writer | Admission and curation | Retained result / later consumer |
|---|---|---|---|
| Initial harness and results | Generic caller/adapters; result-file writer external | Initial human control unresolved. Extraction software checks limits/threshold, filters failures and compacts messages; grouping does not semantically verify evidence. | [MEM-OBJ-trajectories](#mem-obj-trajectories) reaches editor; reduced metadata reaches review calls. |
| Role transcript and spec | Review model authors content; code strips replies, appends turns and normalizes Moderator fields | Role instructions request criticism and conservative repair; no semantic per-turn admission gate or human signoff. | [MEM-OBJ-transcript](#mem-obj-transcript) feeds later calls; [RT-OBJ-review-spec](runtime.md#rt-obj-review-spec) feeds editor and optional checkpoint reuse. |
| Checkpoint / standalone save | Review code writes JSON automatically; generic caller chooses path or supplies standalone payload | Hash/model mismatch rejects reuse; caller-editable content not authenticated. Temp replacement is I/O, not curation. | [MEM-OBJ-checkpoint](#mem-obj-checkpoint) controls resume/cached return. Standalone transcript save has no established reader. |
| Harness revision | Supplied editor authors candidate; trainer selects reference | Strict score improvement admits; equal/lower rejects. No in-place rollback, held-out check or package-enforced evaluator integrity. | [RT-OBJ-frozen-harness](runtime.md#rt-obj-frozen-harness) reaches later collector and executor. Audit tuple is separate. |
| Skills / artifact envelope | Manual/model/caller content; utility writes caller-selected JSON | Required dictionary fields, optional read scope, mandatory parent merge scope and first-ID dedup. Typed objects bypass some checks; no trainer admission inheritance. | Explicit load delivers [MEM-OBJ-evolved-skill](#mem-obj-evolved-skill) to caller; task-agent authority unestablished. |
| Inference and usage records | Runner/client automatically produce records; caller optionally requests output writes | Exception capture or fail-fast, optional output encoding; no semantic answer approval. | [MEM-OBJ-inference-record](#mem-obj-inference-record) and usage segments are audit/output data, not wired learning feedback. |

The raw-to-derived chain is collector results → compacted failures → metadata display → model replies/spec → editor candidate → score-selected harness → later collection/inference. Each arrow is wired, but review sees less evidence than editor, quickstart editing ignores the spec, and real content-dependent change remains unobserved. Compaction alone does not create behavioral guidance; the potential guidance is model/editor-derived, with its reasons possibly in transcript and change rationales. There is no guarantee those reasons enter the final harness or skill artifact. Accepted harnesses, interrupted transcript checkpoints and completed cached specs have different later consumers and must not be collapsed into one learned-memory object.

Cleanup in inspected review code removes transient error/active-turn metadata. Failure tails and history slicing exclude display content without deleting source files or old transcript turns. Rejection keeps the previous harness reference but does not delete the spec checkpoint. Artifact overwrite can replace a file; no exposed retirement protocol invalidates previously loaded objects. These are implementation limits, not claims about external lifecycle management (SRC-1, `src/ecdysis/fdcr/review.py`, `src/ecdysis/training.py`, `src/ecdysis/artifacts.py`; records above).

## Read-back

| Later consumer | Trigger and selector | Delivered retained material / budget | Authority and status |
|---|---|---|---|
| Next FDCR role invocation | Sequential code schedule; transcript tail rule | Last twelve role turns plus failure metadata and static role policy; no token budget | Model advisory context; wired delivery, unobserved semantic dependence. [RT-RTE-failure-review](runtime.md#rt-rte-failure-review). |
| Resumed FDCR / completed review caller | Explicit existing checkpoint path; hash/model equality and status/index | Running state supplies index/transcript, then ordinary sliced context; completed state supplies stored spec/transcript directly | Symbolic index/status directly controls skipped calls; spec remains advisory at editor. [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery). |
| Next-round collector and later executor | Trainer acceptance, then next round / explicit inference invocation | Live retained harness; contents and task context opaque outside synthetic revision example | Program argument with consumer-defined behavioral force, wired; no observed real activation. [RT-BAP-retained-harness](runtime.md#rt-bap-retained-harness). |
| Artifact API caller and test comparison | Explicit path(s)/parent list; optional scope; first occurrence per ID | Loaded artifact or full deduplicated skill units, no relevance ranking or content budget | Structural API delivery only; no task-model consumption. [RT-RTE-artifact-utilities](runtime.md#rt-rte-artifact-utilities), [MEM-ABS-skill-injection](#mem-abs-skill-injection). |
| Caller inspecting outputs | Return objects or explicit JSONL write | Round audit tuple; task outcomes/errors; usage summaries | Audit/output capability, not an automatic adaptation selector. [MEM-OBJ-round-record](#mem-obj-round-record), [MEM-OBJ-inference-record](#mem-obj-inference-record). |

The role schedule automatically supplies accumulated transcript to fresh requests, but it is part of an explicitly invoked review, not unsolicited external memory retrieval. Source file loaders require explicit paths. Static role prompts are working-context policy, not use-derived read-back. `format_update_spec` produces an instruction display for a caller without establishing a later coding-agent route. Plain stores and potential external integrations remain capabilities until a concrete later consumer is established.

## Integration issues

- **No correction to supplied facts is required.** Direct reads support the runtime's distinction between retained harness, cached review and separate artifact APIs. No newly declared record duplicates a supplied referent: trajectory, transcript, checkpoint, skill/envelope, round audit and inference outcome objects fill previously undeclared material parts; existing routes and spec/harness objects receive annotations instead. [MEM-OBJ-checkpoint](#mem-obj-checkpoint) contains retained outputs used by [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery), rather than replacing that route.
- **Checkpoint freshness remains narrower than editor evidence.** Hashing formatted metadata omits messages/task content and several failure fields. Matching cached review can therefore accompany changed editor inputs. This prevents treating equality as a full evidence/policy identity guarantee ([MEM-OBJ-trajectories](#mem-obj-trajectories), [MEM-OBJ-checkpoint](#mem-obj-checkpoint), [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery)).
- **Rejection does not withdraw the retained proposal.** Trainer rejection records a decision but does not update/delete the completed FDCR file. A future same-key invocation can recover its advice. This bounds rollback claims and separates advisory retention from harness admission ([MEM-OBJ-round-record](#mem-obj-round-record), [MEM-OBJ-checkpoint](#mem-obj-checkpoint), [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission)).
- **Real harness form, lineage and changed behavior remain unresolved.** The API deliberately accepts arbitrary payloads. Adapter code is unavailable; quickstart uses predetermined revision rules and ignores the spec. This prevents asserting real trace learning, deep freezing, or content-responsive improvement, without erasing the wired retained-reference path ([RT-OBJ-frozen-harness](runtime.md#rt-obj-frozen-harness), [RT-BAP-retained-harness](runtime.md#rt-bap-retained-harness)).
- **Skill trust and downstream use remain unresolved.** Required fields/default source labels do not verify trace origins, rationale retention or benefit. Merge does not automatically construct complete immediate-parent lineage; first-ID behavior can suppress a new revision. No included task-agent reader establishes skill authority ([MEM-OBJ-evolved-skill](#mem-obj-evolved-skill), [MEM-OBJ-skill-artifact](#mem-obj-skill-artifact), [RT-RTE-artifact-utilities](runtime.md#rt-rte-artifact-utilities), [MEM-ABS-skill-injection](#mem-abs-skill-injection)).
- **Outcome persistence is not feedback wiring.** Inference JSONL lacks the result-object reward schema consumed by extraction. A missing external converter prevents tracing later learning from these outcomes; outputs may also lose opaque payload structure during encoding ([MEM-OBJ-inference-record](#mem-obj-inference-record), [MEM-OBJ-trajectories](#mem-obj-trajectories), [RT-RTE-harness-inference](runtime.md#rt-rte-harness-inference)).

## Limitations and checks

The source checkout HEAD was rechecked against cf93866d545b0974dbb0bc83b39c31fbbdeeecb8; `git status --short` returned no changes. Canonical repository identity and run ID were rechecked against the supplied boundary and prompt. Supplied contracts govern this report; no target code, tests, examples or provider calls were executed. Source quotes establish occurrence and implementation/design, not operation. External task/runtime state, model weights, editor semantics, real score reliability, deployed lifecycle controls and benefits remain uninspected. The scope of every absence is the inspected shipped code, not arbitrary callbacks.

Deterministic validation: `commonplace-run validate-output` on the supplied prompt passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This is a content check, not analytical acceptance, complete invocation-residue checking or evidence of successful operation.

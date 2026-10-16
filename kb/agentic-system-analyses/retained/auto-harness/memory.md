---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "auto-harness memory: diagnostic traces, requested learnings, executable revisions and retained evaluation controls."
run-id: AAS-2026-10-15-auto-harness-92303e444cb2-01
source-identity: https://github.com/neosigmaai/auto-harness
reviewed-boundary: "52360dbbeb8cea8886d90778e634a145c51da735"
---

# auto-harness memory report

## Boundary and evidence

The subject is the shipped improvement plane, not its external coding-agent runtime. Memory scope includes diagnostic retention, requested learning notes, candidate revisions, score/suite/split state, and working-context controls in all three task adapters. Static program and candidate instructions matter as delivery machinery, but their initial installation is not accumulated memory. Candidate edits can become retained behavior-determining material on later imports. Ordinary accumulating task messages are working state, not automatically cross-invocation memory.

All findings use SRC-1 at the reviewed revision. Direct reads covered `program_templates/base.md`, `prepare.py` initialization/template/split code, `gating.py` loaders and gate, `benchmark.py` Terminal parsing/copy/prune, BIRD trace extraction and CLI persistence, `agent/templates/terminal_bench.py`, and `agent/helpers/bird_interact/bird_adk_runtime.py` event/session handling. Supplied runtime findings cover remaining dispatch, tau implementation, BIRD callback registration, dependency contracts and baseline selection; the coverage table distinguishes these. No new source is introduced. Evidence is implementation or doctrine/design, not an observed run. HEAD and clean working-tree checks matched the supplied boundary.

| Entry point / operation | Source paths and inspection basis | Covering records / limit |
|---|---|---|
| Prepare workspace, select templates and initialize baseline/splits | Direct `prepare.py`; baseline timeout filtering supplied by runtime | [RT-RTE-prepare-baseline](runtime.md#rt-rte-prepare-baseline), [MEM-OBJ-task-split](#mem-obj-task-split), preparation annotation |
| CLI result write and later promotion seed load | Direct `benchmark.py`, `gating.py` | [MEM-OBJ-train-results](#mem-obj-train-results), [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission) |
| Suite container and membership promotion | Direct `prepare.py` initialization and `gating.py` load/check/promotion | [MEM-OBJ-suite](#mem-obj-suite), [MEM-OBJ-suite-tasks](#mem-obj-suite-tasks); post-check admission changes future task selection |
| Suite threshold initialization and consumption | Direct `prepare.py` and `gating.py` | [MEM-OBJ-suite-threshold](#mem-obj-suite-threshold); configuration authorship unresolved; existing suite preserves threshold |
| Suite diagnostic overwrite and promotion-time merge | Direct `gating.py` | [MEM-OBJ-suite-last-results](#mem-obj-suite-last-results); pre-admission persistence is not acceptance; no inspected diagnostic consumer beyond merge/serialization |
| Score history append/reload | Direct `gating.py`; recorder behavior supplied | [MEM-OBJ-results](#mem-obj-results), [RT-RTE-iteration-record](runtime.md#rt-rte-iteration-record) |
| Terminal trace retention / cleanup / model context | Direct `benchmark.py`, `agent/templates/terminal_bench.py` | [MEM-OBJ-traces](#mem-obj-traces), [MEM-RTE-trace-retention](#mem-rte-trace-retention), Terminal annotation |
| BIRD session initialization, reset, event serialization, train trace extraction | Direct `agent/helpers/bird_interact/bird_adk_runtime.py`, `benchmark.py`; service lifecycle and candidate callbacks supplied | [RT-RTE-bird-session](runtime.md#rt-rte-bird-session), BIRD annotation, trace records; external ADK assembly and callback behavior remain uninspected |
| Tau factory and next-message API | Supplied `benchmark.py`, `agent/templates/tau_bench.py` findings | [RT-RTE-tau-task](runtime.md#rt-rte-tau-task); external trace retention has no inspected local route |
| Failure diagnosis, code editing, learnings, revert, commit | Direct `program_templates/base.md`; runtime import paths supplied | [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision), [MEM-OBJ-learnings](#mem-obj-learnings), revision annotation |
| Program delivery / task instruction delivery | Direct preparation/Terminal reads plus supplied runtime | [RT-BAP-program-coder](runtime.md#rt-bap-program-coder), [RT-BAP-candidate-runtime](runtime.md#rt-bap-candidate-runtime); delivery is not compliance |
| Model/provider and external host memory | Supplied runtime model components and boundary exclusions | [RT-CMP-candidate-model](runtime.md#rt-cmp-candidate-model), [RT-CMP-coding-model](runtime.md#rt-cmp-coding-model); no provider-state, host-compaction or actual coding-agent context conclusion |

Datasets, actual workspace contents, run traces and learned revisions were not supplied. External tau2, Harbor, ADK, BIRD callbacks and model services are not frozen implementations. These limits prevent claims of actual note reuse, full context retention, reliable verifier truth, effective access restrictions, learning benefit or causal improvement. An available source range not read directly is not an access gap.

## Core ideas

1. Retained state has different authorities. Traces are diagnostic evidence interpreted by the coding agent; learnings are requested natural-language memory; Python revisions execute; suite IDs and score history drive fixed gate predicates. Treating these as one knowledge store hides their different admission controls and failure modes ([MEM-OBJ-traces](#mem-obj-traces), [MEM-OBJ-learnings](#mem-obj-learnings), [RT-BAP-candidate-runtime](runtime.md#rt-bap-candidate-runtime), [RT-BAP-history-gate](runtime.md#rt-bap-history-gate)).
2. The clearest implemented experience-to-later-control transformations are suite promotion and reward-stratified split generation. They retain task membership rather than explanations. Model-authored generalizations and candidate edits are afforded/requested by the outer program, not demonstrated by retained run artifacts ([RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission), [MEM-OBJ-task-split](#mem-obj-task-split), [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision)).
3. Context filtering and trace fidelity are coupled in Terminal: the trace saves already-truncated messages. BIRD diagnostic previews instead serialize events outside the inspected model-context assembly. Neither label “trace” proves a complete original execution transcript ([MEM-OBJ-traces](#mem-obj-traces), task annotations).
4. Files persist, but persistence alone supplies neither automatic read-back nor trustworthy provenance. The learning log has no wired loader here. Gate loaders are wired, but accept local data without authenticating its experiment origin ([MEM-OBJ-learnings](#mem-obj-learnings), [MEM-OBJ-train-results](#mem-obj-train-results), [MEM-OBJ-results](#mem-obj-results)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-learnings
Label: Learnings log

Source-native identity: `workspace/learnings.md`. Storage: local Markdown, initialized if missing by `prepare.py`; existing content is preserved. Form: natural language. Lineage: coding-agent accounts of attempted changes, outcomes, patterns and requests, under the program. Authorship/admission is assigned to the external coding agent, not a per-entry human approval stage; actual permissions and entries are uninspected. Physical initialization is deterministic, not substantive authorship. Its proposed consumer is the coding agent across iterations; the program calls it memory but supplies no explicit read command, selector, injected budget or loader. Reasons can be retained through the requested “what changed” and “what worked / didn't work” fields; their actual presence and later use are unobserved. It is distinct from the executable candidate and program objects; closest supplied route is [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision), which mentions but does not declare this file. Evidence: SRC-1, `prepare.py`, `program_templates/base.md`.

> After every iteration — gate passed or failed — append to `workspace/learnings.md`:
> --- `program_templates/base.md`

> 4. **Always update `learnings.md`** — even on failure; the log is your memory
> --- `program_templates/base.md`

#### MEM-OBJ-train-results
Label: Last benchmark result mapping

Source-native identity: `workspace/train_results.json`. Storage: overwritten local JSON. Form: symbolic task-ID/reward mapping, with split and timestamp metadata. Lineage: CLI runner results, or initially empty state from preparation. Consumer: gate promotion chooses prior failing/non-suite task IDs from `results`; it does not use `split` or timestamp to verify provenance. This is derived evaluation data, not raw dialogue or a formulated explanation. No per-content human approval is coded. Closest supplied records are [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission) and [RT-BAP-history-gate](runtime.md#rt-bap-history-gate); this is their retained input object, not another route. Evidence: SRC-1, `benchmark.py`, `gating.py`, `prepare.py`.

> return data.get("results", {})
> --- `gating.py`

The filename does not enforce train lineage: the CLI writes it after arbitrary requested splits, as already established with passages and consequences in [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission).

#### MEM-OBJ-suite
Label: Regression suite

Source-native identity: `workspace/suite.json`. Storage: local JSON file. Form: symbolic container holding separately operative membership, threshold and diagnostic fields. Preparation initializes the container if absent; `load_suite` decodes it and `save_suite` rewrites the whole file. Shared physical persistence does not give its parts one admission state. Their lineage, consumers, authority and invalidation are assessed separately in [MEM-OBJ-suite-tasks](#mem-obj-suite-tasks), [MEM-OBJ-suite-threshold](#mem-obj-suite-threshold) and [MEM-OBJ-suite-last-results](#mem-obj-suite-last-results). No explanations of task fixes are stored. Closest supplied route is [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission), not an object counterpart; the container remains valid alongside its parts. Evidence: SRC-1, `prepare.py`, `gating.py`.

> json.dump({"tasks": [], "threshold": cfg.get("threshold", 0.8), "last_results": {}}, f, indent=2)
> --- `prepare.py`

#### MEM-OBJ-suite-tasks
Label: Suite task membership

Part of: [MEM-OBJ-suite](#mem-obj-suite)

Source-native identity: `workspace/suite.json` field `tasks`. Storage: JSON array in the local suite file. Representational form: symbolic task IDs. Lineage/admission: preparation initializes an empty array when the container is missing; subsequent promotion is deterministic software admission after both suite and full-test checks pass. The gate selects prior failing/non-suite result IDs, reruns them and unions returned non-`None` rewards of at least 0.5 with existing membership. The external benchmark supplies rewards; the fixed gate predicate decides promotion, without coded per-task human approval. Generic caller/configuration authorship remains unresolved. Consumer/authority: a later `run_gate` uses the array to request train reruns and fixes the suite pass-rate denominator to its length. The automatic experience-derived result retains selection IDs, not raw traces, rewards or reasons. Persistence/invalidation: membership grows on this path; no local demotion or automatic rollback is implemented, and failed checks return before promotion. Manual replacement/deletion is not prevented. This part resolves the selection content within the container; it is not a duplicate of the broader [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission), which supplies the promotion quotations and result-provenance limits. Evidence: SRC-1, `prepare.py`, `gating.py`; implementation is wired, operation uninspected.

> task_ids: list[str] = suite.get("tasks", [])
> --- `gating.py`

#### MEM-OBJ-suite-threshold
Label: Suite acceptance threshold

Part of: [MEM-OBJ-suite](#mem-obj-suite)

Source-native identity: `workspace/suite.json` field `threshold`. Storage: numeric JSON field in the local suite file. Representational form: symbolic decision parameter, not distributed model state. Lineage/admission: preparation takes `cfg.get("threshold", 0.8)` only when creating the missing suite. Existing suite initialization is skipped; gate loading/field lookup defaults to 0.8 when appropriate. Configuration authorship and any human approval are unresolved; deterministic initialization is not per-content human approval. Neither suite reruns nor promotion learn or retune this value. Consumer/authority: `run_gate` compares requested-suite pass rate against the threshold; empty membership skips that check. The parameter is not an observed reward or a reason for accepting individual tasks. Persistence/invalidation: subsequent full-file saves carry it forward; rerunning preparation with a changed configuration does not replace an existing suite's threshold. No automatic expiry, tuning or rollback path is present in these inspected functions. This is the fixed comparison parameter within the container, distinct from promoted IDs and diagnostic outcomes; closest supplied route is [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission). Evidence: SRC-1, `prepare.py`, `gating.py`; initialization and comparison are wired, actual operation uninspected.

> threshold: float = suite.get("threshold", 0.8)
> --- `gating.py`

> suite_passed = pass_rate >= threshold
> --- `gating.py`

#### MEM-OBJ-suite-last-results
Label: Suite diagnostic results

Part of: [MEM-OBJ-suite](#mem-obj-suite)

Source-native identity: `workspace/suite.json` field `last_results`. Storage: local JSON task-ID/reward-or-null mapping. Representational form: symbolic derived outcome data, not dialogue or explanatory theory. Lineage/admission: preparation initializes an empty mapping. For a nonempty suite, gate reruns its task IDs, maps missing results to null, overwrites this field and saves the file before deciding suite acceptance or running the full-test check. These diagnostic writes survive a later gate rejection; they do not certify candidate acceptance. After successful checks, if promotion finds at least one newly fixed task, the code merges the entire `recheck` mapping, including nonpassing rechecks, and saves again. No new pass means that merge is not saved. Admission is deterministic software serialization, not per-result human approval; benchmark reward validity remains external. Consumer/authority: later gate calls load the container, but selection and acceptance use `tasks`, `threshold` and fresh runner results, not this historical diagnostic mapping. The inspected gate uses the mapping for merge/serialization; no separate model injection or diagnostic read-back consumer is established. Persistence/invalidation: the next nonempty-suite rerun replaces the whole mapping, potentially removing previously merged nonmember entries; empty-suite skips can leave old diagnostics untouched. There is no transactional rollback on failed checks. This is the diagnostic part, not a duplicate of the wider [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission). Evidence: SRC-1, `prepare.py`, `gating.py`; writes are wired, actual later diagnostic use uninspected.

> suite["last_results"] = {tid: results.get(tid) for tid in task_ids}
> --- `gating.py`

> suite["last_results"].update(recheck)
> --- `gating.py`

#### MEM-OBJ-results
Label: Iteration score history

Source-native identity: `workspace/results.tsv`. Storage: local append-written TSV, not enforced immutable storage. Form: symbolic iteration, score, commit label, suite counts and timestamp. Lineage: preparation writes a baseline row; recorder accepts caller numbers and appends after its file guard. Consumer: gate selects the maximum nonempty score as the later acceptance floor. Commit and timestamp are access/accounting metadata, not the evaluated candidate or authenticated evaluation evidence. No rationale is stored in these fields. Caller identity and any human approval of numbers are unresolved. Closest supplied records are [RT-RTE-iteration-record](runtime.md#rt-rte-iteration-record) and [RT-BAP-history-gate](runtime.md#rt-bap-history-gate); this declares their retained object, not duplicate execution. Evidence: SRC-1, `gating.py`, and supplied recorder findings in `record.py`.

> return max(scores) if scores else None
> --- `gating.py`

#### MEM-OBJ-task-split
Label: Baseline-derived task splits

Source-native identities: `tbench_data/task_split.json`, `bird_data/task_split.json`. Storage: local JSON. Form: symbolic train/test ID arrays plus creation/seed/task-count metadata. Lineage: baseline rewards determine pass/fail strata, seed 42 shuffles sorted IDs, each stratum is partitioned 70/30, then only membership and metadata persist. The split does not retain rewards or explanatory reasons. Consumer: subsequent benchmark/gate task selection, unless explicit IDs bypass the split. Initialization trigger is preparation's first applicable baseline; the code performs selection without per-task human approval. Split reuse/removal and baseline `None` exclusion are established in [RT-RTE-prepare-baseline](runtime.md#rt-rte-prepare-baseline). This object is not the suite: its provenance, replacement path and role differ. No supplied object counterpart. Evidence: SRC-1, `prepare.py`, `benchmark.py` via the supplied preparation/task routes.

> def generate_terminal_bench_split(results: dict[str, float], seed: int = 42) -> None:
>     """Generate train/test split from baseline results. 70/30 stratified by pass/fail."""
> --- `prepare.py`

#### MEM-OBJ-traces
Label: Latest and first-seen diagnostic traces

Source-native identities: `workspace/traces/latest/<task>/trace.json`, adjacent `result.json`, and corresponding `workspace/traces/baseline/` directories. Storage: local JSON files. Form is mixed by consumer: dialogue/tool text is natural-language diagnostic evidence to the coding agent; role/tool/event structures and reward fields are symbolic serialization. The adjacent result mapping is not identical to dialogue. Lineage: Terminal copies candidate message traces and Harbor results; BIRD extracts dialogue history, tool trajectory, ADK events and final response from external result items and separately saves the full item. BIRD payload completeness is external; serialized ADK text/response parts may already be previews. Terminal messages already omit long-output middles. These are retained traces/selected records, not automatically learned generalized rules. First-seen copies preserve evidence by convention; latest copies are mutable. Consumer: the program directs the outer coding agent to inspect failing train traces; no automatic prompt injection or verified read is shown. Distinct from supplied code/instruction objects; overlaps task routes only as their output, principally [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task), [RT-RTE-bird-session](runtime.md#rt-rte-bird-session). Evidence: SRC-1, `benchmark.py`, `agent/templates/terminal_bench.py`, `agent/helpers/bird_interact/bird_adk_runtime.py`.

> "dialogue_history": item.get("dialogue_history", []),
> "tool_trajectory": item.get("tool_trajectory", []),
> "adk_events": item.get("adk_events", []),
> "final_response": item.get("final_response", ""),
> --- `benchmark.py`

### Routes

#### MEM-RTE-trace-retention
Label: Train trace retention

Endpoints: completed Terminal train job/BIRD train results → code-directed copy or field extraction → latest and first-seen JSON → requested later coding-agent diagnosis. Owner: deterministic adapters for retention, external coding agent for choosing and interpreting files. State effects: file creation/overwrite and Terminal old-job deletion, not automatic candidate revision. This route isolates the retention stage shared across two supplied task routes rather than duplicating either whole task loop. Evidence: SRC-1, `benchmark.py`, `program_templates/base.md`; related routes [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task), [RT-RTE-bird-session](runtime.md#rt-rte-bird-session), [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision).

> if not os.path.exists(base_dest):
> --- `benchmark.py:630-662`

- Immediate return: Latest per-task trace/result files; a first-seen baseline directory if absent, plus printed copy status.
- Later read-back: Program requests failure-directed inspection of train traces by the coding agent; no local automatic loader or exercised read is supplied.
- Delegated visibility: Coding agent can receive retained selected dialogue/events/results; actual filesystem access and read choices are external. Task models do not automatically receive these historical copies.
- Selection predicate: Train split for adapter copying; Terminal iterates trial directories, BIRD selects items with an instance/task ID. Later foreground diagnosis targets failing train tasks by policy, without a wired retrieval budget.
- Invalidation or expiry: Current items overwrite latest files; missing items are not deleted from latest. First-seen directory existence suppresses baseline recopy. Terminal deletes older raw job directories but keeps the selected current job. External/manual deletion remains possible.
- Activation or effect: File retention is wired; diagnostic interpretation and evidence-responsive code changes are afforded by the program, not observed.
- Evidence limits: Copies can be stale or partial, traces can be filtered, and no actual retained files or readers were supplied. Copy completion does not authenticate benchmark outcomes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-prepare-baseline](runtime.md#rt-rte-prepare-baseline)

Memory lineage: initialization preserves preexisting workspace files, but candidate/program copying is unconditional before the prior-history baseline skip. Retained history can therefore outlive the candidate it described. Baseline-to-split is an automatic experience-derived selection update, not a text summary or weight update. The durable result is [MEM-OBJ-task-split](#mem-obj-task-split), read by later runner selection; no reasons beyond IDs/metadata reach that consumer. Evidence: SRC-1, `prepare.py`, supplied route's baseline skip and timeout exclusion account.

#### On [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task)

Working context: each invocation constructs a fresh system/task list, keeping other tasks' histories out. Code filters each bash result before appending and later saving messages; it keeps first/last halves at the 8000-character content limit plus the omission marker. The remaining message list accumulates without an inspected rolling summary or token-budget selector. Tool output is lower-trust task evidence, not an authoritative system instruction merely because it enters a tool message. A fresh task frame resembles an isolated call frame, but the escaping reward and saved traces are explicit by-value products, not pointers back into a model window. Environment files may permit deliberate bash rereads; no automatic reload pointer for removed middle output is emitted. The static instruction is always supplied; historical trace copies are not automatically reintroduced. Evidence: SRC-1, `agent/templates/terminal_bench.py`; supplied route for constants and model limit.

> output = _truncate(output)
> --- `agent/templates/terminal_bench.py`

> json.dump(messages, f, indent=2, default=str)
> --- `agent/templates/terminal_bench.py`

#### On [RT-RTE-tau-task](runtime.md#rt-rte-tau-task)

Working context and storage: mutable `HarnessState` holds per-task messages; the supplied route shows policy prepended to the full current history. No local transform creates a separate summary in that inspected path. External state lifecycle and any trace persistence remain uninspected, preventing a cross-task retention or complete external context-control conclusion. Read-back of benchmark outcome mappings belongs to the CLI/gate, not the ordinary message accumulation. Evidence: SRC-1, `agent/templates/tau_bench.py`, `benchmark.py`, through the supplied route and its verbatim model-call passage.

#### On [RT-RTE-bird-session](runtime.md#rt-rte-bird-session)

Storage and context: caller-provided state enters an ADK in-memory session, referenced by mode/task. Generic HTTP caller identity leaves human versus software initialization unresolved. Subsequent code transformations are known: c-interact appends a phase-reset event; turn handling appends serialized diagnostic events. Reset changes the local reference, not a proven deletion of all backend state. No durable restart checkpoint is wired in the included wrapper. Actual model-visible state selection and callback-written tool trajectory are external; returning `state` does not prove every state field is injected into the model.

Logged user messages use 1200-character previews; event text/function responses use a default 4000-character preview. Function-call args remain structured rather than previewed. These diagnostic summaries are not demonstrated compaction of the actual ADK model window; opaque session content must not be equated with its readable display. Later turn/session use is ordinary task state unless a transformed retained part is shown reaching a later model call. Outer diagnosis can receive copied events through [MEM-RTE-trace-retention](#mem-rte-trace-retention), with these fidelity limits. Evidence: SRC-1, `agent/helpers/bird_interact/bird_adk_runtime.py`, `benchmark.py`.

> "message": self._preview(message, limit=1200),
> --- `agent/helpers/bird_interact/bird_adk_runtime.py`

> return text[:limit] + "...<truncated>"
> --- `agent/helpers/bird_interact/bird_adk_runtime.py`

#### On [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision)

The requested raw-to-derived chain is train traces/outcomes → coding-agent diagnosis → natural-language learnings and executable/instruction edits → later coding-agent work and benchmark imports. Acquisition and semantic curation are distinct: deterministic copies do not themselves derive a hypothesis; the external coding agent is assigned that work. Code can retain a behavioral rule without its historical justification, while the learning note can retain reasons separately. No inspected import path reads those reasons. The program asks notes even after rejected iterations, preserving potential failure evidence beyond code rollback. There is no automatic learnings rollback or deletion rule in the supplied procedure. Evidence: SRC-1, `program_templates/base.md`, `prepare.py`; [MEM-OBJ-learnings](#mem-obj-learnings), [RT-OBJ-agent-code](runtime.md#rt-obj-agent-code).

## Write side

Admission differs by surface. Preparation installs templates and initializes missing workspace files by software rule after generic caller invocation; caller identity does not establish per-content human approval. The coding agent is assigned authorship of candidate edits and learning entries. Gate acceptance is computational, while revert/commit remain instructions to that external agent. The recorder admits caller-supplied scores subject to a path guard rather than a successful-gate certificate ([RT-RTE-prepare-baseline](runtime.md#rt-rte-prepare-baseline), [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision), [RT-RTE-iteration-record](runtime.md#rt-rte-iteration-record)).

Automatic transformations are: CLI outcome serialization, train trace selection/extraction, Terminal output filtering, BIRD diagnostic previewing, suite promotion and baseline-stratified split generation. Only the last two automatically turn experience into durable future selection controls; raw trace retention alone is not a learned instruction update. Suite promotion requires a real non-`None` passing recheck after gate success, whereas suite last-results writes precede final acceptance. None of these retain explanatory reasons for task membership. Opaque external event and model processing does not justify an additional claimed summary/checkpoint route ([MEM-OBJ-suite-tasks](#mem-obj-suite-tasks), [MEM-OBJ-suite-last-results](#mem-obj-suite-last-results), [MEM-OBJ-task-split](#mem-obj-task-split), [MEM-RTE-trace-retention](#mem-rte-trace-retention), task annotations). The suite threshold is initialized from configuration and carried forward, not derived from rerun experience ([MEM-OBJ-suite-threshold](#mem-obj-suite-threshold)).

Rejection/withdrawal is asymmetric. Failed candidate gates request a Python revert but do not automatically undo files. Learnings are requested even on failure; score rows are prescribed only after success but can be appended without a gate certificate. Suite membership has no local demotion path. Raw Terminal jobs are pruned, latest trace files overwrite only encountered items, and first-seen copies are preserved by directory existence. Consequently, evidence withdrawal, code rejection and historical-state invalidation are not one transaction (SRC-1, `program_templates/base.md`, `gating.py`, `benchmark.py`; records above).

## Read-back

- **Deterministic pull:** gate explicitly loads suite IDs/threshold, prior maximum score and failing-task seeds. Selection is by fixed predicates, without model retrieval or semantic ranking; delivery is JSON/TSV decoding into gate/runner calls. These inputs have decision authority but not authenticated truth ([RT-BAP-history-gate](runtime.md#rt-bap-history-gate), [MEM-OBJ-train-results](#mem-obj-train-results), [MEM-OBJ-suite-tasks](#mem-obj-suite-tasks), [MEM-OBJ-suite-threshold](#mem-obj-suite-threshold), [MEM-OBJ-results](#mem-obj-results)). Loading the suite container also loads diagnostics, but no historical-diagnostic decision dependency is established in the inspected gate ([MEM-OBJ-suite-last-results](#mem-obj-suite-last-results)).
- **Runner selection:** retained train/test arrays target subsequent benchmark calls; explicit task IDs form an alternate admission/read path that can bypass split lookup. This is task selection, not task-specific retrieval of retained prose ([MEM-OBJ-task-split](#mem-obj-task-split), supplied task routes).
- **Requested foreground reads:** program-directed failure diagnosis can select trace files. No automatic unsolicited trace push, read budget, freshness check or actual file read is demonstrated. Learning-log read-back is thinner still: the log is called memory, without an implemented loader or explicit per-round read instruction ([MEM-RTE-trace-retention](#mem-rte-trace-retention), [MEM-OBJ-learnings](#mem-obj-learnings)).
- **Executable adoption:** revised candidate Python reaches task runtime through imports/builders; its natural-language constants reach task models. Python has implementation authority; prose requests behavior. Cached BIRD runners and tau registration qualify hot-replacement expectations. Historical reasons are not an input to these consumers ([RT-BAP-candidate-runtime](runtime.md#rt-bap-candidate-runtime), revision annotation).
- **Working-state reuse:** Terminal/tau task histories and BIRD session state follow their task lifecycles. They must not be conflated with a demonstrated cross-task knowledge store. Filtering and context isolation are still real working-context controls even without a learned result (task annotations).

## Integration issues

1. **Freshness qualification, not a route replacement:** runtime describes latest traces as most-recent overwritten files. Source copying only touches encountered task items; it does not clear the directory, and Terminal leaves old trace files when a new trace is absent. Thus “latest” is per-file update behavior, not a complete current-run snapshot. First-seen baseline may also be incomplete because directory existence suppresses later filling. This limits diagnostic comparisons and qualifies [RT-RTE-terminal-task](runtime.md#rt-rte-terminal-task), [RT-RTE-bird-session](runtime.md#rt-rte-bird-session), [MEM-RTE-trace-retention](#mem-rte-trace-retention). Evidence: SRC-1, `benchmark.py` inspected copy loops.
2. **No duplicate referent intended:** new objects declare retained inputs/outputs mentioned but not separately declared in runtime. [MEM-RTE-trace-retention](#mem-rte-trace-retention) spans the retention stages of both task routes, not all of either; neither is its unique container. No supplied record is superseded. The candidate, program and instruction referents remain runtime-owned, receiving annotations rather than new object IDs.
3. **Unresolved readers and opaque processing:** actual learning-note reads, diagnostic use, model-responsive code changes, external tau trace retention, BIRD callback state transformations and ADK model-context selection remain uninspected. These prevent completed trace-to-learning activation or complete transcript claims; they do not erase the wired file/gate paths. Concerned records: [MEM-OBJ-learnings](#mem-obj-learnings), [MEM-OBJ-traces](#mem-obj-traces), [RT-RTE-candidate-revision](runtime.md#rt-rte-candidate-revision), [RT-RTE-tau-task](runtime.md#rt-rte-tau-task), [RT-RTE-bird-session](runtime.md#rt-rte-bird-session). Evidence: SRC-1 paths in their records and boundary external-source limits.
4. **No additional factual correction to supplied provenance findings:** split metadata is ignored by the promotion loader and score append lacks evaluation authentication, already correctly bounded in [RT-RTE-gate-admission](runtime.md#rt-rte-gate-admission) and [RT-RTE-iteration-record](runtime.md#rt-rte-iteration-record). New objects make their distinct later authority explicit rather than treating those weaknesses as absent retention.

5. **Suite part correction:** [MEM-OBJ-suite](#mem-obj-suite) remains a valid container, now resolved into [MEM-OBJ-suite-tasks](#mem-obj-suite-tasks), [MEM-OBJ-suite-threshold](#mem-obj-suite-threshold) and [MEM-OBJ-suite-last-results](#mem-obj-suite-last-results). Direct reinspection of SRC-1 `prepare.py` initialization and `gating.py` loading, checking and promotion confirms different admission timing and authority. Diagnostic writes can survive rejection, membership promotion follows successful checks, and the threshold is carried forward rather than tuned. No part supersedes the container or duplicates the supplied route. This repairs the refusal's missing inventory without weakening pre-admission persistence or post-check promotion.

## Limitations and checks

No target execution, dependency installation, fixtures, provider calls or external-source acquisition was performed. Source identity was rechecked by HEAD and clean status against the supplied full revision. Method identity is the supplied job, member type, worker rules and records contract, read completely; this member does not alter engine-owned method or run metadata.

The evidence establishes retained-file and context-control mechanisms, not actual note consumption, deployed access restrictions, full external context assembly, exercised learning or causal benefit. The stronger “full conversation” and “latest” labels were challenged against actual filtering/copy behavior rather than accepted as completeness guarantees. No warranted global absence claim is declared.

Validation: deterministic output validation passed; it checks structure, identity and quotation occurrence, not analytical correctness or acceptance.

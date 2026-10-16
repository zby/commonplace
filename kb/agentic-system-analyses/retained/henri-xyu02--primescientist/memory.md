---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "PrimeScientist memory: retained experiment trees, diagnostic reductions, workspace inheritance, session continuation and conditional cross-task insight delivery."
run-id: AAS-2026-10-14-primescientist-f880686cf98a-01
source-identity: "https://github.com/henri-xyu02/PrimeScientist"
reviewed-boundary: "29971beac6f4f4b41309b1326762e1b83ceece98"
---

# PrimeScientist memory report

## Boundary and evidence

The subject is the shipped PrimeScientist workflow at the boundary's SRC-1 revision, not Codex's internal memory implementation. Included are tree replay, retained plans and proposal reasons, packets/statistics, logs and diagnostic reductions, inherited code, baseline history, reflector continuation, adapter staging and FIRE-Bench insight loading. External model weights, session payloads, native-skill discovery and host compaction remain opaque. No target execution or supplied run trace establishes actual model use or benefit.

Direct source inspection covered `search/tree.py`; `search/reflector.py` proposal templates, session invocation and public memory operations; `run_search.py` bootstrap, pruning, artifact movement, execution and initialization; `run_vanilla.py` replay, formatting and keep/revert; `benchmarks/utils.py` skill writing; adapter staging and AutoLab workspace creation; and FIRE-Bench fresh/inherited Codex and OpenHands context loaders. All are implementation evidence in SRC-1; prompt text additionally establishes requested behavior, not compliance. The source register remains [boundary](boundary.md#source-register). The supplied runtime provides the remaining dispatch, evaluator and execution-envelope findings explicitly marked below.

| Entry point or memory operation | SRC-1 path | Coverage and conclusion limits |
|---|---|---|
| Search CLI, load/init, force-init, node execution | `run_search.py`, `search/tree.py` | Direct read plus supplied [RT-RTE-search-execution](runtime.md#rt-rte-search-execution); persisted files influence later traversal, not evidence of successful research. |
| Reflect/init public operations, proposals and raw-directory admission | `search/reflector.py`, `run_search.py` | Direct read; [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission), [MEM-OBJ-prior](#mem-obj-prior), [MEM-OBJ-diff](#mem-obj-diff), [MEM-OBJ-changes](#mem-obj-changes). No semantic validation of requested provenance. |
| Pruning and archive withdrawal | `run_search.py`, `search/tree.py` | Direct read; [MEM-OBJ-pruned-children](#mem-obj-pruned-children). Hidden branches are excluded from normal traversal, not erased. |
| Log reduction and diagnostic reload | `search/reflector.py`, `run_search.py` | Direct read; [MEM-RTE-log-brief](#mem-rte-log-brief). Line budget does not bound total tokens or resumed window. |
| Reflector resume and session bookkeeping | `search/reflector.py` | Direct read; [MEM-RTE-session-resume](#mem-rte-session-resume). Payload and host retention/compaction are uninspected. |
| Worker plan staging/native skill configuration | `benchmarks/utils.py`, `benchmarks/autolab/__init__.py`, `benchmarks/fire_bench/__init__.py`, `benchmarks/fire_bench/agents/codex/run_inherit.py` | Direct read; [RT-BAP-plan-worker](runtime.md#rt-bap-plan-worker). File production is visible; actual native-skill invocation remains external. |
| Fresh/inherited FIRE-Bench and alternate OpenHands | `benchmarks/fire_bench/agents/codex/run.py`, `benchmarks/fire_bench/agents/codex/run_inherit.py`, `benchmarks/fire_bench/agents/openhands/run.py` | Direct context/inheritance reads; dispatch/execution envelope supplied by runtime. [MEM-RTE-insight-delivery](#mem-rte-insight-delivery). |
| Baseline CLI, replay/history, keep/revert | `run_vanilla.py` | Direct read; [RT-RTE-vanilla-retention](runtime.md#rt-rte-vanilla-retention), [MEM-OBJ-history-shown](#mem-obj-history-shown). Resume can omit previously shown conclusion text. |
| Evaluation to durable packet and selection | `run_search.py`, `search/tree.py`; adapter evaluation paths | Direct persistence reads, evaluator behavior supplied by [RT-RTE-score-evaluation](runtime.md#rt-rte-score-evaluation). Per-task oracle correctness and most vendored evaluator internals remain uninspected; metric warrant is not established. |
| Adapter hooks and exposed stage APIs | `benchmarks/base.py`, `benchmarks/registry.py`, shipped adapter overrides | Direct read; stage/prepend/post-init are alternative material delivery operations, not independent human approval. Optional terminal_bench is not shipped; no consumer conclusions for it. |
| Utility services, per-task assets, host/Docker/enroot variants | `benchmarks/` | Runtime's execution findings retained; task utility internals and most task assets not directly inspected here. No exhaustive downstream memory or utility-service claim. External runtime tool registries/hooks are outside frozen source; no internal compaction/tool-policy claim. |

## Core ideas

The main durable memory is an experiment tree, not a retrieval index. Python consumes numeric Q/P/visits and packet existence; the reflector interprets plans, outcome packets and diagnostic artifacts; subsequent workers receive selected plans and sometimes prior workspaces. These are different authority paths. Score-derived selection is operative in code, whereas useful interpretation and better research are unobserved. [RT-BAP-score-selector](runtime.md#rt-bap-score-selector), [RT-BAP-plan-worker](runtime.md#rt-bap-plan-worker).

The workflow preserves unsuccessful experience separately from reusable code. Pruning removes a child from ordinary selection but leaves its artifacts and writes a compact failure record for a later reflector. The baseline similarly retains rejected attempt records while reusing only best-so-far code. Diagnostic briefs and history are automatic trace-fed reductions with later consumers; simply retaining full logs would not establish those paths. [MEM-OBJ-pruned-children](#mem-obj-pruned-children), [MEM-RTE-log-brief](#mem-rte-log-brief), [MEM-OBJ-history-shown](#mem-obj-history-shown).

Requested proposal reasons are durable natural-language material, separate from the numeric prior extracted for selection. FIRE-Bench additionally requests a transformation script, a complete plan and a short change explanation. None is made scientifically trustworthy by its filename. The child bootstrap requires plan existence, not evidence fidelity. [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission), [MEM-OBJ-prior](#mem-obj-prior).

Two qualifications defeat a filesystem-only or strictly bounded-context account. The reflector requests continuation of an external Codex session, and hidden full logs remain reachable. Separately, FIRE-Bench's nominally relevant cross-task insights are loaded wholesale after simple file filters; relevance selection is delegated to the worker, not performed by retrieval code. [MEM-RTE-session-resume](#mem-rte-session-resume), [MEM-RTE-insight-delivery](#mem-rte-insight-delivery).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-prior
Label: Proposal prior and retained reasons

Source-native identity: node `prior.json`. Storage substrate: JSON file. Representational form: symbolic numeric `estimate` consumed by Python, with natural-language hypothesis/rationale/changes/risks interpreted by later reflectors. Lineage: requested reflector authorship from packet/log/workspace observations; actual generated content is unobserved. No counterpart after comparison: [RT-OBJ-stats](runtime.md#rt-obj-stats) stores the admitted number, not the proposal's reasons; [RT-OBJ-skill](runtime.md#rt-obj-skill) is the worker plan, not this metadata. SRC-1, `search/reflector.py`, `run_search.py`.

> b) prior.json with structured, detailed reasoning. This is the durable
> record the NEXT reflector will consult instead of your (now-discarded)
> thinking — so invest your analysis here rather than in stdout:
> --- `search/reflector.py`

Python defaults/clamps the estimate without requiring the reason fields. Later reflection is directed to other nodes' priors as needed; pruning copies the reason fields to its failure digest. Reasons therefore have afforded model-guidance authority, not a schema-enforced evidential warrant. Initialization provenance of manually present proposal directories is unresolved; existing raw directories are admitted without a fresh author call. The fields are requested, not observed authored criticisms.

#### MEM-OBJ-diff
Label: FIRE-Bench plan transformation script

Source-native identity: proposal `diff.py`. Storage substrate: node file and, when available, inherited sandbox's `INHERITED_FROM_PARENT/diff.py`. Representational form: symbolic executable Python; its requested execution produces the child's full natural-language plan. No counterpart after comparison: it is neither [RT-OBJ-skill](runtime.md#rt-obj-skill) nor the retained run workspace [RT-OBJ-sandbox](runtime.md#rt-obj-sandbox); it is a node-side proposed transformation subsequently copied into that workspace. SRC-1, `search/reflector.py`, `benchmarks/fire_bench/agents/codex/run_inherit.py`.

> Do NOT write skill.md directly — only via diff.py.
> --- `search/reflector.py`

This is prompt-directed provenance, not an enforced transformation chain: bootstrap does not require the script or check its output. The reflector may execute it under its own external runtime; the inherited runner copies it for worker inspection, not automatic rerun. No separate semantic admission or rollback exists for the script in the inspected copy path.

#### MEM-OBJ-changes
Label: FIRE-Bench child change explanation

Source-native identity: proposal `changes.md`. Storage substrate: node file, then inherited sandbox `INHERITED_FROM_PARENT/changes.md`. Representational form: natural language. Lineage: reflector-requested explanation of the plan delta, distinct from executable transformation and full plan. No counterpart after comparison: [RT-OBJ-skill](runtime.md#rt-obj-skill) is the full/incremental plan; this is optional explanatory material delivered alongside it. SRC-1, `search/reflector.py`, `benchmarks/fire_bench/agents/codex/run_inherit.py`.

> c) changes.md (< 1 KB) — short prose summary of what changed compared to
> the parent's plan. 3-6 bullet points written FOR the child agent
> --- `search/reflector.py`

The runner checks availability, copies bytes, and prepends an instruction to read this file first. Authority is model-interpreted guidance for a later child invocation. Content accuracy, size and consistency with plan/code are not checked at bootstrap. Requested reasons are more extensive in `prior.json`; this summary need not preserve them.

#### MEM-OBJ-packet
Label: Retained outcome packet

Source-native identity: node or baseline iteration `packet.json`. Storage substrate: filesystem JSON. Representational form: mixed symbolic score/path/decision fields and natural-language diagnostics or conclusions. Lineage: benchmark evaluation plus driver-added bookkeeping, not an unmodified agent trace. Distinct from [RT-OBJ-stats](runtime.md#rt-obj-stats): raw packet score is not aggregate Q. No object counterpart after comparison; the producing route is [RT-RTE-score-evaluation](runtime.md#rt-rte-score-evaluation). SRC-1, `search/tree.py`, `run_search.py`, `run_vanilla.py`.

> def write_packet(self, packet: dict) -> None:
>     (self.path / PACKET_FILE).write_text(json.dumps(packet, indent=2), encoding="utf-8")
> --- `search/tree.py`

Consumers differ: Python uses scores and existence/replay fields; reflectors are pointed to diagnostics and outcome evidence. Saving a packet is automatic, not human content approval. Best-of-n search saves the winning packet/artifacts and other-run costs, not equally detailed node-local diagnostic memory of every attempt. Pruned packets survive but artifact-relative paths can become stale after directory rename; the digest and hidden filesystem remain available independently.

#### MEM-OBJ-log-brief
Label: Agent diagnostic log excerpt

Source-native identity: `log_brief.log`. Storage substrate: node text file. Representational form: retained textual excerpt of execution output, possibly containing source, tool and narrative text; model interpretation supplies diagnostic meaning. Lineage and later consumer: [MEM-RTE-log-brief](#mem-rte-log-brief). No counterpart after comparison: [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission) references this input but does not declare it; it is not the full raw log or a semantic model summary. SRC-1, `search/reflector.py`.

> head_block = lines[:head]
> tail_block = lines[-tail:]
> omitted = len(lines) - head - tail
> --- `search/reflector.py`

#### MEM-OBJ-pruned-children
Label: Failure digest of hidden branches

Source-native identity: parent `pruned_children.md`. Storage substrate: appended Markdown file. Representational form: natural-language reason excerpts and textual numerical verdicts, for reflector interpretation. Lineage: driver composes it from child prior, primary score, parent Q and verifier tail. No counterpart after comparison: this is derived failure memory within [RT-RTE-search-execution](runtime.md#rt-rte-search-execution), not its whole execution referent. SRC-1, `run_search.py`.

> f"  hypothesis : {pr.get('hypothesis', '—')}\n"
> f"  rationale  : {pr.get('rationale',  '—')}\n"
> f"  changes    : {pr.get('changes',    '—')}\n"
> f"  risks      : {pr.get('risks',      '—')}"
> --- `run_search.py`

The code prefers readable prior fields, otherwise at most 800 skill characters, then at most 300 verifier-tail characters. Successful JSON parsing alone sets the prior path's summary as usable even if its fields are missing. Thus reasons can be placeholders; the digest is not necessarily a full causal failure explanation. Pruning is computational admission of failure memory, with no per-entry human approval. Re-expansion asks the reflector to read it first and not repeat approaches; that avoidance is not enforced. Hidden branches remain on disk and normally excluded by `get_children`.

#### MEM-OBJ-reflector-session
Label: Reflector session access metadata

Source-native identity: `reflector_session.json`. Storage substrate: task-root JSON. Representational form: symbolic session identifier and cumulative-token counter. Lineage: parsed Codex stdout plus cost parser. Later consumers: continuation command construction and cost delta calculation. No counterpart after comparison: [RT-CMP-reflector-model](runtime.md#rt-cmp-reflector-model) is the model, not this metadata or its opaque session content. SRC-1, `search/reflector.py`.

> session_id     = state.get("session_id")
> last_cumul     = int(state.get("codex_last_cumulative_tokens", 0))
> --- `search/reflector.py`

The identifier is not the transcript or a readable summary of retained knowledge. Provider/client session content and physical substrate beyond this access file remain uninspected. The counter shapes budget accounting, not semantic retrieval. See [MEM-RTE-session-resume](#mem-rte-session-resume).

#### MEM-OBJ-insights
Label: Cross-task insight files and local copies

Source-native identity: benchmark `insights/*.md`, task-local `insights/`, and node `{task}_insight.md` snapshot. Storage substrate: Markdown files. Representational form: natural language, consumed by reflector/worker interpretation. Lineage: pre-existing external files are copied; init touches the root snapshot and optionally copies a live current-task file. Actual insight authorship, evidence quality and automatic production from completed trials are unresolved. No counterpart after comparison: these files are not [RT-OBJ-skill](runtime.md#rt-obj-skill), although worker staging combines them with it. SRC-1, `search/reflector.py`, `run_search.py`, `benchmarks/fire_bench/agents/codex/run.py`.

> # Create empty insight file for this task — filled by reflector after real runs
> root_node.insight_path.touch()
> --- `search/reflector.py`

This comment does not establish a functioning production loop. File presence suffices for copy/load; no evidence check or human approval is performed by those operations. See [MEM-RTE-insight-delivery](#mem-rte-insight-delivery).

#### MEM-OBJ-history-shown
Label: Baseline history delivered to the worker

Source-native identity: `history_shown.md` and staged history-as-skill. Storage substrate: per-iteration Markdown plus live adapter skill file. Representational form: natural-language guidance with textual score/action fields. Lineage: deterministic formatting of prior packets and in-memory attempt summaries. No counterpart after comparison: this is the history output of [RT-RTE-vanilla-retention](runtime.md#rt-rte-vanilla-retention), not the whole route or [RT-OBJ-skill](runtime.md#rt-obj-skill)'s node plan. SRC-1, `run_vanilla.py`.

> history_md = _format_history(results_tsv, packets)
> benchmark.stage_skill(task, history_md)
> (iter_dir / "history_shown.md").write_text(history_md, encoding="utf-8")
> --- `run_vanilla.py`

The last ten attempts and at most 400 summary characters each are shown; score, delta and kept/reverted labels persist even when summaries are empty. The worker is asked to avoid failures and make one improvement. Admission of history text is automatic formatting/staging, separate from score-based admission of reusable code. Resume reads `agent_summary` alone while live history prefers `agent_conclusion`; consequently restart may reduce narrative memory without deleting the packet. Reasons beyond these short summaries need not survive delivery.

### Routes

#### MEM-RTE-log-brief
Label: Reduce trajectory for later reflection

Endpoints: winning retained full log → deterministic excerpt file → later reflector diagnostic reads. Owner: Python reflector wrapper, with the external reflector deciding actual file reads. It is a context-selection route, distinct from the proposal/admission route [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: excerpt file, or no write on full-log read error.
- Later read-back: a subsequent reflector invocation is directed to the completed node's brief.
- Delegated visibility: head and tail are the preferred trajectory view; full hidden log, packets and workspaces remain reachable.
- Selection predicate: expanded node's `.log.log`, otherwise legacy `log.log`; all lines if at most 600, otherwise first 100 and last 500 with omission notice.
- Invalidation or expiry: overwritten when the wrapper generates a new brief; force-init can remove the root; no ordinary timed expiry.
- Activation or effect: code fixes delivered excerpt availability; diagnostic interpretation and resulting plan changes are unobserved.
- Evidence limits: line limits are not token limits; resumed turns and additional reads can enlarge context; no benefit measurement.

SRC-1, `search/reflector.py`, `run_search.py`. This trace-fed write retains literal selected output, not newly inferred lessons. It preferentially omits middle tool/thinking material while preserving header and recent conclusion. The full source is not evicted from disk.

> LOG_BRIEF_HEAD_LINES = 100       # lines kept from the start of the agent log
> LOG_BRIEF_TAIL_LINES = 500      # lines kept from the end
> --- `search/reflector.py`

#### MEM-RTE-session-resume
Label: Continue reflector through saved session

Endpoints: saved session metadata → Codex resume invocation → saved next identifier/counter. Owner: Python wrapper chooses continuation; external Codex owns session content and context restoration. Distinct from [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission): this is its continuity mechanism, also used during initialization, not proposal admission itself. SRC-1, `search/reflector.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reflector success flag and cost dictionary, stdout/stderr log and possible updated session file.
- Later read-back: the next call reads the saved identifier and requests the external session.
- Delegated visibility: prompt names new outcome artifacts; previous session contents are opaque, not embedded in the JSON metadata.
- Selection predicate: existing readable state with session_id selects exec resume; otherwise fresh exec. No content-based session retrieval or window budget is implemented here.
- Invalidation or expiry: nonzero resumed subprocess clears saved state, but subsequent stdout parsing can save an identifier again; timeout returns early without clearing it. Force-init clears the session file when clearing an existing root.
- Activation or effect: invocation arguments request continuity and counter deltas affect cost accounting; restored model memory and behavioral dependence are unobserved.
- Evidence limits: host session availability, compaction, restoration fidelity, expiry and actual window contents are uninspected.

> cmd = base_cmd + ["exec", "resume", "--skip-git-repo-check",
>                   session_id, prompt]
> --- `search/reflector.py`

> if result.stdout:
>     sid = _parse_codex_session_id(result.stdout)
>     if sid:
>         _save_session_state(
> --- `search/reflector.py`

The latter write follows failure clearing without a success guard. Clearing is therefore a recovery attempt, not an invariant that the next call starts fresh. No target execution establishes whether failure stdout actually supplies an identifier.

#### MEM-RTE-insight-delivery
Label: Copy and supply cross-task insights

Endpoints: existing benchmark insight files → local reflector copy or FIRE-Bench worker context → external model. Owners: Python copies/selects files; model chooses relevance. Distinct from [RT-BAP-plan-worker](runtime.md#rt-bap-plan-worker): this names the separately sourced retained input and its selector, not the common final delivery channel. SRC-1, `search/reflector.py`, `benchmarks/fire_bench/agents/codex/run.py`, `benchmarks/fire_bench/agents/codex/run_inherit.py`, `benchmarks/fire_bench/agents/openhands/run.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: copied files for the reflector, or concatenated insight/plan body for worker staging.
- Later read-back: subsequent init/reflection can read local files; FIRE-Bench workers receive other-task text in native skills or inline instruction context.
- Delegated visibility: reflector init requests reading relevant files; worker loading includes all nonempty other-task Markdown files, with task labels, before the current task plan.
- Selection predicate: init skips this task's named insight; reflection copies every Markdown file; worker loaders sort files and skip empty files and the current task stem. No semantic retrieval, score gate or numeric context budget.
- Invalidation or expiry: copy overwrites same-named local files but does not mirror deletions; local stale files can remain. No timed expiry or evidence-based withdrawal is implemented in these copy/load bodies.
- Activation or effect: Python prepares text or file availability; model selection, compliance and benefit are unobserved.
- Evidence limits: existing file provenance and admission before arrival are unresolved; copying does not establish automated experience extraction or a closed cross-task learning loop.

> for insight_file in sorted(insights_dir.glob("*.md")):
>     if not insight_file.stat().st_size:
>         continue
>     # Skip the current task's own insight (included below via skill.md)
>     if insight_file.stem == f"{task_id}_insight":
>         continue
> --- `benchmarks/fire_bench/agents/codex/run.py`

This is automatic supply at worker invocation, not worker-requested targeted retrieval. AutoLab staging directly reads the task skill; no analogous insight concatenation appears in its inspected `run_agent` body. That does not exclude a reflector incorporating pre-existing insight text into its authored plan.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-skill](runtime.md#rt-obj-skill)

Memory lineage: root plan is reflector-authored from instruction and available other-task files; successor plans are requested transformations informed by retained outcomes. Node files survive rounds and task-tree restarts. Admission is model authoring plus Python existence/prior bootstrap, not per-content human approval. File copying is distinct from admission. AutoLab requests compact inherited-state plus incremental guidance; FIRE-Bench requests a complete plan, with [MEM-OBJ-diff](#mem-obj-diff) and [MEM-OBJ-changes](#mem-obj-changes) as separate provenance/explanation surfaces. SRC-1, `search/reflector.py`, `run_search.py`; supporting requested hypothesis/rationale and bootstrap passages are retained in [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission). Physical editability permits human intervention, but no routed human approval is shown.

#### On [RT-OBJ-stats](runtime.md#rt-obj-stats)

Trace lineage: admitted numeric evaluation outcomes automatically update visits/Q up the ancestry; admitted prior estimates initialize P. These symbolic fields are durable behavior-shaping memory for fixed Python traversal, not distributed model weights. Pruned scores do not backpropagate. The update consumer differs from downstream plan consumers: the driver uses numbers, while the reflector is directed to packet/plan content. SRC-1, `search/tree.py`, `run_search.py`; update and selector quotes are retained in [RT-OBJ-stats](runtime.md#rt-obj-stats) and [RT-BAP-score-selector](runtime.md#rt-bap-score-selector).

#### On [RT-OBJ-sandbox](runtime.md#rt-obj-sandbox)

Code/data inheritance is a later consumer route, not mere archival. Search requires positive parent Q and a present parent sandbox; the adapter/runner copies it into a new invocation. AutoLab excludes `_reward`, `.agents`, `target`; FIRE-Bench copies the parent tree, refreshes its staged skill when nonempty and rewrites keys. Available child diff/change files are added separately. The baseline replaces best_sandbox on strict improvement and excludes reward/build, skills, keys and bytecode files. It does not restore an earlier immutable version after a failed destructive copy. SRC-1, `run_search.py`, `run_vanilla.py`, `benchmarks/autolab/__init__.py`, `benchmarks/fire_bench/agents/codex/run_inherit.py`.

> if best_sandbox.exists():
>     shutil.rmtree(best_sandbox)
> shutil.copytree(str(iter_sandbox), str(best_sandbox), ignore=COMMIT_IGNORE)
> --- `run_vanilla.py`

Executable code has symbolic runtime authority; explanatory text is separately model-interpreted. Data/model files inside arbitrary workspaces have unresolved task-specific encodings and provenance: treating the whole directory as natural-language memory or provider weight learning would overstate the evidence.

#### On [RT-RTE-vanilla-retention](runtime.md#rt-rte-vanilla-retention)

Read-back asymmetry: live summaries use conclusion then summary, while packet replay uses summary alone. Thus the runtime's statement that history is reconstructed needs this qualification; scores/actions survive replay but previously displayed text may not. SRC-1, `run_vanilla.py`.

> "summary": p.get("agent_summary", ""),
> --- `run_vanilla.py`

> "summary": packet.get("agent_conclusion", "") or packet.get("agent_summary", ""),
> --- `run_vanilla.py`

## Write side

Acquisition and admission are separate at each write surface. The operator supplies task/options and may edit physical files, but the shipped internal loop has no per-plan approval. The reflector is asked to derive new plans and explicit reasons from prior traces; Python admits children on plan existence and a defaulted/clamped estimate, including pre-existing directories whose authorship is unresolved. Neither the optional explanation/script nor diagnostic grounding is required. This is not human-supervised curation merely because a human launches it. SRC-1, `run_search.py`, `search/reflector.py`; [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission), [MEM-OBJ-prior](#mem-obj-prior).

Evaluation yields retained packets; Python transforms numeric outcomes into Q/visits and uses the best of repeated attempts. Full winning logs/workspaces move into the tree. Automatic later-consumed reductions are the log brief, pruning digest and baseline history. The brief is literal positional selection; the digest mixes prior reasons with numeric rejection and a short verifier tail; baseline history mixes evaluator decisions with agent-supplied narrative. These origins cannot all be called independent verifier evidence. Model-authored successor plans are requested trace-fed behavioral guidance, but no generated plan demonstrates the transformation's semantic fidelity. SRC-1, `run_search.py`, `run_vanilla.py`, `search/reflector.py`; [MEM-RTE-log-brief](#mem-rte-log-brief), [MEM-OBJ-pruned-children](#mem-obj-pruned-children), [MEM-OBJ-history-shown](#mem-obj-history-shown).

Rejection preserves experience selectively. Missing-plan bootstrap archives directories with an error file. Score-pruning saves packet/artifacts, hides a child, excludes its score from backpropagation and appends failure memory. Re-expansion prompts avoid repeating those approaches, without semantic enforcement. Baseline nonimprovement leaves best code unchanged but saves the attempt packet and history. Force-init deletes root/ledgers/session/logs only through the existing-root branch while retaining local insights/instruction; this is coarse reset, not evidence-based withdrawal of particular claims. Insight copying can retain stale local files after source deletion. SRC-1, `run_search.py`, `search/tree.py`, `search/reflector.py`, `run_vanilla.py`; [MEM-RTE-insight-delivery](#mem-rte-insight-delivery).

There is no inspected automatic promotion of outcome-derived insight files: the bounded Python search for insight writes/copies found touching, copying and loading paths; reflection proposal templates request plans/priors/diffs/changes rather than an explicit insight publication step. General shell access leaves discretionary model writing possible, so this is an unresolved producer/admission fact, not an evidenced universal absence. Initial insight provenance remains unknown without suppressing the known subsequent delivery operations. SRC-1, `search/reflector.py`, `run_search.py`, `benchmarks/base.py`, `benchmarks/fire_bench/agents/codex/run.py`.

## Read-back

Symbolic read-back is task-root reload plus Q/P/visits and packet presence controlling the next step. It is scoped by filesystem ancestry and visibility, not query similarity. Pruned branches are excluded from ordinary traversal. Node packet presence is an existence/size test, not packet semantic validation. SRC-1, `search/tree.py`; [RT-BAP-score-selector](runtime.md#rt-bap-score-selector).

Reflector read-back is prompted filesystem inspection: a completed-node pointer, preferred diagnostic brief, packet and selected auxiliary artifacts, with sibling priors/plans/packets available on demand. Root initialization differs: instruction and other-task files are the inputs. Resume adds an opaque continuity channel, so the tree is neither the only memory nor proof of a bounded visible window. A hidden full log remains reloadable; FIRE-Bench permits exceptional reads, and AutoLab supplies diff/verifier pointers to avoid indiscriminate source traversal. Prompts privilege verifier/packet evidence over agent success narratives, but this is trust guidance rather than access control or verified truth. SRC-1, `search/reflector.py`; [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission), [MEM-RTE-session-resume](#mem-rte-session-resume).

Worker invocations receive separately staged plan/history and selected starting code rather than the reflector's full context. Native Codex skills make loading available through descriptions and implicit-invocation policy; runtime-supplied OpenHands findings establish inline delivery. Code copying has direct executable consequences if subsequently run; plan text has model-mediated authority whose activation is unobserved. FIRE-Bench's cross-task body has no implemented relevance/budget selector beyond file filters; baseline history instead has explicit ten-entry/400-character bounds. SRC-1, `benchmarks/utils.py`, `benchmarks/autolab/__init__.py`, `benchmarks/fire_bench/agents/codex/run_inherit.py`, `run_vanilla.py`; [RT-BAP-plan-worker](runtime.md#rt-bap-plan-worker), [MEM-RTE-insight-delivery](#mem-rte-insight-delivery).

The separate worker invocation resembles a task frame: instruction/skill/workspace enter; logs, artifacts and packet escape, not a shared conversation window. The reflector can continue a prior session, so it is not a discarded frame on every call. Files are reachable through explicit tool reads, not live references inside a window; hiding files does not remove already accumulated turns or impose a reachability-based lifetime. External compaction and actual skill-body insertion/removal remain uninspected. SRC-1, `search/reflector.py`; supplied runtime's context account and [RT-RTE-search-execution](runtime.md#rt-rte-search-execution).

## Integration issues

1. Qualify failed-resume recovery in [MEM-RTE-session-resume](#mem-rte-session-resume) against the runtime account and [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission): the saved state is unlinked on nonzero resume but can be saved again from failure stdout; timeouts bypass clearing. SRC-1, `search/reflector.py`. A guaranteed fresh next session is unsupported.
2. Qualify replayed history in [RT-RTE-vanilla-retention](runtime.md#rt-rte-vanilla-retention) using [MEM-OBJ-history-shown](#mem-obj-history-shown): replay omits conclusion-only summaries that live history used. SRC-1, `run_vanilla.py`. Restart continuity of narrative evidence is weaker than continuity of score/action state.
3. Cross-task insight production/admission remains unresolved in [MEM-OBJ-insights](#mem-obj-insights), while [MEM-RTE-insight-delivery](#mem-rte-insight-delivery) is inspectably wired. Comments claiming later population do not identify an enforced producer; general reflector capabilities could write files. SRC-1, `search/reflector.py`, `run_search.py`. Do not infer a closed cross-task learning loop or deny the positive delivery path.
4. [MEM-OBJ-diff](#mem-obj-diff), [MEM-OBJ-changes](#mem-obj-changes), [MEM-OBJ-prior](#mem-obj-prior) are distinct proposal artifacts, not duplicate node skill records. [MEM-OBJ-packet](#mem-obj-packet), [MEM-OBJ-log-brief](#mem-obj-log-brief), [MEM-OBJ-pruned-children](#mem-obj-pruned-children), [MEM-OBJ-history-shown](#mem-obj-history-shown) name previously undeclared inputs/outputs of supplied routes, not replacement routes. No possible duplicate supplied referent remains after comparison; reconciliation should connect them rather than supersede the supplied routes.
5. Source-supported artifact-pointer limit: [MEM-OBJ-packet](#mem-obj-packet) paths are rewritten before score-pruning renames a directory; `_prune_node` does not rewrite those packet paths afterward. SRC-1, `run_search.py`. Hidden artifacts still exist, but a packet path alone does not guarantee valid later dereference. Reflector digest and direct filesystem inspection remain alternative routes.
6. External session payload, model invocation behavior, arbitrary workspace file forms and host-native skill/compaction decisions remain uninspected. These limits affect [MEM-RTE-session-resume](#mem-rte-session-resume), [RT-OBJ-sandbox](runtime.md#rt-obj-sandbox), [RT-BAP-plan-worker](runtime.md#rt-bap-plan-worker), not the inspected file transformations. No observations establish learned capacity or benefit.

## Limitations and checks

Frozen checkout HEAD was rechecked as `29971beac6f4f4b41309b1326762e1b83ceece98` and status was clean. The supplied member/type/record contracts governed this report; no prior analysis, target execution, model service or external source was used. Inspection includes source-supported countercases to filesystem-only memory, guaranteed fresh-session recovery, complete narrative replay, semantic proposal admission and budgeted relevance retrieval. Unknowns remain local to their consumers and do not erase supported paths.

Deterministic validation: the required validate-output command is run against this invocation before return; its passing result establishes structural/quotation checks, not semantic acceptance or observed effectiveness.

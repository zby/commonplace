---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "ModularRSI memory: trace-derived proposal backlog, executable generations, selection metadata, resume state and bounded context handoffs."
run-id: AAS-2026-10-18-modularrsi-4218ceff5530-01
source-identity: https://github.com/IQuestLab/ModularRSI
reviewed-boundary: b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9
---

# ModularRSI memory report

## Boundary and evidence

The included memory boundary follows the shipped evolution and evaluation routes, not just `editor_memory.jsonl`. It includes raw solver/editor traces, derived findings and proposals, proposal/disposition/lease state, implementation manifests, executable generations, archive metadata, bundle replay, resume state, historical passing-trial lookup, context compression, observation selection and editor reference reads. Provider internals, external task contents and the omitted training history remain outside the available evidence. Bundled evaluation trials were not individually inspected; no observed activation, summary fidelity or learning benefit is established here.

All direct inspection uses SRC-1 from [boundary](boundary.md#source-register), at b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9. Implementation passages below describe wiring. Source comments and prompts describe intent, not reliable model compliance. Supplied runtime findings are explicitly cited rather than treated as independent execution evidence.

| Entry point / operation | Source paths (SRC-1; commit-relative) | Coverage and limit |
|---|---|---|
| Evolution / evaluation launch, library import, candidate gates and promotion | `scripts/evolve.sh`, `scripts/evaluate.sh`, `src/harbor/agents/terminus_2_modular/library.py`, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`, `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py` | Supplied [RT-RTE-generation-change](runtime.md#rt-rte-generation-change), [RT-BAP-module-execution](runtime.md#rt-bap-module-execution); direct reflection/two-lane sections checked. No independent gate rerun. |
| Trial summarization, diagnosis, evidence clustering, later brief | `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py`, `src/harbor/agents/terminus_2_modular/self_evo/backlog.py`, `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py`, `src/harbor/agents/terminus_2_modular/self_evo/clustering.py`, `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py` | Direct reads: [MEM-RTE-evidence-brief](#mem-rte-evidence-brief). Snapshot-local retry and efficiency-path limits retained below. |
| Proposal ranking, terminal decisions and interrupted attempts | `src/harbor/agents/terminus_2_modular/self_evo/proposals.py`, `src/harbor/agents/terminus_2_modular/self_evo/portfolio.py`, `src/harbor/agents/terminus_2_modular/self_evo/dispositions.py`, `src/harbor/agents/terminus_2_modular/self_evo/lease.py` | Direct state definitions, folding, selection, disposition and recovery reads: [MEM-OBJ-proposal-state](#mem-obj-proposal-state). No observed recovery. |
| Build manifest, archive sync / confirmation / retirement | `src/harbor/agents/terminus_2_modular/self_evo/manifest.py`, `src/harbor/agents/terminus_2_modular/archive.py`, `src/harbor/agents/terminus_2_modular/self_evo/confirm.py`, `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py` | Direct reads plus supplied promotion account: [MEM-OBJ-implementation-record](#mem-obj-implementation-record), [MEM-OBJ-archive-entry](#mem-obj-archive-entry). Not a deletion or security boundary. |
| Historical pass lookup, progress checkpoint / resume | `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`, `src/harbor/agents/terminus_2_modular/self_evo/router.py` | Direct reads: [MEM-RTE-history-contrast](#mem-rte-history-contrast), [MEM-RTE-progress-resume](#mem-rte-progress-resume). Filesystem contents at a future resume are not guaranteed. |
| Editor-memory and evolution-log append, compact-index API | `src/harbor/agents/terminus_2_modular/self_evo/editor_memory.py`, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`, `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py` | Direct reads and scoped caller search: [MEM-ABS-editor-readback](#mem-abs-editor-readback). An available formatter is not an injected history. |
| Dynamic/static/forced/cache selection | `src/harbor/agents/terminus_2_modular/kernel/orchestration.py`, `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py` | Direct cache read/write and archive filter, plus [RT-RTE-bundle-selection](runtime.md#rt-rte-bundle-selection). Individual alternate selection efficacy uninspected. |
| Installed and released context baseline, editor passthrough | `src/harbor/agents/terminus_2_modular/modules/context_mgmt/baseline.py`, `src/harbor/agents/terminus_2_modular/modules/context_mgmt/passthrough.py`, `generations/merged_active/gen_0/modules/context_mgmt/baseline.py` | Direct algorithm reads and source diff: annotation on [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff). Released fallback does not perform the installed fallback reset. |
| Observation and editor-tool context selection | `src/harbor/agents/terminus_2_modular/modules/observation/baseline.py`, `generations/merged_active/gen_0/modules/observation/terminal_scrollback.py`, `src/harbor/agents/terminus_2_modular/modules/tools/editor_file_tools.py`, `src/harbor/agents/terminus_2_modular/self_evo/run_editor.py` | Direct capture, archive and file-read sections; editor setup searched. Annotation on [RT-RTE-solver-task](runtime.md#rt-rte-solver-task). Other released strategy bodies are not exhaustively audited; no uniform context policy across all evolvable Python is asserted. |
| Released provenance and sanitized evaluation artifacts | `generations/merged_active/README.md`, `trajectories/mergefinal/README.md` | Supplied boundary only. Full training lineage and per-trial memory effectiveness remain uninspected. |

## Core ideas

1. The principal durable behavior change is Python code, not a textual memory index. Its runtime authority is already established by [RT-OBJ-module-library](runtime.md#rt-obj-module-library) and [RT-BAP-module-execution](runtime.md#rt-bap-module-execution). The diagnostic backlog is an upstream, model-interpreted memory that can shape that code; it is not routinely injected into solver chat.
2. Semantic evidence and access/control metadata have different consumers. Finding bodies and causal hypotheses reach models; proposal states, support counts, dispositions, archive statuses and leases control software selection and recovery. Terminal dispositions can suppress reconsideration without deleting their evidence. See [MEM-RTE-evidence-brief](#mem-rte-evidence-brief) and [MEM-BAP-backlog-control](#mem-bap-backlog-control).
3. Retention does not guarantee read-back. `compact_index` can render editor history, but the inspected shipped callers do not inject it. Cross-module handoff and retryable-finding comments similarly exceed the traced consumer wiring in important respects. See [MEM-ABS-editor-readback](#mem-abs-editor-readback) and Integration issues.
4. Context management is deliberately lossy. Even the full QA summary reads history after tail unwinding; the released “FULL history” observation is capped and can suppress stale content. Source labels are not completeness guarantees. See the context and solver annotations.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-finding-record
Label: Retained finding bodies and provenance

Part of: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

This object is the retained evidence output within that route, not another declaration of the route. Source-native identity: `FindingRecord.raw_finding`, with `finding_id`, task/window/lens identity, parse status, support tasks and provenance. Natural-language diagnosis is model-interpreted content inside a symbolic JSON envelope. Storage: per-window `findings/<step>.json`, then `backlog/findings.jsonl`. Raw solver/editor trajectories are its inputs, not identical to the derived finding. The ledger preserves the raw parsed finding dictionary, not the entire original conversation. ID construction uses step, task, lens and position; it is not a semantic-content hash.

Lineage and agency: software summarizes trial results/trajectories; an investigator model authors the diagnosis; parsing and ingestion preserve the result. No per-finding human approval is wired. Corrupt ledger JSON lines are skipped. Admission to storage is distinct from admission to proposal routing: stored non-culprits and parse failures need not reach that next step. Consumers: evidence routing/clustering models; portfolio uses identity/support metadata; selected implementers receive body displays. Full retained evidence and truncated displays are different surfaces (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/backlog.py`, `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py`).

> raw_finding=dict(finding),
> --- `src/harbor/agents/terminus_2_modular/self_evo/backlog.py`

> if len(body) > MAX_FINDING_CHARS:
>         body = body[:MAX_FINDING_CHARS] + "\n… [truncated]"
> --- `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py`

#### MEM-OBJ-proposal-record
Label: Proposal direction and causal rationale

Part of: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

Source-native identity: `ProposalRecord.behavioral_delta`, `causal_hypothesis`, action and target plus finding/support references. This is a retained proposed intervention, not its executable implementation. Natural-language fields state what should change and why; symbolic action/target fields constrain the requested build. Storage: append-only events in `backlog/proposals.jsonl`, folded to records in memory. Model routing and semantic comparison supply content; software creates or links records. Initialization comes from the caller of the proposal API; the shipped evidence pass supplies that caller, not an unstated human curator. Later implementers receive proposal text and matched finding bodies; the final solver does not receive these reasons automatically. Semantic correctness is not established by persistence (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/proposals.py`, `src/harbor/agents/terminus_2_modular/self_evo/clustering.py`).

> behavioral_delta=str(ev.get("behavioral_delta") or ""),
>                 causal_hypothesis=str(ev.get("causal_hypothesis") or ""),
> --- `src/harbor/agents/terminus_2_modular/self_evo/proposals.py`

The explicit rationale consumer is the brief, not the composer:

> delta=proposal.behavioral_delta or "(not stated)",
>         why=proposal.causal_hypothesis or "(not stated)",
> --- `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py`

#### MEM-OBJ-proposal-state
Label: Proposal, disposition and lease control metadata

Part of: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

Distinct from proposal meaning above: symbolic state transitions, attempts/support identity, terminal finding IDs, and unfinished-attempt leases determine eligibility and recovery. Substrates: `backlog/proposals.jsonl`, `backlog/dispositions.jsonl`, `backlog/leases.jsonl`; out-of-scope disposition rows also go to `backlog/out_of_scope/<module>.jsonl`. Reasons are retained text attached to decisions, not a guarantee that later software interprets those reasons. Event-folding and fixed transition/terminal rules supply the operative authority.

The software portfolio selects open proposals only, at most one per incumbent/novelty lane, using attempts, numeric age, task breadth, window breadth and stable jitter. Reviewer classification can permit one second implementation; generic failures do not thereby earn that retry. Lease recovery reopens unstarted selected proposals or settles started ones as rejected implementations. A terminal disposition suppresses rerouting; retryable is deliberately nonterminal. This metadata is software/model governed; launching evolution is not human per-content admission (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/proposals.py`, `src/harbor/agents/terminus_2_modular/self_evo/portfolio.py`, `src/harbor/agents/terminus_2_modular/self_evo/dispositions.py`, `src/harbor/agents/terminus_2_modular/self_evo/lease.py`, `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py`).

> TERMINAL_KINDS = frozenset({OUT_OF_SCOPE, COVERED, STALE, INVALID})
> --- `src/harbor/agents/terminus_2_modular/self_evo/dispositions.py`

> p for p in _proposals.load_proposals(archive_root) if p.state == _proposals.OPEN
> --- `src/harbor/agents/terminus_2_modular/self_evo/portfolio.py`

#### MEM-OBJ-implementation-record
Label: Retained build manifest

Part of: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

Source-native identity: `ImplementationRecord`, in `backlog/implementations.jsonl`; symbolic file lists, staging hash, supersede targets and dropped flag, plus raw `variant_meta_text`. Lineage: `_record_lane_implementation` records what the editor built separately from proposal intent before staging disappears. No manifest label proves byte correctness or successful promotion. Consumers can retrieve latest per-proposal records and live metadata; dropped entries clear files, metadata and retirement targets together. This is not the Python library or the proposal text. Software records/retracts it; no per-record human approval is established (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/manifest.py`, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`). Detailed downstream manifest use beyond supplied promotion findings remains uninspected, so the helpers alone do not establish an additional autonomous consumer route.

> def live_supersede_targets(archive_root: Path | str) -> list[str]:
>     """Who may be retired — dropped proposals retire nobody."""
> --- `src/harbor/agents/terminus_2_modular/self_evo/manifest.py`

#### MEM-OBJ-archive-entry
Label: Archive lineage and selection state

Source-native identity: `ArchiveEntry`, serialized as `archive.json`: qualified variant identity, niche, parents, addresses, change type, birth generation and active/superseded/excluded status. Symbolic identity/status/niche fields operate as selection metadata; addresses and rendered lineage text inform an editor, rather than executing as Python. This object is distinct from the library and descriptions in [RT-OBJ-module-library](runtime.md#rt-obj-module-library) and [RT-OBJ-module-description](runtime.md#rt-obj-module-description), and from [MEM-OBJ-proposal-state](#mem-obj-proposal-state): it tracks admitted variant state, not open intervention state.

Lineage: seed from library, upsert after promotion, mark regressors superseded from confirmation. Initial released history is sanitized; complete ancestral evidence cannot be reconstructed from parent names alone. Software owns these writes, with source metadata partly authored by module editors. Confirmation consumes task/bundle/reward samples; its outcome can withdraw later ordinary selection without deleting Python files. The composer filter returns an empty skip set on archive errors. Editor `<archive>` can request type or lineage views; missing archive falls back to staging-derived niches with a warning when a supplied path failed. This read channel is not access to the full historical trace (SRC-1, `src/harbor/agents/terminus_2_modular/archive.py`, `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py`, `src/harbor/agents/terminus_2_modular/modules/tools/editor_file_tools.py`, `src/harbor/agents/terminus_2_modular/self_evo/confirm.py`).

> if _arch.set_status(
>                 archive_root, f"{module_type}/{reg['variant']}", "superseded"
>             ):
> --- `src/harbor/agents/terminus_2_modular/self_evo/confirm.py`

#### MEM-OBJ-editor-memory
Label: Outcome journal and optional compact display

Part of: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

Source-native identity: `editor_memory.jsonl`; symbolic epoch/module/task/gen/verdict fields and a natural-language change string truncated to 280 characters. Software appends promotion and regression outcomes best-effort; the implementation reads and rewrites the whole prior text, so append-only is logical behavior, not an atomic append guarantee. `compact_index(module, n=12)` filters by module, renders recent rows with 90-character change displays and a rolled_back/no_help taboo list with 110-character displays. It does not preserve full reasons or full code. Its display capability must be separated from an actual consuming editor invocation; see [MEM-ABS-editor-readback](#mem-abs-editor-readback).

The separate `evolution_log.jsonl` journal records generation intent/outcomes through `append_evolution_log`. It is an audit output, not proven read-back in the inspected shipped callers. Neither journal is identical to the actively consumed proposal backlog (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/editor_memory.py`, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`, `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py`).

> "change": (change or "").strip()[:280],
> --- `src/harbor/agents/terminus_2_modular/self_evo/editor_memory.py`

### Routes

#### MEM-RTE-evidence-brief
Label: Trace evidence to later implementation brief

Part of: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: parsed per-task findings, window snapshot, ledger rows and routing/clustering outcomes; the portfolio later returns up to two proposal picks.
- Later read-back: later reflection windows can select still-open proposals; `build_brief` loads all referenced finding IDs and delivers proposal delta/hypothesis plus finding displays to a fresh implementer.
- Delegated visibility: investigators get selected pass/fail summaries and permitted trajectory reads plus staged code; implementers get only their selected proposal/support, not sibling briefs or a merged investigator conversation.
- Selection predicate: task router/cooldown selects investigations; culprit findings not already attached or terminal enter model routing; model semantic comparison links the first same-intervention proposal or software creates one after comparisons resolve; deterministic portfolio ranks open proposals.
- Invalidation or expiry: proposal transitions remove directions from open selection; terminal dispositions stop rerouting; unreadable support is disclosed; rejected staging is discarded. Retryable disposition permits reconsideration but does not itself schedule it.
- Activation or effect: retained diagnosis can shape a later model-authored module change through its brief; structured state controls eligibility. No particular finding's effect on generated bytes or task success was observed.
- Evidence limits: source wiring and prompts establish delivery and requested causal diagnosis, not fidelity, truthful attribution, criticism quality or benefit. Briefs cap each finding at 6000 characters despite the preamble's complete-evidence language.

Owner and mode: operator-configured bounded support-task curriculum; software selects tasks/proposals; investigator/routing/implementer/reviewer models supply content judgments; software validation and reviewer rejection can block further admission. Human workflow launch is not content approval. Task verifier rewards are the outcome reference for contrast, not a reference answer for the semantic clustering model. The later code gates and their fail-open/repair qualifications remain [RT-RTE-generation-change](runtime.md#rt-rte-generation-change), not a new guarantee here.

SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`, `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py`, `src/harbor/agents/terminus_2_modular/self_evo/clustering.py`, `src/harbor/agents/terminus_2_modular/self_evo/portfolio.py`, `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py`:

> placed |= _dispositions.terminal_finding_ids(archive_root)
>     culprits = [r for r in records if r.is_culprit and r.finding_id not in placed]
> --- `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py`

> found = [findings_by_id[f] for f in proposal.finding_ids if f in findings_by_id]
>     missing = [f for f in proposal.finding_ids if f not in findings_by_id]
> --- `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py`

Theory account: findings may be local observations; explicit causal hypotheses are separately addressable proposal fields. Reasons survive in findings/proposals and reach implementers; rejected-code repair briefs can reach a second build from the parent. The solver's executable strategy need not retain or expose those historical reasons. For theory-builder conditions 1–4: condition 1 conclusion status: afforded (localized hypothesis fields); condition 2 conclusion status: wired (brief construction explicitly supplies their content to the implementation decision); condition 3 conclusion status: afforded (requested counterfactual diagnosis and proposal-versus-implementation review); condition 4 conclusion status: wired (support accumulation and bounded second build preserve results for later work). These are architectural findings, not observations of sound theories or actual content-directed criticism. Addressability is at finding/proposal/variant granularity; persistence can cross windows and resume. Learning: improved future capacity is uninspected; storing experience and generating code establish neither improvement nor its cause. The broader reflection/self-change assessment remains in the supplied runtime record.

#### MEM-RTE-history-contrast
Label: Historical pass reconstruction for diagnosis

Part of: [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: best-effort task-to-latest-passing-trial-directory JSON map, then an on-demand `TrialSummary` or None.
- Later read-back: a subsequent encounter without a current passing roll can use an earlier task pass as the investigator's contrast partner.
- Delegated visibility: summarized earlier trial plus readable permitted trace files, not all historical runs or an entire prior solver chat.
- Selection predicate: scalar reward at least 1.0 and a trial directory admit map entries; same task identity selects the stored directory; reread result must still verify as passing.
- Invalidation or expiry: latest pass replaces a task's previous pointer; absent/unreadable/now-nonpassing trial returns None and permits single-sided diagnosis.
- Activation or effect: software reconstructs a contrast input for a later investigator; whether it improves attribution or resulting code is uninspected.
- Evidence limits: pointer persistence is not payload preservation; cleanup can remove its referent. Historical pass and current failure need not share a generation or controlled comparison conditions.

Software owns map maintenance and lookup in the bounded curriculum; no human approval is required per pointer. The verifier reward is the reference outcome, not a semantic proof. This is metadata-assisted reconstruction of derived memory from retained raw trial files, not vector retrieval. SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`:

> mapping[s.task_name] = str(s.trial_dir)
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`

> if summary is None or summary.reward is None or summary.reward < 1.0:
>             return None
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`

#### MEM-RTE-progress-resume
Label: Checkpoint-driven resumed work and context

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `progress.json` snapshots task identity, generation, reward/error, bundle/group state, trial paths, derived summary and reflection outcome; router ledger persists task history/cooldown separately.
- Later read-back: resume skips aligned completed task indices and restores summaries not consumed by a completed reflection; later reflection receives them rather than treating them as already digested.
- Delegated visibility: restored summaries reach routing and investigation, not wholesale replay into solver model context.
- Selection predicate: deterministic task order and index/name alignment permit skips; latest recorded reflection boundary determines pending restoration. Router ledger uses past success/progress/cooldown to select later diagnosis work.
- Invalidation or expiry: unreadable progress is ignored; task-order mismatch moves it aside and reruns without skips. Corrupt router ledger starts fresh. Checkpoint writes are best-effort, not a multi-file transaction.
- Activation or effect: symbolic retained state changes scheduling and supplies later investigation inputs; no observed resumed run was inspected.
- Evidence limits: progress preserves prior rows, but full atomic consistency with archives, proposal events and filesystem state is not established; no universal recovery guarantee follows.

Distinct identity from [RT-RTE-generation-change](runtime.md#rt-rte-generation-change): this route is driver recovery/scheduling, including work that never produces a candidate, not another candidate-admission route. Owner: software acting for the configured operator; serialized summaries contain model-generated last messages and fixed metrics, while IDs, cooldown and reflection markers are symbolic. No new per-checkpoint human admission decision is wired. SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`, `src/harbor/agents/terminus_2_modular/self_evo/router.py`:

> "summary": dataclasses.asdict(r.summary) if r.summary else None,
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`

> pending_summaries.extend(restored_pending)
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`

### Claims

none declared in this member

### Evidenced absences

#### MEM-ABS-editor-readback
Label: No wired compact editor-history consumer in searched callers

- implementation conclusion status: absent

At the frozen SRC-1 revision, searches for `compact_index`, `editor_memory`, `out_of_scope_for`, `module_backlog_path` and `evolution_log` under `src/` and `scripts/` found journal writers and helper definitions, not a compact-index invocation or evolution-log read into an editor. The exact formatter exists, so the absence is **caller wiring in those shipped roots**, not a missing storage capability or a claim about arbitrary external callers. The `archive` action reads archive entries, not these journals. `run_editor` exposes staging, optional trajectory and skill roots rather than the entire archive root as an unrestricted file-read root. Thus comments that the next consolidator sees the anti-flip-flop history do not establish that delivery (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/editor_memory.py`, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`, `src/harbor/agents/terminus_2_modular/self_evo/run_editor.py`, `src/harbor/agents/terminus_2_modular/modules/tools/editor_file_tools.py`).

> def compact_index(archive_root: Path | str, module: str, n: int = 12) -> str:
> --- `src/harbor/agents/terminus_2_modular/self_evo/editor_memory.py`

The finding narrows the boundary's editor-memory consumer language, not [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)'s independently wired proposal read-back. No claim that the main evolution mechanism lacks memory follows.

### Behavioral-authority paths

#### MEM-BAP-backlog-control
Label: Retained evidence controls later work

Consumer: software evidence pass, portfolio, lease recovery and dynamic composer, plus investigator/implementer models. Channel: loaded JSON/JSONL states and constructed brief text. Force: fixed symbolic eligibility, ranking, recovery and exclusion rules for metadata; advisory model interpretation of findings/hypotheses. Horizon: later windows/resume/task selections while files survive and the applicable route reads them. Not a duplicate of [RT-BAP-module-execution](runtime.md#rt-bap-module-execution) or [RT-BAP-description-selection](runtime.md#rt-bap-description-selection): this is retained upstream evidence/control, not Python execution or registration descriptions. SRC-1 passages and paths are retained in [MEM-OBJ-proposal-state](#mem-obj-proposal-state), [MEM-RTE-evidence-brief](#mem-rte-evidence-brief) and [MEM-OBJ-archive-entry](#mem-obj-archive-entry).

## Annotations

#### On [RT-OBJ-module-library](runtime.md#rt-obj-module-library)

Lineage/memory qualification: promoted source is a derived behavior-shaping artifact of trace diagnosis, proposal selection, model editing and admission, not a raw trace. The final runtime consumes executable files; historical hypothesis and criticism survive separately in the backlog and logs, not necessarily alongside each module. Rejection discards staging; confirmation generally changes archive eligibility rather than reverting bytes. The runtime record supplies the executable authority passage; [MEM-RTE-evidence-brief](#mem-rte-evidence-brief) supplies the upstream trace-to-derived chain. Complete released training lineage remains unavailable under the supplied boundary.

#### On [RT-RTE-bundle-selection](runtime.md#rt-rte-bundle-selection)

Storage and read-back: composer cache stores symbolic names/params for the five slots, including helper lists in tools parameters; task instruction SHA-256 selects the filename. Validation checks format/hash/spec shape, not a library-revision identity. Cache-write derives it from selection; cache-read directly reconstructs a bundle before ordinary composer invocation. K-roll/forced pins and static mode are alternative replay/admission paths already identified by the runtime. This is retained selection, not retained semantic diagnosis. Dynamic selection instead receives filtered descriptions and task text without reward-based retrieval. Source trust is therefore module registration text plus symbolic offered-name validation, not warrant from successful past outcomes (SRC-1, `src/harbor/agents/terminus_2_modular/kernel/orchestration.py`, `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py`).

> "instruction_sha256": path.stem,
>         "bundle": _bundle_payload(bundle),
> --- `src/harbor/agents/terminus_2_modular/kernel/orchestration.py`

Archive retirement is best-effort for ordinary dynamic filtering, not universal revocation of retained code:

> except Exception:
>         return frozenset()
> --- `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py:66-88`

#### On [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff)

Raw-to-derived memory: the installed baseline estimates free tokens using model counters or characters/4, with a fallback context limit of 200000; default proactive threshold is 8000 free tokens. Before full summarization it removes **tail** message pairs until the default 4000-token free target. Thus even the “comprehensive” summary is based on surviving history, not guaranteed full raw chat. Summary sees that surviving history; questions see original task, summary and terminal screen with empty history; answers see surviving history plus summary. Natural-language outputs replace the active window with system + question prompt (containing summary/screen) + questions; the answer-derived continuation prompt crosses back for the next call. The retained result has same-task inference authority, not executable authority or proven fidelity. The runtime supplies the replacement quotation (SRC-1, `src/harbor/agents/terminus_2_modular/modules/context_mgmt/baseline.py`).

> chat._messages = chat.messages[:-2]
> --- `src/harbor/agents/terminus_2_modular/modules/context_mgmt/baseline.py`

Fallback correction/qualification: installed overflow tiers 2 and 3 reset to the system message, carrying respectively task plus short model continuation, or task plus the last 1000 screen characters. The **released generation's baseline** omits those reset calls and retains the already unwound chat in these tiers. A direct source diff isolated that difference; it is not a universal property of baseline-named modules. Full QA replacement is shared. Proactive failure can also leave unwinding already performed before the summary failed. There is no demonstrated automatic reload of dropped turns from trajectory references (SRC-1, `generations/merged_active/gen_0/modules/context_mgmt/baseline.py`, installed baseline path above).

> self._reset_chat_to_system_message(chat)
>             return CompressResult(
> --- `src/harbor/agents/terminus_2_modular/modules/context_mgmt/baseline.py:196-197`

Editor contexts are separate frames, not compressed solver histories: setup disables summarization and uses `passthrough`, whose methods return chat unchanged. Investigators return extracted findings; implementers return edits/commit state; reviewers return structured verdicts. Their full chats remain trace artifacts rather than being merged into the caller. This resembles selected-input frames with output-only return, but text is copied by value and a saved trajectory reference is not a dereferenceable model-memory pointer (SRC-1, `src/harbor/agents/terminus_2_modular/modules/context_mgmt/passthrough.py`, `src/harbor/agents/terminus_2_modular/self_evo/run_editor.py`; supplied [RT-RTE-generation-change](runtime.md#rt-rte-generation-change)).

#### On [RT-RTE-solver-task](runtime.md#rt-rte-solver-task)

Working-context controls beyond compression: baseline observation captures incremental output and applies 10000-byte head/tail clipping; omitted middle is not automatically reloaded by that adapter. The released `terminal_scrollback` variant rereads a bounded pane-log tail, merges incremental data, and retains instance fallback history capped at twice the default 200000-byte budget. Its delivered text is clipped to `max_bytes`; stale observations use an 8000-character tail despite the `STALE_TAIL_BYTES` name. Therefore “FULL history” is a descriptive header, not lossless retention. A pane-log reread can restore material absent from a recent observation, but cannot guarantee all historical output under these caps. This is current-task context selection, not cross-task learning (SRC-1, `src/harbor/agents/terminus_2_modular/modules/observation/baseline.py`, `generations/merged_active/gen_0/modules/observation/terminal_scrollback.py`).

> command=f"tail -c {self.max_bytes * 2} '{path}'",
> --- `generations/merged_active/gen_0/modules/observation/terminal_scrollback.py`

> f"{raw[-STALE_TAIL_BYTES:]}"
> --- `generations/merged_active/gen_0/modules/observation/terminal_scrollback.py`

Editor reference context: tool-selected skill listings expose name/description/location; requested `read_file` loads the body from the allowed skill root. Large file displays over 32000 characters use roughly 14000-character head and tail regions with explicit range-read recovery; grep and line ranges afford on-demand reload, unlike baseline chat eviction. `<archive>` requests type/lineage metadata and warns on fallback. These are request-driven reads, not independent unsolicited memory pushes. The supplied runtime distinguishes editor read grants and frozen/reward-file exclusions; none is a semantic trust guarantee for content in allowed traces (SRC-1, `src/harbor/agents/terminus_2_modular/modules/tools/editor_file_tools.py`).

> if len(full) <= 32_000:
> --- `src/harbor/agents/terminus_2_modular/modules/tools/editor_file_tools.py`

## Write side

The trace-fed chain is trial result/trajectory → fixed `TrialSummary` extraction → selected investigator model → parsed finding/snapshot → append-only finding ledger → model routing/semantic clustering → proposal events → portfolio → bounded brief → edited code → gates → generation → later library consumer. Raw traces, summary fields, diagnosed claims, eligibility metadata and executable strategies remain separate. Task rewards supply contrast/reference outcomes, not automatic semantic warrant. Evidence-bearing reasons persist in the backlog and reach implementers; no source read establishes that every reason survives code generation or later solver consumption. See [MEM-RTE-evidence-brief](#mem-rte-evidence-brief), [MEM-RTE-history-contrast](#mem-rte-history-contrast) and the module-library annotation.

Admission differs by write. Software admits summaries/checkpoints using fixed schema and identity rules; investigators author findings without per-content human review; parsing/storage are weaker than proposal admission. Routing models propose interventions; clustering/state rules govern link/create/reject eligibility. Implementers author Python; the software/model gates in [RT-RTE-generation-change](runtime.md#rt-rte-generation-change) admit deployment with the supplied fail-open and post-review-repair limitations. Archive status changes, journal appends and manifest retractions are software maintenance, not new human approvals. Publicly shipped initial module/provenance content is retained as source-authored baseline; its full historical training admission is unavailable, not assumed identical to the live driver.

Rejection is not uniform forgetting. Direction rejection, implementation rejection, taboo and terminal finding disposition control future work differently. One classified bad implementation can be rebuilt from the parent using its repair brief; rejected staging is removed. Archive retirement suppresses ordinary dynamic selection but leaves files importable; cache/static/pin routes do not prove the same revocation. Journals can retain failed outcomes without any confirmed later reader. Progress and history maps separately preserve recovery inputs, subject to best-effort writes and dangling paths. See [MEM-OBJ-proposal-state](#mem-obj-proposal-state), [MEM-OBJ-implementation-record](#mem-obj-implementation-record), [MEM-OBJ-archive-entry](#mem-obj-archive-entry) and [MEM-ABS-editor-readback](#mem-abs-editor-readback).

## Read-back

The actively wired cross-window chain is an automatic reflection push assembled by software, not a foreground solver request for its own autobiography. Its trigger is completed support work; task routing and portfolio select which accumulated evidence reaches which isolated model. Proposal IDs target finding IDs; each displayed finding has a 6000-character budget, not a guarantee of complete evidence. Later task library load consumes promoted code; dynamic composer interprets filtered descriptions and archive status. Cached bundle read, historical pass lookup and checkpoint resume select different retained units with different invalidation rules. See the three memory routes and selection annotation.

Within-task QA compression supplies derived text to the next solver call after budget/overflow triggers. Observation filters decide what terminal material initially enters that context. Editor archive/skill/file actions are request-driven: the model chooses a type/lineage/path/range and gets an allowed display. A storage helper with no traced caller, including compact editor history or manifest APIs beyond the inspected callers, establishes capability only. Neither automatic delivery nor subsequent model compliance is inferred from its existence.

## Integration issues

1. **Editor-memory delivery needs narrowing.** The supplied boundary says editor memory exposes a compact history for editor use. The formatter exists, but no shipped caller wiring was found in the searched roots; source comments about the next consolidator seeing it are not enforcement. [MEM-OBJ-editor-memory](#mem-obj-editor-memory) and [MEM-ABS-editor-readback](#mem-abs-editor-readback) preserve the positive write capability and the bounded consumer absence. This does not contradict the runtime's separate proposal read-back.
2. **Installed versus released fallback differs.** [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff) is explicitly installed-baseline scoped. The annotation adds the released evaluation baseline's omission of tier-2/3 reset, preventing extension of the installed reset claim to default released evaluation. Summary failure/recovery effectiveness remains unobserved.
3. **Complete-evidence and FULL-history labels overstate display completeness.** [MEM-RTE-evidence-brief](#mem-rte-evidence-brief) caps each finding; the solver annotation shows pane-tail and display clipping. These are qualifications of source wording, not an allegation that no useful evidence arrives.
4. **Retryable is not a scheduled retry.** In `collect_evidence`, `records` comes from ingestion of the supplied snapshot, not a sweep of every previously unplaced finding. Nonterminal disposition alone therefore does not establish a future-window retry of that same finding ID. The inspected online caller supplies a newly produced window snapshot. Whether an external caller resubmits an old snapshot is uninspected. This limits [MEM-OBJ-proposal-state](#mem-obj-proposal-state) and [MEM-RTE-evidence-brief](#mem-rte-evidence-brief), not open-proposal selection across windows. Evidence: SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py`, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`.
5. **Cross-module handoff has a producer but no established consuming driver.** `dispositions.record` writes a module-specific file, while the scoped search found only helper definitions, not a shipped cross-module importer. The row carries a finding ID/reason, not a copied full finding payload. [MEM-OBJ-proposal-state](#mem-obj-proposal-state) records the retained handoff, without asserting another run actually uses it. Evidence: SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/dispositions.py`.
6. **Secondary efficiency diagnoses do not visibly enter the current persistence/selection chain.** `_reflect_once` skips an all-passing pending batch. In a mixed batch, `_contrastive_investigate_and_consolidate` persists/routes the primary snapshot before its secondary efficiency investigations; the latter only reassign local findings/culprits and the function returns None. No later ingestion of those secondary results appears in that inspected function. Thus [MEM-RTE-evidence-brief](#mem-rte-evidence-brief) establishes the primary path, not effective efficiency-only durable updates. Evidence: SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`.
7. **Resume and confirmation have different samples.** Progress restores old pending summaries and preserves old rows, but the inspected confirmation caller passes current `records`; full cross-process resumed historical confirmation coverage is not established merely by durable progress. [MEM-RTE-progress-resume](#mem-rte-progress-resume) does not assert that stronger guarantee. Evidence: SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`, `src/harbor/agents/terminus_2_modular/self_evo/confirm.py`.
8. **Identity integration.** Findings, proposal content/state, manifests, archive and journals are distinct retained parts of or inputs to [RT-RTE-generation-change](runtime.md#rt-rte-generation-change); the `Part of` fields preserve containment without redeclaring that route. The resume route spans scheduling/recovery beyond candidate admission and names the overlap. No proposed duplicate declaration replaces supplied module-library, description, selection, context or authority records; those received annotations instead. Peer epistemic/workflow records were not supplied, so possible overlaps with their later declarations remain for reconciliation.

## Limitations and checks

The source HEAD was rechecked as b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9 before inspection. The report follows the supplied memory type and records contract; the method texts and collection contract were read completely. No target code, tests, model calls, services, or fixtures were executed. Source reads and searches remain at SRC-1; no new source identity was introduced.

This is an implementation account with explicit opaque/uninspected alternatives. Model parameter state stays with [RT-CMP-lite-llm](runtime.md#rt-cmp-lite-llm); neither its weights nor provider-side memory was inspected. Individual released strategy effects, training history, actual diagnosis quality, exercised recovery, memory activation and causal improvement remain unestablished. The inventory does not convert available but uninspected files into absences. Syntax/quotation validation cannot establish these semantic properties.

Validation: the invocation-specific `commonplace-run validate-output` check passed after disambiguating one quotation attribution. This establishes output form and quotation occurrence, not semantic acceptance.

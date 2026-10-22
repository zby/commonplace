---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Harness² memory: full-tree experience libraries, trace-derived reflection, reconstructed evidence frames and recovery caches."
run-id: AAS-2026-10-22-harness2-d5a180ba559c-01
source-identity: https://github.com/google-research/harness2
reviewed-boundary: "1cfe254e8d25b15f37048c3730134686abe60335"
---

# Harness² memory report

## Boundary and evidence

The subject is the shipped improvement framework at SRC-1 commit `1cfe254e8d25b15f37048c3730134686abe60335`, not the complete external OpenCode/Codex runtimes. Memory includes adopted harness trees and experience, task-local execution evidence reconstructed for later model sessions, and recovery caches. Static baseline instructions and current solver turns are described as working-context inputs, not automatically classified as retained experience. External provider parameters, native compaction payloads and delegated conversations remain opaque. The source identity and exclusions are those of [boundary](boundary.md#boundary-and-evidence).

Direct reads added implementation coverage of `harness2/core/library.py`, the construction/rendering branches of `harness2/core/context.py`, reflection/parsing in `harness2/core/selection.py`, library restore/admission/prefix handling in `harness2/core/schedule.py`, proposer copy/harvest/cache/fingerprint logic in `harness2/core/proposer.py`, sequential history in `harness2/core/recursion.py`, substrate rendering/configuration, `harness2/cli/demo.py`, `harness2/demo.py`, `harness2/cli/bridge.py`, and WorkBuddy compaction configuration in `third_party/wb_runner/agents/oc_agent.py`. Prompt passages in `harness2/core/prompts.py` are doctrine/design, not observed compliance. Supplied runtime findings cover the wider rollout, selection, launcher, permissions and CLI paths. Source searches checked installed CLI destinations, library operations, truncation, skills, delegation and compaction in included core, adapters and bundled runners. Available but unread bodies are not access gaps.

| Entry point or memory operation | SRC-1 source paths | Coverage and limits |
|---|---|---|
| Sweep/domain task admission and restore | `harness2/cli/run_sweep.py`, `harness2/core/schedule.py` | Supplied [RT-RTE-task-recursion](runtime.md#rt-rte-task-recursion), [RT-RTE-resume-reuse](runtime.md#rt-rte-resume-reuse); direct reads of mode admission, restore and preceding-task restriction. |
| Library writes, reads, deletion, indexing | `harness2/core/library.py` | Direct complete read; [MEM-OBJ-experience](#mem-obj-experience), [MEM-OBJ-library-index](#mem-obj-library-index), [MEM-RTE-library-withdrawal](#mem-rte-library-withdrawal); `tree_of` is a storage API, not independently a later model-consumer route. |
| Reflection and lesson parsing | `harness2/core/selection.py`, `harness2/core/prompts.py` | Direct reads; annotation on [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission). Rejected candidates can contribute lessons; NO_ENTRY can retain edit rows without a library entry. |
| Sequential history and fresh evidence | `harness2/core/recursion.py`, `harness2/core/context.py` | Direct reads; [MEM-RTE-evidence-frame](#mem-rte-evidence-frame). Pool/history and decision files survive between model invocations, not their private conversations. |
| Trajectory selection and budgets | `harness2/substrate/opencode.py`, `harness2/substrate/codex.py`, `harness2/benchmarks/jobbench.py`, `harness2/benchmarks/lab.py`, `harness2/benchmarks/workbuddy.py` | Direct OpenCode renderer read, adapter/substrate searches and supplied runtime; [MEM-OBJ-evidence-tree](#mem-obj-evidence-tree). Codex event variants not exhaustively read: exact variant completeness remains unestablished. |
| Proposer audit/cache and temporary cleanup | `harness2/core/proposer.py` | Direct reads; [MEM-OBJ-cached-response](#mem-obj-cached-response), [MEM-OBJ-call-fingerprint](#mem-obj-call-fingerprint); resume annotation. |
| Always-on memory, skills, subagents, plugins, hooks | `harness2/substrate/opencode.py`, `harness2/substrate/codex.py`, bundled runner trees | Direct surface/advertisement reads plus supplied [RT-BAP-harness-consumption](runtime.md#rt-bap-harness-consumption). Lifecycle hook names are accepted extension opportunities, not evidence of an implemented summarizer. External subagent return contents, skill eviction and compacted checkpoint forms are uninspected; cannot claim complete model-window reconstruction. |
| WorkBuddy native compaction configuration | `third_party/wb_runner/agents/oc_agent.py`, `third_party/wb_runner/agents/codex_agent.py` | Direct OpenCode config reads and bounded searches; [MEM-CLM-compaction-boundary](#mem-clm-compaction-boundary). No native compaction implementation frozen. |
| Judge/report and setup/check | `harness2/core/judge.py`, `harness2/cli/report.py`, `harness2/cli/setup.py`, `harness2/cli/check.py` | Supplied runtime plus scoped searches: measurement/reporting and installation/preflight, not additional lesson consumers established here. Their full bodies were not audited for every retained operational datum; no exhaustive cache inventory claimed. |
| Deterministic demo | `harness2/cli/demo.py`, `harness2/demo.py` | Direct reads; [MEM-CLM-demo-experience](#mem-clm-demo-experience). Same scheduler/library, scripted rather than model-generated lesson. |
| Provider bridge | `harness2/cli/bridge.py` | Direct complete read: saves port/key and renders provider configuration. Operational configuration, not a trace-derived knowledge mechanism. Remote service retention is uninspected. |

No target, test or example was executed. No observed-run or causal-experiment evidence was supplied. Positive implementation findings therefore establish wiring or affordances, not use, valid lessons or improved capacity.

## Core ideas

1. **Retention is full-tree exemplars plus explanations, not automatic solver memory.** Each accepted task entry keeps the adopted tree, choice reason and model-written cue/lesson/evidence. The later improver receives the library as files and is invited to browse an index. It must copy/adapt material into a new accepted harness before that material acquires solver authority. See [MEM-OBJ-experience](#mem-obj-experience), [MEM-OBJ-library-index](#mem-obj-library-index) and [RT-BAP-harness-consumption](runtime.md#rt-bap-harness-consumption).
2. **Reflection is a trace-fed transformation with weak semantic admission.** The requested derivation is raw executions → rendered comparisons and edit rows → at most one transferable lesson. The implementation validates fields and marker strings, not whether the evidence entails the lesson. Rejected candidates are evidence too; adoption alone is explicitly insufficient. See the annotation on [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission).
3. **Files replace a growing shared conversation.** Later stages receive reconstructed evidence frames, including prior decisions/history; per-session temporary workspaces disappear after harvesting. The on-disk inventory can be much larger than the model actually reads. Renderer limits and names-only branches qualify the source's “FULL trajectories” and canonical-rendering labels. See [MEM-RTE-evidence-frame](#mem-rte-evidence-frame).
4. **Withdrawal and recovery operate at different layers.** Prefix retention deletes library entries, while saved summaries can replay admission and audit caches can reuse a response/workspace. Removing a library directory is not demonstrated global revocation of every derived harness or old evidence copy. See [MEM-RTE-library-withdrawal](#mem-rte-library-withdrawal) and the resume annotation.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-experience
Label: EXPERIENCE.md

Source-native identity: per-task `harnesses/<task>/EXPERIENCE.md`, a natural-language explanation on local disk. Distinct from the retained instruction/code objects [RT-OBJ-harness-text](runtime.md#rt-obj-harness-text) and [RT-OBJ-harness-code](runtime.md#rt-obj-harness-code): this document explains adoption and transfer rather than being automatically installed as the next solver harness. It is an output of [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission), not a duplicate route.

Lineage: selection reason plus parsed reflection fields and optional edit rows; task/label/run references and component inventory are rendered by code. Required fields are cue, lesson and evidence; confidence and edits are optional. The model authors the substance; software checks admissibility and writes it; no human content approval is wired. The initial adopted harness can originate from the shipped base or accepted/fallback edits; an adopted tree need not be newly changed. Later improvers receive copies with the full tree; rationale is retained and readable but actual reading is not observed. No executable authority attaches to an evidence/confidence label. SRC-1: `harness2/core/library.py`, `harness2/core/selection.py`; [RT-RTE-edit-admission](runtime.md#rt-rte-edit-admission).

> if exp.get("edits"):
>     lines += ["## What each edit did", str(exp["edits"]).strip(), ""]
> --- `harness2/core/library.py`

> for f in ("cue", "lesson", "evidence", "confidence")
> --- `harness2/core/library.py`

#### MEM-OBJ-library-index
Label: INDEX.md

Source-native identity: domain `INDEX.md`, locally regenerated Markdown. Natural-language navigation text and symbolic relative file addresses are consumed by the improver's reading/tool choices, not by a relevance-ranking engine. It is distinct from [RT-OBJ-harness-text](runtime.md#rt-obj-harness-text): access metadata, not the harness instructions themselves. No supplied object counterpart after comparison.

Lineage: directory enumeration, each entry's cue extracted from EXPERIENCE.md, and component counts/always-on character census read from its tree. The index is a readable summary, not the underlying experience or executable payload. Authoring is deterministic software with no per-index human admission. Domain/mode scoping supplies the coarse filter; entry relevance remains model judgment. All eligible library files are copied, not only a ranked subset. SRC-1: `harness2/core/library.py`, `harness2/core/context.py`.

> "Each entry is an earlier task in THIS domain whose harness was chosen, stored "
> "with its FULL component tree and why it was picked. Browse this index, then "
> "open the entries that look relevant to the matter in front of you.",
> --- `harness2/core/library.py`

#### MEM-OBJ-evidence-tree
Label: ContextTree evidence files

Source-native identity: constructed `context` file tree. Distinct from harness-only [RT-OBJ-harness-text](runtime.md#rt-obj-harness-text) and [RT-OBJ-harness-code](runtime.md#rt-obj-harness-code); those are copied parts, whereas this container also holds task/source, trajectories, decisions, artifact renderings/listings and pool diffs. It is not a new underlying solver conversation.

Substrate: local directories rebuilt from adapter reads, saved task artifacts and library copies. Textual task/trajectory/decision material has natural-language/model-interpreted form; candidate code is delivered for reading as text, not executed by the builder. Diff syntax, labels, filenames and listings are symbolic structure; raw images/binaries are separate copied assets whose semantic interpretation depends on external readers. An opaque artifact is not replaced, for analytical purposes, by its display summary. Raw rollout JSONL is serialized event evidence on disk; the builder delivers rendered text, not necessarily every raw field. Trace origin is mixed: solver messages/tool observations, benchmark task/source data, generated artifact content and proposer decisions. Ground-truth provenance of tool observations is not independently authenticated. SRC-1: `harness2/core/context.py`, `harness2/substrate/opencode.py`.

Curation includes filtering declared leak paths, marker rejection, observation/argument clipping, event-schema filtering, artifact conversion, names-only withholding, and deterministic harness diffs. These operations do not themselves validate factual content. Library copying adds no semantic compression. Later consumers are proposal, composition and reflection sessions; selection has its own independent artifact path described by [RT-RTE-output-selection](runtime.md#rt-rte-output-selection).

> trunc = obs_trunc if obs_trunc is not None else adapter.spec.obs_trunc
> --- `harness2/core/context.py`

> shutil.copytree(library_dir, dest / "library", dirs_exist_ok=True)
> --- `harness2/core/context.py`

#### MEM-OBJ-cached-response
Label: Cached proposer response

Source-native identity: audit `<label>.<fingerprint>.response.md`, natural-language model reply on local disk. Distinct from [RT-OBJ-harness-text](runtime.md#rt-obj-harness-text): reply prose is not itself the installed harness; harvested workspace files carry the proposed tree. Closest supplied route is [RT-RTE-resume-reuse](runtime.md#rt-rte-resume-reuse), which already notes proposer caching.

Lineage: subprocess reply after a nonempty response, with failure audits also possible. Cached nonempty responses are reused under the call key; harvesting callers additionally require a saved workspace directory. Read-back supplies a Reply to code instead of a fresh session, potentially feeding parsing/admission. This is reuse of earlier generated content, not a new semantic lesson transformation. Cache admission checks existence/nonempty text and optional workspace, not lesson truth. Audit metadata is separate symbolic accounting and does not certify response validity. SRC-1: `harness2/core/proposer.py`.

> if require_workspace and not p["workspace"].is_dir():
>     return None
> txt = p["response"].read_text(encoding="utf-8", errors="replace")
> if not txt.strip():
>     return None
> --- `harness2/core/proposer.py`

#### MEM-OBJ-call-fingerprint
Label: Call fingerprint

Source-native identity: `_call_fingerprint` truncated SHA-256 key, symbolic access metadata encoded in cache filenames. Local string/path substrate, not semantic memory or distributed model state. Distinct from [MEM-OBJ-cached-response](#mem-obj-cached-response), whose content is reused, and the harness fingerprint described in [RT-RTE-resume-reuse](runtime.md#rt-rte-resume-reuse), whose object/predicate differs.

Lineage: label, mission, system text, resolved evidence-directory path, sorted relative filenames and file bytes, skipping `__pycache__`; read errors contribute an error token. Consumer is proposer cache lookup. It selects exact keyed reuse, not task relevance. No model reasoning or human approval is involved. The inspected hash inputs do not include the channel model name itself, so namespace/model configuration controls must not be conflated with this function. SRC-1: `harness2/core/proposer.py`.

> for value in (label, mission, system):
> --- `harness2/core/proposer.py`

> return h.hexdigest()[:16]
> --- `harness2/core/proposer.py`

### Routes

#### MEM-RTE-evidence-frame
Label: Reconstructed evidence frame

Distinct identity: the common selection/render/copy/session-lifetime mechanism spans [RT-RTE-task-recursion](runtime.md#rt-rte-task-recursion), [RT-RTE-edit-admission](runtime.md#rt-rte-edit-admission) and [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission); it is not a replacement for any one of them. Trigger: code enters an improvement/composition/reflection stage. Code builds the evidence tree, copies it into a new subprocess session and harvests designated edits/reply. Context effects are specified below; software chooses supplied inputs and the model decides which files to open. No human review occurs at each copy. Content admission remains the separate tree/experience routes, not a consequence of successful file I/O. SRC-1: `harness2/core/context.py`, `harness2/core/proposer.py`, `harness2/core/recursion.py`, `harness2/core/schedule.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ContextTree inventory, then Reply and optional harvested harness workspace; errors can trigger stage fallback.
- Later read-back: accumulated prior compositions, rollout views, decisions and prior-task library are reconstructed as files for subsequent model invocations; full library copying is coarse automatic supply, while browsing individual entries is model-requested reading.
- Delegated visibility: each session gets selected files, not sibling/private conversations; solver and authored subagent contexts remain separate external runtime frames.
- Selection predicate: caller-supplied rollout/pool/history and current harness, adapter task/source/leak rules and deliverables mode, plus domain/mode/preceding-task library membership. There is no code-level cue similarity ranking or top-k retrieval in the inspected library/context path.
- Invalidation or expiry: builder replaces its destination; session tmp is removed in finally; saved task evidence, audit response and harvested tree can outlive the session. Withdrawal of originals does not establish deletion of copies.
- Activation or effect: changes what is reachable through model tools and what edits escape; model attention, compliance and downstream behavioral change are unobserved.
- Evidence limits: file availability is not model-window inclusion; external token limits, native compaction, native skill/subagent returns and provider/tool memory are not fully inspectable here.

> finally:
>     shutil.rmtree(tmp, ignore_errors=True)
> --- `harness2/core/proposer.py`

Working-context control: this resembles a stack frame for supplied context and harvested return, but not a security sandbox or reference-counted heap. Popping the temporary frame removes files, not every audit/copy; retained files require explicit tools to bring their contents into the model window. Sequential recursion retains current composed harness plus history and decisions; it reconstructs later frames instead of preserving an ever-growing foreground conversation. The library is not automatically installed for solvers: SRC-1 `harness2/core/prompts.py` requests copying relevant material into the current tree.

Budgets and loss: `context.build` does not impose a library top-k or total prompt-token budget. SRC-1 `harness2/substrate/opencode.py` clips text/observations and tool arguments and takes a prefix when `max_chars` is exceeded. Adapter trajectory caps are JobBench 8,000,000 characters, LAB 10**9 and WorkBuddy 2,000,000; the adapter/source searches found normal observation budgets of 50,000 and OpenCode's default argument budget is 400. Codex has a separate default argument budget of 2,000. These are render budgets, not context-window guarantees. Names-only mode returns listings before the artifact-body/image/raw branches, while contents mode can preserve rendered text, up to eight images on that branch, and raw originals. Thus “FULL trajectories” means no extra prompt-fitting cut in the builder, not lossless raw evidence.

> if len(rendered) > max_chars:
>     dropped = len(rendered) - max_chars
>     rendered = rendered[:max_chars] + "\n" + _TRUNC_FMT.format(n=dropped)
> --- `harness2/substrate/opencode.py`

#### MEM-RTE-library-withdrawal
Label: Library prefix withdrawal

Distinct from [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission), which mentions retain/forget but owns admission: this is the deletion/reindex operation and its later-consumer consequence. Trigger/owner: before each domain task, scheduler calls retain with preceding task IDs; explicit Library.forget/retain calls afford the same filesystem mutation. Software decides membership from the supplied task list, not human per-entry approval. Generic API caller identity leaves external human control unresolved. Changes are physical removal and deterministic index reconstruction, not content-directed criticism or lesson revision. SRC-1: `harness2/core/library.py`, `harness2/core/schedule.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: deleted entry directories and rebuilt INDEX.md if removals occurred; no semantic rejection report.
- Later read-back: subsequent library context copies omit removed entries; later summary resume can reconstruct eligible prior admissions.
- Delegated visibility: no broadcast to already running/copied model frames is wired in this mechanism.
- Selection predicate: keep set is slugged preceding task IDs; forget addresses named task entries and ignores unknown directories.
- Invalidation or expiry: full entry directory removal; same-task add replaces its harness directory and experience, without a general rollback history. Existing task artifacts/summaries remain a separate recovery source.
- Activation or effect: prevents future library copies from supplying those entries at that point in the task stream; it does not revoke derivative instructions already copied into another harness.
- Evidence limits: no global dependency invalidation, remote erasure or semantic correction propagation is established by these functions; no observed deletion or recovery trace supplied.

> for lib in libs.values():
>     lib.retain(task_ids[: i - 1])
> --- `harness2/core/schedule.py`

> if d.is_dir():
>     shutil.rmtree(d, ignore_errors=True)
>     removed = True
> --- `harness2/core/library.py`

### Claims

#### MEM-CLM-compaction-boundary
Label: External compaction configuration

Claim/finding: SRC-1 `third_party/wb_runner/agents/oc_agent.py` comments that OpenCode derives its compaction threshold from declared context limit and writes that limit when configured. Native-provider mode returns before constructing this provider model entry. The constructor also accepts `context_compact_pct`, but a bounded search of this file found its assignment and no later use. This is distinct from [RT-RTE-solver-execution](runtime.md#rt-rte-solver-execution): it qualifies working-context configuration, not a new observed solver route.

> # OpenCode reads the compaction threshold off the model's declared context limit.
> if self._context_window is not None:
>     model_entry["limit"] = {"context": self._context_window}
> --- `third_party/wb_runner/agents/oc_agent.py`

- implementation conclusion status: wired
- operation conclusion status: uninspected

The wired finding covers only this configuration path; actual compaction is uninspected. The frozen source does not supply the external compactor's summary, verbatim tail, checkpoint alternatives, selection policy, later consumer payload or reload behavior. Codex accepts PreCompact/PostCompact hook names in its surface; that affords authored lifecycle behavior, not evidence that a particular memory update is installed. Missing external internals prevents claims of lossless compaction or trace-derived learning through those opaque routes. No absence of compaction is asserted.

#### MEM-CLM-demo-experience
Label: Deterministic demo experience

The shipped demo is an alternate source of library content through the same scheduler. It uses DemoProposer's fixed text and script replacement, not the selector model. Its choice computes a signed ledger total from task data, providing a task-derived expected outcome in this demo, unlike the ordinary model-selection account. It does not establish ordinary-model oracle access. No supplied object counterpart; closest route is [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission), whose model-authorship statement needs this scope qualifier. SRC-1: `harness2/cli/demo.py`, `harness2/demo.py`.

> class DemoProposer(Proposer):
>     """Scripted edits and selection; no model service or benchmark judge is used."""
> --- `harness2/demo.py`

> "<experience>\ncue: When a ledger includes credits and debits\n"
> "lesson: Include both signs when summing in scripts/summarize.py.\n"
> --- `harness2/demo.py`

Wiring is inspectable, demo execution unobserved. Its apparent observation/confidence wording is scripted, not empirical evidence of the present run. It does not furnish independent support for learning or transfer.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-harness-text](runtime.md#rt-obj-harness-text)

Memory-specific lineage: baseline files can be transformed through model-authored edits, inherited unchanged on failure, retained wholesale after adoption and copied into later improver evidence. `LongTermMEMORY.md` is an always-on text component, not a separate automatically maintained fact service. Its baseline placeholder explicitly starts empty. Codex folds always-on prose into AGENTS.md; skills/subagents advertise descriptions while bodies are loaded/delegated on demand. Surface code sets always-on caps of 24,000 characters for OpenCode and 8,000 for Codex; the claim about Codex's additional 32,768-byte truncation is a source comment, not independently inspected external enforcement. SRC-1: `harness2/substrate/opencode.py`, `harness2/substrate/codex.py`.

> <!-- c3 memory. EMPTY in v0. Evolution adds durable, GENERAL domain facts here (never task-specific answers). -->
> --- `third_party/jb_runner/harness_baseline_oc/LongTermMEMORY.md`

The external solver interprets installed prose; future improvers interpret library exemplars first. Initial general-fact truth/provenance and actual subsequent use are not established by this filename. The body/description split saves always-on context but native eviction/reload mechanics remain outside the inspected runtime boundary.

#### On [RT-OBJ-harness-code](runtime.md#rt-obj-harness-code)

Retained library trees preserve code as well as prose, not only readable index inventories. In improver contexts code is evidence to inspect; after copying/admission/materialization it can acquire interpreter/plugin/hook authority. The inventory summary does not establish the behavior or safety of the underlying payload. A later library reader is not thereby a code executor. Source support and consumer limits are supplied by [RT-BAP-harness-consumption](runtime.md#rt-bap-harness-consumption) and direct library/context reads, SRC-1 `harness2/core/library.py`, `harness2/core/context.py`.

#### On [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission)

Trace-fed update: reflection builds evidence from task-local rollouts, selected harness, all non-base candidate harnesses/rollouts, decisions, copied base harness and adoption JSON. `_distil` duplicates that tree excluding selection.json and invokes the selector channel. It extracts edits separately, saving edits.md before it checks for a valid experience block. Required fields are parsed one line at a time from colon-separated text; missing block/required values produces no experience. A NO_ENTRY reply without a block therefore skips admission while edit rows may survive locally. The guard does not enforce exclusivity if a reply also contains a valid block. SRC-1: `harness2/core/selection.py`.

> edits = _EDITS.search(reply.text)
> if edits:
>     (root / "edits.md").write_text(edits.group(1).strip() + "\n", encoding="utf-8")
> m = _EXP.search(reply.text)
> if not m:
>     return {}
> --- `harness2/core/selection.py`

Requested transformation: compare every candidate with base, attribute each changed component's execution contrast, prefer confounded over invented causal attribution, then retain at most one transferable operation with a cue. Thus rejected candidates may inform the derived lesson. Neither selecting the best deliverable nor retaining a confidence string validates the lesson. No separate human lesson approval is wired. Code performs field/marker admission; the model supplies substantive judgments. The ordinary model route and scripted demo authorship are distinct, see [MEM-CLM-demo-experience](#mem-clm-demo-experience).

> "output read best -- not which edit worked. Treat every candidate as evidence. An edit "
> "that appeared only in a rejected candidate may still be the one that changed behavior "
> "for the better, and an edit inside the adopted candidate may have contributed nothing "
> "to why it was adopted. Read the trajectories, not the verdict.",
> --- `harness2/core/prompts.py`

The durable behavior-shaping result is a full adopted tree plus [MEM-OBJ-experience](#mem-obj-experience), not raw logs alone. Reasons can survive in selection why, edit rows and evidence fields; the full raw trace is not copied into every library entry. Run/label references and the task-local record remain a separate lineage trail. Later improvers can read those reasons in library files, but actual reading and faithful reasoning are unobserved. Trace-fed update wiring does not establish improved capacity, successful self-improvement or reliable criticism.

#### On [RT-RTE-resume-reuse](runtime.md#rt-rte-resume-reuse)

Read-back details: `_restore_libraries` loads saved chosen trees through the surface reader and reuses saved why/label/run/experience via Library.add when selection is successful and experience fields exist. It reconstructs entries rather than rerunning reflection; restored evidence quality is only as good as the saved content and admission checks. Full adopted tree and explanation are recovered, not the private reflection session. SRC-1: `harness2/core/schedule.py`.

> """Replay a skipped task into its libraries from the saved chosen harness."""
> --- `harness2/core/schedule.py`

Proposer read-back is separate: [MEM-OBJ-call-fingerprint](#mem-obj-call-fingerprint) selects [MEM-OBJ-cached-response](#mem-obj-cached-response) and, for harvesting calls, a saved workspace. This is exact-key request/return reuse rather than unsolicited semantic retrieval. CLI namespace model identity checks are not proof that the lower-level key pins model parameters. Cache storage does not imply deployment-wide provenance authentication or semantic correction propagation.

## Write side

The acquisition/admission chain is intentionally layered. Task source files and rendered executions enter evidence by software copying/filtering; no per-file human content decision is established. The proposer authors disk edits, code admits/retries/falls back, and solver executions produce traces/artifacts. Reflection transforms that material into edit rows and possibly a lesson. Library.add admits only qualifying experience and marker-clean tree/text, replaces that task's saved tree and rebuilds navigation. These layers have different authority and checks; starting the workflow is not approving each derived lesson. See [RT-RTE-edit-admission](runtime.md#rt-rte-edit-admission), the experience annotation and [MEM-RTE-evidence-frame](#mem-rte-evidence-frame).

The raw-to-derived chain reaches a later consumer: serialized executions → budgeted rendered evidence plus candidate diffs/decisions → reflection text → retained tree/experience/index → later improver's file tools → newly admitted harness → external solver. Only the last installation path grants direct solver authority. The framework requests causal caution but does not verify content-directed criticism; learning and transfer remain unobserved. Native compaction has no comparably inspectable derived-payload chain here, see [MEM-CLM-compaction-boundary](#mem-clm-compaction-boundary).

Maintenance includes deterministic reindexing, same-task replacement, prefix withdrawal and replay from summaries. A rejected proposal falls back, failed/malformed reflection can skip library admission, and edit rows can outlive refusal to write a transferable entry. [MEM-RTE-library-withdrawal](#mem-rte-library-withdrawal) is structural cleanup, not demonstrated truth maintenance. No unwarranted inference of global revocation is made.

## Read-back

The primary cross-task route is automatic domain/mode/prefix filtering and full-directory supply, followed by model-directed index browsing and file opening. Cue text is retained to guide judgment, not used by a code ranker. There is no code-level per-entry relevance budget in this path. This is not automatic installation of all remembered instructions. The later improver chooses what to copy/adapt, then ordinary admission/materialization separates suggestive evidence from executable solver organization. SRC-1 `harness2/core/library.py`, `harness2/core/context.py`, `harness2/core/schedule.py`; [MEM-RTE-evidence-frame](#mem-rte-evidence-frame), [RT-BAP-harness-consumption](runtime.md#rt-bap-harness-consumption).

Within-task read-back carries current composed trees, previous history, rendered executions and decision notes into fresh stages. These are retained between model invocations even within one task. Observation clipping/prefix caps, failed rendering placeholders and names-only withholding govern the actual delivered record. Selection independently renders eligible outputs, so proposer withholding is not a universal secrecy guarantee. Summary/rollout/proposer caches return prior decisions or outputs under distinct identity/integrity predicates rather than requesting a new judgment. See [RT-RTE-output-selection](runtime.md#rt-rte-output-selection), [RT-RTE-resume-reuse](runtime.md#rt-rte-resume-reuse) and their memory annotations.

Native solver skill loading, delegated subagent isolation and compaction are context-management surfaces, but their detailed retained payloads and return selection depend on excluded external implementations. Static skill bodies are not automatically trace memory; newly authored retained skill bodies can be. Accepted lifecycle hooks are extension affordances rather than proof of a particular trace-to-memory writer.

## Integration issues

- **Scope qualifier for full-trajectory language.** [MEM-RTE-evidence-frame](#mem-rte-evidence-frame) qualifies the source builder's “FULL” label and the supplied runtime's context description: renderers can clip individual messages/arguments and whole rendered prefixes. Evidence: SRC-1 `harness2/substrate/opencode.py`, adapter trajectory methods and scoped Codex renderer search. This prevents treating reflection as necessarily receiving every raw observation. It does not contradict runtime's existing observation-truncation caveat.
- **Alternate authorship/oracle case.** [MEM-CLM-demo-experience](#mem-clm-demo-experience) qualifies model-authorship and answer-oracle generalizations in [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission) and [RT-RTE-output-selection](runtime.md#rt-rte-output-selection): demo uses a scripted proposer and a computed ledger reference outcome. This is a distinct shipped mode, not evidence of ordinary model oracle exposure.
- **No proposed duplicate declarations.** New objects distinguish experience/navigation, constructed evidence and response/key metadata from supplied harness objects. [MEM-RTE-evidence-frame](#mem-rte-evidence-frame) spans several existing runtime routes; [MEM-RTE-library-withdrawal](#mem-rte-library-withdrawal) isolates their mentioned deletion operation. Annotations retain existing referents rather than redeclaring them.
- **Opaque native memory.** [MEM-CLM-compaction-boundary](#mem-clm-compaction-boundary) and [RT-RTE-solver-execution](runtime.md#rt-rte-solver-execution): external compaction checkpoint forms, retained reasons, later consumer payloads and native delegated return/eviction policies remain unresolved. Configuration comments/hook event names cannot settle them. Prevents a complete external working-window account, not the framework library characterization.
- **Withdrawal is not global invalidation.** [MEM-RTE-library-withdrawal](#mem-rte-library-withdrawal) and [RT-RTE-resume-reuse](runtime.md#rt-rte-resume-reuse): copies, derivative harnesses and saved summaries have separate lifetimes. No observed trace establishes semantic correction propagation or irreversible erasure.
- **Capacity and rationale use remain unobserved.** The experience annotation establishes a wired trace-fed retained result and a later consumer opportunity, not improved capacity, actual content-directed criticism, later rationale use or causal benefit. No generated experience artifact was supplied. Native provider state and exact model weights remain opaque as in the runtime components.

## Limitations and checks

Source HEAD was rechecked as `1cfe254e8d25b15f37048c3730134686abe60335`. The invocation's job, member/peer types, collection, worker rules, complete records contract and exact supplied boundary/runtime were read, recovering range continuations before proceeding. No prior analysis, external paper, target execution or additional source identity was used. Direct source inspection challenges complete/lossless context claims, universal model authorship and the interpretation of withdrawal as global revocation. It does not measure learning, transfer, deployment isolation or provider behavior. Detailed uninspected native payloads and available-but-not-exhaustively-read paths are recorded beside their prevented conclusions above.

Validation: the required role-specific commonplace-validate check passed; this establishes structural/citation/quotation checks, not analytical correctness or acceptance.

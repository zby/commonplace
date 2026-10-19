# Batch 23 JAZ exact-publication audit

## Disposition

**hold** — two consequential defects remain in these exact bytes: replay lacks its implemented sequential-nesting precondition, and the profile falsely marks workflow input-origin coverage complete. Generic partial-coverage caveats do not identify the first failure or qualify the second extracted unit. This is a bounded audit, not a replacement analysis or integration authorization.

## Identity and current binding

- run-id: `AAS-2026-10-19-jaz-9d991c410bb9-01`
- method-commit: `3e2491c83a4613d410511af8c3cfde30f4b67689`
- source-revision: `0803d4971be785e95b80054b02259664d70fa3da`
- Source identity: `https://github.com/jaz-lang/JAZ`, SRC-1.
- Auditor profile: independent Pi session, `openai/gpt-6.1-sol`, `medium`, verified through `PI_PROVIDER`, `PI_MODEL`, `PI_REASONING_LEVEL`; no delegation.
- W: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-23-jaz`.
- R: `W/kb/agentic-system-analyses/state/AAS-2026-10-19-jaz-9d991c410bb9-01`.
- P: `W/kb/agentic-system-analyses/retained/jaz-lang--jaz`.
- S: `W/related-systems/jaz-lang--JAZ`.
- T: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/batch-23/jaz.output`.
- Preparation: sibling `batch-23-jaz.preparation.json`; command prefix `W/.venv/bin`.

Fresh SHA-256 checks match **all 109 source entries, 13 publication members and 157 run entries** in [intake cases.jaz](../batch-23-audit-intake.json). P has exactly the recorded filenames. Preparation is `ready`, token `9d991c410bb9`, and binds W, method and prefix; that prefix's validator exists. W HEAD equals method-commit; S HEAD equals source-revision. S status is clean; W status shows only the untracked publication. R parameters bind the source, command prefix and `pi-sol` profile. No incumbent is assigned; origin's JAZ checklist still distinguishes pending JAZ from completed **jaz-evals**.

Independently rehashed preparation `9e273d8f32aa3ea0cfaad6e59ab7a56bec3b164f2dda677db0d8d93bf949e08e`, publication effect `fde6540b36aa4278aca8c85e2ed89349ff12cdcc1702a4ab9dee2f39e8cfbbef`, and T `a9353e4477843ef0cf6482ca60446075a7a9d0a7c15539d4fa25c091278fb2e8`. The completed `R/effects/publish.json` names this run/source/P and its entire `new` map equals intake's publication map. Key published bytes: manifest `ece1588b53948dd1b8297ebee6092e13fe611b27a3e88ad2e4aaeaefa3d0aa68`; profile `621447ec54e75aa3d6e71a6e1d1d5ab035f9f713e8e60a7ea941673ab606bb87`; synthesis `24dd73cbaffe85f873e5af17a2086c8e3af51ac873e376f150014ccf70b52812`. The working manifest is a different type declaration, not publication drift.

## Inspection and historical boundary

Read the commission, audit procedure and workshop README completely, plus the work/analysis collection contracts and applicable set, overview, synthesis, verification and memory-profile types. Inspected complete current boundary, overview, synthesis and three verifications; selected runtime, epistemic and profile passages; decisive frozen-source ranges; selected settled worker histories and retained attempts. This is discrepancy-led coverage, not an all-member or all-source reanalysis.

Read all three intake historical audit leads and the systems-linked archived JAZ review. Their revision strings match this JAZ pin, but historical prose and trace findings were not treated as source truth. The jaz-evals audit concerns a different repository/revision and establishes no JAZ evaluation result. No historical trace was replayed or acquired.

The current synthesis retains the important historical distinctions: controls versus semantic correctness, host grants versus containment, raw-worker parentage, live console objects versus helper text, replay versus safe restoration, abnormal/pre-edit workflow emission versus successful execution, and exported samples versus installed learned weights. Withholding benchmark, reflection and improvement conclusions is not a coverage defect. The two old JAZ hold themes required fresh source checks below; neither historical hold is cleared by publication success.

## H1 — Known replay precondition replaced by generic uncertainty

**Current text:** P `runtime.md:247–260`, `RT-RTE-trajectory-replay`, associates saved queues with live invokes and describes node-local selection/withdrawal. Its qualification says concurrent ownership was not audited end to end. `EPI-RTE-replay-comparison` similarly leaves concurrency uninspected. Synthesis, “What survives and reaches later work,” and its replay limitation carry only partial concurrency/equivalence coverage. None states the implemented sequential-nesting condition or sibling misrouting consequence.

**Fresh source:** S `src/jaz/hooks/builtin/replay.py:393–400` explicitly declares `SEQUENTIAL INVOKES ASSUMED`: interleaved `ainvoke` calls can receive a sibling's queue and latch another invocation's divergence. Implementation at `509–541` confirms it: entry takes the stack-top parent's next child and pushes it; query-send selects `_invoke_stack[-1]` rather than matching the query's invocation ID. This establishes a static counterroute, not an observed concurrency incident.

**Consequence:** saved responses direct executable Python. “Concurrency uninspected” does not tell readers that invocation-local serving and withdrawal require strictly nested execution and can otherwise affect the wrong invocation. The synthesis type requires preservation of conditions changing operation or guarantees. General no-fidelity/no-rollback disclaimers do not identify this authority-selection defect. The historical warning remains source-supported at the exact current pin.

**Unblock:** a separately authorized new publication must state the sequential-nesting condition and sibling queue/divergence misattribution in the relevant records and public synthesis, or justify and explicitly narrow the reviewed replay scope to exclude that counterroute. Revalidate and re-audit changed bytes. No concurrent target execution is needed to decide this finding.

## H2 — Unsupported complete workflow input-origin classification

**Current text:** P `memory-profile.md:997–1018` marks “Workflow materialization input” `known`, with `tool-traces` and `session-logs` findings. Other unresolved units concern rollout conditioning, raw histories/helper settings and remote policy updates, not the workflow's merged namespace. Axis-level `partial` and the generic note about mixed inputs do not qualify this `known` unit. Profile verification expressly accepts it without a blocker.

**Fresh source:** S `src/jaz/hooks/builtin/workflow_replay.py:180–197` stores `inputs={**event.scope, **inputs}` as the full bound namespace. The source explains that this becomes generated function parameters and reconstructed main-call arguments. Lines `454–463` and `485–494` enumerate these values and emit their `repr` into executable output. The workflow write therefore consumes original inputs and resolved scope, not just recorded session code and execution feedback. P `RT-RTE-workflow-emission` withholds exhaustive object reconstruction but supplies no complete original-content/origin classification for those values.

**Consequence:** comparison consumers extracting this unit receive a false complete assessment. The memory-profile type defines `known` as complete within the named scope and includes mixed/opaque original inputs in `trace_source`; the verification type forbids excusing false `known` with a synthesis caveat. The supported positive findings need not be removed, but the unresolved workflow branch cannot be omitted to obtain completeness. This independently confirms the earlier hold theme; no arbitrary payload reconstruction was attempted.

**Unblock:** under separate authority, retain the unresolved merged-input/scope branch in the profile's assessment, scope and explanation, or establish its complete classification through accepted records. Refresh dependent verification/publication and re-audit. This audit cannot repair extracted values by adding a caveat here.

## Bounded operational evidence

Inspected final `tool_execution_end` worker arrays in T, not repeated stream snapshots. Each call below has a successful `toolResult` with the same full ID **inside the same worker**; short IDs below uniquely locate those full IDs within the specified array. Retained attempts independently bind installed output hashes.

- **T line 2841, `000022-report-verification`:** read `call_kNLxo9P0PMUj3wqRqRVJozJ2` returns replay lines 509–703; read `call_ZSdQiS8rV5lrbj0GmLJaj4bU` returns 767–881. Write `call_LTerrTdvYnKuUBzUMhpoubkk` successfully emits the no-blocker verification. Its content check `call_xn6Og37Pxi0Dwi9E7ZMkHftB` returns the qualified member-content pass, not semantic certification. Actual source access thus occurred, but did not preserve H1's condition.
- **T line 3200, `000024-memory-profile`:** write `call_J7fZjQq6G018WpVvxvaYNDAO` creates the profile builder; executions `call_nbxkcEdp10pDLHJz9hdZJcST` and `call_3Xi2f4osH8t5kiRoCyIJlpb7` actually run it, with successful no-output results. The intervening edit changes other classifications. `R/state/attempts/000024-memory-profile.json` binds the published profile hash: H2 is an authored/installed classification, not an unexecuted suggestion.
- **T line 3564, `000026-profile-verification`:** write `call_ekWuOM4j5CoxEzOuN9WveSne` successfully writes the published acceptance; content check `call_FiSg9WcaBGpI7Q1P1kqVRXsj` passes. Attempt 26 pins the same profile hash. The verifier's axis-level partialness reasoning missed H2's unit-level completeness problem.

Selected histories also contain relative input reads, including report-verifier source reads, despite the supplied worker rule requiring absolute input paths. Results resolve the inspected source in the assigned checkout; no wrong-source read or consequential collateral effect was established from those pairs. This is a path-discipline deviation, not blanket worker clearance. Selected actual writes land in the workers' output/identity/scratch areas. No exhaustive supplied-input recovery, write-scope, provider, cleanup or idleness audit was performed. Publication/exit and content passes do not prove every worker obligation. No new target-execution or consequential authority incident is established within this sample; historical incidents remain untouched.

## Validation and stop

From W, with its recorded `W/.venv/bin` first on PATH, ran `commonplace-validate kb/agentic-system-analyses/retained/jaz-lang--jaz`: exit 0, `VALIDATION SUCCESS`, one assembled artifact, zero text files, zero failures/warnings; no notices. This is deterministic validation, not semantic clearance of H1/H2.

Report validation: `commonplace-validate /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/batch-23-jaz.md`, from the same prepared environment: exit 0, `VALIDATION SUCCESS`, one file/one text file, zero failures/warnings; no notices. Implicit workshop-text admissibility is not an audit-specific semantic schema.

Only this report was authored. No delegation, commits, feedback to analysts, source acquisition, target execution, run commands/effects, repairs, integration, cleanup, termination or push occurred. Unpublished timeout cases and independently owned reports were excluded. Stop at H1/H2 rather than expanding into concurrency experiments or full provenance reconstruction. Parent owns any authorized follow-up and exact-byte integration decision. **Current exact publication remains held.**

---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Autocontext memory: bundle serving, separately mutable lessons, compaction, package movement and host read-back at the frozen revision."
run-id: AAS-2026-10-15-autocontext-b7f59f8405c4-01
source-identity: https://github.com/greyhaven-ai/autocontext
reviewed-boundary: f72c154152397f54d55407508b153d28861888a5
---

# Autocontext memory report

## Boundary and evidence

This account covers the memory responsibilities inside the whole-system improvement-plane boundary in [boundary](boundary.md): Python and npm generation context, skill/lesson maintenance, bundle admission, portable knowledge, session consolidation and Pi/MCP read-back. It distinguishes executable source, routing metadata, interpreted advice and audit records. Model weights and inference adapters remain the components declared in [RT-CMP-role-models](runtime.md#rt-cmp-role-models) and [RT-CMP-training-checkpoints](runtime.md#rt-cmp-training-checkpoints), not additional text stores.

All new evidence is static implementation or shipped doctrine/design from SRC-1 at the reviewed commit. The checkout's HEAD was rechecked and its status was clean. No target execution, tests, model calls or archived results were used. External host conversation state, provider weights and actual host discovery of emitted skills remain outside the frozen implementation; this prevents claims about complete conversation retention, host compaction, exercised activation or improvement. Available but uninspected branches below are inspection limits, not absences or access gaps.

The coverage table separates direct source inspection from supplied runtime evidence. Paths are commit-relative in SRC-1. Grouped unresolved rows do not imply that all objects share an admission policy.

| Entry point / memory operation | Source path and evidence basis | Coverage and limits |
| --- | --- | --- |
| Python CLI scenario dispatch and role context | Direct: `autocontext/src/autocontext/cli.py`, `autocontext/src/autocontext/loop/stages.py`, `autocontext/src/autocontext/prompts/templates.py` | [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation), [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly); annotations below add serving precedence and stale filtering. |
| Bundle bootstrap, candidate overlay and matched promotion | Direct: `autocontext/src/autocontext/storage/artifacts.py`, `autocontext/src/autocontext/context_bundles/assembly.py`; supplied runtime: evaluator/coordinator | [MEM-OBJ-context-bundle](#mem-obj-context-bundle), [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion). Full registry transactions and post-promotion rollback not independently audited. |
| Bundle part consumers and validator execution seam | Direct: `autocontext/src/autocontext/context_bundles/assembly.py`, `autocontext/src/autocontext/context_bundles/store.py`, `autocontext/src/autocontext/loop/stage_helpers/context_loaders.py`, `autocontext/src/autocontext/loop/stage_helpers/harness_mutations.py`, `autocontext/src/autocontext/harness/mutations/applier.py`, `autocontext/src/autocontext/harness/mutations/gate.py`, `autocontext/src/autocontext/agents/orchestrator.py`, `autocontext/src/autocontext/loop/generation_pipeline.py`, `autocontext/src/autocontext/execution/harness_loader.py`, `autocontext/src/autocontext/harness/pipeline/validity_gate.py`, `autocontext/src/autocontext/loop/stage_helpers/tournament_prep.py` | Eight part records below separate advice, routing, four mutation types, reference source and executable validators. Validator consumer is wired conditionally; execution/security and other callable consumers uninspected. |
| Generation persistence, rejected-attempt lessons, consolidation | Direct: `autocontext/src/autocontext/storage/artifact_generation_persistence.py`, `autocontext/src/autocontext/storage/artifact_skill_lessons.py`, `autocontext/src/autocontext/loop/stage_helpers/persistence_helpers.py`, `autocontext/src/autocontext/loop/stages.py` | [MEM-OBJ-skill-lessons](#mem-obj-skill-lessons), [MEM-RTE-lesson-maintenance](#mem-rte-lesson-maintenance). |
| Lesson lifecycle and freshness | Direct: `autocontext/src/autocontext/knowledge/lifecycle.py`, `autocontext/src/autocontext/loop/stage_helpers/freshness.py`, `autocontext/src/autocontext/storage/artifacts.py` | [MEM-RTE-lesson-lifecycle](#mem-rte-lesson-lifecycle); stale markers and removal are different from age-based expiry. |
| Deterministic component compaction, ledger and budget | Direct: `autocontext/src/autocontext/domain/context_compaction.py`, `autocontext/src/autocontext/prompts/templates.py`, `autocontext/src/autocontext/loop/stage_helpers/semantic_benchmark.py`, `autocontext/src/autocontext/storage/compaction_ledger.py`; budget details supplied by runtime | [MEM-RTE-component-compaction](#mem-rte-component-compaction), [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly). |
| Python package CLI/import and cross-run snapshot | Direct: `autocontext/src/autocontext/cli_package_commands.py`, `autocontext/src/autocontext/knowledge/package.py`, `autocontext/src/autocontext/storage/artifact_snapshots.py` | [MEM-RTE-package-import](#mem-rte-package-import); inherited-run selection from supplied scenario route. Active-bundle refresh after direct import/restore unresolved. |
| Python MCP knowledge tools and registration | Direct: `autocontext/src/autocontext/mcp/knowledge_tools.py`, `autocontext/src/autocontext/mcp/server.py`, `autocontext/src/autocontext/knowledge/search.py` | [MEM-RTE-requested-readback](#mem-rte-requested-readback). Search returns scenario metadata, not full advice injection. Complete SDK/HTTP authorization not audited. |
| npm playbook admission, prompts and read-back tools | Direct: `ts/src/knowledge/artifact-store.ts`, `ts/src/loop/generation-prompts.ts`, `ts/src/mcp/knowledge-readback-tools.ts`, `ts/src/mcp/server.ts`; supplied runner findings | [RT-RTE-npm-generation](runtime.md#rt-rte-npm-generation). Full TypeScript lesson lifecycle, package import, compaction integration and control-plane memory packs remain uninspected; no parity conclusion. |
| Session consolidation library operations | Direct: `autocontext/src/autocontext/session/memory_consolidation.py`, `ts/src/session/memory-consolidation.ts` | [MEM-RTE-consolidation-preview](#mem-rte-consolidation-preview). Threshold/extraction capability is not durable promotion. |
| Pi registered snapshot tool and ledger display | Direct: `pi/src/index.ts`, `pi/src/runtime-snapshot.ts` | [MEM-RTE-requested-readback](#mem-rte-requested-readback), [MEM-OBJ-compaction-entry](#mem-obj-compaction-entry). Output previews/display summaries are not the full retained payload. |
| Host file-consumer and emitted skills | Direct: `skills/autocontext-consumer/SKILL.md`, `autocontext/src/autocontext/storage/artifact_skill_lessons.py` | [MEM-CLM-file-consumption](#mem-clm-file-consumption). Documented external consumer role is afforded, not observed discovery. |
| Hints, notebook, evidence manifests and derived reports | Direct loading/freshness: `autocontext/src/autocontext/loop/stages.py`, `autocontext/src/autocontext/loop/stage_helpers/freshness.py`, `autocontext/src/autocontext/loop/stage_helpers/semantic_benchmark.py` | [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly) annotation: selected role-specific parts and filters known; full notebook writers, evidence redaction, hint ranking/rotation internals and report generators uninspected. Prevents universal provenance, admission or retention claims. |
| Training, ambient, kernel and trace-derived parameter changes | Supplied: [RT-RTE-training-experiments](runtime.md#rt-rte-training-experiments), [RT-RTE-ambient-promotion](runtime.md#rt-rte-ambient-promotion), [RT-RTE-kernel-evolution](runtime.md#rt-rte-kernel-evolution); direct export option signatures in `autocontext/src/autocontext/cli_package_commands.py` | Retained checkpoints/source, serving bindings, selected feedback and rejection remain included. Full dataset curation, trace origin, model registry reload, production-trace and sharing pipelines not independently inspected; no end-to-end trace-to-weight benefit claim. |
| Task revision, mission/session recovery, persistent host sessions | Supplied: [RT-RTE-task-revision](runtime.md#rt-rte-task-revision), [RT-RTE-runtime-dispatch](runtime.md#rt-rte-runtime-dispatch), runtime coverage | Within-invocation revision is known; complete branch/session reload, host compaction, mission notebook retention and opaque provider state are unresolved. No inference that every persisted event is later consumed. |

## Core ideas

1. **The serving bundle is not identical to the mutable knowledge directory.** Python bootstraps a bundle from legacy state, then uses the active bundle's playbook, hints, tool references, mutations and routing. Separately loaded SKILL lessons and analysis can still change. The matched gate therefore does not cover every behavior-shaping text update. See [MEM-OBJ-context-bundle](#mem-obj-context-bundle), [MEM-RTE-lesson-maintenance](#mem-rte-lesson-maintenance) and the promotion annotation.
2. **Failure survives as advice, not only as a raw trace.** Rollback generates an avoidance lesson containing score, strategy and replay excerpts. Later generations load operational lessons; successful coach lessons can be accumulated and model-consolidated. Neither label establishes truth or useful learning. See [MEM-RTE-lesson-maintenance](#mem-rte-lesson-maintenance).
3. **“Semantic compaction” is deterministic structural selection on the inspected Python path.** It chooses recent sections, bullets, keywords and table rows, then truncates. The delivered component and the audit ledger's shorter summary are different products. A host snapshot can retrieve ledger entries, but automatic generation restoration from those summaries is not established. See [MEM-RTE-component-compaction](#mem-rte-component-compaction).
4. **Admission is mechanism-specific.** Bundle matching, optional playbook approval, direct import, lesson edits and hook-transformed writes have different controls. A caller initiating a run or invoking an API is not necessarily a human approving its contents. The two session consolidators return extracted material without establishing persistence, despite “promoted” field names. See [MEM-RTE-package-import](#mem-rte-package-import), [MEM-RTE-consolidation-preview](#mem-rte-consolidation-preview) and [RT-RTE-npm-generation](runtime.md#rt-rte-npm-generation).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-context-bundle
Label: Immutable context bundle and operative parts

Source-native identity: `ContextBundle` with components indexed by kind/key, parent digest and evaluator epoch. Storage substrate: artifact-store context-bundle registry under the knowledge root. Distinct from [RT-OBJ-strategy](runtime.md#rt-obj-strategy), which is the output executed in a tournament; this object is input to context selection and admission in [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion), not a duplicate route.

This is a valid mixed container, not one part-level authority assessment. Its operative parts are declared separately below: [MEM-OBJ-bundle-advice](#mem-obj-bundle-advice), [MEM-OBJ-routing-config](#mem-obj-routing-config), [MEM-OBJ-prompt-fragment](#mem-obj-prompt-fragment), [MEM-OBJ-context-policy](#mem-obj-context-policy), [MEM-OBJ-completion-check](#mem-obj-completion-check), [MEM-OBJ-tool-instruction](#mem-obj-tool-instruction), [MEM-OBJ-tool-spec](#mem-obj-tool-spec) and [MEM-OBJ-harness-validator](#mem-obj-harness-validator). Digest/epoch/parent are symbolic access and lineage metadata, not explanations supporting advice. SRC-1, `autocontext/src/autocontext/context_bundles/assembly.py`, `autocontext/src/autocontext/storage/artifacts.py`, `autocontext/src/autocontext/loop/stages.py`.

> by_identity = {(component.kind, component.key): component for component in active.components}
> --- `autocontext/src/autocontext/context_bundles/assembly.py`

> f"### Reference helper (not installed or callable): {component.key}\n"
> --- `autocontext/src/autocontext/context_bundles/assembly.py`

Candidate overlays preserve unchanged active components; blank proposed playbook/hints do not delete them. The baseline's initial content can have operator, imported or prior-run provenance; bootstrap itself does not independently establish that provenance's quality. Subsequent candidate transformations are known even when that initial authorship is unknown. Evaluation/admission lineage is not a requirement that the advice contain its causal reasons.

#### MEM-OBJ-bundle-advice
Label: Bundle playbook, hints and legacy tool guidance

Part of: [MEM-OBJ-context-bundle](#mem-obj-context-bundle)

Source-native identity: PLAYBOOK/playbook, HINTS/hints and non-JSON TOOL_GUIDANCE/legacy_tool_context components. Form: natural-language advice. Storage: component content in immutable bundle JSON under the knowledge root. Lineage: legacy file capture at bootstrap; nonblank coach playbook/hints overlay by component identity; unchanged advice survives candidate creation. Initial authorship may be imported, operator-authored or prior-run generated and remains unresolved. Admission: software captures the initial baseline; subsequent candidate publication uses [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion), not per-content human approval. Blank proposals preserve rather than withdraw prior advice. Actual consumers: knowledge setup's playbook/hints/tool strings enter role prompts subject to compaction/budget/channel selection in [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly). Force: interpreted guidance, not a deterministic action gate. Rationale preservation in actual generated content remains uninspected. SRC-1, `autocontext/src/autocontext/context_bundles/assembly.py`, `autocontext/src/autocontext/loop/stages.py`; the container and supplied assembly route provide passages for capture, overlay and delivery.

- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-OBJ-routing-config
Label: Bundle roles routing configuration

Part of: [MEM-OBJ-context-bundle](#mem-obj-context-bundle)

Source-native identity: ROUTING_CONFIG/roles. Form: symbolic JSON, not advice to a model. Storage: bundle component content; effective settings and role router are in-process consumer state. Lineage: `routing_snapshot` captures configured models/providers and flags; candidate assembly overlays a supplied map. Admission: JSON/object/known-field checks, promotion contract, then matched candidate admission. Nonempty DAG/tuning changes are rejected; construction-bound provider/judge changes cannot be promoted against an incumbent. At serving, mismatch with constructed runtime raises rather than silently rebuilding it; live model fields require nonblank strings and flags require booleans. Proposer is generation code using settings and optional proposed changes; software enforces acceptance, not an established human content veto. SRC-1, `autocontext/src/autocontext/context_bundles/assembly.py`, `autocontext/src/autocontext/loop/stages.py`.

Actual consumer: after knowledge setup the generation pipeline calls orchestrator routing synchronization, which updates role model names, settings, role router and coverage cache. Its authority is deterministic configuration of later model calls and relevant flags; provider compliance and actual model identity remain bounded by [RT-CMP-role-models](runtime.md#rt-cmp-role-models). An empty map also resynchronizes from baseline, preventing an older override leaking forward. Matched rejection preserves the incumbent; full administrative rollback remains uninspected. SRC-1, `autocontext/src/autocontext/loop/generation_pipeline.py`, `autocontext/src/autocontext/agents/orchestrator.py`.

> self.competitor.model = effective_settings.model_competitor
> self.analyst.model = effective_settings.model_analyst
> self.coach.model = effective_settings.model_coach
> self.architect.model = effective_settings.model_architect
> self._role_router = RoleRouter(effective_settings)
> --- `autocontext/src/autocontext/agents/orchestrator.py`

- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-OBJ-prompt-fragment
Label: Bundle prompt fragment mutation

Part of: [MEM-OBJ-context-bundle](#mem-obj-context-bundle)

Source-native identity: PROMPT_FRAGMENT, keyed by mutation ID. Storage: JSON mutation payload in the immutable bundle. Form: symbolic typed metadata selecting target role plus natural-language `content` delivered to that model. Lineage: architect Markdown parsed into mutations; legacy baseline can capture saved mutations; candidate assembly preserves approved payloads and marks them active. Admission: `evaluate_mutation` requires nonempty content of at most 10,000 characters and a target role; candidate publication additionally follows matched promotion. Code admits, architect model proposes; initiating a run is not human approval. Invalid proposals are skipped and unchanged components preserved. `bundle_mutations` reconstructs active typed mutations; the applier appends content only when the role exists in the prompt map. Consumer authority is interpreted role guidance, not executable code. Mutation presence also disables the pre-mutation structural prompt split to avoid bypassing flat-prompt changes. SRC-1, `autocontext/src/autocontext/context_bundles/assembly.py`, `autocontext/src/autocontext/harness/mutations/gate.py`, `autocontext/src/autocontext/harness/mutations/applier.py`, `autocontext/src/autocontext/loop/stage_helpers/harness_mutations.py`, `autocontext/src/autocontext/loop/stages.py`.

> if role and role in result:
>     result[role] = f"{result[role]}\n\n{mutation.content}"
> --- `autocontext/src/autocontext/harness/mutations/applier.py`

- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-OBJ-context-policy
Label: Bundle context policy mutation

Part of: [MEM-OBJ-context-bundle](#mem-obj-context-bundle)

Source-native identity: CONTEXT_POLICY mutation. Storage: bundle JSON component, reconstructed into a typed active mutation. Form: symbolic component/type metadata and natural-language policy content. Lineage/admission: captured legacy mutation or architect-proposed payload, nonempty bounded content and nonempty component required by the software gate, followed by candidate matched admission. No per-policy human approval is established. Invalid proposals are omitted; immutable prior content survives unless overlaid. Actual consumer: `render_context_policy_block` formats component/content bullets as “Active context policies”; knowledge setup adds that block to `experiment_log` before prompt preparation. This is advice interpreted by role models, not proof that the named component's selection budget is programmatically changed. Reasons and generated policy truth remain uninspected. SRC-1, `autocontext/src/autocontext/context_bundles/assembly.py`, `autocontext/src/autocontext/harness/mutations/gate.py`, `autocontext/src/autocontext/loop/stage_helpers/harness_mutations.py`, `autocontext/src/autocontext/loop/stages.py`.

> return "Active context policies:\n" + "\n".join(lines)
> --- `autocontext/src/autocontext/loop/stage_helpers/harness_mutations.py`

- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-OBJ-completion-check
Label: Bundle completion check mutation

Part of: [MEM-OBJ-context-bundle](#mem-obj-context-bundle)

Source-native identity: COMPLETION_CHECK mutation. Storage: typed JSON in immutable bundle, reconstructed active on read. Form: symbolic metadata with natural-language checklist content. Lineage: architect proposal or legacy saved mutation; code requires nonempty bounded content and matched candidate admission before later active serving. No content-specific human approval or correctness oracle is established by this gate. Actual consumer on the inspected generation path is the competitor prompt: `get_active_completion_checks` selects content and the stage helper appends a checklist. Despite its name, this path does not execute these strings as binary validity predicates; that authority belongs to the separate validator part. Rejected candidates retain incumbent content, not a changed checklist. SRC-1, `autocontext/src/autocontext/context_bundles/assembly.py`, `autocontext/src/autocontext/harness/mutations/gate.py`, `autocontext/src/autocontext/harness/mutations/applier.py`, `autocontext/src/autocontext/loop/stage_helpers/harness_mutations.py`.

> checklist = "Active completion checks:\n" + "\n".join(f"- {check}" for check in checks)
> prompt_map["competitor"] = f"{prompt_map['competitor']}\n\n{checklist}"
> --- `autocontext/src/autocontext/loop/stage_helpers/harness_mutations.py`

- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-OBJ-tool-instruction
Label: Bundle tool instruction mutation

Part of: [MEM-OBJ-context-bundle](#mem-obj-context-bundle)

Source-native identity: JSON TOOL_GUIDANCE generated from TOOL_INSTRUCTION mutation, distinct from non-JSON legacy guidance and TOOL_SPEC source. Form: symbolic type/tool-name metadata plus natural-language instruction. Storage: immutable component JSON; decoded active mutation during setup. Lineage: legacy mutation capture or architect proposal; software requires nonempty bounded content and tool name, then candidate matched admission. Invalid additions are skipped; authorship is model/caller dependent, not human content approval. Actual consumer: tool-instruction renderer emits tool-name/content bullets and setup appends them to tool context. The model receives advice about a tool; no callable registration or tool grant follows from this payload. SRC-1, `autocontext/src/autocontext/context_bundles/assembly.py`, `autocontext/src/autocontext/harness/mutations/gate.py`, `autocontext/src/autocontext/loop/stage_helpers/harness_mutations.py`, `autocontext/src/autocontext/loop/stages.py`.

> return "Tool-specific instructions:\n" + "\n".join(lines)
> --- `autocontext/src/autocontext/loop/stage_helpers/harness_mutations.py`

- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-OBJ-tool-spec
Label: Bundle reference helper source

Part of: [MEM-OBJ-context-bundle](#mem-obj-context-bundle)

Source-native identity: TOOL_SPEC keyed by proposed tool name. Form: symbolic JSON/name and Python source syntax, consumed here as natural-language/model-readable reference context. Storage: immutable bundle component. Lineage: architect tool specification overlays by identity; code requires a valid identifier, nonempty code and successful `ast.parse`, then candidate matched admission. These are structural and comparative controls, not proof of safe or correct helper behavior; no per-source human approval is established. Actual consumer: `bundle_tool_context` extracts description and source and renders an explicitly noncallable reference into role tool context. No tool installation/grant is established by this rendering. Later strategy code may inline/adapt it, but that potential downstream effect is not an observed execution. Supplied [RT-OBJ-strategy](runtime.md#rt-obj-strategy) remains the separate executor input. SRC-1, `autocontext/src/autocontext/context_bundles/assembly.py`; the container's reference-helper quote supplies the consumer distinction.

- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-OBJ-harness-validator
Label: Bundle executable harness validator source

Part of: [MEM-OBJ-context-bundle](#mem-obj-context-bundle)

Source-native identity: HARNESS_VALIDATOR keyed by harness name. Form: symbolic executable Python, either direct `text/x-python` or the `code` field of JSON. The baseline's Markdown `legacy_harness_context` fallback is not executable material: materialization ignores it. Storage: immutable bundle manifest plus digest-scoped `context_bundles/runtime/<digest>/harness/*.py`. Lineage: legacy harness files captured at bootstrap or architect harness specs overlaid on the active bundle; source name/code/AST checks precede candidate acceptance. Saving materializes source before active serving; a file existing does not itself establish promotion. Subsequent serving admission is the matched bundle protocol. Software enforces it; enabling generation is not a per-validator human approval step. Initial file authorship remains unresolved. SRC-1, `autocontext/src/autocontext/context_bundles/assembly.py`, `autocontext/src/autocontext/context_bundles/store.py`.

> ast.parse(source)
> target = harness_dir / f"{component.key}.py"
> write_text_atomic(target, source.rstrip() + "\n")
> --- `autocontext/src/autocontext/context_bundles/store.py`

Actual consumer wiring is now traced: with two-tier gating enabled, the tournament stage requests the validity harness loader; with harness validators enabled, that loader selects the active digest's immutable directory, not mutable legacy files. An active bundle with no executable validators returns no loader rather than falling back. `HarnessLoader.load` applies confined file/size reads, syntax and AST-safety checks, then inspects callable names via isolated execution and retains proxies. Each proxy calls source in a fresh isolated child. `ValidityGate.check` invokes `validate_strategy` and combines harness errors with scenario errors. The retry helper can request revision and eventually roll back without a tournament. Thus authority is executable validity checking capable of preventing tournament progress, not merely advisory prompt delivery. SRC-1, `autocontext/src/autocontext/loop/stages.py`, `autocontext/src/autocontext/loop/stage_helpers/context_loaders.py`, `autocontext/src/autocontext/execution/harness_loader.py`, `autocontext/src/autocontext/harness/pipeline/validity_gate.py`, `autocontext/src/autocontext/loop/stage_helpers/tournament_prep.py`.

> if bundle_harness_dir is None:
>     return None
> harness_dir = bundle_harness_dir
> --- `autocontext/src/autocontext/loop/stage_helpers/context_loaders.py`

> harness_result = self._harness_loader.validate_strategy(strategy, self._scenario)
> if not harness_result.passed:
>     harness_errors.extend(harness_result.errors)
> --- `autocontext/src/autocontext/harness/pipeline/validity_gate.py`

Load failures become validation errors; no loaded callable or no enabled gate is not evidence of an exercised validator. Executable source may veto on the wired route, but no target execution or security audit was performed. Correctness of generated checks, isolation implementation/serialization behavior, other callable consumers and post-promotion administrative rollback remain uninspected. Rationale is not required by source materialization; no later rationale reader is established. This part refines [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion) and [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation), rather than duplicating either whole route.

- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-OBJ-skill-lessons
Label: Operational lessons in emitted SKILL files

Source-native identity: `## Operational Lessons` in scenario `SKILL.md`, with a separate bundled `playbook.md` copy and resource links. Natural-language content stored in scenario skill directories under `skills_root`; `.claude/skills` symlinks expose those directories. Distinct from runtime strategy and parametric components; it is one retained input of [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly), not that whole route.

Lineage: preexisting bullets plus coach lessons or deterministic rollback warnings, exact-bullet deduplication, optional curator replacement and lifecycle edits. Python's own prompt reader selects only the lesson section and excludes stale-marked lines; a host may read the whole skill/resources on demand. Source authoring requests prescriptive rules; actual explanations and criticism in produced lessons are not supplied. SRC-1, `autocontext/src/autocontext/storage/artifact_skill_lessons.py`, `autocontext/src/autocontext/storage/artifacts.py`.

> active_lines = [line for line in section.splitlines() if "<!-- autocontext:lesson-status=stale -->" not in line]
> --- `autocontext/src/autocontext/storage/artifacts.py`

#### MEM-OBJ-generation-artifacts
Label: Raw generation artifacts and separately derived advice

Source-native identity: generation `metrics.json`, replay JSON, per-generation analysis Markdown, appended `coach_history.md` and architect changelog, plus SQLite activity in persistence helpers. Storage substrate: run/knowledge directories and SQLite. Replay/metrics are symbolic records; raw role output and analysis are natural-language records. Derived SKILL advice is [MEM-OBJ-skill-lessons](#mem-obj-skill-lessons), not synonymous with these records. The object groups trace retention only; admission of its derived advice is separately recorded.

Distinct from [RT-OBJ-strategy](runtime.md#rt-obj-strategy): these include results and role reports rather than only executable strategy input. SRC-1, `autocontext/src/autocontext/storage/artifact_generation_persistence.py`, `autocontext/src/autocontext/loop/stage_helpers/persistence_helpers.py`. Automatic loaders select latest advance analysis, trajectories and reports; they do not copy every raw coach history/replay into every future prompt. Full source material may remain on disk after prompt trimming. There is no evidence that the short warning or consolidated bullets preserve all reasons retained in the raw records.

> self.buffered_append_markdown(scenario_dir / "coach_history.md", coach_md, heading=f"generation_{generation_index}")
> --- `autocontext/src/autocontext/storage/artifact_generation_persistence.py`

#### MEM-OBJ-compaction-entry
Label: Compaction ledger entry and display summary

Source-native identity: `CompactionEntry`: ID, parent, timestamp, summary, first-kept entry identifier, token estimate and details. Storage substrate: per-run `compactions.jsonl` and `compactions.latest`; also recorded through runtime-session compaction recording. Symbolic metadata governs linkage and lookup; natural-language `summary` is a capped display of compacted context. It is distinct from [MEM-OBJ-generation-artifacts](#mem-obj-generation-artifacts) and from runtime's transient `PromptBundle` in [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly).

SRC-1, `autocontext/src/autocontext/domain/context_compaction.py`, `autocontext/src/autocontext/storage/compaction_ledger.py`, `autocontext/src/autocontext/loop/stage_helpers/semantic_benchmark.py`. The summary includes goal/progress boilerplate and at most a 650-token-estimate critical-context excerpt. It is not an opaque checkpoint of complete model state; `component:<key>:kept` is an identifier, not evidence of a reloadable full transcript. Runtime-session recording retains serialized entries and ledger paths. Pi reads recent ledger entries for inspection; a normal generation reads source components again, not demonstrably this summary as its canonical memory.

> context = _truncate_text(compacted, max_tokens=650).strip()
> --- `autocontext/src/autocontext/domain/context_compaction.py`

### Routes

#### MEM-RTE-lesson-maintenance
Label: Trace-fed lesson writing and curator consolidation

Endpoints: generation result/coach output → persistence helper → SKILL lesson accumulator → optional curator consolidation → later generation lesson reader. Owner: persistence/stage code; model coach authors advance lessons and curator authors replacement bullets. This is a distinct maintenance route after [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation), not a second declaration of the entire generation loop. It affects [MEM-OBJ-skill-lessons](#mem-obj-skill-lessons).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: rewritten SKILL and bundled playbook copy; consolidation also records curator output/usage in SQLite.
- Later read-back: subsequent knowledge setup calls `read_skills`; selected operational lessons enter role prompts.
- Delegated visibility: curator receives existing lessons, configured maximum and score trajectory; later role models receive the selected lesson section, not necessarily raw curator reasoning.
- Selection predicate: advance selects coach lessons, unless playbook approval is required; nonadvance constructs an avoidance warning. Consolidation needs enabled curator, no feedback ablation, scheduled generation or severe overflow, and lesson count above the maximum.
- Invalidation or expiry: exact-bullet duplicates are suppressed; consolidation replaces the section; lifecycle stale/removal is separate. No automatic age expiry for skill lessons is implemented by the inspected freshness loader.
- Activation or effect: durable advice is changed and selected for future prompts; actual reliance or better decisions are unobserved.
- Evidence limits: no concrete generated lessons or curator outcomes inspected; full dead-end consolidation/ranking semantics are not audited.

SRC-1, `autocontext/src/autocontext/loop/stage_helpers/persistence_helpers.py`, `autocontext/src/autocontext/storage/artifact_skill_lessons.py`, `autocontext/src/autocontext/loop/stages.py`. Admission is code-controlled accumulation or model-generated replacement, not per-content human approval. Approval configuration suppresses advance skill writing, but rollback warnings still have their own path. The `playbook_result` argument does not provide a separate acceptance test inside the inspected helper. This is a bounded generation maintenance mode, with score trajectory as guidance rather than an expected-answer oracle for lesson truth. Recovery retains raw coach/consolidator records but no automatic inverse of lesson replacement was traced.

> artifacts.replace_skill_lessons(scenario_name, lesson_result.consolidated_lessons)
> --- `autocontext/src/autocontext/loop/stage_helpers/persistence_helpers.py`

> f"Narrative: {ctx.replay_narrative[:150]}. "
> f"Avoid this approach."
> --- `autocontext/src/autocontext/loop/stage_helpers/persistence_helpers.py`

This is a qualifying trace-fed retained-advice path: tournament/attempt data → warning or model lesson → SKILL → later invocation. Raw trace retention alone would not establish it. Reasons can be excerpted or lost; curator reasoning persists as a separate activity record, but its automatic later reader was not established.

#### MEM-RTE-lesson-lifecycle
Label: Lesson removal, stale marking and reactivation

Endpoints: caller action and derived lesson ID → lifecycle functions → playbook/SKILL rewrite or dead-end movement → future readers. Owner: lifecycle code; caller supplies action. Distinct from automatic maintenance in [MEM-RTE-lesson-maintenance](#mem-rte-lesson-maintenance); no supplied runtime counterpart covers this operation's internal semantics.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: found/status result such as active, stale, deleted or deadEnd.
- Later read-back: SKILL stale lines are omitted by the generation lesson reader; deletion removes future file reads; dead-end text is separately loaded by knowledge setup. Active bundle playbook may still supersede the mutable file.
- Delegated visibility: operation addresses derived lesson IDs/text in files; human identity and the full deployed UI authorization are uninspected.
- Selection predicate: matching normalized-text-derived ID plus caller action; approve clears stale status, reject removes the lesson; activate can move a dead end back into playbook lessons.
- Invalidation or expiry: stale marker is reversible; deletion and dead-end movement rewrite files. Age is not consulted by `build_lifecycle` in this implementation.
- Activation or effect: modifies future file-visible content; no guarantee of revoking already copied prompt text, bundled resources, snapshots or immutable active bundles.
- Evidence limits: public implementation operations established; complete HTTP callers, concurrent edit safety and downstream bundle synchronization not audited.

SRC-1, `autocontext/src/autocontext/knowledge/lifecycle.py`, `autocontext/src/autocontext/storage/artifacts.py`, `autocontext/src/autocontext/loop/stage_helpers/freshness.py`. The caller decides edit/admission; no model quality test or answer oracle appears in these operations. It is requested maintenance, not an automatic curriculum. Calling `approve_lesson` is not initial admission of a pending lesson: the view returns an empty pending list and derives active/stale entries from existing content. Physical I/O is software; whether a human chose that particular action remains caller-dependent.

> del lesson_store, staleness_window
> --- `autocontext/src/autocontext/knowledge/lifecycle.py`

> return artifacts.read_skills(ctx.scenario_name), ""
> --- `autocontext/src/autocontext/loop/stage_helpers/freshness.py`

#### MEM-RTE-component-compaction
Label: Component selection, compaction and audit persistence

Part of: [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly)

This is the compaction subroute, not a competing description of the whole prompt assembly. Endpoints: accumulated retained component text → deterministic component selector, optional hooks and final budget → constructed prompts and audit entries. Owner: prompt code and configured extension hooks. It operates on stored knowledge/report copies without deleting their source files.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: compacted component strings in role prompts; changed components generate linked ledger entries and selection telemetry.
- Later read-back: later role invocation consumes compacted advice/history. Durable ledger entries can be requested by Pi snapshot; full automatic restoration of an old prompt from an entry is uninspected.
- Delegated visibility: models receive selected compacted strings after later budget/channel transformations; ledger summary is shorter and is not a complete copy of that input.
- Selection predicate: component name and token estimate; history also compacts above 24 lines or four sections. Hooks can block/rewrite before or after compaction. Final context budget is separate.
- Invalidation or expiry: cache keys include policy, component, input digest and limit, verify full text, and evict least-recently-used entries beyond 512; source changes cause recomputation. Prompt truncation does not withdraw source artifacts.
- Activation or effect: changes what later calls can see, with no evidence that condensed material preserves every reason or improves behavior.
- Evidence limits: static Python implementation; tokenizer/host window guarantees, external hook behavior and npm-equivalent integration are unestablished.

SRC-1, `autocontext/src/autocontext/domain/context_compaction.py`, `autocontext/src/autocontext/prompts/templates.py`, `autocontext/src/autocontext/loop/stage_helpers/semantic_benchmark.py`, `autocontext/src/autocontext/storage/compaction_ledger.py`. Playbook/lessons/analysis/trajectory limits are respectively 2800/1600/1800/1200 estimated tokens; seven components enter the inspected template's semantic pass. History retains four recent sections; lessons prefer six recent sections and recent selected lines; ordinary Markdown prefers early sections/lines; trajectory retains header and eight recent rows. Structured/keyword lines are preferred, with prefix truncation as fallback. This is software selection, not an LLM summarization call or factual admission oracle.

> selected = sections[-4:]
> --- `autocontext/src/autocontext/domain/context_compaction.py`

> selected_sections = sections[-6:] if prefer_recent else sections[:6]
> --- `autocontext/src/autocontext/domain/context_compaction.py`

Working-context consequence: removed text remains in source files where those exist; the prompt gets condensed text and a marker, not an automatically dereferenceable pointer. Runtime's final budget can remove still more, preferentially reports and auxiliary evidence while protecting hints/dead ends. Separate role calls keep unrelated work out and return selected outputs, resembling isolated frames only to that extent; persistent host state can break frame disposal. Supplied [RT-RTE-runtime-dispatch](runtime.md#rt-rte-runtime-dispatch) bounds that analogy.

#### MEM-RTE-package-import
Label: Portable knowledge import and file restoration

Endpoints: package CLI/MCP/library caller → schema/conflict checks → mutable knowledge, SKILL and optional SQLite snapshot → file consumers and potentially future baseline bootstrap. Owner: import code; caller chooses package and conflict policy. Distinct from matched promotion in [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion); package content is not a part of that evaluation route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `ImportResult` reporting written/skipped playbook, hints, harness, skill and snapshot.
- Later read-back: ordinary file readers and emitted skill consumers can read imported text; a future first baseline can incorporate it. Existing active bundle precedence limits whether imported playbook/hints immediately reach generation prompts.
- Delegated visibility: imported playbook/lessons/hints are natural-language advice; harness source is separately written as source, not merely a natural-language claim; score/strategy/provenance metadata is symbolic.
- Selection predicate: package validation, caller scenario override and overwrite/merge/skip rules. Merge writes a playbook only when empty, appends hints and deduplicates skill bullets; existing harness is retained except under overwrite.
- Invalidation or expiry: overwrite replaces mutable content; snapshots permit copying previous files back. Neither operation here demonstrates revocation of existing bundles or a transactional inverse across all written stores.
- Activation or effect: durable knowledge and optionally synthetic imported-run/snapshot records are installed; neither imported scores nor completed status proves fresh evaluation.
- Evidence limits: full harness execution consumers, signature/trust verification, npm package parity and active-bundle refresh are uninspected.

SRC-1, `autocontext/src/autocontext/knowledge/package.py`, `autocontext/src/autocontext/cli_package_commands.py`, `autocontext/src/autocontext/mcp/server.py`, `autocontext/src/autocontext/storage/artifact_snapshots.py`. Schema validation is a format check, not an answer oracle or matched-context test. The operator may explicitly select a package through CLI; generic MCP/library caller identity does not establish human approval. Metadata is written before content conflict branches, so skip is not a global no-write guarantee. Optional SQLite restoration records supplied scores and an imported run, using `agent_provider="package"`.

> sqlite.mark_run_completed(run_id)
> --- `autocontext/src/autocontext/knowledge/package.py`

Cross-run file snapshots copy playbook, hints, hint state, SKILL and harness Python files, not complete context-bundle or model state. Restoration writes those mutable surfaces. Supplied [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation) establishes the inheritance caller; the snapshot method alone would establish only a storage capability.

#### MEM-RTE-consolidation-preview
Label: Session consolidation extraction without durable promotion

Endpoints: library caller supplies counts and artifacts → threshold/extraction → result object. Owner: `MemoryConsolidator` code in each language. Distinct from durable lesson maintenance and runtime's generation routes; no supplied record declares this operation in detail.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: extracted lessons and result metadata; Python additionally extracts passed verification reasons into hints and current notebook objective into notebook updates.
- Later read-back: uninspected — no persistence-to-later-consumer chain is established by either inspected implementation.
- Delegated visibility: caller receives candidates; no model call is performed by these consolidators.
- Selection predicate: force, or completed turns at least 10, or completed sessions at least one by default. Python selects up to three promotable lines per sufficiently long report; TypeScript takes the first 200 characters of each qualifying report.
- Invalidation or expiry: inapplicable — returned candidates do not constitute maintained durable state in the inspected functions.
- Activation or effect: candidate extraction only; fields named promoted/productive do not establish lesson-store writes.
- Evidence limits: any outside caller that later persists the result remains uninspected, not proven absent.

SRC-1, `autocontext/src/autocontext/session/memory_consolidation.py`, `ts/src/session/memory-consolidation.ts`, `autocontext/src/autocontext/domain/context_compaction.py`. Code, not a human or model, selects candidate excerpts; whether a later caller approves them is unresolved. There is no content-validity oracle. The standalone Python lock utility does not prove this method acquires it or that a daemon invokes the operation.

> # In non-dry-run mode, actual persistence would happen here
> # (writing to lesson store, hint manager, notebook, etc.)
> # For now we return what would be promoted.
> --- `autocontext/src/autocontext/session/memory_consolidation.py`

#### MEM-RTE-requested-readback
Label: Requested knowledge and runtime inspection

Endpoints: MCP client or Pi foreground tool request → identifier/query selectors → file/SQLite/ledger reads → tool text and structured details. Owner: registered tool handlers; caller chooses when and what to request. Distinct from automatic generation context delivery in [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: playbook, analysis, trajectory, skill/tool text or search metadata through MCP; Pi runtime snapshot renders text plus structured details with optional truncated output previews.
- Later read-back: subsequent host-model invocation can receive the requested tool result. Host retention, further truncation and compliance are uninspected.
- Delegated visibility: Pi snapshot includes bounded recent compaction entries in details; rendered summary is not the full database, trace or ledger. MCP methods expose the particular selected artifact.
- Selection predicate: scenario/run/generation arguments or natural-language search query and top-k; Pi run/session/scenario filters and row limits. Search ranks token matches across weighted fields and returns scenario metadata, not an automatic best-playbook injection.
- Invalidation or expiry: filesystem-aware search cache revisions allow recomputation after edits; bounded ledger tail reads can omit old entries. No deletion occurs merely because results are omitted.
- Activation or effect: requested delivery and inspection, not unsolicited memory push or enforcement over the host's next action.
- Evidence limits: actual host calls, result-window policies, delegated provider internals and future behavioral influence unobserved.

SRC-1, `autocontext/src/autocontext/mcp/knowledge_tools.py`, `autocontext/src/autocontext/mcp/server.py`, `autocontext/src/autocontext/knowledge/search.py`, `ts/src/mcp/knowledge-readback-tools.ts`, `ts/src/mcp/server.ts`, `pi/src/index.ts`, `pi/src/runtime-snapshot.ts`. Python playbook wrapper and npm registration establish real exposed entry points, not hypothetical arbitrary API consumers. Pi registers a tool with explicit targeting and returns `okTruncated(renderRuntimeSnapshot(snapshot), snapshot)`. The ledger reader selects a bounded file tail, attempts recent lines, discards malformed JSON and returns at most the requested entry count.

> return entries.slice(-request.limit);
> --- `pi/src/runtime-snapshot.ts`

### Claims

#### MEM-CLM-file-consumption
Label: Host-agnostic file consumer instructions

Claimed operation: the shipped consumer skill directs an agent to find scenario knowledge, read playbook/lessons, inspect runs and move packages through CLI. This is doctrine/design in SRC-1, `skills/autocontext-consumer/SKILL.md`, distinct from [RT-CLM-agent-improvement](runtime.md#rt-clm-agent-improvement)'s broader improvement claim. It establishes an afforded later consumer role, not deployed host wiring or reliable discovery.

> Nothing here assumes a particular agent host, and most of it is plain file
> reading - the layout is documented below precisely so an agent can go straight
> to the file it wants.
> --- `skills/autocontext-consumer/SKILL.md`

Its description of `lessons.json` as append-only history is not a sufficient account of Python's operative SKILL lesson path: [MEM-OBJ-skill-lessons](#mem-obj-skill-lessons) and [MEM-RTE-lesson-maintenance](#mem-rte-lesson-maintenance) show replaceable/deletable sections. An absent file also does not prove nothing was learned, given alternative retained surfaces and roots.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion)

Storage/selection scope: the bundle is [MEM-OBJ-context-bundle](#mem-obj-context-bundle). Bootstrap first checks active state and returns it or rolls its evaluator epoch; only absent active state builds from current mutable legacy files. Active playbook/hints/tool context take precedence in generation setup. This means direct file import, restoration or lifecycle editing is not shown to replace the already-active corresponding bundle component. It does not mean all direct writes are inert: skills and recent analysis load separately. SRC-1, `autocontext/src/autocontext/storage/artifacts.py`, `autocontext/src/autocontext/loop/stages.py`.

> if active is not None:
>     if active.evaluator_epoch == evaluator_epoch:
>         return active
> --- `autocontext/src/autocontext/storage/artifacts.py`

#### On [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly)

Read-back is generation-triggered code supply, not an independent unsolicited background retrieval. Selector inputs are scenario/run/generation, active bundle, feedback ablation, enabled features and role. Playbook/hints/tool references come from active bundle when available; SKILL lessons, latest advance analysis, trajectory, dead ends and optional reports are read separately. Notebook content is rendered for competitor/analyst/coach/architect, with freshness filtering of objectives, hypotheses, unresolved questions, observations and follow-ups. Evidence manifests are prepared separately for analyst/architect using prior same-scenario snapshot directories, byte budget and secret-scanning request; full redaction/materialization correctness remains uninspected. SRC-1, `autocontext/src/autocontext/loop/stages.py`, `autocontext/src/autocontext/loop/stage_helpers/freshness.py`, `autocontext/src/autocontext/loop/stage_helpers/semantic_benchmark.py`.

The skill “freshness” helper simply calls `read_skills` and returns no warning. That reader filters explicit stale markers; it does not automatically age skill lessons. Legacy hint freshness has a separate age/confidence/support filter and is deliberately skipped when a bundle is active. These parts must not be generalized into one freshness guarantee. Prompt copies undergo [MEM-RTE-component-compaction](#mem-rte-component-compaction), final budget selection, hook/mutation effects and the runtime's conditional channel split. Selection metadata reports these operations but cannot prove the model saw complete original evidence or obeyed it.

#### On [RT-RTE-npm-generation](runtime.md#rt-rte-npm-generation)

Direct source inspection corroborates different admission and delivery. `writeOrStagePlaybook` either calls direct write or stages; direct `writePlaybook` invokes an artifact-write hook and then a playbook manager, or writes a redirected path. Approval methods are callable operations, not proof of a human executing them. Prompt builders explicitly concatenate current playbook, optional trajectory/dead ends/reports and operator/fresh-start hints. Curator consolidation prompts request reduced duplication and a maximum lesson count, but prompt requests alone do not establish successful consolidation. SRC-1, `ts/src/knowledge/artifact-store.ts`, `ts/src/loop/generation-prompts.ts`; supplied route provides runner wiring and quote support. No full TypeScript/Python compaction or lifecycle parity is inferred.

## Write side

The strongest inspected durable trace-to-advice chain is [MEM-RTE-lesson-maintenance](#mem-rte-lesson-maintenance): attempts produce raw results and coach/analyst reports; advance lessons or deterministic rollback warnings become retained SKILL bullets; later setup selects those bullets. Consolidation can replace them with model-generated bullets. Raw evidence and raw curator reasoning remain separately recorded, but a later generation's lesson input is not guaranteed to retain their reasons. This warrants a trace-fed update finding, not demonstrated improved capacity, content-directed theory criticism or exercised self-improvement.

Bundle proposals separately overlay active state and preserve content lineage. The eight declared parts of [MEM-OBJ-context-bundle](#mem-obj-context-bundle) distinguish initial capture, structural checks and actual later consumers: mutation gates check content/target metadata; code-spec gates check identifiers and syntax; routing rejects unsupported lifecycle changes. Matched evaluation gates candidate publication, while direct imports and lesson edits follow their own software/caller rules. Saving validator source materializes files but does not by itself activate them; enabled generation validity checking selects the active digest and can reject a strategy. Completion-check mutation text instead remains competitor advice. At initialization, legacy/imported file authorship can be unresolved even though bootstrap and later transformations are inspectable. Starting a run is not per-lesson human approval. Hooks can block or rewrite prompt/artifact content; installed hook behavior is external configuration, so no universal content-trust claim follows from default code. SRC-1, `autocontext/src/autocontext/prompts/templates.py`, `autocontext/src/autocontext/storage/artifact_write_methods.py`; [RT-RTE-runtime-dispatch](runtime.md#rt-rte-runtime-dispatch) supplies the imported-code authority limit.

Rejection does not erase experience. Rollback can add avoidance guidance; failed context candidates do not become serving bundles, per supplied [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion). Lesson deletion removes mutable text, stale marking excludes SKILL lines from that reader, and dead-end movement can reclassify content without losing all negative guidance. Snapshot restoration and imported packages can reinstate old material; no all-store revocation was established. Training checkpoint rejection and kernel champion selection retain their distinct recovery and feedback policies in the runtime routes, not the lesson mechanism.

Compaction is a second trace-fed transformation when it processes accumulated reports, analysis and trajectory. It changes delivered copies and emits durable audit summaries; persistence of that ledger is not itself evidence of a second live memory route. Session consolidators are the important counterexample: [MEM-RTE-consolidation-preview](#mem-rte-consolidation-preview) extracts candidate lessons but does not complete the persistence/consumer links.

## Read-back

There are three different directions of delivery:

- **Generation-triggered supply:** code reloads scenario/run-specific knowledge before role calls, performs filters and budgets, and copies selected values into prompts. This is [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly), not foreground model retrieval. Budgeted-away text may remain on disk; no automatic recovery of every omitted passage was established.
- **Requested retrieval:** registered MCP and Pi tools accept IDs/queries and return selected results. [MEM-RTE-requested-readback](#mem-rte-requested-readback) has an actual shipped host-facing consumer seam. Search metadata or an artifact identifier alone is not full content retrieval, and Pi's text preview is not its complete structured details.
- **Afforded file consumption:** shipped consumer instructions and emitted skill/resource links support a host role reading files later. [MEM-CLM-file-consumption](#mem-clm-file-consumption) is a documented consumption path with external discovery unresolved, not automatic injection proven by symlink creation.

Authority differs at the final consumer. Advice is interpreted by role or host models; [MEM-OBJ-routing-config](#mem-obj-routing-config) changes supported live settings, while nonempty tuning/DAG proposals are rejected on this promotion lifecycle rather than silently applied. [MEM-OBJ-harness-validator](#mem-obj-harness-validator) reaches conditional executable validity checking; mutation completion checks remain prompt advice. Source becomes executable only through its particular executor/installer. A TOOL_SPEC renderer explicitly treats code as reference. Training registry activation can instead change parameter selection, and kernel source admission changes the campaign champion; those are not merely advice retrieval. Source trust does not become reliable model compliance because text was put in a system/user channel. No observed execution closes the delivery-to-activation-to-benefit chain.

## Integration issues

Correction-round resolution: [MEM-OBJ-context-bundle](#mem-obj-context-bundle) remains the valid container; its eight newly declared parts each carry their own form, lineage, admission and consumer assessment. [MEM-OBJ-harness-validator](#mem-obj-harness-validator) resolves the former untraced consumer seam through digest-specific materialization, enabled loader selection and the validity gate/retry consumer. [MEM-OBJ-completion-check](#mem-obj-completion-check) instead reaches a prompt checklist; its name does not confer executable veto authority. These records are explicit parts of the container, not duplicate replacements. The earlier central missing-part conflict can be resolved by these declarations; unobserved execution/security and untraced alternative callable consumers remain limits, not absences. No peer report was supplied for revision, and none is modified.

1. **Scope of matched promotion.** [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion) is supported as a scoped protocol, not contradicted. Add the separately mutable SKILL lesson path [MEM-RTE-lesson-maintenance](#mem-rte-lesson-maintenance) when reconciling any whole-context guarantee. Evidence: separate `read_skills` and skill persistence in SRC-1, `autocontext/src/autocontext/loop/stages.py`. Consequence: not every future prompt edit is matched-evaluated.
2. **Direct file edits versus active serving state.** [MEM-RTE-package-import](#mem-rte-package-import), [MEM-RTE-lesson-lifecycle](#mem-rte-lesson-lifecycle) and [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion) need serving precedence retained. Bootstrap returns existing active state; setup overlays active bundle text. The full administrative refresh/rebase operation after import/restore is unresolved. Consequence: do not equate a successful mutable playbook write with immediate generation activation, or deletion with universal withdrawal.
3. **Consolidation label correction.** Boundary/runtime mention session-memory mechanisms but make no detailed durability claim. [MEM-RTE-consolidation-preview](#mem-rte-consolidation-preview) establishes extraction-only implementations in both languages. A later persistent caller remains uninspected. Consequence: do not infer trace-fed durable memory merely from promoted fields or module names.
4. **Freshness scope correction.** [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly) is compatible with filters, but generic aging of all knowledge would be unsupported. [MEM-RTE-lesson-lifecycle](#mem-rte-lesson-lifecycle) and its freshness annotation show explicit stale markers for skill lessons, separate hint/notebook filtering and bundle precedence. Consequence: retain part-specific expiry rather than one global freshness policy.
5. **Compaction/reload distinction.** [MEM-RTE-component-compaction](#mem-rte-component-compaction) is explicitly part of [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly), not a duplicate of that whole route. [MEM-OBJ-compaction-entry](#mem-obj-compaction-entry) has a supported Pi inspection consumer, but automatic prompt restoration from ledger summaries and opaque-host checkpoint alternatives remain uninspected. Consequence: no complete resumability claim from Pi-shaped metadata.
6. **Source doctrine is not canonical storage truth.** [MEM-CLM-file-consumption](#mem-clm-file-consumption)'s append-only lessons description differs from actual mutable SKILL lessons in [MEM-OBJ-skill-lessons](#mem-obj-skill-lessons). Consequence: retain the afforded consumer role while qualifying layout/immutability claims.
7. **Remaining included parts.** Coverage-table rows identify uninspected notebook writers, report generators, hint internals, evidence redaction, TypeScript lifecycle/package/compaction/control-plane memory packs, production trace/dataset curation, session branching and model-serving reload. Their loaders or supplied runtime routes give some positive coverage, but neither full provenance nor universal admission/retention can be concluded. In particular, [RT-CMP-training-checkpoints](runtime.md#rt-cmp-training-checkpoints) does not by itself establish the origin of all training traces or a future exercised serving path.

No new declaration duplicates an existing supplied referent after comparison: new objects describe previously undeclared retained inputs/results, maintenance/request routes are distinct, and the compaction route declares its containing runtime route. No supplied record is superseded. Actual theory formulation, explanatory reasons in generated advice, independent learning benefit and exercised self-improvement remain uninspected; requests for explanations and retained text plumbing do not settle them.

## Limitations and checks

Static implementation establishes the supported wiring and the negative boundary inside the two consolidation functions, not successful operation. No archived learned corpus, trace, benchmark or counterfactual experiment was inspected. Exact model/checkpoint versions are not fixed by this source revision; runtime component records carry those limits. The target source and inspected method inputs were kept read-only; no tests/providers/examples/services were executed. Additional source paths above all belong to SRC-1 at the same full commit; no new source was admitted.

Correction-round source identity recheck: HEAD still equals the reviewed full commit and `git status --short` is empty. Static inspection added the part-consumer paths listed in the coverage table; supplied method/type/records and refusal inputs were read completely. A bounded search mistakenly named `autocontext/src/autocontext/harness/mutations.py` and returned exit 2; the actual mutations package's gate and applier were then read directly. No claim uses that failed path.

The attempted search of `autocontext/src/autocontext/cli_registration.py` reported that no such file exists; no finding relies on it. Actual CLI imports and package-command registration were read instead. A compound search stopped with exit 1 when its freshness query found no match in the initially named helper; the dedicated freshness module was then directly inspected. These are search limits, not target behavior or absence findings.

Deterministic validation: invocation-specific `commonplace-run validate-output` exited successfully with “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Validation checks form and quotation occurrence, not empirical truth, exhaustive coverage or acceptance.

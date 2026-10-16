---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent report verification of Eigenius's formalization, retained state, domain checking and notebook workflow at its frozen partial-loop boundary."
run-id: AAS-2026-10-15-eigenius-fe68ed89519b-01
reviewed-boundary: "836498ebd99733067d45aa6f7b09d4ff5035dd99"
---

# Eigenius report verification

## Verification

The reports support a bounded implementation account, with one additional inventory limit below. I read every supplied member, declaration, annotation and integration issue. The correction-answer files are empty; the structural report reports no findings. I independently inspected source text rather than treating the analysts' validation results as support. The source checkout's HEAD matches the [registered revision](boundary.md#source-register), and its status is clean. No target code, tests, examples or providers were executed. Implementation evidence does not establish successful operation or benefit.

### Runtime and workflow

I traced the CLI's persistent-backend selection and formalizer injection, kernel request validation and task creation, formalizer progression, notebook polling/result fetch, and SDK-mediated optional landing. SRC-1 implementation: `cli/src/main.rs`, `kernel/src/server/formalize.rs`, `crates/eigenius-encoding/src/formalize.rs`, `notebooks/src/runtime/notebookStore.ts`, and `clients/eigenius-ts/src/client.ts`. These support [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize), [RT-OBJ-formalization-artifact](runtime.md#rt-obj-formalization-artifact) and the [workflow completion and rejection account](workflow.md#optional-admission-and-rejection-path). The ignored terminal writes, non-cancelling client deadline, explicit result fetch and immediate optional Load are correctly distinguished. No mandatory human review, guaranteed terminal-result durability or automatic repair is inferred.

For [RT-RTE-reading-selection](runtime.md#rt-rte-reading-selection), I followed candidate presentation, collision refusal, bounded structure groups, decision context and index resolution in SRC-1, `kernel/src/dcg/parse/resolve.rs` and `kernel/src/dcg/reading_ranker.rs`. Membership and distinguishability support a bounded selector, not authorial fidelity. Model configuration, provider request construction and CompleteText implementation support the three runtime model-component records and their distinct mutability/version uncertainties: SRC-1, `kernel/src/dcg/model_config.rs`, `kernel/src/dcg/anthropic_client.rs`, and `orchestration/src/components/complete_text.ts`.

Load's institution-bearing pipeline, program/query output pipelines and direct glossary persistence have materially different admission paths. I checked their executable phase choices and ordering in SRC-1, `kernel/src/server/load.rs`, `kernel/src/commit/pipeline.rs`, `kernel/src/commit/phases.rs`, `kernel/src/server/programs.rs`, `kernel/src/server/query.rs` and `kernel/src/dcg/pipeline.rs`. [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) does not claim universal validation. The complete ValidateProgram handler supports the narrow [RT-ABS-program-typecheck](runtime.md#rt-abs-program-typecheck), not a system-wide absence. Inline and IRI execution reach the shared evaluator; retained symbolic control and model-interpreted prompt authority remain distinct. SRC-1, `kernel/src/program/eval_io.rs` and the runtime program records support this distinction. Startup registration and the local/Docker spawner implementations support [RT-RTE-runtime-registration](runtime.md#rt-rte-runtime-registration), without a deployment or adversarial-containment guarantee.

### Retained state and later consumers

I checked the draw envelope and all four payload records, their question keys and replay consumers against SRC-1, `kernel/src/dcg/draw.rs`, `kernel/src/dcg/reading_ranker.rs`, `kernel/src/dcg/sense_ranker.rs`, `kernel/src/dcg/proposer_record.rs` and `crates/eigenius-encoding/src/claim_kind.rs`. Selection/proposal contextual keys and the narrower kind key are not interchangeable. Rationales are retained stated reasons, not evidence of hidden reasoning or an implemented criticism cycle.

The branch reset, old-head read ordering, live-only transcript collection and empty-draw return independently support [MEM-RTE-draw-retention](memory.md#mem-rte-draw-retention). An all-replay round need not preserve the original draws at the new document head. SRC-1, `crates/eigenius-encoding/tests/served_formalization.rs`, uses inline recordings and compares one served artifact with a fixture; it does not establish three-round branch replay or a passing execution.

I traced query delivery and INTO admission, similarity strategy/pool selection, segment validation/shadow filtering, and non-gating index refresh. SRC-1 implementation: `kernel/src/server/query.rs`, `kernel/src/query/evaluate/similarity.rs`, `kernel/src/query/vector/search.rs` and `kernel/src/server/hooks.rs`. These support [MEM-RTE-query-resources](memory.md#mem-rte-query-resources), [MEM-OBJ-vector-segment](memory.md#mem-obj-vector-segment), [MEM-RTE-index-refresh](memory.md#mem-rte-index-refresh) and retained institution-dispatch authority. They establish later consumers, not complete recall or scientific endorsement. Consolidation's first-modification/tombstone handling and GC's current-session task roots support the restricted [MEM-RTE-state-maintenance](memory.md#mem-rte-state-maintenance): SRC-1, `kernel/src/layer/consolidate.rs` and `kernel/src/server/gc.rs`. Notebook resource conversion, publication and referenced-cell reconstruction support [MEM-OBJ-notebook-cells](memory.md#mem-obj-notebook-cells) and [MEM-RTE-notebook-reopen](memory.md#mem-rte-notebook-reopen), not a complete execution checkpoint: SRC-1, `clients/eigenius-ts/src/notebook.ts`, `clients/eigenius-ts/src/client.ts` and `notebooks/src/runtime/publishedNotebooks.ts`.

### Epistemic scope

I independently followed the proof input extraction, permitted-axiom configuration, export checking, expected-proposition comparison, trace production, disposition and later witness consumer. SRC-1 implementation: `crates/eigenius-lean/src/institution.rs`, `crates/eigenius-lean/src/checker.rs`, `kernel/src/commit/phases.rs`, `kernel/src/layer/witness_admission.rs`, `kernel/src/validation/rules/eigentt_value.rs` and `kernel/src/nbe/check/mod.rs`. The proof-input and verification-trace objects have distinct roles. [EPI-RTE-lean-check](epistemic.md#epi-rte-lean-check), [EPI-RTE-verdict-disposition](epistemic.md#epi-rte-verdict-disposition) and [EPI-RTE-witness-consumption](epistemic.md#epi-rte-witness-consumption) support conditional formal acceptance and consequential later use. They do not prove global soundness, authenticate arbitrary low-level layers or establish empirical premises. ProgramTrace supplies no witness category; rebinding can withdraw ancestor credit. The report preserves these restrictions and the trusted follow-up boundary.

The common statistical result path distinguishes a runnable-plan gate from a positive effect decision and attaches a canonical proposition only conditionally. The executable p/alpha and direction tests support [EPI-RTE-statistical-decision](epistemic.md#epi-rte-statistical-decision), not general scientific acceptance: SRC-1, `crates/eigenius-statistics/src/validate.rs`. CompleteText's literal interpolation supports its bounded text-transformation record, without establishing semantic preservation. File verification and sampled/deferred layout checks support the pinned-file object and the two diagnostic routes, without durable endorsement: SRC-1, `cli/src/data.rs`.

I compared the public claim records against SRC-1, `README.md` and `orchestration/src/mcp/server.ts`. The report correctly retains the discrepancy between the README's older correspondence mechanism and the implemented direct statement comparison. Neither the four-category prose nor “kernel-checked claims” licenses the broader guarantees the reports withhold. Implemented checks, observed accepted discoveries, learning, reflection and self-improvement remain separate conclusions.

### Identity, conflicts and omission search

All declared `Part of:` relations preserve meaningful containers: payloads within draws, draw retention within formalization, verdict disposition within Load, and prompt supply within execution. I checked the remaining identity comparisons in [reconciliation](reconciliation.md#record-identity-and-containment), including corpus versus its contents, provider versus vector state, proof checking versus admission, and query versus its INTO sub-operation. The broader query record remains valid alongside the narrower retention account. No supersession is needed. Reconciliation's integration dispositions preserve the replay-horizon and key qualifications, additional mutation route, partial retrieval state and scoped proof acceptance. No unresolved inter-report contradiction was found; a README/implementation mismatch is not an analyst conflict.

Omission questions were selected from the frozen top-level tree, shipped CLI/MCP/notebook callers and producer-to-consumer dependencies: could another caller collapse generation into mandatory admission, could alternate writes invalidate a universal gate claim, and could persistence/task APIs justify stronger replay or recovery claims? Independent caller and pipeline reads above preserve the reports' distinctions. I additionally inspected SRC-1, `kernel/src/server/tasks.rs`, for cancellation state changes and `kernel/src/server/reflect.rs` for another trace-admission seam. Neither justifies strengthening notebook recovery or making a system-wide negative about reflective behavior. The latter establishes the local inventory omission retained below.

Further omission expansion stopped because these questions have supported dispositions, the reports expressly retain a partial loop, and no identified challenge remains to their central positive findings or emitted evidence strengths. Unassessed importers, workers, complete checker internals, maintenance variants and evaluator designs still prevent whole-system coverage, universal trust or benefit comparisons; they are not evidenced absences. Existing, faithfully scoped uncertainty is not converted into additional defects.

## Blockers

none

## Limits

- The trace-write inventory is incomplete. [MEM-OBJ-layer-resources](memory.md#mem-obj-layer-resources), [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) and [EPI-RTE-witness-consumption](epistemic.md#epi-rte-witness-consumption) do not enumerate the separate Reflect RPC's trace-ingestion path. Direct SRC-1 implementation inspection of `kernel/src/server/reflect.rs` shows request-supplied resources staged and committed through WithRetroactive without AutoOnLoad. Its pipeline construction is explicit:
  > let root = crate::commit::LayerEmission::from_builder(
  >     crate::commit::LayerRole::User,
  >     "reflect",
  >     crate::commit::PipelineKind::WithRetroactive,
  >     crate::commit::EmissionKind::Child,
  >     working,
  > );
  > --- `kernel/src/server/reflect.rs`
  Withhold exhaustive comparisons of trace-acquisition surfaces and evidence-admission coverage, including any inference that Load, program output and INTO exhaust mutation paths. This does not invalidate the reported existence of replay, scoped proof checking or later witness consumption: the reports already withhold universal gate coverage and global soundness. The handler alone also does not establish a self-reflective criticism or learning loop.

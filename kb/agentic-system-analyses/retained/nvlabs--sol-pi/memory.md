---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "SoL-Pi memory: exact observation archives, selected diagnostic receipts, native compaction, delegated transcript transfer and visual crop reuse."
run-id: AAS-2026-10-14-sol-pi-42f04fbbc6bb-01
source-identity: "https://github.com/NVlabs/SoL-Pi"
reviewed-boundary: "41fa7e0e230bedc5e639aed2e7b9cc5698726db1"
---

# SoL-Pi memory report

## Boundary and evidence

The subject is the standalone SoL-Pi extension and its two shipped example integrations at SRC-1, commit `41fa7e0e230bedc5e639aed2e7b9cc5698726db1`. The [boundary](boundary.md) owns source identity and exclusions. Memory scope follows the runtime's context routes: ObservationPack, Evidence-Preserving Reducer, Online Context Compact (OCC), Skill transcript export/result reload and Visual crop artifacts. Configuration and fused file mutation are included as admission and external-state surfaces, not automatically classified as learned memory.

Direct reads for this member covered `src/sol-pi/index.ts`, `src/sol-pi/runtime-paths.ts`, ObservationPack's index/object implementation, reducer candidate/archive/index/receipt/journal implementations, OCC state/tools/extension implementations, the complete Skill transcript exporter, selected launcher functions, and Visual's scene executor and complete Python helper. These are implementation evidence. The supplied runtime contributes the config, provider, economic and action-fusion detail cited below; those findings are distinguished from direct reads. A bounded search of `README.md`, `SECURITY.md`, `docs/compatibility.md` and mechanism test declarations checked retention doctrine and evaluator entry points. Test declarations are not test results.

No target code, test, model call or example was executed. Upstream Pi owns session persistence, native summary construction and model input assembly beyond the inspected extension calls. Provider weights and host hook delivery are not frozen. These limits prevent claims about actual summary fidelity, recall behavior, compliance, savings or successful task completion, not the implementation findings below.

| Entry point / operation | SRC-1 path and inspection basis | Coverage and limit |
|---|---|---|
| Default session-start admission; exported feature factories | `src/sol-pi/index.ts`, direct; config policy supplied by runtime | [RT-RTE-config-admission](runtime.md#rt-rte-config-admission); programmatic callers can bypass file-loader trust checks. Actual configuration author/grants unknown. |
| Fused mutation and shell; later file read | `src/sol-pi/extensions/action-fusion/index.ts`, supplied runtime | [RT-RTE-action-fusion](runtime.md#rt-rte-action-fusion); effects persist as arbitrary workspace products. Content/admission of any particular instruction file is not established. |
| Context projection, archive creation, restore accounting and `obs_recall` | `src/sol-pi/extensions/observation-pack/index.ts`, `src/sol-pi/extensions/observation-pack/observation.ts`, direct | [RT-RTE-observation-replay](runtime.md#rt-rte-observation-replay), [MEM-OBJ-observation](#mem-obj-observation); ledger helper not directly read; no ledger-to-model route established. |
| Plain bash, fused suffix and full-output temporary-file admission | `src/sol-pi/extensions/evidence-preserving-reducer/candidate.ts`, direct | [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt); full log preferred when safe-file checks pass; otherwise inline preview is the reference. |
| Archive, provider result admission, failure fallback, receipt and journal | `src/sol-pi/extensions/evidence-preserving-reducer/archive.ts`, `src/sol-pi/extensions/evidence-preserving-reducer/index.ts`, `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`, `src/sol-pi/extensions/evidence-preserving-reducer/journal.ts`, direct; provider details supplied | [MEM-OBJ-archive-object](#mem-obj-archive-object), [MEM-OBJ-validated-receipt](#mem-obj-validated-receipt), [MEM-OBJ-reducer-journal](#mem-obj-reducer-journal). Local validation is not semantic completeness. |
| `update_plan`, request observations, boundary selection, restore, correction and native/manual compaction callbacks | `src/sol-pi/extensions/online-context-compact/state.ts`, `src/sol-pi/extensions/online-context-compact/tools.ts`, `src/sol-pi/extensions/online-context-compact/extension.ts`, direct; economic arithmetic supplied | [RT-OBJ-online-state](runtime.md#rt-obj-online-state), [MEM-OBJ-progress-summary](#mem-obj-progress-summary), [RT-RTE-online-compaction](runtime.md#rt-rte-online-compaction). Native summary implementation uninspected external dependency. |
| Persistent and no-session roots; retention | `src/sol-pi/runtime-paths.ts`, direct; retention documentation searched | Observation and reducer records; in-memory Pi sessions still produce disk archives. No automatic cross-process recovery follows from a temporary directory. |
| Host transcript export, opt-in prefix, isolated child context | `examples/sol-pi-skill/bin/sol-pi-context`, direct complete; `examples/sol-pi-skill/bin/sol-pi-run` prefix behavior supplied runtime | [MEM-OBJ-context-export](#mem-obj-context-export), [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff). Host transcript authenticity/runtime dispatch unobserved. |
| Run completion, status/result/wait/list reload, notification and usage accounting | `examples/sol-pi-skill/bin/sol-pi-run`, direct functions `summarize`, `run_task`, `run_state`, status/wait/result/list and hook report/notify | [MEM-OBJ-run-result](#mem-obj-run-result), [MEM-OBJ-reducer-journal](#mem-obj-reducer-journal); setup, skill fallback and hook dispatch rely on supplied runtime/boundary rather than new full reads. |
| Visual prompt policy and magnify production/cache reuse/image delivery | `examples/solpi-visual/src/scene/index.ts`, `examples/solpi-visual/src/scene/magnify.py`, direct complete | [MEM-OBJ-magnify-artifact](#mem-obj-magnify-artifact), [RT-RTE-visual-inspection](runtime.md#rt-rte-visual-inspection), [RT-BAP-visual-policy](runtime.md#rt-bap-visual-policy). Rendering and evaluation remain external. |
| Evaluators and maintenance doctrine | Mechanism `tests/` declarations searched; `README.md`, `SECURITY.md`, `docs/compatibility.md` searched | Rejection/recovery is grounded in implementation, not inferred from test names. Exhaustive assertion coverage and live-test success not assessed. |

## Core ideas

1. **Keep exact bytes outside context and alter replay, not history.** ObservationPack archives selected successful text results and replaces repeated provider replay with a pointer and literal edge excerpts. Model-requested pages can bring exact text back. This is neither a generated semantic summary nor automatic evidence relevance selection ([RT-RTE-observation-replay](runtime.md#rt-rte-observation-replay), [MEM-OBJ-observation](#mem-obj-observation)).
2. **Separate evidence selection from diagnosis.** The reducer's isolated model selects quotes; code checks membership, status and size before substituting a receipt. The foreground model retains diagnosis and repair authority. Calling the reducer “lossless” does not make its delivered receipt complete: omitted material remains in the archive, not in the receipt ([RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt), [MEM-OBJ-validated-receipt](#mem-obj-validated-receipt)).
3. **Retain control estimates separately from the native summary.** OCC persists plans and trace-derived budget estimates. Its code later consumes those estimates to select a compaction boundary. The model later receives Pi's summary/recent tail and a generic continuation, not an automatically injected `pendingProgress` checkpoint. Native summarization is a distinct transformation with an external implementation ([RT-OBJ-online-state](runtime.md#rt-obj-online-state), [MEM-OBJ-progress-summary](#mem-obj-progress-summary), [RT-RTE-online-compaction](runtime.md#rt-rte-online-compaction)).
4. **Delegate with a selected input and a narrow return, but shared workspace effects.** Skill export trims a host transcript before starting an independent Pi context. The parent later receives selected final text/status and change information, not the child's complete internal conversation. Files modified in the shared cwd escape this conversational narrowing ([RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff), [MEM-OBJ-context-export](#mem-obj-context-export), [MEM-OBJ-run-result](#mem-obj-run-result)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-observation
Label: Observation archive and replay metadata

Source-native `Observation` describes raw UTF-8 tool text plus symbolic id/hash/size/tool metadata; files live under `<runtimeRoot>/observation-pack/objects/<id>.txt`. Its natural-language content can influence the foreground model as evidence, not as a new system instruction. Identity hashes tool name, tool-call id and content hash, so identical text from distinct tool calls need not share an id. No counterpart object is declared in the supplied runtime; closest record is [RT-RTE-observation-replay](runtime.md#rt-rte-observation-replay), the production/consumption route, not this retained payload (SRC-1, `src/sol-pi/extensions/observation-pack/observation.ts`).

The stored text is not derived memory. The placeholder is a deterministic derived display containing metadata, recall guidance and complete head/tail lines with a total excerpt budget of 1024 bytes; long individual lines can leave an edge excerpt empty. Replay counts are access metadata held in a root/id map, with assistant-history fallback after restoration. JSONL full/placeholder/recall ledger writes are operational records, not text automatically replayed to the model. No later policy consumer of that ledger was established by the directly read index (SRC-1, `src/sol-pi/extensions/observation-pack/index.ts`, `src/sol-pi/extensions/observation-pack/observation.ts`).

> const id = `obs_${hash(`${message.toolName}\0${message.toolCallId}\0${contentHash}`).slice(0, 24)}`;
> --- `src/sol-pi/extensions/observation-pack/observation.ts`

Existing archives are hash/size checked during packing. Recall itself checks a regular non-symlink file and reads a bounded slice; it does not revalidate the whole content hash on each page. Thus “exact recall” describes the archived-text route under intact-storage assumptions, not tamper-proof readback. This qualification complements, rather than replaces, the runtime's external-corruption limit (SRC-1, `src/sol-pi/extensions/observation-pack/observation.ts`).

#### MEM-OBJ-archive-object
Label: Reducer raw-log archive

Source-native `ArchiveObject`: raw natural-language diagnostic output, physically a local UTF-8 file at a SHA-256-derived path under the reducer store root; hash/byte/character/line/path fields are symbolic metadata. It is distinct from an observation object: its producer, identity, error eligibility and later shell-read consumer differ. Closest supplied record is [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt), not an object declaration (SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/archive.ts`).

Archive acquisition precedes provider response validation. Rejected receipts therefore can leave a raw archive and fallback journal entry while the original tool observation remains visible. Existing same-name files with different content throw integrity failures. There is no expiry operation in the inspected archive implementation; host/caller deletion can invalidate receipt paths. The reducer sees the selected body; the later foreground agent is explicitly offered ranged bash reads of this path. Neither consumer is guaranteed to receive the command's full original output when candidate loading fell back to inline text (SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/archive.ts`, `src/sol-pi/extensions/evidence-preserving-reducer/candidate.ts`, `src/sol-pi/extensions/evidence-preserving-reducer/index.ts`).

> const archive = await archiveBody(archiveRoot(config), body);
> --- `src/sol-pi/extensions/evidence-preserving-reducer/index.ts`

#### MEM-OBJ-validated-receipt
Label: ValidatedReceipt and delivered evidence receipt

Source-native `ValidatedReceipt` has symbolic status/uncertainty/evidence fields and natural-language exact quotes. `receiptText` renders those fields, quote hashes/line locations, model usage and archive pointer as model-visible text. It is a derived selection of a trace, not a replacement raw trace or a verified diagnosis. It resides in the substituted tool result; persistence/replay of that result is host-owned. No counterpart operative object is declared in runtime; [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt) governs its admission, while [RT-BAP-reducer-instructions](runtime.md#rt-bap-reducer-instructions) governs the producer model, a distinct consumer (SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`, `src/sol-pi/extensions/evidence-preserving-reducer/index.ts`).

Software verifies schema/source hash/error-derived status, bounded quotes and their occurrence, then net reduction; it does not verify that evidence kinds, uncertainty or apparent causal importance are semantically correct. A failure-signal regex demands a fatal/failure-labelled quote, not coverage of all failures. The quote can be a contiguous substring rather than a complete source line. Literal quotes retain source wording, but the receipt does not retain the model's selection reasons. The foreground consumer receives a warning about authority and a readback instruction, not the reducer's internal reasoning (SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`).

> "readback=use bash with an explicit byte or line range on source_artifact when exact context is needed",
> --- `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`

The prompt's “lossless” label is bounded by the code's selection, not adopted as a completeness claim:

> "You are a lossless test/build output reducer.",
> --- `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`

#### MEM-OBJ-reducer-journal
Label: Reducer decision journal

Source-native reducer journal entries are symbolic custom Pi session entries with candidate, provider-response, applied and fallback kinds. Source hashes/paths, usage, receipt counts and rejection reasons describe provenance/admission; they are not a second semantic summary of the diagnostic log. Closest supplied record is [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt); no supplied journal object exists. The journal is separate from both raw archive and receipt because its consumer and authority differ (SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/journal.ts`, `src/sol-pi/extensions/evidence-preserving-reducer/index.ts`).

> * The entries never enter the LLM context. They record which results were
> * candidates, which were delegated, and why each fallback happened.
> --- `src/sol-pi/extensions/evidence-preserving-reducer/journal.ts`

A concrete shipped later consumer does exist outside the foreground context: Skill's `summarize` reads reducer custom entries, counts applied/fallback outcomes and adds provider-response usage priced from a separate recorded price entry. The derived result reaches status/report consumers. It is accounting influence, not diagnosis authority or learning of a reducer policy (SRC-1, `examples/sol-pi-skill/bin/sol-pi-run`).

> if data.get('kind') == 'provider_response':
>     u = data.get('usage') or {}
> --- `examples/sol-pi-skill/bin/sol-pi-run`

#### MEM-OBJ-progress-summary
Label: ProgressSummary within online state

Part of: [RT-OBJ-online-state](runtime.md#rt-obj-online-state)

`ProgressSummary` is the separately identifiable task-content part of `OnlineState.pendingProgress`: natural-language goal, verification, decisions and next-work strings with symbolic step/file associations, stored inside custom Pi session entries. Its content lineage is model-authored `update_plan` input, not independent command verification. Only a completion transition with supplied progress constructs a summary, using the first completed step's id and unfinished goals for next work (SRC-1, `src/sol-pi/extensions/online-context-compact/extension.ts`, `src/sol-pi/extensions/online-context-compact/state.ts`).

> pendingProgress: progress ? [...state.pendingProgress, progress] : state.pendingProgress,
> --- `src/sol-pi/extensions/online-context-compact/state.ts`

It can retain stated decisions and verification assertions, but no required rationale or criticism field exists. Restore parses and carries it; `recordCompaction`, correction and completed-plan handoff clear it. The directly inspected OCC code passes only a fixed preservation instruction to native compaction, not this array, and adds only a generic continuation. Therefore persistence of these strings does not establish a dedicated model read-back checkpoint. Original plan-tool messages may still occur in history selected by the external summarizer (SRC-1, `src/sol-pi/extensions/online-context-compact/extension.ts`, `src/sol-pi/extensions/online-context-compact/state.ts`).

#### MEM-OBJ-context-export
Label: Exported host conversation prefix

Source-native exporter output is a natural-language Markdown prefix derived from host JSONL transcript rows, optional host compaction summaries and trimmed tool traces. It is written to the child prompt and retained by the launcher as `prompt.md`; transcript/session/cwd strings provide symbolic provenance. It differs from the `result.json` return and from the child's session history. Closest supplied record is [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff), a route spanning all those objects; no counterpart object is supplied (SRC-1, `examples/sol-pi-skill/bin/sol-pi-context`, `examples/sol-pi-skill/bin/sol-pi-run`).

Export begins at the latest recognized host compaction, reuses its summary/replacement history, excludes nonselected roles/blocks, renders tool calls as short argument summaries and clips tool text. Default tool limit is 2000 characters; default overall recent-block target is 200000. The newest block is retained even when it alone exceeds the target; headers and clipping markers also mean this is not a strict output bound. By default the most recent recognized handoff and later events are dropped; `--keep-last-request` is an explicit alternate. This is lossy reference context, not shared conversation identity or all original reasons (SRC-1, `examples/sol-pi-skill/bin/sol-pi-context`).

> if total + len(block) > max_chars and kept:
>     break
> --- `examples/sol-pi-skill/bin/sol-pi-context`

Consumer authority is task-reference information in the child prompt, with guidance to reread files before relying on earlier commands. The exporter does not authenticate the historical claims. A user requesting export initiates selection, not approval of every retained statement (SRC-1, `examples/sol-pi-skill/bin/sol-pi-context`; supplied [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff)).

#### MEM-OBJ-run-result
Label: Skill result.json

Source-native `result.json` is symbolic run/status/cost/mechanism/session/event metadata plus natural-language final text/error. It is derived by `summarize` from emitted events, session entries, return code and elapsed time, then persisted in the managed run directory. It is distinct from raw `events.jsonl`, session JSONL, `stderr.log`, prompt and run metadata: the result selects the last nonblank assistant text and aggregates counts rather than retaining all trajectory content. Closest supplied record is [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff); it describes the surrounding route, not a duplicate result object (SRC-1, `examples/sol-pi-skill/bin/sol-pi-run`).

> if text.strip():
>     final = text
> --- `examples/sol-pi-skill/bin/sol-pi-run`

`run_state` prefers the persisted result, otherwise derives partial state from metadata/events and liveness heuristics. `status`, `wait`, `result`, `list` and hook notification consume it. Hook reports deliver trimmed final text, costs, current workspace change information and full-result/session pointers to a parent model through a host reminder/context mechanism. They ask the parent to check changes, not accept completion as verified. The stored `done` flag follows process/stop status, not a task answer oracle. No per-content human approval or automatic patch rollback is inserted at result creation (SRC-1, `examples/sol-pi-skill/bin/sol-pi-run`).

#### MEM-OBJ-magnify-artifact
Label: Magnify crop artifact and RECEIPT.json

Source-native crop PNGs and `RECEIPT.json` persist under a hash-keyed Visual runtime `magnify` directory. PNG pixel arrays encode sampled visual content consumed by the model through image blocks; this is not learned model parameter state. JSON metadata is symbolic provenance: source/tool/output hashes, source size, EXIF orientation, selected boxes, interpolation, scale and coordinate mapping. The readable JSON returned by the helper is a subset of the full receipt, not the image itself. Closest supplied record is [RT-RTE-visual-inspection](runtime.md#rt-rte-visual-inspection); no supplied artifact declaration exists (SRC-1, `examples/solpi-visual/src/scene/magnify.py`, `examples/solpi-visual/src/scene/index.ts`).

The foreground model chooses source/reference and independent boxes. Code admits only supported existing images and bounded nonempty in-frame crops, then deterministically crops/interpolates; a second model does not author new detail. Key construction includes helper hash and complete per-image metadata, including source hash. A later invocation recomputes outputs/identity and can verify/reuse matching files. An existing same-key artifact with changed receipt or PNG hashes is rejected rather than overwritten. The helper cleans its temporary construction directory; it does not delete committed artifacts in that path (SRC-1, `examples/solpi-visual/src/scene/magnify.py`).

> if (target/'RECEIPT.json').read_bytes()!=encoded or any(digest((target/(k+'.png')).read_bytes())!=v[1]['output_sha256'] for k,v in assets.items()):raise ValueError('Existing artifact differs; refusing overwrite')
> --- `examples/solpi-visual/src/scene/magnify.py`

This fills the runtime's explicitly uninspected cache boundary. It does not establish correctness of interpolation, filesystem race immunity or actual model image understanding. Crop reuse can deliver retained image bytes at a later invocation, but there is no inspected unsolicited replay of a past crop or learned visual policy update.

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-observation-replay](runtime.md#rt-rte-observation-replay)

Memory read-back is two operations, not one inferred retrieval faculty: code independently selects repeated eligible retained messages for placeholder projection, while the foreground model explicitly requests an id/byte offset for archive read-back. The first selector uses error flag, pure-text content, byte threshold, receipt marker and replay count; the second uses no semantic relevance ranker. Recall's hard output bounds are 16 KiB/400 lines including headers, with reserved content budgets of 15872 bytes/398 lines. Offset/next-offset chooses a page, not content-targeted evidence selection. Foreground text delivery is wired; changed decisions are unobserved (SRC-1, `src/sol-pi/extensions/observation-pack/index.ts`, `src/sol-pi/extensions/observation-pack/observation.ts`).

> const RECALL_MAX_BYTES = 16 * 1024;
> const RECALL_MAX_LINES = 400;
> --- `src/sol-pi/extensions/observation-pack/index.ts`

Storage admission is code-owned: eligibility and archive integrity, then per-observation fail-open projection. Authorship belongs to the originating tool/workspace process, whose text may itself contain external data; tool labels do not authenticate that provenance. No human reviews each archived item or excerpt. Persisted history stays intact. After compaction, a known id and surviving root permit recall; deleted pointers/unknown ids are not recovered by a semantic search tool. Temporary no-session files survive shutdown by design but root lookup is process-local (SRC-1, `src/sol-pi/runtime-paths.ts`; [MEM-OBJ-observation](#mem-obj-observation)).

#### On [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt)

Write agency is split: originating tools produce logs, reducer model proposes selected evidence, code admits the receipt and Pi persists the resulting observation under its session contract. The body can come from a safe Pi full-output file or inline output. A full-output pointer is an alternative acquisition path, not proof that every admitted archive is complete. No human content veto is added. Raw-to-derived-to-later-consumer chain: tool log → [MEM-OBJ-archive-object](#mem-obj-archive-object) → [MEM-OBJ-validated-receipt](#mem-obj-validated-receipt) → later foreground context; a model-requested shell range can return omitted source bytes. Journal → Skill summary is a separate accounting chain, not automatic foreground memory (SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/candidate.ts`, `src/sol-pi/extensions/evidence-preserving-reducer/index.ts`, `examples/sol-pi-skill/bin/sol-pi-run`).

Admission preserves raw evidence outside the window and quoted source wording inside it; it need not preserve selection rationale or all failures. Failed model calls, invalid receipts and non-smaller receipts ordinarily return no replacement. Archive creation occurs before those failures, so rejection does not mean erasing retained raw input. Archive/integrity and journal exceptions are not all covered by the provider catch (SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/index.ts`). Source trust remains limited despite the producer instruction and local checks documented in [RT-BAP-reducer-instructions](runtime.md#rt-bap-reducer-instructions).

#### On [RT-OBJ-online-state](runtime.md#rt-obj-online-state)

The symbolic control part has a direct later code consumer: provider observations update request/growth/debt statistics; `turn_end` reads them with current projected context, plan status and window information to decide compaction. `restoreOnlineState` scans the active branch backward for a valid entry, skips malformed entries and otherwise initializes defaults. Code authors these measurements; the foreground model authors plan/status/progress content. Schema admission verifies shape, not truthful completion or verification. User steering/correction resets plan/estimates without undoing completed file effects; compaction preserves plan but clears pending progress and size baseline (SRC-1, `src/sol-pi/extensions/online-context-compact/state.ts`, `src/sol-pi/extensions/online-context-compact/extension.ts`).

> if (entry?.type !== "custom" || entry.customType !== ONLINE_STATE_ENTRY) continue;
> const state = parseOnlineState(entry.data);
> if (state) return state;
> --- `src/sol-pi/extensions/online-context-compact/state.ts`

This is automatic trace-fed control-state adaptation with retained estimates affecting later context decisions, not merely raw-log retention. It does not establish improved capacity, a revised economic theory or model parameter learning. [MEM-OBJ-progress-summary](#mem-obj-progress-summary) separates task-content strings from the estimate consumer.

#### On [RT-RTE-online-compaction](runtime.md#rt-rte-online-compaction)

There are two retained products: versioned control state consumed by extension code, and Pi's natural-language summary/recent tail consumed by later model invocations. The extension requests preservation of work/verification/decisions/remaining work but does not implement or inspect the summary generator. No additional task-specific checkpoint injection is established. Model self-reports nominate boundaries; code uses tool-success, economic and window gates; manual/native compaction bypasses that selection but still updates state through `session_compact` (SRC-1, `src/sol-pi/extensions/online-context-compact/extension.ts`; supplied economics in [RT-RTE-online-compaction](runtime.md#rt-rte-online-compaction)).

> customInstructions: BOUNDARY_COMPACTION_INSTRUCTIONS,
> --- `src/sol-pi/extensions/online-context-compact/extension.ts`

The 20000-token recent-tail default and 1000-token summary estimate are selection inputs, not enforced summary output size or known actual retained-tail setting. Selected old history is summarized, recent material remains under Pi's native cut, and a generic hidden message starts a later turn. Recovery from recognized precommit refusals retains existing context and continues; unknown errors/cancellation are distinct. Summary rationale retention and factual faithfulness remain uninspected, not absent. Access to original session history is not equivalent to automatic model-visible replay after a cut (SRC-1, `src/sol-pi/extensions/online-context-compact/extension.ts`).

#### On [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff)

[MEM-OBJ-context-export](#mem-obj-context-export) crosses into the child as selected reference text; [MEM-OBJ-run-result](#mem-obj-run-result) crosses back as selected final text and metadata. Inner raw events/session logs remain reachable through returned paths, but default host notification does not replay them. The child frame therefore keeps most conversation out of the parent context, while shared filesystem effects escape independently of the return. This resembles a separate call frame only for context isolation, not a sandbox or a guarantee that only a return value escapes (SRC-1, `examples/sol-pi-skill/bin/sol-pi-run`, `examples/sol-pi-skill/bin/sol-pi-context`).

Stored results reach concrete later invocations of CLI and hook consumers, not hypothetical API callers. Returned status/cost/final text can inform a parent but has no mechanical authority to certify task correctness. Timeout terminates processes without reverting workspace mutations; `result.json` and raw traces remain diagnostic artifacts. The exact host delivery/compliance remains unobserved (SRC-1, `examples/sol-pi-skill/bin/sol-pi-run`).

#### On [RT-RTE-visual-inspection](runtime.md#rt-rte-visual-inspection)

The helper's later same-input cache path verifies receipt and output hashes before reuse, resolving the supplied runtime's explicit cache uncertainty. The executor then reads actual PNG bytes and delivers image blocks alongside the selected receipt display. Full provenance stays in `RECEIPT.json`; returned JSON is narrower. Cache reuse does not make a prior interpretation authoritative, and receipt labels such as `evaluation_unchanged` are not an evaluator result (SRC-1, `examples/solpi-visual/src/scene/magnify.py`, `examples/solpi-visual/src/scene/index.ts`; [MEM-OBJ-magnify-artifact](#mem-obj-magnify-artifact)).

#### On [RT-OBJ-sol-pi-config](runtime.md#rt-obj-sol-pi-config)

Configuration is persistent symbolic capability/policy state, not automatically an experience-derived artifact. The supplied file route permits human/operator authorship but does not establish the author of any actual file. Default loading validates a selected file; exported registration/factory APIs leave initialization ownership with their caller. Ordinary ongoing transformations remain code/model owned after initialization. One-time registration is not a live content-curation loop (SRC-1, `src/sol-pi/index.ts`; supplied [RT-RTE-config-admission](runtime.md#rt-rte-config-admission)).

## Write side

| Mechanism | Admission versus authorship | Retained result, rejection and withdrawal |
|---|---|---|
| Observation packing | Tool producers supply raw text; code eligibility/integrity checks admit archives and projection. No per-item human approval. | [MEM-OBJ-observation](#mem-obj-observation); projection is nondestructive to history. Per-item packing failure preserves original context message. External deletion removes recallability, not stored host history. |
| Diagnostic reduction | Tool output supplies raw input; model proposes quotes; software decides acceptance. Source body/hash/error metadata are local check references, not a correct-diagnosis oracle. | [MEM-OBJ-archive-object](#mem-obj-archive-object), [MEM-OBJ-validated-receipt](#mem-obj-validated-receipt), [MEM-OBJ-reducer-journal](#mem-obj-reducer-journal). Rejection keeps original observation; raw archive/journal may remain. No admitted-receipt retraction protocol was established in the inspected reducer code. |
| OCC plan/progress | Foreground model proposes complete plan and optional evidence assertions. Schema/transition code admits them; tool cancellation can reject. No independent human or command-verification check. | [RT-OBJ-online-state](runtime.md#rt-obj-online-state), [MEM-OBJ-progress-summary](#mem-obj-progress-summary). Correction/handoff/compaction reset different fields; newest valid branch entry restores state. |
| OCC estimates and summary | Code transforms request/context/boundary traces into persisted estimates; economic/window rules select; Pi owns summary generation and commit/refusal. | Estimates influence subsequent code decisions; summary replaces old model context for later invocations. Failed precommit compaction can retain existing context. Summary reasons/fidelity unknown. |
| Skill prefix/result | Caller requests transfer; exporter deterministically filters; child model authors answer; launcher selects and aggregates. Workflow start is not per-content human approval. | [MEM-OBJ-context-export](#mem-obj-context-export), [MEM-OBJ-run-result](#mem-obj-run-result). Failed runs/timeouts preserve diagnostic state and already made workspace effects; parent is asked to check changes. |
| Visual crops | Foreground model requests box/source; helper checks format/dimensions and writes deterministic images/receipt. No secondary model or human crop approval. | [MEM-OBJ-magnify-artifact](#mem-obj-magnify-artifact). Corrupt same-key content rejected; construction temp directories removed; committed crop cache retained. |
| Config / arbitrary file edits | Config author/caller ownership unresolved for actual deployment; loader validates types/trust, while programmatic APIs have caller-owned initialization. Fused edits follow model tool arguments. | [RT-RTE-config-admission](runtime.md#rt-rte-config-admission), [RT-RTE-action-fusion](runtime.md#rt-rte-action-fusion). Arbitrary edited files are not presumed to be adopted instructions or learned knowledge. |

The trace-fed transformations have different later consumers. Raw logs alone have no update authority. The reducer's derived receipt shapes later model input without changing the reducer's static instructions. OCC estimates change future selection by code; native summaries replace accumulated context; Skill export/result transforms traces into later child/parent context. These paths establish retention and delivery, not improved competence or evidence-responsive revision of the shipped strategies. Quotes retain source text; generic reminders do not retain task rationale; result export retains only whatever reasons the selected final text contains (SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`, `src/sol-pi/extensions/online-context-compact/extension.ts`, `examples/sol-pi-skill/bin/sol-pi-run`, `examples/sol-pi-skill/bin/sol-pi-context`).

## Read-back

- **Observation projection is automatic supply; recall is a pull.** Provider-context construction independently selects repeated results for placeholders. The foreground model must explicitly request id/offset pages to recover omitted text. No automatic semantic retrieval from all archives was established in the inspected pack index; raw history is still host-retained. [RT-RTE-observation-replay](runtime.md#rt-rte-observation-replay) and its annotation give budgets and restoration limits.
- **Receipt delivery is automatic substitution; archive recovery is an afforded foreground shell read.** The reducer gets a selected log rather than complete session context, and the foreground gets admitted quote selection rather than nested reasoning. The explicit readback instruction establishes a documented consumer role, not an observed shell read. [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt) distinguishes that affordance from substitution wiring.
- **OCC has code restore and model summary consumption, not one universal checkpoint.** On session start/tree move, code selects latest valid active-branch state. It later uses measured estimates for compaction; Pi supplies summary/tail to the foreground and SoL-Pi triggers continuation. `pendingProgress` persistence alone supplies no dedicated prompt read-back. [RT-OBJ-online-state](runtime.md#rt-obj-online-state), [MEM-OBJ-progress-summary](#mem-obj-progress-summary), [RT-RTE-online-compaction](runtime.md#rt-rte-online-compaction).
- **Skill has explicit inward selection and independently notified outward delivery.** An opt-in or hook-selected transcript becomes a lossy child prefix; later status/result/wait/list and notification reread stored results. Parent receives final/report, while raw events and child history stay outside its default window. [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff), [MEM-OBJ-context-export](#mem-obj-context-export), [MEM-OBJ-run-result](#mem-obj-run-result).
- **Visual cache reuse is exact-input reuse with actual image delivery.** The model chooses paths/boxes; helper identity selects a matching artifact, not relevance-ranked memory. TypeScript reads returned image paths and delivers PNG bytes. [MEM-OBJ-magnify-artifact](#mem-obj-magnify-artifact), [RT-RTE-visual-inspection](runtime.md#rt-rte-visual-inspection).

These mechanisms put archived text outside the window while carrying its pointer by value; the pointer is not automatically dereferenced or counted for liveness. Native compaction leaves summary/tail rather than all archived observations. Separate child context limits conversational replay, not shared-workspace effects. Reachability depends on retained pointers, files, roots and explicit consumers, not a universal managed memory heap (SRC-1, `src/sol-pi/extensions/observation-pack/index.ts`, `src/sol-pi/extensions/online-context-compact/extension.ts`, `examples/sol-pi-skill/bin/sol-pi-run`).

## Integration issues

1. **Runtime cache uncertainty is resolved, not contradicted.** [RT-RTE-visual-inspection](runtime.md#rt-rte-visual-inspection) left Python cache behavior uninspected. [MEM-OBJ-magnify-artifact](#mem-obj-magnify-artifact) establishes helper/source/metadata-derived identity, validation of existing bytes, refusal to overwrite mismatches and temporary-directory cleanup (SRC-1, `examples/solpi-visual/src/scene/magnify.py`). Reconciliation should carry this positive detail without attributing it to the earlier runtime inspection.
2. **Keep OCC progress and native summary separate.** [MEM-OBJ-progress-summary](#mem-obj-progress-summary) is explicitly part of [RT-OBJ-online-state](runtime.md#rt-obj-online-state), not a duplicate container. Its persisted decision strings have no dedicated prompt-injection route in the inspected OCC code. Pi may summarize original messages, but that external mechanism cannot be inferred from parsing custom state. This prevents treating `pendingProgress` as a verified alternate task checkpoint (SRC-1, `src/sol-pi/extensions/online-context-compact/state.ts`, `src/sol-pi/extensions/online-context-compact/extension.ts`).
3. **Scope exactness and trust.** [MEM-OBJ-observation](#mem-obj-observation) adds the recall-time whole-hash verification limit to [RT-RTE-observation-replay](runtime.md#rt-rte-observation-replay); [MEM-OBJ-validated-receipt](#mem-obj-validated-receipt) rejects a completeness reading of the source's “lossless” label while preserving the runtime's exact-membership finding. No supplied positive fact needs correction. Actual summary fidelity, provider interpretation and host delivery remain unknown, preventing operation/benefit claims (SRC-1, `src/sol-pi/extensions/observation-pack/observation.ts`, `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`).
4. **No proposed duplicate or supersession.** New payload objects have no object counterpart in the supplied runtime; their closest route records and distinct identities are stated at each declaration. [MEM-OBJ-progress-summary](#mem-obj-progress-summary) is the sole declared containment relation. Journal accounting adds a shipped later consumer to [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt) and [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff), not a second journal identity.
5. **Remaining inspection limits.** Core helper algorithms not directly reread here rely on the supplied runtime where cited; evaluator assertions and live execution were not exhaustively inspected. Host/native summary internals and actual config authorship/grants remain outside available implementation evidence. No reported source/test result closes these gaps. These are conclusion limits, not blockers or inferred absences.

## Limitations and checks

The frozen checkout's HEAD was rechecked as `41fa7e0e230bedc5e639aed2e7b9cc5698726db1`, with clean tracked status. Input run identity and source identity match the supplied boundary/prompt. Method identity is the supplied memory type, memory job, worker rules and records contract; no other run or prior characterization was used. New reads stayed in SRC-1 and writes stayed within assigned outputs/worker identity. No observed run or causal experiment was introduced.

Source inspection establishes configured wiring and bounded readback affordances, not activation, successful memory use, causal savings, improved capacity, universal secrecy or robust upstream summary behavior. Available but uninspected files are not absent evidence. A validation pass checks structure and quotation occurrence, not semantic support or acceptance.

Validation: output validation completed successfully with the invocation's `commonplace-run validate-output` command.

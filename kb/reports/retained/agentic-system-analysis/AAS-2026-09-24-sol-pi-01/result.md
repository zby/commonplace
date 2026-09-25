---
type: types/agentic-system-analysis-result.md
description: Complete code-grounded analysis of SoL-Pi as an optional Pi extension, with bounded archive, reducer
  and native compaction contracts
run-id: AAS-2026-09-24-sol-pi-01
system: SoL-Pi
run-date: '2026-09-24'
result-disposition: complete
target-class: extension or tool mechanism
boundary-kind: complete artifact, partial loop
reviewed-boundary: 1559b5cb12c72da4a485bc50fe326586b216fb19
analysis-cutoff: '2026-09-24'
evidence-tier: code-grounded
memory-comparison:
  scope: Accumulated SoL-Pi observation and diagnostic archives, derived receipts, projection access metadata, retained
    plan/progress and scheduling statistics, and the native compaction/continuation boundary when the optional mechanisms
    are enabled. Includes host session retention and replay only as source-visible call contracts; excludes Pi internals,
    provider weights, ordinary edited project files and shipped static configuration/instructions.
  axes:
    storage_substrate:
      assessment: known
      basis: wired
      values:
      - files
      - in-memory
      records:
      - OBJ-5
      - OBJ-6
      - OBJ-7
      - OBJ-8
      - OBJ-9
      - OBJ-10
      note: Session-derived archive files and host session-log persistence, with live counters, restored state and
        projected messages in memory; no separate database or vector service is wired.
    representational_form:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - OBJ-5
      - OBJ-7
      - OBJ-8
      - OBJ-9
      note: Visible receipts, plans and control metadata supply natural-language and symbolic parts. Arbitrary retained
        host messages and native compacted replay payload are not fully characterized at this boundary; visible
        text summaries do not establish the complete union.
    lineage:
      assessment: known
      basis: wired
      values:
      - authored
      - imported
      - other-compiled
      - trace-extracted
      records:
      - OBJ-5
      - OBJ-6
      - OBJ-7
      - OBJ-8
      - OBJ-9
      - RTE-10
      note: Agent-authored plans; imported tool observations; mechanically compiled placeholders and scheduling
        statistics; diagnostic evidence extraction and host-contract trace compaction. Host internal derivation
        algorithms remain excluded.
    behavioral_authority:
      assessment: known
      basis: wired
      values:
      - instruction
      - knowledge
      - routing
      - validation
      records:
      - BAP-3
      - BAP-4
      - RTE-6
      - RTE-8
      - RTE-9
      - RTE-10
      note: Evidence and summaries inform the assistant; returned working plans direct remaining work; retained
        plan/statistics route compaction; archived bytes validate candidates and existing objects. Static reducer
        instructions and the generic continuation reminder are not themselves learned memory.
    write_agency:
      assessment: known
      basis: wired
      values:
      - automatic
      records:
      - RTE-4
      - RTE-6
      - RTE-8
      - RTE-9
      - RTE-10
      note: Model-authored update_plan calls and automatic archival, extraction and state appends. Human feature
        adoption and correction input trigger operations but do not establish a manual memory editor.
    curation_operations:
      assessment: known
      basis: wired
      values:
      - consolidate
      - evolve
      - invalidate
      records:
      - RTE-6
      - RTE-8
      - RTE-9
      - RTE-10
      note: Receipts and native compaction reduce retained content; plan/statistics updates evolve state; corrections
        and compaction retire current plan/progress while earlier entries remain. Hash reuse, receipt-local duplicate
        removal and temporary context projection do not establish retained-memory dedup or decay.
    read_back_direction:
      assessment: known
      basis: afforded
      values:
      - pull
      - push
      records:
      - RTE-4
      - RTE-5
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-9
      - RTE-10
      note: obs_recall pull is wired; explicit bash-range archive readback is afforded to the frontier agent. Observation
        projection, state restoration and host-contract compacted continuation supply retained material automatically.
    read_back_signal:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - RTE-4
      - RTE-6
      - RTE-8
      - RTE-9
      note: Visible selection includes coarse size/age projection and latest-valid state, plus reducer judgment
        over diagnostic evidence. Host-owned branch history/compacted-context assembly is passed leaf identity but
        not inspected; its full selection union cannot be inferred from identifiers alone.
    trace_learning:
      assessment: known
      basis: wired
      values:
      - 'yes'
      records:
      - RTE-6
      - RTE-9
      - RTE-10
      note: Automatically retained evidence receipts, native compaction continuation at its call contract, and persisted
        request/token statistics have later behavior-shaping consumers. Novel claims and measured improvement are
        not required.
    trace_source:
      assessment: known
      basis: wired
      values:
      - tool-traces
      - session-logs
      - event-streams
      records:
      - RTE-6
      - RTE-9
      - RTE-10
      note: Diagnostic tool_result traces feed receipts; session history feeds native compaction; provider-request/context/boundary
        events feed persisted scheduler estimates.
    learning_scope:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - RTE-6
      - RTE-9
      - RTE-10
      note: Native continuation explicitly resumes the active parent task. Reducer archives and scheduler histories
        are session-scoped without a demonstrated task reset, preventing a complete per-task/cross-task union. Session
        identity is not a task horizon.
    learning_timing:
      assessment: known
      basis: wired
      values:
      - online
      records:
      - RTE-6
      - RTE-9
      - RTE-10
      note: All qualifying transformations run during ongoing execution or its boundary compaction and resume; no
        offline training or separate staged adoption pipeline is supplied.
    distilled_form:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - RTE-6
      - RTE-9
      - RTE-10
      note: Receipts expose text plus structured metadata and scheduler statistics are symbolic. Native summary
        generation and all retained replay payload parts are opaque host responsibilities; a string callback alone
        does not classify the entire consumed artifact.
    faithfulness_tested:
      assessment: known
      basis: wired
      values:
      - 'no'
      records:
      - ABS-1
      note: No retained execution evidence in this frozen evidence set tests downstream dependence on recalled content.
        Exact-quote validation and faux-provider test source do not meet that requirement.
---

# SoL-Pi agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-24-sol-pi-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/sol-pi.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-24-sol-pi-01/memory-report.md`

**Memory analysis report SHA-256:** 5269409114aee630bed7f67434b1a6aef0410427f888602cc96c237949d1bf35

Run AAS-2026-09-24-sol-pi-01 opened 2026-09-24. Source-native system: SoL-Pi. The run state alone declares publication completion.

## Boundary and evidence

The intended use is to distinguish what the released efficiency extension actually controls from the enclosing coding agent and the historical auto-research process that produced it. Target class: extension or tool mechanism. Boundary kind: complete artifact, partial loop. Evidence tier: code-grounded, at `https://github.com/NVlabs/SoL-Pi` commit `1559b5cb12c72da4a485bc50fe326586b216fb19`, cutoff 2026-09-24.

Included: configuration and feature registration; fused file/shell tools; observation archiving and recall; diagnostic-log reduction; plan-driven native compaction and continuation. Excluded: Pi's implementation of its agent loop, tools, native summary production, session context construction, trust decisions, authentication and model transport; external providers and operating-system enforcement; the earlier auto-research harness and its experimental records. These exclusions prevent claims about complete deployed permissions, native compaction fidelity, exact model weights, or causal improvement of the historical research process. The optional paper capture was not used. Primary-source reads were commit-addressed; no prior SoL-Pi review or sibling result supplied evidence.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git repository | `https://github.com/NVlabs/SoL-Pi`; access root `/home/zby/llm/commonplace/related-systems/NVlabs--SoL-Pi` | `1559b5cb12c72da4a485bc50fe326586b216fb19` | implementation | `src/sol-pi/` configuration, four extension families and source-selected tests | full commit-relative paths and quotations on canonical records | host/provider code and deployed run traces excluded; wiring is not execution evidence |
| SRC-2 | same Git repository | `https://github.com/NVlabs/SoL-Pi` | `1559b5cb12c72da4a485bc50fe326586b216fb19` | doctrine/design; reported operation kept distinct | `README.md`, `docs/compatibility.md`, `SECURITY.md`, configuration documentation | claims and scope records | compatibility and auto-research origin are author reports, not inspected run or causal experiment capsules |

## Shared records

### Components

CMP-1 — SoL-Pi extension dispatcher and symbolic mechanisms. TypeScript registration, tool wrappers, event hooks, archives and policy calculations run inside Pi. The package does not own the enclosing agent turn loop or an isolation layer. Implementation conclusion status: wired. SRC-1 `src/sol-pi/index.ts`; `src/sol-pi/config.ts`. Current grant set/deployed isolation: uninspected; capability surface includes host filesystem writes, shell execution and a nested reducer model call when corresponding features are enabled. SRC-2 `SECURITY.md` explicitly states the process boundary.

> SoL-Pi is a Pi extension. It runs with the filesystem, process, network, and credential permissions of the Pi process that loads it. SoL-Pi is not a sandbox or permission boundary.
> --- `SECURITY.md` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

CMP-2 — Configured reducer model. Distributed-parametric component requested through Pi's registry. Default provider is `openai-codex`, model `gpt-5.6-luna`; configuration can replace both names. Endpoint resolution conclusion status: wired; exact immutable parameter identity and provider-side parameter updates conclusion statuses: uninspected. The inspected route performs completion, not an inspected training operation. A mutable model name and pinned package revision do not establish fixed weights. SRC-1 `src/sol-pi/extensions/evidence-preserving-reducer/config.ts`; `src/sol-pi/extensions/evidence-preserving-reducer/provider.ts`.

> export const DEFAULT_REDUCER_PROVIDER = ["openai", "codex"].join("-");
> export const DEFAULT_REDUCER_MODEL = ["gpt-5.6", "luna"].join("-");
> --- `src/sol-pi/extensions/evidence-preserving-reducer/config.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

> if (typeof registry.complete === "function") {
>     response = await registry.complete(model, requestContext, requestOptions);
> } else {
>     const auth = await registry.getApiKeyAndHeaders(model);
> --- `src/sol-pi/extensions/evidence-preserving-reducer/provider.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

CMP-3 — Pi main agent and native compaction services. Excluded host distributed-parametric components are reached through public extension hooks and `context.compact`; the extension reads model context-window metadata but does not pin their weights or inspect native summary generation. Call-boundary conclusion status: wired; internal formulation, exact model identity, parameter changes and summary fidelity conclusion statuses: uninspected. SRC-1 `src/sol-pi/extensions/online-context-compact/extension.ts`; SRC-2 `docs/compatibility.md`. Those gaps limit the memory comparison's aggregate knowledge of host-owned payloads.

### Operative objects

OBJ-1 — Effective `sol-pi.json` configuration. Authored symbolic JSON in a trusted project location or user directory; selected once when the extension initializes. Features default false. Provider/model route and a non-negative cache-write/read ratio shape enabled operations. Human/operator configuration provides operational authority; schema validation is not a test of suitability. Conclusion status: wired. SRC-1 `src/sol-pi/config.ts`; `src/sol-pi/index.ts`.

OBJ-2 — Fused edit/write request with optional `then_run`. Model-authored symbolic file mutation plus Bash command, received through a replacement public tool schema. Instructions describe the intended operation, while Pi's inherited definitions perform it. The command is not restricted to a test; documented examples include build, start/restart and install. Its target files and process side effects are task products, not necessarily retained memory. Conclusion status: wired. SRC-1 `src/sol-pi/extensions/action-fusion/index.ts`; `src/sol-pi/extensions/action-fusion/then-run.ts`.

OBJ-3 — Combined mutation/command observation. Imported execution output plus extension status marker, preserving successful mutation even when the subsequent command fails. Tool observations can contain truth-apt statements, but the extension does not validate arbitrary command semantics. This object feeds Pi and, if eligible, the reducer/observation routes. Form: mixed symbolic envelope and arbitrary text output; storage/later session retention belong partly to Pi. Conclusion status: wired. SRC-1 `src/sol-pi/extensions/action-fusion/then-run.ts`; `src/sol-pi/extensions/evidence-preserving-reducer/candidate.ts`.

OBJ-4 — Symbolic compaction economic model. Static formal assumptions relate estimated remaining requests and context savings to the incremental cache-write cost and carried debt. This is an operative formulated prediction/policy, not an empirical measurement of benefit. Formulation conclusion status: wired; operative-use conclusion status: wired; content-directed criticism conclusion status: uninspected; theory revision conclusion status: uninspected; changed scheduling as its inputs change conclusion status: wired; improved capacity attributable to criticism conclusion status: uninspected. Assumptions and constants are separately inspectable/editable in source, giving addressability at that code boundary. The running route updates counters and debt rather than rewriting the formula. Source rationale is partly explicit in variable names and equations; the model consumer executes these equations, not a retained historical explanation. SRC-1 `src/sol-pi/extensions/online-context-compact/economics.ts`; `src/sol-pi/extensions/online-context-compact/extension.ts`.

> const savingTokens = input.archiveTokens - input.memoTokens;
> const incrementalCacheCostRatio =
>     input.cacheWriteReadRatio === null ? null : Math.max(0, input.cacheWriteReadRatio - 1);
> const breakevenRequests =
>     savingTokens > 0 && incrementalCacheCostRatio !== null
>         ? (input.writeTokens * incrementalCacheCostRatio) / savingTokens
>         : null;
> --- `src/sol-pi/extensions/online-context-compact/economics.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

OBJ-5 — Observation archive and projection metadata

Implementation conclusion status: wired. Raw eligible successful pure-text tool results are joined into text and stored at `<sessionDir>/sol-pi/<sessionId>/observation-pack/objects/<observation-id>.txt`. IDs derive from tool name, tool-call identity and content hash. The object contains trace evidence; its hash, byte/line/token counts, send counts and placeholder are access metadata, not new factual knowledge. Live send counts use an in-memory map; the append-only ledger stores request/projection/recall events. The placeholder contains identity, metrics, recall instructions and at most 1,024 excerpt bytes split between first and last complete lines. It is reconstructed for projection, not written as a standalone durable derived memory. SRC-1 `src/sol-pi/extensions/observation-pack/observation.ts:12-28,67-116,123-196`; `src/sol-pi/extensions/observation-pack/index.ts:53-63,137-209`; `src/sol-pi/extensions/observation-pack/ledger.ts:15-19`.

> export const FULL_SENDS = 2;
> --- `src/sol-pi/extensions/observation-pack/observation.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

OBJ-6 — Content-addressed diagnostic archive

Implementation conclusion status: wired. Eligible bash logs, including command suffixes from fused write/edit calls, are archived as `<runtimeRoot>/evidence-preserving-reducer/objects/<first-two-hash-characters>/<sha256>.txt`. This is imported raw tool evidence, not a summary. An existing same-name object must match the exact bytes and hash. When a tool result points to a qualifying regular, non-symlink temporary `pi-bash-*.log` directly under the operating-system temporary directory, the reducer reads that fuller source; otherwise it uses inline output. The archived “raw” body can therefore still be the inline preview when the full-output path is unavailable or rejected. SRC-1 `src/sol-pi/extensions/evidence-preserving-reducer/archive.ts:20-52`; `src/sol-pi/extensions/evidence-preserving-reducer/candidate.ts:29-100`; `src/sol-pi/extensions/evidence-preserving-reducer/config.ts:59-68`.

> 		await writeFile(path, body, { encoding: "utf8", flag: "wx", mode: 0o600 });
> --- `src/sol-pi/extensions/evidence-preserving-reducer/archive.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

OBJ-7 — Verified diagnostic receipt

Implementation conclusion status: wired. The model proposes structured evidence; validation produces a receipt containing status, uncertainty, command/source hashes, source size/path, reducer identity/usage and quoted evidence with line numbers and quote hashes. The resulting text replaces the corresponding tool-result body and is retained/replayed through Pi's tool history contract. SoL-Pi does not separately write a receipt file. It preserves the fused mutation's other result blocks. The receipt is advisory diagnostic evidence; source identification and typed fields are symbolic metadata. Model output outside text blocks is discarded. SRC-1 `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts:146-176`; `src/sol-pi/extensions/evidence-preserving-reducer/index.ts:126-176`; `src/sol-pi/extensions/evidence-preserving-reducer/candidate.ts:64-97`; `src/sol-pi/extensions/evidence-preserving-reducer/provider.ts:55-56`.

> 		content: reducible.projectReceipt(receipt),
> --- `src/sol-pi/extensions/evidence-preserving-reducer/index.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

OBJ-8 — Online plan, progress and scheduling state

Implementation conclusion status: wired. Versioned custom session entries store plan steps, optional concise progress, request counts, boundary intervals, context growth, native compaction count and cache-debt estimates. The latest valid state on the current branch is restored into memory. Plan/progress strings are agent-authored natural language in a symbolic structure; counters and statuses are executable control inputs. The append-only previous entries preserve history while each new state supersedes the current state. Custom state is not injected into model context. `update_plan` separately returns its new plan snapshot as a tool result. SRC-1 `src/sol-pi/extensions/online-context-compact/state.ts:8-33,86-145,147-207`; `src/sol-pi/extensions/online-context-compact/extension.ts:178-244`; SRC-2 `SECURITY.md:16-18`.

> 	pi.appendEntry(ONLINE_STATE_ENTRY, state);
> --- `src/sol-pi/extensions/online-context-compact/state.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

OBJ-9 — Native compaction record and resumed context

Implementation conclusion status: wired at the host call boundary. SoL-Pi requests native compaction with preservation instructions, receives a callback exposing `compaction.summary`, and calls host `buildSessionContext(entries, leafId)` after the compaction event and on restoration. Pi owns the retained compaction entry and the message payload used for the next turn. The callback string and generic reminder do not reveal the complete retained/replayed payload or its derivation algorithm. The opaque host parts remain explicitly unclassified; no claim of a second SoL-Pi checkpoint format is made. SRC-1 `src/sol-pi/extensions/online-context-compact/extension.ts:130-148,178-185,346-398,418-431`; SRC-2 `docs/compatibility.md:42-48`; test interface contract SRC-1 `tests/online-context-compact-agent-session.test.ts:81-90,146-156`.

> 						customInstructions: BOUNDARY_COMPACTION_INSTRUCTIONS,
> --- `src/sol-pi/extensions/online-context-compact/extension.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

OBJ-10 — Diagnostic journal and projection ledger

Implementation conclusion status: wired. EPR appends non-context session entries with candidate, provider, rejection and applied-receipt metadata; ObservationPack appends timestamped JSONL events. These are raw operational traces and provenance records, not an implemented learner or model-retrieval store. No in-boundary later automatic reader for the journal/ledger was found. They are retained alongside the operative objects but do not independently establish trace learning. SRC-1 `src/sol-pi/extensions/evidence-preserving-reducer/journal.ts:8-23`; `src/sol-pi/extensions/evidence-preserving-reducer/index.ts:77-159`; `src/sol-pi/extensions/observation-pack/ledger.ts:8-19`.

### Routes

RTE-1 — Configuration admission and once-per-extension feature registration. Trigger: Pi `session_start`. Owner: symbolic extension initializer; principal: operator who supplied OBJ-1 under Pi's trust decision. Trusted project config wins over the global file; files are not merged. Missing config selects all-disabled defaults. Unknown keys, wrong version/types or negative/nonfinite ratio throw. After loading, feature flags register their tools/event handlers, with Online Context Compact last. Immediate return is registration; no learned output or automatic later read-back occurs on this route. Persistence is the authored config file, not a runtime memory update. Reconfiguration requires a fresh initialization; this route does not infer changed config from later outcomes. The host determines project trust and extension loading. SRC-1 `src/sol-pi/config.ts`; `src/sol-pi/index.ts`.

Implementation conclusion status: wired. Guarantee strength: invariant for local type/flag conditions, external contract for trust and lifecycle. Operator proposes/admits configuration, parser can veto invalid values, and disabling features requires replacing config and restarting the relevant lifecycle. Guidance is static settings, not a formulated tentative theory. Theory formulation/use/criticism and improved capacity are inapplicable to this symbolic configuration admission itself. No answer oracle is involved. Current enabled features in a real deployment are uninspected.

> actionFusion: false,
> observationPack: false,
> evidencePreservingReducer: false,
> --- `src/sol-pi/config.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

> pi.on("session_start", (_event, ctx) => {
>     if (initialized) return;
>     initialized = true;
>     registerConfiguredFeatures(pi, loadConfig(ctx));
> });
> --- `src/sol-pi/index.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

RTE-2 — Action Fusion execution and file-change guard. Trigger: enabled replacement edit/write call. The model proposes both the file mutation and optional subsequent command in OBJ-2. A canonical-path queue serializes this instance's fused operations for that file. The host mutation runs first; if it throws, the command is skipped. Without `then_run`, the mutation result returns directly. Otherwise the extension hashes the file, yields, hashes again, and skips on detected change. It delegates Bash execution to Pi and returns combined OBJ-3. A command failure reports failure while retaining the mutation; there is no transactional rollback of the edit. SRC-1 `src/sol-pi/extensions/action-fusion/index.ts`; `src/sol-pi/extensions/action-fusion/then-run.ts`; `src/sol-pi/extensions/action-fusion/file-queue.ts`.

Implementation conclusion status: wired; operation and effectiveness conclusion statuses: uninspected. Immediate return is the combined tool result; retained/later context is owned by Pi and the integrated observation mechanisms. There is no selected cross-task memory or delegated model call in fusion itself. Queue entries expire on completion. The canonical-path queue is not a global filesystem lock: external processes and other tool/extension paths can change files, and a change after the final hash is outside its observation interval. Queue ownership/enforcement point: SoL-Pi instance; strength: invariant for its queued operations, best effort interference detection for outsiders. Bash privileges, cancellation and tool permission behavior require Pi's contract; the current deployment was not inspected.

This route admits product/capability effects directly through requested file and shell actions. Model proposes command; host wrappers may reject invalid mutations or observed interference; no separate SoL-Pi human approval transition is wired. Arbitrary checks may use expected values supplied by the task or command, but no system-level answer oracle is established. Guidance consists of current task/model decisions; no theory criticism or automatic revision of the efficiency mechanism follows from command success.

> mutationResult = await mutate();
> --- `src/sol-pi/extensions/action-fusion/then-run.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

> const mutationHash = await fileSha256(path);
> await yieldForInterference();
> const commandHash = await fileSha256(path);
> if (mutationHash !== commandHash) {
>     throw new Error("target content changed after the fused mutation");
> }
> --- `src/sol-pi/extensions/action-fusion/then-run.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

> const bashResult = await bash.execute(`${toolCallId}:then_run`, thenRun, signal, undefined, ctx);
> --- `src/sol-pi/extensions/action-fusion/then-run.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

RTE-4 — Automatic observation archive and context projection

Implementation conclusion status: wired. Trigger: each `context` event. Producer/selector: ObservationPack scans already assembled messages, filters successful pure-text results larger than 10 KiB, excludes reducer receipts, ensures the raw object exists and uses send count to select full content or placeholder. Current in-memory count is preferred; the number of following assistant messages supplies a resume estimate. Delivery: rewritten outgoing context to the next provider request, without a request by that model for the selected archive content. This is coarse push by eligibility/age and fixed head/tail budgets; observation IDs on the placeholder do not make it an identifier-targeted push. The consumer is the frontier assistant. Archive failures inside the per-result projection block preserve that observation. The outer `runtimeRoot` resolution precedes that block; the report does not generalize this catch to every possible failure. SRC-1 `src/sol-pi/extensions/observation-pack/index.ts:137-209`; `src/sol-pi/extensions/observation-pack/observation.ts:67-116,158-196`.

>  * The mechanism never edits history in place. It rewrites only at the
>  * projection layer (`pi.on("context")`), so the stored session stays intact and
>  * recall keeps working after native compaction or a session resume.
> --- `src/sol-pi/extensions/observation-pack/index.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

RTE-5 — Exact observation pull

Implementation conclusion status: wired. The frontier assistant calls registered `obs_recall(id, offset)`. The tool reads OBJ-5 from the current session root, returns bounded text plus next offset and EOF, and logs the access. Output is capped at 16 KiB and 400 lines including headers. This is pull, not another push merely because the code returns requested text. There is no lexical/vector search or cross-session catalog. The ID grammar rejects path traversal; file opening refuses symlinks and requires a regular file. Recall itself does not recompute the entire content hash, so creation-time identity checking is not a continuing attestation against later external edits. SRC-1 `src/sol-pi/extensions/observation-pack/index.ts:41-49,65-115`; `src/sol-pi/extensions/observation-pack/observation.ts:20-22,94-96,213-251`.

> 			description: "Read a stored large tool result by observation id and byte offset.",
> --- `src/sol-pi/extensions/observation-pack/index.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

RTE-6 — Diagnostic reduction and retained evidence delivery

Implementation conclusion status: wired at the extension and host tool-history handoff. Trigger: eligible `tool_result`, including Action Fusion command output. Producer: configured reducer model automatically receives the archived diagnostic body, command hash and exit/error status. It selects exact quotations by judgment, constrained to at most 12 items of at most 600 characters. Validator accepts a smaller receipt or leaves the original result unchanged. Persistence: OBJ-6 raw file; OBJ-7 replacement tool result through the host history contract. Later consumer: frontier assistant seeing the receipt in current and later context, with manual exact readback afforded by RTE-7. The automatic selection supplies evidence the assistant did not request from a retained archive; it is inferred-judgment push in this extraction step, separate from opaque host history selection on later replay. SRC-1 `src/sol-pi/extensions/evidence-preserving-reducer/index.ts:58-176,179-195`; `src/sol-pi/extensions/evidence-preserving-reducer/config.ts:14-29`; `src/sol-pi/extensions/evidence-preserving-reducer/provider.ts:105-158`.

This is a qualifying trace-fed derived-memory route: automatic extraction, retained receipt and later assistant context. The local source proves replacement and the host call contract, not host persistence internals or observed downstream use. It neither proposes repairs nor retains a reason for a prescribed action; its quote evidence can support the later assistant's diagnosis without being a retained explanatory theory.

> 			!body.includes(quote)
> --- `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

Admission detail: the reducer prompt asks for exact evidence and forbids diagnosis, repair suggestions or invented commands. This is static procedural guidance; selected text and metadata persist, not a repair theory or its criticism. The model proposes excerpts; symbolic receipt validation can veto them. Source hash, status equality, boolean uncertainty, label membership, length/count and exact quote occurrence are checked. A failing body with a failure-signal match needs an item labeled fatal/failure; label semantics and exhaustive coverage are not proved. This archive is an occurrence reference, not an answer oracle for the task. Receipt-local duplicate elimination is not cross-memory curation. SRC-1 `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts:37-143`. Model-internal theory formulation/criticism and attributable capacity improvement remain uninspected.

RTE-7 — Diagnostic archive readback

Implementation conclusion status: afforded. The receipt directs the frontier assistant to call bash with an explicit byte or line range on its source path. That names both consumer and supported interface; it is more than an unused file-storage API. SoL-Pi supplies no dedicated EPR recall tool, automatic source expansion, or fixed output budget for this bash route. Whether a particular agent follows the receipt is not established. SRC-1 `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts:172-175`.

> 		"readback=use bash with an explicit byte or line range on source_artifact when exact context is needed",
> --- `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

RTE-8 — Plan replacement, restoration and withdrawal

Implementation conclusion status: wired. The agent calls `update_plan` with a complete plan and optional progress. The extension validates it, compares previous step IDs/statuses, records newly completed boundaries, appends OBJ-8 and returns the plan snapshot. Up to 128 steps are allowed. At session start/tree navigation or lazy initialization, the extension scans the active branch backwards for the latest valid state of the right version/type; the restored state is delivered to the scheduler, not the model. This automatic state supply is coarse latest-valid selection inside a host-selected branch; `customType` is a format discriminator, not proof of targeted identifier retrieval. `CORRECTION:` input or steering appends a reset state; compaction clears current plan/progress. These are current-state invalidations with earlier history retained. SRC-1 `src/sol-pi/extensions/online-context-compact/extension.ts:77-87,178-234,247-257,418-431`; `src/sol-pi/extensions/online-context-compact/state.ts:133-145,161-207`; `src/sol-pi/extensions/online-context-compact/plan.ts:21-78`; `src/sol-pi/extensions/online-context-compact/tools.ts:48-75`.

> 		if (state) return state;
> --- `src/sol-pi/extensions/online-context-compact/state.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

Progress fields may retain decisions and verification, but only the first newly completed step receives the submitted progress summary. No route reads `pendingProgress` as a task-specific prompt or feeds it into the native compaction instructions. Its strings are parsed during restoration and then retained/cleared; the scheduler uses plan status and statistics. Therefore retained decision wording is not evidence that later reasoning reads its rationale. The agent can of course have progress wording in its ordinary tool-call history, whose host compaction is outside this state-specific route.

Admission roles: the agent proposes the complete plan and any progress text; the parser can veto malformed shapes, while goal/status advice is not a truth evaluator. The returned plan guides work; its status and statistics guide the scheduler. Reset/replacement supersedes current state rather than erasing historical entries. No answer oracle checks completion. Progress rationale can be retained, but this state route does not deliver it to a later reasoning consumer. Content-directed theory criticism or improved capacity is uninspected.

RTE-9 — Native compaction and automatic parent-task continuation

Implementation conclusion status: wired at the host call boundary. Newly completed plan steps create a pending boundary. `turn_end` requires the matching successful tool result and a non-aborted/non-error assistant turn. Estimated context size, remaining plan boundaries, past request intervals, growth, debt and configured cache ratio decide whether compaction is worth requesting or needed for window pressure; a host cut-point feasibility check must also pass. On selection, the extension aborts the active run, waits for `agent_settled`, calls `context.compact`, waits for completion/error, then on success sends the generic reminder with `triggerTurn: true`. The next assistant turn consumes the compacted host context. A settlement barrier waits for this continuation. SRC-1 `src/sol-pi/extensions/online-context-compact/extension.ts:260-431`; `src/sol-pi/extensions/online-context-compact/economics.ts:122-237`; SRC-2 `docs/compatibility.md:44-50`.

> 							{ triggerTurn: true },
> --- `src/sol-pi/extensions/online-context-compact/extension.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

Persistence and reuse are supplied by the Pi session compaction contract; the generic reminder is separately persisted as a hidden custom message. This trace-fed summary/continuation route qualifies at the wired boundary even though the host summary-generation algorithm is excluded. It is online and explicitly continues the active parent task. Selection of retained summary/tail messages is host-owned: the extension passes all entries plus leaf ID to `buildSessionContext`, and consumes the returned messages for its estimates, but does not implement or reveal complete payload assembly. No additional SoL-Pi memo/checkpoint alternative exists in the inspected persistence routes. Rationale preservation is requested only at the level of “important decisions,” without requiring reasons or showing a later diagnostic rationale reader.

> 	"Online context compaction finished. The parent task is still active. " +
> 	"Before continuing work, call update_plan with a fresh plan for the remaining work.";
> --- `src/sol-pi/extensions/online-context-compact/extension.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

Admission roles: the model signals plan completion; code applies OBJ-4 and native-feasibility conditions; host cancellation/error can veto continuation. Static preservation instructions guide the excluded summarizer. Native summary content, formulation, criticism and accepted truth are uninspected. The extension consumes callback success for operational continuation, not epistemic acceptance. On successful compaction it clears the old plan/progress and prompts reconstruction; on error or cancellation it does not arm that continuation. Guarantee strength is protocol at the Pi interface, requiring compatible events and settlement semantics; no actual continued run was observed.

RTE-10 — Persisted trace statistics change later compaction decisions

Implementation conclusion status: wired. `before_provider_request` derives request count, positive token-growth aggregates and debt repayment from observed context; boundary completion derives request intervals. Every update appends OBJ-8. Later restored/current statistics feed `decideCompaction` to estimate the remaining request horizon and choose compaction. This is a second use of session state beyond plan storage: automatic event-trace reduction produces durable symbolic behavior-shaping material consumed by later scheduling. It qualifies under the commissioned trace-learning criterion even without model-weight learning or novel claims. It shares the online timing of RTE-6 and RTE-9. Task horizon remains unknown because statistics are tied to session state, some fields survive compaction, and no ordinary new-task reset is implemented. SRC-1 `src/sol-pi/extensions/online-context-compact/extension.ts:195-199,241-244,285-303`; `src/sol-pi/extensions/online-context-compact/state.ts:147-207`; `src/sol-pi/extensions/online-context-compact/economics.ts:70-119,149-196`.

> 				completedBoundaryRequestCounts: state.completedBoundaryRequestCounts,
> --- `src/sol-pi/extensions/online-context-compact/extension.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

Policy guidance is OBJ-4: derived counters update its inputs, and the resulting scheduling decision does not itself criticize or revise the formula. Formulation and operative use of that authored formal model are wired; criticism, formula revision and improved capacity attributable to criticism are uninspected. Measured token/request data are inputs, not an independent answer oracle for whether compaction will preserve task quality.

### Claims

CLM-1 — The release packages four reusable efficiency mechanisms discovered through scaled auto-research loops. Conclusion status: claimed for historical origin; implementation of the four exported mechanisms is wired in this result. The source boundary is the released extension, not the earlier research loop. SRC-2 `README.md`.

> SoL-Pi is a standalone extension for Pi that packages four reusable efficiency mechanisms discovered through scaled auto-research loops.
> --- `README.md` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

CLM-2 — Evidence preservation means original observations remain locally available and the reducer checks retained quotations. Conclusion status: claimed at the source-description layer, with bounded implementation support on the integrated archive/reducer records. Quote occurrence establishes provenance of selected text, not semantic completeness or correct diagnostic labeling. SRC-2 `README.md`; SRC-1 `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`.

> "Do not diagnose a fix, recommend an edit, invent a command, or claim that an omitted failure is absent.",
> --- `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

CLM-3 — Compatibility checks and efficiency objectives. SRC-2 `docs/compatibility.md` reports the then-current test suite and integration checks on Pi 0.85.1/0.84.2, and explicitly distinguishes deterministic faux-provider integration from live authentication/token savings. Conclusion status: claimed; no execution capsule from this analysis supports an observed or causal efficiency claim. The configured economic model is a decision heuristic, not measured savings at this deployment.

> These integration tests use Pi's deterministic faux provider; they verify runtime compatibility, not live provider authentication or token savings.
> --- `docs/compatibility.md` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

### Evidenced absences

ABS-1 — No retained test of downstream dependence on recalled content

Conclusion status: absent, within the frozen supplied repository evidence and the inspected test/documentation boundary. Test source specifies quote rejection, exact-byte recall and deterministic compaction/continuation compatibility. It is not retained execution evidence demonstrating that recalled information changed an agent's answer or action. In particular the integration test supplies a deterministic summary itself. This prevents a `faithfulness_tested: yes` classification and any observed benefit claim. SRC-1 `tests/online-context-compact-agent-session.test.ts:81-90,135-161`; SRC-2 `docs/compatibility.md:67-69`; evidence-check implementation SRC-1 `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts:94-143`.

> 						summary: `deterministic compacted history ${"s".repeat(6_000)}`,
> --- `tests/online-context-compact-agent-session.test.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

Recorded search boundary: SRC-1/SRC-2, commit `1559b5cb12c72da4a485bc50fe326586b216fb19`; enumerated `tests/`, `docs/` and `README.md` with commit-addressed `ls-tree`, then searched those roots with case-insensitive extended query `faithful|recall|faux|deterministic|accuracy|benchmark|ablation|token savings`. Hits led to the exact-recall tests, deterministic-provider integration and compatibility text cited here. This is an absence of retained downstream-dependence evidence in that supplied test/documentation set, not a claim about unpublished evaluations.

### Behavioral-authority paths

BAP-1 — Consumer extension dispatcher; channel OBJ-1 configuration plus Pi project-trust flag; force routing/enablement; horizon one initialized extension lifecycle. SRC-1 `src/sol-pi/index.ts`; `src/sol-pi/config.ts`. Conclusion status: wired. Configuration changes available operations without establishing knowledge about their efficacy.

BAP-2 — Consumer Pi edit/write/Bash executors; channel OBJ-2 tool call; force operational execution under host grants; horizon one fused call. SRC-1 `src/sol-pi/extensions/action-fusion/index.ts`; `src/sol-pi/extensions/action-fusion/then-run.ts`. Conclusion status: wired. Reported command success does not warrant task correctness.

BAP-3 — Evidence has advisory force; integrity gates are narrower

Consumer: reducer validator and frontier assistant; channel: archived bytes and replacement/recall tool results; force: validation and advisory evidence respectively; horizon: candidate admission and later turns while retained. Implementation conclusion status: wired. Raw archives validate object reuse and EPR quote occurrence. The receipt explicitly leaves diagnosis, repair, rerun and adjudication to the frontier agent. The reducer receives a prompt to treat logs as untrusted data; heuristic likely-secret rejection gates eligible input before the model call. Those are prompt and regex measures, not proof that all hostile instructions or secrets are removed. Quote hashes identify content; they do not establish source truth or relevance. The archive is writable by the local user and is not a signed revision chain. SRC-1 `src/sol-pi/extensions/evidence-preserving-reducer/index.ts:64-77`; `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts:37-50,94-143,172-175`; `src/sol-pi/extensions/evidence-preserving-reducer/archive.ts:32-44`.

> 		"authority=Sol retains diagnosis, repair, rerun, and pass/fail adjudication",
> --- `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts` @ `1559b5cb12c72da4a485bc50fe326586b216fb19`

BAP-4 — Plan content and scheduling control have different consumers

Consumer: frontier assistant and compaction scheduler; channel: returned plan, restored custom state and native context; force: task instruction and scheduling; horizon: current plan and session statistics. Implementation conclusion status: wired. Model-authored goals return as the working plan, while persisted plan status and measured statistics govern automatic compaction routing. There is no validation that declared completed steps actually succeeded or that submitted verification strings describe real checks. Transition advice detects ID reuse with a changed goal and advises at most one step in progress, but does not enforce a semantic plan proof. Native preservation instructions and the reminder are static extension instructions; their insertion does not by itself establish learned instruction content. SRC-1 `src/sol-pi/extensions/online-context-compact/plan.ts:36-78`; `src/sol-pi/extensions/online-context-compact/extension.ts:202-228,260-311`.

## Runtime account

Ordinary enabled invocation starts when Pi loads the extension and signals session start. RTE-1 selects one valid configuration and installs only enabled features. Pi still owns the user request, agent identity, main model, turn scheduling and permission envelope. When the main agent edits/writes with `then_run`, RTE-2 removes a model decision between mutation and shell execution. The resulting observation can enter two distinct context routes: eligible diagnostic output may be replaced with a checked reducer receipt, while ObservationPack can replace repeated large tool-result text in the model-facing context with local recall handles. Those transforms preserve different things and use different evidence contracts.

With Online Context Compact enabled, model-authored `update_plan` calls identify newly completed steps. A valid tool result and nonaborted turn can become a compaction candidate. The symbolic economic/window policy considers request history, remaining steps, estimated replay savings, cache ratio and native feasibility. On selection it aborts the active run, waits for settlement, calls native compaction, and triggers a hidden generic continuation only after the success callback. Pi's host summary and actual continued execution remain outside this source boundary. State and role ownership are retained in the specialist's canonical records.

Operating mode is a host coding session processing open user tasks. Efficiency actions are triggered by tool outputs, plan boundaries and context/request counters, not a benchmark curriculum or supplied gold answer. Human contribution: choose enabled mechanisms, model route and ratio, and control the host session. Model contribution: choose tasks/actions/plan statuses and reducer excerpt selection. Symbolic code decides eligibility, receipt admission and compaction economics; the host executes and may cancel. No production-harness rewrite or successor search is inferred from the historical auto-research description. Mechanism configuration and output selection are distinct from self-improving the mechanism.

Material alternatives: missing/default config yields no mechanism; untrusted project config falls through to user config; plain edit/write omits the fused command; reducer may accept a plain Bash log or fused-command suffix and preserve other blocks; reducer completion uses modern registry completion or a legacy authentication-plus-compat API; native compaction is host-owned; later third-party context transforms can change what Pi sends beyond the extension's growth estimate. None of these routes is a new sandbox.

Four static forcing cases bound the guarantees:

1. Mutation fails or content changes between hash reads: fused command is skipped. Command failure after a successful mutation leaves that mutation in place. RTE-2.
2. Reducer proposes a nonexistent quotation, wrong source identity or mismatched status: the local validator rejects replacement. Valid quote membership alone does not prove that all important failures were selected or that a `failure` label is semantically appropriate. Integrated reducer route.
3. Reducer model is missing, times out or returns an invalid/oversized receipt: handled cases return no replacement. Archive creation/integrity exceptions occur outside that model-call catch; whether Pi preserves the original observation on such a hook error is uninspected. No unconditional extension-only fallback guarantee is asserted.
4. Native compaction is selected, cancelled or followed by tree navigation: the extension waits for settlement/callbacks, blocks tree navigation while compacting, and arms continuation only on success. Absence of the required Pi events, a changed host contract, or later asynchronous third-party handlers limits the continuation guarantee.

No dynamic check planned. Considered pure-policy tests, mocked Pi integration and live-provider runs. Static inspection directly supports the deterministic rejection and dispatch claims; mock execution would not establish real provider behavior, compaction fidelity or token savings. No live Pi runtime/dependencies/credentials were provisioned, and no command attempt is misreported as an executed test.

## Lens scoping

### Memory/context scope

Full lens commissioned against SRC-1 and SRC-2. Trigger: archived observations, reducer receipts, exact recall and host-native compaction/continuation. Include accumulated session objects and their write, projection, recall and maintenance routes; exclude static config/instructions and opaque host/provider internals except their named interfaces. A complete artifact/partial-loop scope prevents importing the host's memory guarantees.

### Epistemic scope

Full lens under `kb/instructions/analyse-external-system-epistemic-architecture.md`, applied locally as a sparse overlay. Trigger: CLM-2 evidence preservation and model-selected diagnostic receipts; plan completion and economic decisions have consequential operational force. Assess imported tool outputs, selection/format transformations, receipt validation, context retention and admission. Do not infer that a log summarizer produces warranted diagnosis, that a plan status verifies work, or that an economic estimate measures causal benefit. Historical auto-research and actual instances are outside the inspected evidence.

## Lens outputs

### Memory/context lens

The specialist inventoried OBJ-5, OBJ-6, OBJ-7, OBJ-8, OBJ-9 and OBJ-10 through RTE-4, RTE-5, RTE-6, RTE-7, RTE-8, RTE-9 and RTE-10. Its findings below annotate those canonical records.

#### Write side

Acquisition is automatic after human feature adoption. ObservationPack writes a raw copy of eligible retained tool history; EPR writes its raw log before asking the reducer model for selected evidence. The former's repeated context placeholder is not durably stored as a derived artifact, so it alone does not establish trace learning. The latter's returned receipt becomes the shorter tool-history artifact at the host handoff and does qualify. Both plain bash and fused write/edit command-result variants are included in RTE-6; fused result reconstruction preserves the mutation's other output.

EPR requires at least 4,096 source bytes, rejects more than 600,000 characters and likely-secret matches, limits model output to 2,048 tokens or the model's smaller limit, and uses a 90-second operation timeout. It rejects provider failures, invalid schema/hash/status/quotes and receipts no smaller than the source. These fallbacks return the unmodified tool result through the hook. Archive writing occurs before the model-call `try`; an archive integrity/I/O exception is not caught by that fallback. Whole-runtime recovery then depends on excluded Pi behavior. SRC-1 `src/sol-pi/extensions/evidence-preserving-reducer/config.ts:14-29,59-68`; `src/sol-pi/extensions/evidence-preserving-reducer/index.ts:64-147`; `src/sol-pi/extensions/evidence-preserving-reducer/provider.ts:74-91,115-149`.

Online plan updates are automatic agent authorship rather than automatic extraction of an entire dialogue. Completion progress can summarize preceding work, but its state record lacks a later model-reading route of its own. In contrast, RTE-10's retained trace statistics demonstrably feed later scheduler code. RTE-9 delegates history condensation to Pi and reuses the compacted result through automatic continuation. These three qualifying routes—RTE-6, RTE-9 and RTE-10—are all included in the learning axes. None warrants an assertion of learned weights or improved capacity.

Maintenance is narrow. Raw archives have integrity-checked reuse, not near-duplicate merging. Receipts eliminate duplicate kind/quote pairs inside one newly produced receipt; this is not curation across retained memories. ObservationPack context replacement leaves stored history unchanged. Native compaction and EPR consolidate supplied evidence; plan updates and statistics evolve current state; corrections/compaction invalidate current plan/progress while the session log preserves earlier entries. No automatic raw-archive deletion route was found, consistent with SRC-2 `README.md:114-124`. An operator can remove local files or sessions, but that filesystem possibility is not a shipped editing/adoption interface for individual memories.

Rationale is distinct from evidence and numerical provenance. Receipts preserve selected evidence and source identifiers, not reasons for prescribed repairs. Plan progress permits decision strings but neither requires causal reasons nor routes those state strings to a later model consumer. Compaction asks Pi to preserve decisions, verification and remaining work but does not test rationale preservation. Scheduler counters contain sufficient numerical inputs for decisions; the code applies a shipped economic policy rather than retaining a model-authored explanation to criticize later. This boundary supports adaptation of context and scheduling, not a demonstrated cycle of content-directed criticism and improved capacity.

#### Read-back

RTE-5 and RTE-7 are requested archive reads: respectively a wired purpose-built observation tool and an afforded explicit bash-range instruction to the frontier agent. Their identifiers and paths are pull selectors. Neither establishes identifier-based push.

RTE-4 automatically supplies full or excerpted retained observations to the next provider call according to size/type/send age, with fixed excerpt budgets. RTE-6 automatically selects archived diagnostic evidence by model judgment and returns a receipt at the tool-history handoff. Later receipt replay uses Pi's context assembly. RTE-8 automatically supplies the latest valid state from the current branch to extension code. RTE-10 reuses that state to choose whether to request compaction. RTE-9 automatically triggers an assistant turn after the host has compacted history; Pi selects and supplies the retained summary/tail. The extension's leaf-ID argument identifies the host assembly boundary but does not prove the internal matching/selection operation.

The compaction scheduler assumes a default retained tail of 20,000 tokens and estimates the native memo as 1,000 tokens. These are economic-estimate inputs, not extension-enforced actual summary or retained-tail budgets. A programmatic factory can receive a matching non-default tail; normal configuration does not read the host's actual active value. Window pressure can override the economic gate when there is positive estimated compression. A later third-party context transformer is outside the extension's growth estimate. SRC-1 `src/sol-pi/extensions/online-context-compact/extension.ts:35-36,53-58,276-308`; `src/sol-pi/extensions/online-context-compact/economics.ts:170-196`; SRC-2 `docs/compatibility.md:40-42`.

All routes establish delivery or affordance, not causal influence on a particular answer. Exact recall remains available while its session archive exists; it is not automatic recovery of every omitted fact. Automatic continuation is explicitly wired only after successful boundary compaction, not after cancellation or exit. Test source checks fake-provider control flow and completion; it does not demonstrate diagnostic accuracy or savings in a live run.

#### Comparison rationale

The fourteen axes cover the same scope. File storage includes extension archives and source-visible host session-log persistence; in-memory storage includes live send counts, state and projected messages. Static configuration and ordinary project edits are outside memory scope, so they do not add manual authorship or repository storage. Raw imported traces, agent-authored plans, mechanically compiled state/projection data and extracted evidence/compaction explain the lineage union.

Unknown aggregate forms are deliberate. Visible content establishes natural-language and symbolic parts, but the commissioned boundary includes native compaction and replay while excluding the producer's internals. A callback `summary` string, a readable result, or a JSON container cannot certify the complete consumed payload. The same limitation applies to the distilled-form union across every qualifying route. It does not erase the visible symbolic scheduler state or receipt representation.

Read-back direction has an afforded union because the generic EPR archive read is only afforded; the dedicated observation tool and automatic projections are wired. Push selection has visible coarse and inferred-judgment cases, but unknown host replay selection prevents a complete known union. The report deliberately does not infer `identifier` from observation IDs, type tags, or an opaque `buildSessionContext` leaf argument.

The positive trace-learning classification includes extraction and compaction even when they create no novel claim. It also includes retained event-derived scheduling statistics because later compaction behavior depends on them. The absence of a task horizon for EPR and persisted scheduler history prevents aggregating their session-scoped reuse as solely per-task. The native continuation has an explicit active parent-task scope; that alone cannot resolve the union. All qualifying routes occur online. No retained faithful-recall dependency experiment was supplied, so faithfulness is “no” within this evidence boundary, not a global claim that none exists elsewhere.

#### Route return and horizon audit

All route evidence is static wiring except the afforded RTE-7. Activation in a particular model answer remains uninspected. The executor/selector, context and immediate return are specified on each canonical record; these residual dispositions prevent treating delivery as effective use.

| route | immediate return and later consumer | delegated visibility | invalidation, expiry and limits |
|---|---|---|---|
| RTE-4 | full text or handle to provider; later assistant may recall | existing assembled text only, no nested model call | projection changes by send age; raw object lasts with session archive; outer path failures host-owned |
| RTE-5 | bounded bytes to requesting assistant | current-session selected archive slice | missing/deleted file prevents recall; no total-hash recheck on each read |
| RTE-6 | receipt or unchanged result; host later replays receipt | reducer sees selected raw diagnostic body and metadata, not full task | replacement rejected by shape/source/size checks; archive failure outside model fallback; host retention owns expiry |
| RTE-7 | requested bash range, if assistant invokes it | host Bash can read the named archive under its grants | no dedicated output limit or universal automatic recovery; file lifetime bounds availability |
| RTE-8 | plan snapshot to model; latest valid state to scheduler | custom state is not model context | corrections/steering reset state; compaction clears plan/progress; earlier entries persist |
| RTE-9 | host compaction callback then triggered turn on success | excluded native summarizer sees host-selected history | cancellation/error does not resume; estimates do not enforce actual tail/summary sizes |
| RTE-10 | updated persisted counts/debt; later scheduler reads them | numerical state to symbolic policy, not a model | fields may survive compaction, preventing a known task horizon; updates do not revise OBJ-4 |

### Epistemic lens

#### 1. Source-and-claim boundary

See SRC-1 and SRC-2, CLM-1, CLM-2 and CLM-3 and the declared extension boundary. The question is what content the extension imports, selects, checks and licenses for later reliance. Main-agent diagnosis, task solving, answer oracles and native summary internals remain unassessed. Evidence-layer statuses remain implementation or source claims, not observed run outcomes.

#### 2. Epistemic-object overlay

OBJ-1 is normative configuration; OBJ-2 is a requested action; OBJ-3 imports tool output and status; OBJ-4 is a formal economic prediction used for scheduling. The memory records distinguish exact archived bodies from receipt fields, observation handles and plan/economic state. Those parts have different truth conditions: byte provenance, model selection of relevance, a model's claim of task completion, and a calculated prediction of compaction value cannot share one evaluator.

#### 3. Authority-route ledger

| route/function | architectural status | target/content relation | check or evaluator | epistemic license | operational authority and limits |
|---|---|---|---|---|---|
| RTE-1: operational admission/selection/consumption | implemented | OBJ-1; no content change | config schema and host trust signal at initialization | valid settings shape, not effective policy | BAP-1 enables tools/hooks; host trust implementation excluded |
| RTE-2: content transformation | implemented | OBJ-2/OBJ-3; non-truth-apt policy/content update to task files plus acquisition/import of output | host mutation and shell executor | returned process evidence, not task correctness | BAP-2 executes effects, retains mutation on command failure |
| RTE-2: check/evidence production | implemented | target file; no content change | adjacent hash reads around a yield | equality at sampled times | skip on observed interference; no global lock |

| RTE-4: content transformation | implemented | OBJ-5; non-ampliative reshaping of selected text | size/type/send-age predicate on each context event | source excerpt with recoverable identity; completeness not licensed | BAP-3 supplies a projection, not an accepted diagnosis |
| RTE-4: retention | implemented | OBJ-5 raw acquisition/import; operational metadata derivation | archive creation/reuse | original stored bytes, with local lifetime limits | local evidence available to RTE-5 |
| RTE-5: operational admission/selection/consumption | implemented | OBJ-5; no content change | requested ID/offset plus path/type checks | returned slice only; source truth untested | BAP-3 supplies requested observation bytes |
| RTE-6: content transformation | implemented | OBJ-7 selected quotes: non-ampliative reshaping; hashes/positions: entailed derivation; semantic labels: indeterminate | reducer proposes against OBJ-6 body | exact occurrence only after the following check; relevance/completeness unresolved | model proposal has no replacement force until admission |
| RTE-6: check/evidence production | implemented | OBJ-7; no content change | schema, hash, status, quote membership and size domain | source occurrence and declared shape, not diagnosis | symbolic check result controls subsequent admission |
| RTE-6: disposition/acceptance | implemented | OBJ-7; no content change | validator pass on eligible output | limited acceptance for replacing a diagnostic display; no epistemic acceptance of labels/repair | BAP-3 permits shorter tool-result replacement or retains original |
| RTE-6: retention | implemented | OBJ-6 raw import and OBJ-7 checked selection | archive write and host history handoff | provenance retained, upstream truth unknown | later host replay/readback; no lifecycle integration inferred |
| RTE-7: operational admission/selection/consumption | doctrine only | OBJ-6; no content change | source receipt names bash-range reader | original slice if requested; no accuracy license | BAP-3 affords caller-selected read; actual call unobserved |
| RTE-8: check/evidence production | implemented | OBJ-8 plan/progress; no content change | shape/version/ID/status parser | valid plan structure, not task completion | check can veto malformed update |
| RTE-8: disposition/acceptance | implemented | OBJ-8; non-truth-apt working-plan update | schema-valid full replacement | admission for scheduling use, not truth of completed work | BAP-4 changes plan and may create a compaction boundary |
| RTE-8: retention | implemented | OBJ-8; non-truth-apt state replacement plus stored progress assertions | append and latest-valid restore | lineage only; rationale strings untested | scheduler consumes status/counters; no later rationale reader established |
| RTE-8: lineage/freshness/recovery | implemented | OBJ-8; no new truth-apt content | correction, steering, compaction and active branch | latest valid state applicability only | reset/restore current state; historical entries remain |
| RTE-9: operational admission/selection/consumption | implemented | OBJ-4 and OBJ-8; no content change | economic/window policy, boundary, feasibility, nonabort conditions | predicted cost preference under explicit estimates | BAP-4 selects host compaction; no proved preservation |
| RTE-9: content transformation | not determinable | OBJ-9; truth-apt transformation indeterminate | native summarizer excluded | preservation, entailment or ampliation cannot be classified | source-visible host call only; internals unassessed |
| RTE-9: retention | implemented | OBJ-9; no additional content change at extension boundary | host compaction callback/history contract | persistence contract, not acceptance of summary claims | retained context consumed by next turn |
| RTE-9: operational admission/selection/consumption | implemented | OBJ-9; no content change | callback success, then triggerTurn | no epistemic license added | BAP-4 resumes parent task; error/cancel vetoes |
| RTE-10: content transformation | implemented | OBJ-8 statistics; entailed derivation within token/count arithmetic | request/context/boundary events | derived counts/estimates from supplied values; future predictions untested | state feeds later policy |
| RTE-10: retention | implemented | OBJ-8; no additional content change | custom state append | lineage only | later scheduler receives accumulated statistics |
| RTE-10: behavior/policy adaptation | implemented | OBJ-4 applied to OBJ-8; non-truth-apt scheduling adaptation | fixed economic formula with changed statistics | no empirical license that predicted savings occur | BAP-4 changes compaction selection without revising formula |

Ledger fields inherit their precise source anchors, activation predicates and horizons from the named canonical records. CLM-2 applies to evidence preservation on RTE-4, RTE-5, RTE-6 and RTE-7; CLM-3 applies to RTE-9 and RTE-10. The mismatch is the same bounded one: local integrity or continuation cannot license semantic completeness or measured savings. Other ledger rows make no broader warrant claim. No observed candidate state is implied by any implemented row. RTE-7 is an explicit source-side readback instruction with an afforded tool interface; excluded host Bash implementation prevents assigning this epistemic overlay an inspected implementation status.

#### 4. Per-object lifecycle disposition

No lifecycle record for OBJ-1: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-1. No lifecycle record for OBJ-2: no identified truth-apt candidate in this command request; relevant direct-adaptation or update routes: RTE-2. OBJ-3 is acquisition/import of task output; discovery lifecycle is not applicable to the import itself, and upstream truth is uninspected.

Retained quotations are non-ampliative selections from a log; hash/status derivations have a finite symbolic warrant. Diagnostic labels and uncertainty flags are model-produced and have only membership/type checks, so semantic adequacy is uninspected. Plan progress can contain claims about verification or decisions, but retaining them and using `completed` as a boundary does not verify the claim. Native summary transformation is indeterminate from this extension boundary. OBJ-4 is an authored formal conjecture about future request cost, with implemented derivation and operational use but no inspected empirical test/criticism or epistemic acceptance transition. Its source artifact exists, so observed candidate state for its historical production/testing/acceptance is not determinable; the source alone supplies no lifecycle trace. No instance-linked generated ampliative theory, test, acceptance or post-acceptance integration is established. Observed candidate state: no instance observed for model-generated receipt/plan/summary instances in the analysis evidence; source tests are not such observations.

OBJ-5 and OBJ-6: acquisition/import and non-ampliative projection through RTE-4, RTE-5, RTE-6 and RTE-7; discovery lifecycle not applicable. Their warrant is stored-byte identity, not source truth. OBJ-7: quotes are non-ampliative reshaping and metadata entailed derivation through RTE-6; semantic labels/uncertainty remain indeterminate between correct restatement and model-added interpretation. Shape/occurrence checks and operational admission are implemented; no generated instance is observed. A retained receipt plus task-context evaluation would be needed to settle semantic adequacy.

OBJ-8: numerical statistics derive within RTE-10's arithmetic domain; discovery lifecycle not applicable to those counts. Plan goals are non-truth-apt instructions. Progress/verification assertions are indeterminate from this boundary; RTE-8 retains them and checks structure, while task truth and upstream reasoning are uninspected. No model-generated instance is observed. OBJ-9: native compaction is indeterminate between preservation, derivation and ampliative addition; RTE-9 preserves host lineage and uses callback success, but a pinned producer and instance-linked original/summary comparison are needed to classify its content. No generated instance is observed. OBJ-10: acquisition of operational events and metadata derivation, discovery lifecycle not applicable; no in-boundary later truth-evaluating consumer is established.

OBJ-4 lifecycle (authored formal economic conjecture): observation/anomaly, initial conjecture production, empirical test, evidence-consuming acceptance and historical integration have architectural status not determinable and observed candidate state not determinable because the released formula is available without its research history. Derived consequence calculation and operational scheduling have architectural status implemented; observed candidate state not determinable because no execution of that candidate is retained here. Acceptance criterion/intended historical research comparison and accepted empirical scope are uninspected. Current operational use is the named compaction policy; it must not be relabeled post-acceptance epistemic integration. This disposes the available formulated theory separately from unavailable model-generated instances.

#### 5. System-claim versus route comparison

| claim | doctrine/design and implemented routes | observed/causal evidence | conclusion |
|---|---|---|---|
| CLM-1 | four feature registrations and their routes are implemented | historical discovery process only reported; no experiment capsule | release characterization supported; do not assign it the external research loop |
| CLM-2 | archives, hashes, quote-occurrence checks and recall are implemented | no actual retained receipt/run or faithfulness intervention inspected | checked source occurrence, not complete semantic preservation |
| CLM-3 | economic calculation and compatibility call surfaces implemented | reported faux-provider checks, no live savings comparison | code supports an efficiency policy, not measured improvement at this pin |

#### 6. Bounded conclusion

SoL-Pi's strongest epistemic contribution is preservation and checkability of selected evidence. It narrows which transformed observations may replace raw text and retains ways to recover the source. Its checks do not make the selection exhaustive, validate every semantic label, or supply a correct repair. Compaction admission is driven by an economic model and model-authored progress state; those are operational decisions rather than acceptance of new knowledge about the task.

## Reconciliation

The fresh specialist used the unchanged frozen input and same source pin. Input and method hashes match the report frontmatter, report status is complete, and its source anchors were checked against the pinned blobs. The epistemic lens was applied locally after the runtime baseline; it is not an independent duplicate confirmation of the specialist.

| specialist proposal | canonical record | disposition |
|---|---|---|
| MEM-OBJ-1 | OBJ-5 | adopted at original evidence status |
| MEM-OBJ-2 | OBJ-6 | adopted at original evidence status |
| MEM-OBJ-3 | OBJ-7 | adopted at original evidence status |
| MEM-OBJ-4 | OBJ-8 | adopted at original evidence status |
| MEM-OBJ-5 | OBJ-9 | adopted at original evidence status |
| MEM-OBJ-6 | OBJ-10 | adopted at original evidence status |
| MEM-RTE-1 | RTE-4 | adopted at original evidence status |
| MEM-RTE-2 | RTE-5 | adopted at original evidence status |
| MEM-RTE-3 | RTE-6 | adopted at original evidence status |
| MEM-RTE-4 | RTE-7 | adopted at original evidence status |
| MEM-RTE-5 | RTE-8 | adopted at original evidence status |
| MEM-RTE-6 | RTE-9 | adopted at original evidence status |
| MEM-RTE-7 | RTE-10 | adopted at original evidence status |
| MEM-BAP-1 | BAP-3 | adopted at original evidence status |
| MEM-BAP-2 | BAP-4 | adopted at original evidence status |
| MEM-ABS-1 | ABS-1 | adopted at original evidence status |

All six integration issues were retained: raw/derived/opaque objects remain distinct; both reducer variants and event-derived scheduling remain included; quote completeness, plan correctness and unconditional archive fallback are not inferred; host limits and uncertain aggregate classifications remain; all features are default-off; no supplied canonical fact required correction. The absence record adds an explicit parent search boundary to the specialist's same narrow test/documentation conclusion. This is an evidence-boundary clarification, not a stronger claim.

OBJ-4 is the parent's distinct static economic model; OBJ-8 is accumulated state, so their identities do not collide. The third route slot was reserved but never assigned a referent and remains a gap. RTE-9 and RTE-10 reference OBJ-4 rather than creating duplicate scheduling mechanisms. Authority fields add consumer/channel/horizon detail to BAP-3 and BAP-4. The memory profile was mapped token-for-token; unknown host representation, selection and task horizon were preserved. No substantive conflict required choosing a stronger status, and no previous review contributed evidence.

## Bounded synthesis

SoL-Pi moves selected efficiency work into an extension around Pi: predictable post-edit commands can run without another model turn; repeated observations can become recall handles; a reducer can propose source-checked evidence receipts; and completed plan steps can trigger economically selected native compaction followed by automatic continuation. These routes are conditional because all features are disabled by default. The source establishes extension wiring, while actual savings and preserved task quality require runtime comparisons.

The evidence-preserving reducer offers a narrow, useful contract: retained text must occur in the archived body and replacement must satisfy format/status/size checks. It leaves diagnosis and repair with the main agent. Neither an exact quote nor a valid receipt establishes that omitted evidence was irrelevant. Similarly, `completed` plan status is a scheduling input, not a correctness certificate. The symbolic economic calculation predicts when smaller context should repay its rewriting cost; it does not validate the prediction by revising its formula from observed outcomes.

The supported improvement contribution is the wiring of mechanisms designed to reduce repeat work and context traffic. Historical auto-research selection remains claimed; achieved savings or improved capacity at this revision are uninspected. Conjectural learning through criticism of an operative formulated theory is uninspected: the code supplies fixed policies and retains experience-derived context, but no candidate-linked theory criticism/improvement route is established. Reflection conclusion status: wired in the narrow operational sense that a representation of the extension’s own prior compaction count and cache debt affects later compaction policy and is updated after those operations; request/context growth supplies additional workload evidence. Revision of a self-theory of theory-building organization is uninspected. Self-improvement at the released extension boundary is uninspected; automatic context adaptation and trace-fed retention alone do not establish it.

For a host coding session, the practical distinction is between preserving recoverable evidence and proving complete understanding. The former has explicit archive/check/recall mechanisms; the latter remains the agent's responsibility. Changed host event/compaction APIs, downstream extension ordering, exact native summary evidence, and matched baseline/intervention trajectories would materially change this assessment. No product ranking or Commonplace transfer recommendation follows from this boundary.

## Limitations

| limitation | affected IDs | inspected boundary | conclusion prevented | resolving evidence |
|---|---|---|---|---|
| excluded host behavior | CMP-1, CMP-3, RTE-1, RTE-2 | public calls/hooks only | complete loop, permissions, hook-error fallback and native-summary fidelity | pinned Pi source and deployed integration trace |
| no actual model/run artifacts | CMP-2, CLM-2, CLM-3; memory routes below | source and documentation | activation, reliable recall and causal efficiency benefit | retained receipts/context/outputs and matched interventions |
| provider identity and weights opaque | CMP-2, CMP-3 | model registry names | immutable model identity or runtime parameter updates | provider version/weight evidence |
| historical research process outside release | CLM-1 | README origin claim | recursive self-improvement of the research harness | frozen research code and experiment records |
| scoped interference/fallback checks | RTE-2 and reducer route | local queue/hash and modeled fallback paths | global locking or all-errors preservation | host/OS contract and targeted deployed probes |
| native compaction is host-owned | CMP-3 and compaction route | trigger, callbacks and continuation | exact transformed-content semantics and aggregate representation | pinned native compaction implementation and retained summaries |

## Verification and blockers

### Semantic verification

Checked the source pin, source layers, canonical uniqueness, complete mapped IDs, specialist identity/input/method/report hashes, and quote support. The full baseline covers conditional registration, fused tools, both reducer variants, archive/recall, plan/state recovery and compaction continuation. Static forcing cases delimit interference, validation, error fallback and host settlement. Parameter identity remains separate from parameter updates.

The comparison scope matches OBJ-5, OBJ-6, OBJ-7, OBJ-8, OBJ-9 and OBJ-10. Every qualifying trace-fed retained transformation is included: RTE-6 uses tool traces online with session/task horizon unresolved; RTE-9 uses session history online and explicitly continues the parent task; RTE-10 uses event traces online with a session-bound horizon that cannot be classified as solely per-task. Their dependent source/timing assessments and uncertain horizon/form assessments retain these differences. Raw journal storage, ephemeral projections and ordinary file edits were not counted as additional learning routes.

Push checks named the consumer, trigger and selection: RTE-4 coarse type/size/send age; RTE-6 reducer judgment; RTE-8 latest valid active-branch state to scheduler; RTE-9 host-selected compacted history to the resumed model; RTE-10 state statistics to later policy. Requested RTE-5 and RTE-7 reads remain pull. IDs on files or a host leaf argument do not establish identifier push. Opaque host selection/representation blocks a complete known union. BAP-3 and BAP-4 distinguish evidence from operational force. Admission/rejection and guidance are recorded without calling schema checks theory criticism. OBJ-4's formulation, use, criticism, revision and improvement have separate statuses; reflection is a narrow state-policy connection, not a theory-builder claim.

The epistemic overlay separates check from admission, retention from post-acceptance integration, and architectural status from observed candidate state. No wired route was upgraded to observed activation or causal savings. ABS-1 has a recorded scoped search and prevents a positive faithfulness-tested claim. No execution capsule is claimed. No evidence or semantic blocker remains.

### Deterministic validation

Exact target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-24-sol-pi-01/result.md`. Validation result: `commonplace-validate --full` passed with no errors or warnings.

### Blockers

None.

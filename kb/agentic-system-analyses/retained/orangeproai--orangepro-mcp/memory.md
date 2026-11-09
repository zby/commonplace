---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "OrangePro memory report: fingerprint-bound drafts, graph-selected context, durable proof decisions and reuse boundaries."
run-id: AAS-2026-11-08-orangepro-mcp-4e3d3a22c7c8-01
source-identity: https://github.com/orangeproai/orangepro-mcp
reviewed-boundary: "039cd936e38eb7d52d0e03ded3b3168373d55d77"
---

# OrangePro memory report

## Boundary and evidence

Memory here means the local retained graph, generated artifacts, candidate associations, proof records and saved execution/report state that affect later invocations. Context engineering includes graph-to-prompt selection even when no new memory results. The whole shipped artifact remains included under the [boundary](boundary.md#boundary-and-evidence); host conversation history and hosted backend internals are not attributed to OrangePro. This is not a general conversational memory service.

All findings use SRC-1 at the frozen commit. Direct inspection rechecked HEAD and read bounded implementation ranges in `src/local/workspace.ts`, `src/local/operations.ts`, `src/local/generate/generator.ts`, `src/local/ledger.ts`, `src/local/runReuse.ts`, `src/local/draftTest.ts` and `src/local/mcp.ts`. Searches inspected CLI dispatch, MCP registrations and cache implementations. The supplied runtime supplies the other traced routes explicitly identified below; those are not represented as new direct reads. No target, example, test, provider or service was executed. Implementation evidence establishes wiring, not exercised behavior or benefit.

### Coverage inventory

All source paths below belong to SRC-1. “Supplied” means reliance on the runtime's source-grounded account; “direct” means newly inspected text. Material unresolved parts remain in scope with the prevented conclusion beside them.

| Entry or memory operation | Source path and inspection basis | Record coverage, limit or prevented conclusion |
|---|---|---|
| CLI start/analyze/update/status/gaps/generate/explain/export/jobs; corresponding local MCP tools | `src/local/cli.ts` dispatch search; `src/local/mcp.ts` registration search and explain/export/install bodies; direct | Shared operations are the memory entry points, not a separate host transcript store. [RT-RTE-start-run](runtime.md#rt-rte-start-run), [RT-RTE-test-generation](runtime.md#rt-rte-test-generation), [MEM-RTE-context-selection](#mem-rte-context-selection). No hook-based transcript injection established by these entry points. |
| Workspace graph load/save/init and schema gate | `src/local/workspace.ts`, direct complete | [RT-OBJ-graph](runtime.md#rt-obj-graph), annotation below. Symbolic graph structure and natural-language descriptions have different consumers. |
| Full analysis preservation and incremental stale marking | `src/local/operations.ts`, direct preservation/update/merge ranges | [RT-OBJ-generated-tests](runtime.md#rt-obj-generated-tests), [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission). Full analysis can discard obsolete drafts; update can retain them marked stale. |
| Parse/resolution cache load, persistence and lookup | `src/local/operations.ts`, direct; `src/local/analyze/parseCache.ts`, `src/local/resolve/resolverCache.ts`, bounded searches | [MEM-OBJ-parse-cache](#mem-obj-parse-cache), [MEM-OBJ-resolver-cache](#mem-obj-resolver-cache). Search establishes key/gate/shape mechanisms, not exhaustive correctness of extraction or cache invalidation. |
| Pinned draft reuse and fresh draft append | `src/local/generate/generator.ts`, `src/local/operations.ts`, direct | [RT-RTE-test-generation](runtime.md#rt-rte-test-generation), [RT-OBJ-generated-tests](runtime.md#rt-obj-generated-tests). Provider configuration is resolved before pinning; no-key serving is not established. |
| Grounded, raw, v5 planning/repair and comparison contexts | `src/local/generate/generator.ts`, direct gather/excerpt/pin ranges and repair search; other branches supplied | [MEM-RTE-context-selection](#mem-rte-context-selection), [RT-RTE-generation-compare](runtime.md#rt-rte-generation-compare). No host-window compaction inferred. |
| Staged AI links/flows and alternate apply calls | `src/local/aiGraph/links.ts`, `src/local/flows/llmFlowDiscovery.ts`, supplied; flow preservation direct in `src/local/operations.ts` | [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission). Flow-chain exclusion does not exclude weak link reasons from prompts. |
| Static record, dynamic proof, stats, RTM, auto skip and reports | `src/local/ledger.ts`, direct; `src/local/operations.ts`, direct consumer/load ranges; `src/local/rtm.ts`, `src/local/autoProve.ts`, supplied | [MEM-OBJ-ledger](#mem-obj-ledger), [RT-OBJ-dynamic-proof](runtime.md#rt-obj-dynamic-proof), [RT-BAP-proof-credit](runtime.md#rt-bap-proof-credit). Proof record is derived decision metadata, not the complete raw runner trace. |
| Start shortcut and report model rerender | `src/local/runReuse.ts`, direct complete; `src/local/operations.ts`, direct reuse/save/report searches | [MEM-OBJ-run-key](#mem-obj-run-key), [MEM-RTE-start-reuse](#mem-rte-start-reuse). Display artifacts differ from live graph reload. |
| Proof-attempt diagnostics and report patch statuses | `src/local/operations.ts` doctor/report loads, direct; proof-run workflow supplied | [RT-RTE-start-run](runtime.md#rt-rte-start-run), [RT-RTE-actions-delivery](runtime.md#rt-rte-actions-delivery). Sidecar internals and every report renderer uninspected; no claim that every failure reason feeds a model. |
| Fault brief, candidate repair, persistent attempt budget, export receipt | `src/local/draftTest.ts`, direct selected ranges; `src/local/candidateTest.ts`, `src/local/exportTests.ts`, supplied via runtime | [RT-RTE-draft-verification](runtime.md#rt-rte-draft-verification), annotation below. Receipt replay internals remain uninspected; general resumption of the prior repair conversation is not established. |
| Installed Actions profile/workflow, replay and GitHub PR read-back | `src/local/actionsInstall.ts`, `src/local/actionsRun.ts`, `src/local/publishTests.ts`, supplied | [RT-RTE-actions-delivery](runtime.md#rt-rte-actions-delivery). Profile/candidate authorship unresolved; installation is not evidence of per-test human admission. |
| Detached job state/results and comparison reports | `src/local/jobs/runner.ts`, supplied; compare artifact writes in `src/local/operations.ts`, direct search | [RT-RTE-generation-compare](runtime.md#rt-rte-generation-compare). Files support polling; automatic semantic learning from job logs not established. |
| Hosted run/log/health and QA/grounding service calls | `src/server.ts`, `src/orangeproTools.ts`, `src/apiClient.ts`, `packages/mcp-remote/src/index.ts`, supplied | [RT-RTE-platform-call](runtime.md#rt-rte-platform-call). Remote payloads are opaque backend data; adapters do not expose storage encoding, maintenance or later model selection. |
| Agent workflow instructions and skill/rule distribution | `src/local/agentWorkflow.ts`, `skills/opro/SKILL.md`, `rules/orangepro.mdc`, supplied boundary/runtime | Static shipped guidance, not use-accumulated memory. Host adoption and its model-visible window are outside this evidence. |
| Telemetry infrastructure, build/release/evaluation fixtures | `infra/telemetry-worker/src/index.ts`, boundary inventory; tests/scripts supplied runtime limits | No established later generation consumer of telemetry. Binary infrastructure cache excluded by boundary. Tests are not observed executions; no retained-memory effectiveness conclusion follows. |

## Core ideas

1. **A durable draft is a reusable product, not necessarily training evidence.** The generator can return an unchanged target's runnable draft verbatim without another model call. Code checks fingerprints and flags; proof is a separate admission. See [RT-OBJ-generated-tests](runtime.md#rt-obj-generated-tests) and its annotation.
2. **Retained evidence enters two different authorities.** Graph descriptions, acceptance criteria and weak-link reasons become model context through [MEM-RTE-context-selection](#mem-rte-context-selection). Certificates instead enter fixed code predicates and future work selection through [RT-BAP-proof-credit](runtime.md#rt-bap-proof-credit). The latter does not require a model to interpret a textual rationale.
3. **Retention and withdrawal are consumer-relative.** Full analysis drops obsolete drafts, incremental update marks grounding-touched drafts stale, and RTM can preserve an older matching proof despite a newer failure. There is no single “latest memory wins” rule. See [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof) and [RT-OBJ-generated-tests](runtime.md#rt-obj-generated-tests).
4. **Saved views are not a live recomputation.** Start can rerender saved report data and return its saved result without analysis, proof or model calls. Its reuse key includes ledger and proof-run manifests but excludes ordinary `.orangepro/` outputs from the code key. See [MEM-RTE-start-reuse](#mem-rte-start-reuse). This qualifies any claim that every invocation revalidates every stored artifact.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-ledger
Label: Local gap-fill ledger

The source-native `Ledger` is `.orangepro/ledger.json`, a filesystem JSON container of symbolic `LedgerRecord` values. It includes success/failure statuses, reason, target identity, provenance and optional dynamic certificate. This is distinct from its closest supplied record, the certificate payload [RT-OBJ-dynamic-proof](runtime.md#rt-obj-dynamic-proof); the latter is a part of a ledger record, not the whole history. SRC-1: `src/local/ledger.ts`.

Trace lineage is runner outcome or static record request → operation's derived status/certificate/reason → append. Raw stdout/stderr are not the ledger as a whole; optional bounded Python diagnostic tails differ from complete execution traces. RTM, stats, report and automatic worklist consumers read retained decisions. At those consumers, symbolic predicates determine credit or work eligibility; natural-language reasons explain outcomes to callers. Human approval of each append is not required by these writers. Physical local write access is not authenticated proof origin. No model-parameter update follows from append.

> ledger.records.push(record);
> mkdirSync(workspacePaths(root).dir, { recursive: true });
> writeFileSync(path, JSON.stringify(ledger, null, 2) + "\n", "utf8");
> --- `src/local/ledger.ts`

#### MEM-OBJ-parse-cache
Label: Persistent parse cache

No supplied counterpart after comparison with [RT-OBJ-graph](runtime.md#rt-obj-graph): this is a separate derived cache feeding graph construction, not the graph container. Filesystem `parse-cache.json` stores symbolic symbol extraction and test-name data. Acquisition is deterministic parsing of customer files, not agent conversation. Cache methods use content hash plus language for symbols and content hash for test names; structural/version checks govern load. The analyzer consumes hits in later analysis. Source authenticity and parser semantic correctness do not follow from matching keys. SRC-1: `src/local/analyze/parseCache.ts`, `src/local/operations.ts`.

> const key = `sym:${hash}:${language ?? ""}`;
> --- `src/local/analyze/parseCache.ts`

The analysis driver loads it with empty-cache fallback, then best-effort persists derived cache data. Software admission and physical I/O are automatic, without per-entry human approval. This is recomputation reuse, not demonstrated learning from test outcomes.

#### MEM-OBJ-resolver-cache
Label: Persistent resolver cache

Separate from [MEM-OBJ-parse-cache](#mem-obj-parse-cache) and the supplied graph: filesystem `resolver-cache.json` retains symbolic module-resolution results, not source prose or embeddings. The resolver's gate is derived from filesystem shape/configuration content and resolver version; loaded entries undergo shape checks. Later resolution uses cached results under that gate. Source semantics and hostile local edits are not authenticated. The exact completeness of dependency invalidation remains unaudited. SRC-1: `src/local/resolve/resolverCache.ts`, `src/local/operations.ts`.

> return hashString(`v${RESOLVER_VERSION}\n${sorted.join("\n")}\n${configDigest.join("\n")}`);
> --- `src/local/resolve/resolverCache.ts`

#### MEM-OBJ-run-key
Label: Start run key

Distinct operative access metadata underlying [RT-RTE-start-run](runtime.md#rt-rte-start-run), with no supplied object counterpart. `run-key.json` retains symbolic hashes/versions/timestamps on the local filesystem. It does not contain the report's findings. Separately saved last-start result and report JSON hold selected derived outputs; HTML/Markdown are readable projections rather than the complete graph or raw runner state. Code's next start invocation consumes the key to decide full recomputation versus saved-result reuse. SRC-1: `src/local/runReuse.ts`, `src/local/operations.ts`.

> export const RUN_KEY_FILE = "run-key.json";
> --- `src/local/runReuse.ts`

Lineage is current Git/files/config/ledger/flags/version inputs → digest fields → saved key after a full run. Model-key presence, not secret bytes, enters the input key. Large files above 64 MiB are keyed by size and modification time rather than content, limiting a claim of universal byte-exact invalidation. This is software-controlled admission, not a content approval event.

> if (st.size > HASH_BYTES_LIMIT) return `size:${st.size}:mtime:${Math.floor(st.mtimeMs)}`;
> --- `src/local/runReuse.ts`

### Routes

#### MEM-RTE-context-selection
Label: Graph-to-generation context selection

Part of: [RT-RTE-test-generation](runtime.md#rt-rte-test-generation)

This is the context-selection subroute, not a duplicate end-to-end generation route. A selected target triggers `gatherContext`; code selects acceptance/workflow/actors/examples, linked files, symbol metadata and weak candidate-edge reasons, then reads current source excerpts. Prompt assembly delivers that bounded material to the configured provider. Graph JSON is retained; source excerpt strings are transient request context in this path. SRC-1: `src/local/generate/generator.ts`; prompt force is supplied by [RT-BAP-generation-prompt](runtime.md#rt-bap-generation-prompt).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Planning context, entity IDs, source references and weak-context usage metadata to generation.
- Later read-back: Persisted graph material reaches later provider invocations when selected; live file text is reread separately, not retrieved from a transcript summary.
- Delegated visibility: Provider sees selected strings, not the host's whole conversation or filesystem.
- Selection predicate: Target identity and graph relations; up to four related files, five symbol descriptions per related file, ten example behavior entries; excerpt selector prioritizes target, referenced symbols, associated signatures and existing test heads under an 8000-character budget.
- Invalidation or expiry: Source excerpts are rebuilt for the request; graph freshness and candidate trust remain distinct from prompt delivery. No automatic deletion of already delivered provider context is established.
- Activation or effect: Bounds and shapes model-visible evidence; actual compliance and changed test quality unobserved.
- Evidence limits: Character budgeting is not a total tokenizer/window guarantee; raw-mode generation uses another path, and provider internals remain opaque.

> const MAX_RELATED_FILES = 4;
> --- `src/local/generate/generator.ts`

> const MAX_EXCERPT_CHARS = 8000;
> --- `src/local/generate/generator.ts`

> weakContext.push(`${ce.relationship_type}: ${ce.reason} (confidence ${ce.confidence}).`);
> --- `src/local/generate/generator.ts`

Working-context control is selection before invocation, not removal from an accumulated conversation. Referenced symbols are ranked by direct reference, package proximity and type-like status; over-budget later excerpts are omitted, while the first may be truncated. Material left out remains in graph/files and can be reread by another target request. This resembles pushing selected values into a per-request frame; it is not a live pointer heap or a transcript-compaction service. V5 repair can re-present malformed plan text in a new call; it does not prove durable historical reasoning memory. SRC-1: `src/local/generate/generator.ts`.

#### MEM-RTE-start-reuse
Label: Saved start-result read-back

Part of: [RT-RTE-start-run](runtime.md#rt-rte-start-run)

CLI/MCP start → compute key and output-presence/pending-generation checks → reuse decision → read saved report model and last result → rerender and return. Code owns admission and selection; caller `fresh` can force recomputation. No model chooses or approves the saved content. This is a shortcut within start, not another orchestration engine. SRC-1: `src/local/runReuse.ts`, `src/local/operations.ts`; [MEM-OBJ-run-key](#mem-obj-run-key).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Earlier StartResult plus refreshed report path, checked time and explicit no-analysis/proof/model-call guidance.
- Later read-back: Saved full-run result and report model are consumed on a subsequent matching start.
- Delegated visibility: inapplicable — successful shortcut calls no model or proof child.
- Selection predicate: Matching code/input/analysis keys, present saved outputs, no retry-worthy generation failure; renderer/tool change can rerender without reanalysis.
- Invalidation or expiry: Fresh, missing/non-Git key, absent outputs, code/input/analysis changes or pending generation force full computation. No time-to-live is imposed by the inspected decision.
- Activation or effect: Suppresses repeated analysis/proof/generation and returns retained decisions; successful speed or correctness benefit is unobserved.
- Evidence limits: Key agreement is not content authentication; ordinary workspace outputs are excluded from the code digest. Graph and candidate-file mutation alone is not thereby guaranteed to invalidate reuse.

> if (previous.analysis !== current.analysis) return { kind: "full", reason: "analysis_changed", previous };
> if (input.generationPending) return { kind: "full", reason: "generation_pending", previous };
> return { kind: "reuse", rerender: previous.renderer !== current.renderer || previous.tool !== current.tool, previous };
> --- `src/local/runReuse.ts`

> const ownOutputs = `${prefix}.orangepro/`;
> --- `src/local/runReuse.ts`

The key explicitly includes ledger and proof-run manifests as exceptions via input hashing. Successful full runs save results only when final reports were written. Malformed/missing saved data or rerender failure can fall through to full computation. There is no content-edit or rollback transaction here; saved outputs are replaced by later successful writes. Retry eligibility is based on stored failure/status text, not demonstrated model diagnosis.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-graph](runtime.md#rt-obj-graph)

Storage is filesystem JSON, with a schema-version gate but no general authenticity verification on arbitrary field values. Derived nodes/edges come from repository analysis/enrichers and candidate admission; acceptance/description text remains interpreted content, while IDs, strengths, fingerprints and relations drive fixed selectors. Load is not retrieval by semantic similarity. No vector/embedding store is established in these inspected local paths. This does not characterize the opaque backend. SRC-1: `src/local/workspace.ts`, `src/local/operations.ts`, [MEM-RTE-context-selection](#mem-rte-context-selection).

> if (graph.schema_version !== LOCAL_GRAPH_SCHEMA_VERSION) {
> --- `src/local/workspace.ts`

#### On [RT-OBJ-generated-tests](runtime.md#rt-obj-generated-tests)

Full reanalysis retains tests only with a current CodeSymbol target, a matching fingerprint and no stale flag; generation-run membership is trimmed to retained IDs. Incremental update instead marks drafts stale when grounding references touch changed files. Thus physical retention differs from reuse eligibility. SRC-1: `src/local/operations.ts`.

> if (!target || !currentSymbols.has(target) || !test.target_fingerprint || test.stale === true) continue;
> if (targetFingerprint(graph, target) !== test.target_fingerprint) continue;
> --- `src/local/operations.ts`

> if (touches && !t.stale) {
>   staleCount++;
>   return { ...t, stale: true };
> }
> --- `src/local/operations.ts`

Pinned reuse selects the last matching run's runnable, non-stale tests for the target fingerprint; it is not a new model rewrite. Fresh drafts append, pinned drafts do not duplicate. The target check does not by itself attest that every dependency or external expectation is unchanged. Graph citation validation proves reference resolution, not correctness of the generated assertion. Body edits by a local user/process are not cryptographically excluded. SRC-1: `src/local/generate/generator.ts`, `src/local/operations.ts`.

> const latestRunId = matches[matches.length - 1].run_id;
> return matches.filter((t) => t.run_id === latestRunId);
> --- `src/local/generate/generator.ts`

#### On [RT-RTE-test-generation](runtime.md#rt-rte-test-generation)

Admission into graph storage is software-controlled after generation/body processing, not per-content human approval. Later host editing or refusal is a separate route; automatic proof can write/run without that host step. Pinned output preserves original lineage rather than appending another generation run. Provider resolution precedes `generateTests`, so the implemented no-provider return can prevent serving retained drafts even when they exist. SRC-1: `src/local/operations.ts`; [RT-RTE-start-run](runtime.md#rt-rte-start-run).

> const freshTests = result.generated_tests.filter((t) => !t.pinned);
> --- `src/local/operations.ts`

#### On [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission)

Separate staged JSON and graph candidate metadata preserve model proposals and their weak/candidate identity. Subsequent graph apply and flow preservation revalidate structure/anchors. Human withholding is afforded by separate apply, not required by start. Candidate-edge reasons can become natural-language weak context at the provider; deterministic flow-chain selection excludes the separate candidate-flow lane. The closest source witness for that distinction is [MEM-RTE-context-selection](#mem-rte-context-selection) plus the runtime's quoted apply checks. No candidate-link relevance benefit is observed. SRC-1: `src/local/operations.ts`, `src/local/generate/generator.ts`; supplied `src/local/aiGraph/links.ts`, `src/local/flows/llmFlowDiscovery.ts`.

#### On [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof)

Raw baseline/mutant results become derived symbolic admission metadata in [MEM-OBJ-ledger](#mem-obj-ledger). Later RTM/auto selection consumes certificate and fingerprint rather than a general model-authored lesson. Failure reasons can remain as diagnostic content. A later unsuccessful record does not necessarily withdraw an older still-matching proof, as the supplied RTM selector establishes. This is a trace-fed retained decision path, not evidence of improved capacity, weight learning or revised test-generation policy. SRC-1: `src/local/ledger.ts`; supplied `src/local/rtm.ts`, `src/local/autoProve.ts`.

#### On [RT-RTE-draft-verification](runtime.md#rt-rte-draft-verification)

Attempt folders retain prompts/replies/patches/manifests; counts from earlier runs constrain later drafting. Within one invocation, a failed candidate and classified observations enter the next model request with the unchanged brief. These are raw-to-derived feedback and a later consumer, not just unused logging. The repair text requests setup-only changes, and code checks a baseline. Reasons are retained and delivered locally to repair, but reliable model compliance and successful improvement are unobserved. SRC-1: `src/local/draftTest.ts`; supplied verification gates in `src/local/candidateTest.ts`.

> "# What happened when OrangePro ran it",
> outcome,
> --- `src/local/draftTest.ts`

> const prompt = attempts.length === 0 ? firstPrompt : repairPrompt(firstPrompt, previous, outcomeText);
> --- `src/local/draftTest.ts`

Cross-invocation replay is narrower than resuming the previous model context: `baseline`, `previous` and `outcomeText` initialize empty even while persisted attempt counts are loaded. Checked `generation-request.json` is an alternative retained input, not a free-form conversation checkpoint.

> let baseline: ModelReply | null = null;
> let previous: ModelReply | null = null;
> let outcomeText = "";
> --- `src/local/draftTest.ts`

#### On [RT-RTE-generation-compare](runtime.md#rt-rte-generation-compare)

Detached status/result files provide read-back to polling caller; comparison artifacts preserve both suites and scores. Child-process separation excludes the host transcript, but is not itself subagent-context compaction. The supplied route establishes no automatic installation of a winner as new model/prompt policy. Comparison storage therefore does not establish trace learning. SRC-1: supplied `src/local/jobs/runner.ts`, `src/local/operations.ts`.

#### On [RT-RTE-actions-delivery](runtime.md#rt-rte-actions-delivery)

Installed workflow/profile is symbolic production machinery consumed on later events. Candidate test text has executable authority only through replay/verification and eventually a downstream accepted repository change; publication opens a draft PR, not a merge. Caller confirmation admits installation/publication; candidate authorship and any earlier human content approval remain unresolved. Receipts, manifests and PR read-back are recovery/admission state, not generalized lessons. SRC-1: supplied `src/local/actionsInstall.ts`, `src/local/actionsRun.ts`, `src/local/publishTests.ts`.

#### On [RT-RTE-platform-call](runtime.md#rt-rte-platform-call)

Backend run/log/QA responses are immediate text delivery at the adapter. Their internal storage, lineage, numerical representations, revision rules, later model consumers and context budgets remain uninspected. Caller-selected IDs establish targeting of a service resource, not semantic retrieval of retained knowledge. No local-to-hosted memory synchronization is established by the supplied adapter account. SRC-1: supplied `src/orangeproTools.ts`, `src/apiClient.ts`, `packages/mcp-remote/src/index.ts`.

## Write side

Acquisition has separate admission mechanisms. Deterministic analysis scans the customer checkout and writes derived graph/cache state; invocation authorizes a workflow but does not prove a human approved every discovered claim. Model generation proposes tests; structural/body/runnable checks govern draft storage, and dynamic proof separately governs public credit. AI link/flow apply has software validation and an optional standalone caller pause; start combines generation and apply. See [RT-OBJ-graph](runtime.md#rt-obj-graph), [RT-RTE-test-generation](runtime.md#rt-rte-test-generation), [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission).

Maintenance does not have one universal replacement policy. Analysis reconstructs graph content while selectively preserving valid generated artifacts and candidate flows. Update marks grounding-touched drafts stale. Cache misses recompute; malformed cache input falls back empty; malformed graph schema refuses load. Start reuse can bypass recomputation when its metadata allows it. These mechanisms are software curation/reuse, not semantic warrant or immunity to local tampering. See [MEM-OBJ-parse-cache](#mem-obj-parse-cache), [MEM-OBJ-resolver-cache](#mem-obj-resolver-cache), [MEM-RTE-start-reuse](#mem-rte-start-reuse).

The outcome-fed paths differ. Baseline/mutant execution produces a ledger decision that later grants credit or changes target selection; optional reason/diagnostics remain explanatory material, not a consumed new strategy. Fault verification produces classified observations that the same drafting invocation supplies to a repair call; durable counts also limit later invocations. The resulting test may be admitted as a verified/exportable artifact. Neither chain establishes improved future capacity merely because feedback persists. See [MEM-OBJ-ledger](#mem-obj-ledger), [RT-RTE-draft-verification](runtime.md#rt-rte-draft-verification).

Withdrawal is bounded: stale/missing target drafts cease reuse, malformed/stale flows are rejected or revalidated, failed setup leaves proof ledger untouched, and unsuccessful proof can append unproven without erasing an earlier current proof. Actions install/publish can refuse edited managed files or a moved base. Unsuccessful artifacts can remain on disk. No universal erasure, rollback of arbitrary repository commands, or backend deletion protocol follows. SRC-1: `src/local/operations.ts`, `src/local/generate/generator.ts`; supplied [RT-RTE-targeted-proof](runtime.md#rt-rte-targeted-proof), [RT-RTE-actions-delivery](runtime.md#rt-rte-actions-delivery).

## Read-back

The concrete consumers are later generation calls, analysis/resolution, report/RTM/automatic worklist code, start shortcut, candidate repair and host polling/delivery. They are not interchangeable. [MEM-RTE-context-selection](#mem-rte-context-selection) is code-initiated selection inside a requested generation operation, not independent unsolicited injection into the host window. [MEM-RTE-start-reuse](#mem-rte-start-reuse) selects a saved whole result by matching input metadata, not by query similarity. Pinned draft read-back returns a retained executable product verbatim, with lineage, rather than asking a model to summarize it.

Proof credit is fixed-rule authority over later reports and skip decisions; provider prompt content has interpreted advisory/instruction force. Export and explain afford human/host inspection of provenance and draft metadata; storing an export alone does not establish that a hosted consumer imported it. The installed Actions profile has a known later event consumer, unlike an unspecified hypothetical caller of a storage API. Opaque platform state retains only the service affordance in [RT-RTE-platform-call](runtime.md#rt-rte-platform-call).

Working-context control is local to request construction and process/task boundaries. Selected excerpts and malformed-plan repair inputs bound provider visibility; comparison uses separate calls and detached jobs carry flags/environment rather than a conversation. No inspected route establishes host transcript eviction, long-term summary compaction or automatic rehydration of removed host turns. This is an evidence limit about the target boundary, not a whole-runtime absence claim. SRC-1: `src/local/generate/generator.ts`; [RT-RTE-generation-compare](runtime.md#rt-rte-generation-compare).

## Integration issues

- No supplied fact requires correction. [MEM-RTE-context-selection](#mem-rte-context-selection) and [MEM-RTE-start-reuse](#mem-rte-start-reuse) are declared subroutes, not proposed replacements for their runtime containers. [MEM-OBJ-ledger](#mem-obj-ledger) is distinct from the certificate payload [RT-OBJ-dynamic-proof](runtime.md#rt-obj-dynamic-proof). No other possible duplicate identified after comparison.
- Fingerprint currency does not establish dependency/expectation currency. Full preservation, incremental stale marking and pinned generation use different checks. Evidence: quoted checks on [RT-OBJ-generated-tests](runtime.md#rt-obj-generated-tests). Consequence: do not describe one uniform freshness invariant across all consumers.
- Saved start reuse does not hash every workspace output. Evidence: [MEM-RTE-start-reuse](#mem-rte-start-reuse), `src/local/runReuse.ts`. Consequence: fresh report presentation is not necessarily a fresh graph/proof computation or exhaustive candidate revalidation.
- Retained proof-attempt sidecar internals, full receipt replay and all cache dependency paths are not exhaustively inspected. Evidence: inventory and [MEM-OBJ-resolver-cache](#mem-obj-resolver-cache), [RT-RTE-actions-delivery](runtime.md#rt-rte-actions-delivery). Consequence: no complete diagnostic-feedback, replay-security or invalidation-correctness claim.
- Hosted memory substrate/maintenance and profile/candidate approval provenance remain unresolved. Evidence: [RT-RTE-platform-call](runtime.md#rt-rte-platform-call), [RT-RTE-actions-delivery](runtime.md#rt-rte-actions-delivery). Consequence: local symbolic/text findings cannot classify opaque backend memory or infer human-controlled content admission.

## Limitations and checks

Source HEAD rechecked as 039cd936e38eb7d52d0e03ded3b3168373d55d77. Supplied run identity, repository identity, boundary/type and worker/record procedures were read completely; truncated-size notices for bounded input ranges were followed through their final empty range. This is static source analysis. There is no observed execution, activation, learning or quality benefit evidence. Provider internal state and host context policy remain outside the inspectable target. Quotation occurrence and schema checks do not establish analytical completeness.

Validation: passed with the assigned role/artifact validator; no findings.

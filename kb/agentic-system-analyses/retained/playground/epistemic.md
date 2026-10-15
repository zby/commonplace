---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Playground epistemic routes: file and execution evidence, operational gates, ancillary transformations and unimplemented model-memory claims."
run-id: AAS-2026-10-14-playground-88ee8a292f9b-01
reviewed-boundary: de28ac8fdda30c7a5c2ee099de089e65a685195f
---

# Playground epistemic report

## Source-and-claim boundary

The question is what the shipped provider acquires, transforms, checks and licenses for later reliance, as distinct from the model-memory loop described in its documents. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity is see [Source register](boundary.md#source-register). All source references below are SRC-1 at the frozen revision. Implementation deductions are not observations. No target execution, model call or causal experiment was supplied or performed.

External MCP clients and Faculties implementations are excluded. Their absence prevents attributing semantic evaluation, memory acceptance, model parameter change or downstream compliance to Playground. The provider can deliver truth-apt file text and execution reports without deciding that their substantive assertions are true. Arbitrary shell execution permits caller-supplied evaluators; that affordance is not a shipped epistemic evaluator. Ancillary shipped scripts are assessed separately from the provider dispatch.

### Coverage

| Entry point or operation | Source path | Coverage and records | Remaining limit |
|---|---|---|---|
| Executable dispatch, stdio and HTTP, administrative lifecycle | SRC-1: `src/main.rs` | Direct enum/main read; supplied [RT-RTE-sandbox-exec](runtime.md#rt-rte-sandbox-exec), [RT-RTE-tenant-provision](runtime.md#rt-rte-tenant-provision) | Admin details largely supplied; no deployed grants or revocation effects observed. |
| Eight registered tools, result and file handling | SRC-1: `src/mcp.rs` | Direct dispatch, file parser/check/encoder and render reads; [EPI-RTE-file-check](#epi-rte-file-check), [EPI-RTE-file-disposition](#epi-rte-file-disposition), [EPI-RTE-result-render](#epi-rte-result-render); supplied session/exec/job findings | No semantic content evaluator found in these branches; command-internal programs remain arbitrary. |
| Job output, terminal publication, polling and eviction | SRC-1: `src/jobs.rs` | Direct poll/render/terminal reads; [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs) and [EPI-RTE-result-render](#epi-rte-result-render) | Output may be omitted or decoded lossily; terminal observation is server-side, not client acknowledgement. |
| Authentication, native catalogue, worker routing and unknown outcomes | SRC-1: `src/mcp_http.rs`, `src/mcp_http/workers.rs` | Supplied [RT-RTE-worker-forward](runtime.md#rt-rte-worker-forward), [RT-BAP-worker-mapping](runtime.md#rt-bap-worker-mapping) | Native answers, tools and model internals opaque. |
| Backend execution, cleanup, file persistence and source bundles | SRC-1: `src/sandbox/jail.rs`, `src/sandbox/lima.rs`, `src/sandbox/runner.rs`, `src/sandbox/faculties.rs` | Supplied [RT-RTE-sandbox-exec](runtime.md#rt-rte-sandbox-exec), [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs), [RT-RTE-bundle-build](runtime.md#rt-rte-bundle-build) | Host-dependent proof and build completion do not prove answer truth, improvement or universal append-only enforcement. |
| Native worker service | SRC-1: `deploy/freebsd/playground_faculties` | Supplied [RT-RTE-worker-forward](runtime.md#rt-rte-worker-forward) | Launch/restart conditions are operational, not criticism of answers. |
| Public-edge smoke and optional cancellation check | SRC-1: `deploy/freebsd/smoke.sh` | Direct full read; [EPI-RTE-smoke-check](#epi-rte-smoke-check) | Designed check only; no result supplied. |
| Timestamp migration | SRC-1: `scripts/migrate_timestamps.rs` | Direct full read; [EPI-RTE-timestamp-reshape](#epi-rte-timestamp-reshape), [EPI-RTE-timestamp-retain](#epi-rte-timestamp-retain) | External storage/parser semantics and actual datasets uninspected. |
| Wiki link rewriting | SRC-1: `scripts/rewrite-links.sh` | Direct full read; [EPI-RTE-link-rewrite](#epi-rte-link-rewrite) | External `wiki` resolver unavailable; semantic preservation not determined. |
| Telemetry display | SRC-1: `scripts/view_telemetry.rs` | Direct full read; [EPI-RTE-telemetry-report](#epi-rte-telemetry-report) | Data authenticity, missing-value coverage and external storage internals unknown. |
| Memory architecture, base/corporate prompts, event loop | SRC-1: `docs/playground_memory_architecture.md`, `prompts/system_prompt.md`, `prompts/system_prompt_corpo.md`, `docs/playground_event_model.md` | Direct full reads; [EPI-CLM-memory-provenance](#epi-clm-memory-provenance), [EPI-CLM-shell-causality](#epi-clm-shell-causality) | Doctrine not evidence of current prompt loading, summary creation, acceptance or iteration. |
| Older design and configuration, other docs, templates, proxy/OAuth details, other deployment checks and Rust tests | SRC-1: `design.md`, `docs/playground.md`, `docs/memory_temporal_redesign.md`, `scripts/lima-session.yaml.tmpl`, `scripts/lima.yaml.tmpl`, `deploy/freebsd/Caddyfile`, `src/oauth.rs`, `tests/` | Boundary/supplied runtime coverage plus bounded source searches, not detailed inspection here | Relevant uninspected paths prevent a system-complete negative about every possible evaluator or maintenance hook. Tests supply no observed pass. |
| Archive importer fragments, external Faculties | SRC-1: `importers/`, `faculties` | Exclusions are see boundary | Prevent attribution of functioning archive ingestion, external memory and model cognition. |

Consequential warrant claims are [EPI-CLM-file-lossless](#epi-clm-file-lossless), [EPI-CLM-memory-provenance](#epi-clm-memory-provenance) and [EPI-CLM-shell-causality](#epi-clm-shell-causality). Persistence is see [RT-CLM-persistent-sandbox](runtime.md#rt-clm-persistent-sandbox). No system-wide knowledge-production or reliability verdict follows from this coverage.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-file-payload](#epi-obj-file-payload) | Arbitrary caller/file propositions, when present | File exchange | SRC-1: `src/mcp.rs` | Particular assertions and original evidence provenance not supplied. |
| [EPI-OBJ-exec-result](#epi-obj-exec-result) | stdout/stderr assertions plus exit/error/cancel observations | Execution feedback | SRC-1: `src/mcp.rs`, `src/jobs.rs` | Process success is not source truth; output loss/decoding changes evidence delivered. |
| [RT-OBJ-worker-manifest](runtime.md#rt-obj-worker-manifest) | None required: routing policy rather than asserted answer | see record | SRC-1: `src/mcp_http/workers.rs` | Operational destination authority, not epistemic endorsement. |
| [EPI-OBJ-timestamp-tribles](#epi-obj-timestamp-tribles) | Entity timestamp interval assertions | Migration input/output | SRC-1: `scripts/migrate_timestamps.rs` | Encoding domain is inspectable; whether original timestamps are true is not. |
| [EPI-OBJ-wiki-fragments](#epi-obj-wiki-fragments) | Arbitrary fragment assertions and referenced entities | Link expansion | SRC-1: `scripts/rewrite-links.sh` | External resolution may alter referents; unavailable implementation. |
| [EPI-OBJ-telemetry-spans](#epi-obj-telemetry-spans) | Recorded durations, counts and aggregate claims | Diagnostic display | SRC-1: `scripts/view_telemetry.rs` | Invalid durations are filtered; actual measurements and completeness unknown. |
| [EPI-CLM-memory-provenance](#epi-clm-memory-provenance) | Documented summary texts and temporal associations, not a supplied candidate instance | see claim | SRC-1: `docs/playground_memory_architecture.md` | No implemented memory object or instance established in provider. |

## Authority-route ledger

Route ID: [RT-RTE-file-exchange](runtime.md#rt-rte-file-exchange)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-file-payload](#epi-obj-file-payload)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: sandbox file bytes or caller payload entering file exchange.
Evaluator/condition and domain: encoding/parser/clean-shell rules; substantive truth unassessed.
Activation and timing: see route.
Possible or observed result: see route; source warrant unknown, byte fidelity preserved within successful bounded read/write protocol, not authenticated provenance.
Implemented force: file bytes delivered or replaced.
Epistemic authority and scope: no license for substantive assertions merely from transport success.
Operational authority: behavior permitted, blocked, or changed: accepted writes replace files accessible to later commands; reads deliver content.
Behavioral-authority path: client receives MCP content; shell/filesystem consumes bytes, enforcing current write and later persisted effects; client interpretation unknown.
Evidence source ID and local anchor: SRC-1: `src/mcp.rs`.
Claim IDs or none: [EPI-CLM-file-lossless](#epi-clm-file-lossless).
Mismatch marker or none: none within protocol; overwrite is not knowledge acceptance.
Gap/limit: malicious/false text can satisfy every file-tool check.

Route ID: [EPI-RTE-file-check](#epi-rte-file-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-file-payload](#epi-obj-file-payload)
Content/update relation: no content change
Transition or check target: payload encoding/size and shell command completion, not a proposition inside file text.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: parser rejection or completion predicate true/false; no observed run.
Implemented force: produces predicate/error consumed by disposition.
Epistemic authority and scope: valid bounded payload and reported command completion only.
Operational authority: behavior permitted, blocked, or changed: predicate participates in file call continuation/success.
Behavioral-authority path: file handler through Rust result/error, enforcing current call.
Evidence source ID and local anchor: SRC-1: `src/mcp.rs`.
Claim IDs or none: [EPI-CLM-file-lossless](#epi-clm-file-lossless).
Mismatch marker or none: none.
Gap/limit: no post-write equality check, transaction or semantic evaluator.

Route ID: [EPI-RTE-file-disposition](#epi-rte-file-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-file-payload](#epi-obj-file-payload)
Content/update relation: no content change
Transition or check target: admitting payload/exposing file success or error.
Evaluator/condition and domain: see record.
Activation and timing: parser before execution; command check after possible mutation.
Possible or observed result: admitted call, normal content or `isError`; source-only.
Implemented force: enforcement at parser/return boundary; failure cannot undo a partial file.
Epistemic authority and scope: operational file admission only, not evidence-consuming acceptance of an ampliative claim.
Operational authority: behavior permitted, blocked, or changed: invalid payload cannot reach write; unsuccessful file command cannot return normal file success.
Behavioral-authority path: provider/file handler then client, enforcing call admission and result class; downstream interpretation advisory/unknown.
Evidence source ID and local anchor: SRC-1: `src/mcp.rs`.
Claim IDs or none: [EPI-CLM-file-lossless](#epi-clm-file-lossless).
Mismatch marker or none: none.
Gap/limit: generic caller identity does not establish human per-content approval.

Route ID: [EPI-RTE-result-render](#epi-rte-result-render)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-exec-result](#epi-obj-exec-result)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: process bytes/status to delivered text/JSON.
Evaluator/condition and domain: see record; bounded selection plus UTF-8 decoding.
Activation and timing: terminal synchronous return or cursor-selected poll.
Possible or observed result: rendered report; valid UTF-8 surviving bytes are reshaped, malformed bytes replaced, dropped output omitted. Arbitrary semantic preservation is not established.
Implemented force: determines what evidence client receives.
Epistemic authority and scope: backend-reported status and surviving output only; exit zero does not endorse arbitrary stdout.
Operational authority: behavior permitted, blocked, or changed: client receives formatted outcome; job terminal state affects capacity separately.
Behavioral-authority path: MCP client, content channel, advisory execution report, current response and retained-job polling horizon.
Evidence source ID and local anchor: SRC-1: `src/mcp.rs`, `src/jobs.rs`.
Claim IDs or none: [EPI-CLM-shell-causality](#epi-clm-shell-causality).
Mismatch marker or none: provider feedback is not proof of deterministic replay or model-loop causality.
Gap/limit: semantic content not individually supplied; command-internal tests possible but uninspected.

Route ID: [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-exec-result](#epi-obj-exec-result)
Content/update relation: no content change
Transition or check target: bounded job output/state retained for later poll.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route; retention does not constitute acceptance or lifecycle integration.
Implemented force: survives reconnect within same daemon; drops/expiry constrain later evidence.
Epistemic authority and scope: no new warrant beyond retained backend report.
Operational authority: behavior permitted, blocked, or changed: capacity refusal/eviction and later output delivery; cleanup-control loss shuts admission.
Behavioral-authority path: job manager via fixed state rules, enforcing job admission and bounded read-back, daemon/TTL horizon; client continuation external.
Evidence source ID and local anchor: SRC-1: `src/jobs.rs`.
Claim IDs or none: none.
Mismatch marker or none: final-page observation is not proof of client receipt.
Gap/limit: cleanup/rejection is operational protection, not withdrawal of a false claim.

Route ID: [RT-RTE-sandbox-exec](runtime.md#rt-rte-sandbox-exec), [RT-RTE-tenant-provision](runtime.md#rt-rte-tenant-provision), [RT-RTE-worker-forward](runtime.md#rt-rte-worker-forward)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see routes and [RT-OBJ-worker-manifest](runtime.md#rt-obj-worker-manifest).
Content/update relation: non-truth-apt policy/content update: provisioning, authentication and destination selection
Transition or check target: account/session/backend ownership and fixed worker destination, not answer content.
Evaluator/condition and domain: see routes; software validation with operator configuration.
Activation and timing: see routes.
Possible or observed result: authorized execution/forwarding or refusal; no observed outcome.
Implemented force: gate outside arbitrary shell/native answer semantics.
Epistemic authority and scope: caller/destination authority does not establish truth of returned text.
Operational authority: behavior permitted, blocked, or changed: admitted commands can execute, credentials can be revoked on subsequent requests, workers receive fixed routed requests.
Behavioral-authority path: see [RT-BAP-shell-command](runtime.md#rt-bap-shell-command) and [RT-BAP-worker-mapping](runtime.md#rt-bap-worker-mapping).
Evidence source ID and local anchor: SRC-1: `src/main.rs`, `src/mcp_http.rs`, `src/mcp_http/workers.rs`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: no per-command semantic approval; worker timeout neither retries nor proves cancellation.

Route ID: [RT-RTE-bundle-build](runtime.md#rt-rte-bundle-build)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see route; executable bundle.
Content/update relation: non-truth-apt policy/content update: source-driven capability installation
Transition or check target: fingerprint cache or compile/stage completion.
Evaluator/condition and domain: see route; compilation is not behavioral quality evaluation.
Activation and timing: see route.
Possible or observed result: cached/built cohort or rejection on failure.
Implemented force: completion stamp selects later installation/reuse.
Epistemic authority and scope: build/stage completion only, not true answers or improved capability.
Operational authority: behavior permitted, blocked, or changed: shell executable cohort available to subsequent sessions.
Behavioral-authority path: builder/cache/guest PATH, permissive capability admission, source-fingerprint/cache and guest-lifetime horizon.
Evidence source ID and local anchor: SRC-1: `src/sandbox/faculties.rs`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: external source behavior uninspected; no causal benefit evidence.

Route ID: [EPI-RTE-timestamp-reshape](#epi-rte-timestamp-reshape)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-timestamp-tribles](#epi-obj-timestamp-tribles)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: correctly encoded LE timestamp intervals mapped to new OBE attributes.
Evaluator/condition and domain: explicit integer decoding/re-encoding; source truth unchanged.
Activation and timing: operator script invocation scanning recognized attributes.
Possible or observed result: same interval endpoints under new encoding, deduplicated against existing facts; no observed migration.
Implemented force: produces proposed additions.
Epistemic authority and scope: mathematical encoding preservation for correctly typed LE values only.
Operational authority: behavior permitted, blocked, or changed: additions passed to retain route.
Behavioral-authority path: migration code through symbolic tribles, current computation; external readers not inspected.
Evidence source ID and local anchor: SRC-1: `scripts/migrate_timestamps.rs`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: ISO conversion additionally depends on external hifitime interpretation; invalid UTF-8/empty/parse-failed values skipped. No substantive timestamp verification.

Route ID: [EPI-RTE-timestamp-retain](#epi-rte-timestamp-retain)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-timestamp-tribles](#epi-obj-timestamp-tribles)
Content/update relation: no content change
Transition or check target: nonempty new fact set and dry-run flag.
Evaluator/condition and domain: script fixed rule, not epistemic acceptance.
Activation and timing: after migration pass; operator may choose dry-run.
Possible or observed result: commit/push or no write; errors propagate.
Implemented force: requests append of new facts, no explicit deletion of old ones.
Epistemic authority and scope: none newly granted.
Operational authority: behavior permitted, blocked, or changed: alternate timestamp attributes persisted for external consumers.
Behavioral-authority path: script workspace/repository API, write request, branch horizon; storage and downstream semantics external.
Evidence source ID and local anchor: SRC-1: `scripts/migrate_timestamps.rs`.
Claim IDs or none: none.
Mismatch marker or none: retention is not lifecycle integration after acceptance.
Gap/limit: no observed storage result or automatic semantic rollback.

Route ID: [EPI-RTE-link-rewrite](#epi-rte-link-rewrite)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-fragments](#epi-obj-wiki-fragments)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: shortened wiki/files references in fragment text.
Evaluator/condition and domain: shell wrapper calls external resolver; semantic target unavailable.
Activation and timing: manual script pass; changed output admitted to edit.
Possible or observed result: returned expansions edited, errors skipped, ambiguities collected; no observed edit.
Implemented force: persisted edit request when original differs from returned text.
Epistemic authority and scope: no checked substantive warrant; full IDs alone do not prove original intended referents.
Operational authority: behavior permitted, blocked, or changed: external wiki content/references may change later retrieval.
Behavioral-authority path: wrapper → external wiki edit, write request, stored fragment horizon unknown.
Evidence source ID and local anchor: SRC-1: `scripts/rewrite-links.sh`.
Claim IDs or none: none.
Mismatch marker or none: ambiguity handling is declared in comments; external resolver enforcement uninspected.
Gap/limit: non-ampliative reshaping remains possible, but requires resolver/intent evidence; shell command substitution also strips trailing newlines.

Route ID: [EPI-RTE-telemetry-report](#epi-rte-telemetry-report)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-telemetry-spans](#epi-obj-telemetry-spans)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: successfully decoded span durations grouped by resolved name.
Evaluator/condition and domain: integer sum/count over selected records; floating display approximates milliseconds.
Activation and timing: script invocation over fixed branch.
Possible or observed result: ranked durations and grouped sum/count; no observed output.
Implemented force: stdout only, no automatic policy update.
Epistemic authority and scope: arithmetic claims about selected decoded records conditional on supplied values; no warrant for measurement truth or causal bottleneck attribution.
Operational authority: behavior permitted, blocked, or changed: diagnostic information available to operator, continuation external.
Behavioral-authority path: stdout to operator, advisory, current report horizon.
Evidence source ID and local anchor: SRC-1: `scripts/view_telemetry.rs`.
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: same-name distinct spans merged, invalid durations omitted; aggregate is not total wall time. Arithmetic range must avoid overflow.

Route ID: [EPI-RTE-smoke-check](#epi-rte-smoke-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: selected provider responses/process states, not arbitrary knowledge claims.
Content/update relation: no content change
Transition or check target: selected deployment contract and optional cancellation fixture.
Evaluator/condition and domain: see record; fixed reference outcomes, curl/jq/grep and FreeBSD process probes.
Activation and timing: manual operator script; cancellation explicitly opted in.
Possible or observed result: abort/error or printed pass; no supplied pass.
Implemented force: failure stops script; cleanup trap attempts test teardown; pass prints only, no wired release gate.
Epistemic authority and scope: bounded behavioral test outcome if run under required conditions; neither universal isolation nor causal mechanism/transfer proof.
Operational authority: behavior permitted, blocked, or changed: script continuation/termination and fixture cleanup only.
Behavioral-authority path: shell predicates, enforcing test continuation; stdout/stderr operator advisory, test-run horizon.
Evidence source ID and local anchor: SRC-1: `deploy/freebsd/smoke.sh`.
Claim IDs or none: [RT-CLM-persistent-sandbox](runtime.md#rt-clm-persistent-sandbox).
Mismatch marker or none: comments calling the test a proof are bounded to its fixtures and conditions.
Gap/limit: no executed comparison; marker grep establishes presence, not exact arbitrary output integrity.

Route ID: [EPI-CLM-memory-provenance](#epi-clm-memory-provenance), [EPI-CLM-shell-causality](#epi-clm-shell-causality)
Route function: other — described model-memory loop
Architectural status: doctrine only
Object/candidate ID: documented memory summaries and cognition events; no operational instance established.
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: historical interactions to summaries, time-overlap associations and model context.
Evaluator/condition and domain: docs specify temporal queries/budget rules; prompts request consolidation and grounded conduct, not evidence-consuming acceptance of summary truth.
Activation and timing: document describes model/user-directed memory creation; current executable connection not found in inspected dispatch.
Possible or observed result: described summaries/cover; neither observed nor attributed as provider implementation.
Implemented force: none established in current provider.
Epistemic authority and scope: temporal association would not itself prove summarization lineage, endorsement or truth even if externally implemented.
Operational authority: behavior permitted, blocked, or changed: requested model recall/consolidation only; loading/compliance unknown.
Behavioral-authority path: authored natural-language prompts to intended external model, advisory request if loaded; actual channel/horizon unestablished.
Evidence source ID and local anchor: SRC-1: `docs/playground_memory_architecture.md`, `docs/playground_event_model.md`, `prompts/system_prompt.md`, `prompts/system_prompt_corpo.md`, `src/main.rs`.
Claim IDs or none: see Route ID.
Mismatch marker or none: documents describe a model loop beyond the current shipped provider.
Gap/limit: no accepted ampliative product, formulated criticism, integration or iterative improvement established by these texts alone.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-file-lossless](#epi-clm-file-lossless) | see record | SRC-1: `README.md`; doctrine/design | Explicit bounded byte-lossless read contract | [RT-RTE-file-exchange](runtime.md#rt-rte-file-exchange), [EPI-RTE-file-check](#epi-rte-file-check), [EPI-RTE-file-disposition](#epi-rte-file-disposition) | None | Source protocol construction, no deployed transport/file equality experiment | UTF-8-valid text or lossless blob encoding; oversized input refused | Not provenance authentication, concurrent snapshot consistency or semantic truth. |
| [EPI-CLM-memory-provenance](#epi-clm-memory-provenance) | see record | SRC-1: `docs/playground_memory_architecture.md`; doctrine/design | Detailed time-overlap retrieval and hierarchy | None established for current provider | None | Temporal coincidence does not identify actual source use; future imports can join association | Documented memory design and requested consolidation | Current implementation attribution and semantic provenance unestablished. |
| [EPI-CLM-shell-causality](#epi-clm-shell-causality) | see record | SRC-1: `docs/playground_event_model.md`; doctrine/design | Sequential model-command-result loop described | [RT-RTE-sandbox-exec](runtime.md#rt-rte-sandbox-exec), [EPI-RTE-result-render](#epi-rte-result-render) implement only provider transport portion | None | Arbitrary shell effects/external state need not be repeatable; concurrent jobs and lossy bounded delivery differ from complete deterministic logs | Shipped provider supplies execution feedback, client selects continuation | No shipped cognition loop or deterministic replay proof. |
| [RT-CLM-persistent-sandbox](runtime.md#rt-clm-persistent-sandbox) | see record | SRC-1: `README.md`; doctrine/design | Explicit handle/storage distinction | [RT-RTE-tenant-provision](runtime.md#rt-rte-tenant-provision), [RT-RTE-sandbox-exec](runtime.md#rt-rte-sandbox-exec) | None; [EPI-RTE-smoke-check](#epi-rte-smoke-check) is test implementation only | Selected close/reopen fixture would test persistence, not arbitrary data correctness | Retention across handle release is wired | Retained text is not accepted knowledge. |

## Bounded conclusion

Playground's file protocol acquires caller/file content with bounded encoding checks. It preserves delivered bytes through valid UTF-8 or base64 rather than endorsing their assertions; initial source warrant remains unknown. Writes and arbitrary commands can retain content for later consumers without a semantic acceptance criterion. The file success predicate licenses an operational result for one file call, not an accepted ampliative claim. See [RT-RTE-file-exchange](runtime.md#rt-rte-file-exchange), [EPI-RTE-file-check](#epi-rte-file-check) and [EPI-RTE-file-disposition](#epi-rte-file-disposition).

Execution status and output are evidence candidates for the external client. Lossy decoding, bounded eviction and polling determine the evidence actually delivered. Retained output is not an integrated theory; cleanup fail-stop, credential checks and worker mapping enforce operational authority with no answer oracle. A worker timeout explicitly leaves outcome unknown rather than asserting failure or safe replay. See [EPI-RTE-result-render](#epi-rte-result-render), [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs) and [RT-RTE-worker-forward](runtime.md#rt-rte-worker-forward).

Ancillary routes have distinct licenses. LE interval migration is non-ampliative encoding preservation conditional on correctly typed premises; retention adds mapped facts, not acceptance. Telemetry sums/counts derive conditional propositions over selected decoded measurements, not verified measurements or causal explanations. Link rewriting may preserve or alter referents; external resolution is required to decide. Smoke assertions check narrow deployment outcomes and control the test script, with no observed result or automatic product admission consumer. See [EPI-RTE-timestamp-reshape](#epi-rte-timestamp-reshape), [EPI-RTE-timestamp-retain](#epi-rte-timestamp-retain), [EPI-RTE-telemetry-report](#epi-rte-telemetry-report), [EPI-RTE-link-rewrite](#epi-rte-link-rewrite) and [EPI-RTE-smoke-check](#epi-rte-smoke-check).

The inspected provider routes do not establish production, evidence-consuming acceptance and lifecycle integration of an ampliative truth claim. This is a scoped result, not a complete negative across uninspected external workers, arbitrary command programs or remaining repository checks. The strongest contrary witnesses are the documented memory loop and shipped migration/telemetry/check scripts; they prevent collapsing the system to mere byte transport, but do not supply a semantic acceptance loop. Temporal overlap is a retrieval association, not demonstrated derivation lineage. See [EPI-CLM-memory-provenance](#epi-clm-memory-provenance) and [EPI-CLM-shell-causality](#epi-clm-shell-causality).

Distributed-parametric model state is external and uninspected: no parameter-change, exact-version or mutable-endpoint conclusion is licensed. Prompt-authored self-directed conduct is a request, not proven autonomy or reflection. No inspected route supplies formulated content-directed criticism retained for a next theory round; direct operational policy changes (credentials, mapping, bundles) are distinct from such criticism. Learning benefit and exercised self-improvement remain unestablished independently of persistence and installed capability. These limitations follow the supplied runtime boundary and the specific doctrine/route records, not a single system-wide score.

## Shared records

### Operative objects

#### EPI-OBJ-file-payload
Label: File payload

Material content carried by [RT-RTE-file-exchange](runtime.md#rt-rte-file-exchange), not a duplicate of the route. Representational form: arbitrary natural-language or symbolic bytes, encoded as UTF-8/base64 in symbolic JSON. Substrate: caller/provider buffers and sandbox files. Individual truth-apt content and original provenance not determinable without an instance. SRC-1 implementation: `src/mcp.rs`.

> (Some(value), None) => value
>     .as_str()
>     .ok_or_else(|| anyhow!("write 'text' payload must be a string"))?
>     .as_bytes()
>     .to_vec(),
> --- `src/mcp.rs`

#### EPI-OBJ-exec-result
Label: ExecResult output and status

Material feedback carried by [RT-RTE-sandbox-exec](runtime.md#rt-rte-sandbox-exec) and [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs), rather than a second job manager. Form: arbitrary output text/bytes and symbolic status. Substrate: in-memory output ring/terminal structures; later persistence by client is uninspected. SRC-1 implementation: `src/jobs.rs`.

> Ok(result) => JobTerminal::Exited {
>     exit_code: result.exit_code,
>     error: result.error,
> },
> --- `src/jobs.rs`

#### EPI-OBJ-timestamp-tribles
Label: Timestamp tribles

Symbolic entity/attribute/value records read from pile branches and accumulated in TribleSet; stored in an external pile via repository API. No counterpart after comparison with supplied runtime records: this ancillary migration content differs from provider registry/jobs and bundle sources. SRC-1 implementation: `scripts/migrate_timestamps.rs`.

> let e = &trible.data[0..16];
> let a = &trible.data[16..32];
> let v = &trible.data[32..64];
> --- `scripts/migrate_timestamps.rs`

#### EPI-OBJ-wiki-fragments
Label: Wiki fragments

Exported arbitrary natural-language/symbolic fragment strings, including wiki/files links; shell variables/temp files mediate external pile reads/edits. No counterpart after comparison with supplied runtime objects; provider file exchange does not identify these external fragment entities. SRC-1 implementation: `scripts/rewrite-links.sh`.

> # Export content
> original=$(eval "$WIKI" export "$frag_id" 2>/dev/null) || continue
> --- `scripts/rewrite-links.sh`

#### EPI-OBJ-telemetry-spans
Label: Telemetry spans

Symbolic ID/name/duration records from telemetry pile, vectors and name aggregates in script process memory. No counterpart after comparison with supplied runtime job records: this script reads an independent fixed telemetry branch, not JobManager's output ring. SRC-1 implementation: `scripts/view_telemetry.rs`.

> let mut pile = Pile::<Blake3>::open("./telemetry.pile").unwrap();
> --- `scripts/view_telemetry.rs`

### Routes

#### EPI-RTE-file-check
Label: File protocol checks
Part of: [RT-RTE-file-exchange](runtime.md#rt-rte-file-exchange)

Endpoints: file arguments/backend result → parser/completion predicate → file handler. Owner: fixed Rust code; target domain is valid exclusive payload, byte ceiling and reported command completion. Parser before execution; completion predicate after. No answer oracle; caller proposes content (human versus computational authorship unresolved), software decides/vetoes protocol validity. Operating mode: open file request. Semantic truth is not evaluated. SRC-1 implementation: `src/mcp.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: valid bytes or predicate success/error.
- Later read-back: inapplicable — predicate is not separately retained.
- Delegated visibility: backend receives admitted bytes; handler receives execution result.
- Selection predicate: exactly one valid payload within ceiling; exit zero, no error and not cancelled for completion.
- Invalidation or expiry: inapplicable — checks are per call.
- Activation or effect: failure interrupts file call; actual operation unobserved.
- Evidence limits: does not inspect truth, compare post-write bytes or undo partial writes.

> if result.exit_code == Some(0) && result.error.is_none() && !result.cancelled {
>     return Ok(());
> }
> --- `src/mcp.rs`

> if bytes.len() > MAX_FILE_BYTES {
>     return Err(anyhow!(
>         "write payload is {} bytes; limit is {} bytes",
>         bytes.len(),
>         MAX_FILE_BYTES
>     ));
> }
> --- `src/mcp.rs`

#### EPI-RTE-file-disposition
Label: File call disposition
Part of: [RT-RTE-file-exchange](runtime.md#rt-rte-file-exchange)

Endpoints: check result → file handler → ordinary MCP result or error. Owner: provider dispatch. Distinct from check: consumes its result and chooses continuation/return class. Caller proposes target/content; software vetoes invalid payload or failure; no human per-content gate and no answer oracle. Mode: open request; guidance is parser and file protocol. Successful writes persist content; rejected post-execution calls may leave partial data, with caller recovery and no automatic rollback. SRC-1 implementation: `src/mcp.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: normal read/write result on protocol success or `isError` failure.
- Later read-back: written file content, not an acceptance receipt, can reach later file/exec calls.
- Delegated visibility: admitted file command goes to backend; client receives result class.
- Selection predicate: successful parse and file-command predicate; read also refuses over-limit captured bytes.
- Invalidation or expiry: later filesystem mutation can replace admitted bytes.
- Activation or effect: checks constrain admission/return, not substantive knowledge reliance.
- Evidence limits: post-execution rejection cannot promise no mutation; client behavior unobserved.

> ensure_file_command_succeeded("write", &result)?;
> --- `src/mcp.rs`

> Err(e) => DispatchOutcome::Result(tool_err(&format!("{e:#}"))),
> --- `src/mcp.rs`

#### EPI-RTE-result-render
Label: Execution result rendering

Overlaps [RT-RTE-sandbox-exec](runtime.md#rt-rte-sandbox-exec) and [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs), but is not contained in exactly one: a cross-route delivery transformation, not a duplicate execution kernel. Endpoints: selected bytes/status → decoder/renderer → MCP client. Owner: output log and renderer. State effects: output paging plus a final-page observation flag affecting later eviction. SRC-1 implementation: `src/mcp.rs`, `src/jobs.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: synchronous text with stream/error labels and exit suffix; polling JSON contains surviving chunks, cursor/gap/drop metadata and terminal status.
- Later read-back: job polling can replay surviving chunks; synchronous handle forgotten as in supplied route.
- Delegated visibility: caller receives formatted retained output, not necessarily producer's complete byte stream.
- Selection predicate: cursor clamped to surviving range and current tail; page byte cap; synchronous renders surviving ring.
- Invalidation or expiry: ring eviction, terminal TTL and daemon restart as in supplied retained route.
- Activation or effect: transformation changes delivered evidence; downstream semantic reliance unobserved.
- Evidence limits: neither lossy text nor exit zero proves source assertions; marker text can be printed by caller code.

> let stdout = String::from_utf8_lossy(&result.stdout);
> let stderr = String::from_utf8_lossy(&result.stderr);
> --- `src/mcp.rs`

> out.push_str(&format!("\n[exit {}]", result.exit_code.unwrap_or(-1)));
> --- `src/mcp.rs`

> // Terminal publication sealed the output sink, so this snapshot
> // owns the last page. This records server-side observation, not a
> // network delivery acknowledgement: callers must retain returned
> // pages before submitting work that may recycle a completed id.
> self.terminal_observed.store(true, Ordering::Release);
> --- `src/jobs.rs`

Concrete implementation deduction, not target execution: valid UTF-8 stdout `claim\n`, empty stderr/no error and exit 0 become `claim\n\n[exit 0]`. A caller can print `2+2=5` and exit 0; the renderer preserves the false assertion alongside a genuine process-success report. For malformed UTF-8, replacement decoding prevents byte identity; dropped prefixes produce the error below rather than reconstructing evidence.

> let suffix = "earliest output was evicted from the bounded job log";
> result.error = Some(match result.error {
>     Some(error) => format!("{error}; {suffix}"),
>     None => suffix.to_string(),
> });
> --- `src/jobs.rs`

#### EPI-RTE-timestamp-reshape
Label: Timestamp encoding migration

Endpoints: selected old-attribute tribles → integer/ISO conversion → proposed additions. Owner: manual script, fixed mapping and iteration. No counterpart after comparison with supplied runtime routes; not the provider's bundle fingerprint operation. SRC-1 implementation: `scripts/migrate_timestamps.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: new encoded tribles accumulated and per-branch counts printed.
- Later read-back: inapplicable — this transformation produces additions; separate retention route writes them.
- Delegated visibility: external parser receives ISO text; repository checkout supplies records.
- Selection predicate: recognized old attribute IDs; absent matching new record; parseable ISO where applicable.
- Invalidation or expiry: inapplicable — one conversion pass over checkout; source truth is not invalidated.
- Activation or effect: encoding/domain-specific new attribute facts prepared.
- Evidence limits: external hifitime parser interpretation uninspected; no dataset accuracy check or observed conversion.

> let lower = i128::from_le_bytes(le_value[0..16].try_into().unwrap());
> let upper = i128::from_le_bytes(le_value[16..32].try_into().unwrap());
> let mut obe = [0u8; 32];
> obe[0..16].copy_from_slice(&((lower as u128) ^ SIGN_BIT).to_be_bytes());
> obe[16..32].copy_from_slice(&((upper as u128) ^ SIGN_BIT).to_be_bytes());
> obe
> --- `scripts/migrate_timestamps.rs`

Concrete deduction: an LE interval whose endpoints both encode signed integer zero becomes two big-endian 16-byte words beginning `0x80` followed by fifteen zero bytes, preserving zero under the specified sign-bit-biased encoding. The entity remains unchanged and the attribute follows the migration map. This proves encoding behavior, not that a real event occurred at that timestamp.

> let s = std::str::from_utf8(v).unwrap_or("").trim_end_matches('\0');
> if s.is_empty() {
>     continue;
> }
> --- `scripts/migrate_timestamps.rs`

> eprintln!("    warning: failed to parse compass timestamp: {s:?}");
> --- `scripts/migrate_timestamps.rs`

#### EPI-RTE-timestamp-retain
Label: Timestamp migration commit

Endpoints: proposed additions → workspace commit/push → pile branch. Owner: script/software, operator starts and can choose dry-run. No counterpart after comparison with supplied runtime routes; retained branch additions are not provider file replacement. Trigger: nonempty migration set outside dry-run. Guidance: hard-coded migration attribute maps; no answer oracle or semantic approval. Software decides write eligibility and propagates push errors; no automatic rollback established. Mode: administrative migration, not improvement experiment. SRC-1 implementation: `scripts/migrate_timestamps.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: committed message or propagated push error.
- Later read-back: external branch readers can access additions if storage commits succeed; specific consumers uninspected.
- Delegated visibility: repository API receives new fact set and commit message.
- Selection predicate: total additions positive and dry_run false.
- Invalidation or expiry: no deletion/expiry of old timestamp facts implemented by this script.
- Activation or effect: persistent append requested; actual write unobserved.
- Evidence limits: storage implementation outside frozen source; retention neither acceptance nor observed lifecycle integration.

> if total > 0 && !cli.dry_run {
>     ws.commit(change, "migrate timestamps to NsTAIInterval");
>     repo.push(&mut ws)
>         .map_err(|e| anyhow::anyhow!("push branch {branch_name}: {e:?}"))?;
>     println!("    committed.");
> }
> --- `scripts/migrate_timestamps.rs`

#### EPI-RTE-link-rewrite
Label: Wiki link rewrite wrapper

Endpoints: external fragment export → prefix screening → external `fix-truncated` → changed-text edit. Owner: operator-launched shell script plus opaque wiki resolver. No counterpart after comparison with supplied runtime routes: fragment maintenance is not provider dispatch or bundle building. Trigger: recognized short link prefixes. Software calls resolver, skips error, collects ambiguity reports and edits changed output; operator receives ambiguity list for manual review, not a required pre-edit approval gate. Guidance: full-ID link policy. Mode: batch maintenance; answer oracle uninspected — external resolver may compare candidates, but no reference truth supplied here. No semantic rollback implemented. SRC-1 implementation: `scripts/rewrite-links.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: counts, errors and ambiguity list.
- Later read-back: external wiki edits can affect subsequent fragment exports/queries; those consumers uninspected.
- Delegated visibility: external wiki process receives temporary fragment text and target fragment ID.
- Selection predicate: short wiki/files link patterns and changed returned text; resolver error skips edit.
- Invalidation or expiry: external edit version/recovery semantics uninspected.
- Activation or effect: wrapper requests edit; correctness and actual operation unobserved.
- Evidence limits: resolver unavailable; comments promise ambiguous prefixes unchanged but wrapper itself does not enforce that by content comparison.

> fixed=$(eval "$WIKI" fix-truncated "@$tmpfile" 2>/tmp/rewrite-stderr.txt) || {
>     echo "  ERROR on $frag_id"
>     SKIPPED=$((SKIPPED + 1))
>     continue
> }
> --- `scripts/rewrite-links.sh`

> if [[ "$original" != "$fixed" ]]; then
>     echo "$fixed" > "$tmpfile"
>     eval "$WIKI" edit "$frag_id" "@$tmpfile" 2>/dev/null
> --- `scripts/rewrite-links.sh`

#### EPI-RTE-telemetry-report
Label: Telemetry duration report

Endpoints: fixed telemetry branch → decoded spans → name groups/sums/counts → ranked stdout. Owner: script. No counterpart after comparison with supplied runtime routes; diagnostics read telemetry, not job output. Form: symbolic data and arithmetic, not model inference. SRC-1 implementation: `scripts/view_telemetry.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: selected top spans and top name aggregates printed.
- Later read-back: inapplicable — report is not retained by script.
- Delegated visibility: operator gets top 30 spans and top 20 groups, not every source fact.
- Selection predicate: kind_span with decodable u128 duration; first resolvable name or ID fallback; duration-descending selection.
- Invalidation or expiry: inapplicable — report reflects one checkout, no persisted report lifecycle.
- Activation or effect: diagnostic output; no wired behavioral adaptation consumer.
- Evidence limits: filtered records and overlapping durations prevent unconditional completeness/wall-time claims; data authenticity unknown.

> let dur: u128 = dur_val.try_from_value().ok()?;
> --- `scripts/view_telemetry.rs`

> for (name, dur) in &spans {
>     let entry = by_name.entry(name.clone()).or_insert((0, 0));
>     entry.0 += dur;
>     entry.1 += 1;
> }
> --- `scripts/view_telemetry.rs`

Concrete deduction: two selected records sharing name `x` with duration values 1,000,000 and 2,000,000 produce count 2, sum 3,000,000 and displayed 3.0ms. This is entailed by the selected records and arithmetic within range, not by proof that those measurements are true or disjoint.

#### EPI-RTE-smoke-check
Label: Deployment smoke assertions

Endpoints: selected network responses/fixture processes → curl/jq/grep/process checks → script continue/abort/pass → operator. Owner: operator-script evaluator. No counterpart after comparison with supplied runtime routes: this explicitly checks the provider, rather than executes a normal client command for an arbitrary task. Target domain: selected auth/MCP/tool/persistence outcomes; optional FreeBSD cancellation with unrelated sentinel contrast. Operator proposes deployment/opts in; software decides assertions and vetoes continuation. Answer oracle: fixture reference outcomes (401, successful protocol, eight tools, known markers, exit zero, same reopened sandbox, dead descendant/live sentinel). Mode: smoke test, not broad curriculum. No production admission or implementation revision automatically consumes result. SRC-1 implementation: `deploy/freebsd/smoke.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: explicit pass message or failure exit.
- Later read-back: inapplicable — temporary responses removed; durable report retention not implemented.
- Delegated visibility: provider receives synthetic requests, process probes receive selected PID/jail targets; operator sees pass/error.
- Selection predicate: configured endpoint/token; optional cancellation requires opt-in FreeBSD/root checks.
- Invalidation or expiry: cleanup trap removes temp files and attempts cancel/close/session deletion; persistent tenant sandbox remains.
- Activation or effect: assertions gate test continuation; no actual check result supplied.
- Evidence limits: narrow fixtures, no observed operation or causal mechanism attribution; cleanup can fail silently.

> [ "$BOX" = "$OLD_BOX" ] || die "reopened tenant returned a different sandbox id"
> --- `deploy/freebsd/smoke.sh`

> if jexec "$BOX" /bin/sh -c \
>     "test -s '$DESCENDANT_PID_FILE' && kill -0 \"\$(cat '$DESCENDANT_PID_FILE')\"" 2>/dev/null; then
>     die "detached TERM-ignoring descendant survived job_cancel"
> fi
> jexec "$BOX" /bin/sh -c \
>     "test -s '$SENTINEL_PID_FILE' && kill -0 \"\$(cat '$SENTINEL_PID_FILE')\"" || \
>     die "unrelated jail sentinel died during job_cancel"
> --- `deploy/freebsd/smoke.sh`

### Claims

#### EPI-CLM-file-lossless
Label: Lossless bounded file read

Claimed operation: README promises up to 3 MiB file read without byte loss and MIME-dependent representation. Distinct from supplied [RT-CLM-persistent-sandbox](runtime.md#rt-clm-persistent-sandbox): this claims encoding fidelity, not lifetime. Implementation comparison uses [RT-RTE-file-exchange](runtime.md#rt-rte-file-exchange) plus its check/disposition parts. SRC-1 doctrine/design: `README.md`; implementation: `src/mcp.rs`.

> - `read` — read up to 3 MiB from a sandbox file without byte loss; textual
>   files are returned as text, images as MCP image content, and other binary
>   media as MIME-labelled embedded resources.
> --- `README.md`

> // A textual filename does not make malformed bytes safe to decode.
> // Fall back to a blob so the read remains lossless.
> --- `src/mcp.rs`

#### EPI-CLM-memory-provenance
Label: Memory temporal provenance

Claimed operation: implemented hierarchical summaries and provenance recovered by temporal overlap, including future data. No counterpart after comparison with supplied runtime claims: provider persistence does not identify this external summary/context algorithm. Doctrine only within current provider boundary. Time association cannot establish actual input lineage or summary acceptance. SRC-1 doctrine/design: `docs/playground_memory_architecture.md`.

> This document describes the memory system as currently implemented. The system
> provides manually curated, hierarchical summaries of past interactions that the
> model uses as long-term context.
> --- `docs/playground_memory_architecture.md`

> returns every cognition exec result whose `finished_at` and every archive
> message whose `created_at` falls within the chunk's `[start_at, end_at]`
> interval, chronologically ordered.
> --- `docs/playground_memory_architecture.md`

> - **Chunks can be written before the data lands.** A reflective summary
>   written today against a not-yet-imported chatgpt-data-dump becomes
>   automatically associated with that data the moment it lands on the
>   archive branch, because the time-range query catches it.
> --- `docs/playground_memory_architecture.md`

Prompts request episode consolidation, but neither prompt loading nor reliable execution was established:

> - When context pressure builds (breath shows high fill %). Consolidate the oldest moment events forward into memories that cover coherent episodes.
> --- `prompts/system_prompt.md`

#### EPI-CLM-shell-causality
Label: Shell causality and replay

Claimed operation: one side-effecting command per model turn yields deterministic/replayable log and concrete causal grounding. Distinct from supplied [RT-CLM-persistent-sandbox](runtime.md#rt-clm-persistent-sandbox); overlaps execution routes only at transport portion. Current main dispatch contains provider/account/invite/cleanup, not a cognition worker; command output and status alone cannot prove repeatable side effects or model-grounding behavior. SRC-1 doctrine/design: `docs/playground_event_model.md`; implementation contrast: `src/main.rs`.

> The core invariant: **one side-effecting command per turn**. The model emits a
> command, the shell executes it, and the output becomes the next observation.
> This sequential discipline keeps the interaction log deterministic and
> replayable.
> --- `docs/playground_event_model.md`

> CommandMode::Mcp(args) => run_mcp(args),
> #[cfg(feature = "mcp-http")]
> CommandMode::McpHttp(args) => run_mcp_http(args),
> --- `src/main.rs`

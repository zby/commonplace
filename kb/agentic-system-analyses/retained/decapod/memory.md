---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Decapod memory: repository knowledge and governance, lossless originals with lossy summaries, requested context delivery and opaque internalization artifacts."
run-id: AAS-2026-10-14-decapod-c44705119841-01
source-identity: https://github.com/DecapodLabs/decapod
reviewed-boundary: "067b8f55071e13dd103779998168b4c9ffd31a79"
---

# Decapod memory report

## Boundary and evidence

Decapod retains work outside ephemeral CLI processes. This member includes knowledge, federation decisions, trajectories and Jev history, living-spec context, archive replacement and restoration, LCM originals and summaries, aptitude preferences/prompts/observations, feedback proposals, portable context bundles and internalization artifacts. Sessions, tasks, checkpoints and readiness are included as coordination or acceptance memory, not treated as interchangeable with knowledge. Static embedded constitution text supplies working context but is not material accumulated through use. The whole-system boundary remains that of [boundary](boundary.md#boundary-and-evidence); inspection depth is narrower than inclusion.

All direct findings below use SRC-1 at `067b8f55071e13dd103779998168b4c9ffd31a79`. Added reads supply implementation evidence only, including source comments as attributed design. No target execution, model call or test was performed. Supplied runtime findings are distinguished from direct reads. External host conversations, model parameters, remote storage and configured internalizer executables are outside acquired implementation evidence. They prevent claims about actual window replacement, adapter inference activation, provider internals and operational improvement.

### Coverage inventory

| Entry point or operation | Source paths and inspection basis | Records or unresolved fact and conclusion prevented |
| --- | --- | --- |
| `data knowledge add/search/promote`, RPC `store.upsert/query` knowledge | Direct: `src/decapod/lib.rs`, `src/decapod/plugins/knowledge.rs`; command definitions searched in `src/decapod/cli.rs` | [MEM-OBJ-knowledge-entry](#mem-obj-knowledge-entry), [MEM-RTE-knowledge-store](#mem-rte-knowledge-store), [MEM-RTE-promotion-lifecycle](#mem-rte-promotion-lifecycle). CLI/RPC do not expose all schema-advertised lifecycle options. |
| Knowledge feedback/decay/conflict APIs | Direct complete `src/decapod/plugins/knowledge.rs`; caller search across `src/` | [MEM-RTE-promotion-lifecycle](#mem-rte-promotion-lifecycle). Storage/maintenance capability, not established scheduled decay or feedback-driven ranking. |
| Successful task handoff | Direct bounded `src/decapod/core/todo.rs` handoff aftermath | [MEM-RTE-handoff-memory](#mem-rte-handoff-memory). Automatic trace-derived knowledge has a later search route; recipient automatic consumption and full reconciliation recovery uninspected. |
| `data context audit/pack/restore`, archive list/verify | Direct complete `src/decapod/plugins/context.rs`, `src/decapod/plugins/archive.rs`, dispatch in `src/decapod/lib.rs` | [MEM-OBJ-archive-entry](#mem-obj-archive-entry), [MEM-RTE-archive-context](#mem-rte-archive-context). File replacement is not direct host-window eviction. |
| `context lcm ingest/list/show/summarize/summary/rebuild` | Direct operative ranges and complete CLI dispatcher in `src/decapod/plugins/lcm.rs`; group dispatch in `src/decapod/lib.rs` searched | [MEM-OBJ-lcm-event](#mem-obj-lcm-event), [MEM-OBJ-summary-entry](#mem-obj-summary-entry), [MEM-RTE-lcm-summary](#mem-rte-lcm-summary). No automatic inference injection established. |
| `context internalize create/attach/detach/inspect`, validation gate | Direct `src/decapod/plugins/internalize.rs` profile, producer, inspector, mount lifecycle; `src/decapod/core/validate.rs` artifact/lease gate; dispatch searched | [MEM-OBJ-internalization-manifest](#mem-obj-internalization-manifest), [MEM-OBJ-adapter-payload](#mem-obj-adapter-payload), [MEM-RTE-internalization-lease](#mem-rte-internalization-lease). Encoding of external adapter and actual inference loader unresolved. |
| `data aptitude` preferences, observations, prompt/remind/consolidate; public prompt-add API | Direct operative functions and complete command match in `src/decapod/plugins/aptitude.rs`; caller search in `src/` | [MEM-OBJ-preference](#mem-obj-preference), [MEM-OBJ-agent-prompt](#mem-obj-agent-prompt), [MEM-OBJ-observation](#mem-obj-observation), [MEM-RTE-aptitude-reminders](#mem-rte-aptitude-reminders). Prompt initialization authority unresolved; known later selection is not suppressed. |
| `data federation`, RPC decisions | Direct node add/edit/supersede/status and `src/decapod/plugins/federation_ext.rs` list; direct RPC handlers in `src/decapod/lib.rs` | [MEM-OBJ-federation-node](#mem-obj-federation-node), [MEM-RTE-decision-memory](#mem-rte-decision-memory). RPC decision upsert rejects invalid fixed provenance before persistence; valid library writes and independent RPC reads remain supported. Full edge traversal/search/import/rebuild and typed decision-tree producer remain available but uninspected; exhaustive graph curation not established. |
| `decide` sessions, questions and decisions | Dispatch and function inventory searched in `src/decapod/lib.rs`, `src/decapod/plugins/decide.rs` | Included alternative admission surface. Question/option validation, rationale retention, session progression and federation projection not traced; no complete decision-memory producer account follows. |
| Trajectory record/get, assurance observation, governance validation | Direct `src/decapod/core/trajectory.rs` load/write/record, complete Jev append/reset in `src/decapod/core/jev_history.rs`, durable-context assembly in `src/decapod/core/assurance.rs`; supplied runtime validation/publish | [MEM-OBJ-trajectory-artifact](#mem-obj-trajectory-artifact), [MEM-OBJ-jev-ledger](#mem-obj-jev-ledger), [MEM-RTE-governance-reload](#mem-rte-governance-reload), [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe). Full plans, claims and custody/checkpoint transformations uninspected; semantic criticism not inferred. |
| Context resolve, local specs, constitution bindings | Direct local-spec projection in `src/decapod/core/project_specs.rs`; supplied `src/decapod/core/docs.rs` and RPC selection findings | [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve), annotation below. Full override merge, spec initialization/healing and binding configuration admission not directly retraced. Prevents exhaustive project-authority lineage claim. |
| Capsule query, bundle export/import | Direct `src/decapod/core/context_capsule.rs`, complete `src/decapod/core/context_bundle.rs`, RPC bundle handlers in `src/decapod/lib.rs` | [MEM-OBJ-portable-context-bundle](#mem-obj-portable-context-bundle), [MEM-RTE-bundle-transfer](#mem-rte-bundle-transfer). Capsule-policy configuration was not traced; effective-policy limit supported through caller, not complete policy admission. |
| `govern feedback add/propose` | Direct complete `src/decapod/plugins/feedback.rs`; direct `GovernCommand::Feedback` dispatcher in `src/decapod/lib.rs` and subcommands in `src/decapod/cli.rs` | [MEM-OBJ-feedback-entry](#mem-obj-feedback-entry), [MEM-RTE-feedback-proposal](#mem-rte-feedback-proposal). Shipped commands write/reload/print feedback and proposal; actual preference adoption uninspected. |
| `auto reflex`, cron/heartbeat/watcher/workflow, eval/health | CLI/plugin registry and function inventory searched in `src/decapod/cli.rs`, `src/decapod/lib.rs`, `src/decapod/plugins/mod.rs`, `src/decapod/plugins/reflex.rs` | Included operative alternatives. Reflex trigger/action configuration, scheduled maintenance, evaluator retention and their later consumers are available but not traced. Prevents exhaustive executable-memory and automatic-curation conclusions. |
| RPC operation traces, sessions, tasks, workspace custody, receipts and accepted executor | Supplied runtime; bounded task-handoff read only | [RT-OBJ-agent-session](runtime.md#rt-obj-agent-session), [RT-RTE-workspace-ensure](runtime.md#rt-rte-workspace-ensure), [RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate). Raw RPC trace later consumers and complete coordination cleanup not traced; no derived-learning claim from logging. |
| Shipped agent contracts, build/CI/release evaluators and hooks | Supplied boundary/runtime doctrine and driver coverage; direct complete `src/decapod/hooks/commit-msg.sh` | [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery), [RT-BAP-readiness-gates](runtime.md#rt-bap-readiness-gates). Commit hook checks subject syntax, not memory synthesis. Full driver-generated evidence and external host activation uninspected. |

The inventory covers included alternatives and explicitly retains their gaps; it does not assert full loop inspection for every plugin. Source searches checked CLI dispatch, registered schemas, the shipped commit hook, library functions and source callers. Search hits establish locations, not deployed operation.

## Core ideas

1. **Requested delivery dominates inspected agent memory routes.** Knowledge search, LCM summary/show, archive restore, aptitude reminders and bundle import return material to the caller. Persistence and printing establish later accessibility, not automatic model-window inclusion or behavioral adoption. The supplied context route is likewise on-demand ([MEM-RTE-knowledge-store](#mem-rte-knowledge-store), [MEM-RTE-lcm-summary](#mem-rte-lcm-summary), [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery)).
2. **Original retention and summary fidelity differ.** A successful noncolliding archive pack copies a complete file and replaces its working copy with caller-authored summary plus pointer. LCM derives a deterministic chronological prefix, capped at 64 KiB, with hashes of selected originals. Neither mechanism establishes semantic summarization or automatic preservation of reasons in the displayed text ([MEM-RTE-archive-context](#mem-rte-archive-context), [MEM-RTE-lcm-summary](#mem-rte-lcm-summary)).
3. **Text authority and check authority differ.** Knowledge, preferences and spec snippets require interpretation by a host. Governance identities, status flags, hashes and bundle freshness checks cause executable acceptance/rejection at specific consumers. Provenance syntax and approver strings do not authenticate truth or a human's decision ([MEM-RTE-promotion-lifecycle](#mem-rte-promotion-lifecycle), [MEM-BAP-retained-content](#mem-bap-retained-content), [RT-BAP-readiness-gates](runtime.md#rt-bap-readiness-gates)).
4. **“Internalization” is not proof of parameter learning.** The shipped default writes an empty adapter. Custom profiles can produce opaque bytes, but attach writes a lease and logs; no inference loader was identified in the bounded consumer search. The payload's encoding and external model mutability remain unresolved ([MEM-RTE-internalization-lease](#mem-rte-internalization-lease)).
5. **Trace-derived retention has at least one concrete cross-route path.** A successful task handoff formats caller-supplied summary into persistent knowledge and an aptitude observation. Subsequent knowledge search can deliver that result. This is automatic derivation into accessible memory, not demonstrated learning or evidence of automatic recipient ingestion ([MEM-RTE-handoff-memory](#mem-rte-handoff-memory)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-knowledge-entry
Label: Knowledge entry

Source-native identity: `KnowledgeEntry` in the canonical local database under `Store.root`; title/content are natural-language material, while ID, provenance scheme, status, merge lineage, TTL and timestamps are symbolic access/lifecycle metadata. Caller content and provenance are retained together; format validation does not verify a source's truth. CLI/RPC and successful handoff supply entries. Later `search_knowledge` returns active content and provenance by value to the host. Distinct from [RT-OBJ-agent-session](runtime.md#rt-obj-agent-session): retained knowledge, not authentication/custody. No supplied operative-object counterpart after comparison. Evidence: SRC-1, `src/decapod/plugins/knowledge.rs`, `src/decapod/lib.rs`, `src/decapod/core/todo.rs`.

#### MEM-OBJ-archive-entry
Label: Archive entry and original file

Source-native identity: `ArchiveEntry` is symbolic ID/path/content-hash/summary-hash/time in `decapod.db`; original natural-language session file is copied to `memory/archive/<epoch>.md` under the context root. The original working file becomes caller summary plus path and archive ID. These are separate content and access surfaces: the archive index retains hashes, not summary text. Restore consumes the archived file; list consumes only metadata. Seconds-based names and overwriting writes permit two packs in one second to overwrite earlier bytes before index registration, so the index/pointer does not guarantee durable original retention for all packs. No supplied counterpart; distinct from [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve)'s selected doctrine/specs. Evidence: SRC-1, `src/decapod/plugins/archive.rs`, `src/decapod/plugins/context.rs`.

#### MEM-OBJ-lcm-event
Label: LCM original event

Source-native identity: `LcmEvent` containing verbatim caller content, kind, actor, metadata, timestamp and content hash. Natural-language interaction/tool/artifact content is wrapped in symbolic identity and metadata in canonical `events` stream `lcm`; an `originals_index` stores metadata in the same database. Kind labels and actor strings do not authenticate origin. File ingestion can retain a complete UTF-8 file; CLI stdin reads one line. `show_original` returns the first matching hash; summarize consumes selected originals. No supplied counterpart; unlike [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe), it retains originals rather than a provider judgment. Evidence: SRC-1, `src/decapod/plugins/lcm.rs`.

#### MEM-OBJ-summary-entry
Label: LCM summary entry

Source-native identity: `SummaryEntry`, natural-language chronological concatenation/prefix with symbolic scope, timestamp, original hashes, summary hash and rough token estimate in database `summaries`. Derived directly by code from [MEM-OBJ-lcm-event](#mem-obj-lcm-event), not by a summarizing model. CLI summary lookup returns content and all original hashes, enabling separate original retrieval. No supplied counterpart after comparison; it is not the static context selection of [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve). Reasons survive only if present in originals and retained in the prefix; hashes preserve access lineage, not rationale completeness. Evidence: SRC-1, `src/decapod/plugins/lcm.rs`.

#### MEM-OBJ-internalization-manifest
Label: Internalization manifest and mount metadata

Source-native identity: `InternalizationManifest`, symbolic JSON under `.decapod/managed/artifacts/internalizations/<id>/manifest.json`. It records source/model/profile, source and adapter hashes, replay recipe, TTL, provenance and capabilities. Session mount JSON and attach/detach logs are separate symbolic control/access records under the resolved control root's session directory. Metadata describes [MEM-OBJ-adapter-payload](#mem-obj-adapter-payload), not its readable content. Source filename, requested model name and profile are caller/config inputs, not parameter pins. No supplied counterpart; differs from [RT-OBJ-agent-session](runtime.md#rt-obj-agent-session) because it declares artifact leases, not local session credential validity. Evidence: SRC-1, `src/decapod/plugins/internalize.rs`.

#### MEM-OBJ-adapter-payload
Label: Internalization adapter payload

Source-native identity: `adapter.bin` in the manifest's artifact directory. Storage is filesystem bytes. Representational form is unresolved for custom external producers: the filename and `adapter_format` label do not establish symbolic versus distributed-parametric encoding. Builtin `noop` writes an empty file. Lineage is local source file → configured executable or builtin → hashed payload → inspect/attach checks. The known downstream consumer hashes bytes; a model loader and actual parameter changes are uninspected. No exact external model version is established by caller `base_model_id`; external endpoint mutability and training behavior are unknown. No supplied counterpart; [RT-CMP-jev](runtime.md#rt-cmp-jev) is a separate remote observation provider. Evidence: SRC-1, `src/decapod/plugins/internalize.rs`.

#### MEM-OBJ-preference
Label: Aptitude preference

Source-native identity: `Preference` in database `preferences`, indexed by category/key. Value and optional context/source are interpreted text; confidence/access counts/timestamps are symbolic metadata. Caller supplies values; upsert overwrites same category/key, lookup updates access metrics and delete removes a preference. Reminders render selected values with confidence. No supplied counterpart; not [RT-OBJ-agent-session](runtime.md#rt-obj-agent-session). Evidence: SRC-1, `src/decapod/plugins/aptitude.rs`.

#### MEM-OBJ-agent-prompt
Label: Aptitude agent prompt

Source-native identity: `AgentPrompt` in database `agent_prompts`. Natural-language `prompt_text` is distinct from symbolic context, priority, active flag, usage and time. Public add API admits caller text; no source caller of that add function was identified in the bounded `src/` search beyond its declaration. Initialization and actual author remain unresolved, not assumed human. Known prompt/reminder CLI paths later select and print rows. No supplied counterpart; distinct from [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery)'s embedded/spec delivery surface. Evidence: SRC-1, `src/decapod/plugins/aptitude.rs`, dispatch in `src/decapod/lib.rs`.

#### MEM-OBJ-observation
Label: Aptitude observation

Source-native identity: `Observation`, JSON stored in `meta` under aptitude namespace `observation:<id>`. Caller text, category and regex-matched pattern ID are retained with symbolic processed/time fields. Handoff can produce text automatically; explicit observe is another route. Pending displays recent unprocessed content. Pattern matching annotates input; it does not itself admit a new preference. No supplied counterpart; differs from [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe)'s Jev judgment. Evidence: SRC-1, `src/decapod/plugins/aptitude.rs`, `src/decapod/core/todo.rs`.

#### MEM-OBJ-federation-node
Label: Federation decision node

Source-native identity: `FederationNode` in database `nodes`, with source/supersedes relations in `node_edges` and transactional change events. Natural-language title/body/rationale coexist with symbolic type/status/priority/confidence/scope/effective times. Federation library writes with valid sources can retain decision content. RPC decision input formats chosen option and rationale but supplies invalid provenance `rpc:store.upsert`; `add_node` rejects it before database writes. This RPC seam is not a producer of persisted nodes; provenance/enum checks govern library admission. RPC query list returns body and lifecycle fields but sets `sources` and `edges` to `None`; provenance may persist without reaching this consumer. No supplied counterpart; separate from [RT-OBJ-accepted-executor](runtime.md#rt-obj-accepted-executor)'s executable admission authority. Evidence: SRC-1, `src/decapod/plugins/federation.rs`, `src/decapod/plugins/federation_ext.rs`, `src/decapod/lib.rs`.

#### MEM-OBJ-trajectory-artifact
Label: Trajectory artifact

Source-native identity: `TrajectoryArtifact`, active `trajectory` section in `.decapod/governance.json`, with prior committed versions in Git. Symbolic run/task/custody/check/path state wraps natural-language feedback, observations, blockers and assumptions. Caller updates extend arrays, replace named checks and loop-attempt entries, optionally clear blockers and recompute canonical hash. Raw shell/model transcripts are not implied by tool-call names or declared commands. Later assurance and validation inspect this curated declaration. No supplied operative-object counterpart; closely related to [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe)'s durable trajectory input, not a duplicate route. Evidence: SRC-1, `src/decapod/core/trajectory.rs`, `src/decapod/core/assurance.rs`.

#### MEM-OBJ-jev-ledger
Label: Jev observation ledger

Source-native identity: `JevObservationLedger` in governance `jev` section, keyed by trajectory run and observation IDs. Typed numerical observation/no-observation plus operation, normalized paths, redacted diff summary and sequence are symbolic evidence with optional natural-language context. Results originate from assurance/provider, not learned parameters. New trajectory removes the prior active section; committed history remains accessible through Git. Loader/reset/append and validation consume ledger structure; not established as an input to the next Jev assessment. No supplied object counterpart; output evidence of [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe). Evidence: SRC-1, `src/decapod/core/jev_history.rs`, `src/decapod/core/assurance.rs`, `src/decapod/core/validate.rs`.

> //! The ledger is a repository artifact, not a policy input. It groups every
> //! Jev result produced during the active trajectory run so Git can preserve
> //! the evidence with the PR. A new trajectory run replaces the active ledger;
> //! prior committed ledgers remain recoverable through Git history.
> --- `src/decapod/core/jev_history.rs`

#### MEM-OBJ-portable-context-bundle
Label: Portable context bundle

Source-native identity: `PortableContextBundle`, JSON at `.decapod/managed/context/bundles/<bundle_hash>.json`, plus persisted capsule. Natural-language snippet text, uncertainty and constraints coexist with symbolic source references, policy binding, input hashes, capabilities, environment and optional workunit. Built from selected embedded/merged docs and configured project identity, not automatically extracted trace memory. Later import reads and validates persisted bytes before returning them. No supplied counterpart; separate portable artifact alongside [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve)'s immediate capsule. Evidence: SRC-1, `src/decapod/core/context_bundle.rs`, `src/decapod/core/context_capsule.rs`, `src/decapod/lib.rs`.

#### MEM-OBJ-feedback-entry
Label: Feedback entry

Source-native identity: `FeedbackEntry` in canonical local database `feedback`, despite schema's `feedback.db` storage label. Natural-language source/text/links with symbolic ID/time. Explicit caller supplies content; latest ten are later consumed by proposal formatting. No supplied counterpart; not [MEM-OBJ-observation](#mem-obj-observation)'s regex-annotated aptitude input. Evidence: SRC-1, `src/decapod/plugins/feedback.rs`.

### Routes

#### MEM-RTE-knowledge-store
Label: Knowledge admission and requested retrieval

Endpoints/progression: CLI add or RPC knowledge upsert → initialize database → `add_knowledge` validations → broker write → later CLI search/RPC query → active-row substring selection → serialized entries to host. Code owns format/status admission; caller proposes content. Human authorship or per-content approval is unresolved. Open requests, no expected-answer oracle. Provenance must match a scheme, not pass a source-truth test. Ordinary callers hardcode no merge key, active/persistent status, no expiry, and default relevance search with no temporal options. Library conflict/lifecycle alternatives are separately retained in [MEM-RTE-promotion-lifecycle](#mem-rte-promotion-lifecycle). No supplied route counterpart; supplements [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve), whose store query is a suggestion rather than execution. Evidence: SRC-1, `src/decapod/lib.rs`, `src/decapod/plugins/knowledge.rs`.

- Immediate return: Write ID/action or validation/storage error; query returns serialized content, provenance and lifecycle metadata.
- Later read-back: A later search/query invocation loads accumulated active knowledge and delivers it to the requesting host.
- Delegated visibility: Calling host receives text/JSON; insertion into a model or recipient frame is uninspected.
- Selection predicate: SQL LIKE over title/content/provenance with active status; empty RPC text matches all active rows. No implemented relevance score or result/token budget in this path.
- Invalidation or expiry: Search excludes non-active rows but does not independently filter `expires_ts`; lifecycle mutation must mark expired material stale.
- Activation or effect: Rows persist and query returns content; host reliance or improved action is unobserved.
- Evidence limits: Source syntax is not verified evidence; no host transcript or exhaustive broker/dependency inspection.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let q = format!("%{query}%");
> --- `src/decapod/plugins/knowledge.rs`

#### MEM-RTE-promotion-lifecycle
Label: Knowledge promotion and lifecycle APIs

Endpoints/progression: caller promotion request → require nonempty source ID/evidence/approver/actor/reason → append knowledge event → later `procedural/` add → lookup event and validate procedural target/evidence/approver → admit row. Independent add with merge key can overwrite content/provenance, supersede active row and link replacement, or reject conflict. Decay finds expired active decay/ephemeral rows, optionally marks stale and logs event; subsequent search suppresses them. Retrieval-feedback API appends query/returned/used/outcome/source, but search's inspected ranking uses time, not those outcomes. Distinct from [MEM-RTE-knowledge-store](#mem-rte-knowledge-store)'s shipped basic callers and no supplied counterpart. Evidence: SRC-1, `src/decapod/plugins/knowledge.rs`, `src/decapod/lib.rs`.

Admission: code can reject malformed fields, missing promotion event, invalid enum/time, or requested conflict rejection. Caller supplies replacement and alleged approver; a nonempty `approved_by` is not authenticated human approval. Promotion records evidence references and reason but does not itself rewrite a source entry or prove a substantive procedural derivation. No expected-answer oracle; open caller-controlled writes under fixed validation rules. Merge overwrites prior body without an explicit old-content archive in this function; supersede keeps old row with lineage. Manual replacement/re-add is a capability, not an inspected automatic rollback. Decay's `policy` string is logged, not a selector of alternative pruning algorithms.

- Immediate return: Promotion event, add action/superseded IDs, decay stale IDs/dry-run result, or feedback event ID; errors veto covered writes.
- Later read-back: Procedural admission reads promotion event; search reads active lifecycle state, not promotion reason/evidence body automatically.
- Delegated visibility: API/CLI caller receives structured outputs; no independently pushed host instruction established.
- Selection predicate: Procedural ID prefix; matching active root-scope merge key; expiry cutoff for decay; library temporal search filters creation time and optional recency-decay ranking.
- Invalidation or expiry: Superseded/deprecated/stale rows excluded from ordinary search; persistent entries not selected by decay. Dry run logs without status change.
- Activation or effect: Code updates content/status and event ledger. No outcome-driven semantic update or automatic scheduled decay was identified in `src/` caller search.
- Evidence limits: Public functions/schema advertise more operations than frozen CLI/RPC dispatch exposes. Approver identity/source validity and external library usage remain unestablished.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Promotion and later procedural checks have shipped wiring, while library decay/feedback/conflict variants are afforded capabilities; the aggregate status does not imply all are CLI-accessible.

> fn is_procedural_entry_id(id: &str) -> bool {
>     id.starts_with("procedural/")
> }
> --- `src/decapod/plugins/knowledge.rs`

> "UPDATE knowledge SET status = 'stale', updated_at = ?2 WHERE id = ?1",
> --- `src/decapod/plugins/knowledge.rs`

#### MEM-RTE-handoff-memory
Label: Task handoff memory derivation

Endpoints/progression: successful task-handoff status → code formats from/to/task/caller summary → best-effort active persistent knowledge add with handoff-event provenance → aptitude observation → branch reconciliation attempt. Automatic producer is code; semantic summary author remains caller. No per-content human approval, truth check, expected-answer oracle or model transformation is shown. Admission uses normal knowledge/observation checks; both write errors are discarded. Branch recovery is not fully traced. Distinct from [RT-RTE-workspace-ensure](runtime.md#rt-rte-workspace-ensure)'s custody preparation and [MEM-RTE-knowledge-store](#mem-rte-knowledge-store)'s explicit writes. Evidence: SRC-1, `src/decapod/core/todo.rs`, `src/decapod/plugins/knowledge.rs`, `src/decapod/plugins/aptitude.rs`.

- Immediate return: The inspected aftermath builds reconciliation result; memory write errors do not become handoff failure here.
- Later read-back: Persistent handoff knowledge can be retrieved by later knowledge search; aptitude pending displays the derived observation.
- Delegated visibility: Shared store contains the result; automatic target-agent injection uninspected.
- Selection predicate: Handoff status `ok`; derived content includes task ID, principals and supplied summary.
- Invalidation or expiry: Active persistent knowledge has no expiry here; observation processed state controls pending inclusion.
- Activation or effect: Software derives retained text from handoff input; no demonstrated recipient reliance or capacity improvement.
- Evidence limits: Partial handoff inspection, discarded write failures and untraced reconciliation prevent a reliable-delivery guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let content = format!("Handoff from {from:?} to {to}. Summary: {summary}");
> --- `src/decapod/core/todo.rs`

#### MEM-RTE-archive-context
Label: File context packing and restoration

Endpoints/progression: caller pack(path, summary) → require nonempty summary/readable unarchived file → copy full original into archive → register hashes/path → replace original file with summary/pointer → later caller restore(ID, profile, current files) → resolve archive → count current plus added tokens → return full content if within budget. Caller authors the summary; software performs I/O and budget admission, not semantic compression. Host/human per-content approval unresolved; no oracle. Recovery can require manual cleanup when archive succeeds but original replacement fails. No supplied counterpart; distinct from [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve)'s additive context supply. Evidence: SRC-1, `src/decapod/plugins/context.rs`, `src/decapod/plugins/archive.rs`, `src/decapod/lib.rs`.

- Immediate return: Pack archive path or error; audit token count/warning; restore prints archived content or budget error.
- Later read-back: Later invocation restores original by archive ID; subsequent ordinary file reads can see summary/pointer instead of original.
- Delegated visibility: File and CLI stdout reach host tools; Decapod does not replace existing conversation turns or spawn a reasoning frame.
- Selection predicate: Exact requested archive ID; caller-specified current files and profile, not task relevance. Tokenizer is cl100k_base; defaults main 32000/recovery 64000, configurable through `CONTEXT.json`.
- Invalidation or expiry: Already-archived marker blocks repack; restore budget rejects excess but does not erase original. No archive TTL shown.
- Activation or effect: File replacement is wired working-context reduction only for consumers that reread that file. Restore returns bytes without updating the source file or model window.
- Evidence limits: Budget counts listed files, not actual host context. Seconds-based archive ID/path and overwriting `fs::write` before registration allow same-second packs to overwrite prior bytes even if registration subsequently rejects the ID; reliable recovery/all-packs durability is not guaranteed. No collision run was observed. Restore does not invoke archive content-hash verification; verify checks original hash and nonempty summary hash, not summary meaning/link completeness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let archive_id = format!("arc_{now}");
> let archive_path = archive_dir.join(format!("{now}.md"));
> --- `src/decapod/plugins/context.rs`

> if let Err(e) = fs::write(&archive_path, &content) {
> --- `src/decapod/plugins/context.rs`

> // MOVE-not-TRIM: Replace original with summary + pointer
> --- `src/decapod/plugins/context.rs`

> // Simplified: just confirm the index entry has a non-empty summary_hash recorded.
> --- `src/decapod/plugins/archive.rs`

#### MEM-RTE-lcm-summary
Label: LCM original retention and summary read-back

Endpoints/progression: explicit CLI file/one-line stdin ingestion → append raw content event and content-hash index → requested summarize → select all or latest identified session → chronological concatenation → 64 KiB prefix → store summary/hash/original hashes → later summary/show CLI returns retained result or original. Code derives text without a model; caller controls ingestion and summary trigger, not per-byte summary approval. Kind validation and storage gate admission, not accuracy; no expected-answer oracle. Rebuild can check hashes and skip mismatches, while deleting/repopulating the derived index. It does not revise originals or automatically critique summary meaning. No supplied counterpart; raw-to-derived chain differs from [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve). Evidence: SRC-1, `src/decapod/plugins/lcm.rs`, dispatch in `src/decapod/lib.rs`.

- Immediate return: Ingest hash/event/time/size; summarize hash/count/estimate; summary/show returns retained JSON content; rebuild status/errors.
- Later read-back: A later `summary` reads stored text and original hashes; `show` reopens raw event by content hash.
- Delegated visibility: Requested stdout JSON to host, not automatic injection, eviction or a delegated model frame.
- Selection predicate: All ledger events or most recent nonempty session ID; timestamp-string order; prefix favors early selected material. Summary lookup by hash or newest timestamp.
- Invalidation or expiry: Originals remain available; index rebuildable. New originals require another requested summarize. No summary TTL or automatic stale-summary rejection in lookup.
- Activation or effect: Automatic deterministic transformation after explicit trigger creates durable text and lineage. Later behavioral use is unobserved.
- Evidence limits: “Lossless” applies to original retention, not summary content. Summary links originals directly; recursive summary-of-summary behavior not shown. Byte slicing can fall inside UTF-8 and fail rather than produce safe text; no execution reliability asserted.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Truncate to budget (64KB for summary text)
> let budget = 64 * 1024;
> let summary_text = if concatenated.len() > budget {
>     concatenated[..budget].to_string()
> } else {
>     concatenated
> };
> --- `src/decapod/plugins/lcm.rs`

#### MEM-RTE-aptitude-reminders
Label: Aptitude content and reminder selection

Endpoints/progression: caller preference add/upsert or public prompt add → database → later CLI get/list/prompt/remind selects retained values/text → print. Observation records caller/handoff content and first regex pattern; pending reads unprocessed rows. Proposed preference suggestions from pattern matches are printed, not automatically admitted. Code validates pattern regex; software persists caller values/prompts without semantic approval. Human content control and prompt initialization remain unresolved. Open requests, no expected-answer oracle. Deletion is preference withdrawal; pattern upsert preserves ID/time; consolidation analyzes category/key-prefix groups but execution function does not alter preference content. Distinct from [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve)'s constitution/spec selection. Evidence: SRC-1, `src/decapod/plugins/aptitude.rs`, `src/decapod/lib.rs`.

- Immediate return: IDs, selected preferences/prompts/reminders, observation match suggestions or consolidation messages.
- Later read-back: Later prompt/remind/get commands load accumulated text and metadata; pending reads observations, not derived preferences.
- Delegated visibility: CLI stdout or API return to requesting host; no automatic pre-inference prompt insertion established.
- Selection predicate: Exact category/key lookup; prompts active and context equal caller context or global, priority descending then usage ascending, default limit five; reminders use three prompts and first three category-matching preferences.
- Invalidation or expiry: Preference upsert overwrites same category/key; delete removes it; processed observations leave pending. Active prompt flag governs selection; no TTL demonstrated.
- Activation or effect: Prompt reads increment usage, thereby changing later tie-break selection; preference lookup updates access metrics. Content revision from observations or consolidation is not shown.
- Evidence limits: Usage is access metadata, not evidence of host adoption. Public prompt-add is afforded; known read CLI wiring coexists with unknown actual initialization.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // consolidations table folded away (#1131); retain preference-side analysis only.
> // Previously this only wrote audit rows (no preference mutation).
> let _ = (store, group, target_id);
> Ok(true)
> --- `src/decapod/plugins/aptitude.rs`

#### MEM-RTE-decision-memory
Label: Decision node admission and retrieval

Endpoints/progression: RPC caller title/chosen/rationale → formatted decision body → federation add/type/provenance checks → validation error before persistence because literal source `rpc:store.upsert` fails the anchored provenance regex. Separately, federation library callers supplying valid fields/sources → transactional node/source-edge/event persistence → later RPC query type decision → list to host. The real read capability does not complete the rejected RPC producer chain. Library edit rejects critical or non-active nodes; supersede marks old inactive, links replacement and records caller reason; status transitions persist reasons in events. Caller proposes and chooses content; software vetoes invalid structural changes, not substantive decision errors. No authenticated human approval or answer oracle; open caller requests. No supplied counterpart; not [RT-OBJ-accepted-executor](runtime.md#rt-obj-accepted-executor). Evidence: SRC-1, `src/decapod/lib.rs`, `src/decapod/plugins/federation.rs`, `src/decapod/plugins/federation_ext.rs`.

- Immediate return: RPC decision upsert returns provenance validation error, not Node ID/stored success; valid library add can return a node; RPC query returns decision bodies/status; library errors on prohibited edit/transition.
- Later read-back: RPC query can return decision nodes admitted through other federation writes in later invocations; no retained node results from this rejected RPC upsert.
- Delegated visibility: Calling host receives JSON, without automatic model enforcement.
- Selection predicate: RPC type decision only, newest update first; no requested relevance or active-status filter, result/token limit, source-edge expansion or pagination in inspected branch.
- Invalidation or expiry: Supersession/status changes persist, but RPC list can still return superseded decisions. Consumer must interpret lifecycle fields; no automatic suppression here.
- Activation or effect: Valid federation library writes retain content and audit reasons; RPC upsert's invalid source prevents this effect. Subsequent query exposes stored body but not source/supersedes edges.
- Evidence limits: `wired` describes the implemented rejection, library persistence and RPC list, not successful RPC producer-to-read-back retention. Full federation search/export/rebuild and `decide` producer not traced. Retained event reason is not established as automatically read with RPC list.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let content = format!("Decision: {chosen}\nRationale: {rationale}");
> --- `src/decapod/lib.rs`

> "rpc:store.upsert",
> --- `src/decapod/lib.rs`

> r"^(file:[^#]+(#L\d+(-L\d+)?)?|url:[^ ]+|cmd:[^ ]+|commit:[a-f0-9]+|event:.+)$",
> --- `src/decapod/plugins/federation.rs`

> for src in &sources {
>     validate_provenance(src)?;
> }
> --- `src/decapod/plugins/federation.rs`

> sources: None,
> edges: None,
> --- `src/decapod/plugins/federation_ext.rs`

#### MEM-RTE-governance-reload
Label: Trajectory and Jev retention consumers

Endpoints/progression: caller trajectory update → normalization/canonical hash/loop validation → active governance section replacement → later trajectory get/assurance → validated state-labelled governance text; provider observation → Jev append/redaction/ledger validation → later append/reset and governance validation. Code owns structural admission; caller supplies trajectory claims and provider supplies numerical result. No verified per-content human approval or expected answer is established. Recovery for prior committed versions is Git history, not automatic rollback. Distinct from, and extends persistence of, [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe); generic provider progression remains in runtime. Evidence: SRC-1, `src/decapod/core/trajectory.rs`, `src/decapod/core/jev_history.rs`, `src/decapod/core/assurance.rs`, `src/decapod/core/validate.rs`.

- Immediate return: Canonical trajectory/observation or error; persistence failure becomes no-observation in supplied assurance route.
- Later read-back: Later assurance reloads active trajectory/plan/claims/validation; later record extends current trajectory; validator loads Jev ledger and checks trajectory association.
- Delegated visibility: Jev receives narrowed governance context through runtime provider route; human reviewers can inspect tracked Git evidence. Raw provider HTTP exchange is not retained here.
- Selection predicate: Active governance sections and matching run ID; same-run ledger append, new-run reset; not query-based semantic selection.
- Invalidation or expiry: Active trajectory and Jev sections replaced/reset across runs; committed prior versions require explicit history access. Invalid/missing governance becomes typed state, not silently valid text.
- Activation or effect: Retained trajectory can inform next assurance evaluation; Jev ledger supports custody/validation, not policy approval or established recursive probability feedback.
- Evidence limits: Full checkpoint/evaluator/claims/plan lineage is uninspected. Declared commands and checks are not observed execution; content-directed criticism and better future capacity are not inferred.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> trajectory: Self::validated_artifact_state(
>     trajectory::load_trajectory_cookie(repo_root),
>     repo_root,
>     "trajectory",
> ),
> --- `src/decapod/core/assurance.rs`

#### MEM-RTE-bundle-transfer
Label: Portable context export and import

Endpoints/progression: RPC export(topic/scope/task/limit) → resolve capsule policy → rank scoped fragments, scope-filter/fallback/truncate → construct identity/workunit/uncertainty/constraints → canonical hash/current-input validation → write bundle/capsule → later RPC import(path) → read/validate/rewrite → return bundle. Code selects snippets and gates import; caller supplies topic and optional authored uncertainty/constraints, not per-snippet approval. No content-truth oracle; structural hashes, input fingerprints and capabilities are fixed acceptance references. Open requested transfer. Distinct artifact transfer, not duplicate [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve). Evidence: SRC-1, `src/decapod/core/context_bundle.rs`, `src/decapod/core/context_capsule.rs`, `src/decapod/lib.rs`.

- Immediate return: Bundle and path on export; import status/bundle/path or stale/tampered/identity error.
- Later read-back: Later import reads persisted by-value snippets, identity and caller uncertainty/constraints.
- Delegated visibility: Calling host receives JSON; another compatible repository/process may supply a path. Actual remote transfer and model insertion unobserved.
- Selection predicate: Topic-ranked embedded/merged docs then scope filter, fallback lexically sorted scoped paths if no matches; effective count limit, not total context-token budget. Import exact caller path.
- Invalidation or expiry: Schema/hash checks and current config/spec/repository fingerprint/capabilities/task consistency reject stale/incompatible input. No TTL shown.
- Activation or effect: Export/import persist copies and return selected text; checks impose authority at admission, not instruction obedience at host.
- Evidence limits: Bare capsule writes recompute hash, not the same full receiving-repository bundle validation. Policy configuration lineage and host compatibility beyond encoded checks are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "CONTEXT_BUNDLE_STALE: config/spec inputs differ from the receiving repository"
> --- `src/decapod/core/context_bundle.rs`

#### MEM-RTE-internalization-lease
Label: Internalization artifact and lease lifecycle

Endpoints/progression: CLI create(local source, model, profile, TTL/scopes) → source/binary hashes and request ID → cached manifest or execute profile → hash adapter and persist manifest → inspect/attach → integrity/expiry/replay/tool checks → persist session mount and attach log → detach removes mount and logs. Software owns structural admission; configured external executable determines custom payload. Caller controls source/model/profile; per-content human approval and semantic correctness unresolved. No answer oracle; integrity bytes and profile-declared determinism are acceptance references. Cache hit returns manifest without repeating inspect; attach later checks. Default noop writes empty bytes. Recovery is inspect/recreate/detach, not demonstrated parameter rollback. Distinct from [RT-CMP-jev](runtime.md#rt-cmp-jev)'s provider observation. Evidence: SRC-1, `src/decapod/plugins/internalize.rs`, `src/decapod/core/validate.rs`, dispatch in `src/decapod/lib.rs`.

- Immediate return: Create manifest/hash/cache result; attach lease/capabilities/provenance; inspect status/integrity; detach result or rejection.
- Later read-back: Inspect/attach reload manifest and adapter for integrity; detach reloads mount; validation reads artifact and remaining lease metadata. A later inference consumer of payload bytes is uninspected.
- Delegated visibility: External executable receives source path, base-model name, output directory and params. Calling host receives metadata, not a decoded summary or automatic adapter injection.
- Selection predicate: Caller local source/profile/model/scopes/TTL and exact artifact/session/tool; cached request identity; permitted tool and integrity/expiry checks on attach.
- Invalidation or expiry: Artifact TTL can reject attach; detach removes lease only, leaving payload/history. Validation flags expired lease files still present rather than automatically deleting them.
- Activation or effect: Known attach effect is mount JSON plus attach log. Source label `behavior-changing` does not prove model activation or parameter learning.
- Evidence limits: Custom executable internals/encoding, actual loader and model pin/mutation unknown. Bounded `src/` search found payload-path/mount references in internalize and validator, not inference loading; this is a limit, not a universal absence claim.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if self.executable == "builtin:noop" {
>     crate::core::fs_permissions::write_private(&adapter_file, b"")
>         .map_err(InternalizeError::Io)?;
>     return Ok((adapter_file, self.default_params.clone()));
> }
> --- `src/decapod/plugins/internalize.rs`

> fs::remove_file(&mount_file).map_err(InternalizeError::Io)?;
> --- `src/decapod/plugins/internalize.rs`

#### MEM-RTE-feedback-proposal
Label: Requested feedback proposal

Endpoints/progression: CLI `govern feedback add` initializes database and calls API add source/text/links → persist feedback → later CLI `govern feedback propose` initializes database and calls propose to read newest ten → format evidence and fixed placeholder diff against SYSTEM.md → return non-binding text. Code does not infer a substantive new rule or persist an adopted preference. Caller authors feedback; per-content approval unresolved. Open requests, no expected-answer oracle. Possible duplicate of supplied peer [EPI-RTE-feedback-proposal](epistemic.md#epi-rte-feedback-proposal): same add/propose functions, stored feedback and requested proposal consumer. Unlike [RT-RTE-validate-candidate](runtime.md#rt-rte-validate-candidate), it admits no project change. Evidence: SRC-1, `src/decapod/plugins/feedback.rs`, `src/decapod/lib.rs`, `src/decapod/cli.rs`.

- Immediate return: Feedback ID or proposal string/no-feedback message.
- Later read-back: Later propose reloads accumulated feedback; proposal itself has no persistent write in this function.
- Delegated visibility: Shipped CLI prints feedback ID or proposal to calling host; model-window insertion and adoption consumer uninspected.
- Selection predicate: Latest ten ordered by stored created_at text; no semantic evidence ranking.
- Invalidation or expiry: No feedback expiry or proposal acceptance/withdrawal shown in this inspected module.
- Activation or effect: Retains raw feedback and formats it with a constant proposed-rule placeholder, not established evidence-responsive preference revision.
- Evidence limits: Command wiring establishes requested read-back, not observed host adoption or meaningful theory criticism. Placeholder diff remains non-binding and does not install preferences.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> FeedbackCommand::Propose => {
>     let proposal = feedback::propose_prefs(project_store)?;
>     println!("{proposal}");
> }
> --- `src/decapod/lib.rs`

> "- [Placeholder rule]
> + [New rule derived from feedback]
> ",
> --- `src/decapod/plugins/feedback.rs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-content
Label: Requested retained content guidance

Consumer: external host agent or human. Channels: knowledge/decision query, archive restore, LCM summary/show and aptitude prompt/remind outputs. Force: interpretable retained content; not universal command authority, automatic model activation or a guarantee of compliance. Horizon: later invocations/sessions over accumulated database/files and repeated retrieval. Distinct from [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery)'s static constitution/project-spec delivery; same external consumer class but different retained parts and selectors. Evidence: SRC-1, `src/decapod/lib.rs`, `src/decapod/plugins/lcm.rs`, `src/decapod/plugins/context.rs`, `src/decapod/plugins/aptitude.rs`; supporting passages and routes above.

## Annotations

#### On [RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve)

Read-back content differs from the whole source file: local project specs yield first relevant content-line summaries, with configured product summary/architecture taking precedence over inferred spec snippets. The direct `local_project_specs_context` read supports selective projection, not full living-spec rationale delivery. Storage is authored repository Markdown and config; text is natural-language knowledge, canonical paths/hash/authority fields symbolic metadata. Agent/human semantic authorship is prescribed in supplied runtime; full initialization admission and overrides remain uninspected. These fields supplement the runtime's selector/fragment-budget limits and do not duplicate its route identity. Evidence: SRC-1, `src/decapod/core/project_specs.rs`.

> // Match init's authority ordering: configured project identity wins over
> // inferred snippets. Failure to read it does not authorize task-line inference.
> --- `src/decapod/core/project_specs.rs`

#### On [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe)

Returned provider judgments become [MEM-OBJ-jev-ledger](#mem-obj-jev-ledger) with trajectory lineage, normalized paths and redacted diff, not a raw HTTP transcript. Later append/reset and validation consume them structurally. The inspected durable context supplied to the provider contains plan/claims/trajectory/validation, not the Jev history section; thus retaining observations does not establish feedback into a subsequent model probability. See [MEM-RTE-governance-reload](#mem-rte-governance-reload). Evidence: SRC-1, `src/decapod/core/jev_history.rs`, `src/decapod/core/assurance.rs`.

## Write side

Explicit caller content dominates knowledge, valid federation decision writes, preference, prompt and feedback admission. RPC decision upsert is a rejected proposal rather than admission because its fixed provenance source is invalid. Software validates structures and persistence; no authenticated per-content human approval can be inferred from starting a command or passing an approver string. Knowledge promotion retains a reason/evidence event, but the procedural row's later search receives provenance ID rather than automatic event expansion. Federation supersession keeps reason in an event; the inspected RPC query omits edges/sources, so audit retention and consumer-visible rationale differ ([MEM-RTE-promotion-lifecycle](#mem-rte-promotion-lifecycle), [MEM-RTE-decision-memory](#mem-rte-decision-memory)).

Automatic trace-fed writes include handoff text/observation, LCM chronological derivation after a requested trigger, trajectory normalization/custody updates and provider-result ledger append. Their origins differ: caller handoff summary, supplied originals, caller-authored trajectory updates and numerical provider result. No generic “agent memory learning” inference follows. LCM retains original pointers but its bounded derived text can omit reasons; noncolliding archive pack copies originals but same-second collisions can overwrite them, and caller summary completeness is not checked. Handoff reasons survive only if the caller summary supplies them. The inspected later consumers are search/pending, summary/show/restore, assurance and structural validators respectively ([MEM-RTE-handoff-memory](#mem-rte-handoff-memory), [MEM-RTE-lcm-summary](#mem-rte-lcm-summary), [MEM-RTE-archive-context](#mem-rte-archive-context), [MEM-RTE-governance-reload](#mem-rte-governance-reload)).

Working-context checkpoints have materially different alternatives: archive summary plus pointer, LCM stored summary plus original hashes, persisted capsule/bundle selected snippets, and opaque adapter plus manifest/lease. They are not interchangeable summary representations. The first two originate from retained files/events; capsule export selects doctrine/current repository identity; custom internalization derives opaque bytes from a local file. Default noop supplies no derived content. No target-internal model compaction call was established on these inspected paths ([MEM-RTE-bundle-transfer](#mem-rte-bundle-transfer), [MEM-RTE-internalization-lease](#mem-rte-internalization-lease)).

Maintenance ranges from content overwrite/supersession and status withdrawal to expiry staling, index reconstruction, processed-observation marking, usage metrics and mount deletion. Aptitude consolidation's success output does not establish preference mutation. Feedback proposal's claimed new-rule label is a fixed placeholder, not evidence-directed content revision. Archive verification checks hash existence/content, not meaningful summary fidelity; internalization inspection checks integrity/replay metadata, not task performance. Full eval/health/scheduler transformations remain unresolved in the coverage table, preventing exhaustive cleanup or evaluation-fed memory-update claims.

## Read-back

The operative chains are linked in the route records rather than inferred from storage names:

- Knowledge/handoff → caller substring search → active row content/provenance → host. Library time filtering is optional; expiration is not directly enforced by search.
- Valid federation write → decision node → caller RPC decision list → body/status without edge/source expansion → host. RPC decision upsert instead rejects `rpc:store.upsert` before persistence; it does not feed this chain. Superseded content can still reach this RPC consumer.
- Original session file → caller summary/pointer replacement → subsequent file consumer; explicit restore reopens full archive under a file-based token budget.
- LCM originals → requested chronological prefix → later summary lookup → host; original hash allows separate exact reload. This does not automatically remove old conversation turns.
- Aptitude prompts/preferences → caller context/category selection and small count limits → host reminders; returned usage metadata changes future ordering without establishing adopted behavior.
- Active trajectory → later assurance assembly → narrowed provider input; Jev history → later ledger maintenance/validation, not an established policy input.
- Bundle file → requested import and current-input validation → by-value context to host. Model-window liveness and trust policy remain host responsibilities.
- Internalization artifact → inspect/attach integrity read → symbolic lease; no established inference consumer of opaque bytes.
- CLI feedback add → retained feedback → later CLI propose selects newest ten → printed evidence/placeholder diff → calling host; no installed preference or observed adoption.

No inspected push selector independently supplies retained text to a running model. Handoff is an automatic write, not an unsolicited inference-context delivery. Separate-context frames, conversation trimming and discarded-turn reload are external/uninspected; Git worktrees and optional containers do not establish model-context isolation, as [RT-RTE-workspace-ensure](runtime.md#rt-rte-workspace-ensure) explains. In the stack-frame lens, no inspected Decapod operation allocates/pops a reasoning frame. Archive and bundle pointers identify external material that a later tool may reload, but returned text is by value: neither a live model-window reference nor automatic memory reclamation.

## Integration issues

1. **No supported correction to supplied runtime generic facts.** Direct local-spec projection and governance-output consumers refine, rather than contradict, the supplied context/assurance account. Annotations retain the narrower payload and history roles ([RT-RTE-context-resolve](runtime.md#rt-rte-context-resolve), [RT-RTE-assurance-observe](runtime.md#rt-rte-assurance-observe)).
2. **Feedback declaration may duplicate the supplied peer fragment.** [MEM-RTE-feedback-proposal](#mem-rte-feedback-proposal) and [EPI-RTE-feedback-proposal](epistemic.md#epi-rte-feedback-proposal) describe the same feedback add/propose route. Reconciliation can connect these without treating prefix differences as distinct mechanisms. Other declarations have no identified supplied counterpart. Governance reload overlaps assurance persistence, and retained-content authority shares the external host consumer with runtime context delivery, but the newly declared artifacts/selector paths are distinct. Do not supersede the runtime provider route merely because this report follows its retained result ([MEM-RTE-governance-reload](#mem-rte-governance-reload), [MEM-BAP-retained-content](#mem-bap-retained-content)).
3. **Exposed library operations versus shipped commands.** Knowledge schema lists decay/retrieval feedback/conflict/temporal options that ordinary CLI/RPC do not forward. Scheduled decay and feedback-driven content/ranking remain unestablished; source caller search finds their definitions only. Reconciliation must preserve afforded library capabilities without upgrading them to scheduled host operation ([MEM-RTE-promotion-lifecycle](#mem-rte-promotion-lifecycle)).
4. **Approver authentication and procedure/source binding.** Procedural add checks a recorded event's target/evidence/approver, but not verified human identity or semantic content derivation from source. Event creation accepts a source ID without inspecting that source's content. This prevents claims of human-controlled or evidence-validated procedural admission beyond field checks ([MEM-RTE-promotion-lifecycle](#mem-rte-promotion-lifecycle)).
5. **Opaque adapter and attach semantics.** Full custom payload encoding, actual inference loading, base-model immutable version and parameter mutation are unresolved. Default empty adapter and metadata-only attach are concrete counterexamples to inferring learned behavioral compression from labels. Validation flags stale leases but does not establish inference detachment enforcement ([MEM-OBJ-adapter-payload](#mem-obj-adapter-payload), [MEM-RTE-internalization-lease](#mem-rte-internalization-lease)).
6. **Prompt initialization versus known consumption.** Public prompt-add admits text; bounded caller search does not establish initial authors or approval. Subsequent CLI selection and metric updates are supported and must not be reduced to unknown just because initialization control is unknown ([MEM-OBJ-agent-prompt](#mem-obj-agent-prompt), [MEM-RTE-aptitude-reminders](#mem-rte-aptitude-reminders)).
7. **Summary labels and reason reachability.** LCM's deterministic summary is a capped chronological concatenation, not semantic consolidation; archive pointer summary is caller-authored. LCM originals remain reloadable; archive original reload depends on noncolliding retention. Reasons may not reach the immediate derived consumer. This prevents lossless-summary and rationale-completeness conclusions ([MEM-RTE-lcm-summary](#mem-rte-lcm-summary), [MEM-RTE-archive-context](#mem-rte-archive-context)).
8. **Decision producer rejection and withdrawal/read-back mismatch.** RPC upsert supplies invalid `rpc:store.upsert` provenance and errors before persistence; the former producer-to-read-back assertion is withdrawn. Valid federation library admission and the independent RPC list remain supported (SRC-1, `src/decapod/lib.rs`, `src/decapod/plugins/federation.rs`). Library supersession preserves old node and reason, but RPC query has no active-status filter and omits edges/sources. Thus withdrawal state can reach the host without automatically suppressing old text or exposing reason lineage ([MEM-RTE-decision-memory](#mem-rte-decision-memory)).
9. **Remaining included alternatives.** Typed `decide` producer, full federation graph paths, reflex trigger/action rules, scheduler/eval/health retention, RPC trace consumers, spec/override initialization, full plans/claims/checkpoints and remote drivers remain insufficiently inspected as named in the inventory. In particular, optional worker lesson writes in `src/decapod/core/todo.rs` and health/reflex remediation in `src/decapod/plugins/health.rs` and `src/decapod/plugins/reflex.rs` remain untraced beyond source inventory searches. Withhold exhaustive automatic-curation, trace-origin and evaluator/authority-route conclusions; lesson write success, activation and remediation completion are unestablished. Their admission control, transformations, lineage and later consumers cannot be assigned exhaustive conclusions. These are available-source inspection limits, not absent mechanisms; no invented record IDs are assigned to missing parts.
10. **No observed adoption or improvement.** Every retained-text route lacks target execution evidence. Accessible content and static next-round structural consumers do not establish better future capacity, reliable model activation, content-directed criticism, autonomous theory building or exercised self-improvement. These properties remain independently unestablished, not bundled as a negative system classification.

## Limitations and checks

Source HEAD was directly rechecked and equals the supplied frozen commit. All new source paths belong to SRC-1; no source identity or boundary was changed. Supplied invocation, member types, boundary, complete bounded runtime and record contract were read, including continuation checks. Authoring followed the supplied worker procedure rather than KB authoring skills. Model and effort were reported from Pi environment. Both supplied refusal blockers were rechecked against frozen source and corrected; answers accompany this report. Added correction reads cover federation provenance/add admission, RPC decision upsert, feedback CLI definition/dispatch and complete feedback formatter. Archive naming/write ordering was also rechecked.

Static source inspection supports storage, implemented selectors and covered consumers, not deployment activation or benefit. Known artifacts and routes coexist with the explicit alternative-surface gaps above. No source/tests/examples/providers were executed. Deterministic validation is performed with the supplied isolated `commonplace-run validate-output` command; its final successful result checks form, citations and quotation occurrence, not semantic acceptance or complete loop coverage.

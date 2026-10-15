---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Playground memory surfaces: persistent tenant files and opaque native piles, bounded job replay, maintenance scripts and unwired model-context doctrine."
run-id: AAS-2026-10-14-playground-88ee8a292f9b-01
source-identity: "https://github.com/triblespace/playground"
reviewed-boundary: de28ac8fdda30c7a5c2ee099de089e65a685195f
---

# Playground memory report

## Boundary and evidence

The subject is the shipped sandbox MCP provider and optional native-worker gateway, not the model-shell loop described in its documents. Memory scope includes files that later calls can read or execute, native pile custody and initialization, job-output replay, startup/teardown, and auxiliary maintenance. Shipped memory documents and prompts are included as doctrine/design, not executable context assembly. External Faculties semantics, model context, archive-import execution and actual deployed storage contents remain outside the boundary fixed in [boundary](boundary.md#boundary-and-evidence).

Direct source inspection at SRC-1 added bounded reads of `src/main.rs` dispatch/module declarations, `src/mcp.rs` tool dispatch/file handlers/payload parsing/MIME conversion, `src/jobs.rs` ring/paging/terminal-observation/eviction logic, jail onboarding and profile setup, Lima mount rendering/destruction, both full prompts, full memory architecture/history/event documents, an older operating guide's memory instructions, and the complete three auxiliary scripts. The supplied [runtime account](runtime.md#runtime-account) supplies HTTP authority, worker forwarding, execution capability, bundle construction and wider lifecycle findings. No target, script, service or test was executed. All new source evidence uses the existing SRC-1; comments describing measurements remain reported operation, not supplied observed traces.

| Entry point or operation | Source path and inspection basis | Coverage and limit |
|---|---|---|
| CLI/provider catalogue | Direct: `src/main.rs`, `src/mcp.rs` | Dispatch has provider/admin/cleanup commands and eight sandbox tools; [MEM-ABS-context-loader](#mem-abs-context-loader). No current cognition-loop entry inferred. |
| File acquisition/replacement and later read | Direct: `src/mcp.rs`; supplied lifecycle | [RT-RTE-file-exchange](runtime.md#rt-rte-file-exchange), [MEM-OBJ-workspace-files](#mem-obj-workspace-files). Caller paths, not semantic retrieval. |
| Shell mutation and profile consumption | Direct profile producer; supplied shell consumer: `src/sandbox/jail.rs`, `src/sandbox/lima.rs` | [MEM-OBJ-session-profile](#mem-obj-session-profile), [RT-RTE-sandbox-exec](runtime.md#rt-rte-sandbox-exec). Generic caller's human/model identity unresolved. |
| Job replay, bounds, rejection and cleanup | Direct: `src/jobs.rs`; supplied backend eligibility | [MEM-OBJ-output-log](#mem-obj-output-log), [MEM-OBJ-job-snapshot](#mem-obj-job-snapshot), annotation on [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs). Raw results, not summaries. |
| Jail provision/reuse/reattach/destroy | Direct onboarding/profile; bounded source search of lifecycle and provenance: `src/sandbox/jail.rs`; supplied wider lifecycle | [MEM-OBJ-self-pile](#mem-obj-self-pile), [MEM-OBJ-shared-pile](#mem-obj-shared-pile), [MEM-OBJ-self-key](#mem-obj-self-key), [MEM-RTE-native-onboarding](#mem-rte-native-onboarding). Host piles survive clone destruction. Native admission internals unavailable. |
| Lima provision/read-through/destroy | Direct mount rendering/destruction: `src/sandbox/lima.rs`; supplied wider lifecycle | Same self-pile/key objects; exact-file hardlink views expose live originals. No native semantic initializer established here. |
| Native worker persistent-state access | Supplied: `src/mcp_http/workers.rs`, `deploy/freebsd/playground_faculties` | Annotation on [RT-RTE-worker-forward](runtime.md#rt-rte-worker-forward). Worker receives pile/key/persona, but selected native content and later model consumption are external. |
| Tenant credentials, worker mapping, bundle cache | Supplied: `src/main.rs`, `src/mcp_http.rs`, `src/sandbox/faculties.rs` | [RT-RTE-tenant-provision](runtime.md#rt-rte-tenant-provision), [RT-OBJ-worker-manifest](runtime.md#rt-obj-worker-manifest), [RT-RTE-bundle-build](runtime.md#rt-rte-bundle-build). Access/capability metadata, not recollections or trace-derived knowledge. |
| Timestamp migration and wiki-link rewrite | Direct full reads: `scripts/migrate_timestamps.rs`, `scripts/rewrite-links.sh` | [MEM-RTE-storage-maintenance](#mem-rte-storage-maintenance). Native acceptance and actual later use unresolved. |
| Telemetry readout | Direct full read: `scripts/view_telemetry.rs` | [MEM-RTE-telemetry-display](#mem-rte-telemetry-display). Existing spans → console aggregates; no retained adaptation shown. Trace producer external/uninspected. |
| Summary creation, temporal provenance and automatic cover | Direct: `docs/playground_memory_architecture.md`, `docs/memory_temporal_redesign.md`, `docs/playground_event_model.md`, `prompts/system_prompt.md`, `prompts/system_prompt_corpo.md` | [MEM-CLM-memory-cover](#mem-clm-memory-cover). Documented alternative, not a wired provider route. |
| Legacy lenses/consolidation commands and importer fragments | Direct bounded guide read: `docs/playground.md`; importers excluded by boundary | [MEM-CLM-memory-cover](#mem-clm-memory-cover). Guide disagrees with history/current dispatch; no functioning archive loop attributed. |

## Core ideas

Playground retains operational material for caller-directed use. File read-back is literal path selection. Job replay is sequence selection over bounded process-memory output. Neither is an implemented semantic memory selector or a model summarizer. Pile custody is durable, but opaque native bytes must not be classified from their filename as verified summaries, theories or raw experience. See [MEM-OBJ-self-pile](#mem-obj-self-pile) and [MEM-OBJ-output-log](#mem-obj-output-log).

The three retention horizons differ. Closing a sandbox handle preserves its workspace. Destroying the sandbox removes its clone/disk but leaves the external pile and signer. Restarting the daemon loses jobs, regardless of durable workspace custody. Replaying a terminal job is bounded and lossy at display conversion; preserving a pile does not establish that any native content passes admission or reaches a model. SRC-1: `src/jobs.rs`, `src/sandbox/jail.rs`, `src/sandbox/lima.rs`; [RT-CLM-persistent-sandbox](runtime.md#rt-clm-persistent-sandbox).

The strongest source-native context mechanism is declared rather than wired here: hierarchical temporal summaries take priority over recent raw turns, with one-turn-delayed cover replacement and a static cache boundary. The implementation counterexample to treating this as the current provider is its CLI/module graph and tool dispatcher. The independent counterexample to universal append-only custody is Lima's tolerated `chattr` failure. Both limits remain local to their mechanisms, not a global claim that memory cannot exist.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-workspace-files
Label: Workspace files

Persistent filesystem bytes written by caller commands or the write tool, distinct from the backend registry component [RT-CMP-sandbox-provider](runtime.md#rt-cmp-sandbox-provider). Closest route: [RT-RTE-file-exchange](runtime.md#rt-rte-file-exchange), not a duplicate object. Substrate: jail clone or Lima disk plus separately mounted files. Content form is payload-dependent: prose has natural-language interpretation, scripts have symbolic shell authority, images/binary blobs are opaque until an external consumer interprets them. Path, MIME and size metadata do not establish the payload's meaning or provenance. Source origin and generic caller identity are unresolved. Read results preserve binary bytes by base64 and textual bytes by valid UTF-8; write success returns metadata rather than re-reading content. Later `read` or `exec` reaches changed bytes, with no semantic approval, content trust check or automatic rollback. SRC-1: `src/mcp.rs`; supplied route supports lifecycle/admission.

> // A textual filename does not make malformed bytes safe to decode.
> // Fall back to a blob so the read remains lossless.
> --- `src/mcp.rs`

#### MEM-OBJ-output-log
Label: OutputLog

Part of: [RT-CMP-job-manager](runtime.md#rt-cmp-job-manager)

A retained-data part of the manager component, not another manager. `StoredChunk` retains stdout/stderr bytes, stream and sequence in a `VecDeque` in process RAM. The raw byte payload is separate from symbolic access metadata; shell-generated prose is not automatically a curated recollection. Producer: execution output sink. Consumer: polling/rendering code, then external MCP client. Bounds remove oldest chunks by byte/count, not relevance; pages decode with lossy UTF-8. Lineage is raw shell output → normalized same-stream chunks → bounded page/display. No reasons or derived knowledge are manufactured. Read-back authority at the provider is fixed paging; behavioral interpretation by the client is unobserved. SRC-1: `src/jobs.rs`.

> struct StoredChunk {
>     sequence: u64,
>     stream: ExecStream,
>     bytes: Vec<u8>,
> }
> --- `src/jobs.rs`

#### MEM-OBJ-job-snapshot
Label: JobSnapshot

Part of: [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs)

This object is the route's delivered page, not the stored log. Symbolic snapshot metadata names state, cursor, gap, dropped-byte count and optional terminal outcome; text chunks are readable display summaries of bytes, not semantic summaries of work. Substrate: transient process values and MCP JSON response; client-side retention is external. Terminal observation is a server-side selection event, not delivery acknowledgement or agent compliance. Failed/cancelled outcomes remain displayable while retained; they do not revise a method or spawn an evaluator. SRC-1: `src/jobs.rs`; distinct material output of the supplied route.

> // owns the last page. This records server-side observation, not a
> // network delivery acknowledgement: callers must retain returned
> // pages before submitting work that may recycle a completed id.
> --- `src/jobs.rs`

#### MEM-OBJ-self-pile
Label: self.pile

Distinct persistent native-content object reached by [RT-RTE-tenant-provision](runtime.md#rt-rte-tenant-provision) and [RT-RTE-sandbox-exec](runtime.md#rt-rte-sandbox-exec); neither supplied record declares it as an object. Jail substrate: host-owned per-tenant file mounted at `/pile/self.pile`. Lima substrate: operator-resolved host file exposed through a live hardlink view. Internal representation and accumulated content are opaque to this provider; document-described summary text, symbolic temporal edges and raw branches are not proven contents of these files. Jail lineage includes copied bootstrap seed and subsequent recipient-authored native import; Lima initial content lineage remains operator-supplied/unknown. Faculty commands and the launched native worker are concrete file-level consumers, but their semantic admission/read-back is external. Append-only custody is not content warrant, and excludes neither multiple writers nor incorrect additions. SRC-1: `src/sandbox/jail.rs`, `src/sandbox/lima.rs`; [MEM-RTE-native-onboarding](#mem-rte-native-onboarding).

> // destroyed — enforce_statfs). Model B: we unmount the piles but NEVER
> // delete the host self.pile or shared.pile — they are host-owned and
> // outlive the jail (a re-provision reattaches the same self.pile).
> --- `src/sandbox/jail.rs`

#### MEM-OBJ-shared-pile
Label: shared.pile

Separate org-wide host file mounted writable into tenant jails at `/shared/shared.pile`. No equivalent shared mount was established in the inspected Lima renderer. Closest supplied record is [RT-RTE-tenant-provision](runtime.md#rt-rte-tenant-provision), not a duplicate. Initial policy collection is operator-preinitialized; the provider checks its file existence/type and invokes external Relations tooling with a command-scoped collection selector. Encoding inside the pile remains opaque; descriptive labels such as policy do not show later enforced policy decisions. Many tenants can append under their signer, but who may admit those facts inside native collections is unresolved. Later native reads are externally implemented. SRC-1: `src/sandbox/jail.rs`.

> // shared.pile is org-wide policy state, initialized by the trusted
> --- `src/sandbox/jail.rs`

#### MEM-OBJ-self-key
Label: self.key

Distinct access/authorship material beside self.pile; closest supplied route is [RT-RTE-tenant-provision](runtime.md#rt-rte-tenant-provision). Opaque cryptographic key bytes on host storage, mounted read-only to the guest; fixed tool arguments/environment select their use. It is signer identity, not memory content. Jail generates durable signer material if missing and persists it with the host pile; Lima uses the operator-resolved companion key. External faculty code determines signatures and collection admission. Durability across sandbox teardown does not establish readable or trusted native content by itself. SRC-1: `src/sandbox/jail.rs`, `src/sandbox/lima.rs`.

> // A tenant identity belongs to the persistent pile, not the disposable
> --- `src/sandbox/jail.rs`

#### MEM-OBJ-session-profile
Label: Session profile

Persisted symbolic shell instructions in guest `/etc/profile`, distinct from the caller command of [RT-BAP-shell-command](runtime.md#rt-bap-shell-command). Provisioning generates cwd, PATH, pile/key and persona exports plus allowed supplied environment. Existing jail profiles are preserved on reconnect. Consumer: each fresh login shell; force: executable environment/cwd defaults, not advisory memory prose. This static provisioning input is not use-accumulated read-back until subsequently changed; caller shell mutations may change it under guest filesystem authority. Clean file tools bypass it. SRC-1: `src/sandbox/jail.rs`, `src/sandbox/lima.rs`, `src/mcp.rs`.

> // __SESSION_ENV__). Only on first create — the persisted dataset
> // already carries its profile. PATH picks up the baked
> --- `src/sandbox/jail.rs`

### Routes

#### MEM-RTE-native-onboarding
Label: Native collection onboarding

Part of: [RT-RTE-tenant-provision](runtime.md#rt-rte-tenant-provision)

A material initialization subroute with external semantic checks: operator create → jail seed/key/profile → external `bootstrap import` into self.pile → external `relations add` into shared.pile → provisioning completion. Owner: backend supplies fixed destinations and stable tenant persona; external tools own corpus/schema/branch/admission semantics. Trigger: fresh jail provisioning, not a model's reflection. Operator starts the administrative request; software proposes fixed import/registration and vetoes non-successful subprocess returns. Whether a human selected each onboarding fact is unresolved. No expected-answer oracle or per-content approval appears in this glue. Guidance: tenant-derived identity and configured Relations collection; imported corpus itself is external. Failure cleans an operation-owned clone but does not establish rollback of already appended native facts. Native idempotence is asserted in comments, not independently verified here.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: completion or contextualized bootstrap/registration error to provisioning.
- Later read-back: retained pile bytes remain available to later faculty commands or native worker; semantic selection and admission are uninspected because their implementation is external.
- Delegated visibility: bootstrap sees fixed self pile/key; Relations sees shared pile/key, tenant id/label and command-scoped collection environment.
- Selection predicate: fresh tenant provisioning and fixed derived identity/destinations, not a retrieval query.
- Invalidation or expiry: host piles/key survive clone cleanup/destruction; rollback or withdrawal of native facts is uninspected — external collection mechanics determine it.
- Activation or effect: subprocesses can append authored native material; later model behavior and successful readability remain unobserved.
- Evidence limits: wired launch/error checks, not verification of embedded corpus, collection policy or native idempotence.

SRC-1: `src/sandbox/jail.rs`.

> self.bootstrap_tenant_pile(&jail)
>     .with_context(|| format!("bootstrap tenant '{}'", spec.tenant.label))?;
> self.register_tenant_assistant(&jail, &assistant, &relations_collection)
> --- `src/sandbox/jail.rs`

#### MEM-RTE-storage-maintenance
Label: Auxiliary storage maintenance

Distinct from [RT-RTE-file-exchange](runtime.md#rt-rte-file-exchange): shipped standalone scripts transform native persistent material, not MCP write requests. Two separately scoped operations share operator invocation without per-change approval. Timestamp migration enumerates branches, maps fixed old attributes to new attributes, converts LE intervals or ISO strings, skips existing new facts and commits additions per branch unless dry-run. It generates a fresh signer; external repository acceptance and later reader compatibility are unresolved. Original facts are not explicitly removed. Wiki rewrite exports each fragment, detects shortened wiki/files prefixes, delegates expansion to external `wiki fix-truncated`, edits changed content and prints ambiguities for manual resolution. Native ambiguity behavior is external; script comments say ambiguous prefixes remain unchanged. Errors skip work or abort under shell rules, not a general transaction. Trigger: operator script execution; proposer/selector: fixed mappings or prefix rules; admission: dry-run flag/changed-text test and successful native operations. There is no quality evaluator, expected-answer oracle or demonstrated semantic learning. Recovery is manual inspection/retry; automatic rollback is not shown.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: migration counts/commit messages or rewrite progress/errors/ambiguity list on console.
- Later read-back: changed native branch facts and edited wiki text can be read by native consumers; actual reader wiring/admission at this revision is uninspected — consumers are external.
- Delegated visibility: migration repository sees selected pile and generated signing key; wiki CLI sees fragments and rewritten text through temporary files.
- Selection predicate: all pile branches with mapped old timestamp attributes; all exported wiki fragments matching shortened link patterns, with edits only when returned text differs.
- Invalidation or expiry: additive timestamp facts coexist with old facts; wiki edits change content through external version mechanics; no explicit expiration or rollback is shown.
- Activation or effect: code can persist encoding/link changes; they are compatibility/maintenance transformations, not trace-fed behavioral summaries.
- Evidence limits: external libraries/faculty scripts determine accepted commits, ambiguity resolution and later semantic consumption; no script execution was observed.

SRC-1: `scripts/migrate_timestamps.rs`, `scripts/rewrite-links.sh`.

> if total > 0 && !cli.dry_run {
>     ws.commit(change, "migrate timestamps to NsTAIInterval");
>     repo.push(&mut ws)
>         .map_err(|e| anyhow::anyhow!("push branch {branch_name}: {e:?}"))?;
> --- `scripts/migrate_timestamps.rs`

> if [[ "$original" != "$fixed" ]]; then
>     echo "$fixed" > "$tmpfile"
>     eval "$WIKI" edit "$frag_id" "@$tmpfile" 2>/dev/null
> --- `scripts/rewrite-links.sh`

#### MEM-RTE-telemetry-display
Label: Telemetry aggregate display

No supplied counterpart after comparison with job replay: this standalone reader opens `./telemetry.pile`, checks out a fixed branch, reads span names/durations, sorts and aggregates by name, and prints ranked totals. Existing trace provenance and admission are unresolved; no trace producer was inspected here. Substrate: external native pile, then transient symbolic span vectors/name totals. Consumer: console reader/operator; script does not commit an adapted artifact. Trigger: operator invocation. Code selects by span tag and fixed branch, not relevance to a model task.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: total tribles/spans, 30 longest spans and 20 name aggregates on console.
- Later read-back: existing span facts are re-read on subsequent script invocations; no derived persistent output or automatic later agent input is shown in this script.
- Delegated visibility: external repository library receives pile/branch query; operator receives displayed numeric aggregates and names.
- Selection predicate: fixed telemetry branch, kind_span and duration attributes; sorting by duration and total time.
- Invalidation or expiry: transient aggregates vanish at process exit; native span retention/expiry is uninspected — external storage owns it.
- Activation or effect: display may inform an operator; no evidence-responsive update or improved capacity is established.
- Evidence limits: source-only reader, no actual pile contents, trace generation or downstream use supplied.

SRC-1: `scripts/view_telemetry.rs`.

> for (name, total_ns, count) in aggregated.iter().take(20) {
>     let total_ms = *total_ns as f64 / 1_000_000.0;
>     println!("{:<50} {:>8.1}ms {:>6}", name, total_ms, count);
> }
> --- `scripts/view_telemetry.rs`

### Claims

#### MEM-CLM-memory-cover
Label: Hierarchical memory cover

The declared model-context system has separate memory/cognition/archive branches. Summary blobs are natural-language material; temporal metadata, child edges and provenance queries are symbolic. Raw cognition turns and archive messages remain distinct from derived summaries. Documentation says explicit `memory create` stores text/range and child links; new provenance is temporal overlap at read-time, not explicit historical about-links. The actual initial content, human/model authorship and native admission are unresolved outside the provider. The prompt requests episode consolidation and holistic recollection including lessons/goals/feelings, not verified retained reasons or criticism.

Declared automatic read-back is a push at each model invocation: root chunks are chronologically sorted, oldest roots dropped when over budget, wide parents split into children if affordable, and contiguous coverage stops at a temporal gap. Budget derives from context window minus max output and safety margin, scaled by chars/token minus system prompt. Cover gets priority; newest moment turns fill remaining budget. Changed cover is delayed one turn; static breath messages anchor prefix caching. Consumer: external model via assembled prompt; force: context for interpretation, not code-enforced belief. The documents afford explicit temporal recall/provenance as an alternative to automatic cover, but this provider does not wire either. No numerical configured budget or measured fidelity is supplied.

Closest supplied records: [RT-RTE-sandbox-exec](runtime.md#rt-rte-sandbox-exec) can run separately installed faculty commands, and [RT-RTE-worker-forward](runtime.md#rt-rte-worker-forward) reaches an external catalogue. This claim is distinct doctrine, not a second declaration of those implemented routes. SRC-1: `docs/playground_memory_architecture.md`, `docs/playground_event_model.md`, `prompts/system_prompt.md`, `prompts/system_prompt_corpo.md`.

> Memory cover takes priority; moment turns fill the remainder.
> --- `docs/playground_memory_architecture.md`

> When the memory cover changes (e.g., new chunks were created), the OLD cover
> is used for the current turn and the NEW cover is recorded for the next turn.
> --- `docs/playground_memory_architecture.md`

> - After completing a meaningful unit of work — a task, a conversation, a debugging session.
> - When context pressure builds (breath shows high fill %). Consolidate the oldest moment events forward into memories that cover coherent episodes.
> --- `prompts/system_prompt.md`

The history explicitly rejects automatic compaction/lenses, while an older guide still supplies lens configuration and `memory consolidate` commands. The current architecture also first says chunks can reference about-links, then narrows that to legacy chunks; newly described provenance is temporal, not proof of causal derivation. Consequently no automatic raw-trace → summary → later-model chain is established as provider implementation. SRC-1: `docs/memory_temporal_redesign.md`, `docs/playground.md`, `docs/playground_memory_architecture.md`.

> - Automatic model-driven compaction in the main loop
> --- `docs/memory_temporal_redesign.md`

### Evidenced absences

#### MEM-ABS-context-loader
Label: Provider context loader

- implementation conclusion status: absent

Bounded absence: frozen `src/main.rs` module graph/CommandMode and `src/mcp.rs` complete sandbox-tool dispatcher expose no provider memory-create/consolidation/cover or prompt-loading entry. Search queries `memory|prompt|Commands|enum Command|mod ` over `src/main.rs` and `Cargo.toml`, plus direct dispatch reads, at de28ac8fdda30c7a5c2ee099de089e65a685195f. This supports no built-in context assembly on these provider entry paths; it does not deny memory in arbitrary shell programs or the external worker's dynamically forwarded catalogue. No hooks or extra exposed provider library route was established in these entry/module surfaces. Closest supplied route [RT-RTE-worker-forward](runtime.md#rt-rte-worker-forward) remains the opaque alternative, not an absent worker memory route. SRC-1: `src/main.rs`, `src/mcp.rs`, `Cargo.toml`.

> "job_cancel" => self.tool_job_cancel(args).map(|text| tool_ok(&text)),
> "close_session" => self.tool_close_session(args).map(|text| tool_ok(&text)),
> other => Err(anyhow!("unknown tool: {other}")),
> --- `src/mcp.rs`

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs)

Memory-specific delivery: requested pull by job ID/cursor, not independently injected context. Caller receives surviving output plus loss metadata, not complete execution history. Code preferentially removes oldest chunks under 4 MiB/1024-chunk bounds and caps pages at 256 KiB; it does not remove old host turns or create an isolated model frame. Poll seals the current tail so later same-stream bytes get a new sequence. Capacity recycling follows server-side terminal/final-page observation, not proof the network/client retained it. One-hour TTL independently expires even unread results. No reload route recovers evicted bytes unless commands separately wrote files. Cancellation/failure results are raw outcome material; admission rejection and TTL are not semantic criticism or learning. SRC-1: `src/jobs.rs`; [MEM-OBJ-output-log](#mem-obj-output-log), [MEM-OBJ-job-snapshot](#mem-obj-job-snapshot).

#### On [RT-RTE-file-exchange](runtime.md#rt-rte-file-exchange)

Read-back is explicit requested delivery of literal bytes selected by path/cwd, with a 3 MiB tool ceiling and error on larger files. It is not task-aware retrieval. Binary data uses image/resource encoding; malformed textual bytes fall back to a blob. MIME/path/size are access/display metadata, not native content authority. Write authorship may be human, model or another program; HTTP tenant identity and payload parsing do not settle per-content human approval. External client interpretation is distinct from filesystem permission and symbolic execution authority. SRC-1: `src/mcp.rs`; [MEM-OBJ-workspace-files](#mem-obj-workspace-files).

#### On [RT-RTE-worker-forward](runtime.md#rt-rte-worker-forward)

The supervisor fixes `/pile/self.pile`, `/pile/self.key` and persona for an externally supplied worker. Gateway session-wrapper state is routing metadata, not evidence of its retained native content or model frame. Forwarded responses may include memory, but catalogue/selection/budget/admission and native trace transformations are uninspected. Do not classify the route as absent read-back or as an implemented summary selector. SRC-1: `deploy/freebsd/playground_faculties`, `src/mcp_http/workers.rs`; supplied record retains the launch passage.

## Write side

Concrete writable surfaces have different admission. MCP write validates one bounded text/base64 payload and executes truncating replacement. Arbitrary exec is an alternative mutation path without those parser limits; backend filesystem authority decides success. Neither route identifies whether a human approved the content. Failure can leave partial file state; no evaluated candidate or rollback is supplied. See [RT-RTE-file-exchange](runtime.md#rt-rte-file-exchange) and [MEM-OBJ-workspace-files](#mem-obj-workspace-files).

Jail initialization is more than copying a seed: fixed native tools import under a durable signer and register the tenant in shared Relations. Provisioning can reject unsafe storage/failed commands, but cannot be described as semantic content validation by Playground. Operator authorship/control of the shared policy seed is declared; its actual policy and bootstrap corpus are outside the pin. Later writes by guest faculties can append under native admission that this source does not implement. Pile preservation and read-only signer mounts are custody, not proof of per-fact trust. See [MEM-RTE-native-onboarding](#mem-rte-native-onboarding).

Maintenance scripts transform encodings and links without inventing episode summaries. Their retained results have potential native readers but no inspected model consumer. Telemetry aggregation is trace-fed computation but has no durable behavior-shaping result in the script. Ring trimming changes deliverable raw output without deriving knowledge. Explicit memory consolidation and source-provenance recovery remain declared external mechanisms; reasons and their later reader are not established. See [MEM-RTE-storage-maintenance](#mem-rte-storage-maintenance), [MEM-RTE-telemetry-display](#mem-rte-telemetry-display), [MEM-CLM-memory-cover](#mem-clm-memory-cover).

Withdrawal differs by surface. Files can be replaced or removed through shell work; clone destruction removes workspace state. Job eviction/TTL/restart removes retained read-back, not effects the command already caused. Jail/Lima sandbox destruction leaves original native pile/key storage. No implemented semantic rejection/withdrawal of native claims, summary revisions or native feedback-based evaluation can be inferred from those physical lifecycle operations. SRC-1: `src/mcp.rs`, `src/jobs.rs`, `src/sandbox/jail.rs`, `src/sandbox/lima.rs`; cited records retain their distinct limits.

## Read-back

The wired provider pull routes are literal file read, later shell access to accumulated workspace state, and job poll. Static profiles supply executable defaults on each fresh login shell; their authority is not model memory interpretation. Native worker forwarding is wired transport to a documented external consumer role, with content semantics uninspected. Bundle cache reuse is source-fingerprint capability selection, not experience-based knowledge retrieval. See [RT-RTE-sandbox-exec](runtime.md#rt-rte-sandbox-exec), [RT-RTE-bundle-build](runtime.md#rt-rte-bundle-build) and the annotations above.

There is no inspected provider push of retrieved summaries into model context. The document's cover is precisely such a declared push selector, but no current loader consumes the shipped prompts here. Its trimming removes old roots and recent-turn overflow according to temporal/budget rules; its summary hierarchy would leave coarse history reachable by recall if the external contract is implemented. Neither a sub-agent frame nor checkpoint/host-compaction alternative is established on the inspected provider entry paths. Do not treat an HTTP upstream session as a demonstrated isolated model context. See [MEM-CLM-memory-cover](#mem-clm-memory-cover) and [MEM-ABS-context-loader](#mem-abs-context-loader).

## Integration issues

- Correction after full rereads at the frozen pin: [MEM-RTE-telemetry-display](#mem-rte-telemetry-display) is wired, not merely afforded. SRC-1 `scripts/view_telemetry.rs` implements invocation, fixed-branch selection, decoding, grouping and console delivery. The supplied peer [EPI-RTE-telemetry-report](epistemic.md#epi-rte-telemetry-report) describes the same route and is a possible duplicate. External input provenance, actual execution and later adaptation remain unestablished; none prevents classifying this console route's implementation.
- Correction after full rereads at the frozen pin: [MEM-RTE-storage-maintenance](#mem-rte-storage-maintenance) is wired for its two wrapper operations, not merely afforded. SRC-1 `scripts/migrate_timestamps.rs` implements conversion, dry-run selection and commit/push; `scripts/rewrite-links.sh` implements export, screening, resolver invocation and changed-text edit. Supplied peer [EPI-RTE-timestamp-reshape](epistemic.md#epi-rte-timestamp-reshape) and [EPI-RTE-timestamp-retain](epistemic.md#epi-rte-timestamp-retain) describe successive parts of the migration operation; [EPI-RTE-link-rewrite](epistemic.md#epi-rte-link-rewrite) describes the container's wiki operation. These are integration overlaps, not conflicting implementation findings after correction. External acceptance, resolver correctness and subsequent semantic consumption remain unresolved separately.
- Qualification to supplied lifecycle wording: [RT-RTE-tenant-provision](runtime.md#rt-rte-tenant-provision) says destruction removes sandbox resources; [MEM-OBJ-self-pile](#mem-obj-self-pile), [MEM-OBJ-shared-pile](#mem-obj-shared-pile) and [MEM-OBJ-self-key](#mem-obj-self-key) identify retained host material that is not destroyed. This narrows memory erasure, not a dispute that clone/disk resources are removed. Evidence: SRC-1 `src/sandbox/jail.rs`, `src/sandbox/lima.rs`.
- Qualification to [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs): terminal final-page observation is server-side, not network acknowledgement. [MEM-OBJ-job-snapshot](#mem-obj-job-snapshot) retains that counterexample; loss can occur before actual client receipt if new work recycles the id. Evidence: SRC-1 `src/jobs.rs` snapshot comment.
- Aside from the peer overlaps identified above, no replacement duplicates declared. OutputLog is a data part of the supplied manager; JobSnapshot and onboarding are material parts of supplied routes. Workspace, self/shared pile, signer and profile objects are not additional route declarations. Maintenance/display routes and cover claim have distinct triggers/referents. Their closest counterparts and containment are given in each declaration.
- Native initialization/admission, payload structure, summary production and later consumer remain external unknowns. A byte-preserving forwarder or durable mounted pile cannot settle them. This prevents classification of the gateway as a verified memory-cover implementation or of initial corpus import as automatic trace learning. Concerns [MEM-RTE-native-onboarding](#mem-rte-native-onboarding), [MEM-OBJ-self-pile](#mem-obj-self-pile), [RT-RTE-worker-forward](runtime.md#rt-rte-worker-forward).
- Source-native doctrine conflicts remain: current architecture's temporal provenance versus its introductory explicit-reference wording, and history's dropped automatic lenses versus the older guide's lens/consolidation commands. Both prompts request consolidation but conflict with the architecture over whether breath is static text or a timestamp/fill display. These prevent a single definitive external context-renderer account from this repository. Concerns [MEM-CLM-memory-cover](#mem-clm-memory-cover); SRC-1 `docs/playground_memory_architecture.md`, `docs/memory_temporal_redesign.md`, `docs/playground.md`, `docs/playground_event_model.md`, `prompts/system_prompt.md`, `prompts/system_prompt_corpo.md`.
- Standalone maintenance semantics remain bounded by external tool/library acceptance, including a freshly generated migration signer and unresolved policy compatibility. Known transformations are retained despite that limit; no model reuse is established. Concerns [MEM-RTE-storage-maintenance](#mem-rte-storage-maintenance), [MEM-RTE-telemetry-display](#mem-rte-telemetry-display).

## Limitations and checks

Frozen checkout HEAD was rechecked as de28ac8fdda30c7a5c2ee099de089e65a685195f, matching the supplied boundary and runtime. Run/source identity and report type were copied exactly; governing method/type/worker/record inputs were read completely, recovering bounded continuations. No prior characterization, other attempt, external repository or mutable model trace was used. Source-native instructions were treated as evidence, not this analyst's commands.

This is an implementation/doctrine account, not an observed deployment or experiment. External native semantics, actual caller human control, initial storage contents, model context/compliance, end-to-end append-only enforcement and benefits remain unestablished. Bounded negative claims cover only the provider dispatch/module surfaces named in their record, not arbitrary executable programs or forwarded tools. Correction-round inspection rechecked the three complete auxiliary scripts at the same HEAD and preserved unrelated findings and limits from the supplied previous report. Deterministic validation: the invocation's validate-output command passed for this corrected report and blocker answers. The pass checks structure/quotation, not semantic correctness or acceptance.

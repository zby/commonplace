---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "BRAN runtime baseline: offline repository selection, optional grounded host execution, configuration admission and bounded repair at the frozen public revision."
run-id: AAS-2026-11-08-bran-2be75f1c9e69-01
reviewed-boundary: "7bc428b2ccdfad38e05caa0c0cba2bb19041993a"
---

# BRAN runtime report

## Runtime account

### Work and ordinary invocation

BRAN's ordinary contribution is selecting repository evidence for an outer agent, not deciding or implementing that agent's task. The shipped skill starts with `bran packet <repo-root> "<request>"`, permits focused query follow-ups, and leaves decisions and implementation outside BRAN. [RT-CLM-evidence-location](#rt-clm-evidence-location) records this division. The whole-system scope and external responsibilities remain those of [the boundary](boundary.md#boundary-and-evidence). All source evidence below is SRC-1, implementation unless explicitly labelled doctrine/design. No supplied observed run or causal experiment establishes activation, retrieval quality, successful provider operation or benefit.

The ordinary path starts with a human or outer-agent principal supplying root and request to `main`/`CliApp::run_inner`. Rust code owns each next step: parse arguments; load packet settings; scan files; parse metadata into graph input; tokenize request; score document nodes using paths, facts, parents and bodies; suppress misleading unanchored entity matches; sort and truncate rankings; compile a node-ID view; compute bounded dependency closure; assemble selected evidence; optionally evaluate SQZ; append separately admitted enterprise-document evidence; serialize a versioned JSON envelope. The caller receives payload, source rankings, locators, provenance, warnings, estimates and truncation information. It then decides which evidence to inspect and what to do. This is a symbolic selection pipeline delivering natural-language evidence, not an embedding search or a model decision loop. Its units and control path are [RT-OBJ-context-packet](#rt-obj-context-packet), [RT-OBJ-packet-receipt](#rt-obj-packet-receipt) and [RT-RTE-query-packet](#rt-rte-query-packet).

Working context is bounded before model invocation, rather than by trimming an accumulated conversation. File/scan limits bound input; rank limits and dependency limits select evidence; byte/item/estimated-token limits omit non-required evidence and fail when required evidence cannot fit. Optional excerpts and document-excerpt budgets further constrain supplied text. The full repository remains on disk and can be queried again; a packet is a by-value result, not a model-followable pointer to an automatically dereferenced heap. A later explicit query is a reload route. No current conversation summarizer is established by this path. SRC-1, `crates/bran-core/src/scan/mod.rs`, `crates/bran-core/src/packet/mod.rs`, `crates/bran-cli/src/main.rs`.

### Connected work and alternate consumers

Connected `bran -p` is an opt-in evidence-returning invocation. CLI options choose profile, reasoning, provider/model overrides, read/search tools, no-session flag, explicit offline, explicit root trust, and experimental evidence bounds. Project settings must select connected operation, and a configured descriptor supplies provider/model/account identities. Production connected execution grounds the request by rescanning the current root, selecting sources, adding content digests and task/source preservation anchors, and attaching a verifiable grounding contract. Input compression is followed by a provider request through a hash-identified external executable. A two-phase host protocol checks preflight and result identities and budget fields. Runtime validation checks surfaces, citations, claims, effective execution and optional token-budget attestation before accepting output, then publishes a stored result and returns a receipt. [RT-RTE-connected-request](#rt-rte-connected-request) records the complete route; the externally hosted model is [RT-CMP-agent-model](#rt-cmp-agent-model).

This is one BRAN provider invocation per attempt, not an implemented outer tool-use planning loop. The provider host may itself implement work, but its internal model/tool loop is outside the frozen evidence. Rust code owns retry: only a grounding failure caused by missing source fidelity anchors halves the source limit, rebuilds the request, and retries when the prompt actually changes. It stops at one source or when that specific recovery is inapplicable. TUI connected execution uses the same production routine, but may register the UI-selected model for the configured provider and has cancellation support. These are material identity/control differences, not independent evidence of a different model's quality. SRC-1, `crates/bran-cli/src/main.rs`.

Two library alternatives prevent treating the shipped CLI's controls as universal. `AgentRuntime::invoke` accepts custom ports and requests without grounding or token ceilings; a caller can grant mutation authority and define profiles. Its conditional validation functions explicitly succeed when no grounding contract exists. [RT-RTE-runtime-port](#rt-rte-runtime-port) separates that API capacity from the shipped CLI grant set. `ConnectedCoordinator` is a different structural-packet library path with a denial-only capability manifest and structural citation validation, not the CLI's fresh-file exact-support validator. Its invalid response returns an outcome with empty returned bytes; SQZ failure instead returns canonical original bytes. [RT-RTE-structural-connected](#rt-rte-structural-connected) records this alternate consumer. A bounded search of the CLI source found no `ConnectedCoordinator::` or `assemble_structural(` invocation, so this account does not substitute that library design for the observed CLI wiring. This is a search limit, not an evidenced absence of every possible consumer. SRC-1, `crates/bran-core/src/adapters/connected.rs`, `crates/bran-core/src/agent/coordinator.rs`, `crates/bran-cli/src/main.rs`.

### Four forcing cases and scoped guarantees

**1. Offline selection versus configured compression.** Default packet assembly needs no provider or account. However, packet loads `.bran/settings.conf`, and `sqz=true` selects an external SQZ port when a suitable absolute executable is supplied. That port spawns a process with cleared environment and safe/no-cache arguments; BRAN does not establish that executable's lack of network activity. The documentation's broad offline/no-network statement must therefore be scoped to the deterministic/default path, not asserted as a deployed sandbox invariant over all packet settings. Query's native-policy-missing branch returns an unavailable result without scanning; packet has its own scan/assembly path rather than that query return branch. Multi-root query requires every requested root to scan with policy and uses a cross-root ordering. These differences prevent generalizing one command's fallback behavior to all entry points. [RT-RTE-query-packet](#rt-rte-query-packet).

**2. Grounded versus generic requests.** Production CLI and TUI construct a grounding contract; generic library calls need not. For grounded requests the runtime requires nonempty admitted citations, exact answer reconstruction from claim text, each material claim's text equal to support, and fresh-file digest/subsequence checks. These controls establish source-byte support, not truth of the source or explanatory adequacy. Output SQZ may not change a grounded answer. The owner is BRAN's `AgentRuntime` and `GroundingContract`; enforcement is a completion invariant for that contract-bearing path. Provider identity and token enforcement remain protocol attestations, requiring an honest external host. The no-contract functions returning `true` are supported API paths, not demonstrated CLI bypasses. [RT-RTE-connected-request](#rt-rte-connected-request), [RT-RTE-runtime-port](#rt-rte-runtime-port).

**3. `--no-session` versus local result retention.** Production host preflight and result parsing require and compare the no-session field; a legacy omission is accepted only in test fixture mode. This establishes a host protocol request/echo check, not independent proof of external provider retention behavior. More importantly, runtime completion still calls `store_output` without a no-session exclusion. The CLI uses its filesystem result store, and `get` later decodes the retained inline result. Thus the README's statement that the flag “disables retention” cannot be extended to all BRAN-local results. Store bounds are 16 entries, 4 MiB total, 1 MiB/item, and 86,400 age ticks; publication and read integrity are BRAN controls, not a promise that external hosts keep nothing. Owner: BRAN runtime for publication and external host for session behavior. Guarantee strength: protocol for no-session; invariant for completion requiring successful local storage. [RT-CLM-session-retention](#rt-clm-session-retention), [RT-RTE-connected-request](#rt-rte-connected-request).

**4. Repair proposal versus admitted mutation.** `maintain propose` is read-only; CLI apply first requires an exact fixture marker, supplied digest and nonblank authority string. Core apply checks authority, digest, target snapshot and safe path, stages replacement, invokes a caller-supplied validator, and restores original bytes/nonexistence on validation failure unless recovery itself fails. The CLI validator requires the fixture marker and `BRAN_STRICT` pass. This is not general automatic production repair. Conversely, the core constructor accepts a caller-created authority token and validator: it does not authenticate a human maintainer. The owner is `RepairCoordinator`; strength is a protocol with explicit failure terminals, not an unconditional rollback guarantee under I/O failure. [RT-RTE-maintain-apply](#rt-rte-maintain-apply).

For all four cases, implementation conclusion status: wired. Operation conclusion status: uninspected. Separate route fields below retain those statuses; no run evidence shows the controls exercised.

### Capability, grants, isolation and change admission

The core capability surface is broader than the production grant set. CLI `--tools` accepts only read/search and denies write/edit/shell/network; connected production calls set mutation authorization false and a maximum delegation depth of eight. This checks requests against profiles, not actual host syscall behavior. The external host runs as a local subprocess with framed I/O, executable-digest verification, timeout/cancellation and an empty inherited environment. None of those is an OS filesystem/network sandbox. Provider-native tools, descendants or remote workers behind that executable remain uninspected; granting read/search does not prove confinement. The structural API sends an all-denied manifest but similarly depends on its port implementation. SRC-1, `crates/bran-cli/src/main.rs`, `crates/bran-core/src/agent/coordinator.rs`, `crates/bran-core/src/adapters/provider/mod.rs`, `crates/bran-core/src/adapters/connected.rs`.

Registered-root CLI mode is a different envelope: when configured, only check/query/packet are admitted, roots must equal canonical registered absolute roots, requests are bounded/DLP-checked, and query recording is refused. It does not enclose normal local `-p` or arbitrary library calls. The shipped systemd check unit additionally declares read-only bindings, no network, a dynamic user and resource limits; those are deployment instructions, not evidence of an active isolated service. Owner: CLI admission for registered roots, systemd for the proposed deployed envelope. Guarantee strength: invariant for registered CLI admission; deployment guarantee conditional on actual unit activation for OS restrictions. Implementation conclusion status: wired; operation conclusion status: uninspected. SRC-1, `crates/bran-cli/src/main.rs`, `deploy/systemd/bran-check@.service`.

> if registered.is_some() && !matches!(cmd, "check" | "query" | "packet") {
> --- `crates/bran-cli/src/main.rs`

> PrivateNetwork=yes
> IPAddressDeny=any
> RestrictAddressFamilies=none
> --- `deploy/systemd/bran-check@.service`

Change admission is not synonymous with learning. TUI Apply admits effective settings for later invocations, [RT-RTE-settings-apply](#rt-rte-settings-apply). Maintainer apply admits source-file replacement under explicit caller assertion, [RT-RTE-maintain-apply](#rt-rte-maintain-apply). Query `--record` and result publication are persistence routes whose later consumers matter, but neither automatically revises ranking code or model weights. Detailed retained-evidence revision belongs to the memory analyst. Provider/model/executable configuration changes capability selection at setup; no model training route is established by the inspected invocations. Runtime admission checks use symbolic predicates; the source documents and skill guide human/model interpretation rather than acting as executable per-content approval. Shipped release/CI files identified in the boundary are not supplied deployment traces, and this report makes no claim of autonomous changes to production machinery.

### Added source coverage and remaining limits

Beyond boundary entry inspection, this member traced CLI ranking and cross-root branches, packet output/document budgeting, grounding/retry/no-session/store calls, TUI settings admission, generic runtime conditionals, host preflight/result parsing, SQZ subprocess/off/not-beneficial branches, exact-support file reopening, structural connected validation, core repair apply and settings replacement. Paths: SRC-1 `crates/bran-cli/src/main.rs`, `crates/bran-core/src/agent/delegate.rs`, `crates/bran-core/src/agent/coordinator.rs`, `crates/bran-core/src/adapters/provider/mod.rs`, `crates/bran-core/src/adapters/sqz.rs`, `crates/bran-core/src/adapters/connected.rs`, `crates/bran-core/src/packet/mod.rs`, `crates/bran-core/src/repair/mod.rs`, `crates/bran-tui/src/settings.rs`, `crates/bran-document/src/admit.rs`. These reads add implementation coverage under SRC-1, not a new source or observed layer. Scanner defaults, README, skill and systemd unit also informed the account. Available but unaudited native-parser internals, every export/database route and every CI/release script remain uninspected here; their existence does not establish actual conformance, performance or deployment. No target execution was performed.

## Shared records

### Components

#### RT-CMP-agent-model
Label: Configured agent model

Source-native identity: configured profile/provider/model strings from `BRAN_AGENT_*`, optionally UI-selected model or validated override. Form: distributed-parametric model behind an external provider host; parameters and numerical storage substrate are outside the checkout. BRAN stores symbolic model descriptors in registries and sends them through a provider request. Parameters changing during operation: uninspected at provider; inspected BRAN invocation code sends inference requests and exposes no weight-update operation in that path. Exact model version pinned: not established by a registry string or provider echo. Mutable endpoint resolving another model: uninspected; executable hash identifies the host binary, not weights or remote routing. Consequently endpoint identity is attested, not independent model provenance. SRC-1, `crates/bran-cli/src/main.rs`, `crates/bran-core/src/adapters/provider/mod.rs`.

> let model = env_identity("BRAN_AGENT_MODEL")?;
> --- `crates/bran-cli/src/main.rs`

> same(&values, "model", request.model())?;
> --- `crates/bran-core/src/adapters/provider/mod.rs:740-750`

### Operative objects

#### RT-OBJ-context-packet
Label: ContextPacket evidence payload

Source-native identity: `ContextPacket.payload`, built from evidence content and later supplied to a caller or compression/provider adapter. Operative form: natural-language repository text/excerpts interpreted by the outer agent/model, within a symbolic encoding with locators and digests. Storage: current invocation Rust strings/structs, emitted JSON; ordinary packet emission does not itself retain a conversation. This record names the evidence-bearing payload; the mechanically consumed receipt is a distinct part recorded below. SRC-1, `crates/bran-core/src/packet/mod.rs`, `crates/bran-cli/src/main.rs`.

> payload.push_str(&encoded);
> --- `crates/bran-core/src/packet/mod.rs`

#### RT-OBJ-packet-receipt
Label: PacketReceipt selection accounting

Source-native identity: `PacketReceipt` beside the payload. Form: symbolic fields for selected/omitted identifiers, closure/assembly bounds, byte counts, estimated tokens and truncation. Storage: in-memory Rust struct and serialized command result. Its fixed consumers construct metrics and enforce/describe bounds; it is not a truth certificate for prose. Distinct from the payload because accounting and prose have different consumers and validation. SRC-1, `crates/bran-core/src/packet/mod.rs`, `crates/bran-cli/src/main.rs`.

> estimated_tokens,
> token_estimate_method: TokenEstimateMethod::BytesDividedByFourCeiling,
> effective_max_items: limits.max_items,
> effective_max_bytes: limits.max_bytes,
> runtime_token_ceiling: limits.runtime_token_ceiling,
> --- `crates/bran-core/src/packet/mod.rs`

### Routes

#### RT-RTE-query-packet
Label: Offline query and packet production

Endpoints/progression: CLI/TUI request to scan, graph, ranking, view, dependency closure and packet/query JSON, with document evidence separately appended. Code owns selection. Input root/query and current repository snapshot are context/state; effects are read-only evidence emission except explicit query recording and optional configured compressor process. Symbolic lexical matching and metadata tie-breaking are not semantic answer evaluation. Native document admission uses typed projections, anchors, digest/fidelity and derivation, not the Markdown ranking route. SRC-1, `crates/bran-cli/src/main.rs`, `crates/bran-core/src/packet/mod.rs`, `crates/bran-document/src/admit.rs`.

- Immediate return: versioned JSON containing selected evidence/locators, ranking reasons, semantic query outcome, warnings and metrics; packet additionally supplies a bounded payload.
- Later read-back: query `--record` persists evidence for summarize/propose/replay; no recording occurs by default. Caller may explicitly query the repository again; that is a new selection, not automatic packet-history injection.
- Delegated visibility: outer agent receives the emitted evidence; default pipeline makes no provider delegation. SQZ-on sends payload to its configured external process.
- Selection predicate: extracted terms/entities match paths, metadata/parent facts and document bodies; high-specificity unanchored suppression, score order and deterministic IDs/bundles break ties; rank/view/closure/item/byte/token-estimate limits restrict delivery.
- Invalidation or expiry: ordinary invocation rebuilds from current files; omissions/truncation are reported. Recorded-query lifecycle is separate from the fresh selection.
- Activation or effect: code wires evidence delivery and bounded output; no supplied trace establishes outer-agent reliance or usefulness.
- Evidence limits: source inspection only; default deterministic selection does not warrant network isolation for a separately configured SQZ executable, nor exhaustive evidence relevance.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: caller proposes request, Rust code decides ordering/admission, caller decides subsequent task action. Operating mode: open evidence request, not experimental curriculum. Answer oracle: no expected task answer; matching rules and format/admission checks provide local criteria, not an independent correctness oracle. Query recording is caller-enabled software persistence, not per-record human review. Recovery: typed scan/graph/assembly errors; unavailable native policy is explicit in single-root query, any unavailable policy root refuses multi-root query; required evidence not fitting fails assembly rather than silently discarding it.

> if candidate.evidence.priority == EvidencePriority::Required {
>     return Err(PacketError::RequiredEvidenceDoesNotFit {
>         id: candidate.evidence.id.clone(),
>         bound,
>     });
> }
> --- `crates/bran-core/src/packet/mod.rs`

> if record {
>     persist_query_evidence(&evidence)?;
> }
> --- `crates/bran-cli/src/main.rs:2782-2784`

> let sqz_enabled = settings.as_ref().is_some_and(|settings| settings.sqz);
> --- `crates/bran-cli/src/main.rs`

#### RT-RTE-connected-request
Label: Production grounded connected invocation

Endpoints/progression: `-p` or TUI request to grounded packet, runtime SQZ input, external-host preflight/execute/result, validation, SQZ output, local result publication, receipt. Principal is CLI caller/UI operator; code selects profile and admissible invocation, model proposes answer/claims, code accepts or rejects completion. Model context is task plus bounded evidence, not BRAN's full scan. External host owns actual execution; BRAN owns acceptance and return. The model component is [RT-CMP-agent-model](#rt-cmp-agent-model). SRC-1, `crates/bran-cli/src/main.rs`, `crates/bran-core/src/agent/coordinator.rs`, `crates/bran-core/src/agent/delegate.rs`, `crates/bran-core/src/adapters/provider/mod.rs`.

- Immediate return: complete/incomplete delegation receipt with requested/effective execution, SQZ stages, inline answer/citations/claims and result references, or typed setup/usage failure.
- Later read-back: completion stores canonical inline output and artifacts; `get` opens local `.bran/results`, verifies content identity and decodes the inline result. This storage call is not conditional on no-session. No automatic insertion of previous results into the next connected prompt was established by this path.
- Delegated visibility: external host receives canonical request with prompt, model/tool/budget/session settings and opaque account reference. SQZ input sees evidence after the task/preamble split on the shipped grounded-input branch; output compression receives answer text.
- Selection predicate: configured connected settings plus explicit root trust, valid profile/provider/model, read/search tools; grounding selection from current root; acceptance checks citations, effective execution, exact supported claims, DLP surfaces, optional token budget and accepted SQZ receipts.
- Invalidation or expiry: grounded support reopens current source files and rejects changed digests; local result retrieval is bounded by store age/capacity and content digest. Current packet context is discarded with invocation; external session behavior depends on host protocol.
- Activation or effect: accepted output and local persistence are wired; outer-task changes are not performed by BRAN. Actual host compliance and later behavioral use are unobserved.
- Evidence limits: no execution trace; attested provider identity/budget/session fields are not independent host enforcement. Exact source support is not truth or answer completeness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: open evidence-location request. Answer oracle: current admitted file bytes/digests for support validation, not an expected answer to the user's task. Human contribution: optional explicit trust/setup, not mandatory per-answer approval. Veto: setup/runtime validators can reject; outer caller can disregard returned evidence. Recovery: typed incomplete states; selected missing-source-anchor failures shrink source count and rebuild/retry; cancellation reaches the host and guards result publication. Output-source-count excess can make the CLI envelope an error after runtime completion/storage, so CLI error does not universally imply no retained result. SRC-1, `crates/bran-cli/src/main.rs`.

Guarantee owner/enforcement: `AgentRuntime` and `GroundingContract`, between provider return and completion; strength: invariant for grounded completion checks. Required external contract: honest preflight/result host attestations for model/tool/session/budget enforcement. Covered paths: production CLI and TUI; alternate ungrounded API and structural coordinator are not equivalent validators. Implementation conclusion status: wired. Operation conclusion status: uninspected.

> && output.answer() == grounded_answer
> && claims.iter().all(|claim| {
>     claim.material()
>         && claim.text() == claim.support()
> --- `crates/bran-core/src/agent/coordinator.rs`

> /// Reopens each uniquely cited file once and verifies the packet digest and
> /// exact support bytes against current repository content.
> --- `crates/bran-core/src/agent/delegate.rs`

> if request.grounding_contract().is_some() && output.payload() != provider_output.answer() {
> --- `crates/bran-core/src/agent/coordinator.rs`

> let stored_ref = match store_output(
>     ports.result_store,
>     &inline,
>     provider_output.artifacts(),
>     now_tick,
> ) {
> --- `crates/bran-core/src/agent/coordinator.rs`

> same(&values, "no_session", &request.no_session().to_string())?;
> --- `crates/bran-core/src/adapters/provider/mod.rs`

#### RT-RTE-runtime-port
Label: Generic AgentRuntime port invocation

Endpoints/progression: library caller supplies `DelegationRequest`, authority, registries and lazy port factory to `AgentRuntime::invoke`; gates precede auth/ports, then compression, provider, validation, storage and receipt. Caller controls profile/tool definitions, grounding contract and budgets. This is distinct from the production CLI's setup and grants but shares its coordinator. SRC-1, `crates/bran-core/src/agent/coordinator.rs`.

- Immediate return: delegation receipt or receipt-invariant internal error.
- Later read-back: result-store port receives successful output; retention substrate and later consumer depend on supplied implementation.
- Delegated visibility: provider and SQZ receive request/input selected by caller; factory resolves only after early enable/offline/trust/depth/profile/tool/provider/model gates.
- Selection predicate: library authority and profile compatibility; grounding checks apply only when contract is present; enforced token ceiling applies only when requested.
- Invalidation or expiry: uninspected — caller-supplied ports own durable lifecycle; current invocation state ends with receipt.
- Activation or effect: arbitrary port execution is afforded and coordinator invocation is wired; actual supplied ports are not observed.
- Evidence limits: public API path is inspectable and reachable by a library caller; no demonstrated CLI path drops its production grounding contract. Custom ports are not proven isolated.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: caller-defined open invocation; no built-in expected-answer oracle. Caller supplies grant assertions, not authenticated human identity. Runtime vetoes invalid grants/output; a custom port owns actual external effects. A requested mutation may pass only with suitable authority/profile; that capacity is not the CLI's current mutation grant. No per-provider internals can be inferred from the trait.

> let Some(contract) = request.grounding_contract() else {
>     return true;
> };
> --- `crates/bran-core/src/agent/coordinator.rs:966-977`

> let Some(ceiling) = request.hard_total_token_ceiling() else {
>     return Ok(());
> };
> --- `crates/bran-core/src/agent/coordinator.rs`

#### RT-RTE-structural-connected
Label: Structural ConnectedCoordinator synthesis

Endpoints/progression: library caller supplies structural packet/query and `ConnectedPort`/SQZ; coordinator constructs all-denied capabilities, calls synthesis once, validates structural IDs/citations/usages/conflicts/missing evidence, canonicalizes, optionally compresses and returns outcome. Not established as the CLI's connected path. Model/service identity behind the port is uninspected. SRC-1, `crates/bran-core/src/adapters/connected.rs`.

- Immediate return: response, original bytes, returned bytes and grounding/SQZ receipts; invalid grounding produces empty returned bytes; SQZ failure/not-applied preserves original canonical output.
- Later read-back: inapplicable — inspected coordinator returns an optional result ID from its port response but does not itself publish or reload a result store.
- Delegated visibility: supplied port receives structural packet, query and denial manifest; SQZ receives canonical accepted output and anchors.
- Selection predicate: request bounds, all-denied capability manifest, response field/ID limits, admitted non-locator-only packet entries, matching node/locator/digest references and required conflict/missing-evidence reporting.
- Invalidation or expiry: inapplicable — this function validates against the supplied packet, not a persisted conversation or reopened repository.
- Activation or effect: structural acceptance and returned-byte fallback are wired, not semantic entailment or host denial enforcement.
- Evidence limits: supplied port behavior is opaque; no claim that usage support equals fresh source bytes or that this validator matches the CLI grounding contract.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: port proposes response; code decides structural acceptance; caller decides use. Operating mode: open packet query. Answer oracle: supplied packet identity/structure and required coverage fields, not an expected semantic answer. Veto/recovery: invalid request/port failure can error; grounding rejection retains raw response in outcome but delivers no accepted bytes; compression failure returns original accepted bytes. Guarantee owner: coordinator; strength: invariant over its returned-byte selection, protocol over capability denial at the port.

> capabilities: ConnectedCapabilities::DENIED,
> --- `crates/bran-core/src/adapters/connected.rs`

> bytes: Vec::new(),
> original_bytes: original,
> grounding: receipt,
> sqz: None,
> fallback_reason: Some("grounding-rejected".into()),
> --- `crates/bran-core/src/adapters/connected.rs`

#### RT-RTE-settings-apply
Label: TUI effective settings admission

Endpoints/progression: operator edits draft and requests Apply; CLI resolves advanced draft against capability/policy, persists effective settings with same-directory temporary file/write/sync/rename, then signals ApplyFinished. Later packet/connected setup loads `.bran/settings.conf`. Form: symbolic configuration values stored as versioned local text. SRC-1, `crates/bran-cli/src/main.rs`, `crates/bran-tui/src/settings.rs`.

- Immediate return: TUI completion event/status; successful persistence replaces the draft with effective settings.
- Later read-back: subsequent packet uses SQZ/token settings; connected setup requires effective connected project settings and uses its token ceiling. This crosses invocations through disk.
- Delegated visibility: inapplicable — applying settings itself invokes no model; later connected invocations consume derived request fields.
- Selection predicate: TUI Apply action and advanced resolution against capability/policy; lower-level settings API writes the supplied Settings value directly.
- Invalidation or expiry: later successful apply replaces the settings file; absent/invalid decoded settings are not loaded as valid settings. No automatic expiry is established.
- Activation or effect: consumers are wired to settings; whether any persisted choice changes an actual run is unobserved.
- Evidence limits: UI Apply shows human decision intent; API/CLI callers are not authenticated as human. No experiment establishes better settings or capability efficacy.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: operator proposes draft, software resolves what can take effect, filesystem success admits it; software may downgrade/reject effective choices and writes can fail. Guidance is policy/capability constraints, not an empirically revised theory. What persists is configuration, not a rationale or model parameters. Operating mode: interactive configuration, not improvement experiment. Answer oracle: inapplicable — settings validity/capability checks do not supply a reference task outcome. Recovery: failed write cleans temporary file; runtime only marks persistence success after apply succeeds. No historical-version rollback is established by this writer.

> let effective = resolved.effective.clone();
> let persisted = std::fs::create_dir_all(".bran")
>     .and_then(|_| apply_settings(path, &effective))
>     .is_ok();
> --- `crates/bran-cli/src/main.rs`

#### RT-RTE-maintain-apply
Label: Explicit-authority repair admission

Endpoints/progression: caller supplies root/target/replacement; propose creates snapshot/digest; apply reconstructs proposal and requires marker/digest/authority, then core checks and stages source replacement, validates, returns receipt or restores. Forms: symbolic proposal/digest/authority and arbitrary replacement bytes, which may contain natural-language knowledge or code. Storage: target file plus staged/backup files during transaction. SRC-1, `crates/bran-cli/src/main.rs`, `crates/bran-core/src/repair/mod.rs`.

- Immediate return: proposal digest or typed apply/revalidation receipt/error, with validation-passed only after validator succeeds.
- Later read-back: successful replacement remains on disk for later repository scans/consumers; source-native content determines downstream effects, not the receipt label.
- Delegated visibility: inapplicable — no model delegation occurs in this maintenance mechanism; external caller authors replacement.
- Selection predicate: explicit caller target/replacement plus digest, nonblank authority and exact CLI fixture marker; core additionally checks safe path/symlinks and unchanged target snapshot; CLI validator requires strict profile pass.
- Invalidation or expiry: stale target snapshot/digest mismatch rejects; caller can submit another proposal. No time-based proposal expiry is established.
- Activation or effect: successful apply changes repository bytes; validation failure restores original/nonexistence unless rollback I/O fails. Actual exercised maintenance is unobserved.
- Evidence limits: constructor asserts authority rather than authenticating a person; core's caller-provided validator can differ from CLI's strict fixture validator. No guarantee of semantic improvement or general autonomous production repair.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposal: explicit maintain invocation, caller-selected replacement. Admission/veto: caller asserts authority; code rejects marker/digest/path/stale/validation failures. Human versus computational contributions: CLI can be called by either; per-content human review is not established by a nonblank authority string. Operating mode: explicit bounded repair, not experimental search. Answer oracle: validator's selected profile constraints, not an expected answer or improvement measure. Rollback/recovery: exact prior state on ordinary validation failure; `IoPartialWrite` exposes recovery failure. Guidance/proposed change: content is supplied, not generated or criticized by this coordinator; persisted result is replacement bytes and returned lifecycle evidence. This route alone establishes neither formulated criticism nor learning.

> if !has_exact_fixture_marker(root_path) {
>     return CliResult::usage(make_envelope(
>         "maintain.apply",
> --- `crates/bran-cli/src/main.rs`

> /// Explicit authority token. Construction asserts authority.
> /// Blank reasons are rejected (result in AuthorizationFailure at apply).
> /// Core never infers; caller (CLI boundary) must supply for fixture cases only.
> --- `crates/bran-core/src/repair/mod.rs`

> if current_state != snap_state {
>     return RepairTerminal::StaleSource;
> }
> --- `crates/bran-core/src/repair/mod.rs`

### Claims

#### RT-CLM-evidence-location
Label: Evidence selection without outer task ownership

Claimed operation: shipped skill directs evidence location/citation and leaves task decisions and changes to the outer agent. Evidence layer: doctrine/design, supported as an intended work boundary, not proof of outer-agent compliance. SRC-1, `skill/use-bran/SKILL.md`.

> BRAN locates and cites repository evidence. It does not decide or implement the
> outer task; the outer agent owns all decisions and changes.
> --- `skill/use-bran/SKILL.md`

#### RT-CLM-session-retention
Label: No-session retention claim

Claimed operation: README says no-session disables retention. Evidence layer: doctrine/design. Qualification: host request/echo carries the flag, but unconditional successful-output publication in [RT-RTE-connected-request](#rt-rte-connected-request) prevents a system-wide no-retention conclusion. The account distinguishes host sessions from BRAN-local stored results, rather than inferring retention absence from the option name. SRC-1, `README.md`, `crates/bran-core/src/agent/coordinator.rs`.

> `--tools read,search` limits it to repository read and search. `--no-session`
> disables retention. `--offline` forces the deterministic profile even when a
> profile is configured, so you can always fall back:
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-evidence-supply
Label: Selected evidence into agent context

Consumer: outer agent receiving packet/query JSON, or connected model behind provider port. Channel: selected natural-language evidence plus source identifiers and symbolic receipt; force: evidence supply, not enforced task instruction or guaranteed compliance. Horizon: current reasoning invocation; later explicit queries/retrieval can resupply evidence. Working-context isolation is by bounded request construction, not demonstrated provider conversation isolation. See [RT-RTE-query-packet](#rt-rte-query-packet) and [RT-RTE-connected-request](#rt-rte-connected-request). SRC-1, `skill/use-bran/SKILL.md`, `crates/bran-cli/src/main.rs`.

> 5. Continue the outer task using the cited evidence; keep decisions and
>    implementation with the outer agent.
> --- `skill/use-bran/SKILL.md`

#### RT-BAP-settings-consumption
Label: Retained settings into invocation controls

Consumer: packet and connected setup code. Channel: disk `.bran/settings.conf` decoded into typed settings and request fields. Force: executable configuration of compression/profile/token limits, conditional on the selected path; not a model-interpreted recommendation. Horizon: subsequent invocations in the project until replacement or invalidation. See [RT-RTE-settings-apply](#rt-rte-settings-apply). SRC-1, `crates/bran-cli/src/main.rs`.

> let token_ceiling = settings.as_ref().and_then(|settings| {
>     settings
>         .connected_agent_task_token_ceiling
>         .map(|value| value as usize)
> });
> --- `crates/bran-cli/src/main.rs`

## Annotations

none

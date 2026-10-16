---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "MentisDB runtime baseline: memory admission and read-back, alternate transports, extraction, skill admission and release updates at the frozen Rust/Python boundary."
run-id: AAS-2026-10-14-mentisdb-a8b5903ae3e2-01
reviewed-boundary: "4c9b95041da68c5a26dece9f8776ff54b05b910c"
---

# MentisDB runtime report

## Runtime account

### Work and evidence basis

MentisDB performs memory-service work, not the surrounding agent's task execution. A caller supplies text and identity, the Rust engine admits structured records to a chain, and later requests select retained material for return. It also versions instruction bundles and optionally asks an external model to extract candidate memories. Host agents choose when to call these surfaces and whether returned text changes their behavior. The boundary supplies SRC-1 and the frozen revision; no target program, test, benchmark or provider was executed for this report. Implementation wiring is inspectable; activation and benefit remain unobserved. SRC-1, `src/server.rs`, `src/lib.rs`, `pymentisdb/langchain.py`, `src/llm.rs`.

Additional implementation coverage beyond the boundary's initial trace includes bounded reads of binary stdio dispatch and release installation, REST/MCP authorization, service append/search/context/extraction/skill/branch/merge handlers, core append/open/integrity/derived-flush paths, binary writer flushing, skill upload/persistence/read reconstruction, dashboard PIN and skill upload, CLI backup/search and backup restore staging. The full core operating skill and Python LangChain adapter were read. These are implementation and doctrine/design evidence, not execution records. SRC-1, `src/bin/mentisdb.rs`, `src/server.rs`, `src/lib.rs`, `src/skills.rs`, `src/dashboard.rs`, `src/cli/mod.rs`, `src/backup.rs`, `src/search/fastembed_provider.rs`, `MENTISDB_SKILL.md`, `pymentisdb/langchain.py`.

### Ordinary invocation: admit now, consume later

The shipped operating instruction tells a host agent to discover a chain, bootstrap it, load the skill, reuse an identity, read recent context and checkpoint. It also requests a search before every append. This is natural-language guidance, not a server-enforced prerequisite. The principal can be a model-operated host, a human client or programmatic integration; an `agent_id` in a request is attribution, not proof of that principal's authenticated identity. The next-step owner remains the host. See [RT-RTE-memory-roundtrip](#rt-rte-memory-roundtrip) and [RT-BAP-core-skill](#rt-bap-core-skill). SRC-1, `MENTISDB_SKILL.md`, `src/server.rs`.

For an ordinary REST append, `POST /v1/thoughts` reaches the append service through the REST router. The service resolves the chain, parses type and role, resolves attribution defaults, assembles content, metadata and relations, then takes that chain's write lock. `append_thought` validates positional references, adds reference relations, normalizes metadata and computes the new record's hash from its predecessor. Storage admission precedes in-memory index updates. The service releases the exclusive lock before flushing queued derived state; it then logs the interaction, optionally schedules a host callback and returns thought JSON and the chain head hash. Different cached chains have separate locks; this trace establishes intra-service coordination, not multi-process isolation. SRC-1, `src/server.rs`, `src/lib.rs`.

> self.storage.append_thought(&thought)?;
> --- `src/lib.rs`

That write is not the final possible failure point. Vector-sidecar synchronization, registry persistence and derived flushing occur afterward. Thus an error response is not proof that no thought was admitted, and the inspected path does not roll the canonical append back after every downstream error. This forcing case limits an all-or-nothing interpretation. The binary writer flushes a buffered file to the OS; its inspected helper does not establish power-loss durability. The public API also permits disabling immediate flush and custom storage adapters. SRC-1, `src/lib.rs`, `src/server.rs`.

Later, a recent-context request takes a read lock, selects the newest non-invalidated thoughts, optionally filters attribution, reverses the result into chronological order and returns a catch-up prompt. Ranked search instead assembles a structured query, searches the requested chain plus discovered ancestor chains, deduplicates by UUID, sorts hits by total score, and returns a paginated result with content, scores and provenance fields. It can include invalidated records when requested. This is selected read-back, not automatic delivery to every agent. SRC-1, `src/server.rs`.

The shipped Python consumer is especially consequential: `add_messages` writes every nonempty string message using the same configured attribution and thought type; `get_messages` asks ranked search for at most twenty thoughts of that type without supplying the current user input as search text. It labels a returned message Assistant when its thought's agent ID equals the configured ID, otherwise Human. Original Human/AI message class is not retained by this write path. A load converts the resulting list to a string under `chat_history` by default. Retrieval exceptions become an empty message list. Therefore prompt delivery can silently disappear, and this adapter's reconstructed roles are not a reliable transcript of original speaker roles. Its `session_id` field is not passed by `add_messages` or used in `get_messages`; `clear` is a no-op. This is an implemented producer-and-consumer loop, not evidence that any LangChain agent used it successfully. SRC-1, `pymentisdb/langchain.py`.

> if hit.thought.agent_id == self.agent_id:
>     messages.append(AIMessage(content=content))
> else:
>     messages.append(HumanMessage(content=content))
> --- `pymentisdb/langchain.py`

### Alternate paths and four forcing cases

The capability surface includes direct Rust methods, REST, HTTP/HTTPS MCP, legacy HTTP tool execution, local or proxied stdio MCP, dashboard operations and shipped CLI/Python callers. Binary dispatch includes daemon, headless, stdio and combined modes. The examined CLI search posts to REST; backup/restore use local files. The stdio path probes for a daemon, tries launching one, then proxies requests or falls back to a local service. The local path calls the protocol directly rather than traversing HTTP middleware. These are materially different enforcement envelopes even when they reach equivalent storage operations. SRC-1, `src/bin/mentisdb.rs`, `src/server.rs`, `src/cli/mod.rs`.

Four source-supported challenges shaped this account:

1. **Append acknowledged versus append atomic:** canonical storage append occurs before fallible derived work. The service may return an error after the thought has reached storage. Flush policy and adapter contract also limit durability. This prevents treating error as non-admission or success as unconditional crash-proof persistence. SRC-1, `src/lib.rs`, `src/server.rs`.
2. **Authenticated HTTP versus local/UI paths:** enabled HTTP authorization checks active token scope, but local stdio invokes protocol execution directly, direct Rust callers invoke methods directly, and dashboard upload calls the registry without the service's signature check. PIN authentication is a different gate. Consequently no universal authorization/signature guarantee follows from the service handler. SRC-1, `src/server.rs`, `src/bin/mentisdb.rs`, `src/dashboard.rs`, `src/skills.rs`.
3. **Branch as namespace versus tenant isolation:** ranked search automatically discovers and reads ancestors. The inspected search handler does not reauthorize each discovered ancestor; the HTTP authorizer considers request chain fields, including explicit nested fields, rather than the later discovered traversal. This prevents treating branch keys or scope tags as a demonstrated tenant-isolation boundary. No exploit or deployed breach was observed. SRC-1, `src/server.rs`, `src/lib.rs`.
4. **Extracted candidates versus automatic durable learning:** extraction parses model JSON into candidate inputs and returns them; the service does not append that batch. The caller still owns whether to write. Separately, the LangChain adapter writes messages directly without extraction or per-message review. Therefore neither an extraction review requirement nor automatic extraction can be generalized to every memory-writing route. SRC-1, `src/llm.rs`, `src/server.rs`, `pymentisdb/langchain.py`.

### Guarantees and boundaries of force

**Chain consistency.** Owner: `MentisDb`. Enforcement: record construction, `verify_integrity`, and `open_with_storage`. Strength: invariant for the admitted/reopened representation under the storage contract. Covered paths include callers using the shared append/open methods, not arbitrary filesystem writers or custom adapters' durability internals. Reopening checks indices and canonical hashes, accepts a valid legacy-hash chain through migration, and otherwise rejects failed integrity. It may rewrite migrated data, so append-only describes ordinary thought admission, not an absolute ban on file rewriting. External contract: faithful storage load/write and exclusive/coordinated access to backing files. Implementation conclusion status: wired. Operation conclusion status: uninspected. Hash consistency does not prove factual accuracy, authorship or protection against an actor rewriting a complete chain. SRC-1, `src/lib.rs`.

> if thought.hash != compute_thought_hash(thought) {
>     return false;
> }
> --- `src/lib.rs`

**HTTP access.** Owner: service configuration plus token store. Enforcement: MCP bearer authorizer and REST middleware. Strength: policy conditional on enabling access. Active tokens have read and write capability within accepted scope; there is no separate read-only capability in the inspected authorizer. REST skill/admin/list routes have their own any-active-token classification; it is not identical to explicit chain checks. Required external contract: deployment controls network exposure, credentials, local process/file access and host connections. Implementation conclusion status: wired. Deployment conclusion status: uninspected. The current token grant set, PIN, bind overrides and OS isolation are not supplied. The configuration's loopback defaults are not evidence of a particular deployed envelope. See [RT-RTE-access-control](#rt-rte-access-control). SRC-1, `src/server.rs`, `src/dashboard.rs`.

**Skill signatures.** Owner: service upload handler. Enforcement: registered-agent resolution and Ed25519 verification when that agent has active keys. Strength: conditional invariant on this service path, not universal proof of trustworthy instruction content. Direct registry and dashboard upload bypass that handler; agents without active keys do not trigger its mandatory signature check. Required external contract: key provisioning and secret custody. Implementation conclusion status: wired. Operation conclusion status: uninspected. See [RT-RTE-skill-admission](#rt-rte-skill-admission). SRC-1, `src/server.rs`, `src/skills.rs`, `src/dashboard.rs`.

**Search-before-write and checkpointing.** Owner: host agent interpreting the core skill. Enforcement: natural-language request only. Strength: protocol, not an append invariant. Direct append and Python message writes remain available without demonstrating prior search. Implementation conclusion status: afforded. Operation conclusion status: uninspected. No claim of instruction obedience follows. SRC-1, `MENTISDB_SKILL.md`, `src/server.rs`, `pymentisdb/langchain.py`.

### Context, model components and changes

Context supply is selective: recent-context limits history; ranked search filters and paginates; the Python adapter reconstructs a bounded prompt string. Summary candidates are returned for a caller to use rather than replacing a host context window automatically. The core skill requests checkpointing before host compaction and shared-memory preparation before host sub-agent launches. MentisDB does not thereby own the host's scheduling, isolated frames or actual context eviction. Branches isolate retained namespaces, but ancestor read-back intentionally crosses them. The window receives text by value; a chain key is an external retrieval address, not a live pointer followed automatically by the model. SRC-1, `src/server.rs`, `MENTISDB_SKILL.md`, `pymentisdb/langchain.py`.

The external extraction model and local MiniLM embedding model are separate distributed-parametric components: [RT-CMP-extraction-model](#rt-cmp-extraction-model), [RT-CMP-fast-embed-provider](#rt-cmp-fast-embed-provider). Local weights are used for inference; no training appears in the inspected adapter. Extraction's provider/model selection can change through environment and remote resolution. Exact provider weights are outside the frozen boundary. The default local-embeddings feature attempts MiniLM and can fall back to `LocalTextV1`; startup failure can therefore change the retrieval implementation rather than only fail the request. SRC-1, `src/llm.rs`, `src/search/fastembed_provider.rs`, `src/lib.rs`, `Cargo.toml`.

Change admission is split. Callers admit thoughts through [RT-RTE-memory-roundtrip](#rt-rte-memory-roundtrip), with optional relation-driven invalidation and configured lexical deduplication. Registered service agents or direct registry/UI callers admit instruction versions through [RT-RTE-skill-admission](#rt-rte-skill-admission). Branch/merge and restore admit reorganized/imported retained state through [RT-RTE-state-maintenance](#rt-rte-state-maintenance). Release update installs a product binary through [RT-RTE-release-update](#rt-rte-release-update). None of these mechanisms by itself establishes improved future task capacity, content-directed theory criticism, or exercised self-improvement. Detailed memory revision semantics remain for the memory analyst.

Unresolved implementation details include complete federated/context-bundle transformations, summary builder internals, webhook retries and delivery, all dashboard mutation routes, TUI controls, evaluator answer matching, extension/provider internals and cross-process concurrency. These available but incompletely inspected paths prevent an exhaustive correctness/security/reliability assessment, not the bounded positive route account above. No live grant set, retained chain, model asset, benchmark result or execution trace was supplied. SRC-1, `src/server.rs`, `src/dashboard.rs`, `src/tui.rs`, `src/webhooks.rs`, `src/search/mod.rs`, `lme-benches/longmemeval_bench.py`.

## Shared records

### Components

#### RT-CMP-extraction-model
Label: OpenAI-compatible extraction model

Source-native identity: configured `LlmExtractionConfig.model`, default `gpt-4o`, invoked by `extract_memories_from_text`. Representational form: distributed-parametric model; prompt and returned statements are separate natural-language content with JSON symbolic envelopes. Storage substrate: opaque external provider weights/state, not the chain file. SRC-1, `src/llm.rs`.

Parameters changing during operation: uninspected — this adapter requests inference and contains no parameter-update operation; remote internals are outside the source. Exact version pinned: no; a model name is supplied, not a frozen weight digest. Mutable endpoint resolving to another model: possible; configured base URL/model and remote alias resolution are not fixed by this source. Output returns provider-reported model metadata, which does not pin the parameters. Used by [RT-RTE-memory-extraction](#rt-rte-memory-extraction).

> const DEFAULT_LLM_MODEL: &str = "gpt-4o";
> --- `src/llm.rs`

#### RT-CMP-fast-embed-provider
Label: FastEmbed MiniLM provider

Source-native identity: `FastEmbedProvider`, `EmbeddingModel::AllMiniLML6V2`; metadata reports provider ID `fastembed-all-minilm-l6-v2`, dimension 384, version label `1`. Representational form: distributed-parametric weights and dense embedding outputs. Storage substrate: downloaded/cached model via dependency; managed vector sidecars are derived chain state. SRC-1, `src/search/fastembed_provider.rs`, `src/lib.rs`.

Parameters changing during operation: no parameter-update path in the inspected adapter; it calls embedding inference under a mutex. Dependency internals remain uninspected. Exact version pinned: model-family enum and space label are set, but no exact model artifact hash is pinned in this adapter. Mutable endpoint resolving to another model: no runtime remote inference endpoint here; first-use download/cache artifact resolution remains dependency-controlled. Feature and initialization failure can select `LocalTextV1` instead, a distinct provider, not proof of mutable MiniLM weights. Used by the service's chain-open/search path in [RT-RTE-memory-roundtrip](#rt-rte-memory-roundtrip).

> log::warn!("FastEmbed provider init failed, falling back to LocalTextV1: {e}");
> --- `src/lib.rs`

### Operative objects

#### RT-OBJ-thought
Label: Thought record envelope

Source-native identity: `Thought`, UUID, index, agent attribution, predecessor hash and canonical hash. Representational form: symbolic envelope consumed by fixed indexing/filter/hash rules. Storage substrate: configured `StorageAdapter`, ordinarily binary chain files; in-memory indexes are derived. Natural-language `content` is a distinct operative part whose meaning the envelope does not validate. Evidence: SRC-1, `src/lib.rs`, `src/server.rs`. The memory analyst may separately declare the content part and its revision paths.

> let index = self.thoughts.len() as u64;
> --- `src/lib.rs`

#### RT-OBJ-skill-registry
Label: SkillRegistry version store

Source-native identity: `SkillRegistry` containing `SkillEntry` versions, lifecycle status and content hashes. Representational form: symbolic version/lifecycle machinery; reconstructed instruction bodies have natural-language authority only when interpreted by a consumer. Storage substrate: bincode registry persisted through temporary-file write and rename; versions use an initial full body and later diff patches. Evidence: SRC-1, `src/skills.rs`.

> let temp_path = path.with_extension("bin.tmp");
> fs::write(&temp_path, payload)?;
> fs::rename(&temp_path, path)?;
> --- `src/skills.rs`

#### RT-OBJ-core-skill
Label: Embedded MentisDB operating skill

Source-native identity: root `MENTISDB_SKILL.md`, embedded as `MENTISDB_SKILL_MD` and exposed as `mentisdb://skill/core` and tool/HTTP responses. Representational form: natural-language operating instructions, with symbolic frontmatter and tool identifiers. Storage substrate: source Markdown compiled into the binary; any host-local saved copy depends on the host following its instruction. This is static shipped material, not accumulated read-back. Evidence: SRC-1, `MENTISDB_SKILL.md`, `src/server.rs`, `src/bin/mentisdb.rs`.

> const MENTISDB_SKILL_MD: &str = include_str!("../MENTISDB_SKILL.md");
> --- `src/server.rs`

### Routes

#### RT-RTE-memory-roundtrip
Label: Caller memory admission and later context return

Endpoints/progression: host or Python caller → REST/MCP append service → chain/storage → later recent-context or ranked-search request → host prompt material. Direct Rust append is an alternate entry. Owner: caller owns timing and content; service owns parsing, chain locking and transport response; core owns record construction and storage admission. Symbolic query rules choose records; their content is interpreted downstream. SRC-1, `src/server.rs`, `src/lib.rs`, `pymentisdb/langchain.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: admitted thought JSON and head hash, or error; later context call returns catch-up prompt or scored hit list.
- Later read-back: retained thoughts are reloaded on open and selected by later requests; the Python adapter formats hits under its memory variable.
- Delegated visibility: agents sharing accessible chains can request the same state; branch ranked search includes ancestor hits. Host sub-agent supply is instructed, not observed.
- Selection predicate: caller chain/filter/text/graph/time options; recent-context defaults to last twelve non-invalidated records; Python adapter requests twenty of its configured thought type with no text query.
- Invalidation or expiry: invalidating relations affect default retrieval; callers can request invalidated records. Canonical thought history is not deleted by adapter clear.
- Activation or effect: storage/index updates are wired; prompt delivery is wired in the Python adapter; changed host reasoning or action is uninspected.
- Evidence limits: source trace only; custom adapter semantics, host scheduling, deployed credentials, cross-process races and task benefit are not established.

Admission account: open caller requests propose content. Service/core code decides schema/reference admission; caller can refrain, HTTP authorization can veto where enabled, and storage can reject I/O. No universal human per-content approval is implemented by this route. Search-before-write guidance can shape a host proposal but is not checked by append. Optional deduplication adds a `Supersedes` relation using token-set similarity, not a human truth judgment. Recovery is explicit later correction/invalidation, reopening and backup/restore; no unconditional rollback after post-write errors is shown. Answer oracle: inapplicable — no expected-answer reference is used to decide ordinary append. Operating mode: open requests and automatic Python message writes; improvement triggers are host-selected lessons/checkpoints/corrections, not a server-controlled learning curriculum. SRC-1, `MENTISDB_SKILL.md`, `src/lib.rs`, `src/server.rs`, `pymentisdb/langchain.py`.

> guard.defer_next_derived_flush();
> --- `src/server.rs`

> chain.read().await.flush_pending_derived()?;
> --- `src/server.rs`

#### RT-RTE-access-control
Label: HTTP authorization and alternate local access

Endpoints/progression: incoming HTTP request → enabled-token check and route/payload scope classification → service execution or rejection. Owner: configuration/operator controls enabling and token issuance; Rust authorizer decides admissibility. Alternate local stdio dispatch and direct library calls bypass HTTP middleware; dashboard uses PIN/session checks. Context/state effects include binding omitted request chain keys for single-chain tokens; no content-quality review follows. SRC-1, `src/server.rs`, `src/bin/mentisdb.rs`, `src/dashboard.rs`, `src/auth.rs`.

- implementation conclusion status: wired
- deployment conclusion status: uninspected
- Immediate return: authorized operation result or authentication failure; dashboard failure redirects to login.
- Later read-back: token records govern later requests; this is access-control configuration, not memory content returned to a model.
- Delegated visibility: any holder of an active scoped token receives the corresponding accepted HTTP capabilities; actual delegates and grants are uninspected.
- Selection predicate: access-enabled flag, active token, route class and explicit request chain fields; dashboard alternatively checks configured PIN or live session token.
- Invalidation or expiry: revoked tokens cease active authorization; dashboard sessions expire by timeout. Deployed revocations are uninspected.
- Activation or effect: code permits or blocks HTTP dispatch; it does not sandbox an authorized callback, local process or filesystem writer.
- Evidence limits: not a complete security audit; discovered ancestor-chain access and any-active-token REST skill classifications limit stronger isolation conclusions.

Decision roles: operator issues/revokes tokens, code checks credentials, requesting caller selects operation. Human per-content approval is not supplied by this authentication gate. Answer oracle: inapplicable — scope/credential rules are policy, not answer references. Operating mode: request-by-request policy enforcement, conditional on configuration. Guarantee strength: policy. No deployed grant set or isolation envelope is evidenced.

> // Tokens are full-access (read + write) within their scope. There is no
> // separate read-only capability in the CLI or dashboard.
> --- `src/server.rs`

> match protocol.execute(&canonical, arguments).await {
> --- `src/bin/mentisdb.rs`

#### RT-RTE-memory-extraction
Label: Opt-in candidate extraction

Endpoints/progression: caller text/template → extraction service or direct extraction function → configured external model → JSON parser/validation → candidate `ThoughtInput` list. Owner: caller triggers and optionally supplies template; model proposes statements; parser accepts schema-shaped candidates; caller owns subsequent append. Context: system memory-analyst message plus text/template user message; no enclosing task-agent tool loop is implemented here. Uses [RT-CMP-extraction-model](#rt-cmp-extraction-model). SRC-1, `src/server.rs`, `src/llm.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: candidate thoughts, reported model and token usage, or configuration/API/parse error.
- Later read-back: inapplicable — this extraction path does not persist candidates; separate caller append is required for retained read-back.
- Delegated visibility: uninspected — remote provider receives submitted text, but provider retention and third-party visibility are outside the source.
- Selection predicate: supplied text and optional template, first response choice, structured thoughts array and schema transformation.
- Invalidation or expiry: inapplicable — transient candidate return has no durable lifecycle in this route.
- Activation or effect: remote inference and candidate conversion are wired; memory admission and downstream behavior are separate operations.
- Evidence limits: prompt conservatism is requested, not verified factuality; provider internals, execution and caller review remain uninspected.

Proposal guidance: default prompt asks concise independently meaningful statements, conservative extraction and specific types. Rejection ability: missing credentials, failed provider request, malformed JSON or schema mismatch produce errors; a caller can discard candidates. Rollback: inapplicable before durable append. Answer oracle: inapplicable — no reference answer is used. Operating mode: open, opt-in extraction requests, not autonomous batch learning. Human contribution: unspecified caller may review, but no per-candidate approval event is required by this service before it returns candidates. SRC-1, `src/llm.rs`, `src/server.rs`.

> let thoughts = validate_and_transform_thoughts(extracted.thoughts)?;
> --- `src/llm.rs`

#### RT-RTE-skill-admission
Label: Skill upload, version reconstruction and return

Endpoints/progression: service upload request → registered-agent lookup → conditional signature check → registry import/validation/version append/persist → later search/read → reconstructed exported skill text. Alternate dashboard and direct registry callers reach registry upload without the service signature gate. Owner: caller authors and chooses upload; service validates identity/signature where applicable; registry handles versions. Uses [RT-OBJ-skill-registry](#rt-obj-skill-registry). SRC-1, `src/server.rs`, `src/skills.rs`, `src/dashboard.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: latest skill summary with identity/version/status metadata, or error.
- Later read-back: later read reconstructs a requested version or the latest from stored full/delta content, parses and exports it in requested format.
- Delegated visibility: callers with route access can search/read the registry; actual host loading and adherence are not observed.
- Selection predicate: explicit skill/version IDs for read, query filters for search; omitted version selects latest, not a proven best version.
- Invalidation or expiry: deprecate/revoke/delete APIs change lifecycle or remove state; inspected read reconstruction does not itself reject a revoked entry. Upload reactivates non-revoked entries.
- Activation or effect: instruction versions and indexes change; a returned skill body can guide a host interpreter, but installation/obedience is not guaranteed.
- Evidence limits: service signature checks do not cover dashboard/direct registry admission; atomic rename is not a complete multi-process transaction or crash-durability proof.

Admission account: trigger is explicit upload; proposed change is instruction content. Service agents with active keys require a valid content signature, while registry import and document validation enforce structure, not quality. Dashboard admission accepts its supplied agent ID directly. Human approval of each version is unresolved; UI availability is not proof of human authorship. Caller can withhold upload, code can reject invalid input/signature, and later lifecycle changes can retire content. Recovery includes reading earlier version IDs; automatic behavioral rollback is not shown. Guidance shaping each uploaded proposal is uninspected — no concrete live uploaded skill was supplied. Answer oracle: inapplicable — no reference task result selects a version. Operating mode: open uploads; persistence retains bodies/patches and provenance, not demonstrated criticism of a theory. SRC-1, `src/server.rs`, `src/skills.rs`, `src/dashboard.rs`.

> verify_ed25519_signature(&key.public_key_bytes, request.content.as_bytes(), sig_bytes)
>     .map_err(Box::<dyn Error + Send + Sync>::from)?;
> --- `src/server.rs`

> let summary = skills.upload_skill(upload).map_err(internal_error)?;
> --- `src/dashboard.rs`

#### RT-RTE-state-maintenance
Label: Explicit branch, merge and archive restoration

Endpoints/progression: branch request → core branch operation → cached new chain; merge request → source-to-target remapped thought inputs → sequential append → source deregistration after success; restore archive → manifest/checksum/path checks → staging → target file copies/import reconciliation. Owners: requesting caller chooses target/source/archive; Rust code transforms and writes; CLI operator can confirm restore. These mechanisms admit retained-state changes, not product improvement. SRC-1, `src/server.rs`, `src/backup.rs`, `src/cli/mod.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: branch IDs, merge result, or restore success/error and CLI report.
- Later read-back: changed chains/files are available to later reopen and search; branch searches can traverse ancestor chains.
- Delegated visibility: clients selecting accessible target/branch keys can retrieve resulting state; branches are not proven tenant isolation.
- Selection predicate: explicit source/target keys, branch anchor, archive manifest and overwrite/import policy; merge copies source thoughts rather than selecting a demonstrated superior subset.
- Invalidation or expiry: successful merge deregisters source; errors retain source but may leave a target prefix appended. Restore applies requested overwrite/import behavior.
- Activation or effect: retained state changes, including transformed attribution on merge; downstream model effects remain uninspected.
- Evidence limits: no transaction-wide rollback demonstrated; full restore conflict reconciliation and every metadata loss case were not inspected.

Admission account: explicit requests propose branch/import/merge. Software decides structural checks and deterministic transformations; caller can cancel before invoking. Merge maps exact agent IDs first, otherwise compares character-set Jaccard similarity with thought-count tie-breaking. It creates inputs from content/type/role/importance/confidence/tags/concepts; the inspected copy does not carry the original relations or positional refs into the target. Thus an ordinary successful merge is not an identity-preserving replay of all source graph metadata. Restore verifies the archive before writes and uses staging, but copy failure is not evidence of whole-instance rollback. The CLI attempts daemon flush for backup and proceeds with a warning on some failures; successful probing blocks restore while daemon is running. Library callers do not inherit every CLI guard. Guidance shaping proposed content and any expected-answer oracle are inapplicable — these are administrative structural operations. Operating mode: explicit administration. SRC-1, `src/server.rs`, `src/backup.rs`, `src/cli/mod.rs`.

> // Verify all checksums before writing anything
> --- `src/backup.rs`

> // All thoughts successfully appended — evict source from the cache and
> // deregister it from disk.
> --- `src/server.rs`

#### RT-RTE-release-update
Label: Release binary admission through Cargo

Endpoints/progression: explicit update/force-update command → latest-release fetch → version comparison/optional human prompt → `cargo install` for selected repository tag with locked dependencies and forced binary replacement → restart instruction. Owner: operator initiates; code selects release metadata and executes Cargo; external repository/build tool supplies the product. SRC-1, `src/bin/mentisdb.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: current/up-to-date/skipped/installed notice or fetch/build/location error.
- Later read-back: inapplicable — this installs executable organization, not accumulated memory returned by retrieval.
- Delegated visibility: uninspected — remote release service and Cargo obtain requests; build-time dependency behavior is not frozen.
- Selection predicate: latest release and newer-version comparison in ordinary mode; force mode bypasses enabled/version/prompt conditions shown in the ordinary path.
- Invalidation or expiry: forced installation replaces the installed binary; restart is required to use it in the standalone path.
- Activation or effect: external installation command is wired; no installed new version or subsequent execution was observed.
- Evidence limits: reviewed implementation only; fetched future release code, supply-chain authenticity and rollback are not established.

Admission account: proposed product change is a published release, not a memory-derived patch. Ordinary update requires interactive acceptance and refuses unattended prompting; force-update is explicitly initiated without that per-release confirmation. Code detects failed Cargo execution and locates the installed binary; a successful install is not a causal quality assessment. Answer oracle: inapplicable — version ordering is not reference task performance. Operating mode: operator-directed maintenance. Recovery/rollback: no automatic restoration of an older binary demonstrated in this path. No self-improvement attribution is made: runtime evidence does not determine a locally generated improvement, and subsequent improved operation is unobserved. SRC-1, `src/bin/mentisdb.rs`.

> let status = Command::new(&cargo)
>     .args(build_cargo_install_args(tag, repo))
>     .status()?;
> --- `src/bin/mentisdb.rs`

### Claims

#### RT-CLM-startup-protocol
Label: Claimed mandatory memory startup

Claimed operation: host agents must discover/reuse chain and identity, load skill and recent state, then checkpoint; search precedes writes. Source: SRC-1, `MENTISDB_SKILL.md`. Doctrine conclusion status: claimed. Operation conclusion status: uninspected. The direct service and Python write paths challenge any inference that this prescription is universally enforced. See [RT-RTE-memory-roundtrip](#rt-rte-memory-roundtrip).

> **READ BEFORE WRITE.** Never skip steps 1–5.
> --- `MENTISDB_SKILL.md`

#### RT-CLM-extraction-review
Label: Claimed caller review of extraction

Claimed operation: callers review/validate and optionally sign untrusted candidate inputs before durable append. Source: SRC-1, `src/llm.rs`. Doctrine conclusion status: claimed. Implementation conclusion status: wired for separation of extraction return from service append, not for actual caller review. Operation conclusion status: uninspected. See [RT-RTE-memory-extraction](#rt-rte-memory-extraction).

> //! LLM output is **untrusted**. The returned [`ExtractionResult`] contains
> //! [`ThoughtInput`] records that callers must review, validate, and
> //! optionally sign before appending to a chain.
> --- `src/llm.rs`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-core-skill
Label: Core operating instruction delivery to host agents

Consumer: external host model/agent. Channel: embedded MCP resource, skill tool/HTTP return, and requested host-local global skill copy. Force: natural-language instruction, conditional on host interpretation; it does not enforce the prior-search/identity/compaction policy inside append. Horizon: current host invocation and potentially later projects/sessions if the host saves the requested copy. Static shipped material is not accumulated read-back. Evidence: SRC-1, `MENTISDB_SKILL.md`, `src/server.rs`, `src/bin/mentisdb.rs`. Delivery is wired; local saving, compliance and benefit are uninspected. Object: [RT-OBJ-core-skill](#rt-obj-core-skill).

> After every call to `mentisdb_skill_md`, **write the returned content to your harness's global skill store, replacing any older file already there**.
> --- `MENTISDB_SKILL.md`

#### RT-BAP-retained-context
Label: Returned memories and skills as host guidance

Consumer: host model/human reading returned thoughts, catch-up prompt, reconstructed skill or Python memory variable. Channel: MCP/REST response and prompt-string formatting. Force: natural-language knowledge or instructions at the downstream interpreter; symbolic filters/version selection determine what reaches it, not whether it is obeyed. Horizon: later invocations/sessions while records/versions remain retrievable. Evidence: SRC-1, `src/server.rs`, `src/skills.rs`, `pymentisdb/langchain.py`. The implementation wires retained read-back; neither changed behavior nor demonstrated benefit is observed. Routes: [RT-RTE-memory-roundtrip](#rt-rte-memory-roundtrip), [RT-RTE-skill-admission](#rt-rte-skill-admission).

> formatted = self._format_messages(messages)
> return {self.memory_key: formatted}
> --- `pymentisdb/langchain.py`

## Annotations

none

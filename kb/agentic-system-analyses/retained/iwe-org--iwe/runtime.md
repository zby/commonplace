---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "IWE runtime baseline: local document commands, MCP persistence, editor reload and host-dependent memory procedures."
run-id: AAS-2026-11-08-iwe-923f804db3b4-01
reviewed-boundary: "930c184b7cc8508d207e6ca7999ca6e415bc02ac"
---

# IWE runtime report

## Runtime account

IWE supplies a document and context service, not the agent's next-token or next-tool loop. The external human or agent selects commands; deterministic Rust code parses, selects, transforms and persists documents. Agent-facing instructions add a proposed capture and maintenance protocol. They do not turn the store into an enclosing permission system. The source basis is SRC-1 at the boundary's frozen commit. Implementation below means inspected wiring, not a successful execution. No supplied operational trace, deployment grant configuration or causal experiment establishes activation or benefit.

### Ordinary shipped invocation

An ordinary write is `iwe create <key> --strict --content <document>`, followed later by `iwe retrieve -k <key>`. The caller supplies the identity and Markdown; CLI dispatch loads configuration, derives the workspace, prepares content or a configured template, normalizes it, optionally validates the pending document, writes it and prints its path. An optional editor launch follows the write. The process exits rather than owning an autonomous continuation. Another CLI invocation reloads the filesystem into a graph, selects seeds and expansions, budgets the result and renders it. See [RT-RTE-cli-document](#rt-rte-cli-document) and [RT-RTE-document-retrieval](#rt-rte-document-retrieval). SRC-1, `crates/iwe/src/main.rs`.

The principal is the OS process's caller. Key identity is distinct from title; configuration binds the workspace, format, templates and schemas. Neither the code's caller identity nor use of `--strict` demonstrates human approval of a particular fact. The executor's effect boundary is ordinary local filesystem authority, not model-specific isolation. Disk files survive the process; graph state is reconstructed on later CLI invocations. CLI writes and MCP writes can reach the same store, while an editor may hold a different unsaved buffer.

### Material alternate routes and forcing cases

1. **Omit `--strict`, or use body replacement rather than mutation operators.** Create validates only when requested. Body replacement with strict validates changed output but does not pass through mutation mode's requirement for document/block `expect` guards. Both are supported CLI paths, not hypothetical library callers. This defeats a system-wide interpretation of either mandatory schema admission or mandatory expected-count guards. SRC-1, `crates/iwe/src/main.rs`.
2. **Use MCP instead of CLI.** `iwe_create` and `iwe_update` validate pending content without a strict option; generic `iwe_query` checks mutating operation guards before inspecting `dry_run`, validates resulting documents and persists only when not previewing. Existing-key create with `if_exists: skip` returns without validating the supplied replacement because it writes nothing. Thus skip is not a schema-checked replacement. See [RT-RTE-mcp-document](#rt-rte-mcp-document). SRC-1, `crates/iwec/src/lib.rs`.
3. **Edit files outside the capture procedure.** The post-tool helper reads already-written files and emits corrective context for selected host tools; the LSP admits buffer text and later disk state. Neither consults a per-content selection decision from distill. This defeats the prompt's literal exclusivity claim, without establishing that any particular deployed agent disobeys it. See [RT-RTE-editor-reload](#rt-rte-editor-reload). SRC-1, `crates/iwe/src/internal/claude/hook/post_tool.rs`, `crates/iwes/src/router/server.rs`.
4. **Select versus expand retrieval.** CLI search filters seed candidates; nonsearch filters intersect explicit seeds or supply them when empty. The reader then expands edges and applies `exclude` to emitted document keys. The seed filter is not reapplied to every expanded document. This is a selection facility, not an authorization boundary. No universal exclusion guarantee is inferred for backlink or parent metadata. See [RT-RTE-document-retrieval](#rt-rte-document-retrieval). SRC-1, `crates/iwe/src/main.rs`, `crates/diwe/src/retrieve.rs`.

These are static forcing cases. No malformed input, concurrent deployment, symlink attack, host permission configuration or real user interaction was executed. Path-component rejection in the shared filesystem layer is not evidence of an OS sandbox or symlink containment. SRC-1, `crates/diwe/src/fs.rs`.

### Control ownership and reliability

| Control | Owner and enforcement point | Strength and covered paths | External contract and limit |
| --- | --- | --- | --- |
| Schema admission | CLI `gate_pending`; MCP `ensure_schema_clean` before persistence | invariant for reaching these checked branches, conditional on configured bindings; CLI opt-in, inspected MCP create/update/query mandatory | Schemas must bind and express the desired constraints. Structural acceptance does not certify truth, human selection or usefulness. Implementation conclusion status: wired. Operation conclusion status: uninspected. |
| User selection before capture | External agent following distill's ask/write order | protocol, not universal storage invariant; named user instructions are another selection mode, unattended work normally stages only | Host must deliver instructions and model must comply; CLI, MCP and editor paths do not require a selection token. Implementation conclusion status: afforded. Operation conclusion status: uninspected. |
| MCP memory/disk consistency after write error | `persist_changes` reloads affected keys from disk on error; graph mutation follows successful disk writes | best effort recovery, not an all-files transaction | Filesystem writes can partially complete; process-local graph lock does not serialize other processes. Implementation conclusion status: wired. Operation conclusion status: uninspected. |
| Editor working-copy ownership | LSP open-document set suppresses external reload; close releases ownership and reloads | invariant within the inspected handlers | Editor client supplies notifications and applies edits; this is not durable conflict resolution across clients. Implementation conclusion status: wired. Operation conclusion status: uninspected. |

The filesystem applies removals, creates and updates sequentially. An error returns after preceding effects, with no transaction-wide rollback in the inspected function. MCP recovers its graph from disk rather than undoing successful files. Warning generation follows persistence, so similarity warnings are not vetoes. SRC-1, `crates/diwe/src/fs.rs`, `crates/iwec/src/lib.rs`.

MCP loads a graph into `Arc<RwLock<Graph>>`, starts a filesystem watcher and serves stdio by default, or HTTP at `/mcp` with default loopback host. The inspected HTTP setup constructs a router without an application authentication gate. This is not proof of a secure public deployment; caller-specified binding and external network controls matter. There is no model invocation in these traced CRUD/retrieval handlers. External agents own provider selection, model versions, permissions, tool scheduling, subprocesses, remote workers and conversation compaction. No exact model or deployed grant set can be inferred from the string “Claude.” SRC-1, `crates/iwec/src/main.rs`, `crates/iwec/src/lib.rs`; the model-free product declaration is retained in [boundary](boundary.md#boundary-and-evidence).

### Host-dependent memory loop

The shipped procedure is read → stage → select → write → record, with later session-start discovery. [RT-RTE-session-capture](#rt-rte-session-capture) distinguishes code bookkeeping from the host's proposing and selection behavior. [RT-RTE-session-index](#rt-rte-session-index) delivers a filtered index and optional policy section, not every stored body. [RT-RTE-policy-maintenance](#rt-rte-policy-maintenance) requests user-mediated changes to the write policy and taxonomy. These are distinct from deterministic schema checks. Actual retained content, its revisions and the full memory inventory belong to the memory analysis.

Working-context control consists here of bounded transcript windows, proposed per-session subagent isolation, selected index projections and later explicit retrieval. Subagents are requested by the prompt; IWE does not implement a worker runtime. The proposed isolated reader receives a session ID and selected policy sections, writes its session's inbox, and stops before admission. What crosses back is durable staged candidates rather than the reader's whole working context. This resembles an isolated frame only at the procedural level: neither launch, host window ownership nor frame disposal is enforced here. Transcript pointers and inbox state permit resumption after host compaction, but IWE does not itself trim the host conversation. SRC-1, `crates/iwe/templates/claude/prompts/distill.md`, `crates/iwe/src/internal/claude/session.rs`, `crates/iwe/src/internal/claude/hook/index.rs`.

### Added inspection coverage

Beyond the boundary's initial scope this member inspected CLI create, preparation, retrieval, graph loading and both update modes; MCP create/update/query, schema/error recovery, startup transports and server construction; shared filesystem path and mutation logic; `crates/diwe/src/retrieve.rs` selection/expansion/output construction; LSP open/close and external reload handlers; session read/stage/complete and record serialization; the complete distill/reflect prompts, memory-index template and index renderer; and post-tool report production. All are SRC-1 implementation or embedded doctrine/design, not additional sources or observed runs. Dependency internals, watcher timing, all refactoring transformations, init variants and all retrieval renderer metadata paths were not exhaustively traced; this report makes no universal safety or full transactional claim for them.

## Shared records

### Components

none declared in this member

No distributed-parametric component is implemented by the inspected paths. Model-backed interpretation occurs in the excluded host. Its parameter changes, exact version and mutable endpoint resolution remain uninspected; a stable model label would not pin weights.

### Operative objects

#### RT-OBJ-graph
Label: Workspace graph

Source-native identity: `Graph`, constructed from workspace files by CLI loading and MCP startup. Representational form: symbolic document keys, graph edges and parsed structures; natural-language document payload is interpreted by human/model consumers, not by graph indexing alone. Storage substrate: process memory, reconstructed from ordinary Markdown or configured-format filesystem documents. MCP holds a shared read/write lock; this does not govern external process writes. SRC-1, `crates/iwe/src/main.rs`, `crates/iwec/src/lib.rs`.

> graph: Arc::new(RwLock::new(graph)),
> base_path: Some(workspace),
> --- `crates/iwec/src/lib.rs`

#### RT-OBJ-session-record
Label: Session record bookkeeping

Source-native identity: `SessionRecord`; pending proposals, progress, captures and rejection ledger are outside the document graph. Representational form: symbolic YAML fields with natural-language candidate/evidence/rejection payloads. Storage substrate: files under `.iwe/claude/`, serialized using `serde_yaml` and overwritten by `save_session_record`. This is a progress/admission record, not proof that a user made a selection. SRC-1, `crates/iwe/src/internal/claude/record.rs`, `crates/iwe/src/internal/claude/session.rs`.

> Ok(serialized) => std::fs::write(path, serialized).is_ok(),
> --- `crates/iwe/src/internal/claude/record.rs`

### Routes

#### RT-RTE-cli-document
Label: CLI document admission

The human or external agent supplies the proposed key/content or template variables. CLI code decides argument validity, prepares and normalizes the document, optionally applies schema admission, then writes. In create content mode it requires explicit identity and rejects overwrite mode; template mode can compose a configured template. Update has separate body-overwrite and structured mutation paths. The caller controls the change; there is no software test of per-fact human consent. Schema failure can reject a strict write. Operating mode: open caller requests; answer oracle: inapplicable — schema predicates are structural checks, not a reference answer. Recovery: report/exit on error; no multi-document undo demonstrated. Guidance comes from caller content, configured templates and optionally the host's policy prompt; persistent result is the filesystem document. SRC-1, `crates/iwe/src/main.rs`, `crates/diwe/src/fs.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: create prints the resulting path; update prints changed/unchanged or preview reporting unless quiet.
- Later read-back: subsequent CLI loads and server reload paths can consume written documents.
- Delegated visibility: inapplicable — CLI implements no agent delegation; host controls who receives stdout and files.
- Selection predicate: explicit key/content or configured template for create; key/filter and operators for mutation updates; body replacement requires one key.
- Invalidation or expiry: caller-controlled update/delete; no automatic lifetime shown in these functions.
- Activation or effect: filesystem create/overwrite and normalization are wired; downstream behavioral activation is unobserved.
- Evidence limits: strict validation is conditional; body mode does not enforce mutation-mode count guards; no supplied execution or rollback result.

> if args.strict {
>     gate_pending(&config, &[(prepared.key.clone(), prepared.content.clone())]);
> }
> --- `crates/iwe/src/main.rs`

> if args.strict && !args.dry_run {
>     enforce_strict_update(doc_expect.is_some(), &update_doc);
> }
> --- `crates/iwe/src/main.rs`

#### RT-RTE-document-retrieval
Label: Document selection and retrieval

CLI caller chooses key/filter or lexical/fuzzy search, expansion depths, output format and budgets. The command loads the graph and optionally a lexical index; `DocumentReader::retrieve_many` filters seed keys, truncates seed count, traverses requested edge directions, deduplicates and excludes keys, builds document outputs, then applies document budgets. Code owns ranking/traversal; the host or human chooses what to do next. Forms: symbolic predicates and keys over text/graph structures, returning natural-language bodies plus symbolic metadata. SRC-1, `crates/iwe/src/main.rs`, `crates/diwe/src/retrieve.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: rendered Markdown, serialized JSON/YAML documents or keys, plus truncation warning where applicable.
- Later read-back: retained documents from earlier writes become current invocation input; retrieval itself does not revise their content.
- Delegated visibility: uninspected — external caller decides which agent receives returned material.
- Selection predicate: explicit/filter-derived seeds or ranked lexical/fuzzy candidates; independently requested graph expansions; exclude applies to emitted document keys.
- Invalidation or expiry: fresh CLI graph load reflects current disk state; caller updates/deletes content separately.
- Activation or effect: context supply only; no observed compliance or answer improvement.
- Evidence limits: seed filter is not a mandatory predicate on all expanded documents; metadata edges have separate construction rules; no universal confidentiality claim.

> for key in &effective_keys {
>     let keys_to_process = self.collect_document_keys(key, options);
>
>     for doc_key in keys_to_process {
>         if seen_keys.contains(&doc_key) || options.exclude.contains(&doc_key) {
>             continue;
>         }
> --- `crates/diwe/src/retrieve.rs`

#### RT-RTE-mcp-document
Label: MCP document admission

An external MCP client invokes tools against the server's shared graph. Create requires complete content and explicit key; nonempty template/variables/frontmatter options are rejected rather than silently honored. Create skip at an existing identity returns `created: false`. Update checks existence, validates proposed content and persists it. Generic query parses an operation, checks mutation guards, executes symbolically, validates pending content and conditionally persists. These are software admission checks; no human-selection control is required by these handlers. Operating mode: open tool requests; proposer/decider is the external caller for content, server for admissibility; answer oracle: inapplicable — guards and schemas test structure/count, not semantic correctness. Rejection returns MCP errors; persistence failure reloads affected graph keys from disk, without undoing earlier file effects. SRC-1, `crates/iwec/src/lib.rs`, `crates/iwec/src/main.rs`, `crates/diwe/src/fs.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: tool JSON/text result, errors or post-write warnings; query dry-run returns proposed changes without persistence.
- Later read-back: successful writes enter disk and the server graph for later tools/resources and other readers.
- Delegated visibility: same shared server graph is reachable by clients of that server; host permissions and client isolation remain external.
- Selection predicate: tool arguments, key existence, operation filters, required guards and configured schema bindings.
- Invalidation or expiry: later mutation/deletion and filesystem watching; process lifetime bounds in-memory state.
- Activation or effect: document persistence plus graph update; schema warnings and similarity warnings are not semantic proof.
- Evidence limits: inspected create/update/query controls do not establish every alternative tool's complete guard coverage; no deployed authentication/isolation or concurrency run supplied.

> self.ensure_schema_clean(&[(key.clone(), markdown.clone())])?;
>
> self.persist_changes(&mut graph, &Changes::new().create(key.clone(), markdown))?;
> --- `crates/iwec/src/lib.rs`

> "template mode is not yet supported; pass the complete document in 'content'"
> --- `crates/iwec/src/lib.rs`

> Self::apply_changes(graph, changes);
> Ok(())
> --- `crates/iwec/src/lib.rs`

#### RT-RTE-session-capture
Label: Session capture procedure

Trigger: a user asks to remember named content or to distill selected sessions. The host agent proposes candidates under the store policy and deduplicates them; the user selects/edits/skips; the host agent writes through strict CLI calls and records outcomes. Unattended execution is instructed to stage only except for an item already named in the instruction. The code reads bounded transcript chunks, parses/stages proposals and saves session records; it does not itself ask a human or certify selection. Completion resolves written links, may link area hubs, advances progress and settles/drops pending proposals. Operating mode: open user requests, with procedural bounded transcript windows. Answer oracle: user selection governs admission, not an expected-answer oracle for factual correctness. SRC-1, `crates/iwe/templates/claude/prompts/distill.md`, `crates/iwe/src/internal/claude/session.rs`, `crates/iwe/src/internal/claude/record.rs`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: transcript window/candidate inbox or bookkeeping report; final procedure asks the agent to list keys and backlog.
- Later read-back: inbox and session progress permit resumed capture; written documents can enter later retrieval/index delivery; rejection ledger can inform policy proposals.
- Delegated visibility: prompt requests one subagent per session for multiple sessions, supplied selected policy sections and knowledge filter, stopping after staging; launch and returned context are host-owned.
- Selection predicate: policy-guided candidate proposal and dedup, then explicit user selection or a named remember instruction; code staging is not equivalent to that decision.
- Invalidation or expiry: session completion settles by written key/rejected title and can reject remaining pending candidates; explicit adopt marks progress without reading, per procedure.
- Activation or effect: stage writes bookkeeping outside the graph; strict CLI writes admit retained documents separately; subsequent behavioral effect is unobserved.
- Evidence limits: the instruction's exclusivity is not a filesystem invariant; subagent isolation and compliance are unobserved; progress saves are not transactional with document writes.

Recovery is resumable rather than transactional: durable inbox entries can be revisited after interruption, but document writes and subsequent completion are separate operations. The decision roles are separated in prose, not protected by separate credentials. Guidance retained is the policy, candidate evidence and rejection/write records, not changed model parameters.

> Nothing is written until every candidate has its answer (§6), and **skipping everything is a valid and common answer** — take it without argument and never re-propose the same items. Never open with the whole set as prose, and never make the user retype a title.
> --- `crates/iwe/templates/claude/prompts/distill.md`

> record.stage_proposal(proposal);
> let pending = record.pending_proposals().len();
> --- `crates/iwe/src/internal/claude/session.rs`

#### RT-RTE-session-index
Label: Session start context delivery

The host invokes the helper with a JSON payload. CLI reads `cwd` and session identity, opens the configured graph only if a `MEMORY` document exists, renders the memory index and prints it if present. Configured injection slices choose/filter/sort documents; code deduplicates across slices and excludes `MEMORY` and `queries` from listed document entries. Default projection is title/key, with sort field added when applicable. The template includes the optional policy section separately, and points to explicit retrieval for bodies. This exclusion therefore does not exclude policy text from the overall output. SRC-1, `crates/iwe/src/main.rs`, `crates/iwe/src/internal/claude/hook/store.rs`, `crates/iwe/src/internal/claude/hook/index.rs`, `crates/iwe/templates/claude/memory_index.md.jinja`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: rendered `<iwe-memory>` text, or no output when store/index conditions fail.
- Later read-back: selected metadata about documents retained across sessions, plus the current policy's session-start section, reaches the helper's output.
- Delegated visibility: uninspected — external plugin/host must invoke the helper and deliver stdout to a model context; no wiring trace supplied.
- Selection predicate: policy injection slices, machinery exclusion, already-seen keys, per-slice limits/budgets; invalid slice configuration falls back to default slices.
- Invalidation or expiry: each invocation reloads the store; later writes change future selection; no host-window eviction mechanism implemented here.
- Activation or effect: prints discovery context and optional backlog reminder, records reminder timing; actual model action is unobserved.
- Evidence limits: index presence is not full-body delivery or activation; clipping keeps the first rendered line even when it alone exceeds budget, so max_tokens is not an absolute output-size invariant.

> if !kept.is_empty() && used + cost > budget {
>     break;
> }
> --- `crates/iwe/src/internal/claude/hook/index.rs`

> Read one with `iwe retrieve -k <key>`; search with `iwe find --lexical "<terms>" --limit 5`.
> --- `crates/iwe/templates/claude/memory_index.md.jinja`

#### RT-RTE-policy-maintenance
Label: Policy and taxonomy maintenance

Trigger: a user maintenance request, failing policy check or a pattern of acceptances/rejections. The host agent diagnoses and proposes exact policy wording, fields, areas, entities or curation operations; the user chooses or vetoes; the host applies edits and verifies queries/schema coverage. Admission is requested human-mediated procedure, executed using general document/configuration editing capabilities. No autonomous scheduler or enforced approval gate is established. Mode: open user requests with count/query previews, not a controlled optimization curriculum. Answer oracle: user choice and structural/query counts, not an expected correct policy. SRC-1, `crates/iwe/templates/claude/prompts/distill.md`, `crates/iwe/templates/claude/prompts/reflect.md`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: requested change summary with keys, fields, moves, deletions and policy changes; no commit requested.
- Later read-back: edited policy is read by subsequent capture; injection frontmatter is consumed by the next helper invocation; templates/schemas shape later writes.
- Delegated visibility: inapplicable — no maintenance delegation machinery is implemented by this prompt.
- Selection predicate: user request/confirmation plus policy curation permissions; previews and expect guards are instructed for bulk operations.
- Invalidation or expiry: edits replace prior policy/configuration; deletion of MEMORY disables memory helpers rather than deleting the whole store.
- Activation or effect: procedure can change future admission guidance and context selection; actual edits and downstream behavioral changes remain unobserved.
- Evidence limits: generic CLI/editor authority can bypass procedural confirmation; no demonstrated improvement or autonomous policy learning follows from a retained rejection ledger.

Guidance: the policy says what to capture, how to write, dedup/update, provenance, curation and session-start text. The procedure asks for proposal, user choice, backfill, proof queries and teaching the write path. Repeated rejections can shape a proposed revision to that guidance, rather than changing weights. Recovery includes previews, guards and user review; no automatic policy-version rollback is established.

Theory account, limited to these shipped method texts: localized guidance is inspectable and replaceable, and subsequent code consumes symbolic injection settings. Model consumption of the natural-language capture method remains a requested behavior. The policy-feedback instruction asks for pattern-based revisions but does not itself supply a content-directed criticism trace or placement of blame. Theory-builder conditions 1–4: condition 1 conclusion status: afforded (a store can hold whole localized method sections); condition 2 conclusion status: afforded (the host is instructed to decide from them; symbolic injection settings have wired consumers); condition 3 conclusion status: uninspected (no actual challenged policy claim, outcome and blame assignment supplied); condition 4 conclusion status: afforded (edited policy can be reread on the next run, but iterative criticism is not observed). Addressability: named sections and individual YAML settings expose revisable parts; user policy contents remain uninspected. Persistence horizon: cross-session files with later helper/agent consumers. Learning conclusion status: uninspected — no improved future capacity or attribution evidence. Reflection conclusion status: afforded for user-assisted revision of capture policy from its rejection records; actual two-way exercised behavior is unobserved. Reflective theory-builder and autonomous theory-builder conclusions remain uninspected: neither follows from the prompt alone, and user selection is deliberately internal to this described procedure. No exercised self-improvement attribution is made; policy installation and later loading do not establish subsequent operation causally depending on an evidence-shaped change.

> When the recent rejections show a pattern — the same kind of item declined repeatedly, or a kind the user keeps accepting that the policy never asked for — propose one concrete `MEMORY.md` edit with exact wording and apply it only after they confirm:
> --- `crates/iwe/templates/claude/prompts/distill.md`

#### RT-RTE-editor-reload
Label: Editor and external file reload

The LSP accepts an opened buffer as its graph's working copy. External updates/removals reload from disk except for open documents; closing releases that ownership and reloads disk. A missing disk file can drop the graph document. The external editor owns durable saves and applies returned edits; this path is not distill admission. The optional post-tool helper is a separate after-write diagnostic path for selected tool names, not a pre-write veto. SRC-1, `crates/iwes/src/router/server.rs`, `crates/iwe/src/internal/claude/hook/post_tool.rs`, `crates/iwe/src/main.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: updated LSP graph state; selected post-tool reports become a notice and additionalContext JSON, not rollback.
- Later read-back: saved files are available to future CLI/server loads; unsaved editor text remains a current working copy, not necessarily durable memory.
- Delegated visibility: uninspected — editor and host choose delivery and save behavior.
- Selection predicate: workspace-resolvable URI/key; open-document ownership; post-tool name/path/format filters.
- Invalidation or expiry: close reloads disk; external disk removal drops a non-open document; opening changes working-copy ownership.
- Activation or effect: navigation/graph state changes and corrective diagnostic output; no enforced user-selection or schema gate in the inspected reload handlers.
- Evidence limits: handlers do not establish deployed client behavior, universal monitoring of shell writes or successful conflict recovery.

> pub fn apply_external_update(&mut self, key: Key) {
>     if self.open_documents.contains(&key) {
>         return;
>     }
>     self.reload_document_from_disk(key);
> }
> --- `crates/iwes/src/router/server.rs`

> self.open_documents.remove(&key);
> self.reload_document_from_disk(key);
> --- `crates/iwes/src/router/server.rs`

### Claims

#### RT-CLM-capture-exclusivity
Label: Selected capture exclusivity claim

Claimed operation: distill calls itself the only memory write path and says every written document was chosen by the user. Source: embedded prompt, doctrine/design, SRC-1, `crates/iwe/templates/claude/prompts/distill.md`.

> Read sessions with the user and write what they select. Nothing reaches memory unselected: this skill is the only write path, and every document it writes was chosen by the user — by name ("remember that X") or from the candidates §5 puts to them.
> --- `crates/iwe/templates/claude/prompts/distill.md`

- claim conclusion status: claimed

It is a scoped host protocol, not a universal enforced property: [RT-RTE-cli-document](#rt-rte-cli-document), [RT-RTE-mcp-document](#rt-rte-mcp-document) and [RT-RTE-editor-reload](#rt-rte-editor-reload) are alternate storage/working-copy paths without that decision check. No actual unauthorized write is established.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-session-policy
Label: Session policy delivery authority

Consumer: external host agent at session start. Channel: helper stdout rendered into a memory-index template, subject to excluded host/plugin invocation and delivery. Force: natural-language instruction, not a code-enforced command; the policy section and optional backlog reminder can request subsequent actions. Horizon: later sessions using the same store. Implementation output is wired; host delivery/compliance is uninspected. SRC-1, `crates/iwe/src/internal/claude/hook/index.rs`, `crates/iwe/templates/claude/memory_index.md.jinja`.

> {% if policy %}
> {{ policy }}
> {% endif %}
> --- `crates/iwe/templates/claude/memory_index.md.jinja`

#### RT-BAP-schema-admission
Label: Schema check admission authority

Consumer: CLI strict-write and inspected MCP create/update/query handlers. Channel: configured schema validation of pending content. Force: symbolic rejection before the checked persistence call. Horizon: each checked write until bindings/configuration change. This is separate from the natural-language policy's influence on candidate authorship. It has no semantic truth or selection authority beyond encoded constraints. SRC-1, `crates/iwec/src/lib.rs`, `crates/iwe/src/main.rs`.

> Ok(run) if run.reports.is_empty() => Ok(()),
> Ok(run) => Err(schema_violation_error(&run.reports)),
> --- `crates/iwec/src/lib.rs`

## Annotations

none

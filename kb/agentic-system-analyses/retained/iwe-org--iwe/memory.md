---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "IWE memory: policy-governed transcript distillation, durable inbox, document reuse and alternate MCP context paths."
run-id: AAS-2026-11-08-iwe-923f804db3b4-01
source-identity: https://github.com/iwe-org/iwe
reviewed-boundary: "930c184b7cc8508d207e6ca7999ca6e415bc02ac"
---

# IWE memory report

## Boundary and evidence

IWE retains project documents and capture bookkeeping, while an external agent supplies semantic judgment and owns its conversation window. This report covers the whole-system memory scope established by [boundary](boundary.md#boundary-and-evidence): CLI and Claude helpers, embedded capture/maintenance instructions, graph/filesystem state, MCP context and mutation surfaces, and editor reload. It excludes host model internals, the separate plugin repository, Mac app and actual user stores/transcripts. Those exclusions prevent deployed hook, host-compaction, parameter-learning and memory-benefit conclusions, not inspection of the shipped helpers.

All direct source evidence is SRC-1 at the reviewed commit. HEAD was rechecked as `930c184b7cc8508d207e6ca7999ca6e415bc02ac`. Direct reads added the complete digest, record, policy, enable, index and store implementations; complete starter/typed policies and distill/reflect prompts; selected session read/stage/inbox/complete/adopt/brief/rejection functions; CLI dispatch; MCP resources/prompts, squash, rename/extract/inline/normalize; shared retrieval construction and budgeting; post-tool diagnostic production; and agent-instruction initialization. These are implementation or doctrine/design evidence, not observed runs. Supplied runtime findings remain identified below rather than passed off as direct inspection.

| Entry point or operation | Source paths, SRC-1 | Coverage and conclusion limit |
| --- | --- | --- |
| Initialize memory, starter/typed/custom ontology and policy | `crates/iwe/src/internal/claude/enable.rs`; `crates/iwe/templates/claude/enable/starter.md`; `crates/iwe/templates/claude/enable/typed.md` | Direct: [MEM-RTE-memory-enable](#mem-rte-memory-enable), policy parts below. Actual custom body, schema and initiating principal unknown. |
| Capture instruction and transcript digest/read | `crates/iwe/templates/claude/prompts/distill.md`; `crates/iwe/src/internal/claude/digest.rs`; `crates/iwe/src/internal/claude/session.rs` | Direct: annotation on [RT-RTE-session-capture](runtime.md#rt-rte-session-capture). Raw JSONL is filtered before the proposing reader sees it. |
| Stage, inbox, complete, rejection feedback | `crates/iwe/src/internal/claude/session.rs`; `crates/iwe/src/internal/claude/record.rs` | Direct: [MEM-OBJ-proposal](#mem-obj-proposal), [MEM-OBJ-rejected](#mem-obj-rejected), [MEM-RTE-inbox-read](#mem-rte-inbox-read). Staging validates shape, not evidence truth or human selection. |
| Adopt unread sessions | `crates/iwe/src/internal/claude/session.rs` | Direct: [MEM-RTE-session-adopt](#mem-rte-session-adopt). Progress can mean deliberate non-reading. |
| Strict and non-strict CLI writes; MCP create/update/query | `crates/iwe/src/main.rs`; `crates/iwec/src/lib.rs` | Supplied [RT-RTE-cli-document](runtime.md#rt-rte-cli-document), [RT-RTE-mcp-document](runtime.md#rt-rte-mcp-document); dispatch directly checked. No universal per-content human gate. |
| Session-start, brief and policy check | `crates/iwe/src/internal/claude/hook/index.rs`; `crates/iwe/src/internal/claude/hook/store.rs`; `crates/iwe/src/internal/claude/policy.rs`; `crates/iwe/src/internal/claude/session.rs` | Direct: policy objects, rejected ledger and annotations on [RT-RTE-session-index](runtime.md#rt-rte-session-index), [RT-RTE-policy-maintenance](runtime.md#rt-rte-policy-maintenance). Plugin invocation remains external. |
| Explicit retrieval, find, graph expansion, budgets | `crates/diwe/src/retrieve.rs`; `crates/iwe/src/main.rs`; `crates/iwec/src/lib.rs` | Retrieval construction directly read; CLI search/ranking from supplied [RT-RTE-document-retrieval](runtime.md#rt-rte-document-retrieval). All ranking internals not audited. |
| MCP resources, review/refactor/explore, squash/tree/stats | `crates/iwec/src/lib.rs` | Direct: [MEM-RTE-mcp-context](#mem-rte-mcp-context). Registered channels establish context output, not client/model receipt. |
| Merge, forget, taxonomy and policy evolution | `crates/iwe/templates/claude/prompts/reflect.md`; `crates/iwe/templates/claude/prompts/distill.md` | Direct doctrine: annotation on [RT-RTE-policy-maintenance](runtime.md#rt-rte-policy-maintenance). Actual curation and semantic changes unobserved. |
| MCP structural edits and normalization | `crates/iwec/src/lib.rs` | Direct: [MEM-RTE-graph-restructure](#mem-rte-graph-restructure); extract/inline internals and attach/delete implementation details not fully traced, preventing complete transformation and rollback guarantees. |
| Post-tool diagnostics | `crates/iwe/src/internal/claude/hook/post_tool.rs`; `crates/iwe/src/main.rs` | Direct production and delivery JSON checked; supplied [RT-RTE-editor-reload](runtime.md#rt-rte-editor-reload) covers alternate editor admission. Diagnostic text does not undo writes. |
| CLI/server loading, disk persistence and editor working copies | `crates/diwe/src/fs.rs`; `crates/iwec/src/main.rs`; `crates/iwes/src/router/server.rs` | Supplied runtime evidence, not independently reread here: [RT-OBJ-graph](runtime.md#rt-obj-graph), [RT-RTE-editor-reload](runtime.md#rt-rte-editor-reload). Watcher timing/concurrency unobserved. |
| Host instruction discovery | `crates/iwe/src/init/agents.rs` | Direct static AGENTS section and MCP registration. Not itself trace-fed memory; actual host discovery and agent-authored extension of recurring queries uninspected. |
| Evaluators and performance | `crates/iwe/tests/internal_test.rs`; `crates/iwe/benches/load.rs`; `crates/iwe/src/init/agents.rs` | Boundary inventories CLI tests/benchmark source; this member read initialization test definitions only. No evaluator outcomes, retrieval-quality measurement or causal benefit established. Other evaluator cases remain available but uninspected. |

## Core ideas

1. **Candidate persistence is separate from knowledge admission.** The durable inbox survives interruption without exposing proposals as ordinary graph documents. Its full evidence can be requested separately from its grouped display. See [MEM-OBJ-proposal](#mem-obj-proposal) and [MEM-RTE-inbox-read](#mem-rte-inbox-read).
2. **One policy has different consumers.** Natural-language sections guide the proposing/curating agent; symbolic frontmatter configures deterministic context selection. Editing one is not evidence of changing the other. See [MEM-OBJ-policy-body](#mem-obj-policy-body) and [MEM-OBJ-policy-knobs](#mem-obj-policy-knobs).
3. **Session start is discovery plus selected instruction, not full memory recall.** Titles/keys and a named policy section are pushed to helper stdout; bodies require explicit retrieval. The host must actually deliver that stdout. See [RT-RTE-session-index](runtime.md#rt-rte-session-index) and [RT-BAP-session-policy](runtime.md#rt-bap-session-policy).
4. **Semantic curation is a host procedure; structure is code.** The prompts ask an agent and user to deduplicate, merge, reject and revise policy. Schemas reject encoded structural violations on checked routes. General CLI, MCP and editor paths remain alternatives to the capture procedure. See [RT-CLM-capture-exclusivity](runtime.md#rt-clm-capture-exclusivity), [RT-BAP-schema-admission](runtime.md#rt-bap-schema-admission) and [MEM-RTE-graph-restructure](#mem-rte-graph-restructure).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-documents
Label: Durable workspace documents

Source-native identity: keyed workspace documents, physically Markdown or configured format files. Representational form is split by consumption: prose bodies convey facts, reasons, rules and links through human/model interpretation; parsed fields/keys/edges are symbolic input to graph queries and schemas. Storage is the workspace filesystem, not model weights. This is the durable backing content of [RT-OBJ-graph](runtime.md#rt-obj-graph), not a duplicate of its process-memory graph referent. Policy parts below have separate consumers. SRC-1, `crates/iwe/templates/claude/enable/starter.md`, `crates/iwe/templates/claude/enable/typed.md`, `crates/diwe/src/retrieve.rs`.

Lineage ranges from caller-authored notes and configured templates to policy-guided transcript-derived facts. Existing user documents' original admission is unresolved. Subsequent CRUD admission is known from the runtime routes. Capture requests one fact per document, provenance timestamp/session and why it matters; typed capture requests decisions with reasons, learnings and gotchas. Those are requested content, not a guarantee that actual stores retain a rationale. Derived documents can reach later CLI/MCP readers and selected index metadata; models interpret text without an IWE semantic truth gate.

> <Two to six sentences. State the fact, then why it matters. Quote error
> messages verbatim — codes, identifiers, environment variable names — and name
> the files and commands involved, so the item is findable by lexical search.>
> --- `crates/iwe/templates/claude/enable/starter.md`

#### MEM-OBJ-policy-body
Label: MEMORY policy body

Source-native identity: `MEMORY` body, named level-two sections. Storage: a workspace document; representational form: natural-language guidance. Distinct from [MEM-OBJ-policy-knobs](#mem-obj-policy-knobs), which is read by code, and from [RT-BAP-session-policy](runtime.md#rt-bap-session-policy), which is a delivery path rather than content. SRC-1, `crates/iwe/src/internal/claude/hook/store.rs`, `crates/iwe/templates/claude/prompts/reflect.md`.

Initial content can be starter, typed or caller-supplied policy; exact deployed text and human approval unknown. Later agent reads via brief supply capture criteria, write shape, dedup, provenance and curation. `At session start` alone is extracted for automatic index output. Its force is interpreted instruction, not filesystem privilege. The complete body is not automatically pushed by the index. Cross-session persistence permits revisable behavior guidance, without proving learning or compliance.

> pub fn policy_section(&self, title: &str) -> Option<String> {
>     section_of(&self.policy_body(), title)
> }
> --- `crates/iwe/src/internal/claude/hook/store.rs`

#### MEM-OBJ-policy-knobs
Label: MEMORY policy frontmatter knobs

Source-native identity: `distill` and `injection` mapping in `MEMORY` frontmatter, with environment fallbacks. Representational form: symbolic YAML settings consumed by Rust, separately from natural-language policy. Storage: workspace document, copied to `MemoryStore.knobs`; environment is an alternate configuration input, not retained transcript memory. SRC-1, `crates/iwe/src/internal/claude/hook/store.rs`, `crates/iwe/src/internal/claude/hook/index.rs`.

Lineage: enable's starter/typed/custom knobs, later caller edits, or environment defaults when no usable document knob applies. Consumers choose transcript chunk size, proposal-count guidance, reminder interval and ordered injection slices. Injection scope is the union of slice filters conjoined with machinery exclusion; sort, limits and token budgets do not restrict that scope. Thus the brief's knowledge filter describes eligibility, not the exact currently emitted index. This is distinct from [RT-RTE-session-index](runtime.md#rt-rte-session-index), its consumer route. Actual store configuration remains uninspected.

> pub fn injection_scope(&self) -> Filter {
>     let slices = self
>         .injection_slices()
>         .unwrap_or_else(|_| Slice::default_slices());
> --- `crates/iwe/src/internal/claude/hook/store.rs`

#### MEM-OBJ-proposal
Label: Staged Proposal

Part of: [RT-OBJ-session-record](runtime.md#rt-obj-session-record)

Source-native identity: `Proposal`, a YAML-serialized struct in `.iwe/claude/sessions/<id>.yaml`, outside the graph. Symbolic key/updates/status/classification organize natural-language title/body/evidence. The body and evidence are operative parts of the same proposal: full inbox reads expose both, while grouped reads expose summary/body but omit evidence. No opaque numerical payload is hidden behind this display. SRC-1, `crates/iwe/src/internal/claude/record.rs`, `crates/iwe/src/internal/claude/session.rs`.

Lineage: caller-supplied YAML, procedurally proposed from conversation and dedup search. Code resets status to Pending, requires nonempty title/key/body/evidence, rejects MEMORY as key and checks an updates target exists. It does not authenticate the evidence quotation, enforce the printed max_proposals limit or establish a user's selection. The proposer may be a model; physical persistence is Rust filesystem I/O; staging is software admission distinct from subsequent user-directed knowledge admission. Pending entries survive sessions and compaction. Consumers are later inbox readers and completion matching by key/title, not graph retrieval. Written/rejected proposals retain their fields; adopt removes pending ones.

> proposal.status = ProposalStatus::Pending;
> proposal.title = proposal.title.trim().to_string();
> --- `crates/iwe/src/internal/claude/session.rs`

#### MEM-OBJ-rejected
Label: Rejection ledger

Part of: [RT-OBJ-session-record](runtime.md#rt-obj-session-record)

Source-native identity: `rejected: Vec<String>`, YAML strings with candidate titles and optionally reasons. Natural-language feedback payload in a symbolic list; storage is session-record files. Unlike [MEM-OBJ-proposal](#mem-obj-proposal), this list is sampled by `recent_rejections` for the policy brief. SRC-1, `crates/iwe/src/internal/claude/record.rs`, `crates/iwe/src/internal/claude/session.rs`, `crates/iwe/templates/claude/prompts/distill.md`.

Lineage: explicit rejected strings plus titles generated when completion rejects remaining pending entries. All are recorded as rejection signals even though code cannot distinguish a never-presented candidate from a user skip. `recent_rejections` sorts records by distilled_at, ended and session, reverses each list and takes 20 strings. Brief presents those to the host agent; the prompt requests an exact policy revision after user confirmation when a pattern warrants it. This affords a trace-fed guidance-update chain: conversation/proposal dispositions → ledger → brief/model/user revision → retained MEMORY → later capture/index consumer. It is not an automatic learned parameter update, nor proof of improved future action. Policy-change rationale need not be retained in MEMORY; input rejection strings persist separately.

> `--drop-pending` then turns down whatever is left staged on that session, recording each title in the ledger — the sweep that closes the run and the whole of what `Skip all` needs. It cannot tell a candidate nobody asked about from one the user skipped, so it goes in the last call, never between rounds.
> --- `crates/iwe/templates/claude/prompts/distill.md`

### Routes

#### MEM-RTE-memory-enable
Label: Memory initialization

An explicit caller invokes enable; code chooses starter/typed or supplied body/config/schemas/knobs, initializes a workspace if necessary, installs nonclashing ontology and writes MEMORY. Distinct from subsequent [RT-RTE-cli-document](runtime.md#rt-rte-cli-document) admission: this initializes policy and machinery. Proposer is the caller or shipped template author; software decides option compatibility, readable inputs, clashes and configuration parsing. No per-content human approval is checked. Operating mode: open requests. Answer oracle: inapplicable — parsing and clash checks are structural, not expected policy answers. Rejection exits; config parse failure restores prior config text, but later schema/file failures do not establish atomic rollback of the whole initialization. Guidance persists as policy/config/schemas and optional queries cookbook. SRC-1, `crates/iwe/src/internal/claude/enable.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: initialization/install messages or errors; existing MEMORY is refused with an inspect-policy message.
- Later read-back: later helper invocation loads MEMORY knobs and body; later strict writes consume installed schema bindings.
- Delegated visibility: uninspected — caller/host decides who sees results and policy.
- Selection predicate: typed/default/custom options, existing files and config/schema table clashes.
- Invalidation or expiry: subsequent edits replace configuration; deleting MEMORY disables helpers, not general graph reads.
- Activation or effect: persistent machinery installation; actual later agent behavior unobserved.
- Evidence limits: caller identity is not proof of human authorship or per-content consent; deployed custom policy contents unknown.

> if workspace.join(format!("MEMORY.{}", extension)).is_file() {
>     eprintln!("already memory-enabled — inspect the policy with `iwe retrieve -k MEMORY`");
>     return 2;
> }
> --- `crates/iwe/src/internal/claude/enable.rs`

#### MEM-RTE-inbox-read
Label: Durable inbox read-back

Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

This narrower code route serves already-staged proposals, rather than rereading raw sessions. Caller requests all pending groups or one session's full entries; code reads session records and renders them. The later host agent uses grouped candidates to merge/propose a decision and requests full evidence when needed. Human selection is procedural, not performed by this read handler. SRC-1, `crates/iwe/src/internal/claude/session.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: grouped key-targeted summaries or full one-session proposals including evidence.
- Later read-back: prior staged body/evidence are available after interrupted capture or host compaction.
- Delegated visibility: subagents are instructed to stage into separate records; the foreground reader can read all records, but host isolation is external.
- Selection predicate: pending status; optional explicit session; groups use updates target or key and sort by group size then key.
- Invalidation or expiry: complete changes status to written/rejected; adopt can drop pending entries entirely.
- Activation or effect: restores candidates into caller context, not graph admission or verified human choice.
- Evidence limits: no model-receipt trace; grouped output omits evidence, so full-evidence decisions require the separate session read-back.

> report.push_str(&entry_field("body", &proposal.body));
> report.push_str(&entry_field("evidence", &proposal.evidence));
> --- `crates/iwe/src/internal/claude/session.rs`

#### MEM-RTE-session-adopt
Label: Unread session adoption

Unlike [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), adopt deliberately advances progress without semantic extraction. Caller names sessions or code selects pending inactive rows. Code refuses current/active conversations, marks transcript length as distilled and removes pending proposals. Software checks identity/liveness and persists; user scope choice is requested by distill but not authenticated. Mode: open caller maintenance request; answer oracle: inapplicable — no factual candidate judgment occurs. Recovery: failures can skip individual saves; no batch transaction. SRC-1, `crates/iwe/src/internal/claude/session.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: adopted/refused/skipped counts and dropped-proposal count.
- Later read-back: future read defaults start after adopted lines; pending inbox material removed by adoption no longer appears.
- Delegated visibility: inapplicable — no worker launch in handler.
- Selection predicate: explicit safe IDs or pending rows; exclude current/active, already complete and empty sessions.
- Invalidation or expiry: record remains progress metadata; explicit --from can still request a different transcript span while raw file exists.
- Activation or effect: updates bookkeeping and erases pending candidates without adding document knowledge or rejection feedback.
- Evidence limits: the word distilled in progress fields does not prove transcript inspection or extraction; actual user's choice unobserved.

> record.distilled_lines = row.lines;
> record.set_transcript(&row.path);
> record.set_size(row.size, row.lines);
> let dropped = record.drop_pending_proposals();
> --- `crates/iwe/src/internal/claude/session.rs`

#### MEM-RTE-mcp-context
Label: MCP context alternatives

External MCP clients request documents/resources or explore/review/refactor prompts. Server code reads the shared graph and constructs text/JSON; the client is the documented external consumer role, not an invented library caller. Distinct from [RT-RTE-mcp-document](runtime.md#rt-rte-mcp-document), which admits writes; overlaps [RT-RTE-document-retrieval](runtime.md#rt-rte-document-retrieval) only at the shared DocumentReader. Resources, fixed prompt expansions and squash are additional selection/delivery paths. SRC-1, `crates/iwec/src/lib.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: document resource text, graph/config metadata, User-role prompt messages or squashed Markdown.
- Later read-back: graph content persisted by previous invocations can enter a new client invocation through these handlers.
- Delegated visibility: uninspected — MCP client controls delivery to a human, foreground model or worker.
- Selection predicate: document resource URI key; review includes/included_by depths 2/2 and backlinks; refactor depths 3/1 and backlinks; explore statistics; squash explicit key and depth default 2; tree roots/selector/depth; resource listing advertises first 100 document keys, not a read permission cap.
- Invalidation or expiry: shared graph reload/mutation changes later responses; no content expiry in these handlers.
- Activation or effect: prompt messages request review or restructuring, not automatic model execution or compliance.
- Evidence limits: resource document reads differ from DocumentReader output; no deployed client delivery, semantic adequacy or causal benefit demonstrated.

> let content = graph
>     .get_document(&key)
>     .ok_or_else(|| {
>         McpError::resource_not_found(format!("Document '{}' not found", key_str), None)
>     })?
>     .to_string();
> --- `crates/iwec/src/lib.rs`

#### MEM-RTE-graph-restructure
Label: MCP structural maintenance

Separate operations from the create/update/query referents of [RT-RTE-mcp-document](runtime.md#rt-rte-mcp-document): rename rewrites key references; extract selects a section and creates a standalone document; inline selects a reference and inserts target content; normalize compares graph export with disk and persists canonical text. Caller proposes/selects/vetoes requests; code selects blocks, rejects missing/ambiguous selectors, and schema-checks pending rename/extract/inline changes. Normalize's inspected handler goes directly to persistence, without that check. Mode: open requests; answer oracle: inapplicable — structural checks do not judge semantic improvement. Dry-run on the first three prevents persistence; no transaction-wide rollback established. These alter retained material but do not themselves supply content-directed criticism. SRC-1, `crates/iwec/src/lib.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: proposed changes, section/reference listing, persisted changes or normalization count.
- Later read-back: later graph/resource/CLI reads receive changed structure and content.
- Delegated visibility: uninspected — host controls which agent executes or sees the operation.
- Selection predicate: explicit old/new keys or source key plus block/section/reference selector; normalize uses differing exported documents.
- Invalidation or expiry: replacements/deletions affect old representation; keep_target controls inline target retention; no history-based rollback shown.
- Activation or effect: deterministic text/graph restructuring, not demonstrated semantic correction or improved retrieval.
- Evidence limits: lower-level extract/inline transformations and all remaining attach/delete variants not exhaustively read; no universal preservation or strict-schema guarantee follows.

> let changed = updates.updates.len();
> self.persist_changes(&mut graph, &updates)?;
> --- `crates/iwec/src/lib.rs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-graph](runtime.md#rt-obj-graph)

Storage/form distinction: the in-memory graph parses [MEM-OBJ-documents](#mem-obj-documents); indexing is not semantic endorsement. Its current working-copy state may differ from durable disk, as the supplied editor route explains. No embedding or provider state is needed to explain the inspected key/edge and lexical retrieval paths; this does not establish absence across every uninspected dependency.

#### On [RT-OBJ-session-record](runtime.md#rt-obj-session-record)

The record's progress, transcript byte/line cache, captures, title and summary are access/history metadata, not the same thing as extracted project knowledge. Captures store at/through/wrote references, not document bodies or proof of selection. The title/summary are set once if absent. Proposal and rejection payloads have distinct later consumers declared above. SRC-1, `crates/iwe/src/internal/claude/record.rs`.

> if self.summary.is_none() {
>     self.summary = single_line(summary);
> }
> --- `crates/iwe/src/internal/claude/record.rs`

#### On [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Raw-to-derived lineage is lossy before model judgment. `session_read` defaults to the saved distilled line, takes one digest chunk and prints coverage and max_proposals. Digest reads external Claude JSONL, preserves user/assistant text and visible thinking text, labels tool calls/results, clips ordinary results to 240 characters, errors to 600, selected input summaries to 200 and unknown-block string-leaf summaries to 200. Nonconversation records, meta-user text and identified old sweep-feedback spans are omitted. Unknown blocks become readable summaries, not opaque-payload retention; omitted nontext content is not recoverable from that summary. Oversized rendered lines are clipped while coverage advances past their raw line. Chunk control limits the capture reader's context, not the host's full working conversation. SRC-1, `crates/iwe/src/internal/claude/digest.rs`, `crates/iwe/src/internal/claude/session.rs`.

> const TOOL_RESULT_LIMIT: usize = 240;
> const TOOL_ERROR_LIMIT: usize = 600;
> const TOOL_INPUT_LIMIT: usize = 200;
> const UNKNOWN_BLOCK_LIMIT: usize = 200;
> --- `crates/iwe/src/internal/claude/digest.rs`

> self.covered = index + 1;
> out.push(self.take(index + 1));
> return;
> --- `crates/iwe/src/internal/claude/digest.rs`

The derived chain is raw conversation → filtered digest or live conversation already held by the host → model/caller Proposal with evidence → durable inbox → user selection/edit → document → future retrieval/index. Raw inputs mix human turns, assistant text, exposed thinking and tool observations; this is not purely human-authored memory. The model is asked to require a quote and not promote an unconfirmed suggestion to a decision. Those are source-trust rules at the proposing consumer; staging only checks nonempty evidence. Documents request rationale, but the inbox evidence is not automatically copied into their body or automatically served with future graph retrieval. Session pointer and candidate evidence permit further investigation rather than self-contained proof.

Subagent isolation is instructed for multiple sessions: each receives a session ID, selected policy sections and knowledge filter; output crosses the boundary as staged proposals. This resembles a frame whose large reading context stays out of the parent, but IWE supplies neither the launch nor frame disposal. A compacted parent can reload the inbox rather than all transcript context. No IWE host-window summarizer or automatic compaction checkpoint is established by these files; host compaction remains an external responsibility, not an evidenced universal absence.

#### On [RT-RTE-session-index](runtime.md#rt-rte-session-index)

Automatic push selector uses ordered policy slices, prior emitted keys, filters/sort and optional per-slice count/token budgets. Default is 20 created-bearing documents, newest first, title/key only; typed policy uses decisions then recent documents, 10 each. A sort field is included in the projection. Per-slice heading cost is subtracted before selecting/rendering. Policy `At session start`, template prose and reminders are outside these slice budgets. If no group is produced, rendering returns None before policy delivery: MEMORY existence alone does not guarantee policy text is emitted. SRC-1, `crates/iwe/src/internal/claude/hook/index.rs`, `crates/iwe/src/internal/claude/hook/store.rs`.

> let groups = injection_groups(store);
> if groups.is_empty() {
>     return None;
> }
> --- `crates/iwe/src/internal/claude/hook/index.rs`

The retained text influences discovery and the policy may ask the host to offer capture; actual receipt/compliance remains outside the repository. There is no behavioral activation evidence. Filter eligibility, emitted titles and full body delivery must not be conflated.

#### On [RT-RTE-document-retrieval](runtime.md#rt-rte-document-retrieval)

The body path calls `to_markdown_skip_frontmatter`; DocumentOutput adds title/key and edge arrays, not arbitrary provenance or lifecycle frontmatter. Symbolic predicates may select by frontmatter without delivering those fields. A resource read provides a different path to document text. In particular, a `session` provenance field in a stored file does not imply this retrieval route delivers that field. Parent metadata is built regardless of children/backlinks flags. Budgets apply after traversal; content may be truncated with an omission marker, and edge payload counts contribute to document budget. Selection is caller-requested, unlike session-start push; this supplies context, not an authorization or truth boundary. SRC-1, `crates/diwe/src/retrieve.rs`.

> fn get_document_content(&self, key: &Key) -> String {
>     self.graph.to_markdown_skip_frontmatter(key)
> }
> --- `crates/diwe/src/retrieve.rs`

#### On [RT-RTE-policy-maintenance](runtime.md#rt-rte-policy-maintenance)

Curation permissions vary with retained policy rather than a system-wide automatic lifecycle: starter allows bounded same-fact merges but no age pruning; typed allows merge, topic promotion and bounded age pruning while protecting decisions and topic-included documents. Reflect asks for dry-run/count guards, machinery exclusion, schema/backfill/template updates and proof queries. It also affords tombstones via a declared superseded_by field, requiring later passes to exclude them. No generic retrieval predicate automatically enforces that convention. Consumers must select using the configured lifecycle filter. Policy changes replace behavior guidance; the ledger-to-policy path is described in [MEM-OBJ-rejected](#mem-obj-rejected), and actual criticism, update and improved capacity remain unobserved. SRC-1, `crates/iwe/templates/claude/prompts/reflect.md`, `crates/iwe/templates/claude/enable/starter.md`, `crates/iwe/templates/claude/enable/typed.md`.

> When the curation section declares a lifecycle field (`superseded_by`), tombstone instead: `iwe update -k <duplicate-key> --set superseded_by=<survivor-key> --expect 1`, and exclude `superseded_by: { $exists: true }` from later passes.
> --- `crates/iwe/templates/claude/prompts/reflect.md`

#### On [RT-RTE-editor-reload](runtime.md#rt-rte-editor-reload)

Post-tool output can bring schema/similarity feedback into current host context after persistence. It does not retain an independently curated lesson. Recognition is limited to selected tools and parsed command/output shapes; shell writes are not universally inspected. This corrective prompt is different from later-session memory feedback: semantic dedup still requires reading the match and applying the policy. SRC-1, `crates/iwe/src/internal/claude/hook/post_tool.rs`, `crates/iwe/src/main.rs`.

> "additionalContext": report.context,
> --- `crates/iwe/src/main.rs`

## Write side

Admission differs by mechanism; authorship, choosing content and writing bytes must stay separate.

| Mechanism | Content proposer and admission control | Persistent result and later consumer |
| --- | --- | --- |
| Initial memory enable | Caller chooses shipped or custom inputs; code rejects clashes/invalid combinations; no human-per-content check | Policy, knobs, ontology; later brief/index/strict-write consumers, [MEM-RTE-memory-enable](#mem-rte-memory-enable). |
| Session read and stage | Host/model extracts under policy; software checks proposal shape, not quote fidelity; no user selection needed to stage | Durable proposals; later inbox readers, [MEM-RTE-inbox-read](#mem-rte-inbox-read). Digest itself is returned context, not a separately saved semantic memory. |
| Selected fact writing | User selection/edit is requested; agent authors documents; strict CLI checks structural bindings; physical I/O is software | Derived project documents; graph retrieval and metadata injection, [RT-RTE-session-capture](runtime.md#rt-rte-session-capture). |
| Ordinary CLI/MCP/editor writes | Generic human or agent caller determines content; conditional CLI or checked MCP schemas govern selected paths; editor reload is an alternative | Same documents, without required inbox or selection token; supplied runtime routes bound the checks. |
| Complete and rejection | Caller reports wrote/rejected/offered; code matches existence/key/title, sweeps pending if requested; it does not certify a human answer | Capture pointers and rejection ledger; future brief, [MEM-OBJ-rejected](#mem-obj-rejected). |
| Adopt | Caller scopes; software excludes live/current and removes pending, without reading | Progress only; later reads skip the span by default, [MEM-RTE-session-adopt](#mem-rte-session-adopt). |
| Reflect/merge/forget/reorganize | Agent proposes; user choice and policy curation permission requested; CLI and configuration edits physically apply | Revised/deleted facts, links, schema and policy; later selection/readers. No universal automatic expiry. |
| MCP structural maintenance | Client requests; code selects/validates supported structural edits; normalize persists canonical export separately | Changed document organization; later MCP/CLI context, [MEM-RTE-graph-restructure](#mem-rte-graph-restructure). |

The qualifying trace-fed update is not mere transcript retention. The procedure transforms conversational evidence into future facts/rules and can transform acceptance/rejection feedback into the store's future capture method. Both depend on host judgment and requested user admission. Neither code bookkeeping nor a policy label establishes semantic improvement. Reasons are requested in fact bodies and may survive; full line-range evidence remains in proposals, while ordinary retrieval omits frontmatter and does not fetch the session record. A later reader must separately request it if source reasons matter.

Rejection and withdrawal differ: complete retains rejected statuses/strings; adopt drops pending entries without rejection feedback; document deletion removes later graph content after reload; tombstones remain stored and need consumer filters. Policy deletion disables the memory helpers but leaves ordinary documents readable. There is no inferred universal forgetting of host context or backups.

## Read-back

There are four materially different later-consumer chains:

- **Automatic discovery:** retained documents → code-selected metadata slices and policy section → helper stdout → external plugin/host context, conditional on invocation and nonempty groups. This is automatic selection once triggered, not an autonomous daemon or evidence of model compliance. See [RT-RTE-session-index](runtime.md#rt-rte-session-index).
- **Requested document context:** explicit keys, query/ranked seeds and graph expansion → budgeted body/edge output → CLI caller or MCP client. Resource and prompt alternatives have their own projections/depths. A document identifier selects an explicitly requested object; it does not by itself establish a separate relevance-targeting mechanism. See [RT-RTE-document-retrieval](runtime.md#rt-rte-document-retrieval) and [MEM-RTE-mcp-context](#mem-rte-mcp-context).
- **Resumed capture:** session progress and durable proposals → requested transcript span or pending inbox → later proposing/selecting agent. The grouped display is not all evidence; one-session inbox supplies it. See [MEM-RTE-inbox-read](#mem-rte-inbox-read).
- **Feedback-guided maintenance:** retained rejection strings plus current policy/schema census → brief → host diagnosis/proposal and user confirmation → edited policy → later capture decisions and code selection. Delivery of reasons does not establish content-directed criticism, learning or exercised self-improvement. See [MEM-OBJ-rejected](#mem-obj-rejected) and [RT-RTE-policy-maintenance](runtime.md#rt-rte-policy-maintenance).

Working-context control consists of these projections/budgets, lossy transcript windows, requested isolated readers and explicit reload. IWE does not own host context eviction. Persistent keys are actionable reload inputs only when a later agent calls a tool; the context window does not hold dereferenceable graph pointers. Saved progress is neither a full continuation checkpoint nor proof of reading.

## Integration issues

- **Runtime wording correction:** [RT-RTE-session-index](runtime.md#rt-rte-session-index) correctly distinguishes metadata and body, but its policy-delivery account needs the additional no-groups guard documented above. A store with MEMORY yet no emitted group produces no index/policy output. Consequence: policy existence cannot establish session-start instruction receipt. SRC-1, `crates/iwe/src/internal/claude/hook/index.rs`.
- **Brief description correction:** runtime's maintenance discussion and boundary's loop are broadly supported, but the embedded prompts claim the brief includes ten recent documents. Inspected `session_brief` instead prints injection_groups, whose default starter limit is 20 and whose custom slices can have other limits. Treat the ten-document description as source doctrine, not universal implementation. Consequence: context budget and sample coverage are policy-dependent. SRC-1, `crates/iwe/src/internal/claude/session.rs`, `crates/iwe/src/internal/claude/hook/store.rs`; concerns [RT-RTE-policy-maintenance](runtime.md#rt-rte-policy-maintenance).
- **Provenance projection:** [MEM-OBJ-documents](#mem-obj-documents) can store session/provenance fields, while [RT-RTE-document-retrieval](runtime.md#rt-rte-document-retrieval) does not deliver arbitrary frontmatter. Consequence: downstream source trust cannot rely on stored fields automatically reaching this reader. The resource path in [MEM-RTE-mcp-context](#mem-rte-mcp-context) is a distinct alternative, not proof that ordinary retrieval supplies provenance.
- **Feedback interpretation:** [MEM-OBJ-rejected](#mem-obj-rejected) and [MEM-RTE-session-adopt](#mem-rte-session-adopt) separate explicit rejection, sweep rejection and dropped unread proposals. Consequence: neither rejected counts nor distilled_lines alone prove actual human feedback or reading; this qualifies [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), not its underlying existence.
- **Overlap accounting:** [MEM-RTE-inbox-read](#mem-rte-inbox-read) is explicitly part of supplied capture, and proposal/rejection objects are parts of the supplied session record. Documents are durable backing content, not a replacement for process graph. MCP context and structural maintenance overlap shared graph/retrieval machinery but not the supplied admission route's create/update/query identity. No candidate duplicate requiring supersession was found after comparison.
- **Remaining questions:** actual host wiring, deployed policy/custom ontology and original document authorship, semantic extract/inline preservation, all attach/delete variants, watcher timing, executed user selection and measured benefit remain unresolved within the scopes named in the coverage table. They prevent end-to-end reliability, universal write-check, learning and causal benefit conclusions; they do not erase known persistent transformations or later consumers.

## Limitations and checks

Source identity was rechecked against HEAD; new reads stay within SRC-1's registered repository and revision. No target, test, example, model or external service was executed. The supplied member/type and record rules were read completely in the required batches. No prior analysis was used. Validation checks form and quotation occurrence, not semantic support or workflow acceptance.

Deterministic validation: passed with `commonplace-validate` for this report, artifact and memory role. Remaining weaknesses are host delivery/compliance, uninspected deployed content and lower-level alternate maintenance/evaluator details, not concealed claims of absent mechanisms.

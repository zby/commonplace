---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "RightMemory's graph, correction cases, pending evidence, context bookkeeping and shared-view memory paths."
run-id: AAS-2026-11-08-rightmemory-cbec05309c2b-01
source-identity: https://github.com/rightl/rightmemory
reviewed-boundary: "62534bd82c58718f31c99692fed4c5d159e218ec"
---

# RightMemory memory report

## Boundary and evidence

This account covers the memory lifecycle inside the supplied whole-system [boundary](boundary.md): local Memory, Pursuit, Agent Corrections, edit feedback, submission evidence, role continuity, maintenance, mirrored files and question views. The internal runtime and native-assistant route are distinct consumers, not interchangeable implementations. It excludes provider internals and actual deployed conversations, roots and remote content as the boundary does. No target execution was performed. SRC-1 supplies implementation, doctrine/design and reported operation, not observed operation or causal benefit.

Direct reads added the schema and module references, Update/Pruner/Insight prompts, guidance-review skill, selector rendering, retrieval context construction, source indexing, embedding cache/selection, native context preparation, opening-context projection, shared-view builder/questions/notes, guidance capture, cancellation, retained-record storage and installer seeds. Runtime findings supply the admission/sync/executor details explicitly cited below; those were not independently exhaustively audited here.

| Entry point or operation | SRC-1 paths | Coverage and limit |
| --- | --- | --- |
| Dispatch and registered interfaces | `rightmemory/entrypoint.py`, `rightmemory/mcp.py`, `rightmemory/assistant_mcp.py`, `rightmemory/cli.py` | Direct dispatch/tool reads confirm retrieval, submission, guidance, assistant preparation/completion/sync, update undo and sharing commands. Route implementations below and supplied runtime cover these families; command presence is not execution. |
| Memory graph and linked resources | `rightmemory/reference/rightmemory-schema.md`, `rightmemory/reference/MEMORY_RULES.md`, `rightmemory/retrieve_selection.py`, `rightmemory/retrieval_index.py` | [MEM-OBJ-memory](#mem-obj-memory), [MEM-OBJ-markdown-evidence](#mem-obj-markdown-evidence), [MEM-OBJ-memory-skill](#mem-obj-memory-skill); direct reads distinguish graph, evidence and instructions. |
| Pursuit and opening context | `rightmemory/reference/PURSUIT_RULES.md`, `rightmemory/opening_context.py` | [MEM-OBJ-pursuits](#mem-obj-pursuits), [MEM-RTE-opening-context](#mem-rte-opening-context); editor admission supplied by [RT-RTE-pursuit-editor](runtime.md#rt-rte-pursuit-editor). |
| Correction cases and edit feedback | `rightmemory/reference/AGENT_CORRECTION_MEMORY_RULES.md`, `rightmemory/reference/RIGHTMEMORY_EDIT_CORRECTION_RULES.md`, `rightmemory/retrieve_selection.py` | [MEM-OBJ-agent-corrections](#mem-obj-agent-corrections), [MEM-OBJ-edit-feedback](#mem-obj-edit-feedback); limits are requested semantic policy versus structurally enforced shape. |
| Update and pending read-back | `rightmemory/prompts/update.md`, `rightmemory/recent_submitted.py`, `rightmemory/runtime.py`, `rightmemory/update_record.py`, `rightmemory/async_update.py` | [MEM-OBJ-update-evidence](#mem-obj-update-evidence); publication supplied by [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update); native completion by [RT-RTE-native-assistant](runtime.md#rt-rte-native-assistant). |
| Guidance capture/review | `rightmemory/guidance.py`, `skills/review-agent-guidance-inbox/SKILL.md` | [MEM-OBJ-guidance-inbox](#mem-obj-guidance-inbox), [MEM-RTE-guidance-review](#mem-rte-guidance-review). Human proposal approval is specific to this path, not universal. |
| Agent retrieval continuity and budget | `rightmemory/retrieve_context.py`, `rightmemory/runtime.py`, `rightmemory/reference/RETRIEVE_CONTRACT.md` | [MEM-OBJ-retrieve-context](#mem-obj-retrieve-context), annotation on [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval). Provider session payload internals and host compaction remain outside evidence. |
| Independent embedding retrieval | `rightmemory/retrieval_index.py`, `rightmemory/embedding_retrieval.py` | [MEM-OBJ-vectors](#mem-obj-vectors), annotation on [RT-RTE-embedding-retrieval](runtime.md#rt-rte-embedding-retrieval); model identity/fixity from runtime component records. |
| Native context isolation | `rightmemory/assistant_context.py`, `rightmemory/assistant_mcp.py` | Annotation on [RT-RTE-native-assistant](runtime.md#rt-rte-native-assistant); live-file access, not a frozen model window or internal delivery ledger. |
| Prune, Insight, historical recovery and manual editing | `rightmemory/prompts/pruner.md`, `rightmemory/prompts/insight.md`, `skills/maintain-rightmemory/SKILL.md` | Direct prompt reads plus supplied [RT-RTE-maintenance-cycles](runtime.md#rt-rte-maintenance-cycles), [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance); [MEM-OBJ-insight-logs](#mem-obj-insight-logs). Detailed Historian execution and all rollback cases uninspected; no guarantee of automatic restoration. |
| Sync and shared-file admission | `rightmemory/sync.py`, `rightmemory/shared_view_files.py` | Supplied [RT-RTE-sync-admission](runtime.md#rt-rte-sync-admission), [RT-RTE-file-import](runtime.md#rt-rte-file-import). Git-file transport internals remain uninspected, preventing a universal transport-validation claim. |
| Shared production, questions and feedback | `rightmemory/shared_view_builder.py`, `rightmemory/shared_view_questions.py`, `rightmemory/shared_views.py`, `rightmemory/reference/SHARED_VIEW_RULES.md` | [MEM-OBJ-shared-view](#mem-obj-shared-view), [MEM-RTE-view-refresh](#mem-rte-view-refresh), [MEM-RTE-question-view](#mem-rte-question-view). Hub internals, remote actors and withdrawal propagation are not fully inspected. |
| Seed admission | `rightmemory/install_core.py`, `MEMORY.example.md`, `PURSUITS.example.md` | Direct reads: bootstrap copies examples, existing state is preserved. Operator replacement is requested; samples are not actual user facts. |
| Evaluation | `experiments/README.md` | Direct bounded read of reported integrated-backend results and ranking/rejection discussions. Private labels/raw reports unavailable; no independent quality, speed or benefit finding. |

## Core ideas

1. Retained meaning and navigation are separate operative parts. Markdown assertions and instructions affect a model through interpretation; IDs, typed edges, ranges and hashes drive symbolic selection. File naming alone does not establish graph membership. [MEM-OBJ-memory](#mem-obj-memory).
2. Not every saved correction has the same consumer. Agent Corrections helps future task work; `corrections.md` criticizes proposed memory edits and is a late check for curation, excluded from ordinary retrieval. [MEM-OBJ-agent-corrections](#mem-obj-agent-corrections), [MEM-OBJ-edit-feedback](#mem-obj-edit-feedback).
3. Pending evidence can reach retrieval before semantic admission. Its status is preserved rather than treating persistence as truth. Successful Update may derive durable guidance from agent/user interaction evidence, but the retained raw batch is not itself the resulting guidance. [MEM-OBJ-update-evidence](#mem-obj-update-evidence).
4. Internal retrieval has a program-controlled terminal channel: the model selects and code returns original material. Selection accuracy, semantic compliance and host adoption remain independent questions. Native retrieval instead lets host children author the handoff. [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval), [RT-RTE-native-assistant](runtime.md#rt-rte-native-assistant).
5. A mirrored package remains external context, including complete instruction assets; validation and namespace isolation do not establish truth or authorize automatic execution. A question view is explicitly asked, not implicitly expanded during Retrieve. [MEM-OBJ-shared-view](#mem-obj-shared-view), [MEM-RTE-question-view](#mem-rte-question-view).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memory
Label: Memory document tree

Canonical `MEMORY.md` and recursively reachable F# `MEMORY_<id>.md` files store durable facts, preferences, operating guidance, decisions, scope and open questions. Storage: local UTF-8 Markdown in the Git-backed memory root. Natural-language meaning is interpreted by Retrieve, Update, Pruner, Insight and later host agents. Symbolic IDs, heading markers, Focus references and typed edges are parsed by graph/selection code; they are not model weights. The graph shares its ID namespace with Pursuit, but the two modules have different admission authority. Distinct from supplied [RT-OBJ-role-instructions](runtime.md#rt-obj-role-instructions): this is mutable user-root semantic state, not package policy. SRC-1: `rightmemory/reference/rightmemory-schema.md`, `rightmemory/reference/MEMORY_RULES.md`.

> It recursively follows `F#` detail references from those roots. Filename patterns alone do not establish graph membership.
> --- `rightmemory/reference/rightmemory-schema.md`

> Memory is durable context that helps a future agent act, decide, interpret, retrieve, or avoid costly rediscovery. It is not a record of everything that happened.
> --- `rightmemory/reference/MEMORY_RULES.md`

Lineage: installer samples initially, then submitted evidence/model reconciliation, authorized maintenance or incoming state; provenance of any real deployment's preexisting content is unavailable. Policy asks for durable nonduplicate value and revision of canonical items; it does not require preserving every justification or source. Reasons survive when needed for scope/interpretation, not as a mandatory derivation ledger. Natural-language operating guidance can shape later work when retrieved, without changing parameters or proving improved capacity.

> preserve provenance only when it helps interpretation or verification;
> --- `rightmemory/reference/MEMORY_RULES.md`

#### MEM-OBJ-markdown-evidence
Label: M# Markdown evidence

Local `M#<id>` points to free-form `MEMORY_<id>.md`, not graph continuation. Form: natural-language/documentary evidence, possibly embedded code interpreted as quoted content; symbolic owner ID/range metadata is separate. Substrate: Git-backed files. Lineage is caller/model/import supplied and not intrinsically authenticated. The internal selector returns explicit line ranges after owner/marker/file checks; embedding indexing splits line passages and preserves complete fenced blocks. Consumers receive selected text, not necessarily the whole evidential context. Distinct from [MEM-OBJ-memory](#mem-obj-memory), with no supplied object counterpart. SRC-1: `rightmemory/reference/rightmemory-schema.md`, `rightmemory/retrieve_selection.py`, `rightmemory/retrieval_index.py`.

> The backing file is retrievable through the heading but is not parsed as graph structure.
> --- `rightmemory/reference/rightmemory-schema.md`

#### MEM-OBJ-memory-skill
Label: S# instruction asset

`MEMORY_SKILL_<id>.md` stores a complete reusable workflow/playbook in free-form instructional Markdown. Natural-language authority is advisory at the consuming model; selection is not code execution. IDs/ownership are symbolic. Storage and admission follow the local root's write paths; authorship can be model or authorized host. Distinct from package [RT-OBJ-role-instructions](runtime.md#rt-obj-role-instructions) and evidence files: the selected unit is the complete instruction. SRC-1: `rightmemory/reference/MEMORY_RULES.md`, `rightmemory/retrieve_selection.py`.

> if ids or ranges:
>     raise RetrieveSelectionError(f"`{source_id}` is selected as one complete skill; ids and ranges are invalid")
> --- `rightmemory/retrieve_selection.py`

#### MEM-OBJ-pursuits
Label: Pursuit map

`PURSUITS.md` and reachable `PURSUIT_<id>.md` retain user-owned ongoing directions. Natural-language titles, ancestry and optional prose carry meaning; symbolic IDs, nesting, edges and ordered Focus IDs drive graph/editor/projection behavior. Storage: Git-backed Markdown with editor journal/checkpoint state described in [RT-RTE-pursuit-editor](runtime.md#rt-rte-pursuit-editor). This object is distinct from that route and from Memory; Update may read it but not choose new directions. Initial examples do not prove a user's intentions. SRC-1: `rightmemory/reference/PURSUIT_RULES.md`, `PURSUITS.example.md`.

> It marks current attention, not an execution queue, importance ranking, or permission to act.
> --- `rightmemory/reference/PURSUIT_RULES.md`

> Update, ordinary orchestration, review, pruning, insight generation, and acting agents may read Pursuit as context. They do not infer, submit, or apply map changes from task progress, blockage, waiting, next steps, handoff, or completion.
> --- `rightmemory/reference/PURSUIT_RULES.md`

#### MEM-OBJ-agent-corrections
Label: Agent Corrections collections

`MEMORY_agent-corrections-writing.md` and `MEMORY_agent-corrections-design.md` store Expression and Substance cases, respectively. Form: natural-language derived contrasts among prior agent work, user redirection and settled result. Storage: fixed non-graph Markdown collections in the Git root. Position IDs are retrieval metadata, not enduring graph identities. Distinct from [RT-OBJ-semantic-operation](runtime.md#rt-obj-semantic-operation), which stores operation phases rather than reusable task cases. SRC-1: `rightmemory/reference/AGENT_CORRECTION_MEMORY_RULES.md`, `rightmemory/retrieve_selection.py`.

> A redirection is evidence; Update or an explicit review workflow decides whether that evidence deserves a reusable entry.
> --- `rightmemory/reference/AGENT_CORRECTION_MEMORY_RULES.md`

Policy bounds each collection to ten entries/180 nonempty lines, each entry to sixteen nonempty lines and each line to 200 characters; replacement is value-based rather than FIFO. Semantic keep/merge/narrow/remove decisions are requested of a model or reviewing host, not established by counting. Runtime notes that supervisor validation disables capacity enforcement for preexisting sync unions; do not infer that every published state obeys the policy bound. Later Retrieve returns entire selected current entries; embedding indexes each case. The contrast preserves some reasons/outcomes but need not preserve verbatim transcripts, and does not independently authenticate the resulting lesson.

> The collections are bounded priority sets, not logs, quotas, or FIFO windows.
> --- `rightmemory/reference/AGENT_CORRECTION_MEMORY_RULES.md`

#### MEM-OBJ-edit-feedback
Label: RightMemory Edit Feedback

Root `corrections.md` stores Candidate, Proposed edit and Accepted edit fragments, including `[no change]`. Form: natural-language exemplars with symbolic section shape, not generalized rules or ordinary semantic graph state. Storage: root Markdown, bounded by policy to ten reusable entries. Human correction/rejection supplies the evidence; actual initial population and all writing callers remain uninspected. Update and explicit guidance review read it after forming tentative judgments. This is a distinct retained consumer path from [MEM-OBJ-agent-corrections](#mem-obj-agent-corrections), not a duplicate of package policy. SRC-1: `rightmemory/reference/RIGHTMEMORY_EDIT_CORRECTION_RULES.md`, `rightmemory/prompts/update.md`, `rightmemory/reference/RETRIEVE_CONTRACT.md`.

> Keep evidence exact. Do not derive general behavior lessons inside this collection.
> --- `rightmemory/reference/RIGHTMEMORY_EDIT_CORRECTION_RULES.md`

> Root `corrections.md` is excluded from ordinary retrieval context.
> --- `rightmemory/reference/RETRIEVE_CONTRACT.md`

#### MEM-OBJ-update-evidence
Label: Submitted candidates and retained batches

Submission messages preserve unsettled agent/caller evidence, not stored wording. Natural-language payload is distinct from symbolic UID/session/display ID/time, queue status and operation identity. Substrates: local async state/outbox, tracked queue and immutable batch JSON through `UpdateRecordStore`; actual retention horizon depends on root maintenance. This is distinct from supplied [RT-OBJ-semantic-operation](runtime.md#rt-obj-semantic-operation): candidates are input evidence, operation phases are control state. SRC-1: `rightmemory/recent_submitted.py`, `rightmemory/update_record.py`, `rightmemory/prompts/update.md`.

> These are pending updater submissions, not settled Memory or Agent Corrections.
> --- `rightmemory/recent_submitted.py`

> Access immutable, tracked candidate batches retained as input provenance.
> --- `rightmemory/update_record.py`

Update consumes batched evidence and may derive Memory/rules or correction cases from it. Evidence can contain agent actions, user responses and outcomes supplied by the host; a session label alone does not establish trace origin or completeness. Internal and embedding retrieval can also return pending messages with their unsettled status. Native readonly collection excludes terminal receipts' candidate UIDs, including unacknowledged copies. Immutable batches preserve input, but the inspected storage API alone does not establish that every later agent rereads completed batches or every retained assertion links back to one.

#### MEM-OBJ-guidance-inbox
Label: Agent guidance inbox

`AGENT_GUIDANCE_INBOX.md` holds captured evidence plus symbolic entry ID/session/time. Natural-language evidence is raw relative to later formal guidance. Storage: tracked root Markdown. `submit_guidance` performs structural validation and fast-forward admission of a capture commit; that is not approval of a behavior rule. Later human-reviewed curation is [MEM-RTE-guidance-review](#mem-rte-guidance-review). No supplied object counterpart; related semantic publication route [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance) has broader authority. SRC-1: `rightmemory/guidance.py`.

> entry = GuidanceEntry(entry_id, session_id, submitted_at, evidence)
> rendered = render_guidance_inbox([*entries, entry])
> --- `rightmemory/guidance.py`

#### MEM-OBJ-retrieve-context
Label: Retrieve snapshots and session coverage

Substrate: `.runtime/retrieve_context/daily-snapshot.json` and per-session JSON; provider continuation state is additionally provider-managed. Natural-language snapshot/history content is separated from symbolic commit markers, coverage hashes/ranges and visible-candidate maps. Snapshot lineage is current root files at generation time; diffs and current resolution update the model-visible representation later. This is not an independent authoritative fact store. No supplied object counterpart; this elaborates retained state of [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval). SRC-1: `rightmemory/retrieve_context.py`, `rightmemory/runtime.py`, `rightmemory/reference/RETRIEVE_CONTRACT.md`.

> delivery_coverage=state.delivery_coverage.merged(delivery or RetrieveDeliveryCoverage()),
> --- `rightmemory/retrieve_context.py`

Successful retrieval retains model history and merges delivery coverage for later invocations. CLI prefix bases share the exact instructions/snapshot/effective configuration, then fork independent logical sessions; failure falls back to a fresh complete prefix. This retains history, not a demonstrated trace-to-generalized-lesson transformation. Provider payload internals, host trimming and internal provider summaries are uninspected; a thread ID is not readable reasoning.

#### MEM-OBJ-vectors
Label: Embedding vector cache

Derived numerical vectors in `.runtime/embedding_retrieval/vectors.json` are distributed numerical representations of current search passages. Symbolic JSON root/model identity/text-hash keys control reuse. Dense vectors guide similarity scoring, not rule interpretation or weight updates. The raw text remains in canonical files and is what the caller receives. No supplied object counterpart: separate from model parameters in [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model). SRC-1: `rightmemory/embedding_retrieval.py`, `rightmemory/retrieval_index.py`.

> pass  # This is a disposable derived cache, not Memory state.
> --- `rightmemory/embedding_retrieval.py`

Cache reload requires root/model metadata matching; per-text vector validation can reject malformed cached values. Current text hashes determine required keys and stale cache keys are dropped on rewrite. This is numerical indexing of retained content, not trace-fed policy learning.

#### MEM-OBJ-insight-logs
Label: Insight logs

Timestamped `insight_logs/*.md` are natural-language derived reflections over Memory and previous logs, stored in Git. Prior logs can become input to later Insight cycles, but the prompt does not automatically promote them into Memory. A log can contain recommendations without being a validated rule or demonstrated improvement. Distinct from supplied [RT-RTE-maintenance-cycles](runtime.md#rt-rte-maintenance-cycles), an execution container. SRC-1: `rightmemory/prompts/insight.md`.

> Do not append to existing logs.
> --- `rightmemory/prompts/insight.md`

> Read `MEMORY.md` first. Use relevant detail files and prior Insight logs when
> they help you see patterns across memory.
> --- `rightmemory/prompts/insight.md`

#### MEM-OBJ-shared-view
Label: Shared-view content and recipe

Provider file views retain natural-language `view.md`, symbolic `recipe.toml` selections/approval/refresh state, and generated `dist/` Memory graph/evidence/instructions. Consumer imports persist under `.runtime/shared_views/imports/<view-id>/`. Question views instead retain natural-language `retriever.md` plus symbolic `question.toml` configuration/access state. These parts have distinct consumers: builder/renderer, import validator/retriever, provider retriever. A container is retained here; numerical vectors of imported text belong to [MEM-OBJ-vectors](#mem-obj-vectors). No supplied object counterpart; related admission is [RT-RTE-file-import](runtime.md#rt-rte-file-import). SRC-1: `rightmemory/reference/SHARED_VIEW_RULES.md`, `rightmemory/shared_view_builder.py`, `rightmemory/shared_view_questions.py`.

> The generated `dist/` directory is preview or publishing output; it is not active provider memory.
> --- `rightmemory/reference/SHARED_VIEW_RULES.md`

> S# remains a complete instruction resource that is never installed or executed automatically.
> --- `rightmemory/reference/SHARED_VIEW_RULES.md`

Imported content has external authorship. Namespacing/validation bounds graph references and backing resources, not truth or model obedience. Selecting the outer MF heading gives local relationship context, not automatically the package. Notes are a further distinct raw feedback surface: HTTP interactions and local JSONL records carry actor/message/task context/status; human/external relationships require a `confirmed` flag before sending. Listing notes/inbox is a read capability, not proof they automatically revise provider memory. SRC-1: `rightmemory/shared_views.py`.

### Routes

#### MEM-RTE-guidance-review
Label: Capture then approve guidance

Guidance submit through CLI/MCP captures evidence with code-owned structural validation; explicit user review then asks the host to judge proposals against Memory/Agent Corrections rules, current state and late edit feedback. Human approval admits proposed meaning/scope, not exact final wording; host authors final edits/removes approved inbox entries in a temporary worktree and follows validation/landing instructions. The host may reject, defer or find evidence already covered. Operating mode: explicit review, not autonomous automatic promotion; no expected-answer oracle. Recovery fences clean root/HEAD and preserves deferred entries; no universal rollback after protocol violation is shown. This is narrower and distinct from [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance), and not [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update). SRC-1: `rightmemory/guidance.py`, `skills/review-agent-guidance-inbox/SKILL.md`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Capture ID at submission; review reports applied proposals/removed and remaining evidence/commit, or no commit.
- Later read-back: Retained inbox evidence reaches explicit reviewer; approved guidance/cases can reach later Retrieve and host work.
- Delegated visibility: Review host sees supporting evidence/current guidance; actual host isolation is not established.
- Selection predicate: Related pending entries, recurring costly contrasts, overlap and explicit user-approved proposal scope.
- Invalidation or expiry: Approved/rejected entry removals are decided in review; deferred and unreviewed entries remain; base changes stop landing.
- Activation or effect: Protocol affords formal guidance changes; host compliance and later changed decisions are unobserved.
- Evidence limits: Capture is wired but review is an instructional protocol, not software-enforced per-content approval of all write paths.

> This is a user-reviewed direct-curation workflow. Do not route inbox entries through Update.
> --- `skills/review-agent-guidance-inbox/SKILL.md`

> Do not present exact final wording, graph ids, or a patch before approval. Apply only explicitly approved proposals.
> --- `skills/review-agent-guidance-inbox/SKILL.md`

#### MEM-RTE-opening-context
Label: Pursuit opening-context projection

The web/editor consumer described in [RT-RTE-pursuit-editor](runtime.md#rt-rte-pursuit-editor) calls projection with a current Pursuit snapshot. Code resolves source path/line/ID against canonical graph, collects both incoming/outgoing one-hop neighbors and ancestors, renders owned prose and relation triples. Distinct from editor mutation: this route selects retained state for a later host, without model relevance judgment. SRC-1: `rightmemory/opening_context.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Structured current/neighbors/ancestors/sections/edges and rendered text.
- Later read-back: Retained Pursuit and linked Memory content becomes a copyable opening context for a later conversation.
- Delegated visibility: Browser/operator receives text; host use is afforded rather than automatically executed.
- Selection predicate: Current Pursuit snapshot plus incoming/outgoing one-hop graph edges, logical ancestors and source ordering; Focus blocks are excluded as neighbors.
- Invalidation or expiry: Path/line/ID must still identify the current graph block; service revision checking is supplied by the runtime editor record.
- Activation or effect: Deterministic context projection is wired; no evidence of actual copying or resulting host behavior.
- Evidence limits: No token budget or semantic relevance guarantee follows from one-hop graph proximity; linked targets are not arbitrary transitive context.

> Project one current Pursuit and its one-hop graph neighborhood.
> --- `rightmemory/opening_context.py`

#### MEM-RTE-view-refresh
Label: Shared file-view semantic refresh

A caller/changed-memory-and-time due check triggers builder role judgment over retained intent/recipe and current provider memory. Extractive recipes are rendered by code; other builder output must supply a valid dist. Caller approves publication scope separately, but refresh explicitly preserves old approval and publishing configuration. Thus new refreshed wording need not receive a new per-content human approval. Distinct upstream production route from [RT-RTE-file-import](runtime.md#rt-rte-file-import). Operating mode: configured maintenance; model proposes selection/content, validation can veto, no semantic answer oracle. Failure restores backed-up view directory; this does not prove reversal of all executor side effects. SRC-1: `rightmemory/shared_view_builder.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Not-due or refreshed-view summary; optionally publish package.
- Later read-back: Refreshed dist reaches later importer selection; recipe/intent/refresh markers shape later refresh decisions.
- Delegated visibility: Builder sees provider-side material; consumer sees validated exported package rather than full provider ancestry.
- Selection predicate: Force flag or positive refresh interval with changed active commit and elapsed/absent refresh time, then builder judgment and recipe validity.
- Invalidation or expiry: Backup restores failed view updates; current import replacement and stale fallback are consumer-side controls, not automatic remote revocation.
- Activation or effect: Package regeneration/conditional publication is wired; relevance, privacy adequacy and downstream adoption remain unobserved.
- Evidence limits: Generative and extractive alternatives are both present; exact deployed content, approval principal and end-to-end withdrawal propagation are uninspected.

> approved=old_recipe.approved,
> --- `rightmemory/shared_view_builder.py`

#### MEM-RTE-question-view
Label: Explicit provider question

Consumer caller explicitly supplies question and MQ connection; HTTP target/credentials route it to provider. Provider checks approval, reads retained `retriever.md`, appends current question and runs the configured runtime role with stable view-specific session identity. This differs from mirrored-file import and ordinary Retrieve's nonexpanding MQ heading. No supplied route counterpart after comparison with [RT-RTE-file-import](runtime.md#rt-rte-file-import). SRC-1: `rightmemory/shared_view_questions.py`, `rightmemory/reference/RETRIEVE_CONTRACT.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Formatted answer or unavailable reason, with start/answer timeouts.
- Later read-back: Provider prompt and configured role session can persist across questions; caller receives answer. Automatic insertion into local canonical Memory is not established by this route.
- Delegated visibility: Provider runtime receives its retriever prompt plus question; caller receives answer rather than provider's full files/history.
- Selection predicate: Explicit MQ connection/view/question; provider prompt and configured role determine retrieval policy, not local MF item selection.
- Invalidation or expiry: Missing connection/HTTP target, unapproved view, missing prompt, timeout or exception yields unavailable; token verification checks current approval and allowed token hashes.
- Activation or effect: Requested delivery is wired; use in caller work or promotion into memory is unobserved.
- Evidence limits: Provider model internals and actual content are unavailable; timeout does not demonstrate cancellation of every external provider effect.

> return runtime.run_session_turn(f"shared-view-question-{view_id}", prompt, on_started=started.set)
> --- `rightmemory/shared_view_questions.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval)

Read-back substrate and lineage: [MEM-OBJ-retrieve-context](#mem-obj-retrieve-context) holds snapshot/history and symbolic delivery state. `runtime.py` directly constructs the model context from snapshot on new conversation, commit diff, newly visible pending submissions, notices for changed previously delivered sources, optionally currently resolved prior material, then the query. Snapshot and diffs cover roots and present correction collections; backing files remain separately readable. SRC-1: `rightmemory/runtime.py`, `rightmemory/retrieve_context.py`, `rightmemory/reference/RETRIEVE_CONTRACT.md`.

Selection returns local IDs, M ranges, whole S instructions, imported IDs/backing selections, whole positional correction cases or exact recent candidate IDs. The renderer preserves source text, ancestor reading context and source ordering rather than model-authored conclusions. This gives models/humans content to interpret under [RT-BAP-host-context](runtime.md#rt-bap-host-context), not an enforced command channel.

Budget is final character count, not model-window tokens. The final renderer rejects oversize output. Crucially, include-returned context uses a separate effectively unbounded renderer, so terminal result limits cannot be asserted as a bound on model input. SRC-1: `rightmemory/runtime.py`.

> context_renderer = RetrieveSelectionRenderer(
>     self.config.memory_root,
>     max_output_chars=sys.maxsize,
> )
> --- `rightmemory/runtime.py`

#### On [RT-RTE-embedding-retrieval](runtime.md#rt-rte-embedding-retrieval)

Direct corpus inspection extends the supplied description: entries include local graph text with ancestry/Focus context, M evidence passages, entire S instructions, validated MF graph/backings, Agent Correction cases and pending submissions. It is not only ordinary Memory nodes. Bare grouping headings do not consume a result slot; MQ gets a notice, not an automatic provider question. Passage size is 2,000 characters for search splitting, not truncation of delivered source. Each source entry gets at most one ranking slot. Candidate-count/reranker/result-count limits choose entries before source-order display; original display parts deduplicate shared ancestry by source identity. SRC-1: `rightmemory/retrieval_index.py`, `rightmemory/embedding_retrieval.py`.

> for entry in collect_recent_submitted_memory(root):
>     entries.append(_pending_entry(entry))
> --- `rightmemory/retrieval_index.py`

> # Each source entry occupies at most one slot, even when it has several search passages.
> --- `rightmemory/embedding_retrieval.py`

[MEM-OBJ-vectors](#mem-obj-vectors) is reusable derived indexing state, while [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model) and [RT-CMP-reranker-model](runtime.md#rt-cmp-reranker-model) own numerical parameter/fixity limits. Fixed-count ranking is not no-answer detection. The source report itself says unrelated queries also receive candidates; neither rank nor structural validity warrants the selected assertions. SRC-1: `experiments/README.md`.

> The four no-answer queries also receive ten candidates; deciding their usefulness belongs to the caller.
> --- `experiments/README.md`

#### On [RT-RTE-native-assistant](runtime.md#rt-rte-native-assistant)

Direct `assistant_context.py` reads confirm that only pending evidence and shared instructions are materialized; canonical files stay live. It supplies graph source paths, fixed corrections and validated MF import directories. It explicitly creates no model/worker/delivery-history state. Host-native children select/interpret files and return useful context; RightMemory cannot establish the host's window isolation or compaction. This resembles a call frame whose selected return escapes, but external files are not automatically dereferenced window pointers. SRC-1: `rightmemory/assistant_context.py`; the instructional child protocol is supplied in the cited runtime record.

> The active root remains live. Only pending submissions and shared role
> instructions are materialized for this invocation; no model, worker, or
> delivery-history state is created.
> --- `rightmemory/assistant_context.py`

#### On [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update)

Memory lineage is submitted evidence → role keep/merge/skip/edit judgment → canonical Memory/Agent Corrections → later source selection → host guidance. The immutable input batch does not equal the derived content. The prompt requests revalidation of stale claims and preservation of consequential uncertainty as questions. Its late `corrections.md` check is a separate retained criticism input, not the entire ordinary retrieval context. Automatic semantic decisions are model-owned; physical I/O/publication is code-owned; starting a workflow is not human approval of its eventual assertions. SRC-1: `rightmemory/prompts/update.md`.

> Revalidate claims that may have become stale instead of copying candidates as fact.
> --- `rightmemory/prompts/update.md`

#### On [RT-RTE-maintenance-cycles](runtime.md#rt-rte-maintenance-cycles)

Pruner compares generation-boundary Git state with current meaning, preserves active-Pursuit references, revised/currently useful items and revival grace, and repairs graph structure after removal. Lifecycle memory is the prune commit body, not inline state markers. A no-removal due cycle still records an empty checkpoint. Insight instead derives new logs from Memory/prior logs; those are not automatically installed active guidance. SRC-1: `rightmemory/prompts/pruner.md`, `rightmemory/prompts/insight.md`.

> Do not add lifecycle markers to memory files. The prune commit body is the lifecycle ledger.
> --- `rightmemory/prompts/pruner.md`

> If pruning is due but no active memory should be removed, make an empty checkpoint commit:
> --- `rightmemory/prompts/pruner.md`

## Write side

**Initialization.** The installer copies illustrative Memory/Pursuit roots for a new store and preserves existing roots. Example text explicitly warns against treating samples as user facts. This gives known file lineage but not per-content human approval of all seed statements; deployed replacement/adoption is unknown. SRC-1: `rightmemory/install_core.py`, `MEMORY.example.md`, `PURSUITS.example.md`.

> Add real user/project Memory before this block, and do not treat sample nodes as user facts.
> --- `MEMORY.example.md`

**Evidence transformation.** Update receives caller submissions rather than raw host context by default. Its prompts ask it to group meaningful threads across sessions, filter most candidates, revise existing canonical content and keep Memory and concrete correction cases only for distinct value. The chain can transform conversation evidence into future behavioral guidance without weight changes; no complete transcript, immutable rationale for every resulting assertion or measured capacity gain follows. Relevant reasons can survive in the canonical item, case contrast or immutable batch, but those are different surfaces with different later readers. [MEM-OBJ-memory](#mem-obj-memory), [MEM-OBJ-agent-corrections](#mem-obj-agent-corrections), [MEM-OBJ-update-evidence](#mem-obj-update-evidence), [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update).

**Admission differs by route.** Automatic/internal and native Update delegate semantic admission to models/host children plus deterministic publication checks. Guidance review requires explicit human approval of proposals. Map changes belong to the user/editor or authorized map maintenance, not inferred task progress. Manual Memory maintenance is a host protocol. Sync and imports admit incoming state under independent structural gates. Thus no universal human-in-the-loop or universal Update provenance claim is justified. [MEM-RTE-guidance-review](#mem-rte-guidance-review), [RT-RTE-native-assistant](runtime.md#rt-rte-native-assistant), [RT-RTE-pursuit-editor](runtime.md#rt-rte-pursuit-editor), [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance), [RT-RTE-sync-admission](runtime.md#rt-rte-sync-admission), [RT-RTE-file-import](runtime.md#rt-rte-file-import).

**Rejection and withdrawal.** An Update no-op leaves semantic state unchanged even though evidence/control receipts can persist. A dirty/stale/invalid candidate can be rejected before landing; that does not mean external executor effects are rolled back. Pending cancellation in `cancel_pending_candidate` removes eligible local jobs/outbox entries but reports `publication_started` once an attempted queue publication crosses authority; reserved jobs remain protected. It is not a general undo of installed Memory. Canonical withdrawal instead needs permitted edits, pruning or synchronized replacement; Pursuit deletion repairs references and removes subtree/backing files under user authority. SRC-1: `rightmemory/async_update.py`, `rightmemory/reference/PURSUIT_RULES.md`; [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update).

> outcome="publication_started",
> --- `rightmemory/async_update.py`

Pruner's unchanged-age heuristic is not mere FIFO expiry: the requested semantic judgment and grace ledger can preserve apparently old content. Historical Git states remain recoverable through the supplied Historian path, not automatically reinstated. Insight logs and completed evidence are retained analysis/provenance, not automatically generalized rules. [RT-RTE-maintenance-cycles](runtime.md#rt-rte-maintenance-cycles), [MEM-OBJ-insight-logs](#mem-obj-insight-logs).

**External material.** Shared construction can select/extract or generate package content; automatic semantic refresh preserves prior approval. Consumer import validates the exact candidate and can retain stale valid context on failure. Notes can send correction evidence to a provider but the inspected note/list functions do not wire automatic adoption. Neither deletion/revocation at a provider nor a local failed refresh establishes immediate erasure of already imported/delivered text. That propagation remains unresolved. [MEM-RTE-view-refresh](#mem-rte-view-refresh), [MEM-OBJ-shared-view](#mem-obj-shared-view), [RT-RTE-file-import](runtime.md#rt-rte-file-import).

## Read-back

Read-back is requested for the principal retrieval routes: caller query → internal semantic selector or numerical ranker → program rendering → caller. Automatic supply inside the internal request envelope is narrower: a new-conversation condition adds root snapshot; commit changes add diffs; candidate visibility changes add pending evidence/status notices; delivered-source changes add update labels; include-returned explicitly requests current versions. The deciding agent for these envelope additions is code. No retrieved instruction is automatically installed as executable machinery. [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval), [RT-RTE-embedding-retrieval](runtime.md#rt-rte-embedding-retrieval), [MEM-OBJ-retrieve-context](#mem-obj-retrieve-context).

Working-context control has several boundaries. CLI prefix forking isolates independent logical retrieval sessions while sharing stable prefix construction; saved histories resume later requests. Internal CLI write operations use one-shot contexts as supplied by the runtime account. Native children isolate retrieval/update work by host instruction, returning a selected handoff rather than their entire work context. No inspected source establishes general host-context compaction or removal of old turns; actual provider/host window management is opaque. Pruning reduces the durable corpus, not necessarily text already in a host's window. Resetting retrieval state or rebuilding an index is not transcript summarization. Files remain reachable by explicit tool reads, not automatic memory references. [RT-RTE-native-assistant](runtime.md#rt-rte-native-assistant), [RT-RTE-maintenance-cycles](runtime.md#rt-rte-maintenance-cycles); SRC-1: `rightmemory/reference/RETRIEVE_CONTRACT.md`, `rightmemory/assistant_context.py`.

Specialist consumers differ from the foreground host: Update/review use edit feedback; Pruner uses boundary snapshots and grace commit bodies; Insight uses prior logs; editor projection supplies graph-neighborhood opening context; MQ uses provider instructions and a question. Storage of a batch or listable feedback record alone does not prove an additional later semantic reader. [MEM-OBJ-edit-feedback](#mem-obj-edit-feedback), [MEM-RTE-opening-context](#mem-rte-opening-context), [MEM-RTE-question-view](#mem-rte-question-view).

Authority remains consumer-relative. Code gives IDs/ranges/counts/hash comparisons fixed effects, but prose acquires behavioral force only through model/human interpretation. Host skills request reconciliation with current evidence and actual application of relevant guidance. Source delivery supports that behavioral path, not compliance, improved capacity or successful self-improvement. [RT-BAP-host-context](runtime.md#rt-bap-host-context), [RT-BAP-role-policy](runtime.md#rt-bap-role-policy).

## Integration issues

- No supplied fact is contradicted by this inspection. The embedding corpus elaboration matters: [RT-RTE-embedding-retrieval](runtime.md#rt-rte-embedding-retrieval) includes imported/backing/correction/pending entries as well as graph text, and its result limit is entry-count, not semantic answer detection. SRC-1: `rightmemory/retrieval_index.py`, `rightmemory/embedding_retrieval.py`.
- No new declaration intentionally duplicates a supplied referent. [MEM-OBJ-retrieve-context](#mem-obj-retrieve-context), [MEM-OBJ-update-evidence](#mem-obj-update-evidence), [MEM-OBJ-insight-logs](#mem-obj-insight-logs) are stored objects belonging to supplied route accounts; [MEM-RTE-opening-context](#mem-rte-opening-context) is read projection, not the editor write route; [MEM-RTE-guidance-review](#mem-rte-guidance-review) is narrower than general maintenance; shared production/question routes differ from consumer import. The comparisons in each declaration retain their closest supplied record.
- Real deployment input provenance, exact model/endpoint identity, actual host compliance and provider window management remain unresolved. Consequence: no complete transcript lineage, fixed-model reproducibility, exercised compaction or activation claim. [MEM-OBJ-update-evidence](#mem-obj-update-evidence), [MEM-OBJ-retrieve-context](#mem-obj-retrieve-context), [RT-CMP-role-model](runtime.md#rt-cmp-role-model).
- Initial writing control for existing edit feedback and real roots is uninspected. Subsequent Update/review consumption is supported independently; uncertainty about initialization must not suppress that positive. [MEM-OBJ-edit-feedback](#mem-obj-edit-feedback), [MEM-OBJ-memory](#mem-obj-memory).
- Shared refresh carries forward approval, but the API cannot establish the approval principal is human. Full Git-file/hub checks and remote withdrawal propagation remain uninspected. Consequence: no universal per-content approval or immediate purge guarantee. [MEM-RTE-view-refresh](#mem-rte-view-refresh), [MEM-OBJ-shared-view](#mem-obj-shared-view), [RT-RTE-file-import](runtime.md#rt-rte-file-import).
- Completed immutable batch read-back and automatic provider-note adoption are not established by their storage/list APIs. Consequence: retain provenance/feedback capabilities without inventing an autonomous curation loop. [MEM-OBJ-update-evidence](#mem-obj-update-evidence), [MEM-OBJ-shared-view](#mem-obj-shared-view).

## Limitations and checks

The source HEAD was rechecked as `62534bd82c58718f31c99692fed4c5d159e218ec`; all added source reads are within SRC-1 at that boundary. Method identity is the invocation-supplied job, memory type, worker rules and records contract read before analysis. No prior analysis, external source, target execution or provider call was used.

Counterchecks rejected stronger readings: submitted evidence is not admitted fact; correction filenames do not determine Expression/Substance semantics; no-op pruning still has a checkpoint; final-output budget does not bound include-returned input; old approval survives semantic refresh; positional cases are not graph nodes; MF/S delivery is not automatic execution; numerical rankings do not certify no-answer detection. The source's benchmark report is attributed reported operation with private inputs/raw reports unavailable, not an independently observed run or evidence of downstream task benefit. SRC-1: `experiments/README.md`; records above retain the implementation and policy warrants.

Validation: the invocation's role-specific commonplace-validate command exited successfully: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Form and quote occurrence do not establish semantic correctness or workflow acceptance.

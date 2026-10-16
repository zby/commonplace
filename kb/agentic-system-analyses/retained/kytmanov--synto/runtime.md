---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Synto runtime baseline tracing vault production, publication, query, MCP and exported agent instructions at the frozen commit."
run-id: AAS-2026-10-15-synto-eabcdcce3da2-01
reviewed-boundary: "91ac6a3681df0552b6c9baef159439c7ebd780c9"
---

# Synto runtime report

## Runtime account

Synto ships a staged knowledge-production application, not a general model-controlled tool loop. An operator supplies a vault and source notes; Python schedules model analysis and article writing, retains their results, and optionally publishes drafts. Later questions use a separate select-pages/answer sequence. External agents can instead read an exported pack or invoke MCP handlers. The consequential result is retained knowledge and its delivery, not verified factual truth. The entry point is `synto.cli:cli` (SRC-1, `pyproject.toml`). The boundary's import and extraction account remains applicable; this report starts the ordinary invocation with Markdown already in `raw/`.

All findings below are implementation or doctrine/design findings at SRC-1. No application, test, provider or example was executed; actual activation, accuracy, reliability and benefit remain unobserved. Additional implementation coverage beyond the boundary's initial reads includes `src/synto/client_factory.py`, `src/synto/protocols.py`, `src/synto/openai_compat_client.py`, `src/synto/structured_output.py`, `src/synto/pipeline/lock.py`, and `src/synto/watcher.py`, plus the cited lifecycle functions. Prompt and generated-instruction wording supplies doctrine/design evidence, not compliance evidence.

### Ordinary invocation and ownership

For `synto run`, the human chooses the vault and flags, including model/provider overrides, automatic approval, confidence threshold, fixing and dry run. The CLI loads configuration, router and database, acquires the vault pipeline lock, calls `PipelineOrchestrator.run`, and renders counts, failures and timings. The orchestrator owns progression; the fast model proposes analysis, the heavy model proposes articles, and Python owns persistence and stage transitions. Models do not choose arbitrary next tools on this inspected route (SRC-1, `src/synto/cli.py`, `src/synto/pipeline/orchestrator.py`, `src/synto/protocols.py`). See [RT-RTE-pipeline-run](#rt-rte-pipeline-run).

The orchestrator enumerates changed/eligible Markdown, ingests notes individually, rebuilds the index when ingestion succeeds, and prioritizes concepts associated with those sources. A missing/empty priority result can fall back to all eligible concepts. Ingestion hashes the body, skips current duplicates, handles a disappeared old path as a rename, and uses a prompt-version check. It preprocesses clips, removes opaque media/OCR text from model context, and requests structured fast-model analysis. Database records, concept identities and generated source summaries outlive the invocation; raw-file analysis metadata is kept in the database rather than written into the original note (SRC-1, `src/synto/pipeline/ingest.py`).

Compilation loads concept/source relationships, current titles, vault conventions, a bounded existing-article excerpt and recent rejection feedback. Source gathering has a context budget. The heavy endpoint produces a `SingleArticle`; Python repairs and sanitizes Markdown, writes a draft and records compilation state. A source-less stub uses a distinct fast-model prompt and zero confidence. Ordinary compilation skips pending drafts and body-hash-detected manual edits unless forced; a malformed published article can fall through to regeneration. These are explicit exceptions to any unqualified preservation claim (SRC-1, `src/synto/pipeline/compile.py`).

Lint is a separate stage, not a universal publication veto. Optional fixing creates at most three broken-link stubs in this orchestrator call. A second compile round retries transient failures, while a distinct escalation lifts the draft soft cap for truncation. Provider context-overflow handling progressively reduces source and existing-article budgets and marks a successful fallback draft degraded. Thus recovery can change what evidence reaches the writer; success after reduction does not establish full-source coverage (SRC-1, `src/synto/pipeline/orchestrator.py`, `src/synto/pipeline/compile.py`).

If requested, automatic approval publishes only this invocation's draft paths, with a confidence threshold. Otherwise the terminal product is drafts plus the CLI report, leaving human review for later. Optional Git auto-commit records selected vault directories; pre-staged changes can block committing and failure produces a warning rather than undoing generated files (SRC-1, `src/synto/pipeline/orchestrator.py`). Admission and rejection are [RT-RTE-draft-publication](#rt-rte-draft-publication).

### Forcing cases and guarantee boundaries

The selected forcing cases are: automatic approval versus manual review; direct orchestrator calls versus cooperating CLI locking; reduced-context compilation versus full-source assumptions; and MCP source-summary access versus article visibility. They materially qualify review, serialization, evidence coverage and confidentiality claims. No deployed configuration or host isolation envelope was supplied.

| Proposed guarantee | Owner and enforcement point | Strength, coverage and external contract | Conclusion statuses |
|---|---|---|---|
| One pipeline writer at a time | CLI callers acquire `pipeline_lock`; the orchestrator itself delegates this to its caller | protocol: cooperating callers sharing the lock, with local-filesystem lock semantics. Watch batches use the same lock; a busy watch batch is skipped. Direct API calls, external edits and independent consumers are not made safe by that protocol. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Human review before publication | Explicit approve/verify commands or the orchestrator's approval branch | policy: configurable, not invariant. `auto_approve` publishes without per-content human approval; the comparison driver also uses it. Verification is not a prerequisite in `publish_drafts`. | implementation conclusion status: wired; operation conclusion status: uninspected |
| A failed publication does not discard the draft first | `publish_drafts` orders destination write, database publication, then draft deletion | best effort: protects against deleting the draft before those preceding steps; not one atomic transaction across SQLite and the filesystem. Requires both substrates to honor successful writes. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Private article bodies excluded from MCP answering | `_load_pages` applies the MCP visibility predicate to resolved paths before loading bodies | policy: covers ordinary article paths, including alias resolution; not an all-channel confidentiality guarantee. Source-summary paths are expressly exempt; the router still receives the general index. CLI query and pack export have different paths. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Model output follows a schema | `request_structured` plus Pydantic parsing and retries | best effort for obtaining a parseable result; validation is not a factual-answer oracle. Endpoint/provider behavior remains external. | implementation conclusion status: wired; operation conclusion status: uninspected |

Serialization's contract is explicit (SRC-1, `src/synto/pipeline/orchestrator.py`):

> Orchestrates the full pipeline. Caller is responsible for acquiring the
> pipeline lock before calling run() — this class does NOT lock internally.
> --- `src/synto/pipeline/orchestrator.py`

The implementation warns about its environmental precondition (SRC-1, `src/synto/pipeline/lock.py`):

> Vault must be on a local filesystem — flock() is unreliable on NFS/Dropbox.
> --- `src/synto/pipeline/lock.py`

Capability, grant and deployment must remain separate. The application process can write the configured vault, invoke Git and send inference requests using configured credentials. The inspected model interface returns strings or numerical embeddings, not a local shell capability. That is not proof that an arbitrary configured provider is tool-free: OpenAI-compatible options are merged into its request last, so provider-native parameters can override defaults. Their semantics and actual deployment grants remain uninspected (SRC-1, `src/synto/protocols.py`, `src/synto/client_factory.py`, `src/synto/openai_compat_client.py`):

> if options:
>     # Provider-native params (top_p, reasoning_effort, ...); merged last to override.
>     payload.update(options)
> --- `src/synto/openai_compat_client.py`

### Alternate consumers and change planes

A query uses a fast-model page selector and heavy-model answer writer, not an autonomous iterative research session. Each call receives selected text by value; source files remain available for future invocations. Limits include capped page counts, per-page character slices, title-list caps and optional graph neighbors. This resembles bounded call frames with explicit return values, but no pointer in the model window automatically reloads a file. New API calls reconstruct context (SRC-1, `src/synto/pipeline/query.py`). See [RT-RTE-query-answer](#rt-rte-query-answer).

MCP exposes read/search primitives and an answer handler. The latter invokes the same query engine with a visibility callback, then filters the reported selected-page list. Filtering that list is not evidence that all answer inputs passed article policy: source summaries bypass that callback's article check. Source-segment license gates are a different mechanism, with process-lifetime cached grandfathering for vaults without declared licenses (SRC-1, `src/synto/serve.py`). See [RT-RTE-mcp-answer](#rt-rte-mcp-answer).

Pack export copies more than published concept articles: drafts, raw notes, source summaries, queries and synthesis are included through separate tree-copy paths. It emits routing metadata and agent instructions. MCP policy therefore cannot be generalized to exported filesystem content. A consumer's adherence to read-only and grounding instructions belongs to the excluded host, not an enforced pack sandbox (SRC-1, `src/synto/pack_export.py`). See [RT-RTE-pack-export](#rt-rte-pack-export) and [RT-BAP-pack-guidance](#rt-bap-pack-guidance).

Knowledge changes also enter through explicit identity curation and optional query saving/synthesis. These bypass draft publication as their universal admission mechanism. Retained rejection feedback can guide a later writer, but this report does not infer improved capacity or automated criticism of Synto's own method from that delivery. Detailed memory transformations belong to the memory analyst. The shipped comparison driver builds isolated contestant vaults and retains outputs for examination; it is not shown installing a winning model or revising production machinery. See [RT-RTE-concept-curation](#rt-rte-concept-curation) and [RT-RTE-compare-eval](#rt-rte-compare-eval).

## Shared records

### Components

#### RT-CMP-fast
Label: Fast model endpoint

The source-native `fast` role is a distributed-parametric inference component accessed through a `RoleEndpoint` containing client, model name, context size, thinking flag, temperature and options. Weights reside at the local or remote provider, not in Synto's vault. The inspected calls request inference, not parameter updates; provider-side mutation is uninspected. Exact weights/version are not pinned by a role name. Configuration or a mutable endpoint/model alias can resolve to a different model. It analyzes notes, selects query pages and writes source-less stubs (SRC-1, `src/synto/client_factory.py`, `src/synto/pipeline/ingest.py`, `src/synto/pipeline/query.py`, `src/synto/pipeline/compile.py`).

> A `ModelRouter` resolves each role (fast / heavy / embed) independently and builds one
> client per unique connection
> --- `src/synto/client_factory.py`

#### RT-CMP-heavy
Label: Heavy model endpoint

The `heavy` role is separately configurable distributed-parametric inference for concept writing and answers. Storage substrate is the external/local provider's numerical model state. Synto passes a model string, not an immutable weight digest. No inspected route trains it; whether the provider changes parameters between calls is uninspected. A mutable provider endpoint can substitute models independently of retained vault text. Fast and heavy may share a client connection without being the same operative role (SRC-1, `src/synto/client_factory.py`, `src/synto/pipeline/compile.py`, `src/synto/pipeline/query.py`).

#### RT-CMP-embed
Label: Embed model endpoint

The optional `embed` role maps text to dense vectors using provider-held distributed-parametric state. `ingest_note` only invokes it when a RAG store is explicitly injected. Ordinary orchestrator calls inspected here do not inject one. Exact model version and weights are not pinned by the role machinery; no parameter-update API is present in the inspected protocol, and external mutation remains uninspected. Dense output provenance depends on the selected endpoint (SRC-1, `src/synto/client_factory.py`, `src/synto/protocols.py`, `src/synto/pipeline/ingest.py`).

> # Chunk + embed only when RAG store is wired in (Phase 2)
> if rag is not None:
> --- `src/synto/pipeline/ingest.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-pipeline-run
Label: Source analysis and concept compilation

Endpoints are raw Markdown → fast analysis/database → heavy concept draft/files/database → lint → optional publication. The principal is the invoking operator; Python owns scheduling, hashing, state transitions and writes. Model roles propose content; code selects eligible concepts and parses responses. Source paths, concept identities and compile-run identifiers coordinate persistence. Operating mode is an open-ended vault-processing request, not an experiment; there is no reference-answer oracle for article truth. A human can withhold publication or reject drafts, but automatic approval removes that per-content gate. Admission guidance includes source-type prompts, conventions, title hints and rejection feedback; generated text and metadata persist, not model weights (SRC-1, `src/synto/pipeline/orchestrator.py`, `src/synto/pipeline/ingest.py`, `src/synto/pipeline/compile.py`).

- Immediate return: PipelineReport and draft paths/counts, failures and timings rendered by CLI.
- Later read-back: Analysis, concept/source relationships, generated summaries and drafts are retained for later compilation/review/query/export; checkpoint analysis can resume interrupted ingestion.
- Delegated visibility: Fast calls receive preprocessed units and concept hints; heavy calls receive budgeted source text, conventions, title hints, optional existing text and rejection feedback. No general parent conversation is delegated.
- Selection predicate: Raw body hash/status/prompt version; concept eligibility and optional changed-source priority; pending-draft and manual-edit checks unless forced.
- Invalidation or expiry: Changed content/prompt checks and explicit force affect reuse; per-concept failures/deferred states govern retries. Retained files have no time-based expiry established here.
- Activation or effect: Code can write retained analysis and drafts and trigger publication; compliance with prose guidance and factual quality are unobserved.
- Evidence limits: Source wiring only; no supplied vault, model response or completed invocation. RAG injection is an optional API path, not demonstrated ordinary operation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Recovery is bounded: transient second round, truncation escalation and reduced-context fallback, not unlimited self-repair. Reduced-context success marks a review-relevant warning:

> prompt_degraded = True
> --- `src/synto/pipeline/compile.py`

Manual-edit preservation is qualified by the explicit override (SRC-1, `src/synto/pipeline/compile.py`):

> Pass force=True to recompile even manually-edited articles.
> --- `src/synto/pipeline/compile.py`

#### RT-RTE-draft-publication
Label: Draft admission and rejection

Endpoints are draft → published Markdown/database or draft → deletion/rejection history. `approve_drafts` calls `publish_drafts`; `verify_drafts` is a separate in-place status change. Human commands select drafts and may supply notes/feedback; automatic calls select generated paths and apply a numeric threshold without per-draft human judgment. Python decides admissibility from path, existence and confidence, not a semantic oracle. Lint results do not appear as a publication predicate. Operating mode is review/admission, with rejection enabling recompilation rather than measuring improvement (SRC-1, `src/synto/pipeline/compile.py`, `src/synto/pipeline/orchestrator.py`).

- Immediate return: Published/verified paths, or completion of draft rejection.
- Later read-back: Published articles feed later indexes/query/export; stored rejection feedback is loaded into later concept-writing prompts, up to three records in the inspected compiler.
- Delegated visibility: Human review can inspect drafts; the writer receives feedback strings on recompilation, not an independently verified account of the rejection.
- Selection predicate: Explicit paths or all drafts; canonical containment under the drafts directory; optional minimum confidence. Publication does not require verified status.
- Invalidation or expiry: Rejection deletes the draft and resets source compile state to pending; accumulated feedback can block a concept at the rejection cap until unblocked.
- Activation or effect: Publication writes a destination and updates DB before deleting the draft; rejection can change later prompt input. Neither establishes successful semantic correction.
- Evidence limits: No observed reviewer decision, crash recovery or generated revision. Cross-substrate atomicity and factual approval are not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission recovery is ordered, not transactional across all resources:

> write_note(target, meta, body)  # write to destination first
> --- `src/synto/pipeline/compile.py`

> draft_path.unlink()  # remove draft only after DB is consistent
> --- `src/synto/pipeline/compile.py`

Feedback is explicitly behavioral guidance, not just an audit log:

> prompt += "\n\nPREVIOUS REJECTIONS — address these issues in this version:\n"
> --- `src/synto/pipeline/compile.py`

This route can carry a person's content-directed criticism, but the implementation does not establish that arbitrary feedback formulates a theory, assigns blame or produces an effective revision. No system-wide theory-builder or self-improvement conclusion is asserted.

#### RT-RTE-query-answer
Label: Page selection and answer generation

Endpoints are question/index → fast `PageSelection` → resolved page bodies → heavy `QueryAnswer` → sanitized answer. Python owns the two-call sequence, alias expansion, optional graph expansion, page loading and output sanitization. Models propose relevance and answer text, not filesystem actions. Optional CLI saves admit the generated answer directly to queries or synthesis; invoking those flags is not per-content human review. Synthesis-specific checks/recovery remain in that save mechanism rather than the draft gate. No expected-answer oracle is used; operating mode is an open question (SRC-1, `src/synto/pipeline/query.py`, `src/synto/engines.py`).

- Immediate return: Answer text/title, selected page names and optional save results; missing index returns a setup message.
- Later read-back: With save/synthesize, answer files and refreshed indexes are retained; synthesis pages can enter later page selection. Without saving, the ordinary answer itself is not persisted by this function.
- Delegated visibility: Fast sees index and expanded routing question; heavy sees selected body slices and original question, not the complete vault or fast model's hidden processing.
- Selection predicate: Model relevance selection, configured page cap, path resolution, optional visibility predicate, and optional confidence-filtered graph neighbors.
- Invalidation or expiry: Context is rebuilt per call; source files remain outside the model window. Save duplication/manual-edit conflicts have explicit save error paths; no general answer-validity expiry is established.
- Activation or effect: Models receive page content as evidence and grounding instructions; actual grounding and answer correctness are unobserved. Explicit saving changes later available knowledge.
- Evidence limits: No supplied answer run. Selected names can exceed successfully loaded bodies; a selected-page list is not proof of delivered evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The actual page-to-context transformation is bounded (SRC-1, `src/synto/pipeline/query.py`):

> parts.append(f"# {page_title}\n\n{body[:MAX_CHARS_PER_PAGE]}")
> --- `src/synto/pipeline/query.py`

The route's grounding policy is a request, not an entailment check:

> "Answer using the wiki content. Use [[wikilinks]] only for existing wiki pages from "
> --- `src/synto/pipeline/query.py`

#### RT-RTE-mcp-answer
Label: MCP answer and visibility boundary

Endpoints are external MCP question → server handler → shared QueryEngine → answer dictionary. The client owns invocation; server code owns dispatch, article visibility and optional audit; fast/heavy decisions are as in [RT-RTE-query-answer](#rt-rte-query-answer). Primitive handlers offer article/source reads and searches without synthesized answers. License policy for verbatim source access and article visibility are distinct controls. No content mutation admission or answer oracle is involved in this handler (SRC-1, `src/synto/serve.py`).

- Immediate return: Answer, title, filtered selected_pages and index_found; primitive tools return their respective records or passages.
- Later read-back: Optional MCP audit events can persist call metadata; this answer handler does not request saving answers to knowledge.
- Delegated visibility: The query engine receives a visibility predicate for resolved page paths. Source-summary paths are expressly allowed; the normal index still supplies routing context. Audit visibility depends on configuration.
- Selection predicate: Page selection follows query policy; ordinary article bodies require public visibility and no excluded tag. Verbatim-source handlers use source license policy, not that article predicate.
- Invalidation or expiry: Effective grandfathered source-access mode is cached for the process lifetime; source license changes may require restart to affect it. New query contexts are independently built.
- Activation or effect: Code excludes disallowed ordinary article bodies at load time and filters reported names, but does not establish all-channel secrecy or grounded-answer compliance.
- Evidence limits: No client trace, deployment authentication/isolation evidence or provider privacy evidence. The source-summary exception prevents generalizing the article gate to all answer content.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The forcing branch is explicit (SRC-1, `src/synto/serve.py`):

> if Path(resolved_rel_path).parts[: len(sources_parts)] == sources_parts:
>     return True
> --- `src/synto/serve.py`

The separate license policy deliberately has a legacy relaxation:

> effective = "permissive_only" if declared is not None else "all"
> --- `src/synto/serve.py`

#### RT-RTE-pack-export
Label: Pack and agent-instruction generation

Endpoints are retained vault/readonly database → pack files and generated `AGENTS.md`/`CLAUDE.md`. The operator chooses export and output path; exporter code chooses content and refreshes managed trees. This admits generated instructional files and knowledge into a separate consumer environment, without per-item approval. Static template guidance tells the consumer how to route, verify and avoid edits; human text outside generated blocks is preserved by block merging. Re-export is the refresh mechanism, not an automatic downstream rollout or rollback. No oracle or model proposal is used for the export itself (SRC-1, `src/synto/pack_export.py`).

- Immediate return: ExportResult and portable directory containing metadata, articles and supporting trees.
- Later read-back: Agents/people and PackReader can reopen exported files across sessions; generated instructions direct later consumption.
- Delegated visibility: Pack readers can inspect copied raw notes, drafts, source summaries, queries and synthesis in addition to concept articles. MCP visibility is not consulted by this export function.
- Selection predicate: Published concept refs for the articles tree, plus separate optional tree-copy paths and generated metadata payloads.
- Invalidation or expiry: Managed directories are reset on export; generated instruction blocks are refreshed. No live synchronization or expiry of previously distributed packs is established.
- Activation or effect: Files and instructions are delivered on disk; downstream instruction loading/compliance is host-dependent and unobserved.
- Evidence limits: Export implementation is inspected, not an executed export or consuming-agent trace. Portable does not imply access-controlled.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The material alternate path includes unpublished content:

> _copy_optional_tree(config.drafts_dir, out_dir / "drafts")
> --- `src/synto/pack_export.py`

> _copy_raw_notes(config.raw_dir, out_dir / "raw")
> --- `src/synto/pack_export.py`

#### RT-RTE-concept-curation
Label: Explicit concept identity changes

Endpoints are operator-supplied concept names/source partitions → database identity changes, article retirement/stubs and link rewrites. The inspected merge and split functions require explicit arguments; computation checks identities, collisions and manual-edit hashes. The human chooses the proposed semantic grouping; software enforces preconditions. Suggestions are not equivalent to applying a change. Mode is explicit maintenance, with no reference-answer oracle. Merge can refuse edited content unless absorb_edits is granted; split similarly requires an override and carries original content into its primary sense. Unmerge is a source-native recovery route; arbitrary all-state rollback is not established by its existence (SRC-1, `src/synto/pipeline/maintain.py`).

- Immediate return: MergeReport/SplitReport or explicit errors; dry run supplies a preview without those mutations.
- Later read-back: New identities, aliases, source allocation, retired files and stubs change later routing, compilation and linking.
- Delegated visibility: No model call in these inspected mutation functions; a human supplies semantic decisions, while later compilers receive resulting concept/source state.
- Selection predicate: Named identities and, for split, supplied senses/source lists; collision and edit-protection preflight checks.
- Invalidation or expiry: Merge/split alter identity relationships and generated article state; retired content and unmerge support bounded recovery. No general expiry policy applies.
- Activation or effect: Deterministic database/file mutations are wired; semantic correctness and downstream improvement remain unobserved.
- Evidence limits: Source only; not a demonstrated maintenance episode. This record is the change-admission boundary, not an inventory of every curation transform.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The split proposal is supplied as structured caller data:

> senses is a list of (new_name, [source_paths]).
> Creates stub articles for each sense plus a disambiguation stub at the bare label.
> --- `src/synto/pipeline/maintain.py`

#### RT-RTE-compare-eval
Label: Offline evaluation and contestant runs

The evaluator reads retained vaults and optional query fixtures; the comparison runner builds separate contestant vaults, automatically publishes pipeline outputs and optionally queries each. Python owns scheduling and artifact capture; configured models generate articles and answers. Humans configure contestants and can inspect differences. Fixture expectations support structural coverage checks, not an oracle of answer truth. Operating modes are offline structural evaluation and bounded contestant comparison. These inspected drivers retain reports rather than installing a winning production configuration (SRC-1, `src/synto/pipeline/eval.py`, `src/synto/compare/runner.py`).

- Immediate return: EvalResult or ContestantRunResult with diagnostics, timings, snapshots and query outputs.
- Later read-back: Comparison artifacts include stats.json, queries.json, pages.json and wiki snapshots for later inspection; no automatic production-policy consumer is established here.
- Delegated visibility: Contestants receive copied raw sources and effective configuration in separate vaults; they do not share the active vault's generated article state through this setup.
- Selection predicate: Configured contestants, optional raw sample and query list; structural evaluator checks article/citation coverage, index validity and link resolution.
- Invalidation or expiry: Temporary contestant vaults are removed unless retained; artifacts survive separately. Partial execution/errors are recorded rather than treated as a completed comparison.
- Activation or effect: Wiring supports measured artifact generation; no supplied run or causal isolation establishes model/component benefit.
- Evidence limits: Tests and drivers were not run. term_recall is skipped and live evaluation raises an explicit not-implemented exit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The comparison path is a counterexample to mandatory manual publication:

> auto_approve=True, max_rounds=2
> --- `src/synto/compare/runner.py`

The evaluator's boundary is explicit:

> "synto eval --live is not implemented in Phase 1A. Use offline mode without --live."
> --- `src/synto/pipeline/eval.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-pack-guidance
Label: Generated pack guidance to later agents

Consumer: an external agent host that loads exported AGENTS.md or CLAUDE.md. Channel: natural-language generated Markdown stored in pack files, alongside symbolic JSON indexes and content paths. Force: requested instruction/routing guidance, not an executable sandbox or demonstrated host compliance. Horizon: later tasks and sessions using that exported pack, until replaced or bypassed. [RT-RTE-pack-export](#rt-rte-pack-export) is its admission route (SRC-1, `src/synto/pack_export.py`).

> "- Treat pack files as read-only unless explicitly asked to edit them.\n"
> --- `src/synto/pack_export.py`

#### RT-BAP-rejection-guidance
Label: Retained rejection guidance to writer

Consumer: heavy-model concept writer. Channel: natural-language feedback stored by rejection and appended to a later writing prompt under previous rejections. Force: model-interpreted instruction to address issues, with separate software blocking at the rejection cap. Horizon: later compilation rounds/sessions while records remain. The software stores and delivers feedback but does not establish its correctness or compliance. See [RT-RTE-draft-publication](#rt-rte-draft-publication) for the checked passage and admission mechanism (SRC-1, `src/synto/pipeline/compile.py`).

## Annotations

none

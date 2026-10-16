---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Kompl runtime baseline: compile orchestration, knowledge admission, query feedback and alternate maintenance paths at the frozen commit."
run-id: AAS-2026-10-14-kompl-9cffb1e5eb86-01
reviewed-boundary: "17970c969b0c2576bf722840e0e2db3c6416a7aa"
---

# Kompl runtime report

## Runtime account

Kompl is a knowledge compiler and server, not a model-directed enclosing agent runtime. Its application code owns progression. Models supply extraction, disambiguation, triage, page prose, schema prose and answers; they do not choose arbitrary tools or schedule the compile graph in the inspected driver. The boundary includes its built-in chat and maintenance callers, but excludes external MCP agents. All findings below concern SRC-1 at the frozen revision. Implementation wiring is inspectable; successful operation, model compliance, activation and benefit at that revision are unobserved. No target code or tests were executed. Historical provider evaluations remain attributed evidence under [the boundary](boundary.md#boundary-and-evidence), not demonstrations of this invocation.

### Ordinary shipped invocation

A user includes staged files, URLs or pasted text and finalizes a session. The principal is a local API caller; the shipped UI supplies a human-facing path, but the API does not authenticate a human identity. `session_id`, then `source_id`, `plan_id` and `page_id` identify progression and retained products, not security principals. Finalization filters included pending/legacy-ingested rows, checks another running session, creates durable `compile_progress`, stamps a compile model and posts to n8n. A trigger failure returns 503 while leaving queued state for reconciliation. n8n acknowledges its webhook with 202 and calls the app's compile driver. It does not own the long-running graph. [RT-RTE-session-compile](#rt-rte-session-compile) records the return and recovery distinctions. SRC-1: `app/src/app/api/onboarding/finalize/route.ts`, `n8n/workflows/session-compile.json`, `app/src/app/api/compile/run/route.ts`.

The driver returns `started` while an in-process background promise runs. It ingests staged material after health checks, then extracts each source, resolves names, matches sources to existing pages, plans pages, drafts by layer, injects cross-references, commits, and bootstraps a schema. Ordinary state is SQLite progress, sources, extractions and page plans; the Python service handles conversion, model calls, compressed files and vectors. The app owns the next step and HTTP timeouts; providers own generation. The configured graph is symbolic code, whereas the prompts and generated prose require model interpretation. This is delegated computation, not delegation to autonomous workers. SRC-1: `app/src/app/api/compile/run/route.ts`, `app/src/app/api/compile/draft/route.ts`, `docker-compose.yml`.

Extraction reads retained raw markdown; NER and a profile select keyphrase methods, TF-IDF and structured model extraction. It persists extraction output and mention sets. Resolution uses existing aliases and page titles, fuzzy matching, embedding similarity and model disambiguation for ambiguous pairs; new aliases survive to later sessions. Matching takes at most three TF-IDF candidates per source above 0.15, then asks model triage for update/contradiction/skip. Planning applies code rules: source pages, historical mention thresholds for entities/concepts, relationship-based comparison pages and overview pages. A skip can still attach provenance; a contradiction records an activity entry rather than revising the page through that match branch. These roles and their lack of an answer oracle are separated in [RT-RTE-plan-draft](#rt-rte-plan-draft). SRC-1: `app/src/app/api/compile/extract/route.ts`, `app/src/app/api/compile/resolve/route.ts`, `app/src/app/api/compile/match/route.ts`, `app/src/app/api/compile/plan/route.ts`.

Drafting constructs a new, bounded context per page call: selected sources, extracted dossiers, optional existing page text, schema, related summaries, known titles and categories. Dossier ranking caps sources by TF-IDF relevance with a recency fallback; comparisons bypass that cap. Page layers run in order, with bounded concurrent calls within a layer. Later layers receive summaries of earlier drafts. Original-source pages pass raw text through without a drafting model. Known titles are capped at 200; the Python draft function prefix-truncates the assembled prompt to the configured character cap, then appends category instructions. A requested full update is therefore not evidence that every source reaches the model. Individual invocations resemble temporary frames: selected inputs enter and returned prose escapes to `page_plans`; hidden provider context handling is not inspectable. Later rereading is explicit code and disk/database I/O, not a reference inside the model window. SRC-1: `app/src/app/api/compile/draft/route.ts`, `nlp-service/services/llm_client.py`.

Cross-reference in the shipped app is deterministic title/alias injection, not the older model cross-reference API that remains in the Python service. The driver commits only eligible plan states. Auto-approval defaults on; when off, content plans enter pending approval, while provenance-only plans still commit. Per-page SQLite transactions persist page metadata, pending markdown, provenance, FTS and committed-plan status. File flush follows; aliases and vector indexes have separate non-critical updates. The result is retained wiki content, progress/activity information and possibly schema instructions. Completion is not a promise that every source or draft succeeded. On a first compile with auto-approval off, no committed plans may remain for schema bootstrap: the schema handler returns `no_committed_pages`, which can fail the driver after drafts have already been queued for review. Manual queuing is therefore not itself proof of a completed compile. SRC-1: `app/src/app/api/compile/crossref/route.ts`, `app/src/app/api/compile/commit/route.ts`, `app/src/app/api/compile/schema/route.ts`, `app/src/lib/db.ts`.

### Consumption and feedback

The wiki/MCP route serves page prose and provenance without an answering model. The built-in chat instead chooses index-first model selection below an estimated 6000-token index, otherwise FTS/vector weighted ranking, and reads selected page files. The app supplies at most ten pages, selects up to eleven earliest timestamp-ordered session messages and drops the final selected row, and further clips the first five pages to 2000 characters and the rest to 300. The code comment calls the first five “full content,” but the actual delivered content is clipped. A metadata-question bypass answers from database statistics without any model; a no-page bypass returns a fixed message. [RT-RTE-chat-feedback](#rt-rte-chat-feedback) and [RT-RTE-mcp-read](#rt-rte-mcp-read) distinguish these consumers. SRC-1: `app/src/lib/retrieval.ts`, `app/src/app/api/chat/route.ts`, `mcp-server/index.ts`.

Chat saves question/answer history. Three or more **retrieved pages**, not verified citation use, trigger a pending FAQ draft. Pending creation is wired, but ordinary approval cannot install that FAQ when its retrieved page IDs are not also existing source IDs: the shared helper inserts them as provenance source IDs and the foreign-key failure returns `commit_failed`. Empty-citation manual saves and coincident source/page IDs are supported exceptions, not a repair of ordinary automatic FAQ adoption. Neither storing a proposal nor these exceptional admission paths establish factual improvement. MCP exposes search, read, list and statistics only in the inspected server. The external agent decides when to call them and what delivered text does to its own decisions. Kompl does not receive authority over that agent merely by returning a tool result. SRC-1: `app/src/app/api/chat/route.ts`, `app/src/lib/approve-plan.ts`, `mcp-server/index.ts`.

### Controls, forcing cases and guarantee coverage

The capability surface includes application mutation APIs, direct Python model/storage APIs, local CLI/Docker/Git operations and operator filesystem access. The current Compose configuration binds app, NLP and n8n host ports to loopback; it shares the data volume read-write across services. These are deployment choices, not evidence of the actual deployed isolation envelope. No live deployment or client grant set was supplied. A local API caller can invoke approval or direct maintenance without proving human review. The provider adapters inspected create generation/completion requests without tool grants; that narrowly supports text-generation roles, not an audit of every ingestion subprocess or upstream n8n extension. SRC-1: `docker-compose.yml`, `nlp-service/services/providers/gemini.py`, `nlp-service/services/providers/deepseek.py`, `cli/src/commands/update.ts`.

Four forcing cases bound the load-bearing conclusions:

1. **Flush failure and approval success:** the compile driver fails a session on nonzero session-scoped pending flush failures, but single-plan approval logs a flush error and still returns success after the database commit. Thus “committed” cannot universally mean a current file exists. Both paths retain outbox content for retry/startup. The database reader prefers an existing file before pending content, while chat retrieval reads through Python file storage without that fallback. An unflushed update can therefore expose old file prose; a new unflushed page can be omitted from chat. [RT-CLM-durable-completion](#rt-clm-durable-completion), [RT-RTE-draft-approval](#rt-rte-draft-approval). SRC-1: `app/src/app/api/compile/run/route.ts`, `app/src/lib/approve-plan.ts`, `app/src/lib/db.ts`, `app/src/lib/retrieval.ts`.
2. **Deletion-triggered redraft:** source deletion can directly redraft and commit a surviving page, without the compile auto-approval/thin-draft gate or normal existing-page/schema/dossier context. Short-source deletion retains prose plus a provenance note; failure falls back to a note/count update. This defeats a system-wide claim that all page changes require approval or all deletion removes the source's semantic contribution. [RT-RTE-source-maintenance](#rt-rte-source-maintenance). SRC-1: `app/src/lib/source-delete.ts`, `app/src/lib/recompile.ts`.
3. **Archive import:** an empty-wiki import restores supplied content, settings, histories, plans and optional precomputed vectors directly. It does not route each page through model drafting or draft approval. Files written inside a SQLite transaction are not rolled back by SQLite. [RT-RTE-archive-import](#rt-rte-archive-import). SRC-1: `app/src/app/api/import/route.ts`.
4. **Query clipping and draft feedback:** retrieval can fall back to popular pages, omit unreadable files and clip content before answer synthesis. History selection preserves earliest rows, not a recent tail. The draft trigger counts retrieved pages regardless of actual citation use, and ordinary page-ID provenance blocks approval unless those IDs also exist as source IDs. Pending creation therefore does not establish an end-to-end compounding cycle. These implementation constraints bound wiki-grounding and compounding claims; no executed failure or failure rate is established. [RT-RTE-chat-feedback](#rt-rte-chat-feedback). SRC-1: `app/src/lib/retrieval.ts`, `app/src/app/api/chat/route.ts`.

The storage service archives the current gzip file before writing a sibling temporary file and renaming it into place. Its guarantee is **protocol**, owned by `write_page`: no partial gzip is installed by that final rename, assuming same-filesystem rename semantics. Archiving and installing are two operations; a failure between them can leave the current path absent. There is no inspected fsync in this function, so it does not establish power-loss durability. Import uses another write path. Shared writable volume access also means app-only database ownership is a code convention, not a filesystem permission guarantee. SRC-1: `nlp-service/services/file_store.py`, `app/src/app/api/import/route.ts`, `docker-compose.yml`.

> previous_path = str(safe_join(_PAGES_DIR, f"{page_id}.{ts}-{usec:06d}.md.gz"))
>         os.replace(current_path, previous_path)
> --- `nlp-service/services/file_store.py`

> # Both handles fully closed above — gzip trailer is flushed.
>         os.replace(tmp_path, current_path)
> --- `nlp-service/services/file_store.py`

Operational recovery includes database-derived extraction/draft retry, cancellation checks between steps/new source calls, pending flush reconciliation at startup and commit retry, and best-effort vector upserts. An in-flight extraction may finish after cancellation; the background promise is not a durable job execution engine. The finalization concurrency gate does not by itself prove exclusion across direct compile/subroute callers. Timings, progress, provider usage and activity failures aid diagnosis but do not verify semantic accuracy. SRC-1: `app/src/app/api/compile/run/route.ts`, `app/instrumentation.ts`, `app/src/app/api/onboarding/finalize/route.ts`, `nlp-service/services/providers/gemini.py`.

Additional inspected SRC-1 implementation coverage beyond the boundary's initial read includes full approval/rejection handlers, the source-delete redraft helper, import implementation, deterministic crossref, provider request construction, retrieval clipping, local NLP model loaders, Docker model installation and CLI update. Lint reports orphans/staleness/missing links/dead provenance and best-effort summary-pair contradictions; it logs findings rather than automatically revising all challenged pages. It also requests regeneration of the saved-links page. Product updates follow operator-invoked Git fast-forward, CLI relink, image pull, build/restart and health polling, not model-selected successor code. Remaining uninspected details include exhaustive conversion branches, helper internals for saved-links regeneration, every UI caller and evaluator assertion. These limit an exhaustive security, maintenance and semantic-coverage judgment, not the positively traced paths. SRC-1: `app/src/app/api/wiki/lint-pass/route.ts`, `cli/src/commands/update.ts`, `nlp-service/Dockerfile`.

## Shared records

### Components

#### RT-CMP-gemini
Label: Gemini generation provider

Distributed-parametric remote generation, accessed through `GeminiProvider` and model-name strings. Kompl stores configuration and usage, not provider weights. Compile defaults to `gemini-2.5-flash`; caller/session settings select the actual name. Parameters are not updated by the inspected completion call; provider-internal change is uninspected. Exact weights/version are not pinned, and a provider-resolved endpoint/model alias can change behind the name. Session model stamping fixes a name, not weights. SRC-1: `nlp-service/services/providers/gemini.py`, `nlp-service/services/llm_client.py`, `app/src/app/api/onboarding/finalize/route.ts`.

> return client.models.generate_content(model=req.model, contents=contents, config=config)
> --- `nlp-service/services/providers/gemini.py`

#### RT-CMP-deepseek
Label: DeepSeek generation provider

Distributed-parametric remote completion, accessed by `deepseek-*` prefix through `DeepSeekProvider`; remote substrate and weights remain opaque. No parameter update is sent by the inspected adapter. Exact serving version/weights are not pinned; provider resolution of the selected name is mutable. JSON-object output plus local validation is not a semantic correctness guarantee. SRC-1: `nlp-service/services/providers/__init__.py`, `nlp-service/services/providers/deepseek.py`.

> response = client.post("/v1/chat/completions", json=body)
> --- `nlp-service/services/providers/deepseek.py`

#### RT-CMP-mini-lm
Label: Resolution and vector embedding model

`SentenceTransformer("all-MiniLM-L6-v2")` supplies distributed-parametric embeddings for resolution and wiki vectors. The process caches a local model object; Chroma stores derived dense vectors separately. The inspected loader/encode path changes neither weights nor trains the model. No exact model revision is supplied to the loader; upstream/cache resolution can differ between installs, though a loaded process singleton is not hot-swapped by this route. Vector upsert changes derived representations, not the model parameters. SRC-1: `nlp-service/routers/resolution.py`, `nlp-service/services/vector_store.py`.

> _embed_model = SentenceTransformer("all-MiniLM-L6-v2")
> --- `nlp-service/routers/resolution.py`

#### RT-CMP-key-bert
Label: KeyBERT extraction component

Local KeyBERT model object with distributed-parametric embedding backend, cached separately from the resolution singleton. The inspected code constructs `KeyBERT()` and uses `extract_keywords`; it does not update parameters. Exact backend revision is not pinned at this construction point; the log names MiniLM but constructor defaults are an external package contract. Backend resolution across installs is not established; no runtime endpoint/hot-swap is wired here. SRC-1: `nlp-service/routers/extraction.py`.

> _kw_model = KeyBERT()
> --- `nlp-service/routers/extraction.py`

#### RT-CMP-spacy
Label: spaCy NER pipeline

Local `en_core_web_sm` pipeline augmented by TextRank. Its learned model state is distributed-parametric; the Python pipeline object is the operative substrate. `spacy.load` and inference do not train it. The Docker build downloads a named model rather than an immutable model artifact revision, so exact weights are not pinned by the inspected install path. No remote serving alias or runtime model replacement is used by this loader; install-time resolution remains dependent on spaCy's download contract. SRC-1: `nlp-service/routers/extraction.py`, `nlp-service/Dockerfile`.

> _nlp = spacy.load("en_core_web_sm")
> _nlp.add_pipe("textrank")  # pytextrank component for /extract/textrank
> --- `nlp-service/routers/extraction.py`

### Operative objects

#### RT-OBJ-page-plans
Label: Page-plan control state

Symbolic control portion of SQLite `page_plans`: plan/session IDs, action, target page, source IDs, related plan IDs and draft status. Fixed app predicates choose planned/failed/drafted/crossreffed/pending-approval/committed branches. Generated `draft_content` is a separate natural-language payload, not part of this control-state assessment. Plan persistence enables retry and approval across requests. SRC-1: `app/src/app/api/compile/run/route.ts`, `app/src/app/api/compile/plan/route.ts`, `app/src/app/api/compile/commit/route.ts`.

> const plans = getPagePlansByStatus(session_id, 'crossreffed');
> --- `app/src/app/api/compile/commit/route.ts`

#### RT-OBJ-schema
Label: Generated wiki schema instructions

Natural-language maintenance instructions stored at `/data/schema.md`. Bootstrap derives them from committed plan titles/types/categories; later draft calls interpret them as conventions. They are neither a Python/SQL schema nor the deterministic planner's policy. SRC-1: `app/src/app/api/compile/schema/route.ts`, `nlp-service/services/llm_client.py`.

> if schema:
>         parts += ["Wiki schema (follow these conventions):", schema, ""]
> --- `nlp-service/services/llm_client.py`

### Routes

#### RT-RTE-session-compile
Label: Staging through session compile

App finalization → n8n webhook → app background driver → ingestion/extract/resolve/match/plan/draft/crossref/commit/schema. The application owns progression and progress writes; callers supply session identity and staged selection, not a next-tool model policy. Endpoint effect boundaries are app-owned database/files and service/provider requests. SRC-1: `app/src/app/api/onboarding/finalize/route.ts`, `n8n/workflows/session-compile.json`, `app/src/app/api/compile/run/route.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Finalize returns queued counts or trigger failure; webhook acknowledges 202; compile/run returns started before the pipeline finishes.
- Later read-back: Progress, sources, extractions and plans drive subsequent retry; pages and aliases enter later compilation/consumption.
- Delegated visibility: n8n receives the session ID; Python routes receive task-specific inputs; provider calls receive constructed text, not the whole app database.
- Selection predicate: Included staged rows and source/plan database state; background code decides each successive step.
- Invalidation or expiry: Cancelled/failed/completed progress affects admission; retry filters existing extractions/plans rather than blindly restarting everything.
- Activation or effect: Wired ingestion, model dispatch, durable control-state writes and page admission; actual completed invocation unobserved.
- Evidence limits: In-process background work is not proof of crash-surviving execution or exclusion across every direct endpoint.

> runCompilePipeline(session_id).catch((err: unknown) => {
> --- `app/src/app/api/compile/run/route.ts`

#### RT-RTE-plan-draft
Label: Source analysis, page selection and drafting

Extraction and name resolution supply canonical objects; model triage and symbolic planning select page changes; draft calls propose prose; deterministic crossref transforms it before admission. App code owns thresholds, planning, state and layer order. Models judge ambiguous identity/update candidates and author text. User selection starts the workflow but is not per-page approval. Admission remains [RT-RTE-draft-approval](#rt-rte-draft-approval). SRC-1: `app/src/app/api/compile/extract/route.ts`, `app/src/app/api/compile/resolve/route.ts`, `app/src/app/api/compile/match/route.ts`, `app/src/app/api/compile/plan/route.ts`, `app/src/app/api/compile/draft/route.ts`, `app/src/app/api/compile/crossref/route.ts`, `nlp-service/services/llm_client.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Structured extraction/match/plan/draft counts and stored plan prose; not necessarily an admitted wiki page.
- Later read-back: Aliases, historical mentions, prior page prose, raw sources and schema shape subsequent source/page calls.
- Delegated visibility: Model sees selected dossiers/sources and optional prior-page/schema context; prefix truncation can remove trailing sources; later draft layers receive prior-layer summaries.
- Selection predicate: Historical promotion counts, TF-IDF candidates above 0.15 capped at three, triage decisions, layer type and dossier relevance/recency caps.
- Invalidation or expiry: Retry replans when newly extracted sources are unrepresented; failed/planned drafts can be retried; committed plans are preserved.
- Activation or effect: Code wires model judgments into plan action and returned prose into stored drafts; semantic compliance and actual activation are unobserved.
- Evidence limits: No expected-answer oracle is used in this production selection path; model judgment and provenance do not certify truth.

Operating mode: open user-supplied sources, not a bounded curriculum or comparative experiment. Proposer: extraction/drafting models plus code planner. Decider: fixed planner and later commit/approval gates; caller can withhold inclusion, cancel, or reject pending content. Guidance is shipped prompts plus retained schema and existing prose; proposals persist as drafts, and triage reasons/contradictions can persist in activity records. This route does not assess whether arbitrary subject-matter prose formulates a theory.

> const topCandidates = tfidfResult.top_matches
>       .filter((m) => m.similarity > 0.15)
>       .slice(0, 3);
> --- `app/src/app/api/compile/match/route.ts`

> if len(prompt) > _GEMINI_INPUT_TOKEN_CAP:
>         prompt = prompt[:_GEMINI_INPUT_TOKEN_CAP]
>
>     prompt += cat_suffix
> --- `nlp-service/services/llm_client.py`

#### RT-RTE-draft-approval
Label: Automatic and explicit page admission

Compile commit handles crossreffed plans, null/thin gates and auto/manual modes. Explicit single/bulk approval uses `commitSinglePlan` for pending plans. Chat proposals reach this helper, but their ordinary page-ID `source_ids` violate provenance's source foreign key and return `commit_failed`; empty-citation manual saves or IDs also present in `sources` can pass that constraint. App code is the executor; the generated markdown is the change, SQLite outbox is first persistence, Python storage is later file effect. SRC-1: `app/src/app/api/compile/commit/route.ts`, `app/src/lib/approve-plan.ts`, `app/src/app/api/drafts/[plan_id]/approve/route.ts`, `app/src/app/api/drafts/[plan_id]/reject/route.ts`, `app/src/lib/db.ts`, `app/instrumentation.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Compile returns committed/failed/pending/flush counts; explicit approval returns committed true after database success even if file flush failed.
- Later read-back: Successfully admitted prose reaches wiki/MCP and future draft calls; ordinary chat page-ID provenance failure rolls back before an outbox is installed. Pending outbox content after database success supports startup/retry; FTS and vectors support later selection separately.
- Delegated visibility: Storage receives page ID and markdown; vector worker receives page ID/metadata; pending drafts remain visible to approval callers.
- Selection predicate: Auto-approve unless setting equals '0'; otherwise pending approval, with provenance-only exempt. Explicit approval requires pending state and nonempty content, not the compile thin-body check.
- Invalidation or expiry: Reject marks a pending row rejected and keeps it for audit; committed-plan states prevent ordinary repeated admission; no timed draft expiry inspected.
- Activation or effect: Database transaction changes page/provenance/FTS state; successful flush installs file content; downstream model behavioral change remains unobserved.
- Evidence limits: Approval API invocation does not establish a human reviewed the proposal; file/index consistency is not one atomic operation. The chat provenance obstruction is an implementation constraint, not an observed failure or measured rate; see [MEM-CLM-chat-provenance](memory.md#mem-clm-chat-provenance).

Trigger: compile commit or explicit approval. Proposer: drafting model or chat answer route. Decider/veto: configured software gates or an approval/rejection caller; the UI affords human decision but caller provenance is unresolved at the API. Operating mode: open content admission. Answer oracle: none in the inspected commit/helper. Guidance from earlier drafting persists in prose, not as an approval proof. Recovery: pending-content reconcile; previous file versions support inspection/recovery, not automatic semantic rollback. Compile durability policy is scoped in [RT-CLM-durable-completion](#rt-clm-durable-completion).

> export function getAutoApprove(): boolean {
>   return getSetting('auto_approve') !== '0';
> }
> --- `app/src/lib/db.ts`

> // DB commit succeeded — pending_content stays for boot reconciler.
> --- `app/src/lib/approve-plan.ts`

#### RT-RTE-schema-bootstrap
Label: Generated standing maintenance guidance

Compile schema checks existence, summarizes committed plans, requests model schema prose and writes `/data/schema.md`; draft loading later passes it to the model. The app owns installation; model proposes conventions. The existing file vetoes normal bootstrap replacement, but a failed existence check does not establish file absence. Deterministic app crossref/planning does not consume this prose as executable policy. SRC-1: `app/src/app/api/compile/schema/route.ts`, `app/src/app/api/compile/draft/route.ts`, `app/src/app/api/compile/crossref/route.ts`, `nlp-service/services/llm_client.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Schema-generated result/path or already-exists/no-committed-pages/provider/write error.
- Later read-back: The schema file enters later draft model inputs across sessions.
- Delegated visibility: Generator sees plan title/type/category summaries; drafting sees schema prose when the file can be loaded.
- Selection predicate: Bootstrap when file is not confirmed present and committed plans exist; no periodic criticism/revision predicate inspected here.
- Invalidation or expiry: Existing schema skips ordinary regeneration; import can install another schema; no expiry in this route.
- Activation or effect: File installation and delivery as conventions are wired; compliance and behavioral influence of its contents are unobserved.
- Evidence limits: No execution sample of schema text was supplied; the generator's requested coverage is not proof of the generated content or its correctness.

Admission: software accepts nonempty generation and a successful write, without per-schema human approval in this handler. Operating mode: open first-session bootstrap, not an oracle-backed experiment. Answer oracle: none inspected. Recovery: retry on provider/write failure; a stored file prevents normal regeneration; automatic rollback is not established here.

Theory account: the generator requests a localized maintenance rule set—page creation, naming, frontmatter, links, contradiction handling and quality standards. It derives conventions from initial page metadata rather than criticizing an existing method against measured outcomes. The schema is retained guidance, not evidence of a theory builder.

Theory-builder conditions 1–4:

- condition 1 implementation conclusion status: afforded
- condition 2 implementation conclusion status: wired
- condition 2 operation conclusion status: uninspected
- condition 3 conclusion status: uninspected
- condition 4 conclusion status: uninspected

Condition 1: one whole natural-language rule document can carry the requested conventions; no actual generated instance inspected. Condition 2: draft input requests dependence on those conventions, without observed compliance. Condition 3: generator/bootstrap paths supply no evidence of content-directed criticism of a formulated schema; inaccessible model processing is not an absence finding. Condition 4: cross-session delivery exists, but no criticism-result-to-next-round trace was supplied.

Addressability: a whole Markdown document is independently replaceable; actual assumption/scope granularity is uninspected. Persistence: file spans sessions and later drafting is wired. Learning: improved future capacity and attribution uninspected. Reflection: page metadata feeds a representation of maintenance conventions and conventions return to drafting; this is a limited wired feedback possibility, not observed criticism of its own operation. Reflective/autonomous theory-builder and self-improvement membership are not established by this bootstrap; critic/iteration/evidence-responsive links remain unestablished independently of delivery.

> Write the schema as a concise markdown document. It will be used as standing
> instructions for the LLM on all future wiki updates.
> --- `nlp-service/services/llm_client.py`

#### RT-RTE-chat-feedback
Label: Wiki answering and pending FAQ creation

App chat → retrieval → Python page selection/synthesis → persisted answer and optional pending draft. App owns context limits and draft trigger; selection model or fixed hybrid scoring chooses pages; answer model proposes an answer. SRC-1: `app/src/app/api/chat/route.ts`, `app/src/lib/retrieval.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Answer/citations/pages-used, a metadata/no-content response, or synthesis error; user message is inserted before later failures.
- Later read-back: Up to ten entries from the earliest timestamp-ordered stored session rows enter later turns; unselected rows remain stored. Pending FAQ adoption is blocked by ordinary page-ID provenance unless every stored ID also exists as a source ID; exceptional successful approval permits later wiki retrieval.
- Delegated visibility: At most ten selected readable pages, first five clipped to 2000 characters and remainder to 300; up to ten role/content history entries supplied to synthesis, without historical citation metadata. Python applies history[-10:] to this already bounded selection; external provider state is opaque.
- Selection predicate: Small-index model selection or larger-index FTS/vector/source-count/recency ranking; empty/failed selection can fall back to popular pages. History uses session equality, ascending timestamp and LIMIT 11, then slice(0, -1), not a descending recent-tail query. FAQ trigger is retrieved count >=3.
- Invalidation or expiry: Once history exceeds eleven rows, later rows are excluded and the dropped final selected row need not be the current question; the current question is supplied separately. This selection produces no summary and deletes no stored rows. Page-ID draft cleanup covers pending sessions matching chat-% only; automatic drafts keep the caller's unchanged session ID, so nonmatching sessions are not covered. Pending approval can reject content.
- Activation or effect: Wired answer/history writes and best-effort pending FAQ creation; no evidence that a FAQ improved later answering.
- Evidence limits: Pages-used counts delivered candidates, not verified use or attribution; selection/synthesis requests are not semantic guarantees.

Admission: model-generated answer and caller question form a pending draft; code inserts it best effort, then explicit approval attempts installation. `insertChatDraft` stores retrieved page IDs in `source_ids`; `commitSinglePlan` inserts them into provenance whose foreign key references `sources(source_id)`, with app foreign keys enabled. Ordinary disjoint IDs cause transaction rollback and `commit_failed`, leaving the proposal pending rather than installing a FAQ. A manual save with empty citations has no IDs to insert; imported or deliberately coincident source/page IDs can satisfy the constraint. These exceptions do not establish ordinary automatic adoption. Starting chat is not per-content approval. Operating mode: open questions; metadata bypass uses database facts, not an expected-answer oracle for synthesis. Answer oracle: none inspected for synthesis. Guidance: wiki-grounding prompts and clipped selected prose. Rejection/recovery: pending draft rejection; synthesis failures leave the already inserted question; approval uses the separate outbox path. The retained result is prose/history, not an update to provider parameters. Learning or exercised self-improvement is unestablished: the source establishes answering, history read-back and pending proposal creation, with constrained adoption, not an ordinary end-to-end compounding cycle, evidence-responsive improvement or subsequent causal dependence.

The history correction agrees with [MEM-RTE-history-read](memory.md#mem-rte-history-read); the provenance constraint agrees with [MEM-CLM-chat-provenance](memory.md#mem-clm-chat-provenance). Added SRC-1 implementation inspection: `app/src/lib/db.ts`, `app/src/lib/approve-plan.ts`, `scripts/migrate.py`, `app/src/app/api/chat/save-draft/route.ts`. Manual save prefixes its session as `chat-manual-` and maps citation page IDs into the same helper; automatic creation does not add that prefix. Cleanup therefore cannot be generalized to every automatic FAQ or to semantic removal from retained prose. No long conversation or adoption failure was executed.

> ORDER BY created_at ASC
>        LIMIT ?`
> --- `app/src/lib/db.ts:2193-2203`

> .slice(0, -1)
> --- `app/src/app/api/chat/route.ts`

> .run(data.plan_id, data.session_id, data.title, JSON.stringify(data.pages_used ?? []), data.draft_content);
> --- `app/src/lib/db.ts`

> insertProvenance({ source_id: sid, page_id, content_hash: contentHash, contribution_type: contribType });
> --- `app/src/lib/approve-plan.ts`

> source_id TEXT NOT NULL REFERENCES sources(source_id),
> --- `scripts/migrate.py:45-52`

> _db.pragma('foreign_keys = ON');
> --- `app/src/lib/db.ts`

> AND session_id LIKE 'chat-%'
>           AND EXISTS (SELECT 1 FROM json_each(source_ids) WHERE value = ?)`
> --- `app/src/lib/db.ts`

> markdown: i < 5 ? p.content.slice(0, 2000) : `[Summary only] ${p.content.slice(0, 300)}`,
> --- `app/src/app/api/chat/route.ts`

> if (pages.length >= 3) {
> --- `app/src/app/api/chat/route.ts`

#### RT-RTE-mcp-read
Label: External agent wiki consumption

Stdio MCP handlers fetch app search/page/index/health APIs and return formatted text to an external client. Kompl code owns request execution and formatting, not client scheduling or answering. SRC-1: `mcp-server/index.ts`, `app/src/app/api/wiki/[page_id]/data/route.ts`, `app/src/lib/db.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Search metadata, page prose/provenance, filtered listing, statistics or explicit network/status errors as text.
- Later read-back: Retained wiki prose can be requested in later external invocations; this read route accumulates no new knowledge itself.
- Delegated visibility: External client receives formatted content; its own prompt/context inclusion and tool grant set are uninspected.
- Selection predicate: Explicit query/page ID/category/type supplied by client; list filters are client-side; read by ID returns that stored page.
- Invalidation or expiry: Current page files/database rows define later reads; external client caching/expiry is outside boundary.
- Activation or effect: Tool-result delivery is wired; downstream agent action or compliance is unobserved.
- Evidence limits: Read-only server tool surface does not constrain the external agent's other tools or local API access.

> const content = readPageMarkdown(page_id) ?? '';
> --- `app/src/app/api/wiki/[page_id]/data/route.ts`

#### RT-RTE-source-maintenance
Label: Source deletion and surviving-page redraft

Shared delete helper prunes source-associated state and chooses page deletion, note/count fallback or redraft. `recompilePage` proposes replacement prose from remaining readable sources, installs an outbox transaction, flushes, syncs links and requests vectors. App code owns admission; it does not ask the compile approval setting. SRC-1: `app/src/lib/source-delete.ts`, `app/src/lib/recompile.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Delete outcome/counts; redraft returns rewritten/archived or throws to the caller's fallback.
- Later read-back: Remaining or redrafted page prose and changed source/provenance state reach later wiki/draft/query consumers.
- Delegated visibility: Redraft model gets remaining readable raw sources and categories, but explicitly null existing content/schema and no related pages.
- Selection predicate: Remaining-source count, batch sibling exclusions and current short-source threshold; <=1 remaining leads to page deletion, short-source branch to a note, otherwise redraft.
- Invalidation or expiry: Removed source and selected pages/drafts lose their normal read path; file/vector deletions may run best effort. A retained note branch does not remove all derived prose.
- Activation or effect: Wired direct database/content changes and best-effort secondary effects; semantic removal accuracy is unobserved.
- Evidence limits: A flush/link failure can occur after outbox installation; caller fallback is not full rollback of prior effects.

Trigger: caller deletion. Proposed change: remove pages or rewrite surviving pages without the removed source. Proposer: code cascade and drafting model; decider: cascade rules, not human review of replacement prose; caller can choose not to initiate deletion. Operating mode: open maintenance. Answer oracle: none inspected. Guidance: shipped page prompt/categories; prior schema intentionally omitted. Recovery: outbox flush reconciliation, note/count fallback and previous file archive; automatic semantic rollback is not established.

> existing_content: null,
>       schema: null,
> --- `app/src/lib/recompile.ts`

#### RT-RTE-archive-import
Label: Direct archive restoration

Local multipart caller supplies a Kompl ZIP; app checks manifest/empty wiki/safe IDs and directly restores compressed files, schema, database rows/settings and optional vectors. No drafting model decides whether these contents are true. SRC-1: `app/src/app/api/import/route.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Imported counts or validation/precondition error; secondary vector restoration is asynchronous.
- Later read-back: Restored pages, schema, aliases, histories/plans and settings enter ordinary consumers; stored vectors can be restored without re-embedding.
- Delegated visibility: App receives archive material; vector service receives supplied embedding entries or later backfill request.
- Selection predicate: Kompl manifest and no existing user pages, safe page/source IDs; rows and basename-selected raw/page buffers come from the archive.
- Invalidation or expiry: System saved-links state is cleared; import rejects a nonempty user wiki. No content expiry is added.
- Activation or effect: Direct restoration is wired, bypassing compile thin gates and per-page approval; files are physically written by app rather than Python page writer.
- Evidence limits: SQLite rollback does not undo filesystem writes; archive choice does not prove human review of each restored item or embedding provenance.

Admission: caller chooses archive, fixed software checks accept structure, app writes. Rejection: manifest, ID and empty-wiki guards. Operating mode: open restoration, no answer oracle. Guidance is imported schema/settings rather than a model proposal process. Recovery: route has no complete cross-filesystem rollback; external backup/restore is an operator responsibility. No theory criticism or improved capability is inferred from restoring content.

> for (const [filename, buf] of pageBuffers) {
>       fs.writeFileSync(path.join(DATA_ROOT, 'pages', filename), buf);
>     }
> --- `app/src/app/api/import/route.ts`

#### RT-RTE-product-update
Label: Operator-invoked product update

CLI checks Docker and Git repository, fast-forwards source, relinks CLI, pulls images, builds/restarts and polls health. The proposed successor is upstream repository/image content, not a locally generated code candidate. CLI owns execution; operator invokes it with local Git/Docker authority. SRC-1: `cli/src/commands/update.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ready/degraded message or failure/health-timeout process exit.
- Later read-back: Installed code/configuration governs later service runs; no memory read-back is implied by unchanged data volumes.
- Delegated visibility: Git, package relink and Docker helpers receive project-directory context; external repository/image internals beyond the frozen source are outside evidence.
- Selection predicate: Operator invocation, repository/Docker checks and fast-forward pull; health poll is readiness evidence, not an answer oracle or semantic regression verdict.
- Invalidation or expiry: New build replaces running machinery; installed revision is not pinned to this analysis by the updater.
- Activation or effect: Code wires successor fetch/build/restart; deployment success is unobserved.
- Evidence limits: This handler has no automatic full rollback if relink/build fails after source pull; helper internals and upstream authenticity were not audited.

Admission: upstream proposes released changes; operator initiates, fast-forward and build checks gate progression, no model decides successor. Operating mode: open maintenance, not self-improvement experiment. Guidance: fixed update sequence; changes persist as installed files/images. Rejection/recovery: exits on stage errors, logs/health troubleshooting on timeout; automatic reversion not established.

> pullFfOnly(config.projectDir)
> --- `cli/src/commands/update.ts`

### Claims

#### RT-CLM-durable-completion
Label: Session completion waits for page flush

The driver claims never to signal completion with committed page files missing. Owner: app compile driver plus session-scoped commit reconcile. Enforcement: nonzero `flush_failures` throws before completion. Strength: policy with outbox/retry protocol, not a deployment or filesystem power-loss guarantee. Coverage: session committed content plans; provenance-only/pending/rejected/thin/failed content is not universally admitted. Alternate approval returns success on flush failure; import and direct storage are not covered by this driver gate. External contract: successful storage response, gzip/write/rename behavior and durable SQLite/volume behavior. SRC-1: `app/src/app/api/compile/run/route.ts`, `app/src/app/api/compile/commit/route.ts`, `app/src/lib/approve-plan.ts`, `nlp-service/services/file_store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- guarantee strength: policy

> if (commitResult.flush_failures > 0) {
> --- `app/src/app/api/compile/run/route.ts`

The name “completed” also does not certify every source extracted or every draft succeeded: extraction can continue after partial failure, and draft failure counts are reported without automatically aborting later steps. This narrows the claim to committed-file flush policy, not content completeness.

#### RT-CLM-local-isolation
Label: Local-only deployment and database ownership

Compose claims unauthenticated single-tenant APIs should be loopback-only and app should alone open SQLite. Owner: deployment configuration/operator for network exposure; application/service implementations for database convention. Strength: deployment guarantee conditional on this Compose port binding and host/proxy controls, but **policy** for shared-volume database ownership. Capability and configured grants differ: NLP/n8n have the same read-write data volume, so lack of database-opening calls is not an isolation permission. Direct local callers remain materially equivalent paths to mutation. SRC-1: `docker-compose.yml`.

- implementation conclusion status: wired
- deployment conclusion status: uninspected
- guarantee strength: deployment guarantee

> - "127.0.0.1:3000:3000"
> --- `docker-compose.yml`

> # default; the enforcement is at the code layer: nlp-service never
> --- `docker-compose.yml`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-schema-drafting
Label: Schema instruction authority over drafting

Consumer: page-drafting model. Channel: schema prose loaded from file and inserted into the user prompt with “follow these conventions.” Force: requested natural-language instruction, not enforced planner policy. Horizon: later compile sessions while the schema remains installed/loadable. Delivery is wired; compliance and benefit unobserved. The generated schema cannot override the code's deterministic page planner merely because it requests creation conventions. SRC-1: `app/src/app/api/compile/draft/route.ts`, `nlp-service/services/llm_client.py`; passage in [RT-OBJ-schema](#rt-obj-schema).

#### RT-BAP-wiki-answering
Label: Wiki evidence supplied to answer models and agents

Consumers: built-in answer model and external MCP agent. Channels: clipped selected-page prompt versus formatted page tool result. Force: source/context content interpreted by a model; no fixed-rule enforcement of truth. Horizon: later questions or client requests after admission/restoration. The two delivery paths differ in selection, clipping and outbox fallback; neither establishes downstream compliance. SRC-1: `app/src/app/api/chat/route.ts`, `mcp-server/index.ts`, `app/src/app/api/wiki/[page_id]/data/route.ts`; passages in [RT-RTE-chat-feedback](#rt-rte-chat-feedback) and [RT-RTE-mcp-read](#rt-rte-mcp-read).

## Annotations

none

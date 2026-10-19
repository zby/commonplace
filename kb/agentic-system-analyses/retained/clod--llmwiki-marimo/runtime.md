---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Runtime baseline of llmwiki-marimo: ingestion, three chat modes, save admission and maintenance at the frozen source revision."
run-id: AAS-2026-10-18-llmwiki-marimo-58054ccd9ae7-01
reviewed-boundary: "0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7"
---

# llmwiki-marimo runtime report

## Runtime account

### Evidence and consequential work

This is an implementation account of SRC-1 at the boundary's frozen commit, not a report of executed workloads. No target, tests, examples or providers were run. Model compliance, exercised activation, performance and benefit remain unobserved. The target produces retained knowledge from documents, maintains pages and indexes, and consumes them in later chat. It is not just a returning chat agent. Its ingestion and save services own writes, while its standard chat agent receives retrieval tools (SRC-1, `base/services/ingest.py`, `base/services/chat.py`, `base/domain/chat/agent.py`).

Added inspection beyond the boundary's initial pass includes the complete agent factory and chat service; selected bodies in pre-retrieval, history, grounding, generators, repair dispatch, settings/vocabulary, verification NLI and model-evaluation code; and their web/marimo callers. These supply implementation evidence. The concept-update template supplies doctrine/design evidence. All remain SRC-1; no new evidence source or execution layer is introduced.

### Ordinary shipped invocation

The quickstart launches uvicorn against `web.app:app`; the shipped web app and retained marimo apps both call shared services. Quickstart's localhost URL is an operator convenience, not evidence of a deployment sandbox. A workspace identifies files and its SQLite database; web application state caches agents per open wiki. Conversation and turn IDs select application-held message lists and pending turns (SRC-1, `quickstart.py`, `web/state.py`, `web/routes/chat.py`, `marimo/read_app.py`, `marimo/read_app_tabs.py`).

An ordinary end-to-end use begins with an upload or source scan. The service invokes the document pipeline, which validates formats/extractor availability, checks whether the source needs ingestion, extracts and chunks text, commits source rows, requests model extraction, and creates or merges concept pages. It writes a summary, references and index entries; non-batch ingestion updates overview/log/history. Upload orchestration then performs scoped reconciliation, cross-linking and optional verification. Computation admits generated page content without a per-page approval step. Failure returns an `IngestResult`, with compensating page recovery rather than one global transaction. See [RT-RTE-document-ingest](#rt-rte-document-ingest) and [RT-RTE-wiki-maintenance](#rt-rte-wiki-maintenance).

The web chat POST defaults to pre-retrieval. It appends a user message and returns bubbles that open an SSE request; the stream handler obtains the cached agents and dispatches the selected mode. In pre-retrieval, code first removes refused exchanges, compacts advisory tables and caps prior history. A lexical scope/roster gate then selects wiki chunks, raw-source chunks, collection pages or data-tool routing. An optional condenser rewrites an otherwise uncovered follow-up. Code injects selected context into a localized template; PydanticAI owns the subsequent answer/tool loop. The final `ChatResult` returns answer, passages, substitutions, path and token totals. The web handler stores the assistant message, renders it and optionally annotates unsupported sentences. Exceptions produce an error event and remove the pending question. See [RT-RTE-preretrieval-chat](#rt-rte-preretrieval-chat).

Saving is another user action, not a chat tool call. Web drafting structures answered exchanges into a concept page and displays an editable review dialog. Save submits title and Markdown; the service writes it, repairs deterministically and commits. Marimo instead passes its last response to `save_answer`, which structures and writes without an intervening draft review. See [RT-RTE-chat-save](#rt-rte-chat-save). Source content, prompt instructions and code rules have different force, described in [RT-BAP-chat-instructions](#rt-bap-chat-instructions).

### Control envelope and forcing cases

Four inspected forcing cases qualify tempting system-wide claims:

1. **Strict versus streaming grounding.** Strict mode calls `enforce_grounding` after an agent run. Streaming invokes the full agent event stream but emits text immediately and applies no equivalent post-check. Both are reachable via web mode selection and marimo dispatch. Thus grounding is mode-scoped, not universal ([RT-RTE-strict-chat](#rt-rte-strict-chat), [RT-RTE-streaming-chat](#rt-rte-streaming-chat)).
2. **Pre-retrieval alternatives.** The gate covers the original question and an accepted condensed rewrite. An open page can supply coverage; collection questions can obtain overview/index directly; known-data/advisory questions can run with no injected context. Tool-result grounding is checked only when `plan.context is None`; raw-source context additionally gets lexical coverage testing, while curated context does not. This is deliberate branch-specific enforcement, not proof that every sentence follows evidence ([RT-RTE-preretrieval-chat](#rt-rte-preretrieval-chat)).
3. **Review is a caller protocol.** The web review UI provides an opportunity to edit/veto, but `/chat/save` accepts nonempty submitted Markdown without requiring a prior draft or verification token. Marimo's `save_answer`, and the service's `save_conversation`, have no review interval. The latter explicitly drafts and saves sequentially. Human initiation does not establish approval of each generated proposition ([RT-RTE-chat-save](#rt-rte-chat-save)).
4. **Malformed extraction does not necessarily reject admission.** JSON parse failure can return the raw response as `document_summary` with no concepts. The pipeline still builds the summary. The parser is therefore a representation fallback, not a truth or universal format-admission gate ([RT-RTE-document-ingest](#rt-rte-document-ingest)).

There is also a shipped direct-agent evaluator: it calls `run_sync` without service guardrails, then grades output. This prevents extending service-level guarantees to all model calls ([RT-RTE-model-evaluation](#rt-rte-model-evaluation)). Direct OpenAI calls in generation similarly do not pass the chat guardrail. The smallest inspected enforcement surface is the service branch, not the model endpoint.

**Capability surface, grants and isolation differ.** `create_agent` can accept arbitrary Python `extra_tools` and prompt additions. `build_agents` currently grants wiki/source retrieval plus conditionally activated dataset/finance tools; the pre-retrieval agent omits the three wiki retrieval tools, and the condenser is built without workspace or extra tools. Finance activates only after manifest validation has a passing category. These are composition-time grants, not a model-selected extension install mechanism (SRC-1, `base/domain/chat/agent.py`, `base/services/chat.py`, `base/domain/finance_argentina/agent_tool.py`). The factory's extensibility prevents interpreting its read-only intent as an invariant over arbitrary external callers.

The inspected chat registration supplies no shell or write tool; this says nothing about arbitrary injected Python tools. Extraction and history management can invoke host subprocesses outside the chat tool loop (SRC-1, `base/domain/ingestion/extractor.py`, `base/domain/rollback/revert.py`). Effects execute with the application's filesystem/database/provider access. No supplied deployment establishes an OS isolation envelope or current user permissions. Provider-native behavior, dependency-level retries and tool execution isolation remain outside the inspected integration. Temperature settings are requests to the provider, not evidence of deterministic model output ([RT-CMP-openai-model](#rt-cmp-openai-model)).

The web busy lock serializes selected mutation jobs/save operations; services explicitly rely on callers for locking. It is not a cross-process transaction or protection of every library caller (SRC-1, `web/state.py`, `web/routes/chat.py`, `base/services/wiki.py`). Runtime tracing and context/token capture provide audit material, not an independent answer oracle. Optional verification marks answers or stored pages rather than universally blocking them. Its numerical classifier is separate from the generation model ([RT-CMP-local-nli-verifier](#rt-cmp-local-nli-verifier)).

### Guarantee ledger

| Guarantee / owner | Enforcement point and strength | Covered and alternate paths | External contract and limits | Conclusion statuses |
|---|---|---|---|---|
| Strict answer must have a substantive tool return / chat service | `enforce_grounding`; invariant of this post-processing branch | Strict service return; not streaming, direct agents or injected pre-retrieval context | PydanticAI message typing/history; substring sentinels approximate substantive evidence. `all_messages()` may include supplied history. Does not prove answer entailment. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Pre-retrieval retrieval/scope gate / pre-retrieval orchestrator | `plan_retrieval` plus pre/post checks; invariant of branch dispatch, best effort for evidential sufficiency | Original and rewritten questions; open-page, collection, dataset/advisory and source routes differ | SQLite/data/file correctness and provider output; lexical coverage is not semantic verification | implementation conclusion status: wired; operation conclusion status: uninspected |
| No autonomous wiki saving by standard chat tool set / composition root | Registered tools; invariant of inspected standard grants | Standard retrieval agents; separate UI/services persist; arbitrary `extra_tools` not covered | Registered Python tools and PydanticAI contract; not an OS permission boundary | implementation conclusion status: wired; operation conclusion status: uninspected |
| User may review web conversation draft / web UI | Two-step dialog; protocol | Normal web dialog; save endpoint does not enforce draft provenance, marimo/service convenience path lack review | Human must inspect/veto; deterministic post-save repairs may still change the page | implementation conclusion status: wired; operation conclusion status: uninspected |
| Recover failed writes / ingestion and history services | Compensation and forward restore; best effort | Pipeline-created/overwritten pages; Git/index restore when prerequisites hold | Not an all-artifact transaction; Git/extractors/snapshots required. No crash-consistency proof | implementation conclusion status: wired; operation conclusion status: uninspected |

Ledger evidence is SRC-1, `base/services/chat.py`, `base/domain/chat/guardrail.py`, `base/domain/chat/preretrieval.py`, `base/domain/chat/agent.py`, `web/routes/chat.py`, `base/domain/ingestion/pipeline.py`, `base/domain/rollback/revert.py`; minimum passages are retained in the corresponding records below. These guarantees do not establish exercised reliability or causal improvement.

## Shared records

### Components

#### RT-CMP-openai-model
Label: Configured OpenAI-compatible generation models

Source-native identity: `OpenAIChatModel(model, provider=...)` for answer/condenser agents, and `client.chat.completions.create(model=model, ...)` for generation. Distributed-parametric content resides behind configured local or remote model endpoints; exact weights and substrate are opaque. Chat and ingestion can use different settings. Parameters are not updated by the inspected inference integrations; provider-side training/state is uninspected. Exact model versions are not pinned by this repository's caller-supplied name. A mutable endpoint/name can resolve to another model. `temperature=0.0` for chat and higher generation temperatures constrain requested sampling, not implementation-independent determinism (SRC-1, `base/domain/chat/agent.py`, `base/domain/ingestion/wiki_generator.py`, `web/state.py`).

> llm = OpenAIChatModel(
>         model,
>         provider=_make_provider(base_url, api_key),
>     )
> --- `base/domain/chat/agent.py`

`_make_provider` selects the dedicated OpenRouter provider for its hostname and otherwise uses the supplied OpenAI-compatible base URL. No supplied execution establishes provider compliance or quality. This container groups the same configurable inference mechanism, not a claim that chat, condensation and ingestion use one immutable weight set.

#### RT-CMP-local-nli-verifier
Label: LocalNliVerifier

Source-native identity: `LocalNliVerifier`; distributed-parametric sequence-classifier weights and tokenizer loaded from the local Hugging Face cache. Default model name is `MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7`; a constructor can supply another. Exact model revision is not pinned; different cache contents/model-name resolutions can supply different parameters. Inference uses `.eval()` and `torch.inference_mode()` and does not train weights. Unlike the generation component this integration uses cached artifacts, not a live generation endpoint. Initial download/cache provenance and weights are uninspected (SRC-1, `base/domain/verify/nli.py`).

> self._model = AutoModelForSequenceClassification.from_pretrained(
>             self.model_name, local_files_only=True,
>         ).eval()
> --- `base/domain/verify/nli.py`

It scores passage/sentence pairs; tokenization truncates only the passage side. Its maximum-length and scoring behavior bound what verification sees. Web integration uses it optionally to annotate, not to establish an unconditional refusal gate (SRC-1, `web/routes/chat.py`).

### Operative objects

none declared in this member

### Routes

#### RT-RTE-document-ingest
Label: Document ingestion and page admission

Endpoints: upload/scan callers → ingest service → pipeline → retained wiki and source index. Human supplies documents and starts work; deterministic pipeline owns progression, while generation calls propose summaries/concepts/merged prose. UUID document IDs, relative source paths and generated slugs connect source rows and pages. Source text is committed before generation. Existing concept body and new insight go to `build_concept_page`; generated Markdown is passed to `create_page(overwrite=True)`. SQLite rows/chunks/references and filesystem pages/index/overview/log are effects, not one atomic transaction (SRC-1, `base/services/ingest.py`, `base/domain/ingestion/pipeline.py`, `base/domain/ingestion/wiki_generator.py`).

- Immediate return: `IngestResult` per file with ingested/skipped/failed status and progress callbacks; upload orchestration returns the result list.
- Later read-back: Existing concept pages enter later ingestion merges; wiki/source indexes and pages enter later retrieval. Overview/index enter collection chat.
- Delegated visibility: Extracted text goes to model extraction; concept updates receive existing body and new insight. Models do not receive unrestricted database ownership.
- Selection predicate: Supported file and extractor availability, `needs_ingestion`, extracted concept names/slugs and upload touched-page IDs determine work.
- Invalidation or expiry: Changed sources are eligible for reingestion; page overwrite clears stale state and replaces derived content; secondary aliases can fail independently.
- Activation or effect: Code writes model-proposed Markdown and derived state without per-content human approval; later use is wired, successful semantic activation unobserved.
- Evidence limits: No execution or factual-quality evidence; compensation does not establish global rollback of aliases, overview, log, index and source rows.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: open document-processing requests, not a curriculum or candidate tournament. Code rejects invalid inputs or handles exceptions; the operator can withhold the job, but there is no per-generated-page veto in this path. No independent answer oracle is used. Templates guide extraction and merging; the update instruction says:

> Integrate the new insight. Add the source to the Sources section as a new list item: - {filename}.
> Keep all existing content. Output only the updated markdown page.
> --- `prompts/concept_update_template.en.md`

This is model guidance, not enforced preservation. The consumer strips existing frontmatter before constructing the update prompt (SRC-1, `base/domain/ingestion/wiki_generator.py`). A representation-error forcing branch is explicit:

> except (json.JSONDecodeError, TypeError):
>         logger.warning("extract_structured: JSON parse failed for %s, using fallback", filename)
>         return ExtractionResult(document_summary=raw, concepts=[])
> --- `base/domain/ingestion/wiki_generator.py`

Recovery snapshots pages before overwrites and compensates on caught failure, marks the source failed and returns an error. It is not evidence of semantic rejection or rollback after every process crash:

> rolled_back = _rollback_wiki_pages(db_path, workspace, wiki_compensations, language=language)
> --- `base/domain/ingestion/pipeline.py`

No claim of formulated theory criticism, learning or improved capacity follows from merging insights; those properties require distinct evidence.

#### RT-RTE-preretrieval-chat
Label: Code-selected pre-retrieval chat

Endpoints: web/marimo turn → history shaping → gate/retrieval → optional condenser → answer agent → post-processing. Code owns scope and context selection; the model owns answer phrasing and any granted dataset/overlay calls. Workspace/db dependencies, conversation ID, current question, selected page and trimmed prior messages supply context. Natural-language prompts/passages feed a distributed-parametric model; symbolic predicates choose which material arrives (SRC-1, `base/services/chat.py`, `base/domain/chat/preretrieval.py`, `base/domain/chat/history.py`).

- Immediate return: Final answer or rendered refusal plus `ChatResult` context, generated additions, raw substitution, path and token counts; web returns SSE-rendered content.
- Later read-back: Caller-kept exchanges become later history after refusal removal, table compaction and last-six-message slicing; current injected passages alone are not automatically retained as a wiki page.
- Delegated visibility: Condenser receives a composed question/history prompt, returns only a rewrite; answer agent receives selected passages plus trimmed prior conversation, not an independent sub-agent transcript.
- Selection predicate: Blacklist first; roster/dataset names and aliases, advisory/collection intent, open-page body, FTS wiki hits then raw hits; an uncovered follow-up with history may be condensed and rechecked.
- Invalidation or expiry: Model history drops refused exchanges, table tails and older messages; full UI answers remain caller-held. Wiki/data tools can retrieve external-to-window content again; discarded old turns have no automatic full-history reload here.
- Activation or effect: Code can refuse before answer generation; raw-source answers get lexical coverage testing; context-free data answers need a substantive tool result. Curated-context delivery does not establish semantic compliance.
- Evidence limits: No executed scope or quality result; condensation's internal processing is opaque. No universal entailment guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The deciding agents for context control are code rules and, conditionally, one model rewrite call. This resembles an isolated rewrite frame whose return escapes, but does not expose a shared addressable heap: earlier UI content is not a dereferenceable pointer in the model window. Compacted advisory values can be recomputed by tools; removed conversation text is not automatically recoverable through that mechanism.

> if condense is not None and history and not (in_roster or has_data or open_block):
> --- `base/domain/chat/preretrieval.py`

> if plan.context is None:
>         grounded = has_grounding(messages)
> --- `base/domain/chat/preretrieval.py`

> return compacted[-(max_turns * 2):]
> --- `base/domain/chat/history.py`

No answer oracle is involved in this open QA mode. Scope lists and lexical thresholds are code/configuration rules; the model is not judging candidate successors. Collection pages and current open page are explicit alternative context routes, so absence of FTS hits does not imply absence of delivered knowledge.

#### RT-RTE-strict-chat
Label: Strict agentic retrieval and post-check

Endpoints: turn service → `agents.agent.run` → tool/model loop → grounding gate → table/citation post-processors. PydanticAI owns model/tool iteration; code owns final return substitution. The standard tools read wiki pages, search wiki/source text and optionally query dataset/finance data. Tool execution uses the db dependency and host process (SRC-1, `base/services/chat.py`, `base/domain/chat/agent.py`, `base/domain/chat/guardrail.py`).

- Immediate return: `ChatResult`, with refusal substituted when the run's messages lack a substantive tool result, otherwise post-processed answer.
- Later read-back: Caller-kept answer can enter later shaped history or be explicitly saved; tool messages are not themselves the caller's turn-history representation.
- Delegated visibility: Registered tool inputs/results and prior shaped text go through the agent; no separate worker delegation is wired in this service.
- Selection predicate: Model chooses tool calls under prompt guidance; deterministic substring markers classify tool-return content as substantive.
- Invalidation or expiry: Same refusal filtering/history cap as pre-retrieval; result context is turn-local unless caller retains it.
- Activation or effect: Code changes the returned answer on failed proxy grounding and appends tables/citations where possible; does not prove answer-source entailment.
- Evidence limits: `result.all_messages()` is supplied to the checker, not an explicitly isolated current-turn tool list; provider/PydanticAI history semantics matter. No observed run or sentence-correctness guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return output if has_grounding(messages) else refusal
> --- `base/domain/chat/guardrail.py`

The check accepts any substantive `ToolReturnPart`, not a domain-specific verified fact. A tool result that the answer ignores can still pass. This is an invariant of output substitution under the check's predicate, not invariant truth. Open QA has no reference-answer oracle. Streaming and the evaluator are materially equivalent model-entry alternatives that omit this service post-check.

#### RT-RTE-streaming-chat
Label: Unchecked streaming agent route

Endpoints: web/marimo streaming selection → `run_stream_events` → text deltas → final result. Same retrieval-agent grants and shaped prior history as strict mode, but a different return boundary. Code consumes all event rounds and yields text parts as they arrive (SRC-1, `base/services/chat.py`, `web/routes/chat.py`, `marimo/read_app.py`, `marimo/read_app_tabs.py`).

- Immediate return: Text chunks, then final `ChatResult` with collected passages/path/tokens; string-only wrapper emits only chunks.
- Later read-back: Full assembled text becomes caller-kept assistant history and can be explicitly saved.
- Delegated visibility: Model-selected tool calls/results use the same agent dependency as strict mode.
- Selection predicate: Human/UI mode choice; model chooses tools, code selects text-start and text-delta events.
- Invalidation or expiry: Prior history is shaped as in other modes; emitted text cannot be made unseen by a later final event.
- Activation or effect: Immediate output display without strict grounding substitution, citation/table enforcement or web answer verification for this mode.
- Evidence limits: Source establishes reachable unchecked display, not a demonstrated incorrect answer.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> The streaming mode runs no check: each chunk is shown as it arrives.
> --- `base/services/chat.py`

Web validates that mode is one of the supported constants and explicitly dispatches streaming; this is not merely an unreachable helper. No answer oracle or change-admission decision occurs during streaming.

#### RT-RTE-chat-save
Label: Chat-to-wiki admission

Endpoints: web draft/review/save or marimo last-response save → structuring/write helpers → retained concept/summary page. Web draft collects answered exchanges, drops refused/unanswered exchanges, and sends content plus any existing page to a model. Web save accepts title/Markdown and uses deterministic repair; marimo `save_answer` calls `save_to_wiki` with a model client and therefore can also invoke model-capable post-save repair. Title/category select directory and slug. Human initiates both; only the normal web dialog separates proposal from approval (SRC-1, `web/routes/chat.py`, `base/services/chat.py`, `base/domain/chat/wiki_tools.py`, `marimo/read_app.py`, `marimo/read_app_tabs.py`).

- Immediate return: Draft object/dialog before writing, or save confirmation after page/index/reference effects and repair; web service also commits history.
- Later read-back: Saved page enters retrieval and future same-slug structuring/merging; unsaved draft is not retained knowledge by this path.
- Delegated visibility: Structuring model receives selected conversation/last answer and existing page; reviewed web save does not send approved Markdown through another generation call.
- Selection predicate: User-selected title/category and answered exchanges or last marimo response; same slug determines replacement.
- Invalidation or expiry: Page can be overwritten/edited/deleted; web history supports later restoration subject to index prerequisites.
- Activation or effect: Software writes model-structured or user-edited Markdown and updates references/index. Deterministic repairs can modify post-save state, so raw submitted bytes are not guaranteed to be the ultimate page.
- Evidence limits: Neither save endpoint nor convenience service requires a verified draft provenance record. Human approval of every proposition is not established across callers.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: open user-directed save, not an experiment. Model proposes structure/merge; web user can edit or cancel before submission. Save endpoint requires nonempty input and a free application lock, not verification success. Optional draft verification annotates without writing and does not veto. Marimo has no second review of generated structure. The service alternative states:

> `draft_conversation`, then `save_reviewed_page` on the
> draft, with no review in between.
> --- `base/services/chat.py`

> draft = draft_wiki_page(db_path, workspace, title, content, category,
>                             client=client, model=model, language=language)
>     return write_wiki_page(db_path, workspace, title, draft.markdown, category,
>                            client=client, model=model, language=language)
> --- `base/domain/chat/wiki_tools.py`

No answer oracle governs admission. Existing page/content and localized structuring instructions guide the proposal. What persists is page content and derived indexes/history, not the model's inaccessible reasoning. Reference synchronization errors and repair errors can be logged without aborting the primary save, limiting all-or-nothing claims (SRC-1, `base/domain/chat/wiki_tools.py`).

#### RT-RTE-wiki-maintenance
Label: Wiki reconciliation and restoration

Endpoints: upload follow-up or explicit scan/regeneration/lint/edit/delete/reindex/history action → service/domain handlers → pages/index/history. Deterministic checks and optional model checks diagnose issues; repair dispatch decides action by issue type, with model-dependent stale/missing-concept fixes conditional on a supplied client. Human starts the maintenance action but does not approve each repair's resulting content (SRC-1, `base/services/ingest.py`, `base/domain/repair/runner.py`, `base/services/wiki.py`).

- Immediate return: Results/progress, issue count, page version, deletion status or revert result depending on requested operation.
- Later read-back: Repaired/edited/restored pages and rebuilt indexes feed later retrieval/ingestion; diagnostic annotations are also page content where handlers write them.
- Delegated visibility: Model-capable repairs receive scoped issue/source material; deterministic dispatch and persistence remain host responsibilities.
- Selection predicate: Issue check type; ingestion touched-page filtering excludes selected repairs, including orphan deletion; manual page ID and expected version; target Git revision for history restoration.
- Invalidation or expiry: Writes invalidate derived verification where integrated; edit/delete/restore can supersede pages; reindex rebuilds derived lookup state. No global expiry promise.
- Activation or effect: Auto-repair changes pages, links or annotations; manual edit preserves frontmatter and checks version only when supplied; restore chooses snapshot or reindex before mutating.
- Evidence limits: Detailed lint-model prompts, every repair algorithm and crash/failure combination were not audited. Source inspection establishes admission machinery, not successful factual correction.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: mixed modes—automatic post-ingest reconciliation, explicit wiki-wide sweep and direct human editing/restoration. Code can skip unknown/advisory issues and refuse prerequisites; humans can withhold jobs or later restore history. `full_repair=False` removes model checks/repairs from reconciliation, not from the preceding ingestion generation:

> repair_client = client if full_repair else None
> --- `base/services/ingest.py`

> elif issue.check in _NEEDS_LLM and llm_client is None:
> --- `base/domain/repair/runner.py`

> _ADVISORY_CHECKS = {"vocab_stale", "vocab_covered", "vocab_ambiguous", "thin_page",
>                     "unpaged_source", "unsupported_sentences", "unverified_pages"}
> --- `base/domain/repair/runner.py`

Thus unsupported-sentence findings do not automatically cause sentence deletion. Contradiction repair's handler describes annotation rather than adjudication:

> """Append an idempotent ⚠️ warning callout to page A flagging the contradiction."""
> --- `base/domain/repair/actions.py`

Manual edit version enforcement is conditional, not a universal compare-and-swap:

> if expected_version is not None and current != expected_version:
> --- `base/services/wiki.py`

History restoration is a new forward commit, not rewriting source history. Its preflight dirty check has an explicit forced alternative; index recovery needs a usable snapshot or reindex prerequisites (SRC-1, `base/domain/rollback/revert.py`). Repairs use source/config/check rules, not a general independent answer oracle. Content criticism and warning retention alone do not establish an iterative theory builder or improved future capacity; this record makes no such attribution.

#### RT-RTE-configure-grants
Label: Configuration and conditional capability admission

Endpoints: settings/vocabulary edit or workspace data change → validated files/config loading → agent construction/retrieval policy. User supplies scalar settings, blacklist/aliases/rejections or datasets; generated aliases are separately admitted during ingestion. Symbolic TOML/config predicates govern scope and registrations, while prompt strings guide interpretation. The standard composition root, not the model, installs finance/data tools (SRC-1, `base/services/settings.py`, `base/services/vocabulary.py`, `base/services/chat.py`, `base/domain/chat/agent.py`, `base/domain/finance_argentina/agent_tool.py`).

- Immediate return: Written keys or vocabulary mutation result; activation returns tools/prompt or `(None, None)` to the factory.
- Later read-back: Config and dataset files shape subsequent config loads, retrieval and constructed agents; generated aliases can therefore change later gate decisions.
- Delegated visibility: Registered tools and prompt addenda reach the answer agent. No model-authorized plugin download or arbitrary code installation is shown in this route.
- Selection predicate: Scalar validation; roster/collision checks for aliases/blacklist; active dataset condition; finance manifest with at least one passing category; arbitrary factory extra tools remain a separate caller capability.
- Invalidation or expiry: Web settings/vocabulary routes reset cached agents; existing agent objects otherwise remain cached. File mutation alone does not prove every interface refreshes grants immediately.
- Activation or effect: Configuration admits scope/control changes and composition-time capabilities; actual tool use or better answers is unobserved.
- Evidence limits: Not a complete parser/security audit; dataset update concurrency and marimo refresh parity remain uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is human configuration plus code validation, not model self-extension. The proposed change persists in configuration/history or data files. Settings errors reject invalid changes; vocabulary checks can reject covered blacklist terms or alias collisions. History can restore versioned configuration; no universal data rollback claim is made. No reference-answer oracle or improvement curriculum governs these edits.

> if report.passing:
>         return [estimar_alternativas, *make_data_tools(source, report.passing)], FINANCE_PROMPT_ADDENDUM
>     return None, None
> --- `base/domain/finance_argentina/agent_tool.py`

> if extra_tools:
>         tools.extend(extra_tools)
> --- `base/domain/chat/agent.py`

The latter is a Python caller affordance; the inspected shipped root grants the manifest-controlled overlay, not unrestricted model-controlled extensions.

#### RT-RTE-model-evaluation
Label: Direct-agent model suitability evaluation

Endpoints: installer/operator → fixed fairy-tale checks → directly constructed agent → graders and exit verdict. Script owns question/candidate ordering; model owns tool selection and answers. It uses a strict-search prompt for the off-topic check and production defaults for citation checks, not the full chat service (SRC-1, `scripts/eval_chat_model.py`, `quickstart.py`).

- Immediate return: Printed check results/verdict and exit status distinguishing failures from no model response.
- Later read-back: uninspected — no inspected automatic retention-to-training or answer-policy update is established by this evaluator.
- Delegated visibility: Model receives fixed questions, selected prompt and database tool dependency.
- Selection predicate: Configured or explicitly listed models; fixed grader tests for refusal/citations/synthesis and tool-call count.
- Invalidation or expiry: inapplicable — this inspected evaluation path does not itself replace a retained knowledge candidate.
- Activation or effect: Measures source-defined suitability and informs operator/installer decisions; does not apply service grounding substitution or automatically update weights.
- Evidence limits: No execution evidence. Graders proxy observable answer features and tool use, not general correctness or causal superiority.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: bounded fixed-question check rather than open production requests. Script authors supply expected reference properties; code graders decide pass/fail. The reference outcome is refusal/citation shape and retrieval calls, not an independent fact oracle. Human chooses deployment response; automatic model successor installation is not established.

> result = agent.run_sync(question, deps=db_path)
> --- `scripts/eval_chat_model.py`

> if requires_retrieval and n_tools == 0:
>             passed = False
> --- `scripts/eval_chat_model.py`

### Claims

#### RT-CLM-readonly-chat
Label: Standard chat read-only tool intent

Claimed operation: the factory describes its chat tools as read-only and assigns saving to an explicit user action (SRC-1, `base/domain/chat/agent.py`). This holds as a description of standard registered grants, not a prohibition over the generic `extra_tools` API or ingestion/save services.

> The agent has no write tool by design: saving a chat response as a wiki page is the
>     user's explicit action via the "Save to wiki" form (read_app.py → save_to_wiki).
> --- `base/domain/chat/agent.py`

- implementation conclusion status: wired
- operation conclusion status: uninspected

These statuses cover the inspected standard grants. Saving still involves software-generated content after a user action, and a web dialog is not present in every path.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-chat-instructions
Label: Prompt and configuration authority over chat

Consumer: generation/condenser agents and deterministic pre-retrieval orchestration. Channel: localized system prompts, optional configured prompt, overlay addenda, user-template context, and symbolic configuration predicates. Force: prompt text requests model behavior; registered-tool lists and branch predicates impose code-level limits; retrieved page prose is evidence supplied for interpretation, not executable Python. Horizon: agent lifetime for built prompt/grants, per-turn for selected context, and later invocations for retained config/page-derived inputs. SRC-1, `base/services/chat.py`, `base/domain/chat/agent.py`, `base/domain/chat/preretrieval.py`, `web/state.py`.

> system_prompt=effective_prompt,
> --- `base/domain/chat/agent.py`

> tools = [read_wiki_page, search_wiki_fts, search_source_chunks] if include_wiki_tools else []
> --- `base/domain/chat/agent.py`

This path establishes delivery and code-controlled affordances, not compliance or beneficial activation. The creation of a later behavior-shaping page/configuration can be traced through the routes above without inferring that fixed model weights imply an unchanging overall system.

## Annotations

none

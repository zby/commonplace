---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "LLM-WIKI-MCP runtime baseline: shipped ask paths, deterministic retrieval, model synthesis and local change admission at the frozen revision."
run-id: AAS-2026-10-15-llm-wiki-mcp-5dff0dd0576a-01
reviewed-boundary: "25efb7631082fa3732723fee08e24d39b43311fa"
---

# LLM-WIKI-MCP runtime report

## Runtime account

### Work and entry paths

The shipped work is maintaining local Markdown knowledge and returning selected knowledge or an answer through an interactive CLI, one-shot CLI, Python API or MCP. The boundary and source identity are fixed by [boundary](boundary.md#boundary-and-evidence). This report uses SRC-1 implementation and separately attributed design evidence, not execution evidence. No target code, tests, examples or provider requests were executed. Operation, model compliance and benefit remain unobserved.

The ordinary invocation traced here is an interactive `/ask <subject question>` in agentic mode. It is not equivalent to the one-shot `llm-wiki ask` command. The former calls the final `release_ask`; the latter calls `engine.ask_ollama`, which delegates to `WikiStore.ask_ollama`. MCP exposes both families, and the Python engine also exposes retrieval without any model call. These materially different paths are recorded in [RT-RTE-agentic-ask](#rt-rte-agentic-ask), [RT-RTE-plain-ask](#rt-rte-plain-ask), [RT-RTE-store-ask](#rt-rte-store-ask) and [RT-RTE-mcp-dispatch](#rt-rte-mcp-dispatch). SRC-1: `pyproject.toml`, `src/llm_wiki_mcp/cli.py`, `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`.

> if cmd == "ask":
>     data = engine.ask_ollama(" ".join(args.question), top_k=args.top_k, model=args.model, host=args.host, temperature=args.temperature, timeout_seconds=args.timeout_seconds, max_context_chars=args.max_context_chars, dry_run=args.dry_run)
>     human_print(data, "ask", args.json); return 0
> --- `src/llm_wiki_mcp/cli.py`

> mode = release_current_ask_mode(str(vault))
> payload = release_ask(str(vault), question_text, mode=mode, max_tool_calls=14, dry_run=False)
> --- `src/llm_wiki_mcp/cli.py`

Repeated function definitions matter here. The final ask definitions near the context-budget implementation supersede earlier loops. The final tool executor explicitly handles history, page reads and search before delegating to a saved predecessor; that predecessor was saved before the sanitising wrapper, not inferred from the first definition with the same name. The final planner calls an undefined `release_plan_tools_base` inside a caught exception; its ordinary fallback is search and capabilities, with history added for short questions. Thus older, richer planner bodies do not establish the currently active ordinary plan. SRC-1: `src/llm_wiki_mcp/context_api.py`.

> try:
>     base=release_plan_tools_base(question,max_tool_calls,intent)
> except Exception:
>     base=["wiki_search_with_notes","wiki_capabilities"]
> --- `src/llm_wiki_mcp/context_api.py`

### Ordinary invocation and ownership

A user starts the CLI shell and supplies a question. The engine resolves a vault, constructs its store/index, and seeds an empty wiki by default. The shell parses the question, reads the configured mode, and calls the unified ask dispatcher. Code, not the model, owns intent resolution, tool selection, search, full-page expansion and the decision whether to invoke synthesis. The model receives an already assembled text prompt and returns text; the inspected provider request contains no native tool definitions or callback loop. There is no model-selected next tool in this final ask path. The endpoint model is [RT-CMP-ollama-model](#rt-cmp-ollama-model).

The final agentic loop constructs runtime-question or ordinary plans. Ordinary plans start with search-with-notes, capabilities and ask history. Search scans Markdown pages and sidecar notes, scores lexical matches with title/note bonuses, and returns ranked centred snippets. Successful search titles lead to fuller page reads. Each read gets a per-source character budget, then code builds a pack containing system guidance, operational self-context, reduced recent question/answer history, current question and selected source/tool evidence. A second history channel serializes sanitized `wiki_ask_history` results as tool evidence; these rows retain stored prompt fields, subject to serialization and source/whole-pack truncation rather than the dedicated history-section budget. Some collected tool results are not included by the pack builder: it handles page reads, search results and a named subset of runtime tools. Therefore a trace entry is not proof that its complete result reached the model. SRC-1: `src/llm_wiki_mcp/context_api.py`; [RT-OBJ-context-pack](#rt-obj-context-pack).

For a subject question, code POSTs the prompt to the configured Ollama-compatible endpoint. A blank first response triggers a second, expanded-evidence synthesis attempt. A still-empty answer is routed to a deterministic evidence fallback. Runtime/identity/history/config/context-window questions instead receive deterministic answers without synthesis. A non-dry ask then attempts to record its question, first prompt, answer, tool names and model/context metadata. A persistence exception becomes metrics error data rather than suppressing the answer. The shell prints the answer; the API returns a structured dictionary containing answer, evidence, trace, model result and prompt. The process returns to its next input, not to an autonomous self-scheduled task. SRC-1: `src/llm_wiki_mcp/cli.py`, `src/llm_wiki_mcp/context_api.py`.

### Forcing cases and qualified guarantees

Four source forcing cases bound the account. They are inspected branches, not executed tests.

1. **Runtime question or dry run.** A basic operational question bypasses the model; a dry run returns before synthesis and ask-turn persistence, but after evidence collection and config access. These cases challenge any claim that every ask invokes the model or that dry run entails zero filesystem effects. Engine construction may already create directories, database and seed pages; config loading may write default config. [RT-RTE-agentic-ask](#rt-rte-agentic-ask).
2. **Blank or failed synthesis.** Agentic ask has a second model call and a deterministic fallback, but retains the first model result's `ok` for its top-level status. An answer can coexist with `ok: false`. The stored `prompt` and exposed `llm_prompt` remain the first prompt, even when a second prompt produced the answer. The separate second-pass builder does not call the final context-pack budgeter. [RT-RTE-agentic-ask](#rt-rte-agentic-ask), [RT-CLM-context-budget](#rt-clm-context-budget).
3. **Alternate ask routes.** Plain mode and store ask build different prompts and do not use the agentic context pack or its history-selection policy. Store ask's model/host overrides and temperature option are real alternate request controls. The release adapter accepts a temperature argument but does not place it in its request payload. [RT-RTE-plain-ask](#rt-rte-plain-ask), [RT-RTE-store-ask](#rt-rte-store-ask).
4. **Direct mutation.** The agentic system prompt's nonmutation instruction does not constrain the entire product. MCP registered handlers and direct store methods can create/update/delete pages, ingest files, set config and apply repairs; the CLI can invoke `$EDITOR` through `os.system`. The caller selects these paths; no per-content human approval is inserted by the inspected dispatch. [RT-RTE-mcp-dispatch](#rt-rte-mcp-dispatch), [RT-RTE-knowledge-write](#rt-rte-knowledge-write), [RT-RTE-runtime-config](#rt-rte-runtime-config).

The nonmutation rule's owner is the shipped prompt plus the code-selected evidence executor. Its strength is **policy** for the model instruction, with code-restricted action dispatch on the inspected ask path, not a deployment guarantee or a whole-system write ban. Its subject is wiki mutation during ask, not automatic ask-history/config/metrics writes. Actual model compliance and host-side restrictions require external contracts not supplied here. The capability surface includes the write handlers and editor command; the current grant set of any deployed MCP host is uninspected. The isolation envelope is the actual process's OS permissions and configured endpoint, also uninspected. A default localhost address is not proof of network isolation. SRC-1: `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`, `src/llm_wiki_mcp/cli.py`.

The context budget's owner is the pack-building code. It is **best effort**, based on a character-derived token estimate, not a guarantee of model-native capacity or output correctness. It covers the first agentic pack, not the independently constructed second-pass prompt, plain ask or store ask. The tool-call setting is likewise not a strict total-work bound: the loop permits `max_tool_calls + 4`, and subsequent full-page expansion and second-pass retrieval add work outside it. No supplied run establishes latency or answer quality. [RT-CLM-context-budget](#rt-clm-context-budget).

### Change admission and evidence coverage

Knowledge enters through caller-supplied page bodies, provenance-aware file extraction, deterministic sidecar-note generation, lint repair and automatic ask-turn retention. Caller-triggered ingestion is not per-content human approval: code detects new/changed sources, proposes a plan, and writes when apply is enabled. Sidecar generation is a term/link template despite its AI-notes label. Code/content review, confidence and correctness must not be inferred from those labels. Detailed retained-memory revisions are left to the memory analyst. [RT-RTE-knowledge-write](#rt-rte-knowledge-write).

Runtime settings admit changes to future model selection, host, mode and budgets; documentation consolidation can overwrite generated documentation and archive consumed source files. These are distinct admission mechanisms, not model self-modification. Source/build changes remain ordinary external development at this boundary; this report establishes no autonomous code deployment mechanism. [RT-RTE-runtime-config](#rt-rte-runtime-config), [RT-RTE-docs-consolidate](#rt-rte-docs-consolidate).

Added inspection within SRC-1 includes the final contextual `WikiStore.search` monkey-patch, the complete one-shot CLI dispatcher, both Ollama adapters, the saved tool-executor predecessor and active planner fallback, lint-repair admission, direct page writes, the second-pass prompt builder and documentation consolidation. These passages supply implementation evidence. `pyproject.toml` supplies the packaged entry contract and optional SDK/extractor dependencies. No new source or execution layer is introduced. Provider internals, host grants, concurrency behavior across multiple writers, all possible malformed inputs and complete maintenance correctness remain unobserved or uninspected; none is asserted absent.

## Shared records

### Components

#### RT-CMP-ollama-model
Label: Configured Ollama model

The source-native model is the configured `ollama.model`, defaulting to `llama3.2:3b`, resolved by an Ollama-compatible HTTP host. Its operative form is distributed-parametric; weights and provider state reside outside the frozen checkout. The local implementation stores only config and request/response data. SRC-1: `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`.

Parameters changing during operation: uninspected at the provider; inspected local adapters issue generation requests, not parameter updates. Exact version pinned: no, the default is a model tag without a weight digest. Mutable endpoint resolving to another model: afforded by editable host/model config and store-ask per-call overrides; actual resolution is unobserved. Both adapter families use this component role, not demonstrably identical deployed weights.

> host = host or ollama.get("host", "http://localhost:11434")
> model = model or ollama.get("model", "llama3.2:3b")
> payload = {"model": model, "prompt": prompt, "stream": False}
> --- `src/llm_wiki_mcp/context_api.py`

### Operative objects

#### RT-OBJ-context-pack
Label: Agent context pack

Source-native identity: dictionary returned by `release_build_agent_context_pack`. The dictionary/settings/metadata are symbolic structures in process memory; its `prompt` is natural-language Markdown plus JSON rendered for model interpretation. The operative prompt is not itself weights or an executable tool grant. Its dedicated recent-history section contains selected questions/answers, not stored prompts. Separately, its tool-evidence section can contain serialized `wiki_ask_history` rows, including stored prompt fields preserved by the sanitizer. Past prompt text can therefore enter the prompt through this second channel, subject to sanitization and truncation; the prompt as a whole does not exclude it. Other contents are selected page text, reduced search fields, operational guidance and limited tool evidence. The first prompt can subsequently be stored as part of ask history. SRC-1: `src/llm_wiki_mcp/context_api.py`.

> history_md = release_recent_history_markdown(vault_path, limit=8, answer_chars=900)
> history_md = release_trim_to_token_budget(history_md, settings["history_budget_tokens"])
> --- `src/llm_wiki_mcp/context_api.py`

> elif tool in {"wiki_capabilities", "wiki_tool_catalog", "wiki_command_tool_map", "wiki_ask_history"}:
>     # Keep runtime/tool evidence, but compact it.
>     source_sections.append(f"## Tool Evidence: {tool}\n\n```json\n" + _release_json.dumps(result, indent=2, ensure_ascii=False)[:6000] + "\n```")
> --- `src/llm_wiki_mcp/context_api.py`

The final executor loads full history rows and applies `release_sanitize_public_obj`. That sanitizer redacts designated path fields and sanitizes strings recursively, but does not remove `prompt` keys. The tool-evidence JSON is cut to 6000 characters, then shares the remaining source budget and final whole-pack trim. Neither full-row delivery nor complete delivery of any stored prompt is guaranteed. `history_tokens_estimate` measures only the reduced recent-history section, not all historical material in the prompt. SRC-1: `src/llm_wiki_mcp/context_api.py`.

> "history": release_sanitize_public_obj(rows),
> "count": len(rows),
> "note": "Each row may include question, prompt/context, answer, sources/tools and estimated token counts.",
> --- `src/llm_wiki_mcp/context_api.py:4134-4136`

> prompt = release_trim_to_token_budget(prompt, settings["context_budget_tokens"], suffix="\n\n[context pack truncated to configured context_budget_tokens]")
> --- `src/llm_wiki_mcp/context_api.py`

### Routes

#### RT-RTE-agentic-ask
Label: Agentic ask execution

Endpoints and progression: interactive ask or MCP/Python `release_ask` → final `release_agentic_ask` → deterministic intent/plan → read-only evidence executor → context pack → model generation or basic-answer router → optional second synthesis/fallback → history/metrics attempt → answer dictionary. Code owns next steps; no runtime-model tool-choice role is wired in this final path. The principal is the user or host caller; no separate internal agent identity or approval principal is selected. Context and process state are the question, resolved intent, focus page, trace and evidence; effects cross local vault I/O and the configured HTTP endpoint. Coordination is a sequential local function, not delegated agents. SRC-1: `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/cli.py`, `src/llm_wiki_mcp/server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Answer dictionary with trace, evidence, context pack and first prompt; dry run returns `answer: None` and evidence without generation.
- Later read-back: Unless disabled or failed, recorded turns can enter later packs through reduced recent questions/answers and through sanitized full-row `wiki_ask_history` tool results, including stored prompt fields subject to truncation. Persistence/compaction details belong to the memory analysis.
- Delegated visibility: Configured endpoint receives the assembled prompt; no delegated worker context is created. MCP callers receive the returned dictionary through dispatch.
- Selection predicate: Code recognizes basic operational questions; other questions use lexical page/note ranking, configured source limits and fuller reads of selected titles. Only recognized evidence types enter the pack.
- Invalidation or expiry: Each invocation rebuilds evidence and trims recent history and source text using active budgets; retained files persist separately. No model-context invalidation contract is supplied.
- Activation or effect: Wiring requests answer synthesis and attempts automatic turn/metrics writes; a basic question instead selects deterministic text. Behavioral dependence of a deployed model on a particular passage is unobserved.
- Evidence limits: No observed ask or provider result. A nonempty fallback does not establish model success, source correctness or a truthful answer.

Decision roles and operating mode: open user requests, not a bounded experiment/curriculum. Code decides basic mode, source expansion and blank-answer recovery; the model proposes answer text only. No expected-answer oracle is supplied to this route. Its blank-string test is an output-availability check, not a correctness oracle.

Admission: the automatic recorder proposes a record from the current question, first prompt, final answer and metadata. `history_enabled` can suppress append; compression is separately configurable. No human per-turn approval is required. Recovery catches persistence failures into metrics error data; no atomic rollback of all ask artifacts is established. Guidance applied to answering is the shipped system prompt plus answer-first instruction and retrieved material; retained results are turns/metrics, not a rewritten method. This describes ordinary answer production, not a claimed theory-criticism loop.

> context_pack = release_build_agent_context_pack(vault_path, original, intent, trace, evidence)
> prompt = context_pack["prompt"]
>
> if dry_run or not synthesize:
>     return {
> --- `src/llm_wiki_mcp/context_api.py`

> if not answer and "release_try_second_pass_synthesis" in globals():
>     second = release_try_second_pass_synthesis(vault_path, original, trace, evidence)
>     answer = second.get("answer") or ""
>     llm = {**llm, "second_pass": second.get("llm")}
>     evidence = evidence + release_sanitize_public_obj(second.get("extra_evidence", []))
> --- `src/llm_wiki_mcp/context_api.py:4438-4442`

Working-context control: the dedicated recent-history renderer takes the latest eight turns, cuts each historical answer to 900 characters, then trims that section to its history budget. This is not a bound on all historical exposure: the separate `wiki_ask_history` tool channel returns sanitized full rows, including stored prompts, and serializes its result up to 6000 characters into source evidence. That channel shares the remaining source budget and final whole-pack trim, not the dedicated history budget. `history_tokens_estimate` counts only the rendered recent-history section. Per-source page reads are character-capped; a whole-pack trim preferentially loses the tail, where retrieved wiki/tool evidence, including this second history channel, is placed. External pages remain available for later retrieval even if omitted now. This is selected material copied by value, not a sub-agent frame or a model-followable pointer. There is no special context isolation frame in this route.

#### RT-RTE-plain-ask
Label: Release plain ask

Endpoints: unified ask with mode `plain`, or direct release plain API → page/note search → up to five page reads → a distinct JSON evidence prompt → release Ollama adapter → result. Unified dispatch additionally sanitises the answer and attempts recording, whereas the direct plain helper does not record. Code owns all selection. SRC-1: `src/llm_wiki_mcp/context_api.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Search, prompt, answer and LLM result; dry run returns the built prompt without generation.
- Later read-back: Unified plain dispatch records a turn for later readers; direct plain helper alone does not. This prompt itself does not select retained conversation history.
- Delegated visibility: Endpoint sees the plain prompt, not the agentic context pack.
- Selection predicate: Top-k page/note search; each selected page contributes at most its first 4000 characters and evidence JSON is cut at 16000 characters.
- Invalidation or expiry: Prompt rebuilt each call; direct page text can change between calls. No model-side expiry is inspectable.
- Activation or effect: Requests model text and, through unified dispatch, records an answer; success unobserved.
- Evidence limits: Failure produces a nonempty failure message, so unified dispatch's empty-answer fallback need not run. Agentic history and context-budget assurances cannot be transferred here.

Operating mode is open requests; model writes text, code decides dispatch and failure handling; there is no answer oracle. Automatic recording has the same recorder admission mechanism described in [RT-RTE-agentic-ask](#rt-rte-agentic-ask), but only when invoked through unified dispatch.

> prompt += _release_json.dumps(evidence, indent=2, ensure_ascii=False)[:16000]
> prompt += "\n\nAnswer using only the evidence above. If evidence is weak, say so."
> --- `src/llm_wiki_mcp/context_api.py`

#### RT-RTE-store-ask
Label: Store retrieval and ask

Endpoints: one-shot CLI `ask`, Python engine `ask_ollama`, or MCP `wiki_ask_ollama` → store `retrieve_articles` → store prompt → server Ollama adapter. Retrieval/context-only callers may stop before generation. `WikiStore.search` is replaced at context API import by the final contextual implementation: FTS candidates, then fallback token/title matching over at most 1000 indexed rows, with cached results and centred snippets. Retrieved article bodies are subsequently read from Markdown, not taken directly from the snippets. SRC-1: `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`, `src/llm_wiki_mcp/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Retrieval-only gives article bodies/context/metadata; ask gives retrieval, prompt, model/host and model answer or error; dry run stops before HTTP.
- Later read-back: Reads retained wiki and index; inspected store ask does not itself append release ask history. Retention by an external caller is uninspected.
- Delegated visibility: Provider sees the store prompt and retrieved context; a retrieval-only consumer receives the returned articles without invoking a provider here.
- Selection predicate: Configurable top-k, per-article and total character budgets; query/limit/vault-keyed search cache precedes database search.
- Invalidation or expiry: Markdown/index change through write/reindex routes; cached results have a TTL. Immediate invalidation for every writer is not established here.
- Activation or effect: Code invokes generation using model/host/temperature/timeout overrides, or just returns selected context. Correct use by later consumers is unobserved.
- Evidence limits: No observed request, deployment settings or cache-freshness guarantee; this is not the unified agentic ask path.

Operating mode is open requests. Code selects articles; model supplies an answer; no reference-answer oracle or candidate comparison is wired. Budget controls govern retrieved bodies, not a proven model-native token limit. There is no new knowledge admission in the ask body.

> llm = call_ollama_generate(llm_prompt, host=host, model=model, temperature=temperature, timeout_seconds=timeout_seconds)
> result.update({'ok': bool(llm.get('ok')), 'answer': llm.get('response',''), 'ollama': llm})
> --- `src/llm_wiki_mcp/server.py`

#### RT-RTE-mcp-dispatch
Label: MCP tool dispatch

Endpoints: external MCP host → official SDK stdio server → namespace-stripped tool name → registered Python handler → structured and text result. Handler table includes retrieval, generation, config and mutation paths. SDK supplies protocol transport; code calls the handler synchronously inside an async callback. Host scheduling and permission decisions remain external. SRC-1: `src/llm_wiki_mcp/server.py`, `pyproject.toml`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `CallToolResult` with text JSON, structured content and error flag; unknown names raise, handler exceptions become error results.
- Later read-back: Dispatch has no independent retained-content selection; selected handlers can write/read knowledge, history and configuration.
- Delegated visibility: Host receives tool output; the tool does not define what the host reveals to a model or another principal.
- Selection predicate: Name membership in `TOOL_HANDLERS`, then handler-specific arguments; this is not a per-user grant check.
- Invalidation or expiry: Registry assembled by shipped import-time code; no per-call grant expiry is shown in this callback.
- Activation or effect: Invokes the named handler with process permissions, including mutation when that handler supports it.
- Evidence limits: Actual SDK installation, host grants, isolation and concurrent use unobserved; registry membership alone establishes no deployed authorization.

> if internal_name not in TOOL_HANDLERS:
>     raise ValueError(f'Unknown tool: {name}')
> try:
>     structured=TOOL_HANDLERS[internal_name](arguments or {})
> --- `src/llm_wiki_mcp/server.py`

#### RT-RTE-knowledge-write
Label: Local knowledge admission

Endpoints: caller body/file/maintenance command → page creation/update, provenance ingestion, sidecar-note iteration or lint repair → local files/index/provenance → later retrieval. These are related local-knowledge writes with distinct admission predicates below, not one universally gated editor. SRC-1: `src/llm_wiki_mcp/server.py`, `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Page metadata/hash, ingest plan/processed/errors, note terms/link candidates, or repair before/after/actions.
- Later read-back: Page text feeds store and page/note search; notes feed page/note search and combined context; changed index feeds store retrieval.
- Delegated visibility: MCP callers can request these writes and see their results; external host review is uninspected. CLI editor executes a configured external editor with process privileges.
- Selection predicate: Caller chooses page/body or input path; ingestion compares provenance for new/changed files; note generator extracts terms and candidate links; lint repair selects broken links, orphan pages and short pages.
- Invalidation or expiry: Replace/append/prepend edits and re-ingestion change pages; reindex rebuilds derived search tables; rerunning notes rewrites sidecars. No universal automatic semantic invalidation is established.
- Activation or effect: Code writes supplied/extracted/template text, indexes pages or reindexes after successful ingestion; subsequent use is wired but not observed.
- Evidence limits: Structural admission is not source truth, semantic review, or demonstrated improvement. A write followed by index failure can leave partial state.

Admission roles: direct create rejects an existing path unless overwrite is set; update selects a supported mode, not an epistemic approval. Provenance ingestion proposes new/updated lists, then writes when `apply` is true (MCP applies unless dry-run is requested); per-file errors are collected and do not roll back previous files. Caller can veto application by choosing dry run. Source extraction guidance supplies wrapper/provenance text, not a model-authored synthesis. Sidecar iteration deterministically rewrites terms and link suggestions from page/old-note content; there is no separate human acceptance before its file write. Repair is dry-run by default; apply permits code-selected structural edits, and missing-page creation needs its own flag. Its before/after lint reports are structural checks, not expected-answer oracles. Open caller requests trigger these routes, not a controlled improvement experiment. Authors can be human or computational callers; the generic API does not resolve that identity. Recovery includes reindex and rerunning ingestion/notes; no general prior-version restoration is established.

> if path.exists() and not overwrite:
>     raise FileExistsError(f'Page already exists: {title}')
> --- `src/llm_wiki_mcp/server.py`

> wiki_path.write_text(content, encoding="utf-8")
> release_record_ingest_result(vault_path, p, wiki_title=title, wiki_path=str(wiki_path), action="updated_or_new")
> --- `src/llm_wiki_mcp/context_api.py`

> path = release_note_path(vault_path, title); path.write_text(note, encoding="utf-8")
> return {"ok":True,"title":source_path.stem,"note_path":str(path),"candidate_links":links,"terms":terms}
> --- `src/llm_wiki_mcp/context_api.py`

> if apply and actions:
>     self.reindex()
>     after = self.lint()
> --- `src/llm_wiki_mcp/server.py`

#### RT-RTE-runtime-config
Label: Runtime configuration admission

Endpoints: config command or MCP config handler → dotted-key setter/save → vault JSON config → later loaders selecting model, host, history settings, ask mode and context budgets. Symbolic values are stored as JSON on disk, not model parameters. SRC-1: `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`, `src/llm_wiki_mcp/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Updated configuration or configuration path; editor path delegates to a caller-configured command.
- Later read-back: Subsequent generation, mode dispatch, context construction and recording load active values.
- Delegated visibility: Calling MCP host can inspect/set values where handlers expose them; provider gets the resulting request, not necessarily the configuration file.
- Selection predicate: Caller chooses key/value; loader merges defaults, setter parses booleans/numbers, context settings enforce local minima/defaults.
- Invalidation or expiry: Later edits/reset replace effective settings; config has no inherent expiry.
- Activation or effect: Changes future code decisions and request destination/model; no parameter update follows merely from changing the model tag.
- Evidence limits: No deployment configuration supplied. Successful save is not provider availability, safe host selection or model compatibility.

Admission: caller proposes values and can veto by not setting them; generic setters persist without a separate human approval or trial oracle. Malformed file content falls back to defaults at read time. The release writer uses temporary-file replacement, reducing partial-file exposure, but does not preserve an automatic previous-version backup. Operator edit/reset can replace settings. Guidance is shipped defaults and explicit setter rules, retained as JSON. This is open configuration, not a measured successor-selection experiment.

> tmp.write_text(_release_json.dumps(config, indent=2, sort_keys=True), encoding="utf-8")
> tmp.replace(path)
> --- `src/llm_wiki_mcp/context_api.py`

#### RT-RTE-docs-consolidate
Label: Documentation consolidation admission

Endpoints: explicit CLI/MCP consolidation request → fixed category/file mapping → overwritten category documents, generated index and optional archive moves. Source-native guidance is the static mapping and keep-list, not a model critique. Material is natural-language Markdown consumed by later people/agents, manipulated by symbolic file rules. SRC-1: `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Written paths and archive count.
- Later read-back: Generated documentation/index can guide later operators or agents; no supplied run shows subsequent consumption.
- Delegated visibility: Invoking caller receives result; no worker is launched.
- Selection predicate: Fixed input basenames and output categories under caller-selected project root; only present mapped inputs are concatenated, archive moves only consumed non-kept files.
- Invalidation or expiry: Rerun overwrites outputs; no timestamp/version validation gate.
- Activation or effect: Writes and moves documentation; does not itself replace running Python code or model weights.
- Evidence limits: Correctness/preservation of meaning and eventual operational use are unobserved. Missing inputs can still yield overwritten category outputs.

Admission: caller triggers consolidation and chooses archive flag; code decides writes and moves without per-document approval. There is no separate rejection phase after proposal, correctness oracle or automatic rollback. Archive preserves some consumed inputs when enabled but is not a full backup of overwritten outputs; an existing archive destination is deleted before move. This is an open maintenance command, not source-evidenced self-improvement.

> target=docs/outname
> target.write_text("\n".join(parts),encoding="utf-8")
> written.append(str(target))
> --- `src/llm_wiki_mcp/context_api.py`

### Claims

#### RT-CLM-context-budget
Label: Configurable context budget

The source claims a configurable ask context pack and an inspectable dry/debug prompt. The pack builder enforces estimated-text budgets, but does not establish the provider's exact token window or completeness of evidence. Owner: final pack-building code. Enforcement: dedicated recent-history-section truncation, tool-evidence serialization caps, remaining-source trimming, page-read character cap and final `release_trim_to_token_budget`. The dedicated history budget and `history_tokens_estimate` cover only the reduced recent-history section, not serialized history-tool rows containing stored prompts. Guarantee strength: best effort. Covered path: first agentic pack. Alternate paths: plain/store prompts and independent second-pass builder. External contract required: provider-native tokenization/context behavior and compliant answer generation, neither supplied. SRC-1: `src/llm_wiki_mcp/context_api.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> The result is used by `/ask`, `/ask-agentic-dry`, and `/debug-context` so the
> user can inspect exactly what the model is likely to see.
> --- `src/llm_wiki_mcp/context_api.py`

The qualifier “likely” is material: second-pass synthesis can use another prompt, and dry-run evidence gathering can access a different vault state from a later actual ask. The debug output is first-pass source visibility, not a trace of provider execution.

#### RT-CLM-ask-nonmutation
Label: Agentic ask nonmutation rule

The prompt asks the model not to mutate the wiki during ask. The inspected final ask owns a fixed evidence-execution path and receives model text, not model-selected arbitrary actions. This bounds local ask execution, not all caller capabilities. Automatic persistence remains wired, and direct mutation handlers/editor paths remain available elsewhere. Owner: shipped prompt/code. Enforcement: prompt rule plus code-selected dispatch, not a universal permission layer. Guarantee strength: policy for the natural-language rule. Required external contract: host permissions and OS isolation for claims extending beyond that path. SRC-1: `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`, `src/llm_wiki_mcp/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> 6. Never mutate the wiki during agentic ask unless the user explicitly uses an apply/edit command.
> --- `src/llm_wiki_mcp/context_api.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-answer-guidance
Label: Answer prompt guidance

Consumer: configured Ollama model. Channel: POSTed `prompt` containing shipped system rules, operational self-context, selected recent turns and selected wiki/tool evidence. Force: natural-language instruction and evidential framing, not a hard execution permission; model compliance unobserved. Horizon: current generation, with later influence possible through recorded answers reselected into history. Selection and trimming intervene before delivery, so retained text is not automatically delivered in full. SRC-1: `src/llm_wiki_mcp/context_api.py`; [RT-OBJ-context-pack](#rt-obj-context-pack), [RT-RTE-agentic-ask](#rt-rte-agentic-ask).

> Answer the user directly first. Use the operational self-context, ask/reply history, and wiki sources below. If evidence is incomplete, say what is uncertain and still give the best supported answer. Do not output only references or raw extracts.
> --- `src/llm_wiki_mcp/context_api.py`

#### RT-BAP-config-control
Label: Configuration control of requests

Consumer: local loaders/dispatchers/request adapters. Channel: vault JSON configuration read into symbolic fields. Force: executable selection of endpoint, model tag, ask mode and numeric budgets, subject to parsing/default/minimum rules rather than model interpretation. Horizon: later invocations until superseded by edits/reset or per-call overrides. Actual request execution and behavioral effect unobserved. SRC-1: `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`; [RT-RTE-runtime-config](#rt-rte-runtime-config), [RT-CMP-ollama-model](#rt-cmp-ollama-model).

> """Unified ask entry point with configurable context budgets."""
> mode = (mode or release_current_ask_mode(vault_path) or "agentic").lower()
> --- `src/llm_wiki_mcp/context_api.py`

## Annotations

none

---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Zikkaron runtime baseline: MCP memory operations, direct SQLite host hooks, compaction replay, instruction installation and evaluation at the frozen source revision."
run-id: AAS-2026-10-15-zikkaron-0102ec63c6e5-01
reviewed-boundary: dda34a5d903d04ecb5517af214d437873c833302
---

# Zikkaron runtime report

## Runtime account

Zikkaron supplies memory and selected context to an external conversational host. It does not own the host's ordinary next-action generation loop. Its own consequential decisions are admission, transformation, ranking, protection and restoration of retained content. Claude Code owns whether to invoke tools and whether delivered text changes task behavior. The shipped benchmark drivers do contain answer-generation and judging calls; they are a separate bounded evaluation mode, not the ordinary MCP service's controller. Evidence is static implementation and source-native doctrine from SRC-1 at the boundary pin. No target execution, provider response, successful hook delivery, activation or benefit was supplied or generated.

### Ordinary shipped invocation

The installed `zikkaron` command dispatches through `zikkaron.__main__:cli`; without a subcommand it runs the service, defaulting to stdio, with SSE and streamable HTTP alternatives. `main` initializes the shared storage, starts consolidation and a cwd file watcher, attempts global instruction synchronization and project hook installation, then gives transport ownership to FastMCP. SIGINT/SIGTERM and the transport's `finally` call shutdown: stop maintenance, flush the sensory buffer and close storage. Configuration comes from Pydantic settings with the `ZIKKARON_` prefix; default storage is `~/.zikkaron/memory.db`. These are executable entry paths, not evidence of deployment (SRC-1, `pyproject.toml`, `zikkaron/__main__.py`, `zikkaron/config.py`, `zikkaron/server.py`).

> try:
>     mcp_server.run(transport=transport)
> finally:
>     shutdown()
> --- `zikkaron/server.py`

One ordinary use is host-selected `remember(content, context, tags)`, followed on a later task or session by `recall(query)`. The host supplies the proposed natural-language content and directory identity; code, not a generation model, owns the subsequent admission decision. The predictive gate can return `stored: False` before insertion. Admitted content is embedded, scored, curated or directly inserted, stamped with CRDT provenance when available, and augmented with protection/link/checkpoint metadata. The response is the resulting memory dictionary without binary vectors, sometimes with related context. Later recall delegates candidate selection to HippoRetriever, applies ranking and context packing, returns selected dictionaries and also changes access heat, timestamps, transition counts and reconsolidation state. Those retained effects can affect subsequent selection. See [RT-RTE-remember-recall](#rt-rte-remember-recall), [RT-RTE-context-selection](#rt-rte-context-selection) and the component records below. Detailed revision semantics belong to the memory analysis.

Persistence is local SQLite with WAL, FTS and sqlite-vec; dense embeddings are BLOBs, while IDs, tags, scores, graph edges and timestamps have fixed code consumers. Text becomes a behavioral input only after tool return or hook delivery. Directory strings and the default CRDT agent identity are labels, not verified principals. The service's previous-recall tracker uses a literal `default` session key, so this inspected path does not separate recall-transition learning by actual MCP session (SRC-1, `zikkaron/storage.py`, `zikkaron/server.py`).

> session_key = "default"
> top_id = merged[0]["id"]
> prev_id = _last_recalled_ids.get(session_key)
> --- `zikkaron/server.py`

### Material alternate loops and four forcing cases

1. **A stored memory need not have passed the explicit write gate.** The PostToolUse script and HTTP auto-capture endpoint insert an action log directly; consolidation groups it into retained summary memories. `anchor` directly inserts protected memories; project seeding deletes old seed entries then inserts replacements. Benchmark ingestion calls storage directly with settings and embedding engines, enabling enrichment not necessarily enabled by ordinary insert callers. Thus “only surprising information is stored” is too strong system-wide, and even the gate has keyword/tag bypasses and a continuity discount. [RT-RTE-trace-consolidation](#rt-rte-trace-consolidation), [RT-RTE-seed-admission](#rt-rte-seed-admission), [RT-RTE-replay-context](#rt-rte-replay-context), [RT-CLM-write-gate](#rt-clm-write-gate). SRC-1, `zikkaron/server.py`, `zikkaron/predictive_coding.py`, `zikkaron/consolidation.py`, `zikkaron/restoration.py`, `zikkaron/seed.py`, `benchmarks/test_e_locomo.py`.
2. **A “hard” retrieval rule does not mediate every memory-to-host path.** HippoRetriever applies rules late in recall, but prompt-recall and session-start scripts issue their own SQL and restore queries storage directly. The prompt hook supplements local FTS matches with other directories; restoration anchors, recent memories and the active checkpoint are not all directory-filtered. Neither rule enforcement nor project-local context is a universal authorization barrier. [RT-RTE-rule-admission](#rt-rte-rule-admission), [RT-RTE-hook-context](#rt-rte-hook-context), [RT-RTE-replay-context](#rt-rte-replay-context). SRC-1, `zikkaron/retrieval.py`, `zikkaron/rules_engine.py`, `zikkaron/hooks/prompt-recall.py`, `zikkaron/hooks/session-start-context.py`, `zikkaron/restoration.py`.
3. **PreCompact drain does not copy the host's whole current conversation.** The shell hook extracts cwd, invokes a CLI and discards its output. The drain implementation increments an epoch and updates a checkpoint or creates a placeholder. Restore reconstructs from already retained material; it cannot thereby promise verbatim recovery of unrecorded turns. Each new checkpoint deactivates all prior active checkpoints, and lookup has no directory/session argument. Its global selection can return another project's checkpoint. [RT-RTE-replay-context](#rt-rte-replay-context), [RT-CLM-context-replay](#rt-clm-context-replay). SRC-1, `zikkaron/hooks/pre-compact-drain.sh`, `zikkaron/__main__.py`, `zikkaron/restoration.py`, `zikkaron/storage.py`.
4. **Prompt-recall's latency budget is not a preemptive deadline.** The code checks elapsed time before entering vector search and after synchronous model loading. A slow import/load can already exceed the stated budget before that check returns an empty vector list. FTS remains a fallback, not proof of a <100 ms or 0.5 s end-to-end bound. Its 3000-character budget counts content rather than the complete formatted output. [RT-RTE-hook-context](#rt-rte-hook-context), [RT-CLM-hook-budget](#rt-clm-hook-budget). SRC-1, `zikkaron/hooks/prompt-recall.py`.

These are static counterpaths, not reproduced failures. They challenge universal readings while preserving the implemented narrower capacities.

### Ownership, grants and effect boundaries

The capability surface includes memory insertion/deletion, rule and trigger creation, file-scanning seeding, instruction-file writes, executable hook installation, checkpointing, and direct database maintenance. `sync_instructions` accepts a path; `install_hooks` accepts a directory. In the inspected service wrappers there is no per-content human approval step before these mutations. The current host grant set—what tools a user has enabled, its approval policy and actual filesystem permissions—is uninspected. It is not inferred from registration decorators. The deployed isolation envelope is likewise unobserved. FastMCP is configured on `127.0.0.1`, but this is an interface default, not a verified deployment guarantee or a sandbox around model loading, copied hooks or file writes (SRC-1, `zikkaron/server.py`).

> mcp_server = FastMCP(
>     name="zikkaron",
>     instructions="Biologically-inspired persistent memory engine for Claude Code.",
>     host="127.0.0.1",
>     port=settings.PORT,
> )
> --- `zikkaron/server.py`

The external contract is substantial: Claude Code must load the synchronized instructions, execute the configured events, provide JSON inputs and inject stdout; the CLI must be on the hook process's PATH; all relevant processes must address the same DB. In fact post-tool capture and session-start use a hard-coded default DB while prompt-recall reads `ZIKKARON_DB_PATH` and server/CLI honor configuration. A nondefault DB can split these loops. Startup hook/instruction failures are nonfatal; the hooks also often suppress errors. This favors continuation, not guaranteed recording or restoration. SRC-1, `zikkaron/server.py`, `zikkaron/hooks/post-tool-capture.py`, `zikkaron/hooks/session-start-context.py`, `zikkaron/hooks/prompt-recall.py`, `zikkaron/hooks/post-compact-rehydrate.sh`.

> db_path = Path("~/.zikkaron/memory.db").expanduser()
> if not db_path.exists():
>     return
> --- `zikkaron/hooks/post-tool-capture.py`

> except Exception:
>     # Never fail the hook — swallow all errors
>     pass
> --- `zikkaron/hooks/post-tool-capture.py`

The maintenance daemon shares storage with the service, and independent hooks/CLI processes open the same file. SQLite WAL is wired; whole `remember` and consolidation operations include multiple commits, so this evidence does not establish transactional all-or-nothing updates across all metadata. Nor does it establish multi-agent isolation or exactly-once action summarization. No remote worker delegation or production shell executor is attributed to the MCP service. Actual shell processes occur in its installed hook contract and the LongMemEval driver; model-supplied remote code is also permitted by the embedding loader. Those alternate executors are not covered merely because MCP tools are local. See [RT-CMP-embedding-engine](#rt-cmp-embedding-engine) and [RT-RTE-evaluation-mode](#rt-rte-evaluation-mode).

### Controls, admission and remaining inspection limits

Runtime-client controls include `max_results`, `min_heat`, configured ranker flags, explicit remember/forget/anchor/checkpoint, usefulness ratings, rules, dry-run seeding and force consolidation. These determine what is persisted or delivered, not what the host must believe. Context control is by retrieval/packing, bounded hook output and restoration from checkpoints; actual removal of accumulated host context is owned by Claude Code. There is no target-owned sub-agent frame evidenced in these traced loops. The host compaction horizon resembles replacement of a working window with selected retained material, not preservation of a frame by reference: the window receives text by value, and unrecorded discarded content is not recoverable through a pointer.

[RT-RTE-install-integration](#rt-rte-install-integration) admits shipped instructions and executable event configuration; [RT-RTE-rule-admission](#rt-rte-rule-admission) admits fixed-consumer symbolic policy; [RT-RTE-seed-admission](#rt-rte-seed-admission) and [RT-RTE-trace-consolidation](#rt-rte-trace-consolidation) admit knowledge without per-item human review. Package release uses a published GitHub release, a test job and PyPI trusted publishing; it is a maintainer/CI path rather than a service-owned autonomous product updater (SRC-1, `.github/workflows/publish.yml`, `pyproject.toml`). Tests are configured gates, not observed passing runs. No product self-improvement or capacity gain is inferred from that release mechanism or from the name `memify`.

Added inspection under SRC-1 extends the boundary's initial coverage to the gate's bypass/continuity policy; late retrieval, reranker and context-packing branches; action-log grouping; global checkpoint selection; seed replacement; rule parser/admission/consumer; embedding, enrichment, Hopfield, HDC and successor-representation components; evaluator generation/judging and subprocess calls; and the publish gate. These supply implementation evidence, with comments/docstrings supplying doctrine where separately identified. Unresolved internals include the complete curation/reconsolidation/CRDT merge algorithms, all domain/sleep transformations, detailed graph and enrichment correctness, optional dependency implementations and host processing. Their wiring is visible, but this report makes no comprehensive verification or absence claim about them. Benchmark scores, actual grants, isolation, recovery under concurrent failures and causal benefit remain unobserved.

## Shared records

### Components

#### RT-CMP-embedding-engine
Label: EmbeddingEngine

Local SentenceTransformer inference converts text to normalized dense float32 BLOBs. Weights are distributed-parametric; loaded models live in process memory/cache, outputs in SQLite. Parameters are not updated by the inspected encode methods; the query cache changes, not model weights. Exact model artifact version is not pinned: loading uses a model name without a revision. A name/cache resolution can supply different weights between installations; this is not a fixed content-addressed endpoint. Remote dependency internals are uninspected. The prompt hook separately constructs SentenceTransformer, so shared-wrapper cache/loading protections do not cover it. SRC-1, `zikkaron/embeddings.py`, `zikkaron/hooks/prompt-recall.py`.

> self._model = SentenceTransformer(
>     self.model_name, trust_remote_code=True,
>     local_files_only=local_only,
> )
> --- `zikkaron/embeddings.py`

> vec = self._model.encode(text)
> arr = self._normalize(np.asarray(vec, dtype=np.float32))
> result = arr.tobytes()
> --- `zikkaron/embeddings.py`

The fallback retries local and potentially online loading; only ImportError becomes the wrapper's permanent unavailable state. Fixed inference is not evidence against learning through retained text or numerical state elsewhere.

#### RT-CMP-gte-reranker
Label: GTE reranker

Distributed-parametric CrossEncoder loaded in RAM by configured name `Alibaba-NLP/gte-reranker-modernbert-base`; it scores query/content pairs, truncated to 512 content characters in this branch. Inspected code predicts and blends scores, without weight updates. Exact artifact revision is unpinned; name resolution may change externally, although there is no remote provider endpoint in this local branch. On failure it records a false sentinel and can fall back. SRC-1, `zikkaron/retrieval.py`, `zikkaron/config.py`.

> self._gte_reranker = STCrossEncoder(
>     self._settings.GTE_RERANKER_MODEL,
>     max_length=self._settings.GTE_RERANKER_MAX_LENGTH,
> )
> --- `zikkaron/retrieval.py`

#### RT-CMP-flashrank-ranker
Label: FlashRank Ranker

Distributed-parametric ONNX reranker, RAM plus local cache. The inspected caller invokes inference, not weight training. Artifact version is not pinned; the fixed model-name string can resolve to different external artifacts across installs, while dependency behavior remains uninspected. It is a fallback, not assured availability. SRC-1, `zikkaron/retrieval.py`.

> self._flashrank_ranker = Ranker(
>     model_name="ms-marco-MiniLM-L-12-v2",
>     cache_dir=os.path.expanduser("~/.cache/flashrank"),
> )
> --- `zikkaron/retrieval.py`

#### RT-CMP-cross-encoder
Label: Sentence-transformers CrossEncoder fallback

Distributed-parametric local CrossEncoder in RAM, name selected by `CROSS_ENCODER_MODEL`. Predict-only in the inspected fallback; no operational weight change is wired there. Exact artifact version is unpinned and external name/cache resolution can change it. It is distinct from GTE and FlashRank because loading and fallback failures differ. SRC-1, `zikkaron/retrieval.py`, `zikkaron/config.py`.

> self._cross_encoder = CrossEncoder(
>     self._settings.CROSS_ENCODER_MODEL
> )
> --- `zikkaron/retrieval.py`

#### RT-CMP-nli-model
Label: NLI model

Distributed-parametric local CrossEncoder in RAM; default `cross-encoder/nli-deberta-v3-base`. It scores premise/hypothesis pairs; code assumes class index 2 is entailment. Predict-only, with no weight updates in the inspected route. Artifact revision is unpinned; external named model resolution may change it, and correctness of the assumed class mapping is not established here. SRC-1, `zikkaron/retrieval.py`, `zikkaron/config.py`.

> self._nli_model = CrossEncoder(self._settings.NLI_MODEL)
> --- `zikkaron/retrieval.py`

#### RT-CMP-comet-inferencer
Label: CometInferencer

Distributed-parametric seq2seq inference in RAM/model cache, used by optional index enrichment and optional query expansion. The loader selects the configured `COMET_MODEL`, without artifact revision pinning; mutable external name resolution may change weights. `.eval()` and generation paths wire inference, not operational training. Generated natural-language inferences are separately retained/delivered content, not model parameters. SRC-1, `zikkaron/enrichment.py`, `zikkaron/config.py`, `zikkaron/retrieval.py`.

> self._tokenizer = AutoTokenizer.from_pretrained(model_name)
> self._model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(self._device)
> self._model.eval()
> --- `zikkaron/enrichment.py:289-307`

#### RT-CMP-doc2-query
Label: Doc2QueryExpander

Separate distributed-parametric seq2seq model for synthetic query enrichment, stored in process memory/cache. Default `doc2query/msmarco-t5-small-v1`; no exact revision pin. External name resolution may change weights; inspected loader/generation uses evaluation inference rather than training. Inclusion in storage enrichment depends on caller-provided settings and embeddings. SRC-1, `zikkaron/enrichment.py`, `zikkaron/storage.py`, `zikkaron/config.py`.

> self._tokenizer = AutoTokenizer.from_pretrained(model_name)
> self._model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(self._device)
> self._model.eval()
> --- `zikkaron/enrichment.py:385-403`

#### RT-CMP-hopfield-memory
Label: HopfieldMemory

A distributed dense pattern matrix is rebuilt from hot stored embeddings, capped by `HOPFIELD_MAX_PATTERNS`, and cached in RAM. It changes when rebuilt from changed retained memories, not through a gradient-trained weight updater. Its source algorithm is fixed by SRC-1, but exact numerical contents depend on DB state and unpinned embedding artifacts. No mutable provider endpoint resolves this matrix. SRC-1, `zikkaron/hopfield.py`.

> self._pattern_matrix = np.stack(rows)  # shape (N, d)
> --- `zikkaron/hopfield.py`

#### RT-CMP-hdc-encoder
Label: HDCEncoder

Distributed dense bipolar vectors are generated from a default seed 42 and a mutable in-process codebook; memory vectors are stored as bytes. Runtime growth creates atoms, not trained model weights. Algorithm and initial seed are fixed in SRC-1, but the actual codebook depends on access history, and a seed alone does not pin the operative state. No provider/model endpoint is used. SRC-1, `zikkaron/hdc_encoder.py`, `zikkaron/server.py`.

> if name not in self._codebook:
>     self._codebook[name] = self._random_vector()
> return self._codebook[name]
> --- `zikkaron/hdc_encoder.py`

#### RT-CMP-cognitive-map
Label: CognitiveMap

Distributed numerical successor matrix and coordinates derive from symbolic transition-count rows in SQLite; matrix caches are in RAM. Numerical state changes during use: transition recording marks it dirty, rebuilding computes an inverse/series, and an indexed TD update changes a matrix row. This is not a pinned pretrained artifact; its algorithm is pinned by SRC-1, contents depend on runtime DB state. No mutable remote model endpoint. SRC-1, `zikkaron/cognitive_map.py`, `zikkaron/server.py`.

> delta = e_to + self._discount * self._sr_matrix[j] - self._sr_matrix[i]
> self._sr_matrix[i] += self._lr * delta
> --- `zikkaron/cognitive_map.py`

#### RT-CMP-evaluation-models
Label: Evaluation generation and judging models

The LoCoMo driver selects separate generation and judge model/provider arguments, using OpenAI, Anthropic, Gemini or local Transformers. Distributed-parametric provider weights are outside the checkout; the local model is loaded in RAM/cache. The inspected local call generates under `torch.no_grad()` with no weight-update path; provider-internal updates are uninspected. Neither remote aliases nor local `from_pretrained` artifact revisions are pinned, and provider endpoints/name resolution can change the model across runs. A further LongMemEval mode delegates to `claude -p` without selecting an exact model, leaving the model and host state opaque. Local loading caches one model globally, so changing judge model names in the same process does not itself reload a different local model. SRC-1, `benchmarks/run_locomo_jscore.py`, `benchmarks/run_longmemeval.py`.

> if _LOCAL_MODEL is not None:
>     return
> --- `benchmarks/run_locomo_jscore.py`

> _LOCAL_MODEL = AutoModelForCausalLM.from_pretrained(model_name, **load_kwargs)
> --- `benchmarks/run_locomo_jscore.py`

### Operative objects

#### RT-OBJ-zikkaron-section
Label: Canonical Zikkaron instruction section

Natural-language instructions interpreted by the external host model; canonical template in `server.py`, installed in the global CLAUDE.md or caller-selected path. This is a static shipped policy synchronized to disk, not a use-derived memory. It asks the host to recall at startup, get context before tasks and remember significant outcomes; instructions do not enforce compliance. SRC-1, `zikkaron/server.py`.

> - Before starting any task, call `get_project_context` for the current working directory
> - After completing any significant task, call `remember` to store what was done, decisions made, and outcomes
> --- `zikkaron/server.py`

#### RT-OBJ-hooks-config
Label: Installed hooks configuration

Symbolic JSON in project `.claude/settings.json` plus executable Python/shell copies under `.claude/hooks`. Claude Code interprets event matchers and command strings; script code determines database effects. Distinct from the instruction object because host event delivery, rather than model interpretation of prose, triggers it. SRC-1, `zikkaron/server.py`.

> settings_data["hooks"] = hooks_config
> settings_path.write_text(json.dumps(settings_data, indent=2))
> --- `zikkaron/server.py`

#### RT-OBJ-memory-rules
Label: memory_rules

Symbolic condition/action records in SQLite, admitted by parser and applied by RulesEngine. Scope, priority, active flag and action magnitude have fixed consumers. Natural-language-looking strings such as `importance > 0.7` are interpreted by code, not a language model in this route. These are selection controls, not host tool permissions. SRC-1, `zikkaron/rules_engine.py`, `zikkaron/storage.py`.

> # Validate condition parses correctly
> _parse_condition(condition)
> 
> # Validate action parses correctly
> _parse_action(action)
> --- `zikkaron/rules_engine.py`

### Routes

#### RT-RTE-remember-recall
Label: Explicit remember and subsequent recall

Host MCP caller proposes text/tags/directory; `remember` owns admission and persistence, then returns to the host. The gate decides by numerical novelty and keyword/tag bypasses; curator owns merge/link/create when present, direct storage is the fallback. No expected-answer oracle or per-content human veto is wired in this wrapper. Human authorship/control depends on the caller and is unresolved. Operating mode is open host requests, not a bounded curriculum. Knowledge-change guidance is the configured admission/curation policy; rejection is the gate's false result, recovery includes caller retry/forget rather than a whole-operation rollback. Source-native revisions remain for the memory analyst.

- Immediate return: rejection dictionary or stored memory dictionary, with vectors removed and optional reinjected related text.
- Later read-back: stored text, scores and links become inputs to later recall, project context and replay.
- Delegated visibility: host receives selected dictionaries; no separate child-agent visibility is wired by this function.
- Selection predicate: predictive novelty threshold, continuity discount and error/decision/important-tag bypasses at admission; later selection follows the linked retrieval route.
- Invalidation or expiry: forget, decay, staleness and later curation can change availability; no fixed lifetime is promised.
- Activation or effect: SQL writes and response construction are wired; actual host reliance is uninspected.
- Evidence limits: static SRC-1 implementation, `zikkaron/server.py`, `zikkaron/predictive_coding.py`; no successful invocation or observed learning benefit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not should_store:
>     return {
>         "stored": False,
> --- `zikkaron/server.py`

> effective_threshold = max(0.1, self._threshold - discount)
> --- `zikkaron/predictive_coding.py`

This route uses [RT-CMP-embedding-engine](#rt-cmp-embedding-engine), [RT-CMP-hdc-encoder](#rt-cmp-hdc-encoder) and later [RT-CMP-cognitive-map](#rt-cmp-cognitive-map). Its caller can exercise the keyword/tag bypass; this is intentional admission policy, not a novelty invariant.

#### RT-RTE-context-selection
Label: Service recall context selection

Query, requested count and heat floor reach HippoRetriever. Code routes signals by query analysis, collects vector/FTS/graph and other enabled candidates, fuses scores (default setting `convex`, not merely the WRRF docstring), reranks, merges profiles/beliefs, applies diversity and rules, then context packing. The server wrapper subsequently boosts heat, records transitions and invokes reconsolidation. This is code-owned selection with learned inference scores, not an answer oracle. No per-result human selection is wired. SRC-1, `zikkaron/retrieval.py`, `zikkaron/server.py`, `zikkaron/config.py`.

- Immediate return: memory dictionaries selected by ranking/rules and possibly chunked or summarized by metacognition.
- Later read-back: returned access updates and transition state affect later invocations; current result metadata alone is not retained learning.
- Delegated visibility: only the selected/packed return crosses to the caller; candidate pool and omitted content remain in storage.
- Selection predicate: query analysis, heat, configured signal weights, reranker scores, optional symbolic rules and importance/heat/confidence chunk ranking.
- Invalidation or expiry: changed DB state/configuration/model resolution changes future selection; no stable result-set promise.
- Activation or effect: code controls result delivery and access-state mutations; changed conversational behavior is unobserved.
- Evidence limits: optional model availability and all signal algorithms were not independently verified; packer can add overflow summaries after an earlier count trim.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> result_memories = self._rules_engine.apply_rules(result_memories, directory)
> --- `zikkaron/retrieval.py`

> # Step 4: Take top max_chunks
> selected = scored_chunks[:max_chunks]
> overflow = scored_chunks[max_chunks:]
> --- `zikkaron/metacognition.py`

The packer groups related memories, preserves selected full chunks and adds summaries of overflow; it is neither an exact four-memory cap nor host-window eviction. Exceptions in packing return the unoptimized selection. Numerical consumers include [RT-CMP-gte-reranker](#rt-cmp-gte-reranker), [RT-CMP-flashrank-ranker](#rt-cmp-flashrank-ranker), [RT-CMP-cross-encoder](#rt-cmp-cross-encoder), [RT-CMP-nli-model](#rt-cmp-nli-model), [RT-CMP-hopfield-memory](#rt-cmp-hopfield-memory), [RT-CMP-hdc-encoder](#rt-cmp-hdc-encoder) and [RT-CMP-cognitive-map](#rt-cmp-cognitive-map). Availability/flags determine participation, not observed exercise.

#### RT-RTE-trace-consolidation
Label: Tool trace capture and background consolidation

Host PostToolUse events start a fresh script process; HTTP and CLI capture are alternate endpoints. Input-derived summaries, tool identity, cwd, session and timestamp become `action_log` rows without the remember gate. The daemon checks idle time and runs a cycle, or the caller forces consolidation. Code proposes and admits summary memories from directory/time groups; groups of three or more create summaries, all fetched groups are marked processed even if too small. No individual human approval or expected-answer oracle is wired. The improvement trigger is idle/forced processing, not evidence of improved capacity. Policy keeps counts and at most five truncated details; these persist as low-heat episodic memories. SRC-1, `zikkaron/hooks/post-tool-capture.py`, `zikkaron/server.py`, `zikkaron/__main__.py`, `zikkaron/consolidation.py`.

- Immediate return: hook normally emits nothing; HTTP returns captured/skipped/error; force consolidation returns counters.
- Later read-back: summaries enter memory retrieval; raw actions also reach the session-start hook, even before summary production.
- Delegated visibility: maintenance runs on a daemon thread sharing storage, not a separately prompted agent; host later sees selected text.
- Selection predicate: capture skips own MCP-tool prefix; processing selects up to 200 unprocessed rows, groups by directory and 30-minute bucket, admits summary only for groups with at least three actions.
- Invalidation or expiry: processed flags remove rows from subsequent processing; decay/curation affect summaries. Hook failures can silently omit records.
- Activation or effect: trace-fed durable insertion and later consumer wiring exist; actual recording, replay and behavioral benefit remain unobserved.
- Evidence limits: no run demonstrates exactly-once behavior or concurrent failure recovery; multi-commit insertion and processed marking do not establish atomic end-to-end processing.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if len(actions) >= 3:
>     tools_str = ", ".join(f"{t}({c})" for t, c in sorted(tool_counts.items(), key=lambda x: -x[1]))
>     content = f"Session activity [{tools_str}]: {len(actions)} tool calls"
> --- `zikkaron/consolidation.py`

Rejection is mechanical (prefix, missing DB, too-small groups), not content approval. Recovery is best-effort retries of future cycles; there is no automatic whole-cycle undo in this traced path. The rest of the cycle wires decay, duplicate merge, graph work, domain processing, memify, CLS and compression; their internal knowledge transformations are not recharacterized here.

#### RT-RTE-hook-context
Label: Automatic prompt and session context

UserPromptSubmit and SessionStart host events run independent scripts, not the service recall wrapper. Prompt JSON supplies query and cwd; FTS runs first, optional local vector inference follows, results are merged/ranked/formatted and printed. Session-start reads the latest active checkpoint, hot project memories, global anchors and recent actions. Host owns actual stdout injection. SRC-1, `zikkaron/hooks/prompt-recall.py`, `zikkaron/hooks/session-start-context.py`.

- Immediate return: stdout Markdown context or silent no-op on missing inputs/database/results and many errors.
- Later read-back: independently selected retained memories/checkpoint/actions are delivered to later prompts or sessions; this read path itself does not persist a new memory.
- Delegated visibility: only formatted text crosses back from the hook subprocess; full rows and vector model state do not.
- Selection predicate: prompt FTS uses first 15 cleaned terms, current directory first then global supplement, nonstale/heat filters, vector hits and local/manual/heat boosts; top five results and content-character truncation. Session-start uses separate fixed SQL limits.
- Invalidation or expiry: each event reselects current DB rows; no fixed expiry for delivered text, whose host-window retention is external.
- Activation or effect: output construction is wired; Claude Code delivery and subsequent compliance are unobserved.
- Evidence limits: synchronous vector loading is not preempted; default-DB divergence can split capture/consumption, and global supplement/checkpoint/anchors prevent a project-isolation guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if time.monotonic() - t0 > 0.15:
>     # Model loading took too long, skip vector search
>     return []
> --- `zikkaron/hooks/prompt-recall.py`

> # Plain text stdout is auto-injected as context by Claude Code
> # This is simpler and more reliable than JSON hookSpecificOutput
> print(context)
> --- `zikkaron/hooks/prompt-recall.py`

This is unsolicited supply relative to host tool selection: the host event triggers retrieval from the user's prompt even if the foreground model never asks to recall. The deciding selector is code, not an autonomous foreground agent. [RT-CMP-embedding-engine](#rt-cmp-embedding-engine) describes the shared model family but the hook's separate loader has its own cache/time behavior.

#### RT-RTE-replay-context
Label: Checkpoint anchor drain and restoration

Caller `checkpoint` supplies structured working state; `anchor` proposes protected text and directly inserts it. PreCompact calls `zikkaron drain` in a subprocess, incrementing an epoch and updating/creating a checkpoint. SessionStart compact invokes `zikkaron restore`; the lightweight CLI opens its own storage/retrieval/replay engines without daemons and prints formatted context. HTTP pre/post-compact and MCP restore are alternate paths; HTTP pre-compact additionally attempts forced consolidation. Code admits caller content, with no per-content approval or answer oracle. Trigger is explicit preservation/significant remember event/host compaction, and mode is open host use. SRC-1, `zikkaron/server.py`, `zikkaron/__main__.py`, `zikkaron/restoration.py`, `zikkaron/hooks/pre-compact-drain.sh`, `zikkaron/hooks/post-compact-rehydrate.sh`.

- Immediate return: checkpoint/anchor IDs, drain status, or restore dictionary/Markdown depending on entry path.
- Later read-back: checkpoints, protected anchors, recent memories, hot project material and optional SR predictions reach post-compaction or later session context.
- Delegated visibility: CLI subprocess returns only formatted stdout; outer host window compaction and residual window contents are opaque.
- Selection predicate: global active checkpoint; bounded global anchors/recent memories; hot directory lookup; optional SR navigation from checkpoint task and bounded gaps; formatting further caps/truncates recent/hot/predicted sections.
- Invalidation or expiry: checkpoint insertion deactivates all prior checkpoints globally; anchor inclusion requires positive heat and is bounded by a configured limit, not all anchors forever.
- Activation or effect: persistence and reconstruction are wired; full-conversation restoration and subsequent use are unobserved and not guaranteed by this code.
- Evidence limits: drain does not receive conversation text; shell hooks suppress errors, and directory labels do not scope every selected section.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self._conn.execute("UPDATE checkpoints SET is_active = 0 WHERE is_active = 1")
> --- `zikkaron/storage.py`

> active = self._storage.get_active_checkpoint()
> auto_created = False
> --- `zikkaron/restoration.py`

Proposed change is a caller-written snapshot/protected fact or an automatic placeholder/micro-checkpoint. Admission is immediate storage; rejected/unavailable writes fail or are swallowed upstream. Recovery is reconstruction from retained material, not rollback to the exact discarded window. Static guidance asks for periodic checkpoints; it does not make that state available automatically. No context-frame isolation is supplied by replay itself.

#### RT-RTE-seed-admission
Label: Project seed admission

Host tool or CLI requests a scan; scan/generation code proposes project-summary memories and code admits them directly. No per-memory human review or answer oracle. Human starting a scan is not approval of each derived claim. Dry run is an explicit nonwriting mode; normal mode deletes prior seed entries for that project and inserts replacements. Guidance is shipped scan/template/heat policy, not a learned proposal method. SRC-1, `zikkaron/seed.py`, `zikkaron/server.py`, `zikkaron/__main__.py`.

- Immediate return: preview/stats in dry run, or created/replaced counts after persistence.
- Later read-back: seed summaries become ordinary recall/project-context inputs.
- Delegated visibility: project files are consumed locally; host receives counts/preview, not an agent-subtask transcript.
- Selection predicate: scan_project and generate_memories choose supported project structure/configuration/documentation; normal insertion bypasses remember's gate and curator deduplication.
- Invalidation or expiry: reseeding deletes existing seed memories for the root; ordinary maintenance can subsequently affect replacements.
- Activation or effect: file read, replacement and memory insertion are wired; factual completeness and host use are unobserved.
- Evidence limits: external project files are not frozen, and mid-seed failure can follow deletion; no atomic whole-seed rollback is established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # Insert directly (no curator dedup since we already cleared old seeds)
> memory_id = storage.insert_memory({
> --- `zikkaron/seed.py`

Rejection ability is caller choice of dry run plus implementation failures, not a substantive approval gate. Retry/reseed is available; reconstruction of deleted old seed state is not promised by this route.

#### RT-RTE-rule-admission
Label: Retrieval rule admission

MCP caller proposes rule type/scope/condition/action/priority. RulesEngine validates enumerated values and parses condition/action; hard rules must use filter. Code can veto malformed inputs; no human review or expected-answer oracle. Accepted symbolic policy is persisted and applied on future service retrieval. Operating mode is caller-directed policy editing, not measured successor optimization. SRC-1, `zikkaron/server.py`, `zikkaron/rules_engine.py`.

- Immediate return: created rule ID or validation error.
- Later read-back: active rules are selected by global/directory-prefix/file-glob scope and influence later retrieval.
- Delegated visibility: retrieval code receives rules; host sees the resulting selection, and can query rules separately.
- Selection predicate: type/scope/parser validation at write, active/scope/priority at read, condition evaluation and fixed filter/boost/penalty semantics at effect.
- Invalidation or expiry: stored active state and storage update/delete methods govern lifetime; this inspected MCP surface exposes add/get rather than a full rollback tool.
- Activation or effect: wired into HippoRetriever; alternate direct-SQL hooks and replay are outside this enforcement point.
- Evidence limits: no executed rule or downstream host behavior was supplied; scope is inferred from retrieved content in the consumer, not an authenticated requester boundary.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if rule_type == "hard":
>     # Filter: keep only memories that satisfy the condition
>     result = [
>         m for m in result
>         if self.evaluate_condition(condition, m)
>     ]
> --- `zikkaron/rules_engine.py`

Change guidance is user/caller policy expressed in a fixed grammar. Persistence is [RT-OBJ-memory-rules](#rt-obj-memory-rules); malformed proposals are rejected before insertion. Existing storage methods afford removal/update, but no exercised recovery protocol is observed. This is not evidence of formulated criticism or theory-building iteration.

#### RT-RTE-install-integration
Label: Instruction synchronization and hook installation

Startup and explicit MCP calls admit behavioral instructions and executable integration configuration. The shipped canonical template proposes the instruction text; package scripts and installation code propose event commands. Software writes them without per-update human approval in this path. Caller can choose paths, filesystem errors can prevent writes, and a missing instruction parent returns skipped. There is no answer oracle. Mode is installation/update synchronization, not an experiment. SRC-1, `zikkaron/server.py`.

- Immediate return: synced/installed/skipped dictionaries; startup logs and continues on exception.
- Later read-back: host loads installed prose and event configuration on later invocations; this static synchronization is not use-derived memory read-back.
- Delegated visibility: global instructions can affect other projects; project hook commands launch separate local processes under host authority.
- Selection predicate: replace an existing Memory System section or append; copy five hook files and assign the four relevant event arrays in existing settings JSON.
- Invalidation or expiry: subsequent startups resynchronize; filesystem contents persist until changed, with no automatic expiry.
- Activation or effect: file mutation is wired; host loading/execution and instruction compliance are unobserved.
- Evidence limits: errors are nonfatal, event arrays are assigned rather than merged itemwise, and no backup/automatic rollback is wired in the inspected installer.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> for filename, mode in hook_files.items():
>     src = package_hooks / filename
>     dst = hooks_dir / filename
>     if src.exists():
>         shutil.copy2(src, dst)
>         dst.chmod(mode)
> --- `zikkaron/server.py`

> md_path.write_text(new_content)
> --- `zikkaron/server.py`

Persistence and downstream force differ: [RT-OBJ-zikkaron-section](#rt-obj-zikkaron-section) is an interpreted instruction request; [RT-OBJ-hooks-config](#rt-obj-hooks-config) is a host event command contract. Recovery would require editing/restoring files; the shown code does not preserve prior versions. Package release admission is external maintainer release plus CI tests, not this runtime revising its own implementation.

#### RT-RTE-evaluation-mode
Label: Dataset retrieval generation and judging

A benchmark operator selects data/configuration/model/provider. LoCoMo creates per-conversation storage, ingests observations through storage helpers, retrieves for each question, formats top context memories with dates, generates an answer, and scores against dataset gold answers using F1 and optional LLM judgment. The driver decides progression; generation proposes an answer, not a product update. The oracle is the dataset's answer supplied to F1/judge; the generation input contains retrieved content and question, not that gold answer in this function. LongMemEval provides another bounded mode using `claude -p` for reading and judging. SRC-1, `benchmarks/run_locomo_jscore.py`, `benchmarks/test_e_locomo.py`, `benchmarks/run_longmemeval.py`.

- Immediate return: generated answers, correctness/F1 records and aggregate report; failure paths substitute fallback answers/failed judgments.
- Later read-back: evaluation results can be saved by the driver; no automatic admission from these judgments into production policy or model weights is established in the inspected loop.
- Delegated visibility: generation receives selected top-k memory text; judge receives question, gold and generated answer. Remote providers receive these messages; subprocess mode returns parsed result text only.
- Selection predicate: selected conversations/questions, settings overrides, retrieval count, top-k context, provider/model choice, optional f1-only switch.
- Invalidation or expiry: per-conversation evaluation DB is recreated in this LoCoMo path; result lifetime is operator/file controlled.
- Activation or effect: concrete generation/judge calls are wired, but no responses/runs or causal performance contrast was supplied.
- Evidence limits: datasets, credentials, provider internals, model artifacts and output records are outside the frozen evidence; local global-model caching can collapse nominally separate generation/judge model selections.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> judgment = judge_answer(
>     question, gold_answer, generated,
>     provider=judge_provider, model=judge_model,
> )
> --- `benchmarks/run_locomo_jscore.py`

> cmd = ["claude", "-p", "--output-format", "json"]
> --- `benchmarks/run_longmemeval.py`

The latter call has a subprocess timeout and empty-string error fallback; its enclosing Claude permissions/session behavior are not established here. [RT-CMP-evaluation-models](#rt-cmp-evaluation-models) owns model fixity limits. These scores are answer comparisons, not a guaranteed product-change gate or evidence of content-directed criticism of the memory method.

### Claims

#### RT-CLM-write-gate
Label: Store only prediction errors

The predictive gate's source docstring says:

> Only stores prediction errors — information that violates the existing
> generative model for a directory context.
> --- `zikkaron/predictive_coding.py`

SRC-1, `zikkaron/predictive_coding.py`. Owner: PredictiveCodingGate invoked by `remember`. Enforcement: early return in [RT-RTE-remember-recall](#rt-rte-remember-recall). Guarantee strength: policy. Implementation conclusion status: wired. Operation conclusion status: uninspected. This is a heuristic admission policy with intentional bypasses, not a storage-wide invariant. Capture/consolidation, seeds and anchors have separate admission mechanisms. It requires callers to enter through remember; direct storage paths do not inherit it. No truth or utility guarantee follows from high surprisal.

#### RT-CLM-context-replay
Label: Anchors always included in restoration

> They are ALWAYS included in restoration regardless of other scoring.
> --- `zikkaron/restoration.py`

SRC-1, `zikkaron/restoration.py`. Owner: HippocampalReplay. Enforcement: protected-positive-heat anchor query and formatter in [RT-RTE-replay-context](#rt-rte-replay-context). Guarantee strength: best effort. Implementation conclusion status: wired. Operation conclusion status: uninspected. The anchor query is limited and requires heat > 0; the session-start path has its own limit four. Thus the defensible guarantee is preferential bounded selection, not every anchor forever, nor complete host-window restoration. External contract: successful writes, hooks/CLI execution and host injection. The shell's success exit despite errors does not establish restoration success.

#### RT-CLM-hook-budget
Label: Prompt recall latency and output budget

> Each invocation is a fresh process; vector search is skipped if model load exceeds 150ms.
> --- `zikkaron/hooks/prompt-recall.py`

SRC-1, `zikkaron/hooks/prompt-recall.py`. Owner: prompt-recall script. Enforcement: elapsed checks before vector work and after synchronous load, plus content-character accounting in formatter. Guarantee strength: best effort. Implementation conclusion status: wired. Operation conclusion status: uninspected. The checks choose fallback but do not interrupt imports/loading; the 3000-character setting is not a total-message/token bound. Coverage: prompt hook only; service recall and restoration have distinct controls. External contract: dependency/model performance and host event timeouts, uninspected here.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-host-instructions
Label: Host instruction authority

Consumer: external Claude Code model. Channel: installed global instruction prose from [RT-OBJ-zikkaron-section](#rt-obj-zikkaron-section), written by [RT-RTE-install-integration](#rt-rte-install-integration). Force: requested standing behavior, not code enforcement. Horizon: subsequent host sessions/projects that load the file. SRC-1, `zikkaron/server.py`. The verbatim task-start/task-end directives above establish the request; host loading and compliance are unobserved.

#### RT-BAP-context-delivery
Label: Retained content as model context

Consumer: foreground host or benchmark generation model. Channel: MCP tool results, hook stdout, restoration Markdown or evaluator context messages. Force: information/instruction-like text interpreted by the model, not a hard obligation to use it. Horizon: later prompts, compaction boundaries and sessions when selected. [RT-RTE-context-selection](#rt-rte-context-selection), [RT-RTE-hook-context](#rt-rte-hook-context), [RT-RTE-replay-context](#rt-rte-replay-context) and [RT-RTE-evaluation-mode](#rt-rte-evaluation-mode) establish producer/selection/delivery paths. SRC-1, `zikkaron/server.py`, `zikkaron/hooks/prompt-recall.py`, `zikkaron/restoration.py`, `benchmarks/run_locomo_jscore.py`. Delivery does not establish changed behavior or beneficial learning.

#### RT-BAP-retrieval-rules
Label: Symbolic selection authority

Consumer: HippoRetriever through RulesEngine. Channel: active SQLite rule rows. Force: deterministic filtering/score adjustments on this path's selected memories; not a system-wide data-access policy. Horizon: later retrieval calls until changed/deactivated/deleted. [RT-RTE-rule-admission](#rt-rte-rule-admission) and [RT-OBJ-memory-rules](#rt-obj-memory-rules) retain admission and exact consumer evidence. SRC-1, `zikkaron/rules_engine.py`, `zikkaron/retrieval.py`. Direct SQL consumers and replay bypass this force.

## Annotations

none

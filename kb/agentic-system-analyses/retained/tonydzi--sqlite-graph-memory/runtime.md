---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "sqlite-graph-memory runtime: MCP recall, CLI forcing routes, indexing, transcript capture and change admission at the frozen public revision."
run-id: AAS-2026-11-08-sqlite-graph-memory-ca3785ec5c2e-01
reviewed-boundary: f05db2778159d50a0ad8a35be4f2be3a6aea94b1
---

# sqlite-graph-memory runtime report

## Runtime account

The shipped system returns retrieved context; it does not own the agent's answer-generation loop. An enclosing MCP client chooses when and why to call `memory_recall`. The package owns selection and formatting after that request, not the client's adoption of the result. Its second principal loop is a host-triggered Stop hook that parses transcript text into a ledger, not a model-driven reflection step. These responsibilities and external-host limits follow the [boundary](boundary.md); implementation evidence below is SRC-1 at its frozen revision. No target code, test, example or model was executed. Activation in a real host and downstream benefit remain unobserved.

### Ordinary invocation and return

An operator installs an embedding extra, builds an index over a chosen Markdown directory and registers `sgm-mcp`. `pyproject.toml` also registers `sqlite-graph-memory` to the same server. The stdio loop accepts newline-delimited JSON, advertises one tool and processes requests sequentially. The requesting host supplies a query and optionally a mode. `memory_recall` defaults to associative mode; unknown modes passed to `run_recall` fall back to associative. The advertised string schema is not a comprehensive runtime argument validator: the handler checks query truthiness and passes it on; malformed non-string arguments are not thereby supported inputs (SRC-1, `src/sqlite_graph_memory/mcp_server.py`, `pyproject.toml`).

[RT-RTE-mcp-recall](#rt-rte-mcp-recall) traces the return boundary. The server invokes a Python child with an argument list, not a shell, sets a unique answer-file path, preserves the launcher's working directory and inherits the rest of its environment. The child reloads a NumPy matrix and pickled metadata, embeds `query: ` plus the query with [RT-CMP-e5-model](#rt-cmp-e5-model), scores all chunks and retains each file's best chunk up to a default pool of 60 files. Associative recall follows outgoing links from the first 15 seed hits, adding at most 40 indexed neighbor chunks. Link parsing ignores fenced and inline code. It resolves plain stems and qualified paths; it does not recursively traverse the added neighbors. Links are read from current files, while scores and delivered snippets come from the last index build (SRC-1, `src/sqlite_graph_memory/brain_ask.py`).

The foreground package policy is symbolic Python. Default ordering is dense similarity, not a cross-encoder judgment. Optional reranking uses [RT-CMP-rerank-model](#rt-cmp-rerank-model) on query/title/snippet pairs. The ranked list has at most 12 entries; `--ask` formats only its first eight as headings, dates, scores and stored snippets. MCP returns the answer-file text as tool-result content and deletes the temporary file. There is no generated final answer or citation-verification stage in this path. Knowledge and instruction-like text inside retrieved snippets arrives through the same textual result channel; whether the host treats it as evidence or as instructions is outside the frozen implementation ([RT-BAP-context-delivery](#rt-bap-context-delivery)).

### Four forcing cases and guarantee coverage

1. **Entity-shaped query, graph mode.** `looks_like_entity` uses token count, known tools, capitalization and underscore rules. The normal CLI graph path computes general expansion first, then, for an entity-shaped query, replaces the selected candidate additions with `superseded_by`-only additions. It does not filter closed notes or guarantee replacement inclusion after ranking. `--ab` returns before this gate: its associative arm uses unrestricted expansion even for an entity-shaped query. The benchmark adapter instead omits all expansion for a gated entity, including supersession following; `run_eval.py` expands every query, recording the entity flag without using it as a gate; `run_ablation.py` follows supersession in gated hop-enabled cells. These are reachable shipped branches, not hypothetical direct-call bypasses. Hence a universal claim that all package consumers share one entity policy would be false ([RT-RTE-recall-options](#rt-rte-recall-options), [RT-RTE-evaluation-paths](#rt-rte-evaluation-paths)).
2. **Optional PPR and reranking.** The inherited environment can enable reranking or PageRank even though the MCP input schema exposes neither. PPR is an ordering lane over existing candidates, not a candidate producer; it protects the first five ranked positions and fuses the tail. It can be enabled even with direct mode, which means “no graph expansion” need not mean “no graph-dependent ordering.” A/B explicitly declines PPR. Graph/PPR failures fall back to the previous candidate/order path; missing index or model loading failure is not covered by that local fallback. General expansion can already have read files before the entity gate is applied. The guarantee concerns selected additions, not avoidance of graph I/O (SRC-1, `src/sqlite_graph_memory/brain_ask.py`, `src/sqlite_graph_memory/ppr.py`).
3. **Child failure or empty answer file.** MCP checks the child exit code before reading its scoped file, returns an error on failure or timeout, and does not substitute stdout for an empty file. This prevents startup notices from becoming a success answer on this path. It does not validate retrieved statements, make the child sandboxed, or protect against an untrusted pickled index. Direct CLI calls do not share the parent timeout or scoped-output management ([RT-CLM-scoped-return](#rt-clm-scoped-return)).
4. **Index/capture admission under failure.** Hidden paths are skipped by default but explicitly admitting hidden paths is supported; sync-conflict filenames remain excluded. Incremental reuse trusts matching size and mtime plus an existing stored hash without rehashing that file. Index writes are three successive file writes rather than one atomic snapshot. The hook advances its offset before row insertion and skips gaps above 4 MiB. The installed hook can propagate storage errors; only module/script invocation suppresses them. Neither path guarantees reliable, exactly-once capture; an index freshness or complete-ledger guarantee is unwarranted ([RT-RTE-index-admission](#rt-rte-index-admission), [RT-RTE-turnstate-capture](#rt-rte-turnstate-capture)).

### Effects, working context and deployed envelope

Capabilities differ by entry path. MCP advertises only recall, but the recall child can read the configured index and note paths, load model artifacts, write an answer and, in A/B mode, write SQLite telemetry and optional JSON. `sgm-index` admits filesystem content into persistent index files. The Stop hook appends derived transcript rows; the viewer later displays them by session or recency. `sgm-stats` and `sgm-doctor` are additional packaged operator entry points, not agent-generation loops (`pyproject.toml`). This report does not assess all their diagnostic checks.

The actual grant set is the environment, process identity and filesystem access supplied by deployment. The inspected server provides neither a per-call user-approval gate nor a deployment isolation specification. Its subprocess is crash containment, not an OS permission boundary. In particular, index metadata is deserialized with `pickle.loads`, and graph reads use stored file paths. Operators must supply a trusted index, permitted note access and an external client/OS security contract; “local” does not establish safe handling of hostile artifacts (SRC-1, `src/sqlite_graph_memory/mcp_server.py`, `src/sqlite_graph_memory/brain_ask.py`).

Selection and clipping bound the delivered working context: candidate deduplication, top-N ranking, the eight-snippet bundle, and stored 600-character snippet limits keep other material out. The deciding agent here is code plus optional numerical ranking, not a summarizing runtime LLM. This is on-demand supply from an external store, not eviction of prior host turns. The package does not manipulate the host's accumulated conversation window on the inspected return path. A separate OS child isolates computation but not a separate agent reasoning context; only its textual return crosses back. The stack-frame analogy applies to the child lifecycle only, not to a claimed subagent/compaction architecture. Later calls can reread the persistent index, whereas full-note reload or conversation trimming is the host's responsibility (SRC-1, `src/sqlite_graph_memory/brain_ask.py`, `src/sqlite_graph_memory/index_notes.py`, `src/sqlite_graph_memory/mcp_server.py`).

### Change and measurement planes

Index refresh is operator/caller-triggered content admission, not per-note approval. Stop capture is automatic once the host registers it. Neither loop changes model parameters. [RT-RTE-change-admission](#rt-rte-change-admission) distinguishes contributor doctrine, portable memory instructions and the release workflow. Contributor rules demand before/after retrieval measurements and reserve model/schema changes for humans; the inspected publisher enforces build/metadata/entry-point checks but does not implement that whole judgment protocol. Shipped instructions can shape an external agent only after a host installs and consumes them ([RT-BAP-temporal-instructions](#rt-bap-temporal-instructions)).

Evaluation reuses retrieval functions but not necessarily the CLI's policy composition. The benchmark adapter always loads a cross-encoder and adds extractive answering and a score-based abstention threshold. That is evaluator behavior, not the MCP answer contract. The gold evaluator supplies reference sets and metrics; A/B recall telemetry supplies a within-query list difference, not an answer oracle or evidence of improved task success. No supplied result artifact was assessed here for observed execution or causal attribution. Added same-pin inspection coverage in this member includes the relevant `score_gold` and `score_grid` branches, `BITEMPORAL.md`, contributor rules, the publishing/testing workflows, and release instructions. These passages supply implementation or doctrine, not newly observed runs (SRC-1, `eval/run_eval.py`, `eval/run_ablation.py`, `bench/adapters/sgm.py`, `.github/workflows/tests.yml`, `.github/workflows/publish.yml`, `docs/RELEASING.md`).

## Shared records

### Components

#### RT-CMP-e5-model
Label: multilingual-e5-base encoder

Source-native identity: `intfloat/multilingual-e5-base`, selected by `E5_MODEL` and ONNX `E5_REPO`. Distributed-parametric weights are stored in external model caches; output vectors are distributed-parametric numerical arrays persisted in the index. The Python selection/pooling rules are symbolic. Both indexing and query scoring use this encoder. No parameter-update operation appears in the inspected encode/load paths. Exact model-byte version is not pinned: neither the SentenceTransformer constructor nor Hugging Face download names a commit revision. A mutable repository resolution/cache can therefore select different artifacts; the model is not an online hosted inference endpoint. Provider repository/weight internals and equality between cached installations remain uninspected (SRC-1, `src/sqlite_graph_memory/brain_ask.py`, `src/sqlite_graph_memory/onnx_backend.py`).

> E5_MODEL = 'intfloat/multilingual-e5-base'
> --- `src/sqlite_graph_memory/brain_ask.py`

> return [hf_hub_download(repo, f, cache_dir=cache) for f in files]
> --- `src/sqlite_graph_memory/onnx_backend.py`

Auto backend selection prefers installed ONNX dependencies. Auto-selected ONNX load failures may fall back to torch if available and annotate the answer; explicitly forced ONNX failures are raised. Runtime choice and downloadable artifacts are not guaranteed by installing the base NumPy-only package (SRC-1, `src/sqlite_graph_memory/brain_ask.py`, `pyproject.toml`).

#### RT-CMP-rerank-model
Label: mmarco cross-encoder

Source-native identity: `cross-encoder/mmarco-mMiniLMv2-L12-H384-v1`. Distributed-parametric weights live in external model caches, with symbolic invocation and sorting code. It scores query/title/snippet pairs only when reranking is enabled in the CLI, but always in the inspected benchmark adapter. The inspected paths perform inference, not weight updates. Model name is fixed in code, exact artifact revision is not pinned, and cache/repository resolution is mutable; no remote inference-service endpoint is configured here. Internals and byte-level backend equivalence remain outside this source boundary (SRC-1, `src/sqlite_graph_memory/brain_ask.py`, `src/sqlite_graph_memory/onnx_backend.py`, `bench/adapters/sgm.py`).

> return '--rerank' in argv or str(env.get('SGM_RERANK', '')).strip() == '1'
> --- `src/sqlite_graph_memory/brain_ask.py`

> self.ce = ba.load_reranker('cpu')
> --- `bench/adapters/sgm.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-mcp-recall
Label: MCP request to scoped context return

The host proposes the query and mode; symbolic server/CLI code owns the next step until the return. Endpoint progression is stdio JSON-RPC → `handle_request` → `run_recall` → child CLI → scoped answer file → MCP text. Client configuration selects index/database paths and inherited backend/order options; the client may separately impose a shorter timeout. This is open-request operation with no answer oracle or human approval inside retrieval. Representation is symbolic control plus numerical scoring and natural-language snippets. SRC-1, `src/sqlite_graph_memory/mcp_server.py`, `src/sqlite_graph_memory/brain_ask.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Context bundle, A/B list comparison or an error text and `isError` flag.
- Later read-back: Each child reloads the retained index; this request does not itself revise note content. A/B persistence is described in the options route.
- Delegated visibility: Child receives query, process environment and index/note access; parent receives its scoped answer text or captured failure output, not a model reasoning transcript.
- Selection predicate: Mode chooses flags; dense pool deduplicates by path, graph expansion and optional ordering precede at most eight snippet entries for `--ask`.
- Invalidation or expiry: Per-call answer file is deleted in `finally`; durable index is refreshed separately, not invalidated by this call.
- Activation or effect: Code wires result delivery to the MCP client; downstream use by an agent is uninspected.
- Evidence limits: Static implementation only; neither successful deployment nor answer correctness is established.

> call_env = {**os.environ, "BRAIN_ANSWER_OUT": str(temp_ans_file)}
> --- `src/sqlite_graph_memory/mcp_server.py`

> for i, sc in reranked[:8]:
> --- `src/sqlite_graph_memory/brain_ask.py`

#### RT-RTE-recall-options
Label: Recall alternate ordering and A/B routes

CLI callers can choose direct, graph, A/B, pool, PPR and rerank controls; MCP exposes only the first three mode choices but inherits the rest through environment. Code's query-shape heuristic controls ordinary graph candidates; inference supplies scores rather than an approval verdict. A/B computes both arms, persists list-difference telemetry with swallowed database errors and returns a comparison instead of the ordinary snippet bundle. Its no-oracle list comparison does not decide a product change. PPR graph state is in-process, cached by a metadata fingerprint; the builder's metadata has paths/titles/snippets/dates but no `sha`, so a same-path content edit need not change that fingerprint within a long-lived direct-import consumer. A new MCP child does not reuse that process cache. SRC-1, `src/sqlite_graph_memory/brain_ask.py`, `src/sqlite_graph_memory/ppr.py`, `src/sqlite_graph_memory/index_notes.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Direct/associative result text, or A/B ranked-title comparison; optional structured JSON diff in A/B.
- Later read-back: `ab_recall` accumulates telemetry, but the inspected recall selector does not consume it to update policy; later telemetry inspection is external to that selector.
- Delegated visibility: MCP invokes the same CLI options for its modes; direct imports can call individual functions without the CLI gate.
- Selection predicate: Default dense top-60 unique files; graph seeds 15, additions at most 40; entity CLI path substitutes supersession-only additions; A/B bypasses this substitution. Reranking opt-in, PPR orders existing candidates and protects first five.
- Invalidation or expiry: Per-query rankings end with the invocation; PPR cache lives in process memory and uses metadata fingerprinting, not a note-content watcher. Telemetry has no expiry in the inspected writer.
- Activation or effect: Options alter candidate membership, order or output form; actual gain is uninspected.
- Evidence limits: Local graph/PPR fallback does not guarantee the whole invocation succeeds. Ordering a superseding note is not enforcing temporal truth or hiding the old note.

> if ab:
>     A = rerank(base_order); B = rerank(graph_order)
> --- `src/sqlite_graph_memory/brain_ask.py`

> gated = graph and looks_like_entity(query)
> if gated:
>     sys.stderr.write("wiki-graph gated OFF (entity-like query) -> Direct only, except superseded_by\n")
>     sup_added = expand_1hop(sims, meta, base_order, only_superseded=True)
>     order = base_order + sup_added
>     graph_set = set(sup_added)
> --- `src/sqlite_graph_memory/brain_ask.py`

> return (items[:head] + [items[head + p] for p in fused])[:topn]
> --- `src/sqlite_graph_memory/ppr.py`

#### RT-RTE-index-admission
Label: Caller-triggered index admission

Operator CLI or an importing caller triggers `build_index` over a directory. Note authors supply proposed text; deterministic enumeration, parsing and chunking admit it without per-content approval or truth review. Default encoder inference produces vectors; callers may inject an encoder. Guidance is the fixed chunk settings and inclusion rules, not an LLM editor prompt. The index stores vectors, a pickled list of text snippets/path/date/title metadata and a JSON manifest. No answer oracle is applied. Full rebuild, changed settings or corrupt/missing prior index/manifest trigger rebuilding; otherwise unchanged rows survive and missing files lose rows. SRC-1, `src/sqlite_graph_memory/index_notes.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counts of files, chunks and new texts, with CLI status text.
- Later read-back: Subsequent CLI/MCP/evaluator invocations load persisted matrix and metadata; snippets, not full original chunks, are delivered to recall consumers.
- Delegated visibility: Encoder receives passage-prefixed body chunks; model-cache fetching is delegated to the embedding stack, not another agent.
- Selection predicate: Recursive `*.md`, hidden components excluded unless configured, sync-conflict names always skipped; frontmatter removed; 1200-character windows with 200 overlap, minimum 40 characters; stored snippet first 600 characters.
- Invalidation or expiry: Rebuild drops rows for removed/changed files; same size/mtime fast path can reuse the stored hash without reading changed bytes. `--full` forces regeneration. No automatic scheduled refresh is implemented by this entry point.
- Activation or effect: Proposed file content becomes a future retrievable index entry. No human per-note veto, semantic rejection or gain test is in this writer.
- Evidence limits: Three successive artifact writes are not a transactional snapshot; explicit rollback is not supplied by `build_index`. Rebuilding is recovery, not a preserved previous version. Note authorship and deployment scheduling remain external.

> if not include_hidden and any(part.startswith('.') for part in rel.parts):
>     continue
> if CONFLICT_MARKER in p.name:
>     continue
> --- `src/sqlite_graph_memory/index_notes.py`

> np.save(emb_path, emb)
> meta_path.write_bytes(pickle.dumps(meta))
> manifest_path.write_text(json.dumps({'settings': settings, 'files': current_files}, indent=2),
>                          encoding='utf-8')
> --- `src/sqlite_graph_memory/index_notes.py`

#### RT-RTE-turnstate-capture
Label: Stop-hook transcript capture and viewer return

Once registered by the operator, the external host triggers the hook after a turn. Input event supplies session identity, transcript path and cwd; a fallback searches matching session files. Code selects a new transcript tail using a per-session temp offset. Symbolic parsers select the last real user ask, assistant text, tool names, commands, file paths and bilingual decision/TODO lines. Truncated fields and evidence path/byte range become a SQLite `turns` row. Proposed material is host transcript data; software extraction and SQL insertion admit it without model or human content approval. This is automatic recording under fixed parsing rules, with no answer oracle and no semantic revision proposal. The example registers `sgm-turnstate-hook`, whose console entry point calls `main` directly, bypassing the module/script wrapper. A valid event with meaningful new content reaches SQLite connection and insertion; an unavailable parent directory in `TURNSTATE_DB` can cause an uncaught storage exception after the offset has advanced. This does not establish how the external host handles that failure. SRC-1, `src/sqlite_graph_memory/turnstate_hook.py`, `src/sqlite_graph_memory/turnstate_show.py`, `pyproject.toml`, `examples/claude-code-stop-hook.json`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Successful hook calls and explicit early returns emit no output. The installed `sgm-turnstate-hook` calls `main` directly and can propagate storage exceptions; it does not inherit the module/script wrapper's catch and forced zero exit. Only running the module/script as main suppresses exceptions and exits zero. Viewer returns selected text or statistics to stdout.
- Later read-back: `sgm-turnstate-show` selects by optional session and descending id with a limit, then displays chronologically. Automatic delivery of ledger rows to recall/model context is not established by these modules.
- Delegated visibility: Host supplies transcript; no subagent or extraction-model invocation occurs in this parser. Viewer exposes only selected and further clipped fields, not complete evidence records.
- Selection predicate: Valid offset, gap at most 4 MiB, meaningful parsed content; ask/summary/commands/decisions clipped; tool-result-only noise may produce no row.
- Invalidation or expiry: Offset in temp storage advances even before SQLite persistence and may reset when missing/invalid; durable row expiry is not defined in the inspected writer/viewer.
- Activation or effect: Derived state survives for later ledger inspection, not demonstrated agent behavior change. Raw transcript remains a pointer target rather than a copied full source.
- Evidence limits: Recording is not exactly once or lossless; big gaps skip capture, failed writes can lose a slice, and missing offsets can allow reprocessing. Error suppression covers module/script invocation only, not the ordinary installed entry point. External host response to propagated errors is uninspected. No transactional offset/row rollback or per-session lock is provided here.

> write_offset(sid, fsize)                   # advance regardless, never re-process
> --- `src/sqlite_graph_memory/turnstate_hook.py`

> sgm-turnstate-hook = "sqlite_graph_memory.turnstate_hook:main"
> --- `pyproject.toml`

> "command": "sgm-turnstate-hook",
> --- `examples/claude-code-stop-hook.json`

> con = sqlite3.connect(db_path(), timeout=3.0)
> --- `src/sqlite_graph_memory/turnstate_hook.py`

> if __name__ == "__main__":
>     try:
>         main()
>     except Exception:
>         pass   # never break a session
>     sys.exit(0)
> --- `src/sqlite_graph_memory/turnstate_hook.py`

#### RT-RTE-evaluation-paths
Label: Gold and benchmark consumer policy composition

Evaluation is a bounded comparison mode chosen by a caller, not autonomous production optimization. `score_gold` consumes query/reference-note sets, calls shared retrieval functions and scores ranked stems. The caller provides reference outcomes through `g['gold']`; code supplies Recall/MRR/nDCG arithmetic. Ablation cells select hop limits, pool and gate settings; a caller chooses the grid, not the inference model. The benchmark adapter builds/reloads the index, always loads the cross-encoder and returns extractive answering with a fixed abstention rule. Maintainers judge changes; these evaluators do not install a selected successor. SRC-1, `eval/run_eval.py`, `eval/run_ablation.py`, `bench/adapters/sgm.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Per-query rankings/metrics or benchmark answer/citation objects, with summaries persisted by evaluator callers.
- Later read-back: Persisted metric outputs can inform later maintainer comparison; actual use of these outputs to decide a change is uninspected.
- Delegated visibility: Index-building subprocess in adapter setup; scoring uses numerical encoders/reranker, not a delegated reasoning agent.
- Selection predicate: `score_gold` always expands, irrespective of its recorded entity flag; ablation uses supersession-only expansion when gated; benchmark graph mode suppresses expansion entirely on gated entities. Adapter answer is selected through `best_sentence` and rejected when top reranker score is below 0.0 or sentence is absent.
- Invalidation or expiry: Scores are tied to supplied gold/config/index; source does not make all results estimates of the default MCP path. Re-running can compare configurations, but does not automatically revise the deployed code.
- Activation or effect: Returned ranks feed metric arithmetic or extractive answering; neither measurement wiring nor a nonempty result establishes task benefit.
- Evidence limits: Only selected implementation branches inspected; benchmark result files and their run conditions are not assessed here. Shared function imports do not prove identical composed policies.

> added = ba.expand_1hop(sims, meta, base, by_base)
> lists = {'vector': ba.rerank_candidates(ce, g['query'], base, meta, sims=sims)}
> --- `eval/run_eval.py`

> if self.mode == 'graph' and not (self.gate and ba.looks_like_entity(question)):
>     added = ba.expand_1hop(sims, self.meta, cand, self.by_base,
>                            ghops=self._ghops or ba.GHOPS, gmax=self._gmax or ba.GMAX)
>     self.graph_added += len(added)
>     cand = cand + added
> --- `bench/adapters/sgm.py`

#### RT-RTE-change-admission
Label: Contributor and release change admission

Contributors propose code, model, schema or instruction changes. `AGENTS.md` asks for a fixed gold file, before/after measurements and reverting class regressions worse than 0.01 nDCG; model/schema/framework decisions require human involvement. These are natural-language contributor rules, not gates inside recall. `.github/workflows/tests.yml` wires tests, a deliberately mutated metric negative check and wheel-install checks on configured events. Release publication/manual workflow dispatch triggers `.github/workflows/publish.yml`, which builds, checks strict metadata and executable presence, then publishes through OIDC and a `pypi` environment. External repository protections, environment approvals and PyPI trust registration determine actual admission authority and are not visible here. SRC-1, these files and `docs/RELEASING.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CI job results and built distributions, then a publication attempt and registry registration when downstream prerequisites pass.
- Later read-back: Published code/instructions can govern future installed invocations. No source-supplied execution establishes which build is live in any deployment.
- Delegated visibility: GitHub runners receive source and publication permissions; provider actions implement external build/publication machinery, not agent delegation.
- Selection predicate: Workflow step success gates downstream jobs; documented measurement/human review rules are not an automatic requirement of the inspected publisher. No production answer oracle selects the package version.
- Invalidation or expiry: Future releases can replace installed behavior only when consumers upgrade. Doctrine calls for reversion on retrieval regression; no automatic package rollback is wired in the publisher, which skips existing artifacts.
- Activation or effect: Mechanism affords and wires product/production admission. Human approval policy, exercised publication and later deployment effects are uninspected.
- Evidence limits: Static workflow definitions are not passing CI evidence. No claim that every possible repository admission path must use these jobs; branch protection and environment reviewer settings are external.

> A regression worse than 0.01 nDCG@12 on any class is a reason to revert, not to explain.
> --- `AGENTS.md`

> environment: pypi
> permissions:
>   id-token: write   # the whole point: OIDC instead of a stored token
> --- `.github/workflows/publish.yml`

### Claims

#### RT-CLM-scoped-return
Label: Scoped recall error containment

Claimed operation: isolate model-load failure in a child and return only the call's answer file on successful completion. Owner: MCP server. Enforcement points: `subprocess.run`, return-code check, scoped-file read and cleanup in `run_recall`. Guarantee strength: best effort for service continuity; invariant for the inspected successful-answer branch's use of its designated answer file rather than stdout. Required external contract: process creation/capture/timeout semantics, trusted child and artifacts, writable temp directory and MCP client handling of errors. Covered paths: three MCP modes and server direct-test wrapper. Alternate paths: bare CLI/direct-import callers do not receive this process envelope; JSON-RPC malformed nested shapes can raise outside `run_recall`, so universal server robustness is not established. SRC-1, `src/sqlite_graph_memory/mcp_server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> An empty answer file means no notes matched; stdout is never promoted to an answer
> because it carries startup notices, load reports, and tokenizer warnings.
> --- `src/sqlite_graph_memory/mcp_server.py`

> if res.returncode != 0:
>     err = (res.stderr or res.stdout or "").strip()
>     return f"Recall error (exit code {res.returncode}):\n{err}", True
> --- `src/sqlite_graph_memory/mcp_server.py`

#### RT-CLM-temporal-scope
Label: Temporal doctrine versus selected replacement access

The portable block requests closing rather than overwriting and preferring open records. The inspected indexer strips frontmatter from embedded text and stores date/title/path/snippet, not validity windows; normal recall ranks without `valid_to` filtering. It does parse `superseded_by` for the entity exception. Thus the package wires replacement access, not the block's entire temporal-answer policy. This is a scoped comparison of inspected code to doctrine, not an absence claim about an enclosing host or private pipeline. SRC-1, `BITEMPORAL.md`, `src/sqlite_graph_memory/index_notes.py`, `src/sqlite_graph_memory/brain_ask.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> When I recall, I prefer records whose `valid_to` is empty. A closed record is history:
> I may cite it only as "was true until <valid_to>", never as the current state.
> --- `BITEMPORAL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-context-delivery
Label: Retrieved snippet to host tool result

Consumer: enclosing MCP client's agent. Channel: textual `memory_recall` result containing formatted stored snippets. Force: advisory context/evidence at this package boundary, not enforced instructions or validated answers. Horizon: immediate host turn, potentially later turns if the host retains the result; the latter is uninspected. Code determines selection and delivery but has no demonstrated compliance or activation evidence. SRC-1, `src/sqlite_graph_memory/mcp_server.py`, `src/sqlite_graph_memory/brain_ask.py`.

> "content": [{"type": "text", "text": result_text}],
> "isError": is_error
> --- `src/sqlite_graph_memory/mcp_server.py`

#### RT-BAP-temporal-instructions
Label: Portable temporal block to external writer

Consumer: an external memory-writing/answering agent, only when an operator installs the block. Channel: copied agent instruction file or system prompt. Force: natural-language behavioral prescription, including reserving deletion for the owning human; enforcement and agent compliance are not established by publishing the text. Horizon: subsequent operations under that installed instruction version. The package does not itself run a model author under this block. No assessment of theory-building, reflection or learning follows merely from the supplied rules. SRC-1, `BITEMPORAL.md`.

> A block you can paste into an agent's instruction file (`CLAUDE.md`, `AGENTS.md`,
> `.cursor/rules`, a system prompt) so the agent stops overwriting what it knew and starts
> closing it instead.
> --- `BITEMPORAL.md`

## Annotations

none

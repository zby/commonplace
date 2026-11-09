---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "sqlite-graph-memory's note index, query-time graph selection, transcript ledger and distinct later consumers."
run-id: AAS-2026-11-08-sqlite-graph-memory-ca3785ec5c2e-01
source-identity: https://github.com/tonydzi/sqlite-graph-memory
reviewed-boundary: f05db2778159d50a0ad8a35be4f2be3a6aea94b1
---

# sqlite-graph-memory memory report

## Boundary and evidence

The memory scope is the public package's note-to-context path, Stop-hook ledger, operator inspection, shipped evaluation consumers and portable maintenance instructions. It is not the enclosing agent's conversation manager or the maintainer's private pipeline. The frozen source is SRC-1 in [boundary](boundary.md), revision `f05db2778159d50a0ad8a35be4f2be3a6aea94b1`. All findings below are static implementation or attributed doctrine. No target execution or independent retrieval-quality measurement was performed.

Direct reads covered `pyproject.toml`, `examples/README.md`, `examples/claude-code-stop-hook.json`, `BITEMPORAL.md`, `src/sqlite_graph_memory/index_notes.py`, `src/sqlite_graph_memory/brain_ask.py`, `src/sqlite_graph_memory/mcp_server.py`, `src/sqlite_graph_memory/ppr.py`, `src/sqlite_graph_memory/schema.sql`, `src/sqlite_graph_memory/turnstate_hook.py`, `src/sqlite_graph_memory/turnstate_show.py`, `src/sqlite_graph_memory/vault_stats.py`, `src/sqlite_graph_memory/doctor.py`, `bench/adapters/sgm.py` and `bench/adapters/_extract.py`. These add implementation coverage under the existing SRC-1, not a new source or observed run. Evaluation scoring, contributor/release admission and encoder internals below rely on the supplied runtime findings, not fresh inspection of those files. External note authors, host sessions, weights and private temporal-edge implementations remain outside the available evidence. Available tests, benchmark results and support documents not read here are uninspected, not absent.

| Entry point / operation | SRC-1 path and evidence basis | Coverage / prevented conclusion |
|---|---|---|
| `sgm-index`, imported `build_index` | `pyproject.toml`, `src/sqlite_graph_memory/index_notes.py`; direct implementation | [RT-RTE-index-admission](runtime.md#rt-rte-index-admission), [MEM-OBJ-notes](#mem-obj-notes), [MEM-OBJ-brain-e5](#mem-obj-brain-e5), [MEM-OBJ-brain-meta](#mem-obj-brain-meta), [MEM-OBJ-brain-manifest](#mem-obj-brain-manifest); initial content authorship/control unresolved |
| `sgm-ask`, exported retrieval helpers | `src/sqlite_graph_memory/brain_ask.py`; direct implementation | [RT-RTE-recall-options](runtime.md#rt-rte-recall-options); direct, graph, A/B, entity exception, pool and rerank paths; policy differs across callers |
| PPR alternate ordering/cache | `src/sqlite_graph_memory/ppr.py`; direct implementation | Annotation on [RT-RTE-recall-options](runtime.md#rt-rte-recall-options); in-memory graph, not SQL graph or persistent learned ranking |
| `sgm-mcp`, package-name alias, `--test`, registered `memory_recall` | `pyproject.toml`, `src/sqlite_graph_memory/mcp_server.py`; direct implementation | [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall), [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery); tool return established, host adoption uninspected |
| Stop event / `sgm-turnstate-hook` | `examples/claude-code-stop-hook.json`, `src/sqlite_graph_memory/turnstate_hook.py`; direct implementation/configuration | [RT-RTE-turnstate-capture](runtime.md#rt-rte-turnstate-capture), [MEM-OBJ-turns](#mem-obj-turns), [MEM-OBJ-turnstate-offset](#mem-obj-turnstate-offset); host installation/exercise not established |
| `sgm-turnstate-show`, session/recency/stats | `src/sqlite_graph_memory/turnstate_show.py`; direct implementation | Same capture-route annotation; retained rows reach a clipped operator display, not demonstrated model read-back |
| `sgm-stats`, `sgm-doctor` | `src/sqlite_graph_memory/vault_stats.py`, `src/sqlite_graph_memory/doctor.py`; direct implementation | [MEM-RTE-vault-health](#mem-rte-vault-health); measurements/advice do not automatically revise retained content |
| Gold evaluator / ablation | `eval/run_eval.py`, `eval/run_ablation.py`; supplied runtime only | [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths); reference sets and metrics are evaluator inputs/outputs, not recall policy updates |
| Benchmark index reload and answer layer | `bench/adapters/sgm.py`, `bench/adapters/_extract.py`; direct implementation | [MEM-OBJ-benchmark-raw](#mem-obj-benchmark-raw), annotation on [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths); independent full-body answer channel, not MCP snippet answering |
| Portable close/replace instructions | `BITEMPORAL.md`; direct doctrine | [RT-BAP-temporal-instructions](runtime.md#rt-bap-temporal-instructions), [RT-CLM-temporal-scope](runtime.md#rt-clm-temporal-scope); installation/compliance and complete temporal filtering unestablished |
| Contributor/evaluation/release gates | Supplied [RT-RTE-change-admission](runtime.md#rt-rte-change-admission) | Product revisions are distinct from index admission; actual human decisions/publication not inspected |

## Core ideas

1. The durable knowledge channel is a derived index over external Markdown, not a SQLite knowledge graph. Text snippets and vectors persist in separate files; SQL holds a transcript ledger and A/B counters. Graph edges are read from current notes. This mixes current links with potentially older indexed text, rather than making one synchronized snapshot ([MEM-OBJ-notes](#mem-obj-notes), [MEM-OBJ-brain-meta](#mem-obj-brain-meta), [MEM-OBJ-ab-recall](#mem-obj-ab-recall)).
2. Request-driven recall selects rather than summarizes. Dense scoring chooses one best chunk per file; link expansion adds already-indexed neighbors; optional numerical ordering changes ranks. Only the stored first 600 characters of a selected chunk reach the ordinary bundle, despite embedding up to 1200 characters. Ranking relevance therefore does not establish that the supporting part of the chunk reaches the host ([RT-RTE-index-admission](runtime.md#rt-rte-index-admission), [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall)).
3. The transcript hook automatically derives records from usage, but the visible later consumer is a ledger viewer. Neither retaining a line labelled a decision nor displaying it establishes adoption as future instructions. The package's ordinary recall path loads the note index, not the `turns` rows ([MEM-OBJ-turns](#mem-obj-turns), [RT-RTE-turnstate-capture](runtime.md#rt-rte-turnstate-capture)).
4. Closing a wrong record with a reason is prescribed in natural language. Indexed frontmatter removal and non-temporal ranking do not implement that full prescription. Supersession adds a possible replacement; it neither withdraws the old snippet nor guarantees delivery of the reason ([RT-CLM-temporal-scope](runtime.md#rt-clm-temporal-scope)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-notes
Label: Markdown notes and live links

Source-native identity: the `*.md` files under the caller's notes directory. Storage: filesystem Markdown. Body prose is natural-language material; frontmatter date/replacement fields, paths and parsed wikilink targets have symbolic consumption paths. The body may itself contain instructions, but retrieval does not distinguish trusted instructions from other text. Original authorship and trace provenance are external/unresolved; indexing a corpus does not imply human approval of every note. The indexer derives chunks and strips frontmatter. Query expansion separately rereads source paths; it uses live outgoing links to select indexed chunks, not full current neighbor text. The metadata path is a pointer, not retained source bytes or a verified source version. Distinct from the supplied index-admission and recall route records: this object is their original content substrate, not their progression. SRC-1, `src/sqlite_graph_memory/index_notes.py`, `src/sqlite_graph_memory/brain_ask.py`.

> body = t[m.end():] if m else t
> --- `src/sqlite_graph_memory/index_notes.py`

> try: t = Path(path).read_text(encoding='utf-8', errors='ignore')
> except Exception: return []
> t = FENCED_CODE_RX.sub('', t)
> t = INLINE_CODE_RX.sub('', t)
> return [m.strip() for m in WIKILINK_RX.findall(t)]
> --- `src/sqlite_graph_memory/brain_ask.py`

#### MEM-OBJ-brain-e5
Label: _brain_e5 embedding matrix

Source-native identity: `_brain_e5.npy`; float32 numerical chunk vectors on disk, distributed-parametric representational form, consumed by matrix multiplication against a query vector. Produced from `passage: ` plus body windows by the encoder; injected encoders are also supported, so provenance is not universally the default model. Vectors encode content for numerical selection, not readable reasons. Index updates replace or preserve rows; recall/evaluators reload them. The matrix shapes selection but is not executable instruction authority. It differs from [RT-CMP-e5-model](runtime.md#rt-cmp-e5-model): output representations, not encoder weights. Model pinning/update limits are in that component record. Closest supplied route is [RT-RTE-index-admission](runtime.md#rt-rte-index-admission), not an object duplicate. SRC-1, `src/sqlite_graph_memory/index_notes.py`, `src/sqlite_graph_memory/brain_ask.py`.

> return emb @ qv
> --- `src/sqlite_graph_memory/brain_ask.py`

#### MEM-OBJ-brain-meta
Label: _brain_e5_meta text and access metadata

Source-native identity: `_brain_e5_meta.pkl`, a pickled list aligned with matrix rows. Its natural-language part is a truncated body snippet; symbolic access/display fields are path, title from filename stem and frontmatter date. These parts have different consumers: snippets feed optional cross-encoder scoring and host context; paths control graph filesystem access and file deduplication; date/title format the display. No source hash or byte-span field is written into a chunk record. Reasons inside a body survive only if within the stored prefix; the metadata does not independently retain correction rationale or validity windows. The loader trusts pickle deserialization, so deployment must trust the index artifact, not merely distrust its prose. This object is distinct from its writer [RT-RTE-index-admission](runtime.md#rt-rte-index-admission) and reader [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall); no supplied object counterpart. SRC-1, `src/sqlite_graph_memory/index_notes.py`, `src/sqlite_graph_memory/brain_ask.py`.

> meta.append({'path': str(p), 'title': title,
>              'snippet': c[:SNIPPET_CHARS], 'date': date})
> texts.append('passage: ' + c)     # e5 expects the passage: prefix
> --- `src/sqlite_graph_memory/index_notes.py`

> meta = pickle.loads(Path(meta_path or META).read_bytes())
> --- `src/sqlite_graph_memory/brain_ask.py`

#### MEM-OBJ-brain-manifest
Label: _brain_e5_manifest freshness metadata

Source-native identity: `_brain_e5_manifest.json`; symbolic JSON on disk, storing settings plus per-path size/mtime/hash. Lineage: filesystem stat, conditional SHA-256 and fixed settings. Consumer: the next `build_index`, not the host model. Authority: governs reuse versus regeneration of vectors/snippets; it is access/maintenance metadata, not note knowledge. Same-size/mtime reuse trusts a previous nonempty hash rather than rereading the file. Changing a model's downloaded bytes without changing its configured name is not represented in the settings fingerprint. This object refines persistence facts of [RT-RTE-index-admission](runtime.md#rt-rte-index-admission), not a duplicate route. SRC-1, `src/sqlite_graph_memory/index_notes.py`.

> return {'E5_MODEL': E5_MODEL, 'CHUNK_CHARS': CHUNK_CHARS,
>         'CHUNK_OVERLAP': CHUNK_OVERLAP, 'SNIPPET_CHARS': SNIPPET_CHARS}
> --- `src/sqlite_graph_memory/index_notes.py`

#### MEM-OBJ-turns
Label: TurnState derived rows

Source-native identity: SQLite `turns`. Mixed representation: natural-language ask/assistant text/decision lines, symbolic JSON tool/file/command lists and session/time/project/evidence metadata. Its producer reads host JSONL: last accepted user text, concatenated assistant text, tool-use inputs and regex matches. `summary` is concatenation then clipping, not an abstractive model summary or verified account of actions. Commands/tool names record attempted calls, not demonstrated tool success. Raw tool results are not a separately retained outcome record here. The raw transcript is an external file named by `evidence` and byte range, not copied into this table. Preserving that pointer does not preserve readable evidence when the file disappears.

Admission is automatic deterministic extraction once registered; no per-row human or model approval. Ask is capped at 500 characters, assistant summary at 1200, commands at 20 of 200 characters, unique decisions at 10. The later viewer omits evidence/byte spans in its SELECT and further clips text. Thus it does not automatically show the record's reasons or complete provenance. Consumer authority is operator information; no observed future agent activation. This is the retained object of [RT-RTE-turnstate-capture](runtime.md#rt-rte-turnstate-capture), not a second declaration of that route. SRC-1, `src/sqlite_graph_memory/turnstate_hook.py`, `src/sqlite_graph_memory/turnstate_show.py`.

> summary = "\n".join(summary_parts).strip()
> --- `src/sqlite_graph_memory/turnstate_hook.py`

> q = ("select ts,project,ask,summary,files,tools,commands,decisions,session_id "
>      "from turns ")
> --- `src/sqlite_graph_memory/turnstate_show.py`

#### MEM-OBJ-turnstate-offset
Label: Per-session transcript offset

Source-native identity: sanitized session-specific `claude-turnstate-*.off` file in the temporary directory. Symbolic integer control metadata, not knowledge text. Producer is the hook; the next hook reads it to decide which transcript slice to omit. Missing/invalid/out-of-range offsets reset to zero; gaps greater than 4 MiB are skipped with advancement. Advancement precedes semantic extraction and SQL commit. Consequently this ephemeral checkpoint can outlive a failed insertion or disappear before the next hook, producing loss or reprocessing. It is a distinct control object from the durable row, even though both participate in [RT-RTE-turnstate-capture](runtime.md#rt-rte-turnstate-capture). SRC-1, `src/sqlite_graph_memory/turnstate_hook.py`.

> write_offset(sid, fsize)                   # advance regardless, never re-process
> --- `src/sqlite_graph_memory/turnstate_hook.py`

#### MEM-OBJ-ab-recall
Label: A/B recall telemetry

Source-native identity: SQLite `ab_recall` plus optional `BRAIN_AB_JSON` file. SQL retains symbolic counters, timestamp/query/source label and truncated promoted-title text. Optional JSON retains two ranked lists, scores, graph/new flags and snippet prefixes up to 200 characters. Produced automatically by `--ab`; database/JSON write exceptions are swallowed. No oracle labels correctness, and `source` is an environment label rather than verified trace origin. A/B compares retrieval lists, not demonstrated answer quality. This material is for immediate comparison and afforded external inspection; the inspected selector does not read the accumulated table to revise itself. Neither a dashboard consumer nor autonomous policy revision is wired in the read paths inspected here. Distinct from [RT-RTE-recall-options](runtime.md#rt-rte-recall-options), which owns its production route. SRC-1, `src/sqlite_graph_memory/brain_ask.py`, `src/sqlite_graph_memory/schema.sql`.

> 'snippet': meta[i].get('snippet', '')[:200],
> --- `src/sqlite_graph_memory/brain_ask.py`

#### MEM-OBJ-benchmark-raw
Label: Benchmark raw-note map

Source-native identity: adapter `self.raw`, an in-process dictionary populated from top-level vault `*.md` files. Natural-language note bodies retain full file text in RAM; lowercase stems are symbolic keys. Unlike the persistent snippet index, this is setup-time working state, not a new accumulated memory store. The extractor strips frontmatter, ignores heading/blank lines, splits normalized sentences and chooses the greatest positive content-word overlap among the first three ranked note IDs. It may therefore answer from text beyond the indexed snippet. The answer layer consumes actual prose with a fixed symbolic rule, not a model reader. Duplicate stems collapse under the dictionary key and nested notes are not loaded by this glob; this limits answer coverage even if the recursive index retrieves them. This is distinct from [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths), its enclosing evaluator route, and from production MCP delivery. SRC-1, `bench/adapters/sgm.py`, `bench/adapters/_extract.py`.

> self.raw = {p.stem.lower(): p.read_text(encoding='utf-8') for p in Path(vault_dir).glob('*.md')}
> --- `bench/adapters/sgm.py`

> for nid in ranked_ids[:depth]:
>     for s in sentences(read_note(nid)):
>         ov = len(qt & tokens(s))
>         if ov > best[2]:
>             best = (nid, s, ov)
> --- `bench/adapters/_extract.py`

### Routes

#### MEM-RTE-vault-health
Label: Operator memory-health inspection

The caller triggers `sgm-stats` on a notes directory or `sgm-doctor` on its environment/index configuration. Deterministic code computes graph/date metrics or checks dependency/cache/index presence, then emits a report. No model author, answer oracle or automated content successor is involved. A human may choose to act on the output, but this route does not implement that subsequent admission. Distinct from [RT-RTE-index-admission](runtime.md#rt-rte-index-admission): diagnostic reading, not note/index mutation. SRC-1, `src/sqlite_graph_memory/vault_stats.py`, `src/sqlite_graph_memory/doctor.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Text or JSON vault metrics with verdict/exit code; doctor returns checks and repair advice.
- Later read-back: Notes are re-inspected by stats; doctor checks index/model-cache presence. Neither stores a history or loads a prior diagnostic report here.
- Delegated visibility: inapplicable — these paths inspect local state without a delegated agent.
- Selection predicate: Stats uses note filters and live links, path-based graph nodes, and concept date/type/folder rules; doctor uses environment/default paths and dependency availability.
- Invalidation or expiry: Reports are invocation-local; no persistent diagnostic checkpoint or content expiry is imposed.
- Activation or effect: Computed verdict changes stdout/exit status, not the note corpus, ranking policy or model context.
- Evidence limits: A health threshold is not a semantic truth/admission test; doctor presence checks do not establish index integrity or successful recall.

> print(json.dumps(report, indent=2, ensure_ascii=False) if a.json else render(report))
> return report['exit_code']
> --- `src/sqlite_graph_memory/vault_stats.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-index-admission](runtime.md#rt-rte-index-admission)

Storage and lineage split across [MEM-OBJ-brain-e5](#mem-obj-brain-e5), [MEM-OBJ-brain-meta](#mem-obj-brain-meta) and [MEM-OBJ-brain-manifest](#mem-obj-brain-manifest). Unchanged rows persist; deletion/change removes previous rows during rebuild, rather than retaining a versioned reason for withdrawal. Chunking is deterministic curation, not claim validation. Rebuild can restore an index from existing notes but cannot recover overwritten source facts. An explicitly supplied encoder's provenance/control remains the importing caller's responsibility (SRC-1, `src/sqlite_graph_memory/index_notes.py`; supplied route quotation supports three successive writes).

#### On [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall)

Read-back is requested by the host's query, not independently pushed. Code chooses content using query vectors, persisted chunks and optionally current links/numerical reranking. The budget is counts and characters, not an enforced host token-window limit: default pool 60 files, graph seeds 15, additions 40, ranked 12, bundle 8 snippets. Deduplication removes other chunks even when another part of a note could matter. The temporary answer file is a delivery artifact deleted after return, not a conversational checkpoint. Backend warning text can precede the bundle. The actual host receives title/date/score/snippet, not full source text, source hashes or all retrieval candidates (SRC-1, `src/sqlite_graph_memory/brain_ask.py`, `src/sqlite_graph_memory/mcp_server.py`; supplied route quotes support the eight-item cut and environment setup).

#### On [RT-RTE-recall-options](runtime.md#rt-rte-recall-options)

Additional selection limit: PPR does not implement the same target resolution as 1-hop expansion. Its file-stem nodes merge same-named files; edge lookup uses raw stripped/lowercased target against those stems, so folder-qualified and `.md` targets accepted by 1-hop resolution need not resolve in PPR. Cache fingerprints use path and optional `sha`, but the indexer emits no `sha` field. With unchanged path/row layout, content edits can leave a long-lived process using an old graph. This is a transient derived selector, not persistent knowledge or learned parameters. MCP's per-query child limits cache horizon to that child; importing consumers can retain it across queries. SRC-1, `src/sqlite_graph_memory/ppr.py`, `src/sqlite_graph_memory/index_notes.py`, `src/sqlite_graph_memory/brain_ask.py`.

> v = idx.get(tgt.strip().lower())
> --- `src/sqlite_graph_memory/ppr.py`

> h.update(str(m.get('sha', '')).encode('utf-8', 'replace'))
> --- `src/sqlite_graph_memory/ppr.py`

#### On [RT-RTE-turnstate-capture](runtime.md#rt-rte-turnstate-capture)

Trace-fed update chain: external host user/assistant/tool-use JSONL → deterministic parse/regex/dedup/clip → [MEM-OBJ-turns](#mem-obj-turns) → viewer stdout. It preserves fragments and source pointers, not a learned method or model-generated judgment. Later behavior-shaping use is not wired by these modules. The viewer shows ask 160, summary 200, six file basenames, twelve tools, first command prefix and six decision lines; full evidence pointers and byte spans do not cross this display boundary. Session/recency are selection predicates, not semantic targeting. The hook's fallback database can be a temp-path DB, whereas the viewer defaults only to the home-path DB: without matching `TURNSTATE_DB`, fallback persistence may not be seen by the default viewer. SRC-1, `src/sqlite_graph_memory/turnstate_hook.py`, `src/sqlite_graph_memory/turnstate_show.py`.

> print("💬 summary: %s" % summary.replace("\n", " ")[:200])
> --- `src/sqlite_graph_memory/turnstate_show.py`

#### On [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths)

The benchmark has a second text read channel through [MEM-OBJ-benchmark-raw](#mem-obj-benchmark-raw); answering is not limited to indexed snippets. Its rejection rule checks the top reranker score and whether any overlap-selected sentence exists. This does not validate that sentence's truth, temporal currency or relationship to the top scoring chunk. Gold metrics/ablation outputs described by the supplied runtime can inform maintainer decisions; inspected package recall does not automatically ingest them as knowledge or policy. SRC-1, `bench/adapters/sgm.py`, `bench/adapters/_extract.py`; gold/ablation details remain supplied-runtime evidence.

#### On [RT-BAP-temporal-instructions](runtime.md#rt-bap-temporal-instructions)

Write agency is explicitly an instructed external agent; deletion is reserved for a human. Installation is human/operator control over the instruction block, not proof of per-fact approval. Content-directed correction is prescribed as closing and replacing while retaining a reason; later reason consumption is not guaranteed by snippet truncation or the ledger viewer. There is no package-run author under this block. SRC-1, `BITEMPORAL.md`.

> A wrong record is closed the same way, with a one-line reason, not erased. The
>    history of a mistake is part of the memory.
> --- `BITEMPORAL.md`

## Write side

Admission and authorship must be kept separate:

| Mechanism | Proposed material / author | Actual admission and veto | Retention / rejection / recovery |
|---|---|---|---|
| Notes to index | Existing caller-selected Markdown; original author/human involvement unresolved | Caller starts indexer; software filters files, strips frontmatter, chunks and embeds. No per-note truth or human-approval gate | [RT-RTE-index-admission](runtime.md#rt-rte-index-admission): changed/removed files lose old rows; full rebuild is recovery, not rollback history |
| Transcript to ledger | Host transcript, including user and assistant text and attempted tool-use inputs | Installed Stop hook plus deterministic parser; no per-row semantic veto. Empty/noisy slices and oversized gaps are rejected/skipped | [MEM-OBJ-turns](#mem-obj-turns), [MEM-OBJ-turnstate-offset](#mem-obj-turnstate-offset): clipping and independent offset checkpoint can lose information; no retained alternative summary form |
| Recall to A/B log | User query and two computed rankings | Software appends counters/optional JSON; no oracle or human per-query approval | [MEM-OBJ-ab-recall](#mem-obj-ab-recall): write errors swallowed; no selector feedback update |
| Portable note correction | External instructed writer | Doctrine says close/replace, retain reason, reserve deletion to owner; compliance/enforcement unresolved | [RT-BAP-temporal-instructions](runtime.md#rt-bap-temporal-instructions): history preservation is requested, not ensured by index rebuild |
| Benchmark answer | Extractor over setup-time raw notes | Top score and sentence-presence rejection; no human approval per answer | [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths): evaluation answer does not revise memory |
| Package/model/schema changes | Contributor proposal | Supplied contributor doctrine and release machinery, not indexer admission | [RT-RTE-change-admission](runtime.md#rt-rte-change-admission): maintained/published product, no inspected automatic metric-to-policy update |

The known transformations remain meaningful despite unresolved original note provenance. Index chunking, clipping, row reuse and withdrawal are implemented. They do not critique claims. A trace-derived ledger row is a derived trace; no later behavior-determining artifact update is established merely by labelling assistant lines decisions. No improvement in future capacity is demonstrated by these write paths. These are scoped limits on the inspected chains, not a claim that external agents cannot learn from them.

## Read-back

Ordinary memory read-back is note-derived state reloaded for a later CLI/MCP query. The request supplies semantic targeting; code and optional models choose retained material. Delivery is a textual tool result, advisory at this package boundary ([RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery)). Static maintenance instructions are a different, operator-installed instruction channel; they are not usage-accumulated read-back.

Ledger read-back is session/recency inspection, with additional losses at display. It is not evidence of unsolicited injection. A/B SQL/JSON supplies comparison artifacts with no inspected automatic later policy consumer. Evaluators consume index state and reference outcomes; the benchmark additionally reads whole-note working copies. These routes must not be collapsed into the production snippet path.

Working-context control here means keeping most external material out through retrieval, best-chunk deduplication and bounded presentation. It does not mean trimming accumulated host turns. The MCP child has process isolation, not a separate model reasoning frame; only its return text crosses back. The stack-frame analogy fits child lifetime but does not establish agent-frame/compaction behavior. Material not delivered remains in the persistent index or external notes and can be selected by a later query. There is no package-enforced host-context liveness rule or token budget. SRC-1, `src/sqlite_graph_memory/brain_ask.py`, `src/sqlite_graph_memory/mcp_server.py`; [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall).

## Integration issues

- No correction to a supplied runtime fact is required. The added PPR target-resolution distinction qualifies any later assertion that all graph selectors share one graph: [RT-RTE-recall-options](runtime.md#rt-rte-recall-options), SRC-1 `src/sqlite_graph_memory/ppr.py` versus `src/sqlite_graph_memory/brain_ask.py`. PPR merges stems and does not normalize targets like 1-hop expansion.
- No new declaration is intended as a duplicate of a supplied record. Objects describe substrates/results absent from runtime's object section; existing routes and authority paths receive annotations. [MEM-RTE-vault-health](#mem-rte-vault-health) adds diagnostic readers, not a replacement index-admission route.
- Initial note provenance, human per-content control and deployment refresh scheduling remain unresolved for [MEM-OBJ-notes](#mem-obj-notes) and [RT-RTE-index-admission](runtime.md#rt-rte-index-admission). Generic CLI authorship cannot settle them; this prevents attributing a universal human-curated or trace-derived corpus.
- Actual host consumption/compliance is uninspected for [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery) and [RT-BAP-temporal-instructions](runtime.md#rt-bap-temporal-instructions). The distinction prevents inferring exercised learning or temporal-answer guarantees from delivery/doctrine alone.
- [MEM-OBJ-turns](#mem-obj-turns) and [MEM-OBJ-turnstate-offset](#mem-obj-turnstate-offset) establish retention plus display, not future model adoption. No source-supplied session trace is available to close that integration question. Raw evidence retention depends on an external transcript path; the viewer does not expose the stored evidence fields.
- Configuration can separate the ledger, telemetry and viewer even though schema comments describe one file: hook defaults to home storage with a temp fallback, recall A/B defaults to cwd `turnstate.db`, viewer defaults to home storage. Shared `TURNSTATE_DB` can align them. This qualifies a single-database deployment assumption, not the table schemas ([MEM-OBJ-ab-recall](#mem-obj-ab-recall), [RT-RTE-turnstate-capture](runtime.md#rt-rte-turnstate-capture); SRC-1 `src/sqlite_graph_memory/brain_ask.py`, `src/sqlite_graph_memory/turnstate_hook.py`, `src/sqlite_graph_memory/turnstate_show.py`).
- Evaluation result artifacts, their identity/configuration and later maintainer adoption were not inspected. [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths) supports evaluator wiring, not observed gains or policy learning. The full-body benchmark channel additionally prevents treating its answer scores as direct measurements of MCP snippet delivery.

## Limitations and checks

The source identity/revision was rechecked with `git rev-parse HEAD` at the supplied frozen checkout and equals the boundary pin. All direct evidence is same-pin source text; no new source, test execution, model invocation or installation was introduced. Public instructions are attributed prescriptions. No private ledger/vault, host session, downloaded weight bytes, causal experiment or successful deployment is supplied. These limits prevent claims of lossless capture, exercised automatic memory adoption, complete temporal truth filtering or improved agent capability.

Deterministic validation: the prepared worktree's role-specific `commonplace-validate` check passed. This establishes form, links and quotation occurrence, not semantic acceptance or demonstrated benefit.

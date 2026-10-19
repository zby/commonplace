---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "LLM-Wiki-v3 runtime baseline: extraction, curated admission, index-backed retrieval and evaluation at the frozen source revision."
run-id: AAS-2026-10-18-llm-wiki-v3-0c553a3118eb-01
reviewed-boundary: "267541db838cbca757a112bd0cfa47fa61eb5fb2"
---

# LLM-Wiki-v3 runtime report

## Runtime account

### Boundary and execution basis

The target is a Markdown knowledge system, not a general agent executor. The shipped `wiki` console script invokes a Typer CLI. Its consequential paths ingest source documents, stage extracted pages, move reviewed pages into registered namespace directories, rebuild indexes, return ranked identifiers and provenance, and evaluate retrieval or ingestion. The seed script is another retained-page producer. MCP serving and downstream answer generation are not supplied by the inspected CLI; the boundary already distinguishes intent from implementation ([boundary](boundary.md#boundary-and-evidence); SRC-1, `pyproject.toml`, `src/wiki/cli/__init__.py`).

All findings below concern inspected implementation or declared guidance at SRC-1. No target code, provider, test, seed driver or evaluation was executed. Actual model compliance, deployed isolation, activation of returned context and benefit remain unobserved. Added implementation coverage includes complete reads of `src/wiki/retrieve/{bm25,dense,graph,rerank}.py` (the individual paths are cited in their records), `src/wiki/ingest/chunk.py`, `src/wiki/ingest/diff.py`, `src/wiki/ingest/spancheck.py`, `src/wiki/audit.py` and `src/wiki/eval/harness.py`. The seed driver inspection here covers its imports/source declarations and complete `main`; hand-authored page specifications were not individually audited. These are implementation evidence, not an expanded source register.

### Ordinary operator invocation

An operator runs `wiki ingest <source>`. CLI path validation requires a readable file. Root discovery supplies the wiki root; the CLI constructs cheap and escalation Anthropic extractors. The pipeline hashes and stores original bytes, decodes retained text as UTF-8, splits it into overlapping chunks and processes chunks sequentially. Each call receives the root `AGENTS.md` as instructions plus source identity/offset instructions and one chunk as the user message. It does not receive the existing knowledge corpus. The provider is requested to return a `propose_pages` tool result, not to execute filesystem tools. Code owns the next step after every response ([RT-RTE-source-ingest](#rt-rte-source-ingest)).

The provider proposes localized page fields, bodies and supporting quotes. Code locates quotes in the full raw text, builds provenance, runs schema/footnote and token-overlap checks, and retries a chunk on the stronger model if no nonempty all-valid page set was returned. The retry receives the same chunk/instructions, not an explicit critique of the first response. The pipeline retains the last attempt's pages if no all-valid set is found. It deduplicates by ID, labels new versus patch, stages only valid pages, and writes a manifest. “Accepted” in that manifest means staged, not admitted to knowledge. The terminal CLI output reports staged and rejected IDs and issues (SRC-1, `src/wiki/ingest/pipeline.py`, `src/wiki/cli/__init__.py`).

A subsequent `wiki review` displays at most the first 800 characters, optionally opens an external editor, and prompts accept/reject/skip/quit. Acceptance moves the file into the directory selected by its current type and the namespace registry, then optionally stages and commits that destination. Rejection deletes the pending page. The model does not decide this CLI admission; a callable primitive can also be used without that interactive decision. Later `wiki rebuild` loads retained pages and rebuilds the three index families; `wiki query` retrieves identifiers, scores, component paths and source IDs. It neither emits page bodies nor compiles a downstream prompt ([RT-RTE-page-review](#rt-rte-page-review), [RT-RTE-index-query](#rt-rte-index-query)).

### Forcing cases and guarantee coverage

Four forcing cases bound the ordinary account. They are source traces, not executed probes.

1. **Uncited text versus a bad cited claim.** The validator iterates existing citation markers; the overlap checker likewise iterates extracted marked claims. Neither enumerates all substantive uncited sentences. Bad marked claims can fail overlap, but an unmarked body is not rejected by those body loops. Thus provenance is a requested extraction policy plus partial software enforcement, not a semantic truth invariant ([RT-CLM-provenance-policy](#rt-clm-provenance-policy)).
2. **Edited or directly accepted pending content.** CLI `--edit` is followed directly by the decision prompt. `accept_page` reparses type and checks registry membership but does not call schema or span validation. Its public `commit=False` argument is reachable from the shipped CLI `--no-commit`. Even when a Git hook is installed, that hook calls structural validation, not the span checker, and runs after the file move. A uniform revalidation-on-admission claim would be false ([RT-RTE-page-review](#rt-rte-page-review)).
3. **Same-ID replacement and curated seed.** Ingest diffing flags a changed existing body but does not veto it. Review uses `Path.replace`, so a same-name destination is replaced; it does not implement the instruction's automatic old-page retention or reciprocal supersession update. The seed driver directly writes validated pages, bypassing pending/review entirely. Its author curated the content, but starting the script is not per-page interactive approval ([RT-RTE-curated-seed](#rt-rte-curated-seed), [RT-CLM-history-policy](#rt-clm-history-policy)).
4. **Fresh page filter versus stale index output.** `load_pages` excludes superseded pages by default. Rebuild uses that filter, but query's ordinary fused return does not restrict IDs to the fresh page dictionary. A stale BM25/graph/dense result can therefore remain an output ID with empty provenance; the optional active rerank branch filters candidate IDs first. Also, graph edges may name missing targets. The supported CLI can select rerank, but dependency absence returns to the unfiltered fused branch. There is no query-wide current-page exclusion guarantee ([RT-RTE-index-query](#rt-rte-index-query)).

The provenance policy's owner is the extractor prompt; its software enforcement points are quote location, schema validation and marked-claim overlap. Guarantee strength: best effort. Its external contracts are faithful model output, accurate source text and compatible parsing/fuzzy-match libraries. The code establishes wiring, not complete semantic entailment or truth.

- provenance implementation conclusion status: wired
- provenance operation conclusion status: uninspected

The cost guard's owner is the ingest pipeline. Its enforcement point is cumulative configured-price accounting **after** a model response and before validating its pages. Guarantee strength: invariant for raising once that computed total exceeds the ceiling on this path, not an invariant on actual provider charges. It covers pipeline extractor calls, including escalation; direct `AnthropicExtractor.extract` and query-bootstrap calls do not pass through it. Unknown model names price at zero. External billing and actual usage accounting remain provider contracts (SRC-1, `src/wiki/config.py`, `src/wiki/ingest/pipeline.py`, `src/wiki/extract.py`, `src/wiki/cli/__init__.py`).

> usage.add(res)
> if usage.cost_usd > INGEST_COST_CEILING_USD:
> --- `src/wiki/ingest/pipeline.py`

> pin, pout = MODEL_PRICING.get(model, (0.0, 0.0))
> --- `src/wiki/config.py`

- cost-guard implementation conclusion status: wired
- cost-guard operation conclusion status: uninspected

Human admission is a protocol of the interactive review path, not an authorization boundary around all writes. The CLI operator can edit, reject, skip or quit; library callers and the curated seed driver have other paths. Filesystem permissions, provider credentials and optional Git hooks are deployment responsibilities. The source supplies no evidence of a deployed sandbox. The extraction call's capability surface is one structured proposal schema; its current request grants that tool shape only, not a shell. Separately, the host Python process writes raw/pending/knowledge/index/evaluation/audit files and can launch the editor and Git subprocesses. Do not collapse these host capabilities into model tool grants (SRC-1, `src/wiki/extract.py`, `src/wiki/review.py`, `src/wiki/cli/__init__.py`, `scripts/seed_corpus.py`).

### Coordination, recovery and working context

There is no multiworker scheduler in these inspected loops: Python sequences chunks, page decisions and component builds. Provider calls return structured values to that executor. Chunking limits each model invocation's source content, retaining an overlap tail; each call starts a fresh messages list rather than accumulating a conversation. Whole source text remains in raw storage and host memory for quote location. There is no model-call reload tool in this route. Escalation reconstructs the same selected input in a new call. This resembles a per-chunk frame whose result escapes into pages, but not addressable heap references inside the model window (SRC-1, `src/wiki/ingest/chunk.py`, `src/wiki/extract.py`, `src/wiki/ingest/pipeline.py`).

Audit contexts append success/failure, elapsed time and supplied usage fields and rethrow exceptions. Raw storage occurs before the ingest audit context; review moves before its audit context. Index builds unlink and recreate component databases independently; no cross-component transaction or failure rollback appears in those builders. Consequently a failed commit, later seed page failure or interrupted rebuild need not undo prior filesystem effects. Git can preserve accepted history when committing succeeds; it is not automatic transactional recovery. No run trace establishes exercised recovery (SRC-1, `src/wiki/audit.py`, `src/wiki/ingest/pipeline.py`, `src/wiki/review.py`, `src/wiki/retrieve/rebuild.py`, `src/wiki/retrieve/bm25.py`, `src/wiki/retrieve/dense.py`, `src/wiki/retrieve/graph.py`, `scripts/seed_corpus.py`).

Evaluation is an operator-invoked measurement route, not an automatic product promotion gate. Dataset expected IDs are its answer oracle. Component comparison explicitly reports only; query bootstrap writes candidates for human review and merge. No inspected path takes those measurements and automatically revises models, instructions, code or retained page assertions ([RT-RTE-eval-report](#rt-rte-eval-report), [RT-RTE-query-bootstrap](#rt-rte-query-bootstrap)). This is a scoped account of these consumers, not a claim about inaccessible provider learning or all possible manual development.

## Shared records

### Components

#### RT-CMP-haiku-extractor
Label: Cheap Anthropic extraction model

Source-native identity: `CHEAP_MODEL = "claude-haiku-4-5-20251001"`. Distributed-parametric model accessed through the Anthropic service; parameters are on provider infrastructure, not stored by this repository. Used in extraction and candidate query generation. No parameter-update operation appears in these call sites. A date-bearing model identifier is configured, but exact weights/service implementation are not frozen in SRC-1; whether the endpoint can be remapped by the provider is uninspected. Caller-supplied extractor models are also supported. Evidence: SRC-1, `src/wiki/config.py`, `src/wiki/extract.py`, `src/wiki/cli/__init__.py`.

> CHEAP_MODEL = "claude-haiku-4-5-20251001"
> --- `src/wiki/config.py`

#### RT-CMP-sonnet-extractor
Label: Escalation Anthropic extraction model

Source-native identity: `ESCALATE_MODEL = "claude-sonnet-4-6"`. Distributed-parametric model on provider infrastructure. The CLI uses it as the second extractor, not as a persistent autonomous critic. No local parameter mutation is wired. The alias has no exact weight digest or dated version in this source; provider remapping remains possible under an external service contract, not observed here. Evidence: SRC-1, `src/wiki/config.py`, `src/wiki/ingest/pipeline.py`, `src/wiki/cli/__init__.py`.

> ESCALATE_MODEL = "claude-sonnet-4-6"
> --- `src/wiki/config.py`

#### RT-CMP-dense-embedding
Label: Optional BGE embedding model

Source-native identity: `BAAI/bge-small-en-v1.5`, loaded through fastembed into a module singleton. Distributed-parametric model, external model cache/runtime substrate; derived page vectors are numerical blobs in `indexes/vectors.sqlite`. There is embedding inference, not weight training, in the inspected implementation. Model name is pinned as a string but no artifact revision/digest is passed to the loader. There is no remote inference endpoint here; resolution of that name to downloaded artifacts belongs to fastembed and is uninspected. Rebuilding vectors changes representations, not model parameters. Evidence: SRC-1, `src/wiki/retrieve/dense.py`, `pyproject.toml`.

> _model = TextEmbedding(model_name=MODEL_NAME)
> --- `src/wiki/retrieve/dense.py`

#### RT-CMP-cross-encoder
Label: Optional MiniLM cross-encoder

Source-native identity: `Xenova/ms-marco-MiniLM-L-6-v2`, lazily loaded through fastembed. Distributed-parametric model on external cache/runtime substrate; scores are current-query values. No parameter training/update is wired. The name lacks an artifact revision/digest. No remote inference endpoint is invoked by this module; possible changes in name-to-artifact resolution are outside inspected dependencies. Its importability changes the return branch, not merely speed. Evidence: SRC-1, `src/wiki/retrieve/rerank.py`, `src/wiki/retrieve/query.py`.

> _model = TextCrossEncoder(model_name=MODEL_NAME)
> --- `src/wiki/retrieve/rerank.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-source-ingest
Label: Source extraction to pending proposals

Operator/file input → raw store → chunks → extractor calls → validated proposed pages → pending files and manifest. Python owns progression. Model proposes; schema/quote/overlap code can reject; the human has no per-content decision until later review. Guidance is the root `AGENTS.md`: extract less, avoid outside knowledge, cite each claim, use schemas and do not silently overwrite history. Page text, symbolic metadata and raw bytes persist, not the model's internal reasoning. Mode: open document ingestion under a fixed schema, not an experimental curriculum. There is no expected-answer oracle; source spans are a lexical reference for checks, not a truth oracle. Improvement trigger here is validation failure causing alternate-model extraction, not a learned policy revision. Rollback is not transactional; raw retention precedes processing and valid pending files can replace same-ID pending files. Actor labels are audit strings, not authorization identities. Evidence: SRC-1, `src/wiki/ingest/pipeline.py`, `src/wiki/ingest/hashing.py`, `src/wiki/ingest/chunk.py`, `src/wiki/ingest/diff.py`, `src/wiki/extract.py`, `AGENTS.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Manifest with source ID, usage, staged IDs and rejected-page issues; CLI renders a summary.
- Later read-back: Pending Markdown is consumed by review; retained raw text supports subsequent source checks. This call does not read prior extraction outcomes to tune its instructions.
- Delegated visibility: Anthropic receives the selected source chunk, source ID/offsets, proposal schema and root ingest instructions; it does not receive the full existing corpus through this call.
- Selection predicate: Chunk boundaries and overlap select source text; first nonempty all-valid extractor result wins per chunk, otherwise last result is retained; first occurrence of each page ID wins deduplication; only issue-free pages are staged.
- Invalidation or expiry: No timer; a later same-ID staged page or same-source manifest can overwrite its predecessor. Manual review can delete or move pending pages.
- Activation or effect: Code is wired to store source bytes and valid proposals; compliance of generated claims and actual writes in an execution are unobserved.
- Evidence limits: Static implementation only; provider fidelity, semantic entailment and monetary billing accuracy are not demonstrated.

> if pages and all(p.is_valid for p in pages):
>     return pages
> --- `src/wiki/ingest/pipeline.py`

> if page.is_valid:
>     dest = pending / f"{page.id}.md"
>     dest.write_text(page.to_markdown(), encoding="utf-8")
> --- `src/wiki/ingest/pipeline.py`

#### RT-RTE-page-review
Label: Interactive review and callable page acceptance

Pending page → human CLI decision → registered knowledge directory or deletion. Human proposes edits and chooses accept/reject in the CLI; callable primitives do not require proof of that decision. Code determines the destination from parsed type and registry, then performs the move. Admission is a human protocol in the CLI, software I/O in the primitive. Mode: open per-page review; no software answer oracle. No score threshold chooses acceptance. Root ingest doctrine shaped the original model proposal but is not re-read by this primitive. Accepted content persists; rejection deletes the pending file, not its raw source. Recovery after a move/commit failure is manual or Git-based, not an implemented rollback. Evidence: SRC-1, `src/wiki/review.py`, `src/wiki/cli/__init__.py`, `scripts/pre-commit`, `src/wiki/validate.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Destination path for acceptance; CLI prints accepted/rejected/skipped status.
- Later read-back: Knowledge files feed rebuild, query page loading, query bootstrap and evaluators; skipped pending pages remain available to another review invocation.
- Delegated visibility: Human sees a truncated preview and optionally the editor's file; editor and Git subprocesses inherit host execution authority, not model delegation.
- Selection predicate: All sorted pending Markdown files; CLI decision chooses each action. The primitive accepts a supplied page path and rejects unknown namespaces.
- Invalidation or expiry: Accept moves the file out of pending and may replace an existing destination; reject deletes it; no expiry clock or automatic old-page supersession update.
- Activation or effect: Retained-page replacement is wired; downstream changed behavior and successful commits are unobserved.
- Evidence limits: No schema/span revalidation in `accept_page`; optional installed hook structurally checks working-tree files after movement. Human correctness and deployed hook installation are not established.

> dest = _dest_for(root, page_path)
> dest.parent.mkdir(parents=True, exist_ok=True)
> page_path.replace(dest)
> --- `src/wiki/review.py`

#### RT-RTE-curated-seed
Label: Curated seed direct admission

Operator invokes shipped script → hand-authored `PAGES` and `SRC` → raw-store writes → `build_page` → schema and span checks → namespace Markdown writes. Human source authors supply the proposed content and quotes in the script; code rejects a failing page and decides whether execution continues. The invoking operator is not asked to approve each page. Guidance is encoded in curated specs and shared construction/check functions; root `AGENTS.md` is not supplied to a model on this route. Mode: fixed seed corpus, not open model extraction. Reference source prose and quotes support lexical checks, not an independently adjudicated oracle of historical truth. Earlier writes survive a later failure; overwrite recovery is manual/Git-dependent. Evidence: SRC-1, `scripts/seed_corpus.py`, `src/wiki/ingest/pipeline.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Failure code with issues on the first failed page, or printed seeded count and success code.
- Later read-back: Directly written knowledge pages feed ordinary loaders and rebuilds; raw source bytes feed provenance checking.
- Delegated visibility: inapplicable — this driver makes no model call or delegated worker invocation.
- Selection predicate: Iteration over shipped page specifications; each page must pass accumulated quote, schema and span issues before write.
- Invalidation or expiry: Same destination is overwritten; no expiry or interactive veto after invocation. Failure stops remaining pages, not earlier writes.
- Activation or effect: Direct retained-content admission is wired; no executed seed or subsequent consumption supplied.
- Evidence limits: Complete `main` inspected; every curated page specification was not audited here. No claim that all seeds pass in the frozen environment.

> if issues:
>     print(f"SEED FAIL {spec['id']}:")
>     for i in issues:
>         print("   -", i)
>     return 1
> dest = root / registry[spec["type"]]["dir"] / f"{spec['id']}.md"
> dest.write_text(page.to_markdown(), encoding="utf-8")
> --- `scripts/seed_corpus.py`

#### RT-RTE-index-query
Label: Rebuild and index-backed query

Operator rebuild → current nonsuperseded pages → lexical/graph/optional dense indexes; later operator or evaluator query → enabled component lists → reciprocal-rank fusion → optional cross-encoder → identifier result. Code owns selection, not a generative agent. Symbolic rules select graph seeds by ID/alias token intersection, traverse up to two hops and fuse ranks; distributed-parametric inference supplies optional embedding/reranking scores. `classify_query` exists but `retrieve` does not call it. Rebuild and query are separate invocations, not automatic on admission. Runtime-client flags enable components and reranking; CLI exposes `k` and rerank only. Recovery is manual rebuild, with component-local replacement rather than a global snapshot transaction. Evidence: SRC-1, `src/wiki/retrieve/rebuild.py`, `src/wiki/retrieve/store.py`, `src/wiki/retrieve/query.py`, `src/wiki/retrieve/bm25.py`, `src/wiki/retrieve/dense.py`, `src/wiki/retrieve/graph.py`, `src/wiki/retrieve/rerank.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rebuild manifest/counts or query dictionaries containing page ID, score, retrieval path and source-ID provenance; no page body or generated answer.
- Later read-back: SQLite indexes persist for later search calls; query itself does not write a remembered answer or update retained assertions.
- Delegated visibility: Optional local encoder sees page search text during build and query text during search; cross-encoder sees query and candidate search text. No downstream agent invocation is supplied.
- Selection predicate: Default nonsuperseded load; BM25 top 50, dense top 50 if available/nonempty, graph token seeds plus two-hop walk; RRF top 30 then k results. Active rerank filters candidates to IDs in current pages; ordinary fallback does not.
- Invalidation or expiry: Explicit rebuild replaces indexes; query has no index freshness/hash check. Import absence disables dense or rerank; missing indexes yield empty component results. Dependency/model-load failures after availability checks are not a guaranteed graceful fallback.
- Activation or effect: Ranked output and derived-state construction are wired; actual context delivery to an answering agent and answer changes are unobserved.
- Evidence limits: Stale indexes and dangling graph targets prevent universal current-page/supersession exclusion. Model artifact identity and deployed component availability are uninspected.

> candidates = [
>     (pid, pages[pid].search_text()) for pid, _, _ in fused if pid in pages
> ]
> --- `src/wiki/retrieve/query.py`

> "page_id": pid,
> "score": score,
> "retrieval_path": sources,
> "provenance": _provenance(pages[pid]) if pid in pages else [],
> --- `src/wiki/retrieve/query.py`

The ordinary return's conditional provenance expression supports empty provenance, not freshness enforcement.

#### RT-RTE-eval-report
Label: Operator measurement and saved evaluation reports

Operator evaluation command → dataset or retained source spans → retrieval/ingest metrics → report artifacts. In retrieval comparison, code runs fixed adapters and computes scores against dataset expected IDs. Human-supplied dataset labels are the answer oracle; the model is not asked to grade retrieval. Source-span overlap is the ingest reference measure, not truth adjudication. Mode: bounded evaluation of a fixed dataset/current corpus. Human can inspect saved output; no software veto admits a product change here. Improvement trigger is an operator's later judgment, not an automatic updater. Evidence: SRC-1, `src/wiki/eval/harness.py`, `src/wiki/cli/__init__.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Overall, by-type and per-query metrics or mean ingest faithfulness; component command reports relative results.
- Later read-back: Baseline JSON and timestamped Markdown persist as reports; no inspected consumer uses them to change retrieval settings automatically.
- Delegated visibility: Evaluator adapters receive each query; optional retrieval components have the visibility described in the index-query route. Ingest evaluation is local.
- Selection predicate: Nonempty JSONL dataset rows and their expected IDs for retrieval; namespace pages with source entries and loadable raw text for ingest evaluation. Missing raw source causes that page to be skipped in the CLI ingest metric.
- Invalidation or expiry: Latest named baseline/component JSON can be overwritten; timestamped reports retain prior output. No automatic expiry or promotion rollback.
- Activation or effect: Reporting and saving are wired; metric improvement, causal component benefit and adoption into production are not established by this inspection.
- Evidence limits: Metrics depend on labels and evaluated subset. Source-authored saved baselines are reported operation, not executions reproduced here.

> rel = set(q["expected_page_ids"])
> --- `src/wiki/eval/harness.py`

> typer.echo("(gate relaxed for toy corpus — reporting only)")
> --- `src/wiki/cli/__init__.py`

#### RT-RTE-query-bootstrap
Label: Candidate evaluation-query generation

Operator request → retained page bodies → direct Anthropic calls → candidate JSONL. Model proposes queries; code associates each nonempty line with the current page stem as expected ID and `lookup` type. The command requests human review and merge; it does not enforce a merge decision or verify that each query really has that answer. Mode: per-page candidate generation, not oracle-backed automatic evaluation-data admission. Root extraction instructions, structured propose tool and ingest cost guard are not used. Proposed changes persist in the chosen output file; the default is separate from the active dataset, but `out` is caller-selectable and not protected against naming the active dataset. Human review is therefore a documented protocol, not universal file-write enforcement. Existing output is truncated by opening in write mode. Evidence: SRC-1, `src/wiki/cli/__init__.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed candidate count and review/merge reminder.
- Later read-back: Default candidate file requires a later merge to reach active evaluation; a caller-selected active-dataset path can place generated rows directly at that consumer's location.
- Delegated visibility: Anthropic receives the retained page body and a short query-generation instruction, one call per namespace page.
- Selection predicate: Every Markdown page found through registered directories; unlike `load_pages`, this loop does not filter superseded pages. Every nonempty response line is written without query-semantic validation.
- Invalidation or expiry: Chosen output is overwritten on invocation; partial output may survive failure; no automatic rollback or expiry.
- Activation or effect: Candidate dataset writing is wired; human review, merge and later evaluation consumption are unobserved.
- Evidence limits: No model-response examples or exercised output-path choices are supplied; inferred wiring does not establish trustworthy query labels.

> with out_path.open("w", encoding="utf-8") as fh:
> --- `src/wiki/cli/__init__.py`

> typer.echo(f"wrote {n} candidate queries → {out} (review & merge into queries.jsonl)")
> --- `src/wiki/cli/__init__.py`

### Claims

#### RT-CLM-provenance-policy
Label: Every-claim provenance and no invention policy

Claimed operation: extractor instructions require a citation for every substantive claim and forbid invention. This is natural-language model guidance. Software quote location accepts exact matches or fuzzy alignment at score 85; marked-claim span checking uses token-set overlap threshold 60. Schema/body checking validates existing markers against source-array length. These checks do not prove semantic support and do not detect every uncited assertion. Owner: ingest guidance and pipeline checks; strength: policy for all-claim coverage, best effort for overlap. SRC-1, `AGENTS.md`, `src/wiki/ingest/pipeline.py`, `src/wiki/ingest/spancheck.py`, `src/wiki/validate.py`, `src/wiki/config.py`.

> Every substantive claim in the body ends with a `[^src:N]` footnote whose `N`
> is a 1-based index into that array. A claim with no citation is a bug.
> --- `AGENTS.md`

> for claim, n in extract_claims(body):
> --- `src/wiki/ingest/spancheck.py`

> for m in _FOOTNOTE_RE.finditer(body):
> --- `src/wiki/validate.py`

#### RT-CLM-history-policy
Label: Supersede rather than overwrite instruction

Claimed operation: conflicting information should create a new page with supersession links and leave the old page in place. This is model/reviewer guidance, not a storage invariant. The actual diff only flags a changed body; review can replace an existing destination. Neither the move primitive nor the seed writer updates the old page's reciprocal link automatically. SRC-1, `AGENTS.md`, `src/wiki/ingest/diff.py`, `src/wiki/review.py`, `scripts/seed_corpus.py`; implementation witness is [RT-RTE-page-review](#rt-rte-page-review).

> Old pages stay.
> --- `AGENTS.md`

> if current.body.strip() != proposed.body.strip():
>     proposed.contradicts.append(
> --- `src/wiki/ingest/diff.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-ingest-instructions
Label: Root instructions into extraction

Consumer: Anthropic extraction invocation. Channel: root `AGENTS.md` text interpolated into the system argument, alongside source identity and quote instructions. Force: natural-language behavioral guidance, distinct from the symbolic `propose_pages` tool schema and code-enforced validators. Horizon: reloaded for each chunk/attempt; changes to that root file could shape later extractions, but no inspected automatic mechanism revises it. Delivery is wired; compliance is unobserved. Evidence: SRC-1, `src/wiki/ingest/pipeline.py`, `src/wiki/extract.py`, `AGENTS.md`.

> agents = root / "AGENTS.md"
> return agents.read_text(encoding="utf-8") if agents.is_file() else ""
> --- `src/wiki/ingest/pipeline.py`

> system=context,
> tools=[PROPOSE_TOOL],
> tool_choice={"type": "tool", "name": "propose_pages"},
> --- `src/wiki/extract.py`

## Annotations

none

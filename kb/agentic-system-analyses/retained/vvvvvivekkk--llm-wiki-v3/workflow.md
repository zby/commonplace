---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "LLM-Wiki-v3 workflow from operator source ingestion through model extraction, human admission and later retrieval, including rejection and recovery limits."
run-id: AAS-2026-10-18-llm-wiki-v3-0c553a3118eb-01
reviewed-boundary: "267541db838cbca757a112bd0cfa47fa61eb5fb2"
---

# LLM-Wiki-v3 workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is operator-initiated source ingestion → model proposals → pending-page review → retained knowledge → explicit index rebuild → later query. It was selected because these shipped producers and consumers connect through actual files, rather than through an imagined agent orchestrator. The workflow is a sequence of separately invoked commands, not one automatically completed task. Its delivered result is retained Markdown and, after further operator action, ranked retrieval metadata; a downstream agent answer is outside the established path ([RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-page-review](runtime.md#rt-rte-page-review), [RT-RTE-index-query](runtime.md#rt-rte-index-query)).

The evidence is SRC-1 at the boundary's frozen commit. Direct inspection for this member covered all of `src/wiki/ingest/pipeline.py`, `src/wiki/extract.py`, `src/wiki/review.py`, `src/wiki/retrieve/rebuild.py`, `src/wiki/retrieve/query.py`, and the ingest, review, rebuild and query commands in `src/wiki/cli/__init__.py`. These passages supply implementation evidence. No target execution, provider response, interactive review session or successful end-to-end delivery was observed. Runtime records supply the broader validation and recovery evidence cited below; no peer memory or epistemic member was supplied.

### 1. Operator request becomes bounded extraction work

An operator supplies a readable source file to `wiki ingest`. The CLI discovers the root and constructs cheap and escalation extractors. Python retains the original bytes, reloads source text, chunks it, and sequentially calls the extractor for each chunk. The actor argument records attribution; it does not authenticate a principal. The operator starts ingestion but does not approve each proposed claim at this stage ([RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); SRC-1, `src/wiki/cli/__init__.py`, `src/wiki/ingest/pipeline.py`).

The handoff to Anthropic supplies root ingest instructions, source ID, chunk character bounds, one chunk's text, and the structured `propose_pages` schema. The model returns proposed IDs, types, bodies, fields and supporting quotes. It neither selects the next chunk nor writes knowledge files. Each request has a fresh user message rather than a growing shared conversation; existing knowledge is not supplied to this extraction call. Host code retains full source text for subsequent quote location. The instruction channel is natural-language guidance, while the proposal schema constrains the requested return shape ([RT-BAP-ingest-instructions](runtime.md#rt-bap-ingest-instructions); SRC-1, `src/wiki/extract.py`, `src/wiki/ingest/pipeline.py`).

### 2. Software verifies proposals and chooses escalation

Code locates returned quotes in the full source, constructs source spans and frontmatter, and combines quote-location, schema and marked-claim overlap issues. These checks can reject proposals; they are not an oracle for historical truth or semantic entailment. The requirement to cite every substantive claim remains stronger than the checks over existing markers ([RT-CLM-provenance-policy](runtime.md#rt-clm-provenance-policy)).

The consequential decision is per chunk: the first nonempty all-valid page set wins. If the cheap attempt is empty or contains any invalid page, the pipeline tries the stronger extractor. That is fresh extraction on the same selected source, not a critic receiving the first attempt and diagnosing its mistakes. If all attempts fail that acceptance predicate, the last attempt's pages continue to staging assessment ([RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); SRC-1, `src/wiki/ingest/pipeline.py`).

This gives a concrete rejection branch. Suppose the cheap attempt contains both a valid page and a page whose quote cannot be located. The invalid page prevents the whole cheap set from winning. Escalation replaces that set rather than merging its valid subset with the retry. If the last attempt is also mixed, its valid pages can still be staged and its invalid pages reported as rejected. The code therefore supports partial staging, not an all-or-nothing source transaction. An empty final set produces no pages from that chunk; it does not preserve earlier proposals (SRC-1, `src/wiki/ingest/pipeline.py`; [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)).

### 3. Pending files hand responsibility back to the operator

After all chunks return, Python deduplicates by ID, keeping the first occurrence, computes new/patch and contradiction information, writes issue-free Markdown to pending, and records rejected IDs/issues in the manifest. The CLI reports counts, IDs and contradiction flags. Manifest “accepted” means staged; it does not mean admitted to retained knowledge. Pending Markdown, not the model conversation or manifest alone, is the next command's input ([RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); SRC-1, `src/wiki/ingest/pipeline.py`, `src/wiki/cli/__init__.py`).

There is no automatic handoff into review. The operator invokes `wiki review`, sees a preview of up to 800 characters, can request an external editor, and chooses accept, reject, skip or quit. Rejection deletes that pending file, leaving raw source retention unaffected. Skip and quit leave unfinished work available for another invocation ([RT-RTE-page-review](runtime.md#rt-rte-page-review); SRC-1, `src/wiki/cli/__init__.py`, `src/wiki/review.py`).

Acceptance reparses the current page type, checks namespace membership, moves the file to the registered knowledge directory and optionally invokes Git. This is the retained-content delivery point, not proof of successful downstream use. In particular, edits are not followed by pipeline schema/span revalidation. The operator's decision is a protocol of this CLI route, not a universal authorization boundary: callable acceptance and the separately shipped curated seed writer are alternate admission paths ([RT-RTE-page-review](runtime.md#rt-rte-page-review), [RT-RTE-curated-seed](runtime.md#rt-rte-curated-seed)). Same-name acceptance can replace a destination; the instruction to preserve old pages through supersession is not automatically enforced ([RT-CLM-history-policy](runtime.md#rt-clm-history-policy)).

### 4. Later operator actions make knowledge searchable

Acceptance does not rebuild indexes. A later `wiki rebuild` loads current nonsuperseded pages and sequentially constructs lexical, graph and available dense indexes, then writes a build manifest. A later `wiki query` obtains component rankings, fuses them, optionally reranks, and returns page IDs, scores, retrieval paths and source IDs. The CLI prints those fields, not page bodies or an assembled answering prompt ([RT-RTE-index-query](runtime.md#rt-rte-index-query); SRC-1, `src/wiki/retrieve/rebuild.py`, `src/wiki/retrieve/query.py`, `src/wiki/cli/__init__.py`).

Thus a successful admission does not itself establish search freshness. The ordinary fused query branch does not filter every output ID against currently loaded pages; stale IDs can retain a rank and receive empty provenance. The active rerank branch filters candidates first, but requesting rerank does not guarantee that branch is available. These are limits on what the final retrieval result establishes, not evidence that a stale result occurred in a run ([RT-RTE-index-query](runtime.md#rt-rte-index-query)). No supplied consumer turns this return into an observed agent answer.

### Failure ownership and completion limits

Software owns validation rejection and alternate-model selection; the operator owns content admission and subsequent command invocation. The CLI separately handles Anthropic client initialization failure and the configured ingest cost-ceiling exception. The latter check occurs after a response, so it cannot prevent that call's expenditure; it interrupts ingestion before normal completion (SRC-1, `src/wiki/cli/__init__.py`, `src/wiki/ingest/pipeline.py`; [runtime recovery account](runtime.md#coordination-recovery-and-working-context)).

The source does not make these stages transactional. Raw storage precedes extraction; acceptance moves the page before optional Git operations; component index replacement is not one shared transaction. A failed commit therefore does not establish that the move was undone. Human repair, available Git history and explicit rebuild are recovery resources, not a demonstrated automatic rollback protocol ([RT-RTE-page-review](runtime.md#rt-rte-page-review), [RT-RTE-index-query](runtime.md#rt-rte-index-query); [runtime recovery account](runtime.md#coordination-recovery-and-working-context)).

Completion must consequently be stated at each boundary: ingest returns a staging manifest; review returns accepted destinations or rejection/skip messages; rebuild returns a build manifest; query returns retrieval metadata. Source inspection establishes these wired handoffs, not their successful exercise, model fidelity, human correctness or beneficial downstream reasoning.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Workflow-specific retry consequence: a mixed cheap result is discarded when escalation runs; the last attempt, not the union of valid proposals, reaches cross-chunk deduplication and staging. This explains why the retry is replacement extraction rather than incremental repair. Direct implementation evidence: SRC-1, `src/wiki/ingest/pipeline.py`.

> last = pages
> if pages and all(p.is_valid for p in pages):
>     return pages
> return last
> --- `src/wiki/ingest/pipeline.py`

#### On [RT-RTE-page-review](runtime.md#rt-rte-page-review)

Workflow handoff boundary: review obtains the pending-file list once, displays a bounded preview, optionally invokes the editor, and only then asks for a decision. This supplies a human opportunity to revise content, not evidence of a complete review or a post-edit verification pass. Direct implementation evidence: SRC-1, `src/wiki/cli/__init__.py`.

> typer.echo(page_path.read_text(encoding="utf-8")[:800])
> if edit:
>     subprocess.run([os.environ.get("EDITOR", "vi"), str(page_path)])
> choice = typer.prompt("[a]ccept / [r]eject / [s]kip / [q]uit", default="s").strip().lower()
> --- `src/wiki/cli/__init__.py`

#### On [RT-RTE-index-query](runtime.md#rt-rte-index-query)

Workflow completion boundary: the shipped query command consumes retrieval dictionaries and prints four metadata fields. No body-loading or answer-generation step follows in this command. This limits delivery to retrieval metadata, independently of the README's intended agent audience. Direct implementation evidence: SRC-1, `src/wiki/cli/__init__.py`.

> for r in retrieve(wiki_root, text, k=k, do_rerank=rerank):
>     path = ",".join(r["retrieval_path"]) or "-"
>     prov = ",".join(r["provenance"]) or "-"
>     typer.echo(f"{r['page_id']}\t{r['score']:.4f}\t{path}\t{prov}")
> --- `src/wiki/cli/__init__.py`

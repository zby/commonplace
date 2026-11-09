---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "post-graph-rag workflow: the shipped three-document quickstart from extraction and persistence through retrieved answer delivery, with bounded degradation and no answer-verification loop."
run-id: AAS-2026-11-08-post-graph-rag-448d75e4222d-01
reviewed-boundary: "bce4146a7dc4684e9b66806915c29b0eed57ba23"
---

# post-graph-rag workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is the shipped quickstart: index three documents, then answer a question requiring their facts to be joined. It was selected because one executable caller connects production, retention, retrieval, synthesis and visible delivery rather than leaving those capabilities as unrelated APIs. It is a multi-step model-assisted workflow, not a multi-agent delegation protocol. Python owns progression; model services receive bounded content-processing requests. The enclosing exploration/verifier loop is a consumer responsibility, as established in [boundary](boundary.md#boundary-and-evidence).

All source findings use SRC-1 at the frozen revision. This member directly inspected `examples/01_quickstart.py`, `examples/_shared.py`, indexing/preparation/writer and retrieval/synthesis sections of `post_graph_rag/engine.py`, and extraction/validation sections of `post_graph_rag/extractor.py`. These supply implementation and embedded doctrine, not observed execution. No target was run and no tracked benchmark result was assessed. The related runtime records remain the canonical declarations; this member adds workflow interpretation and annotations, not duplicate records.

### 1. Caller establishes the job and supplies documents

The quickstart constructs GraphRAG using environment-derived provider/database settings and a timestamp-suffixed realm, initializes it, and indexes the three document strings sequentially. The documents describe an acquisition, leadership appointment and product technology. The per-run realm is demonstration isolation, not deletion of prior realms or proof of a security boundary. The caller, not a model, chooses the corpus, ordering and final question. SRC-1, `examples/01_quickstart.py`, `examples/_shared.py`:

> rag = GraphRAG(make_config(fresh_realm("example_quickstart")))
> await rag.initialize()
> --- `examples/01_quickstart.py`

Each handoff to `index_document` supplies the text and a source filename. The example supplies no custom extractor or per-record approval step. It awaits each indexing call before asking the question. [RT-RTE-document-admission](runtime.md#rt-rte-document-admission) owns the admission route; [RT-RTE-extractor-extension](runtime.md#rt-rte-extractor-extension) bounds the guarantees when a caller changes its extraction mechanism.

### 2. Extraction proposes structure; code admits it

`index_document` prepares a chunk before writing it. Preparation derives DocumentContext from metadata when appropriate and concurrently requests the passage embedding and extraction. The embedding provider receives text; the extraction model receives system guidance plus context and document text. These are service calls, not independently scheduled agents with their own task queues. Their results return to the engine; models do not directly execute database writes. See [RT-CMP-extraction-model](runtime.md#rt-cmp-extraction-model), [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model) and [RT-BAP-extraction-guidance](runtime.md#rt-bap-extraction-guidance).

On the default model path, extraction parses the result, can request additional missed records through configured gleaning passes, merges those proposals and invokes `_validate`. Gleaning is additional extraction under the same guidance, not an independent verifier deciding whether the final answer is correct. Validation drops empty or unsuitable entity names, vague/self-referential relations, unresolved pronouns and configured low-confidence or negated triples. It can reject all structure. This is a symbolic admission policy applied to model proposals, not factual certification. SRC-1, `post_graph_rag/extractor.py`; minimum passages appear in the document-admission annotation below.

Prepared entity descriptions, missing endpoint names and relation text then receive derived embeddings. The passage and those derived representations have different failure consequences. Python passes the prepared bundle to the writer; no human content approval intervenes on this path. [RT-RTE-document-admission](runtime.md#rt-rte-document-admission) supplies the preparation and persistence evidence.

### 3. Persistence enables the later answering invocation

The writer stamps document identity/content hash and inserts the passage with its vector before attempting graph structure. It upserts entities, resolves aliases, creates missing endpoint entities, writes relations with source-chunk provenance, optionally supersedes conflicting relations, and links mentioned entities to the chunk. Its return includes a chunk ID, extraction counts and degradation/error indicators. These are persistence and process outcomes, not a proof that all proposed relations were written or correct. SRC-1, `post_graph_rag/engine.py`; [RT-RTE-document-admission](runtime.md#rt-rte-document-admission).

The quickstart prints only the entity extraction count. It neither examines all degradation flags nor decides to repair an incomplete graph before proceeding. The successful return of an indexing call therefore acts as its progression condition, not as a semantic completeness gate. This distinction matters because passage-only admission is explicitly supported.

### 4. The question selects retained material for synthesis

After all indexing calls return, the caller asks who built Meridian's technology and their current Northwind role. The engine's query route obtains structured data first. Auxiliary keyword extraction and embeddings drive searches; entity seeds drive graph walks, and configured relation-vector, lexical and mention-expansion channels can add material. Code filters, merges and optionally reranks relation candidates before formatting the context. These operations select from retained passages and graph state; they do not delegate an open-ended research task. [RT-RTE-question-answer](runtime.md#rt-rte-question-answer) owns this route and its temporal, channel and budget limitations. SRC-1, `post_graph_rag/engine.py`.

The synthesis consumer receives rendered passages, entity descriptions and graph relationships, plus any selected community reports and reference list. Not every retrieved metadata field survives rendering. Negation and optional validity dates are rendered into relation text; reference numbering connects passages to the prompt's citation instruction. Caller history, if supplied, precedes this user message. Context budgets clip rendered material rather than impose a hard total model-window bound. The quickstart does not build communities or supply history, and its use does not establish that the cross-document facts were actually retrieved or used. [RT-BAP-answer-context](runtime.md#rt-bap-answer-context) supplies the message-channel evidence.

### 5. Delivery is an answer return and print, not verified acceptance

For the ordinary nonstreaming path, the engine awaits synthesis and returns the answer with retrieved-document, entity, relation and reference metadata. The quickstart prints the answer and up to eight retrieved triples, then closes the library in `finally`. It has no reference answer, judge call, user approval or branch that rejects a wrong answer and repeats retrieval. The prompt asks the synthesis model to admit insufficient context, but code does not certify that behavior. This bounded finding concerns the inspected quickstart/query path, not all shipped evaluators or external consumers. SRC-1, `examples/01_quickstart.py`, `post_graph_rag/engine.py`; [RT-RTE-question-answer](runtime.md#rt-rte-question-answer).

Thus “delivered” means the model response reached the returned dictionary and the caller's print operation. It does not mean verified correctness, successful joining of all three documents, durable answer storage or demonstrated benefit over another retrieval system. The workflow has admission checks before graph writes but no corresponding correctness veto before answer delivery.

### Failure and recovery ownership

Two supported degradation paths can still reach answering. An `ExtractionError` becomes empty structure while preserving eligibility to store the passage/vector. A derived `EmbeddingError` discards proposed structure and sets a degradation flag. After passage insertion, ordinary structural-write exceptions are accumulated rather than undoing the passage. The vector/document channel can therefore remain available even when the graph channel loses content; that is a wired fallback opportunity, not observed answer recovery. Other preparation failures and passage-insertion failures can propagate. The quickstart has cleanup but no retry handler; an exception during indexing prevents reaching its later question. SRC-1, `post_graph_rag/engine.py`; [RT-RTE-document-admission](runtime.md#rt-rte-document-admission).

Recovery from counted structural loss belongs to a caller that inspects results and chooses re-indexing. The example does not implement that decision. Nor should its direct chunk API be confused with `index_text` replacement/unchanged-document behavior: the runtime route documents that distinction. Provider retry/failover is a separate service mechanism, not a workflow-level verification-and-repair cycle. [RT-RTE-direct-answer](runtime.md#rt-rte-direct-answer) also bounds the alternate streaming path: opening can fail over, while mid-stream failures propagate. Neither mechanism establishes successful execution at this frozen boundary.

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

#### On [RT-RTE-document-admission](runtime.md#rt-rte-document-admission)

Workflow handoff: the quickstart supplies text/source and waits for each result, but exposes only an extraction count to the operator. It does not use returned degradation indicators to veto progression. SRC-1, `examples/01_quickstart.py`:

> for source, text in DOCS:
>     res = await rag.index_document(text, metadata={"source": source})
>     print(f"indexed {source}: {res['entities_extracted']} entities")
> --- `examples/01_quickstart.py`

Verification role: on the default model branch, gleaning precedes the validation gate. The gate rejects unsuitable proposals rather than proving source entailment. SRC-1, `post_graph_rag/extractor.py`:

> result = self._merge(result, extra)
>
> return self._validate(result)
> --- `post_graph_rag/extractor.py`

> if t.confidence < self.min_confidence:
>     continue
> if t.negated and self.drop_negated:
>     continue
> --- `post_graph_rag/extractor.py`

> if not entities and not triples:
>     raise ExtractionError(
>         "All extracted entities and triples were rejected as empty, pronominal or non-specific."
>     )
> --- `post_graph_rag/extractor.py`

#### On [RT-RTE-question-answer](runtime.md#rt-rte-question-answer)

Workflow delivery criterion: the nonstreaming response is returned to the quickstart and printed without an answer-correctness branch. The retrieved triples are displayed separately; their display is not verification that synthesis used them faithfully. SRC-1, `examples/01_quickstart.py`:

> print(out["answer"])
>
> banner("Relations the answer was built from")
> for t in out.get("retrieved_graph_triples", [])[:8]:
>     print(f"  {t}")
> --- `examples/01_quickstart.py`

SRC-1, `post_graph_rag/engine.py`, wires synthesis response directly into the returned product:

> answer = await self.llm.chat_completion(messages, role="synthesis")
>
> return {
>     "question": question,
>     "answer": answer,
>     "mode": mode,
>     "keywords": data_res["metadata"]["keywords"],
> --- `post_graph_rag/engine.py`

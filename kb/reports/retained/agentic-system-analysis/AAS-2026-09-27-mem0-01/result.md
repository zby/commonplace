---
{
  "type": "types/agentic-system-analysis-result.md",
  "description": "Mem0 synchronous OSS Python memory APIs: pinned runtime, memory and epistemic analysis",
  "run-id": "AAS-2026-09-27-mem0-01",
  "system": "Mem0",
  "run-date": "2026-09-27",
  "result-disposition": "complete",
  "target-class": "memory/knowledge/context-engineering system",
  "boundary-kind": "subsystem-only",
  "reviewed-boundary": "94c3fe9f238f3dbf29c9ce98643bd71eb13077cd",
  "analysis-cutoff": "2026-09-27",
  "evidence-tier": "code-grounded",
  "memory-comparison": {
    "scope": "Synchronous OSS Python Memory retained facts/raw messages, SQLite message window/history, entity access collection, optional procedural and vision preprocessing paths, configured vector adapters and documented/shipped consumer surfaces. Excludes AsyncMemory, hosted internals, enclosing agent execution, provider internals, telemetry and static instructions. Adapter substrate coverage is partial.",
    "axes": {
      "storage_substrate": {
        "assessment": "partial",
        "values": [
          "vector",
          "sqlite",
          "files",
          "rdbms"
        ],
        "evidence": {
          "vector": {
            "basis": "wired",
            "records": [
              "OBJ-2",
              "OBJ-4"
            ],
            "note": "Memory and entity collections use the configured vector adapter."
          },
          "sqlite": {
            "basis": "wired",
            "records": [
              "OBJ-3"
            ],
            "note": "SQLite holds the message window and change history."
          },
          "files": {
            "basis": "wired",
            "records": [
              "CMP-6"
            ],
            "note": "FAISS adapter saves index and JSON docstore files."
          },
          "rdbms": {
            "basis": "wired",
            "records": [
              "CMP-6"
            ],
            "note": "PGVector adapter creates a PostgreSQL table with vector and JSONB columns."
          }
        },
        "records": [
          "OBJ-2",
          "OBJ-4",
          "OBJ-3",
          "CMP-6"
        ],
        "note": "Provider registry inspected; remaining backend adapters have not all been inspected. This is not a complete substrate union."
      },
      "representational_form": {
        "assessment": "known",
        "values": [
          "natural-language",
          "symbolic"
        ],
        "evidence": {
          "natural-language": {
            "basis": "wired",
            "records": [
              "OBJ-2",
              "OBJ-3",
              "OBJ-5"
            ],
            "note": "Facts, messages and procedural summaries are text."
          },
          "symbolic": {
            "basis": "wired",
            "records": [
              "OBJ-2",
              "OBJ-3",
              "OBJ-4"
            ],
            "note": "Structured metadata, vector values, entity links and history rows are operative symbolic data."
          }
        },
        "records": [
          "OBJ-2",
          "OBJ-3",
          "OBJ-5",
          "OBJ-4"
        ],
        "note": "Covers data exchanged by synchronous Memory and the inspected adapter boundary. Provider model weights and internal representations are excluded; embeddings are retained numeric data, not trained weights."
      },
      "lineage": {
        "assessment": "known",
        "values": [
          "authored",
          "imported",
          "trace-extracted",
          "other-compiled"
        ],
        "evidence": {
          "authored": {
            "basis": "wired",
            "records": [
              "RTE-4"
            ],
            "note": "Direct raw-text addition and explicit text update preserve caller-authored content."
          },
          "imported": {
            "basis": "wired",
            "records": [
              "OBJ-3",
              "RTE-2"
            ],
            "note": "Submitted message bodies are copied into the bounded SQLite window."
          },
          "trace-extracted": {
            "basis": "wired",
            "records": [
              "RTE-2",
              "OBJ-5"
            ],
            "note": "LLM extraction and procedural summarization derive text from submitted interactions."
          },
          "other-compiled": {
            "basis": "wired",
            "records": [
              "OBJ-4",
              "RTE-2"
            ],
            "note": "Entity links, embeddings and optional image descriptions are derived access/context material."
          }
        },
        "records": [
          "RTE-4",
          "OBJ-3",
          "RTE-2",
          "OBJ-5",
          "OBJ-4"
        ],
        "note": "Separate raw retention, trace extraction, authoring, and secondary compilation; no weight-learning route is counted."
      },
      "behavioral_authority": {
        "assessment": "known",
        "values": [
          "knowledge",
          "ranking"
        ],
        "evidence": {
          "knowledge": {
            "basis": "wired",
            "records": [
              "RTE-2"
            ],
            "note": "Existing memory text and recent messages inform the extraction model; external answer use is afforded by the example."
          },
          "ranking": {
            "basis": "wired",
            "records": [
              "OBJ-4",
              "RTE-3"
            ],
            "note": "Entity links and retained lexical/vector access data determine retrieval scores."
          }
        },
        "records": [
          "RTE-2",
          "OBJ-4",
          "RTE-3"
        ],
        "note": "Descriptive facts about agent configuration and the procedural label do not establish binding instructions at a later consumer. Static extraction prompts and caller identity controls are not learned memory authority."
      },
      "write_agency": {
        "assessment": "known",
        "values": [
          "automatic",
          "manual"
        ],
        "evidence": {
          "automatic": {
            "basis": "wired",
            "records": [
              "RTE-2",
              "OBJ-5"
            ],
            "note": "Extraction, summarization, entity linking and history writes occur automatically after invocation."
          },
          "manual": {
            "basis": "wired",
            "records": [
              "RTE-4"
            ],
            "note": "infer=False and update permit explicit caller text authoring."
          }
        },
        "records": [
          "RTE-2",
          "OBJ-5",
          "RTE-4"
        ],
        "note": "An operator-triggered extraction is still automatic; manual refers to authoring retained content through explicit APIs."
      },
      "curation_operations": {
        "assessment": "known",
        "values": [
          "dedup",
          "evolve",
          "invalidate",
          "decay"
        ],
        "evidence": {
          "dedup": {
            "basis": "wired",
            "records": [
              "OBJ-4"
            ],
            "note": "Entity records merge exact or sufficiently similar entities and union linked memory IDs."
          },
          "evolve": {
            "basis": "wired",
            "records": [
              "RTE-4"
            ],
            "note": "Explicit update replaces existing memory text while retaining change history."
          },
          "invalidate": {
            "basis": "wired",
            "records": [
              "RTE-4"
            ],
            "note": "Delete removes current vector reliance and records the old text in history; expiration hides retained entries."
          },
          "decay": {
            "basis": "wired",
            "records": [
              "OBJ-3"
            ],
            "note": "The message window evicts entries beyond its most recent ten."
          }
        },
        "records": [
          "OBJ-4",
          "RTE-4",
          "OBJ-3"
        ],
        "note": "Hash suppression on acquisition is not the dedup witness. Extraction ADD, transient ranking boosts and summary creation do not establish consolidate, synthesize or promote over already retained content."
      },
      "read_back_direction": {
        "assessment": "known",
        "values": [
          "pull",
          "push"
        ],
        "evidence": {
          "pull": {
            "basis": "afforded",
            "records": [
              "RTE-5"
            ],
            "note": "The documented chat application requests memory through search; no execution was observed."
          },
          "push": {
            "basis": "wired",
            "records": [
              "RTE-2"
            ],
            "note": "An add invocation automatically selects retained history and existing memories for the extraction model."
          }
        },
        "records": [
          "RTE-5",
          "RTE-2"
        ],
        "note": "The README also affords push to an answer model. The broken proxy does not upgrade external delivery. Internal selector calls are not double-counted as another supply direction."
      },
      "read_back_signal": {
        "assessment": "known",
        "values": [
          "identifier",
          "inferred-embedding",
          "inferred-lexical"
        ],
        "evidence": {
          "identifier": {
            "basis": "wired",
            "records": [
              "RTE-2",
              "OBJ-3"
            ],
            "note": "The automatic message-history selector matches session_scope before supplying the extraction prompt."
          },
          "inferred-embedding": {
            "basis": "wired",
            "records": [
              "RTE-2"
            ],
            "note": "New messages embed a query selecting ten old memories for extraction."
          },
          "inferred-lexical": {
            "basis": "afforded",
            "records": [
              "RTE-5",
              "RTE-3"
            ],
            "note": "The documented automatic chat injection uses search, whose compatible adapters add keyword scores."
          }
        },
        "records": [
          "RTE-2",
          "OBJ-3",
          "RTE-5",
          "RTE-3"
        ],
        "note": "Signals characterize automatic supply to extraction and the afforded answer example. Optional reranking changes a requested API response; no additional automatic model-supply route using rerank=True was established."
      },
      "trace_learning": {
        "assessment": "known",
        "values": [
          "yes"
        ],
        "evidence": {
          "yes": {
            "basis": "wired",
            "records": [
              "RTE-2",
              "OBJ-4",
              "OBJ-5"
            ],
            "note": "Automatic trace-fed derived memory is durable and consumed by later extraction and ranking; improved performance is not required."
          }
        },
        "records": [
          "RTE-2",
          "OBJ-4",
          "OBJ-5"
        ],
        "note": "The same collection also holds raw authored memory; raw retention alone is not the positive witness."
      },
      "trace_source": {
        "assessment": "partial",
        "values": [
          "session-logs"
        ],
        "evidence": {
          "session-logs": {
            "basis": "wired",
            "records": [
              "RTE-2"
            ],
            "note": "Submitted user/assistant conversations produce durable extracted facts and entity access data."
          }
        },
        "records": [
          "RTE-2",
          "OBJ-5"
        ],
        "note": "Procedural creation accepts arbitrary message content and its prompt requests execution history; actual trajectory/tool-trace coverage and later task use are not established. Keep the witnessed conversation source without claiming an exhaustive source set."
      },
      "learning_scope": {
        "assessment": "not-determinable",
        "values": [],
        "evidence": {},
        "records": [
          "RTE-2",
          "OBJ-5",
          "RTE-5"
        ],
        "note": "user_id, agent_id and run_id partition retention but do not fix task horizons. The procedural prompt describes task continuation, without a wired task-continuation consumer or established aggregate horizon."
      },
      "learning_timing": {
        "assessment": "partial",
        "values": [
          "online"
        ],
        "evidence": {
          "online": {
            "basis": "afforded",
            "records": [
              "RTE-5"
            ],
            "note": "The documented chat loop derives memories after each answer for subsequent requests."
          }
        },
        "records": [
          "RTE-2",
          "OBJ-5",
          "RTE-5"
        ],
        "note": "Synchronous implementation establishes invocation-time writes, not when arbitrary procedural or batch callers run relative to their tasks; no exhaustive timing union is asserted."
      },
      "distilled_form": {
        "assessment": "known",
        "values": [
          "natural-language",
          "symbolic"
        ],
        "evidence": {
          "natural-language": {
            "basis": "wired",
            "records": [
              "RTE-2",
              "OBJ-5"
            ],
            "note": "Extracted fact text and procedural summaries are durable language artifacts."
          },
          "symbolic": {
            "basis": "wired",
            "records": [
              "OBJ-4"
            ],
            "note": "Trace-derived facts yield durable entity records and numeric/lexical access structures that shape ranking."
          }
        },
        "records": [
          "RTE-2",
          "OBJ-5",
          "OBJ-4"
        ],
        "note": "Both forms belong to qualifying trace-fed routes; no trained-parameter update is established."
      },
      "faithfulness_tested": {
        "assessment": "not-determinable",
        "values": [],
        "evidence": {},
        "records": [
          "CLM-3"
        ],
        "note": "No retained execution evidence was supplied or generated. Source implementation and a chat example cannot establish dependence on recalled content or a system-wide negative about experiments."
      }
    }
  }
}
---

# Mem0 agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-mem0-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/mem0.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-mem0-01/memory-report.md`

**Memory analysis report SHA-256:** feb04b83ddd4329c9b395b9c8c07d6aa419056068afc087b3ede4d429cac4129

Run AAS-2026-09-27-mem0-01 uses the source-native name Mem0. The intended retained result is `kb/reports/retained/agentic-system-analysis/AAS-2026-09-27-mem0-01/result.md`. Only the completed run state establishes publication.

## Boundary and evidence

Evidence basis: static inspection of implementation and shipped documentation at `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`, inspected 2026-09-27. This analysis characterizes the synchronous OSS Python `Memory` API and relevant shipped adapters/examples. It supports decisions about what this subsystem owns and what evidence its memory routes supply. It is a memory/knowledge/context-engineering system under a subsystem-only boundary, not an enclosing agent runtime.

Included are ordinary inferred addition, raw insertion, procedural summaries, retrieval, history, entity access structures, explicit revision and deletion, configuration and provider hooks. The public example is inspected as an integration recipe, not an observed host execution. The asynchronous class, hosted service internals, REST server authentication, JavaScript SDK and UI, excluded graph demonstrations, and enclosing agent execution are outside the functional boundary. These exclusions prevent conclusions about their algorithms, security guarantees, lifecycle or deployed behavior. Provider implementations inspected here describe SDK calls and local model loading; inaccessible model internals prevent claims about their weights, private reasoning, provider guarantees or training. Backing-store families remain configurable; no live persistence, retrieval quality, multi-tenant isolation or performance experiment was executed.

The only external evidence identity is the pinned repository. Commit-addressed reads use `/home/zby/llm/commonplace/related-systems/mem0ai--mem0`; worktree state and current HEAD are not evidence. No prior review or analytical result was read. Existing destination eligibility was inspected only by the publication command.

## Source register

| Source ID | Kind | Identity/location | Revision | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/mem0ai/mem0` | `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` | Implementation; separately labelled doctrine/design in README and prompts | Synchronous `mem0/memory/main.py`, `mem0/memory/storage.py`, `mem0/memory/utils.py`, `mem0/utils/scoring.py`, `mem0/proxy/main.py`, selected FAISS/PGVector/Redis storage adapters, configuration/prompts, OpenAI LLM/embedding adapters, factory, entity extraction and spaCy loader, optional rerankers, README | Full paths on records; all quotes attributed to this commit | No observed run or causal experiment; no hosted/provider internals; scope-specific unknowns below |

## Shared records

### Components

### CMP-1 — Synchronous Memory coordinator

Implementation conclusion status: wired. Python code stores a configured vector adapter, LLM adapter, embedding adapter and SQLite history manager; optional reranker is initialized by configuration. The subsystem owns sequencing inside a returning method invocation; the caller owns the next invocation. Evidence: SRC-1 `mem0/memory/main.py:488-514`.

> self.llm = LlmFactory.create(self.config.llm.provider, self.config.llm.config)
> self.db = SQLiteManager(self.config.history_db_path)
> --- `mem0/memory/main.py:499-500` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

The provider-error path is distinct from parse failure: the former propagates an exception for caller fallback, while the latter can yield an empty extraction. This is a control distinction, not proof that empty results mean no memorable content. Evidence: SRC-1 `mem0/memory/main.py:966-991`.

> raise LLMError(f"LLM extraction failed: {e}") from e
> --- `mem0/memory/main.py:971` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> except Exception as e:
>     logger.error(f"Error parsing extraction response: {e}")
>     extracted_memories = []
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-2 — Extraction and procedural-summary language model

Adapter call conclusion status: wired. The inspected OpenAI adapter sends messages and configured model to a chat-completion endpoint. Default identity is the mutable model name `gpt-5-mini`, with configurable provider endpoint and an OpenRouter alternative; exact weight/version pinning conclusion status: uninspected. Parameter changes inside the provider during operation: uninspected. The adapter exposes inference calls, not evidence of provider weight training. Custom providers admitted through RTE-1 are outside this specific adapter characterization. Evidence: SRC-1 `mem0/llms/openai.py:38-54,109-149`.

> if not self.config.model:
>     self.config.model = "gpt-5-mini"
> --- `mem0/llms/openai.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> response = self.client.chat.completions.create(**params)
> --- `mem0/llms/openai.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-3 — Embedding model

Inference call conclusion status: wired. The OpenAI adapter defaults to `text-embedding-3-small`, takes text and returns a float vector. Representational form: distributed-parametric component; its output vector is an access structure, not retained model weights. Exact weight/version pinning and provider parameter changes: uninspected. Configured model names and endpoints do not identify immutable provider weights. Evidence: SRC-1 `mem0/embeddings/openai.py:11-55`.

> self.config.model = self.config.model or "text-embedding-3-small"
> --- `mem0/embeddings/openai.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> return self.client.embeddings.create(**kwargs).data[0].embedding
> --- `mem0/embeddings/openai.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-4 — spaCy entity and lemma pipelines

Conditional loading/inference conclusion status: wired. The loader requests `en_core_web_sm`, downloads it if missing, and loads the full or lemma pipeline. The entity extractor returns an empty list if loading fails. The model-name reference is not an immutable package/model hash; exact installed parameters and training internals: uninspected. Selected wrappers use inference, while parameter change during operation beyond loading is uninspected. This model can change retrieval access structures; it is not a model trained by memory accumulation. Evidence: SRC-1 `mem0/utils/spacy_models.py:20-65,81-84`; `mem0/utils/entity_extraction.py:751-758`.

> download("en_core_web_sm")
> --- `mem0/utils/spacy_models.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> _nlp_full = spacy.load("en_core_web_sm")
> --- `mem0/utils/spacy_models.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> nlp = get_nlp_full()
> if nlp is None:
>     return []
> --- `mem0/utils/entity_extraction.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-5 — Optional reranker components

Conditional integration conclusion status: wired: search uses a configured reranker only when requested, and falls back to original results on failure. Inspected model-backed alternatives are an LLM relevance scorer, a local SentenceTransformer CrossEncoder and Cohere's remote rerank API. Hugging Face and ZeroEntropy are registered alternatives whose internal implementations are uninspected here; they prevent an exhaustive provider-level reliability assessment. Local CrossEncoder is loaded by model name without an inspected immutable revision; remote identities are configured endpoint/model names. Exact parameter identity and provider-side changes: uninspected. Inspected wrappers perform inference rather than showing parameter training. Evidence: SRC-1 `mem0/utils/factory.py:226-280`; `mem0/reranker/llm_reranker.py:60-95,135-157`; `mem0/reranker/sentence_transformer_reranker.py:43-85`; `mem0/reranker/cohere_reranker.py:33-74`; `mem0/memory/main.py:1512-1518`.

> self.model = CrossEncoder(self.config.model, device=self.config.device)
> --- `mem0/reranker/sentence_transformer_reranker.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> "Given a query and a document, score how relevant the document is to the query.\n\n"
> --- `mem0/reranker/llm_reranker.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-6 — Configured storage alternatives and coverage

Implementation conclusion status: wired. Evidence: SRC-1 `mem0/configs/base.py:29-57`; `mem0/vector_stores/configs.py:6-68`; `mem0/memory/main.py:488-514,559-580`; `mem0/vector_stores/faiss.py:146-173,227-249`; `mem0/vector_stores/pgvector.py:262-277,311-329`; `mem0/vector_stores/redis.py:79-146`. Registry alternatives include qdrant (default), chroma, pgvector, pinecone, mongodb, milvus, baidu, cassandra, neptune, upstash_vector, azure_ai_search, azure_mysql, redis, valkey, databricks, elasticsearch, vertex_ai_vector_search, opensearch, supabase, weaviate, faiss, langchain, s3_vectors, turbopuffer and oracledb. This is a registry inventory, not verification of every adapter's semantics.

FAISS writes an index and JSON docstore; PGVector persists vector/payload tuples in PostgreSQL; Redis delegates structured data insertion to its index. The complete substrate union remains partial because most adapters were not inspected in depth. The report positively supports vector, SQLite, files and RDBMS. It does not infer graph substrate merely from the neptune registry entry or rule out additional KV/service-object/in-memory backends. SQL/vector providers do not imply learning model weights.

>             index_path = f"{self.path}/{self.collection_name}.faiss"
>             json_docstore_path = f"{self.path}/{self.collection_name}.json"
> 
>             faiss.write_index(self.index, index_path)
> --- `mem0/vector_stores/faiss.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

>             with open(json_docstore_path, "w", encoding="utf-8") as f:
>                 json.dump(data, f, indent=2)
> --- `mem0/vector_stores/faiss.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

>                 CREATE TABLE IF NOT EXISTS {} (
>                     id UUID PRIMARY KEY,
>                     vector vector({}),
>                     payload JSONB
>                 );
> --- `mem0/vector_stores/pgvector.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### Operative objects

### OBJ-1 — Shipped extraction and procedural-summary instructions

Source-native objects: `ADDITIVE_EXTRACTION_PROMPT`, `AGENT_CONTEXT_SUFFIX`, `PROCEDURAL_MEMORY_SYSTEM_PROMPT`, and caller custom instructions. Form: natural-language instruction encoded in repository Python strings. Static shipped guidance is outside the accumulated-memory comparison scope. It defines a proposed solution to preserving useful context: extract self-contained memories from new messages while using prior memories to avoid repetition and resolve references. Procedural guidance instead asks for a continuation summary preserving execution outputs. Consumption conclusion status: wired via the extraction and procedural model messages. Instruction compliance remains uninspected without model output.

The instructions expose named sections and rules that an operator can inspect and replace; this is textual addressability. Their historical reasons and test record are not made available by their role as prompt text. A caller may provide substitute guidance; evidence that the subsystem criticizes and revises its own guidance is uninspected. Evidence: SRC-1 `mem0/configs/prompts.py:326-359,468-518,947-958`; `mem0/memory/main.py:943-964,2018-2031`.

> Use these ONLY for deduplication and linking — do NOT extract new memories from Existing Memories. Your extractions must come exclusively from New Messages.
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### OBJ-2 — Memory records and access payload

Implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/main.py:1017-1041,1975-2005,1703-1745`. Stored data consists of language text, UUID, content hash, creation/update timestamps, identity and caller metadata, lemmatized text and an embedding. An API result displays `memory` from payload `data`; it does not substitute an unrelated readable summary for an opaque consumed payload. Numeric embeddings are access data, not updated model parameters. Data comes from extraction, direct authoring, image descriptions or procedural summaries. Later consumers are the extractor, search/ranking code and optionally an external answer application. Authority is knowledge for language content and ranking for access structures. The extracted `attributed_to` label records model-assigned origin, not independent verification.

>             memory_id = str(uuid.uuid4())
>             mem_metadata = deepcopy(metadata)
>             mem_metadata["data"] = text
>             mem_metadata["text_lemmatized"] = text_lemmatized
>             mem_metadata["hash"] = mem_hash
>             if "created_at" not in mem_metadata:
>                 mem_metadata["created_at"] = datetime.now(timezone.utc).isoformat()
>             mem_metadata["updated_at"] = mem_metadata["created_at"]
>             if mem.get("attributed_to"):
>                 mem_metadata["attributed_to"] = mem["attributed_to"]
> --- `mem0/memory/main.py:1030-1039` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### OBJ-3 — SQLite message window and change history

Implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/storage.py:102-148,257-324`; `mem0/configs/base.py:42-45`; `mem0/memory/main.py:920-955,1960-1973`. The default on-disk history database contains separate history and messages tables. History retains old/new text, event, timestamps and deletion status; the public history method returns changes for an ID. The messages table copies role/content/name and scope, then deletes rows beyond the most recent ten in that scope. Raw-message retention is not itself trace learning. Its later automatic supply into extraction is knowledge context. The prompt builder further truncates each historical content string to 300 characters (`mem0/configs/prompts.py:965-991`). Neither cap is a token budget for new messages or complete memories.

>                     DELETE FROM messages WHERE session_scope = ? AND id NOT IN (
>                         SELECT id FROM (
>                             SELECT id FROM messages WHERE session_scope = ? ORDER BY created_at DESC LIMIT 10
>                         )
>                     )
>                 """,
>                     (session_scope, session_scope),
> --- `mem0/memory/storage.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### OBJ-4 — Entity collection and retained memory links

Implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/main.py:559-648,1100-1204,1747-1827`; `mem0/utils/entity_extraction.py:1-15`; `mem0/utils/scoring.py:94-139`. A lazily created collection uses the same configured vector adapter, with entity text/type, identity filters, embedding and linked memory IDs. The inferred-add pipeline extracts entities from newly persisted facts, merges exact or similarity-at-least-0.95 matches and unions the IDs. This qualifies as dedup over retained entities, unlike mere hash suppression during fact acquisition. Query entities select retained entity rows; their linked IDs change memory ranking. The query path processes at most eight entities, with up to 500 matches per entity and four concurrent search workers. Failures can fall back to ranking without these boosts. No explanatory reason for a link or merge is retained for later diagnosis.

>                         semantic_match = matches[0] if matches and matches[0].score >= 0.95 else None
>                         match = exact_match or semantic_match
>                         if match:
>                             # Update existing entity
>                             payload = match.payload or {}
>                             linked = set(payload.get("linked_memory_ids", []))
>                             linked |= memory_ids
>                             payload["linked_memory_ids"] = sorted(linked)
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

>                         num_linked = max(len(linked_memory_ids), 1)
>                         memory_count_weight = 1.0 / (1.0 + 0.001 * ((num_linked - 1) ** 2))
>                         boost = similarity * ENTITY_BOOST_WEIGHT * memory_count_weight
> 
>                         for memory_id in linked_memory_ids:
>                             if memory_id:
>                                 memory_key = str(memory_id)
>                                 memory_boosts[memory_key] = max(memory_boosts.get(memory_key, 0.0), boost)
> --- `mem0/memory/main.py:1815-1822` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### OBJ-5 — Optional procedural summary

Implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/main.py:853-864,2007-2050`; `mem0/configs/prompts.py:326-359`. Requires agent_id and procedural memory type to enter the dedicated branch; it runs before ordinary inference/vision processing. The supplied interaction messages enter an LLM call and the returned text is embedded/stored with memory_type. Empty summaries raise ValueError. Generic search and the next inferred add can select it from the same collection; no specialized procedure executor or task-resumption consumer is established. The prompt asks for objectives, action results, findings and errors, but does not enforce preservation of causal reasons. Any rationale that survives inside the summary can be read as text by a later generic consumer; there is no separate reason field or diagnostic reader. Its requested complete verbatim execution record is a prompt demand, not a fidelity guarantee.

>         metadata = {**metadata, "memory_type": MemoryType.PROCEDURAL.value}
>         embeddings = self.embedding_model.embed(procedural_memory, memory_action="add")
>         memory_id = self._create_memory(procedural_memory, {procedural_memory: embeddings}, metadata=metadata)
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

>   2. **Action Result (Mandatory, Unmodified)**:
>      - Immediately follow the agent action with its exact, unaltered output.
>      - Record all returned data, responses, HTML snippets, JSON content, or error messages exactly as received. This is critical for constructing the final output later.
> 
>   3. **Embedded Metadata**:
>      For the same numbered step, include additional context such as:
>      - **Key Findings**: Any important information discovered (e.g., URLs, data points, search results).
>      - **Navigation History**: For browser agents, detail which pages were visited, including their URLs and relevance.
>      - **Errors & Challenges**: Document any error messages, exceptions, or challenges encountered along with any attempted recovery or troubleshooting.
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### Routes

### RTE-1 — Caller configuration and provider admission

Implementation conclusion status: wired. Trigger/principal: an embedding application supplies configuration or registers an LLM provider. The Python factory owns the next step: resolve provider string, validate config and import the named class. The proposed change is executable provider code or caller-supplied extraction guidance; the caller proposes and selects it. The factory can reject an unknown provider or invalid config, but that is compatibility admission, not a judgment of semantic correctness. Capabilities execute under the host process and its credentials. No deployed isolation envelope was inspected. Guidance is configuration and caller intent; its rationale and objective are not prescribed by this route.

Persistence: configuration and class mappings live in the caller process; package/config persistence is caller-owned. Return: an instantiated provider or error. Later read-back: factory mappings are read during construction; accumulated-memory read-back is inapplicable here. Delegated visibility: the adapter receives submitted context; broader host access is uninspected. Selector: provider name and config. Invalidation: caller replaces config or process; rollback is caller-managed. Effect: subsequent calls use the chosen adapter. Recovery: import/config errors propagate. Guarantee strength: code-level compatibility checks within factories, not a sandbox or deployment guarantee. Alternate registered providers and callbacks prevent attributing OpenAI-specific constraints to all paths. Evidence: SRC-1 `mem0/utils/factory.py:29-32,69-84,128-139`; `mem0/memory/main.py:488-505`.

> module_path, class_name = class_type.rsplit(".", 1)
> module = importlib.import_module(module_path)
> return getattr(module, class_name)
> --- `mem0/utils/factory.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> cls.provider_to_class[name] = (class_path, config_class)
> --- `mem0/utils/factory.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### RTE-2 — Inferred add and automatic context reuse

Implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/main.py:760-879,881-991,993-1098,1206-1220`; `mem0/configs/prompts.py:468-516,947-1062`; `mem0/memory/utils.py:61-76,161-232`. Trigger: caller invokes add with infer=True. Producer: extraction LLM, then embedder and entity compiler. Input: submitted textual conversation, optional image-derived description, retained scoped message window and top-ten semantically selected old memories. Persistence: new vector records, history entries, entity links and the updated ten-message window. Later consumer: subsequent extraction LLM, plus query ranking and the external application afforded in RTE-5. Implementation conclusion status: wired.

Selection is automatic relative to the extraction model: the caller requests a write, while the pipeline chooses memory context. The history selector performs an actual scope match; the existing-memory selector embeds parsed new messages. The extraction model receives old text as user-prompt sections. There is no requirement that the model explicitly request memory. Identifier and embedding signals are therefore wired push evidence.

>         # Phase 0: Context gathering
>         session_scope = _build_session_scope(filters)
>         last_messages = self.db.get_last_messages(session_scope, limit=10)
>         parsed_messages = parse_messages(messages)
> 
>         # Phase 1: Existing memory retrieval
>         search_filters = {k: v for k, v in filters.items() if k in ("user_id", "agent_id", "run_id") and v}
>         query_embedding = self.embedding_model.embed(parsed_messages, "search")
>         existing_results = self.vector_store.search(
>             query=parsed_messages,
>             vectors=query_embedding,
>             top_k=10,
>             filters=search_filters,
>         )
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

>         user_prompt = generate_additive_extraction_prompt(
>             existing_memories=existing_memories,
>             new_messages=parsed_messages,
>             last_k_messages=last_messages,
>             custom_instructions=custom_instr,
>         )
> 
>         try:
>             response = self.llm.generate_response(
>                 messages=[
>                     {"role": "system", "content": system_prompt},
>                     {"role": "user", "content": user_prompt},
>                 ],
>                 response_format={"type": "json_object"},
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

The source's extraction prompt requires ADD-only facts and attribution from both user and assistant messages. Its optional summary/recent-extraction sections are empty in this synchronous call; their presence in the prompt builder does not establish a maintained profile summary. The code retains only selected fields from extraction output, not arbitrary proposed link arrays or reasons. Content hashes suppress exact repetition within the retrieved neighborhood and current batch, not across the entire collection. Parse failures become no extracted memories while preserving recent messages; LLM transport failures raise, and a complete insertion failure raises VectorStoreError. Partial vector insertion can leave a subset accepted; history/entity failures are not an atomic rollback of the primary insertion.

Vision-enabled input uses a generated text description before ordinary extraction. With vision disabled, text blocks are retained and image-only blocks are skipped. This supplies an optional compilation route but no retained visual embedding or opaque image memory object within this boundary. The ordinary parser accepts system/user/assistant text and skips contentless tool-call messages; it does not establish tool-trace learning merely because a message once accompanied a tool invocation.

The selected vision preprocessing is evidenced directly:

> response = llm.generate_response(messages=messages)
> return response
> --- `mem0/memory/utils.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> description = get_image_description(msg, llm, vision_details)
> returned_messages.append({"role": role, "content": description})
> --- `mem0/memory/utils.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

Derived facts do not require a source-message pointer or the reason for a recommendation. `attributed_to` and caller metadata may help provenance, but no later reader reconstructs justifications from the history table. User text, assistant suggestions and existing facts can all affect subsequent extraction, so accuracy instructions are not a trust proof.

> You are a Memory Extractor — a precise, evidence-bound processor responsible for extracting rich, contextual memories from conversations. Your sole operation is ADD: identify every piece of memorable information and produce self-contained, contextually rich factual statements.
> 
> You extract from BOTH user and assistant messages. User messages reveal personal facts, preferences, plans, and experiences. Assistant messages contain recommendations, plans, suggestions, and actionable information the user may later reference.
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

Route audit for RTE-2: immediate terminal output is a list of ADD events, or an exception/empty list under the inspected failure cases. The next-step owner is synchronous Python except model content selection. External provider visibility is the assembled prompt, including selected retained text; provider handling beyond the call is uninspected. Persistence and selection are described above. Invalidation is manual withdrawal/expiry or window eviction; automatic extraction does not replace old facts. Effect is new stored content and possible later delivery, while activation is uninspected. Admission uses OBJ-1 guidance, parsing, embedding availability, bounded duplicate suppression and store confirmation; the model proposes, code/store reject, and the caller may later edit/delete. There is no rollback across vector/history/entity stores. Guarantee strength: protocol and best effort across stores, conditional on provider contracts. Explanatory rationale and formulated criticism are not required output fields; their presence inside model processing is uninspected.

### RTE-3 — Requested search and ranking

Implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/main.py:1393-1536,1642-1745`; `mem0/utils/scoring.py:94-139`. Trigger: an application requests search with a query and at least one identity filter. The API embeds the query, fetches max(4*top_k, 60) semantic candidates and asks the adapter for keyword scores. Expired entries are suppressed by default. Entity links add boosts; semantic score thresholding occurs before combining. Only semantic candidates enter the final ranking pool, so keyword-only discoveries are not automatically additional candidates. Default top_k is 20; configured reranking is opt-in and falls back on error. The API returns text, metadata and optionally score details to the requesting application. The concrete application role is shown by RTE-5; a callable search API alone would not prove an enclosing agent route.

>         # Step 3: Semantic search (over-fetch for scoring pool)
>         internal_limit = max(limit * 4, 60)
>         semantic_results = self.vector_store.search(
>             query=query, vectors=embeddings, top_k=internal_limit, filters=filters
>         )
> 
>         # Step 4: Keyword search (if store supports it)
>         keyword_results = self.vector_store.keyword_search(
>             query=query_lemmatized, top_k=internal_limit, filters=filters
>         )
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

>         semantic_score = result.get("score") or 0.0
>         if semantic_score < threshold:
>             continue
> 
>         mem_id_str = str(mem_id)
>         bm25_score = bm25_scores.get(mem_id_str, 0.0)
>         entity_boost = entity_boosts.get(mem_id_str, 0.0)
> 
>         raw_combined = semantic_score + bm25_score + entity_boost
>         combined = min(raw_combined / max_possible, 1.0)
> --- `mem0/utils/scoring.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

Route audit for RTE-3: next-step owner is retrieval/scoring code, with optional CMP-5 model relevance judgment; policy is numeric ranking rather than fact verification. State is retained payload/access data; immediate output is ranked memory records. The query does not itself create durable memory. Later consumption is RTE-2 or the distinct afforded RTE-5, not a guaranteed consequence of every search. Delegated visibility is candidate text/query to a configured reranker, conditional on `rerank=True`. Selection, expiry and budget are explicit above; activation and relevance benefit are uninspected. Provider errors may propagate; reranking failure falls back. Guarantee strength: code-level filtering and ordering conditional on adapter responses, not truth or host isolation.

### RTE-4 — Explicit authoring, revision and withdrawal

Implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/main.py:881-916,1829-1881,1904-1958,2052-2140,1340-1391`. The caller can add text with infer=False, update text/metadata by memory ID, clear/set expiration or delete current memory. Raw addition skips system messages and retains role/actor metadata. Update re-embeds text and records the old/new value; text changes also refresh entity links. Delete removes the vector record and retains a DELETE history entry with old text. Expiration hides records in default search/get_all; get by ID remains available without that expiration filter (`mem0/memory/main.py:1222-1267`). These are evolution and withdrawal controls, not automatic conflict resolution. Entity cleanup is best effort and explicitly skips work if the entity collection has not been initialized in this instance (`mem0/memory/main.py:652-705`). A caller can edit facts directly; no human approval gate is required by these methods.

>         self.db.add_history(
>             memory_id,
>             prev_value,
>             data,
>             "UPDATE",
>             created_at=new_metadata["created_at"],
>             updated_at=new_metadata["updated_at"],
>             actor_id=new_metadata.get("actor_id"),
>             role=new_metadata.get("role"),
>         )
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

>         self.vector_store.delete(vector_id=memory_id)
>         self.db.add_history(
>             memory_id,
>             prev_value,
>             None,
>             "DELETE",
>             created_at=created_at,
>             updated_at=updated_at,
>             actor_id=existing_memory.payload.get("actor_id"),
>             role=existing_memory.payload.get("role"),
>             is_deleted=1,
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

Route audit for RTE-4: the caller owns proposed text/metadata/withdrawal and its reasons; Python and store operations admit compatible changes or raise for missing/invalid input. Memory identity metadata is preserved against caller metadata overrides. Raw addition returns ADD records; update/delete return success messages after their writes. Persistence reaches the vector store and history in separate steps; the old value is a history record, not automatic rollback. Later read-back occurs through RTE-2 or RTE-3; deletion removes the primary current record, while expiry affects normal search/listing. Provider visibility includes text sent for embedding. No automatic expiry is inferred for by-ID get. Operator APIs permit correction, but evidence of content-directed criticism motivating any actual edit is uninspected. Guidance is caller-supplied content; it may express a rule or theory, but the API does not require one. The caller selects retention and can delete/replace it; no internal answer oracle or human approval gate is established. Guarantee strength: explicit API protocol, with best-effort entity cleanup.

### RTE-5 — Documented chat application consumer

Implementation conclusion status: wired. Evidence: SRC-1 `README.md:202-236`. Conclusion status: afforded. The named chat_with_memories application searches with the current user message and user_id, requests three memories, renders their language content into the answer model's system prompt, then writes the completed conversation after the answer. It provides a concrete consumer role and supports pull from the application's viewpoint, followed by automatic supply to the answer model. It is documented code, not an executed deployment or retained behavioral test. Placement under system role supplies knowledge to answer from; it does not prove that arbitrary recalled content acquires instruction authority. No token limit bounds the three memories. Successive requests are explicit, but distinct task/project horizons are not.

> def chat_with_memories(message: str, user_id: str = "default_user") -> str:
>     # Retrieve relevant memories
>     relevant_memories = memory.search(query=message, filters={"user_id": user_id}, top_k=3)
>     memories_str = "\n".join(f"- {entry['memory']}" for entry in relevant_memories["results"])
> 
>     # Generate Assistant response
>     system_prompt = f"You are a helpful AI. Answer the question based on query and memories.\nUser Memories:\n{memories_str}"
>     messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": message}]
>     response = openai_client.chat.completions.create(model="gpt-5-mini", messages=messages)
> --- `README.md` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

>     # Create new memories from the conversation
>     messages.append({"role": "assistant", "content": assistant_response})
>     memory.add(messages, user_id=user_id)
> --- `README.md` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

Route audit for RTE-5: the application owns each chat turn and selects by current message plus user scope; the answer model owns generated answer content. Immediate return is the assistant response; the conversation is then submitted for persistent memory acquisition before return. The next call reuses accumulated memory. Selected text is visible to the answer-model provider; host/provider permissions are outside scope. Invalidation follows memory API behavior, with no example-specific rollback or retry. Force is contextual knowledge, not demonstrated obedience to arbitrary embedded instructions. Activation, deployed effects, error recovery and benefit are uninspected. Guarantee strength: documented integration affordance.

### RTE-6 — Incompatible OSS proxy route

Compatibility-check conclusion status: wired. Intended successful delivery conclusion status: uninspected. Evidence: SRC-1 `mem0/proxy/main.py:30-35,100-109,149-186`; `mem0/memory/main.py:165-172,760-773,1449-1450`. The proxy selects OSS Memory when no API key is supplied. Its intended path starts a write thread, searches using the last six messages, then places retrieved facts into the user message before LiteLLM completion. However its add call passes unsupported filters, and its search call passes top-level user_id/agent_id/run_id that this pinned Memory rejects. Thus the intended OSS answer-delivery path is not a working wired witness. This is a code-grounded compatibility finding, not an observed failure. Hosted behavior is outside scope. The incompatible proxy cannot establish automatic successful writes, delivery, instruction authority or timing values.

>         return self.mem0_client.search(
>             query="\n".join(message_input),
>             user_id=user_id,
>             agent_id=agent_id,
>             run_id=run_id,
>             filters=filters,
>             top_k=top_k,
>         )
> --- `mem0/proxy/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> def _reject_top_level_entity_params(kwargs: Dict[str, Any], method_name: str) -> None:
>     """Reject top-level entity parameters - must use filters instead."""
>     invalid_keys = ENTITY_PARAMS & set(kwargs.keys())
>     if invalid_keys:
>         raise ValueError(
>             f"Top-level entity parameters {invalid_keys} are not supported in {method_name}(). "
>             f"Use filters={{'user_id': '...'}} instead."
>         )
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

Route audit for RTE-6: the proxy caller initiates completion; a daemon thread attempts the write and the foreground call requests recall. Its immediate effect at the inspected OSS signatures is an incompatible call path, so successful terminal completion, persistence and later visibility are not established. Intended selectors use the last six messages and supplied identities; intended provider visibility would be formatted facts, but the foreground rejection prevents treating that as delivered. Recovery/rollback and expired-result handling beyond the rejected call are uninspected. Guarantee strength: no claimed successful-delivery guarantee. This route remains explicitly included as a failed compatibility witness, with hosted behavior excluded.

### RTE-7 — Procedural-summary admission and generic reuse

Implementation conclusion status: wired. This is the route associated with OBJ-5, not another object. Caller-supplied agent_id plus procedural memory type triggers a dedicated branch before ordinary extraction. CMP-2 proposes summary text using the procedural guidance in OBJ-1; the code strips fences, rejects empty output, embeds the summary and persists it through the same create helper. The code and backing store can veto invalid/failed persistence, but do not check verbatim fidelity or summary truth. Immediate result is an ADD event. Provider visibility includes the submitted interaction and instruction. Persistence is language summary plus metadata/history; later read-back is possible through the generic collection query used by RTE-2 and RTE-3. Selection is generic similarity and identity scope, not a specialized task-resumption selector. Invalidation is RTE-4; rollback is not a multi-store transaction. Recovery consists of propagating generation/empty-output/storage failure. Guarantee strength: nonempty-content protocol and best-effort language instruction. Activation and continuation benefit are uninspected.

The guidance asks to preserve task objective, actions, results and errors. Retained rationale is optional text, not an enforced causal explanation or criticism record. The summary derives from supplied messages, not from an independently checked answer oracle. A later generic extractor can receive this text, but consumption by an actual continuation agent and the task horizon remain uninspected. Theory-builder conditions 1–4 are addressed separately below rather than inferred from the procedural label. Evidence: SRC-1 `mem0/memory/main.py:853-864,2007-2050`; OBJ-5; RTE-2.

### Claims

### CLM-1 — README learning and managed benchmark claims

Claim conclusion status: claimed. README describes continuous learning and publishes benchmark scores, but explicitly says those scores are for the managed platform and include proprietary optimizations. The inspected OSS implementation supports memory accumulation and read-back; hosted benchmark execution is outside SRC-1's inspected evidence layers. Learning through criticism of consumed theories and measured OSS improvement remain uninspected. Evidence: SRC-1 `README.md:47-81`.

> Scores reflect Mem0's managed platform, which includes proprietary optimizations not available in the open-source SDK; open-source users should expect directionally similar gains but not identical numbers.
> --- `README.md` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> It remembers user preferences, adapts to individual needs, and continuously learns over time
> --- `README.md` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CLM-2 — Legacy add docstring versus additive implementation

Documentation conclusion status: claimed. The `add` docstring still describes an LLM deciding add/update/delete, while the inspected inferred branch and extraction instructions use ADD-only output. Explicit caller update/delete remain separate routes. This is a documentation/implementation mismatch, not evidence that a hidden automatic revision loop runs. Evidence: SRC-1 `mem0/memory/main.py:793-796,942-964,1048-1075,1207-1212`; OBJ-1.

> If True (default), an LLM is used to extract key facts from
> 'messages' and decide whether to add, update, or delete related memories.
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CLM-3 — Evidence ceiling for faithfulness and benefit

Evidence conclusion status: uninspected. Evidence: SRC-1 `README.md:209-224`; `mem0/configs/prompts.py:326-359`; `mem0/memory/main.py:2034-2045`. The inspected implementation and example establish retention and possible delivery, not activated dependence on particular recalled facts, complete procedural fidelity or improved outcomes. No retained execution experiment was supplied or run. This prevents a yes faithfulness classification, but does not establish that Mem0 has never been tested elsewhere. faithfulness_tested is not-determinable, not an unsupported universal no.

>         if not procedural_memory:
>             raise ValueError(
>                 "The LLM returned no content for the procedural memory summary. "
>                 "The model may have declined the request or returned an empty response."
>             )
> --- `mem0/memory/main.py:2034-2038` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### Evidenced absences

No broad absence is asserted from uninspected provider or host behavior. Specialist bounded absence records, if any, follow.

### Behavioral-authority paths

### BAP-1 — Static extraction policy into model messages

Implementation conclusion status: wired. Consumer: extraction/summary LLM. Channel: system prompt and caller custom instructions. Force: instruction; not formal enforcement or epistemic warrant. Horizon: one generation, repeated while the same configuration is used. The directive in OBJ-1 constrains intended content; provider compliance and behavioral activation are uninspected. Evidence: SRC-1 `mem0/memory/main.py:943-964,2018-2031`; OBJ-1.

### BAP-2 — Retained knowledge into extraction

Implementation conclusion status: wired. Consumer: CMP-2 extraction model; channel: generated user prompt with existing memories and previous messages; force: knowledge/context under OBJ-1 instructions, not epistemic certification. Horizon: a later inferred addition using RTE-2. Selector uses scope-matched history and embedding-selected facts, not an explicit model recall request. Activation is uninspected. Evidence: SRC-1 `mem0/memory/main.py:920-964`; OBJ-2; OBJ-3; RTE-2.

### BAP-3 — Retained access structures into ranking

Implementation conclusion status: wired. Consumer: retrieval/scoring code; channel: vector and lexical matches plus entity-to-memory links; force: ranking. Horizon: subsequent search with the configured backend and available NLP. A numeric rank is operational selection, not truth endorsement. Evidence: SRC-1 `mem0/memory/main.py:1642-1701,1747-1827`; `mem0/utils/scoring.py:94-139`; OBJ-4; RTE-3.

### BAP-4 — Recalled facts into an answer model

Conclusion status: afforded. Consumer: answer model in the README chat application; channel: system-message memory text assembled by RTE-5; force: contextual knowledge for an answer; horizon: the current response, with later conversation retention through RTE-2. The recipe alone does not show activation, obeying embedded instructions or benefit. Evidence: SRC-1 `README.md:209-224`; RTE-5.

## Runtime account

The ordinary invocation begins with the embedding application constructing CMP-1 and calling `add(messages, user_id=...)`. It normalizes identities and message shapes, reads recent scoped messages and related retained facts, and submits the assembled context and OBJ-1 instructions to CMP-2. The method parses model output, embeds proposed texts with CMP-3, filters missing/duplicate entries, persists confirmed records, attempts history/entity maintenance, saves recent messages and returns event records. Model generation proposes content; Python and store responses govern persistence. No internal scheduler keeps pursuing a goal after return. The next call, application response and external action remain caller-owned.

Subsequent `search` calls combine semantic candidates, optional keyword scores and entity boosts, apply threshold/top-k and expiry rules, optionally rerank with CMP-5, then return memory text and metadata. The README integration recipe requests three memories, embeds returned text in the answer model's system message, then feeds the completed conversation back into `add`. That recipe establishes an afforded enclosing-consumer route; it is not an executed conversation in this analysis. Source evidence and memory route identities are registered below through specialist integration.

The material alternatives are direct raw insertion (`infer=False`), procedural-summary creation, explicit update/delete, by-ID retrieval/history, list retrieval, configurable providers, optional NLP/keyword/reranker features, and adapter/example callers. The procedural branch selects before ordinary extraction; raw insertion bypasses extraction judgment. A guarantee attributed to inferred addition therefore does not cover either alternative by default. RTE-1 admits extension code under the host's permissions; a model adapter callback can also execute application code. No assumption about host approval policy, delegation, shell isolation or deployed grants follows from library identity filters.

Four static forcing cases challenge the ordinary route:

1. **Unavailable model versus unusable output.** Extraction provider exceptions raise `LLMError`, allowing caller retry/fallback. Parse failure instead produces an empty extraction and saves messages. The code distinguishes a provider failure from empty extraction, but malformed content and no facts can still share an empty return. Evidence: SRC-1 `mem0/memory/main.py:956-991`.
2. **Partial persistence.** Batch insert failure triggers individual inserts. Only confirmed records enter the return list; failure to insert any raises `VectorStoreError`. History and entity failures may be logged after vector persistence. This is a best-effort multi-store sequence, not an inspected cross-store transaction or rollback guarantee. Evidence: SRC-1 `mem0/memory/main.py:1052-1098,1191-1212`.
3. **Scope enforcement and alternate entry paths.** Addition requires an identity and strips scope keys from freeform metadata; search requires identity filters. By-ID `get`, `update` and `delete` accept the memory ID directly. These are caller-facing scoping mechanisms, not authentication of the claimed principal. An enclosing server may add authorization, but its policy is excluded. Evidence: SRC-1 `mem0/memory/main.py:360-403,1222-1237,1450-1478,1829-1902`.
4. **Conditional retrieval features.** Missing NLP yields no extracted entities; stores may lack keyword support; expiry is hidden in normal search but can be included with `show_expired`; reranker failure returns original results. No uniform relevance or expiry claim is extended to by-ID reads. Evidence: SRC-1 `mem0/memory/main.py:543-551,1512-1518,1642-1704`; CMP-4; CMP-5.

Execution preflight: **no dynamic check planned**. Considered provider-failure injection, partial-store insertion and an end-to-end recall comparison. Static branches suffice to characterize wiring and bounded enforcement; live models/stores are not authorized and no isolated runtime fixture was needed for this source characterization. All target execution, behavioral activation, retrieval benefit, deployed isolation and timing remain uninspected. Validation commands verify analysis artifacts, not operation of Mem0.

Decision roles are explicit. The caller provides messages, identities, configuration, query and manual revisions; CMP-2 proposes derived content; deterministic code rejects missing texts, hash duplicates and unsuccessful persistence; the configured store decides whether an insert succeeds. Retrieval scores select context and optional models rerank it. No supplied expected answer or reference outcome is consumed by these library routes as an answer oracle. The README benchmark is a separate reported claim, not a runtime oracle. Model-generated relevance or usefulness judgments are not an expected answer. The operating mode is open requests through the memory API; bounded benchmark execution was not inspected. Proposed changes target retained content and access structures, while provider/configuration change is caller-initiated. Fault recovery and per-route revision admission are recorded on the memory routes; no human approval step is inferred from a callable edit API.

Capability, grant and isolation are separate: adapters can call external APIs or local packages, and RTE-1 can load registered Python code; actual credentials, deployment permissions and sandboxing are uninspected. The library guarantees only the code-level checks just identified, conditional on adapter contracts. It does not own the surrounding agent's termination, task planning or action approval.

## Lens scoping

### Memory/context scope

Depth: full. Trigger evidence: SRC-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5 and RTE-2. The frozen specialist input covered the synchronous Memory retained objects, all material write and later-consumer branches, access structures and relevant adapter/example surfaces. Included provider alternatives have partial substrate inspection; arbitrary procedural callers leave source and timing uncertainty. Hosted internals, AsyncMemory and enclosing execution remain excluded. Full depth is warranted because retention, selection and reuse are the subsystem's primary work.

### Epistemic scope

Depth: full. Trigger evidence: SRC-1, OBJ-1 and CLM-1. The inspected subsystem transforms messages into truth-apt memory statements and summaries, retains them, and selects them for later reliance. The question is which transformations and checks support that reliance, distinct from storage and relevance. Included families are imported raw messages, inferred facts, procedural summaries, entity access structures, explicit revision/deletion and retrieval admission. Hosted evaluation, inaccessible model reasoning, enclosing answer generation and uninspected provider adapters prevent stronger semantic or outcome judgments. The lens uses the shared records as a sparse overlay.

## Lens outputs

### Memory/context lens

The specialist inventoried facts and numeric/lexical access payloads (OBJ-2), the SQLite message window and separate change history (OBJ-3), retained entity links (OBJ-4), and procedural summaries (OBJ-5). Internal automatic context reuse in RTE-2 is the strongest wired read-back route: the extractor receives scope-matched history and semantically selected old memories. Requested external recall and automatic answer-model delivery remain afforded through RTE-5. RTE-6 is incompatible at the pin and supplies no successful delivery witness.

The write chain is conversation → extracted text → later extraction or an afforded answer; a second chain compiles facts into retained entities consumed by ranking. Procedural summaries can re-enter generic memory selection, but the task-continuation host is not established. RTE-3 covers search/ranking and RTE-4 covers caller-directed editing/withdrawal. The profile retains natural-language and symbolic forms, automatic and manual authoring, entity deduplication, explicit evolution/invalidation and message-window decay. Acquisition hash suppression is not its dedup witness.

The all-fourteen-axis profile is the mapped specialist profile. Storage remains partial over configurable backends; trace-source and timing remain partial, task horizon and faithfulness testing not determinable. Online timing is afforded by the documented chat recipe, not inferred from synchronous calls. Session identities do not prove cross-task or per-task scope. Neither model-weight learning nor binding procedural instruction authority is inferred from vectors or labels. Rationale can survive only as ordinary retained text; the index and history paths do not create a guaranteed diagnostic explanation. No activated behavior or improved outcome was observed.

### Epistemic lens

#### 1. Source-and-claim boundary

Mem0 at the Run identity pin; source register: SRC-1. Question: what can the inspected retention and selection routes warrant about the content they keep? Assessed families and exclusions are in Epistemic scope. CLM-1 is the learning/benchmark claim; CLM-2 is the stale mutation description; CLM-3 bounds fidelity and behavioral evidence. No candidate-linked run, test outcome or causal comparison is present. Hosted benchmark claims cannot establish OSS warrant or mechanism effects.

#### 2. Epistemic-object overlay

| Object | Epistemic part and candidate content | Lineage/producer/consumer | Gap |
|---|---|---|---|
| OBJ-1 | Proposed method rules about useful extraction and continuation summaries; no per-invocation empirical finding | See OBJ-1 and BAP-1 | Compliance, criticism and reasons for adoption uninspected |
| OBJ-2 | Text: claims about users, assistants, events or recommendations; metadata/access vectors are distinct non-truth-apt operational parts | See OBJ-2, RTE-2, RTE-4, BAP-2 | Source attribution is model output, not independent verification |
| OBJ-3 | Message part: imported claims; history part: recorded API changes, not a judgment that changed content is true | See OBJ-3 and RTE-2; history returned by explicit API | Original source truth and retained-event completeness remain uninspected |
| OBJ-4 | Entity labels and memory-link membership; scoring structures operationally select content | See OBJ-4 and BAP-3 | Semantic equivalence of a model/similarity match is not proved by threshold |
| OBJ-5 | Summary assertions about task objective, actions/results and errors | See OBJ-5 and RTE-7 | Actual summary fidelity/entailment not established by prompt demand |

#### 3. Authority-route ledger

All rows have architectural status **implemented**, except the README consumer rows whose architectural status is **doctrine only** and successful proxy delivery, which is **not determinable** after a source-established incompatible call. All have observed candidate state **no instance observed**. These are separate fields; implementation does not constitute observed acceptance. Generic identities and progression remain on canonical records.

| Route / function | Content/update relation; target, evaluator and timing | Operational force; epistemic license; authority and limits |
|---|---|---|
| RTE-2 / content transformation (import) | acquisition/import of submitted textual messages; on add, parser/vision branch supplies model input | Imported source claims have unknown warrant; copying preserves neither external truth nor a validated origin; BAP-2 |
| RTE-2 / content transformation (vision) | indeterminate: model description replaces image/multimodal input when enabled | Description is candidate content; preservation versus added inference requires paired image/output evidence; BAP-2 |
| RTE-2 / content transformation (extraction) | indeterminate: facts are generated from new messages with selected old context and OBJ-1 policy | Can be preservation/reshaping, contextual derivation or ampliation; output type and fluency do not decide; BAP-2 |
| RTE-2 / check/evidence production | no content change: JSON parsing, missing-text/embedding and retrieved-neighborhood hash tests before insertion | Establish processability and exact-match exclusion in that bounded set, not truth or global dedup; input-error dispositions in CMP-1 |
| RTE-2 / disposition/acceptance | no content change: code omits rejected entries and store confirmations select persisted records | Operational admission to memory, not evidence-consuming epistemic acceptance against a truth criterion; BAP-2 |
| RTE-2 / retention | no content change: confirmed facts and updated message window retained after add | Later availability/knowledge force through BAP-2; neither retention nor model attribution certifies content |
| RTE-2 / operational admission/selection/consumption | no content change: scope and embedding selectors supply old messages/facts to extractor on later add | BAP-2 gives knowledge context; automatic delivery is wired, activation and dependence uninspected |
| RTE-2 / content transformation (entity compilation) | indeterminate for linguistic labels; symbolic union/normalization for access links on accepted fact write | Model/heuristic entities and similarity matches organize memory; a union of IDs is valid set manipulation but proves no semantic sameness; BAP-3 |
| RTE-3 / operational admission/selection/consumption | no content change: semantic threshold, fused scores, expiry and optional reranker decide returned context | BAP-3 ranking permits visibility; it does not verify facts. CMP-5 evaluates relevance, not supplied reference answers |
| RTE-4 / content transformation | acquisition/import for raw authored text and replacement text; metadata update is non-truth-apt policy/content update | Caller authorizes edit; API accepts compatible content without a truth adjudication. Warrant remains caller/source dependent |
| RTE-4 / disposition/acceptance | no content change: compatible update/delete by ID, optional expiry | Current reliance can change or withdraw; this is operational choice, not epistemic refutation |
| RTE-4 / lineage/freshness/recovery | no content change: record old/new values and best-effort entity refresh | Event history establishes intended change bookkeeping, not source proof or automatic rollback |
| RTE-5 / operational admission/selection/consumption | no content change: documented application requests three facts and supplies them to answer model | BAP-4 afforded knowledge use; no observed activation or outcome. Claim link: CLM-1 |
| RTE-6 / operational admission/selection/consumption | no content change intended; incompatible arguments precede successful recall | No successful OSS delivery license; code-grounded mismatch remains separate from an observed failure |
| RTE-7 / content transformation | indeterminate: requested preservation of execution history, actual summary semantics unavailable | Nonempty model text is not proven faithful reshaping; OBJ-5 may omit or add content |
| RTE-7 / check/evidence production | no content change: nonempty output check after generation | Establishes content exists, not verbatim fidelity, causal reasons or truth; CLM-3 |
| RTE-7 / retention | no content change: summary stored in normal collection with type metadata | Enables generic knowledge read-back through BAP-2; no dedicated procedure executor or task-resumption authority |
| RTE-1 / disposition/acceptance | non-truth-apt policy/content update: caller config/provider selection | Python compatibility admission and caller operational authority, no knowledge-production license |

No post-acceptance lifecycle-integration row is asserted: no candidate-linked epistemic acceptance is established by this evidence. This is a bounded evidential limit on these routes, not an absence claim about inaccessible model reasoning.

#### 4. Per-object lifecycle disposition

The text of OBJ-2 from RTE-4 and the copied-message part of OBJ-3 are acquisition/import, with discovery lifecycle not applicable to mere acquisition. Their external source warrant is unknown. OBJ-3 history records concern operations; no separate claim that a history value is an epistemically accepted fact follows.

For extracted OBJ-2 through RTE-2, transformation is **indeterminate**: faithful extraction/reshaping, entailment from context and ampliative inference remain possible. Lineage is the submitted context and selected prior memories, with optional image-description preprocessing. Implemented checks are parsing, text/embedding availability and bounded hash exclusion; implemented retention/use are RTE-2 and RTE-3. Paired inputs/outputs plus an appropriate source-fidelity or truth check would decide preservation and warrant. Observed candidate state: **no instance observed**.

For OBJ-5 through RTE-7, transformation is **indeterminate** between requested faithful summary and outputs containing omissions or added claims. Implemented nonempty checking and retention do not settle it. A retained input/summary comparison and a consuming continuation record would resolve fidelity and use. Observed candidate state: **no instance observed**. A requirement to preserve outputs is not a performed test.

For OBJ-4, entity membership is **indeterminate** as a semantic classification, while numeric storage and set-union mechanics are non-ampliative symbolic reshaping. The similarity threshold supplies operational merge authority, not evidence of correct linguistic identity. A labeled or independently checked input/output record would resolve that part. No ampliative candidate is established sufficiently to assign the six discovery phases; it would be a category error to infer an accepted conjecture from its storage.

No lifecycle record for OBJ-1: no generated candidate truth-apt output for this static guidance object; relevant direct configuration/update route: RTE-1. Its proposed method content is assessed under theory-builder conditions below. Access metadata parts of OBJ-2 and structural history fields in OBJ-3 likewise support operational selection/bookkeeping rather than a separately accepted truth-apt discovery.

#### 5. System-claim versus route comparison

| Claim | Doctrine/design | Implemented support | Observed/causal support | Supported conclusion and mismatch |
|---|---|---|---|---|
| CLM-1 | Continuous-learning language and managed benchmark table | RTE-2, RTE-3, RTE-7 support accumulation, context reuse and ranking; RTE-5 offers a consumer recipe | None in this source-only run; hosted benchmark evidence excluded | Trace-fed retention is supported; criticism-driven capacity gain and OSS benchmark scores are not established |
| CLM-2 | add docstring mentions update/delete decisions | RTE-2 is ADD-only; RTE-4 provides explicit caller edits | No executed mutation trace | Preserve documentation mismatch; do not impute automatic conflict revision |
| CLM-3 | Procedural prompt demands unmodified outputs | RTE-7 rejects empty content, stores summary | No fidelity/activation experiment | A requested property and nonempty storage do not establish complete preservation or benefit |

#### 6. Bounded conclusion

The subsystem acquires messages, generates candidate facts/summaries and compiles access structures. It applies syntactic, compatibility and relevance checks with real operational force. These checks support usable storage and selection, while source truth, semantic preservation and epistemic acceptance remain separately unresolved. Existing-memory reuse is wired; the observed semantic quality and capacity effects of that reuse are not. A memory-related pipeline need not perform scientific knowledge production to fulfill its deliberately operational role.

## Reconciliation

The fresh specialist read only the frozen source and current method. Its complete report, source identity, reviewed boundary, input hash and method hash match this run; the final report SHA-256 is bound in Run identity. The shared source checker independently accepted all 50 report anchors. No report edits or post-handoff citation repairs were made.

| Specialist proposal | Accepted canonical record | Disposition |
|---|---|---|
| MEM-CMP-1 | CMP-6 | Accepted with original referent, evidence and limitations |
| MEM-OBJ-1 | OBJ-2 | Accepted with original referent, evidence and limitations |
| MEM-OBJ-2 | OBJ-3 | Accepted with original referent, evidence and limitations |
| MEM-OBJ-3 | OBJ-4 | Accepted with original referent, evidence and limitations |
| MEM-OBJ-4 | OBJ-5 | Accepted with original referent, evidence and limitations |
| MEM-RTE-1 | RTE-2 | Accepted with original referent, evidence and limitations |
| MEM-RTE-2 | RTE-3 | Accepted with original referent, evidence and limitations |
| MEM-RTE-3 | RTE-4 | Accepted with original referent, evidence and limitations |
| MEM-RTE-4 | RTE-5 | Accepted with original referent, evidence and limitations |
| MEM-RTE-5 | RTE-6 | Accepted with original referent, evidence and limitations |
| MEM-CLM-1 | CLM-3 | Accepted with original referent, evidence and limitations |

RTE-7 adds an explicit route view of the already accepted procedural branch in OBJ-5; it does not change the specialist's classifications or invent a continuation host. BAP-2, BAP-3 and BAP-4 make the corresponding accepted consumer/channel/force distinctions explicit. Coordinator component records cover model identity and runtime control; CMP-6 covers storage alternatives. They do not compete for ownership of memory classifications.

All material integration issues are disposed: CLM-2 retains the stale add docstring; RTE-2 retains the empty summary/recent-memory builder inputs and limited provenance; OBJ-5 and RTE-7 retain the unknown continuation consumer and horizon; RTE-6 retains the incompatible proxy; CMP-6 retains incomplete provider coverage. The component/configuration inspection and memory report agree that a graph-named adapter or old demo does not prove a separate active graph-memory pipeline. This is integrated evidence, not a claim of independent semantic clearance or independent lens convergence. No unsupported statuses were strengthened. No anchored conflict or unresolved specialist correction remains.

## Bounded synthesis

Mem0 supplies a returning memory service inside an application: it chooses what conversational material to retain, builds access structures and makes selected retained text available to later calls. Its internal extractor already consumes old memory, so the memory loop does not depend entirely on an imagined agent caller. The surrounding application's answer generation, action decisions and deployment security remain outside this boundary.

The most consequential design distinction is between additive acquisition and explicit revision. Ordinary inference adds new facts and does bounded duplicate suppression; it does not automatically resolve contradictory facts through the update/delete policy described in the stale docstring. Caller edits and withdrawal are separate, while entity merging changes retrieval access rather than adjudicating claim truth. The ten-message history cap and ten-neighbor extraction context provide concrete selection limits, but neither is a total token budget. Multi-store writes can partially succeed. A user needing later context gets a wired acquisition/read-back mechanism; a user needing a verified fact ledger or reliable task continuation still needs evidence beyond these routes.

Learning's strongest supported contribution is a **wired** trace-fed retention path: derived language facts, procedural summaries and symbolic entity/access structures can affect later context selection and extraction. This is what the `trace_learning` axis describes. **Learning through criticism of consumed theories: uninspected.** No retained comparison establishes improved capacity, the degree of transfer or attribution to criticism; the README's hosted benchmark numbers cannot fill that gap. Unknown task horizons are preserved rather than inferred from user/agent/run identifiers.

The [theory-builder definition](../../../../notes/definitions/theory-builder.md) is applied separately to guidance and retained content. For the proposed extraction method in OBJ-1, **condition 1, localized content: wired**: named textual rules say what to extract and what prior context is for. **Condition 2, consumption: wired at the instruction-call path** through BAP-1 and RTE-2; actual content-sensitive behavioral activation is uninspected. **Condition 3, content-directed criticism: uninspected**: deduplication, error handling and relevance scoring do not by themselves show a formulated attempt to refute the extraction method's claims. Inaccessible model processing is neither proof of criticism nor proof of its absence. **Condition 4, iteration of criticism: uninspected**: new memories feed later calls, but no retained criticism or criticism-derived method revision is established. Theory-builder membership is therefore **uninspected**, not inferred from the memory cycle.

For the retained-memory route, **condition 1: afforded** at most for caller-supplied rules or solutions that may be stored; many ordinary personal facts are not proposed problem-solving theories. **Condition 2: wired** for generic knowledge delivery to the extractor, but consumption of a particular retained theory through its content is **uninspected**. **Condition 3: uninspected** and **condition 4: uninspected**, because a fact edit, summary or entity merge is not evidence of formulated criticism followed by its uptake. RTE-7 preserves continuation-oriented content without establishing a procedure-execution or criticism route. No theory status is assigned from the storage label alone.

Addressability is a separate property: OBJ-1 exposes named textual rules; stored records expose whole text and metadata by UUID, with whole-entry update rather than a formal map of assumptions or reasons. Persistence is also separate: memory/history can survive process calls and restarts under durable storage configuration; the recent-message window deliberately evicts old entries, and task/project horizon remains unknown. Neither property completes an unresolved criticism path.

[Reflection](../../../../notes/definitions/reflective-system.md) has a narrow **wired** architectural witness for the selected aspect of current retained-memory content: RTE-2 builds an existing-memory representation from its own store, supplies it under deduplication/context instructions, and admits resulting additions that change the represented store. Store changes can therefore alter the next representation, and representation-mediated generation can alter later stored content. This says nothing about observed activation or reflection over Mem0's implementation and standards of criticism. Agent-self-description in stored text is not sufficient to extend reflection to an excluded agent. The reflective theory-builder qualifier remains **uninspected** because method criticism and iteration are not established.

Autonomy is recorded by role, not by a grade. Acquisition proposals, context selection, storage admission and ranking are **wired** computational steps after caller invocation. The caller owns configuration and explicit edits/deletions; actual human versus agent performance of those caller roles is uninspected. Formulated criticism, blame assignment and theory successor selection are uninspected, so **autonomous theory-builder status: uninspected**.

[Self-improvement](../../../../notes/definitions/self-improving-system.md) has a supported partial contribution: **wired** content-responsive memory changes enter later knowledge/ranking paths, toward the source's objective of preserving useful context. The available source describes an improvement-oriented standing pathway; **self-improvement exercised over an observed horizon: uninspected**, because no later operation is shown to depend causally on the update. Successful improvement is likewise uninspected. This is separate from model-weight changes, which the adapter evidence does not establish.

The assessment would change with candidate-linked extraction/summary records, independent fidelity or truth checks, an executed continuation consumer, and a comparison varying recalled content while holding relevant conditions fixed. A source revision repairing proxy signatures would change that route's compatibility disposition. Full adapter inspection could close the partial storage union. Evidence of retained formulated criticism and later use could change the theory-builder findings; merely adding more stored facts would not settle them.

## Limitations

| Limitation | Affected records | Inspected boundary | Conclusion prevented | Resolving evidence |
|---|---|---|---|---|
| No runtime or causal experiment | SRC-1, CLM-1, CLM-3, RTE-2, RTE-5, RTE-7 | Pinned code and documentation | Activation, faithfulness, improved capacity or occurrent self-improvement | Retained inputs/outputs and a controlled recall comparison |
| Model internals and immutable weight identity inaccessible | CMP-2, CMP-3, CMP-4, CMP-5 | SDK calls/model-name loading | Private criticism, exact parameter fixity, semantic guarantee | Pinned model identity and inspectable provider/run evidence |
| Configurable adapter coverage incomplete | CMP-6, RTE-1, RTE-3 | Factory/interface and selected storage adapters | Exhaustive substrate union and deployed durability/isolation | Inspect remaining selected backend implementations/configurations |
| Arbitrary procedural and batch callers | OBJ-5, RTE-7, RTE-2 | Generic message API and continuation prompt | Complete trace-source/timing union or task horizon | Actual calling workflow and task-linked continuation evidence |
| External answer example not executed; proxy incompatible | RTE-5, RTE-6, BAP-4 | README code and proxy/Memory signatures | Wired successful OSS proxy delivery or deployed answer dependence | Corrected compatible source and retained execution |
| Source truth and derivation unspecified | OBJ-2, OBJ-3, OBJ-4, OBJ-5 | Stored content, model prompts and syntax/relevance checks | Epistemic acceptance, complete preservation or theory criticism | Candidate-linked evidence, criteria and criticism uptake |
| Hosted/REST/async/JavaScript/agent boundaries excluded | CLM-1, CMP-1 | Synchronous Python subsystem | Hosted score transfer, authentication guarantee or enclosing runtime behavior | Separately frozen authorized implementation/evidence boundary |


## Verification and blockers

### Semantic verification

The shared records were reconciled before publication. Checked routes: RTE-1 configuration admission; RTE-2 ordinary extraction, retained-history supply, image preprocessing and entity compilation; RTE-3 selection/ranking; RTE-4 raw authoring, explicit revision/deletion/expiry; RTE-5 documented chat; RTE-6 incompatible proxy; RTE-7 procedural summary. Quotes support their attached findings, not merely source locations. All specialist proposals map by exact tokens to distinct declared records; the original report and its final hash are unchanged.

The comparison profile uses the same retained-object/interface scope as OBJ-2, OBJ-3, OBJ-4, OBJ-5 and these routes. CMP-6 accounts for uninspected backend alternatives with partial substrate coverage. The representation/lineage/authority sets characterize the exchanged operative objects and inspected consumers, while inaccessible provider internals remain excluded. Raw logs alone were not treated as trace learning. Derived conversational facts, entity structures and procedural summaries all received later-consumer checks; the summary's generic collection reuse qualifies without inventing an actual task-resumption host. Partial source/timing and unknown task horizon remain attached to that branch.

Push selection checks name the extraction LLM, add trigger, scope-matched recent-message selector and embedded-message selector over old facts. Identifier push is the actual automatic history match, not just a query ID. The documented application's requested pull is distinct from its automatic answer-model supply. Lexical signal is afforded there; optional reranking has no invented automatic delivery consumer. RTE-6 contributes no successful-delivery value. No score, source attribution, parse success, storage confirmation or expiration check was upgraded to truth acceptance. No delivery was upgraded to activation, and trace-learning membership was not upgraded to criticism-driven learning.

The ontology findings separately record theory-builder conditions 1–4, addressability, persistence, learning, reflection, autonomy and self-improvement. The narrow reflected aspect is retained-memory contents, not an excluded agent or the subsystem's own criticism methodology. The epistemic overlay keeps architectural status distinct from observed candidate state, distinguishes acquisition from indeterminate model transformations, and does not invent accepted ampliative claims. Known assessment/value support, exclusions and partial unions were checked against the integrated records. No substantive specialist conflict or unresolved semantic blocker remains.

### Deterministic validation

Targets: this exact result, its frozen memory input/report, the running run state and the generated candidate at its intended public path. The typed result validation passed cleanly, with no warnings or failures. The shared `verify-sources` check passed all 92 source-anchor checks. Both checks are repeated on final bytes before publication. The specialist report passed typed validation and all 50 source checks; its input/method/report identity checks passed. An initial source check of the coordinator draft rejected an overlong entity-extractor range; the function was reread and the citation replaced with its actual supporting span, after which that check passed. This is a source-anchor correction, not a change to the finding. No persisted receipt substitutes for the checks on current bytes.

### Blockers

None.

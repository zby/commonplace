---
{
  "type": "types/agentic-system-analysis-result.md",
  "description": "Mem0 synchronous OSS memory: additive extraction, scoped context reuse, hybrid retrieval, and the limits of correction and warrant",
  "run-id": "AAS-2026-09-26-mem0-02",
  "system": "Mem0",
  "run-date": "2026-09-26",
  "result-disposition": "complete",
  "target-class": "memory/knowledge/context-engineering system",
  "boundary-kind": "subsystem-only",
  "reviewed-boundary": "94c3fe9f238f3dbf29c9ce98643bd71eb13077cd",
  "analysis-cutoff": "2026-09-26",
  "evidence-tier": "code-grounded",
  "memory-comparison": {
    "scope": "OSS synchronous Python Memory with default Qdrant/OpenAI adapters and SQLite history/messages: inferred and raw add, procedural summaries, explicit CRUD, get/get_all/search/history, entity access records, default search, expiration and immutable identity handling, and caller extraction instructions. Excludes AsyncMemory, other providers, optional reranker internals, vision, cloud/server/SDK integrations, evaluation packages and enclosing-agent execution. Static prompts guide writes but are not changed-through-use memory.",
    "axes": {
      "storage_substrate": {
        "assessment": "known",
        "values": [
          "sqlite",
          "vector"
        ],
        "evidence": {
          "sqlite": {
            "basis": "wired",
            "records": [
              "OBJ-2",
              "OBJ-3"
            ],
            "note": "SQLite history and recent-message tables persist separate audit and context records."
          },
          "vector": {
            "basis": "wired",
            "records": [
              "OBJ-1",
              "OBJ-4"
            ],
            "note": "Default Qdrant collections persist text payloads, embeddings and entity access records."
          }
        },
        "records": [
          "OBJ-1",
          "OBJ-2",
          "OBJ-3",
          "OBJ-4"
        ],
        "note": "Covers default logical stores; physical files underlying databases are not a second memory medium. Provider internals and alternative stores are outside scope."
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
              "OBJ-1",
              "OBJ-2",
              "OBJ-3"
            ],
            "note": "Retained memory text and message/history text are delivered as readable content."
          },
          "symbolic": {
            "basis": "wired",
            "records": [
              "OBJ-1",
              "OBJ-3",
              "OBJ-4",
              "RTE-6"
            ],
            "note": "Identity fields, dates, vector coordinates and entity links have program-defined retrieval operations; they are access structures, not retained model parameters."
          }
        },
        "records": [
          "OBJ-1",
          "OBJ-2",
          "OBJ-3",
          "OBJ-4"
        ],
        "note": "Covers retained operative parts. Remote and NLP model parameters are not changed-through-use memory objects within this boundary."
      },
      "lineage": {
        "assessment": "known",
        "values": [
          "authored",
          "imported",
          "other-compiled",
          "trace-extracted"
        ],
        "evidence": {
          "authored": {
            "basis": "afforded",
            "records": [
              "RTE-2"
            ],
            "note": "Caller can author replacement text or raw memories; no human editor deployment was inspected."
          },
          "imported": {
            "basis": "wired",
            "records": [
              "RTE-2",
              "OBJ-3"
            ],
            "note": "Raw message content is copied to memory or the recent-message table."
          },
          "other-compiled": {
            "basis": "wired",
            "records": [
              "OBJ-1",
              "OBJ-4",
              "RTE-6"
            ],
            "note": "Embeddings, lexical representations and entity access records are generated from retained text."
          },
          "trace-extracted": {
            "basis": "wired",
            "records": [
              "RTE-1",
              "RTE-4"
            ],
            "note": "Conversation content automatically produces durable natural-language facts; procedural summarization is an additional admitted transformation."
          }
        },
        "records": [
          "RTE-1",
          "RTE-2",
          "RTE-4",
          "OBJ-3",
          "RTE-6"
        ],
        "note": "Authorship describes the afforded caller role; direct copying and extraction are separate inspected branches."
      },
      "behavioral_authority": {
        "assessment": "known",
        "values": [
          "knowledge",
          "ranking",
          "routing"
        ],
        "evidence": {
          "knowledge": {
            "basis": "wired",
            "records": [
              "BAP-1"
            ],
            "note": "Stored facts and recent messages are supplied to the next extraction LLM as evidential context."
          },
          "ranking": {
            "basis": "wired",
            "records": [
              "OBJ-1",
              "OBJ-4",
              "RTE-6"
            ],
            "note": "Stored vectors, lexical data and entity links affect deterministic candidate scoring."
          },
          "routing": {
            "basis": "wired",
            "records": [
              "OBJ-1",
              "OBJ-3",
              "RTE-5"
            ],
            "note": "Persisted identity fields select the memory partition and recent-message context supplied to extraction."
          }
        },
        "records": [
          "BAP-1",
          "BAP-2",
          "RTE-5",
          "RTE-6",
          "RTE-4"
        ],
        "note": "Procedural label does not establish instruction authority; summaries use the ordinary memory consumer. Shipped/custom extraction instructions are not learned memory and are excluded from the axis."
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
              "RTE-1",
              "RTE-4",
              "RTE-6"
            ],
            "note": "Caller-triggered extraction, summarization and entity compilation run automatically."
          },
          "manual": {
            "basis": "afforded",
            "records": [
              "RTE-2"
            ],
            "note": "Raw add and explicit text update allow caller-authored memory; no deployed human authoring workflow is established."
          }
        },
        "records": [
          "RTE-1",
          "RTE-2",
          "RTE-4",
          "RTE-6"
        ],
        "note": "A human or application initiating add does not turn automatic extraction into manual writing."
      },
      "curation_operations": {
        "assessment": "known",
        "values": [
          "decay",
          "dedup",
          "evolve",
          "invalidate"
        ],
        "evidence": {
          "decay": {
            "basis": "wired",
            "records": [
              "OBJ-3",
              "RTE-5"
            ],
            "note": "SQLite evicts retained messages beyond ten per identity scope."
          },
          "dedup": {
            "basis": "wired",
            "records": [
              "OBJ-4",
              "RTE-6"
            ],
            "note": "Entity upsert merges linked-memory sets into an exact or semantically near matching retained entity row."
          },
          "evolve": {
            "basis": "wired",
            "records": [
              "RTE-2"
            ],
            "note": "Explicit update replaces an existing memory text or metadata and retains its old text in history."
          },
          "invalidate": {
            "basis": "wired",
            "records": [
              "RTE-2",
              "OBJ-2"
            ],
            "note": "Explicit delete removes an active vector record while preserving a DELETE history event and old text."
          }
        },
        "records": [
          "RTE-1",
          "RTE-2",
          "RTE-4",
          "RTE-5",
          "RTE-6"
        ],
        "note": "ADD-only fact extraction does not revise retained facts. Duplicate acquisition avoidance is not itself retained-memory dedup. Expiration adds partial read suppression; it is not a global withdrawal mechanism."
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
              "RTE-3",
              "BAP-2"
            ],
            "note": "README names a chat application requesting search results and inserting them in its answering model context; deployment is not inspected."
          },
          "push": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "BAP-1"
            ],
            "note": "Every inferred add automatically supplies selected prior messages and memories to the extraction model without a recall request by that model."
          }
        },
        "records": [
          "RTE-3",
          "RTE-5",
          "BAP-1",
          "BAP-2"
        ],
        "note": "Internal automatic extraction context is wired independently of the externally afforded requested consumer route."
      },
      "read_back_signal": {
        "assessment": "known",
        "values": [
          "identifier",
          "inferred-embedding"
        ],
        "evidence": {
          "identifier": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "OBJ-3"
            ],
            "note": "Exact session_scope match selects prior message rows; identity payload filters constrain the vector partition."
          },
          "inferred-embedding": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "OBJ-1"
            ],
            "note": "Embedding of new parsed messages selects ten retained memory texts for extraction."
          }
        },
        "records": [
          "RTE-5"
        ],
        "note": "Describes push selection only. Public search lexical/entity scoring belongs to the requested route and does not add a push signal. Recency/count budgets do not alone add coarse targeting."
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
              "RTE-1",
              "RTE-5",
              "BAP-1"
            ],
            "note": "Automatic conversation-to-fact writes persist and become input to later extraction. No demonstrated improvement is implied."
          }
        },
        "records": [
          "RTE-1",
          "RTE-4",
          "RTE-5"
        ],
        "note": "Raw-log retention alone is insufficient; derived fact reuse supplies the qualifying route, with procedural summary reuse through the same vector store."
      },
      "trace_source": {
        "assessment": "known",
        "values": [
          "session-logs",
          "tool-traces",
          "trajectories"
        ],
        "evidence": {
          "session-logs": {
            "basis": "wired",
            "records": [
              "RTE-1",
              "OBJ-3"
            ],
            "note": "User/assistant messages feed durable fact extraction and recent-message context."
          },
          "tool-traces": {
            "basis": "afforded",
            "records": [
              "RTE-4"
            ],
            "note": "Procedural prompt explicitly accepts exact action outputs, including tool/API results, supplied in textual execution history."
          },
          "trajectories": {
            "basis": "afforded",
            "records": [
              "RTE-4"
            ],
            "note": "Procedural prompt describes an agent execution history over steps with actions, outcomes and current context; no automatic enclosing-agent capture is inspected."
          }
        },
        "records": [
          "RTE-1",
          "RTE-4"
        ],
        "note": "Includes only textual inputs and supported procedural consumer intent. Opaque tool-call payloads and external capture machinery are outside scope."
      },
      "learning_scope": {
        "assessment": "partial",
        "values": [
          "per-task"
        ],
        "evidence": {
          "per-task": {
            "basis": "afforded",
            "records": [
              "RTE-4"
            ],
            "note": "Default procedural prompt states that retained execution history enables the agent to continue the task."
          }
        },
        "records": [
          "RTE-1",
          "RTE-4",
          "RTE-5"
        ],
        "note": "Task horizon of ordinary fact extraction and caller-defined procedural prompts is not established by user_id, agent_id or run_id. These included alternatives prevent a complete horizon set; persistent user scope alone does not prove cross-task use."
      },
      "learning_timing": {
        "assessment": "known",
        "values": [
          "online"
        ],
        "evidence": {
          "online": {
            "basis": "wired",
            "records": [
              "RTE-1",
              "RTE-5"
            ],
            "note": "An inferred add reads accumulated context, writes facts and saves current messages during the synchronous interaction path; the next add reads that retained state."
          }
        },
        "records": [
          "RTE-1",
          "RTE-4"
        ],
        "note": "Procedural creation is another synchronous requested transformation, with ongoing-task continuation as documented intent. No distinct offline trainer or staged promotion is in the admitted routes."
      },
      "distilled_form": {
        "assessment": "known",
        "values": [
          "natural-language"
        ],
        "evidence": {
          "natural-language": {
            "basis": "wired",
            "records": [
              "RTE-1",
              "RTE-4",
              "OBJ-1"
            ],
            "note": "Qualifying trace transformations emit fact strings or a readable procedural summary. Embeddings/index metadata are downstream access compilation rather than an additional learned policy."
          }
        },
        "records": [
          "RTE-1",
          "RTE-4",
          "OBJ-1"
        ],
        "note": "Same fact and procedural routes as trace_learning, trace_source and learning_timing; output is text with optional metadata, not model-weight updates."
      },
      "faithfulness_tested": {
        "assessment": "not-determinable",
        "values": [],
        "evidence": {},
        "records": [
          "RTE-1",
          "RTE-3",
          "RTE-4"
        ],
        "note": "No retained execution evidence was admitted or produced that tests dependence on recalled content. Source code and prompt integrity demands cannot determine this execution-evidence axis; evaluation packages are excluded."
      }
    }
  }
}
---

# Mem0 synchronous OSS memory analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-mem0-02/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/mem0.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-mem0-02/memory-report.md`
**Memory analysis report SHA-256:** 55b4f64ced0f412d502a68c4f8f4fd97981ca119476a323fd373a24e87c50254

Source-only analysis opened on 2026-09-26. The public review and exact retained result are intended projections; completion is declared only by the run state.

## Boundary and evidence

Evidence basis: static implementation and shipped prompts/documentation from Mem0 at commit `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`, resolved from the default branch on 2026-09-26. No live model run, performance measurement, or causal experiment was performed. The purpose is to characterize the selected OSS subsystem and its per-value memory comparison evidence.

The target is the synchronous Python `Memory` API for textual messages, with default Qdrant, OpenAI LLM and embedder adapters, SQLite history/session context, and the conditional NLP/BM25 branches reached by those paths. It includes inferred add, raw add, procedural memory, explicit CRUD, requested search/get/get_all/history, entity indexing, expiration, identity-field preservation, and caller-customized prompts. This is a subsystem-only boundary, not a claim about all of Mem0.

Excluded: `AsyncMemory` (no sync/async parity conclusion), other providers/backends (no cross-backend guarantee), optional reranker implementations and vision processing (no classification of those modes), the platform/cloud implementation and server (no cloud behavior or deployed authentication conclusion), other SDKs/integrations/evaluation packages (no ecosystem or benchmark conclusion), and enclosing agents (no deployed answer quality, activation, or tool-effect guarantee). README's OSS example establishes a documented external consumer role, not an observed host deployment. Provider internals and exact model weights are inaccessible; this prevents training/fixity or causal model-quality claims. Dependencies include provider credentials, Qdrant client/storage, SQLite, and optionally spaCy model assets and FastEmbed. No credentials were inspected.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/mem0ai/mem0` | `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` | implementation | Synchronous Memory functions, storage, default adapters, entity/lemma/scoring support and configuration | `mem0/memory/main.py:148-457,487-2189`; `mem0/memory/storage.py:102-340`; `mem0/llms/openai.py:14-150`; `mem0/embeddings/openai.py:11-81`; `mem0/vector_stores/qdrant.py:30-597`; `mem0/utils/scoring.py:17-139`; `mem0/utils/spacy_models.py:21-90`; `mem0/utils/entity_extraction.py`; `mem0/configs/base.py:34-66` | Dependencies' internals and deployed runs uninspected; implementation supports wiring, not observed success |
| SRC-2 | Git | `https://github.com/mem0ai/mem0` | `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` | doctrine/design | Active extraction and procedural prompts, API docstrings and OSS README consumer example | `mem0/configs/prompts.py:326-390,468-946,947-1062`; `mem0/memory/main.py:774-817`; `README.md:195-225` | Prompt instructions and examples do not establish model compliance or deployment |

Operational source access root: `/home/zby/llm/commonplace/related-systems/mem0ai--mem0`. All evidence reads used commit-addressed `git --no-replace-objects` commands; neither worktree bytes nor prior reviews supplied evidence. Source quotations below use full commit attribution and are retained once on their canonical supporting records.

## Shared records

### Components

**CMP-1 — Memory coordinator.** Symbolic Python dispatch, validation, filters, prompt assembly, batch persistence, and return formatting. SRC-1 `mem0/memory/main.py:487-2189`. Wiring: `wired`. The caller selects identities, data, raw/inferred/procedural mode, credentials/configuration and explicit mutations. This component returns to a host; it does not own the host's agent loop.

**CMP-2 — OpenAI LLM adapter.** Distributed-parametric model behind a symbolic adapter; default model name `gpt-5-mini`. SRC-1 `mem0/llms/openai.py:14-150`. Request/response wiring: `wired`; exact weight/version pinning: `uninspected` because model names resolve through configurable endpoints rather than a recorded immutable weight digest. Parameter changes inside provider operation: `uninspected`; the inspected adapter issues inference requests and exposes no local optimizer. Callback invocation is an external extension point, not an approval check: callback failures are logged without vetoing the response. Provider-native tools exist on the adapter surface, but RTE-1 and RTE-4 do not supply them.

> response = self.client.chat.completions.create(**params)
> --- `mem0/llms/openai.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

**CMP-3 — OpenAI embedding adapter.** Distributed-parametric embedding service producing numeric access representations. Default model `text-embedding-3-small`; batching chunks at 100 and checks response count. SRC-1 `mem0/embeddings/openai.py:11-81`. Wiring: `wired`. Exact parameter identity and provider training during operation: independently `uninspected`; mutable endpoint/model-name resolution prevents fixed-weight claims. Stored vectors are derived access data, not learned model weights.

> self.config.model = self.config.model or "text-embedding-3-small"
> --- `mem0/embeddings/openai.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

**CMP-4 — Conditional spaCy NLP.** The entity/lemma routes load `en_core_web_sm`, download it if absent and return no NLP object on loading failure. Symbolic extraction rules consume parametric tagging/NER outputs. SRC-1 `mem0/utils/spacy_models.py:21-90`; `mem0/utils/entity_extraction.py`. Wiring: `wired` conditional on installation/load; observed use: `uninspected`. Exact package/model version is not pinned here; parameter changes within the dependency remain `uninspected`. The inspected caller loads/uses the model; it does not train it.

> _nlp_full = spacy.load("en_core_web_sm")
> --- `mem0/utils/spacy_models.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

**CMP-5 — Qdrant BM25 and symbolic ranking.** The adapter lazily requests `SparseTextEmbedding(model_name="Qdrant/bm25")` and returns no keyword scores when the sparse slot/encoder is unavailable. The name alone does not establish learned parameters; dependency internals are `uninspected`. The inspected hybrid scorer is symbolic arithmetic, not a learned router. SRC-1 `mem0/vector_stores/qdrant.py:93-127,454-484`; `mem0/utils/scoring.py:58-139`. Conditional wiring: `wired`.


### Operative objects

**OBJ-1.** Qdrant memory points: readable `data`, UUID, hash, timestamps, identity/attribution/expiration metadata, lemmatized text and dense/optional sparse vectors. Raw, extracted and procedural text share this representation. Text is content; numeric vectors and keys are access structures. Lineage varies by route. Default local Qdrant path is `/tmp/qdrant`; durability depends on retaining that storage.

Evidence: SRC-1 `mem0/memory/main.py:1027-1045,1975-2005,2043-2045`; `mem0/configs/vector_stores/qdrant.py:10-24`; `mem0/vector_stores/qdrant.py:186-247`; wired.

Memory text has three admitted origins: inferred facts (RTE-1), raw/caller-authored content (RTE-2), and procedural summaries (RTE-4). These parts share storage but retain distinct lineage and epistemic dispositions. Numeric embeddings are access data, not updated model parameters; optional sparse vectors and symbolic scope/link/expiry fields participate in selection. Storage wiring does not establish that an actual point has survived a deployment restart.



**OBJ-2.** SQLite history records per memory UUID: old/new text, event, creation/update time, deletion flag, actor and role. This is a mutation audit, not the source conversation or a preserved explanation of a model decision. Consumer is explicit history request. Default path is `MEM0_DIR/history.db` or `~/.mem0/history.db`.

Evidence: SRC-1 `mem0/configs/base.py:11-13,43-46`; `mem0/memory/storage.py:102-126,227-255`; wired storage, external inspection afforded.

History preserves old/new values and events rather than source messages, verified reasons, or a per-claim proof. A caller may put extra provenance in metadata; the default model pipeline does not manufacture it.

>                     CREATE TABLE IF NOT EXISTS history (
>                         id           TEXT PRIMARY KEY,
>                         memory_id    TEXT,
>                         old_memory   TEXT,
>                         new_memory   TEXT,
>                         event        TEXT,
>                         created_at   DATETIME,
>                         updated_at   DATETIME,
>                         is_deleted   INTEGER,
>                         actor_id     TEXT,
>                         role         TEXT
>                     )
>                 """
> --- `mem0/memory/storage.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

**OBJ-3.** SQLite messages keyed by escaped composite identity scope, holding role/content/name/time. Raw traces, latest ten retained per scope; prior scope-matched rows are sent into later extraction, with display truncation.

Evidence: SRC-1 `mem0/memory/main.py:407-420,918-921`; `mem0/memory/storage.py:128-149,257-324`; wired.

The display formatter truncates each prior message to 300 content characters. It does not impose an equivalent bound on each selected fact or on total prompt size.

> PAST_MESSAGE_TRUNCATION_LIMIT = 300
> 
> 
> def _truncate_content(text, limit=PAST_MESSAGE_TRUNCATION_LIMIT):
>     """Truncate text to limit characters, appending '...' when shortened."""
>     if len(text) <= limit:
>         return text
>     return text[:limit] + "..."
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

**OBJ-4.** Separate Qdrant entity collection sharing the client. Rows hold extracted name/type, identity scope, embeddings and linked memory IDs. Near matches merge linked sets. This compiled index can affect public search ordering; it does not establish factual entity resolution correctness.

Evidence: SRC-1 `mem0/memory/main.py:559-650,1105-1204,1747-1827`; wired with optional NLP dependencies and tolerated failures.

Near-match associations are computed from text and have ranking force. They are distinct from the model-requested related-memory links, which RTE-1 does not retain.



**OBJ-5.** Shipped additive/procedural prompts plus optional config/per-call instructions. Natural-language authoring surface controlling extraction. Retained in code/config, but not accumulated or revised through the admitted memory loop, so excluded from memory storage/lineage/authority classifications.

Evidence: SRC-1 `mem0/memory/main.py:943-962,2017-2026`; SRC-2 `mem0/configs/prompts.py:326-405,468-525,1016-1062`; wired consumption, caller customization afforded.

The active additive guidance directs extraction from user and assistant messages, attribution, reference resolution, contextual richness and duplicate avoidance. The procedural guidance asks for task-continuation history. Per-call instructions take precedence over configured custom instructions in RTE-1; RTE-4 accepts a replacement system prompt. These are caller/shipped method choices, not memory-derived method revisions.



### Routes

**RTE-1.** `add(infer=True)` on textual messages: gather prior context, request ADD-only facts, parse JSON, embed fact strings, suppress exact hashes in retrieved neighbors/current batch, insert confirmed records into OBJ-1, append OBJ-2 ADD history, index entities, save OBJ-3. Later inferred add automatically receives the retained fact text. Model extraction proposes; code admits nonempty embeddable text and successful writes, with no semantic verifier.

wired; SRC-1 `mem0/memory/main.py:881-1220`; SRC-2 `mem0/configs/prompts.py:468-525,665-707`. Seed correction: additive changes, not automatic UPDATE/DELETE.

The immediate return contains only confirmed ADD records. Later read-back uses RTE-5 or caller-requested RTE-3; there is no delegated consumer inside this subsystem. Trigger/next-step owner is CMP-1, with CMP-2 proposing text under OBJ-5. The admission policy is structural and persistence-based; code can discard empty/unembeddable/duplicate candidates or fail writes, but does not compare content to an answer oracle. Proposed links and rationale are not distinct retained fields; only text and optional attribution from each model item enter the payload. Existing hashes cover the ten selected neighbors and current batch, not the entire corpus. Raw source messages persist only in the rolling OBJ-3 window. Revision means additive retained change here; RTE-2 owns replacement/withdrawal. Invalidation/expiry at later reads is route-specific. Recovery uses per-record fallbacks and public mutation/history, not a transaction across all stores. The operation is computational after caller invocation; no per-candidate human veto is wired.

> You are a Memory Extractor — a precise, evidence-bound processor responsible for extracting rich, contextual memories from conversations. Your sole operation is ADD: identify every piece of memorable information and produce self-contained, contextually rich factual statements.
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

>                 mem_metadata["created_at"] = datetime.now(timezone.utc).isoformat()
>             mem_metadata["updated_at"] = mem_metadata["created_at"]
>             if mem.get("attributed_to"):
>                 mem_metadata["attributed_to"] = mem["attributed_to"]
> 
>             records.append((memory_id, text, embed_map[text], mem_metadata))
> 
>         if not records:
>             self.db.save_messages(messages, session_scope)
>             return []
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

>         persisted_records = []
>         try:
>             self.vector_store.insert(
>                 vectors=all_vectors,
>                 ids=all_ids,
>                 payloads=all_payloads,
>             )
>             persisted_records = records
>         except Exception:
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

**RTE-2.** Raw add skips system-role messages and copies other textual content with role/name-derived actor metadata; explicit update revises text/metadata, re-embeds, records history and refreshes entity links on text change. Explicit delete removes vector content and records old text/deletion; delete_all loops filtered batches; reset clears stores/history/messages subject to entity-store initialization.

wired implementation; manual authorship afforded; SRC-1 `mem0/memory/main.py:881-915,1829-1958,1975-2005,2052-2174`.

The caller proposes and decides raw text, replacements, metadata changes or removal; CMP-1 executes validated operations without an independent content oracle. Human authoring is afforded by that interface; no deployed human editor was inspected. Raw writes skip system-role messages and return before recent-message saving/entity compilation. Update/delete returns an acknowledgement; later RTE-3 can inspect history, and RTE-5 can consume remaining/revised points. Text remains mutable: the preserved identity fields do not make facts immutable. Explicit delete withdraws the current vector record while history preserves prior text if its separate write succeeds. Reset clears stores and history, not an evidentially retained rejection. No delegated visibility or automatic rollback exists in this finite path; failed secondary writes may leave partial effects. The revision guidance is caller-supplied content; its rationale, criticism, or correctness is uninspected unless supplied as ordinary text.

> msg_content = message_dict["content"]
> msg_embeddings = self.embedding_model.embed(msg_content, "add")
> mem_id = self._create_memory(msg_content, {msg_content: msg_embeddings}, per_msg_meta)
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

>     On the creation path there is no prior payload, so pass an empty dict and every
>     identity key present in `metadata` is dropped with a warning.
>     """
>     clean = {}
>     for key, value in metadata.items():
>         if key not in _IDENTITY_KEYS:
>             clean[key] = value
>         elif value != existing_payload.get(key):
>             logger.warning(f"{context}: ignoring metadata['{key}'] - identity fields cannot be set through metadata")
>     return clean
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> 
>         self.vector_store.update(
>             vector_id=memory_id,
>             vector=embeddings,
>             payload=new_metadata,
>         )
>         logger.info(f"Updating memory with ID {memory_id=} with {data=}")
> 
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
>         )
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

**RTE-3.** Requesting callers use search/get/get_all/history. Search returns scored readable memory and metadata; get uses UUID; get_all uses identity/metadata filters; history uses UUID. README identifies a chat application requesting search and delivering memory strings in its answer model's system context. The other methods establish storage/inspection capability without an inspected autonomous agent consumer.

afforded external consumer; wired API implementation; SRC-1 `mem0/memory/main.py:1222-1536,1960-1973`; SRC-2 `README.md:204-230`.

The requester owns invocation and query/identity/UUID selection. The coordinator returns readable records, scores and metadata or history; it does not invoke the external answering model. Public search is a bounded semantic candidate pool with hybrid reordering supplied by RTE-6; get/get_all/history are direct inspection capabilities. Expiry hides points only in search/get_all unless show_expired is true; UUID get and the RTE-5 extraction selector do not share that predicate. Search/get_all count limits can yield fewer results after filtering. There is no delegated consumer within the selected library. Read operations do not revise content; unsupported parameters fail before search, and optional reranking is excluded from this boundary. Activation and answer quality are uninspected.

>         formatted_memories = []
>         for mem in actual_memories:
>             if not show_expired and _payload_is_expired(mem.payload):
>                 continue
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

**RTE-4.** `add` with agent_id and procedural memory_type invokes summarization before the normal infer branch. It sends supplied messages with default/custom system instructions, requires nonempty output, embeds the summary and persists through `_create_memory` as OBJ-1 with a procedural marker. Default prompt asks for execution history adequate to continue the task. Ordinary selection can later deliver this summary to extraction; there is no distinct procedural executor or automatic continuation agent.

wired summarization/storage and generic internal reuse; afforded task-continuation consumer intent; SRC-1 `mem0/memory/main.py:853-864,2007-2050`; SRC-2 `mem0/configs/prompts.py:326-363`.

The model CMP-2 proposes a summary under default/custom OBJ-5 guidance; CMP-1 rejects empty output and persists nonempty text through the same primary vector/history helper as raw add. This branch runs before infer=False dispatch when the agent_id/procedural condition holds. Immediate return is one ADD record. Later RTE-5 may select the summary as ordinary memory text; external task continuation is afforded by the prompt and requesting interface, with no dedicated executor. Raw/procedural creation does not save OBJ-3 or initially compile entity links. The default guidance explicitly includes actions, tool/API outputs, findings, errors and task state. It may preserve reasons present in that input, but no typed rationale field, fidelity comparator or later criticism consumer is guaranteed. Task horizon is afforded per-task for the default prompt; custom prompt horizon remains undetermined. Expiry/recovery follow the ordinary vector/history paths. No delegated actor or separate expected-answer oracle is supplied.

> You are provided with the agent’s execution history over the past N steps. Your task is to produce a comprehensive summary of the agent's output history that contains every detail necessary for the agent to continue the task without ambiguity.
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

>      - Precisely describe what the agent did (e.g., "Clicked on the 'Blog' link", "Called API to fetch content", "Scraped page data").
>      - Include all parameters, target elements, or methods involved.
> 
>   2. **Action Result (Mandatory, Unmodified)**:
>      - Immediately follow the agent action with its exact, unaltered output.
>      - Record all returned data, responses, HTML snippets, JSON content, or error messages exactly as received. This is critical for constructing the final output later.
> 
>   3. **Embedded Metadata**:
>      For the same numbered step, include additional context such as:
>      - **Key Findings**: Any important information discovered (e.g., URLs, data points, search results).
>      - **Navigation History**: For browser agents, detail which pages were visited, including their URLs and relevance.
>      - **Errors & Challenges**: Document any error messages, exceptions, or challenges encountered along with any attempted recovery or troubleshooting.
>      - **Current Context**: Describe the state after the action (e.g., "Agent is on the blog detail page" or "JSON data stored for further processing") and what the agent plans to do next.
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

>         metadata = {**metadata, "memory_type": MemoryType.PROCEDURAL.value}
>         embeddings = self.embedding_model.embed(procedural_memory, memory_action="add")
>         memory_id = self._create_memory(procedural_memory, {procedural_memory: embeddings}, metadata=metadata)
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

**RTE-5.** Proposed context-supply/maintenance route: on every inferred add, exact composite identity selects recent OBJ-3 rows; new-message embedding plus identity filters selects up to ten OBJ-1 texts. Prompt builder delivers both to CMP-2. After extraction, message persistence evicts old rows beyond ten. Scope IDs are targeting inputs, not task-horizon declarations.

wired; SRC-1 `mem0/memory/main.py:407-420,918-963,1208-1209`; `mem0/memory/storage.py:257-324`; SRC-2 `mem0/configs/prompts.py:966-993,1037-1048`.

This is a subroute of RTE-1, not a second write analysis. Its next-step owner is CMP-1; CMP-2 is the later consumer. Exact scope equality selects OBJ-3 rows, and current-message embeddings plus identity filters select OBJ-1. Both selections happen without a recall request from CMP-2, establishing push. The limits are ten prior messages, 300 displayed characters per prior message and ten selected memories; selected memory length/current input lack a total prompt budget. Summary and Recently Extracted Memories prompt slots are left empty by this caller. Content force is knowledge, with identity data supplying routing. Message expiry is recent-window eviction; vector expiration is not applied here. The routine returns context internally, then its caller returns ADD results; delegated visibility is inapplicable. SQLite saves have a transaction, but no rollback spans vector writes and this context save.

>         # === V3 PHASED BATCH PIPELINE ===
> 
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

>                 # Evict old messages beyond the most recent 10 for this scope.
>                 # Wrapped in a derived table to force SQLite to materialize the
>                 # ORDER BY before the outer NOT IN evaluates it.
>                 self.connection.execute(
>                     """
>                     DELETE FROM messages WHERE session_scope = ? AND id NOT IN (
>                         SELECT id FROM (
>                             SELECT id FROM messages WHERE session_scope = ? ORDER BY created_at DESC LIMIT 10
>                         )
>                     )
>                 """,
>                     (session_scope, session_scope),
> --- `mem0/memory/storage.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

**RTE-6.** Proposed entity-index/search route: extract textual entities, embed them, exact/near-match and merge linked memory IDs; public search retrieves semantic candidates, conditional lexical scores and entity boosts, then applies fixed scoring. Compiled retained access records have ranking authority; compilation is not new substantive claim synthesis.

wired conditional mechanism; SRC-1 `mem0/memory/main.py:586-730,1105-1204,1642-1827`; `mem0/vector_stores/qdrant.py:93-126,186-247,454-484`; `mem0/utils/scoring.py:59-139`.

This subroute serves RTE-1/RTE-2 maintenance and RTE-3 selection. Conditional NLP extracts entities; embeddings and exact/near-match rules propose associations; code merges a retained entity linked-ID set when similarity reaches 0.95 or exact text matches. Code may skip failed embeddings or tolerate secondary index failures. Raw/procedural creation initially bypasses this index. Cleanup returns immediately if the entity store was never initialized in this process; reset likewise only clears an initialized entity store. Public query ranking considers up to eight query entities, up to 500 matches per entity, and a 0.5 similarity gate for boosts. The semantic candidate pool is max(4*top_k, 60); keyword/entity signals do not introduce candidates absent from it. The semantic threshold gates before hybrid combination. Only access state changes; its guidance is symbolic matching/scoring policy, not a criticism-responsive theory. Exact text matches and similarity thresholds do not verify real-world identity. No delegated consumer exists; immediate result is index maintenance or scores, later effect is ranking. Callback/dependency failures do not create a common rollback across stores.

>                     vectors=entity_embedding,
>                     top_k=1,
>                     filters=search_filters,
>                 )
> 
>             semantic_match = existing[0] if existing and existing[0].score >= 0.95 else None
>             match = exact_match or semantic_match
>             if match:
>                 # Update existing entity's linked_memory_ids
>                 payload = match.payload or {}
>                 linked_ids = payload.get("linked_memory_ids", [])
>                 if memory_id not in linked_ids:
>                     linked_ids.append(memory_id)
>                     payload["linked_memory_ids"] = linked_ids
>                     self.entity_store.update(
>                         vector_id=match.id,
>                         vector=None,
>                         payload=payload,
>                     )
>             else:
>                 # Create new entity
>                 entity_id = str(uuid.uuid4())
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

>                         num_linked = max(len(linked_memory_ids), 1)
>                         memory_count_weight = 1.0 / (1.0 + 0.001 * ((num_linked - 1) ** 2))
>                         boost = similarity * ENTITY_BOOST_WEIGHT * memory_count_weight
> 
>                         for memory_id in linked_memory_ids:
>                             if memory_id:
>                                 memory_key = str(memory_id)
>                                 memory_boosts[memory_key] = max(memory_boosts.get(memory_key, 0.0), boost)
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### Claims

**CLM-1 — Inferred add documentation promises mutation choice.** SRC-2 `mem0/memory/main.py:788-793`, `claimed`. The active RTE-1 implementation and active additive prompt support ADD only; explicit RTE-2 supplies update/delete. This mismatch is bounded to the inspected synchronous entry path.

> If True (default), an LLM is used to extract key facts from
> 'messages' and decide whether to add, update, or delete related memories.
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

**CLM-2 — Contextual extraction and preservation doctrine.** The active extraction prompt asks for self-contained facts, correct attribution, semantic deduplication and links; the procedural prompt asks to preserve every action output verbatim. SRC-2 `mem0/configs/prompts.py:326-356,468-535`. These are `claimed` quality constraints. RTE-1 and RTE-4 wire generation/persistence, but neither JSON parsing, embeddings nor retention certifies faithful content.


**CLM-3 — Memories can inform a later assistant response.** SRC-2 `README.md:204-223`, `afforded` as a documented external-consumer route through RTE-3 and BAP-2, not a deployed operation. The example puts returned memory text in a system prompt; the library's return alone does not grant it instruction force in every host.


### Evidenced absences

**ABS-1 — No separate semantic-fidelity admission check in the selected memory-write paths.** Conclusion status: `absent` for an explicit coordinator check between model output and storage, not for hidden model reasoning or excluded evaluations. Searched boundary: SRC-1 `mem0/memory/main.py:881-1220,2007-2050` at the reviewed commit; manual control-flow inspection plus `git grep -n -i -E 'verif|faith|critic|approve|rollback|feedback'` on `mem0/memory/main.py`. The search returned no matches; the positive control flow on RTE-1 and RTE-4 establishes parse/nonempty/embedding/hash/persistence checks instead. This prevents treating successful storage as verified extraction or accepted truth. It does not show that no external application checks content.

### Behavioral-authority paths

**BAP-1.** Later extraction model CMP-2 receives prior facts and messages in its user prompt; force is advisory/evidential knowledge under the static extractor instructions. Persisted identity data route the selected parts. Horizon: later additions under matching scope, task boundary undetermined.

wired; SRC-1 `mem0/memory/main.py:918-963`; SRC-2 `mem0/configs/prompts.py:503-525,1037-1048`.

The selector and exact/semantic budgets are RTE-5; delivery is wired, behavioral activation remains uninspected. Stored identity fields constrain which retained content reaches this consumer.



**BAP-2.** External chat application requests RTE-3 search results and places memory text in its answering model's system context. The enclosing instruction says to answer using query and memories; recalled facts retain knowledge authority rather than becoming executable commands.

afforded; SRC-2 `README.md:208-217`. No deployed caller or benefit inspection.

The documented consumer answers from requested memories. The memory text is evidence/context within that example; its system-channel placement does not establish a universal enforcement, executable-skill or independent instruction authority.

> 
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

## Runtime account

The ordinary invocation begins with an application calling `Memory.add(messages, user_id=...)`. The application supplies the principal and identity strings; the library validates/scopes them rather than authenticating the principal. RTE-1 owns the next steps: read scope-matched recent messages, embed new input, select ten vector memories, assemble the active prompt, call the LLM once, parse candidates, batch-embed, suppress exact hashes, persist successful new records, attempt history/entity maintenance, save recent messages, and return ADD results. Execution is a returning memory computation; there is no autonomous tool-use loop or delegated agent in this boundary. Thread-pool entity searches coordinate storage requests, not independently acting agents.

RTE-2 deliberately bypasses extraction for raw writes and accepts caller-directed replacement/deletion. RTE-4 summarizes an agent's supplied history using a separate prompt, then embeds and stores one procedural memory. RTE-3 serves caller-requested memory and history. The README host consumes a requested result, makes its own model call and later submits messages; that host remains external. Entity ranking, raw/direct access, and internal extraction retrieval are material alternatives, so public-search filters cannot be promoted into system-wide guarantees.

Decision roles are explicit. In RTE-1 the caller supplies messages, identity and optional instructions; CMP-2 proposes memory text; deterministic code decides structural eligibility, hash suppression and which successful writes appear in the return. There is no per-candidate human approval step. RTE-2 places content selection and veto in the caller; code executes the request. RTE-4 places summary production in CMP-2, and rejects empty output before persistence. The modes are open application requests, with an optional task-history summary request, not an inspected curriculum or bounded improvement experiment. Current messages and existing memory are inputs, not an independently supplied expected answer. No answer oracle was inspected for these operational modes; hidden model reasoning remains unknown.

The capability surface includes configured provider calls, local or configured Qdrant storage, SQLite, prompt overrides, callbacks and explicit mutation. The current runtime grant set is whatever credentials and process/filesystem access the embedding/LLM/storage clients receive; this analysis did not inspect a deployed grant set. The deployed isolation envelope is therefore `uninspected`. Identity-field preservation is a local invariant owned by `_strip_identity_keys` on create/update metadata, not a cross-tenant authorization guarantee: caller-supplied top-level IDs and identifier-only get/update/delete/history remain separate access paths. Source: SRC-1 `mem0/memory/main.py:148-174,315-419,1222-1268,1829-1974`.

Four forcing cases were traced statically:

1. **Contradictory/new fact:** the active add path proposes new records and skips exact hashes. It does not dispatch model-requested UPDATE/DELETE. Caller intervention is a separate RTE-2 path. This resolves CLM-1 without running a probabilistic model.
2. **Expired memory:** public search/get_all suppress it by default, while get and extraction's direct vector read do not apply that predicate. `show_expired` can also bypass hiding. Expiration is a route-local retention/use policy, not universal erasure.
3. **Malformed model response or provider failure:** generation failure raises `LLMError`; parse failure becomes no extracted memories while messages are still saved. Batch embedding falls back individually; unavailable embeddings remove candidate eligibility. Thus an empty ADD result does not uniquely mean no relevant content.
4. **Partial storage failure:** batch insert falls back to per-record insert; only confirmed writes enter returned ADD results. History and entity failures can be logged after primary persistence. SQLite message writes have their own transaction; there is no inspected cross-store rollback. A final message-save failure can occur after vector writes, so callers need reconciliation rather than assuming an exception means no effects.

The load-bearing persistence guarantee is best effort across stores, owned by Memory and bounded by each dependency's success/exception contract. The confirmed-write return rule covers inferred add; it does not establish a distributed transaction or exactly-once retry semantics. Recovery through public history exposes prior text but does not automatically restore vectors or replay a multi-store transaction. Source: SRC-1 `mem0/memory/main.py:970-1218,1975-2143`; `mem0/memory/storage.py:257-296`.

No dynamic check planned. Considered a model-based contradiction test, a dependency-mocked failure test, and a live recall-quality test. Static branching and side-effect order suffice for the bounded wiring findings; mocks would not establish backend atomicity, while model fidelity/benefit would need declared fixtures, credentials and retained executions beyond this source-only pass. No failed attempt is presented as a negative result.

## Lens scoping

### Memory/context scope

Full depth. Trigger evidence SRC-1; objects OBJ-1, OBJ-2, OBJ-3, OBJ-4 and their derivative parts; routes RTE-1, RTE-2, RTE-3, RTE-4 and accepted specialist additions. The boundary is retained content changed through use, access representations and write/maintenance/later-consumer paths in the scoped subsystem. OBJ-5's static/caller-provided prompts shape the analysis but do not count as accumulated memory merely because they enter context. The fresh specialist's exact frozen input/report identities appear in Run identity and Reconciliation.

### Epistemic scope

Full depth. SRC-1 and SRC-2 establish truth-apt factual/summary outputs, prompting constraints, structural admission and later consumption. The question is which routes transform content and what licenses reliance, rather than whether memory exists. RTE-1, RTE-2, RTE-3 and RTE-4 plus access-maintenance records are assessed; excluded providers/host loops/evaluations prevent wider acceptance, activation and improvement conclusions. Both lenses use the same frozen subsystem boundary.

## Lens outputs

### Memory/context lens

The fresh specialist inventoried the distinct fact, raw-content and procedural parts of OBJ-1, OBJ-2 audit history, OBJ-3 rolling context, OBJ-4 access records and the excluded-from-memory static guidance OBJ-5. RTE-5 supplies the strongest internal reuse witness: selected accumulated facts and messages reach CMP-2 before every inferred extraction. The requested external consumer RTE-3 and BAP-2 is independently afforded by README. The profile therefore preserves wired push/knowledge and afforded pull rather than assigning one strength to the whole axis.

RTE-1 and RTE-4 automatically transform traces into durable readable text and can feed later RTE-5 context. This establishes the specified trace-learning write mechanism, not demonstrated improvement. Session-log extraction is wired; procedural tool-trace/trajectory input is afforded. Default procedural guidance supports afforded per-task continuation; ordinary extraction and custom procedural task horizons remain unknown, so learning_scope is partial. Timing/form share those same qualifying routes: synchronous online text production and generic subsequent reuse. No retained dependence experiment supports faithfulness_tested, which is not-determinable.

Per-value maintenance witnesses remain separate: RTE-5's retained-message eviction supports decay; RTE-6's entity-set merge supports dedup; RTE-2 supports evolve and history-preserving invalidate. Hash-based acquisition avoidance does not become retained-fact consolidation. Expiry is partial visibility control, and no field named immutable blocks text edits. Entity links are compiled independently of the prompt-requested memory links that RTE-1 discards. Raw/procedural creation skips message saving/entity indexing, and cleanup can skip an uninitialized entity store. These source-visible routes establish limits, not observed corruption or poor performance.

SQLite/vector are logical storage substrates, while readable content and symbolic access structures coexist. The parametric components produce access values or text but are not changed-through-use retained model parameters in this boundary. No source-native procedural label establishes a separately executable skill. No curation quality, factual truth, answer activation or improved capacity was inferred from persistence or scores.

### Epistemic lens

Invoked `kb/instructions/analyse-external-system-epistemic-architecture.md` in sparse overlay mode. The six blocks below annotate the shared register; architectural status and candidate state remain independent of conclusion status.

#### 1. Source-and-claim boundary

Mem0, frozen revision and exclusions: see Boundary and evidence, SRC-1 and SRC-2. Material route families: RTE-1 transformation and admission; RTE-2 acquisition, revision and withdrawal; RTE-3 selection; RTE-4 summary transformation; ancillary entity/history/context maintenance. Question: does the subsystem retain candidates, or evaluate content so that it warrants acceptance? CLM-1, CLM-2 and CLM-3 are the inspected claims. No observed candidate or retained experiment was supplied, preventing observed-disposition and causal-benefit findings.

#### 2. Epistemic-object inventory

| object | epistemic annotation | evidence and limit |
|---|---|---|
| OBJ-1 | Text is truth-apt about speakers, preferences, actions or supplied content. Model extraction can preserve, interpret or amplify source statements; transformation fidelity is indeterminate without instances. | See RTE-1 and SRC-2 active prompt; operational retention does not establish truth. |
| OBJ-2 | History records assert prior memory events/text; they evidence local bookkeeping if observed, not truth of the recorded memory. | See RTE-2 and RTE-3; no concrete event observed. |
| OBJ-3 | Recent messages retain attributed input for reference resolution; acquisition preserves the submitted bytes at storage boundaries, while prompt formatting truncates presentation. | See RTE-1; no guarantee that original speaker statements were true. |
| OBJ-4 | Entity labels and memory links are access metadata, including fallible NLP/embedding matches. They support ranking, not endorsement. | See accepted entity route; similarity is not entity-identity proof. |
| OBJ-5 | Static/caller-authored method guidance says how to extract/summarize; consumption is wired, but its asserted effectiveness is not validated by a run. | SRC-2 `mem0/configs/prompts.py:468-535,1016-1062`. |

OBJ-1's procedural derived-text part is separately disposed by RTE-4 below; it may claim task state and prior actions, not merely issue instructions. Numeric access representations have no independently individuated candidate truth claim; see their shared object records.

#### 3. Authority-route ledger

| route and function | architectural status | target/relation and evaluator | force and authority | observed state, evidence and limit |
|---|---|---|---|---|
| RTE-1 content transformation | implemented | OBJ-1 candidate text from new messages and retained context; preservation versus amplification indeterminate; CMP-2 interprets prompt | Generates a candidate, no independent epistemic license | no instance observed; SRC-1 `mem0/memory/main.py:923-993`; CLM-2 |
| RTE-1 disposition/acceptance | implemented | Nonempty embeddable text, exact hash suppression, store success; no content change in admission | Operational admission for retention; JSON/embedding/hash checks license processing, not factual truth | no instance observed; SRC-1 `mem0/memory/main.py:994-1113`; CLM-1 mismatch |
| RTE-1 retention | implemented | Candidate text becomes current vector record with metadata | Available to RTE-1 and RTE-3; retention precedes any evidenced epistemic acceptance | no instance observed; see OBJ-1 and BAP-1 |
| RTE-2 content transformation | implemented | Raw import or caller-chosen revision/withdrawal; caller is proposer/decider, structural checks are executor | Caller-selected memory content; external justification unknown | no instance observed; SRC-1 `mem0/memory/main.py:881-916,1829-1974,2052-2143` |
| RTE-3 operational admission/selection/consumption | implemented | No content change; query filters, vector relevance, conditional lexical/entity score and expiry | Ranking/availability authority, no truth check; BAP-2 governs external delivery | no instance observed; SRC-1 `mem0/memory/main.py:1222-1392,1393-1537,1642-1828` |
| RTE-4 content transformation | implemented | Agent execution-history summary; intended non-ampliative reshaping, actual preservation indeterminate | CMP-2 supplies a nonempty candidate; no inspected fidelity comparator | no instance observed; SRC-1 `mem0/memory/main.py:2007-2050`; CLM-2 |
| RTE-4 retention | implemented | Summary and type metadata become ordinary searchable memory | Available for later context; no post-acceptance lifecycle integration is established | no instance observed; see RTE-4 and BAP-1 and BAP-2 |

Ancillary entity/context/history functions are lifecycle plumbing, not extra acceptance stages. Their source-native persistence and selector roles are on shared records. Every implementation above is conditional on API invocation/dependencies, not evidence of execution. There is no mismatch between a deliberately operational memory scope and a knowledge-production goal it did not undertake; the specific mismatches are CLM-1's mutation description and CLM-2's unverified fidelity requirements.

#### 4. Per-object lifecycle disposition

OBJ-1 via RTE-1: transformation **indeterminate** between faithful extraction/reshaping and ampliative interpretation. The prompt permits implicit preferences and context enrichment, so unconditional entailment is unwarranted. Lineage retains text, scope, hash, timestamps and optional attribution but not a source-to-each-claim proof. Implemented checks are parse/embedding/hash/persistence; current warrant is source/model-dependent. Candidate state is **no instance observed** at production, checking, admission and use; claim-level acceptance and post-acceptance integration are not determinable from those checks. Paired messages, extracted entries and a defined fidelity criterion would resolve preservation for actual cases.

Procedural text via RTE-4: intended non-ampliative summary; actual transformation **indeterminate** because verbatim preservation is a prompt instruction, and no candidate execution is retained. The same no-instance state applies. A stored narrative of errors is neither a formulated criticism of the extraction method nor a later-consumed correction unless a corresponding route is shown.

OBJ-2 and OBJ-3: acquisition/bookkeeping and bounded presentation reshaping; discovery lifecycle **not applicable** to those operations. They preserve submitted/event text within storage mechanics, not independent source truth. OBJ-4: transformation **indeterminate** for entity equivalence judgments; label/link production and use are implemented, but semantic entity identity and observed candidate dispositions are unestablished. No lifecycle record for numeric access data: no candidate truth-apt output is individuated there; relevant direct adaptation is access/ranking maintenance. OBJ-5 is authored method guidance acquired from shipped/configured text; no observed candidate test/revision lifecycle. There is no global “no truth-apt output” conclusion because OBJ-1 and procedural text do carry candidate claims.

#### 5. System-claim versus route comparison

CLM-1: doctrine says automatic add/update/delete; RTE-1 implements additive extraction, RTE-2 supplies explicit mutations. No observed or causal support was supplied for automatic reconciliation. CLM-2: the prompts declare completeness, attribution and output preservation; RTE-1 and RTE-4 implement generation and retention, with structural rather than factual checks. No retained run establishes adherence. CLM-3: the README documents an assistant role consuming retrieved text; RTE-3 affords that route, with no observed host activation or causal outcome. Each conclusion is bounded to the cited path and its evidence layer.

#### 6. Bounded conclusion

The subsystem acquires submitted content, proposes derived memories, retains eligible candidates and selects them for later use. The core admission checks authorize storage/use, not accepted truth. Existing text can influence later extraction and external replies, but no result here establishes which model interpretations are faithful, which memories improve a response, or which content deserves epistemic acceptance. Explicit editing is a recovery surface whose justification belongs to the caller.

## Reconciliation

The commissioned input SHA-256 is `9e76234f73769f98484fe79e0f0f9ce3be80b1a47ca05aff20bfe1d8dbc82b6c`; the specialist method SHA-256 is `193df45a1b39c1ecdb5c4774d3fbbde0f9fc914f81fd60269a8d63ef959fbd1d`. The complete report's run, repository, full commit, input hash and bytes match this run. Its reported model identity is unknown. All comparison evidence and substantive limitations are integrated here, so the local report is provenance rather than a required reading dependency.

Exact token mappings: MEM-RTE-1 → RTE-5; MEM-RTE-2 → RTE-6. All other supplied IDs retain their referents. RTE-5 is automatic context supply/window maintenance within RTE-1; RTE-6 is entity access maintenance/ranking serving RTE-1, RTE-2 and RTE-3. These are shared subroutes, not duplicated independent pipelines.

All eight report issues are accepted: (1) register RTE-5 and preserve wired push separately from afforded pull; (2) register RTE-6 and attach dedup to retained entity sets; (3) amend RTE-1 to ADD-only while RTE-2 owns replacement/deletion; (4) retain discarded model-link versus compiled entity-link distinction on OBJ-4/RTE-1; (5) bound expiry and identity immutability to actual paths/fields; (6) preserve RTE-4 and its custom-prompt uncertainty, without executable-skill or rationale claims; (7) keep learning_scope partial and faithfulness_tested not-determinable; (8) retain raw/procedural bypasses, uninitialized-index cleanup and best-effort multi-store effects. No blocking conflict remains. After the specialist turn ended, the coordinator mechanically corrected citation endpoints beyond the exact blob lengths in the report and this result; quoted bytes and all substantive findings/profile values are unchanged. A specialist follow-up could not run because the thread limit was reached. The report discloses this correction and was revalidated before its final hash was bound here.

The coordinator independently traced the additive/docstring mismatch and public/internal expiry split before receiving the report, but sent the additive finding to the specialist while it was working. That exchange is recorded as a shared correction, not independent convergence. The epistemic overlay cites the adopted memory records and adds no stronger consumption, fidelity or improvement claims. No prior reviews, other pilots or comparison outputs supplied source findings.

## Bounded synthesis

Mem0's scoped OSS subsystem makes accumulated conversational material available both to its own next extraction and to an external requesting application. Its strongest supported contribution is a wired, bounded context-and-write route: it retrieves existing entries and recent messages, produces structured candidate facts, retains successful writes, and can derive a task-continuation summary. This establishes retained adaptation at the memory layer. It does not establish improved future capacity attributable to criticism, because no such outcome comparison was observed.

The ordinary path is additive. Separate explicit mutation, expiration, recent-message eviction and history provide maintenance with different effects and recovery limits. Public hybrid retrieval applies richer scoring and expiry suppression than internal extraction retrieval. These distinctions matter when a caller assumes a correction, deletion or expiry acts identically on every consumer. Per-value comparison evidence preserves the actual witness: internal context assembly is wired; the external answer consumer is documented and afforded.

For **theory-builder conditions 1–4**, OBJ-5 provides a localized proposed method for extracting useful memory (condition 1: `wired` as explicit text) and RTE-1 and RTE-4 consume it (condition 2: `wired`). Content-directed criticism of that method and a criticism-responsive successor are `uninspected` beyond the finite harness; no such method-revision path was found in the inspected coordinator functions. Iteration of a criticized method is likewise `uninspected`, so theory-builder membership is not established. The stored facts themselves are not all automatically theories: whether an actual entry formulates a proposed solution, and what criticism it receives inside the model, needs instance evidence. Addressability is entry-level for memory CRUD and section-level for prompts; persisted criticism/assumptions are not required fields. Memory text and selected recent messages persist across invocations; only the externally documented task/agent roles support task-horizon interpretations, not identity labels alone.

**Learning:** wired memory accumulation and reuse are the supported partial contribution; improved capacity caused by criticism is `uninspected`. **Reflection:** agent-perspective facts and task summaries can represent an excluded host, but no causally connected self-representation of the scoped Memory machinery was established (`uninspected`). **Autonomous theory builder:** `inapplicable` as a demonstrated qualifier because builder membership is unestablished; computational proposal/admission and caller-controlled explicit edits are described separately above. **Self-improvement:** retained context changes future inputs (`wired`); improvement to the subsystem's method or capacities from evaluating its own operation remains `uninspected`. These properties are independent, and the comparison axis trace_learning has its narrower write-route meaning.

Evidence that would change the assessment includes retained paired extraction/recall executions testing fidelity and dependence, an explicit content-directed revision-and-reuse route for method texts, a common expiry predicate on all read paths, and transaction/recovery evidence across vector, history and message storage. A different provider, async implementation or cloud scope requires its own analysis.

## Limitations

| limitation | affected source, record, or route IDs | inspected boundary | conclusion prevented | evidence that would resolve it |
|---|---|---|---|---|
| No executed model/recall comparison | SRC-1, SRC-2, RTE-1, RTE-3, RTE-4 | Static synchronous subsystem | Observed fidelity, activation, learning or causal benefit | Retained paired inputs, outputs, intervention and assessment |
| Provider/dependency internals opaque | CMP-2, CMP-3, CMP-4, CMP-5 | Adapter calls and local loading code | Exact weight fixity, training and dependency-level correctness | Immutable model/dependency artifacts and appropriate probes |
| Host/cloud/async/alternate providers excluded | RTE-1, RTE-2, RTE-3, RTE-4 | Declared OSS scope | Whole-product completeness, deployed isolation or universal guarantees | Separate frozen source boundaries and route inspections |
| No source-to-claim acceptance record | OBJ-1, RTE-1, RTE-4 | Extraction and summary admission | Established source truth or epistemic acceptance | Candidate-linked support/check and intended-use criterion |
| Best-effort cross-store effects | RTE-1, RTE-2 | Successful primary writes and auxiliary maintenance | Atomic multi-store recovery and exactly-once replay | Fault-intervention traces and explicit recovery contract |

## Verification and blockers

### Semantic verification

Checked every admitting route RTE-1, RTE-2, RTE-4, RTE-5 and RTE-6 for trigger, proposal/admission/veto, retained result, later consumer and recovery. Checked RTE-3 alternatives against scope/expiry/selection claims. Canonical IDs are unique, complete and mapped by exact tokens; the six shared subsections preserve generic ownership. All fourteen comparison axes match the synchronous default-provider boundary and keep per-value evidence separate from coverage.

RTE-1 and RTE-4 were each checked for trace-fed production, persistence and later RTE-5 consumption; source, horizon, timing and text form were assessed for both. Raw OBJ-3 logging alone does not establish trace learning. Default procedural continuation supports per-task, while ordinary/custom branches keep horizon coverage partial. Read-back push signals name a real selector: exact identity matches retained rows/partitions, and embedding similarity selects prior fact text. Public lexical/entity scoring remains on requested pull and is not misclassified as another push signal. Static prompts and provider parameters stay outside the changed-through-use memory profile. Explicit update/delete, entity merging and recent-message eviction support distinct maintenance values.

Checked status separation: implementation is wired, documented external consumption is afforded, prompts are claimed requirements, and every epistemic candidate state remains no instance observed. Source quotations preserve exact text at the full frozen commit and support their attached mechanisms; no quotation stands in for an absence boundary. Theory-builder conditions, learning, reflection, autonomy and self-improvement are separate findings. Partial task horizon and unavailable execution evidence are retained uncertainties, not structural blockers. Source/method/input/report identity checks passed; deterministic validation and frozen-source publication checks are required before projection.

### Deterministic validation

Target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-mem0-02/result.md`. `commonplace-validate --full` passed with no warnings or failures on the completed result; publication also checks the frozen-source anchors and exact bytes.

### Blockers

none

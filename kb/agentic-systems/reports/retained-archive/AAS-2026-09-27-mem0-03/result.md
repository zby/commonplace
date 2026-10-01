---
{
  "type": "types/agentic-system-analysis-result.md",
  "description": "Mem0: additive memory extraction, contextual read-back and service control at a pinned source boundary",
  "run-id": "AAS-2026-09-27-mem0-03",
  "system": "Mem0",
  "run-date": "2026-09-27",
  "result-disposition": "complete",
  "target-class": "memory/knowledge/context-engineering system",
  "boundary-kind": "whole-system",
  "reviewed-boundary": "94c3fe9f238f3dbf29c9ce98643bd71eb13077cd",
  "analysis-cutoff": "2026-09-27",
  "evidence-tier": "code-grounded",
  "memory-comparison": {
    "scope": "Retained Python OSS facts, procedural summaries, entity access structures, raw message history; shared Python agent-plugin-core local traces, spool, hosted memory objects and later coding-agent recall. Hosted internals, TypeScript SDK and other host adapters are included opaque/uninspected alternatives. External provider internals and deployed outcomes are excluded.",
    "axes": {
      "storage_substrate": {
        "assessment": "partial",
        "values": [
          "vector",
          "sqlite",
          "files",
          "service-object"
        ],
        "evidence": {
          "vector": {
            "basis": "wired",
            "records": [
              "OBJ-3",
              "OBJ-4"
            ],
            "note": "Python memory and entity collections use vector stores."
          },
          "sqlite": {
            "basis": "wired",
            "records": [
              "OBJ-5",
              "OBJ-6"
            ],
            "note": "Python history/messages and plugin evidence/retrieval tables."
          },
          "files": {
            "basis": "wired",
            "records": [
              "OBJ-6"
            ],
            "note": "Pending flush handoffs persist as JSON files."
          },
          "service-object": {
            "basis": "wired",
            "records": [
              "OBJ-7",
              "RTE-8"
            ],
            "note": "Plugin writes and retrieves hosted memory objects; physical backend storage is opaque."
          }
        },
        "records": [
          "OBJ-3",
          "OBJ-4",
          "OBJ-5",
          "OBJ-6",
          "OBJ-7",
          "RTE-8"
        ],
        "note": "Hosted internals, TypeScript SDK and other host adapters remain opaque or uninspected; this is a supported subset."
      },
      "representational_form": {
        "assessment": "partial",
        "values": [
          "natural-language",
          "symbolic"
        ],
        "evidence": {
          "natural-language": {
            "basis": "wired",
            "records": [
              "OBJ-3",
              "OBJ-5",
              "OBJ-7"
            ],
            "note": "Fact text, messages and returned memory text."
          },
          "symbolic": {
            "basis": "wired",
            "records": [
              "OBJ-4",
              "OBJ-6"
            ],
            "note": "Entity-to-memory links, structured scope and retrieval metadata."
          }
        },
        "records": [
          "OBJ-3",
          "OBJ-5",
          "OBJ-7",
          "OBJ-4",
          "OBJ-6"
        ],
        "note": "Hosted internals, TypeScript SDK and other host adapters remain opaque or uninspected; this is a supported subset. Vector embeddings are access representations, not evidence of trained memory parameters."
      },
      "lineage": {
        "assessment": "partial",
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
              "RTE-6"
            ],
            "note": "Caller text can be stored directly with infer=False or explicitly update an entry."
          },
          "imported": {
            "basis": "wired",
            "records": [
              "OBJ-5",
              "OBJ-6"
            ],
            "note": "Message and tool-event inputs are retained from host/caller traces."
          },
          "trace-extracted": {
            "basis": "wired",
            "records": [
              "RTE-5"
            ],
            "note": "LLM turns conversation messages into durable facts."
          },
          "other-compiled": {
            "basis": "wired",
            "records": [
              "OBJ-4"
            ],
            "note": "Entity extraction derives symbolic access links from retained fact text."
          }
        },
        "records": [
          "RTE-6",
          "OBJ-5",
          "OBJ-6",
          "RTE-5",
          "OBJ-4"
        ],
        "note": "Hosted internals, TypeScript SDK and other host adapters remain opaque or uninspected; this is a supported subset."
      },
      "behavioral_authority": {
        "assessment": "partial",
        "values": [
          "knowledge",
          "ranking"
        ],
        "evidence": {
          "knowledge": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-9"
            ],
            "note": "Prior facts enter extractor context; plugin memories enter coding-agent additionalContext."
          },
          "ranking": {
            "basis": "wired",
            "records": [
              "OBJ-4",
              "RTE-7"
            ],
            "note": "Retained entity links contribute boosts to memory ranking."
          }
        },
        "records": [
          "RTE-5",
          "RTE-9",
          "OBJ-4",
          "RTE-7"
        ],
        "note": "Hosted internals, TypeScript SDK and other host adapters remain opaque or uninspected; this is a supported subset. No shipped static prompt is counted as accumulated memory authority."
      },
      "write_agency": {
        "assessment": "partial",
        "values": [
          "automatic",
          "manual"
        ],
        "evidence": {
          "automatic": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-8"
            ],
            "note": "Automatic extraction and hook-driven persistence; user triggering does not make extraction manual."
          },
          "manual": {
            "basis": "wired",
            "records": [
              "RTE-6"
            ],
            "note": "Explicit authoring/update/deletion interface controls retained text."
          }
        },
        "records": [
          "RTE-5",
          "RTE-8",
          "RTE-6"
        ],
        "note": "Hosted internals, TypeScript SDK and other host adapters remain opaque or uninspected; this is a supported subset."
      },
      "curation_operations": {
        "assessment": "partial",
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
            "note": "Near-matching retained entities merge their linked-memory sets; fact acquisition hash suppression alone is not this witness."
          },
          "evolve": {
            "basis": "wired",
            "records": [
              "RTE-6"
            ],
            "note": "Explicit update rewrites an existing UUID and records the previous text."
          },
          "invalidate": {
            "basis": "wired",
            "records": [
              "RTE-6"
            ],
            "note": "Deletion removes current vector entry while history retains the withdrawn text."
          },
          "decay": {
            "basis": "wired",
            "records": [
              "OBJ-5"
            ],
            "note": "Rolling message retention evicts older messages beyond ten per scope."
          }
        },
        "records": [
          "OBJ-4",
          "RTE-6",
          "OBJ-5"
        ],
        "note": "Hosted internals, TypeScript SDK and other host adapters remain opaque or uninspected; this is a supported subset. These witnesses include access metadata and raw context within the declared memory boundary, not solely derived facts."
      },
      "read_back_direction": {
        "assessment": "partial",
        "values": [
          "pull",
          "push"
        ],
        "evidence": {
          "pull": {
            "basis": "wired",
            "records": [
              "RTE-10"
            ],
            "note": "Coding agent calls the MCP search tool and gets requested text."
          },
          "push": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-9"
            ],
            "note": "Extractor receives automatic prior-memory context; first-prompt hook supplies prior memories to the coding agent."
          }
        },
        "records": [
          "RTE-10",
          "RTE-5",
          "RTE-9"
        ],
        "note": "Hosted internals, TypeScript SDK and other host adapters remain opaque or uninspected; this is a supported subset."
      },
      "read_back_signal": {
        "assessment": "partial",
        "values": [
          "identifier",
          "inferred-embedding"
        ],
        "evidence": {
          "identifier": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-9"
            ],
            "note": "Automatic context is scoped by identity: OSS history session scope and plugin repository/user filters."
          },
          "inferred-embedding": {
            "basis": "wired",
            "records": [
              "RTE-5"
            ],
            "note": "OSS add automatically embeds incoming messages and selects ten prior facts for its extraction LLM."
          }
        },
        "records": [
          "RTE-5",
          "RTE-9"
        ],
        "note": "Hosted internals, TypeScript SDK and other host adapters remain opaque or uninspected; this is a supported subset. Hosted query-matching internals are not inferred from the API name; requested OSS search lexical scoring does not itself establish lexical push."
      },
      "trace_learning": {
        "assessment": "partial",
        "values": [
          "yes"
        ],
        "evidence": {
          "yes": {
            "basis": "wired",
            "records": [
              "RTE-5"
            ],
            "note": "Conversation-fed automatic fact creation persists into later extraction context. This is behavior-shaping recall, not evidence of improved performance."
          }
        },
        "records": [
          "RTE-5"
        ],
        "note": "Hosted internals, TypeScript SDK and other host adapters remain opaque or uninspected; this is a supported subset. Plugin generation depends on opaque hosted extraction; procedural generation lacks inspected end-user continuation wiring."
      },
      "trace_source": {
        "assessment": "partial",
        "values": [
          "session-logs",
          "event-streams",
          "tool-traces",
          "trajectories"
        ],
        "evidence": {
          "session-logs": {
            "basis": "wired",
            "records": [
              "RTE-5"
            ],
            "note": "Conversation message histories feed OSS extraction."
          },
          "event-streams": {
            "basis": "afforded",
            "records": [
              "RTE-8"
            ],
            "note": "Hook events feed a staged hosted extraction request and a later coding-agent recall route."
          },
          "tool-traces": {
            "basis": "afforded",
            "records": [
              "RTE-8"
            ],
            "note": "Changed paths and conditional command evidence join conversation messages in hosted extraction input."
          },
          "trajectories": {
            "basis": "afforded",
            "records": [
              "RTE-11"
            ],
            "note": "Procedural summary generation accepts execution history for a named task-continuation consumer; no dedicated continuation assembly was inspected."
          }
        },
        "records": [
          "RTE-5",
          "RTE-8",
          "RTE-11"
        ],
        "note": "Hosted internals, TypeScript SDK and other host adapters remain opaque or uninspected; this is a supported subset. Hosted transformation is opaque; the plugin orchestration is wired."
      },
      "learning_scope": {
        "assessment": "partial",
        "values": [
          "per-project",
          "cross-task",
          "per-task"
        ],
        "evidence": {
          "per-project": {
            "basis": "afforded",
            "records": [
              "RTE-8",
              "RTE-9"
            ],
            "note": "Project memory is extracted for later coding work and recalled within repository scope."
          },
          "cross-task": {
            "basis": "afforded",
            "records": [
              "RTE-8",
              "RTE-10"
            ],
            "note": "The implementation explicitly waits for extraction before a later task can search; tool description offers earlier-work recall."
          },
          "per-task": {
            "basis": "afforded",
            "records": [
              "RTE-11"
            ],
            "note": "The procedural prompt names an agent continuing its current task; generated summaries persist and generic retrieval is available. Dedicated continuation wiring is uninspected."
          }
        },
        "records": [
          "RTE-8",
          "RTE-9",
          "RTE-10",
          "RTE-11"
        ],
        "note": "Hosted internals, TypeScript SDK and other host adapters remain opaque/uninspected. OSS identity scopes alone do not establish horizons; procedural per-task scope comes from the explicit continuation consumer, at afforded strength."
      },
      "learning_timing": {
        "assessment": "partial",
        "values": [
          "online",
          "staged"
        ],
        "evidence": {
          "online": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-11"
            ],
            "note": "OSS add runs extraction and persistence during the caller operation, feeding later add operations. Procedural generation also runs during add, but its later task-continuation use is only afforded."
          },
          "staged": {
            "basis": "afforded",
            "records": [
              "RTE-8"
            ],
            "note": "Hook events spool locally, then checkpoint/session-end handoff sends batches to hosted extraction before later recall."
          }
        },
        "records": [
          "RTE-5",
          "RTE-8",
          "RTE-11"
        ],
        "note": "Hosted internals, TypeScript SDK and other host adapters remain opaque or uninspected; this is a supported subset. Staged orchestration is wired; opaque hosted transformation limits the qualifying learning chain."
      },
      "distilled_form": {
        "assessment": "partial",
        "values": [
          "natural-language",
          "symbolic"
        ],
        "evidence": {
          "natural-language": {
            "basis": "wired",
            "records": [
              "RTE-5",
              "RTE-11"
            ],
            "note": "Extracted fact text is consumed by later extraction. Procedural continuation summaries are also natural-language output, with later consumption afforded."
          },
          "symbolic": {
            "basis": "wired",
            "records": [
              "OBJ-4",
              "RTE-7"
            ],
            "note": "Trace-derived facts produce persistent entity links consumed by the later ranker."
          }
        },
        "records": [
          "RTE-5",
          "OBJ-4",
          "RTE-7",
          "RTE-11"
        ],
        "note": "Hosted internals, TypeScript SDK and other host adapters remain opaque or uninspected; this is a supported subset. These are the same OSS fact routes and hosted extraction family used for source/scope/timing; no parameter learning is established."
      },
      "faithfulness_tested": {
        "assessment": "uninspected",
        "values": [],
        "evidence": {},
        "records": [
          "CLM-4"
        ],
        "note": "No retained execution evidence testing dependence on recalled content was inspected; test source or retrieval telemetry would not by itself establish yes."
      }
    }
  }
}
---

# Mem0 — exact agentic-system analysis

## Run identity

**Run state:** kb/reports/state/agentic-system-analysis/AAS-2026-09-27-mem0-03/run-state.md
**Generated review:** kb/agentic-systems/reviews/mem0.md
**Memory analysis report:** kb/reports/state/agentic-system-analysis/AAS-2026-09-27-mem0-03/memory-report.md
**Memory analysis report SHA-256:** ab99229977c752ed19e26f7f76b5565bf2dd0fe714a358d1477567ba1b171bad
Coordinator model: unknown; runtime identifies the agent as GPT-6-based but does not expose an exact model identifier. Specialist model identity is retained with its report.

## Boundary and evidence

Evidence basis: implementation and shipped documentation inspected at commit `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` on 2026-09-27; no execution or causal experiment performed. This result explains the repository-supplied Mem0 memory library, HTTP service and representative shared host-integration mechanisms. It is a whole-system account at that responsibility horizon, not an enclosing autonomous agent. Mem0 returns memories and service results; consuming applications and hosts own task planning, tools, final answers and actual use of supplied context.

The source boundary includes Python OSS sync/async memory, hosted-client interfaces, shared agent-plugin-core, representative host connections, server control and configurable models. TypeScript SDK and other host-specific differences remain included but incompletely inspected alternatives; their unknowns limit aggregate coverage. The hosted backend, external LLM/embedding internals, deployed databases and host runtime internals are opaque external dependencies. Their exclusion prevents claims about hosted extraction policy, exact model weights, deployed isolation, successful context activation or measured benefit. The reviewed code is evidence of wiring; a mutable package install or provider endpoint is not pinned by the repository commit. No prior system analyses informed this construction.

## Source register

| Source ID | Kind | Identity/location | Revision | Evidence layer | Inspected scope | Citation anchors | Access gaps and prevented conclusion |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/mem0ai/mem0` | `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` | Implementation, separately from doctrine/design in README and prompts | Python memory/configuration/provider code, server control, shared plugin routes detailed below; docs describe intended roles | Full commit-relative paths on records; generated quotes bind exact bytes | No provider/backend runs or causal comparisons; remaining SDK/adapters partial |

Access root: `/home/zby/llm/commonplace/related-systems/mem0ai--mem0`. Origin and full commit verified. All source content came from commit-addressed Git reads. Incumbent destination was inspected only through the publication command, returning eligibility and digest; its prose was not read.

## Shared records

### Components

### CMP-1 — Extraction and summary LLM

Implementation conclusion status: wired. The Python OpenAI adapter calls a configured model endpoint and returns generated text. Default identity is `gpt-5-mini`; alternate providers and caller models are configurable. Exact-weight identity conclusion status: uninspected; the alias does not pin provider weights. Parameter-update conclusion status: uninspected for provider internals; inspected adapter performs inference and has no optimizer in that call path. This does not rule out memory-mediated adaptation. Evidence: SRC-1 `mem0/llms/openai.py`, `mem0/utils/factory.py`, `mem0/configs/llms/base.py`. Representation is distributed-parametric behind a request/response API.

> if not self.config.model:
>             self.config.model = "gpt-5-mini"
> --- `mem0/llms/openai.py:39-40` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-2 — Embedding model

Implementation conclusion status: wired. Default `text-embedding-3-small` embeds memory and query text; configurable URL and model resolve through an external provider. Exact-weight identity and provider parameter changes: uninspected. The inspected adapter normalizes newlines, sends embedding requests and checks batch result length; it does not train the model. Evidence: SRC-1 `mem0/embeddings/openai.py`.

> self.config.model = self.config.model or "text-embedding-3-small"
> --- `mem0/embeddings/openai.py:15-15` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-3 — Optional spaCy analysis

Implementation conclusion status: wired. Shared loader uses installed `en_core_web_sm`, downloading it if missing, for entity and lemma preprocessing. Deployment model version is uninspected: this loader names a package without binding its bytes. Operational parameter training is uninspected beyond these inference-only loader routes. Failure is cached and returns no model, allowing reduced NLP functionality. Evidence: SRC-1 `mem0/utils/spacy_models.py`, `mem0/utils/entity_extraction.py`.

> _nlp_full = spacy.load("en_core_web_sm")
> --- `mem0/utils/spacy_models.py:60-60` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-4 — Optional relevance reranker

Implementation conclusion status: wired. Search optionally reranks retrieved candidates and falls back to original results on failure. Inspected LLM reranker asks a configured model for relevance scores, clamps parsed numbers, uses 0.5 on scoring failure and sorts. This is relevance ranking, not an answer oracle or truth check. Other configured reranker implementations and their exact parameter identities remain uninspected. Evidence: SRC-1 `mem0/reranker/llm_reranker.py`, `mem0/memory/main.py`.

> "Given a query and a document, score how relevant the document is to the query.\n\n"
> --- `mem0/reranker/llm_reranker.py:80-80` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### Operative objects

### OBJ-1 — Server configuration and persisted overrides

Implementation conclusion status: wired. Symbolic configuration dictionaries describe provider choices and natural-language custom extraction instructions. The server holds a current dictionary and memory instance, with JSON overrides in relational Settings storage. Runtime initialization consumes merged defaults/overrides. This is configuration authority for subsequent operations; it is not acquired memory in the comparison profile. Evidence: SRC-1 `server/server_state.py`, `mem0/configs/base.py`.

### OBJ-2 — Generated instruction and test-message proposal

Implementation conclusion status: wired. A use-case request produces natural-language custom instructions and an example test message. Both are returned to the caller, not installed by the generation endpoint. The instruction text proposes priorities, while the example supplies no independent expected answer or validation evidence. Evidence: SRC-1 `server/main.py`.

> return {"custom_instructions": instructions, "test_message": test_message}
> --- `server/main.py:362-362` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### OBJ-3 — Python fact text and procedural summaries

Object; implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/main.py`, `mem0/configs/prompts.py`. The vector-store payload contains natural-language `data`, a UUID, text hash, lemmatized text, creation/update timestamps, caller scope metadata, and optional attribution. Embeddings support access; they are not modified model weights. Facts are trace-extracted; direct `infer=False` writes may be authored or imported. Procedural summaries occupy the same store with a memory-type marker. Later consumers are the extraction LLM through RTE-5 and retrieval callers through RTE-7; no special procedural continuation consumer was established.

> memory_id = str(uuid.uuid4())
>             mem_metadata = deepcopy(metadata)
>             mem_metadata["data"] = text
>             mem_metadata["text_lemmatized"] = text_lemmatized
>             mem_metadata["hash"] = mem_hash
>             if "created_at" not in mem_metadata:
>                 mem_metadata["created_at"] = datetime.now(timezone.utc).isoformat()
>             mem_metadata["updated_at"] = mem_metadata["created_at"]
>             if mem.get("attributed_to"):
>                 mem_metadata["attributed_to"] = mem["attributed_to"]
> 
>             records.append((memory_id, text, embed_map[text], mem_metadata))
> --- `mem0/memory/main.py:1030-1041` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> metadata = {**metadata, "memory_type": MemoryType.PROCEDURAL.value}
>         embeddings = self.embedding_model.embed(procedural_memory, memory_action="add")
>         memory_id = self._create_memory(procedural_memory, {procedural_memory: embeddings}, metadata=metadata)
>         capture_event("mem0._create_procedural_memory", self, {"memory_id": memory_id, "sync_type": "sync"})
> 
>         result = {"results": [{"id": memory_id, "memory": procedural_memory, "event": "ADD"}]}
> --- `mem0/memory/main.py:2043-2048` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### OBJ-4 — Entity collection and linked-memory access metadata

Object; implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/main.py`. The lazy entity store uses the configured vector provider in a separate entities collection. Entity extraction derives entity text/type and linked-memory-ID sets from persisted fact texts. Exact normalized matches or semantic matches at 0.95 merge linked sets into existing entity records. This supports dedup of retained access metadata, not a claim that whole fact records merge. Query entity matches subsequently contribute memory ranking boosts (RTE-7). Form is symbolic plus natural-language labels; derivation is other-compiled from facts. Authority is ranking. There is no retained explanation of why one entity link is correct beyond text and identity/score data.

> semantic_match = matches[0] if matches and matches[0].score >= 0.95 else None
>                         match = exact_match or semantic_match
>                         if match:
>                             # Update existing entity
>                             payload = match.payload or {}
>                             linked = set(payload.get("linked_memory_ids", []))
>                             linked |= memory_ids
>                             payload["linked_memory_ids"] = sorted(linked)
>                             try:
>                                 self.entity_store.update(
>                                     vector_id=match.id,
>                                     vector=None,
>                                     payload=payload,
> --- `mem0/memory/main.py:1166-1178` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> for match in matches:
>                         similarity = match.score if hasattr(match, 'score') else 0.0
>                         if similarity < 0.5:
>                             continue
> 
>                         payload = match.payload if hasattr(match, 'payload') else {}
>                         linked_memory_ids = payload.get("linked_memory_ids", [])
>                         if not isinstance(linked_memory_ids, list):
>                             continue
> 
>                         num_linked = max(len(linked_memory_ids), 1)
>                         memory_count_weight = 1.0 / (1.0 + 0.001 * ((num_linked - 1) ** 2))
>                         boost = similarity * ENTITY_BOOST_WEIGHT * memory_count_weight
> 
>                         for memory_id in linked_memory_ids:
>                             if memory_id:
>                                 memory_key = str(memory_id)
>                                 memory_boosts[memory_key] = max(memory_boosts.get(memory_key, 0.0), boost)
> --- `mem0/memory/main.py:1805-1822` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### OBJ-5 — Python SQLite message window and mutation history

Object; implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/storage.py`, `mem0/memory/main.py`. Raw message rows retain role/content/name under a deterministic scope assembled from provided user/agent/run IDs. The next extraction consumes the latest ten. `save_messages` evicts older messages beyond ten per scope: a narrow decay witness on raw context. Separate history retains old/new text and operation metadata for explicit history callers. History is not an automatic rationale/review loop; no consumer of mutation reasons was found, and there is no reason column in this schema.

> CREATE TABLE IF NOT EXISTS history (
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
> --- `mem0/memory/storage.py:108-119` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> # Evict old messages beyond the most recent 10 for this scope.
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
>                 )
> --- `mem0/memory/storage.py:279-291` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### OBJ-6 — Plugin local evidence, retrieval cache and flush spool

Object; implementation conclusion status: wired. Evidence: SRC-1 `integrations/agent-plugin-core/python/memory_core.py`, `integrations/agent-plugin-core/python/hook_runner.py`. SQLite holds events, session scopes, flush state, retrieval texts, operations and subagent records. Pending worker handoffs additionally use JSON files. Events are imported/raw session details; extraction-message packets are deterministic selections/formatting. These are distinct from hosted derived memories. Retrieval copies preserve returned memory text for later subagent context reuse, but `search_memories` marks them before `format_context` trims the returned text to budget. Thus the cache's claim to contain the exact supplied memories is stronger than demonstrated formatted delivery. Event and flush metadata support recovery and diagnostics, not model-weight training.

> CREATE TABLE IF NOT EXISTS events (
>                 id INTEGER PRIMARY KEY AUTOINCREMENT,
>                 repo_id TEXT NOT NULL,
>                 app_id TEXT NOT NULL,
>                 session_id TEXT NOT NULL,
>                 created_at TEXT NOT NULL,
>                 kind TEXT NOT NULL,
>                 payload_json TEXT NOT NULL,
>                 flush_id TEXT
>             );
>             CREATE INDEX IF NOT EXISTS events_session_idx
>                 ON events(repo_id, session_id, flush_id, id);
> --- `integrations/agent-plugin-core/python/memory_core.py:600-611` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> pending_dir = data_dir() / "pending"
>     pending_dir.mkdir(parents=True, exist_ok=True)
>     material = (
>         f"{hook_input.get('cwd', '')}\0{hook_input.get('session_id', '')}\0{reason}"
>     )
>     digest = hashlib.sha256(material.encode()).hexdigest()[:24]
>     handoff_path = pending_dir / f"{digest}-{uuid.uuid4().hex[:8]}.json"
>     temporary_path = handoff_path.with_suffix(".tmp")
>     temporary_path.write_text(
>         json.dumps({
>             "hook_input": hook_input,
>             "reason": reason,
>             "wait_for_inflight": wait_for_inflight,
>         }),
>         encoding="utf-8",
>     )
>     temporary_path.replace(handoff_path)
> --- `integrations/agent-plugin-core/python/hook_runner.py:173-189` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> """Return the exact memories already supplied to the main conversation."""
>         rows = self.conn.execute(
>             """SELECT memory_id, rank, score, memory_text
>                FROM retrievals
>                WHERE session_id = ? AND repo_id = ?
>                ORDER BY COALESCE(rank, 2147483647), injected_at, memory_id""",
>             (session_id, repo_id),
>         ).fetchall()
> --- `integrations/agent-plugin-core/python/memory_core.py:1024-1031` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### OBJ-7 — Hosted memory objects and feedback interface

Object; interface conclusion status: wired. Backend conclusion status: uninspected. Evidence: SRC-1 `mem0/client/main.py`, `integrations/agent-plugin-core/python/memory_core.py`. The SDK and plugin call versioned add/search APIs and handle service memory IDs and text results. The plugin sends both shared-project and personal extraction instructions. Hosted object representation beyond returned fields, storage substrate, model/prompt changes, revision policy and causal effect of feedback remain opaque. `feedback_reason` can be submitted but the client shows no later route consuming the reason or revising memory because of it.

> kwargs = self._prepare_params(kwargs)
>         payload = self._prepare_payload(messages, kwargs)
>         response = self.client.post("/v3/memories/add/", json=payload)
>         response.raise_for_status()
> --- `mem0/client/main.py:334-337` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> data = {
>             "memory_id": memory_id,
>             "feedback": feedback,
>             "feedback_reason": feedback_reason,
>         }
> 
>         response = self.client.post("/v1/feedback/", json=data)
>         response.raise_for_status()
>         capture_client_event("client.feedback", self, {**data, "sync_type": "sync"})
>         return response.json()
> --- `mem0/client/main.py:1221-1230` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### Routes

### RTE-1 — Self-hosted HTTP admission and memory dispatch

Implementation conclusion status: wired. Trigger/principal: HTTP caller with JWT, API key or configured bypass. Next-step owner: FastAPI dependency and endpoint code; its symbolic policy authenticates, checks admin role for configuration/reset/bulk deletion and unrestricted listing, then dispatches to the shared Memory instance. Context includes request identifiers and filters. Immediate terminal output is the library result or HTTP error; later reads use the underlying memory routes, not the request log. Persistence is owned by the library/backend. Delegated visibility is determined by supplied identifiers and backend; host task delegation is outside this route. Selection is caller-directed, expiry handling follows library methods; the raw admin listing explicitly bypasses expiry filtering. No context activation is observed.

Authentication is not identical to ownership binding: inspected get-by-ID passes the requested ID directly after authentication, and add/search accept caller-supplied identifiers. A deployed tenant-isolation guarantee therefore cannot be inferred from the existence of login. Guarantee owner/enforcement: endpoint dependencies provide conditional protocol enforcement; direct Python calls bypass this HTTP guard, and AUTH_DISABLED permits unauthenticated requests. Current deployment grants and network isolation remain uninspected. Errors return through client-error/upstream-error paths; no cross-store rollback is promised here. Evidence: SRC-1 `server/main.py`, `server/auth.py`.

> def get_memory(memory_id: str, _auth=Depends(verify_auth)):
>     """Retrieve a specific memory by ID."""
>     try:
>         return get_memory_instance().get(memory_id)
> --- `server/main.py:444-447` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> if AUTH_DISABLED:
>         _mark_auth_type(request, "disabled")
>         return None
> --- `server/auth.py:167-169` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### RTE-2 — Administrative configuration replacement

Implementation conclusion status: wired. Trigger: admin caller submits updates. Proposer/decider is the caller; server role and bundled-provider checks can reject. The process merges OBJ-1, assigns current configuration, constructs a new Memory instance, and saves overrides. Guidance is operator-supplied symbolic settings and optional natural-language extraction instructions, retained as overrides for restart and consumed by subsequent memory calls. Immediate output reports successful configuration; later consumer is initialization or memory dispatch. No dynamic change to model weights is involved. No automatic diagnosis or evidence-based successor comparison is established; answer oracle is inapplicable to this configuration admission route.

Guarantee strength: protocol plus best-effort persistence, not atomic rollback. Assignment occurs before instance construction; failure may leave the dictionary changed while the old instance remains. Persistence errors are logged, not propagated. Recovery requires a subsequent caller update/restart using available persisted settings; automatic rollback is not present in the inspected function. Required external contract: provider construction, database transaction and credentials must succeed. Delegated visibility: the singleton affects server callers; no agent-level delegation rule. Selection/expiry: updated keys merge without a TTL. Operational effect is instance replacement; activation and improvement are unobserved. Addressability is configuration-key level. Theory-builder conditions 1–4 and learning are not established by operator edit admission alone. Evidence: SRC-1 `server/main.py`, `server/server_state.py`.

> def set_config(config: Dict[str, Any], _auth=Depends(require_admin)):
>     """Set memory configuration. Requires admin role."""
>     _validate_bundled_providers(config)
>     update_config(config)
> --- `server/main.py:333-336` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> next_config = _merge_config(_current_config, updates)
>         _current_config = next_config
>         _memory_instance = Memory.from_config(next_config)
>         overrides = _load_overrides()
>         overrides = _merge_config(overrides, updates)
>         _save_overrides(overrides)
> --- `server/server_state.py:89-94` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> except Exception:
>         logging.warning("Failed to persist config overrides to database", exc_info=True)
> --- `server/server_state.py:60-61` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### RTE-3 — Instruction proposal generation

Implementation conclusion status: wired. Authenticated use-case request makes CMP-1 propose OBJ-2 under a static format/priority prompt. The server splits text markers or returns the unsplit response with a default test sentence. Caller receives the result and retains veto over any later installation through RTE-2. No persistence, later read-back, expiry or delegation is implemented in this return-only endpoint; any subsequent adoption is afforded, not wired from this request. No actual test executes and no answer oracle is supplied. Recovery returns an upstream error. Its prompt is inspectable guidance, not a criticism process that revises the generator. Evidence: SRC-1 `server/main.py`.

> response = llm.generate_response([{"role": "user", "content": prompt}])
> --- `server/main.py:355-355` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### RTE-4 — Provider registration and deployment resolution

Implementation conclusion status: wired. Direct library code may register provider name/class/config mappings; factory import then runs that implementation under the process's authority. Registering caller owns proposal/admission and can overwrite the mapping. Rejection is normal factory/config/import failure, not a semantic review. Registry state is process-local; restoration requires re-registration or restart. Server configuration has a narrower bundled-provider allowlist. Static source-defined class mappings are not accumulated memory. Immediate return updates the mapping; future factory calls consume it. No expiry, agent delegation or automatic improvement test is specified. Guarantee strength is none for sandbox isolation inside imported provider code; deployed isolation is external. Evidence: SRC-1 `mem0/utils/factory.py`, `server/main.py`.

> if config_class is None:
>             config_class = BaseLlmConfig
>         cls.provider_to_class[name] = (class_path, config_class)
> --- `mem0/utils/factory.py:137-139` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

The shipped Compose command installs an unversioned `mem0ai` package before launching the server, so executing it does not establish execution of this pinned library. That deployment admission route changes installed runtime bytes according to package resolution; exact installed identity is uninspected.

> sh -c "rm -rf /app/packages && pip install -q --force-reinstall --no-deps mem0ai && alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
> --- `server/docker-compose.yaml:21-21` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### RTE-5 — Additive extraction and automatic context reuse

Route; implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/main.py`, `mem0/configs/prompts.py`. Trigger: caller add with inference enabled. Producer: configured LLM. Inputs: new parsed messages, ten recent scope-matched messages, ten prior facts selected by embedding search under scope filters, optional custom instructions. Persisted output: new fact UUIDs/text, embeddings, metadata, ADD history, entity links. Later add calls automatically supply retained facts and raw message history to the extraction LLM. That automatic selection is push into this named consumer; the caller did not individually request those memories. Identifier and inferred-embedding signals are both implemented. This supplies a wired trace-learning witness without claiming improved performance or a task horizon.

Normal extraction is additive. Output parse failure becomes no extracted memories while messages are still retained; LLM call failures raise. Text with no successful embedding is skipped; hash matches against retrieved existing facts/current batch are skipped. Persistence falls back from batch insertion to individual records and records success only for confirmed insertions. This is bounded duplicate admission, not an automatic semantic revision loop. The returned model's `linked_memory_ids` are not copied into the fact payload by the inspected persistence code; entity links are a separate mechanism. The prompt asks the LLM to avoid semantically equivalent re-extraction, but that is model-mediated admission rather than independent validation.

> # ROLE
> 
> You are a Memory Extractor — a precise, evidence-bound processor responsible for extracting rich, contextual memories from conversations. Your sole operation is ADD: identify every piece of memorable information and produce self-contained, contextually rich factual statements.
> 
> You extract from BOTH user and assistant messages. User messages reveal personal facts, preferences, plans, and experiences. Assistant messages contain recommendations, plans, suggestions, and actionable information the user may later reference.
> --- `mem0/configs/prompts.py:470-474` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> # Phase 0: Context gathering
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
> 
>         # Map UUIDs to integers (anti-hallucination)
>         existing_memories = []
>         uuid_mapping = {}
>         for idx, mem in enumerate(existing_results):
>             uuid_mapping[str(idx)] = mem.id
>             existing_memories.append({"id": str(idx), "text": mem.payload.get("data", "")})
> --- `mem0/memory/main.py:920-940` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> # === V3 PHASED BATCH PIPELINE (async) ===
> 
>         # Phase 0: Context gathering
>         session_scope = _build_session_scope(effective_filters)
>         last_messages = await asyncio.to_thread(self.db.get_last_messages, session_scope, 10)
>         parsed_messages = parse_messages(messages)
> 
>         # Phase 1: Existing memory retrieval
>         search_filters = {k: v for k, v in effective_filters.items() if k in ("user_id", "agent_id", "run_id") and v}
>         query_embedding = await asyncio.to_thread(self.embedding_model.embed, parsed_messages, "search")
>         existing_results = await asyncio.to_thread(
>             self.vector_store.search,
>             query=parsed_messages,
>             vectors=query_embedding,
>             top_k=10,
>             filters=search_filters,
>         )
> --- `mem0/memory/main.py:2600-2616` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

The sync and inspected async paths both use this additive design. Fact text may retain context/rationale in prose, but neither writer requires a separately checkable reason nor preserves the source message IDs for every fact. Later extraction reads the whole selected text; it can read any reason present, without a guarantee one exists.


Guidance and revision admission: the extraction prompt proposes relevance/completeness/deduplication rules; current optional caller instructions specialize them. Stored facts and recent messages supply data/reference context, not a separate authoritative answer oracle. The LLM proposes; parsing/dedup/embedding checks and store availability can veto individual writes. Code retains new text, not a formulated criticism record. Theory-builder conditions 1–4: localized guidance/text is wired; consumption as model input is wired; content-directed criticism and resulting revision or changed reliance are uninspected; criticism-driven iteration is uninspected. Addressability is fact UUID/text plus separate prompt/configuration, without guaranteed source-message-level rationale. Ordinary retained-text recurrence is wired, but learning through criticism is uninspected. These findings do not infer inaccessible model reasoning from its output.

### RTE-6 — Explicit authoring, revision and withdrawal

Route; implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/main.py`. A caller can bypass inference, retain non-system message content directly, explicitly update an existing UUID, or delete it. Update reads the old value, preserves scope identity against metadata changes, rewrites embeddings/text and logs previous/new text; changed text triggers entity-link cleanup/re-extraction. Delete removes the current vector record and logs its old text with deletion status, then cleans entity links. This supports manual write agency, evolve and invalidate. Neither operation performs an independent truth check or requires a retained rationale. Expiration hides records from ordinary search/get_all unless requested otherwise; it does not physically erase history. No automatic contradiction repair should be inferred from these explicit APIs.

> per_msg_meta = deepcopy(metadata)
>                 per_msg_meta["role"] = message_dict["role"]
> 
>                 actor_name = message_dict.get("name")
>                 if actor_name:
>                     per_msg_meta["actor_id"] = actor_name
> 
>                 msg_content = message_dict["content"]
>                 msg_embeddings = self.embedding_model.embed(msg_content, "add")
>                 mem_id = self._create_memory(msg_content, {msg_content: msg_embeddings}, per_msg_meta)
> --- `mem0/memory/main.py:896-905` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> self.vector_store.update(
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
> --- `mem0/memory/main.py:2087-2103` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> self.vector_store.delete(vector_id=memory_id)
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
> --- `mem0/memory/main.py:2125-2136` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> for mem in semantic_results:
>             payload = mem.payload if hasattr(mem, 'payload') else {}
>             if not show_expired and _payload_is_expired(payload):
>                 continue
> --- `mem0/memory/main.py:1682-1685` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Guidance and roles: caller-provided content determines the replacement; the caller proposes, decides and can withhold it, while validation/backend operations can reject. Its reason and standards of criticism are uninspected. Retained old/new text enables later inspection but does not reconstruct a criticism by itself. Rollback is another explicit update using available history, not an atomic reversal across vector/history/entity stores. Theory-builder conditions 1–4: localized text is wired; later consumption paths are wired/afforded as separately recorded; content-directed criticism and criticism-led iteration remain uninspected. Learning attribution is uninspected.

### RTE-7 — OSS caller search and entity-assisted ranking

Route; API capability conclusion status: wired. End-agent consumption conclusion status: afforded. Evidence: SRC-1 `mem0/memory/main.py`. The caller supplies query and identity filters; search embeds the query, overfetches max(top_k*4,60), obtains optional keyword results, computes BM25/entity boosts, removes expired candidates by default, and ranks to the requested limit (default 20). Entity matching considers at most eight extracted query entities, searches each entity store up to 500 matches and consumes linked IDs. Optional reranking is configured separately. Return is structured readable fact text plus metadata and score. This API alone does not identify an external consuming agent; therefore the profile's pull witness is the explicit coding-agent tool in RTE-10, not a hypothetical caller of this method. Lexical scoring here is not counted as lexical push.

> # Step 8: Score and rank
>         scored_results = score_and_rank(
>             semantic_results=candidates,
>             bm25_scores=bm25_scores,
>             entity_boosts=entity_boosts,
>             threshold=threshold,
>             top_k=limit,
>             explain=explain,
>         )
> --- `mem0/memory/main.py:1693-1701` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### RTE-8 — Hook evidence to staged hosted memory

Route; client orchestration conclusion status: wired. Hosted transformation conclusion status: afforded. Evidence: SRC-1 `integrations/agent-plugin-core/python/memory_core.py`, `integrations/agent-plugin-core/python/hook_runner.py`. User prompts, assistant stops and tool results become local events. Stop can schedule periodic or idle work; flush supports session-end and explicit reasons. `prepare_flush` reuses pending packets, bounds attempts (five), or selects unflushed events. A durable handoff starts a detached worker; extraction is batched at an estimated 24,000 input tokens, preserving exchanges when possible and splitting oversized messages. Returned event IDs are stored before polling; retries resume stored jobs. The client waits for server success/failure rather than treating accepted submission as completed extraction.

`build_episode` constructs broad diagnostic material, but the flush discards its rendered episode string and sends selected user/assistant messages plus changed paths/conditional command evidence. Subagent-stop events are not directly appended in its extraction-message loop; host transcript messages may already contain supporting material. Raw trace capture therefore must not be equated with every trace being learned. Test/build evidence remains mainly local diagnostics. The output contract asks for concise repository facts for future work and personal preferences; later first-prompt/MCP routes consume service text. This supports an afforded per-project/cross-task learning chain and staged timing, with local wiring and opaque hosted transformation kept separate.

> evidence = build_semantic_evidence(structured)
>     messages = [
>         {"role": message["role"], "content": redact(message["content"]).strip()}
>         for message in structured.get("extraction_messages", [])
>         if message.get("role") in {"user", "assistant"} and message.get("content")
>     ]
>     if evidence:
>         for message in reversed(messages):
>             if message["role"] == "assistant":
>                 message["content"] = f"{message['content']}\n\n{evidence}"
>                 break
>         else:
>             messages.append({"role": "assistant", "content": evidence})
> 
>     return messages
> --- `integrations/agent-plugin-core/python/memory_core.py:1690-1704` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> "source": _PLATFORM_SOURCE,
>         "metadata": {**metadata, "author": write_user, "dirs": directory_chain(repo)},
>         "agent_custom_instructions": PROJECT_MEMORY_INSTRUCTIONS,
>         "custom_instructions": PERSONAL_MEMORY_INSTRUCTIONS,
>         "custom_categories": CODING_MEMORY_CATEGORIES,
>         "infer": True,
>     }
> --- `integrations/agent-plugin-core/python/memory_core.py:2015-2021` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> def _wait_for_event(api_url: str, key: str, event_id: str) -> tuple[str, int, int]:
>     """Wait for extraction to finish before a later task can search the store."""
> --- `integrations/agent-plugin-core/python/memory_core.py:1904-1905` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> PROJECT_MEMORY_INSTRUCTIONS = """Save concise repository facts that will help with future coding work.
> 
> A completed change should produce one memory explaining the resulting behavior, where it is implemented when useful, and any important constraints or reasoning. Exploration or accepted decisions may produce separate memories only when they are independently useful.
> 
> Use the coding agent's final response for conclusions about current repository behavior. Do not save proposed or recommended changes unless the user accepted them or the coding agent completed them. Treat subagent responses as supporting repository evidence, not as decisions.
> 
> Write about the repository, not the user, assistant, session, or task. Do not include test results, documentation updates, release notes, or temporary state.
> 
> If nothing useful was established, return no memories."""
> --- `integrations/agent-plugin-core/python/memory_core.py:74-82` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

The project prompt explicitly requests important constraints or reasoning and treats the coding agent's final answer as its conclusion source; proposed changes require acceptance/completion. That is a model instruction, not independent verification. Any rationale surviving into hosted memory text is read with that text on recall; source IDs and rationale preservation are not enforced by the client. The remember skill is a manual request followed by automatic extraction, not a distinct direct-write implementation. Pause/resume and scoped forgetting are user controls; they are not evidence of truth-based curation.


Guidance and roles: shipped project/personal memory instructions guide an opaque hosted proposer; caller/host events trigger batching, the backend decides extracted content, and transport checks accept only completed jobs. Local pause/forget/manual controls let a user withhold future capture or withdraw material. The content can include constraints/reasoning, but no source-linked criticism record is required. Theory-builder conditions 1–4: localized source instructions are wired; hosted consumption of them is afforded by the request contract; formulated criticism and its result are uninspected; criticism-led iteration is uninspected. Project/cross-task recurrence is afforded, while actual learning attribution remains uninspected.

### RTE-9 — First-prompt automatic coding-agent supply

Route; implementation conclusion status: wired. Host activation conclusion status: uninspected. Evidence: SRC-1 `integrations/agent-plugin-core/python/hook_runner.py`, `integrations/agent-plugin-core/python/memory_core.py`. On the first qualifying prompt (default minimum 20 characters), the hook queries using at most 6,000 prompt characters, asks for five memories with a two-second request timeout, and emits `UserPromptSubmit` additionalContext. Filters select personal/shared memory in the repository, optionally directory scope. Search excludes task_episode records and already-seen IDs for tracked sessions. Format defaults to 4,000 characters, bounded configuration 1,000–10,000; it may truncate the first entry. It labels non-main branches but does not use that label as proof that content is valid on the current branch. Consumer: the coding agent receiving host hook context. Authority: advisory knowledge, not enforcement. Delivery wiring is not observed host activation or benefit.

> result = search_memories(
>         store, repo, session_id, bounded(prompt, 6000),
>         top_k=5, operation="first-prompt-search", timeout=2,
>     )
>     if not result.memories:
>         return {}
>     context = format_context(
>         result.memories,
>         "Mem0 found these relevant memories from earlier work in this repository:",
>     )
>     telemetry.record(
>         "context_injected",
>         repo=repo, session_id=session_id, trigger="first-prompt",
>         memory_count=len(result.memories), context_chars=len(context),
>         prompt_chars=len(prompt),
>     )
>     return {
>         "hookSpecificOutput": {
>             "hookEventName": "UserPromptSubmit",
>             "additionalContext": context,
>         },
> --- `integrations/agent-plugin-core/python/hook_runner.py:73-93` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> def _search_filters(user: str, repo: RepoContext, scope: str) -> dict[str, Any]:
>     """Build the scope filter: app_id scopes to the repo, then union shared and personal lanes."""
>     app_scope = {"app_id": repo.app_id}
>     mine = {"AND": [{"user_id": user}, app_scope]}
>     if scope == "mine":
>         return mine
>     projects = [{"AND": [{"agent_id": project_id}, app_scope]} for project_id in _shared_project_ids(repo)]
>     shared: dict[str, Any] = projects[0] if len(projects) == 1 else {"OR": projects}
>     if scope == "dir" and repo.directory:
>         shared = {"AND": [shared, {"metadata": {"dirs": {"contains": repo.directory}}}]}
>     return {"OR": [shared, mine]}
> --- `integrations/agent-plugin-core/python/memory_core.py:251-261` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### RTE-10 — Explicit coding-agent MCP recall

Route; implementation conclusion status: wired. Agent activation conclusion status: uninspected. Evidence: SRC-1 `integrations/agent-plugin-core/python/mcp_server.py`, `integrations/agent-plugin-core/python/memory_core.py`. The declared tool tells a coding agent to search earlier work when earlier decisions, fixes, commands or results can help. Agent requests query, top_k, category, scope and optional run ID; the handler validates and calls hosted search, returning formatted text. This is pull because the consumer asks for memories. Default top_k is three, permitted 1–20. No tracked session is passed by this handler, so the hook's already-shown suppression does not apply. Its scope descriptions explicitly permit cross-session earlier-work recall. Content formatting still bounds output. Hosting and invocation by a deployed agent were not tested.

> def call_search_memories(arguments: Any, cwd: str | None = None) -> str:
>     query, top_k, category, scope, run_id = _validate_arguments(arguments)
>     repo = resolve_repo(cwd or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())
>     result = search_memories(
>         None,
>         repo,
>         None,
>         query,
>         top_k=top_k,
>         category=category,
>         scope=scope,
>         run_id=run_id,
>         operation="mcp-search",
>     )
>     return format_search_result(result)
> --- `integrations/agent-plugin-core/python/mcp_server.py:115-129` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### RTE-11 — Procedural continuation and subagent context alternatives

Route family; generation/helper implementation conclusion status: wired. Later consumer integration conclusion status: afforded. Evidence: SRC-1 `mem0/memory/main.py`, `mem0/configs/prompts.py`, `integrations/agent-plugin-core/python/memory_core.py`. Procedural mode asks an LLM to summarize execution history for an agent continuing a task, then persists the natural-language result under agent identity. The default prompt calls for every output verbatim, a demand rather than a checked property; the implementation rejects only empty output before embedding/persistence. Async supports either the configured generator or a supplied LangChain LLM. Creation does not itself assemble a continuation context. Generic retrieval and next-extraction access are available, but a dedicated consumer reading the summary to resume a task was not inspected. The named continuation consumer and generic retrieval interface establish an afforded per-task learning route. They do not establish host wiring or impose a per-task retention boundary on the general store. The horizon comes from the prompt's explicit continuation objective, not the procedural label or run ID.

Separately, `record_subagent_start` selects cached retrievals by session/repository, formats them and returns context only on first start. This affords identifier-targeted reuse for a native subagent; this report did not inspect the specific host adapter that delivers this returned string. Cached text can differ from the main agent's actual truncated context. The helper adds no new learning or guarantee of subagent uptake.

> PROCEDURAL_MEMORY_SYSTEM_PROMPT = """
> You are a memory summarization system that records and preserves the complete interaction history between a human and an AI agent. You are provided with the agent’s execution history over the past N steps. Your task is to produce a comprehensive summary of the agent's output history that contains every detail necessary for the agent to continue the task without ambiguity. **Every output produced by the agent must be recorded verbatim as part of the summary.**
> --- `mem0/configs/prompts.py:326-327` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> """Record a native subagent and reuse the main turn's retrieved memories."""
>     session_id = _session_id(hook_input)
>     repo = store.repo_for_session(session_id, hook_input.get("cwd"))
>     agent_id = bounded(hook_input.get("agent_id", "unknown-agent"), 200)
>     agent_type = bounded(hook_input.get("agent_type", "unknown-agent"), 200)
>     context = combine_context(
>         format_context(store.injected_memories(session_id, repo.identity))
>     )
>     first_start = store.start_subagent(
>         repo, session_id, agent_id, agent_type, len(context)
> --- `integrations/agent-plugin-core/python/memory_core.py:1388-1397` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Guidance and roles for procedural generation: the shipped preservation prompt or caller prompt directs the LLM; nonempty-output and metadata checks can reject before persistence. The retained summary may contain plans, errors or rationale, but the summarizer does not require a formulated criticism or evaluate resulting improvement. Theory-builder conditions 1–4: localized guidance/summary is wired; generator consumption is wired and continuation consumption afforded; content-directed criticism and resulting revision are uninspected; criticism-led iteration is uninspected. Summary persistence is durable across calls under configured scope, while the named intended use is continuation of one task. Its task horizon and lifetime are different findings. The subagent helper copies prior context and proposes no new memory revision; criticism and learning are inapplicable to that copying step itself.

### RTE-12 — Proxy completion injection attempt with incompatible calls

Route; implementation conclusion status: afforded. Successful recall conclusion status: uninspected. Evidence: SRC-1 `mem0/proxy/main.py`, `mem0/memory/main.py`, `mem0/client/main.py`. The proxy intends to asynchronously add messages and retrieve memories from the last six messages before calling LiteLLM. However it passes `filters` into Python `Memory.add`, whose inspected signature does not accept it, and passes top-level user/agent/run IDs into search. Both pinned Memory and MemoryClient search reject those top-level identity arguments. This static incompatibility prevents using the attempted proxy path as a functioning automatic-supply witness; no execution was run to measure failure. Hosted response formatting may also differ, but that separate issue was not needed for the conclusion.

> def _fetch_relevant_memories(self, messages, user_id, agent_id, run_id, filters, top_k):
>         # Currently, only pass the last 6 messages to the search API to prevent long query
>         message_input = [f"{message['role']}: {message['content']}" for message in messages][-6:]
>         # TODO: Make it better by summarizing the past conversation
>         return self.mem0_client.search(
>             query="\n".join(message_input),
>             user_id=user_id,
>             agent_id=agent_id,
>             run_id=run_id,
>             filters=filters,
>             top_k=top_k,
>         )
> --- `mem0/proxy/main.py:163-174` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> if reference_date is not None:
>             raise ValueError(get_temporal_feature_error_message("sync", "search", "reference_date"))
> 
>         # Reject top-level entity params - must use filters instead
>         _reject_top_level_entity_params(kwargs, "search")
> 
>         # Validate search parameters (before applying defaults)
>         _validate_search_params(threshold=threshold, top_k=top_k)
> --- `mem0/memory/main.py:1446-1453` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### Claims

### CLM-1 — Managed benchmark and learning claims

Claim conclusion status: claimed. README describes a memory layer that remembers preferences and continuously learns, and reports improved managed-platform benchmark scores. The inspected OSS code supports retained extraction and retrieval mechanisms, not reproduction or causal attribution of those benchmark differences. Its own prose explicitly limits those numbers to the proprietary platform. No benchmark output or external evaluation repository was admitted to this source boundary. Evidence: SRC-1 `README.md`.

> Scores reflect Mem0's managed platform, which includes proprietary optimizations not available in the open-source SDK; open-source users should expect directionally similar gains but not identical numbers.
> --- `README.md:54-54` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CLM-3 — Extraction failure and persistence distinctions

Implementation conclusion status: wired. Provider failure is raised, while parse failure can become empty extraction. Batch insertion falls back to individual writes, and a complete insertion failure raises a store error after saving messages. Successful insertion is distinct from successful history/entity maintenance. This record supports runtime forcing cases without claiming observed failures. Evidence: SRC-1 `mem0/memory/main.py`.

> logger.error(f"LLM extraction failed: {e}")
>             raise LLMError(f"LLM extraction failed: {e}") from e
> --- `mem0/memory/main.py:970-971` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> except Exception as e:
>             logger.error(f"Error parsing extraction response: {e}")
>             extracted_memories = []
> --- `mem0/memory/main.py:984-986` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> if not persisted_records:
>             self.db.save_messages(messages, session_scope)
>             raise VectorStoreError(
>                 f"Failed to insert any of the {len(records)} extracted memories into the vector store"
>             )
> --- `mem0/memory/main.py:1072-1076` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CLM-2 — Extraction and summary guidance

Claim conclusion status: claimed. The additive prompt asks for new-message extraction with old memory used for deduplication/linking. The procedural prompt asks for preservation of execution history and verbatim outputs. These are guidance, not enforced semantic guarantees; the resulting text can be checked only with a candidate and its source. Evidence: SRC-1 `mem0/configs/prompts.py`.

> Use these ONLY for deduplication and linking — do NOT extract new memories from Existing Memories. Your extractions must come exclusively from New Messages.
> --- `mem0/configs/prompts.py:511-511` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

The procedural preservation wording is quoted on RTE-11.

### CLM-4 — Coverage and outcome limits

Claim; conclusion status: uninspected. Evidence: SRC-1 `mem0/client/main.py`, `integrations/agent-plugin-core/python/memory_core.py`. Hosted internals and TypeScript/other adapters are included alternatives whose mechanisms were not established. Code inspection establishes possible execution, not retained observed or causal outcomes. No recalled-content dependence experiment was inspected, and operation/retrieval counters are insufficient for that question. Therefore faithfulness_tested is uninspected, not no. This record prevents complete profile coverage and prevents promoting any wired route to observed benefit.

### Evidenced absences

The absence below is confined to its recorded source search; opacity remains a limitation.

### ABS-1 — No dedicated graph route in the inspected Python engine

Evidenced absence; conclusion status: absent. Evidence: SRC-1 `mem0/configs/base.py`, `mem0/memory/main.py`, `mem0/utils/factory.py`. Pinned-tree inspection and case-insensitive graph search in those three files found no graph configuration or invocation. Memory initializes vector storage, LLM, embeddings, SQLite history and optional reranker; its entity store is another vector collection. This is a bounded Python-engine absence, not absence of graphs in hosted services, TypeScript alternatives or all provider internals. It prevents importing a historical graph-memory characterization into this Python pin.

> class MemoryConfig(BaseModel):
>     vector_store: VectorStoreConfig = Field(
>         description="Configuration for the vector store",
>         default_factory=VectorStoreConfig,
>     )
>     llm: LlmConfig = Field(
>         description="Configuration for the language model",
>         default_factory=LlmConfig,
>     )
>     embedder: EmbedderConfig = Field(
>         description="Configuration for the embedding model",
>         default_factory=EmbedderConfig,
>     )
>     history_db_path: str = Field(
>         description="Path to the history database",
>         default=os.path.join(mem0_dir, "history.db"),
>     )
> --- `mem0/configs/base.py:29-45` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### Behavioral-authority paths

### BAP-1 — Server configuration authority

Implementation conclusion status: wired. Consumer: Memory constructor and subsequent request methods; channel: merged configuration and configured prompt; force: provider routing and extraction instruction; horizon: current instance and persisted overrides across restarts when persistence succeeds. Evidence: SRC-1 `server/server_state.py`, `mem0/configs/base.py`; see RTE-2.

### BAP-2 — HTTP admission authority

Implementation conclusion status: wired. Consumer: request handlers; channel: authentication/admin dependencies; force: permits or blocks operation; horizon: request. It is operational authorization, not epistemic warrant for returned memories. Evidence: SRC-1 `server/auth.py`, `server/main.py`; see RTE-1.

### BAP-3 — Retained references into extraction

Implementation conclusion status: wired. Consumer: CMP-1; channel: new extraction user prompt containing selected facts/history; force: advisory knowledge under extraction instructions; horizon: later add invocations within supplied identity scope. See RTE-5 and SRC-1 `mem0/memory/main.py`. Delivery is not observed activation.

### BAP-4 — Entity links into ranking

Implementation conclusion status: wired. Consumer: search scorer; channel: retained entity-to-memory IDs and computed boosts; force: ranking; horizon: future search until links change/delete. See OBJ-4, RTE-7 and SRC-1 `mem0/memory/main.py`.

### BAP-5 — Hook memory into coding-agent context

Implementation conclusion status: wired. Consumer: host coding agent; channel: UserPromptSubmit additionalContext; force: advisory knowledge; horizon: the host invocation, with cache available for same-session helper reuse. See RTE-9 and SRC-1 `integrations/agent-plugin-core/python/hook_runner.py`. Host activation and subagent adapter delivery remain uninspected.

### BAP-6 — Requested MCP recall

Implementation conclusion status: wired. Consumer: calling coding agent; channel: tool text result; force: advisory knowledge; horizon: requesting invocation. See RTE-10 and SRC-1 `integrations/agent-plugin-core/python/mcp_server.py`. The consumer chooses whether to use it.

## Runtime account

Ordinary operation is request-bounded. A caller chooses identity scope and calls add; extraction receives conversation text, previous messages and retrieved existing memories, invokes a configured LLM once, embeds accepted output texts and inserts new records. Subsequent search retrieves a bounded result set, optionally reranks it and returns it. A host integration may supply those results automatically to an external agent. Mem0 controls its selection, persistence and transport; the external agent controls task continuation and final tool effects. The stored summary is not itself an enclosing runtime checkpoint.

Static forcing cases selected:

1. Extraction failure versus empty extraction: provider failure raises LLMError for caller fallback, while response parsing can produce an empty extracted set and still save messages. Empty result therefore does not uniformly establish that no relevant fact existed. The library, not an enclosing agent scheduler, owns these return choices. Evidence: SRC-1 `mem0/memory/main.py`.
2. Partial persistence: batch vector insertion falls back to per-record insertion; only acknowledged inserts enter returned ADD results. History/entity failures may be logged after memory persistence. This is best effort across stores, not an atomic all-or-nothing guarantee; backend insert semantics remain an external contract. Evidence: SRC-1 `mem0/memory/main.py`.
3. HTTP alternate authority: direct Python bypasses server authentication; AUTH_DISABLED bypasses authentication on the server; read-by-ID does not derive a memory scope from the authenticated user. See RTE-1. No deployed tenant-isolation conclusion is made.
4. Configuration failure: RTE-2 assigns the configuration dictionary before successful construction and suppresses persistence failure. The returned settings and effective instance can diverge on failure. A retry/rollback policy outside that function is uninspected.

No dynamic check planned. A live add/search probe, provider-failure injection and configuration reconstruction test were considered. Static branch inspection suffices for the wired claims made here; provider/service credentials and deployed backend behavior are outside this frozen source analysis. No successful operation, activation or measured benefit is inferred from unexecuted test code.

The capability surface includes library providers and manual CRUD, hosted client requests, HTTP service administration and host hooks/tools. The current grant set is a deployment choice; no configured credential values, host approval rules or running isolation envelope were inspected. Registered provider classes run inside the application process. Persistence and remote calls require backend/provider contracts. The bundled server allowlist restricts its configuration path without restricting all direct-library extension paths.

Decision roles: callers provide messages, identifiers, instruction overrides and manual edits; extraction models propose facts or summaries; code checks formatting, available embeddings and storage outcomes; stored context and model instructions shape selection. These are not independent expected answers. Humans may revise/delete memory or configure providers, but their diagnosis and justification are outside the request implementation. Open requests are the inspected operating mode. Published benchmark claims concern a separate managed-platform comparison, not an inspected curriculum or online improvement controller.



The memory-route audit distinguishes persistence and delivery from activation:

| Route | Immediate result and later consumer | Selection, withdrawal and delegated visibility | Recovery/evidence limit |
|---|---|---|---|
| RTE-5 | ADD result; facts/history later enter extractor | Identity plus embedding; explicit edit/delete, rolling raw-history eviction; no task delegation in library | Provider errors raised; parse/embedding/store partial outcomes; no observed activation |
| RTE-6 | Explicit mutation result; later search/extraction sees current text, history callers see old text | UUID/caller scope; delete/expiry alter reliance; no separate delegated visibility | Multi-store recovery not atomic; caller may revise again |
| RTE-7 | Ranked result; external consuming agent only afforded | Query, scope, threshold, expiry, top-k, optional reranker; caller controls propagation | Fallback from reranker; no end-agent use observed |
| RTE-8 | Submission/job completion; service memory later reaches hook/MCP | Selected event/messages, repo/user scope; pause/forget; raw subagent events not all included | Spool, event-ID polling, bounded retry; hosted extraction and successful learning opaque |
| RTE-9 | Hook context; coding agent receives selected prior work | First qualifying prompt, scope, five results and character budget; seen IDs; branch label advisory | Two-second request budget; cached full text may exceed delivery; no observed uptake |
| RTE-10 | Tool text; requesting coding agent | Explicit query/scope/run/top-k; no hook session suppression; returned material may be passed onward by caller | Hosted/interface errors remain possible; invocation not observed |
| RTE-11 | Summary ADD or subagent helper context | Procedural identity scope; generic edit/delete; helper session/repo match and first-start | Empty summary rejected; dedicated continuation and host subagent delivery uninspected |
| RTE-12 | Intended completion with memory; successful route unestablished | Intended last-six-message query with incompatible parameters | Static API mismatch blocks working-path inference; no execution trace |

No required runtime route has an unexplained empty return/read-back/delegation/selection/expiry/effect field. Actual activation is uninspected throughout; wired selection effects are separately identified on the records.

## Lens scoping

### Memory/context scope

Full depth; memory is the product's primary responsibility. The frozen specialist input names retained objects, derivation, selection and later consumers, with hosted internals and incompletely inspected SDK/adapters limiting coverage. Trigger: CLM-1, CLM-2 and memory API implementation in SRC-1. Canonical objects are OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7; routes are RTE-5, RTE-6, RTE-7, RTE-8, RTE-9, RTE-10, RTE-11, RTE-12.

### Epistemic scope

Full depth for extraction, procedural summaries, relevance selection and instruction proposals: these create or admit truth-apt content and change later reliance. Trigger: CLM-1, CLM-2, OBJ-2 and inspected SRC-1 prompts/implementation. Classify-only routes are HTTP authorization, configuration and provider registration, RTE-1, RTE-2, RTE-4: operational authority does not grant truth. Hosted reasoning, other adapter differences and actual candidate trajectories remain uninspected; no system-complete warrant conclusion follows.

## Lens outputs

### Memory/context lens

The specialist inventoried OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7 and RTE-5, RTE-6, RTE-7, RTE-8, RTE-9, RTE-10, RTE-11, RTE-12. Its source-native findings and generated quotations are integrated above. Conversation-derived facts feed later extraction; entity metadata affects ranking; the shared plugin stages traces for hosted extraction and returns selected memory through automatic first-prompt supply or explicit MCP search. Procedural summaries offer task continuation without a dedicated inspected continuation assembler. The incompatible proxy call shape is not counted as working push.

Partial coverage assessments are preserved. Content and access metadata jointly explain vector, SQLite, files and service-object storage. Entity-link merging supports dedup; explicit update/deletion supports evolve and invalidate; rolling raw-message eviction supplies decay. These narrow witnesses do not imply semantic fact consolidation. Natural-language and symbolic forms describe facts and derived access structures, not learned model parameters.

Qualifying learning routes are RTE-5 (conversation facts and downstream entity derivation), RTE-8 (staged hosted extraction, afforded because transformation is opaque), and the procedural subpath of RTE-11 (continuation, afforded because later consumption is not wired). Online/staged timing, session-log/event/tool/trajectory sources and project/cross-task/per-task horizons retain separate bases. Generic identity scopes alone supply no task horizon. Push has actual selectors: RTE-5 selects history by identity and facts by embedding; RTE-9 selects repository/personal lanes by identity, with hosted matching opaque. The subagent helper in RTE-11 copies selected cached context without an additional learning claim. RTE-10 is requested recall, so it supplies pull.

No observed faithful use or benefit was supplied. The faithfulness field is uninspected. Opaque hosted and adapter alternatives prevent complete aggregate value sets. Raw subagent events and counters are not treated as learning or activation evidence.

### Epistemic lens

#### 1. Source-and-claim boundary

System/revision/boundary: see SRC-1 and Boundary and evidence. Question: what licenses reliance on newly extracted facts, summaries, retrieved material and proposed instructions? Assessed families are RTE-3, RTE-5, RTE-6, RTE-7, RTE-8, RTE-9, RTE-10, RTE-11 and their operational guards. Hosted admission internals, TypeScript/other adapters and observed candidate trajectories are unassessed. Their omission prevents system-complete warrant claims. CLM-1 reports managed benchmark/learning claims; CLM-2 supplies extraction/preservation doctrine. Implementation is not observed operation.

#### 2. Epistemic-object overlay

| Object/part | Candidate content and claimed role | Warrant/lineage limit |
|---|---|---|
| See OBJ-1 | Provider settings and extraction priorities are operational configuration | No factual success conclusion follows from configuration admission |
| See OBJ-2 | Proposal about which facts matter for a use case; synthetic test sentence | LLM proposal, not independently tested guidance or expected-answer oracle |
| See OBJ-3, fact part | Statements about users, assistant recommendations, plans and events | Trace extraction may preserve, interpret or add meaning; no candidate pairs to decide entailment |
| See OBJ-3, procedural part | Claimed account of execution history for continuation | Preservation demanded by prompt, not checked by the nonempty-output guard |
| See OBJ-4 | Entity identity/type and links to relevant memories | Similarity merges are operational access decisions; identity correctness is not certified |
| See OBJ-5 | Raw messages and old/new mutation text | Import preserves records available to the writer; history does not establish source truth or rationale |
| See OBJ-6 | Local events, selected packet, cached retrieved texts and spool | Deterministic selection/transport, with known pre-truncation cache versus delivered-context distinction |
| See OBJ-7 | Returned hosted facts and submitted feedback | Backend transformation and use of feedback reasons uninspected |

#### 3. Authority-route ledger

All rows below have observed candidate state: no instance observed. Architectural status is separate from conclusion status. Generic owners, endpoints and evidence are on the referenced canonical record. Each row states one function; linked rows keep production, checking, disposition and retention separate.

| Route | Function | Architectural status | Target/content relation | Evaluator and timing | Operational force and epistemic license |
|---|---|---|---|---|---|
| RTE-3 | content transformation | implemented | OBJ-2; non-truth-apt instruction proposal plus indeterminate example sentence | CMP-1 at request under format/use-case guidance | Returns proposal; no installation or factual warrant |
| RTE-5 | content transformation | implemented | OBJ-3 facts; indeterminate truth-apt extraction | CMP-1 with new messages and retained references during add | Proposes new facts; preservation, derivation and conjecture remain possible |
| RTE-5 | check/evidence production | implemented | OBJ-3; no content change | Parsing, text/embedding availability and hash comparison | Checks admissible format/duplicates, not truth or entailment |
| RTE-5 | disposition/acceptance | implemented | OBJ-3; no content change | Model omission and code skip rules before insert | Operational ADD admission; no independent epistemic acceptance criterion |
| RTE-5 | retention | implemented | OBJ-3, OBJ-4, OBJ-5; new records/access structures | Store acknowledgments, history/entity follow-up | Retains admitted texts; storage does not endorse them |
| RTE-5 | operational admission/selection/consumption | implemented | OBJ-3, OBJ-5; no content change | Automatic identity/history and embedding selection before extraction | Advisory evidence to extractor; no observed activation |
| RTE-6 | content transformation | implemented | OBJ-3; acquisition/import or caller text replacement | Caller chooses supplied text or deletion | Alters current reliance without requiring criticism/rationale |
| RTE-6 | retention | implemented | OBJ-3, OBJ-5; no additional content change | Vector update/delete and history writer | Current material changes, history persists; no truth license |
| RTE-7 | operational admission/selection/consumption | implemented | OBJ-3, OBJ-4; no content change | Scope/expiry, relevance fusion and optional reranker | Changes ranking/returned set; relevance is not truth |
| RTE-8 | content transformation | implemented | OBJ-6 packet; non-ampliative selection/formatting | Host event selection, redaction and batching before submission | Transports selected evidence, not every captured event |
| RTE-8 | content transformation | not determinable | OBJ-7; indeterminate hosted extraction | Hosted model/process after submission | API affords derived memory; actual epistemic checks opaque |
| RTE-8 | lineage/freshness/recovery | implemented | OBJ-6, OBJ-7; no content change | Persisted job IDs and success/failure polling | Resumes delivery; completed job does not establish correct facts |
| RTE-9 | operational admission/selection/consumption | implemented | OBJ-7 to OBJ-6; no content change | First prompt, repository/personal scope and bounded formatting | Advisory host additionalContext; no verified answer authority |
| RTE-10 | operational admission/selection/consumption | implemented | OBJ-7; no content change | Coding agent's explicit query/scope/tool request | Requested text response; no observed uptake |
| RTE-11, procedural part | content transformation | implemented | OBJ-3 summary; indeterminate truth-apt reshaping | CMP-1 or async alternate generator under preservation prompt | Nonempty summary stored; no faithfulness check |
| RTE-11, subagent part | operational admission/selection/consumption | implemented | OBJ-6; no content change | Session/repository cache match, first-start predicate | Helper returns selected context; actual adapter delivery uninspected |
| RTE-12 | operational admission/selection/consumption | not determinable | OBJ-3 or OBJ-7; no intended content change | Proxy calls conflict with current API | Intended recall cannot support working delivery conclusion |

Classify-only authority: RTE-1 authenticates requests, RTE-2 admits caller configuration, RTE-4 resolves provider code. They change permitted operations or machinery, not epistemic warrant. No answer oracle is evidenced in these routes. Project extraction instructions in RTE-8 prefer completed/accepted changes and the coding agent's final response; that gives a source-selection policy, not an independent test of repository truth.

#### 4. Per-object lifecycle dispositions

For OBJ-3 facts and summaries, transformation is indeterminate: acquisition/reshaping, entailment or ampliative interpretation cannot be distinguished without actual source/output pairs. Checks and retention are implemented on RTE-5 and RTE-11, but no observed instance establishes semantic preservation or accepted conjecture. A similarity/hash check cannot settle it. No discovery-lifecycle phase is inferred from the ADD label. Current warrant is extracted or summarized source testimony, not verified content.

For OBJ-4, entity extraction/link merging produces access metadata with indeterminate identity assertions; its ranking consumption is implemented on RTE-7, but entity correctness lacks candidate-linked validation. For OBJ-5 and the raw/packet/cache parts of OBJ-6, acquisition and non-ampliative selection preserve recorded inputs to the degree shown, with no claim of source truth. Discovery lifecycle is not applicable to those transport transformations. The cache/delivery mismatch prevents treating a retrieval row as evidence of complete contextual presence.

For OBJ-7, hosted derivation is indeterminate; candidates, acceptance criteria and downstream feedback use are unavailable. No phase is observed. For OBJ-2, instructions are operational proposals rather than established truth-apt theories; the example sentence's correspondence to a real use case is indeterminate. No lifecycle record for OBJ-1: no candidate truth-apt output for this configuration object; relevant update route RTE-2. No ampliative lifecycle instance has been established, so none is labeled accepted, rejected, integrated or improved.

#### 5. System-claim versus route comparison

| Claim | Route support | Observed/causal support | Supported conclusion and unresolved gap |
|---|---|---|---|
| CLM-1 | RTE-5, RTE-7, RTE-8, RTE-9, RTE-10 retain and retrieve memory | None inspected | Memory wiring is supported; managed benchmark values and criticism-attributable learning are not established here |
| CLM-2 | RTE-5, RTE-11 implement prompt-driven generation | No source/output candidate pairs | Extraction/preservation are requested, not guaranteed |
| CLM-3 | RTE-5 implements differentiated failure handling | No executed failure trace | Static possible outcomes only; no failure frequency claim |
| CLM-4 | Hosted client/interface and partial alternative inspection | None inspected | Prevents complete profile, not the supported positive routes |

#### 6. Bounded conclusion

Mem0 grants operational reliance through extraction, persistence, ranking and context delivery. Within the inspected routes it neither verifies every recalled statement nor establishes that a generated instruction or procedural summary improved future action. Imported testimony can remain useful without becoming accepted ampliative knowledge. The epistemic effect of hosted feedback and model-internal reasoning remains uninspected. No single epistemic grade is assigned.


## Reconciliation

The fresh specialist report's run, source pin, complete status, frozen-input digest, method digest and final report digest were checked before integration. Its reported runtime model identity is unknown; it was commissioned with the gpt-6-astra override. No component proposal overlapped the coordinator's components. Every proposed record was adopted under the mapping below; no shared canonical ID was redefined.

MEM-OBJ-1 → OBJ-3; MEM-OBJ-2 → OBJ-4; MEM-OBJ-3 → OBJ-5; MEM-OBJ-4 → OBJ-6; MEM-OBJ-5 → OBJ-7; MEM-RTE-1 → RTE-5; MEM-RTE-2 → RTE-6; MEM-RTE-3 → RTE-7; MEM-RTE-4 → RTE-8; MEM-RTE-5 → RTE-9; MEM-RTE-6 → RTE-10; MEM-RTE-7 → RTE-11; MEM-RTE-8 → RTE-12; MEM-ABS-1 → ABS-1; MEM-CLM-1 → CLM-4.

Material dispositions: the input's graph request did not assert existence; ABS-1 retains the bounded negative. The additive implementation governs RTE-5 despite the stale add docstring. Prompt-requested fact links and persisted entity links remain different mechanisms on RTE-5 and OBJ-4. Manual remember requests do not change automatic extraction into manual direct writing. Procedural continuation and subagent context copying remain distinguishable subpaths on RTE-11, with separate evidence and no upgraded continuation claim. The proxy mismatch on RTE-12 is not a functioning recall witness. Cached pre-truncation text and retrieval counters on OBJ-6 do not establish model uptake. Hosted extraction and all unknown alternatives retain partial coverage.

Specialist quotations were copied unchanged to canonical records. The coordinator's shorter overlapping procedural-prompt quote was removed in favor of the specialist's complete quote on RTE-11; the report itself was not edited. No substantive disagreement requiring reanalysis remains. Shared observations of additive extraction are not claimed as independent lens convergence. The epistemic overlay interprets accepted records instead of drafting another memory analysis.

## Bounded synthesis

Mem0 separates memory acquisition and selection from the host's task loop. In the inspected OSS route, one extraction call proposes additional facts using current messages, recent history and existing memories. Structured access metadata, vectors, optional NLP entities and reranking determine which retained texts return later. Host integration can automate supply; manual API users retain responsibility for putting returned material into a consuming model's context. The additive implementation leaves changes and contradictions represented by additional material unless a caller uses explicit maintenance operations.

This division matters in two scenarios. As an application library, it supplies a configurable memory computation whose authorization and final context use belong to the application. As a self-hosted service, HTTP authentication and admin checks add admission controls, but caller-supplied memory identifiers remain distinct from authenticated account ownership. Its deployment recipe can install library bytes different from the inspected commit. As a host plugin, operation additionally depends on hook registration, backend delivery and the consuming host's semantics.

The strongest supported learning contribution is a wired route from conversation or execution traces into durable natural-language material used by later memory operations or afforded to a host. That satisfies the comparison's trace-learning criterion where specified; it does not establish improved capacity attributable to criticism. The source reports managed benchmark gains, but this analysis has neither managed implementation nor candidate-linked intervention evidence. Learning conclusion status: uninspected for that stronger attribution.

Theory-builder conditions 1–4 are assessed separately. Localized extraction guidance and memory text are wired; content consumption is wired for the extractor's supplied guidance and retained reference context, with actual activation unobserved. A working process of formulated criticism directed at a consumed theory, its blame assignment, resulting revision or changed reliance, and iteration of that criticism are uninspected. An additive duplicate decision, a relevance score or a caller edit cannot fill those links. Consequently theory-builder membership is uninspected within this boundary. Rule-level and memory-ID addressability are supported, but finer assumptions or justifications need not be independently retained.

Reflection conclusion status: uninspected for a two-way self-representation of the memory system's own methods. A configuration surface is wired; that alone does not establish reflective criticism, and configuration/state can diverge on construction failure. Autonomous theory-builder qualifier: uninspected because a complete criticism-and-iteration process is not established. Ordinary extraction and selection are computational, while caller-directed administration is external to those automatic steps. Self-improvement conclusion status: uninspected for an exercised, objective-relative improvement route; the wired standing memory-adaptation pathway supports later context without demonstrating improved subsequent behavior. Each statement concerns a different property, not a shared grade.

A pinned deployment plus candidate/source pairs, recorded context delivery and a controlled recall intervention would strengthen activation and benefit findings. Evidence of content-directed criticism whose result shapes later rounds would change the theory-builder account. Inspection of the managed backend and all SDK/host alternatives would reduce present coverage uncertainty; benchmark prose alone cannot do so.

Concept mappings use Commonplace's [theory builder](../../../../notes/definitions/theory-builder.md), [reflective system](../../../../notes/definitions/reflective-system.md) and [self-improving system](../../../../notes/definitions/self-improving-system.md) definitions. These definitions organize the assessment; the source-native routes remain the evidence.


## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Resolving evidence |
|---|---|---|---|---|
| Hosted backend opaque | SRC-1, CLM-1 | Repository interfaces and README | Managed extraction, isolation and benchmark causality | Pinned backend implementation and evaluation artifacts |
| No observed operation | SRC-1, CMP-1, CMP-2, CMP-3, CMP-4 | Static implementation | Actual context activation, success rates, latency and benefit | Candidate-linked traces and appropriately designed comparison |
| Alternative coverage partial | SRC-1 | Python and representative shared integration | Complete aggregate over TypeScript and every host adapter | Same-pin targeted alternative-route inspection |
| Provider identities mutable | CMP-1, CMP-2, CMP-3, CMP-4 | Adapter/configuration/loader | Exact weights or universal parameter fixity | Deployed model version/content attestations |
| Deployment differs from source pin | RTE-4 | Compose recipe | Running server necessarily uses pinned OSS code | Package lock/content digest and deployment evidence |
| Grants and isolation uninspected | RTE-1, BAP-2 | Admission dependency and endpoints | Tenant isolation or host approval envelope | Deployment configuration and end-to-end authorization tests |
| No criticism-linked iteration evidence | CLM-2, OBJ-2, RTE-3 | Prompts and transformation routes | Theory-builder membership or learning attribution | Formulated criticisms, dispositions and subsequent consumers |
| Configuration persistence best effort | OBJ-1, RTE-2 | Update and persistence functions | Atomic effective/durable reconfiguration | Changed implementation or demonstrated external recovery contract |


## Verification and blockers

### Semantic verification

Checked canonical identity and source anchors, all adopted specialist proposals and fourteen profile axes against the same frozen scope. Checked RTE-5, RTE-8 and procedural RTE-11 for trace source, timing, horizon and distilled form; entity derivation through OBJ-4/RTE-7 carries the symbolic form while generic OSS scope remains horizon-unknown. Raw log retention and subagent copying alone do not add learning. Checked automatic selectors on RTE-5 and RTE-9 for trigger, selector input and retained output; RTE-10 remains requested pull. Hosted selection and transformation are not inferred from API names. Known fields are not manufactured by dropping opaque alternatives: supported positive axes remain partial and faithfulness remains uninspected.

Checked authority, component identity/fixity limits, revision admission and recovery; no conditional HTTP guard is generalized to direct library use. Theory-builder conditions, activation and improvement remain distinct. Both lenses use canonical records and preserve their own evidence vocabulary. Every quote was generated from the pinned source; the report's longer procedural quote replaces one overlapping shorter passage. No specialist semantics were strengthened, and no independent convergence was claimed. No dynamic test is represented as executed.

### Deterministic validation

Target: `commonplace-validate --full kb/reports/state/agentic-system-analysis/AAS-2026-09-27-mem0-03/result.md`. Validation returned exit status 0 and PASS (clean), with no warnings or failures. It checked the schema, canonical references, all fourteen comparison axes and 49 well-formed quote anchors. The specialist report separately passed its structural check; neither check independently clears the integrated semantics.

### Blockers

None.

---
{
  "type": "agentic-system-analyses/types/agentic-system-memory-profile.md",
  "description": "post-graph-rag memory comparison: PostgreSQL passage/graph/vector retention, community reports, exposure-fed access state and shipped evaluation consumers.",
  "run-id": "AAS-2026-11-08-post-graph-rag-448d75e4222d-01",
  "source-identity": "https://github.com/crajah/post-graph-rag",
  "reviewed-boundary": "bce4146a7dc4684e9b66806915c29b0eed57ba23",
  "memory-comparison": {
    "version": 2,
    "scope": "Retained passages, extracted entity/relation prose and symbolic identity/provenance/lifecycle state, stored embeddings, community reports and membership/rating metadata, retrieval events and exposure-derived archive flags; their ingestion, direct-store, custom-extractor, maintenance, query, reporting, inspection, polling and shipped evaluation/replay routes. Includes unresolved extra retention/provenance and later consumption in injected implementations and unassessed evaluator alternatives. Excludes static shipped prompts/configuration, ordinary current-request/history state without an established retained route, transient answer/contradiction objects, provider model training/weights and external dependency internals; persisted evaluation outputs remain included without presumed automatic adoption.",
    "axes": {
      "storage_substrate": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Engine-retained passages, entity/relation parts, community parts and retrieval events",
            "assessment": "known",
            "findings": [
              {
                "value": "rdbms",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-documents",
                  "memory.md#mem-obj-entity-metadata",
                  "memory.md#mem-obj-relation-metadata",
                  "memory.md#mem-obj-community-text",
                  "memory.md#mem-obj-retrieval-events"
                ],
                "note": "PostgreSQL vertices/edges and their payloads retain these operative parts."
              },
              {
                "value": "graph",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-documents",
                  "memory.md#mem-obj-entity-metadata",
                  "memory.md#mem-obj-relation-metadata",
                  "memory.md#mem-obj-community-text",
                  "memory.md#mem-obj-retrieval-events"
                ],
                "note": "PostgreSQL vertices/edges and their payloads retain these operative parts."
              }
            ],
            "records": [
              "memory.md#mem-obj-documents",
              "memory.md#mem-obj-entities",
              "memory.md#mem-obj-entity-metadata",
              "memory.md#mem-obj-relations",
              "memory.md#mem-obj-relation-metadata",
              "memory.md#mem-obj-community-text",
              "memory.md#mem-obj-community-metadata",
              "memory.md#mem-obj-retrieval-events"
            ],
            "note": "The memory inventory identifies the database objects and their graph organization; this does not inspect dependency internals."
          },
          {
            "scope": "Retained embeddings for documents, entities, optional relations and reports",
            "assessment": "known",
            "findings": [
              {
                "value": "rdbms",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-embeddings"
                ],
                "note": "Database vector columns retain representations used by nearest-neighbor consumers."
              },
              {
                "value": "vector",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-embeddings"
                ],
                "note": "Database vector columns retain representations used by nearest-neighbor consumers."
              }
            ],
            "records": [
              "memory.md#mem-obj-embeddings"
            ],
            "note": "Vector storage is separate from text and graph metadata; geometry is not a model-weight update."
          },
          {
            "scope": "Evaluation result/grade outputs and replay baseline files",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evaluation-memory",
                  "epistemic.md#epi-obj-grade"
                ],
                "note": "Shipped evaluators persist JSON; replay reloads baseline records."
              }
            ],
            "records": [
              "memory.md#mem-rte-evaluation-memory",
              "epistemic.md#epi-obj-grade"
            ],
            "note": "This includes file retention, not proof of every benchmark output's contents."
          },
          {
            "scope": "Additional retention inside caller-injected extractor/services",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extractor-extension"
            ],
            "note": "Injected implementations' extra storage is unresolved; their known graph outputs are included above."
          }
        ],
        "records": [
          "memory.md#mem-obj-documents",
          "memory.md#mem-obj-entities",
          "memory.md#mem-obj-entity-metadata",
          "memory.md#mem-obj-relations",
          "memory.md#mem-obj-relation-metadata",
          "memory.md#mem-obj-community-text",
          "memory.md#mem-obj-community-metadata",
          "memory.md#mem-obj-retrieval-events",
          "memory.md#mem-obj-embeddings",
          "memory.md#mem-rte-evaluation-memory",
          "epistemic.md#epi-obj-grade",
          "runtime.md#rt-rte-extractor-extension"
        ],
        "note": "Known database and evaluation-file surfaces coexist with unresolved custom implementation storage. Provider weights and static package files are not retained memory created by these routes."
      },
      "representational_form": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Passage, entity description, relation prose and community prose at model/context consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-documents",
                  "memory.md#mem-obj-entities",
                  "memory.md#mem-obj-relations",
                  "memory.md#mem-obj-community-text"
                ],
                "note": "Models interpret retained source assertions, descriptions and reports as contextual evidence."
              }
            ],
            "records": [
              "memory.md#mem-obj-documents",
              "memory.md#mem-obj-entities",
              "memory.md#mem-obj-relations",
              "memory.md#mem-obj-community-text"
            ],
            "note": "Names and alias display are interpreted text here; equality and lexical consumers are separated below."
          },
          {
            "scope": "Identity, provenance, lifecycle, hierarchy, rating, event fields and relation lexical access",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-entity-metadata",
                  "memory.md#mem-obj-relation-metadata",
                  "memory.md#mem-obj-community-metadata",
                  "memory.md#mem-obj-retrieval-events",
                  "memory.md#mem-obj-relations"
                ],
                "note": "Fixed rules consume IDs, flags, counts, scores and lexical fields; numeric ratings are not distributed parameters."
              }
            ],
            "records": [
              "memory.md#mem-obj-documents",
              "memory.md#mem-obj-entity-metadata",
              "memory.md#mem-obj-relation-metadata",
              "memory.md#mem-obj-community-metadata",
              "memory.md#mem-obj-retrieval-events",
              "memory.md#mem-obj-relations"
            ],
            "note": "Document hashes and source fields also control replacement and references."
          },
          {
            "scope": "Stored dense embeddings at similarity consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "parametric",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-embeddings"
                ],
                "note": "Nearest-neighbor consumers operate on distributed dense numerical encodings, not readable assertions."
              }
            ],
            "records": [
              "memory.md#mem-obj-embeddings"
            ],
            "note": "The hash fallback is separately symbolic; one parametric witness does not classify that alternative."
          },
          {
            "scope": "Deterministic term-hash embedding fallback",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-cmp-local-embedding"
                ],
                "note": "Term hashing uses a fixed algorithm rather than learned dense representation."
              }
            ],
            "records": [
              "runtime.md#rt-cmp-local-embedding",
              "memory.md#mem-obj-embeddings"
            ],
            "note": "Only the explicit hash alternative is classified here; remote and local learned alternatives remain distinct."
          },
          {
            "scope": "Evaluation JSON/replay payloads",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evaluation-memory",
                  "epistemic.md#epi-obj-grade"
                ],
                "note": "Structured questions/spaces/golds, labels and aggregates have fixed file-reader/scorer roles."
              },
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evaluation-memory",
                  "epistemic.md#epi-obj-grade"
                ],
                "note": "Stored gold/prediction text is interpreted by judges; replay supplies questions to query."
              }
            ],
            "records": [
              "memory.md#mem-rte-evaluation-memory",
              "epistemic.md#epi-obj-grade"
            ],
            "note": "The records establish these parts, not the contents of unassessed result bodies."
          },
          {
            "scope": "Additional injected extractor/service retained payloads",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extractor-extension"
            ],
            "note": "No encoding or later consumption of possible extra retained payloads is established."
          }
        ],
        "records": [
          "memory.md#mem-obj-documents",
          "memory.md#mem-obj-entities",
          "memory.md#mem-obj-relations",
          "memory.md#mem-obj-community-text",
          "memory.md#mem-obj-entity-metadata",
          "memory.md#mem-obj-relation-metadata",
          "memory.md#mem-obj-community-metadata",
          "memory.md#mem-obj-retrieval-events",
          "memory.md#mem-obj-embeddings",
          "runtime.md#rt-cmp-local-embedding",
          "memory.md#mem-rte-evaluation-memory",
          "epistemic.md#epi-obj-grade",
          "runtime.md#rt-rte-extractor-extension"
        ],
        "note": "Operative text, fixed-rule fields and numerical vectors are split by consumer; custom implementation payloads prevent a complete-form assertion."
      },
      "lineage": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Caller passages, conversational dataset turns and replay baseline input",
            "assessment": "known",
            "findings": [
              {
                "value": "imported",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-documents",
                  "memory.md#mem-rte-evaluation-memory"
                ],
                "note": "Documents, dataset sessions and prior baseline questions enter from caller/file inputs."
              }
            ],
            "records": [
              "memory.md#mem-obj-documents",
              "memory.md#mem-rte-evaluation-memory"
            ],
            "note": "Import identifies the entry path, not human authorship or truth of source content."
          },
          {
            "scope": "Default extracted entities/relations, their merges, generated reports, embeddings and lifecycle/access state",
            "assessment": "known",
            "findings": [
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-document-admission",
                  "memory.md#mem-obj-entities",
                  "memory.md#mem-obj-relation-metadata",
                  "memory.md#mem-obj-community-text",
                  "memory.md#mem-obj-embeddings",
                  "runtime.md#rt-rte-retention-control"
                ],
                "note": "Model/code transformations derive retained products from imported content, existing graph state and access statistics."
              }
            ],
            "records": [
              "runtime.md#rt-rte-document-admission",
              "memory.md#mem-obj-entities",
              "memory.md#mem-obj-entity-metadata",
              "memory.md#mem-obj-relations",
              "memory.md#mem-obj-relation-metadata",
              "memory.md#mem-obj-community-text",
              "memory.md#mem-obj-community-metadata",
              "memory.md#mem-obj-embeddings",
              "runtime.md#rt-rte-retention-control"
            ],
            "note": "Known derivation does not establish provider training lineage or custom proposal provenance."
          },
          {
            "scope": "Retrieval event records and exposure-derived archive state",
            "assessment": "known",
            "findings": [
              {
                "value": "trace-extracted",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-retrieval-events",
                  "runtime.md#rt-rte-retention-control"
                ],
                "note": "Retrieval activity produces access traces; aggregates select durable archive timestamps."
              }
            ],
            "records": [
              "memory.md#mem-obj-retrieval-events",
              "runtime.md#rt-rte-retention-control"
            ],
            "note": "The traced activity records exposure, not correctness."
          },
          {
            "scope": "Session-derived graph facts in the conversational harness",
            "assessment": "known",
            "findings": [
              {
                "value": "trace-extracted",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evaluation-memory",
                  "runtime.md#rt-rte-document-admission"
                ],
                "note": "Rendered conversational turns are automatically extracted into facts consumed by later questions."
              }
            ],
            "records": [
              "memory.md#mem-rte-evaluation-memory",
              "runtime.md#rt-rte-document-admission"
            ],
            "note": "This is dataset conversation, not proven experience of the running engine itself."
          },
          {
            "scope": "Caller-supplied/direct-store content and external extractor proposal origin",
            "assessment": "partial",
            "findings": [
              {
                "value": "imported",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-extractor-extension",
                  "runtime.md#rt-rte-document-admission"
                ],
                "note": "External callback results enter the graph through supported admission interfaces."
              }
            ],
            "records": [
              "runtime.md#rt-rte-extractor-extension",
              "runtime.md#rt-rte-document-admission"
            ],
            "note": "The imported entry path is known; whether supplied content was originally authored, trace-derived or otherwise compiled is unresolved."
          },
          {
            "scope": "Embedding initial provenance and unassessed evaluator/injected retention derivations",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-embeddings",
              "runtime.md#rt-rte-extractor-extension",
              "memory.md#mem-rte-evaluation-memory"
            ],
            "note": "Records do not establish provider training provenance or every alternative's initial derivation; known subsequent embedding calls remain above."
          }
        ],
        "records": [
          "memory.md#mem-obj-documents",
          "memory.md#mem-rte-evaluation-memory",
          "runtime.md#rt-rte-document-admission",
          "memory.md#mem-obj-entities",
          "memory.md#mem-obj-entity-metadata",
          "memory.md#mem-obj-relations",
          "memory.md#mem-obj-relation-metadata",
          "memory.md#mem-obj-community-text",
          "memory.md#mem-obj-community-metadata",
          "memory.md#mem-obj-embeddings",
          "runtime.md#rt-rte-retention-control",
          "memory.md#mem-obj-retrieval-events",
          "runtime.md#rt-rte-extractor-extension"
        ],
        "note": "Known import and downstream compilation do not erase unknown initial provenance. No evidence establishes a human-authored retained-memory admission as such."
      },
      "behavioral_authority": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Passages, entity/relation prose and reports delivered to synthesis, report models or context callers",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-documents",
                  "memory.md#mem-obj-entities",
                  "memory.md#mem-obj-relations",
                  "memory.md#mem-obj-community-text",
                  "runtime.md#rt-rte-question-answer"
                ],
                "note": "Retained assertions and summaries supply evidence/context, not a verified truth license."
              }
            ],
            "records": [
              "memory.md#mem-obj-documents",
              "memory.md#mem-obj-entities",
              "memory.md#mem-obj-relations",
              "memory.md#mem-obj-community-text",
              "runtime.md#rt-rte-question-answer"
            ],
            "note": "The static answer/extraction prompts are excluded; their directions are not authority of accumulated prose."
          },
          {
            "scope": "Retained embeddings, lexical relation text, relation cues and community ratings at rankers",
            "assessment": "known",
            "findings": [
              {
                "value": "ranking",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-embeddings",
                  "memory.md#mem-obj-relations",
                  "memory.md#mem-obj-relation-metadata",
                  "memory.md#mem-obj-community-metadata",
                  "runtime.md#rt-rte-question-answer"
                ],
                "note": "Similarity, lexical scoring, relation cues and rating/size affect relative retrieval priority."
              }
            ],
            "records": [
              "memory.md#mem-obj-embeddings",
              "memory.md#mem-obj-relations",
              "memory.md#mem-obj-relation-metadata",
              "memory.md#mem-obj-community-metadata",
              "runtime.md#rt-rte-question-answer"
            ],
            "note": "Fixed scoring can give content ranking force without learned ranking policy."
          },
          {
            "scope": "Archive/dormancy/supersession and temporal controls at entity/relation/snapshot eligibility checks",
            "assessment": "known",
            "findings": [
              {
                "value": "enforcement",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-entity-metadata",
                  "memory.md#mem-obj-relation-metadata",
                  "runtime.md#rt-rte-retention-control",
                  "memory.md#mem-rte-document-withdrawal",
                  "epistemic.md#epi-rte-supersession-write"
                ],
                "note": "Stored control fields exclude candidates on named consumers, not every answer channel."
              },
              {
                "value": "validation",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-entity-metadata",
                  "memory.md#mem-obj-relation-metadata",
                  "runtime.md#rt-rte-retention-control",
                  "epistemic.md#epi-rte-supersession-write"
                ],
                "note": "Stored flags and scope fields supply eligibility criteria against which selected candidates are tested."
              }
            ],
            "records": [
              "memory.md#mem-obj-entity-metadata",
              "memory.md#mem-obj-relation-metadata",
              "runtime.md#rt-rte-retention-control",
              "memory.md#mem-rte-document-withdrawal",
              "epistemic.md#epi-rte-supersession-write"
            ],
            "note": "Both the criterion and the enforced exclusion are local to actual filters; stale reports/documents may still carry old assertions."
          },
          {
            "scope": "Document identities/hashes, alias/mention/provenance and hierarchy/replay fields at later operations",
            "assessment": "known",
            "findings": [
              {
                "value": "routing",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-documents",
                  "memory.md#mem-obj-entity-metadata",
                  "memory.md#mem-obj-relation-metadata",
                  "memory.md#mem-obj-community-metadata",
                  "memory.md#mem-rte-evaluation-memory"
                ],
                "note": "Hashes select skip/replace; aliases resolve future upserts; provenance and hierarchy/replay identities select affected rows or later input scope."
              }
            ],
            "records": [
              "memory.md#mem-obj-documents",
              "memory.md#mem-obj-entity-metadata",
              "memory.md#mem-obj-relation-metadata",
              "memory.md#mem-obj-community-metadata",
              "memory.md#mem-rte-evaluation-memory"
            ],
            "note": "These symbolic fields select operation, target or input; they are not standing natural-language directions."
          },
          {
            "scope": "Retrieval events at retention update consumer",
            "assessment": "known",
            "findings": [
              {
                "value": "learning",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-retrieval-events",
                  "runtime.md#rt-rte-retention-control"
                ],
                "note": "Retained experience feeds a durable behavior-shaping update to archive eligibility."
              }
            ],
            "records": [
              "memory.md#mem-obj-retrieval-events",
              "runtime.md#rt-rte-retention-control"
            ],
            "note": "This authority names the update path, not demonstrated capacity improvement; resulting flags enforce later selection."
          },
          {
            "scope": "Session traces at conversational extraction consumer",
            "assessment": "known",
            "findings": [
              {
                "value": "learning",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evaluation-memory",
                  "runtime.md#rt-rte-document-admission"
                ],
                "note": "Recorded turns feed automatic retained fact construction for later contextual use."
              }
            ],
            "records": [
              "memory.md#mem-rte-evaluation-memory",
              "runtime.md#rt-rte-document-admission"
            ],
            "note": "Derived facts have downstream knowledge authority; their trace input has the separate update-consumer role."
          },
          {
            "scope": "Evaluation grades at an external operator or automatic adoption consumer",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "epistemic.md#epi-obj-grade",
              "epistemic.md#epi-rte-benchmark-check",
              "memory.md#mem-rte-evaluation-memory"
            ],
            "note": "Scores are saved and reported, but no actual later automatic product-adoption consumer is established; possible operator use is not a wired learning path."
          },
          {
            "scope": "Additional injected retained content and consumers",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extractor-extension"
            ],
            "note": "Extra retained parts and their consequential consumers remain opaque."
          }
        ],
        "records": [
          "memory.md#mem-obj-documents",
          "memory.md#mem-obj-entities",
          "memory.md#mem-obj-relations",
          "memory.md#mem-obj-community-text",
          "runtime.md#rt-rte-question-answer",
          "memory.md#mem-obj-embeddings",
          "memory.md#mem-obj-relation-metadata",
          "memory.md#mem-obj-community-metadata",
          "memory.md#mem-obj-entity-metadata",
          "runtime.md#rt-rte-retention-control",
          "memory.md#mem-rte-document-withdrawal",
          "epistemic.md#epi-rte-supersession-write",
          "memory.md#mem-rte-evaluation-memory",
          "memory.md#mem-obj-retrieval-events",
          "runtime.md#rt-rte-document-admission",
          "epistemic.md#epi-obj-grade",
          "epistemic.md#epi-rte-benchmark-check",
          "runtime.md#rt-rte-extractor-extension"
        ],
        "note": "The record-supported consumer paths establish several coexisting forces. No retained standing instruction or online parameter update is inferred from shipped prompts or provider components."
      },
      "write_agency": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Default extraction/embedding admission, graph upserts, telemetry, report build and lifecycle updates",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-document-admission",
                  "runtime.md#rt-rte-community-build",
                  "runtime.md#rt-rte-retention-control",
                  "memory.md#mem-rte-document-withdrawal"
                ],
                "note": "Software/model admits individual records and changes flags after caller initiation, without per-content operator approval."
              }
            ],
            "records": [
              "runtime.md#rt-rte-document-admission",
              "runtime.md#rt-rte-community-build",
              "runtime.md#rt-rte-retention-control",
              "memory.md#mem-rte-document-withdrawal",
              "memory.md#mem-obj-retrieval-events",
              "epistemic.md#epi-rte-relation-upsert",
              "epistemic.md#epi-rte-supersession-write"
            ],
            "note": "Caller triggering a build, retention or deletion does not make downstream selected writes manual."
          },
          {
            "scope": "Evaluation session extraction and saved evaluator outputs",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evaluation-memory",
                  "epistemic.md#epi-rte-benchmark-check"
                ],
                "note": "Harness code and model gates admit per-fact products and serialize results/grades without per-item human review."
              }
            ],
            "records": [
              "memory.md#mem-rte-evaluation-memory",
              "epistemic.md#epi-rte-benchmark-check"
            ],
            "note": "Choosing a dataset or scorer is not per-content approval."
          },
          {
            "scope": "Initial document/direct-store content supply and custom extractor/service admission",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-documents",
              "runtime.md#rt-rte-extractor-extension",
              "runtime.md#rt-rte-document-admission"
            ],
            "note": "Generic caller identity does not establish an explicit human content decision, nor every custom implementation's admission policy."
          }
        ],
        "records": [
          "runtime.md#rt-rte-document-admission",
          "runtime.md#rt-rte-community-build",
          "runtime.md#rt-rte-retention-control",
          "memory.md#mem-rte-document-withdrawal",
          "memory.md#mem-obj-retrieval-events",
          "epistemic.md#epi-rte-relation-upsert",
          "epistemic.md#epi-rte-supersession-write",
          "memory.md#mem-rte-evaluation-memory",
          "epistemic.md#epi-rte-benchmark-check",
          "memory.md#mem-obj-documents",
          "runtime.md#rt-rte-extractor-extension"
        ],
        "note": "Known automatic mechanisms coexist with unresolved initial supply/custom control; no manual finding is inferred from a caller API."
      },
      "curation_operations": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Default extraction of entity descriptions and standing conversational facts; community and parent report compression",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-document-admission",
                  "memory.md#mem-obj-entities",
                  "memory.md#mem-obj-community-text",
                  "runtime.md#rt-rte-community-build",
                  "memory.md#mem-rte-evaluation-memory"
                ],
                "note": "Extraction and reporting reduce source or retained graph/session material to descriptions, facts and summaries."
              }
            ],
            "records": [
              "runtime.md#rt-rte-document-admission",
              "memory.md#mem-obj-entities",
              "memory.md#mem-obj-community-text",
              "runtime.md#rt-rte-community-build",
              "memory.md#mem-rte-evaluation-memory"
            ],
            "note": "The transformation is classified as compression, not proof of semantic faithfulness. Dropped scope or hallucination risk does not establish synthesize."
          },
          {
            "scope": "Alias resolution, same-key entity/relation merges and gleaned-result merging",
            "assessment": "known",
            "findings": [
              {
                "value": "dedup",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-entity-metadata",
                  "memory.md#mem-obj-entities",
                  "memory.md#mem-obj-relation-metadata",
                  "epistemic.md#epi-rte-relation-upsert"
                ],
                "note": "Alias and same-key matching combine repeat identities/assertions; this exceeds a collision check because retained payloads are merged."
              },
              {
                "value": "evolve",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-entities",
                  "memory.md#mem-obj-relation-metadata",
                  "epistemic.md#epi-rte-relation-upsert"
                ],
                "note": "Existing descriptions, confidence, polarity, validity and provenance can be revised by upsert."
              }
            ],
            "records": [
              "memory.md#mem-obj-entity-metadata",
              "memory.md#mem-obj-entities",
              "memory.md#mem-obj-relation-metadata",
              "epistemic.md#epi-rte-relation-upsert"
            ],
            "note": "Payload replacement is wired, while correctness and preservation of source scope are unobserved."
          },
          {
            "scope": "Supersession, provenance withdrawal, dormancy and revival",
            "assessment": "known",
            "findings": [
              {
                "value": "invalidate",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-document-withdrawal",
                  "epistemic.md#epi-rte-supersession-write",
                  "memory.md#mem-obj-relation-metadata"
                ],
                "note": "Flags withdraw reliance on retained graph assertions while leaving rows/addressable history."
              },
              {
                "value": "evolve",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-document-withdrawal",
                  "memory.md#mem-obj-relation-metadata"
                ],
                "note": "Source lists/weights and dormancy/revival state change existing entries."
              }
            ],
            "records": [
              "memory.md#mem-rte-document-withdrawal",
              "memory.md#mem-obj-relation-metadata",
              "epistemic.md#epi-rte-supersession-write"
            ],
            "note": "Deleted raw passages are not retained history; old reports are not universally withdrawn."
          },
          {
            "scope": "Exposure-based retention archiving",
            "assessment": "known",
            "findings": [
              {
                "value": "decay",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-retention-control",
                  "memory.md#mem-obj-retrieval-events"
                ],
                "note": "Low-scored entities are demoted from later seed and snapshot eligibility."
              }
            ],
            "records": [
              "runtime.md#rt-rte-retention-control",
              "memory.md#mem-obj-retrieval-events",
              "memory.md#mem-obj-entity-metadata"
            ],
            "note": "No universal forgetting across document/relation/report channels is asserted."
          },
          {
            "scope": "Opaque custom extraction transformations and unassessed evaluator adoption/maintenance",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extractor-extension",
              "memory.md#mem-rte-evaluation-memory",
              "epistemic.md#epi-rte-benchmark-check"
            ],
            "note": "No controlled operation is established for these alternatives; no inferred synthesize or promote from route names, outputs or scores."
          }
        ],
        "records": [
          "runtime.md#rt-rte-document-admission",
          "memory.md#mem-obj-entities",
          "memory.md#mem-obj-community-text",
          "runtime.md#rt-rte-community-build",
          "memory.md#mem-rte-evaluation-memory",
          "memory.md#mem-obj-entity-metadata",
          "memory.md#mem-obj-relation-metadata",
          "epistemic.md#epi-rte-relation-upsert",
          "memory.md#mem-rte-document-withdrawal",
          "epistemic.md#epi-rte-supersession-write",
          "runtime.md#rt-rte-retention-control",
          "memory.md#mem-obj-retrieval-events",
          "runtime.md#rt-rte-extractor-extension",
          "epistemic.md#epi-rte-benchmark-check"
        ],
        "note": "Consolidation, deduplication, revision, invalidation and demotion are supported locally. Unknown branches prevent a complete inventory; rebuild/acquisition alone adds no curation value."
      },
      "read_back_direction": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Question-driven retrieval, caller-triggered report builds/retention, change polling, drill-down and replay",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-question-answer",
                  "runtime.md#rt-rte-community-build",
                  "runtime.md#rt-rte-retention-control",
                  "memory.md#mem-rte-change-polling",
                  "memory.md#mem-rte-evaluation-memory"
                ],
                "note": "Consumers request retained corpus, reports, events or replay records; internal automatic selection fulfills those requests."
              },
              {
                "value": "pull",
                "basis": "afforded",
                "records": [
                  "memory.md#mem-rte-corpus-inspection"
                ],
                "note": "Document and community inspection exposes requested retained structures to a documented consumer role."
              }
            ],
            "records": [
              "runtime.md#rt-rte-question-answer",
              "runtime.md#rt-rte-community-build",
              "runtime.md#rt-rte-retention-control",
              "memory.md#mem-rte-change-polling",
              "memory.md#mem-rte-corpus-inspection",
              "memory.md#mem-rte-evaluation-memory"
            ],
            "note": "Later requests read accumulated material. Synthesis delivery after query is not an additional unsolicited push."
          },
          {
            "scope": "Additional injected-service consumers and unassessed evaluation output adoption",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extractor-extension",
              "memory.md#mem-rte-evaluation-memory",
              "epistemic.md#epi-rte-benchmark-check"
            ],
            "note": "Records do not settle additional later-consumer routes or whether they are requested; known pull does not exclude unresolved push."
          }
        ],
        "records": [
          "runtime.md#rt-rte-question-answer",
          "runtime.md#rt-rte-community-build",
          "runtime.md#rt-rte-retention-control",
          "memory.md#mem-rte-change-polling",
          "memory.md#mem-rte-corpus-inspection",
          "memory.md#mem-rte-evaluation-memory",
          "runtime.md#rt-rte-extractor-extension",
          "epistemic.md#epi-rte-benchmark-check"
        ],
        "note": "All inspected read-back is consumer-requested. Coverage of custom/evaluator alternatives is unresolved, so no system-complete pull-only assertion is made."
      },
      "read_back_signal": {
        "assessment": "not-determinable",
        "units": [
          {
            "scope": "Assessed query/build/maintenance/polling/inspection/replay pull chains",
            "assessment": "inapplicable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-question-answer",
              "runtime.md#rt-rte-community-build",
              "runtime.md#rt-rte-retention-control",
              "memory.md#mem-rte-change-polling",
              "memory.md#mem-rte-corpus-inspection",
              "memory.md#mem-rte-evaluation-memory"
            ],
            "note": "These chains fulfill explicit requests; their vectors, lexical matches and IDs are pull selectors, not push signals."
          },
          {
            "scope": "Potential additional injected-service or evaluation-adoption delivery",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extractor-extension",
              "memory.md#mem-rte-evaluation-memory",
              "epistemic.md#epi-rte-benchmark-check"
            ],
            "note": "No actual push trigger, input and selected retained part is recorded for unresolved alternatives; no controlled push signal can be assigned."
          }
        ],
        "records": [
          "runtime.md#rt-rte-question-answer",
          "runtime.md#rt-rte-community-build",
          "runtime.md#rt-rte-retention-control",
          "memory.md#mem-rte-change-polling",
          "memory.md#mem-rte-corpus-inspection",
          "memory.md#mem-rte-evaluation-memory",
          "runtime.md#rt-rte-extractor-extension",
          "epistemic.md#epi-rte-benchmark-check"
        ],
        "note": "No supported push signal exists in the classified records. Whole-axis inapplicability is unwarranted because the broader included alternatives are not completely assessed."
      },
      "trace_learning": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Retrieval exposure to retention score to durable archive state to later seed/snapshot consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-retrieval-events",
                  "runtime.md#rt-rte-retention-control",
                  "memory.md#mem-obj-entity-metadata"
                ],
                "note": "Automatic trace-fed archive writes change durable selection state consumed by later queries/builds."
              }
            ],
            "records": [
              "memory.md#mem-obj-retrieval-events",
              "runtime.md#rt-rte-retention-control",
              "memory.md#mem-obj-entity-metadata"
            ],
            "note": "Requires telemetry and caller non-dry-run retention. Wired capacity is not observed use, improved answers or trained weights."
          },
          {
            "scope": "Conversational session extraction to retained graph facts to later benchmark questions",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evaluation-memory",
                  "runtime.md#rt-rte-document-admission",
                  "memory.md#mem-obj-documents"
                ],
                "note": "Recorded turns feed automatic fact writes; later questions receive the derived graph/source context."
              }
            ],
            "records": [
              "memory.md#mem-rte-evaluation-memory",
              "runtime.md#rt-rte-document-admission",
              "memory.md#mem-obj-documents"
            ],
            "note": "Dataset origin and per-instance schema cleanup bound the horizon; own-runtime experience is not required."
          },
          {
            "scope": "Custom extractor/service trace origin and unassessed evaluator update alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extractor-extension",
              "memory.md#mem-rte-evaluation-memory",
              "epistemic.md#epi-rte-benchmark-check"
            ],
            "note": "Input origin and automatic later behavior-shaping writes are not settled for these alternatives. Raw result/log retention alone is insufficient."
          }
        ],
        "records": [
          "memory.md#mem-obj-retrieval-events",
          "runtime.md#rt-rte-retention-control",
          "memory.md#mem-obj-entity-metadata",
          "memory.md#mem-rte-evaluation-memory",
          "runtime.md#rt-rte-document-admission",
          "memory.md#mem-obj-documents",
          "runtime.md#rt-rte-extractor-extension",
          "epistemic.md#epi-rte-benchmark-check"
        ],
        "note": "Two qualifying wired paths support a system union yes with partial coverage. No local no is assigned: supplied reports declare no bounded absence record for a complete negative learning unit."
      },
      "trace_source": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Retention update input: timestamped retrieval exposure events",
            "assessment": "known",
            "findings": [
              {
                "value": "event-streams",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-retrieval-events",
                  "runtime.md#rt-rte-retention-control"
                ],
                "note": "Discrete retrieval events supply selected IDs and hit/recency aggregates to archive scoring."
              }
            ],
            "records": [
              "memory.md#mem-obj-retrieval-events",
              "runtime.md#rt-rte-retention-control"
            ],
            "note": "Hashes/IDs are events of retrieval exposure, not session messages, tool transcripts or answer-quality feedback."
          },
          {
            "scope": "Conversational harness fact-extraction input",
            "assessment": "known",
            "findings": [
              {
                "value": "session-logs",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-evaluation-memory"
                ],
                "note": "Original conversational turns retain user/assistant session origin when rendered into document text."
              }
            ],
            "records": [
              "memory.md#mem-rte-evaluation-memory",
              "runtime.md#rt-rte-document-admission"
            ],
            "note": "Wrapping turns as documents does not add event-streams; no linked action/outcome trajectory use is established."
          },
          {
            "scope": "Custom/injected trace inputs and unresolved evaluator update alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-extractor-extension",
              "memory.md#mem-rte-evaluation-memory",
              "epistemic.md#epi-rte-benchmark-check"
            ],
            "note": "Unknown original input and update consumers prevent assigning a trace-source value or inapplicability."
          }
        ],
        "records": [
          "memory.md#mem-obj-retrieval-events",
          "runtime.md#rt-rte-retention-control",
          "memory.md#mem-rte-evaluation-memory",
          "runtime.md#rt-rte-document-admission",
          "runtime.md#rt-rte-extractor-extension",
          "epistemic.md#epi-rte-benchmark-check"
        ],
        "note": "Classifies original inputs of qualifying writes, not every imported document or all files retained for reporting. Both event-stream and session sources have wired local warrants; remaining routes are unresolved."
      }
    }
  }
}
---

# post-graph-rag memory profile

## Comparison rationale

### Boundary and coverage

The profile classifies the accepted records, not fresh source observations. PostgreSQL graph payloads and vector columns are retained memory; process-local query parameters and static shipped prompts are not. File retention is included for shipped evaluator results and replay inputs. Custom proposal provenance, possible extra storage and unassessed evaluator consumers remain local unresolved units rather than being erased by inspected database witnesses. See [MEM-OBJ-documents](memory.md#mem-obj-documents), [MEM-OBJ-embeddings](memory.md#mem-obj-embeddings), [MEM-RTE-evaluation-memory](memory.md#mem-rte-evaluation-memory) and [RT-RTE-extractor-extension](runtime.md#rt-rte-extractor-extension).

Known units describe complete classification only within their named part and consumer path. All positive bases are implementation wiring except the separately afforded inspection consumer. No finding claims observed execution, reliable model compliance or causal benefit. The profile makes no complete-value assertion for unresolved injected or evaluation-adoption alternatives. Their unknowns are not evidence that extra behavior exists.

### Encoding, lineage and authority

Graph storage and symbolic form are independent: stored prose has natural-language consumption, metadata has fixed-rule consumption, and learned dense vectors have distributed-parametric consumption. The deterministic term-hash fallback is symbolic rather than learned. Provider training provenance remains unresolved without obscuring the known call that produces a retained embedding. See [MEM-OBJ-embeddings](memory.md#mem-obj-embeddings) and [RT-CMP-local-embedding](runtime.md#rt-cmp-local-embedding).

Imported source passages and software/model-derived products coexist. Session-derived facts and retrieval-derived archive fields additionally have trace-extracted lineage. No generic caller identity proves human-authored memory or per-content human admission. The known automatic write mechanisms remain classified even where initial proposal provenance is unknown. See [RT-RTE-document-admission](runtime.md#rt-rte-document-admission), [MEM-OBJ-documents](memory.md#mem-obj-documents) and [MEM-RTE-evaluation-memory](memory.md#mem-rte-evaluation-memory).

Retained prose supplies knowledge at model/context consumers. Embeddings, lexical text and ratings influence ranking. Stored eligibility fields are validation criteria with enforced exclusions on their named consumers; routing fields select operation targets or input scope. These are distinct from the static prompts' instruction force. No all-channel withholding is inferred from archive, dormancy or supersession: old passages and reports can still carry an assertion. See [MEM-BAP-access-state](memory.md#mem-bap-access-state), [MEM-OBJ-relation-metadata](memory.md#mem-obj-relation-metadata), [MEM-OBJ-community-metadata](memory.md#mem-obj-community-metadata) and [EPI-RTE-supersession-write](epistemic.md#epi-rte-supersession-write).

### Transformations and later consumption

Extraction and reporting consolidate material. Model requests and lossy projections do not establish faithful semantic preservation, but that uncertainty does not turn consolidation into synthesis. No recorded witness establishes a newly introduced claim as the implemented synthesis operation. Same-key/alias merges both deduplicate and revise existing payloads. Supersession/withdrawal invalidate reliance while retaining graph residue, and retention demotes access eligibility. See [MEM-OBJ-entities](memory.md#mem-obj-entities), [MEM-OBJ-community-text](memory.md#mem-obj-community-text), [EPI-RTE-relation-upsert](epistemic.md#epi-rte-relation-upsert), [EPI-RTE-community-render](epistemic.md#epi-rte-community-render) and [MEM-RTE-document-withdrawal](memory.md#mem-rte-document-withdrawal).

Questions request corpus retrieval; builds request graph/child-report input; maintenance requests event/statistical input; replay requests prior baseline records. Selection and delivery inside those chains remain pull, not another push merely because software chooses results. Therefore the assessed pull chains have no push signal. Unknown additional consumers prevent a whole-inventory inapplicable signal assessment. See [RT-RTE-question-answer](runtime.md#rt-rte-question-answer), [RT-RTE-community-build](runtime.md#rt-rte-community-build), [RT-RTE-retention-control](runtime.md#rt-rte-retention-control), [MEM-RTE-change-polling](memory.md#mem-rte-change-polling) and [MEM-RTE-evaluation-memory](memory.md#mem-rte-evaluation-memory).

### Trace-fed writes and unions

Two wired routes qualify independently. Retrieval events feed archive writes whose flags alter later seeds/snapshots. Session turns feed automatic durable fact construction whose results reach later benchmark questions. Their update inputs have learning authority; archive flags downstream enforce eligibility and extracted facts downstream provide knowledge. The original trace sources are respectively event-streams and session-logs. Neither route requires parameter training, a new true proposition, observed improvement or own-agent experience. Instance-local cleanup bounds conversational persistence but does not remove later-invocation consumption. See [MEM-OBJ-retrieval-events](memory.md#mem-obj-retrieval-events), [RT-RTE-retention-control](runtime.md#rt-rte-retention-control) and [MEM-RTE-evaluation-memory](memory.md#mem-rte-evaluation-memory).

The derived learning union supports yes at wired basis, with partial inventory coverage. No no is inferred from parameter fixity, saved grades without an update consumer, or raw logs alone. Other evaluated/injected origins and adoption mechanisms remain unresolved. Session wrappers do not add an event-stream source, and neither hash records nor session chronology alone establishes tool-traces or trajectories. See [EPI-RTE-benchmark-check](epistemic.md#epi-rte-benchmark-check) and [RT-RTE-extractor-extension](runtime.md#rt-rte-extractor-extension).

### Supersessions and source-read log

Reconciliation replaces the duplicate epistemic passage with [MEM-OBJ-documents](memory.md#mem-obj-documents), report prose with [MEM-OBJ-community-text](memory.md#mem-obj-community-text), and source-withdrawal route with [MEM-RTE-document-withdrawal](memory.md#mem-rte-document-withdrawal). This profile uses those canonical records. The replacements alter no controlled value: they identify the same retained objects/routes while preserving their limits. Entity/relation containers remain valid alongside their separately consumed parts, and community rating remains a part of the broader metadata inventory rather than a duplicate.

No source files were read. All classifications and assessment warrants come from the supplied accepted members and their record passages; no records, quotations or evidence were added.

---
{
  "type": "agentic-system-analyses/types/agentic-system-memory-profile.md",
  "description": "Kompl memory comparison: compiled wiki and access indexes, drafting conventions, conversational feedback and failure-trace projections at the frozen commit.",
  "run-id": "AAS-2026-10-14-kompl-9cffb1e5eb86-01",
  "source-identity": "https://github.com/tuirk/Kompl",
  "reviewed-boundary": "17970c969b0c2576bf722840e0e2db3c6416a7aa",
  "memory-comparison": {
    "version": 2,
    "scope": "Included: converted raw sources; retained extractions, aliases and mentions; draft prose and cross-invocation summaries; current/outbox/previous wiki prose and access metadata; SQLite FTS; Chroma embeddings, document prefixes and metadata; generated or restored schema; chat turns and FAQ candidates; activity/lint/failure records and saved-links projections; accumulated plan/progress/settings only at recorded later consumers; archive and direct replacement alternatives; unresolved provider-hidden continuation/checkpoint state on included calls. Excluded: static shipped code/prompts/instructions, fixed installed/provider model weights, transient current-call values with no later consumer, external MCP agents' own storage/context decisions, and unrelated product-update machinery. Provider-hidden memory is an unresolved alternative, not an asserted retained object.",
    "axes": {
      "storage_substrate": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Converted raw source payloads",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-raw"
                ],
                "note": "Raw markdown persists in source-ID gzip files."
              }
            ],
            "records": [
              "memory.md#mem-obj-raw"
            ],
            "note": "Gzip encoding does not change the filesystem substrate."
          },
          {
            "scope": "Current and previous wiki prose and page outbox",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-pages"
                ],
                "note": "Current and previous gzip markdown is later readable."
              },
              {
                "value": "sqlite",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-pages"
                ],
                "note": "Pending content persists in the page outbox for recovery and fallback reads."
              }
            ],
            "records": [
              "memory.md#mem-obj-pages"
            ],
            "note": "The file archive and SQLite pending-content are separate retained copies, both operative."
          },
          {
            "scope": "Extractions, aliases, mentions, FTS, plans/drafts, chat and maintenance/control metadata",
            "assessment": "known",
            "findings": [
              {
                "value": "sqlite",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-extractions",
                  "memory.md#mem-obj-aliases",
                  "memory.md#mem-obj-mentions",
                  "memory.md#mem-obj-pages-fts",
                  "runtime.md#rt-obj-page-plans",
                  "epistemic.md#epi-obj-draft-content",
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-history-read",
                  "memory.md#mem-obj-activity-log",
                  "memory.md#mem-rte-lint-retention"
                ],
                "note": "Retained extraction, access, proposal, interaction and maintenance state is stored in SQLite."
              }
            ],
            "records": [
              "memory.md#mem-obj-extractions",
              "memory.md#mem-obj-aliases",
              "memory.md#mem-obj-mentions",
              "memory.md#mem-obj-pages-fts",
              "runtime.md#rt-obj-page-plans",
              "epistemic.md#epi-obj-draft-content",
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-rte-history-read",
              "memory.md#mem-obj-activity-log",
              "memory.md#mem-rte-lint-retention"
            ],
            "note": "These are app-owned SQLite objects. Progress and settings are included only where accumulated values drive later retry or overdue checks."
          },
          {
            "scope": "Generated or restored maintenance schema",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-schema",
                  "runtime.md#rt-rte-schema-bootstrap",
                  "runtime.md#rt-rte-archive-import",
                  "memory.md#mem-rte-storage-write"
                ],
                "note": "The standing document is retained at /data/schema.md."
              }
            ],
            "records": [
              "runtime.md#rt-obj-schema",
              "runtime.md#rt-rte-schema-bootstrap",
              "runtime.md#rt-rte-archive-import",
              "memory.md#mem-rte-storage-write"
            ],
            "note": "All recorded installation alternatives target a text file."
          },
          {
            "scope": "Dense vectors and their IDs, metadata and document prefixes",
            "assessment": "known",
            "findings": [
              {
                "value": "vector",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-wiki-pages"
                ],
                "note": "The wiki_pages collection persists under /data/vectors."
              }
            ],
            "records": [
              "memory.md#mem-obj-wiki-pages"
            ],
            "note": "Chroma retention is recorded; its internal persistence implementation is not reclassified as an additional database substrate."
          },
          {
            "scope": "Provider-hidden continuation/context state on the included model-call paths, if retained across invocations",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-chat-feedback",
              "runtime.md#rt-rte-plan-draft"
            ],
            "note": "The reports do not inspect provider-hidden checkpoints or context. They establish neither this alternative's existence nor its storage substrate; it remains included as an unresolved alternative, not inferred provider memory."
          }
        ],
        "records": [
          "memory.md#mem-obj-raw",
          "memory.md#mem-obj-pages",
          "memory.md#mem-obj-extractions",
          "memory.md#mem-obj-aliases",
          "memory.md#mem-obj-mentions",
          "memory.md#mem-obj-pages-fts",
          "runtime.md#rt-obj-page-plans",
          "epistemic.md#epi-obj-draft-content",
          "memory.md#mem-obj-chat-messages",
          "memory.md#mem-rte-history-read",
          "memory.md#mem-obj-activity-log",
          "memory.md#mem-rte-lint-retention",
          "runtime.md#rt-obj-schema",
          "runtime.md#rt-rte-schema-bootstrap",
          "runtime.md#rt-rte-archive-import",
          "memory.md#mem-rte-storage-write",
          "memory.md#mem-obj-wiki-pages",
          "runtime.md#rt-rte-chat-feedback",
          "runtime.md#rt-rte-plan-draft"
        ],
        "note": "The recorded local memory inventory has file, SQLite and vector substrates. Hidden provider continuation state is unresolved; static model weights and shipped code are excluded, not classified as accumulated memory."
      },
      "representational_form": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Raw prose, wiki/current/outbox/previous prose, draft payloads, schema, chat text and diagnostic reasons",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-raw",
                  "memory.md#mem-obj-pages",
                  "runtime.md#rt-obj-page-plans",
                  "epistemic.md#epi-obj-draft-content",
                  "runtime.md#rt-obj-schema",
                  "runtime.md#rt-rte-schema-bootstrap",
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-history-read",
                  "memory.md#mem-obj-activity-log",
                  "memory.md#mem-rte-lint-retention"
                ],
                "note": "Prose and standing conventions have interpretation-dependent consumers."
              }
            ],
            "records": [
              "memory.md#mem-obj-raw",
              "memory.md#mem-obj-pages",
              "runtime.md#rt-obj-page-plans",
              "epistemic.md#epi-obj-draft-content",
              "runtime.md#rt-obj-schema",
              "runtime.md#rt-rte-schema-bootstrap",
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-rte-history-read",
              "memory.md#mem-obj-activity-log",
              "memory.md#mem-rte-lint-retention"
            ],
            "note": "These parts reach humans or models as interpreted text, independently of file/SQLite encoding."
          },
          {
            "scope": "Natural-language extraction claims and descriptions",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-extractions",
                  "epistemic.md#epi-obj-extraction-output"
                ],
                "note": "Extracted claims and dossiers supply interpreted factual reference."
              }
            ],
            "records": [
              "memory.md#mem-obj-extractions",
              "epistemic.md#epi-obj-extraction-output"
            ],
            "note": "Separate from JSON fields and quantitative features."
          },
          {
            "scope": "Structured extraction fields, aliases, mention relationships/counts, FTS access representation and plan/control/provenance fields",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-extractions",
                  "memory.md#mem-obj-aliases",
                  "memory.md#mem-obj-mentions",
                  "memory.md#mem-obj-pages-fts",
                  "runtime.md#rt-obj-page-plans",
                  "epistemic.md#epi-obj-draft-content",
                  "memory.md#mem-obj-pages",
                  "memory.md#mem-obj-activity-log",
                  "memory.md#mem-rte-lint-retention"
                ],
                "note": "Fixed lookup, counting, state predicates and FTS rules operate over localized fields."
              }
            ],
            "records": [
              "memory.md#mem-obj-extractions",
              "memory.md#mem-obj-aliases",
              "memory.md#mem-obj-mentions",
              "memory.md#mem-obj-pages-fts",
              "runtime.md#rt-obj-page-plans",
              "epistemic.md#epi-obj-draft-content",
              "memory.md#mem-obj-pages",
              "memory.md#mem-obj-activity-log",
              "memory.md#mem-rte-lint-retention"
            ],
            "note": "JSON is not uniformly symbolic: this unit covers fields with fixed-rule consumers, not their prose payloads."
          },
          {
            "scope": "Chat role/session/citation fields and vector IDs/metadata",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-history-read",
                  "memory.md#mem-obj-wiki-pages"
                ],
                "note": "Exact session/ID and metadata rules select and describe stored objects."
              }
            ],
            "records": [
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-rte-history-read",
              "memory.md#mem-obj-wiki-pages"
            ],
            "note": "Delivery of message text and page prose is classified separately."
          },
          {
            "scope": "Chroma dense embeddings",
            "assessment": "known",
            "findings": [
              {
                "value": "parametric",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-wiki-pages"
                ],
                "note": "Dense vectors spread similarity information across numerical coordinates."
              }
            ],
            "records": [
              "memory.md#mem-obj-wiki-pages"
            ],
            "note": "These are distributed numerical representations, not updated model weights."
          },
          {
            "scope": "Chroma document prefixes",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-wiki-pages"
                ],
                "note": "Retained document prefixes support display/access/backup."
              }
            ],
            "records": [
              "memory.md#mem-obj-wiki-pages"
            ],
            "note": "Prefixes remain text even though vector similarity, not these strings, selects candidate IDs."
          },
          {
            "scope": "Provider-hidden continuation/context state on the included model-call paths, if retained across invocations",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-chat-feedback",
              "runtime.md#rt-rte-plan-draft"
            ],
            "note": "The reports do not inspect provider-hidden checkpoints or context. They establish neither this alternative's existence nor its representational form; it remains included as an unresolved alternative, not inferred provider memory."
          }
        ],
        "records": [
          "memory.md#mem-obj-raw",
          "memory.md#mem-obj-pages",
          "runtime.md#rt-obj-page-plans",
          "epistemic.md#epi-obj-draft-content",
          "runtime.md#rt-obj-schema",
          "runtime.md#rt-rte-schema-bootstrap",
          "memory.md#mem-obj-chat-messages",
          "memory.md#mem-rte-history-read",
          "memory.md#mem-obj-activity-log",
          "memory.md#mem-rte-lint-retention",
          "memory.md#mem-obj-extractions",
          "epistemic.md#epi-obj-extraction-output",
          "memory.md#mem-obj-aliases",
          "memory.md#mem-obj-mentions",
          "memory.md#mem-obj-pages-fts",
          "memory.md#mem-obj-wiki-pages",
          "runtime.md#rt-rte-chat-feedback",
          "runtime.md#rt-rte-plan-draft"
        ],
        "note": "Mixed stores are split into interpreted prose, fixed-rule fields and distributed dense vectors. Actual generated schema content is not inspected, but its text delivery format is wired. Provider state form remains unresolved."
      },
      "lineage": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Acquired source markdown and original-source page passthrough",
            "assessment": "known",
            "findings": [
              {
                "value": "imported",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-raw",
                  "memory.md#mem-obj-pages",
                  "runtime.md#rt-rte-plan-draft"
                ],
                "note": "External source material enters raw storage and source reproduction pages."
              },
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-raw",
                  "memory.md#mem-obj-pages",
                  "runtime.md#rt-rte-plan-draft"
                ],
                "note": "Conversion and deterministic frontmatter wrapping transform the imported representation."
              }
            ],
            "records": [
              "memory.md#mem-obj-raw",
              "memory.md#mem-obj-pages",
              "runtime.md#rt-rte-plan-draft"
            ],
            "note": "Converted text preserves an acquisition path, not guaranteed original bytes or source warrant."
          },
          {
            "scope": "Model-produced extraction claims, page drafts/redrafts and generated schema",
            "assessment": "known",
            "findings": [
              {
                "value": "authored",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-extractions",
                  "runtime.md#rt-obj-page-plans",
                  "epistemic.md#epi-obj-draft-content",
                  "runtime.md#rt-obj-schema",
                  "runtime.md#rt-rte-schema-bootstrap",
                  "runtime.md#rt-rte-plan-draft",
                  "runtime.md#rt-rte-source-maintenance"
                ],
                "note": "Models produce claims/prose and maintenance conventions from selected input."
              },
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-extractions",
                  "runtime.md#rt-obj-page-plans",
                  "epistemic.md#epi-obj-draft-content",
                  "runtime.md#rt-obj-schema",
                  "runtime.md#rt-rte-schema-bootstrap",
                  "runtime.md#rt-rte-plan-draft",
                  "runtime.md#rt-rte-source-maintenance"
                ],
                "note": "Fixed planning, dossier construction and link/wrapper processing assemble derived retained artifacts."
              }
            ],
            "records": [
              "memory.md#mem-obj-extractions",
              "runtime.md#rt-obj-page-plans",
              "epistemic.md#epi-obj-draft-content",
              "runtime.md#rt-obj-schema",
              "runtime.md#rt-rte-schema-bootstrap",
              "runtime.md#rt-rte-plan-draft",
              "runtime.md#rt-rte-source-maintenance"
            ],
            "note": "Model authorship and surrounding code compilation are separate derivation stages; generated content fidelity remains unobserved."
          },
          {
            "scope": "Aliases, mention indexes and FTS from source/page content",
            "assessment": "known",
            "findings": [
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-aliases",
                  "memory.md#mem-obj-mentions",
                  "memory.md#mem-obj-pages-fts"
                ],
                "note": "Resolution, counting and indexing compile source-derived access state."
              }
            ],
            "records": [
              "memory.md#mem-obj-aliases",
              "memory.md#mem-obj-mentions",
              "memory.md#mem-obj-pages-fts"
            ],
            "note": "These are derived access structures, not records of agent experience."
          },
          {
            "scope": "Locally generated Chroma embeddings and metadata",
            "assessment": "known",
            "findings": [
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-wiki-pages"
                ],
                "note": "Embedding the first 2000 page characters and storing associated metadata produces derived access state."
              }
            ],
            "records": [
              "memory.md#mem-obj-wiki-pages"
            ],
            "note": "Known embedding path is separate from restored embeddings."
          },
          {
            "scope": "Archive-restored pages, raw text, schema, histories, plans and vectors",
            "assessment": "partial",
            "findings": [
              {
                "value": "imported",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-archive-import",
                  "memory.md#mem-obj-wiki-pages"
                ],
                "note": "Restoration installs archive-supplied retained content directly."
              }
            ],
            "records": [
              "runtime.md#rt-rte-archive-import",
              "memory.md#mem-obj-wiki-pages"
            ],
            "note": "Archive origin establishes import, but not pre-archive authorship, embedding model/content or original admission."
          },
          {
            "scope": "Chat turn text and triage/lint diagnostic records",
            "assessment": "known",
            "findings": [
              {
                "value": "authored",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-history-read",
                  "memory.md#mem-obj-activity-log",
                  "memory.md#mem-rte-lint-retention"
                ],
                "note": "Caller/model/fixed answer text and model diagnostic reasons have identifiable immediate producers."
              },
              {
                "value": "trace-extracted",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-history-read",
                  "memory.md#mem-obj-activity-log",
                  "memory.md#mem-rte-lint-retention"
                ],
                "note": "Runtime records retain conversational turns and maintenance outcomes for later consumers."
              }
            ],
            "records": [
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-rte-history-read",
              "memory.md#mem-obj-activity-log",
              "memory.md#mem-rte-lint-retention"
            ],
            "note": "Raw recorded interaction and diagnostics are separated from the derived FAQ and saved-links projections."
          },
          {
            "scope": "Automatic FAQ wrapper and saved-links projection",
            "assessment": "known",
            "findings": [
              {
                "value": "trace-extracted",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-saved-links",
                  "runtime.md#rt-rte-chat-feedback",
                  "memory.md#mem-clm-chat-provenance"
                ],
                "note": "Answers and unresolved-ingestion events feed retained derived prose."
              },
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-saved-links",
                  "runtime.md#rt-rte-chat-feedback",
                  "memory.md#mem-clm-chat-provenance"
                ],
                "note": "Fixed wrappers, metadata/error shortening and status templates compile that prose."
              }
            ],
            "records": [
              "memory.md#mem-rte-saved-links",
              "runtime.md#rt-rte-chat-feedback",
              "memory.md#mem-clm-chat-provenance"
            ],
            "note": "These transformations consume interaction/failure records rather than establishing new source corroboration."
          },
          {
            "scope": "Submitted replacement text and initial provenance of imported embeddings",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-rte-storage-write",
              "memory.md#mem-rte-manual-save",
              "memory.md#mem-obj-wiki-pages"
            ],
            "note": "Generic caller identity and supplied embeddings do not establish original authorship or derivation. The known import path does not resolve earlier provenance."
          },
          {
            "scope": "Provider-hidden continuation/context state on the included model-call paths, if retained across invocations",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-chat-feedback",
              "runtime.md#rt-rte-plan-draft"
            ],
            "note": "The reports do not inspect provider-hidden checkpoints or context. They establish neither this alternative's existence nor its derivation path; it remains included as an unresolved alternative, not inferred provider memory."
          }
        ],
        "records": [
          "memory.md#mem-obj-raw",
          "memory.md#mem-obj-pages",
          "runtime.md#rt-rte-plan-draft",
          "memory.md#mem-obj-extractions",
          "runtime.md#rt-obj-page-plans",
          "epistemic.md#epi-obj-draft-content",
          "runtime.md#rt-obj-schema",
          "runtime.md#rt-rte-schema-bootstrap",
          "runtime.md#rt-rte-source-maintenance",
          "memory.md#mem-obj-aliases",
          "memory.md#mem-obj-mentions",
          "memory.md#mem-obj-pages-fts",
          "memory.md#mem-obj-wiki-pages",
          "runtime.md#rt-rte-archive-import",
          "memory.md#mem-obj-chat-messages",
          "memory.md#mem-rte-history-read",
          "memory.md#mem-obj-activity-log",
          "memory.md#mem-rte-lint-retention",
          "memory.md#mem-rte-saved-links",
          "runtime.md#rt-rte-chat-feedback",
          "memory.md#mem-clm-chat-provenance",
          "memory.md#mem-rte-storage-write",
          "memory.md#mem-rte-manual-save"
        ],
        "note": "Immediate acquisition, authored generation, deterministic compilation and trace derivation coexist. Pre-import provenance, direct replacement origin and hidden provider-state lineage remain unresolved."
      },
      "behavioral_authority": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Raw sources, extraction prose, existing pages, earlier draft summaries and chat history at later drafting/answering consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-raw",
                  "memory.md#mem-obj-extractions",
                  "memory.md#mem-obj-pages",
                  "runtime.md#rt-obj-page-plans",
                  "epistemic.md#epi-obj-draft-content",
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-history-read",
                  "runtime.md#rt-rte-plan-draft",
                  "runtime.md#rt-bap-wiki-answering"
                ],
                "note": "Retained text supplies evidence and context for subsequent generation."
              }
            ],
            "records": [
              "memory.md#mem-obj-raw",
              "memory.md#mem-obj-extractions",
              "memory.md#mem-obj-pages",
              "runtime.md#rt-obj-page-plans",
              "epistemic.md#epi-obj-draft-content",
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-rte-history-read",
              "runtime.md#rt-rte-plan-draft",
              "runtime.md#rt-bap-wiki-answering"
            ],
            "note": "This records supplied context/reference, not truth acceptance or model compliance."
          },
          {
            "scope": "Wiki and prior-version prose at explicit human/MCP readers",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-pages",
                  "runtime.md#rt-rte-mcp-read"
                ],
                "note": "Displayed or requested retained prose supplies reference material."
              }
            ],
            "records": [
              "memory.md#mem-obj-pages",
              "runtime.md#rt-rte-mcp-read"
            ],
            "note": "External agents receive requested tool results; their subsequent decisions remain outside the boundary."
          },
          {
            "scope": "Standing schema at later drafting model",
            "assessment": "known",
            "findings": [
              {
                "value": "instruction",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-schema",
                  "runtime.md#rt-rte-schema-bootstrap",
                  "runtime.md#rt-bap-schema-drafting"
                ],
                "note": "Loaded schema prose is explicitly supplied as conventions to follow."
              }
            ],
            "records": [
              "runtime.md#rt-obj-schema",
              "runtime.md#rt-rte-schema-bootstrap",
              "runtime.md#rt-bap-schema-drafting"
            ],
            "note": "The instruction request is wired; it does not enforce deterministic planning and actual compliance is unobserved."
          },
          {
            "scope": "FTS text, Chroma dense features and page title/summary/source-count/recency at query candidate selection",
            "assessment": "known",
            "findings": [
              {
                "value": "ranking",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-aliases",
                  "memory.md#mem-obj-mentions",
                  "memory.md#mem-obj-pages-fts",
                  "memory.md#mem-obj-wiki-pages",
                  "runtime.md#rt-rte-chat-feedback"
                ],
                "note": "Retained text/features influence relative page priority in lexical, vector and hybrid/model selection."
              }
            ],
            "records": [
              "memory.md#mem-obj-aliases",
              "memory.md#mem-obj-mentions",
              "memory.md#mem-obj-pages-fts",
              "memory.md#mem-obj-wiki-pages",
              "runtime.md#rt-rte-chat-feedback"
            ],
            "note": "Fixed scoring gives retained inputs ranking force even though no retained learned ranking policy is established."
          },
          {
            "scope": "Aliases, mention counts, plan/session IDs, settings and progress at subsequent resolution/planning/retry/startup consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "routing",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-aliases",
                  "memory.md#mem-obj-mentions",
                  "memory.md#mem-obj-pages-fts",
                  "runtime.md#rt-obj-page-plans",
                  "epistemic.md#epi-obj-draft-content",
                  "memory.md#mem-obj-activity-log",
                  "memory.md#mem-rte-lint-retention",
                  "runtime.md#rt-rte-session-compile"
                ],
                "note": "Retained identity/count/status/timing state selects operations, destinations or subsequent work."
              }
            ],
            "records": [
              "memory.md#mem-obj-aliases",
              "memory.md#mem-obj-mentions",
              "memory.md#mem-obj-pages-fts",
              "runtime.md#rt-obj-page-plans",
              "epistemic.md#epi-obj-draft-content",
              "memory.md#mem-obj-activity-log",
              "memory.md#mem-rte-lint-retention",
              "runtime.md#rt-rte-session-compile"
            ],
            "note": "Only state with a recorded later operational consumer is included, not all database metadata."
          },
          {
            "scope": "Pending-plan status and source/provenance dependencies at approval and cleanup",
            "assessment": "known",
            "findings": [
              {
                "value": "validation",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-page-plans",
                  "epistemic.md#epi-obj-draft-content",
                  "memory.md#mem-rte-withdrawal-cleanup",
                  "runtime.md#rt-rte-source-maintenance",
                  "epistemic.md#epi-rte-zombie-cleanup",
                  "runtime.md#rt-rte-draft-approval"
                ],
                "note": "Retained state/dependencies determine admissibility or conformity to an operational predicate."
              },
              {
                "value": "enforcement",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-page-plans",
                  "epistemic.md#epi-obj-draft-content",
                  "memory.md#mem-rte-withdrawal-cleanup",
                  "runtime.md#rt-rte-source-maintenance",
                  "epistemic.md#epi-rte-zombie-cleanup",
                  "runtime.md#rt-rte-draft-approval"
                ],
                "note": "State/dependency guards permit or block installation, or remove availability."
              }
            ],
            "records": [
              "runtime.md#rt-obj-page-plans",
              "epistemic.md#epi-obj-draft-content",
              "memory.md#mem-rte-withdrawal-cleanup",
              "runtime.md#rt-rte-source-maintenance",
              "epistemic.md#epi-rte-zombie-cleanup",
              "runtime.md#rt-rte-draft-approval"
            ],
            "note": "Fixed pending-state and dependency predicates have both criterion and veto consequences. These are operational, not factual acceptance criteria."
          },
          {
            "scope": "Archived-source status at default page-index selection",
            "assessment": "known",
            "findings": [
              {
                "value": "enforcement",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-withdrawal-cleanup",
                  "runtime.md#rt-rte-source-maintenance",
                  "epistemic.md#epi-rte-zombie-cleanup"
                ],
                "note": "All-archived source status excludes affected pages from default indexes."
              }
            ],
            "records": [
              "memory.md#mem-rte-withdrawal-cleanup",
              "runtime.md#rt-rte-source-maintenance",
              "epistemic.md#epi-rte-zombie-cleanup"
            ],
            "note": "Default suppression is enforced; direct-ID prohibition and semantic removal are not established."
          },
          {
            "scope": "Saved-links failure records at projection and derived page at later wiki/query consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "learning",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-saved-links"
                ],
                "note": "Retained failure experience feeds a durable page update that can shape later context."
              },
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-saved-links"
                ],
                "note": "Generated failure/status prose is later readable and retrievable."
              }
            ],
            "records": [
              "memory.md#mem-rte-saved-links"
            ],
            "note": "Update-consumer force and downstream reference force are distinct."
          },
          {
            "scope": "Recorded answer at automatic FAQ proposal update and pending review consumer",
            "assessment": "partial",
            "findings": [
              {
                "value": "learning",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-chat-feedback",
                  "memory.md#mem-clm-chat-provenance"
                ],
                "note": "Interaction experience feeds automatic durable FAQ candidate construction."
              },
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-chat-feedback",
                  "memory.md#mem-clm-chat-provenance"
                ],
                "note": "The retained candidate supplies content to later review/approval."
              }
            ],
            "records": [
              "runtime.md#rt-rte-chat-feedback",
              "memory.md#mem-clm-chat-provenance"
            ],
            "note": "The durable proposal route is wired. Ordinary page-based adoption fails; exceptional empty/coincident-ID admission must not upgrade it to a complete ordinary wiki cycle."
          },
          {
            "scope": "Triage/lint findings and reasons at operator/sidebar display",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-activity-log",
                  "memory.md#mem-rte-lint-retention",
                  "epistemic.md#epi-rte-triage-disposition"
                ],
                "note": "Retained reasons/findings inform later operator inspection without automatically revising challenged prose."
              }
            ],
            "records": [
              "memory.md#mem-obj-activity-log",
              "memory.md#mem-rte-lint-retention",
              "epistemic.md#epi-rte-triage-disposition"
            ],
            "note": "Advisory diagnostic force is distinct from the planner consuming the immediate triage result."
          },
          {
            "scope": "Imported vector documents and unconsumed metadata beyond recorded readers",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-wiki-pages",
              "runtime.md#rt-rte-archive-import"
            ],
            "note": "The records establish access/display/backup roles but not every actual consumer or behavioral force of restored payloads; no authority is inferred for unconsumed metadata."
          },
          {
            "scope": "Provider-hidden continuation/context state on the included model-call paths, if retained across invocations",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-chat-feedback",
              "runtime.md#rt-rte-plan-draft"
            ],
            "note": "The reports do not inspect provider-hidden checkpoints or context. They establish neither this alternative's existence nor its consumer and effect; it remains included as an unresolved alternative, not inferred provider memory."
          }
        ],
        "records": [
          "memory.md#mem-obj-raw",
          "memory.md#mem-obj-extractions",
          "memory.md#mem-obj-pages",
          "runtime.md#rt-obj-page-plans",
          "epistemic.md#epi-obj-draft-content",
          "memory.md#mem-obj-chat-messages",
          "memory.md#mem-rte-history-read",
          "runtime.md#rt-rte-plan-draft",
          "runtime.md#rt-bap-wiki-answering",
          "runtime.md#rt-rte-mcp-read",
          "runtime.md#rt-obj-schema",
          "runtime.md#rt-rte-schema-bootstrap",
          "runtime.md#rt-bap-schema-drafting",
          "memory.md#mem-obj-aliases",
          "memory.md#mem-obj-mentions",
          "memory.md#mem-obj-pages-fts",
          "memory.md#mem-obj-wiki-pages",
          "runtime.md#rt-rte-chat-feedback",
          "memory.md#mem-obj-activity-log",
          "memory.md#mem-rte-lint-retention",
          "runtime.md#rt-rte-session-compile",
          "memory.md#mem-rte-withdrawal-cleanup",
          "runtime.md#rt-rte-source-maintenance",
          "epistemic.md#epi-rte-zombie-cleanup",
          "runtime.md#rt-rte-draft-approval",
          "memory.md#mem-rte-saved-links",
          "memory.md#mem-clm-chat-provenance",
          "epistemic.md#epi-rte-triage-disposition",
          "runtime.md#rt-rte-archive-import"
        ],
        "note": "Authority is assigned at named consumers: context, conventions, ranking, routing, validation, enforcement and trace-fed updates coexist. No finding claims observed compliance, epistemic acceptance or improved capacity; imported/hidden alternative consumers remain unresolved."
      },
      "write_agency": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Conversion/extraction/index/alias/mention writes and automatic ordinary compile admission",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-raw",
                  "memory.md#mem-obj-extractions",
                  "memory.md#mem-obj-aliases",
                  "memory.md#mem-obj-mentions",
                  "memory.md#mem-obj-pages-fts",
                  "runtime.md#rt-rte-session-compile",
                  "runtime.md#rt-rte-draft-approval"
                ],
                "note": "Software/model admission retains derived state and auto-approved page prose without a per-content operator decision."
              }
            ],
            "records": [
              "memory.md#mem-obj-raw",
              "memory.md#mem-obj-extractions",
              "memory.md#mem-obj-aliases",
              "memory.md#mem-obj-mentions",
              "memory.md#mem-obj-pages-fts",
              "runtime.md#rt-rte-session-compile",
              "runtime.md#rt-rte-draft-approval"
            ],
            "note": "Starting compile or selecting sources is not approval of each resulting retained item."
          },
          {
            "scope": "Schema bootstrap, vector upsert/backfill and saved-links regeneration",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-schema",
                  "runtime.md#rt-rte-schema-bootstrap",
                  "memory.md#mem-obj-wiki-pages",
                  "memory.md#mem-rte-saved-links"
                ],
                "note": "Software installs generated guidance, vector state and deterministic trace projection."
              }
            ],
            "records": [
              "runtime.md#rt-obj-schema",
              "runtime.md#rt-rte-schema-bootstrap",
              "memory.md#mem-obj-wiki-pages",
              "memory.md#mem-rte-saved-links"
            ],
            "note": "These mechanisms automatically accept nonempty/structurally valid output or execute fixed projection; no per-item semantic approval is recorded."
          },
          {
            "scope": "Chat turn storage and automatic FAQ proposal creation",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-history-read",
                  "runtime.md#rt-rte-chat-feedback",
                  "memory.md#mem-clm-chat-provenance"
                ],
                "note": "Questions/answers and the retrieved-count-triggered pending draft are retained by code."
              }
            ],
            "records": [
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-rte-history-read",
              "runtime.md#rt-rte-chat-feedback",
              "memory.md#mem-clm-chat-provenance"
            ],
            "note": "Proposal insertion is automatic; later wiki installation is separately constrained."
          },
          {
            "scope": "Deletion-triggered surviving-page redraft and software cascade",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-withdrawal-cleanup",
                  "runtime.md#rt-rte-source-maintenance",
                  "epistemic.md#epi-rte-zombie-cleanup"
                ],
                "note": "Rules and generation directly admit maintenance effects without per-effect approval."
              }
            ],
            "records": [
              "memory.md#mem-rte-withdrawal-cleanup",
              "runtime.md#rt-rte-source-maintenance",
              "epistemic.md#epi-rte-zombie-cleanup"
            ],
            "note": "Caller initiation does not make each replacement-prose or cascade admission a human decision."
          },
          {
            "scope": "Shipped pending-draft approve/reject and Save to wiki human-facing decision paths",
            "assessment": "known",
            "findings": [
              {
                "value": "manual",
                "basis": "afforded",
                "records": [
                  "runtime.md#rt-rte-draft-approval",
                  "memory.md#mem-rte-manual-save"
                ],
                "note": "A human-facing save/approval route allows an explicit decision supplying or approving retained content."
              }
            ],
            "records": [
              "runtime.md#rt-rte-draft-approval",
              "memory.md#mem-rte-manual-save"
            ],
            "note": "The UI affords explicit human content selection or approval, not proof that any API invocation came from a reviewing human."
          },
          {
            "scope": "Actual approval/save caller, archive-supplied contents and direct file replacement",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-draft-approval",
              "memory.md#mem-rte-manual-save",
              "runtime.md#rt-rte-archive-import",
              "memory.md#mem-rte-storage-write"
            ],
            "note": "The records identify caller control and fixed guards, not whether a human made the explicit content decision. Actual manual versus software-controlled admission cannot be determined from generic caller identity."
          },
          {
            "scope": "Provider-hidden continuation/context state on the included model-call paths, if retained across invocations",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-chat-feedback",
              "runtime.md#rt-rte-plan-draft"
            ],
            "note": "The reports do not inspect provider-hidden checkpoints or context. They establish neither this alternative's existence nor its admission control; it remains included as an unresolved alternative, not inferred provider memory."
          }
        ],
        "records": [
          "memory.md#mem-obj-raw",
          "memory.md#mem-obj-extractions",
          "memory.md#mem-obj-aliases",
          "memory.md#mem-obj-mentions",
          "memory.md#mem-obj-pages-fts",
          "runtime.md#rt-rte-session-compile",
          "runtime.md#rt-rte-draft-approval",
          "runtime.md#rt-obj-schema",
          "runtime.md#rt-rte-schema-bootstrap",
          "memory.md#mem-obj-wiki-pages",
          "memory.md#mem-rte-saved-links",
          "memory.md#mem-obj-chat-messages",
          "memory.md#mem-rte-history-read",
          "runtime.md#rt-rte-chat-feedback",
          "memory.md#mem-clm-chat-provenance",
          "memory.md#mem-rte-withdrawal-cleanup",
          "runtime.md#rt-rte-source-maintenance",
          "epistemic.md#epi-rte-zombie-cleanup",
          "memory.md#mem-rte-manual-save",
          "runtime.md#rt-rte-archive-import",
          "memory.md#mem-rte-storage-write",
          "runtime.md#rt-rte-plan-draft"
        ],
        "note": "Automatic admission is wired on several independent mechanisms; explicit human admission is afforded, not observed or universally attributable at the API. Caller-driven restoration/replacement and hidden state remain unresolved."
      },
      "curation_operations": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Earlier-layer draft-summary reduction and saved-links description/error reduction",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-plan-draft",
                  "memory.md#mem-rte-saved-links"
                ],
                "note": "Selected earlier drafts become reduced summary context; stored failure descriptions/errors become shortened page descriptions."
              }
            ],
            "records": [
              "runtime.md#rt-rte-plan-draft",
              "memory.md#mem-rte-saved-links"
            ],
            "note": "These implemented reductions operate on retained draft/trace content even if the originals remain stored."
          },
          {
            "scope": "Requested source synthesis and coherent wiki updates",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "afforded",
                "records": [
                  "runtime.md#rt-rte-plan-draft",
                  "epistemic.md#epi-obj-draft-content"
                ],
                "note": "Drafting requests a reduced, coherent account of existing source claims."
              }
            ],
            "records": [
              "runtime.md#rt-rte-plan-draft",
              "epistemic.md#epi-obj-draft-content"
            ],
            "note": "The prompt requests reduction across retained source content; generated semantic compliance is not recorded."
          },
          {
            "scope": "Existing-page drafting and deletion redraft",
            "assessment": "known",
            "findings": [
              {
                "value": "evolve",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-plan-draft",
                  "runtime.md#rt-rte-source-maintenance",
                  "memory.md#mem-obj-pages"
                ],
                "note": "Existing page content can be updated or replaced by a newly admitted redraft."
              }
            ],
            "records": [
              "runtime.md#rt-rte-plan-draft",
              "runtime.md#rt-rte-source-maintenance",
              "memory.md#mem-obj-pages"
            ],
            "note": "Installed replacement revises an existing entry. Fidelity and semantic deletion remain unobserved."
          },
          {
            "scope": "Historical mention-threshold page creation",
            "assessment": "known",
            "findings": [
              {
                "value": "promote",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-mentions",
                  "runtime.md#rt-rte-plan-draft"
                ],
                "note": "Historical thresholds raise accumulated source mentions into standalone wiki pages."
              }
            ],
            "records": [
              "memory.md#mem-obj-mentions",
              "runtime.md#rt-rte-plan-draft"
            ],
            "note": "Retained mention evidence raises entities/concepts into their own page tier; frequency is not independent corroboration."
          },
          {
            "scope": "Archive suppression and rejected proposal retention",
            "assessment": "known",
            "findings": [
              {
                "value": "invalidate",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-withdrawal-cleanup",
                  "runtime.md#rt-rte-source-maintenance",
                  "epistemic.md#epi-rte-zombie-cleanup",
                  "runtime.md#rt-rte-draft-approval"
                ],
                "note": "Archival withdraws default query reliance; rejection withholds a retained pending proposal from installation."
              }
            ],
            "records": [
              "memory.md#mem-rte-withdrawal-cleanup",
              "runtime.md#rt-rte-source-maintenance",
              "epistemic.md#epi-rte-zombie-cleanup",
              "runtime.md#rt-rte-draft-approval"
            ],
            "note": "History/prose can remain while default current reliance or candidate installation is withheld."
          },
          {
            "scope": "Source/page/dependency deletion and projection removal",
            "assessment": "known",
            "findings": [
              {
                "value": "decay",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-withdrawal-cleanup",
                  "runtime.md#rt-rte-source-maintenance",
                  "epistemic.md#epi-rte-zombie-cleanup",
                  "memory.md#mem-rte-saved-links"
                ],
                "note": "Cleanup removes retained entries or their normal access state; resolved/dismissed failures leave the projection."
              }
            ],
            "records": [
              "memory.md#mem-rte-withdrawal-cleanup",
              "runtime.md#rt-rte-source-maintenance",
              "epistemic.md#epi-rte-zombie-cleanup",
              "memory.md#mem-rte-saved-links"
            ],
            "note": "Deleting operative lookup/content state is forgetting, not proven erasure of every semantic contribution or filesystem residue."
          },
          {
            "scope": "Saved-links empty-set assertion branch",
            "assessment": "known",
            "findings": [
              {
                "value": "synthesize",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-saved-links"
                ],
                "note": "The fixed empty template creates a claim absent from the retained inputs; this is not a model-extraction faithfulness defect."
              }
            ],
            "records": [
              "memory.md#mem-rte-saved-links"
            ],
            "note": "The canonical record inherits the reconciled epistemic empty-branch witness: dismissal can produce an imported-all assertion not present in or entailed by the failure records."
          },
          {
            "scope": "Generated extraction/wiki meaning, restored content history and generic replacement transformations",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-extractions",
              "runtime.md#rt-rte-archive-import",
              "memory.md#mem-rte-storage-write",
              "runtime.md#rt-rte-plan-draft"
            ],
            "note": "Actual paired generation inputs/outputs and pre-import transformation history are missing. Requested synthesis does not establish newly created claims, deduplication or every implemented curation operation."
          },
          {
            "scope": "Provider-hidden continuation/context state on the included model-call paths, if retained across invocations",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-chat-feedback",
              "runtime.md#rt-rte-plan-draft"
            ],
            "note": "The reports do not inspect provider-hidden checkpoints or context. They establish neither this alternative's existence nor its transformation; it remains included as an unresolved alternative, not inferred provider memory."
          }
        ],
        "records": [
          "runtime.md#rt-rte-plan-draft",
          "memory.md#mem-rte-saved-links",
          "epistemic.md#epi-obj-draft-content",
          "runtime.md#rt-rte-source-maintenance",
          "memory.md#mem-obj-pages",
          "memory.md#mem-obj-mentions",
          "memory.md#mem-rte-withdrawal-cleanup",
          "epistemic.md#epi-rte-zombie-cleanup",
          "runtime.md#rt-rte-draft-approval",
          "memory.md#mem-obj-extractions",
          "runtime.md#rt-rte-archive-import",
          "memory.md#mem-rte-storage-write",
          "runtime.md#rt-rte-chat-feedback"
        ],
        "note": "Consolidation, evolution, promotion, invalidation, forgetting and one deterministic synthesis branch have local warrants. Index rebuild/upsert and primary-key replacement alone do not add deduplication. Unresolved model, import and direct-write semantics prevent complete enumeration."
      },
      "read_back_direction": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Requested wiki/MCP/previous-version/history/diagnostic reads",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-pages",
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-history-read",
                  "memory.md#mem-obj-activity-log",
                  "memory.md#mem-rte-lint-retention",
                  "runtime.md#rt-rte-mcp-read"
                ],
                "note": "Humans, external clients and application readers request retained material and receive it."
              }
            ],
            "records": [
              "memory.md#mem-obj-pages",
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-rte-history-read",
              "memory.md#mem-obj-activity-log",
              "memory.md#mem-rte-lint-retention",
              "runtime.md#rt-rte-mcp-read"
            ],
            "note": "Exact ID or query lookup fulfills a consumer request; delivery of the response is not a second push."
          },
          {
            "scope": "Question-driven page retrieval and compile/source-ID data loading",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-chat-feedback",
                  "runtime.md#rt-rte-plan-draft",
                  "memory.md#mem-obj-raw",
                  "memory.md#mem-obj-extractions"
                ],
                "note": "A question or compile operation requests selected retained page/source/dossier material."
              }
            ],
            "records": [
              "runtime.md#rt-rte-chat-feedback",
              "runtime.md#rt-rte-plan-draft",
              "memory.md#mem-obj-raw",
              "memory.md#mem-obj-extractions"
            ],
            "note": "The automatic selection inside a requested question response remains pull, as recorded in the memory account."
          },
          {
            "scope": "Automatic standing-schema, dossier and prior-layer/old-page context supply at drafting invocation",
            "assessment": "known",
            "findings": [
              {
                "value": "push",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-plan-draft",
                  "runtime.md#rt-obj-schema",
                  "runtime.md#rt-rte-schema-bootstrap",
                  "runtime.md#rt-obj-page-plans",
                  "epistemic.md#epi-obj-draft-content",
                  "memory.md#mem-obj-extractions"
                ],
                "note": "On a page-draft trigger, code injects saved conventions, selected extraction dossiers, applicable old prose and selected earlier-layer summaries into the new model call."
              }
            ],
            "records": [
              "runtime.md#rt-rte-plan-draft",
              "runtime.md#rt-obj-schema",
              "runtime.md#rt-rte-schema-bootstrap",
              "runtime.md#rt-obj-page-plans",
              "epistemic.md#epi-obj-draft-content",
              "memory.md#mem-obj-extractions"
            ],
            "note": "Separate upstream code reads from downstream model delivery: the drafting model does not request these remembered inputs; application context construction supplies them automatically."
          },
          {
            "scope": "Automatic stored-history supply to answer-model invocation",
            "assessment": "known",
            "findings": [
              {
                "value": "push",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-history-read",
                  "runtime.md#rt-rte-chat-feedback"
                ],
                "note": "After question insertion, the session selector supplies up to ten earliest retained turns to synthesis."
              }
            ],
            "records": [
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-rte-history-read",
              "runtime.md#rt-rte-chat-feedback"
            ],
            "note": "The user question requests an answer, not the selected old turns; code augments the answering invocation with stored role/content history. This is distinct from requested wiki retrieval."
          },
          {
            "scope": "Independent external injection and provider-hidden read-back",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-chat-feedback",
              "runtime.md#rt-rte-plan-draft",
              "runtime.md#rt-rte-mcp-read"
            ],
            "note": "No independent unsolicited external-agent delivery was supplied. Hidden provider continuation is uninspected; absence of a deployed push trace is not a bounded absence warrant."
          }
        ],
        "records": [
          "memory.md#mem-obj-pages",
          "memory.md#mem-obj-chat-messages",
          "memory.md#mem-rte-history-read",
          "memory.md#mem-obj-activity-log",
          "memory.md#mem-rte-lint-retention",
          "runtime.md#rt-rte-mcp-read",
          "runtime.md#rt-rte-chat-feedback",
          "runtime.md#rt-rte-plan-draft",
          "memory.md#mem-obj-raw",
          "memory.md#mem-obj-extractions",
          "runtime.md#rt-obj-schema",
          "runtime.md#rt-rte-schema-bootstrap",
          "runtime.md#rt-obj-page-plans",
          "epistemic.md#epi-obj-draft-content"
        ],
        "note": "Requested wiki/query returns are pull; automatic schema, historical-turn and prior-draft context augmentation are push operations at the model-consumption boundary. Unknown provider continuation prevents a complete direction inventory; no external unsolicited push is asserted."
      },
      "read_back_signal": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Standing schema push into each later page-draft call",
            "assessment": "known",
            "findings": [
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-schema",
                  "runtime.md#rt-rte-schema-bootstrap",
                  "runtime.md#rt-rte-plan-draft"
                ],
                "note": "The same available standing schema is supplied without query-specific identity or relevance matching."
              }
            ],
            "records": [
              "runtime.md#rt-obj-schema",
              "runtime.md#rt-rte-schema-bootstrap",
              "runtime.md#rt-rte-plan-draft"
            ],
            "note": "Trigger: page drafting. Selector input: schema file availability/existence. Selected part: the installed whole convention document; budget clipping does not create targeted relevance selection."
          },
          {
            "scope": "Existing-page context push into update drafting",
            "assessment": "known",
            "findings": [
              {
                "value": "identifier",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-plan-draft",
                  "memory.md#mem-obj-pages"
                ],
                "note": "The planned target identifies the old page content delivered to drafting."
              }
            ],
            "records": [
              "runtime.md#rt-rte-plan-draft",
              "memory.md#mem-obj-pages"
            ],
            "note": "Trigger: update plan. Selector input: target page ID. Selected part: that page's retained prose; identity matching is operative, not just an ID in a catalog."
          },
          {
            "scope": "Related earlier-layer draft summaries pushed into later drafting",
            "assessment": "known",
            "findings": [
              {
                "value": "identifier",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-plan-draft",
                  "runtime.md#rt-obj-page-plans",
                  "epistemic.md#epi-obj-draft-content"
                ],
                "note": "Related-plan identity selects which retained draft summaries cross into later calls."
              }
            ],
            "records": [
              "runtime.md#rt-rte-plan-draft",
              "runtime.md#rt-obj-page-plans",
              "epistemic.md#epi-obj-draft-content"
            ],
            "note": "Trigger: later-layer task. Selector input: related plan relationships/IDs. Selected part: persisted earlier draft summaries; layer order and availability separately bound supply."
          },
          {
            "scope": "Dossier augmentation at drafting",
            "assessment": "known",
            "findings": [
              {
                "value": "inferred-lexical",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-plan-draft",
                  "memory.md#mem-obj-extractions"
                ],
                "note": "TF-IDF relevance ranks/caps retained dossiers."
              },
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-plan-draft",
                  "memory.md#mem-obj-extractions"
                ],
                "note": "Recency fallback and comparison bypass supply dossiers without targeted relevance on those branches."
              }
            ],
            "records": [
              "runtime.md#rt-rte-plan-draft",
              "memory.md#mem-obj-extractions"
            ],
            "note": "Trigger: page drafting. Selector input: page relevance against source extraction dossiers. Selected part: capped dossier material, distinct from the separately supplied raw-source list."
          },
          {
            "scope": "Chat-history context push",
            "assessment": "known",
            "findings": [
              {
                "value": "identifier",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-history-read"
                ],
                "note": "Session identity selects the delivered stored conversation."
              },
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-rte-history-read"
                ],
                "note": "Chronological limit/window filtering further bounds the selected turns without semantic targeting."
              }
            ],
            "records": [
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-rte-history-read"
            ],
            "note": "Trigger: next question. Selector input: session equality, ascending timestamp, LIMIT 11 and removal of final returned row. Selected part: role/content of up to ten earliest rows, not citation metadata or a summary."
          },
          {
            "scope": "Signals of provider-hidden continuation/read-back",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-chat-feedback",
              "runtime.md#rt-rte-plan-draft"
            ],
            "note": "Provider checkpoint forms, triggers and selectors were not inspected. Known local push selectors cannot establish these alternative signals or make the axis pull-only inapplicable."
          }
        ],
        "records": [
          "runtime.md#rt-obj-schema",
          "runtime.md#rt-rte-schema-bootstrap",
          "runtime.md#rt-rte-plan-draft",
          "memory.md#mem-obj-pages",
          "runtime.md#rt-obj-page-plans",
          "epistemic.md#epi-obj-draft-content",
          "memory.md#mem-obj-extractions",
          "memory.md#mem-obj-chat-messages",
          "memory.md#mem-rte-history-read",
          "runtime.md#rt-rte-chat-feedback"
        ],
        "note": "Signals describe automatic context augmentation, not IDs on requested MCP pages. Query retrieval has recorded model, lexical and embedding ranking but remains a requested pull operation; it is not relabeled as push merely to add signal values. Provider alternatives remain unresolved."
      },
      "trace_learning": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Saved-links automatic failure-trace projection for later wiki/query consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-saved-links"
                ],
                "note": "Ingestion failure experience feeds automatically installed prose that can shape later work."
              }
            ],
            "records": [
              "memory.md#mem-rte-saved-links"
            ],
            "note": "Automatic trace-fed reduction creates a durable context artifact with later readable/retrievable consumers. No novel knowledge, parameter update or observed benefit is required."
          },
          {
            "scope": "Automatic chat-answer FAQ candidate and exceptional wiki-adoption paths",
            "assessment": "partial",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-chat-feedback",
                  "memory.md#mem-clm-chat-provenance",
                  "runtime.md#rt-rte-draft-approval"
                ],
                "note": "Recorded conversational answer content automatically becomes a durable FAQ candidate for later consumers."
              }
            ],
            "records": [
              "runtime.md#rt-rte-chat-feedback",
              "memory.md#mem-clm-chat-provenance",
              "runtime.md#rt-rte-draft-approval"
            ],
            "note": "Automatic durable proposal construction and later review are wired; ordinary disjoint page-ID provenance blocks wiki adoption. Only exceptional coincident IDs permit that approval path, not a universal ordinary compounding cycle."
          },
          {
            "scope": "Raw chat/lint/activity retention and their possible further updates",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-rte-history-read",
              "memory.md#mem-obj-activity-log",
              "memory.md#mem-rte-lint-retention"
            ],
            "note": "Raw logs and ordinary history replay alone do not establish the qualifying durable derived update. The reports establish diagnostics/replay but no automatic lint-to-new-guidance route; this is not a bounded negative for every possible trace-fed update."
          },
          {
            "scope": "Caller-selected answer saves and direct/archive replacement",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-rte-manual-save",
              "memory.md#mem-rte-storage-write",
              "runtime.md#rt-rte-archive-import"
            ],
            "note": "Supplied content need not be a stored answer; human versus automatic caller admission and original input provenance are unresolved. Manual save cannot be universally counted as automatic trace learning."
          },
          {
            "scope": "Ordinary source-derived pages/schema and possible trace-valued source inputs",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-raw",
              "memory.md#mem-obj-extractions",
              "runtime.md#rt-obj-schema",
              "runtime.md#rt-rte-schema-bootstrap",
              "runtime.md#rt-rte-plan-draft"
            ],
            "note": "Normal sources are recorded as imported knowledge, not agent-action traces. The actual open-ended source content and schema metadata origin do not establish a qualifying automatic trace chain for every included input."
          },
          {
            "scope": "Provider-hidden continuation/context state on the included model-call paths, if retained across invocations",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-chat-feedback",
              "runtime.md#rt-rte-plan-draft"
            ],
            "note": "The reports do not inspect provider-hidden checkpoints or context. They establish neither this alternative's existence nor its trace-fed update and later consumer; it remains included as an unresolved alternative, not inferred provider memory."
          }
        ],
        "records": [
          "memory.md#mem-rte-saved-links",
          "runtime.md#rt-rte-chat-feedback",
          "memory.md#mem-clm-chat-provenance",
          "runtime.md#rt-rte-draft-approval",
          "memory.md#mem-obj-chat-messages",
          "memory.md#mem-rte-history-read",
          "memory.md#mem-obj-activity-log",
          "memory.md#mem-rte-lint-retention",
          "memory.md#mem-rte-manual-save",
          "memory.md#mem-rte-storage-write",
          "runtime.md#rt-rte-archive-import",
          "memory.md#mem-obj-raw",
          "memory.md#mem-obj-extractions",
          "runtime.md#rt-obj-schema",
          "runtime.md#rt-rte-schema-bootstrap",
          "runtime.md#rt-rte-plan-draft"
        ],
        "note": "Two local positive routes survive, but ordinary FAQ wiki adoption, alternative caller content, open source origin and hidden provider updates remain unresolved. No system-wide or local no is asserted without bounded absence records; learning here does not assert improved capacity."
      },
      "trace_source": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Original failed-ingestion activity feeding saved-links projection",
            "assessment": "known",
            "findings": [
              {
                "value": "event-streams",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-saved-links"
                ],
                "note": "Recorded discrete ingestion failure/outcome events feed the status/failure page."
              }
            ],
            "records": [
              "memory.md#mem-rte-saved-links"
            ],
            "note": "Unresolved ingestion failures record discrete runtime outcomes with error/metadata fields; original failed documents themselves are not established trace sources."
          },
          {
            "scope": "Recorded conversational answer feeding automatic FAQ proposal",
            "assessment": "partial",
            "findings": [
              {
                "value": "session-logs",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-chat-feedback",
                  "memory.md#mem-obj-chat-messages",
                  "memory.md#mem-clm-chat-provenance"
                ],
                "note": "Agent chat turns supply the question/answer material compiled into the durable candidate."
              }
            ],
            "records": [
              "runtime.md#rt-rte-chat-feedback",
              "memory.md#mem-obj-chat-messages",
              "memory.md#mem-clm-chat-provenance"
            ],
            "note": "The original experience is conversational question/answer content; a FAQ wrapper does not change its origin to environmental events."
          },
          {
            "scope": "Origin of supplied manual-save/import/direct replacement content",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-rte-manual-save",
              "runtime.md#rt-rte-archive-import",
              "memory.md#mem-rte-storage-write"
            ],
            "note": "The supplied prose may not match a retained conversation and its original input is unverified. Session IDs/citations alone cannot establish a controlled trace-source value."
          },
          {
            "scope": "Open source inputs, raw diagnostic streams and hidden provider update inputs",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-raw",
              "memory.md#mem-obj-activity-log",
              "memory.md#mem-rte-lint-retention",
              "runtime.md#rt-rte-chat-feedback",
              "runtime.md#rt-rte-plan-draft"
            ],
            "note": "No qualifying automatic update chain is established for every ordinary source/diagnostic/provider alternative. Original trace content cannot be inferred from serialization or service role; tool-traces and trajectories are not asserted from error names alone."
          }
        ],
        "records": [
          "memory.md#mem-rte-saved-links",
          "runtime.md#rt-rte-chat-feedback",
          "memory.md#mem-obj-chat-messages",
          "memory.md#mem-clm-chat-provenance",
          "memory.md#mem-rte-manual-save",
          "runtime.md#rt-rte-archive-import",
          "memory.md#mem-rte-storage-write",
          "memory.md#mem-obj-raw",
          "memory.md#mem-obj-activity-log",
          "memory.md#mem-rte-lint-retention",
          "runtime.md#rt-rte-plan-draft"
        ],
        "note": "Known failure-event and conversational sources attach only to their qualifying local automatic updates. Unresolved qualifying writes and input provenance prevent a complete source inventory or inapplicability."
      }
    }
  }
}
---

# Kompl memory profile

## Comparison rationale

This profile classifies accepted records, not source files or a live instance. All positive implementation findings are local wiring or affordances; none are observations of operation, compliance, grounding or benefit. The local retained-object inventory comes from [MEM-OBJ-raw](memory.md#mem-obj-raw), [MEM-OBJ-extractions](memory.md#mem-obj-extractions), [MEM-OBJ-pages](memory.md#mem-obj-pages), [MEM-OBJ-wiki-pages](memory.md#mem-obj-wiki-pages) and their separate access, proposal and conversation records. Encoding does not determine storage substrate. Dense embeddings are parametric representations in vector storage, not updated MiniLM weights. Restored embeddings retain an imported path without resolved pre-import provenance.

The reconciliation supersedes the epistemic manual-save, lint and saved-links routes with [MEM-RTE-manual-save](memory.md#mem-rte-manual-save), [MEM-RTE-lint-retention](memory.md#mem-rte-lint-retention) and [MEM-RTE-saved-links](memory.md#mem-rte-saved-links). Classification cites those canonical destinations. In particular, the saved-links route retains the complementary empty-set witness: dismissal can produce an imported-all assertion not entailed by the retained failures. That implemented deterministic branch supports synthesis independently of model prose whose actual semantic transformation is unknown. The extraction bundle and its model-output part, and the plan control container and its prose payload, remain distinct valid referents; they are not superseded wholesale.

Read-back distinguishes upstream request from downstream augmentation. [RT-RTE-mcp-read](runtime.md#rt-rte-mcp-read) is requested delivery. Question-driven page retrieval in [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback) also remains pull. Automatically supplying saved conventions, target-page prose and earlier-layer draft summaries to a drafting model is a separate context-augmentation operation on [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft); the model makes no memory request. Likewise, code adds old conversation turns to answer synthesis under [MEM-RTE-history-read](memory.md#mem-rte-history-read). Identity, relevance and coarse budget selectors are retained separately. Requested query ranking is not converted into unsolicited push merely because code selects and delivers pages.

The runtime and memory mechanisms now agree on earliest-row history selection and ordinary FAQ provenance failure. The reconciliation retains conflicts only about memory's characterization of an earlier runtime position. They do not prevent these bounded classifications: [MEM-RTE-history-read](memory.md#mem-rte-history-read) establishes replay selection without summary production; [MEM-CLM-chat-provenance](memory.md#mem-clm-chat-provenance) prevents treating ordinary pending FAQ creation as a universally wired wiki-compounding cycle. Empty-citation manual saves and coincident page/source IDs are exceptions, not repairs of ordinary automatic adoption.

Trace learning is assessed at automatic durable trace-fed writes, not at raw log storage or parameter training. [MEM-RTE-saved-links](memory.md#mem-rte-saved-links) has a concrete trace-to-page-to-later-consumer route. [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback) has an automatic trace-to-pending-candidate route with a later reviewer, while ordinary wiki installation is constrained. Learning authority at those update consumers and knowledge authority at the downstream page/candidate readers are separate paths. Neither establishes improved capacity or exercised self-improvement. Generic caller identity does not prove manual admission; the UI's explicit content-selection/review route affords it without resolving arbitrary API callers.

Every axis remains partial because local positives do not exhaust hidden continuation, supplied replacement provenance and other named included alternatives. Static weights are excluded from accumulated memory, not declared absent learning. No absence records warrant a global negative for trace learning, provider memory, or read-back. Generated schema rationale, actual paired model transformations, original imported embedding derivation and hidden checkpoint inputs are missing recorded facts; no source understanding is substituted for them.

Source-read log: none. This worker read only the supplied invocation, contracts and pinned members; it performed no additional target-source reads.

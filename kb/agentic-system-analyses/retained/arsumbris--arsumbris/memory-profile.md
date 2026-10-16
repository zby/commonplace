---
{
  "type": "agentic-system-analyses/types/agentic-system-memory-profile.md",
  "description": "Arsumbris accumulated file knowledge, graph access, configuration reuse and opaque session/host memory alternatives at its documentary entry-repository boundary.",
  "run-id": "AAS-2026-10-15-arsumbris-a9be6bac297f-01",
  "source-identity": "https://github.com/arsumbris/arsumbris",
  "reviewed-boundary": "716bb14f2bf50e249d414525c8e07c50478fc786",
  "memory-comparison": {
    "version": 2,
    "scope": "Changed repository knowledge and types, indexed opaque assets, their live graph access structure, device metadata reused by later merges/launches, declared session ledger and saved pane/viewer state, governed write metadata, and unresolved accumulated outputs of ingestion/computed or changed guidance. Includes their admission, maintenance and later-consumer routes. Excludes unchanged shipped instructions/profile policy, executable platform code as such, ordinary transient UI coordination and external harness/provider weights; absent sibling implementations limit all opaque alternatives rather than establishing absence.",
    "axes": {
      "storage_substrate": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Changed repository knowledge, symbolic fields, type definitions and indexed assets",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-knowledge-files",
                  "memory.md#mem-obj-type-definitions"
                ],
                "note": "Knowledge and definitions persist as repository files."
              },
              {
                "value": "repo",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-knowledge-files",
                  "memory.md#mem-obj-type-definitions"
                ],
                "note": "Git-tracked repositories organize the retained knowledge."
              }
            ],
            "records": [
              "memory.md#mem-obj-knowledge-files",
              "memory.md#mem-obj-type-definitions"
            ],
            "note": "The durable substrate is Git-tracked files, including opaque asset payloads; their encoding does not change storage."
          },
          {
            "scope": "File-derived live graph and access index",
            "assessment": "known",
            "findings": [
              {
                "value": "graph",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-live-graph",
                  "memory.md#mem-rte-graph-reuse"
                ],
                "note": "Mounted files become a relational typed graph."
              },
              {
                "value": "in-memory",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-live-graph",
                  "memory.md#mem-rte-graph-reuse"
                ],
                "note": "The graph is explicitly held in memory."
              }
            ],
            "records": [
              "memory.md#mem-obj-live-graph",
              "memory.md#mem-rte-graph-reuse"
            ],
            "note": "The documented graph is an in-memory access structure, not a separately established durable database."
          },
          {
            "scope": "Device access metadata",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-device-config",
                  "runtime.md#rt-rte-device-seeding"
                ],
                "note": "The seeder writes local YAML files."
              }
            ],
            "records": [
              "runtime.md#rt-obj-device-config",
              "runtime.md#rt-rte-device-seeding"
            ],
            "note": "Producer persistence is inspected; downstream host/engine storage contracts add no other substrate."
          },
          {
            "scope": "Session ledger backing",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-session-ledger"
            ],
            "note": "Appends are declared; no physical storage or durability contract identifies a controlled substrate."
          },
          {
            "scope": "Shared pane configuration and viewer-local state",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-host-edit",
              "memory.md#mem-obj-view-store"
            ],
            "note": "saveConfig promises persistence but exact storage is unspecified; viewStore lifetime and backing are opaque."
          },
          {
            "scope": "Computed context, source-note ingestion and governed stamp outputs",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-bap-profile-guidance",
              "epistemic.md#epi-rte-source-ingest",
              "epistemic.md#epi-obj-write-metadata",
              "epistemic.md#epi-rte-hook-lineage"
            ],
            "note": "Their existence or output labels do not resolve all retained payloads or backing stores. Source notes may join repository files, but their complete persistence chain is uninspected."
          }
        ],
        "records": [
          "memory.md#mem-obj-knowledge-files",
          "memory.md#mem-obj-type-definitions",
          "memory.md#mem-obj-live-graph",
          "memory.md#mem-rte-graph-reuse",
          "runtime.md#rt-obj-device-config",
          "runtime.md#rt-rte-device-seeding",
          "memory.md#mem-obj-session-ledger",
          "runtime.md#rt-rte-host-edit",
          "memory.md#mem-obj-view-store",
          "runtime.md#rt-bap-profile-guidance",
          "epistemic.md#epi-rte-source-ingest",
          "epistemic.md#epi-obj-write-metadata",
          "epistemic.md#epi-rte-hook-lineage"
        ],
        "note": "Documented file/graph substrates and implemented device files are resolved locally; ledger backing, viewer state, pane storage and computed/ingested alternatives remain unresolved."
      },
      "representational_form": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Knowledge Markdown bodies at human/agent readers",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-knowledge-files"
                ],
                "note": "Bodies can supply natural-language knowledge to later readers."
              }
            ],
            "records": [
              "memory.md#mem-obj-knowledge-files"
            ],
            "note": "Interpreted prose is separate from fields and references."
          },
          {
            "scope": "Knowledge fields/references, type rules and parsed graph structure",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-knowledge-files",
                  "memory.md#mem-obj-type-definitions",
                  "memory.md#mem-obj-live-graph",
                  "memory.md#mem-rte-graph-reuse"
                ],
                "note": "Fields, references, constraints and parsed relations have fixed consumer rules."
              }
            ],
            "records": [
              "memory.md#mem-obj-knowledge-files",
              "memory.md#mem-obj-type-definitions",
              "memory.md#mem-obj-live-graph",
              "memory.md#mem-rte-graph-reuse"
            ],
            "note": "Localized fields and fixed engine rules are symbolic; prose guidance inside types is not thereby a symbolic semantic check."
          },
          {
            "scope": "Device registry and path maps",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-device-config",
                  "runtime.md#rt-rte-device-seeding"
                ],
                "note": "Parsed mappings determine retained configuration."
              }
            ],
            "records": [
              "runtime.md#rt-obj-device-config",
              "runtime.md#rt-rte-device-seeding"
            ],
            "note": "The inspected merge consumer handles symbolic name/path associations."
          },
          {
            "scope": "Shared composition pool entries/references",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-host-edit"
                ],
                "note": "Pool entries and references arrange projection instances."
              }
            ],
            "records": [
              "runtime.md#rt-rte-host-edit"
            ],
            "note": "Documented saved configuration is symbolic, unlike opaque viewer state."
          },
          {
            "scope": "Session event envelope",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-session-ledger"
                ],
                "note": "The ledger is described as a symbolic sequence of events."
              }
            ],
            "records": [
              "memory.md#mem-obj-session-ledger"
            ],
            "note": "Only the event sequence is classified; payload form is unresolved."
          },
          {
            "scope": "Governed write metadata envelope",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "claimed",
                "records": [
                  "epistemic.md#epi-obj-write-metadata",
                  "epistemic.md#epi-rte-hook-lineage"
                ],
                "note": "A stamper folds metadata into writes."
              }
            ],
            "records": [
              "epistemic.md#epi-obj-write-metadata",
              "epistemic.md#epi-rte-hook-lineage"
            ],
            "note": "Symbolic metadata is declared; concrete keys and interpretation are not supplied."
          },
          {
            "scope": "Indexed media/assets, ledger payloads, viewer store, computed injection and ingested note payloads",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-knowledge-files",
              "memory.md#mem-obj-session-ledger",
              "memory.md#mem-obj-view-store",
              "runtime.md#rt-bap-profile-guidance",
              "epistemic.md#epi-rte-source-ingest"
            ],
            "note": "Opaque payloads cannot be classified from an index entry or a launch/display description. Static skill instruction bodies are excluded from accumulated memory; changed guidance consumption remains unresolved."
          }
        ],
        "records": [
          "memory.md#mem-obj-knowledge-files",
          "memory.md#mem-obj-type-definitions",
          "memory.md#mem-obj-live-graph",
          "memory.md#mem-rte-graph-reuse",
          "runtime.md#rt-obj-device-config",
          "runtime.md#rt-rte-device-seeding",
          "runtime.md#rt-rte-host-edit",
          "memory.md#mem-obj-session-ledger",
          "epistemic.md#epi-obj-write-metadata",
          "epistemic.md#epi-rte-hook-lineage",
          "memory.md#mem-obj-view-store",
          "runtime.md#rt-bap-profile-guidance",
          "epistemic.md#epi-rte-source-ingest"
        ],
        "note": "Text and symbolic operative parts are distinguished; opaque media, event payloads and local/generated state prevent complete coverage. No model weights are included merely because a harness consumes knowledge."
      },
      "lineage": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Type-definition authoring",
            "assessment": "known",
            "findings": [
              {
                "value": "authored",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-type-definitions"
                ],
                "note": "Definitions are explicitly authored in the YAML typing language."
              }
            ],
            "records": [
              "memory.md#mem-obj-type-definitions"
            ],
            "note": "Users define repository types; this does not resolve authorship of every knowledge body."
          },
          {
            "scope": "File-to-live-graph derivation",
            "assessment": "known",
            "findings": [
              {
                "value": "other-compiled",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-live-graph",
                  "memory.md#mem-rte-graph-reuse"
                ],
                "note": "Parsing and change-driven indexing derive the graph from files."
              }
            ],
            "records": [
              "memory.md#mem-obj-live-graph",
              "memory.md#mem-rte-graph-reuse"
            ],
            "note": "The graph is compiled by indexing files, not by abstracting session experience."
          },
          {
            "scope": "Device registry acquisition and merge/render",
            "assessment": "known",
            "findings": [
              {
                "value": "imported",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-device-config",
                  "runtime.md#rt-rte-device-seeding",
                  "epistemic.md#epi-obj-registry-paths"
                ],
                "note": "Existing registry and manifest associations enter the merge."
              },
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-device-config",
                  "runtime.md#rt-rte-device-seeding",
                  "epistemic.md#epi-obj-registry-paths"
                ],
                "note": "Discovery, parsing, deterministic selection and rendering generate registry output."
              }
            ],
            "records": [
              "runtime.md#rt-obj-device-config",
              "runtime.md#rt-rte-device-seeding",
              "epistemic.md#epi-obj-registry-paths"
            ],
            "note": "The inspected path imports existing mappings/manifests and compiles selected output; parser lossiness prevents a lossless-copy claim."
          },
          {
            "scope": "Raw session event acquisition",
            "assessment": "known",
            "findings": [
              {
                "value": "imported",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-session-ledger",
                  "epistemic.md#epi-rte-hook-lineage"
                ],
                "note": "Pipeline events are appended to the session ledger."
              }
            ],
            "records": [
              "memory.md#mem-obj-session-ledger",
              "epistemic.md#epi-rte-hook-lineage"
            ],
            "note": "This is acquisition of events, not extraction of a durable behavior-shaping lesson."
          },
          {
            "scope": "Initial knowledge and assets; pane/viewer content; stamped metadata; computed context; source-note outputs",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-knowledge-files",
              "runtime.md#rt-rte-host-edit",
              "memory.md#mem-obj-view-store",
              "epistemic.md#epi-obj-write-metadata",
              "epistemic.md#epi-rte-hook-lineage",
              "runtime.md#rt-bap-profile-guidance",
              "epistemic.md#epi-rte-source-ingest"
            ],
            "note": "Initial provenance, concrete producers and semantic derivation paths are unspecified. Package names alone cannot establish consolidation, synthesis or trace extraction."
          }
        ],
        "records": [
          "memory.md#mem-obj-type-definitions",
          "memory.md#mem-obj-live-graph",
          "memory.md#mem-rte-graph-reuse",
          "runtime.md#rt-obj-device-config",
          "runtime.md#rt-rte-device-seeding",
          "epistemic.md#epi-obj-registry-paths",
          "memory.md#mem-obj-session-ledger",
          "epistemic.md#epi-rte-hook-lineage",
          "memory.md#mem-obj-knowledge-files",
          "runtime.md#rt-rte-host-edit",
          "memory.md#mem-obj-view-store",
          "epistemic.md#epi-obj-write-metadata",
          "runtime.md#rt-bap-profile-guidance",
          "epistemic.md#epi-rte-source-ingest"
        ],
        "note": "Known authoring, indexing and configuration derivations coexist with unspecified initial content provenance and opaque ingest/context branches."
      },
      "behavioral_authority": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Changed knowledge prose at later graph/UI/agent readers",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-knowledge-files",
                  "memory.md#mem-obj-live-graph",
                  "memory.md#mem-rte-graph-reuse"
                ],
                "note": "Later file/graph readers receive reference content."
              }
            ],
            "records": [
              "memory.md#mem-obj-knowledge-files",
              "memory.md#mem-obj-live-graph",
              "memory.md#mem-rte-graph-reuse"
            ],
            "note": "Retrieval/rendering supplies content without warranting its truth or model compliance."
          },
          {
            "scope": "Retained type constraints at engine diagnostics",
            "assessment": "known",
            "findings": [
              {
                "value": "validation",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-type-definitions",
                  "epistemic.md#epi-rte-type-diagnostics",
                  "runtime.md#rt-clm-diagnostic-saves"
                ],
                "note": "Engine type rules assess fields, references and body constraints."
              }
            ],
            "records": [
              "memory.md#mem-obj-type-definitions",
              "epistemic.md#epi-rte-type-diagnostics",
              "runtime.md#rt-clm-diagnostic-saves"
            ],
            "note": "Validation assesses structural conformity; diagnostics do not veto save/read."
          },
          {
            "scope": "Type and runtime metadata at extension discovery/load",
            "assessment": "known",
            "findings": [
              {
                "value": "routing",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-type-definitions",
                  "runtime.md#rt-rte-extension-load"
                ],
                "note": "Type queries and entry metadata select executable extensions."
              },
              {
                "value": "validation",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-type-definitions",
                  "runtime.md#rt-rte-extension-load"
                ],
                "note": "Runtime metadata and contract versions determine eligibility."
              },
              {
                "value": "enforcement",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-type-definitions",
                  "runtime.md#rt-rte-extension-load"
                ],
                "note": "The declared loader refuses incompatible or missing/ambiguous metadata."
              }
            ],
            "records": [
              "memory.md#mem-obj-type-definitions",
              "runtime.md#rt-rte-extension-load"
            ],
            "note": "These effects concern subsequently used definitions, not the mere presence of static SDK code."
          },
          {
            "scope": "Device registry rows at subsequent seeder merge",
            "assessment": "known",
            "findings": [
              {
                "value": "routing",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-device-config",
                  "runtime.md#rt-rte-device-seeding"
                ],
                "note": "Previously retained name/path mappings select locations kept in the next configuration."
              }
            ],
            "records": [
              "runtime.md#rt-obj-device-config",
              "runtime.md#rt-rte-device-seeding"
            ],
            "note": "Preserved mappings affect later discovery/merge output; this consumer is implemented independently of the documented launcher."
          },
          {
            "scope": "Device locations/tool paths and saved composition at documented host/engine consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "routing",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-obj-device-config",
                  "runtime.md#rt-rte-device-seeding",
                  "runtime.md#rt-rte-host-edit"
                ],
                "note": "Paths select repositories/tools/templates; composition references select projection instances."
              }
            ],
            "records": [
              "runtime.md#rt-obj-device-config",
              "runtime.md#rt-rte-device-seeding",
              "runtime.md#rt-rte-host-edit"
            ],
            "note": "Launch/resolution and UI arrangement are documentary consumers, not inspected execution."
          },
          {
            "scope": "Ledger, stamp payloads, viewer store, source notes and computed or changed guidance",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-session-ledger",
              "epistemic.md#epi-obj-write-metadata",
              "epistemic.md#epi-rte-hook-lineage",
              "memory.md#mem-obj-view-store",
              "epistemic.md#epi-rte-source-ingest",
              "runtime.md#rt-bap-profile-guidance"
            ],
            "note": "Ledger replay is not established; metadata interpretation and viewer lifetime are unknown. Guidance instruction intent is documented, but no changed-guidance-to-later-invocation chain establishes accumulated instruction memory. No learning or ranking authority follows from mere retention."
          }
        ],
        "records": [
          "memory.md#mem-obj-knowledge-files",
          "memory.md#mem-obj-live-graph",
          "memory.md#mem-rte-graph-reuse",
          "memory.md#mem-obj-type-definitions",
          "epistemic.md#epi-rte-type-diagnostics",
          "runtime.md#rt-clm-diagnostic-saves",
          "runtime.md#rt-rte-extension-load",
          "runtime.md#rt-obj-device-config",
          "runtime.md#rt-rte-device-seeding",
          "runtime.md#rt-rte-host-edit",
          "memory.md#mem-obj-session-ledger",
          "epistemic.md#epi-obj-write-metadata",
          "epistemic.md#epi-rte-hook-lineage",
          "memory.md#mem-obj-view-store",
          "epistemic.md#epi-rte-source-ingest",
          "runtime.md#rt-bap-profile-guidance"
        ],
        "note": "Each positive names a consumer and force; opaque payload consumers and later context delivery prevent a complete union. Static profile/tool policy is not counted as accumulated memory."
      },
      "write_agency": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Mediator admission and model-supplied overwrite on governed tool path",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-mediated-action"
                ],
                "note": "Software/model admission on the allow/deny route is automatic."
              }
            ],
            "records": [
              "runtime.md#rt-rte-mediated-action"
            ],
            "note": "The model proposes replacement text and software permits/denies it without an established per-content operator decision; ask is assessed separately."
          },
          {
            "scope": "Direct human file editing branch",
            "assessment": "known",
            "findings": [
              {
                "value": "manual",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-live-graph",
                  "memory.md#mem-rte-graph-reuse",
                  "runtime.md#rt-rte-host-edit"
                ],
                "note": "Explicit human text editing supplies the retained content."
              }
            ],
            "records": [
              "memory.md#mem-obj-live-graph",
              "memory.md#mem-rte-graph-reuse",
              "runtime.md#rt-rte-host-edit"
            ],
            "note": "This branch is limited to a human supplying/editing text, not every projection-generated change or agent launch."
          },
          {
            "scope": "Change-driven graph update",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-live-graph",
                  "memory.md#mem-rte-graph-reuse"
                ],
                "note": "File changes trigger automatic graph updates."
              }
            ],
            "records": [
              "memory.md#mem-obj-live-graph",
              "memory.md#mem-rte-graph-reuse"
            ],
            "note": "Code indexes admitted file changes without a separate human decision for each indexed part."
          },
          {
            "scope": "Device registry discovery/merge admission",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-device-config",
                  "runtime.md#rt-rte-device-seeding"
                ],
                "note": "Code selects and merges configuration entries after caller opt-in."
              }
            ],
            "records": [
              "runtime.md#rt-obj-device-config",
              "runtime.md#rt-rte-device-seeding"
            ],
            "note": "--write authorizes the run, not each discovered mapping; entry selection is deterministic."
          },
          {
            "scope": "Session observation append",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-session-ledger",
                  "runtime.md#rt-rte-mediated-action"
                ],
                "note": "The pipeline admits events to the ledger automatically."
              }
            ],
            "records": [
              "memory.md#mem-obj-session-ledger",
              "runtime.md#rt-rte-mediated-action"
            ],
            "note": "The observe stage appends pipeline events rather than awaiting content approval."
          },
          {
            "scope": "ask approval, arbitrary projection/filesystem writers, initial content, saved/viewer state and ingest/stamp/context transforms",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-mediated-action",
              "runtime.md#rt-rte-host-edit",
              "memory.md#mem-obj-view-store",
              "memory.md#mem-obj-knowledge-files",
              "epistemic.md#epi-rte-source-ingest",
              "epistemic.md#epi-obj-write-metadata",
              "epistemic.md#epi-rte-hook-lineage",
              "runtime.md#rt-bap-profile-guidance"
            ],
            "note": "Generic caller identity or a save API does not resolve per-content human control; the ask interface and opaque transformation admissions are absent from the records."
          }
        ],
        "records": [
          "runtime.md#rt-rte-mediated-action",
          "memory.md#mem-obj-live-graph",
          "memory.md#mem-rte-graph-reuse",
          "runtime.md#rt-rte-host-edit",
          "runtime.md#rt-obj-device-config",
          "runtime.md#rt-rte-device-seeding",
          "memory.md#mem-obj-session-ledger",
          "memory.md#mem-obj-view-store",
          "memory.md#mem-obj-knowledge-files",
          "epistemic.md#epi-rte-source-ingest",
          "epistemic.md#epi-obj-write-metadata",
          "epistemic.md#epi-rte-hook-lineage",
          "runtime.md#rt-bap-profile-guidance"
        ],
        "note": "Software admission and explicit human content editing are distinguished from workflow initiation; ask, generic filesystem callers, initialization and opaque package writes remain unresolved."
      },
      "curation_operations": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Retained knowledge overwrite",
            "assessment": "known",
            "findings": [
              {
                "value": "evolve",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-mediated-action",
                  "memory.md#mem-obj-live-graph",
                  "memory.md#mem-rte-graph-reuse"
                ],
                "note": "Replacement content revises the existing knowledge entry."
              }
            ],
            "records": [
              "runtime.md#rt-rte-mediated-action",
              "memory.md#mem-obj-live-graph",
              "memory.md#mem-rte-graph-reuse"
            ],
            "note": "The documented full replacement revises an existing retained file; no exercised improvement or synthesis is asserted."
          },
          {
            "scope": "Other knowledge maintenance, asset processing, ingestion, computed guidance, ledger/viewer state and configuration maintenance",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-clm-maintenance-limits",
              "epistemic.md#epi-rte-source-ingest",
              "runtime.md#rt-bap-profile-guidance",
              "memory.md#mem-obj-session-ledger",
              "memory.md#mem-obj-view-store",
              "runtime.md#rt-obj-device-config",
              "runtime.md#rt-rte-device-seeding"
            ],
            "note": "No implemented semantic transformation, bounded negative or comprehensive withdrawal consumer establishes deduplication, consolidation, synthesis, promotion, decay or invalidation for these alternatives. Device merge/index refresh alone establish none of those values."
          }
        ],
        "records": [
          "runtime.md#rt-rte-mediated-action",
          "memory.md#mem-obj-live-graph",
          "memory.md#mem-rte-graph-reuse",
          "memory.md#mem-clm-maintenance-limits",
          "epistemic.md#epi-rte-source-ingest",
          "runtime.md#rt-bap-profile-guidance",
          "memory.md#mem-obj-session-ledger",
          "memory.md#mem-obj-view-store",
          "runtime.md#rt-obj-device-config",
          "runtime.md#rt-rte-device-seeding"
        ],
        "note": "An existing-file overwrite supports revision locally. Indexing, registry merging, mutation-preview names and package labels do not establish additional semantic curation operations."
      },
      "read_back_direction": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Later explicit file/graph request",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-live-graph",
                  "memory.md#mem-rte-graph-reuse",
                  "runtime.md#rt-rte-host-edit"
                ],
                "note": "A later client/projection requests retained file or graph content."
              }
            ],
            "records": [
              "memory.md#mem-obj-live-graph",
              "memory.md#mem-rte-graph-reuse",
              "runtime.md#rt-rte-host-edit"
            ],
            "note": "A repository/path request followed by returned/rendered content is pull, not identifier push."
          },
          {
            "scope": "Subsequent seeder configuration load/merge",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-device-config",
                  "runtime.md#rt-rte-device-seeding"
                ],
                "note": "The subsequent merge explicitly reads existing registry files."
              }
            ],
            "records": [
              "runtime.md#rt-obj-device-config",
              "runtime.md#rt-rte-device-seeding"
            ],
            "note": "The seeder rereads retained configuration as an input to another invocation; the load requests that material."
          },
          {
            "scope": "Change subscription delivery",
            "assessment": "known",
            "findings": [
              {
                "value": "push",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-live-graph",
                  "memory.md#mem-rte-graph-reuse"
                ],
                "note": "Change-triggered updates are supplied to subscribed consumers."
              }
            ],
            "records": [
              "memory.md#mem-obj-live-graph",
              "memory.md#mem-rte-graph-reuse"
            ],
            "note": "After subscription, the declared service streams changes without a new content request for each change; subscription setup remains a request."
          },
          {
            "scope": "Ledger replay, saved pane/viewer reload, computed/changed guidance and source-note later consumption",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-session-ledger",
              "runtime.md#rt-rte-host-edit",
              "memory.md#mem-obj-view-store",
              "runtime.md#rt-bap-profile-guidance",
              "epistemic.md#epi-rte-source-ingest"
            ],
            "note": "A retained object name or static launch materialization does not establish a later accumulated-memory consumer. Exact guidance-selected parts and reload/replay routes are unspecified."
          }
        ],
        "records": [
          "memory.md#mem-obj-live-graph",
          "memory.md#mem-rte-graph-reuse",
          "runtime.md#rt-rte-host-edit",
          "runtime.md#rt-obj-device-config",
          "runtime.md#rt-rte-device-seeding",
          "memory.md#mem-obj-session-ledger",
          "memory.md#mem-obj-view-store",
          "runtime.md#rt-bap-profile-guidance",
          "epistemic.md#epi-rte-source-ingest"
        ],
        "note": "File and registry reuse are established locally. Subscription delivery is distinct from requested reads; guidance, ledger, saved/viewer state and opaque ingestion retain unresolved later-consumer coverage."
      },
      "read_back_signal": {
        "assessment": "not-determinable",
        "units": [
          {
            "scope": "Subscription selector and delivered changed parts",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-live-graph",
              "memory.md#mem-rte-graph-reuse"
            ],
            "note": "Subscriptions stream changes; filter granularity, identity matching and exact delivered retained content are not specified. Mounted-domain scope alone does not establish a coarse selection operation."
          },
          {
            "scope": "Computed/changed guidance and opaque later delivery alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-bap-profile-guidance",
              "memory.md#mem-obj-session-ledger",
              "runtime.md#rt-rte-host-edit",
              "memory.md#mem-obj-view-store",
              "epistemic.md#epi-rte-source-ingest"
            ],
            "note": "Graph-walk seeds are targeting inputs, not an inspected selector or identified payload. Triggered skill matching and later accumulated-content delivery remain unresolved."
          },
          {
            "scope": "Explicit file and configuration requests",
            "assessment": "inapplicable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-live-graph",
              "memory.md#mem-rte-graph-reuse",
              "runtime.md#rt-obj-device-config",
              "runtime.md#rt-rte-device-seeding"
            ],
            "note": "Read-back signal classifies push selection; these local operations fulfill requests and introduce no push selector."
          }
        ],
        "records": [
          "memory.md#mem-obj-live-graph",
          "memory.md#mem-rte-graph-reuse",
          "runtime.md#rt-bap-profile-guidance",
          "memory.md#mem-obj-session-ledger",
          "runtime.md#rt-rte-host-edit",
          "memory.md#mem-obj-view-store",
          "epistemic.md#epi-rte-source-ingest",
          "runtime.md#rt-obj-device-config",
          "runtime.md#rt-rte-device-seeding"
        ],
        "note": "The subscription push is documented, but accepted records do not identify its actual selector input and delivered retained parts sufficiently to classify a signal. A pull witness cannot make unresolved push alternatives inapplicable."
      },
      "trace_learning": {
        "assessment": "not-determinable",
        "units": [
          {
            "scope": "Session ledger to later behavior-shaping artifact",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-session-ledger",
              "epistemic.md#epi-rte-hook-lineage"
            ],
            "note": "Raw events are recorded, but no automatic derived artifact and later consumer are established."
          },
          {
            "scope": "Computed injection, source-note transforms and changed guidance",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-bap-profile-guidance",
              "epistemic.md#epi-rte-source-ingest"
            ],
            "note": "Inputs, durable derived result and later invocation chain are unspecified. Session-start timing alone does not establish trace feeding."
          },
          {
            "scope": "File indexing and device configuration merge",
            "assessment": "inapplicable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-live-graph",
              "memory.md#mem-rte-graph-reuse",
              "runtime.md#rt-obj-device-config",
              "runtime.md#rt-rte-device-seeding"
            ],
            "note": "These known transformations index files or merge configuration, rather than automatically derive behavior-shaping artifacts from activity traces."
          },
          {
            "scope": "Initial knowledge, host/viewer state and stamped output alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-knowledge-files",
              "runtime.md#rt-rte-host-edit",
              "memory.md#mem-obj-view-store",
              "epistemic.md#epi-obj-write-metadata",
              "epistemic.md#epi-rte-hook-lineage"
            ],
            "note": "No qualifying trace-fed update and later consumer are recorded; incomplete provenance prevents a bounded negative."
          }
        ],
        "records": [
          "memory.md#mem-obj-session-ledger",
          "epistemic.md#epi-rte-hook-lineage",
          "runtime.md#rt-bap-profile-guidance",
          "epistemic.md#epi-rte-source-ingest",
          "memory.md#mem-obj-live-graph",
          "memory.md#mem-rte-graph-reuse",
          "runtime.md#rt-obj-device-config",
          "runtime.md#rt-rte-device-seeding",
          "memory.md#mem-obj-knowledge-files",
          "runtime.md#rt-rte-host-edit",
          "memory.md#mem-obj-view-store",
          "epistemic.md#epi-obj-write-metadata"
        ],
        "note": "No accepted bounded absence or qualifying positive chain resolves the included opaque alternatives. Event recording alone is insufficient; do not turn an unestablished learning route into a system-wide no."
      },
      "trace_source": {
        "assessment": "not-determinable",
        "units": [
          {
            "scope": "Ledger-derived update candidate",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-session-ledger",
              "epistemic.md#epi-rte-hook-lineage"
            ],
            "note": "Events are recorded but no qualifying learning write consuming them is established; no event-streams finding is inferred from the observer label."
          },
          {
            "scope": "Computed guidance, ingest and other unresolved write alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-bap-profile-guidance",
              "epistemic.md#epi-rte-source-ingest",
              "memory.md#mem-obj-knowledge-files",
              "runtime.md#rt-rte-host-edit",
              "memory.md#mem-obj-view-store",
              "epistemic.md#epi-obj-write-metadata",
              "epistemic.md#epi-rte-hook-lineage"
            ],
            "note": "No qualifying update or original input content is identified. Session logs, tool traces, event streams and trajectories cannot be classified from package names or hook timing."
          },
          {
            "scope": "Non-trace file indexing and configuration merge",
            "assessment": "inapplicable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-live-graph",
              "memory.md#mem-rte-graph-reuse",
              "runtime.md#rt-obj-device-config",
              "runtime.md#rt-rte-device-seeding"
            ],
            "note": "These local transformations have no qualifying trace-learning route whose source would be classified."
          }
        ],
        "records": [
          "memory.md#mem-obj-session-ledger",
          "epistemic.md#epi-rte-hook-lineage",
          "runtime.md#rt-bap-profile-guidance",
          "epistemic.md#epi-rte-source-ingest",
          "memory.md#mem-obj-knowledge-files",
          "runtime.md#rt-rte-host-edit",
          "memory.md#mem-obj-view-store",
          "epistemic.md#epi-obj-write-metadata",
          "memory.md#mem-obj-live-graph",
          "memory.md#mem-rte-graph-reuse",
          "runtime.md#rt-obj-device-config",
          "runtime.md#rt-rte-device-seeding"
        ],
        "note": "Trace source cannot be assigned without a qualifying trace-fed write. The ledger event origin is not by itself a learning-route source; unresolved injection/ingest inputs remain included."
      }
    }
  }
}
---

# Arsumbris memory profile

## Comparison rationale

This is a partial documentary memory inventory, not a classification of the full platform's storage or permission envelope. Files and their in-memory graph are separate operative parts. Indexed assets remain opaque even though their file substrate is known. The ledger's symbolic envelope does not reveal its payload form or backing store. See [MEM-OBJ-knowledge-files](memory.md#mem-obj-knowledge-files), [MEM-OBJ-live-graph](memory.md#mem-obj-live-graph) and [MEM-OBJ-session-ledger](memory.md#mem-obj-session-ledger).

The implemented seeder supplies a narrow wired witness for configuration writes and subsequent merge reuse. Host/engine launch consumers remain claimed. Its caller's write opt-in is not per-entry human admission. Parsed rows are preserved, not arbitrary YAML semantics; the parser qualification remains attached to [EPI-OBJ-registry-paths](epistemic.md#epi-obj-registry-paths). Neither registry merging nor index refresh is semantic curation. The documented overwrite route supports evolving an existing file, without establishing synthesis, truth acceptance or exercised improvement; see [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action).

Explicit file requests and change subscriptions are different operations. A requested path does not support identifier-based push. Subscription details are too thin to determine a push signal. Static skills/injects describe working context rather than accumulated memory; any changed/computed guidance route remains unresolved because its retained inputs, selected payload and later consumption are not established by [RT-BAP-profile-guidance](runtime.md#rt-bap-profile-guidance). Intended instruction delivery therefore does not create a positive accumulated-memory instruction finding.

Reconciliation supersedes the epistemic knowledge-file, type-definition and session-ledger objects with their memory counterparts, and the epistemic graph-index route with the memory graph-reuse route. All profile citations use those canonical memory identities. The epistemic diagnostic, stamp, registry-part and ingest records remain distinct. These identity resolutions change no local evidence basis and supply no missing operation evidence.

No qualifying automatic trace-to-durable-artifact-to-later-consumer chain is recorded. This prevents a positive trace-learning or trace-source classification, but the unresolved computed-context and package alternatives prevent a bounded negative too. Learning authority is likewise not inferred from event retention. See [MEM-OBJ-session-ledger](memory.md#mem-obj-session-ledger) and [EPI-RTE-source-ingest](epistemic.md#epi-rte-source-ingest).

Source-read log: none. Classification used only the supplied accepted members and reconciliation; no source ambiguity required a direct source read. No execution or causal evidence upgrades the documentary findings.

---
{
  "type": "agentic-system-analyses/types/agentic-system-memory-profile.md",
  "description": "MGI-Mind memory comparison: retained content, retrieval indexes and trace-derived reliance state at the frozen source boundary.",
  "run-id": "AAS-2026-11-08-mgi-mind-e0f02081480f-01",
  "source-identity": "https://github.com/madgodinc/mgi-mind",
  "reviewed-boundary": "a8defc36f7d0bcd5108714763a12625a0eda0868",
  "memory-comparison": {
    "version": 2,
    "scope": "Accumulated notes and quarantine, fact assertions/lifecycle/cardinality, procedures and skills with retrieval indexes/outcome statistics, typed signals, sessions, pinned blocks, query/origin activity, access/audit journals, vault and their admission, maintenance, export and later-consumer routes. Includes unresolved initialization/backfill, cache, restore and consumer alternatives retained by accepted records. Excludes shipped static prompts, unmodified inference weights, ordinary current-request response envelopes and uninspected external host/provider internals.",
    "axes": {
      "storage_substrate": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Qdrant note payloads, quarantine, facts and cardinality, procedures, skills, outcome statistics and typed signals",
            "assessment": "known",
            "findings": [
              {
                "value": "service-object",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-memory",
                  "memory.md#mem-obj-quarantine",
                  "memory.md#mem-obj-fact",
                  "memory.md#mem-obj-fact-state",
                  "memory.md#mem-obj-procedure",
                  "memory.md#mem-obj-skill",
                  "memory.md#mem-obj-procstats",
                  "memory.md#mem-obj-external-signals"
                ],
                "note": "Qdrant points and collections retain these objects; the service is the operative substrate, not inferred underlying database files."
              }
            ],
            "records": [
              "memory.md#mem-obj-memory",
              "memory.md#mem-obj-quarantine",
              "memory.md#mem-obj-fact",
              "memory.md#mem-obj-fact-state",
              "memory.md#mem-obj-procedure",
              "memory.md#mem-obj-skill",
              "memory.md#mem-obj-procstats",
              "memory.md#mem-obj-external-signals"
            ],
            "note": "Qdrant points and collections retain these objects; the service is the operative substrate, not inferred underlying database files."
          },
          {
            "scope": "Qdrant note/procedure/skill dense and sparse retrieval indexes",
            "assessment": "known",
            "findings": [
              {
                "value": "vector",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-memory-vectors",
                  "memory.md#mem-obj-procedure",
                  "memory.md#mem-obj-skill"
                ],
                "note": "Stored vectors are consumed by retrieval; vectorless facts and statistics are excluded from this unit."
              }
            ],
            "records": [
              "memory.md#mem-obj-memory-vectors",
              "memory.md#mem-obj-procedure",
              "memory.md#mem-obj-skill"
            ],
            "note": "Stored vectors are consumed by retrieval; vectorless facts and statistics are excluded from this unit."
          },
          {
            "scope": "Session files, blocks, durable origin centroids, access and audit journals, vault",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-session",
                  "memory.md#mem-obj-blocks",
                  "memory.md#mem-obj-origin-context",
                  "memory.md#mem-obj-access",
                  "memory.md#mem-obj-audit",
                  "memory.md#mem-obj-vault"
                ],
                "note": "Local Markdown, JSON, log and encrypted files retain these distinct surfaces."
              }
            ],
            "records": [
              "memory.md#mem-obj-session",
              "memory.md#mem-obj-blocks",
              "memory.md#mem-obj-origin-context",
              "memory.md#mem-obj-access",
              "memory.md#mem-obj-audit",
              "memory.md#mem-obj-vault"
            ],
            "note": "Local Markdown, JSON, log and encrypted files retain these distinct surfaces."
          },
          {
            "scope": "Recent query-vector activity buffer",
            "assessment": "known",
            "findings": [
              {
                "value": "in-memory",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-origin-context"
                ],
                "note": "Process-local query activity feeds later centroid comparisons and durable origin state; not an entire host transcript."
              }
            ],
            "records": [
              "memory.md#mem-obj-origin-context"
            ],
            "note": "Process-local query activity feeds later centroid comparisons and durable origin state; not an entire host transcript."
          },
          {
            "scope": "Migration/backfill, calibration, complete checkpoint restore/reassembly and derived activity caches",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-origin-context",
              "memory.md#mem-obj-memory",
              "memory.md#mem-obj-session"
            ],
            "note": "Accepted inventory retains incompletely traced initialization/cache and restore alternatives; no complete substrate inventory follows."
          }
        ],
        "records": [
          "memory.md#mem-obj-memory",
          "memory.md#mem-obj-quarantine",
          "memory.md#mem-obj-fact",
          "memory.md#mem-obj-fact-state",
          "memory.md#mem-obj-procedure",
          "memory.md#mem-obj-skill",
          "memory.md#mem-obj-procstats",
          "memory.md#mem-obj-external-signals",
          "memory.md#mem-obj-memory-vectors",
          "memory.md#mem-obj-session",
          "memory.md#mem-obj-blocks",
          "memory.md#mem-obj-origin-context",
          "memory.md#mem-obj-access",
          "memory.md#mem-obj-audit",
          "memory.md#mem-obj-vault"
        ],
        "note": "Known operative substrates coexist with incompletely traced maintenance/checkpoint alternatives. Static model files and external host weights are excluded: no use-updated weights are established."
      },
      "representational_form": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Returned note, fact assertion, procedure, skill, summary and pinned-block prose; audit prose snapshots",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-memory",
                  "memory.md#mem-obj-fact",
                  "memory.md#mem-obj-procedure",
                  "memory.md#mem-obj-skill",
                  "memory.md#mem-obj-session",
                  "memory.md#mem-obj-blocks",
                  "memory.md#mem-obj-audit"
                ],
                "note": "Hosts/operators interpret prose; fact slots also have a distinct fixed-rule path."
              }
            ],
            "records": [
              "memory.md#mem-obj-memory",
              "memory.md#mem-obj-fact",
              "memory.md#mem-obj-procedure",
              "memory.md#mem-obj-skill",
              "memory.md#mem-obj-session",
              "memory.md#mem-obj-blocks",
              "memory.md#mem-obj-audit"
            ],
            "note": "Hosts/operators interpret prose; fact slots also have a distinct fixed-rule path."
          },
          {
            "scope": "Metadata, lifecycle/cardinality, triple matching slots, names, sparse indexes, stats, signals and journals",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-fact",
                  "memory.md#mem-obj-fact-state",
                  "memory.md#mem-obj-memory-vectors",
                  "memory.md#mem-obj-procstats",
                  "memory.md#mem-obj-external-signals",
                  "memory.md#mem-obj-access",
                  "memory.md#mem-obj-audit",
                  "memory.md#mem-obj-session",
                  "memory.md#mem-obj-blocks"
                ],
                "note": "Localized fields and sparse lexical indexes are consumed by fixed rules; their serialization does not make them prose."
              }
            ],
            "records": [
              "memory.md#mem-obj-fact",
              "memory.md#mem-obj-fact-state",
              "memory.md#mem-obj-memory-vectors",
              "memory.md#mem-obj-procstats",
              "memory.md#mem-obj-external-signals",
              "memory.md#mem-obj-access",
              "memory.md#mem-obj-audit",
              "memory.md#mem-obj-session",
              "memory.md#mem-obj-blocks"
            ],
            "note": "Localized fields and sparse lexical indexes are consumed by fixed rules; their serialization does not make them prose."
          },
          {
            "scope": "Dense retrieval embeddings and query/origin centroids",
            "assessment": "known",
            "findings": [
              {
                "value": "parametric",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-memory-vectors",
                  "memory.md#mem-obj-origin-context",
                  "memory.md#mem-obj-procedure",
                  "memory.md#mem-obj-skill"
                ],
                "note": "Dense numerical representations distribute selection information; they are not learned model-weight updates."
              }
            ],
            "records": [
              "memory.md#mem-obj-memory-vectors",
              "memory.md#mem-obj-origin-context",
              "memory.md#mem-obj-procedure",
              "memory.md#mem-obj-skill"
            ],
            "note": "Dense numerical representations distribute selection information; they are not learned model-weight updates."
          },
          {
            "scope": "Original secret values in encrypted vault",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-vault"
            ],
            "note": "Encrypted encoding and readable key metadata do not establish the arbitrary value's intrinsic form."
          },
          {
            "scope": "Untraced migration/backfill, cache and restore payload alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-origin-context",
              "memory.md#mem-obj-memory"
            ],
            "note": "No full payload/consumer inventory establishes every included form."
          }
        ],
        "records": [
          "memory.md#mem-obj-memory",
          "memory.md#mem-obj-fact",
          "memory.md#mem-obj-procedure",
          "memory.md#mem-obj-skill",
          "memory.md#mem-obj-session",
          "memory.md#mem-obj-blocks",
          "memory.md#mem-obj-audit",
          "memory.md#mem-obj-fact-state",
          "memory.md#mem-obj-memory-vectors",
          "memory.md#mem-obj-procstats",
          "memory.md#mem-obj-external-signals",
          "memory.md#mem-obj-access",
          "memory.md#mem-obj-origin-context",
          "memory.md#mem-obj-vault"
        ],
        "note": "Split text interpretation, fixed-rule fields and dense numerical paths; opaque vault values and incompletely traced payloads prevent complete coverage."
      },
      "lineage": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Caller-composed notes, asserted facts, procedures, skills, pinned blocks and session summaries",
            "assessment": "known",
            "findings": [
              {
                "value": "authored",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-memory",
                  "memory.md#mem-obj-fact",
                  "memory.md#mem-obj-procedure",
                  "memory.md#mem-obj-skill",
                  "memory.md#mem-obj-blocks",
                  "memory.md#mem-obj-session"
                ],
                "note": "Caller-authored paths exist; human authorship is not implied."
              }
            ],
            "records": [
              "memory.md#mem-obj-memory",
              "memory.md#mem-obj-fact",
              "memory.md#mem-obj-procedure",
              "memory.md#mem-obj-skill",
              "memory.md#mem-obj-blocks",
              "memory.md#mem-obj-session"
            ],
            "note": "Caller-authored paths exist; human authorship is not implied."
          },
          {
            "scope": "Citation snippets, fetched web Markdown and Markdown reconciliation",
            "assessment": "known",
            "findings": [
              {
                "value": "imported",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-memory",
                  "epistemic.md#epi-rte-provenance-import",
                  "runtime.md#rt-rte-markdown-reconcile"
                ],
                "note": "Existing external/disk material enters storage; citation shape does not authenticate source warrant."
              }
            ],
            "records": [
              "memory.md#mem-obj-memory",
              "epistemic.md#epi-rte-provenance-import",
              "runtime.md#rt-rte-markdown-reconcile"
            ],
            "note": "Existing external/disk material enters storage; citation shape does not authenticate source warrant."
          },
          {
            "scope": "Harvested user/assistant text and outcome/access-derived state",
            "assessment": "known",
            "findings": [
              {
                "value": "trace-extracted",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-transcript-harvest",
                  "memory.md#mem-rte-outcome-ranking",
                  "memory.md#mem-obj-access",
                  "memory.md#mem-obj-origin-context"
                ],
                "note": "Activity supplies excerpts, counters and centroids; transcript source metadata is degraded."
              }
            ],
            "records": [
              "memory.md#mem-rte-transcript-harvest",
              "memory.md#mem-rte-outcome-ranking",
              "memory.md#mem-obj-access",
              "memory.md#mem-obj-origin-context"
            ],
            "note": "Activity supplies excerpts, counters and centroids; transcript source metadata is degraded."
          },
          {
            "scope": "Chunk/vector generation, optional fact extraction and portable rendering",
            "assessment": "known",
            "findings": [
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-memory-vectors",
                  "runtime.md#rt-rte-auto-extraction",
                  "memory.md#mem-rte-portable-export"
                ],
                "note": "Software/model transformations derive indexes, triples and exports; no semantic-fidelity guarantee is implied."
              }
            ],
            "records": [
              "memory.md#mem-obj-memory-vectors",
              "runtime.md#rt-rte-auto-extraction",
              "memory.md#mem-rte-portable-export"
            ],
            "note": "Software/model transformations derive indexes, triples and exports; no semantic-fidelity guarantee is implied."
          },
          {
            "scope": "Initial installed content, skill bodies, legacy statistics seeds, migrations and exact embedding provenance",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-skill",
              "memory.md#mem-obj-procstats",
              "memory.md#mem-obj-memory-vectors"
            ],
            "note": "Known subsequent derivation does not resolve initial provenance or backfill state."
          }
        ],
        "records": [
          "memory.md#mem-obj-memory",
          "memory.md#mem-obj-fact",
          "memory.md#mem-obj-procedure",
          "memory.md#mem-obj-skill",
          "memory.md#mem-obj-blocks",
          "memory.md#mem-obj-session",
          "epistemic.md#epi-rte-provenance-import",
          "runtime.md#rt-rte-markdown-reconcile",
          "memory.md#mem-rte-transcript-harvest",
          "memory.md#mem-rte-outcome-ranking",
          "memory.md#mem-obj-access",
          "memory.md#mem-obj-origin-context",
          "memory.md#mem-obj-memory-vectors",
          "runtime.md#rt-rte-auto-extraction",
          "memory.md#mem-rte-portable-export",
          "memory.md#mem-obj-procstats"
        ],
        "note": "Several derivation paths coexist; source labels do not authenticate history."
      },
      "behavioral_authority": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Notes, facts and session summaries returned to a requesting host; vault values to terminal operator",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-bap-host-recall",
                  "memory.md#mem-obj-fact",
                  "memory.md#mem-obj-session",
                  "memory.md#mem-obj-vault"
                ],
                "note": "Content supplies contextual/reference material, not mandatory beliefs or verified truth."
              }
            ],
            "records": [
              "runtime.md#rt-bap-host-recall",
              "memory.md#mem-obj-fact",
              "memory.md#mem-obj-session",
              "memory.md#mem-obj-vault"
            ],
            "note": "Content supplies contextual/reference material, not mandatory beliefs or verified truth."
          },
          {
            "scope": "Retrieved procedure fixes and skill bodies",
            "assessment": "known",
            "findings": [
              {
                "value": "instruction",
                "basis": "wired",
                "records": [
                  "memory.md#mem-bap-playbook-guidance",
                  "runtime.md#rt-rte-skill-admission"
                ],
                "note": "Playbooks provide directions to the requesting assistant/operator; compliance remains unobserved."
              }
            ],
            "records": [
              "memory.md#mem-bap-playbook-guidance",
              "runtime.md#rt-rte-skill-admission"
            ],
            "note": "Playbooks provide directions to the requesting assistant/operator; compliance remains unobserved."
          },
          {
            "scope": "Portable exported fixes installed as host guidance",
            "assessment": "known",
            "findings": [
              {
                "value": "instruction",
                "basis": "afforded",
                "records": [
                  "memory.md#mem-rte-portable-export"
                ],
                "note": "Host-file consumption is afforded, not automatic installation."
              }
            ],
            "records": [
              "memory.md#mem-rte-portable-export"
            ],
            "note": "Host-file consumption is afforded, not automatic installation."
          },
          {
            "scope": "Retained vectors/text/triggers, outcome stats and drift state at ranking consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "ranking",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-memory-vectors",
                  "memory.md#mem-rte-outcome-ranking",
                  "memory.md#mem-rte-fact-retest",
                  "memory.md#mem-obj-procedure",
                  "memory.md#mem-obj-skill"
                ],
                "note": "Retained parts affect relative priority through hybrid retrieval, trust scores or conditional doubt ordering."
              }
            ],
            "records": [
              "memory.md#mem-obj-memory-vectors",
              "memory.md#mem-rte-outcome-ranking",
              "memory.md#mem-rte-fact-retest",
              "memory.md#mem-obj-procedure",
              "memory.md#mem-obj-skill"
            ],
            "note": "Retained parts affect relative priority through hybrid retrieval, trust scores or conditional doubt ordering."
          },
          {
            "scope": "Fact validity/status and withdrawal state at read/add predicates",
            "assessment": "known",
            "findings": [
              {
                "value": "enforcement",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-fact-lifecycle",
                  "epistemic.md#epi-rte-fact-withdrawal"
                ],
                "note": "Retained tombstones veto reassertion and visibility; candidate admission checks the retained invalidation criterion."
              },
              {
                "value": "validation",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-fact-lifecycle",
                  "epistemic.md#epi-rte-fact-withdrawal"
                ],
                "note": "Retained tombstones veto reassertion and visibility; candidate admission checks the retained invalidation criterion."
              }
            ],
            "records": [
              "memory.md#mem-rte-fact-lifecycle",
              "epistemic.md#epi-rte-fact-withdrawal"
            ],
            "note": "Retained tombstones veto reassertion and visibility; candidate admission checks the retained invalidation criterion."
          },
          {
            "scope": "Retained cardinality and prior fact standing at conflict branch selection",
            "assessment": "known",
            "findings": [
              {
                "value": "routing",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-fact-state",
                  "epistemic.md#epi-rte-fact-comparison"
                ],
                "note": "Cardinality determines whether an axis duels; incumbent history supplies comparison criteria, not source-truth proof."
              },
              {
                "value": "validation",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-fact-state",
                  "epistemic.md#epi-rte-fact-comparison"
                ],
                "note": "Cardinality determines whether an axis duels; incumbent history supplies comparison criteria, not source-truth proof."
              }
            ],
            "records": [
              "memory.md#mem-obj-fact-state",
              "epistemic.md#epi-rte-fact-comparison"
            ],
            "note": "Cardinality determines whether an axis duels; incumbent history supplies comparison criteria, not source-truth proof."
          },
          {
            "scope": "Reported outcomes and access traces at durable reliance-update consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "learning",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-outcome-ranking",
                  "memory.md#mem-obj-access",
                  "runtime.md#rt-rte-store-consolidation"
                ],
                "note": "Experience feeds durable counters or retrieval-membership changes; this authority does not establish improved capacity."
              }
            ],
            "records": [
              "memory.md#mem-rte-outcome-ranking",
              "memory.md#mem-obj-access",
              "runtime.md#rt-rte-store-consolidation"
            ],
            "note": "Experience feeds durable counters or retrieval-membership changes; this authority does not establish improved capacity."
          },
          {
            "scope": "Quarantine/archive flags at retrieval filters",
            "assessment": "known",
            "findings": [
              {
                "value": "enforcement",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-quarantine",
                  "runtime.md#rt-rte-store-consolidation"
                ],
                "note": "Retained visibility state withholds ordinary delivery until separate restoration/promotion."
              }
            ],
            "records": [
              "memory.md#mem-obj-quarantine",
              "runtime.md#rt-rte-store-consolidation"
            ],
            "note": "Retained visibility state withholds ordinary delivery until separate restoration/promotion."
          },
          {
            "scope": "Pinned-block contents, arbitrary initial content and untraced maintenance/restore consumers",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-blocks",
              "memory.md#mem-obj-skill",
              "memory.md#mem-obj-memory"
            ],
            "note": "Placement alone cannot decide whether arbitrary content supplies instructions, reference or another force; full consumers are not traced."
          }
        ],
        "records": [
          "runtime.md#rt-bap-host-recall",
          "memory.md#mem-obj-fact",
          "memory.md#mem-obj-session",
          "memory.md#mem-obj-vault",
          "memory.md#mem-bap-playbook-guidance",
          "runtime.md#rt-rte-skill-admission",
          "memory.md#mem-rte-portable-export",
          "memory.md#mem-obj-memory-vectors",
          "memory.md#mem-rte-outcome-ranking",
          "memory.md#mem-rte-fact-retest",
          "memory.md#mem-obj-procedure",
          "memory.md#mem-obj-skill",
          "memory.md#mem-rte-fact-lifecycle",
          "epistemic.md#epi-rte-fact-withdrawal",
          "memory.md#mem-obj-fact-state",
          "epistemic.md#epi-rte-fact-comparison",
          "memory.md#mem-obj-access",
          "runtime.md#rt-rte-store-consolidation",
          "memory.md#mem-obj-quarantine",
          "memory.md#mem-obj-blocks",
          "memory.md#mem-obj-memory"
        ],
        "note": "Authority is per retained part and consumer. HTTP startup ACLs and shipped static instructions are not automatically classified as accumulated memory."
      },
      "write_agency": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Assistant tool add, ingest, extraction, transcript block admission, fact and skill/block updates, outcome statistics",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-assistant-memory",
                  "runtime.md#rt-rte-ingest-admission",
                  "runtime.md#rt-rte-auto-extraction",
                  "memory.md#mem-rte-transcript-harvest",
                  "memory.md#mem-rte-fact-lifecycle",
                  "runtime.md#rt-rte-skill-admission",
                  "memory.md#mem-rte-pinned-blocks",
                  "memory.md#mem-rte-outcome-ranking"
                ],
                "note": "Software/model admission has no mandatory per-content human decision; initiating a workflow is not approval of each item."
              }
            ],
            "records": [
              "runtime.md#rt-rte-assistant-memory",
              "runtime.md#rt-rte-ingest-admission",
              "runtime.md#rt-rte-auto-extraction",
              "memory.md#mem-rte-transcript-harvest",
              "memory.md#mem-rte-fact-lifecycle",
              "runtime.md#rt-rte-skill-admission",
              "memory.md#mem-rte-pinned-blocks",
              "memory.md#mem-rte-outcome-ranking"
            ],
            "note": "Software/model admission has no mandatory per-content human decision; initiating a workflow is not approval of each item."
          },
          {
            "scope": "Apply-gated Markdown replacements and consolidation mutations",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-markdown-reconcile",
                  "runtime.md#rt-rte-store-consolidation"
                ],
                "note": "Generic caller chooses apply; software chooses individual replacements/survivors without an established per-item human decision."
              }
            ],
            "records": [
              "runtime.md#rt-rte-markdown-reconcile",
              "runtime.md#rt-rte-store-consolidation"
            ],
            "note": "Generic caller chooses apply; software chooses individual replacements/survivors without an established per-item human decision."
          },
          {
            "scope": "Terminal vault content admission",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-vault"
            ],
            "note": "Password and terminal interaction establish an operator surface, not an explicit recorded per-content human decision."
          },
          {
            "scope": "Initial installed content, session-summary production, migration/backfill and checkpoint replacement",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-session",
              "memory.md#mem-obj-skill",
              "memory.md#mem-obj-procstats"
            ],
            "note": "Caller identity and source-authorship alone do not establish initial control or summary-production agency."
          }
        ],
        "records": [
          "runtime.md#rt-rte-assistant-memory",
          "runtime.md#rt-rte-ingest-admission",
          "runtime.md#rt-rte-auto-extraction",
          "memory.md#mem-rte-transcript-harvest",
          "memory.md#mem-rte-fact-lifecycle",
          "runtime.md#rt-rte-skill-admission",
          "memory.md#mem-rte-pinned-blocks",
          "memory.md#mem-rte-outcome-ranking",
          "runtime.md#rt-rte-markdown-reconcile",
          "runtime.md#rt-rte-store-consolidation",
          "memory.md#mem-obj-vault",
          "memory.md#mem-obj-session",
          "memory.md#mem-obj-skill",
          "memory.md#mem-obj-procstats"
        ],
        "note": "Automatic admissions are supported; no manual finding is inferred from CLI use, a password or an apply flag."
      },
      "curation_operations": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Near-duplicate consolidation survivor selection",
            "assessment": "known",
            "findings": [
              {
                "value": "dedup",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-store-consolidation"
                ],
                "note": "Policy deletes selected duplicates, keeping longer content/older tie; not semantic summary generation."
              }
            ],
            "records": [
              "runtime.md#rt-rte-store-consolidation"
            ],
            "note": "Policy deletes selected duplicates, keeping longer content/older tie; not semantic summary generation."
          },
          {
            "scope": "Cold-note maintenance from access counts",
            "assessment": "known",
            "findings": [
              {
                "value": "decay",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-access",
                  "runtime.md#rt-rte-store-consolidation"
                ],
                "note": "When applied, coldness archives or prunes retained notes and changes future membership."
              }
            ],
            "records": [
              "memory.md#mem-obj-access",
              "runtime.md#rt-rte-store-consolidation"
            ],
            "note": "When applied, coldness archives or prunes retained notes and changes future membership."
          },
          {
            "scope": "Quarantine promotion and expiry",
            "assessment": "known",
            "findings": [
              {
                "value": "promote",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-quarantine",
                  "runtime.md#rt-rte-ingest-admission"
                ],
                "note": "Promotion raises visibility; expiry deletes still-quarantined candidates, preserving only bounded audit history."
              },
              {
                "value": "decay",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-quarantine",
                  "runtime.md#rt-rte-ingest-admission"
                ],
                "note": "Promotion raises visibility; expiry deletes still-quarantined candidates, preserving only bounded audit history."
              }
            ],
            "records": [
              "memory.md#mem-obj-quarantine",
              "runtime.md#rt-rte-ingest-admission"
            ],
            "note": "Promotion raises visibility; expiry deletes still-quarantined candidates, preserving only bounded audit history."
          },
          {
            "scope": "Fact withdrawal and duel retirement",
            "assessment": "known",
            "findings": [
              {
                "value": "invalidate",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-fact-lifecycle",
                  "epistemic.md#epi-rte-fact-withdrawal"
                ],
                "note": "Reliance is withdrawn while historical triple state remains; restore is separate."
              }
            ],
            "records": [
              "memory.md#mem-rte-fact-lifecycle",
              "epistemic.md#epi-rte-fact-withdrawal"
            ],
            "note": "Reliance is withdrawn while historical triple state remains; restore is separate."
          },
          {
            "scope": "Named skill/block overwrite and Markdown/note replacement",
            "assessment": "known",
            "findings": [
              {
                "value": "evolve",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-skill-admission",
                  "memory.md#mem-rte-pinned-blocks",
                  "runtime.md#rt-rte-markdown-reconcile",
                  "memory.md#mem-obj-memory"
                ],
                "note": "Existing retained entries/content are revised; old-body rollback is not guaranteed."
              }
            ],
            "records": [
              "runtime.md#rt-rte-skill-admission",
              "memory.md#mem-rte-pinned-blocks",
              "runtime.md#rt-rte-markdown-reconcile",
              "memory.md#mem-obj-memory"
            ],
            "note": "Existing retained entries/content are revised; old-body rollback is not guaranteed."
          },
          {
            "scope": "Typed-signal latest-per-key retention",
            "assessment": "known",
            "findings": [
              {
                "value": "dedup",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-external-signals",
                  "epistemic.md#epi-rte-outcome-recording"
                ],
                "note": "Same type/source reports replace prior log state without necessarily correcting earlier derived counters."
              },
              {
                "value": "evolve",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-external-signals",
                  "epistemic.md#epi-rte-outcome-recording"
                ],
                "note": "Same type/source reports replace prior log state without necessarily correcting earlier derived counters."
              }
            ],
            "records": [
              "memory.md#mem-obj-external-signals",
              "epistemic.md#epi-rte-outcome-recording"
            ],
            "note": "Same type/source reports replace prior log state without necessarily correcting earlier derived counters."
          },
          {
            "scope": "Optional automatic extraction of retained memory text, including harvested session messages, into standing fact triples",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-transcript-harvest",
                  "runtime.md#rt-rte-auto-extraction",
                  "memory.md#mem-rte-fact-lifecycle",
                  "runtime.md#rt-rte-context-briefing"
                ],
                "note": "The worker extracts triples from accepted memory content and submits them to durable fact admission. This compresses retained claims into standing facts, even while messages remain. Wiring requires the extractor feature, installed server and admitted memory; actual output fidelity, entailment, operation and benefit are unobserved."
              }
            ],
            "records": [
              "memory.md#mem-rte-transcript-harvest",
              "runtime.md#rt-rte-auto-extraction",
              "memory.md#mem-rte-fact-lifecycle",
              "runtime.md#rt-rte-context-briefing"
            ],
            "note": "The worker extracts triples from accepted memory content and submits them to durable fact admission. This compresses retained claims into standing facts, even while messages remain. Wiring requires the extractor feature, installed server and admitted memory; actual output fidelity, entailment, operation and benefit are unobserved."
          },
          {
            "scope": "Caller session-summary production",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-session"
            ],
            "note": "The server retains a caller-supplied summary; its production mechanism and transformation are not established."
          },
          {
            "scope": "Migration/calibration/backfill and full restore transformations",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-memory",
              "memory.md#mem-obj-origin-context"
            ],
            "note": "Accepted records retain incomplete transformation coverage."
          }
        ],
        "records": [
          "runtime.md#rt-rte-store-consolidation",
          "memory.md#mem-obj-access",
          "memory.md#mem-obj-quarantine",
          "runtime.md#rt-rte-ingest-admission",
          "memory.md#mem-rte-fact-lifecycle",
          "epistemic.md#epi-rte-fact-withdrawal",
          "runtime.md#rt-rte-skill-admission",
          "memory.md#mem-rte-pinned-blocks",
          "runtime.md#rt-rte-markdown-reconcile",
          "memory.md#mem-obj-memory",
          "memory.md#mem-obj-external-signals",
          "epistemic.md#epi-rte-outcome-recording",
          "runtime.md#rt-rte-auto-extraction",
          "epistemic.md#epi-rte-extraction-parser",
          "memory.md#mem-obj-session",
          "memory.md#mem-obj-origin-context",
          "memory.md#mem-rte-transcript-harvest",
          "runtime.md#rt-rte-context-briefing"
        ],
        "note": "Implemented operations include conditional standing-fact extraction as consolidation, alongside dedup, decay, promotion, withdrawal and replacement. Summary production and untraced maintenance remain unresolved; no supported synthesize finding."
      },
      "read_back_direction": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Requested search, unified recall, fact queries, session/context, skill match/show and terminal vault retrieval",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-assistant-memory",
                  "memory.md#mem-rte-unified-recall",
                  "epistemic.md#epi-rte-fact-consumption",
                  "runtime.md#rt-rte-context-briefing",
                  "runtime.md#rt-rte-skill-admission",
                  "memory.md#mem-obj-vault"
                ],
                "note": "Consumers request retained material. Automatic selection inside a request is not an independent unsolicited push."
              }
            ],
            "records": [
              "runtime.md#rt-rte-assistant-memory",
              "memory.md#mem-rte-unified-recall",
              "epistemic.md#epi-rte-fact-consumption",
              "runtime.md#rt-rte-context-briefing",
              "runtime.md#rt-rte-skill-admission",
              "memory.md#mem-obj-vault"
            ],
            "note": "Consumers request retained material. Automatic selection inside a request is not an independent unsolicited push."
          },
          {
            "scope": "Portable export for subsequent host-file consumption",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "afforded",
                "records": [
                  "memory.md#mem-rte-portable-export"
                ],
                "note": "Caller requests export and can install it for later use; external loading is afforded."
              }
            ],
            "records": [
              "memory.md#mem-rte-portable-export"
            ],
            "note": "Caller requests export and can install it for later use; external loading is afforded."
          },
          {
            "scope": "Background fact-retest candidate delivery to confidence evaluator",
            "assessment": "known",
            "findings": [
              {
                "value": "push",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-fact-retest",
                  "epistemic.md#epi-rte-confidence-retest"
                ],
                "note": "Automatic maintenance tick selects retained fact state without a request from that evaluator's end user; mode/startup conditions remain local."
              }
            ],
            "records": [
              "memory.md#mem-rte-fact-retest",
              "epistemic.md#epi-rte-confidence-retest"
            ],
            "note": "Automatic maintenance tick selects retained fact state without a request from that evaluator's end user; mode/startup conditions remain local."
          },
          {
            "scope": "Full restore/reassembly, administrative readers and untraced host consumption alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-memory",
              "memory.md#mem-obj-audit",
              "memory.md#mem-obj-session"
            ],
            "note": "Some readers and checkpoint consumers are only inventoried; complete direction coverage is not established."
          }
        ],
        "records": [
          "runtime.md#rt-rte-assistant-memory",
          "memory.md#mem-rte-unified-recall",
          "epistemic.md#epi-rte-fact-consumption",
          "runtime.md#rt-rte-context-briefing",
          "runtime.md#rt-rte-skill-admission",
          "memory.md#mem-obj-vault",
          "memory.md#mem-rte-portable-export",
          "memory.md#mem-rte-fact-retest",
          "epistemic.md#epi-rte-confidence-retest",
          "memory.md#mem-obj-memory",
          "memory.md#mem-obj-audit",
          "memory.md#mem-obj-session"
        ],
        "note": "Requested host delivery is pull. Background maintenance is a separate automatic server-consumer path, not proof of unsolicited model-context injection."
      },
      "read_back_signal": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Background fact retest",
            "assessment": "partial",
            "findings": [
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-fact-retest",
                  "epistemic.md#epi-rte-confidence-retest"
                ],
                "note": "Trigger is maintenance tick; selector takes bounded eligible fact candidates (up to 50), selecting retained scalar fact state for recomputation; exact prioritization remains unresolved."
              }
            ],
            "records": [
              "memory.md#mem-rte-fact-retest",
              "epistemic.md#epi-rte-confidence-retest"
            ],
            "note": "Trigger is maintenance tick; selector takes bounded eligible fact candidates (up to 50), selecting retained scalar fact state for recomputation; exact prioritization remains unresolved."
          },
          {
            "scope": "Detailed retest prioritization and unresolved alternative consumer routes",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-rte-fact-retest",
              "memory.md#mem-obj-memory"
            ],
            "note": "The records do not resolve all candidate-priority inputs or untraced read-back alternatives."
          },
          {
            "scope": "Requested host/terminal retrieval operations",
            "assessment": "inapplicable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-assistant-memory",
              "runtime.md#rt-rte-context-briefing",
              "memory.md#mem-rte-unified-recall",
              "memory.md#mem-obj-vault"
            ],
            "note": "Signal classifies push selection, not query or identifier choices made in an explicit consumer request."
          }
        ],
        "records": [
          "memory.md#mem-rte-fact-retest",
          "epistemic.md#epi-rte-confidence-retest",
          "memory.md#mem-obj-memory",
          "runtime.md#rt-rte-assistant-memory",
          "runtime.md#rt-rte-context-briefing",
          "memory.md#mem-rte-unified-recall",
          "memory.md#mem-obj-vault"
        ],
        "note": "Coarse bounded maintenance selection is established, not a complete selector inventory. Query embeddings on requested search do not establish inferred-embedding push."
      },
      "trace_learning": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Outcome reports transformed automatically into durable playbook ranking statistics",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-outcome-ranking",
                  "epistemic.md#epi-rte-outcome-trust"
                ],
                "note": "Reported reuse feeds software-admitted counters/verified state consumed by later recall/match; qualifying behavior-shaping memory, not demonstrated improvement."
              }
            ],
            "records": [
              "memory.md#mem-rte-outcome-ranking",
              "epistemic.md#epi-rte-outcome-trust"
            ],
            "note": "Reported reuse feeds software-admitted counters/verified state consumed by later recall/match; qualifying behavior-shaping memory, not demonstrated improvement."
          },
          {
            "scope": "Search access traces transformed into maintenance membership changes",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-access",
                  "runtime.md#rt-rte-store-consolidation"
                ],
                "note": "Accumulated access counts feed automatic coldness decisions when apply is enabled; archive/prune changes subsequent retrieval."
              }
            ],
            "records": [
              "memory.md#mem-obj-access",
              "runtime.md#rt-rte-store-consolidation"
            ],
            "note": "Accumulated access counts feed automatic coldness decisions when apply is enabled; archive/prune changes subsequent retrieval."
          },
          {
            "scope": "Query activity transformed into durable origin/doubt state",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-origin-context",
                  "memory.md#mem-rte-fact-retest",
                  "epistemic.md#epi-rte-drift-evaluation"
                ],
                "note": "Query embeddings form retained origin vectors; conditional enforce-mode drift updates counters affecting later fact ordering."
              }
            ],
            "records": [
              "memory.md#mem-obj-origin-context",
              "memory.md#mem-rte-fact-retest",
              "epistemic.md#epi-rte-drift-evaluation"
            ],
            "note": "Query embeddings form retained origin vectors; conditional enforce-mode drift updates counters affecting later fact ordering."
          },
          {
            "scope": "Harvested session text through conditional automatic extraction to durable facts and later fact-query/context consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-transcript-harvest",
                  "runtime.md#rt-rte-auto-extraction",
                  "memory.md#mem-rte-fact-lifecycle",
                  "runtime.md#rt-rte-context-briefing"
                ],
                "note": "The parser admits user/assistant text through ingest; accepted memory can trigger automatic triple extraction and fact admission, with later query/briefing consumption. Feature, installation and admission conditions bound this wired route. Actual triples, semantic fidelity, activation and improved capacity remain unobserved."
              }
            ],
            "records": [
              "memory.md#mem-rte-transcript-harvest",
              "runtime.md#rt-rte-auto-extraction",
              "memory.md#mem-rte-fact-lifecycle",
              "runtime.md#rt-rte-context-briefing"
            ],
            "note": "The parser admits user/assistant text through ingest; accepted memory can trigger automatic triple extraction and fact admission, with later query/briefing consumption. Feature, installation and admission conditions bound this wired route. Actual triples, semantic fidelity, activation and improved capacity remain unobserved."
          },
          {
            "scope": "Caller summaries and actual initial playbook production",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-session",
              "memory.md#mem-obj-skill"
            ],
            "note": "Summary-production control and initial playbook production are unresolved; the conditional transcript extraction witness does not classify these alternatives."
          },
          {
            "scope": "Migration/backfill, calibration, complete checkpoint and evaluator-consumer alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-procstats",
              "memory.md#mem-obj-memory",
              "epistemic.md#epi-rte-benchmark-evaluation"
            ],
            "note": "No bounded absence records cover these included alternatives; no local or system-wide no is warranted."
          }
        ],
        "records": [
          "memory.md#mem-rte-outcome-ranking",
          "epistemic.md#epi-rte-outcome-trust",
          "memory.md#mem-obj-access",
          "runtime.md#rt-rte-store-consolidation",
          "memory.md#mem-obj-origin-context",
          "memory.md#mem-rte-fact-retest",
          "epistemic.md#epi-rte-drift-evaluation",
          "memory.md#mem-rte-transcript-harvest",
          "runtime.md#rt-rte-auto-extraction",
          "memory.md#mem-obj-session",
          "memory.md#mem-obj-skill",
          "memory.md#mem-obj-procstats",
          "memory.md#mem-obj-memory",
          "epistemic.md#epi-rte-benchmark-evaluation",
          "memory.md#mem-rte-fact-lifecycle",
          "runtime.md#rt-rte-context-briefing"
        ],
        "note": "Supported wired yes routes include conditional session-text extraction to durable facts for later consumers. Unknown summary, initial-content and maintenance writes retain partial coverage; no absence or improved-capacity conclusion follows."
      },
      "trace_source": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Query activity and search-surfacing access events feeding origin state or coldness maintenance",
            "assessment": "known",
            "findings": [
              {
                "value": "event-streams",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-origin-context",
                  "memory.md#mem-obj-access",
                  "memory.md#mem-rte-fact-retest",
                  "runtime.md#rt-rte-store-consolidation"
                ],
                "note": "Original inputs are discrete query/access activity recorded by the server, not inferred full conversational trajectories."
              }
            ],
            "records": [
              "memory.md#mem-obj-origin-context",
              "memory.md#mem-obj-access",
              "memory.md#mem-rte-fact-retest",
              "runtime.md#rt-rte-store-consolidation"
            ],
            "note": "Original inputs are discrete query/access activity recorded by the server, not inferred full conversational trajectories."
          },
          {
            "scope": "Reported playbook outcomes feeding durable statistics",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-rte-outcome-ranking",
              "memory.md#mem-obj-external-signals"
            ],
            "note": "Reports may originate from humans, model/tool callers or harnesses; API labels do not establish session-log versus tool-trace versus event-stream content of the original experience."
          },
          {
            "scope": "Conversational messages harvested into memory and conditionally extracted into durable facts for later consumption",
            "assessment": "known",
            "findings": [
              {
                "value": "session-logs",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-transcript-harvest",
                  "runtime.md#rt-rte-auto-extraction",
                  "memory.md#mem-rte-fact-lifecycle",
                  "runtime.md#rt-rte-context-briefing"
                ],
                "note": "Original input is recorded user/assistant conversational text. The parser excludes tool/thinking blocks; serialization as candidates and loss of session-specific source metadata do not change the original content's session-log origin. The extraction feature, installation and admission conditions remain; operation is unobserved."
              }
            ],
            "records": [
              "memory.md#mem-rte-transcript-harvest",
              "runtime.md#rt-rte-auto-extraction",
              "memory.md#mem-rte-fact-lifecycle",
              "runtime.md#rt-rte-context-briefing"
            ],
            "note": "Original input is recorded user/assistant conversational text. The parser excludes tool/thinking blocks; serialization as candidates and loss of session-specific source metadata do not change the original content's session-log origin. The extraction feature, installation and admission conditions remain; operation is unobserved."
          },
          {
            "scope": "Caller-summary production alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-session"
            ],
            "note": "The caller supplies a summary but its original input and production control are unresolved."
          },
          {
            "scope": "Untraced initialization and maintenance/evaluator alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-procstats",
              "epistemic.md#epi-rte-benchmark-evaluation"
            ],
            "note": "Source origin for any additional qualifying write is not established."
          }
        ],
        "records": [
          "memory.md#mem-obj-origin-context",
          "memory.md#mem-obj-access",
          "memory.md#mem-rte-fact-retest",
          "runtime.md#rt-rte-store-consolidation",
          "memory.md#mem-rte-outcome-ranking",
          "memory.md#mem-obj-external-signals",
          "memory.md#mem-rte-transcript-harvest",
          "runtime.md#rt-rte-auto-extraction",
          "memory.md#mem-obj-session",
          "memory.md#mem-obj-procstats",
          "epistemic.md#epi-rte-benchmark-evaluation",
          "memory.md#mem-rte-fact-lifecycle",
          "runtime.md#rt-rte-context-briefing"
        ],
        "note": "Session-log input supports conditional transcript extraction; query/access activity supports event-streams. Outcome-report origins and summary/initialization alternatives remain unresolved, so coverage stays partial."
      }
    }
  }
}
---

# MGI-Mind memory profile

## Comparison rationale

All findings classify accepted records, not fresh source evidence. No source reads were performed. Bases describe inspected wiring or the separately afforded host-file consumer; no observation or causal benefit is asserted.

Reconciliation supersedes the duplicate epistemic memory, fact, procedure, skill, procstats and external-signal objects with their memory-member declarations. Citations above use those canonical declarations. The provenance part and session-summary part remain distinct from their containers. Route overlaps retain their separate functions rather than being treated as stronger evidence of execution.

Qdrant payload persistence maps to service-object; its operative retrieval indexes additionally map to vector. This does not infer Qdrant's internal disk technology. Dense vectors are parametric representations, while sparse hashed lexical indexes are symbolic. Local model artifacts are not use-updated memory. Arbitrary vault values remain unresolved despite known file storage.

The ordinary wrapper delivers requested note text as knowledge, omitting hit identifiers and scores; see [WF-RTE-response-delivery](workflow.md#wf-rte-response-delivery). Procedure and skill bodies instead supply guidance. Derived outcomes exert ranking authority at code consumers, while experience has learning authority at the update consumer. These are separate paths, not proof of reliable learning or changed answers. Pinned placement alone does not classify arbitrary block text as instruction.

Read-back separates explicit host requests from background retest supply. Context selection and match inside requested operations are not independent pushes. Background bounded candidate selection supports coarse supply to a server evaluator; detailed priority remains unresolved. The known pull paths cannot make the entire signal axis inapplicable.

Curation distinguishes duplicate removal, coldness decay, promotion, withdrawal and replacement from standing-fact consolidation. The conditional worker extracts triples from retained memory text and submits them to durable fact admission; harvested session messages can feed that path. This supports wired consolidation without observed outputs or semantic fidelity. The structural-check limits in [EPI-RTE-extraction-parser](epistemic.md#epi-rte-extraction-parser) constrain semantic warrant, not the implemented curation classification. No faithfulness defect is redescribed as synthesis.

Outcome counters, access-derived maintenance, query-derived drift state and conditional transcript-to-fact extraction establish trace-fed durable behavior-shaping routes. [MEM-RTE-transcript-harvest](memory.md#mem-rte-transcript-harvest) supplies user/assistant session-log input; [RT-RTE-auto-extraction](runtime.md#rt-rte-auto-extraction) supplies the feature- and installation-dependent automatic write; [MEM-RTE-fact-lifecycle](memory.md#mem-rte-fact-lifecycle) and [RT-RTE-context-briefing](runtime.md#rt-rte-context-briefing) supply later consumption. This wired route requires admission, not observed triples, entailment or benefit. Tool/thinking blocks are excluded, so this branch does not establish tool-trace origin. Reported success types do not authenticate tool execution or identify the original trace source. No evidenced-absence record supports a local trace-learning no. Session summaries are retained, but their production and control are not established by the session-end storage call alone. Initial and maintenance alternatives stay unresolved rather than disappearing from the inventory.

The fact typed-signal namespace gap remains local to that bridge; it does not erase playbook ranking or scalar drift state. Briefing checks an upper temporal bound, not complete stored intervals. Full restore, migration/backfill, caches and evaluator-result consumers are incompletely traced; these limits prevent complete-value claims, not the supported findings above.
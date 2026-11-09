---
{
  "type": "agentic-system-analyses/types/agentic-system-memory-profile.md",
  "description": "Cortexes memory comparison of retained vault content, retrieval structures, maintenance state and continuation batons.",
  "run-id": "AAS-2026-11-08-cortexes-af94078f2405-01",
  "source-identity": "https://github.com/xbluesky/cortexes",
  "reviewed-boundary": "2b8e79f0099203e0453147b708346349952bb963",
  "memory-comparison": {
    "version": 2,
    "scope": "Filtered Raw; canonical Notes/Projects and directory/log/markers; Chroma text/summary/embeddings, lexical records and wikilink access graph; resumable review ledger; ephemeral takeoff batons; saved evaluation query/gold and reports. Includes unresolved initial page/label provenance and opaque provider update alternatives where they limit trace-learning claims. Excludes shipped static plugin instructions, ordinary transient result lists, external host transcript retention and provider parameter storage as vault substrates. No private vault or observed run is supplied.",
    "axes": {
      "storage_substrate": {
        "assessment": "known",
        "units": [
          {
            "scope": "Canonical Raw, Notes/Projects, directory/log/markers and takeoff batons",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-raw",
                  "memory.md#mem-obj-notes-projects",
                  "memory.md#mem-obj-distilled-marker",
                  "memory.md#mem-obj-takeoff"
                ],
                "note": "Vault Markdown stores content and control metadata."
              },
              {
                "value": "repo",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-raw",
                  "memory.md#mem-obj-notes-projects",
                  "runtime.md#rt-rte-direct-save"
                ],
                "note": "Git retains canonical page/capture history where configured; batons are excluded by policy."
              }
            ],
            "records": [
              "memory.md#mem-obj-raw",
              "memory.md#mem-obj-notes-projects",
              "memory.md#mem-obj-distilled-marker",
              "memory.md#mem-obj-takeoff",
              "runtime.md#rt-rte-direct-save"
            ],
            "note": "File and optional Git retention are established; no universal remote-persistence guarantee."
          },
          {
            "scope": "Chroma body, summary, metadata and document embeddings",
            "assessment": "known",
            "findings": [
              {
                "value": "vector",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-vectorstore"
                ],
                "note": "Persistent local Chroma collection supplies vector retrieval."
              }
            ],
            "records": [
              "memory.md#mem-obj-vectorstore"
            ],
            "note": "Encoding is not a separate database-engine claim; no inferred SQLite substrate."
          },
          {
            "scope": "Lexical index and resumable review ledger",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-bm25",
                  "memory.md#mem-obj-distill-plan"
                ],
                "note": "Pickle lexical records and JSON plan/cache files persist locally."
              }
            ],
            "records": [
              "memory.md#mem-obj-bm25",
              "memory.md#mem-obj-distill-plan"
            ],
            "note": "These are access/control structures, not canonical prose."
          },
          {
            "scope": "Wikilink access topology",
            "assessment": "known",
            "findings": [
              {
                "value": "graph",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-wikilink-graph"
                ],
                "note": "Adjacency represents resolved page links."
              },
              {
                "value": "in-memory",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-wikilink-graph"
                ],
                "note": "Process-local cache stores the derived graph."
              }
            ],
            "records": [
              "memory.md#mem-obj-wikilink-graph"
            ],
            "note": "Graph is not independently persisted by its module."
          },
          {
            "scope": "Evaluation query/gold corpus and optional report",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "epistemic.md#epi-obj-query-gold",
                  "epistemic.md#epi-rte-eval-score"
                ],
                "note": "JSONL input and optional Markdown scorecard persist on caller paths."
              }
            ],
            "records": [
              "epistemic.md#epi-obj-query-gold",
              "epistemic.md#epi-rte-eval-score"
            ],
            "note": "Stdout-only results are not an additional retained substrate."
          }
        ],
        "records": [
          "memory.md#mem-obj-raw",
          "memory.md#mem-obj-notes-projects",
          "memory.md#mem-obj-distilled-marker",
          "memory.md#mem-obj-takeoff",
          "runtime.md#rt-rte-direct-save",
          "memory.md#mem-obj-vectorstore",
          "memory.md#mem-obj-bm25",
          "memory.md#mem-obj-distill-plan",
          "memory.md#mem-obj-wikilink-graph",
          "epistemic.md#epi-obj-query-gold",
          "epistemic.md#epi-rte-eval-score"
        ],
        "note": "Inventory covers recorded content, access structures and control/evaluation artifacts. External model parameters and host transcripts outside vault retention are excluded, not classified as vault storage."
      },
      "representational_form": {
        "assessment": "known",
        "units": [
          {
            "scope": "Retained prose and later interpretive consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-raw",
                  "memory.md#mem-obj-notes-projects",
                  "memory.md#mem-obj-vectorstore",
                  "memory.md#mem-obj-bm25",
                  "memory.md#mem-bap-page-context"
                ],
                "note": "Raw/page prose and summary/display text reach model or human interpretation."
              },
              {
                "value": "natural-language",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-takeoff",
                  "runtime.md#rt-rte-takeoff-handoff"
                ],
                "note": "Curated continuation prose is prescribed for later adoption."
              }
            ],
            "records": [
              "memory.md#mem-obj-raw",
              "memory.md#mem-obj-notes-projects",
              "memory.md#mem-obj-vectorstore",
              "memory.md#mem-obj-bm25",
              "memory.md#mem-bap-page-context",
              "memory.md#mem-obj-takeoff",
              "runtime.md#rt-rte-takeoff-handoff"
            ],
            "note": "Separate wired retrieval representation from prescribed baton production/adoption."
          },
          {
            "scope": "Control metadata, tokens, links and evaluator fields",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-bm25",
                  "memory.md#mem-obj-wikilink-graph",
                  "memory.md#mem-obj-distill-plan",
                  "memory.md#mem-obj-distilled-marker",
                  "epistemic.md#epi-obj-query-gold",
                  "epistemic.md#epi-rte-eval-score"
                ],
                "note": "Localized token, identity, coverage, eligibility and gold/metric fields have fixed program consumers."
              }
            ],
            "records": [
              "memory.md#mem-obj-bm25",
              "memory.md#mem-obj-wikilink-graph",
              "memory.md#mem-obj-distill-plan",
              "memory.md#mem-obj-distilled-marker",
              "epistemic.md#epi-obj-query-gold",
              "epistemic.md#epi-rte-eval-score"
            ],
            "note": "Natural-language labels in a symbolic envelope do not make every part prose."
          },
          {
            "scope": "Dense document embeddings",
            "assessment": "known",
            "findings": [
              {
                "value": "parametric",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-vectorstore"
                ],
                "note": "Numerical distributed representations supply cosine similarity; these are not locally trained model weights."
              }
            ],
            "records": [
              "memory.md#mem-obj-vectorstore"
            ],
            "note": "This classification concerns retained document representations, not provider training."
          }
        ],
        "records": [
          "memory.md#mem-obj-raw",
          "memory.md#mem-obj-notes-projects",
          "memory.md#mem-obj-vectorstore",
          "memory.md#mem-obj-bm25",
          "memory.md#mem-bap-page-context",
          "memory.md#mem-obj-takeoff",
          "runtime.md#rt-rte-takeoff-handoff",
          "memory.md#mem-obj-wikilink-graph",
          "memory.md#mem-obj-distill-plan",
          "memory.md#mem-obj-distilled-marker",
          "epistemic.md#epi-obj-query-gold",
          "epistemic.md#epi-rte-eval-score"
        ],
        "note": "Mixed objects are split by consumed part. Unavailable provider internals are not included as retained vault artifacts."
      },
      "lineage": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Filtered Raw derived from host work",
            "assessment": "known",
            "findings": [
              {
                "value": "trace-extracted",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-raw",
                  "runtime.md#rt-rte-session-capture"
                ],
                "note": "Transcript filtering/classification derives retained session records."
              }
            ],
            "records": [
              "memory.md#mem-obj-raw",
              "runtime.md#rt-rte-session-capture"
            ],
            "note": "Lossy extraction does not imply semantic preservation."
          },
          {
            "scope": "Subsequent page and baton authorship",
            "assessment": "known",
            "findings": [
              {
                "value": "authored",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-notes-projects",
                  "runtime.md#rt-rte-direct-save"
                ],
                "note": "Evolve prescribes authored pages from user-supplied content."
              },
              {
                "value": "trace-extracted",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-notes-projects",
                  "runtime.md#rt-rte-distill-review",
                  "memory.md#mem-obj-takeoff"
                ],
                "note": "Distill drafts and takeoff curation draw on recorded or current session experience."
              }
            ],
            "records": [
              "memory.md#mem-obj-notes-projects",
              "runtime.md#rt-rte-direct-save",
              "runtime.md#rt-rte-distill-review",
              "memory.md#mem-obj-takeoff"
            ],
            "note": "Specific outputs are not supplied; classify prescribed derivation paths, not verified fidelity."
          },
          {
            "scope": "Initial/private canonical page content",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-notes-projects"
            ],
            "note": "Initialization and provenance of particular pre-existing pages are unknown; imported versus authored versus trace-derived lineage cannot be enumerated."
          },
          {
            "scope": "Derived lexical, graph, metadata and retrieval representations",
            "assessment": "known",
            "findings": [
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-bm25",
                  "memory.md#mem-obj-wikilink-graph",
                  "memory.md#mem-obj-vectorstore",
                  "memory.md#mem-obj-distill-plan",
                  "memory.md#mem-obj-distilled-marker"
                ],
                "note": "Parsing, graph construction, indexing and ledger accounting compile access/control state."
              },
              {
                "value": "authored",
                "basis": "wired",
                "records": [
                  "epistemic.md#epi-rte-summary-build",
                  "epistemic.md#epi-rte-query-propose"
                ],
                "note": "Model calls produce summary text and candidate queries under automatic software admission."
              }
            ],
            "records": [
              "memory.md#mem-obj-bm25",
              "memory.md#mem-obj-wikilink-graph",
              "memory.md#mem-obj-vectorstore",
              "memory.md#mem-obj-distill-plan",
              "memory.md#mem-obj-distilled-marker",
              "epistemic.md#epi-rte-summary-build",
              "epistemic.md#epi-rte-query-propose"
            ],
            "note": "Known derivation does not settle inherited source provenance."
          },
          {
            "scope": "Evaluator labels supplied from outside proposal route",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "epistemic.md#epi-obj-query-gold",
              "epistemic.md#epi-rte-eval-score"
            ],
            "note": "Loader validates structure, not label author or origin; caller path alone does not establish imported content lineage."
          }
        ],
        "records": [
          "memory.md#mem-obj-raw",
          "runtime.md#rt-rte-session-capture",
          "memory.md#mem-obj-notes-projects",
          "runtime.md#rt-rte-direct-save",
          "runtime.md#rt-rte-distill-review",
          "memory.md#mem-obj-takeoff",
          "memory.md#mem-obj-bm25",
          "memory.md#mem-obj-wikilink-graph",
          "memory.md#mem-obj-vectorstore",
          "memory.md#mem-obj-distill-plan",
          "memory.md#mem-obj-distilled-marker",
          "epistemic.md#epi-rte-summary-build",
          "epistemic.md#epi-rte-query-propose",
          "epistemic.md#epi-obj-query-gold",
          "epistemic.md#epi-rte-eval-score"
        ],
        "note": "Known subsequent derivations coexist with unknown initial page and label origins. No imported finding is inferred merely from external I/O."
      },
      "behavioral_authority": {
        "assessment": "known",
        "units": [
          {
            "scope": "Page/Raw/display content to foreground reasoning and maintenance",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-bap-page-context",
                  "runtime.md#rt-rte-vault-search",
                  "runtime.md#rt-rte-distill-review"
                ],
                "note": "Retained content supplies reference/context, not verified truth."
              }
            ],
            "records": [
              "memory.md#mem-bap-page-context",
              "runtime.md#rt-rte-vault-search",
              "runtime.md#rt-rte-distill-review"
            ],
            "note": "Ledger wiring and delivery do not prove model compliance."
          },
          {
            "scope": "Continuation baton to later foreground host",
            "assessment": "known",
            "findings": [
              {
                "value": "instruction",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-takeoff",
                  "runtime.md#rt-rte-takeoff-handoff"
                ],
                "note": "Goal/progress/next steps are adopted as continuing work guidance."
              },
              {
                "value": "knowledge",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-takeoff",
                  "runtime.md#rt-rte-takeoff-handoff"
                ],
                "note": "Retained work facts also supply continuation context."
              }
            ],
            "records": [
              "memory.md#mem-obj-takeoff",
              "runtime.md#rt-rte-takeoff-handoff"
            ],
            "note": "Directions and contextual claims share an interpreted consumer, not executable authority."
          },
          {
            "scope": "Retained page text, summaries, embeddings, lexical tokens and graph links to retrieval",
            "assessment": "known",
            "findings": [
              {
                "value": "ranking",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-vectorstore",
                  "memory.md#mem-obj-bm25",
                  "memory.md#mem-obj-wikilink-graph",
                  "runtime.md#rt-rte-vault-search"
                ],
                "note": "Retained features determine candidate discovery and relative priority."
              },
              {
                "value": "routing",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-vectorstore",
                  "memory.md#mem-obj-wikilink-graph",
                  "runtime.md#rt-rte-vault-search"
                ],
                "note": "Paths, repo/type metadata and topology select candidate scope and page destinations."
              }
            ],
            "records": [
              "memory.md#mem-obj-vectorstore",
              "memory.md#mem-obj-bm25",
              "memory.md#mem-obj-wikilink-graph",
              "runtime.md#rt-rte-vault-search"
            ],
            "note": "Fixed ranking code still gives retained inputs ranking authority."
          },
          {
            "scope": "Review ledger and processed markers to page API and queues",
            "assessment": "known",
            "findings": [
              {
                "value": "validation",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-distill-plan",
                  "runtime.md#rt-rte-distill-review"
                ],
                "note": "Source identities, coverage and expected outcome determine API admissibility."
              },
              {
                "value": "enforcement",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-distill-plan",
                  "runtime.md#rt-rte-distill-review"
                ],
                "note": "Failed checks reject pages/sealing/completion on these APIs."
              },
              {
                "value": "routing",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-distill-plan",
                  "memory.md#mem-obj-distilled-marker"
                ],
                "note": "Cursors, active plan and processed outcomes determine next source windows and queue eligibility."
              },
              {
                "value": "enforcement",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-distilled-marker",
                  "runtime.md#rt-rte-distill-review"
                ],
                "note": "Processed states exclude Raw from the relevant eligibility queues."
              }
            ],
            "records": [
              "memory.md#mem-obj-distill-plan",
              "memory.md#mem-obj-distilled-marker",
              "runtime.md#rt-rte-distill-review"
            ],
            "note": "Controls do not attest cognition or prevent alternate direct reads."
          },
          {
            "scope": "Session experience to automatic continuation author",
            "assessment": "known",
            "findings": [
              {
                "value": "learning",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-takeoff",
                  "runtime.md#rt-rte-takeoff-handoff"
                ],
                "note": "Work trace feeds a durable continuation artifact for a later session without per-content approval."
              }
            ],
            "records": [
              "memory.md#mem-obj-takeoff",
              "runtime.md#rt-rte-takeoff-handoff"
            ],
            "note": "Learning authority at update consumer is separate from the output's instruction/knowledge authority and from demonstrated improvement."
          },
          {
            "scope": "Saved query/gold corpus to offline evaluator",
            "assessment": "known",
            "findings": [
              {
                "value": "validation",
                "basis": "wired",
                "records": [
                  "epistemic.md#epi-obj-query-gold",
                  "epistemic.md#epi-rte-eval-score"
                ],
                "note": "Gold membership supplies reference criteria for path-agreement metrics."
              },
              {
                "value": "routing",
                "basis": "wired",
                "records": [
                  "epistemic.md#epi-obj-query-gold",
                  "epistemic.md#epi-rte-eval-score"
                ],
                "note": "Queries and selected gold paths determine evaluation cases."
              }
            ],
            "records": [
              "epistemic.md#epi-obj-query-gold",
              "epistemic.md#epi-rte-eval-score"
            ],
            "note": "Reports have no wired production-policy updater. Log entries lacking a later decision consumer are not assigned authority."
          }
        ],
        "records": [
          "memory.md#mem-bap-page-context",
          "runtime.md#rt-rte-vault-search",
          "runtime.md#rt-rte-distill-review",
          "memory.md#mem-obj-takeoff",
          "runtime.md#rt-rte-takeoff-handoff",
          "memory.md#mem-obj-vectorstore",
          "memory.md#mem-obj-bm25",
          "memory.md#mem-obj-wikilink-graph",
          "memory.md#mem-obj-distill-plan",
          "memory.md#mem-obj-distilled-marker",
          "epistemic.md#epi-obj-query-gold",
          "epistemic.md#epi-rte-eval-score"
        ],
        "note": "Authority is consumer-specific across the recorded inventory. Static plugin method guidance is excluded; unconsumed log/scorecard metadata has no asserted behavioral force."
      },
      "write_agency": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Session capture and derived index/ledger accounting",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-session-capture",
                  "memory.md#mem-obj-vectorstore",
                  "memory.md#mem-obj-bm25",
                  "memory.md#mem-obj-wikilink-graph",
                  "memory.md#mem-obj-distill-plan",
                  "epistemic.md#epi-rte-query-propose"
                ],
                "note": "Software/model admission has no per-content human approval inside these mechanisms."
              }
            ],
            "records": [
              "runtime.md#rt-rte-session-capture",
              "memory.md#mem-obj-vectorstore",
              "memory.md#mem-obj-bm25",
              "memory.md#mem-obj-wikilink-graph",
              "memory.md#mem-obj-distill-plan",
              "epistemic.md#epi-rte-query-propose"
            ],
            "note": "Starting rebuild or proposal does not make the subsequent content admission manual."
          },
          {
            "scope": "Distill draft and broadcast edit admission",
            "assessment": "known",
            "findings": [
              {
                "value": "manual",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-distill-review",
                  "runtime.md#rt-rte-broadcast-edit",
                  "memory.md#mem-obj-notes-projects"
                ],
                "note": "Human verdict/draft and per-change decisions are expressly prescribed."
              }
            ],
            "records": [
              "runtime.md#rt-rte-distill-review",
              "runtime.md#rt-rte-broadcast-edit",
              "memory.md#mem-obj-notes-projects"
            ],
            "note": "Policy, not an executable confirmation monitor."
          },
          {
            "scope": "Direct evolve content supply and generated page admission",
            "assessment": "known",
            "findings": [
              {
                "value": "manual",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-direct-save",
                  "memory.md#mem-obj-notes-projects"
                ],
                "note": "User explicitly supplies content in a save request."
              },
              {
                "value": "automatic",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-direct-save",
                  "memory.md#mem-obj-notes-projects"
                ],
                "note": "Model chooses authored page content/placement with no mandatory final draft gate."
              }
            ],
            "records": [
              "runtime.md#rt-rte-direct-save",
              "memory.md#mem-obj-notes-projects"
            ],
            "note": "Human supply and later model admission are distinct mechanisms."
          },
          {
            "scope": "Takeoff content selection and overwrite",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-takeoff",
                  "runtime.md#rt-rte-takeoff-handoff"
                ],
                "note": "Model curates and writes the baton after handoff initiation without separate content approval."
              }
            ],
            "records": [
              "memory.md#mem-obj-takeoff",
              "runtime.md#rt-rte-takeoff-handoff"
            ],
            "note": "User-triggered workflow is not per-content approval."
          },
          {
            "scope": "Reclaim apply and automatic maintenance skip",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-reclaim-raw",
                  "runtime.md#rt-rte-session-capture",
                  "memory.md#mem-obj-distilled-marker"
                ],
                "note": "Prefix checks/deletion and recognized meta-session skip require no per-file decision."
              }
            ],
            "records": [
              "memory.md#mem-rte-reclaim-raw",
              "runtime.md#rt-rte-session-capture",
              "memory.md#mem-obj-distilled-marker"
            ],
            "note": "This is control of admission/removal, not authorship."
          },
          {
            "scope": "Initial pages, externally supplied gold and caller-directed index withdrawal decision",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-notes-projects",
              "epistemic.md#epi-obj-query-gold",
              "memory.md#mem-rte-index-delete"
            ],
            "note": "Private initialization, label authorship and generic deletion-caller identity do not establish who decided that retained content change."
          }
        ],
        "records": [
          "runtime.md#rt-rte-session-capture",
          "memory.md#mem-obj-vectorstore",
          "memory.md#mem-obj-bm25",
          "memory.md#mem-obj-wikilink-graph",
          "memory.md#mem-obj-distill-plan",
          "epistemic.md#epi-rte-query-propose",
          "runtime.md#rt-rte-distill-review",
          "runtime.md#rt-rte-broadcast-edit",
          "memory.md#mem-obj-notes-projects",
          "runtime.md#rt-rte-direct-save",
          "memory.md#mem-obj-takeoff",
          "runtime.md#rt-rte-takeoff-handoff",
          "memory.md#mem-rte-reclaim-raw",
          "memory.md#mem-obj-distilled-marker",
          "epistemic.md#epi-obj-query-gold",
          "memory.md#mem-rte-index-delete"
        ],
        "note": "Known manual policies and automatic mechanisms do not resolve generic callers or pre-existing content."
      },
      "curation_operations": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Session capture reductions and redundant Raw reclamation",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-raw",
                  "runtime.md#rt-rte-session-capture"
                ],
                "note": "Filtering/sampling compresses retained activity into Raw."
              },
              {
                "value": "dedup",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-session-capture",
                  "memory.md#mem-rte-reclaim-raw"
                ],
                "note": "Selected repetitive blocks and prefix-covered Raw records are reduced/removed."
              }
            ],
            "records": [
              "memory.md#mem-obj-raw",
              "runtime.md#rt-rte-session-capture",
              "memory.md#mem-rte-reclaim-raw"
            ],
            "note": "Preservation is bounded to retained content/body comparisons, not every metadata fact."
          },
          {
            "scope": "Bilingual summary indexing",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "wired",
                "records": [
                  "epistemic.md#epi-rte-summary-build",
                  "memory.md#mem-obj-vectorstore"
                ],
                "note": "Bounded page material is reduced to a retrieval summary or title/tags fallback."
              }
            ],
            "records": [
              "epistemic.md#epi-rte-summary-build",
              "memory.md#mem-obj-vectorstore"
            ],
            "note": "Request/retention is wired; faithful semantics and particular generated claims are not observed."
          },
          {
            "scope": "Distill, broadcast and continuation maintenance",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-distill-review",
                  "memory.md#mem-obj-takeoff"
                ],
                "note": "Extracting standing session content and curating continuation compress retained experience."
              },
              {
                "value": "evolve",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-broadcast-edit",
                  "runtime.md#rt-rte-takeoff-handoff"
                ],
                "note": "Exact-section edits and replacement of an active topic baton revise retained entries."
              }
            ],
            "records": [
              "runtime.md#rt-rte-distill-review",
              "runtime.md#rt-rte-broadcast-edit",
              "runtime.md#rt-rte-takeoff-handoff",
              "memory.md#mem-obj-takeoff"
            ],
            "note": "Contradiction flags alone do not establish invalidate; a candidate search threshold is not implemented dedup."
          },
          {
            "scope": "Semantic novelty or invalidation of particular private page revisions",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-notes-projects",
              "runtime.md#rt-rte-broadcast-edit"
            ],
            "note": "No paired inputs/outputs establish synthesis, entailed derivation or withdrawal of reliance for actual page claims."
          }
        ],
        "records": [
          "memory.md#mem-obj-raw",
          "runtime.md#rt-rte-session-capture",
          "memory.md#mem-rte-reclaim-raw",
          "epistemic.md#epi-rte-summary-build",
          "memory.md#mem-obj-vectorstore",
          "runtime.md#rt-rte-distill-review",
          "runtime.md#rt-rte-broadcast-edit",
          "runtime.md#rt-rte-takeoff-handoff",
          "memory.md#mem-obj-takeoff",
          "memory.md#mem-obj-notes-projects"
        ],
        "note": "Index rebuild/acquisition and explicit index deletion alone are not semantic curation. Baton trash pruning is operational cleanup, not an inferred salience-decay mechanism. Supported consolidation remains despite unknown output semantics."
      },
      "read_back_direction": {
        "assessment": "known",
        "units": [
          {
            "scope": "Query/full-page, archive/maintenance and baton resume requests",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-vault-search",
                  "runtime.md#rt-rte-distill-review"
                ],
                "note": "Queries and selected map/span requests return accumulated content."
              },
              {
                "value": "pull",
                "basis": "afforded",
                "records": [
                  "memory.md#mem-rte-raw-view"
                ],
                "note": "Alternative CLI Raw projection supports requested later reading."
              },
              {
                "value": "pull",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-takeoff-handoff"
                ],
                "note": "Explicit resume loads selected full baton."
              }
            ],
            "records": [
              "runtime.md#rt-rte-vault-search",
              "runtime.md#rt-rte-distill-review",
              "memory.md#mem-rte-raw-view",
              "runtime.md#rt-rte-takeoff-handoff"
            ],
            "note": "Requested delivery is not a second push operation."
          },
          {
            "scope": "SessionStart topic and baton-preview supply",
            "assessment": "known",
            "findings": [
              {
                "value": "push",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-session-start",
                  "memory.md#mem-obj-takeoff"
                ],
                "note": "Lifecycle start supplies retained topic metadata and repo-scoped baton previews without a content request."
              }
            ],
            "records": [
              "runtime.md#rt-rte-session-start",
              "memory.md#mem-obj-takeoff"
            ],
            "note": "Only metadata/preview is pushed, not full vault or baton body."
          },
          {
            "scope": "Evaluation reload",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "wired",
                "records": [
                  "epistemic.md#epi-obj-query-gold",
                  "epistemic.md#epi-rte-eval-score"
                ],
                "note": "Later eval run explicitly loads a saved query/gold file."
              }
            ],
            "records": [
              "epistemic.md#epi-obj-query-gold",
              "epistemic.md#epi-rte-eval-score"
            ],
            "note": "Scorecard output alone has no wired later production consumer."
          }
        ],
        "records": [
          "runtime.md#rt-rte-vault-search",
          "runtime.md#rt-rte-distill-review",
          "memory.md#mem-rte-raw-view",
          "runtime.md#rt-rte-takeoff-handoff",
          "runtime.md#rt-rte-session-start",
          "memory.md#mem-obj-takeoff",
          "epistemic.md#epi-obj-query-gold",
          "epistemic.md#epi-rte-eval-score"
        ],
        "note": "Direction covers recorded later-consumer routes and their distinct selection/delivery operations; static methods and transient projections are not additional retained checkpoints."
      },
      "read_back_signal": {
        "assessment": "known",
        "units": [
          {
            "scope": "SessionStart availability selection of topic metadata",
            "assessment": "known",
            "findings": [
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-session-start"
                ],
                "note": "Trigger is lifecycle start; vault/topic availability selects top-level names, not query-conditioned page bodies."
              }
            ],
            "records": [
              "runtime.md#rt-rte-session-start"
            ],
            "note": "Availability selection is distinct from identity matching."
          },
          {
            "scope": "SessionStart repo-scoped baton previews",
            "assessment": "known",
            "findings": [
              {
                "value": "identifier",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-session-start",
                  "runtime.md#rt-rte-takeoff-handoff",
                  "memory.md#mem-obj-takeoff"
                ],
                "note": "Lifecycle trigger uses current repo identity to select matching retained topic baton summaries/paths."
              }
            ],
            "records": [
              "runtime.md#rt-rte-session-start",
              "runtime.md#rt-rte-takeoff-handoff",
              "memory.md#mem-obj-takeoff"
            ],
            "note": "Actual repo match selects delivered previews; requested topic full-file read remains pull."
          }
        ],
        "records": [
          "runtime.md#rt-rte-session-start",
          "runtime.md#rt-rte-takeoff-handoff",
          "memory.md#mem-obj-takeoff"
        ],
        "note": "Signals classify automatic push selection only. Vector/lexical/model relevance in a requested search does not add inferred push signals."
      },
      "trace_learning": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Automatic continuation baton curation and later adoption",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-takeoff",
                  "runtime.md#rt-rte-takeoff-handoff"
                ],
                "note": "Mixed session work feeds automatic retained goal/progress/next-step curation for a later host session."
              }
            ],
            "records": [
              "memory.md#mem-obj-takeoff",
              "runtime.md#rt-rte-takeoff-handoff"
            ],
            "note": "No per-content approval is required; prescribed trace-fed continuation qualifies without new knowledge or demonstrated benefit."
          },
          {
            "scope": "Human-admitted distilled/broadcast pages",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-distill-review",
              "runtime.md#rt-rte-broadcast-edit",
              "memory.md#mem-obj-notes-projects"
            ],
            "note": "These admission routes are human-controlled and do not independently establish automatic trace learning; no bounded absence record licenses a local no for every page path."
          },
          {
            "scope": "Automatic summary/index generation from possibly trace-derived pages",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-vectorstore",
              "epistemic.md#epi-rte-summary-build",
              "memory.md#mem-obj-notes-projects"
            ],
            "note": "Software admission and later ranking are known, but original page provenance is unresolved; trace-fed versus nontrace inputs cannot be completely classified."
          },
          {
            "scope": "Provider parameter changes",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-obj-vectorstore",
              "runtime.md#rt-rte-session-capture"
            ],
            "note": "Provider internals are opaque. Calls/embeddings do not show training; no negative is inferred."
          }
        ],
        "records": [
          "memory.md#mem-obj-takeoff",
          "runtime.md#rt-rte-takeoff-handoff",
          "runtime.md#rt-rte-distill-review",
          "runtime.md#rt-rte-broadcast-edit",
          "memory.md#mem-obj-notes-projects",
          "memory.md#mem-obj-vectorstore",
          "epistemic.md#epi-rte-summary-build",
          "runtime.md#rt-rte-session-capture"
        ],
        "note": "A claimed yes exists for the baton, while page/index input provenance and provider behavior prevent complete learning coverage. No system-wide no or observed improvement is asserted."
      },
      "trace_source": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Qualifying continuation baton input",
            "assessment": "known",
            "findings": [
              {
                "value": "session-logs",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-takeoff",
                  "runtime.md#rt-rte-takeoff-handoff"
                ],
                "note": "Current user/model work session supplies goal, progress and decisions."
              },
              {
                "value": "tool-traces",
                "basis": "claimed",
                "records": [
                  "memory.md#mem-obj-takeoff"
                ],
                "note": "Mixed working trace includes tool requests/results that can inform continuation."
              }
            ],
            "records": [
              "memory.md#mem-obj-takeoff",
              "runtime.md#rt-rte-takeoff-handoff"
            ],
            "note": "Input origin, not Markdown or handoff labels, determines source classes."
          },
          {
            "scope": "Potentially qualifying automatic page-summary derivatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-notes-projects",
              "memory.md#mem-obj-vectorstore",
              "epistemic.md#epi-rte-summary-build"
            ],
            "note": "A page prefix hides initial provenance; no complete original-input trace-source classification is possible."
          },
          {
            "scope": "Opaque provider update inputs",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-obj-vectorstore",
              "runtime.md#rt-rte-session-capture"
            ],
            "note": "No recorded provider-internal trace-fed write identifies its inputs."
          }
        ],
        "records": [
          "memory.md#mem-obj-takeoff",
          "runtime.md#rt-rte-takeoff-handoff",
          "memory.md#mem-obj-notes-projects",
          "memory.md#mem-obj-vectorstore",
          "epistemic.md#epi-rte-summary-build",
          "runtime.md#rt-rte-session-capture"
        ],
        "note": "Known baton source classes coexist with unresolved alternatives. Raw retention alone does not establish a qualifying learner; event-streams and trajectories are not inferred from lifecycle triggers or next-step prose."
      }
    }
  }
}
---

# Cortexes memory profile

## Comparison rationale

The comparison separates canonical content, retrieval representations, retained control state and the short-lived continuation channel. The inventory is grounded in [MEM-OBJ-raw](memory.md#mem-obj-raw), [MEM-OBJ-notes-projects](memory.md#mem-obj-notes-projects), [MEM-OBJ-vectorstore](memory.md#mem-obj-vectorstore), [MEM-OBJ-distill-plan](memory.md#mem-obj-distill-plan) and [MEM-OBJ-takeoff](memory.md#mem-obj-takeoff). Known coverage describes the recorded mechanisms, not observed adherence, semantic fidelity or deployed benefit.

Reconciliation supersedes the epistemic Raw and Notes object declarations with their memory counterparts and the epistemic index-withdrawal route with [MEM-RTE-index-delete](memory.md#mem-rte-index-delete). This profile uses those canonical destinations. Summary generation, prefix checking/removal and evaluation subfunctions remain distinct parts rather than duplicate whole-route replacements. Index withdrawal changes access, not truth reliance; the early return can leave BM25 present. No invalidate value is inferred from it.

Manual admission is local to the explicitly prescribed human content decision. Starting takeoff does not approve its generated body. Consequently the continuation chain supports a claimed trace-learning yes, while human-confirmed distillation does not establish an automatic write. The baton has both contextual facts and standing next-step guidance. Its learning role at production and instruction/knowledge roles at the later consumer are separate ([RT-RTE-takeoff-handoff](runtime.md#rt-rte-takeoff-handoff), [RT-BAP-baton-context](runtime.md#rt-bap-baton-context)). Unknown initial page provenance prevents turning every derived summary into a fully classified trace-learning route. No evidenced-absence record supplies a local no.

Requested retrieval can rank by lexical, embedding and model judgments without those becoming push signals. The pushed material is only startup topic metadata and repo-selected baton previews; full-page and full-baton loads remain requested returns ([RT-RTE-session-start](runtime.md#rt-rte-session-start), [RT-RTE-vault-search](runtime.md#rt-rte-vault-search)). A display summary does not license claims about the fidelity of the full payload.

Consolidation denotes implemented or prescribed reduction of retained content, not proven semantic faithfulness. Novel synthesis and factual acceptance cannot be inferred from fluent model output or conversational revision. Evaluation gold has criteria authority at the metric consumer, not factual authority over page contents or a wired production updater ([EPI-RTE-eval-score](epistemic.md#epi-rte-eval-score)).

Source-read log: none. This mapping used only the supplied accepted records and reconciliation; no source ambiguity required a direct source read.

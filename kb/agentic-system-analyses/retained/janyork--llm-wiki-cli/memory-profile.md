---
{
  "type": "agentic-system-analyses/types/agentic-system-memory-profile.md",
  "description": "llm-wiki-cli memory comparison: canonical Wiki and control state, temporal and discussion continuity, private learning stores and later consumer routes.",
  "run-id": "AAS-2026-11-08-llm-wiki-cli-135ef8fbe608-01",
  "source-identity": "https://github.com/janyork/llm-wiki-cli",
  "reviewed-boundary": "e1be6ab30e83947e4b0dba97ba910acfe3bd9821",
  "memory-comparison": {
    "version": 2,
    "scope": "Use-accumulated Wiki sources/pages/purpose/schema, indexes/tags/retrieval feedback, temporal capsules/controls, Discussion, Plan/Todo, Tutor turns/checkpoints/Soul, Book blobs/reports/synthesis, Practice items/responses/grades/scheduler state, archive/replica copies and their maintenance and later-consumer routes. Includes untraced goal/learner-fact updates, private-unit Sync, graph sidecars, restore, host and frontend/cloud alternatives. Excludes shipped static skills, fixed runtime binaries, ordinary transient response/pending buffers and external model/provider internals from the retained-memory inventory.",
    "axes": {
      "storage_substrate": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Canonical Wiki, temporal, Discussion, Plan/Todo, Tutor, Book report/metadata and Practice objects",
            "assessment": "known",
            "findings": [
              {
                "value": "sqlite",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-sources",
                  "memory.md#mem-obj-pages",
                  "memory.md#mem-obj-purpose-schema",
                  "memory.md#mem-obj-retrieval-state",
                  "memory.md#mem-obj-tags",
                  "memory.md#mem-obj-memory-events",
                  "memory.md#mem-obj-memory-controls",
                  "memory.md#mem-obj-discussion-items",
                  "memory.md#mem-obj-plans",
                  "memory.md#mem-obj-todo-items",
                  "memory.md#mem-obj-tutor-turns",
                  "memory.md#mem-obj-soul",
                  "memory.md#mem-obj-book-reports",
                  "memory.md#mem-obj-practice-items",
                  "memory.md#mem-obj-practice-responses",
                  "memory.md#mem-obj-fsrs-cards"
                ],
                "note": "Records identify selected Wiki SQLite or independent private plugin SQLite; these are separate stores, not a single shared database."
              }
            ],
            "records": [
              "memory.md#mem-obj-sources",
              "memory.md#mem-obj-pages",
              "memory.md#mem-obj-purpose-schema",
              "memory.md#mem-obj-retrieval-state",
              "memory.md#mem-obj-tags",
              "memory.md#mem-obj-memory-events",
              "memory.md#mem-obj-memory-controls",
              "memory.md#mem-obj-discussion-items",
              "memory.md#mem-obj-plans",
              "memory.md#mem-obj-todo-items",
              "memory.md#mem-obj-tutor-turns",
              "memory.md#mem-obj-soul",
              "memory.md#mem-obj-book-reports",
              "memory.md#mem-obj-practice-items",
              "memory.md#mem-obj-practice-responses",
              "memory.md#mem-obj-fsrs-cards"
            ],
            "note": "Records identify selected Wiki SQLite or independent private plugin SQLite; these are separate stores, not a single shared database."
          },
          {
            "scope": "Rebuildable Wiki/Soul projections and Book original/normalized blobs",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-pages",
                  "memory.md#mem-obj-soul",
                  "memory.md#mem-obj-book-blocks"
                ],
                "note": "Materialized Markdown and content-addressed Book files are retained alongside canonical tables."
              }
            ],
            "records": [
              "memory.md#mem-obj-pages",
              "memory.md#mem-obj-soul",
              "memory.md#mem-obj-book-blocks"
            ],
            "note": "Materialized Markdown and content-addressed Book files are retained alongside canonical tables."
          },
          {
            "scope": "Graph sidecar storage internals and included cloud/private-unit Sync storage transformations",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-obj-derived-indexes",
              "runtime.md#rt-rte-team-sync"
            ],
            "note": "Sidecars and transfer payloads are included; records do not determine every operative backing substrate. Graph output alone does not establish a graph database."
          }
        ],
        "records": [
          "memory.md#mem-obj-sources",
          "memory.md#mem-obj-pages",
          "memory.md#mem-obj-purpose-schema",
          "memory.md#mem-obj-retrieval-state",
          "memory.md#mem-obj-tags",
          "memory.md#mem-obj-memory-events",
          "memory.md#mem-obj-memory-controls",
          "memory.md#mem-obj-discussion-items",
          "memory.md#mem-obj-plans",
          "memory.md#mem-obj-todo-items",
          "memory.md#mem-obj-tutor-turns",
          "memory.md#mem-obj-soul",
          "memory.md#mem-obj-book-reports",
          "memory.md#mem-obj-practice-items",
          "memory.md#mem-obj-practice-responses",
          "memory.md#mem-obj-fsrs-cards",
          "memory.md#mem-obj-book-blocks",
          "memory.md#mem-obj-derived-indexes",
          "runtime.md#rt-rte-team-sync"
        ],
        "note": "Included retained content, control metadata, derived indexes and transported copies; unresolved sidecar/cloud alternatives prevent complete substrate coverage. External provider weights and installed fixed binaries are excluded from use-accumulated memory."
      },
      "representational_form": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Readable evidence, Wiki, temporal capsules, Discussion text, task guidance, Tutor/Soul, Book normalized text/reports and Practice prose",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-sources",
                  "memory.md#mem-obj-pages",
                  "memory.md#mem-obj-purpose-schema",
                  "memory.md#mem-obj-retrieval-state",
                  "memory.md#mem-obj-tags",
                  "memory.md#mem-obj-memory-events",
                  "memory.md#mem-obj-memory-controls",
                  "memory.md#mem-obj-discussion-items",
                  "memory.md#mem-obj-plans",
                  "memory.md#mem-obj-todo-items",
                  "memory.md#mem-obj-tutor-turns",
                  "memory.md#mem-obj-soul",
                  "memory.md#mem-obj-book-reports",
                  "memory.md#mem-obj-practice-items",
                  "memory.md#mem-obj-practice-responses",
                  "memory.md#mem-obj-fsrs-cards",
                  "memory.md#mem-obj-book-blocks"
                ],
                "note": "Agent/human interpretation consumes these prose parts; this does not classify their IDs or scores."
              }
            ],
            "records": [
              "memory.md#mem-obj-sources",
              "memory.md#mem-obj-pages",
              "memory.md#mem-obj-purpose-schema",
              "memory.md#mem-obj-retrieval-state",
              "memory.md#mem-obj-tags",
              "memory.md#mem-obj-memory-events",
              "memory.md#mem-obj-memory-controls",
              "memory.md#mem-obj-discussion-items",
              "memory.md#mem-obj-plans",
              "memory.md#mem-obj-todo-items",
              "memory.md#mem-obj-tutor-turns",
              "memory.md#mem-obj-soul",
              "memory.md#mem-obj-book-reports",
              "memory.md#mem-obj-practice-items",
              "memory.md#mem-obj-practice-responses",
              "memory.md#mem-obj-fsrs-cards",
              "memory.md#mem-obj-book-blocks"
            ],
            "note": "Agent/human interpretation consumes these prose parts; this does not classify their IDs or scores."
          },
          {
            "scope": "IDs, citations, hashes, bindings, flags, control metadata, lexical indexes and scheduler state",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-sources",
                  "memory.md#mem-obj-pages",
                  "memory.md#mem-obj-purpose-schema",
                  "memory.md#mem-obj-retrieval-state",
                  "memory.md#mem-obj-tags",
                  "memory.md#mem-obj-memory-events",
                  "memory.md#mem-obj-memory-controls",
                  "memory.md#mem-obj-discussion-items",
                  "memory.md#mem-obj-plans",
                  "memory.md#mem-obj-todo-items",
                  "memory.md#mem-obj-tutor-turns",
                  "memory.md#mem-obj-soul",
                  "memory.md#mem-obj-book-reports",
                  "memory.md#mem-obj-practice-items",
                  "memory.md#mem-obj-practice-responses",
                  "memory.md#mem-obj-fsrs-cards",
                  "memory.md#mem-obj-derived-indexes",
                  "memory.md#mem-obj-book-blocks"
                ],
                "note": "Code interprets localized fields, numeric FSRS cards, FTS tokens and revision/coverage controls. Numbers alone are not parametric form."
              }
            ],
            "records": [
              "memory.md#mem-obj-sources",
              "memory.md#mem-obj-pages",
              "memory.md#mem-obj-purpose-schema",
              "memory.md#mem-obj-retrieval-state",
              "memory.md#mem-obj-tags",
              "memory.md#mem-obj-memory-events",
              "memory.md#mem-obj-memory-controls",
              "memory.md#mem-obj-discussion-items",
              "memory.md#mem-obj-plans",
              "memory.md#mem-obj-todo-items",
              "memory.md#mem-obj-tutor-turns",
              "memory.md#mem-obj-soul",
              "memory.md#mem-obj-book-reports",
              "memory.md#mem-obj-practice-items",
              "memory.md#mem-obj-practice-responses",
              "memory.md#mem-obj-fsrs-cards",
              "memory.md#mem-obj-derived-indexes",
              "memory.md#mem-obj-book-blocks"
            ],
            "note": "Code interprets localized fields, numeric FSRS cards, FTS tokens and revision/coverage controls. Numbers alone are not parametric form."
          },
          {
            "scope": "Opaque original PDF/EPUB Book bytes and untraced sidecar/cloud payload consumption",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-book-blocks",
              "memory.md#mem-obj-derived-indexes",
              "runtime.md#rt-rte-team-sync"
            ],
            "note": "Readable normalized text cannot classify original opaque bytes or every downstream representation."
          }
        ],
        "records": [
          "memory.md#mem-obj-sources",
          "memory.md#mem-obj-pages",
          "memory.md#mem-obj-purpose-schema",
          "memory.md#mem-obj-retrieval-state",
          "memory.md#mem-obj-tags",
          "memory.md#mem-obj-memory-events",
          "memory.md#mem-obj-memory-controls",
          "memory.md#mem-obj-discussion-items",
          "memory.md#mem-obj-plans",
          "memory.md#mem-obj-todo-items",
          "memory.md#mem-obj-tutor-turns",
          "memory.md#mem-obj-soul",
          "memory.md#mem-obj-book-reports",
          "memory.md#mem-obj-practice-items",
          "memory.md#mem-obj-practice-responses",
          "memory.md#mem-obj-fsrs-cards",
          "memory.md#mem-obj-book-blocks",
          "memory.md#mem-obj-derived-indexes",
          "runtime.md#rt-rte-team-sync"
        ],
        "note": "Mixed objects are split by prose versus fixed-rule consumers. No dense or learned representation is established by inspected indexes; opaque originals and delivery alternatives retain uncertainty."
      },
      "lineage": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Caller-authored Wiki, purpose/schema, task records, Soul and assessment items",
            "assessment": "known",
            "findings": [
              {
                "value": "authored",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-pages",
                  "memory.md#mem-obj-purpose-schema",
                  "memory.md#mem-obj-plans",
                  "memory.md#mem-obj-todo-items",
                  "memory.md#mem-obj-soul",
                  "memory.md#mem-obj-practice-items"
                ],
                "note": "Records identify supplied replacements/guidance; authorship is not human approval."
              }
            ],
            "records": [
              "memory.md#mem-obj-pages",
              "memory.md#mem-obj-purpose-schema",
              "memory.md#mem-obj-plans",
              "memory.md#mem-obj-todo-items",
              "memory.md#mem-obj-soul",
              "memory.md#mem-obj-practice-items"
            ],
            "note": "Records identify supplied replacements/guidance; authorship is not human approval."
          },
          {
            "scope": "Immutable external sources, Book originals and archive/replica copies",
            "assessment": "known",
            "findings": [
              {
                "value": "imported",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-sources",
                  "memory.md#mem-obj-book-blocks",
                  "memory.md#mem-rte-archive-admit",
                  "runtime.md#rt-rte-team-sync"
                ],
                "note": "Acquisition preserves a retained input or copy; initial authorship and converter fidelity remain separate."
              }
            ],
            "records": [
              "memory.md#mem-obj-sources",
              "memory.md#mem-obj-book-blocks",
              "memory.md#mem-rte-archive-admit",
              "runtime.md#rt-rte-team-sync"
            ],
            "note": "Acquisition preserves a retained input or copy; initial authorship and converter fidelity remain separate."
          },
          {
            "scope": "Normalized Book blocks, indexes, objective grades and derived scheduler state",
            "assessment": "known",
            "findings": [
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-book-blocks",
                  "memory.md#mem-obj-derived-indexes",
                  "epistemic.md#epi-rte-practice-grade",
                  "memory.md#mem-rte-practice-review"
                ],
                "note": "Code normalization, indexing, exact comparison and fixed-rule scheduling derive retained parts without establishing new semantic claims."
              }
            ],
            "records": [
              "memory.md#mem-obj-book-blocks",
              "memory.md#mem-obj-derived-indexes",
              "epistemic.md#epi-rte-practice-grade",
              "memory.md#mem-rte-practice-review"
            ],
            "note": "Code normalization, indexing, exact comparison and fixed-rule scheduling derive retained parts without establishing new semantic claims."
          },
          {
            "scope": "Selected temporal experience capsules, Discussion summaries and teaching checkpoints",
            "assessment": "known",
            "findings": [
              {
                "value": "trace-extracted",
                "basis": "afforded",
                "records": [
                  "memory.md#mem-obj-memory-events",
                  "memory.md#mem-obj-discussion-items",
                  "memory.md#mem-obj-tutor-turns"
                ],
                "note": "Selected experience/visible exchanges are distinct from raw replies and exact I/O. Extraction is agent-mediated, not a hidden transcript collector."
              }
            ],
            "records": [
              "memory.md#mem-obj-memory-events",
              "memory.md#mem-obj-discussion-items",
              "memory.md#mem-obj-tutor-turns"
            ],
            "note": "Selected experience/visible exchanges are distinct from raw replies and exact I/O. Extraction is agent-mediated, not a hidden transcript collector."
          },
          {
            "scope": "Initial provenance/conversion fidelity and complete learner-fact/Soul, graph and private Sync derivations",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-sources",
              "memory.md#mem-obj-book-blocks",
              "memory.md#mem-obj-soul",
              "memory.md#mem-obj-derived-indexes",
              "runtime.md#rt-rte-team-sync"
            ],
            "note": "Known subsequent derivation does not settle all initial inputs or opaque transformations."
          }
        ],
        "records": [
          "memory.md#mem-obj-pages",
          "memory.md#mem-obj-purpose-schema",
          "memory.md#mem-obj-plans",
          "memory.md#mem-obj-todo-items",
          "memory.md#mem-obj-soul",
          "memory.md#mem-obj-practice-items",
          "memory.md#mem-obj-sources",
          "memory.md#mem-obj-book-blocks",
          "memory.md#mem-rte-archive-admit",
          "runtime.md#rt-rte-team-sync",
          "memory.md#mem-obj-derived-indexes",
          "epistemic.md#epi-rte-practice-grade",
          "memory.md#mem-rte-practice-review",
          "memory.md#mem-obj-memory-events",
          "memory.md#mem-obj-discussion-items",
          "memory.md#mem-obj-tutor-turns"
        ],
        "note": "Supported derivation paths coexist; citation linkage is not proof of original authorship, truth or faithful conversion."
      },
      "behavioral_authority": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Evidence/page/capsule/Discussion/Book/response content at later agent and human reference consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-bap-wiki-context",
                  "memory.md#mem-bap-discussion-summary",
                  "memory.md#mem-rte-source-admit",
                  "memory.md#mem-rte-book-window",
                  "memory.md#mem-rte-practice-assess"
                ],
                "note": "Retained content supplies evidence and context, not an enforced instruction hierarchy."
              }
            ],
            "records": [
              "runtime.md#rt-bap-wiki-context",
              "memory.md#mem-bap-discussion-summary",
              "memory.md#mem-rte-source-admit",
              "memory.md#mem-rte-book-window",
              "memory.md#mem-rte-practice-assess"
            ],
            "note": "Retained content supplies evidence and context, not an enforced instruction hierarchy."
          },
          {
            "scope": "Retained purpose/schema and Soul at explicit-context/teaching consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "instruction",
                "basis": "afforded",
                "records": [
                  "memory.md#mem-obj-purpose-schema",
                  "memory.md#mem-obj-soul",
                  "runtime.md#rt-bap-soul-guidance"
                ],
                "note": "Standing directions shape intended later work; command delivery is implemented, teaching compliance is prescribed."
              }
            ],
            "records": [
              "memory.md#mem-obj-purpose-schema",
              "memory.md#mem-obj-soul",
              "runtime.md#rt-bap-soul-guidance"
            ],
            "note": "Standing directions shape intended later work; command delivery is implemented, teaching compliance is prescribed."
          },
          {
            "scope": "Page/source lexical content and retained retrieval weights, feedback, tag priority and card risk at selectors",
            "assessment": "known",
            "findings": [
              {
                "value": "ranking",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-derived-indexes",
                  "memory.md#mem-rte-retrieval-adjust",
                  "memory.md#mem-rte-temporal-cycle",
                  "memory.md#mem-obj-tags",
                  "memory.md#mem-rte-practice-review"
                ],
                "note": "Fixed code uses retained text/features/scores to set relative priority. Natural-language reasons are not thereby ranking inputs."
              }
            ],
            "records": [
              "memory.md#mem-obj-derived-indexes",
              "memory.md#mem-rte-retrieval-adjust",
              "memory.md#mem-rte-temporal-cycle",
              "memory.md#mem-obj-tags",
              "memory.md#mem-rte-practice-review"
            ],
            "note": "Fixed code uses retained text/features/scores to set relative priority. Natural-language reasons are not thereby ranking inputs."
          },
          {
            "scope": "Book cursor, task tracking, tag enablement/membership and Tutor checkpoint/binding at continuation selectors",
            "assessment": "known",
            "findings": [
              {
                "value": "routing",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-book-window",
                  "memory.md#mem-rte-task-continuity",
                  "runtime.md#rt-rte-hook-context",
                  "runtime.md#rt-rte-tutor-turn"
                ],
                "note": "Retained state selects next ranges, delivered pages/cues and exact recovery scope."
              }
            ],
            "records": [
              "memory.md#mem-rte-book-window",
              "memory.md#mem-rte-task-continuity",
              "runtime.md#rt-rte-hook-context",
              "runtime.md#rt-rte-tutor-turn"
            ],
            "note": "Retained state selects next ranges, delivered pages/cues and exact recovery scope."
          },
          {
            "scope": "Retained revisions, leases, source hashes, verified/retired state and frozen answer/rubric bindings at admission/check consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "validation",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-book-window",
                  "epistemic.md#epi-rte-practice-verify",
                  "epistemic.md#epi-rte-practice-grade",
                  "runtime.md#rt-rte-tutor-turn"
                ],
                "note": "Retained criteria determine conformity and code can reject stale identity, inadmissible item state or pending/owner mismatch; equality grading licenses only its fixed domain."
              },
              {
                "value": "enforcement",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-book-window",
                  "epistemic.md#epi-rte-practice-verify",
                  "epistemic.md#epi-rte-practice-grade",
                  "runtime.md#rt-rte-tutor-turn"
                ],
                "note": "Retained criteria determine conformity and code can reject stale identity, inadmissible item state or pending/owner mismatch; equality grading licenses only its fixed domain."
              }
            ],
            "records": [
              "memory.md#mem-rte-book-window",
              "epistemic.md#epi-rte-practice-verify",
              "epistemic.md#epi-rte-practice-grade",
              "runtime.md#rt-rte-tutor-turn"
            ],
            "note": "Retained criteria determine conformity and code can reject stale identity, inadmissible item state or pending/owner mismatch; equality grading licenses only its fixed domain."
          },
          {
            "scope": "Review rating/history and prior card at automatic scheduler update",
            "assessment": "known",
            "findings": [
              {
                "value": "learning",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-practice-review",
                  "memory.md#mem-bap-review-schedule"
                ],
                "note": "Experience feeds a durable behavior-shaping card; downstream queue routing/ranking is a separate consumer. No improved capacity is established."
              }
            ],
            "records": [
              "memory.md#mem-rte-practice-review",
              "memory.md#mem-bap-review-schedule"
            ],
            "note": "Experience feeds a durable behavior-shaping card; downstream queue routing/ranking is a separate consumer. No improved capacity is established."
          },
          {
            "scope": "Complete learner-fact/goal updates, private Sync, graph and frontend consumer effects",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-obj-soul",
              "memory.md#mem-obj-derived-indexes",
              "runtime.md#rt-rte-team-sync"
            ],
            "note": "Untraced consumers prevent complete enumeration; no blanket authority is assigned to unconsumed metadata."
          }
        ],
        "records": [
          "runtime.md#rt-bap-wiki-context",
          "memory.md#mem-bap-discussion-summary",
          "memory.md#mem-rte-source-admit",
          "memory.md#mem-rte-book-window",
          "memory.md#mem-rte-practice-assess",
          "memory.md#mem-obj-purpose-schema",
          "memory.md#mem-obj-soul",
          "runtime.md#rt-bap-soul-guidance",
          "memory.md#mem-obj-derived-indexes",
          "memory.md#mem-rte-retrieval-adjust",
          "memory.md#mem-rte-temporal-cycle",
          "memory.md#mem-obj-tags",
          "memory.md#mem-rte-practice-review",
          "memory.md#mem-rte-task-continuity",
          "runtime.md#rt-rte-hook-context",
          "runtime.md#rt-rte-tutor-turn",
          "epistemic.md#epi-rte-practice-verify",
          "epistemic.md#epi-rte-practice-grade",
          "memory.md#mem-bap-review-schedule",
          "runtime.md#rt-rte-team-sync"
        ],
        "note": "Authority is consumer-relative: Wiki remains reference data even in pi's system-prompt envelope. Local controls do not establish universal host enforcement."
      },
      "write_agency": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Conditional host Discussion reply capture and Practice rating-to-card/queue-state admission",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-discussion-capture",
                  "memory.md#mem-rte-practice-review"
                ],
                "note": "Code admits captured reply or derived schedule without a separate human decision approving each retained result."
              }
            ],
            "records": [
              "memory.md#mem-rte-discussion-capture",
              "memory.md#mem-rte-practice-review"
            ],
            "note": "Code admits captured reply or derived schedule without a separate human decision approving each retained result."
          },
          {
            "scope": "Temporal retention/hint metadata and derived index rebuild",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-temporal-cycle",
                  "memory.md#mem-obj-derived-indexes",
                  "runtime.md#rt-rte-work-runner"
                ],
                "note": "Software maintains these parts; initiating a command is not per-result content approval."
              }
            ],
            "records": [
              "memory.md#mem-rte-temporal-cycle",
              "memory.md#mem-obj-derived-indexes",
              "runtime.md#rt-rte-work-runner"
            ],
            "note": "Software maintains these parts; initiating a command is not per-result content approval."
          },
          {
            "scope": "Sensitive/behavior-changing Soul proposals and destructive whole-store archive overwrite under shipped consent policy",
            "assessment": "known",
            "findings": [
              {
                "value": "manual",
                "basis": "claimed",
                "records": [
                  "runtime.md#rt-rte-soul-publish",
                  "memory.md#mem-rte-archive-admit"
                ],
                "note": "Policy requires explicit learner approval or separate human confirmation for the specified retained change. Local approval fields/tokens do not authenticate compliance."
              }
            ],
            "records": [
              "runtime.md#rt-rte-soul-publish",
              "memory.md#mem-rte-archive-admit"
            ],
            "note": "Policy requires explicit learner approval or separate human confirmation for the specified retained change. Local approval fields/tokens do not authenticate compliance."
          },
          {
            "scope": "Generic caller-supplied pages/sources, purpose/schema, tags/feedback, temporal capsules, tasks, Tutor/Soul and Book/Practice submissions",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-page-write",
              "memory.md#mem-rte-source-admit",
              "memory.md#mem-obj-purpose-schema",
              "memory.md#mem-obj-tags",
              "memory.md#mem-rte-retrieval-adjust",
              "memory.md#mem-rte-task-continuity",
              "runtime.md#rt-rte-tutor-turn",
              "runtime.md#rt-rte-soul-publish",
              "memory.md#mem-rte-book-window",
              "memory.md#mem-rte-practice-assess"
            ],
            "note": "External agent/user alternatives and caller-provided provenance do not settle human per-content control for every submission. Physical SQL admission alone does not classify it."
          },
          {
            "scope": "Private-unit Sync, restore and untraced goal/learner-fact admission",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-team-sync",
              "runtime.md#rt-rte-work-runner",
              "memory.md#mem-obj-soul"
            ],
            "note": "Detailed control mechanisms are not in accepted records."
          }
        ],
        "records": [
          "memory.md#mem-rte-discussion-capture",
          "memory.md#mem-rte-practice-review",
          "memory.md#mem-rte-temporal-cycle",
          "memory.md#mem-obj-derived-indexes",
          "runtime.md#rt-rte-work-runner",
          "runtime.md#rt-rte-soul-publish",
          "memory.md#mem-rte-archive-admit",
          "runtime.md#rt-rte-page-write",
          "memory.md#mem-rte-source-admit",
          "memory.md#mem-obj-purpose-schema",
          "memory.md#mem-obj-tags",
          "memory.md#mem-rte-retrieval-adjust",
          "memory.md#mem-rte-task-continuity",
          "runtime.md#rt-rte-tutor-turn",
          "memory.md#mem-rte-book-window",
          "memory.md#mem-rte-practice-assess",
          "runtime.md#rt-rte-team-sync",
          "memory.md#mem-obj-soul"
        ],
        "note": "Classified automatic mechanisms and policy-level human gates are not promoted to a system-wide agency claim."
      },
      "curation_operations": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Page replacement and corrected Book synthesis publication",
            "assessment": "known",
            "findings": [
              {
                "value": "evolve",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-page-write",
                  "memory.md#mem-rte-book-synthesis"
                ],
                "note": "Existing entries have supported replacement/successor mechanisms; code does not establish semantic improvement."
              }
            ],
            "records": [
              "runtime.md#rt-rte-page-write",
              "memory.md#mem-rte-book-synthesis"
            ],
            "note": "Existing entries have supported replacement/successor mechanisms; code does not establish semantic improvement."
          },
          {
            "scope": "Discussion dependency withdrawal/staleness and temporal supersession relations",
            "assessment": "known",
            "findings": [
              {
                "value": "invalidate",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-discussion-revise",
                  "memory.md#mem-rte-temporal-cycle"
                ],
                "note": "Dependent summaries lose current confirmation; explicit supersession can withdraw current reliance while retaining history."
              }
            ],
            "records": [
              "memory.md#mem-rte-discussion-revise",
              "memory.md#mem-rte-temporal-cycle"
            ],
            "note": "Dependent summaries lose current confirmation; explicit supersession can withdraw current reliance while retaining history."
          },
          {
            "scope": "Temporal age/capacity retention",
            "assessment": "known",
            "findings": [
              {
                "value": "decay",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-temporal-cycle"
                ],
                "note": "Automatic eviction forgets eligible retained history; replica preservation is a separate branch."
              }
            ],
            "records": [
              "memory.md#mem-rte-temporal-cycle"
            ],
            "note": "Automatic eviction forgets eligible retained history; replica preservation is a separate branch."
          },
          {
            "scope": "Positive retrieval weights/usefulness signals",
            "assessment": "known",
            "findings": [
              {
                "value": "promote",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-retrieval-adjust",
                  "memory.md#mem-rte-temporal-cycle"
                ],
                "note": "Retained score changes raise selection salience; no semantic truth acceptance follows."
              }
            ],
            "records": [
              "memory.md#mem-rte-retrieval-adjust",
              "memory.md#mem-rte-temporal-cycle"
            ],
            "note": "Retained score changes raise selection salience; no semantic truth acceptance follows."
          },
          {
            "scope": "Agent summaries of visible Discussion and Book windows/hierarchy",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "afforded",
                "records": [
                  "memory.md#mem-rte-discussion-revise",
                  "memory.md#mem-rte-book-window",
                  "memory.md#mem-rte-book-synthesis"
                ],
                "note": "These routes afford reduced accounts of retained material; requested summaries are not observed faithful transformations."
              }
            ],
            "records": [
              "memory.md#mem-rte-discussion-revise",
              "memory.md#mem-rte-book-window",
              "memory.md#mem-rte-book-synthesis"
            ],
            "note": "These routes afford reduced accounts of retained material; requested summaries are not observed faithful transformations."
          },
          {
            "scope": "Duplicate merging, novel semantic synthesis, private Sync/restore and untraced learning revisions",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-book-reports",
              "memory.md#mem-obj-derived-indexes",
              "runtime.md#rt-rte-team-sync",
              "runtime.md#rt-rte-work-runner"
            ],
            "note": "Route names, content hashes and reindexing do not establish dedup or synthesis. No source-to-candidate pair proves a novel claim; other transformations remain uninspected."
          }
        ],
        "records": [
          "runtime.md#rt-rte-page-write",
          "memory.md#mem-rte-book-synthesis",
          "memory.md#mem-rte-discussion-revise",
          "memory.md#mem-rte-temporal-cycle",
          "memory.md#mem-rte-retrieval-adjust",
          "memory.md#mem-rte-book-window",
          "memory.md#mem-obj-book-reports",
          "memory.md#mem-obj-derived-indexes",
          "runtime.md#rt-rte-team-sync",
          "runtime.md#rt-rte-work-runner"
        ],
        "note": "Implemented curation remains separate from agent semantic duties and from database compaction. No novelty or dedup value is inferred from command labels."
      },
      "read_back_direction": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Explicit Wiki/context/search/tag/source, temporal, task/Discussion, Tutor recovery, Book windows and Practice queue requests",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-mcp-recall",
                  "memory.md#mem-rte-source-admit",
                  "memory.md#mem-rte-temporal-cycle",
                  "memory.md#mem-rte-discussion-revise",
                  "memory.md#mem-rte-task-continuity",
                  "runtime.md#rt-rte-tutor-turn",
                  "memory.md#mem-rte-book-window",
                  "memory.md#mem-rte-practice-review"
                ],
                "note": "Code may select retained material within a request, but returning the requested result is pull, including Book's next window and Practice queue."
              }
            ],
            "records": [
              "runtime.md#rt-rte-mcp-recall",
              "memory.md#mem-rte-source-admit",
              "memory.md#mem-rte-temporal-cycle",
              "memory.md#mem-rte-discussion-revise",
              "memory.md#mem-rte-task-continuity",
              "runtime.md#rt-rte-tutor-turn",
              "memory.md#mem-rte-book-window",
              "memory.md#mem-rte-practice-review"
            ],
            "note": "Code may select retained material within a request, but returning the requested result is pull, including Book's next window and Practice queue."
          },
          {
            "scope": "Lifecycle tag-selected pages and context-bound task cues",
            "assessment": "known",
            "findings": [
              {
                "value": "push",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-hook-context",
                  "memory.md#mem-rte-task-continuity"
                ],
                "note": "Mapped host events automatically supply retained bodies/cues without a request for those particular memories; pi appends one-shot context."
              }
            ],
            "records": [
              "runtime.md#rt-rte-hook-context",
              "memory.md#mem-rte-task-continuity"
            ],
            "note": "Mapped host events automatically supply retained bodies/cues without a request for those particular memories; pi appends one-shot context."
          },
          {
            "scope": "Non-pi adapter delivery, frontend/cloud transformations and private-unit Sync consumers",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-hook-context",
              "runtime.md#rt-rte-team-sync",
              "memory.md#mem-obj-book-reports"
            ],
            "note": "Included consumer alternatives are not fully traced; known requested reads do not make them pull-only or absent."
          }
        ],
        "records": [
          "runtime.md#rt-rte-mcp-recall",
          "memory.md#mem-rte-source-admit",
          "memory.md#mem-rte-temporal-cycle",
          "memory.md#mem-rte-discussion-revise",
          "memory.md#mem-rte-task-continuity",
          "runtime.md#rt-rte-tutor-turn",
          "memory.md#mem-rte-book-window",
          "memory.md#mem-rte-practice-review",
          "runtime.md#rt-rte-hook-context",
          "runtime.md#rt-rte-team-sync",
          "memory.md#mem-obj-book-reports"
        ],
        "note": "Both requested retrieval and unsolicited lifecycle supply are wired; no host compliance or complete delivery parity is inferred."
      },
      "read_back_signal": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Lifecycle tag page push",
            "assessment": "known",
            "findings": [
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-hook-context",
                  "memory.md#mem-obj-tags"
                ],
                "note": "Trigger: mapped lifecycle event. Inputs: scope/capabilities and enabled tag membership/priority. Selected retained parts: page bodies. Availability, tag/global limits and render budgets are coarse selection, not inferred semantic relevance."
              }
            ],
            "records": [
              "runtime.md#rt-rte-hook-context",
              "memory.md#mem-obj-tags"
            ],
            "note": "Trigger: mapped lifecycle event. Inputs: scope/capabilities and enabled tag membership/priority. Selected retained parts: page bodies. Availability, tag/global limits and render budgets are coarse selection, not inferred semantic relevance."
          },
          {
            "scope": "Context-bound Plan/Todo cue push",
            "assessment": "known",
            "findings": [
              {
                "value": "identifier",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-task-continuity"
                ],
                "note": "Trigger: host readiness/lifecycle event. Selector matches resolved opaque context to explicit tracking. Delivered parts: tracked Plan continuity and at most three Todo reminders; this is an actual identity-based selection, not just an ID printed in a catalog."
              }
            ],
            "records": [
              "memory.md#mem-rte-task-continuity"
            ],
            "note": "Trigger: host readiness/lifecycle event. Selector matches resolved opaque context to explicit tracking. Delivered parts: tracked Plan continuity and at most three Todo reminders; this is an actual identity-based selection, not just an ID printed in a catalog."
          },
          {
            "scope": "Legacy no-context readiness and non-pi host/frontend supply alternatives",
            "assessment": "uninspected",
            "findings": [],
            "records": [
              "memory.md#mem-rte-task-continuity",
              "runtime.md#rt-rte-hook-context",
              "runtime.md#rt-rte-team-sync"
            ],
            "note": "Aggregate fallback behavior and all delivery selectors are not completely recorded; no lexical, embedding or judgment-based push is inferred from query-driven pull."
          }
        ],
        "records": [
          "runtime.md#rt-rte-hook-context",
          "memory.md#mem-obj-tags",
          "memory.md#mem-rte-task-continuity",
          "runtime.md#rt-rte-team-sync"
        ],
        "note": "Push predicates are classified separately from pull lookup IDs and lexical query search. Incomplete push coverage prevents inapplicability or complete-value claims."
      },
      "trace_learning": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Practice submitted review rating/time to durable FSRS card/debt to later queue",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-practice-review",
                  "memory.md#mem-obj-fsrs-cards",
                  "memory.md#mem-bap-review-schedule"
                ],
                "note": "Code automatically derives retained scheduling state from review experience and later queue selection consumes it. Parameters are fixed here; benefit and rating authenticity are not established."
              }
            ],
            "records": [
              "memory.md#mem-rte-practice-review",
              "memory.md#mem-obj-fsrs-cards",
              "memory.md#mem-bap-review-schedule"
            ],
            "note": "Code automatically derives retained scheduling state from review experience and later queue selection consumes it. Parameters are fixed here; benefit and rating authenticity are not established."
          },
          {
            "scope": "Agent-produced Discussion summaries from retained visible exchanges to explicit recovery/close delivery",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "afforded",
                "records": [
                  "memory.md#mem-rte-discussion-revise",
                  "memory.md#mem-obj-discussion-items",
                  "memory.md#mem-bap-discussion-summary"
                ],
                "note": "Shipped agent summary route affords trace-derived retained context for later use without compulsory approval of every summary. Store accepts supplied summaries; source inspection does not observe model generation or recovery."
              }
            ],
            "records": [
              "memory.md#mem-rte-discussion-revise",
              "memory.md#mem-obj-discussion-items",
              "memory.md#mem-bap-discussion-summary"
            ],
            "note": "Shipped agent summary route affords trace-derived retained context for later use without compulsory approval of every summary. Store accepts supplied summaries; source inspection does not observe model generation or recovery."
          },
          {
            "scope": "Teaching checkpoint from visible turn work to cold/recovery continuation",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "afforded",
                "records": [
                  "runtime.md#rt-rte-tutor-turn",
                  "memory.md#mem-obj-tutor-turns"
                ],
                "note": "Skill-directed external teaching agent retains selected checkpoint/anchor for a later invocation. This is an afforded trace-to-continuation route, not an internal summarizer or proof of improved teaching."
              }
            ],
            "records": [
              "runtime.md#rt-rte-tutor-turn",
              "memory.md#mem-obj-tutor-turns"
            ],
            "note": "Skill-directed external teaching agent retains selected checkpoint/anchor for a later invocation. This is an afforded trace-to-continuation route, not an internal summarizer or proof of improved teaching."
          },
          {
            "scope": "Soul/learner-fact/goal adaptation, generic feedback and Wiki experience write-back, plus private-unit Sync alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-soul-publish",
              "memory.md#mem-obj-soul",
              "memory.md#mem-rte-retrieval-adjust",
              "memory.md#mem-rte-temporal-cycle",
              "runtime.md#rt-rte-team-sync"
            ],
            "note": "Records do not settle complete trace provenance, per-content control and later behavior-shaping transformations for these alternatives. Raw capture alone is insufficient; no bounded absence record supports a local no."
          }
        ],
        "records": [
          "memory.md#mem-rte-practice-review",
          "memory.md#mem-obj-fsrs-cards",
          "memory.md#mem-bap-review-schedule",
          "memory.md#mem-rte-discussion-revise",
          "memory.md#mem-obj-discussion-items",
          "memory.md#mem-bap-discussion-summary",
          "runtime.md#rt-rte-tutor-turn",
          "memory.md#mem-obj-tutor-turns",
          "runtime.md#rt-rte-soul-publish",
          "memory.md#mem-obj-soul",
          "memory.md#mem-rte-retrieval-adjust",
          "memory.md#mem-rte-temporal-cycle",
          "runtime.md#rt-rte-team-sync"
        ],
        "note": "Qualifying scheduler wiring and afforded continuation summaries coexist with unresolved updates. The derived system union supports yes, not a complete inventory or a system-wide no."
      },
      "trace_source": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Practice rating/time input to automatic scheduler update",
            "assessment": "known",
            "findings": [
              {
                "value": "event-streams",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-practice-review",
                  "memory.md#mem-obj-fsrs-cards"
                ],
                "note": "Original content is a discrete learner review event with rating and reviewed time, not a serialized session transcript or linked multi-step trajectory. Caller provenance is not authenticated."
              }
            ],
            "records": [
              "memory.md#mem-rte-practice-review",
              "memory.md#mem-obj-fsrs-cards"
            ],
            "note": "Original content is a discrete learner review event with rating and reviewed time, not a serialized session transcript or linked multi-step trajectory. Caller provenance is not authenticated."
          },
          {
            "scope": "Discussion summary input and Tutor checkpoint input from visible conversational teaching/discussion",
            "assessment": "known",
            "findings": [
              {
                "value": "session-logs",
                "basis": "afforded",
                "records": [
                  "memory.md#mem-obj-discussion-items",
                  "memory.md#mem-rte-discussion-revise",
                  "memory.md#mem-obj-tutor-turns",
                  "runtime.md#rt-rte-tutor-turn"
                ],
                "note": "Visible Q/A or teaching input/reply provide the conversational trace for afforded derived continuity; no hidden chain-of-thought, tool trace or complete host transcript is established."
              }
            ],
            "records": [
              "memory.md#mem-obj-discussion-items",
              "memory.md#mem-rte-discussion-revise",
              "memory.md#mem-obj-tutor-turns",
              "runtime.md#rt-rte-tutor-turn"
            ],
            "note": "Visible Q/A or teaching input/reply provide the conversational trace for afforded derived continuity; no hidden chain-of-thought, tool trace or complete host transcript is established."
          },
          {
            "scope": "Mixed or opaque inputs to Soul/learner-fact, feedback/Wiki updates and untraced learning alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "memory.md#mem-obj-soul",
              "runtime.md#rt-rte-soul-publish",
              "memory.md#mem-rte-retrieval-adjust",
              "memory.md#mem-rte-temporal-cycle",
              "runtime.md#rt-rte-team-sync"
            ],
            "note": "Original trace content and qualifying automatic chains are unresolved. No source values are inferred from labels like learned, fact, event or synthesis."
          }
        ],
        "records": [
          "memory.md#mem-rte-practice-review",
          "memory.md#mem-obj-fsrs-cards",
          "memory.md#mem-obj-discussion-items",
          "memory.md#mem-rte-discussion-revise",
          "memory.md#mem-obj-tutor-turns",
          "runtime.md#rt-rte-tutor-turn",
          "memory.md#mem-obj-soul",
          "runtime.md#rt-rte-soul-publish",
          "memory.md#mem-rte-retrieval-adjust",
          "memory.md#mem-rte-temporal-cycle",
          "runtime.md#rt-rte-team-sync"
        ],
        "note": "Sources follow the original input content of each qualifying write. Static imported source documents alone are lineage, not trace sources; unresolved learning writes keep source coverage incomplete."
      }
    }
  }
}
---

# llm-wiki-cli memory profile

## Comparison rationale

This profile classifies accepted records, not execution results. All wired findings denote inspected capacity. Afforded agent transformations remain separate from wired persistence; no finding establishes compliance, semantic faithfulness, improved capacity or causal benefit. No additional source files were read.

### Identity and canonical records

Reconciliation supersedes the epistemic Practice-items object with [MEM-OBJ-practice-items](memory.md#mem-obj-practice-items), and the epistemic temporal-feedback route with [MEM-RTE-temporal-cycle](memory.md#mem-rte-temporal-cycle). This profile uses those canonical destinations. The narrower [EPI-RTE-practice-grade](epistemic.md#epi-rte-practice-grade) remains distinct from [MEM-RTE-practice-assess](memory.md#mem-rte-practice-assess), particularly for override history. No supersession changes a comparison value or promotes an evidence layer.

### Content, control and consumers

SQLite stores prose and localized control fields together, but their forms and effects differ. [MEM-OBJ-derived-indexes](memory.md#mem-obj-derived-indexes) supports symbolic lexical structures, not embeddings. [MEM-OBJ-book-blocks](memory.md#mem-obj-book-blocks) separates readable normalized text from opaque original bytes; those bytes remain unresolved rather than inheriting the display text's classification. Replication is another route for copies, not enough evidence to assign a service-object or graph substrate to every opaque component.

Knowledge at a reference consumer does not become instruction merely because pi appends it to a system prompt: [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context). Soul and purpose/schema have a different standing-guidance role. Stored weights and text can have ranking force without retained ranking policy. Stored lease/revision/source-state criteria can validate and enforce admission without establishing semantic truth. The [WF-RTE-ingest-preparation](workflow.md#wf-rte-ingest-preparation) packet consumes retained purpose/schema and bounded summaries; its current job-state bookkeeping is not automatically trace learning.

### Admission and curation

Generic callers may be agents or humans. A software transaction does not settle who decides the retained content. Accordingly, known automatic capture/scheduler mechanisms coexist with unresolved generic submission control. Sensitive Soul and destructive archive approval are classified only at the claimed policy layer, not as authenticated human approval on all implemented paths. See [RT-RTE-soul-publish](runtime.md#rt-rte-soul-publish) and [MEM-RTE-archive-admit](memory.md#mem-rte-archive-admit).

Page replacement supports evolve; temporal eviction supports decay; Discussion dependency flags support invalidate. Summary routes afford consolidate. Neither the name Book synthesis nor a missing proof of entailment establishes a novel claim, so synthesize is not asserted. Content-hash reuse and index rebuild likewise do not establish semantic dedup. The semantic uncertainty is retained beside [MEM-RTE-book-synthesis](memory.md#mem-rte-book-synthesis), not resolved by changing a route's name.

### Delivery and trace-fed updates

Book windows and Practice queues fulfill explicit requests even though software chooses a range or orders due items. They remain pull. Tag pages are independently supplied at lifecycle events, while tracked Plan/Todo cues use a real context match. Budget omission is not inferred lexical or semantic selection. Non-pi and no-context fallback alternatives remain unresolved, as [RT-RTE-hook-context](runtime.md#rt-rte-hook-context) and [MEM-RTE-task-continuity](memory.md#mem-rte-task-continuity) require.

The strongest trace-learning witness is review rating/time → FSRS card/debt → later queue: [MEM-RTE-practice-review](memory.md#mem-rte-practice-review). Its original input is a discrete review event. Discussion summaries and teaching checkpoints afford conversational-trace continuation at a different evidence layer. Automatic raw reply capture alone supplies no derived learning artifact. Soul, learner facts and other experience-mediated write-back remain unresolved where original input, control or consumer facts are missing. No absence record warrants a local trace-learning no; the supported yes does not resolve that remaining inventory. See [MEM-RTE-discussion-capture](memory.md#mem-rte-discussion-capture), [MEM-BAP-discussion-summary](memory.md#mem-bap-discussion-summary) and [MEM-OBJ-tutor-turns](memory.md#mem-obj-tutor-turns).

---
{
  "type": "agentic-system-analyses/types/agentic-system-memory-profile.md",
  "description": "OrangePro memory comparison: local evidence graphs, reusable drafts, proof decisions and repair artifacts, with opaque hosted alternatives retained.",
  "run-id": "AAS-2026-11-08-orangepro-mcp-4e3d3a22c7c8-01",
  "source-identity": "https://github.com/orangeproai/orangepro-mcp",
  "reviewed-boundary": "039cd936e38eb7d52d0e03ded3b3168373d55d77",
  "memory-comparison": {
    "version": 2,
    "scope": "Included: use-retained local graph and candidate lanes, generated/pinned tests, parse/resolver caches, ledger/certificates, start keys and saved views, jobs/comparison artifacts, fault/repair/export state, installed profiles and published branch/PR state; hosted retained state remains an opaque included alternative at the adapter boundary. Excluded: host conversation policy, provider inference weights not updated by inspected calls, shipped static instructions, and run-local state with no later-invocation consumer.",
    "axes": {
      "storage_substrate": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Local graph, drafts, ledger, caches, reuse snapshots, staged candidates, jobs and proof/export artifacts",
            "assessment": "known",
            "findings": [
              {
                "value": "files",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-graph",
                  "runtime.md#rt-obj-generated-tests",
                  "memory.md#mem-obj-ledger",
                  "memory.md#mem-obj-parse-cache",
                  "memory.md#mem-obj-resolver-cache",
                  "memory.md#mem-obj-run-key",
                  "runtime.md#rt-rte-generation-compare",
                  "runtime.md#rt-rte-draft-verification",
                  "epistemic.md#epi-obj-fault-evidence",
                  "epistemic.md#epi-obj-verification-receipt"
                ],
                "note": "Operative retained state is persisted as local JSON, code, manifests and readable report files. Graph encoding is not evidence of a separate graph storage engine."
              }
            ],
            "records": [
              "runtime.md#rt-obj-graph",
              "runtime.md#rt-obj-generated-tests",
              "memory.md#mem-obj-ledger",
              "memory.md#mem-obj-parse-cache",
              "memory.md#mem-obj-resolver-cache",
              "memory.md#mem-obj-run-key",
              "runtime.md#rt-rte-generation-compare",
              "runtime.md#rt-rte-draft-verification",
              "epistemic.md#epi-obj-fault-evidence",
              "epistemic.md#epi-obj-verification-receipt"
            ],
            "note": "Records identify filesystem persistence for these parts; numerical scores and symbolic edges do not add vector or database substrates."
          },
          {
            "scope": "Published managed branch and draft PR",
            "assessment": "known",
            "findings": [
              {
                "value": "repo",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-actions-delivery"
                ],
                "note": "Confirmed publication writes the test patch to a GitHub branch; later branch/PR read-back checks delivery state."
              }
            ],
            "records": [
              "runtime.md#rt-rte-actions-delivery"
            ],
            "note": "Repository persistence is wired, while merged adoption is external."
          },
          {
            "scope": "Hosted run/log/QA retained state behind the platform adapters",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-platform-call"
            ],
            "note": "Adapters expose service requests, not backend retained objects, transformations or later consumers; this alternative cannot inherit local classifications."
          }
        ],
        "records": [
          "runtime.md#rt-obj-graph",
          "runtime.md#rt-obj-generated-tests",
          "memory.md#mem-obj-ledger",
          "memory.md#mem-obj-parse-cache",
          "memory.md#mem-obj-resolver-cache",
          "memory.md#mem-obj-run-key",
          "runtime.md#rt-rte-generation-compare",
          "runtime.md#rt-rte-draft-verification",
          "epistemic.md#epi-obj-fault-evidence",
          "epistemic.md#epi-obj-verification-receipt",
          "runtime.md#rt-rte-actions-delivery",
          "runtime.md#rt-rte-platform-call"
        ],
        "note": "Local files and confirmed repository delivery are classified; hosted storage remains opaque. External inference weights and static shipped instructions are excluded from accumulated memory."
      },
      "representational_form": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Graph descriptions, acceptance text, weak-link reasons, draft guidance, oracle prose and diagnostic/report rationale at interpreted consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "natural-language",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-graph",
                  "memory.md#mem-rte-context-selection",
                  "runtime.md#rt-obj-generated-tests",
                  "epistemic.md#epi-obj-oracle",
                  "memory.md#mem-obj-ledger",
                  "epistemic.md#epi-obj-comparison-scores",
                  "runtime.md#rt-rte-draft-verification"
                ],
                "note": "Provider, host or reader interprets retained descriptions, expected behavior, reasons and repair feedback."
              }
            ],
            "records": [
              "runtime.md#rt-obj-graph",
              "memory.md#mem-rte-context-selection",
              "runtime.md#rt-obj-generated-tests",
              "epistemic.md#epi-obj-oracle",
              "memory.md#mem-obj-ledger",
              "epistemic.md#epi-obj-comparison-scores",
              "runtime.md#rt-rte-draft-verification"
            ],
            "note": "This classifies prose paths, not symbolic metadata in the same containers."
          },
          {
            "scope": "Graph access structure, executable tests, cache entries, ledger predicates, keys, counts, scores, manifests, profiles and receipts at fixed consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "symbolic",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-graph",
                  "runtime.md#rt-obj-generated-tests",
                  "memory.md#mem-obj-parse-cache",
                  "memory.md#mem-obj-resolver-cache",
                  "memory.md#mem-obj-ledger",
                  "memory.md#mem-obj-run-key",
                  "epistemic.md#epi-obj-comparison-scores",
                  "epistemic.md#epi-obj-verification-receipt",
                  "runtime.md#rt-rte-actions-delivery"
                ],
                "note": "Localized IDs, code, hashes and fixed-rule numeric/status fields govern selection, execution and admission."
              }
            ],
            "records": [
              "runtime.md#rt-obj-graph",
              "runtime.md#rt-obj-generated-tests",
              "memory.md#mem-obj-parse-cache",
              "memory.md#mem-obj-resolver-cache",
              "memory.md#mem-obj-ledger",
              "memory.md#mem-obj-run-key",
              "epistemic.md#epi-obj-comparison-scores",
              "epistemic.md#epi-obj-verification-receipt",
              "runtime.md#rt-rte-actions-delivery"
            ],
            "note": "Numeric comparison fields are symbolic scores, not distributed-parametric representations."
          },
          {
            "scope": "Hosted run/log/QA retained state behind the platform adapters",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-platform-call"
            ],
            "note": "Adapters expose service requests, not backend retained objects, transformations or later consumers; this alternative cannot inherit local classifications."
          }
        ],
        "records": [
          "runtime.md#rt-obj-graph",
          "memory.md#mem-rte-context-selection",
          "runtime.md#rt-obj-generated-tests",
          "epistemic.md#epi-obj-oracle",
          "memory.md#mem-obj-ledger",
          "epistemic.md#epi-obj-comparison-scores",
          "runtime.md#rt-rte-draft-verification",
          "memory.md#mem-obj-parse-cache",
          "memory.md#mem-obj-resolver-cache",
          "memory.md#mem-obj-run-key",
          "epistemic.md#epi-obj-verification-receipt",
          "runtime.md#rt-rte-actions-delivery",
          "runtime.md#rt-rte-platform-call"
        ],
        "note": "Both interpreted prose and fixed-rule symbolic parts are supported. Opaque hosted payloads cannot be classified from text transport; provider parameters are not a target use-updated retained memory part."
      },
      "lineage": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Checkout-derived graph/source content admitted by analysis",
            "assessment": "known",
            "findings": [
              {
                "value": "imported",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-graph",
                  "memory.md#mem-rte-context-selection"
                ],
                "note": "Repository source/doc content enters retained graph evidence and later generation context."
              }
            ],
            "records": [
              "runtime.md#rt-obj-graph",
              "memory.md#mem-rte-context-selection"
            ],
            "note": "Imported content has unknown source warrant; this does not classify every graph field's origin."
          },
          {
            "scope": "Deterministic parse/resolution caches, access keys and computed comparison metrics",
            "assessment": "known",
            "findings": [
              {
                "value": "other-compiled",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-parse-cache",
                  "memory.md#mem-obj-resolver-cache",
                  "memory.md#mem-obj-run-key",
                  "epistemic.md#epi-obj-comparison-scores"
                ],
                "note": "Parsing, resolution, hashing and fixed formulas derive retained symbolic artifacts without a trace-extraction claim."
              }
            ],
            "records": [
              "memory.md#mem-obj-parse-cache",
              "memory.md#mem-obj-resolver-cache",
              "memory.md#mem-obj-run-key",
              "epistemic.md#epi-obj-comparison-scores"
            ],
            "note": "Recomputation lineage is supported independently of parser correctness."
          },
          {
            "scope": "Model-proposed tests, candidate links/flows and model comparison rationale",
            "assessment": "known",
            "findings": [
              {
                "value": "authored",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-test-generation",
                  "runtime.md#rt-rte-candidate-admission",
                  "epistemic.md#epi-obj-comparison-scores"
                ],
                "note": "Models compose proposed tests, relevance metadata and judgment text; pinning reuses original artifacts rather than creating new lineage."
              }
            ],
            "records": [
              "runtime.md#rt-rte-test-generation",
              "runtime.md#rt-rte-candidate-admission",
              "epistemic.md#epi-obj-comparison-scores"
            ],
            "note": "Authored is a production-path classification, not proof of novelty, entailment or correctness."
          },
          {
            "scope": "Runner-derived proof decisions, fault observations, distilled diagnostics and export receipts",
            "assessment": "known",
            "findings": [
              {
                "value": "trace-extracted",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-ledger",
                  "epistemic.md#epi-obj-fault-evidence",
                  "workflow.md#wf-rte-proof-recovery",
                  "epistemic.md#epi-obj-verification-receipt"
                ],
                "note": "Execution results become retained classifications, status/certificate fields, diagnostic summaries and replay predicates."
              }
            ],
            "records": [
              "memory.md#mem-obj-ledger",
              "epistemic.md#epi-obj-fault-evidence",
              "workflow.md#wf-rte-proof-recovery",
              "epistemic.md#epi-obj-verification-receipt"
            ],
            "note": "These derived records differ from complete raw stdout/stderr."
          },
          {
            "scope": "Initial oracle, configured Actions profile/candidate and externally supplied replacement content",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "epistemic.md#epi-obj-oracle",
              "runtime.md#rt-rte-actions-delivery"
            ],
            "note": "Approval metadata and caller identity do not establish who authored, imported or derived the supplied content."
          },
          {
            "scope": "Hosted run/log/QA retained state behind the platform adapters",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-platform-call"
            ],
            "note": "Adapters expose service requests, not backend retained objects, transformations or later consumers; this alternative cannot inherit local classifications."
          }
        ],
        "records": [
          "runtime.md#rt-obj-graph",
          "memory.md#mem-rte-context-selection",
          "memory.md#mem-obj-parse-cache",
          "memory.md#mem-obj-resolver-cache",
          "memory.md#mem-obj-run-key",
          "epistemic.md#epi-obj-comparison-scores",
          "runtime.md#rt-rte-test-generation",
          "runtime.md#rt-rte-candidate-admission",
          "memory.md#mem-obj-ledger",
          "epistemic.md#epi-obj-fault-evidence",
          "workflow.md#wf-rte-proof-recovery",
          "epistemic.md#epi-obj-verification-receipt",
          "epistemic.md#epi-obj-oracle",
          "runtime.md#rt-rte-actions-delivery",
          "runtime.md#rt-rte-platform-call"
        ],
        "note": "Known production paths do not resolve externally supplied initial content or hosted provenance."
      },
      "behavioral_authority": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Retained graph prose and weak reasons at generation; saved reports, diagnostics and scores at readers",
            "assessment": "known",
            "findings": [
              {
                "value": "knowledge",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-context-selection",
                  "memory.md#mem-obj-ledger",
                  "epistemic.md#epi-obj-comparison-scores",
                  "memory.md#mem-rte-start-reuse",
                  "workflow.md#wf-rte-proof-recovery"
                ],
                "note": "Content provides reference/context or explanatory assessments to providers and callers, without semantic acceptance."
              }
            ],
            "records": [
              "memory.md#mem-rte-context-selection",
              "memory.md#mem-obj-ledger",
              "epistemic.md#epi-obj-comparison-scores",
              "memory.md#mem-rte-start-reuse",
              "workflow.md#wf-rte-proof-recovery"
            ],
            "note": "Delivery licenses a context/reference path, not reliable compliance."
          },
          {
            "scope": "Retained draft code and oracle/brief expected behavior supplied to repair or later test execution",
            "assessment": "known",
            "findings": [
              {
                "value": "instruction",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-generated-tests",
                  "runtime.md#rt-rte-draft-verification",
                  "epistemic.md#epi-obj-oracle",
                  "runtime.md#rt-rte-actions-delivery"
                ],
                "note": "Retained executable bodies direct runners; brief/repair content directs the next model task. Static shipped generation instructions are not counted here."
              }
            ],
            "records": [
              "runtime.md#rt-obj-generated-tests",
              "runtime.md#rt-rte-draft-verification",
              "epistemic.md#epi-obj-oracle",
              "runtime.md#rt-rte-actions-delivery"
            ],
            "note": "Code has fixed executable force; interpreted expected-behavior guidance has model-mediated force."
          },
          {
            "scope": "Graph target/access metadata, fingerprints, pinned-run IDs, run keys, certificates and persistent attempt counts",
            "assessment": "known",
            "findings": [
              {
                "value": "routing",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-context-selection",
                  "runtime.md#rt-obj-generated-tests",
                  "memory.md#mem-obj-run-key",
                  "memory.md#mem-rte-start-reuse",
                  "runtime.md#rt-bap-proof-credit",
                  "runtime.md#rt-rte-draft-verification"
                ],
                "note": "Retained metadata selects evidence, reusable drafts, recomputation versus shortcut, proof work eligibility and remaining attempts."
              }
            ],
            "records": [
              "memory.md#mem-rte-context-selection",
              "runtime.md#rt-obj-generated-tests",
              "memory.md#mem-obj-run-key",
              "memory.md#mem-rte-start-reuse",
              "runtime.md#rt-bap-proof-credit",
              "runtime.md#rt-rte-draft-verification"
            ],
            "note": "Run-local quarantine is excluded from durable routing; persistent counts and sidecar diagnostics are kept distinct."
          },
          {
            "scope": "Current graph/candidate text and metadata used to rank gaps and choose context",
            "assessment": "known",
            "findings": [
              {
                "value": "ranking",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-context-selection",
                  "runtime.md#rt-rte-test-generation",
                  "runtime.md#rt-rte-candidate-admission"
                ],
                "note": "Retained graph relationships and symbol metadata influence relative context and target priority under fixed selection code."
              }
            ],
            "records": [
              "memory.md#mem-rte-context-selection",
              "runtime.md#rt-rte-test-generation",
              "runtime.md#rt-rte-candidate-admission"
            ],
            "note": "Ranking is influence on relative selection, not a learned ranking policy."
          },
          {
            "scope": "Retained graph identities, fingerprints, proof records, attempt baseline, manifests and receipts at admission consumers",
            "assessment": "known",
            "findings": [
              {
                "value": "validation",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-candidate-admission",
                  "runtime.md#rt-bap-proof-credit",
                  "runtime.md#rt-rte-draft-verification",
                  "epistemic.md#epi-rte-export-replay",
                  "runtime.md#rt-rte-actions-delivery"
                ],
                "note": "Retained criteria and evidence determine current-anchor validity, proof tier, repair conformity, export lineage and delivery admissibility."
              },
              {
                "value": "enforcement",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-bap-proof-credit",
                  "runtime.md#rt-rte-draft-verification",
                  "epistemic.md#epi-rte-export-replay",
                  "runtime.md#rt-rte-actions-delivery"
                ],
                "note": "Fixed predicates withhold proof eligibility, disallow excess attempts, refuse invalid exports and block stale/conflicting delivery."
              }
            ],
            "records": [
              "runtime.md#rt-rte-candidate-admission",
              "runtime.md#rt-bap-proof-credit",
              "runtime.md#rt-rte-draft-verification",
              "epistemic.md#epi-rte-export-replay",
              "runtime.md#rt-rte-actions-delivery"
            ],
            "note": "Checking and veto effects coexist; a locally writable record is not authenticated execution evidence."
          },
          {
            "scope": "Retained previous candidate and classified execution feedback at automatic repair",
            "assessment": "known",
            "findings": [
              {
                "value": "learning",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-draft-verification"
                ],
                "note": "Experience and the previous test feed automatic revision of a persisted test artifact that later verification/export can consume."
              }
            ],
            "records": [
              "runtime.md#rt-rte-draft-verification"
            ],
            "note": "Learning authority is local to the update consumer; improved capacity and exercised benefit remain unobserved."
          },
          {
            "scope": "Hosted run/log/QA retained state behind the platform adapters",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-platform-call"
            ],
            "note": "Adapters expose service requests, not backend retained objects, transformations or later consumers; this alternative cannot inherit local classifications."
          }
        ],
        "records": [
          "memory.md#mem-rte-context-selection",
          "memory.md#mem-obj-ledger",
          "epistemic.md#epi-obj-comparison-scores",
          "memory.md#mem-rte-start-reuse",
          "workflow.md#wf-rte-proof-recovery",
          "runtime.md#rt-obj-generated-tests",
          "runtime.md#rt-rte-draft-verification",
          "epistemic.md#epi-obj-oracle",
          "runtime.md#rt-rte-actions-delivery",
          "memory.md#mem-obj-run-key",
          "runtime.md#rt-bap-proof-credit",
          "runtime.md#rt-rte-test-generation",
          "runtime.md#rt-rte-candidate-admission",
          "epistemic.md#epi-rte-export-replay",
          "runtime.md#rt-rte-platform-call"
        ],
        "note": "Authority is consumer-specific. Model advice, executable instructions, selection inputs and admission vetoes are separate paths; hosted authority remains unresolved."
      },
      "write_agency": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Analysis/cache writes, graph draft admission, start AI apply, ledger decisions, saved results, job/attempt/receipt writes and automatic repair",
            "assessment": "known",
            "findings": [
              {
                "value": "automatic",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-parse-cache",
                  "memory.md#mem-obj-resolver-cache",
                  "runtime.md#rt-rte-test-generation",
                  "runtime.md#rt-rte-candidate-admission",
                  "memory.md#mem-obj-ledger",
                  "memory.md#mem-rte-start-reuse",
                  "runtime.md#rt-rte-generation-compare",
                  "runtime.md#rt-rte-draft-verification",
                  "epistemic.md#epi-rte-export-replay"
                ],
                "note": "Code/model mechanisms admit retained content without a human deciding each item; starting the workflow is not per-content approval."
              }
            ],
            "records": [
              "memory.md#mem-obj-parse-cache",
              "memory.md#mem-obj-resolver-cache",
              "runtime.md#rt-rte-test-generation",
              "runtime.md#rt-rte-candidate-admission",
              "memory.md#mem-obj-ledger",
              "memory.md#mem-rte-start-reuse",
              "runtime.md#rt-rte-generation-compare",
              "runtime.md#rt-rte-draft-verification",
              "epistemic.md#epi-rte-export-replay"
            ],
            "note": "Automatic local admission is supported even where a host may later edit/reject a returned draft."
          },
          {
            "scope": "Standalone apply, workflow installation/publication confirmation and initial oracle/profile/candidate supply",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-candidate-admission",
              "runtime.md#rt-rte-actions-delivery",
              "epistemic.md#epi-obj-oracle"
            ],
            "note": "Caller flags and approval fields do not establish an explicit human decision supplying or approving each retained content item. Automatic workflows can provide confirmation; manual agency cannot be inferred."
          },
          {
            "scope": "Hosted run/log/QA retained state behind the platform adapters",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-platform-call"
            ],
            "note": "Adapters expose service requests, not backend retained objects, transformations or later consumers; this alternative cannot inherit local classifications."
          }
        ],
        "records": [
          "memory.md#mem-obj-parse-cache",
          "memory.md#mem-obj-resolver-cache",
          "runtime.md#rt-rte-test-generation",
          "runtime.md#rt-rte-candidate-admission",
          "memory.md#mem-obj-ledger",
          "memory.md#mem-rte-start-reuse",
          "runtime.md#rt-rte-generation-compare",
          "runtime.md#rt-rte-draft-verification",
          "epistemic.md#epi-rte-export-replay",
          "runtime.md#rt-rte-actions-delivery",
          "epistemic.md#epi-obj-oracle",
          "runtime.md#rt-rte-platform-call"
        ],
        "note": "Software-controlled writes are established. Generic caller confirmation does not resolve human control, so no manual finding is inferred."
      },
      "curation_operations": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Candidate-edge application",
            "assessment": "known",
            "findings": [
              {
                "value": "dedup",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-candidate-admission"
                ],
                "note": "Application merges existing and proposed edges through the recorded dedupeCandidateEdges transformation."
              }
            ],
            "records": [
              "runtime.md#rt-rte-candidate-admission"
            ],
            "note": "This is implemented duplicate removal, not merely a primary-key collision check."
          },
          {
            "scope": "Generated-draft freshness maintenance and candidate-flow revalidation",
            "assessment": "known",
            "findings": [
              {
                "value": "invalidate",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-obj-generated-tests",
                  "runtime.md#rt-rte-candidate-admission"
                ],
                "note": "Incremental update marks affected drafts stale, withholding reuse while retaining them; current anchors separately constrain candidate reliance."
              }
            ],
            "records": [
              "runtime.md#rt-obj-generated-tests",
              "runtime.md#rt-rte-candidate-admission"
            ],
            "note": "Full reanalysis can drop obsolete artifacts; the retained stale-marker route establishes withdrawal without requiring universal erasure."
          },
          {
            "scope": "Fault-lane setup repair of the previous test",
            "assessment": "known",
            "findings": [
              {
                "value": "evolve",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-draft-verification"
                ],
                "note": "Automatic repair revises candidate setup under baseline/assertion restrictions and persists another attempt."
              }
            ],
            "records": [
              "runtime.md#rt-rte-draft-verification"
            ],
            "note": "The wired revision request and stored candidate path do not establish successful improvement or reliable model compliance."
          },
          {
            "scope": "Proof-run diagnostics distilled for later doctor/report readers",
            "assessment": "known",
            "findings": [
              {
                "value": "consolidate",
                "basis": "wired",
                "records": [
                  "workflow.md#wf-rte-proof-recovery"
                ],
                "note": "Start persists distilled already-redacted attempt classifications rather than complete raw execution output."
              }
            ],
            "records": [
              "workflow.md#wf-rte-proof-recovery"
            ],
            "note": "This reduces existing outcome material; it is not a demonstrated novel explanatory claim."
          },
          {
            "scope": "Other semantic transformations in generation, comparison, receipt/report helpers and configured content",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-test-generation",
              "epistemic.md#epi-obj-comparison-scores",
              "epistemic.md#epi-obj-verification-receipt",
              "runtime.md#rt-rte-actions-delivery"
            ],
            "note": "Records do not completely enumerate retained-content transformations; indeterminate model entailment cannot establish synthesis, and tier credit is not automatically memory promotion."
          },
          {
            "scope": "Hosted run/log/QA retained state behind the platform adapters",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-platform-call"
            ],
            "note": "Adapters expose service requests, not backend retained objects, transformations or later consumers; this alternative cannot inherit local classifications."
          }
        ],
        "records": [
          "runtime.md#rt-rte-candidate-admission",
          "runtime.md#rt-obj-generated-tests",
          "runtime.md#rt-rte-draft-verification",
          "workflow.md#wf-rte-proof-recovery",
          "runtime.md#rt-rte-test-generation",
          "epistemic.md#epi-obj-comparison-scores",
          "epistemic.md#epi-obj-verification-receipt",
          "runtime.md#rt-rte-actions-delivery",
          "runtime.md#rt-rte-platform-call"
        ],
        "note": "Implemented deduplication, invalidation, revision and diagnostic consolidation are classified locally. No complete operation inventory or unsupported synthesis/decay/promotion claim follows."
      },
      "read_back_direction": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Requested pinned tests, saved start result/reports, job polling, explain/export and platform-facing local artifact requests",
            "assessment": "known",
            "findings": [
              {
                "value": "pull",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-test-generation",
                  "memory.md#mem-rte-start-reuse",
                  "runtime.md#rt-rte-generation-compare",
                  "memory.md#mem-obj-ledger"
                ],
                "note": "A caller asks for generation, start, status or retained results and receives selected stored material in response."
              }
            ],
            "records": [
              "runtime.md#rt-rte-test-generation",
              "memory.md#mem-rte-start-reuse",
              "runtime.md#rt-rte-generation-compare",
              "memory.md#mem-obj-ledger"
            ],
            "note": "Returning the requested artifact is not an extra push merely because delivery is implemented in code."
          },
          {
            "scope": "Automatic provider-context supply, repair feedback supply, proof/worklist selectors and event-driven configured replay",
            "assessment": "known",
            "findings": [
              {
                "value": "push",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-context-selection",
                  "runtime.md#rt-rte-draft-verification",
                  "runtime.md#rt-bap-proof-credit",
                  "runtime.md#rt-rte-actions-delivery"
                ],
                "note": "Internal selectors supply retained evidence/feedback or control state to later model, worklist and Actions consumers without those consumers requesting that retained item."
              }
            ],
            "records": [
              "memory.md#mem-rte-context-selection",
              "runtime.md#rt-rte-draft-verification",
              "runtime.md#rt-bap-proof-credit",
              "runtime.md#rt-rte-actions-delivery"
            ],
            "note": "Push occurs within an operation that may itself have been requested; it is distinct from the outer tool return."
          },
          {
            "scope": "Hosted run/log/QA retained state behind the platform adapters",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-platform-call"
            ],
            "note": "Adapters expose service requests, not backend retained objects, transformations or later consumers; this alternative cannot inherit local classifications."
          }
        ],
        "records": [
          "runtime.md#rt-rte-test-generation",
          "memory.md#mem-rte-start-reuse",
          "runtime.md#rt-rte-generation-compare",
          "memory.md#mem-obj-ledger",
          "memory.md#mem-rte-context-selection",
          "runtime.md#rt-rte-draft-verification",
          "runtime.md#rt-bap-proof-credit",
          "runtime.md#rt-rte-actions-delivery",
          "runtime.md#rt-rte-platform-call"
        ],
        "note": "Requested returns and automatic internal selection coexist. Backend later-consumer delivery is not exposed by the adapter."
      },
      "read_back_signal": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Generation-context push triggered by a selected target",
            "assessment": "known",
            "findings": [
              {
                "value": "identifier",
                "basis": "wired",
                "records": [
                  "memory.md#mem-rte-context-selection"
                ],
                "note": "Trigger: generation target. Selector input: target identity and graph relations. Selected part: linked acceptance/workflow, symbol descriptions and candidate-edge reasons delivered to the provider."
              }
            ],
            "records": [
              "memory.md#mem-rte-context-selection"
            ],
            "note": "An actual target/relationship match selects retained content; character caps constrain payload size but are not semantic retrieval."
          },
          {
            "scope": "Proof/worklist push triggered by later report/start",
            "assessment": "known",
            "findings": [
              {
                "value": "identifier",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-targeted-proof",
                  "runtime.md#rt-bap-proof-credit"
                ],
                "note": "Trigger: current report/worklist construction. Selector inputs: target identity and current fingerprint. Selected part: matching valid historical proof/certificate used for tier and skip decisions."
              }
            ],
            "records": [
              "runtime.md#rt-rte-targeted-proof",
              "runtime.md#rt-bap-proof-credit"
            ],
            "note": "The identifier match is operative rather than an ID merely printed on an artifact."
          },
          {
            "scope": "Repair-feedback push triggered by failed verification within the drafting invocation",
            "assessment": "known",
            "findings": [
              {
                "value": "coarse",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-draft-verification"
                ],
                "note": "Trigger: repair iteration. Selector input: current attempt and classified outcome. Selected part: the previous candidate and its outcome, supplied wholesale to the next repair request."
              }
            ],
            "records": [
              "runtime.md#rt-rte-draft-verification"
            ],
            "note": "This is latest-attempt availability, not semantic similarity or inferred relevance."
          },
          {
            "scope": "All other push selectors, including event/profile eligibility and opaque hosted routes",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-actions-delivery",
              "runtime.md#rt-rte-platform-call"
            ],
            "note": "Records give event/profile conditions but do not completely classify every delivered retained part's selector; opaque backend consumption is unavailable."
          }
        ],
        "records": [
          "memory.md#mem-rte-context-selection",
          "runtime.md#rt-rte-targeted-proof",
          "runtime.md#rt-bap-proof-credit",
          "runtime.md#rt-rte-draft-verification",
          "runtime.md#rt-rte-actions-delivery",
          "runtime.md#rt-rte-platform-call"
        ],
        "note": "Identifier-selected evidence and coarse repair feedback are supported. No embedding, lexical or model-judgment push selector is established by these records; missing coverage is not absence."
      },
      "trace_learning": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Automatic fault-verification feedback to persisted repaired test, followed by verification/export consumption",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-draft-verification",
                  "epistemic.md#epi-rte-export-replay"
                ],
                "note": "Tool execution observations and prior candidate feed automatic repair; attempt artifacts retain the revised behavior-shaping test for subsequent verification and export."
              }
            ],
            "records": [
              "runtime.md#rt-rte-draft-verification",
              "epistemic.md#epi-rte-export-replay"
            ],
            "note": "This is the profile's trace-fed durable-artifact criterion, not a claim of better future capacity or observed success."
          },
          {
            "scope": "Runner outcomes to durable proof decision controlling later report/start work",
            "assessment": "known",
            "findings": [
              {
                "value": "yes",
                "basis": "wired",
                "records": [
                  "memory.md#mem-obj-ledger",
                  "runtime.md#rt-rte-targeted-proof",
                  "runtime.md#rt-bap-proof-credit"
                ],
                "note": "Baseline/mutant execution feeds automatically retained certificate/status decisions that shape later target eligibility and public tier."
              }
            ],
            "records": [
              "memory.md#mem-obj-ledger",
              "runtime.md#rt-rte-targeted-proof",
              "runtime.md#rt-bap-proof-credit"
            ],
            "note": "The durable behavior-shaping artifact is a scoped decision record, not a generalized model-authored strategy or parameter update."
          },
          {
            "scope": "Comparison/job artifacts, caches, configured Actions candidates, diagnostic sidecars and remaining local alternatives",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-generation-compare",
              "memory.md#mem-obj-parse-cache",
              "memory.md#mem-obj-resolver-cache",
              "runtime.md#rt-rte-actions-delivery",
              "workflow.md#wf-rte-proof-recovery"
            ],
            "note": "Some records describe recomputation or display rather than a qualifying learned policy, but no bounded absence record establishes a local no. Configured content provenance and complete later-consumer coverage remain unresolved."
          },
          {
            "scope": "Hosted run/log/QA retained state behind the platform adapters",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-platform-call"
            ],
            "note": "Adapters expose service requests, not backend retained objects, transformations or later consumers; this alternative cannot inherit local classifications."
          }
        ],
        "records": [
          "runtime.md#rt-rte-draft-verification",
          "epistemic.md#epi-rte-export-replay",
          "memory.md#mem-obj-ledger",
          "runtime.md#rt-rte-targeted-proof",
          "runtime.md#rt-bap-proof-credit",
          "runtime.md#rt-rte-generation-compare",
          "memory.md#mem-obj-parse-cache",
          "memory.md#mem-obj-resolver-cache",
          "runtime.md#rt-rte-actions-delivery",
          "workflow.md#wf-rte-proof-recovery",
          "runtime.md#rt-rte-platform-call"
        ],
        "note": "Wired trace-fed repair and proof-decision routes support yes without establishing benefit. Unresolved alternatives prevent complete inventory coverage; there is no warranted local or system-wide no."
      },
      "trace_source": {
        "assessment": "partial",
        "units": [
          {
            "scope": "Fault-repair and proof-decision qualifying writes",
            "assessment": "known",
            "findings": [
              {
                "value": "tool-traces",
                "basis": "wired",
                "records": [
                  "runtime.md#rt-rte-draft-verification",
                  "memory.md#mem-obj-ledger",
                  "runtime.md#rt-rte-targeted-proof",
                  "epistemic.md#epi-rte-export-replay"
                ],
                "note": "Original inputs are test/witness execution results, verification classifications and baseline/mutant feedback; they are tool execution observations, not agent session logs."
              }
            ],
            "records": [
              "runtime.md#rt-rte-draft-verification",
              "memory.md#mem-obj-ledger",
              "runtime.md#rt-rte-targeted-proof",
              "epistemic.md#epi-rte-export-replay"
            ],
            "note": "Multi-stage verification alone does not establish a state/action/outcome trajectory learning input."
          },
          {
            "scope": "Original inputs to other possible local and hosted qualifying updates",
            "assessment": "not-determinable",
            "findings": [],
            "records": [
              "runtime.md#rt-rte-actions-delivery",
              "runtime.md#rt-rte-generation-compare",
              "workflow.md#wf-rte-proof-recovery",
              "runtime.md#rt-rte-platform-call"
            ],
            "note": "Configured candidate origins, diagnostic reuse and backend update consumers are not completely known. No event-stream, session-log or trajectory source can be inferred from scheduling or serialization alone."
          }
        ],
        "records": [
          "runtime.md#rt-rte-draft-verification",
          "memory.md#mem-obj-ledger",
          "runtime.md#rt-rte-targeted-proof",
          "epistemic.md#epi-rte-export-replay",
          "runtime.md#rt-rte-actions-delivery",
          "runtime.md#rt-rte-generation-compare",
          "workflow.md#wf-rte-proof-recovery",
          "runtime.md#rt-rte-platform-call"
        ],
        "note": "Tool-trace origin is supported on the qualifying local updates. Other potential learning routes remain unresolved, so this axis is partial rather than inapplicable."
      }
    }
  }
}
---

# OrangePro memory profile

## Comparison rationale

The comparison follows the accepted records and their annotations. Reconciliation establishes no duplicate supersessions; valid containers and parts remain distinct. Every axis is partial because local witnesses do not enumerate opaque hosted state or all included local alternatives. Uninspected helpers and unknown admission provenance remain uncertainty, not absence.

Filesystem JSON establishes files, not a graph database substrate. Symbolic graph structure and executable code are separated from interpreted descriptions and reasons. External model parameters are inference components rather than an OrangePro use-updated memory object; their opacity does not turn local symbolic scores into parametric memory. See [RT-OBJ-graph](runtime.md#rt-obj-graph), [RT-OBJ-generated-tests](runtime.md#rt-obj-generated-tests) and [RT-RTE-platform-call](runtime.md#rt-rte-platform-call).

The outer request can pull a saved product while internal selection pushes retained context into a later provider invocation. Target/relationship matches select graph evidence; the provider did not independently request those retained parts. Budget filtering constrains delivery but does not establish semantic similarity. See [MEM-RTE-context-selection](memory.md#mem-rte-context-selection) and [MEM-RTE-start-reuse](memory.md#mem-rte-start-reuse).

Trace learning here uses the profile's automatic trace-fed durable-artifact criterion. A repaired test and a retained proof decision have later consumers, although neither establishes improved capacity, a revised general strategy or weight training. The proof record's downstream force is routing/validation rather than a blanket instruction to a model. Repair feedback has learning authority at the update consumer and produces executable instructions for later verification. See [RT-RTE-draft-verification](runtime.md#rt-rte-draft-verification), [MEM-OBJ-ledger](memory.md#mem-obj-ledger), [RT-BAP-proof-credit](runtime.md#rt-bap-proof-credit) and [EPI-RTE-export-replay](epistemic.md#epi-rte-export-replay).

No evidenced-absence records were declared in the supplied reports. Non-qualifying recomputation/display examples therefore do not warrant local trace-learning no findings or inapplicable trace sources across unresolved alternatives. The supported yes findings survive the partial inventory. Generic caller confirmations likewise do not establish manual content admission; Actions may supply them automatically. See [RT-RTE-generation-compare](runtime.md#rt-rte-generation-compare), [RT-RTE-actions-delivery](runtime.md#rt-rte-actions-delivery) and [MEM-OBJ-parse-cache](memory.md#mem-obj-parse-cache).

Curation follows transformations rather than labels: candidate deduplication, stale-mark withdrawal, setup repair and distilled diagnostics have separate warrants. Numeric quality proxies do not establish synthesis or semantic acceptance. Proof credit is a target tier, not by itself promotion of a retained memory entry. See [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission), [RT-OBJ-generated-tests](runtime.md#rt-obj-generated-tests), [WF-RTE-proof-recovery](workflow.md#wf-rte-proof-recovery) and [EPI-RTE-comparison-scoring](epistemic.md#epi-rte-comparison-scoring).

All bases describe implementation wiring, not observed activation or causal benefit. No frozen-source reads were needed or performed for this classification; the supplied accepted records provide its evidence passages.

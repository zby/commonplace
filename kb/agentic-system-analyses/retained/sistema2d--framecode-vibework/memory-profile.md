---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "FrameCode-VibeWork memory comparison: host-curated project files, continuity summaries, revised guidance and optional derived retrieval/check state."
run-id: "AAS-2026-11-08-framecode-vibework-d38fb53e8013-01"
source-identity: "https://github.com/sistema2d/framecode-vibework"
reviewed-boundary: "847cdcedc02d08531961c8367f4e2ddb2dc392f1"
memory-comparison:
  version: 2
  scope: "Retained project wiki bodies and lifecycle metadata, session/archive handoffs, plans/evidence, product expectations and exact QA runs, use-revised skills/policies, disposable text indexes and typed graphs/review findings, decision traces and local verification reports, and their write/maintenance/later-consumer routes. Includes the incompletely inspected navigation graph/catalog and unresolved provenance/linked-evidence alternatives. Excludes unchanged shipped instructions as accumulated memory, ordinary current-run state, external host transcripts/compaction, provider weights/state, live application payloads not retained or linked by these routes, and packaging administration as independent memory mechanisms."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Canonical wiki, session, product/QA, plan/evidence and revised skill files in the project repository"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-wiki-metadata"
                - "memory.md#mem-obj-session"
                - "memory.md#mem-obj-product-contract"
                - "memory.md#mem-obj-qa-run"
                - "runtime.md#rt-rte-governed-change"
                - "runtime.md#rt-obj-skill"
                - "runtime.md#rt-obj-skill-frontmatter"
              note: "Markdown bodies and symbolic frontmatter persist as project files."
            -
              value: "repo"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-wiki-metadata"
                - "memory.md#mem-obj-session"
                - "memory.md#mem-obj-product-contract"
                - "memory.md#mem-obj-qa-run"
                - "runtime.md#rt-rte-governed-change"
                - "runtime.md#rt-obj-skill"
                - "runtime.md#rt-obj-skill-frontmatter"
              note: "Versioned project artifacts and preserved history provide cross-session retention; this is not model storage."
          records:
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-wiki-metadata"
            - "memory.md#mem-obj-session"
            - "memory.md#mem-obj-product-contract"
            - "memory.md#mem-obj-qa-run"
            - "runtime.md#rt-rte-governed-change"
            - "runtime.md#rt-obj-skill"
            - "runtime.md#rt-obj-skill-frontmatter"
          note: "Storage is established for these named artifact families, not deployed instances."
        -
          scope: "Disposable text index, typed graph/review JSON, decision trace and local verification logs/reports"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-index"
                - "memory.md#mem-obj-knowledge-graph"
                - "memory.md#mem-obj-decision-trace"
                - "memory.md#mem-rte-index-build"
                - "runtime.md#rt-rte-local-checks"
              note: "JSONL, JSON and log artifacts are filesystem outputs; graph encoding is not a separate graph database."
          records:
            - "memory.md#mem-obj-context-index"
            - "memory.md#mem-obj-knowledge-graph"
            - "memory.md#mem-obj-decision-trace"
            - "memory.md#mem-rte-index-build"
            - "runtime.md#rt-rte-local-checks"
          note: "Concrete file-producing tools are inspected; no execution is claimed."
        -
          scope: "Navigation graph/generated catalog internals"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-graph"
          note: "The accepted inventory distinguishes this navigation mechanism but does not inspect its full production/persistence body; exact storage classification remains unresolved."
      records:
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-wiki-metadata"
        - "memory.md#mem-obj-session"
        - "memory.md#mem-obj-product-contract"
        - "memory.md#mem-obj-qa-run"
        - "runtime.md#rt-rte-governed-change"
        - "runtime.md#rt-obj-skill"
        - "runtime.md#rt-obj-skill-frontmatter"
        - "memory.md#mem-obj-context-index"
        - "memory.md#mem-obj-knowledge-graph"
        - "memory.md#mem-obj-decision-trace"
        - "memory.md#mem-rte-index-build"
        - "runtime.md#rt-rte-local-checks"
      note: "Known file and repository surfaces coexist with an incompletely inspected navigation/catalog alternative; external host/provider stores are excluded."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Wiki, session, product expectations/observations, plans and revised procedural bodies at host interpretation"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-wiki-metadata"
                - "memory.md#mem-obj-session"
                - "memory.md#mem-obj-product-contract"
                - "memory.md#mem-obj-qa-run"
                - "runtime.md#rt-rte-governed-change"
                - "runtime.md#rt-obj-skill"
                - "runtime.md#rt-obj-skill-frontmatter"
              note: "Hosts interpret prose claims, continuity state, acceptance criteria and procedural directions."
          records:
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-wiki-metadata"
            - "memory.md#mem-obj-session"
            - "memory.md#mem-obj-product-contract"
            - "memory.md#mem-obj-qa-run"
            - "runtime.md#rt-rte-governed-change"
            - "runtime.md#rt-obj-skill"
            - "runtime.md#rt-obj-skill-frontmatter"
          note: "Body-level semantic interpretation is distinct from fixed-rule metadata consumption."
        -
          scope: "Wiki/skill/plan metadata, product/run IDs and hashes, graph/review state and decision traces at Python consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-metadata"
                - "memory.md#mem-obj-product-contract"
                - "memory.md#mem-obj-qa-run"
                - "memory.md#mem-obj-knowledge-graph"
                - "memory.md#mem-obj-decision-trace"
                - "runtime.md#rt-rte-mcp-checks"
              note: "Localized identifiers, enums, relationships and hashes have fixed-rule consumers."
          records:
            - "memory.md#mem-obj-wiki-metadata"
            - "memory.md#mem-obj-product-contract"
            - "memory.md#mem-obj-qa-run"
            - "memory.md#mem-obj-knowledge-graph"
            - "memory.md#mem-obj-decision-trace"
            - "runtime.md#rt-rte-mcp-checks"
          note: "This classifies consumed metadata, not the truth of its assertions."
        -
          scope: "Copied index parts delivered to hosts and scored by deterministic retrieval"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-index"
                - "runtime.md#rt-rte-context-delivery"
              note: "Copied Markdown excerpts reach an interpreting host."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-index"
                - "runtime.md#rt-rte-context-delivery"
              note: "Chunk IDs, hashes, filters and tokenized text/features drive fixed-rule selection."
          records:
            - "memory.md#mem-obj-context-index"
            - "runtime.md#rt-rte-context-delivery"
          note: "The two consumption paths share a file, not a representational role."
        -
          scope: "Linked screenshots/traces/large logs referenced by QA records"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-qa-run"
          note: "Referenced payloads were not supplied; their operative encodings cannot be inferred from readable audit descriptions."
        -
          scope: "Navigation graph/catalog production and consumption details"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-graph"
          note: "The separate navigation surface is not resolved by the inspected typed graph."
      records:
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-wiki-metadata"
        - "memory.md#mem-obj-session"
        - "memory.md#mem-obj-product-contract"
        - "memory.md#mem-obj-qa-run"
        - "runtime.md#rt-rte-governed-change"
        - "runtime.md#rt-obj-skill"
        - "runtime.md#rt-obj-skill-frontmatter"
        - "memory.md#mem-obj-knowledge-graph"
        - "memory.md#mem-obj-decision-trace"
        - "runtime.md#rt-rte-mcp-checks"
        - "memory.md#mem-obj-context-index"
        - "runtime.md#rt-rte-context-delivery"
      note: "No parametric retained-memory part is established; provider weights are outside this memory boundary, not evidenced absent."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Host-created wiki/product notes, plans and revised procedural content"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-rte-product-review"
                - "runtime.md#rt-rte-governed-change"
                - "runtime.md#rt-rte-asset-admission"
              note: "Host/human authors project records and behavior-shaping revisions under prescribed gates."
          records:
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-rte-product-review"
            - "runtime.md#rt-rte-governed-change"
            - "runtime.md#rt-rte-asset-admission"
          note: "This derivation path does not settle every initial source's origin."
        -
          scope: "Raw imported wiki material and release replacement content"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-wiki"
                - "runtime.md#rt-rte-framework-upgrade"
              note: "Raw pages preserve imports; upgrade can copy supplied release content into later-used assets."
          records:
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-framework-upgrade"
          note: "Imported lineage says nothing about initial human approval or source truth."
        -
          scope: "Session continuity and experience-derived reusable notes or skills"
          assessment: "partial"
          findings:
            -
              value: "trace-extracted"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-session-handoff"
                - "runtime.md#rt-rte-asset-admission"
              note: "Actual work decisions, failures and validation are prescribed inputs to retained continuity and method revision."
          records:
            - "memory.md#mem-rte-session-handoff"
            - "runtime.md#rt-rte-asset-admission"
          note: "Trace-informed derivation is specified; mixed original input provenance is not resolved for every note or revision."
        -
          scope: "Index chunks, typed edges/inverses, review findings and tool decision rows"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-index"
                - "memory.md#mem-obj-knowledge-graph"
                - "memory.md#mem-obj-decision-trace"
                - "memory.md#mem-rte-index-build"
                - "runtime.md#rt-rte-local-checks"
              note: "Software copies/packages Markdown and derives symbolic access/review/log state without semantic authorship."
          records:
            - "memory.md#mem-obj-context-index"
            - "memory.md#mem-obj-knowledge-graph"
            - "memory.md#mem-obj-decision-trace"
            - "memory.md#mem-rte-index-build"
            - "runtime.md#rt-rte-local-checks"
          note: "Mechanical derivation does not establish semantic synthesis or learned parameters."
        -
          scope: "Initial provenance of arbitrary wiki inputs and referenced QA evidence"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-qa-run"
          note: "The records do not authenticate all original sources, authors or linked evidence payloads."
        -
          scope: "Navigation graph/catalog derivation body"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-graph"
          note: "A distinct navigation mechanism is named but its complete derivation was not inspected."
      records:
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-rte-product-review"
        - "runtime.md#rt-rte-governed-change"
        - "runtime.md#rt-rte-asset-admission"
        - "runtime.md#rt-rte-framework-upgrade"
        - "memory.md#mem-rte-session-handoff"
        - "memory.md#mem-obj-context-index"
        - "memory.md#mem-obj-knowledge-graph"
        - "memory.md#mem-obj-decision-trace"
        - "memory.md#mem-rte-index-build"
        - "runtime.md#rt-rte-local-checks"
        - "memory.md#mem-obj-qa-run"
      note: "Supported authored, imported, trace-informed and compiled paths are retained without resolving initial or linked-payload provenance."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Wiki/handoff/product evidence and index excerpts at later interpreting hosts"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-bap-knowledge-consumption"
                - "runtime.md#rt-rte-mcp-checks"
                - "runtime.md#rt-rte-context-delivery"
              note: "Content supplies evidence and continuity context subordinate to canonical and host authority."
          records:
            - "memory.md#mem-bap-knowledge-consumption"
            - "runtime.md#rt-rte-mcp-checks"
            - "runtime.md#rt-rte-context-delivery"
          note: "Delivery is supported; actual reliance is unobserved."
        -
          scope: "Retained revised skill/policy bodies at later host loads"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-asset-admission"
                - "runtime.md#rt-bap-policy-consumption"
              note: "Revised operational directions instruct later hosts; static shipped bodies alone are excluded from accumulated memory."
          records:
            - "runtime.md#rt-rte-asset-admission"
            - "runtime.md#rt-bap-policy-consumption"
          note: "The downstream instruction path is separate from the evidential notes used to revise it."
        -
          scope: "Retained work/failure/session evidence at host curation and procedural revision"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-asset-admission"
                - "memory.md#mem-rte-session-handoff"
              note: "Experience is prescribed input to durable notes, continuation summaries and behavior-shaping guidance updates."
          records:
            - "runtime.md#rt-rte-asset-admission"
            - "memory.md#mem-rte-session-handoff"
          note: "This is an update-consumer force, not observed capacity improvement."
        -
          scope: "Indexed text/lifecycle fields at scorer and retained plans at queue ordering"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "runtime.md#rt-rte-mcp-checks"
              note: "Text overlap, status/freshness/authority and plan queue metadata influence relative priority."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "runtime.md#rt-rte-mcp-checks"
          note: "Fixed scoring can consume memory as ranking input without learned ranking policy."
        -
          scope: "Persisted plan state, context_files and wiki dependencies at route/review consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "runtime.md#rt-rte-mcp-checks"
                - "epistemic.md#epi-rte-source-review"
              note: "Plan context references and queue state select scope/recommendations; dependency/digest metadata selects review candidates."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "runtime.md#rt-rte-mcp-checks"
            - "epistemic.md#epi-rte-source-review"
          note: "Selection of scope is not body-level delivery or semantic endorsement."
        -
          scope: "Retained QA contracts/hashes/classifications and wiki provenance metadata at checkers"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-product-contract"
                - "memory.md#mem-obj-qa-run"
                - "epistemic.md#epi-rte-qa-check"
                - "epistemic.md#epi-rte-evidence-check"
              note: "Retained criteria and status assertions determine declared conformance and run reuse."
          records:
            - "memory.md#mem-obj-product-contract"
            - "memory.md#mem-obj-qa-run"
            - "epistemic.md#epi-rte-qa-check"
            - "epistemic.md#epi-rte-evidence-check"
          note: "This validates encoded representations, not factual truth or consent."
        -
          scope: "Retained plan presence at edit hook and selected QA contract/run state at CLI gate"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-hook-lifecycle"
                - "epistemic.md#epi-rte-qa-check"
              note: "Plan presence permits/refuses recognized edits conditionally; contract/result mismatches can refuse QA command success."
          records:
            - "runtime.md#rt-rte-hook-lifecycle"
            - "epistemic.md#epi-rte-qa-check"
          note: "These bounded vetoes do not mediate every host action."
        -
          scope: "Recorded divergence decisions at dependent host action"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-divergence-decision"
              note: "Pending direction blocks dependent continuation by instruction; explicit user direction licenses a bounded action."
          records:
            - "epistemic.md#epi-rte-divergence-decision"
          note: "Declared decision references do not authenticate consultation."
        -
          scope: "Navigation/catalog and unsupplied linked QA payload consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-graph"
            - "memory.md#mem-obj-qa-run"
          note: "Their exact consumer force is not established by a display record or by the typed-graph consumer."
      records:
        - "memory.md#mem-bap-knowledge-consumption"
        - "runtime.md#rt-rte-mcp-checks"
        - "runtime.md#rt-rte-context-delivery"
        - "runtime.md#rt-rte-asset-admission"
        - "runtime.md#rt-bap-policy-consumption"
        - "memory.md#mem-rte-session-handoff"
        - "epistemic.md#epi-rte-source-review"
        - "memory.md#mem-obj-product-contract"
        - "memory.md#mem-obj-qa-run"
        - "epistemic.md#epi-rte-qa-check"
        - "epistemic.md#epi-rte-evidence-check"
        - "runtime.md#rt-rte-hook-lifecycle"
        - "epistemic.md#epi-rte-divergence-decision"
        - "memory.md#mem-obj-knowledge-graph"
      note: "All seven supported forces retain their actual consumer boundaries; uninspected alternatives prevent a complete force inventory."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Index/graph/review derivation, decision tracing and local-check report admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-index-build"
                - "memory.md#mem-rte-source-review"
                - "memory.md#mem-obj-decision-trace"
                - "runtime.md#rt-rte-local-checks"
              note: "Software admits generated state without a per-content human decision; starting the command is not content approval."
          records:
            - "memory.md#mem-rte-index-build"
            - "memory.md#mem-rte-source-review"
            - "memory.md#mem-obj-decision-trace"
            - "runtime.md#rt-rte-local-checks"
          note: "Mechanical writers are distinct from semantic note authors."
        -
          scope: "Host-model session synthesis, wiki curation and procedural revision absent a separate content approval gate"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-session-handoff"
                - "runtime.md#rt-rte-asset-admission"
                - "epistemic.md#epi-rte-wiki-review"
              note: "The prescribed host can admit a synthesis or revision without separate human approval of each item; no inspected FCVW automatic model service implements it."
          records:
            - "memory.md#mem-rte-session-handoff"
            - "runtime.md#rt-rte-asset-admission"
            - "epistemic.md#epi-rte-wiki-review"
          note: "Automatic describes the software/model admission branch at doctrine strength, not background execution or observed activation."
        -
          scope: "Human-authored wiki content and explicit user decisions admitting product-intent changes"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-wiki"
                - "epistemic.md#epi-rte-divergence-decision"
                - "memory.md#mem-rte-product-review"
              note: "Human authorship supplies content; every divergence requires explicit user direction and approved expectation changes require new source/contract treatment."
          records:
            - "memory.md#mem-obj-wiki"
            - "epistemic.md#epi-rte-divergence-decision"
            - "memory.md#mem-rte-product-review"
          note: "General human veto is not generalized into mandatory human admission for all wiki writes."
        -
          scope: "Arbitrary initial imports, generic upgrade apply callers and remaining plan authoring control"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-framework-upgrade"
            - "runtime.md#rt-rte-governed-change"
          note: "Initial note approval is unspecified; an apply flag or generic host identity does not prove per-content human control."
        -
          scope: "Navigation graph/catalog admission body"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-graph"
          note: "Inventory names the mechanism but does not resolve its full writer."
      records:
        - "memory.md#mem-rte-index-build"
        - "memory.md#mem-rte-source-review"
        - "memory.md#mem-obj-decision-trace"
        - "runtime.md#rt-rte-local-checks"
        - "memory.md#mem-rte-session-handoff"
        - "runtime.md#rt-rte-asset-admission"
        - "epistemic.md#epi-rte-wiki-review"
        - "memory.md#mem-obj-wiki"
        - "epistemic.md#epi-rte-divergence-decision"
        - "memory.md#mem-rte-product-review"
        - "runtime.md#rt-rte-framework-upgrade"
        - "runtime.md#rt-rte-governed-change"
        - "memory.md#mem-obj-knowledge-graph"
      note: "Known software/model and explicit human content decisions coexist with unresolved initialization/caller control; neither file I/O nor workflow launch determines agency."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Host synthesis of bounded sessions and reusable source/work notes"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-session-handoff"
                - "runtime.md#rt-rte-asset-admission"
              note: "Extracting concise continuity state and merging reusable knowledge reduces/reorganizes retained source claims."
          records:
            - "memory.md#mem-rte-session-handoff"
            - "runtime.md#rt-rte-asset-admission"
          note: "A source-linked synthesis label does not establish novel-claim synthesis."
        -
          scope: "Host knowledge merge, revision, lifecycle withdrawal and promotion"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-wiki-review"
                - "runtime.md#rt-rte-asset-admission"
              note: "Merge before create avoids or combines overlapping reusable entries."
            -
              value: "evolve"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-wiki-review"
                - "memory.md#mem-rte-source-review"
              note: "Review can update existing knowledge after source changes."
            -
              value: "invalidate"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-wiki-review"
                - "memory.md#mem-rte-source-review"
              note: "Host review may supersede or invalidate reliance while retaining history."
            -
              value: "promote"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-wiki-review"
                - "runtime.md#rt-rte-asset-admission"
              note: "Reusable sourced work/session material is selected into canonical reusable knowledge."
          records:
            - "epistemic.md#epi-rte-wiki-review"
            - "memory.md#mem-rte-source-review"
            - "runtime.md#rt-rte-asset-admission"
          note: "Semantic operations are prescribed host work, not wired consequences of digest warnings."
        -
          scope: "Lifecycle status at retained-index ranking consumer"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
              note: "Obsolete, superseded, contradictory and archived indexed records are downweighted by the recorded multiplier rather than withdrawn."
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "This is reduced salience during retrieval, not deletion or automatic page invalidation."
        -
          scope: "Semantic novelty of host-generated wiki synthesis and generalization"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-wiki-review"
          note: "No paired inputs/outputs establish a new claim absent from inputs; synthesize is not inferred from a page category or fluency."
        -
          scope: "Navigation/catalog maintenance internals"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-graph"
          note: "The separate navigation route was not inspected completely; rebuild alone would establish no curation operation."
      records:
        - "memory.md#mem-rte-session-handoff"
        - "runtime.md#rt-rte-asset-admission"
        - "epistemic.md#epi-rte-wiki-review"
        - "memory.md#mem-rte-source-review"
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-obj-knowledge-graph"
      note: "Supported host transformations remain claimed; wired lifecycle downweighting is separate. Index packaging, hash checks, graph inverse generation and archive relocation alone add no semantic curation value."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested wiki/handoff resume, lexical/graph query, MCP sections/queue/routes and retained-metadata check invocations"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "runtime.md#rt-rte-mcp-checks"
                - "epistemic.md#epi-rte-evidence-check"
                - "epistemic.md#epi-rte-source-review"
                - "memory.md#mem-rte-product-review"
              note: "Invoking consumers request stored excerpts, sections, plan state or metadata comparisons."
            -
              value: "pull"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-session-handoff"
                - "memory.md#mem-bap-knowledge-consumption"
                - "runtime.md#rt-rte-asset-admission"
              note: "Hosts are instructed to request relevant session/project knowledge and revised guidance on demand."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "runtime.md#rt-rte-mcp-checks"
            - "epistemic.md#epi-rte-evidence-check"
            - "epistemic.md#epi-rte-source-review"
            - "memory.md#mem-rte-product-review"
            - "memory.md#mem-rte-session-handoff"
            - "memory.md#mem-bap-knowledge-consumption"
            - "runtime.md#rt-rte-asset-admission"
          note: "Requested delivery does not become push merely because software selects returned records."
        -
          scope: "Opt-in session-start retained-plan identity supply"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-hook-lifecycle"
              note: "At SessionStart code supplies persisted plan filenames in additionalContext without a specific content request."
          records:
            - "runtime.md#rt-rte-hook-lifecycle"
          note: "All active names and up to five pending names are pushed, not plan or handoff bodies."
        -
          scope: "Navigation graph/catalog later delivery details"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-graph"
          note: "Its exact consumer/delivery route is not resolved by the typed-graph retrieval branch."
        -
          scope: "Linked external QA evidence later consumption"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-qa-run"
          note: "Linked payloads and actual later readers are not supplied; audit-body read-back does not resolve them."
      records:
        - "runtime.md#rt-rte-context-delivery"
        - "runtime.md#rt-rte-mcp-checks"
        - "epistemic.md#epi-rte-evidence-check"
        - "epistemic.md#epi-rte-source-review"
        - "memory.md#mem-rte-product-review"
        - "memory.md#mem-rte-session-handoff"
        - "memory.md#mem-bap-knowledge-consumption"
        - "runtime.md#rt-rte-asset-admission"
        - "runtime.md#rt-rte-hook-lifecycle"
        - "memory.md#mem-obj-knowledge-graph"
        - "memory.md#mem-obj-qa-run"
      note: "Both pull and push exist at wired strength, with claimed manual resume as a separate evidence layer. Unresolved delivery alternatives remain included."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Session-start plan-identity push"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-hook-lifecycle"
              note: "Trigger is SessionStart; selector input is in-progress/pending directory membership and sorted names; selected retained parts are all active filenames and first five pending filenames."
          records:
            - "runtime.md#rt-rte-hook-lifecycle"
          note: "Availability/status grouping and a five-entry cap are coarse selection; emitting IDs is not an identity-match targeted push."
        -
          scope: "Completely characterized requested retrieval/section/resume/check routes"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "runtime.md#rt-rte-mcp-checks"
            - "memory.md#mem-rte-session-handoff"
            - "epistemic.md#epi-rte-evidence-check"
            - "epistemic.md#epi-rte-source-review"
            - "memory.md#mem-rte-product-review"
          note: "These operations answer consumer requests. Lexical/identifier selection inside pull does not establish an inferred-lexical or identifier push signal."
        -
          scope: "Navigation/catalog and linked QA payload delivery alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-graph"
            - "memory.md#mem-obj-qa-run"
          note: "Unknown delivery direction prevents concluding push selection is inapplicable for these alternatives."
      records:
        - "runtime.md#rt-rte-hook-lifecycle"
        - "runtime.md#rt-rte-context-delivery"
        - "runtime.md#rt-rte-mcp-checks"
        - "memory.md#mem-rte-session-handoff"
        - "epistemic.md#epi-rte-evidence-check"
        - "epistemic.md#epi-rte-source-review"
        - "memory.md#mem-rte-product-review"
        - "memory.md#mem-obj-knowledge-graph"
        - "memory.md#mem-obj-qa-run"
      note: "The sole classified push uses coarse availability/status selection. Its identifiers and the query's lexical scorer do not establish targeted push values; unresolved alternatives prevent complete coverage."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Model-host continuation synthesis and work-experience-to-reusable-guidance routes without per-content human admission"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-session-handoff"
                - "runtime.md#rt-rte-asset-admission"
              note: "Prescribed work/validation/failure inputs feed host-produced retained summaries or behavior-shaping notes/skills for later host consumption; no separate human content decision is required on this branch."
          records:
            - "memory.md#mem-rte-session-handoff"
            - "runtime.md#rt-rte-asset-admission"
          note: "This meets the trace-fed durable-artifact definition at doctrine strength, despite lacking an implemented FCVW model writer. It establishes neither observed operation nor improved capacity."
        -
          scope: "Raw imports, arbitrary initialization and mixed-provenance alternative note updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-asset-admission"
          note: "Initial admission and exact original trace input are not resolved for each alternative; no system-wide negative or complete learning inventory follows."
        -
          scope: "Decision traces/local reports as inputs to future automatic updates, and navigation/catalog alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-decision-trace"
            - "runtime.md#rt-rte-local-checks"
            - "memory.md#mem-obj-knowledge-graph"
          note: "The writers show retention and review affordances, not a qualifying automatic later update. No evidenced-absence record supports a local no; further update consumers remain unresolved."
      records:
        - "memory.md#mem-rte-session-handoff"
        - "runtime.md#rt-rte-asset-admission"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-decision-trace"
        - "runtime.md#rt-rte-local-checks"
        - "memory.md#mem-obj-knowledge-graph"
      note: "A supported claimed yes coexists with unresolved included update alternatives. No local or system-wide no is asserted without bounded absence records, and no wired/observed learner is inferred."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Conversation-fed experience-note/continuity branch"
          assessment: "partial"
          findings:
            -
              value: "session-logs"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-asset-admission"
                - "memory.md#mem-rte-session-handoff"
              note: "The accepted memory annotation includes conversation among source inputs to experience-derived retained notes; summaries avoid copying full chat."
          records:
            - "runtime.md#rt-rte-asset-admission"
            - "memory.md#mem-rte-session-handoff"
          note: "Conversation-fed derivation is specified, but each actual note's mixed provenance remains unresolved; not every handoff is assumed transcript-fed."
        -
          scope: "Recorded work validation/failure evidence feeding retained summary or method revision"
          assessment: "partial"
          findings:
            -
              value: "tool-traces"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-session-handoff"
                - "runtime.md#rt-rte-asset-admission"
                - "runtime.md#rt-rte-local-checks"
              note: "Validation results and recorded runtime outcomes can supply execution feedback to the prescribed host summary/revision route."
          records:
            - "memory.md#mem-rte-session-handoff"
            - "runtime.md#rt-rte-asset-admission"
            - "runtime.md#rt-rte-local-checks"
          note: "This is the recorded execution-feedback branch, not a claim that every plan, source file or content-free trace is consumed by a learner."
        -
          scope: "Other mixed input origins, arbitrary imports and linked QA evidence in alternative updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-qa-run"
            - "runtime.md#rt-rte-asset-admission"
          note: "Plans/repository sources and provenance labels do not identify an original qualifying trace type; no event-streams or trajectories value follows from serialization or a multistep workflow."
        -
          scope: "Unresolved future consumers of decision traces/reports and navigation artifacts"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-decision-trace"
            - "runtime.md#rt-rte-local-checks"
            - "memory.md#mem-obj-knowledge-graph"
          note: "Without a qualifying update/later-consumer chain these retained artifacts cannot supply a classified learning source."
      records:
        - "runtime.md#rt-rte-asset-admission"
        - "memory.md#mem-rte-session-handoff"
        - "runtime.md#rt-rte-local-checks"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-qa-run"
        - "memory.md#mem-obj-decision-trace"
        - "memory.md#mem-obj-knowledge-graph"
      note: "Only the prescribed conversation and recorded execution-feedback branches support source values at claimed strength; other mixed origins and update alternatives remain unresolved, not inapplicable."
---

# FrameCode-VibeWork memory profile

## Comparison rationale

### Boundary and coverage

FCVW's memory is primarily project-owned files plus disposable access and check artifacts. The host performs semantic curation; Python implements mechanical derivation, selection and consistency checks. The profile separates retained prose from metadata, compiled copies from source pages, and update consumers from downstream readers. It does not classify the enclosing host's weights or transcript system. The navigation graph/catalog remains an included uninspected alternative, and linked QA payloads remain unresolved rather than classified from the audit's readable description. See [MEM-OBJ-wiki](memory.md#mem-obj-wiki), [MEM-OBJ-context-index](memory.md#mem-obj-context-index), [MEM-OBJ-knowledge-graph](memory.md#mem-obj-knowledge-graph) and [MEM-OBJ-qa-run](memory.md#mem-obj-qa-run).

The reconciliation supersedes four epistemic object declarations with the memory declarations: wiki content, wiki metadata, product contract and QA run. All object references here use those canonical memory records. Epistemic phase records remain distinct, including metadata checks, source review and divergence decisions; their valid route containers are not superseded. See [MEM-OBJ-wiki](memory.md#mem-obj-wiki), [MEM-OBJ-wiki-metadata](memory.md#mem-obj-wiki-metadata), [MEM-OBJ-product-contract](memory.md#mem-obj-product-contract), [MEM-OBJ-qa-run](memory.md#mem-obj-qa-run), [EPI-RTE-evidence-check](epistemic.md#epi-rte-evidence-check) and [EPI-RTE-divergence-decision](epistemic.md#epi-rte-divergence-decision).

### Admission, transformation and authority

Automatic admission is not a synonym for an autonomous FCVW service. The index and report writers are wired software admission. The prescribed model-host synthesis and revision branches require no separate human decision per content item, so they support automatic admission only at claimed strength. Human-supplied content and explicit product-divergence direction are separate manual branches. Unspecified initial imports and generic upgrade callers remain unresolved. See [MEM-RTE-index-build](memory.md#mem-rte-index-build), [MEM-RTE-session-handoff](memory.md#mem-rte-session-handoff), [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission), [EPI-RTE-divergence-decision](epistemic.md#epi-rte-divergence-decision) and [RT-RTE-framework-upgrade](runtime.md#rt-rte-framework-upgrade).

Consolidation, deduplication, revision, promotion and invalidation are prescribed host transformations. Source-digest mismatch itself only emits review candidates. Lifecycle downweighting is wired decay at the ranking consumer, not universal withdrawal or deletion. Neither a page called synthesis nor index packaging establishes synthesis of a new claim. See [MEM-RTE-source-review](memory.md#mem-rte-source-review), [EPI-RTE-wiki-review](epistemic.md#epi-rte-wiki-review) and [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery).

Knowledge, instruction and learning name different consumer paths: notes advise later work; revised skill bodies direct later work; retained experience feeds their update. Ranking, routing and validation concern fixed-rule consumers of retained text/metadata. Plan presence and QA run checks have narrow enforcement force, not universal host isolation. Metadata can influence retrieval before the independent validator flags an authority mismatch; no mandatory validation-before-index chain is established. See [MEM-BAP-knowledge-consumption](memory.md#mem-bap-knowledge-consumption), [RT-BAP-policy-consumption](runtime.md#rt-bap-policy-consumption), [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission), [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle), [EPI-RTE-qa-check](epistemic.md#epi-rte-qa-check) and [EPI-RTE-evidence-check](epistemic.md#epi-rte-evidence-check).

### Selection and trace-fed updates

Requested lexical retrieval, section reads, queue requests and handoff resumption are pull. The session-start hook is push of retained plan identities using coarse directory/status selection and a pending-name cap. Filenames in its output do not establish an identity-match selector. References, digests and outlines do not establish delivery of the underlying claim bodies. The current runtime records already incorporate the MCP/hook read-back correction; the memory report's stale integration-issue description does not override them. See [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-RTE-mcp-checks](runtime.md#rt-rte-mcp-checks), [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle) and [MEM-RTE-session-handoff](memory.md#mem-rte-session-handoff).

The prescribed experience-to-summary/guidance branches qualify for a claimed trace-learning yes: work evidence feeds a retained artifact for a later interpreting consumer, without universal per-content human approval. The memory report's narrower denial of an implemented automatic transcript learner is consistent with this claimed, not wired, finding. The conversation-fed and recorded execution-feedback branches retain their separate source warrants. Arbitrary imported files, unresolved mixed origins and content-free trace retention do not establish additional trace sources. A continuation summary need not improve capacity or add knowledge to meet this axis. See [MEM-RTE-session-handoff](memory.md#mem-rte-session-handoff), [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission), [MEM-OBJ-decision-trace](memory.md#mem-obj-decision-trace) and [RT-RTE-local-checks](runtime.md#rt-rte-local-checks).

There are no accepted evidenced-absence records warranting a local trace-learning no. Unresolved alternatives therefore remain not-determinable; neither the absence of target execution nor lack of demonstrated benefit becomes a negative. The derived system union can retain claimed yes, but cannot support a complete-value learning conclusion. No event-stream or trajectory source is inferred merely from a tool hook, a serialized record or a multi-step workflow. See [MEM-OBJ-wiki](memory.md#mem-obj-wiki), [MEM-OBJ-decision-trace](memory.md#mem-obj-decision-trace) and [RT-RTE-asset-admission](runtime.md#rt-rte-asset-admission).

### Source-read log

No source files were read for this classification. Only the invocation's accepted members and governing contracts were read. No named record ambiguity required an additional frozen-source inspection. All findings retain their evidence layer; no observed operation, causal benefit or complete deployment inventory is asserted.

---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "MDCP memory comparison: project documentation, publication/access derivatives and bounded maintainer feedback, with uninspected alternatives retained."
run-id: "AAS-2026-11-08-mdcp-1e4e8314c1e4-01"
source-identity: "https://github.com/betsalel-williamson/mdcp"
reviewed-boundary: "1a198715a4da72dd89bad93f84cf5d4b3ab56b01"
memory-comparison:
  version: 2
  scope: "Included: mutable source shards/indexes, ADR and research observation/position/clause history, compiled guides and site/publication inputs, refs and evidence links/inserts, reported size measurements, recurrence-derived checking guidance, and retained optimizer descriptions/feedback consumed in later invocations. Included but unresolved: other complementary-archetype products, UX/tutorial-specific content/admissions, detailed evaluator helper artifacts, initial/final admissions and arbitrary callback/peer-dependent transformations. Excluded: unchanged shipped skill/checking policy as such, process-local shard cache used only within one compilation, ordinary current-turn state, external host conversation storage/compaction, provider internals and inference weights, and successor Merlon. Updated guidance and temporary optimizer artifacts count only where retained content reaches a later consumer; no production installation or observed use is inferred."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Source shards, indexes, research observations/positions/clauses and ADR history"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "claimed"
              records: ["memory.md#mem-obj-shards","memory.md#mem-obj-research","memory.md#mem-rte-shard-authoring"]
              note: "The prescribed retained content lives in Markdown and accompanying CSV/JSON files."
            -
              value: "repo"
              basis: "claimed"
              records: ["memory.md#mem-obj-shards","memory.md#mem-rte-shard-authoring"]
              note: "The authoring workflow retains versioned repository documents and superseded ADRs; Git history is not a separate semantic store."
          records: ["memory.md#mem-obj-shards","memory.md#mem-obj-research","memory.md#mem-rte-shard-authoring"]
          note: "Classifies the described project-document family, not all complementary archetypes."
        -
          scope: "Persisted compiled guides, refs, evidence links, inline inserts and measurement CSV"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records: ["memory.md#mem-obj-compiled","memory.md#mem-obj-refs","runtime.md#rt-rte-compile-check","epistemic.md#epi-rte-code-evidence","epistemic.md#epi-rte-inline-inserts","epistemic.md#epi-rte-context-size"]
              note: "Inspected writers and later readers operate on Markdown/JSON/CSV files; encoding does not imply a graph or database."
          records: ["memory.md#mem-obj-compiled","memory.md#mem-obj-refs","runtime.md#rt-rte-compile-check","epistemic.md#epi-rte-code-evidence","epistemic.md#epi-rte-inline-inserts","epistemic.md#epi-rte-context-size"]
          note: "Covers wired file persistence, not exact backup expiry or successful publication."
        -
          scope: "Optimizer candidate descriptions and score/history supplied to later proposal/evaluation invocations"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
              note: "History and current descriptions survive across the bounded loop's separate inference invocations in process state."
            -
              value: "files"
              basis: "wired"
              records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
              note: "Temporary skill files and optional JSON/log outputs retain candidate and feedback material; no production installation is inferred."
          records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
          note: "Temporary lifetime does not exclude later-invocation consumption inside the loop."
        -
          scope: "Additional complementary-archetype products, UX/tutorial-specific retained parts, and detailed evaluator grading/viewer/benchmark feedback artifacts"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-obj-mdcp","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-skill-evaluation"]
          note: "The accepted account includes these alternatives but does not inspect their particular storage substrates. Known project-shard and optimizer witnesses do not close this inventory."
      records: ["memory.md#mem-obj-shards","memory.md#mem-obj-research","memory.md#mem-rte-shard-authoring","memory.md#mem-obj-compiled","memory.md#mem-obj-refs","runtime.md#rt-rte-compile-check","epistemic.md#epi-rte-code-evidence","epistemic.md#epi-rte-inline-inserts","epistemic.md#epi-rte-context-size","runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description","runtime.md#rt-obj-mdcp"]
      note: "File/repository and bounded-loop memory witnesses are supported; additional included product/feedback storage remains uninspected. External inference parameters are not accumulated MDCP memory."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Shard, research, ADR and compiled prose at human/host interpretation paths"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "claimed"
              records: ["memory.md#mem-obj-shards","memory.md#mem-obj-research","runtime.md#rt-rte-feature-work"]
              note: "Project intent, contracts, evidence and recommendations are interpreted by later readers."
            -
              value: "natural-language"
              basis: "wired"
              records: ["memory.md#mem-obj-compiled","runtime.md#rt-rte-compile-check","epistemic.md#epi-rte-inline-inserts"]
              note: "Compiled prose and copied insert text persist for later publication readers; the wiring establishes delivery capacity, not semantic compliance."
          records: ["memory.md#mem-obj-shards","memory.md#mem-obj-research","memory.md#mem-obj-compiled","runtime.md#rt-rte-compile-check","epistemic.md#epi-rte-inline-inserts"]
          note: "Text-consumption paths are separate from compiler syntax."
        -
          scope: "Links/order, refs heading identities, code-location fragments and measurement fields at fixed consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "claimed"
              records: ["memory.md#mem-obj-shards","memory.md#mem-obj-research"]
              note: "Index order/links and structured research data have localized encodings; particular research-data methods remain outside this local syntax classification."
            -
              value: "symbolic"
              basis: "wired"
              records: ["memory.md#mem-obj-refs","runtime.md#rt-rte-compile-check","epistemic.md#epi-rte-code-evidence","epistemic.md#epi-obj-context-size","epistemic.md#epi-rte-context-size"]
              note: "Compiler, refs-list/site and measurement consumers use fixed rules for headings, paths, links and metric fields."
          records: ["memory.md#mem-obj-shards","memory.md#mem-obj-research","memory.md#mem-obj-refs","runtime.md#rt-rte-compile-check","epistemic.md#epi-rte-code-evidence","epistemic.md#epi-obj-context-size","epistemic.md#epi-rte-context-size"]
          note: "Natural-language display titles do not make the registry an opaque semantic payload."
        -
          scope: "Optimizer policy descriptions versus outcome scores/history"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
              note: "Candidate description text guides subsequent trigger interpretation and proposal calls."
            -
              value: "symbolic"
              basis: "wired"
              records: ["runtime.md#rt-rte-skill-evaluation"]
              note: "Scores, labels and history fields feed fixed stopping, blinding and candidate selection rules."
          records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
          note: "Candidate text and feedback fields have different consumption paths; neither establishes updated model weights."
        -
          scope: "Additional complementary-archetype products, UX/tutorial-specific retained parts, and detailed evaluator grading/viewer/benchmark feedback artifacts"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-obj-mdcp","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-skill-evaluation"]
          note: "The accepted account includes these alternatives but does not inspect their particular forms and consumption paths. Known project-shard and optimizer witnesses do not close this inventory."
      records: ["memory.md#mem-obj-shards","memory.md#mem-obj-research","memory.md#mem-obj-compiled","runtime.md#rt-rte-compile-check","epistemic.md#epi-rte-inline-inserts","memory.md#mem-obj-refs","epistemic.md#epi-rte-code-evidence","epistemic.md#epi-obj-context-size","epistemic.md#epi-rte-context-size","runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description","runtime.md#rt-obj-mdcp","memory.md#mem-rte-shard-authoring"]
      note: "Both textual and symbolic memory are supported; external model numerical state is an inference dependency, not evidence of retained parametric MDCP updates."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Project shards, ADRs and research positions/clauses produced through authoring"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "claimed"
              records: ["memory.md#mem-obj-shards","memory.md#mem-obj-research","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-feature-work"]
              note: "Agent/human drafting from task, repository inspection and observations is prescribed; it is not automatically extracted conversation history."
          records: ["memory.md#mem-obj-shards","memory.md#mem-obj-research","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-feature-work"]
          note: "Classifies the prescribed production path, not the unknown authorship of every existing sentence."
        -
          scope: "Mechanical shard acquisition and insert expansion"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records: ["runtime.md#rt-rte-shard-import","epistemic.md#epi-rte-inline-inserts"]
              note: "Mapped external documents/directories become shards, and retained insert bodies are copied into compiled text."
          records: ["runtime.md#rt-rte-shard-import","epistemic.md#epi-rte-inline-inserts"]
          note: "Imported source warrant and parser correctness are not inferred."
        -
          scope: "Default assembled guides, refs, evidence locations and measured size CSV"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records: ["runtime.md#rt-rte-compile-check","memory.md#mem-obj-compiled","memory.md#mem-obj-refs","epistemic.md#epi-rte-code-evidence","epistemic.md#epi-rte-context-size"]
              note: "Deterministic assembly, heading extraction, lexical location derivation and size counting derive retained artifacts without trace extraction."
          records: ["runtime.md#rt-rte-compile-check","memory.md#mem-obj-compiled","memory.md#mem-obj-refs","epistemic.md#epi-rte-code-evidence","epistemic.md#epi-rte-context-size"]
          note: "Default transformations are classified separately from arbitrary registered callback semantics."
        -
          scope: "Feedback-produced candidate descriptions in bounded optimization"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
              note: "Execution outcomes become failure/score history consumed by automatic candidate-description revision, then later proposal/evaluation calls."
          records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
          note: "Trace-fed lineage does not establish faithful rationale or production installation."
        -
          scope: "Initial optimizer description provenance and arbitrary callback output derivation"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-skill-evaluation","runtime.md#rt-rte-hook-extension"]
          note: "Records establish supplied initial text and arbitrary replacement strings, not their complete derivation; a known subsequent feedback route cannot resolve those origins."
        -
          scope: "Additional complementary-archetype products, UX/tutorial-specific retained parts, and detailed evaluator grading/viewer/benchmark feedback artifacts"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-obj-mdcp","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-skill-evaluation"]
          note: "The accepted account includes these alternatives but does not inspect their particular lineages. Known project-shard and optimizer witnesses do not close this inventory."
      records: ["memory.md#mem-obj-shards","memory.md#mem-obj-research","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-feature-work","runtime.md#rt-rte-shard-import","epistemic.md#epi-rte-inline-inserts","runtime.md#rt-rte-compile-check","memory.md#mem-obj-compiled","memory.md#mem-obj-refs","epistemic.md#epi-rte-code-evidence","epistemic.md#epi-rte-context-size","runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description","runtime.md#rt-rte-hook-extension","runtime.md#rt-obj-mdcp"]
      note: "Authorship, import, deterministic compilation and bounded trace-fed revision coexist. Initial and callback provenance plus uninspected products prevent complete lineage enumeration."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Project contracts and research evidence/positions at later host or human readers"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "claimed"
              records: ["memory.md#mem-obj-shards","memory.md#mem-obj-research","runtime.md#rt-rte-feature-work"]
              note: "Current contracts and normative clauses guide later implementation/design decisions."
            -
              value: "knowledge"
              basis: "claimed"
              records: ["memory.md#mem-obj-shards","memory.md#mem-obj-research"]
              note: "Explanations and observation records provide reference/evidence; a record does not itself become a rule."
          records: ["memory.md#mem-obj-shards","memory.md#mem-obj-research","runtime.md#rt-rte-feature-work"]
          note: "These are prescribed effects at interpretation consumers, not verified compliance or accepted truth."
        -
          scope: "Compiled prose and incorporated insert content at later publication readers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records: ["memory.md#mem-obj-compiled","runtime.md#rt-rte-compile-check","epistemic.md#epi-rte-inline-inserts"]
              note: "Publication consumers receive retained reference/context content; generation is not independent corroboration."
          records: ["memory.md#mem-obj-compiled","runtime.md#rt-rte-compile-check","epistemic.md#epi-rte-inline-inserts"]
          note: "Wired content delivery does not prove observed agent readership."
        -
          scope: "Retained index/refs/config and revised checking guidance at deterministic consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records: ["memory.md#mem-obj-shards","memory.md#mem-obj-refs","runtime.md#rt-rte-compile-check","runtime.md#rt-obj-config"]
              note: "Index links/order, heading/output identities and config select compilation scope and publication link/navigation destinations."
            -
              value: "validation"
              basis: "claimed"
              records: ["runtime.md#rt-rte-doc-review","runtime.md#rt-obj-config"]
              note: "Recurrence-driven threshold/Vale-rule edits are prescribed criteria for later checks."
            -
              value: "enforcement"
              basis: "claimed"
              records: ["runtime.md#rt-rte-doc-review","runtime.md#rt-rte-compile-check","runtime.md#rt-obj-config"]
              note: "When such retained criteria are installed and enabled at an error/strict gate, failures veto check success, not prior file writes."
          records: ["memory.md#mem-obj-shards","memory.md#mem-obj-refs","runtime.md#rt-rte-compile-check","runtime.md#rt-obj-config","runtime.md#rt-rte-doc-review"]
          note: "Static shipped configuration alone is excluded; this unit includes accumulated indexes/refs and the prescribed mutable policy update path."
        -
          scope: "Optimizer feedback at update/selection consumers and revised candidate at trigger consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records: ["runtime.md#rt-rte-skill-evaluation"]
              note: "Retained execution failures/history feed automatic durable candidate-policy revision for subsequent invocations; this is update authority, not demonstrated capacity gain."
            -
              value: "ranking"
              basis: "wired"
              records: ["runtime.md#rt-rte-skill-evaluation"]
              note: "Persisted/retained passed counts determine relative candidate priority and best-description selection."
            -
              value: "routing"
              basis: "wired"
              records: ["runtime.md#rt-rte-skill-evaluation"]
              note: "Failure counts control continuation/stopping and the next proposal/evaluation input."
            -
              value: "instruction"
              basis: "wired"
              records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
              note: "Candidate prose is installed in temporary skill descriptions for later trigger interpretation, separately from production installation."
          records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
          note: "Different consumers give the feedback and candidate text different forces."
        -
          scope: "Additional complementary-archetype products, UX/tutorial-specific retained parts, and detailed evaluator grading/viewer/benchmark feedback artifacts"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-obj-mdcp","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-skill-evaluation"]
          note: "The accepted account includes these alternatives but does not inspect their particular consumers and behavioral effects. Known project-shard and optimizer witnesses do not close this inventory."
      records: ["memory.md#mem-obj-shards","memory.md#mem-obj-research","runtime.md#rt-rte-feature-work","memory.md#mem-obj-compiled","runtime.md#rt-rte-compile-check","epistemic.md#epi-rte-inline-inserts","memory.md#mem-obj-refs","runtime.md#rt-obj-config","runtime.md#rt-rte-doc-review","runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description","runtime.md#rt-obj-mdcp","memory.md#mem-rte-shard-authoring"]
      note: "Authority is attached to consumed memory, not the entire CLI permission surface. Mechanical gates are conditional; no content's operational use proves semantic acceptance."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Agent-mediated shard authoring, feature updates and semantic review admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "claimed"
              records: ["memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-feature-work","runtime.md#rt-rte-doc-review"]
              note: "Host-agent decisions admit edits without universal per-content human approval; starting work is not manual content admission."
          records: ["memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-feature-work","runtime.md#rt-rte-doc-review"]
          note: "This classifies the prescribed agent-led admission path only; conditional review is a distinct possible mechanism."
        -
          scope: "Import, peer fixes, default derivatives/refs, measurement output and optimizer candidate admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records: ["runtime.md#rt-rte-shard-import","memory.md#mem-rte-peer-fix","runtime.md#rt-rte-compile-check","memory.md#mem-obj-refs","epistemic.md#epi-rte-context-size","runtime.md#rt-rte-skill-evaluation"]
              note: "Software/model control writes or selects resulting retained content without per-content operator approval in these actions."
          records: ["runtime.md#rt-rte-shard-import","memory.md#mem-rte-peer-fix","runtime.md#rt-rte-compile-check","memory.md#mem-obj-refs","epistemic.md#epi-rte-context-size","runtime.md#rt-rte-skill-evaluation"]
          note: "Caller initiation and physical filesystem I/O do not determine agency."
        -
          scope: "Conditional human approval, initial content intake and final optimizer production installation"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-shards","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-feature-work","runtime.md#rt-rte-skill-evaluation"]
          note: "Human review can occur and an author must apply the returned description, but records do not establish who supplies/approves each admitted content item or whether installation is human-controlled. No manual finding is warranted from generic author/caller identity."
        -
          scope: "Arbitrary callback-specific content admission"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-hook-extension"]
          note: "Registration and invocation are wired, but the supplied callback's own admission policy and input control are unspecified."
        -
          scope: "Additional complementary-archetype products, UX/tutorial-specific retained parts, and detailed evaluator grading/viewer/benchmark feedback artifacts"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-obj-mdcp","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-skill-evaluation"]
          note: "The accepted account includes these alternatives but does not inspect their particular admission controls. Known project-shard and optimizer witnesses do not close this inventory."
      records: ["memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-feature-work","runtime.md#rt-rte-doc-review","runtime.md#rt-rte-shard-import","memory.md#mem-rte-peer-fix","runtime.md#rt-rte-compile-check","memory.md#mem-obj-refs","epistemic.md#epi-rte-context-size","runtime.md#rt-rte-skill-evaluation","memory.md#mem-obj-shards","runtime.md#rt-rte-hook-extension","runtime.md#rt-obj-mdcp"]
      note: "Automatic admission is supported at distinct evidence layers. Unresolved initial/final and alternative admissions are retained instead of asserting all writes are automatic or manual."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Semantic current-shard review and as-built revision"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "afforded"
              records: ["runtime.md#rt-rte-doc-review"]
              note: "Review permits merging/reducing existing shard content into a smaller canonical representation."
            -
              value: "dedup"
              basis: "afforded"
              records: ["runtime.md#rt-rte-doc-review"]
              note: "Duplication findings can lead to canonical ownership and removal/merging of repeated content; diagnostics alone do not perform this operation."
            -
              value: "evolve"
              basis: "claimed"
              records: ["memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-feature-work"]
              note: "Current entries are revised to present intent/as-built behavior."
          records: ["runtime.md#rt-rte-doc-review","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-feature-work"]
          note: "Prescribed semantic transformations are not upgraded to implemented automatic cleanup."
        -
          scope: "Research observation and ADR supersession while history remains"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "claimed"
              records: ["memory.md#mem-obj-research","memory.md#mem-rte-shard-authoring"]
              note: "Replacement links withdraw current reliance while keeping the prior observation/ADR available."
          records: ["memory.md#mem-obj-research","memory.md#mem-rte-shard-authoring"]
          note: "Ordinary deletion alone would not establish history-preserving invalidation; these explicit exceptions do."
        -
          scope: "Automatic candidate description replacement using retained feedback"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
              note: "The optimizer revises the current description and uses the result in the next evaluation/proposal round."
          records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
          note: "No synthesis of a new warranted claim or measured improvement follows from model revision."
        -
          scope: "Arbitrary hook transformations, exact external peer fixes and detailed publication/backup maintenance"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-hook-extension","memory.md#mem-rte-peer-fix","runtime.md#rt-rte-compile-check"]
          note: "The wrapper establishes mutation/rewriting, not a controlled curation operation for every opaque transform. Rebuilds, formatting, acquisition and backup alone establish none."
        -
          scope: "Additional complementary-archetype products, UX/tutorial-specific retained parts, and detailed evaluator grading/viewer/benchmark feedback artifacts"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-obj-mdcp","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-skill-evaluation"]
          note: "The accepted account includes these alternatives but does not inspect their particular curation transformations. Known project-shard and optimizer witnesses do not close this inventory."
      records: ["runtime.md#rt-rte-doc-review","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-feature-work","memory.md#mem-obj-research","runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description","runtime.md#rt-rte-hook-extension","memory.md#mem-rte-peer-fix","runtime.md#rt-rte-compile-check","runtime.md#rt-obj-mdcp"]
      note: "Supported maintenance and optimizer revision coexist with opaque transformations. No decay, promotion or synthesis finding is inferred merely from command names or generated prose."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested host shard discovery and review reads"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "claimed"
              records: ["runtime.md#rt-rte-feature-work","memory.md#mem-rte-shard-authoring"]
              note: "The foreground agent requests task-relevant shards through search/index and file reads."
            -
              value: "pull"
              basis: "afforded"
              records: ["runtime.md#rt-rte-doc-review"]
              note: "Review requests indexes, signal-targeted shards and samples; this is an agent-directed read, not autonomous compiler injection."
          records: ["runtime.md#rt-rte-feature-work","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-doc-review"]
          note: "One-shard guidance is qualitative; host window eviction remains outside this memory boundary."
        -
          scope: "Requested compile/check, refs-list, site preparation and measurement file reads"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records: ["runtime.md#rt-rte-compile-check","memory.md#mem-obj-refs","epistemic.md#epi-rte-context-size"]
              note: "Caller-invoked operations request retained source/derived material; deterministic fulfillment and downstream publication assembly are not additional unsolicited model pushes."
          records: ["runtime.md#rt-rte-compile-check","memory.md#mem-obj-refs","epistemic.md#epi-rte-context-size"]
          note: "Later CLI/site readers are concrete consumers, not hypothetical API callers."
        -
          scope: "Optimizer delivery of retained current description and feedback/history to subsequent proposal/evaluation calls"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
              note: "The loop automatically constructs subsequent inference inputs from retained candidate/feedback state without a request for that memory from those model invocations."
          records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
          note: "Automatic input assembly is distinct from a caller's initial request to run optimization."
        -
          scope: "Additional complementary-archetype products, UX/tutorial-specific retained parts, and detailed evaluator grading/viewer/benchmark feedback artifacts"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-obj-mdcp","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-skill-evaluation"]
          note: "The accepted account includes these alternatives but does not inspect their particular read-back operations. Known project-shard and optimizer witnesses do not close this inventory."
      records: ["runtime.md#rt-rte-feature-work","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-doc-review","runtime.md#rt-rte-compile-check","memory.md#mem-obj-refs","epistemic.md#epi-rte-context-size","runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description","runtime.md#rt-obj-mdcp"]
      note: "Both requested reads and automatic optimizer context supply exist. Session-start installation of static vendor skill is excluded from accumulated-memory push."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Optimizer next-proposal/evaluation context supply"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
              note: "Trigger: continuing optimizer iteration. Selector inputs: current description, current failures and retained history. Selected parts: current policy plus failure/history fields with test-prefixed history fields removed. This is fixed availability/status filtering, not a relevance embedding or identifier match."
          records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
          note: "Score-based returned-best selection is separately a ranking effect, not evidence for an inferred relevance push signal."
        -
          scope: "Explicitly requested host, compiler, registry and site read routes"
          assessment: "inapplicable"
          findings: []
          records: ["runtime.md#rt-rte-feature-work","runtime.md#rt-rte-compile-check","memory.md#mem-obj-refs","runtime.md#rt-rte-doc-review"]
          note: "These units fulfill requests for retained material, so their file identities, manifest matching and search terms do not establish a push signal."
        -
          scope: "Additional complementary-archetype products, UX/tutorial-specific retained parts, and detailed evaluator grading/viewer/benchmark feedback artifacts"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-obj-mdcp","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-skill-evaluation"]
          note: "The accepted account includes these alternatives but does not inspect their particular push selectors and selected parts. Known project-shard and optimizer witnesses do not close this inventory."
      records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description","runtime.md#rt-rte-feature-work","runtime.md#rt-rte-compile-check","memory.md#mem-obj-refs","runtime.md#rt-rte-doc-review","runtime.md#rt-obj-mdcp","memory.md#mem-rte-shard-authoring"]
      note: "Only the bounded optimizer's coarse context supply is classified. Pull-only local routes cannot make uninspected alternatives inapplicable across the axis."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Automatic trigger-feedback-driven candidate-description revision with subsequent proposal/evaluation consumers"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
              note: "Execution outcomes are retained as failures/scores/history, automatically feed revised behavior-shaping description text, and reach later inference invocations through temporary skill files and loop inputs."
          records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description"]
          note: "This bounded maintainer learning route qualifies without production installation, parameter updates, observed activation or measured improvement."
        -
          scope: "Recurrence-responsive semantic review updates"
          assessment: "partial"
          findings:
            -
              value: "yes"
              basis: "claimed"
              records: ["runtime.md#rt-rte-doc-review"]
              note: "The workflow asks the host agent to use repeated findings to revise durable thresholds/glossary/Vale guidance for later checks/agents without mandatory per-content human approval."
          records: ["runtime.md#rt-rte-doc-review"]
          note: "The prescription supports the route, not completed uptake. Records do not specify a durable diagnostic history store or all actual trace-to-guidance admissions, preventing a complete route inventory."
        -
          scope: "Initial documents, arbitrary callback updates, external peer behavior and other feedback products"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-shards","runtime.md#rt-rte-hook-extension","memory.md#mem-rte-peer-fix","runtime.md#rt-rte-skill-evaluation"]
          note: "These records do not bound every input/update/later-consumer chain. No evidenced-absence records support local or system-wide no."
        -
          scope: "Additional complementary-archetype products, UX/tutorial-specific retained parts, and detailed evaluator grading/viewer/benchmark feedback artifacts"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-obj-mdcp","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-skill-evaluation"]
          note: "The accepted account includes these alternatives but does not inspect their particular trace-fed writes and later consumers. Known project-shard and optimizer witnesses do not close this inventory."
      records: ["runtime.md#rt-rte-skill-evaluation","epistemic.md#epi-obj-skill-description","runtime.md#rt-rte-doc-review","memory.md#mem-obj-shards","runtime.md#rt-rte-hook-extension","memory.md#mem-rte-peer-fix","runtime.md#rt-obj-mdcp","memory.md#mem-rte-shard-authoring"]
      note: "A wired yes exists in bounded optimization and a claimed recurrence-update route exists. Incomplete alternatives prevent complete learning-inventory coverage; no claim of general capacity improvement or production self-improvement is made."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Trigger optimizer execution feedback consumed by candidate-description revision"
          assessment: "partial"
          findings:
            -
              value: "tool-traces"
              basis: "wired"
              records: ["runtime.md#rt-rte-skill-evaluation"]
              note: "Recorded Claude-subprocess trigger execution outcomes and failure feedback feed the automatic policy update, rather than being merely archived."
          records: ["runtime.md#rt-rte-skill-evaluation"]
          note: "Static should_trigger labels and query text are auxiliary inputs, not session logs merely because sent to a model. The records do not fully expose original content/provenance of all optional proposal logs and broader feedback inputs, so additional source classes remain unresolved."
        -
          scope: "Recurring review findings used to change retained checking guidance"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-doc-review"]
          note: "Repeated findings are named, but the accepted record does not establish their original trace content and recording form sufficiently to choose event-streams, tool-traces, session-logs or trajectories. A workflow recurrence label alone is insufficient."
        -
          scope: "Other qualifying writes among arbitrary callbacks, peer-dependent changes and broader evaluator products"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-hook-extension","memory.md#mem-rte-peer-fix","runtime.md#rt-rte-skill-evaluation"]
          note: "Neither qualifying trace-learning routes nor their original input contents are completely established; another route's positive cannot make these sources inapplicable."
        -
          scope: "Additional complementary-archetype products, UX/tutorial-specific retained parts, and detailed evaluator grading/viewer/benchmark feedback artifacts"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-obj-mdcp","memory.md#mem-rte-shard-authoring","runtime.md#rt-rte-skill-evaluation"]
          note: "The accepted account includes these alternatives but does not inspect their particular original trace content. Known project-shard and optimizer witnesses do not close this inventory."
      records: ["runtime.md#rt-rte-skill-evaluation","runtime.md#rt-rte-doc-review","runtime.md#rt-rte-hook-extension","memory.md#mem-rte-peer-fix","runtime.md#rt-obj-mdcp","memory.md#mem-rte-shard-authoring"]
      note: "Tool-execution feedback has a supported local source mapping. No session-logs or trajectories are inferred from prompts, and no event-streams are inferred solely from wrapping or counting runtime outcomes."
---

# MDCP memory profile

## Comparison rationale

This comparison classifies accepted records, not a new source inspection. All ten axes remain partial because the memory account includes uninspected complementary products and evaluator-helper artifacts. A whole-system functional boundary does not establish complete classification coverage. Local known units describe the named mechanisms, not an assertion that every possible controlled value has been enumerated.

### Documents, derivatives and policy

[MEM-OBJ-shards](memory.md#mem-obj-shards) separates mutable project contracts from installed vendor policy. Text has instruction or knowledge authority at interpreting readers; links and ordering have symbolic routing effects at the compiler. [MEM-OBJ-research](memory.md#mem-obj-research) further separates observations from positions and normative clauses. The observation supplies evidence, not a command. Research-record and ADR supersession support history-preserving invalidation; deletion of ordinary current prose alone would not.

[MEM-OBJ-compiled](memory.md#mem-obj-compiled), [MEM-OBJ-refs](memory.md#mem-obj-refs) and [RT-RTE-compile-check](runtime.md#rt-rte-compile-check) establish file-based derivatives and concrete later CLI/site consumers. A refs title is not a semantic memory payload, and its heading/path fields have fixed consumers. [EPI-RTE-code-evidence](epistemic.md#epi-rte-code-evidence) adds computed lexical locations; [EPI-RTE-inline-inserts](epistemic.md#epi-rte-inline-inserts) adds imported bodies. Neither is independent warrant for surrounding prose. [EPI-OBJ-context-size](epistemic.md#epi-obj-context-size) and [EPI-RTE-context-size](epistemic.md#epi-rte-context-size) add retained measurement fields and their deterministic production route, not observed agent savings.

Static shipped configuration is not itself accumulated memory. The authority inventory includes configuration/checking guidance only on the recurrence-update path described in [RT-RTE-doc-review](runtime.md#rt-rte-doc-review), and includes indexes/refs as changing access structures. Likewise, the host model is not assigned model-weights storage or parametric memory simply because inference consumes these documents. The compiler's process-local shard cache is excluded from later-invocation memory; retained optimizer state crossing separate inference invocations is included.

### Admission and maintenance

[MEM-RTE-shard-authoring](memory.md#mem-rte-shard-authoring) and [RT-RTE-feature-work](runtime.md#rt-rte-feature-work) prescribe agent admission without mandatory per-content human approval. That supports claimed automatic agency for the agent-mediated route, not manual agency from user initiation. Conditional approval, unknown initial content control and the further author action installing a returned optimizer description remain unresolved admissions. Mechanical import, compilation, peer fixing and internal optimizer selection independently support wired automatic agency.

Review merge/dedup operations remain afforded, and current-state authoring and history-preserving supersession remain claimed. The optimizer's candidate revision is wired evolution. No synthesis is inferred from generated wording or research positions without a recorded input/output relation establishing a new claim; no decay or promotion is inferred from deletion, backups or rebuilding. [RT-RTE-hook-extension](runtime.md#rt-rte-hook-extension) and [MEM-RTE-peer-fix](memory.md#mem-rte-peer-fix) establish mutations but not every opaque transformation's semantic operation.

Reconciliation supersedes the epistemic peer-fix declaration with [MEM-RTE-peer-fix](memory.md#mem-rte-peer-fix). This profile uses that canonical route. The amendment changes citation identity, not a value or basis. Compile body and persisted compiled files remain distinct lifecycle scopes; candidate descriptions remain separate from installed vendor skill policy. No other supersession changes a comparison value.

### Read-back and trace-fed policy updates

The host asks for shards, and caller-invoked compile/refs/site operations ask for retained files. Their requested delivery is pull even where deterministic selection occurs inside the chain. File paths and manifest identity matches therefore do not establish identifier-based push. The parent skill's static session-start installation is not accumulated-memory injection.

[RT-RTE-skill-evaluation](runtime.md#rt-rte-skill-evaluation) and [EPI-OBJ-skill-description](epistemic.md#epi-obj-skill-description) establish a different route: the loop supplies retained candidate and failure/history state to subsequent inference invocations automatically. Fixed failure/status and history-field filtering support coarse push. The scores separately have ranking authority at candidate selection. Neither scalar scoring nor a best-description label supports embedding, lexical relevance or model-judgment push selection.

Execution feedback feeds automatic policy-description revision, which later proposal/evaluation invocations consume. That supports wired trace learning within the bounded maintainer loop even though final production installation is separate and operation/benefit are unobserved. The feedback has learning authority at the update consumer; the resulting candidate has instruction authority at its next trigger consumer. Local retained files and cross-invocation loop state supply the relevant horizon; there is no inference of model-weight updates or permanent production modification.

The subprocess execution-feedback part supports tool-traces as an original source. Static fixture labels do not become session logs by entering a model call; runtime occurrence alone does not justify an additional event-streams classification. Optional logs and broader grading inputs retain their unresolved provenance. Review recurrence supports a claimed guidance-update route but does not identify original trace content precisely enough to classify its trace source. No evidenced-absence record licenses a local or system-wide trace-learning no, and unresolved alternatives cannot be made inapplicable by a known route.

### Evidence and remaining coverage

Each finding keeps its own claimed, afforded or wired basis. No observed or causal basis is supplied by this profile. Unknown complementary products, UX/tutorial details, evaluator artifacts, callback semantics, initial/final admission control and precise backup/publication maintenance prevent stronger inventory conclusions. External host compaction and provider state are boundary exclusions, not negative findings about MDCP.

Source-read log: none. The supplied accepted members and reconciliation sufficed; no source ambiguity required reopening a cited source file.

---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Autocontext memory comparison: retained bundles, lessons, reports, compaction ledgers, imported knowledge and model/code improvement state."
run-id: AAS-2026-10-15-autocontext-b7f59f8405c4-01
source-identity: https://github.com/greyhaven-ai/autocontext
reviewed-boundary: f72c154152397f54d55407508b153d28861888a5
memory-comparison:
  version: 2
  scope: >-
    Retained material accumulated or changed through use in Python and npm:
    immutable context-bundle parts, mutable playbooks/hints and SKILL lessons,
    generation reports/replays/metrics and SQLite history, package payloads and
    snapshots, compaction entries and their access structures, training checkpoints,
    serving bindings and evolving training/kernel source. Includes their admission,
    maintenance, prompt delivery, requested MCP/Pi retrieval and afforded host-file
    consumption. Included unresolved alternatives are notebook/report/hint writers,
    evidence and production-trace/dataset processing, npm maintenance and memory
    packs, session/mission reload, configured hooks, provider/host retained state and
    model-serving reload. Excludes unchanged shipped instructions and ordinary
    transient strategy/round state unless retained for a later invocation. Session
    extraction-only returns are not treated as demonstrated durable promotion.
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Bundle advice, routing JSON, four mutation payloads, reference helper source and digest-scoped executable validators"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-context-bundle, memory.md#mem-obj-harness-validator]
              note: "Immutable bundle JSON and materialized validator Python files are the retained substrate; JSON is an encoding, not a database."
          records: [memory.md#mem-obj-context-bundle, memory.md#mem-obj-bundle-advice, memory.md#mem-obj-routing-config, memory.md#mem-obj-prompt-fragment, memory.md#mem-obj-context-policy, memory.md#mem-obj-completion-check, memory.md#mem-obj-tool-instruction, memory.md#mem-obj-tool-spec, memory.md#mem-obj-harness-validator]
          note: "The container enumerates eight operative parts; each is retained in the file-backed bundle."
        - scope: "Mutable lessons, playbooks, hints, package-installed source, snapshots and compaction ledger"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-skill-lessons, memory.md#mem-rte-package-import, memory.md#mem-obj-compaction-entry]
              note: "Markdown, Python, JSON/JSONL and copied snapshot files retain these parts."
          records: [memory.md#mem-obj-skill-lessons, memory.md#mem-rte-package-import, memory.md#mem-obj-compaction-entry]
          note: "Covers inspected file objects, not complete opaque host state reached through skill discovery."
        - scope: "Generation artifacts and imported attributed history"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-generation-artifacts, epistemic.md#epi-obj-package-history]
              note: "Reports, replay/metrics JSON, history Markdown and package metadata are retained on disk."
            - value: sqlite
              basis: wired
              records: [memory.md#mem-obj-generation-artifacts, epistemic.md#epi-obj-package-history]
              note: "Generation/activity records and optional synthetic imported history use SQLite."
          records: [memory.md#mem-obj-generation-artifacts, epistemic.md#epi-obj-package-history]
          note: "File bodies and database rows are separate supported substrates within this inventory."
        - scope: "Python component-compaction lookup cache"
          assessment: known
          findings:
            - value: in-memory
              basis: wired
              records: [memory.md#mem-rte-component-compaction]
              note: "A bounded 512-entry LRU caches component transformations using verified input text and digest/policy keys."
          records: [memory.md#mem-rte-component-compaction]
          note: "This is an access structure, not an opaque full-model checkpoint."
        - scope: "Local training checkpoints, registry artifacts and evolving training/kernel source"
          assessment: partial
          findings:
            - value: files
              basis: wired
              records: [runtime.md#rt-cmp-training-checkpoints, runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution]
              note: "Backend checkpoint directories, registry artifacts and campaign source/receipts are file-retained."
            - value: repo
              basis: wired
              records: [runtime.md#rt-rte-training-experiments]
              note: "Training-source experiments commit train.py and use TrainingGitState for keep/discard recovery."
          records: [runtime.md#rt-cmp-training-checkpoints, runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution, runtime.md#rt-rte-ambient-promotion]
          note: "Backend/serving internals and complete registry reload are not inspected; file paths do not establish immutable parameter identities."
        - scope: "Opaque provider/host sessions, npm memory packs, mission/session state and remaining notebook/evidence/trace stores"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-runtime-dispatch, runtime.md#rt-rte-ambient-promotion, runtime.md#rt-rte-context-assembly]
          note: "Adapters/loaders establish included seams, not their complete operative storage inventory. No service, vector or other substrate is inferred from those seams."
      records: [memory.md#mem-obj-context-bundle, memory.md#mem-obj-generation-artifacts, memory.md#mem-obj-compaction-entry, memory.md#mem-rte-package-import, memory.md#mem-rte-component-compaction, runtime.md#rt-cmp-training-checkpoints, runtime.md#rt-rte-runtime-dispatch]
      note: "The accepted inventory supports file, SQLite, repository and cache storage, while opaque and uninspected stores prevent complete enumeration."
    representational_form:
      assessment: partial
      units:
        - scope: "Advice bodies in bundle playbook/hints/legacy guidance, four mutations, live SKILL lessons, imported guidance, analysis and ledger summaries"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-bundle-advice, memory.md#mem-obj-prompt-fragment, memory.md#mem-obj-context-policy, memory.md#mem-obj-completion-check, memory.md#mem-obj-tool-instruction, memory.md#mem-obj-skill-lessons, memory.md#mem-obj-generation-artifacts, memory.md#mem-obj-compaction-entry, epistemic.md#epi-obj-package-playbook, epistemic.md#epi-obj-package-hints, epistemic.md#epi-obj-package-lessons]
              note: "Text is interpreted by role/host models or inspection consumers; a checklist name does not make its prose executable validation."
          records: [memory.md#mem-obj-bundle-advice, memory.md#mem-obj-skill-lessons, memory.md#mem-obj-compaction-entry, memory.md#mem-obj-generation-artifacts]
          note: "Covers the text parts only; typed wrappers and identities are classified separately."
        - scope: "Routing, mutation target/type metadata, replay/metrics, package strategy/history and ledger access metadata"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-routing-config, memory.md#mem-obj-prompt-fragment, memory.md#mem-obj-context-policy, memory.md#mem-obj-completion-check, memory.md#mem-obj-tool-instruction, memory.md#mem-obj-generation-artifacts, memory.md#mem-obj-compaction-entry, epistemic.md#epi-obj-package-history]
              note: "Localized keys, flags, identifiers, scores and sequence/linkage fields have fixed code consumers; numerical metrics are not distributed parameters."
          records: [memory.md#mem-obj-routing-config, memory.md#mem-obj-generation-artifacts, memory.md#mem-obj-compaction-entry, epistemic.md#epi-obj-package-history]
          note: "Separates access/control data from natural-language payloads."
        - scope: "Reference helper source versus executable validator and evolving training/kernel source"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-tool-spec, memory.md#mem-obj-harness-validator, epistemic.md#epi-obj-package-harness, runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution]
              note: "Python/kernel syntax and typed source payloads are symbolic; installation and execution are route-specific."
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-tool-spec]
              note: "The bundle helper's description/source also reaches a role model as explicitly noncallable reference context."
          records: [memory.md#mem-obj-tool-spec, memory.md#mem-obj-harness-validator, epistemic.md#epi-obj-package-harness, runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution]
          note: "The helper has a separate interpretive consumption path; this does not make its rendering a tool grant."
        - scope: "Trainer-produced checkpoint weights/adapters and their registry metadata"
          assessment: known
          findings:
            - value: parametric
              basis: wired
              records: [runtime.md#rt-cmp-training-checkpoints]
              note: "Training changes distributed numerical weights or adapters."
            - value: symbolic
              basis: wired
              records: [runtime.md#rt-cmp-training-checkpoints, runtime.md#rt-rte-ambient-promotion]
              note: "Registry bindings and evaluation/probation metadata are distinct fixed-rule selection data."
          records: [runtime.md#rt-cmp-training-checkpoints, runtime.md#rt-rte-ambient-promotion]
          note: "Classification describes the implemented component, not observed checkpoint contents or exact parameter versions."
        - scope: "Opaque host/provider continuation payloads and other uninspected memory-pack/notebook/evidence parts"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-runtime-dispatch, runtime.md#rt-rte-context-assembly]
          note: "Readable prompt/ledger summaries do not classify full opaque payloads or omitted parts."
      records: [memory.md#mem-obj-context-bundle, memory.md#mem-obj-generation-artifacts, memory.md#mem-obj-compaction-entry, runtime.md#rt-cmp-training-checkpoints, runtime.md#rt-rte-runtime-dispatch]
      note: "Natural-language, symbolic and parametric parts are supported separately; included opaque alternatives prevent complete coverage."
    lineage:
      assessment: partial
      units:
        - scope: "Subsequent coach/architect bundle proposals and evolving training/kernel programs"
          assessment: known
          findings:
            - value: authored
              basis: wired
              records: [memory.md#mem-obj-bundle-advice, memory.md#mem-obj-prompt-fragment, memory.md#mem-obj-context-policy, memory.md#mem-obj-completion-check, memory.md#mem-obj-tool-instruction, memory.md#mem-obj-tool-spec, memory.md#mem-obj-harness-validator, runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution]
              note: "Model proposals author new advice/source; this is not a claim that generated prose is a checked derivation."
          records: [epistemic.md#epi-rte-role-proposals, memory.md#mem-obj-context-bundle, runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution]
          note: "Scope is the inspected subsequent proposal path, not initial content provenance."
        - scope: "Bundle capture/overlay, routing snapshots and deterministic compaction/access metadata"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-context-bundle, memory.md#mem-obj-routing-config, memory.md#mem-rte-component-compaction, memory.md#mem-obj-compaction-entry]
              note: "Code captures configured state, preserves/overlays components by identity and structurally selects text or emits linkage metadata."
          records: [memory.md#mem-obj-context-bundle, memory.md#mem-obj-routing-config, memory.md#mem-rte-component-compaction, memory.md#mem-obj-compaction-entry]
          note: "Known compilation does not resolve the ancestry of captured text."
        - scope: "Rollback warnings and trace-derived operational lesson maintenance"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-rte-lesson-maintenance]
              note: "Attempt outcomes, strategy and replay excerpts supply durable avoidance lessons; the route also retains coach lessons under its admission conditions."
            - value: authored
              basis: wired
              records: [memory.md#mem-rte-lesson-maintenance]
              note: "Coach/curator models supply authored lesson text and replacement bullets."
          records: [memory.md#mem-rte-lesson-maintenance, memory.md#mem-obj-skill-lessons]
          note: "Model authorship and extraction from experience are distinct supported derivation paths, not an assertion that every bullet has both."
        - scope: "Portable playbook, hints, lessons, attributed history and harness payload admission"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-rte-package-import, epistemic.md#epi-obj-package-playbook, epistemic.md#epi-obj-package-hints, epistemic.md#epi-obj-package-lessons, epistemic.md#epi-obj-package-history, epistemic.md#epi-obj-package-harness]
              note: "External package parts are installed under conflict rules; imported scores are not fresh local measurements."
          records: [memory.md#mem-rte-package-import, epistemic.md#epi-obj-strategy-package]
          note: "Known acquisition lineage does not authenticate original producers or their warrants."
        - scope: "Initial legacy content, original package producers, training data and uninspected hint/notebook/report/host histories"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-bundle-advice, memory.md#mem-obj-harness-validator, epistemic.md#epi-obj-strategy-package, runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-ambient-promotion, runtime.md#rt-rte-runtime-dispatch]
          note: "Records explicitly leave initial authorship, dataset origin and opaque continuation ancestry unresolved; known later transforms cannot classify those origins."
      records: [memory.md#mem-obj-context-bundle, memory.md#mem-rte-lesson-maintenance, memory.md#mem-rte-package-import, memory.md#mem-rte-component-compaction, runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-runtime-dispatch]
      note: "Authored, imported, compiled and trace-extracted paths coexist with unresolved initialization and backend provenance."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Retained playbook, hints, lessons and mutation advice at later role-model prompts"
          assessment: known
          findings:
            - value: instruction
              basis: wired
              records: [runtime.md#rt-bap-context-delivery, memory.md#mem-obj-bundle-advice, memory.md#mem-obj-prompt-fragment, memory.md#mem-obj-context-policy, memory.md#mem-obj-completion-check, memory.md#mem-obj-tool-instruction, memory.md#mem-obj-skill-lessons]
              note: "Prescriptive guidance directs subsequent behavior through interpretation, not deterministic execution."
          records: [runtime.md#rt-bap-context-delivery, memory.md#mem-obj-skill-lessons, memory.md#mem-obj-context-policy, memory.md#mem-obj-completion-check]
          note: "Scope is standing directions actually selected into prompts; delivery is not proof of compliance."
        - scope: "Prior reports, analysis, trajectory and noncallable helper reference at role consumers; requested retained artifacts at host inspection consumers"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [memory.md#mem-obj-generation-artifacts, memory.md#mem-obj-tool-spec, memory.md#mem-rte-requested-readback, runtime.md#rt-rte-context-assembly]
              note: "Retained material supplies reference/evidence/context through prompt assembly or requested tool results, including ledger inspection."
          records: [memory.md#mem-obj-generation-artifacts, memory.md#mem-obj-tool-spec, memory.md#mem-rte-requested-readback]
          note: "Knowledge force does not authenticate source truth; installed imported validator source is not granted this route's authority."
        - scope: "Emitted skill/playbook files at the documented external file consumer"
          assessment: known
          findings:
            - value: instruction
              basis: afforded
              records: [memory.md#mem-clm-file-consumption, memory.md#mem-obj-skill-lessons]
              note: "The shipped consumer role can read retained operational directions; actual host discovery is not wired by the instruction alone."
            - value: knowledge
              basis: afforded
              records: [memory.md#mem-clm-file-consumption]
              note: "The same documented role can inspect retained run material as reference."
          records: [memory.md#mem-clm-file-consumption]
          note: "Keeps afforded external consumption distinct from wired generation and MCP/Pi paths."
        - scope: "Bundle routing configuration at orchestrator synchronization"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-routing-config]
              note: "Retained roles JSON selects effective model/settings/router state for later calls, subject to construction-time restrictions."
          records: [memory.md#mem-obj-routing-config]
          note: "This is fixed-rule configuration, unlike context-policy prose interpreted by models."
        - scope: "Bundle executable validator at enabled validity gate and retry consumer"
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [memory.md#mem-obj-harness-validator]
              note: "Retained validate_strategy source supplies admissibility criteria."
            - value: enforcement
              basis: wired
              records: [memory.md#mem-obj-harness-validator]
              note: "Failed checks can prevent tournament progress and trigger revision or rollback."
          records: [memory.md#mem-obj-harness-validator]
          note: "Conditional wiring is known; actual validator execution, correctness and security are unobserved. Prompt checklist strings are excluded from this unit."
        - scope: "Explicit stale markers at the SKILL lesson reader"
          assessment: known
          findings:
            - value: enforcement
              basis: wired
              records: [memory.md#mem-rte-lesson-lifecycle, memory.md#mem-obj-skill-lessons]
              note: "Retained stale markers exclude marked lines from later lesson delivery, without revoking raw playbook or prior prompt copies."
          records: [memory.md#mem-rte-lesson-lifecycle, memory.md#mem-obj-skill-lessons]
          note: "The force belongs to retained status at this particular reader, not to universal withdrawal."
        - scope: "Retained text at requested lexical search selector"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [memory.md#mem-rte-requested-readback]
              note: "Weighted token matches over retained scenario fields determine relative search results; a learned ranking policy is unnecessary."
          records: [memory.md#mem-rte-requested-readback]
          note: "Search returns metadata, not automatic injection of the highest-ranked playbook."
        - scope: "Retained experience/lessons at curator update and campaign history at training/kernel proposal consumers"
          assessment: known
          findings:
            - value: learning
              basis: wired
              records: [memory.md#mem-rte-lesson-maintenance, runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution]
              note: "Existing lessons/score trajectory feed durable guidance replacement; retained source/recent outcomes and champion history guide subsequent durable program proposals."
          records: [memory.md#mem-rte-lesson-maintenance, runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution]
          note: "Update-consumer force is separate from downstream instruction force and does not establish improved capacity."
        - scope: "Registry/probation/evaluation state at ambient candidate selection and serving binding"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [runtime.md#rt-rte-ambient-promotion]
              note: "Retained eligible evaluation scores select the highest-scoring candidate against incumbent conditions."
            - value: routing
              basis: wired
              records: [runtime.md#rt-rte-ambient-promotion, runtime.md#rt-cmp-training-checkpoints]
              note: "Active registry/serving metadata selects later model targets; actual serving is unobserved."
            - value: validation
              basis: wired
              records: [runtime.md#rt-rte-ambient-promotion]
              note: "Retained target, real-generation/drift and incumbent-anchor metadata determine promotion eligibility."
          records: [runtime.md#rt-rte-ambient-promotion, runtime.md#rt-cmp-training-checkpoints]
          note: "Scope is metadata consumers, not an assertion of reliable learned behavior in opaque weights."
        - scope: "Imported harness execution, checkpoint behavioral contents, notebook/evidence/npm memory packs and opaque host consumers"
          assessment: uninspected
          findings: []
          records: [epistemic.md#epi-obj-package-harness, runtime.md#rt-cmp-training-checkpoints, runtime.md#rt-rte-context-assembly, runtime.md#rt-rte-runtime-dispatch]
          note: "Installed source or a readable summary cannot establish force at untraced consumers; parameter-level knowledge and host retention remain unresolved."
      records: [runtime.md#rt-bap-context-delivery, memory.md#mem-obj-harness-validator, memory.md#mem-obj-routing-config, memory.md#mem-rte-lesson-maintenance, memory.md#mem-rte-requested-readback, runtime.md#rt-rte-ambient-promotion, runtime.md#rt-rte-runtime-dispatch]
      note: "All seven authority values have local supported consumers; this is not complete authority coverage or an observed-effect claim."
    write_agency:
      assessment: partial
      units:
        - scope: "Software bootstrap/overlay and matched bundle admission, lesson accumulation/curator replacement, artifact/ledger persistence and default npm publication"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-obj-context-bundle, runtime.md#rt-rte-context-promotion, memory.md#mem-rte-lesson-maintenance, memory.md#mem-obj-generation-artifacts, memory.md#mem-rte-component-compaction, runtime.md#rt-rte-npm-generation]
              note: "Code/model mechanisms admit retained content without a per-content human decision; starting the run does not make these writes manual."
          records: [memory.md#mem-obj-context-bundle, memory.md#mem-rte-lesson-maintenance, runtime.md#rt-rte-npm-generation, memory.md#mem-rte-component-compaction]
          note: "Known subsequent admission remains valid even when legacy authorship is unknown."
        - scope: "Explicit operator package selection through CLI"
          assessment: known
          findings:
            - value: manual
              basis: afforded
              records: [memory.md#mem-rte-package-import]
              note: "The described operator can explicitly select the package whose contents are installed; this does not classify all MCP/library import calls as human decisions."
          records: [memory.md#mem-rte-package-import]
          note: "This is the operator-controlled branch, not evidence of an actual import or of human control at every caller."
        - scope: "Training source/checkpoint keep-discard, automatic publication and eligible ambient activation; kernel champion admission"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-ambient-promotion, runtime.md#rt-rte-kernel-evolution]
              note: "Configured computational policies select and install updates without per-experiment human approval on these branches."
          records: [runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-ambient-promotion, runtime.md#rt-rte-kernel-evolution]
          note: "Ambient approval-required policy is a separate held branch, not an automatic-activation witness."
        - scope: "Lifecycle action callers, MCP/library import, optional npm approval, ambient required approval and direct/hook-modified writers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-lesson-lifecycle, memory.md#mem-rte-package-import, runtime.md#rt-rte-npm-generation, runtime.md#rt-rte-ambient-promotion, runtime.md#rt-rte-runtime-dispatch]
          note: "Generic caller identity, an approve method or a configuration flag does not establish an explicit human content decision; configured hook control is unresolved."
        - scope: "Initial legacy content and remaining notebook/hint/report/npm/session/mission admissions"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-obj-bundle-advice, runtime.md#rt-rte-context-assembly, runtime.md#rt-rte-runtime-dispatch]
          note: "Initial authorship/control and included untraced writer mechanisms prevent complete admission coverage."
      records: [memory.md#mem-obj-context-bundle, memory.md#mem-rte-lesson-maintenance, memory.md#mem-rte-package-import, memory.md#mem-rte-lesson-lifecycle, runtime.md#rt-rte-npm-generation, runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-runtime-dispatch]
      note: "Automatic implementation and afforded manual package admission coexist; approval labels do not resolve caller-dependent branches."
    curation_operations:
      assessment: partial
      units:
        - scope: "Implemented SKILL accumulation and curator replacement"
          assessment: partial
          findings:
            - value: dedup
              basis: wired
              records: [memory.md#mem-rte-lesson-maintenance, memory.md#mem-obj-skill-lessons]
              note: "Exact-bullet duplicate suppression is implemented."
            - value: evolve
              basis: wired
              records: [memory.md#mem-rte-lesson-maintenance]
              note: "Curator replacement rewrites the existing lesson section."
            - value: consolidate
              basis: afforded
              records: [memory.md#mem-rte-lesson-maintenance]
              note: "Curator receives existing lessons and a maximum and can return reduced replacement bullets; semantic faithfulness and actual compression are not observed."
          records: [memory.md#mem-rte-lesson-maintenance, memory.md#mem-obj-skill-lessons]
          note: "Implemented deduplication/replacement do not prove that every model rewrite preserves existing claims or creates new ones; synthesis remains unresolved."
        - scope: "Deterministic selection over accumulated component text"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [memory.md#mem-rte-component-compaction]
              note: "Existing sections, bullets and trajectory rows are reduced to selected/truncated representations while source files remain."
          records: [memory.md#mem-rte-component-compaction]
          note: "A lossy selection can drop qualifications without becoming a supported synthesis finding; ledger output is an audit summary, not proven canonical restored memory."
        - scope: "Lifecycle stale/deletion and dead-end reactivation"
          assessment: known
          findings:
            - value: invalidate
              basis: wired
              records: [memory.md#mem-rte-lesson-lifecycle]
              note: "Stale marking withdraws current SKILL reliance while retaining marked text."
            - value: decay
              basis: wired
              records: [memory.md#mem-rte-lesson-lifecycle]
              note: "Explicit rejection/deletion forgets a mutable lesson on subsequent file reads; this is not automatic age decay."
            - value: promote
              basis: wired
              records: [memory.md#mem-rte-lesson-lifecycle]
              note: "Reactivation can move retained dead-end material back into active playbook lessons."
          records: [memory.md#mem-rte-lesson-lifecycle]
          note: "These are local transformations, not all-store revocation; already active bundles and delivered copies may survive."
        - scope: "Existing bundle/playbook revision, package merge and retained checkpoint tier transitions"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [memory.md#mem-obj-context-bundle, runtime.md#rt-rte-npm-generation, memory.md#mem-rte-package-import]
              note: "Component-identity overlays and admitted replacements revise existing guidance; package overwrite is a separate replacement path."
            - value: dedup
              basis: wired
              records: [memory.md#mem-rte-package-import, epistemic.md#epi-obj-package-lessons]
              note: "Package merge appends only missing exact lesson bullets."
            - value: promote
              basis: wired
              records: [runtime.md#rt-rte-ambient-promotion, runtime.md#rt-rte-training-experiments]
              note: "Eligible retained checkpoints move to active/serving status; ambient demotes the incumbent to retained rollback state."
          records: [memory.md#mem-obj-context-bundle, memory.md#mem-rte-package-import, runtime.md#rt-rte-npm-generation, runtime.md#rt-rte-ambient-promotion]
          note: "The findings concern actual replacement, duplicate removal and tier change, not merely commands named promotion."
        - scope: "Extraction-only session consolidators and their untraced persistent callers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-consolidation-preview, epistemic.md#epi-rte-report-consolidation]
          note: "Candidate prefix/excerpt returns establish no durable curation; outside persistence remains uninspected, not absent."
        - scope: "Other hint/notebook/report maintenance, npm memory packs, trace/dataset curation and external hooks"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-context-assembly, runtime.md#rt-rte-ambient-promotion, runtime.md#rt-rte-runtime-dispatch]
          note: "Untraced transformations prevent a complete operation inventory, including a system-wide conclusion about synthesis or age decay."
      records: [memory.md#mem-rte-lesson-maintenance, memory.md#mem-rte-component-compaction, memory.md#mem-rte-lesson-lifecycle, memory.md#mem-rte-package-import, runtime.md#rt-rte-ambient-promotion, memory.md#mem-rte-consolidation-preview]
      note: "Retains supported reduction, deduplication, revision, withdrawal, forgetting and tier raising; unresolved semantics and maintenance branches remain explicit."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Generation setup selects retained advice/reports and active routing/validator parts before later role/evaluation invocations"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-context-assembly, memory.md#mem-obj-routing-config, memory.md#mem-obj-harness-validator]
              note: "Generation-triggered code supplies selected retained parts without a foreground consumer request for those artifacts."
          records: [runtime.md#rt-rte-context-assembly, memory.md#mem-rte-component-compaction, memory.md#mem-obj-routing-config, memory.md#mem-obj-harness-validator]
          note: "Internal storage reads are steps within automatic supply, not independently requested foreground retrieval."
        - scope: "Registered MCP knowledge/search and Pi runtime snapshot tools"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [memory.md#mem-rte-requested-readback]
              note: "A host/client requests selected retained artifacts or metadata and receives the result."
          records: [memory.md#mem-rte-requested-readback]
          note: "Handler delivery fulfills that request; it is not a second push merely because code returns data."
        - scope: "Documented external file-consumer role"
          assessment: known
          findings:
            - value: pull
              basis: afforded
              records: [memory.md#mem-clm-file-consumption]
              note: "An agent is instructed how to find and read wanted retained files; actual discovery/use is unobserved."
          records: [memory.md#mem-clm-file-consumption]
          note: "Symlinks and resource links do not establish automatic host injection."
        - scope: "Training/kernel campaign context and ambient registry/serving selection"
          assessment: partial
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution, runtime.md#rt-rte-ambient-promotion]
              note: "Campaign code supplies retained source/history/outcomes to subsequent proposals and registry state selects eligible active model targets."
          records: [runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution, runtime.md#rt-rte-ambient-promotion, runtime.md#rt-cmp-training-checkpoints]
          note: "Complete model-serving reload and downstream inference delivery are uninspected."
        - scope: "Session/mission reload, opaque provider/host continuation, npm memory packs and extraction-result callers"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-runtime-dispatch, memory.md#mem-rte-consolidation-preview, runtime.md#rt-rte-context-assembly]
          note: "Included alternatives lack complete retention-to-later-consumer routes; known tool retrieval cannot make them pull-only."
      records: [runtime.md#rt-rte-context-assembly, memory.md#mem-rte-requested-readback, memory.md#mem-clm-file-consumption, runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-runtime-dispatch]
      note: "Both wired push and pull exist, plus an afforded file pull; unresolved alternatives prevent a complete direction inventory."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Generation-triggered active-bundle and scenario/run/role-specific retained-part selection"
          assessment: known
          findings:
            - value: identifier
              basis: wired
              records: [runtime.md#rt-rte-context-assembly, memory.md#mem-obj-context-bundle, memory.md#mem-obj-routing-config, memory.md#mem-obj-harness-validator]
              note: "At generation setup, scenario/run/generation/role identities and active digest select corresponding bundle components, lessons/reports and digest-specific validators for delivery."
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-context-assembly, memory.md#mem-rte-component-compaction]
              note: "At the same trigger, enabled features, feedback ablation, stale filtering, availability and token/byte budgets gate whole parts or retained prefixes/rows."
          records: [runtime.md#rt-rte-context-assembly, memory.md#mem-rte-component-compaction, memory.md#mem-obj-harness-validator]
          note: "Identity matching selects actual delivered parts; budget/availability filters remain separate from targeting."
        - scope: "Component-compaction keyword/structure selector within automatic prompt delivery"
          assessment: known
          findings:
            - value: inferred-lexical
              basis: wired
              records: [memory.md#mem-rte-component-compaction]
              note: "During generation prompt preparation, keyword/structured-line preference selects retained Markdown content for the compacted copy."
            - value: coarse
              basis: wired
              records: [memory.md#mem-rte-component-compaction]
              note: "Component names, estimated length and recent section/row positions also select what survives."
          records: [memory.md#mem-rte-component-compaction]
          note: "Deterministic lexical selection is not embedding retrieval or model relevance judgment."
        - scope: "Campaign primary-feedback disclosure and ambient active-target choice"
          assessment: partial
          findings:
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-kernel-evolution, runtime.md#rt-rte-training-experiments]
              note: "At later proposal dispatch, campaign code supplies current source/recent outcomes and kernel primary feedback while withholding confirmation detail."
            - value: identifier
              basis: wired
              records: [runtime.md#rt-rte-ambient-promotion]
              note: "Ambient cycles match target/role and current anchor to eligible retained model metadata and serving bindings."
          records: [runtime.md#rt-rte-kernel-evolution, runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-ambient-promotion]
          note: "Complete training-data/serving reload selection and model-internal memory selection are unresolved."
        - scope: "MCP/Pi requested artifact/search return and documented requested file consumption"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-rte-requested-readback, memory.md#mem-clm-file-consumption]
          note: "These completely assessed direction units are pull. IDs and lexical top-k in a requested return do not establish push signals."
        - scope: "Opaque host continuation, remaining notebook/evidence/npm packs and session-result callers"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-runtime-dispatch, runtime.md#rt-rte-context-assembly, memory.md#mem-rte-consolidation-preview]
          note: "Untraced delivery leaves possible selectors unresolved; no inferred-embedding or inferred-judgment value is established for them."
      records: [runtime.md#rt-rte-context-assembly, memory.md#mem-rte-component-compaction, memory.md#mem-rte-requested-readback, runtime.md#rt-rte-ambient-promotion, runtime.md#rt-rte-runtime-dispatch]
      note: "Push has identifier, coarse and lexical selectors; pull units are locally inapplicable, not evidence that the whole axis is inapplicable."
    trace_learning:
      assessment: partial
      units:
        - scope: "Automatic attempt/replay-to-SKILL warning and lesson/curator update followed by later role prompts"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-rte-lesson-maintenance, memory.md#mem-obj-skill-lessons, runtime.md#rt-bap-context-delivery]
              note: "Recorded attempt experience feeds automatic durable avoidance/guidance writes, and later knowledge setup delivers selected lessons. Improvement or novelty is not required for this architectural finding."
          records: [memory.md#mem-rte-lesson-maintenance, memory.md#mem-obj-skill-lessons, runtime.md#rt-bap-context-delivery]
          note: "Support roles precede the current tournament; the deterministic nonadvance warning consumes current results at persistence. The positive does not require a coach to review an as-yet-unrun tournament."
        - scope: "Training/kernel iterative retained source and feedback-to-successor path"
          assessment: partial
          findings:
            - value: "yes"
              basis: wired
              records: [runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution]
              note: "Recent recorded experiment outcomes and champion/history feedback guide automatic retained program revisions used by later experiments/proposals."
          records: [runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution, runtime.md#rt-cmp-training-checkpoints]
          note: "The source-update chain qualifies; complete dataset-to-weight trace provenance and exercised serving are not established by checkpoint publication."
        - scope: "Component compaction and durable audit summary as a possible continuation artifact"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-component-compaction, memory.md#mem-obj-compaction-entry]
          note: "Trace-containing text is reduced and a summary retained, but later ordinary generation consumes source components, not demonstrably the retained ledger summary as behavior-shaping continuation. Requested inspection alone does not resolve that path."
        - scope: "Session extraction returns and possible durable callers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-consolidation-preview, epistemic.md#epi-rte-report-consolidation]
          note: "The inspected functions return candidates without durable promotion. Uninspected callers prevent a bounded negative for the complete route."
        - scope: "Remaining bundle/role-proposal trace provenance, ambient datasets, production traces, notebook/hint/report writers and opaque host continuation"
          assessment: uninspected
          findings: []
          records: [epistemic.md#epi-rte-role-proposals, runtime.md#rt-rte-ambient-promotion, runtime.md#rt-rte-context-assembly, runtime.md#rt-rte-runtime-dispatch]
          note: "Generation requests and static imports alone do not establish an original trace-to-durable-artifact-to-later-consumer chain for every included alternative."
      records: [memory.md#mem-rte-lesson-maintenance, runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution, memory.md#mem-rte-component-compaction, memory.md#mem-rte-consolidation-preview, runtime.md#rt-rte-runtime-dispatch]
      note: "Qualifying automatic trace-fed paths exist. Unresolved durable callers, trace provenance and opaque continuation remain included; no system-wide no or observed learning benefit is asserted."
    trace_source:
      assessment: partial
      units:
        - scope: "Original attempt inputs to the qualifying rollback-warning/SKILL route"
          assessment: known
          findings:
            - value: tool-traces
              basis: wired
              records: [memory.md#mem-rte-lesson-maintenance, memory.md#mem-obj-generation-artifacts]
              note: "Recorded strategy execution scores and failure feedback feed automatic retained warnings."
            - value: trajectories
              basis: wired
              records: [memory.md#mem-rte-lesson-maintenance, memory.md#mem-obj-generation-artifacts]
              note: "Strategy and replay narrative link actions and outcomes; selected excerpts enter the avoidance lesson."
          records: [memory.md#mem-rte-lesson-maintenance, memory.md#mem-obj-generation-artifacts]
          note: "Scope is the inspected warning chain, not every possible coach input. Ordinary model report text is not automatically a session log."
        - scope: "Original experience at curator/coach lesson updates"
          assessment: partial
          findings:
            - value: trajectories
              basis: wired
              records: [memory.md#mem-rte-lesson-maintenance]
              note: "Curator replacement consumes score trajectory alongside existing lessons."
          records: [memory.md#mem-rte-lesson-maintenance, epistemic.md#epi-rte-role-proposals]
          note: "The full origins of preexisting lessons and all model-proposal inputs are unresolved; this positive does not classify them as conversational session logs or runtime event streams."
        - scope: "Original experiment/benchmark feedback at qualifying retained training/kernel program revisions"
          assessment: partial
          findings:
            - value: tool-traces
              basis: wired
              records: [runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution]
              note: "Recorded backend evaluation outcomes and disclosed primary benchmark feedback feed later source proposals."
            - value: trajectories
              basis: wired
              records: [runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution]
              note: "Linked candidate/source and outcome histories supply multi-step experiment experience to later proposals."
          records: [runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution, runtime.md#rt-rte-ambient-promotion]
          note: "Training datasets, base-model ancestry and ambient native-run/agent-output/OTel curation are not traced sufficiently to classify all original inputs."
        - scope: "Unresolved qualifying alternatives: compaction continuation, session-extraction persistence, other writers and opaque host state"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-rte-component-compaction, memory.md#mem-rte-consolidation-preview, runtime.md#rt-rte-runtime-dispatch, runtime.md#rt-rte-context-assembly]
          note: "Without a complete qualifying write/consumer route and original input account, session-log and event-stream sources cannot be inferred from filenames, counters or adapter labels."
      records: [memory.md#mem-rte-lesson-maintenance, memory.md#mem-obj-generation-artifacts, runtime.md#rt-rte-training-experiments, runtime.md#rt-rte-kernel-evolution, memory.md#mem-rte-consolidation-preview, runtime.md#rt-rte-runtime-dispatch]
      note: "Execution feedback and linked experiment/replay experience support tool-traces and trajectories locally. Mixed and opaque origins prevent complete trace-source coverage."
---

# Autocontext memory profile

## Comparison rationale

This is a classification of accepted records, not a fresh source audit. All positive implementation findings are architectural wiring unless their local basis says afforded. No record supplies an observed run or causal experiment for these memory paths. The profile makes no claim of successful learning, reliable advice, safe generated validators or exercised self-improvement.

### Boundary and part distinctions

[MEM-OBJ-context-bundle](memory.md#mem-obj-context-bundle) is a valid mixed container. Its eight parts stay separate where their consumers differ. Advice and four mutation text bodies provide instructions through model interpretation. In particular, the context-policy renderer does not implement a programmatic context budget, and a completion-check string does not execute a veto. [MEM-OBJ-routing-config](memory.md#mem-obj-routing-config) selects actual runtime settings. [MEM-OBJ-harness-validator](memory.md#mem-obj-harness-validator) supplies conditional executable validity criteria and an enforced refusal path. [MEM-OBJ-tool-spec](memory.md#mem-obj-tool-spec) has symbolic source syntax but a noncallable, model-interpreted reference consumer. The JSON wrapper never gives all these parts the same force.

[MEM-OBJ-generation-artifacts](memory.md#mem-obj-generation-artifacts) distinguishes raw replay/metric records from derived lessons. [MEM-OBJ-compaction-entry](memory.md#mem-obj-compaction-entry) distinguishes a retained audit summary and lookup metadata from the compacted prompt body and from opaque host state. Its Pi inspection consumer supports requested reference delivery, not automatic continuation from a complete checkpoint. [RT-CMP-training-checkpoints](runtime.md#rt-cmp-training-checkpoints) supports parametric form and file-backed checkpoint storage; a numerical form does not require guessing a separately hosted storage service. The source pin does not pin exact runtime weights.

### Supersessions and admission

Reconciliation supersedes the epistemic lifecycle and import route declarations with [MEM-RTE-lesson-lifecycle](memory.md#mem-rte-lesson-lifecycle) and [MEM-RTE-package-import](memory.md#mem-rte-package-import). All profile route citations use those canonical records. The epistemic payload objects remain distinct and support imported lineage, form and attributed-history limits. Neither valid container is superseded by its parts. The TypeScript session extraction record overlaps the broader Python/TypeScript preview record without replacing it; neither establishes durable promotion.

Software/model admission is automatic even when a human starts a run. Optional approval methods in [RT-RTE-npm-generation](runtime.md#rt-rte-npm-generation), generic lifecycle callers and MCP/library package callers do not establish human agency. The separately described operator CLI package-selection branch affords manual admission. That weak, local warrant is not upgraded by the stronger automatic implementation witnesses. Unknown initial authorship does not erase known automatic bootstrap and subsequent candidate admission.

### Curation and read-back

[MEM-RTE-component-compaction](memory.md#mem-rte-component-compaction) implements reduction of existing material. Loss of a scope condition is a fidelity risk, not evidence that the operation creates a new claim. [MEM-RTE-lesson-maintenance](memory.md#mem-rte-lesson-maintenance) implements exact deduplication and replacement; curator-mediated semantic consolidation is afforded rather than asserted as an observed faithful transformation. The controlled synthesis value is not established merely by a request for rules or by failure to prove semantic preservation. [EPI-RTE-role-proposals](epistemic.md#epi-rte-role-proposals) keeps that relation unresolved.

Generation-triggered selection in [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly) is push relative to the role consumer. The actual scenario/run/digest identity selects delivered parts; coarse ablation, availability, freshness and budget filters also act. The compaction keyword preference adds lexical selection without embedding inference. In contrast, [MEM-RTE-requested-readback](memory.md#mem-rte-requested-readback) fulfills a consumer request. Its requested identifier and lexical search do not create extra push findings. [MEM-CLM-file-consumption](memory.md#mem-clm-file-consumption) affords a later file-reading role, not host injection merely because skill symlinks exist.

### Trace-fed updates and remaining coverage

The explicit durable witness is [MEM-RTE-lesson-maintenance](memory.md#mem-rte-lesson-maintenance): attempt experience becomes retained warning/lesson content and later role prompts receive it. Existing lessons and score trajectory also feed durable curator replacement, giving retained experience learning authority at the updater and instructions downstream. The workflow's annotation on [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation) places support roles before the current tournament. The warning produced at persistence still consumes current results; no claim that the coach saw that future tournament is necessary.

[RT-RTE-training-experiments](runtime.md#rt-rte-training-experiments) and [RT-RTE-kernel-evolution](runtime.md#rt-rte-kernel-evolution) also connect recorded experience, automatic retained source updates and later proposal/execution consumers. This supports local trace-learning findings without assuming all checkpoints are trained from session logs. Benchmark/backend execution feedback supplies tool traces, and linked candidate/action/outcome histories supply trajectories. No original event-stream or conversational-session source is inferred from an adapter name or from a report's existence.

Every axis remains partial because the accepted inventory includes unresolved alternatives. The records retain uninspected notebook/report writers, hint internals, evidence processing, npm maintenance/memory packs, production-trace/dataset curation, session/mission reload, configured hooks and opaque provider/host state. Some loaders and campaign consumers are known, but their complete origin, admission, storage or later-consumer chains are not. These gaps prevent complete-value statistics, system-wide negatives and a universal admission or revocation guarantee. They are inspection limits, not evidence of absent memory.

Source-read log: none. This job used only the supplied member/type/contract inputs and reconciliation; it added no source evidence or declarations.

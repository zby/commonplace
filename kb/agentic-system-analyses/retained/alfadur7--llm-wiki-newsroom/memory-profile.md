---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Memory profile of llm-wiki-newsroom: accumulated wiki content, derived access state and operator-mediated guidance revision with opaque host alternatives."
run-id: "AAS-2026-11-08-llm-wiki-newsroom-ea04687a5ff6-01"
source-identity: "https://github.com/alfadur7/llm-wiki-newsroom"
reviewed-boundary: "8e209cab483da544852d7213f0e25291d06d8a88"
memory-comparison:
  version: 2
  scope: "Accumulated raw/wiki content and revisions; derived graph, cluster, contradiction, access, dependency and body state; retained exports/briefings; defect/feedback histories, local decisions and revised guidance; their admission, maintenance and later-consumer routes. Includes unresolved QMD retained state, host transcript/context/auto-memory and hosted upload alternatives. Excludes unchanged shipped prompts, external model weights without a recorded operational update, and ordinary current-run diagnostics not shown to become retained memory."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Retained wiki pages, raw landed documents, graph/access/dependency/body/export files, defect ledger and local review checkpoints"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source"
                - "memory.md#mem-obj-hub"
                - "memory.md#mem-obj-narratives"
                - "memory.md#mem-obj-graph"
                - "memory.md#mem-obj-clusters"
                - "memory.md#mem-obj-access-indices"
                - "memory.md#mem-obj-conflict-data"
                - "memory.md#mem-obj-dependencies"
                - "memory.md#mem-obj-pages"
                - "memory.md#mem-obj-defect-log"
                - "memory.md#mem-obj-review-watermarks"
                - "runtime.md#rt-rte-wiki-export"
              note: "Inspected producers and consumers use filesystem artifacts. JSON is an encoding, and graph edges do not establish a graph database substrate."
          records:
            - "memory.md#mem-obj-source"
            - "memory.md#mem-obj-hub"
            - "memory.md#mem-obj-narratives"
            - "memory.md#mem-obj-graph"
            - "memory.md#mem-obj-clusters"
            - "memory.md#mem-obj-access-indices"
            - "memory.md#mem-obj-conflict-data"
            - "memory.md#mem-obj-dependencies"
            - "memory.md#mem-obj-pages"
            - "memory.md#mem-obj-defect-log"
            - "memory.md#mem-obj-review-watermarks"
            - "runtime.md#rt-rte-wiki-export"
          note: "Inspected producers and consumers use filesystem artifacts. JSON is an encoding, and graph edges do not establish a graph database substrate."
        -
          scope: "Repository-local decision notes under the documented lookup contract"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-local-memory"
              note: "Markdown note location is prescribed; only a placeholder is available."
          records:
            - "memory.md#mem-obj-local-memory"
          note: "Markdown note location is prescribed; only a placeholder is available."
        -
          scope: "QMD retained search state and embeddings; host transcripts, resumed/faction contexts and auto-memory; hosted uploaded context"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-qmd"
            - "runtime.md#rt-rte-role-delegation"
            - "runtime.md#rt-rte-faction-authoring"
            - "runtime.md#rt-rte-wiki-export"
            - "memory.md#mem-obj-local-memory"
          note: "Wrappers and protocols do not expose operative persistence internals. No vector, service-object or model-weights substrate is inferred for accumulated memory."
      records:
        - "memory.md#mem-obj-source"
        - "memory.md#mem-obj-hub"
        - "memory.md#mem-obj-narratives"
        - "memory.md#mem-obj-graph"
        - "memory.md#mem-obj-clusters"
        - "memory.md#mem-obj-access-indices"
        - "memory.md#mem-obj-conflict-data"
        - "memory.md#mem-obj-dependencies"
        - "memory.md#mem-obj-pages"
        - "memory.md#mem-obj-defect-log"
        - "memory.md#mem-obj-review-watermarks"
        - "runtime.md#rt-rte-wiki-export"
        - "memory.md#mem-obj-local-memory"
        - "runtime.md#rt-cmp-qmd"
        - "runtime.md#rt-rte-role-delegation"
        - "runtime.md#rt-rte-faction-authoring"
      note: "File witnesses do not enumerate opaque external retained parts. Shipped model weights and unchanged static role prompts are excluded from accumulated-memory storage."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Source/hub/narrative prose, copied browser/export/briefing bodies and retained defect rationales"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source"
                - "memory.md#mem-obj-hub"
                - "memory.md#mem-obj-narratives"
                - "memory.md#mem-obj-pages"
                - "memory.md#mem-obj-defect-log"
                - "runtime.md#rt-rte-wiki-export"
                - "memory.md#mem-rte-briefing-read"
              note: "Models and readers interpret localized text; copying text through JSON does not make its meaning symbolic."
          records:
            - "memory.md#mem-obj-source"
            - "memory.md#mem-obj-hub"
            - "memory.md#mem-obj-narratives"
            - "memory.md#mem-obj-pages"
            - "memory.md#mem-obj-defect-log"
            - "runtime.md#rt-rte-wiki-export"
            - "memory.md#mem-rte-briefing-read"
          note: "Models and readers interpret localized text; copying text through JSON does not make its meaning symbolic."
        -
          scope: "Graph IDs/typed edges, clusters/prior memberships, source-map/backlink indices, dependency dates, review windows and contradiction metadata"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph"
                - "memory.md#mem-obj-clusters"
                - "memory.md#mem-obj-access-indices"
                - "memory.md#mem-obj-dependencies"
                - "memory.md#mem-obj-review-watermarks"
                - "epistemic.md#epi-obj-contradiction-db"
              note: "Fixed consumers parse localized fields. Numerical scores and partition labels are not distributed parameters."
          records:
            - "memory.md#mem-obj-graph"
            - "memory.md#mem-obj-clusters"
            - "memory.md#mem-obj-access-indices"
            - "memory.md#mem-obj-dependencies"
            - "memory.md#mem-obj-review-watermarks"
            - "epistemic.md#epi-obj-contradiction-db"
          note: "Fixed consumers parse localized fields. Numerical scores and partition labels are not distributed parameters."
        -
          scope: "Experiment label arguments and score/manifest fields at later analysis consumer"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "observed"
              records:
                - "epistemic.md#epi-obj-experiment-ledger"
                - "epistemic.md#epi-rte-judge-measurement"
              note: "Supplied experiment artifacts contain prose judgments and program-defined fields; scorer implementation is not inspected."
            -
              value: "symbolic"
              basis: "observed"
              records:
                - "epistemic.md#epi-obj-experiment-ledger"
                - "epistemic.md#epi-rte-judge-measurement"
              note: "Supplied experiment artifacts contain prose judgments and program-defined fields; scorer implementation is not inspected."
          records:
            - "epistemic.md#epi-obj-experiment-ledger"
            - "epistemic.md#epi-rte-judge-measurement"
          note: "Supplied experiment artifacts contain prose judgments and program-defined fields; scorer implementation is not inspected."
        -
          scope: "Local decision notes and adopted role-guidance text at proposing/role models"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-local-memory"
                - "runtime.md#rt-rte-guideline-change"
                - "runtime.md#rt-bap-role-guidance"
              note: "The prescribed consumer interprets note/guidance meaning; actual private payloads and next-cycle reads are unavailable."
          records:
            - "memory.md#mem-obj-local-memory"
            - "runtime.md#rt-rte-guideline-change"
            - "runtime.md#rt-bap-role-guidance"
          note: "The prescribed consumer interprets note/guidance meaning; actual private payloads and next-cycle reads are unavailable."
        -
          scope: "QMD embeddings/payload and host auto-memory or retained conversation-window representations"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-qmd"
            - "runtime.md#rt-rte-role-delegation"
            - "memory.md#mem-obj-local-memory"
          note: "Search mode names and readable displays do not establish the form of opaque consumed state."
      records:
        - "memory.md#mem-obj-source"
        - "memory.md#mem-obj-hub"
        - "memory.md#mem-obj-narratives"
        - "memory.md#mem-obj-pages"
        - "memory.md#mem-obj-defect-log"
        - "runtime.md#rt-rte-wiki-export"
        - "memory.md#mem-rte-briefing-read"
        - "memory.md#mem-obj-graph"
        - "memory.md#mem-obj-clusters"
        - "memory.md#mem-obj-access-indices"
        - "memory.md#mem-obj-dependencies"
        - "memory.md#mem-obj-review-watermarks"
        - "epistemic.md#epi-obj-contradiction-db"
        - "epistemic.md#epi-obj-experiment-ledger"
        - "epistemic.md#epi-rte-judge-measurement"
        - "memory.md#mem-obj-local-memory"
        - "runtime.md#rt-rte-guideline-change"
        - "runtime.md#rt-bap-role-guidance"
        - "runtime.md#rt-cmp-qmd"
        - "runtime.md#rt-rte-role-delegation"
      note: "Separate prose and parser fields even where one file contains both. Opaque payload forms remain unresolved."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Externally acquired raw document content"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-source"
                - "runtime.md#rt-rte-source-ingest"
              note: "Acquisition imports external documents, not wiki operational experience; missing originals prevent complete provenance reconstruction."
          records:
            - "memory.md#mem-obj-source"
            - "runtime.md#rt-rte-source-ingest"
          note: "Acquisition imports external documents, not wiki operational experience; missing originals prevent complete provenance reconstruction."
        -
          scope: "Model-authored source reflections, hubs and narrative revisions"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-source"
                - "memory.md#mem-obj-hub"
                - "memory.md#mem-obj-narratives"
                - "runtime.md#rt-rte-source-ingest"
                - "epistemic.md#epi-rte-narrative-authoring"
              note: "Role instructions specify interpretations and cross-source writing, not a demonstrated execution history for each supplied page."
          records:
            - "memory.md#mem-obj-source"
            - "memory.md#mem-obj-hub"
            - "memory.md#mem-obj-narratives"
            - "runtime.md#rt-rte-source-ingest"
            - "epistemic.md#epi-rte-narrative-authoring"
          note: "Role instructions specify interpretations and cross-source writing, not a demonstrated execution history for each supplied page."
        -
          scope: "Graph/access/dependency/contradiction state, copied reading bundles, export bundles and rebuilt partitions"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph"
                - "memory.md#mem-obj-access-indices"
                - "memory.md#mem-obj-dependencies"
                - "memory.md#mem-obj-pages"
                - "memory.md#mem-rte-cluster-rebuild"
                - "epistemic.md#epi-rte-contradiction-derive"
                - "runtime.md#rt-rte-wiki-export"
              note: "Deterministic transforms compile wiki content and prior state; these are not trace extraction."
          records:
            - "memory.md#mem-obj-graph"
            - "memory.md#mem-obj-access-indices"
            - "memory.md#mem-obj-dependencies"
            - "memory.md#mem-obj-pages"
            - "memory.md#mem-rte-cluster-rebuild"
            - "epistemic.md#epi-rte-contradiction-derive"
            - "runtime.md#rt-rte-wiki-export"
          note: "Deterministic transforms compile wiki content and prior state; these are not trace extraction."
        -
          scope: "Feedback scan hits, counts, clipped samples and checkpoint history derived from conversational reactions"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-feedback-review"
                - "memory.md#mem-obj-review-watermarks"
              note: "Original inputs are user turns; extraction lineage alone does not establish a qualifying automatic learning output."
          records:
            - "memory.md#mem-rte-feedback-review"
            - "memory.md#mem-obj-review-watermarks"
          note: "Original inputs are user turns; extraction lineage alone does not establish a qualifying automatic learning output."
        -
          scope: "Encoded operational diagnoses and proposed guidance revisions"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-defect-log"
                - "memory.md#mem-rte-failure-review"
                - "runtime.md#rt-rte-guideline-change"
              note: "Model interpretation derives diagnoses from verifier outcomes; the final revised guidance remains operator-governed."
            -
              value: "trace-extracted"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-defect-log"
                - "memory.md#mem-rte-failure-review"
                - "runtime.md#rt-rte-guideline-change"
              note: "Model interpretation derives diagnoses from verifier outcomes; the final revised guidance remains operator-governed."
          records:
            - "memory.md#mem-obj-defect-log"
            - "memory.md#mem-rte-failure-review"
            - "runtime.md#rt-rte-guideline-change"
          note: "Model interpretation derives diagnoses from verifier outcomes; the final revised guidance remains operator-governed."
        -
          scope: "Initial cluster labels/local notes/checkpoints, actual raw-original history and QMD embedding provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-clusters"
            - "memory.md#mem-obj-local-memory"
            - "memory.md#mem-obj-review-watermarks"
            - "memory.md#mem-obj-source"
            - "runtime.md#rt-cmp-qmd"
          note: "Known subsequent transformations do not resolve initialization or hidden derivation."
      records:
        - "memory.md#mem-obj-source"
        - "runtime.md#rt-rte-source-ingest"
        - "memory.md#mem-obj-hub"
        - "memory.md#mem-obj-narratives"
        - "epistemic.md#epi-rte-narrative-authoring"
        - "memory.md#mem-obj-graph"
        - "memory.md#mem-obj-access-indices"
        - "memory.md#mem-obj-dependencies"
        - "memory.md#mem-obj-pages"
        - "memory.md#mem-rte-cluster-rebuild"
        - "epistemic.md#epi-rte-contradiction-derive"
        - "runtime.md#rt-rte-wiki-export"
        - "memory.md#mem-rte-feedback-review"
        - "memory.md#mem-obj-review-watermarks"
        - "memory.md#mem-obj-defect-log"
        - "memory.md#mem-rte-failure-review"
        - "runtime.md#rt-rte-guideline-change"
        - "memory.md#mem-obj-clusters"
        - "memory.md#mem-obj-local-memory"
        - "runtime.md#rt-cmp-qmd"
      note: "Known derivation paths coexist with unavailable initial and external provenance."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Wiki prose at later answering, authoring and browser/email readers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-browser-read"
                - "memory.md#mem-rte-briefing-read"
                - "memory.md#mem-obj-pages"
              note: "Reloaded text supplies reference/context to readers, not validated world truth."
          records:
            - "memory.md#mem-rte-browser-read"
            - "memory.md#mem-rte-briefing-read"
            - "memory.md#mem-obj-pages"
          note: "Reloaded text supplies reference/context to readers, not validated world truth."
        -
          scope: "Wiki bodies and rejected-direction notes at later author/proposer model"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-grounding-ladder"
                - "runtime.md#rt-rte-wiki-query"
                - "memory.md#mem-obj-local-memory"
              note: "Requested reads supply evidence or advice; actual reliance is unobserved."
          records:
            - "memory.md#mem-rte-grounding-ladder"
            - "runtime.md#rt-rte-wiki-query"
            - "memory.md#mem-obj-local-memory"
          note: "Requested reads supply evidence or advice; actual reliance is unobserved."
        -
          scope: "Adopted revised role guidance at subsequent role invocation"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-guideline-change"
                - "runtime.md#rt-bap-role-guidance"
              note: "Retained edits supply standing directions on next-cycle grounding; static unchanged prompts are not counted as use-accumulated memory."
          records:
            - "runtime.md#rt-rte-guideline-change"
            - "runtime.md#rt-bap-role-guidance"
          note: "Retained edits supply standing directions on next-cycle grounding; static unchanged prompts are not counted as use-accumulated memory."
        -
          scope: "Defect/transition fields and graph features at failure-mining/discovery consumers"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-rte-failure-review"
                - "memory.md#mem-obj-graph"
              note: "Historical verdict/treatment/support prioritize proposal targets; graph features prioritize bridge hubs without certifying claims."
          records:
            - "memory.md#mem-rte-failure-review"
            - "memory.md#mem-obj-graph"
          note: "Historical verdict/treatment/support prioritize proposal targets; graph features prioritize bridge hubs without certifying claims."
        -
          scope: "Source map, review watermark, dependency dates and partition state at ingest/miner/check/build consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-access-indices"
                - "memory.md#mem-obj-review-watermarks"
                - "memory.md#mem-obj-dependencies"
                - "memory.md#mem-rte-cluster-rebuild"
              note: "Retained fields choose update destinations, review windows, maintenance targets and next-build initialization/reuse."
          records:
            - "memory.md#mem-obj-access-indices"
            - "memory.md#mem-obj-review-watermarks"
            - "memory.md#mem-obj-dependencies"
            - "memory.md#mem-rte-cluster-rebuild"
          note: "Retained fields choose update destinations, review windows, maintenance targets and next-build initialization/reuse."
        -
          scope: "Operational experience at the interpreted guideline-update consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-failure-review"
                - "memory.md#mem-rte-feedback-review"
                - "runtime.md#rt-rte-guideline-change"
              note: "Retained feedback/defects inform durable behavior-shaping edits under operator adoption. This update-consumer authority does not imply automatic trace learning or improved capacity."
          records:
            - "memory.md#mem-rte-failure-review"
            - "memory.md#mem-rte-feedback-review"
            - "runtime.md#rt-rte-guideline-change"
          note: "Retained feedback/defects inform durable behavior-shaping edits under operator adoption. This update-consumer authority does not imply automatic trace learning or improved capacity."
        -
          scope: "Actual private local notes, QMD ranking internals, host retained context and adopted checker/hook content at deterministic consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-local-memory"
            - "runtime.md#rt-cmp-qmd"
            - "runtime.md#rt-rte-guideline-change"
            - "runtime.md#rt-rte-role-delegation"
          note: "Generic changed machinery may enforce or validate, but the records do not identify a retained changed criterion and its complete downstream consumer effects."
      records:
        - "memory.md#mem-rte-browser-read"
        - "memory.md#mem-rte-briefing-read"
        - "memory.md#mem-obj-pages"
        - "memory.md#mem-rte-grounding-ladder"
        - "runtime.md#rt-rte-wiki-query"
        - "memory.md#mem-obj-local-memory"
        - "runtime.md#rt-rte-guideline-change"
        - "runtime.md#rt-bap-role-guidance"
        - "memory.md#mem-rte-failure-review"
        - "memory.md#mem-obj-graph"
        - "memory.md#mem-obj-access-indices"
        - "memory.md#mem-obj-review-watermarks"
        - "memory.md#mem-obj-dependencies"
        - "memory.md#mem-rte-cluster-rebuild"
        - "memory.md#mem-rte-feedback-review"
        - "runtime.md#rt-cmp-qmd"
        - "runtime.md#rt-rte-role-delegation"
      note: "Authority belongs to each consumed part/effect. Raw logging, an accept string and delivery do not establish epistemic acceptance or universal enforcement."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Software rebuild, partition replacement, missing-URL enrichment, mechanical repairs and export copying"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-build-lint"
                - "memory.md#mem-rte-cluster-rebuild"
                - "memory.md#mem-obj-access-indices"
                - "runtime.md#rt-rte-wiki-export"
              note: "Invoking code is not per-content human approval; producer output is admitted algorithmically."
          records:
            - "runtime.md#rt-rte-build-lint"
            - "memory.md#mem-rte-cluster-rebuild"
            - "memory.md#mem-obj-access-indices"
            - "runtime.md#rt-rte-wiki-export"
          note: "Invoking code is not per-content human approval; producer output is admitted algorithmically."
        -
          scope: "Reporter/Columnist ordinary source and hub content admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-source"
                - "runtime.md#rt-rte-source-ingest"
              note: "Models select claim content under the protocol; starting ingest is not explicit approval of each claim."
          records:
            - "memory.md#mem-obj-source"
            - "runtime.md#rt-rte-source-ingest"
          note: "Models select claim content under the protocol; starting ingest is not explicit approval of each claim."
        -
          scope: "Optional saved synthesis and gated guideline adoption"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-wiki-query"
                - "runtime.md#rt-rte-guideline-change"
              note: "Explicit operator approval controls retained save/adoption; model authorship and physical writes are distinct."
          records:
            - "runtime.md#rt-rte-wiki-query"
            - "runtime.md#rt-rte-guideline-change"
          note: "Explicit operator approval controls retained save/adoption; model authorship and physical writes are distinct."
        -
          scope: "Explicit review checkpoint update after scan"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-review-watermarks"
                - "memory.md#mem-rte-feedback-review"
              note: "Checkpoint invocation admits derived dates/counts/history by code, without a separate human decision over each retained value."
          records:
            - "memory.md#mem-obj-review-watermarks"
            - "memory.md#mem-rte-feedback-review"
          note: "Checkpoint invocation admits derived dates/counts/history by code, without a separate human decision over each retained value."
        -
          scope: "Generic caller-supplied defect batches, initial labels/local notes/watermarks and host/provider retention"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-defect-log"
            - "memory.md#mem-obj-clusters"
            - "memory.md#mem-obj-local-memory"
            - "memory.md#mem-obj-review-watermarks"
            - "runtime.md#rt-rte-role-delegation"
            - "runtime.md#rt-cmp-qmd"
          note: "CLI append validation is not proof of who controlled content admission; private initialization and external write mechanisms remain unresolved."
      records:
        - "runtime.md#rt-rte-build-lint"
        - "memory.md#mem-rte-cluster-rebuild"
        - "memory.md#mem-obj-access-indices"
        - "runtime.md#rt-rte-wiki-export"
        - "memory.md#mem-obj-source"
        - "runtime.md#rt-rte-source-ingest"
        - "runtime.md#rt-rte-wiki-query"
        - "runtime.md#rt-rte-guideline-change"
        - "memory.md#mem-obj-review-watermarks"
        - "memory.md#mem-rte-feedback-review"
        - "memory.md#mem-obj-defect-log"
        - "memory.md#mem-obj-clusters"
        - "memory.md#mem-obj-local-memory"
        - "runtime.md#rt-rte-role-delegation"
        - "runtime.md#rt-cmp-qmd"
      note: "Different admission mechanisms remain separate. Human supervision is not a universal manual-write classification."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Source reflection selection/compression from retained originals"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-source"
                - "runtime.md#rt-rte-source-ingest"
              note: "Source guide requests selection of existing claims/quotations; no reliable preservation or new claim follows from the request."
          records:
            - "memory.md#mem-obj-source"
            - "runtime.md#rt-rte-source-ingest"
          note: "Source guide requests selection of existing claims/quotations; no reliable preservation or new claim follows from the request."
        -
          scope: "Existing source/hub/narrative revision and regrounding"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-source-ingest"
                - "memory.md#mem-obj-narratives"
                - "runtime.md#rt-rte-build-lint"
              note: "Role/runbook routes revise existing text; rebuild alone does not revise narrative meaning."
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "memory.md#mem-obj-narratives"
            - "runtime.md#rt-rte-build-lint"
          note: "Role/runbook routes revise existing text; rebuild alone does not revise narrative meaning."
        -
          scope: "Repeated per-file target links reduced to one graph edge"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph"
              note: "Inspected graph producer collapses repeated target links, with separate relation/grade promotion rules."
          records:
            - "memory.md#mem-obj-graph"
          note: "Inspected graph producer collapses repeated target links, with separate relation/grade promotion rules."
        -
          scope: "Retained prior partition replaced or reused during rebuild"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-cluster-rebuild"
              note: "Code updates a retained partition using prior structural state; this does not establish improved communities."
          records:
            - "memory.md#mem-rte-cluster-rebuild"
          note: "Code updates a retained partition using prior structural state; this does not establish improved communities."
        -
          scope: "Semantic joins in synthesis/trail/timeline, withdrawal outcomes, contradiction themes and opaque provider maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-narrative-authoring"
            - "memory.md#mem-obj-narratives"
            - "memory.md#mem-rte-hub-withdrawal"
            - "memory.md#mem-obj-conflict-data"
            - "runtime.md#rt-cmp-qmd"
          note: "Narrative generation is not evidence of a claim absent from inputs. Demotion triage is not completed decay/invalidation, and full maintenance coverage is unavailable."
      records:
        - "memory.md#mem-obj-source"
        - "runtime.md#rt-rte-source-ingest"
        - "memory.md#mem-obj-narratives"
        - "runtime.md#rt-rte-build-lint"
        - "memory.md#mem-obj-graph"
        - "memory.md#mem-rte-cluster-rebuild"
        - "epistemic.md#epi-rte-narrative-authoring"
        - "memory.md#mem-rte-hub-withdrawal"
        - "memory.md#mem-obj-conflict-data"
        - "runtime.md#rt-cmp-qmd"
      note: "No synthesize finding is inferred from command names. Rebuild/copy/acquisition and duplicate lookup alone add no curation value; unresolved alternatives remain included."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested authoring/query body retrieval, browser selection and requested miner reports"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-browser-read"
                - "memory.md#mem-rte-failure-review"
                - "memory.md#mem-rte-feedback-review"
                - "runtime.md#rt-rte-wiki-query"
              note: "Code fulfills later requests for retained bodies or reports; the model answer and body-get protocol remain separately claimed."
          records:
            - "memory.md#mem-rte-browser-read"
            - "memory.md#mem-rte-failure-review"
            - "memory.md#mem-rte-feedback-review"
            - "runtime.md#rt-rte-wiki-query"
          note: "Code fulfills later requests for retained bodies or reports; the model answer and body-get protocol remain separately claimed."
        -
          scope: "Author GROUND expansion, related-work decision-note lookup and transcript handoff recovery"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-grounding-ladder"
                - "memory.md#mem-obj-local-memory"
                - "runtime.md#rt-rte-faction-authoring"
              note: "Later consumers explicitly request retained evidence; recovery is raw trace read-back, not a derived summary."
          records:
            - "memory.md#mem-rte-grounding-ladder"
            - "memory.md#mem-obj-local-memory"
            - "runtime.md#rt-rte-faction-authoring"
          note: "Later consumers explicitly request retained evidence; recovery is raw trace read-back, not a derived summary."
        -
          scope: "Prior partition supplied automatically to subsequent clustering"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-cluster-rebuild"
              note: "Build request triggers automatic historical-membership selection for the computation, rather than an explicit request for that retained partition."
          records:
            - "memory.md#mem-rte-cluster-rebuild"
          note: "Build request triggers automatic historical-membership selection for the computation, rather than an explicit request for that retained partition."
        -
          scope: "Selected persisted briefing delivered to external recipient"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-briefing-read"
              note: "Caller initiates sending; recipient receives selected retained prose without its own retrieval request. Receipt is unobserved."
          records:
            - "memory.md#mem-rte-briefing-read"
          note: "Caller initiates sending; recipient receives selected retained prose without its own retrieval request. Receipt is unobserved."
        -
          scope: "Revised role instructions loaded as role system guidance"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-guideline-change"
                - "runtime.md#rt-bap-role-guidance"
              note: "Role selection supplies the changed standing text by host protocol; explicit touched-file/next-cycle grounding is a separate pull operation."
          records:
            - "runtime.md#rt-rte-guideline-change"
            - "runtime.md#rt-bap-role-guidance"
          note: "Role selection supplies the changed standing text by host protocol; explicit touched-file/next-cycle grounding is a separate pull operation."
        -
          scope: "QMD internal retained-state supply, host auto-memory/resumed windows and hosted export context loading"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-qmd"
            - "runtime.md#rt-rte-role-delegation"
            - "memory.md#mem-obj-local-memory"
            - "runtime.md#rt-rte-wiki-export"
          note: "Requested local retrieval and uploaded files do not resolve opaque internal loading or selection operations."
      records:
        - "memory.md#mem-rte-browser-read"
        - "memory.md#mem-rte-failure-review"
        - "memory.md#mem-rte-feedback-review"
        - "runtime.md#rt-rte-wiki-query"
        - "memory.md#mem-rte-grounding-ladder"
        - "memory.md#mem-obj-local-memory"
        - "runtime.md#rt-rte-faction-authoring"
        - "memory.md#mem-rte-cluster-rebuild"
        - "memory.md#mem-rte-briefing-read"
        - "runtime.md#rt-rte-guideline-change"
        - "runtime.md#rt-bap-role-guidance"
        - "runtime.md#rt-cmp-qmd"
        - "runtime.md#rt-rte-role-delegation"
        - "runtime.md#rt-rte-wiki-export"
      note: "Both request-driven reads and automatic supplies are supported locally. Current hook diagnostics/static reminders are excluded unless accumulated content is established; no global direction closure is possible."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Cluster rebuild's automatic prior-partition selection"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-cluster-rebuild"
              note: "Trigger: cluster build. Selector: graph fingerprint and exact hub-set coverage for reuse; existing-node identity for warm initialization. Selected retained part: prior memberships/assignments. Availability/backend/cold checks are separate coarse gating."
          records:
            - "memory.md#mem-rte-cluster-rebuild"
          note: "Trigger: cluster build. Selector: graph fingerprint and exact hub-set coverage for reuse; existing-node identity for warm initialization. Selected retained part: prior memberships/assignments. Availability/backend/cold checks are separate coarse gating."
        -
          scope: "Cluster prior-state availability and backend/cold branch gating"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-cluster-rebuild"
              note: "Trigger: cluster build. Selector: retained state validity/availability, backend and cold flag. Selected material: prior partition allowed into reuse/warm path; not semantic similarity."
          records:
            - "memory.md#mem-rte-cluster-rebuild"
          note: "Trigger: cluster build. Selector: retained state validity/availability, backend and cold flag. Selected material: prior partition allowed into reuse/warm path; not semantic similarity."
        -
          scope: "Briefing send using numerically latest week"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-briefing-read"
              note: "Trigger: send invocation without explicit file. Selector: maximum integer year/week. Selected part: one whole retained weekly briefing. It is recency selection, not a content match."
          records:
            - "memory.md#mem-rte-briefing-read"
          note: "Trigger: send invocation without explicit file. Selector: maximum integer year/week. Selected part: one whole retained weekly briefing. It is recency selection, not a content match."
        -
          scope: "Briefing send with explicit file choice"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-briefing-read"
              note: "Trigger: caller sending to recipient. Selector: explicit file identity determines the retained body delivered unsolicited to that recipient, not an identifier on a catalog entry."
          records:
            - "memory.md#mem-rte-briefing-read"
          note: "Trigger: caller sending to recipient. Selector: explicit file identity determines the retained body delivered unsolicited to that recipient, not an identifier on a catalog entry."
        -
          scope: "Revised role-guidance supply at named role invocation"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "claimed"
              records:
                - "runtime.md#rt-bap-role-guidance"
                - "runtime.md#rt-rte-guideline-change"
              note: "Trigger: role invocation. Selector: named role definition. Selected part: that role's revised instruction text loaded as system guidance under the host contract."
          records:
            - "runtime.md#rt-bap-role-guidance"
            - "runtime.md#rt-rte-guideline-change"
          note: "Trigger: role invocation. Selector: named role definition. Selected part: that role's revised instruction text loaded as system guidance under the host contract."
        -
          scope: "Automatic hosted export loading, QMD and host auto-memory/context selection"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-wiki-export"
            - "runtime.md#rt-cmp-qmd"
            - "memory.md#mem-obj-local-memory"
            - "runtime.md#rt-rte-role-delegation"
          note: "Export budget recommendations do not establish installed push membership. Retrieval query lex/vec modes alone do not establish embedding/lexical push of retained memory."
      records:
        - "memory.md#mem-rte-cluster-rebuild"
        - "memory.md#mem-rte-briefing-read"
        - "runtime.md#rt-bap-role-guidance"
        - "runtime.md#rt-rte-guideline-change"
        - "runtime.md#rt-rte-wiki-export"
        - "runtime.md#rt-cmp-qmd"
        - "memory.md#mem-obj-local-memory"
        - "runtime.md#rt-rte-role-delegation"
      note: "Signal classification applies only to named push operations. Requested wiki searches are not reclassified as unsolicited injection; no inapplicability is inferred from known pull witnesses."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Defect/feedback-to-guidance and optional decision-note encoding"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-failure-review"
            - "memory.md#mem-rte-feedback-review"
            - "runtime.md#rt-rte-guideline-change"
            - "memory.md#mem-obj-local-memory"
          note: "Automatic selectors are wired, but final durable guidance adoption is explicitly operator-mediated. Optional note encoding and caller-authored defect admission do not establish a complete automatic trace-fed behavior-shaping write. No bounded absence record licenses a local no."
        -
          scope: "Conversational-feedback checkpoint dates, counts and recurrence history consumed by later feedback mining"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-review-watermarks"
                - "memory.md#mem-rte-feedback-review"
              note: "Checkpoint invocation automatically retains reaction-derived counts/history and the review window; subsequent mining consumes that durable state to select later review context. This behavior-shaping routing artifact qualifies without a final guidance edit or demonstrated improvement."
          records:
            - "memory.md#mem-obj-review-watermarks"
            - "memory.md#mem-rte-feedback-review"
          note: "The inspected extraction, checkpoint persistence and later window/history consumer establish this local automatic trace-fed write. Invoking checkpoint is not per-content human approval."
        -
          scope: "Failure-review checkpoint and diagnostic recurrence histories"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-review-watermarks"
            - "memory.md#mem-rte-failure-review"
          note: "Later review-window selection is supported, but caller-authored defects and decision histories have unresolved admission control and mixed origins. This alternative is not resolved by the known conversational-feedback checkpoint route."
        -
          scope: "Host auto-memory, compaction, resumed/faction contexts and opaque provider state"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-local-memory"
            - "runtime.md#rt-rte-role-delegation"
            - "runtime.md#rt-rte-faction-authoring"
            - "runtime.md#rt-cmp-qmd"
          note: "Host internals and actual retained summaries are unavailable. Neither summary learning nor its absence is established."
        -
          scope: "Experiment-output to production update"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-judge-measurement"
            - "epistemic.md#epi-obj-experiment-ledger"
            - "runtime.md#rt-rte-guideline-change"
          note: "Retained labels/scores and later experimental analysis are supported, but automatic durable production-policy update is not traced."
      records:
        - "memory.md#mem-rte-failure-review"
        - "memory.md#mem-rte-feedback-review"
        - "runtime.md#rt-rte-guideline-change"
        - "memory.md#mem-obj-local-memory"
        - "memory.md#mem-obj-review-watermarks"
        - "runtime.md#rt-rte-role-delegation"
        - "runtime.md#rt-rte-faction-authoring"
        - "runtime.md#rt-cmp-qmd"
        - "epistemic.md#epi-rte-judge-measurement"
        - "epistemic.md#epi-obj-experiment-ledger"
      note: "The feedback checkpoint supplies a wired qualifying automatic trace-fed write and a supported system yes. Other admission and host alternatives remain unresolved, so coverage is partial, not complete; no local or system no is asserted. Operator-mediated guidance adoption is a separate mechanism."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Original conversational reactions feeding the qualifying feedback checkpoint write"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-feedback-review"
                - "memory.md#mem-obj-review-watermarks"
              note: "The miner extracts human reaction turns from host transcript JSONL; filtered counts/history persist at checkpoint and shape later mining. Serialization and checkpoint dates do not add event-streams."
          records:
            - "memory.md#mem-rte-feedback-review"
            - "memory.md#mem-obj-review-watermarks"
          note: "Original source content is recorded conversational turns; the actual private transcript contents remain unavailable without obscuring this inspected source route."
        -
          scope: "Original inputs to proposed guidance/local-note writes and unresolved failure-review checkpoint writes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-feedback-review"
            - "memory.md#mem-rte-failure-review"
            - "runtime.md#rt-rte-guideline-change"
          note: "Human reaction turns are recorded conversational material; verifier/deterministic/model defects have mixed operational origins. These facts describe proposal inputs, but admission of the proposed guidance/local-note writes and the mixed failure-review checkpoint origins remain unresolved. The separately classified feedback checkpoint does not resolve these alternatives."
        -
          scope: "Original inputs to host memory/compaction or experiment-fed production learning"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-local-memory"
            - "runtime.md#rt-rte-role-delegation"
            - "runtime.md#rt-rte-faction-authoring"
            - "runtime.md#rt-cmp-qmd"
            - "epistemic.md#epi-rte-judge-measurement"
          note: "Opaque host inputs and missing experiment-to-policy integration prevent classification. Neither source is inapplicable on the strength of a different route's missing learning witness."
      records:
        - "memory.md#mem-obj-review-watermarks"
        - "memory.md#mem-rte-feedback-review"
        - "memory.md#mem-rte-failure-review"
        - "runtime.md#rt-rte-guideline-change"
        - "memory.md#mem-obj-local-memory"
        - "runtime.md#rt-rte-role-delegation"
        - "runtime.md#rt-rte-faction-authoring"
        - "runtime.md#rt-cmp-qmd"
        - "epistemic.md#epi-rte-judge-measurement"
      note: "Conversational-feedback checkpoint input supports session-logs; other qualifying-write candidates remain unresolved, so coverage is partial rather than inapplicable. External static source documents and prior partitions are not relabeled as activity traces."
---

# llm-wiki-newsroom memory profile

## Comparison rationale

### Boundary and evidence strength

The inventory follows the accepted memory objects and routes, not the enclosing host's whole storage. A JSON graph is a symbolic file artifact, not evidence of a graph database. Numeric partition IDs and contradiction scores are localized fields, not distributed parameters. The opaque QMD mode labels cannot classify a retained embedding payload. See [MEM-OBJ-graph](memory.md#mem-obj-graph), [MEM-RTE-cluster-rebuild](memory.md#mem-rte-cluster-rebuild), [EPI-OBJ-contradiction-db](epistemic.md#epi-obj-contradiction-db) and [RT-CMP-qmd](runtime.md#rt-cmp-qmd).

The accepted reconciliation establishes no supersessions. Broader memory containers and narrower epistemic objects retain different extents; classifications do not treat their overlap as independent corroboration. Each axis retains unresolved local initialization, host/provider or semantic-maintenance alternatives. Consequently no axis claims complete boundary coverage. A wired copy/selector is not evidence that the model followed its authoring/review instructions. Experiment artifacts support only their sampled retained fields and judgments, not observed production updates. See [EPI-RTE-judge-measurement](epistemic.md#epi-rte-judge-measurement).

### Admission and curation

Software rebuilds automatically admit generated values once invoked. Model-generated ordinary page content is likewise not individually approved merely because a human initiated ingest. Optional synthesis save and guideline adoption have explicit human decisions, and therefore separate manual mechanisms. Generic ledger callers and unavailable initial notes/labels do not resolve human control. See [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change) and [MEM-OBJ-defect-log](memory.md#mem-obj-defect-log).

A source reflection requests consolidation of imported claims. Regrounding requests evolution. Graph repeated-target collapse implements local deduplication; URL-first duplicate detection alone does not. Cross-source narrative names do not establish synthesis in the controlled sense of a new claim absent from inputs: semantic relation remains indeterminate. Withdrawal triage is not observed deletion or global forgetting. See [MEM-OBJ-source](memory.md#mem-obj-source), [MEM-OBJ-graph](memory.md#mem-obj-graph), [EPI-RTE-narrative-authoring](epistemic.md#epi-rte-narrative-authoring) and [MEM-RTE-hub-withdrawal](memory.md#mem-rte-hub-withdrawal).

### Consumers and selection

Requested wiki reads and miner reports are pull. Automatic injection of prior partition into clustering is a separate push operation, with identity matching distinct from coarse branch gating. Briefing distribution is push relative to its recipient even though the sender initiates the workflow; explicit file identity and latest-week selection remain separate mechanisms. Role guidance supplied by role identity is only a claimed host route. Uploaded export context has no inspected hosted selection mechanism. Current broken-link feedback is not counted as accumulated memory solely because it enters context. See [MEM-RTE-cluster-rebuild](memory.md#mem-rte-cluster-rebuild), [MEM-RTE-briefing-read](memory.md#mem-rte-briefing-read), [RT-BAP-role-guidance](runtime.md#rt-bap-role-guidance), [RT-RTE-wiki-export](runtime.md#rt-rte-wiki-export) and [RT-BAP-hook-feedback](runtime.md#rt-bap-hook-feedback).

### Trace-fed revision limits

Experience has learning authority at a consumer proposing durable rule edits; adopted text has downstream instruction authority. Separately, the feedback checkpoint automatically retains reaction-derived counts/history and review windows for later mining selection. That durable routing artifact is behavior-shaping memory, even though it is not final guidance. It supports wired trace-learning yes and session-logs for its original conversational input. Explicit checkpoint invocation does not make content admission manual. Operator-mediated guidance adoption, mixed failure-review admission and opaque host alternatives remain separate unresolved units. Thus both trace axes have partial coverage with supported positives; no analyst declares an evidenced-absence record, so neither local nor system-wide trace-learning no is asserted. See [MEM-RTE-feedback-review](memory.md#mem-rte-feedback-review), [MEM-RTE-failure-review](memory.md#mem-rte-failure-review), [MEM-OBJ-review-watermarks](memory.md#mem-obj-review-watermarks), [MEM-OBJ-local-memory](memory.md#mem-obj-local-memory) and [RT-RTE-guideline-change](runtime.md#rt-rte-guideline-change).

### Source-read log

No frozen source files were read for this profile. The supplied accepted records carry its warrants; no new records, quotations, execution evidence or verification findings were added.


---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "cass_memory_system memory profile: retained diaries, playbooks, feedback, retrieval metadata and safety patterns, including unresolved external history and caller admissions"
run-id: AAS-2026-10-13-cass-memory-system-30c18219cf68-01
source-identity: "https://github.com/Dicklesworthstone/cass_memory_system"
reviewed-boundary: "8aca3bbb6732321dca041b32c155617784687897"
memory-comparison:
  version: 2
  scope: "CM's accumulated diaries, playbook content/reasons/standing, feedback and outcome/delivery logs, processed/onboarding checkpoints, embedding cache, withdrawal logs, trauma patterns/explanations and exported instruction snapshots; their admitted writes, maintenance and later CLI, HTTP, reflector, scorer and guard consumers. External cass history is included as an opaque retained input/read surface, not as CM-owned indexing. Imported/custom origin and generic caller control remain unresolved. Excludes static shipped method text, ordinary transient validator results, provider/model weights and hidden host/provider state whose retention is outside the supplied boundary; no deployed corpus, activation or benefit is established."
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "CM playbooks, diary JSON, feedback/reasons, delivery/outcome logs, processed/onboarding state, cache, blocked logs, trauma JSONL and project snapshots"
          assessment: known
          findings:
            - {value: files, basis: wired, records: [runtime.md#rt-obj-playbook-bullet, memory.md#mem-obj-diary-entry, memory.md#mem-obj-context-log, memory.md#mem-obj-processed-log, memory.md#mem-obj-embedding-cache, memory.md#mem-obj-blocked-entry, memory.md#mem-obj-trauma-entry, memory.md#mem-rte-provenance-read], note: "Retained state is reloaded from YAML, JSON, JSONL or exported text files. Repository-local placement is not a separate Git-backed memory substrate."}
          records: [runtime.md#rt-obj-playbook-bullet, memory.md#mem-obj-diary-entry, memory.md#mem-obj-context-log, memory.md#mem-obj-processed-log, memory.md#mem-obj-embedding-cache, memory.md#mem-obj-blocked-entry, memory.md#mem-obj-trauma-entry, memory.md#mem-rte-provenance-read]
          note: "These records cover the named local containers; numerical vectors are encoded in a file, not an established vector database."
        - scope: "External cass historical corpus/index used by context and reflection"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-context-read, runtime.md#rt-rte-reflection-update]
          note: "The adapter supplies retained history, but the external index implementation and operative substrate are outside inspection; snippets do not establish that substrate."
      records: [runtime.md#rt-rte-context-read, runtime.md#rt-rte-reflection-update, memory.md#mem-rte-provenance-read, memory.md#mem-obj-embedding-cache]
      note: "Files are established for CM-owned state; the included external historical input prevents complete substrate coverage."
    representational_form:
      assessment: partial
      units:
        - scope: "Rule instruction text, diary descriptions, reasoning/deprecation explanations, feedback context, descriptive task/notes and trauma human_message; linguistic projections and instruction exports"
          assessment: known
          findings:
            - {value: natural-language, basis: wired, records: [runtime.md#rt-obj-playbook-bullet, memory.md#mem-obj-diary-entry, memory.md#mem-obj-reasoning, memory.md#mem-obj-feedback-context, memory.md#mem-obj-context-log, memory.md#mem-obj-human-message, memory.md#mem-rte-provenance-read], note: "Models or recipients interpret these words; file serialization and symbolic references do not change the text's consumption form."}
          records: [runtime.md#rt-obj-playbook-bullet, memory.md#mem-obj-diary-entry, memory.md#mem-obj-reasoning, memory.md#mem-obj-feedback-context, memory.md#mem-obj-context-log, memory.md#mem-obj-human-message, memory.md#mem-rte-provenance-read]
          note: "Known for the named linguistic fields, not for all material in their mixed containers."
        - scope: "Rule IDs/events/counts/state, checkpoint/watermark and delivery/outcome identities, cache access metadata, blocked matching fields and trauma regex/scope/status"
          assessment: known
          findings:
            - {value: symbolic, basis: wired, records: [memory.md#mem-obj-feedback-events, memory.md#mem-obj-processed-log, memory.md#mem-obj-context-log, memory.md#mem-obj-embedding-cache, memory.md#mem-obj-blocked-entry, memory.md#mem-obj-trauma-entry], note: "Localized fields have fixed software consumers for scoring, routing, reuse, withdrawal and matching. Blocked text is consumed by hash/token predicates rather than interpreted as standing advice."}
          records: [memory.md#mem-obj-feedback-events, memory.md#mem-obj-processed-log, memory.md#mem-obj-context-log, memory.md#mem-obj-embedding-cache, memory.md#mem-obj-blocked-entry, memory.md#mem-obj-trauma-entry]
          note: "Splits metadata from linguistic content and dense vectors in the same files."
        - scope: "Retained dense bullet vectors at similarity and semantic duplicate consumers"
          assessment: known
          findings:
            - {value: parametric, basis: wired, records: [memory.md#mem-obj-embedding-cache], note: "Dense numerical representations supply similarity; these cached outputs are not updated model weights."}
          records: [memory.md#mem-obj-embedding-cache]
          note: "Numerical form is established independently of encoder-version uncertainty."
        - scope: "Fast diary outcome status and transient validation-result mixed parts"
          assessment: partial
          findings:
            - {value: symbolic, basis: wired, records: [epistemic.md#epi-obj-session-diary, epistemic.md#epi-rte-diary-inference], note: "The combined diary record and classifier route establish a fixed status label persisted with the summary."}
          records: [epistemic.md#epi-obj-session-diary, epistemic.md#epi-rte-diary-inference, epistemic.md#epi-obj-validation-result]
          note: "Reconciliation retains missing separate status and validator linguistic-part declarations. The diary status is classifiable from the combined record, but independently inventoried parts and durable validator-dossier coverage are unresolved; transient verdict/refinement alone is excluded from accumulated memory."
        - scope: "External historical payloads beyond inspected returned session/snippet text"
          assessment: partial
          findings:
            - {value: natural-language, basis: wired, records: [runtime.md#rt-rte-reflection-update, runtime.md#rt-rte-context-read], note: "Exported session text and returned history snippets enter the inspected linguistic paths."}
          records: [runtime.md#rt-rte-reflection-update, runtime.md#rt-rte-context-read]
          note: "Neither display snippets nor exports classify every opaque index/payload part."
      records: [runtime.md#rt-obj-playbook-bullet, memory.md#mem-obj-embedding-cache, epistemic.md#epi-obj-session-diary, epistemic.md#epi-obj-validation-result, runtime.md#rt-rte-context-read]
      note: "All three forms have local witnesses; mixed-record granularity and opaque history prevent complete inventory coverage."
    lineage:
      assessment: partial
      units:
        - scope: "Diaries, reflected rule words/reasons and transcript-derived feedback/standing"
          assessment: known
          findings:
            - {value: trace-extracted, basis: wired, records: [memory.md#mem-obj-diary-entry, runtime.md#rt-rte-reflection-update, memory.md#mem-obj-reasoning, memory.md#mem-rte-outcome-feedback], note: "Session exports feed durable summaries, proposals and judgments. This derivation does not certify faithful extraction or authenticated originating agents."}
          records: [memory.md#mem-obj-diary-entry, runtime.md#rt-rte-reflection-update, memory.md#mem-obj-reasoning, memory.md#mem-rte-outcome-feedback]
          note: "The derivation route is known even though generated semantic instances and source truth are not supplied."
        - scope: "Caller-formulated onboarding rules"
          assessment: partial
          findings:
            - {value: authored, basis: afforded, records: [runtime.md#rt-rte-onboard-add], note: "The supplied extraction protocol affords formulation by the calling agent, followed by wired add persistence."}
            - {value: trace-extracted, basis: afforded, records: [runtime.md#rt-rte-onboard-add], note: "Onboarding supplies historical sessions for that formulation; faithful caller extraction is not inspected."}
          records: [runtime.md#rt-rte-onboard-add]
          note: "The external semantic authoring process and ordinary add's original content provenance are unresolved."
        - scope: "Portable imports and builtin/custom starter admissions"
          assessment: partial
          findings:
            - {value: imported, basis: wired, records: [memory.md#mem-rte-portable-admission, epistemic.md#epi-rte-playbook-import], note: "Files and presets enter playbooks, including asserted standing and source metadata."}
          records: [memory.md#mem-rte-portable-admission, epistemic.md#epi-rte-playbook-import]
          note: "Known acquisition does not settle initial authoring, trace derivation or custom preset provenance. Shipped words are static before admission; their prior authorship is not independently reconstructed."
        - scope: "Merged/inverted rule words, calculated standing, recovery/delivery bookkeeping and instruction snapshots"
          assessment: known
          findings:
            - {value: other-compiled, basis: wired, records: [memory.md#mem-rte-rule-curation, epistemic.md#epi-rte-curator-inversion, memory.md#mem-obj-processed-log, memory.md#mem-obj-context-log, memory.md#mem-rte-provenance-read], note: "Software combines/reformats existing state or computes control fields; inversion creates avoidance text and project export renders an instruction snapshot."}
          records: [memory.md#mem-rte-rule-curation, epistemic.md#epi-rte-curator-inversion, memory.md#mem-obj-processed-log, memory.md#mem-obj-context-log, memory.md#mem-rte-provenance-read]
          note: "Known for these transformations, not an assertion that their upstream inputs share one origin."
        - scope: "Bullet vector cache"
          assessment: partial
          findings:
            - {value: other-compiled, basis: wired, records: [memory.md#mem-obj-embedding-cache], note: "Software computes numerical encodings from retained bullet content and admits cache entries."}
          records: [memory.md#mem-obj-embedding-cache, runtime.md#rt-cmp-embedding-model]
          note: "Cache derivation is known; mutable/name-only encoder provenance prevents complete embedding lineage."
        - scope: "Scanned trauma descriptions/patterns, caller trauma entries and blocked withdrawal entries"
          assessment: partial
          findings:
            - {value: trace-extracted, basis: wired, records: [memory.md#mem-rte-trauma-admission], note: "History scan extracts known dangerous-command patterns and generated descriptions before approval."}
            - {value: imported, basis: wired, records: [memory.md#mem-rte-trauma-admission], note: "Trauma import supplies persisted entries without authenticated original authorship."}
            - {value: other-compiled, basis: wired, records: [memory.md#mem-obj-blocked-entry, memory.md#mem-rte-rule-withdrawal], note: "Withdrawal records copy selected rule content and persist rejection bookkeeping."}
          records: [memory.md#mem-rte-trauma-admission, memory.md#mem-obj-human-message, memory.md#mem-obj-blocked-entry, memory.md#mem-rte-rule-withdrawal]
          note: "Generic manual pattern/message and withdrawal-reason origins are not resolved by field names or I/O."
        - scope: "External cass corpus initial and index provenance"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-context-read, runtime.md#rt-rte-reflection-update]
          note: "Originating logs and index construction are not supplied; CM export does not reconstruct all upstream lineage."
      records: [runtime.md#rt-rte-reflection-update, runtime.md#rt-rte-onboard-add, memory.md#mem-rte-portable-admission, memory.md#mem-obj-embedding-cache, memory.md#mem-rte-trauma-admission]
      note: "Trace extraction, import, compilation and afforded authorship coexist; initial caller/custom/corpus and encoder provenance remain local unknowns."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Rule words at later context recipient, next reflector and exported agent-file consumer"
          assessment: known
          findings:
            - {value: instruction, basis: wired, records: [runtime.md#rt-obj-playbook-bullet, runtime.md#rt-bap-rule-guidance], note: "Retained imperative rules supply standing directions through context and reflector prompts; guidance is advisory, not a compelled host action."}
            - {value: instruction, basis: afforded, records: [memory.md#mem-rte-provenance-read], note: "Rendered agent-file snapshots afford later host guidance; an actual host load is not inspected."}
          records: [runtime.md#rt-obj-playbook-bullet, runtime.md#rt-bap-rule-guidance, memory.md#mem-rte-provenance-read]
          note: "Distinct delivery strengths remain distinct findings; absence of compliance evidence does not erase instructional force."
        - scope: "Rule content/vectors and standing at context ranking and duplicate selection"
          assessment: known
          findings:
            - {value: ranking, basis: wired, records: [runtime.md#rt-rte-context-read, memory.md#mem-obj-feedback-events, memory.md#mem-obj-embedding-cache], note: "Retained words, dense features and feedback-derived scores influence relative priority even with fixed ranking code."}
            - {value: validation, basis: wired, records: [memory.md#mem-rte-rule-curation, memory.md#mem-obj-embedding-cache], note: "Existing content/features participate in duplicate admissibility checks; warning-only directive conflicts are not veto criteria."}
            - {value: enforcement, basis: wired, records: [memory.md#mem-rte-rule-curation], note: "Duplicate branches can skip additions or suppress deprecated matches before saving; this is distinct from advisory conflict logging."}
          records: [runtime.md#rt-rte-context-read, memory.md#mem-obj-feedback-events, memory.md#mem-obj-embedding-cache, memory.md#mem-rte-rule-curation]
          note: "Named fixed consumers establish priority and duplicate controls, not rule truth."
        - scope: "Diary/session experience and outcome/delivery attribution at durable rule or standing update consumers"
          assessment: known
          findings:
            - {value: learning, basis: wired, records: [runtime.md#rt-rte-reflection-update, memory.md#mem-rte-outcome-feedback, memory.md#mem-obj-diary-entry, memory.md#mem-obj-context-log], note: "Retained experience and attribution inputs feed durable guidance/standing updates for later requests; improved capacity and causal attribution remain unobserved."}
            - {value: knowledge, basis: wired, records: [memory.md#mem-obj-diary-entry, memory.md#mem-rte-provenance-read, runtime.md#rt-rte-context-read], note: "Diaries and historical snippets also supply descriptive context/evidence to reflector and requested diagnostic/context recipients."}
          records: [runtime.md#rt-rte-reflection-update, memory.md#mem-rte-outcome-feedback, memory.md#mem-obj-diary-entry, memory.md#mem-obj-context-log, memory.md#mem-rte-provenance-read]
          note: "Update-consumer learning and recipient knowledge are separate effects, not inferred from each other."
        - scope: "Reasoning, feedback explanations, withdrawn-rule diagnostics and trauma human_message at display recipients"
          assessment: known
          findings:
            - {value: knowledge, basis: wired, records: [memory.md#mem-obj-reasoning, memory.md#mem-obj-feedback-context, memory.md#mem-obj-human-message, memory.md#mem-rte-provenance-read], note: "These fields explain offered guidance, feedback or denial; shortened reasons and absent event histories bound what context recipients learn."}
          records: [memory.md#mem-obj-reasoning, memory.md#mem-obj-feedback-context, memory.md#mem-obj-human-message, memory.md#mem-rte-provenance-read]
          note: "No blanket instructional or enforcing force is assigned to explanation text; stale/omitted reasoning is not evidence of iterative criticism."
        - scope: "Processed/onboarding checkpoint state and outcome session/rule references at next-work selection"
          assessment: known
          findings:
            - {value: routing, basis: wired, records: [memory.md#mem-obj-processed-log, memory.md#mem-rte-outcome-feedback], note: "Stored growth/failure/progress state selects discovery, retry or input windows; matching delivery records select grading targets."}
          records: [memory.md#mem-obj-processed-log, memory.md#mem-rte-outcome-feedback]
          note: "Control over the next input/target is not content advice."
        - scope: "Retired/blocked rule state at merged loaders and active selectors"
          assessment: known
          findings:
            - {value: enforcement, basis: wired, records: [memory.md#mem-obj-blocked-entry, memory.md#mem-obj-feedback-events, memory.md#mem-rte-rule-withdrawal], note: "Current retired flags and blocked-content matches exclude guidance from active delivery, including similar copies under another ID."}
            - {value: validation, basis: wired, records: [memory.md#mem-obj-blocked-entry], note: "Stored blocked text supplies the exact/token-overlap criterion for current reliance eligibility on reload, not universal rejection at every write entry point."}
          records: [memory.md#mem-obj-blocked-entry, memory.md#mem-obj-feedback-events, memory.md#mem-rte-rule-withdrawal]
          note: "Eligibility checks and exclusion coexist; independent exports and legacy copies constrain completeness of withdrawal."
        - scope: "Trauma regex/status at generated host/Git matcher and CLI task-warning matcher"
          assessment: known
          findings:
            - {value: validation, basis: wired, records: [memory.md#mem-obj-trauma-entry, runtime.md#rt-rte-trauma-guard], note: "Stored active patterns define command/staged-text conformity under the matcher; regex membership is not a danger proof."}
            - {value: enforcement, basis: wired, records: [runtime.md#rt-rte-trauma-guard, runtime.md#rt-bap-guard-denial], note: "Matches emit denial JSON or nonzero Git status, conditional on installation and the external host honoring the result."}
            - {value: knowledge, basis: wired, records: [runtime.md#rt-rte-context-read, memory.md#mem-obj-human-message], note: "The memory annotation records a separate CLI-only nonblocking task warning, not identical MCP safety payloads."}
          records: [memory.md#mem-obj-trauma-entry, runtime.md#rt-rte-trauma-guard, runtime.md#rt-bap-guard-denial, runtime.md#rt-rte-context-read]
          note: "Actual consumer paths are known at source level, with host effect explicitly uninspected."
        - scope: "Undeclared diary-status/validator linguistic parts and opaque external history consumers beyond recorded projections"
          assessment: not-determinable
          findings: []
          records: [epistemic.md#epi-obj-session-diary, epistemic.md#epi-obj-validation-result, runtime.md#rt-rte-context-read]
          note: "The recorded granularity and hidden corpus do not establish independent authority paths for every part; current-run validator permission is not automatically retained memory authority."
      records: [runtime.md#rt-bap-rule-guidance, runtime.md#rt-rte-context-read, memory.md#mem-rte-outcome-feedback, memory.md#mem-obj-blocked-entry, memory.md#mem-obj-processed-log, runtime.md#rt-bap-guard-denial, epistemic.md#epi-obj-validation-result]
      note: "All seven forces have named local consumers; inventory/granularity limits prevent complete coverage, not the source-wired positive paths."
    write_agency:
      assessment: partial
      units:
        - scope: "Reflection diary/delta admission, inline/outcome grading, deterministic curation and embedding-cache adoption"
          assessment: known
          findings:
            - {value: automatic, basis: wired, records: [runtime.md#rt-rte-reflection-update, memory.md#mem-rte-outcome-feedback, memory.md#mem-rte-rule-curation, memory.md#mem-obj-embedding-cache], note: "Software/model admission has no per-content human approval; explicitly starting reflection does not make these writes manual."}
          records: [runtime.md#rt-rte-reflection-update, memory.md#mem-rte-outcome-feedback, memory.md#mem-rte-rule-curation, memory.md#mem-obj-embedding-cache]
          note: "Applies to the admitted derived content and metadata, independent of upstream authorship."
        - scope: "Automatic delivery logging, reflection recovery bookkeeping and outcome-derived event replay"
          assessment: known
          findings:
            - {value: automatic, basis: wired, records: [memory.md#mem-obj-context-log, memory.md#mem-obj-processed-log, memory.md#mem-rte-outcome-feedback], note: "Enabled operations compute/adopt their records under code policy rather than individual human review."}
          records: [memory.md#mem-obj-context-log, memory.md#mem-obj-processed-log, memory.md#mem-rte-outcome-feedback]
          note: "Configuration or workflow initiation is not approval of each generated log/checkpoint/event."
        - scope: "Initializer trauma scan batch approval"
          assessment: known
          findings:
            - {value: manual, basis: wired, records: [memory.md#mem-rte-trauma-admission], note: "An explicit human yes/no decision approves the displayed candidate set for permanent blocklist admission."}
          records: [memory.md#mem-rte-trauma-admission]
          note: "Manual admission is supported for this batch branch only; subsequent file I/O does not change its agency."
        - scope: "Generic single/batch add, onboarding caller, direct mark, import/starter replacement, explicit withdrawal/undo/scrub, project export and manual trauma add/import/heal/remove"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-onboard-add, runtime.md#rt-rte-feedback-update, memory.md#mem-rte-portable-admission, memory.md#mem-rte-rule-withdrawal, memory.md#mem-rte-provenance-read, memory.md#mem-rte-trauma-admission]
          note: "Explicit caller selections/replace flags do not resolve whether a human supplied or approved the content versus a computational caller. Software persistence alone cannot classify that decision."
        - scope: "External cass history admission and custom/imported content initialization before CM acquisition"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-reflection-update, memory.md#mem-rte-portable-admission]
          note: "Originating logs, index writers and external authors are not inspected; no upstream manual or automatic finding is licensed."
      records: [runtime.md#rt-rte-reflection-update, memory.md#mem-rte-trauma-admission, runtime.md#rt-rte-onboard-add, memory.md#mem-rte-portable-admission, memory.md#mem-rte-rule-withdrawal]
      note: "Automatic derived admission and manual batch approval coexist with unresolved caller-controlled and external branches."
    curation_operations:
      assessment: partial
      units:
        - scope: "Diary condensation of retained session material"
          assessment: partial
          findings:
            - {value: consolidate, basis: wired, records: [memory.md#mem-obj-diary-entry], note: "The LLM-free branch reduces session text to a first-task/line summary and tags while leaving raw history separately reachable."}
            - {value: consolidate, basis: claimed, records: [memory.md#mem-obj-diary-entry, runtime.md#rt-rte-reflection-update], note: "The model branch requests condensed accomplishments/decisions/lessons; implementation wires the request and persistence, not faithful semantic consolidation by the opaque model."}
          records: [memory.md#mem-obj-diary-entry, runtime.md#rt-rte-reflection-update, epistemic.md#epi-rte-diary-inference]
          note: "Model-output semantic preservation and additional inference are unresolved; default-success status is separate from summary condensation."
        - scope: "Curator/import duplicate handling"
          assessment: known
          findings:
            - {value: dedup, basis: wired, records: [memory.md#mem-rte-rule-curation, memory.md#mem-rte-portable-admission], note: "Exact/hash/overlap and optional similarity branches skip copies or combine feedback/provenance."}
          records: [memory.md#mem-rte-rule-curation, memory.md#mem-rte-portable-admission]
          note: "Recorded duplicate-handling effects establish dedup, independently of merge proposals' semantic transformation."
        - scope: "Rule merge proposal content at successor creation"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-rule-curation]
          note: "Target checks, successor creation, synthetic provenance and source retirement establish structural merge effects, but not that successor words reduce the inputs' existing claims. Without a recorded content relation, neither consolidate nor synthesize is established for this branch."
        - scope: "Replacement, feedback maturity/score processing and withdrawal/undo/scrub"
          assessment: known
          findings:
            - {value: evolve, basis: wired, records: [memory.md#mem-rte-rule-curation, memory.md#mem-rte-portable-admission], note: "Replace mutates existing content or replaces an imported same-ID object; reasons may remain stale."}
            - {value: decay, basis: wired, records: [memory.md#mem-obj-feedback-events, memory.md#mem-rte-outcome-feedback, memory.md#mem-rte-rule-curation], note: "Time-sensitive feedback weighting downweights influence and contributes to pruning thresholds."}
            - {value: promote, basis: wired, records: [memory.md#mem-obj-feedback-events, runtime.md#rt-rte-feedback-update, memory.md#mem-rte-rule-curation], note: "Feedback thresholds raise maturity/salience; preset starter standing is not itself earned promotion."}
            - {value: invalidate, basis: wired, records: [memory.md#mem-rte-rule-withdrawal, memory.md#mem-obj-blocked-entry, memory.md#mem-rte-rule-curation, memory.md#mem-rte-trauma-admission], note: "Deprecation, blocked reload, inversion-source retirement and healing withdraw current reliance while retaining state/history; hard deletion is a different effect."}
          records: [memory.md#mem-rte-rule-curation, memory.md#mem-rte-rule-withdrawal, memory.md#mem-obj-feedback-events, memory.md#mem-rte-trauma-admission]
          note: "Known software effects, with pinned/negative exceptions and residual-copy limits; no useful-learning claim follows."
        - scope: "Avoidance-rule production from harmful retained guidance and forget inversion"
          assessment: known
          findings:
            - {value: synthesize, basis: wired, records: [epistemic.md#epi-rte-curator-inversion, memory.md#mem-rte-rule-withdrawal], note: "Produces a new avoidance directive absent from the positive input, not merely a faithful reduced restatement. It is a policy/content synthesis, not accepted causal knowledge."}
          records: [epistemic.md#epi-rte-curator-inversion, memory.md#mem-rte-rule-withdrawal]
          note: "Generic inversion is distinct from the claimed condition-aware warning example."
        - scope: "Opaque model rule/refinement generation, external caller extraction and remaining uninspected maintenance depth"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-reflection-update, runtime.md#rt-rte-onboard-add, epistemic.md#epi-rte-validation-disposition, memory.md#mem-rte-rule-curation]
          note: "Proposals can reshape, derive or conjecture; no semantic input/output pair resolves every transformation. Warning-only conflict logging is not preventive invalidation, and acquisition/index rebuild alone supplies no curation value."
      records: [memory.md#mem-obj-diary-entry, memory.md#mem-rte-rule-curation, memory.md#mem-rte-rule-withdrawal, epistemic.md#epi-rte-curator-inversion, epistemic.md#epi-rte-validation-disposition]
      note: "All seven operations have local warrants at their own layers; opaque semantic transformations and uninspected depth prevent complete operation enumeration."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Requested task context, why/get/resource/search and portable/project export returns"
          assessment: known
          findings:
            - {value: pull, basis: wired, records: [runtime.md#rt-rte-context-read, memory.md#mem-rte-provenance-read, runtime.md#rt-rte-http-tools], note: "The recipient requests retained material; task ranking and code delivery do not turn the requested response into independent push."}
          records: [runtime.md#rt-rte-context-read, memory.md#mem-rte-provenance-read, runtime.md#rt-rte-http-tools]
          note: "Known requested operations; each reader has its own projection/budget, not context's universal guarantees."
        - scope: "Reflection's automatic selection/supply of diary, existing bullets and related history to the update model"
          assessment: known
          findings:
            - {value: push, basis: wired, records: [runtime.md#rt-rte-reflection-update, memory.md#mem-obj-diary-entry, runtime.md#rt-obj-playbook-bullet], note: "Code supplies retained summary/guidance/history to the delegated model without that consumer requesting those parts; an operator's reflection trigger does not make the model's context supply pull."}
          records: [runtime.md#rt-rte-reflection-update, memory.md#mem-obj-diary-entry, runtime.md#rt-obj-playbook-bullet]
          note: "This is an update-consumer push, not unsolicited injection into every enclosing coding-agent session."
        - scope: "Automatic guard/task-warning reads and internal checkpoint, attribution, cache, blocked/active-state reload consumers"
          assessment: known
          findings:
            - {value: push, basis: wired, records: [runtime.md#rt-rte-trauma-guard, runtime.md#rt-rte-context-read, memory.md#mem-obj-processed-log, memory.md#mem-rte-outcome-feedback, memory.md#mem-obj-embedding-cache, memory.md#mem-obj-blocked-entry], note: "Host events or running computations automatically reload retained controls/attribution/features for fixed consumers rather than responding to a request for those objects."}
          records: [runtime.md#rt-rte-trauma-guard, runtime.md#rt-rte-context-read, memory.md#mem-obj-processed-log, memory.md#mem-rte-outcome-feedback, memory.md#mem-obj-embedding-cache, memory.md#mem-obj-blocked-entry]
          note: "Requested high-level operations can contain automatic control supply; their requested terminal result remains pull."
        - scope: "Exported instruction snapshot at a later external host"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-provenance-read]
          note: "Agent-file purpose affords later guidance, but no recorded host loader, trigger or request/selection/delivery relation establishes pull or push at that later consumer. The separately recorded requested export remains pull; its direction does not resolve the later host read."
        - scope: "External corpus-internal and unspecified opaque consumer alternatives"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-context-read, runtime.md#rt-rte-reflection-update]
          note: "CM request/automatic-supply operations are classifiable; the external index and hosts do not supply complete read-chain coverage."
      records: [runtime.md#rt-rte-context-read, runtime.md#rt-rte-reflection-update, runtime.md#rt-rte-trauma-guard, memory.md#mem-rte-provenance-read, memory.md#mem-obj-processed-log]
      note: "Pull and push coexist at different operations; host adoption and opaque external chains prevent complete boundary enumeration."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Reflection trigger to selected diary/existing-playbook prompt fields"
          assessment: known
          findings:
            - {value: coarse, basis: wired, records: [runtime.md#rt-rte-reflection-update, runtime.md#rt-obj-playbook-bullet, memory.md#mem-obj-diary-entry], note: "Reflection supplies its session summary and formatted existing snapshot with fixed field/size limits; ID display alone is not targeted identifier selection of rules."}
          records: [runtime.md#rt-rte-reflection-update, runtime.md#rt-obj-playbook-bullet, memory.md#mem-obj-diary-entry]
          note: "Scope covers inspected prompt supply, not the opaque selector for every related-history snippet."
        - scope: "Related-history selection into reflection and exported instruction snapshot into a host"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-reflection-update, memory.md#mem-rte-provenance-read]
          note: "At most three related snippets and an afforded agent-file consumer are recorded, but complete selector inputs and host loading conditions do not establish a controlled signal for these alternatives."
        - scope: "Outcome application trigger to latest retained delivery log and existing rule targets; semantic-cache reuse trigger to retained vectors"
          assessment: known
          findings:
            - {value: identifier, basis: wired, records: [memory.md#mem-rte-outcome-feedback, memory.md#mem-obj-context-log, memory.md#mem-obj-embedding-cache], note: "Actual session match selects the latest attribution record and exact rule IDs select update targets; cache bullet-ID/content-hash/model checks select reusable numerical entries."}
          records: [memory.md#mem-rte-outcome-feedback, memory.md#mem-obj-context-log, memory.md#mem-obj-embedding-cache]
          note: "Identifiers act on retained parts delivered to software consumers, not merely as catalog labels."
        - scope: "Discovery/retry and loader triggers to progress/active/blocked control parts"
          assessment: known
          findings:
            - {value: coarse, basis: wired, records: [memory.md#mem-obj-processed-log, memory.md#mem-obj-feedback-events, memory.md#mem-obj-blocked-entry], note: "Progress eligibility, active status and applicable global/repo control files govern supplied state."
              }
            - {value: identifier, basis: wired, records: [memory.md#mem-obj-processed-log, memory.md#mem-obj-blocked-entry], note: "Session identity resolves progress/diary references; blocked IDs and exact content hashes select affected retained entries."}
            - {value: inferred-lexical, basis: wired, records: [memory.md#mem-obj-blocked-entry], note: "Merged-load trigger compares retained blocked text with current bullet tokens; high Jaccard overlap selects copies for withdrawal, not embedding judgment."}
          records: [memory.md#mem-obj-processed-log, memory.md#mem-obj-feedback-events, memory.md#mem-obj-blocked-entry]
          note: "Coarse availability and exact/token targeting remain separate mechanisms."
        - scope: "Pre-tool/Git or CLI task trigger to active trauma controls and matching explanation"
          assessment: known
          findings:
            - {value: coarse, basis: wired, records: [memory.md#mem-obj-trauma-entry, runtime.md#rt-rte-trauma-guard], note: "Active/global/project applicability determines the loaded pattern set before matching."}
            - {value: inferred-lexical, basis: wired, records: [runtime.md#rt-rte-trauma-guard, runtime.md#rt-rte-context-read, memory.md#mem-obj-human-message], note: "Command/staged-line or CLI task text is regex-matched against retained patterns; matches select denial/warning explanations. This is textual targeting, not identity matching or semantic danger judgment."}
          records: [memory.md#mem-obj-trauma-entry, runtime.md#rt-rte-trauma-guard, runtime.md#rt-rte-context-read, memory.md#mem-obj-human-message]
          note: "CLI warnings and host denial differ in force; fixed regex selectors establish neither host activation nor complete tool coverage."
        - scope: "Requested task-context lexical/embedding ranking and requested diagnostic IDs/resources"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-context-read, memory.md#mem-rte-provenance-read]
          note: "These selectors fulfill pull requests; they do not establish inferred-embedding or identifier push merely because an automatic reader computes the return."
      records: [runtime.md#rt-rte-reflection-update, memory.md#mem-rte-outcome-feedback, memory.md#mem-obj-processed-log, memory.md#mem-obj-blocked-entry, runtime.md#rt-rte-trauma-guard, memory.md#mem-rte-provenance-read]
      note: "Coarse, identifier and lexical push have actual automatic consumers; unresolved related-history and external host selectors keep coverage partial rather than inapplicable."
    trace_learning:
      assessment: partial
      units:
        - scope: "Automatic session export to retained diary/rule/reason to next reflector or requested context"
          assessment: known
          findings:
            - {value: "yes", basis: wired, records: [runtime.md#rt-rte-reflection-update, memory.md#mem-obj-diary-entry, memory.md#mem-obj-reasoning, runtime.md#rt-bap-rule-guidance], note: "Automatic trace-fed production persists summaries and behavior-shaping guidance with later consumers; no improved capacity or factual correctness is required for this wired axis."}
          records: [runtime.md#rt-rte-reflection-update, memory.md#mem-obj-diary-entry, memory.md#mem-obj-reasoning, runtime.md#rt-bap-rule-guidance]
          note: "Includes reduced LLM-free diaries when later supplied as context; the no-LLM reflector's lack of new deltas does not negate the retained-summary route."
        - scope: "Inline/session-outcome grading to durable feedback/standing to later scoring and selection"
          assessment: known
          findings:
            - {value: "yes", basis: wired, records: [memory.md#mem-rte-outcome-feedback, memory.md#mem-obj-feedback-events, memory.md#mem-obj-context-log], note: "Transcript judgments and outcome signals automatically change retained reliance metadata; later ranking/state consumers are wired, while attribution accuracy is unobserved."}
          records: [memory.md#mem-rte-outcome-feedback, memory.md#mem-obj-feedback-events, memory.md#mem-obj-context-log]
          note: "Raw delivery-log retention alone is insufficient; the subsequent durable event/standing update supplies the qualifying result."
        - scope: "Onboarding external extraction, explicit caller reports/maintenance/import and approval-gated trauma scan"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-onboard-add, runtime.md#rt-rte-feedback-update, memory.md#mem-rte-portable-admission, memory.md#mem-rte-trauma-admission, memory.md#mem-rte-rule-withdrawal]
          note: "Generic caller identity and external content provenance do not establish automatic trace-fed admission. The inspected trauma scan requires batch human approval, so it does not itself supply an automatic trace-learning yes; there is no bounded absence record licensing a system-wide no."
        - scope: "External history production and opaque provider/host alternatives"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-reflection-update, runtime.md#rt-cmp-generation-model]
          note: "External producers and hidden retention are outside inspected implementations; no additional learning route or negative can be inferred."
      records: [runtime.md#rt-rte-reflection-update, memory.md#mem-rte-outcome-feedback, memory.md#mem-obj-diary-entry, runtime.md#rt-rte-onboard-add, memory.md#mem-rte-trauma-admission]
      note: "Two automatic durable trace-fed chains establish yes; unresolved caller/external alternatives prevent complete route coverage. No local or global no is asserted without a bounded absence warrant."
    trace_source:
      assessment: partial
      units:
        - scope: "Original historical agent sessions feeding automatic diary/rule/reflected-feedback writes"
          assessment: known
          findings:
            - {value: session-logs, basis: wired, records: [runtime.md#rt-rte-reflection-update, memory.md#mem-obj-diary-entry], note: "Recorded user/assistant turns from coding sessions feed sanitized export, diary and rule generation; export serialization does not add event-stream origin."}
            - {value: tool-traces, basis: wired, records: [runtime.md#rt-rte-reflection-update, memory.md#mem-obj-diary-entry], note: "The memory annotation and write account record tool material in original session text used by trace-fed transformation; this value is local to that content, not a claim that every session contains tool results."}
          records: [runtime.md#rt-rte-reflection-update, memory.md#mem-obj-diary-entry]
          note: "Known qualifying source families for the inspected session-fed chain, without authentication or exhaustive historical coverage."
        - scope: "Inline and classified session-outcome grading to retained standing"
          assessment: partial
          findings:
            - {value: session-logs, basis: wired, records: [memory.md#mem-rte-outcome-feedback], note: "Payload-stripped historical session text supplies inline comments, IDs and outcome signals for automatic feedback."}
          records: [memory.md#mem-rte-outcome-feedback, memory.md#mem-obj-context-log]
          note: "Explicit outcome reports can instead come from an unresolved caller, and the records do not settle all mixed performance/sentiment signal origins. A matching delivery log is attribution metadata, not proof of multi-step trajectories or tool-trace-fed grading."
        - scope: "Caller-assisted onboarding/custom imports and trauma history scan admission"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-onboard-add, memory.md#mem-rte-portable-admission, memory.md#mem-rte-trauma-admission]
          note: "Recorded sessions/tool-call records are available upstream, but unresolved or human-gated admission prevents treating these as additional qualifying automatic trace-learning sources. Hook initiation alone does not make callback events the content learned from."
        - scope: "External raw corpus and hidden model/host input alternatives"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-reflection-update, runtime.md#rt-cmp-generation-model]
          note: "No supplied upstream corpus/provider trace resolves additional source content or linked state/action/outcome trajectories."
      records: [runtime.md#rt-rte-reflection-update, memory.md#mem-obj-diary-entry, memory.md#mem-rte-outcome-feedback, memory.md#mem-rte-trauma-admission]
      note: "Session logs and embedded tool material support local positives; mixed explicit outcomes, caller writes and opaque inputs remain unresolved. Neither event-streams nor trajectories is established merely by JSONL logs, callbacks or session chronology."
---

# cass_memory_system memory profile

## Comparison rationale

The profile classifies accumulated memory and its later consumers, not all storage or permissions in the runtime. YAML/JSON/JSONL establish files; repository placement does not establish a separate `repo` substrate. Dense cached vectors establish parametric form, not model-weight learning or a vector database. The encoder's unresolved immutable identity remains a lineage limit even though the cache's derivation and similarity consumer are wired ([MEM-OBJ-embedding-cache](memory.md#mem-obj-embedding-cache), [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model)). External cass is retained as an opaque history input rather than silently dropped to obtain complete coverage ([RT-RTE-context-read](runtime.md#rt-rte-context-read)).

Instruction and knowledge refer to different consumed parts. Rule imperatives supply standing guidance; descriptions, reasons and denial explanations supply context. Existing words, vectors and feedback also affect ranking or duplicate admissibility. Progress checkpoints route later work, while blocked content and trauma patterns can veto eligibility or matched actions. The latter's effective host prevention remains conditional and unobserved ([RT-BAP-rule-guidance](runtime.md#rt-bap-rule-guidance), [MEM-OBJ-reasoning](memory.md#mem-obj-reasoning), [MEM-OBJ-processed-log](memory.md#mem-obj-processed-log), [MEM-OBJ-blocked-entry](memory.md#mem-obj-blocked-entry), [RT-BAP-guard-denial](runtime.md#rt-bap-guard-denial)). These forces do not authenticate source truth or prove useful behavior.

Reconciliation supersedes EPI-RTE-outcome-feedback with [MEM-RTE-outcome-feedback](memory.md#mem-rte-outcome-feedback); every classification of that route cites the canonical memory record. The remaining containers and parts retain their declared identities. Reconciliation's missing separate diary-status and validator-linguistic parts remain explicit inventory limits, not new record IDs or invented dossiers ([EPI-OBJ-session-diary](epistemic.md#epi-obj-session-diary), [EPI-OBJ-validation-result](epistemic.md#epi-obj-validation-result)). The available combined records support the local status finding without resolving independently inventoried parts. Transient verdict/refinement objects are not classified as durable memory solely because they affect current admission.

Starting reflection, import or maintenance does not establish human content approval. Computational reflection and outcome grading are automatic; the trauma initializer's explicit batch approval is manual. Generic add/mark/replace/withdrawal callers remain unresolved at their actual decision points ([RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update), [RT-RTE-onboard-add](runtime.md#rt-rte-onboard-add), [MEM-RTE-portable-admission](memory.md#mem-rte-portable-admission), [MEM-RTE-trauma-admission](memory.md#mem-rte-trauma-admission)). Human approval of scan results is not an automatic trace-learning write.

Curation follows the implemented effect. Duplicate checks can skip copies or combine feedback/provenance. Rule merge checks targets, creates a successor and retires sources, but its recorded structural effects do not establish a reduced representation of the inputs' existing claims; that branch has no positive curation finding and remains not-determinable ([MEM-RTE-rule-curation](memory.md#mem-rte-rule-curation)). The independent fast-diary consolidation witness does not upgrade it. Replacement changes an entry; decay/maturity changes standing; retirement and healing withdraw reliance while preserving state. Inversion introduces an avoidance directive rather than merely shortening the original positive directive. Its synthesis is a policy transformation, not demonstrated acceptance of a new causal explanation ([MEM-RTE-rule-curation](memory.md#mem-rte-rule-curation), [MEM-RTE-rule-withdrawal](memory.md#mem-rte-rule-withdrawal), [EPI-RTE-curator-inversion](epistemic.md#epi-rte-curator-inversion)). Warning-only conflict logging establishes no preventive contradiction gate. Model-requested extraction does not settle every opaque output's semantic transformation; wired persistence is not an upgrade of the requested consolidation into observed faithful consolidation.

Read-back is split by operation. Task context and diagnostic returns fulfill requests and are pull, even though code selects their contents. Reflection automatically supplies retained context to the delegated model; fixed update, checkpoint and safety consumers automatically receive relevant state. Those are push operations inside otherwise caller-started chains. Actual session/ID/hash matches establish identifier targeting; active-state availability is coarse; regex and blocked-token matching are lexical. Requested lexical/embedding context ranking supplies no inferred-embedding push witness ([RT-RTE-context-read](runtime.md#rt-rte-context-read), [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update), [MEM-RTE-outcome-feedback](memory.md#mem-rte-outcome-feedback), [MEM-OBJ-blocked-entry](memory.md#mem-obj-blocked-entry), [RT-RTE-trauma-guard](runtime.md#rt-rte-trauma-guard)). Exported host guidance remains afforded as instruction authority, but its later read-back direction has no positive finding: neither a host request nor automatic supply is recorded. This uncertainty leaves the wired requested export intact and also prevents classifying the later host's push signal ([MEM-RTE-provenance-read](memory.md#mem-rte-provenance-read)).

Automatic summaries/rules and automatic standing updates qualify as trace learning because durable behavior-shaping results reach later consumers. They require neither new knowledge nor measured improvement. Original session turns and embedded tool material establish session-log and tool-trace source findings; a session-end callback is a trigger, not automatically the learned content. Asserted outcomes and delivery records do not establish linked trajectories or causal per-rule usefulness ([MEM-OBJ-diary-entry](memory.md#mem-obj-diary-entry), [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update), [MEM-RTE-outcome-feedback](memory.md#mem-rte-outcome-feedback)). No observed or causal basis is available, and no bounded absence record licenses a global negative.

Source-read log: no additional source reads. This classification uses only the supplied accepted records, their annotations and reconciliation; it adds no evidence, declares no records and reopens no report verification.

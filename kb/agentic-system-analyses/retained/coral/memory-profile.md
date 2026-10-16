---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "CORAL memory profile: shared island knowledge, experiment feedback, checkpoints and opaque host session recovery."
run-id: "AAS-2026-10-15-coral-25e5fdab9dc4-01"
source-identity: "https://github.com/Human-Agent-Society/CORAL"
reviewed-boundary: "0123dfb939b35228cf2c1fde224cd0561e727408"
memory-comparison:
  version: 2
  scope: "Included: retained island/public notes and raw captures, review sidecars, navigation/coverage material, mutable skills/resources and roles, attempt results and feedback, shared-state checkpoint history, migration summaries, session-pointer metadata and opaque resumed conversation alternatives; their admission, maintenance and later-consumer routes. Excluded: candidate code as a product rather than a memory abstraction, unchanged shipped instruction/skill text as such, all-runtime storage/permissions, provider parameters and external harness internals as attributed CORAL implementation. Host recovery effects stay included but unresolved."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "CORAL shared knowledge files, navigation, evolved skill resources, roles, attempts, migration announcements and session-pointer metadata"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-note-navigation"
                - "memory.md#mem-obj-skills"
                - "memory.md#mem-obj-roles"
                - "runtime.md#rt-obj-attempt"
                - "memory.md#mem-obj-migration-arrival"
                - "memory.md#mem-obj-session-state"
              note: "Hub readers and manager operate on retained Markdown, JSON and resource files. This finding includes pointer files, not the opaque conversation they address."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-note-navigation"
            - "memory.md#mem-obj-skills"
            - "memory.md#mem-obj-roles"
            - "runtime.md#rt-obj-attempt"
            - "memory.md#mem-obj-migration-arrival"
            - "memory.md#mem-obj-session-state"
          note: "These named filesystem surfaces are established; this does not inventory external host payload storage."
        -
          scope: "Requested external-source captures and synthesis-review sidecars"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-raw-sources"
                - "epistemic.md#epi-obj-review-json"
              note: "Research and reviewer instructions prescribe raw Markdown and sibling JSON on the shared filesystem."
          records:
            - "memory.md#mem-obj-raw-sources"
            - "epistemic.md#epi-obj-review-json"
          note: "The prescribed locations are known, but no actual capture or review was supplied."
        -
          scope: "Shared-state historical snapshots"
          assessment: "known"
          findings:
            -
              value: "repo"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint"
              note: "A local Git repository retains shared-state snapshots and patches."
          records:
            - "memory.md#mem-obj-checkpoint"
          note: "Repository history is distinct from the files it snapshots; candidate product repositories are not added as memory solely because they store code."
        -
          scope: "Host-owned recovered conversation payload, separate from session pointers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-session-state"
          note: "Payload creation/replay is external and uninspected; local JSONL lookup is not a complete substrate inventory of effective resumed state."
      records:
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-note-navigation"
        - "memory.md#mem-obj-skills"
        - "memory.md#mem-obj-roles"
        - "runtime.md#rt-obj-attempt"
        - "memory.md#mem-obj-migration-arrival"
        - "memory.md#mem-obj-session-state"
        - "memory.md#mem-obj-raw-sources"
        - "epistemic.md#epi-obj-review-json"
        - "memory.md#mem-obj-checkpoint"
      note: "Named CORAL stores are resolved, including requested capture/review stores. The included host conversation alternative remains opaque. Provider weights and all-runtime storage are excluded, not classified as memory substrates."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Knowledge bodies, role and skill guidance, navigation prose, migration prose and attempt explanation at model/human readers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-note-navigation"
                - "memory.md#mem-obj-skills"
                - "memory.md#mem-obj-roles"
                - "memory.md#mem-obj-migration-arrival"
                - "epistemic.md#epi-obj-attempt-feedback"
                - "memory.md#mem-bap-retained-guidance"
              note: "These retained bodies and explanations are interpreted by agents or operators."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-note-navigation"
            - "memory.md#mem-obj-skills"
            - "memory.md#mem-obj-roles"
            - "memory.md#mem-obj-migration-arrival"
            - "epistemic.md#epi-obj-attempt-feedback"
            - "memory.md#mem-bap-retained-guidance"
          note: "The text path is separate from parsed metadata and executable resources; wiring supports delivery, not compliance."
        -
          scope: "Parsed note/skill/role metadata, navigation links, attempt fields, checkpoint patches, session IDs and invoked skill scripts"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-note-navigation"
                - "memory.md#mem-obj-skills"
                - "memory.md#mem-obj-roles"
                - "epistemic.md#epi-obj-attempt-score"
                - "memory.md#mem-obj-checkpoint"
                - "memory.md#mem-obj-session-state"
              note: "Localized fields and links are processed by fixed reader/manager/Git rules; scripts have an executable symbolic path."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-note-navigation"
            - "memory.md#mem-obj-skills"
            - "memory.md#mem-obj-roles"
            - "epistemic.md#epi-obj-attempt-score"
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-obj-session-state"
          note: "Numerical scores are symbolic scalars, not parametric representations; role history citations and index tables are distinct structured parts."
        -
          scope: "Requested raw-source and review-output parts"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-raw-sources"
                - "epistemic.md#epi-obj-review-json"
              note: "Captured assertions and review evidence/judgments use natural language."
            -
              value: "symbolic"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-raw-sources"
                - "epistemic.md#epi-obj-review-json"
              note: "Provenance fields and per-claim review verdict structures use named fields."
          records:
            - "memory.md#mem-obj-raw-sources"
            - "epistemic.md#epi-obj-review-json"
          note: "The prescribed text and structured parts are separated by consumption, though neither has an observed instance."
        -
          scope: "Effective resumed conversation and any host-derived continuation material"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-session-state"
          note: "No payload or host compaction implementation establishes the complete mixture of text, structured tool material or opaque state."
      records:
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-note-navigation"
        - "memory.md#mem-obj-skills"
        - "memory.md#mem-obj-roles"
        - "memory.md#mem-obj-migration-arrival"
        - "epistemic.md#epi-obj-attempt-feedback"
        - "memory.md#mem-bap-retained-guidance"
        - "epistemic.md#epi-obj-attempt-score"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-obj-session-state"
        - "memory.md#mem-obj-raw-sources"
        - "epistemic.md#epi-obj-review-json"
      note: "Known forms cover the specified file parts and consumers; they do not classify the unresolved resumed payload. No parametric memory value is inferred from merely using external models."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Model-authored notes, roles, skills and research coverage judgments"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-knowledge-revision"
                - "memory.md#mem-obj-note-navigation"
                - "memory.md#mem-obj-roles"
                - "memory.md#mem-obj-skills"
              note: "Foreground or specialist models formulate retained knowledge/procedures and coverage judgments without per-content human approval."
            -
              value: "trace-extracted"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-knowledge-revision"
                - "memory.md#mem-obj-skills"
              note: "The result/log/transcript-to-note or skill route explicitly uses experiment experience for later retained guidance."
          records:
            - "memory.md#mem-rte-knowledge-revision"
            - "memory.md#mem-obj-note-navigation"
            - "memory.md#mem-obj-roles"
            - "memory.md#mem-obj-skills"
          note: "Authored formulation and trace derivation coexist on the result-fed branch; external research-only inputs do not thereby become traces."
        -
          scope: "Raw external research assertions"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-raw-sources"
                - "epistemic.md#epi-rte-research-writing"
              note: "Research instructions request fetching and saving external text before synthesis."
          records:
            - "memory.md#mem-obj-raw-sources"
            - "epistemic.md#epi-rte-research-writing"
          note: "Source warrant and capture fidelity are unresolved, not an alternative lineage for the prescribed import route."
        -
          scope: "Generated navigation, checkpoint snapshots and migration summary"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-note-navigation"
                - "memory.md#mem-rte-note-maintenance"
                - "memory.md#mem-obj-checkpoint"
              note: "Index generation derives navigation from filenames/headings/metadata; Git captures existing shared files without semantic extraction."
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-migration-arrival"
                - "runtime.md#rt-rte-island-migration"
              note: "Arrival prose derives an identity/source-island/recent-score coordination summary from migration activity."
          records:
            - "memory.md#mem-obj-note-navigation"
            - "memory.md#mem-rte-note-maintenance"
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-obj-migration-arrival"
            - "runtime.md#rt-rte-island-migration"
          note: "Mechanical compilation is not automatically a lesson; the migration output is a separate event-derived summary."
        -
          scope: "Attempt and grader feedback records"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-attempt"
                - "epistemic.md#epi-obj-attempt-score"
                - "epistemic.md#epi-obj-attempt-feedback"
              note: "Submission and grader machinery record candidate identity and evaluation outcomes for later scheduling and interpretation."
          records:
            - "runtime.md#rt-obj-attempt"
            - "epistemic.md#epi-obj-attempt-score"
            - "epistemic.md#epi-obj-attempt-feedback"
          note: "This lineage alone does not make raw attempt retention trace learning."
        -
          scope: "Initial custom skill/role seed origin and replacement content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-skills"
            - "memory.md#mem-obj-roles"
          note: "Configured files can be copied/replaced, but generic configured paths do not establish their initial authored/imported/compiled derivation."
        -
          scope: "Recovered host conversation and possible derived summaries"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-session-state"
          note: "The original payload and any internal derivation/embedding path were not inspected."
      records:
        - "memory.md#mem-rte-knowledge-revision"
        - "memory.md#mem-obj-note-navigation"
        - "memory.md#mem-obj-roles"
        - "memory.md#mem-obj-skills"
        - "memory.md#mem-obj-raw-sources"
        - "epistemic.md#epi-rte-research-writing"
        - "memory.md#mem-rte-note-maintenance"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-obj-migration-arrival"
        - "runtime.md#rt-rte-island-migration"
        - "runtime.md#rt-obj-attempt"
        - "epistemic.md#epi-obj-attempt-score"
        - "epistemic.md#epi-obj-attempt-feedback"
        - "memory.md#mem-obj-session-state"
      note: "Positive derivations remain local. Known subsequent revision does not resolve initial seed provenance or host payload derivation. Static bundled guidance is excluded except as the starting point of mutable skill/role objects."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Retained notes, raw evidence, attempt feedback and review reports at later readers and revisers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "epistemic.md#epi-obj-attempt-feedback"
                - "memory.md#mem-rte-knowledge-query"
                - "memory.md#mem-bap-retained-guidance"
              note: "Requested reads deliver notes and result explanations as evidence/context/advice."
            -
              value: "knowledge"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-raw-sources"
                - "epistemic.md#epi-obj-review-json"
              note: "Saved external assertions and reviewer judgments are prescribed evidence for research authors."
            -
              value: "learning"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-knowledge-revision"
                - "memory.md#mem-obj-skills"
              note: "Retained experiment records, own transcript and sibling knowledge feed requested durable note/skill/role revisions; this update consumer differs from later planning."
          records:
            - "memory.md#mem-obj-notes"
            - "epistemic.md#epi-obj-attempt-feedback"
            - "memory.md#mem-rte-knowledge-query"
            - "memory.md#mem-bap-retained-guidance"
            - "memory.md#mem-obj-raw-sources"
            - "epistemic.md#epi-obj-review-json"
            - "memory.md#mem-rte-knowledge-revision"
            - "memory.md#mem-obj-skills"
          note: "The update path is afforded, while file delivery is wired; neither status establishes improved capacity."
        -
          scope: "Evolved skills and role descriptions at foreground/specialist agents"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-skills"
                - "memory.md#mem-obj-roles"
                - "memory.md#mem-rte-knowledge-revision"
                - "memory.md#mem-bap-retained-guidance"
              note: "Retained procedures and revised role posture direct subsequent task behavior when read/invoked."
            -
              value: "routing"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-roles"
                - "memory.md#mem-obj-note-navigation"
                - "memory.md#mem-rte-knowledge-revision"
              note: "Role descriptions and coverage judgments guide complementary lanes and research-gap selection."
          records:
            - "memory.md#mem-obj-skills"
            - "memory.md#mem-obj-roles"
            - "memory.md#mem-obj-note-navigation"
            - "memory.md#mem-rte-knowledge-revision"
            - "memory.md#mem-bap-retained-guidance"
          note: "These are prompt-mediated effects, not interpreter-enforced obedience; static shipped task prohibitions are excluded."
        -
          scope: "Attempt score/status/history at manager heartbeat and migration consumers"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-attempt-score"
                - "runtime.md#rt-rte-island-migration"
              note: "Retained numeric outcomes determine relative agent rank and migration eligibility."
            -
              value: "routing"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-attempt-score"
                - "runtime.md#rt-rte-heartbeat-feedback"
                - "runtime.md#rt-rte-island-migration"
              note: "Score history, budgets and attempt identity select interventions, stopping and destination/recipient paths."
          records:
            - "epistemic.md#epi-obj-attempt-score"
            - "runtime.md#rt-rte-heartbeat-feedback"
            - "runtime.md#rt-rte-island-migration"
          note: "Numeric scheduling authority is distinct from the feedback body read by the model."
        -
          scope: "Archived-attempt flags and retained note access/navigation metadata at fixed readers"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-resume-steering"
                - "memory.md#mem-rte-knowledge-query"
                - "memory.md#mem-rte-note-maintenance"
              note: "Archived-attempt state excludes entries from default active views; note/index exclusion predicates constrain their respective readers, not every path."
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-state"
                - "memory.md#mem-rte-knowledge-query"
                - "memory.md#mem-obj-note-navigation"
              note: "Session IDs select recovery targets and retained index/metadata guide file discovery and scoped query delivery."
          records:
            - "runtime.md#rt-rte-resume-steering"
            - "memory.md#mem-rte-knowledge-query"
            - "memory.md#mem-rte-note-maintenance"
            - "memory.md#mem-obj-session-state"
            - "memory.md#mem-obj-note-navigation"
          note: "Direct-hash recovery remains possible; supersession labels do not establish universal withdrawal. Literal note search is filtering, not evidenced relative-score ranking."
        -
          scope: "Saved research-source text at the prescribed synthesis reviewer"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-raw-sources"
                - "epistemic.md#epi-rte-synthesis-review"
              note: "The reviewer compares substantive note claims with cited retained source passages to judge support."
          records:
            - "memory.md#mem-obj-raw-sources"
            - "epistemic.md#epi-rte-synthesis-review"
          note: "This is advisory model evaluation, not an automatic admission veto. Static lint rules are not retained memory criteria."
        -
          scope: "Recovered conversation content at the host and resumed model"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-session-state"
          note: "The pointer selects a session, but the complete consumed payload and its force remain uninspected."
      records:
        - "memory.md#mem-obj-notes"
        - "epistemic.md#epi-obj-attempt-feedback"
        - "memory.md#mem-rte-knowledge-query"
        - "memory.md#mem-bap-retained-guidance"
        - "memory.md#mem-obj-raw-sources"
        - "epistemic.md#epi-obj-review-json"
        - "memory.md#mem-rte-knowledge-revision"
        - "memory.md#mem-obj-skills"
        - "memory.md#mem-obj-roles"
        - "memory.md#mem-obj-note-navigation"
        - "epistemic.md#epi-obj-attempt-score"
        - "runtime.md#rt-rte-heartbeat-feedback"
        - "runtime.md#rt-rte-island-migration"
        - "runtime.md#rt-rte-resume-steering"
        - "memory.md#mem-rte-note-maintenance"
        - "memory.md#mem-obj-session-state"
        - "epistemic.md#epi-rte-synthesis-review"
      note: "Each positive names a retained part and actual or prescribed consumer. Unconsumed metadata has no inferred force; model endpoint weights, static policy files and current-run permissions are not substituted for memory authority. Host payload effects remain unresolved."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Model-mediated knowledge, skill, role, capture, review and semantic-maintenance admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-knowledge-revision"
                - "memory.md#mem-rte-note-maintenance"
                - "memory.md#mem-obj-skills"
                - "memory.md#mem-obj-roles"
              note: "Models choose and admit retained content via ordinary file writes without mandatory per-content human approval."
            -
              value: "automatic"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-research-writing"
                - "epistemic.md#epi-rte-synthesis-review"
                - "epistemic.md#epi-rte-confidence-disposition"
              note: "Research authors/reviewers are instructed to write captures, verdicts and confidence changes; the calling model decides disposition."
          records:
            - "memory.md#mem-rte-knowledge-revision"
            - "memory.md#mem-rte-note-maintenance"
            - "memory.md#mem-obj-skills"
            - "memory.md#mem-obj-roles"
            - "epistemic.md#epi-rte-research-writing"
            - "epistemic.md#epi-rte-synthesis-review"
            - "epistemic.md#epi-rte-confidence-disposition"
          note: "Workflow initiation does not make subsequent model admission manual; prescribed semantic steps are not upgraded to wired by file-copy capability."
        -
          scope: "Attempt/checkpoint creation, grader finalization, index generation, arrival summaries and archival metadata updates"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-attempt"
                - "memory.md#mem-obj-checkpoint"
                - "memory.md#mem-rte-note-maintenance"
                - "memory.md#mem-obj-migration-arrival"
                - "runtime.md#rt-rte-resume-steering"
              note: "Software publishes attempts/snapshots, generates index files, writes arrival summaries and changes active-view state without per-item human acceptance."
          records:
            - "runtime.md#rt-obj-attempt"
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-rte-note-maintenance"
            - "memory.md#mem-obj-migration-arrival"
            - "runtime.md#rt-rte-resume-steering"
          note: "A human may initiate a command; these specified mechanisms admit their generated content automatically."
        -
          scope: "Initial/custom skill and role supply or replacement decision"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-skills"
            - "memory.md#mem-obj-roles"
          note: "Copy behavior is inspected, but configured file selection does not establish a human decision supplying or approving that retained content; no manual value is inferred."
        -
          scope: "Host conversation persistence and any summary admission"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-session-state"
          note: "External host creation and compression controls were not inspected."
      records:
        - "memory.md#mem-rte-knowledge-revision"
        - "memory.md#mem-rte-note-maintenance"
        - "memory.md#mem-obj-skills"
        - "memory.md#mem-obj-roles"
        - "epistemic.md#epi-rte-research-writing"
        - "epistemic.md#epi-rte-synthesis-review"
        - "epistemic.md#epi-rte-confidence-disposition"
        - "runtime.md#rt-obj-attempt"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-obj-migration-arrival"
        - "runtime.md#rt-rte-resume-steering"
        - "memory.md#mem-obj-session-state"
      note: "Known software/model admissions coexist with unresolved initial-content and host admission. There is no supported system-wide manual/automatic exclusivity claim."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Requested semantic consolidation, duplicate merge and existing note/skill/role revision"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-knowledge-revision"
                - "memory.md#mem-rte-note-maintenance"
              note: "Prompts request combining existing notes/results into reusable reduced guidance; this supports consolidation without assuming new claims."
            -
              value: "dedup"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-note-maintenance"
              note: "The model/judge workflow requests merging duplicate content and archiving originals; scorer/judge internals are not a wired correct-dedup witness."
            -
              value: "evolve"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-knowledge-revision"
                - "memory.md#mem-obj-roles"
                - "memory.md#mem-obj-skills"
              note: "Existing skill, role and knowledge entries can be revised following results and meaningful posture changes."
          records:
            - "memory.md#mem-rte-knowledge-revision"
            - "memory.md#mem-rte-note-maintenance"
            - "memory.md#mem-obj-roles"
            - "memory.md#mem-obj-skills"
          note: "These values classify supported requested transformations only; no successful semantic operation was observed."
        -
          scope: "Attempt archival from active views"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-resume-steering"
                - "runtime.md#rt-obj-attempt"
              note: "Archived attempts remain on disk while default leaderboard/status/log readers withdraw them from active reliance."
          records:
            - "runtime.md#rt-rte-resume-steering"
            - "runtime.md#rt-obj-attempt"
          note: "This is bounded to attempt readers, not automatic invalidation of dependent notes or session narrative."
        -
          scope: "Research confidence and source-loss withdrawal"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-confidence-disposition"
              note: "Author instructions mark unsupported notes superseded or needing reverification while preserving history."
          records:
            - "epistemic.md#epi-rte-confidence-disposition"
          note: "This is requested withdrawal, not uniform reader exclusion; raising confidence alone is not evidenced tier/salience promotion."
        -
          scope: "Novel-claim synthesis, dedup helper internals and full maintenance transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-knowledge-revision"
            - "memory.md#mem-rte-note-maintenance"
            - "epistemic.md#epi-rte-research-writing"
          note: "Synthesis wording alone does not establish a new claim absent from inputs. Semantic input/output pairs and uninspected scorer/judge/write-tail details are missing, preventing synthesize classification or complete curation enumeration."
        -
          scope: "Host conversation compaction and alternative summaries"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-session-state"
          note: "No inspected host implementation supports or excludes consolidation, decay or other transformations on recovered conversation."
      records:
        - "memory.md#mem-rte-knowledge-revision"
        - "memory.md#mem-rte-note-maintenance"
        - "memory.md#mem-obj-roles"
        - "memory.md#mem-obj-skills"
        - "runtime.md#rt-rte-resume-steering"
        - "runtime.md#rt-obj-attempt"
        - "epistemic.md#epi-rte-confidence-disposition"
        - "epistemic.md#epi-rte-research-writing"
        - "memory.md#mem-obj-session-state"
      note: "Supported requested operations and wired attempt withdrawal remain visible. Index rebuilding and checkpoint acquisition alone add no curation values. Opaque maintenance/host alternatives prevent a complete axis; no unsupported decay/promote/synthesize negatives are asserted."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Later caller-requested note/skill/raw/metadata/checkpoint access"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-knowledge-query"
                - "memory.md#mem-obj-checkpoint"
                - "memory.md#mem-bap-retained-guidance"
              note: "CLI/API/file requests return retained knowledge, listings or historical patches; fulfilling a request is not a second unsolicited push."
            -
              value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-knowledge-revision"
                - "memory.md#mem-obj-raw-sources"
                - "memory.md#mem-obj-roles"
              note: "Planning, warm-start and research instructions request model reads of prior evidence, roles, index and research output."
          records:
            - "memory.md#mem-rte-knowledge-query"
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-bap-retained-guidance"
            - "memory.md#mem-rte-knowledge-revision"
            - "memory.md#mem-obj-raw-sources"
            - "memory.md#mem-obj-roles"
          note: "Code-backed requested delivery and prompt-mediated model use keep separate warrants; dashboard requests are not broadcasts to all agents."
        -
          scope: "Manager-selected finalized-result feedback to the committing agent"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-heartbeat-feedback"
                - "runtime.md#rt-obj-attempt"
              note: "Polling and heartbeat rules inject selected result fields and prompts through interrupt/resume without a model request for those retained fields."
          records:
            - "runtime.md#rt-rte-heartbeat-feedback"
            - "runtime.md#rt-obj-attempt"
          note: "The selected result plus action prompts is not automatic embedding of full notes/skills; batching prevents per-attempt delivery guarantees."
        -
          scope: "Recovered host payload and host skill-disclosure alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-session-state"
            - "memory.md#mem-obj-skills"
          note: "CORAL can request session recovery, but payload selection/delivery and host progressive-disclosure details were not inspected; no complete direction classification follows."
      records:
        - "memory.md#mem-rte-knowledge-query"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-bap-retained-guidance"
        - "memory.md#mem-rte-knowledge-revision"
        - "memory.md#mem-obj-raw-sources"
        - "memory.md#mem-obj-roles"
        - "runtime.md#rt-rte-heartbeat-feedback"
        - "runtime.md#rt-obj-attempt"
        - "memory.md#mem-obj-session-state"
        - "memory.md#mem-obj-skills"
      note: "Both pull and push exist locally. Known file requests and heartbeat injection do not resolve host recovery or alternate skill-context supply."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Heartbeat result feedback selection and recipient targeting"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-heartbeat-feedback"
                - "epistemic.md#epi-obj-attempt-score"
              note: "Trigger: finalized-attempt polling. Inputs: scored-new availability, budgets, interval/plateau history and stop rules. Selected retained part: one latest result header/feedback plus applicable prompt text; broad eligibility/cadence is coarse selection."
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-heartbeat-feedback"
                - "runtime.md#rt-obj-attempt"
              note: "Trigger: feedback delivery after selection. Input: selected attempt committing-agent identity matched to the live agent. Selected retained part: that result header/feedback delivered to the matched recipient, not a requested file ID."
          records:
            - "runtime.md#rt-rte-heartbeat-feedback"
            - "epistemic.md#epi-obj-attempt-score"
            - "runtime.md#rt-obj-attempt"
          note: "Coarse scheduling and identity-targeted delivery are distinct operations; no embedding or lexical push selector is established by CLI substring search."
        -
          scope: "Explicitly requested file/CLI/API/checkpoint returns"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-knowledge-query"
            - "memory.md#mem-obj-checkpoint"
          note: "These units fulfill requests, so their paths, literal query text, date/status and numeric positions are pull selectors rather than push-signal values."
        -
          scope: "Host resume payload and skill-trigger selection"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-session-state"
            - "memory.md#mem-obj-skills"
          note: "The actual automatic trigger inputs and selected retained payload are not inspected; progressive-disclosure doctrine does not establish implemented inferred-judgment selection."
      records:
        - "runtime.md#rt-rte-heartbeat-feedback"
        - "epistemic.md#epi-obj-attempt-score"
        - "runtime.md#rt-obj-attempt"
        - "memory.md#mem-rte-knowledge-query"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-obj-session-state"
        - "memory.md#mem-obj-skills"
      note: "Heartbeat supplies positive coarse and identifier push witnesses. Pull-only units are locally inapplicable, but unresolved host alternatives keep this axis partial rather than globally inapplicable."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Experiment/log/transcript-fed durable note, skill and role revision followed by later reads"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-knowledge-revision"
                - "memory.md#mem-obj-skills"
                - "memory.md#mem-obj-roles"
                - "memory.md#mem-bap-retained-guidance"
              note: "Models are asked to turn retained results/logs/own transcript into durable guidance/procedures that later agents read. Automatic model admission qualifies even though compliance and improvement are unobserved."
          records:
            - "memory.md#mem-rte-knowledge-revision"
            - "memory.md#mem-obj-skills"
            - "memory.md#mem-obj-roles"
            - "memory.md#mem-bap-retained-guidance"
          note: "This is the afforded trace-fed write/retention/later-consumer chain, not a claim of learned weights or observed improved capacity."
        -
          scope: "Automatic migration arrival-summary write and later knowledge query"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-migration-arrival"
                - "runtime.md#rt-rte-island-migration"
                - "memory.md#mem-rte-knowledge-query"
              note: "Manager derives retained arrival prose from move identity and recent-best score; later notes/API consumers can use it as coordination context."
          records:
            - "memory.md#mem-obj-migration-arrival"
            - "runtime.md#rt-rte-island-migration"
            - "memory.md#mem-rte-knowledge-query"
          note: "A coordination summary qualifies without distilling a successful technique; actual later model dependence is unobserved."
        -
          scope: "Research-only acquisition, raw attempt/checkpoint retention and structural helper output"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw-sources"
            - "memory.md#mem-obj-checkpoint"
            - "runtime.md#rt-obj-attempt"
            - "memory.md#mem-rte-note-maintenance"
            - "memory.md#mem-rte-knowledge-revision"
          note: "These facts alone do not establish a qualifying trace-fed behavior-shaping transformation. The mixed research/revision boundary and uninspected helpers prevent a bounded all-routes no; their known feeds are classified separately above."
        -
          scope: "Host continuation-summary or compaction write followed by resume"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-session-state"
          note: "No inspected implementation establishes whether host traces produce a retained continuation artifact or only replay raw turns."
      records:
        - "memory.md#mem-rte-knowledge-revision"
        - "memory.md#mem-obj-skills"
        - "memory.md#mem-obj-roles"
        - "memory.md#mem-bap-retained-guidance"
        - "memory.md#mem-obj-migration-arrival"
        - "runtime.md#rt-rte-island-migration"
        - "memory.md#mem-rte-knowledge-query"
        - "memory.md#mem-obj-raw-sources"
        - "memory.md#mem-obj-checkpoint"
        - "runtime.md#rt-obj-attempt"
        - "memory.md#mem-rte-note-maintenance"
        - "memory.md#mem-obj-session-state"
      note: "Positive afforded and wired routes remain separate. Raw logging, snapshotting and inference alone do not establish trace learning. No bounded negative record justifies a local or global no; host and mixed-write alternatives remain unresolved."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Experiment-result and own-session inputs to requested knowledge/skill revision"
          assessment: "known"
          findings:
            -
              value: "tool-traces"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-knowledge-revision"
                - "memory.md#mem-obj-skills"
                - "epistemic.md#epi-obj-attempt-feedback"
              note: "Recorded experiment execution feedback and log/result material feed requested explanations/procedures."
            -
              value: "session-logs"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-knowledge-revision"
                - "memory.md#mem-obj-skills"
              note: "The requested own-transcript/trace analysis branch consumes recorded conversational work, not merely imported source prose."
          records:
            - "memory.md#mem-rte-knowledge-revision"
            - "memory.md#mem-obj-skills"
            - "epistemic.md#epi-obj-attempt-feedback"
          note: "Each source value belongs to the afforded update chain. Ordinary external research captures do not become event streams by being stored with metadata."
        -
          scope: "Migration arrival-summary inputs"
          assessment: "known"
          findings:
            -
              value: "event-streams"
              basis: "wired"
              records:
                - "memory.md#mem-obj-migration-arrival"
                - "runtime.md#rt-rte-island-migration"
              note: "The manager consumes the discrete relocation event: agent identity, source/destination context and recent score, to write retained arrival context."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-migration-arrival"
                - "runtime.md#rt-rte-island-migration"
                - "epistemic.md#epi-obj-attempt-score"
              note: "The included recent-best score originates in recorded grader execution outcomes; the mixed summary retains that evaluation-result input alongside migration event state."
          records:
            - "memory.md#mem-obj-migration-arrival"
            - "runtime.md#rt-rte-island-migration"
            - "epistemic.md#epi-obj-attempt-score"
          note: "The original score origin and migration event are distinct mixed inputs; no linked state-action-outcome trajectory is established by the summary."
        -
          scope: "Other content in mixed revision/research and partly inspected maintenance routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-knowledge-revision"
            - "memory.md#mem-obj-raw-sources"
            - "memory.md#mem-rte-note-maintenance"
          note: "The records do not fully enumerate original content for every possible qualifying write. Imported static research alone is not a trace-source value; no source is invented for opaque helpers."
        -
          scope: "Original inputs to any host continuation artifact"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-session-state"
          note: "Conversation/tool/event composition of host-produced summaries is uninspected. A session ID does not classify that payload or its update inputs."
      records:
        - "memory.md#mem-rte-knowledge-revision"
        - "memory.md#mem-obj-skills"
        - "epistemic.md#epi-obj-attempt-feedback"
        - "memory.md#mem-obj-migration-arrival"
        - "runtime.md#rt-rte-island-migration"
        - "epistemic.md#epi-obj-attempt-score"
        - "memory.md#mem-obj-raw-sources"
        - "memory.md#mem-rte-note-maintenance"
        - "memory.md#mem-obj-session-state"
      note: "Trace source is assessed per qualifying update. Event streams and tool feedback are supported on the wired arrival branch; session and execution traces on the afforded revision branch. Unresolved writes prevent completeness or global inapplicability."
---

# CORAL memory profile

## Comparison rationale

The comparison covers mutable, accumulated material rather than every file the runtime uses. In particular, the model identifiers and static launch prohibitions do not establish parametric memory or enforcement authority for the shared knowledge store. Session-pointer metadata is symbolic and file-backed; the effective recovered conversation is a separate unresolved unit ([MEM-OBJ-session-state](memory.md#mem-obj-session-state)). No inspected display summary substitutes for that opaque payload.

Reconciliation makes no supersessions. Notes and research-note records remain valid overlapping scopes; raw captures and review judgments remain separate parts; attempt score and feedback retain distinct consumers. This profile uses the narrower parts where consumer/form matters and keeps the memory revision route's afforded warrant separate from claimed research/review procedures. Wired heartbeat transport does not upgrade requested semantic revision ([MEM-RTE-knowledge-revision](memory.md#mem-rte-knowledge-revision), [EPI-RTE-research-writing](epistemic.md#epi-rte-research-writing), [EPI-OBJ-attempt-score](epistemic.md#epi-obj-attempt-score), [EPI-OBJ-attempt-feedback](epistemic.md#epi-obj-attempt-feedback)).

Automatic admission is not synonymous with mechanical text generation. A model selecting and writing a skill is automatic absent a per-content human decision. Configured seed replacement is separately unresolved: the file-copy operation does not identify who approved the supplied content ([MEM-OBJ-skills](memory.md#mem-obj-skills), [MEM-OBJ-roles](memory.md#mem-obj-roles)). No manual value is inferred from a generic caller.

Knowledge, instruction, learning, routing, ranking, validation and enforcement name different consumers or effects. Experiment evidence feeds a requested artifact update; its output can later advise planning or direct procedures. Numeric attempt history drives manager ranking/routing. Saved source passages serve as criteria for the requested reviewer, not as a mandatory software gate. Archival flags affect fixed active-view readers but do not erase direct-hash access or retract dependent notes ([MEM-BAP-retained-guidance](memory.md#mem-bap-retained-guidance), [RT-RTE-island-migration](runtime.md#rt-rte-island-migration), [EPI-RTE-synthesis-review](epistemic.md#epi-rte-synthesis-review), [RT-RTE-resume-steering](runtime.md#rt-rte-resume-steering)).

Curation follows supported transformations. Consolidation, duplicate merging and entry revision are afforded model work; attempt-view withdrawal is wired. The word synthesis does not establish a new claim absent from inputs, and index regeneration alone is not consolidation. Unknown semantic input/output relations, incomplete helper inspection and host compaction prevent a complete curation inventory ([MEM-RTE-note-maintenance](memory.md#mem-rte-note-maintenance), [MEM-RTE-knowledge-revision](memory.md#mem-rte-knowledge-revision), [EPI-RTE-research-writing](epistemic.md#epi-rte-research-writing)).

Requested query returns are pull even when code filters or physically delivers them. The independent feedback push uses coarse eligibility/cadence and a committing-agent identity match for its selected result. These are not lexical or semantic push retrieval of notes. Skill-trigger and host-recovery policies remain unresolved rather than borrowing the known query route's assessment ([MEM-RTE-knowledge-query](memory.md#mem-rte-knowledge-query), [RT-RTE-heartbeat-feedback](runtime.md#rt-rte-heartbeat-feedback), [MEM-OBJ-skills](memory.md#mem-obj-skills)).

Trace learning is a write-route classification, not a demonstrated-benefit verdict. The requested result/transcript-to-guidance chain supports an afforded positive. The automatic migration announcement supports a wired positive because it derives durable coordination context from relocation and score history for later note consumers. Its original inputs include a runtime relocation event and grader execution feedback; the raw checkpoint alone establishes neither a derived lesson nor a trace-learning negative. External research text is imported content, not a trace merely because it has capture metadata ([MEM-RTE-knowledge-revision](memory.md#mem-rte-knowledge-revision), [MEM-OBJ-migration-arrival](memory.md#mem-obj-migration-arrival), [MEM-OBJ-checkpoint](memory.md#mem-obj-checkpoint), [MEM-OBJ-raw-sources](memory.md#mem-obj-raw-sources)).

All axis coverage is partial because the included recovered-payload alternative and other locally named missing facts remain unresolved. This does not weaken the local positive witnesses or invent absence. No source files were read for this profile: classification uses only the supplied accepted records and their annotations, with reconciliation used for identity resolution. No new records, quotations, execution evidence or causal findings are added.

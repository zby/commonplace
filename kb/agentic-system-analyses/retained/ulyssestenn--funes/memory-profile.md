---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Funes memory profile: retained library files, editorial compilation and later wiki consumption at the frozen revision."
run-id: AAS-2026-10-15-funes-a9e6dbb3946a-01
source-identity: https://github.com/ulyssestenn/funes
reviewed-boundary: 3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11
memory-comparison:
  version: 2
  scope: >-
    Retained library originals, searchable editions, source notes, concepts,
    topics, registry, wiki index, saved outputs, dated health reports and
    changelog; their admission, editorial maintenance and later consumers.
    Includes setup-created local scope/deviation instructions and their future
    loading, but excludes unchanged shipped protocol/scaffold text as memory.
    Standalone helper stdout, transient extraction state, temporary images and
    current CI status are not retained library memory. Saved helper content is
    included when retained for library use. External host/provider internals,
    linked example libraries and unacquired user libraries are excluded, not
    classified as absent. Optional Git versioning is distinguished from files.
  axes:
    storage_substrate:
      assessment: known
      units:
        - scope: "Library originals, editions, wiki prose, navigation, outputs, reports, changelog and setup-created local instructions on disk"
          assessment: known
          findings:
            - value: files
              basis: claimed
              records: [runtime.md#rt-obj-library-tree, runtime.md#rt-rte-library-setup, memory.md#mem-obj-health-reports, memory.md#mem-obj-changelog]
              note: "The prescribed retained library is a file tree; this does not claim an observed populated library."
          records: [runtime.md#rt-obj-library-tree, runtime.md#rt-rte-library-setup, memory.md#mem-obj-health-reports, memory.md#mem-obj-changelog]
          note: "The container and separately described parts cover the included file inventory, including binary originals."
        - scope: "PDF and saved-caption editions produced by the executable helpers"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [runtime.md#rt-rte-pdf-sidecar, runtime.md#rt-rte-caption-fetch, memory.md#mem-obj-text-editions]
              note: "The file-writing branches persist text; stdout-only caption calls do not belong to this retained unit."
          records: [runtime.md#rt-rte-pdf-sidecar, runtime.md#rt-rte-caption-fetch, memory.md#mem-obj-text-editions]
          note: "Includes partial PDF output, alternate caption formats and caller-selected paths when admitted to the library."
        - scope: "Committed versions of the retained library"
          assessment: known
          findings:
            - value: repo
              basis: afforded
              records: [runtime.md#rt-obj-library-tree, runtime.md#rt-rte-library-setup]
              note: "Git affords history and recovery; provisioning requests commit/push, not universal automatic commits of ingest."
          records: [runtime.md#rt-obj-library-tree, runtime.md#rt-rte-library-setup]
          note: "Optional versioned retention is distinct from precommit filesystem retention."
      records: [runtime.md#rt-obj-library-tree, runtime.md#rt-rte-library-setup, memory.md#mem-obj-text-editions, memory.md#mem-obj-health-reports, memory.md#mem-obj-changelog]
      note: "The declared tree and its parts cover the scoped retained substrates. The external model/provider is not an opaque library storage alternative."
    representational_form:
      assessment: partial
      units:
        - scope: "Readable originals and editions, compiled prose, topic descriptions, index labels, registry descriptions, output prose, reports, changelog and new local guidance at agent/human readers"
          assessment: known
          findings:
            - value: natural-language
              basis: claimed
              records: [runtime.md#rt-obj-library-tree, memory.md#mem-obj-raw-originals, memory.md#mem-obj-text-editions, memory.md#mem-obj-source-notes, memory.md#mem-obj-concepts, memory.md#mem-obj-topics, memory.md#mem-obj-source-registry, memory.md#mem-obj-wiki-index, memory.md#mem-obj-outputs, memory.md#mem-obj-health-reports, memory.md#mem-obj-changelog, runtime.md#rt-rte-library-setup]
              note: "These parts receive consequences through interpretation of text, including prescriptions in saved outputs or local scope instructions."
          records: [runtime.md#rt-obj-library-tree, memory.md#mem-bap-wiki-evidence, runtime.md#rt-rte-library-setup]
          note: "This unit concerns readable semantic content, not binary originals or mechanically parsed fields."
        - scope: "PDF page/method/provenance labels and caption JSON fields/timestamps on retained helper outputs"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-text-editions, runtime.md#rt-rte-pdf-sidecar, runtime.md#rt-rte-caption-fetch]
              note: "Localized fields and serialization rules encode provenance and boundaries. Numeric timestamps are not distributed-parametric representations."
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-text-editions, epistemic.md#epi-rte-caption-reshape, runtime.md#rt-rte-pdf-sidecar]
              note: "Executable branches emit readable extracted/transcribed words; their fidelity is not established by this form classification."
          records: [memory.md#mem-obj-text-editions, epistemic.md#epi-rte-caption-reshape, runtime.md#rt-rte-pdf-sidecar]
          note: "Includes plain-text and structured alternatives, without treating the display metadata as the speech payload."
        - scope: "Paths, link targets, frontmatter markers and selected text/counts consumed by mechanical library audits"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [epistemic.md#epi-rte-mechanical-checks, memory.md#mem-obj-source-notes, memory.md#mem-obj-concepts]
              note: "Fixed parser and overlap rules consume localized symbols, even when the same prose is natural language at a Librarian reader."
          records: [epistemic.md#epi-rte-mechanical-checks, runtime.md#rt-obj-library-tree]
          note: "The audit route supplies the actual fixed-rule consumption path; its transient diagnostics are not additional retained memory."
        - scope: "Binary original payloads and unspecified non-prose output formats"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-raw-originals, memory.md#mem-obj-outputs]
          note: "The records identify opaque binaries and allow other output formats without a representation/consumer account. Their storage or linked summaries cannot classify those payloads."
      records: [runtime.md#rt-obj-library-tree, memory.md#mem-obj-raw-originals, memory.md#mem-obj-outputs, memory.md#mem-obj-text-editions, epistemic.md#epi-rte-mechanical-checks, runtime.md#rt-rte-library-setup]
      note: "Readable content and fixed-rule paths are resolved, but opaque originals and unspecified output formats prevent complete form coverage; model weights are outside this memory boundary."
    lineage:
      assessment: known
      units:
        - scope: "Human-supplied raw originals"
          assessment: known
          findings:
            - value: imported
              basis: claimed
              records: [memory.md#mem-obj-raw-originals, runtime.md#rt-rte-ingest-compile]
              note: "Documents, dropped files and pasted material are acquired for verbatim retention; their upstream truth or authorship is not thereby established."
          records: [memory.md#mem-obj-raw-originals, runtime.md#rt-rte-ingest-compile]
          note: "This resolves entry lineage, not every source's earlier history."
        - scope: "Retained machine-extracted PDF and fetched-caption editions"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-text-editions, runtime.md#rt-rte-pdf-sidecar, epistemic.md#epi-rte-caption-reshape]
              note: "Extraction/OCR and serialization derive readable editions, rather than extracting experience from an established activity trace."
            - value: imported
              basis: wired
              records: [runtime.md#rt-rte-caption-fetch, memory.md#mem-obj-text-editions]
              note: "Saved fetched captions enter from an external service; import and local formatting are distinct derivation steps."
          records: [memory.md#mem-obj-text-editions, runtime.md#rt-rte-pdf-sidecar, runtime.md#rt-rte-caption-fetch]
          note: "Includes native/OCR PDF branches and saved caption formats; remote recognition internals are excluded dependencies, not an inferred embedding origin."
        - scope: "Agent transcription and compilation of source notes and concepts from retained sources"
          assessment: known
          findings:
            - value: other-compiled
              basis: claimed
              records: [memory.md#mem-obj-text-editions, memory.md#mem-obj-source-notes, memory.md#mem-obj-concepts, runtime.md#rt-rte-ingest-compile]
              note: "Source-fed abstraction and transcription are requested transformations; supplied chat content is not automatically an agent-session trace."
          records: [memory.md#mem-obj-text-editions, memory.md#mem-obj-source-notes, memory.md#mem-obj-concepts]
          note: "The specified derivation is known at instruction strength without asserting semantic entailment or a produced instance."
        - scope: "Librarian-created topic organization, registry/index updates, outputs, health diagnoses, changelog entries and setup-created local guidance"
          assessment: known
          findings:
            - value: authored
              basis: claimed
              records: [memory.md#mem-obj-topics, memory.md#mem-obj-source-registry, memory.md#mem-obj-wiki-index, memory.md#mem-obj-outputs, memory.md#mem-obj-health-reports, memory.md#mem-obj-changelog, runtime.md#rt-rte-library-setup]
              note: "The Librarian writes organization, generated work, diagnoses and operation descriptions under the procedure; authored does not mean manually admitted."
          records: [memory.md#mem-obj-topics, memory.md#mem-obj-source-registry, memory.md#mem-obj-wiki-index, memory.md#mem-obj-outputs, memory.md#mem-obj-health-reports, memory.md#mem-obj-changelog, runtime.md#rt-rte-library-setup]
          note: "Empty initialization and later updates are separately described by the records; no trace-extraction producer is silently inferred from logging."
      records: [runtime.md#rt-obj-library-tree, runtime.md#rt-rte-ingest-compile, runtime.md#rt-rte-library-setup, memory.md#mem-obj-text-editions, memory.md#mem-obj-changelog]
      note: "Known classifies the recorded entry/derivation mechanisms, not the unknown upstream provenance or factual warrant of arbitrary future source claims."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Originals, readable editions and compiled source/concept content at later compilation, verification and Q&A consumers"
          assessment: known
          findings:
            - value: knowledge
              basis: claimed
              records: [memory.md#mem-obj-raw-originals, memory.md#mem-obj-text-editions, memory.md#mem-obj-source-notes, memory.md#mem-obj-concepts, memory.md#mem-bap-wiki-evidence]
              note: "Retained content is requested evidence and context, not guaranteed truth or an executable instruction to the Librarian."
          records: [memory.md#mem-bap-wiki-evidence, runtime.md#rt-rte-wiki-answer, runtime.md#rt-rte-ingest-compile]
          note: "The actual intended consumers are named; neither activation nor answer benefit is observed."
        - scope: "Topic maps, wiki index/connection notices and registry status at Librarian navigation and pending-source selection"
          assessment: known
          findings:
            - value: routing
              basis: claimed
              records: [memory.md#mem-obj-topics, memory.md#mem-obj-wiki-index, memory.md#mem-obj-source-registry]
              note: "Retained organization informs which source, concept or library the agent reads or compiles; this is discretionary routing, not an implemented ranker."
          records: [memory.md#mem-obj-topics, memory.md#mem-obj-wiki-index, memory.md#mem-obj-source-registry]
          note: "The described selection effect supports routing at instruction strength; IDs alone do not establish ranking."
        - scope: "Setup-created local scope/deviation guidance at future Librarian entry"
          assessment: known
          findings:
            - value: instruction
              basis: claimed
              records: [runtime.md#rt-rte-library-setup, runtime.md#rt-bap-librarian-instructions]
              note: "New retained local guidance directs later work if loaded by the host; unchanged shipped instructions are excluded from accumulated memory."
          records: [runtime.md#rt-rte-library-setup, runtime.md#rt-bap-librarian-instructions]
          note: "Requested instruction authority is not a machine-enforced write barrier."
        - scope: "Saved output substance at offered filing-back and health diagnoses at editorial repair"
          assessment: known
          findings:
            - value: knowledge
              basis: claimed
              records: [memory.md#mem-obj-outputs, memory.md#mem-obj-health-reports, runtime.md#rt-rte-health-audit, runtime.md#rt-rte-wiki-answer]
              note: "Outputs supply reusable content and diagnoses supply advice for fixes in their named workflows. Filing and recurrent report reload are not automatic."
          records: [memory.md#mem-obj-outputs, memory.md#mem-obj-health-reports]
          note: "The finding covers the documented editorial use, not every unspecified future inspection."
        - scope: "Changelog history and unspecified later reload of previous health reports or non-prose outputs"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-changelog, memory.md#mem-obj-health-reports, memory.md#mem-obj-outputs]
          note: "Readable retention alone does not establish a later force. No specified old-log consumer, recurrent report consumer or non-prose consumption path resolves this unit."
      records: [memory.md#mem-bap-wiki-evidence, memory.md#mem-obj-wiki-index, memory.md#mem-obj-source-registry, memory.md#mem-obj-outputs, memory.md#mem-obj-health-reports, memory.md#mem-obj-changelog, runtime.md#rt-bap-librarian-instructions]
      note: "Knowledge, routing and new local instruction authority are supported. Transient audit status is not a retained criterion; no enforcement, validation, ranking or learning value is inferred merely from an audit reading memory. Unspecified later consumers prevent full coverage."
    write_agency:
      assessment: partial
      units:
        - scope: "Human supply of raw source content and explicit approval of cross-library links"
          assessment: known
          findings:
            - value: manual
              basis: claimed
              records: [memory.md#mem-obj-raw-originals, runtime.md#rt-rte-ingest-compile]
              note: "The human supplies the original and must approve the proposed cross-library connection before writing; this is per-content control, not simply workflow initiation."
          records: [memory.md#mem-obj-raw-originals, runtime.md#rt-rte-ingest-compile]
          note: "Human approval is an instruction rule, not demonstrated interception of arbitrary writes."
        - scope: "Routine Librarian admission of raw persistence, transcriptions, source notes, concept revisions, topics, registry/index edits, outputs, reports and changelog"
          assessment: known
          findings:
            - value: automatic
              basis: claimed
              records: [runtime.md#rt-rte-ingest-compile, runtime.md#rt-rte-wiki-answer, runtime.md#rt-rte-health-audit, memory.md#mem-obj-changelog]
              note: "The model admits ordinary edits without mandatory per-content human approval; the human's source request does not make these derived admissions manual."
          records: [runtime.md#rt-rte-ingest-compile, runtime.md#rt-rte-wiki-answer, runtime.md#rt-rte-health-audit, memory.md#mem-obj-changelog]
          note: "Safe fixes belong here; proposed non-safe fixes and offered filing remain distinct decision branches."
        - scope: "PDF extraction and caption serialization/file admission"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-pdf-sidecar, runtime.md#rt-rte-caption-fetch]
              note: "Code admits extracted or serialized content without per-page or per-snippet approval, including partial PDF text."
          records: [runtime.md#rt-rte-pdf-sidecar, runtime.md#rt-rte-caption-fetch]
          note: "Unknown identity of a generic caller does not obscure the subsequent software admission mechanism."
        - scope: "Confirmed setup conventions and agent-authored local instructions/scaffold"
          assessment: known
          findings:
            - value: manual
              basis: claimed
              records: [runtime.md#rt-rte-library-setup]
              note: "The human explicitly settles or has supplied the structural conventions."
            - value: automatic
              basis: claimed
              records: [runtime.md#rt-rte-library-setup]
              note: "The agent authors and admits the resulting files without final per-file approval."
          records: [runtime.md#rt-rte-library-setup]
          note: "Choice of conventions and admission of generated file contents are separate stages of this setup chain."
        - scope: "Durable output filing and non-safe editorial changes proposed to the human"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-outputs, runtime.md#rt-rte-wiki-answer, runtime.md#rt-rte-health-audit]
          note: "The offer/proposal establishes a decision opportunity, but the records do not resolve final per-content admission across the stronger output README wording and shared protocol. No unconditional automatic installation or deployed human veto is established."
      records: [runtime.md#rt-rte-ingest-compile, runtime.md#rt-rte-library-setup, runtime.md#rt-rte-pdf-sidecar, runtime.md#rt-rte-caption-fetch, runtime.md#rt-rte-health-audit, memory.md#mem-obj-outputs]
      note: "Both human-controlled and computational admissions are supported locally; ambiguous offered/proposed changes retain uncertainty instead of inheriting routine edit agency."
    curation_operations:
      assessment: partial
      units:
        - scope: "Source-note abstraction and compression of retained raw source claims"
          assessment: known
          findings:
            - value: consolidate
              basis: claimed
              records: [runtime.md#rt-rte-ingest-compile, memory.md#mem-obj-source-notes]
              note: "The requested summary and takeaways reduce retained source material; keeping originals does not exclude consolidation."
          records: [runtime.md#rt-rte-ingest-compile, memory.md#mem-obj-source-notes]
          note: "This is requested editorial transformation, not an implemented semantic compiler or observed faithful summary."
        - scope: "Merging existing concepts and editorial redo/repair of retained wiki entries"
          assessment: known
          findings:
            - value: dedup
              basis: claimed
              records: [runtime.md#rt-rte-ingest-compile, memory.md#mem-obj-concepts]
              note: "The procedure says merge rather than duplicate; the linter's duplicate detection alone would not establish deduplication."
            - value: evolve
              basis: claimed
              records: [memory.md#mem-obj-concepts, runtime.md#rt-rte-health-audit]
              note: "Existing articles are merged, corrected or redone by the Librarian, rather than only rebuilding an access index."
          records: [memory.md#mem-obj-concepts, runtime.md#rt-rte-ingest-compile, runtime.md#rt-rte-health-audit]
          note: "The evidence layer remains instruction strength despite wired diagnostic helpers."
        - scope: "Novel claim generation, output filing and withdrawal beyond the described editorial revisions"
          assessment: not-determinable
          findings: []
          records: [epistemic.md#epi-obj-wiki, memory.md#mem-obj-outputs, runtime.md#rt-rte-health-audit]
          note: "No actual input/output claim relation establishes synthesis. Filing durable parts is not by itself tier/salience promotion, and criticism/proposed correction does not establish a history-preserving invalidation mechanism."
      records: [runtime.md#rt-rte-ingest-compile, memory.md#mem-obj-source-notes, memory.md#mem-obj-concepts, memory.md#mem-obj-outputs, runtime.md#rt-rte-health-audit, epistemic.md#epi-obj-wiki]
      note: "Consolidation, deduplication and evolution have claimed local warrants. Extraction, primary acquisition, link repair and audits are not additional curation operations by name alone; semantic novelty and further withdrawal operations remain unresolved."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Question-driven wiki retrieval, compilation/source verification and requested editorial inspection"
          assessment: known
          findings:
            - value: pull
              basis: claimed
              records: [runtime.md#rt-rte-wiki-answer, runtime.md#rt-rte-ingest-compile, runtime.md#rt-rte-health-audit, memory.md#mem-bap-wiki-evidence]
              note: "The consumer seeks retained content in response to the question or editorial task; the agent's relevance judgment inside that request does not create another push operation."
          records: [runtime.md#rt-rte-wiki-answer, runtime.md#rt-rte-ingest-compile, runtime.md#rt-rte-health-audit]
          note: "On-demand index/source/concept reading has no fixed numerical context budget. Standalone helper production is not later read-back."
        - scope: "Future loading of setup-created local guidance"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-library-setup, runtime.md#rt-bap-librarian-instructions]
          note: "The instructions allow host loading or an explicit read request; actual host delivery and selection are uninspected. Neither unsolicited push nor exclusively requested pull is established for this included part."
        - scope: "Later use of old health reports/changelog and offered output filing"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-health-reports, memory.md#mem-obj-changelog, memory.md#mem-obj-outputs]
          note: "Reports/logs lack a specified recurrent trigger and outputs require an unresolved follow-up. Retention does not establish an automatic later supply chain."
      records: [runtime.md#rt-rte-wiki-answer, runtime.md#rt-rte-ingest-compile, runtime.md#rt-rte-health-audit, runtime.md#rt-bap-librarian-instructions, memory.md#mem-obj-health-reports, memory.md#mem-obj-changelog, memory.md#mem-obj-outputs]
      note: "Supported pull routes do not resolve the included local-guidance delivery and unspecified later report/output routes; the scoped boundary cannot be declared completely pull-only."
    read_back_signal:
      assessment: not-determinable
      units:
        - scope: "Question-driven wiki and requested source/editorial pull chains"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-wiki-answer, runtime.md#rt-rte-ingest-compile, runtime.md#rt-rte-health-audit, memory.md#mem-bap-wiki-evidence]
          note: "Within these named requested-consumption operations there is no independent push selector to classify. Agent judgment and relative paths used during pull do not establish inferred-judgment or identifier push signals."
        - scope: "Host delivery of newly created local guidance"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-library-setup, runtime.md#rt-bap-librarian-instructions]
          note: "No inspected trigger/selector establishes whether or how a host pushes retained local guidance; folder identity alone is not a demonstrated identity-match selector."
        - scope: "Unspecified later report/log consumption and output-filing follow-up"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-health-reports, memory.md#mem-obj-changelog, memory.md#mem-obj-outputs]
          note: "No complete later selection chain or automatic supply is specified, so no controlled push signal follows."
      records: [runtime.md#rt-rte-wiki-answer, runtime.md#rt-bap-librarian-instructions, memory.md#mem-obj-health-reports, memory.md#mem-obj-changelog, memory.md#mem-obj-outputs]
      note: "Inspection yields no supported positive signal, while unresolved included delivery routes prevent axis-wide inapplicability. No ranking, lexical match, embedding or coarse availability selector is invented."
    trace_learning:
      assessment: not-determinable
      units:
        - scope: "Source-fed compilation, subsequent editorial updates, output filing and setup-created instructions"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-ingest-compile, runtime.md#rt-rte-library-setup, memory.md#mem-obj-raw-originals, memory.md#mem-obj-outputs, memory.md#mem-obj-concepts]
          note: "Automatic source-fed writes and later knowledge consumers are documented, but generic documents/chat/pasted content do not establish original activity-trace content on a qualifying route. Neither a positive trace-fed chain nor a bounded all-source negative is recorded. Setup choices alone are not a session-log extraction chain."
        - scope: "Operation records in changelog/health reports and possible feedback to later work"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-changelog, memory.md#mem-obj-health-reports, runtime.md#rt-rte-health-audit, runtime.md#rt-abs-model-driver]
          note: "Logging activity or retaining diagnoses does not close a trace-to-durable-behavior-shaping-write-to-later-consumer chain. No automatic recurrent report/log consumer is specified; the missing driver bounds implementation but does not prove every instruction-mediated update absent."
      records: [runtime.md#rt-rte-ingest-compile, runtime.md#rt-rte-library-setup, memory.md#mem-obj-raw-originals, memory.md#mem-obj-outputs, memory.md#mem-obj-changelog, memory.md#mem-obj-health-reports, runtime.md#rt-abs-model-driver]
      note: "No qualifying positive route is established by the accepted records. This is not a system-wide no: arbitrary source origins and missing later report/log consumers prevent a complete bounded absence classification. No learning benefit or parameter change is inferred."
    trace_source:
      assessment: not-determinable
      units:
        - scope: "Potential trace-fed source compilation, output reuse or editorial report/log update routes"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-raw-originals, memory.md#mem-obj-text-editions, memory.md#mem-obj-outputs, memory.md#mem-obj-health-reports, memory.md#mem-obj-changelog, runtime.md#rt-rte-ingest-compile]
          note: "No qualifying trace-learning chain establishes an original trace input. A chat-fed document is not necessarily a recorded agent session; caption timestamps do not by themselves identify environmental events. Health findings and change descriptions lack a specified subsequent automatic update consumer."
      records: [memory.md#mem-obj-raw-originals, memory.md#mem-obj-text-editions, memory.md#mem-obj-outputs, memory.md#mem-obj-health-reports, memory.md#mem-obj-changelog, runtime.md#rt-rte-ingest-compile]
      note: "No source category can be asserted. This is not inapplicable because bounded complete absence of trace learning has not been established; tool output acquisition alone is not tool-trace learning."
---

# Funes memory profile

## Comparison rationale

The inventory is the retained library and its later-consumer routes, not all
storage reachable by an external agent. [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree)
and its memory-declared parts distinguish ordinary files from optional Git
history. [RT-CMP-librarian-model](runtime.md#rt-cmp-librarian-model) is an external
component, not evidence that library memory resides in model weights. The
profile excludes unchanged shipped instructions but includes the local scope
and deviation text created by [RT-RTE-library-setup](runtime.md#rt-rte-library-setup).
Its future instruction authority is documented, while host delivery remains
uninspected under [RT-BAP-librarian-instructions](runtime.md#rt-bap-librarian-instructions).
This difference is why storage can be resolved while read-back remains partial.

The reconciliation supersedes the epistemic raw-original and output declarations
with [MEM-OBJ-raw-originals](memory.md#mem-obj-raw-originals) and
[MEM-OBJ-outputs](memory.md#mem-obj-outputs). The profile uses those canonical
records. Other overlaps remain valid containers or parts, not supersessions.
The combined caption object does not license one classification for fetched
speech and track-list availability metadata; only retained editions are
classified here through [MEM-OBJ-text-editions](memory.md#mem-obj-text-editions)
and [RT-RTE-caption-fetch](runtime.md#rt-rte-caption-fetch). Similarly, the
combined audit-results object does not turn transient diagnostics into retained
health reports. The unresolved part-declaration conflicts limit claims of
complete object-level separation, but do not prevent the bounded classifications
of retained reports in [MEM-OBJ-health-reports](memory.md#mem-obj-health-reports)
or fixed-rule consumption in
[EPI-RTE-mechanical-checks](epistemic.md#epi-rte-mechanical-checks).

Requested semantic operations keep claimed bases. Executable PDF and caption
writes keep wired bases. Neither upgrades the other. The retained substance of
[MEM-OBJ-source-notes](memory.md#mem-obj-source-notes) is knowledge at a later
Librarian reader and symbolic text at the mechanical audit consumer. Audit
findings themselves do not establish retained validation or enforcement
criteria. The status consumer in
[EPI-RTE-audit-disposition](epistemic.md#epi-rte-audit-disposition) receives a
current command result, not a remembered policy certificate.

Compilation supports consolidation of source claims, merging supports dedup,
and correction supports evolution. The indeterminate actual semantic relation
in [EPI-OBJ-wiki](epistemic.md#epi-obj-wiki) prevents a synthesis finding; the
word synthesis in an output description is insufficient. No particular output
has been shown to create a claim absent from its inputs. Automatic admission
of these requested model-authored changes does not imply manual approval
because the human started ingest. Conversely, the explicit cross-library
approval in [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile) supports a
local manual mechanism without proving a universal write barrier.

The ordinary wiki read in [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer)
fulfills a question-driven request. Agent relevance judgment inside that pull
chain does not establish a push signal. Setup-created guidance could have a
different delivery route, but the records leave that host behavior uninspected.
Old report/log availability in [MEM-OBJ-health-reports](memory.md#mem-obj-health-reports)
and [MEM-OBJ-changelog](memory.md#mem-obj-changelog) is not recurrent consumption.
These limits prevent both an axis-wide pull-only assertion and signal
inapplicability.

Trace-learning uncertainty is independent of the positive automatic writes,
curation and later knowledge authority. The accepted records describe generic
source acquisition, not a qualifying original trace input for every such write.
Logging operations does not itself demonstrate the required subsequent update
and consumer. No local or system-wide negative is manufactured from lack of
execution evidence or from [RT-ABS-model-driver](runtime.md#rt-abs-model-driver),
which only bounds the shipped executable driver. The empty scaffold and lack
of run evidence preclude observed or causal findings, not claimed mechanisms.

Source-read log: none. This classification uses only the supplied accepted
members and reconciliation; no frozen-source reread or new evidence was added.

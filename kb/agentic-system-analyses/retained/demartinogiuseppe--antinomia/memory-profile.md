---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Antinomia memory comparison: retained vault content, feedback, configuration and recovery routes at the frozen plugin revision."
run-id: "AAS-2026-11-08-antinomia-19694628edc2-01"
source-identity: "https://github.com/demartinogiuseppe/antinomia"
reviewed-boundary: "6fafd01082fbecb2a18803500a1abe70a2bdc9f4"
memory-comparison:
  version: 2
  scope: "Retained vault note prose and inline assumptions; U-note text; typed/dependency/dismissal metadata; PDF/YouTube source hubs and originals; persisted settings/run summaries; migration backups and optional raw-response notes, with their shipped admission, maintenance and later model/human/control consumers. Excludes static shipped prompts/templates as accumulated memory, transient comparison results and reconstructible working caches, external provider weights/retention, host implementation and human learning. Existing-content provenance, settings substrate, PDF internals and unestablished trace-fed update/automatic delivery routes remain explicit uncertainties."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Vault Markdown bodies, frontmatter, source hubs, PDF attachments, raw debug notes and migration copies"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records: ["memory.md#mem-obj-note-content","memory.md#mem-obj-presupposition","memory.md#mem-obj-note-metadata","memory.md#mem-obj-hunter-feedback","memory.md#mem-obj-source-hubs","memory.md#mem-obj-migration-backup","memory.md#mem-obj-hunter-raw"]
              note: "Operative retained parts reside in vault or adapter files; YAML encoding and dependency edges do not make a separate database or graph substrate."
          records: ["memory.md#mem-obj-note-content","memory.md#mem-obj-presupposition","memory.md#mem-obj-note-metadata","memory.md#mem-obj-hunter-feedback","memory.md#mem-obj-source-hubs","memory.md#mem-obj-migration-backup","memory.md#mem-obj-hunter-raw"]
          note: "The recorded vault object inventory establishes file storage for these parts."
        - scope: "Persisted plugin settings and run summary"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-plugin-settings"]
          note: "saveData/loadData establish persistence through the host, but the exact host backing substrate is not recorded; no file/database value is inferred."
      records: ["memory.md#mem-obj-note-content","memory.md#mem-obj-presupposition","memory.md#mem-obj-note-metadata","memory.md#mem-obj-hunter-feedback","memory.md#mem-obj-source-hubs","memory.md#mem-obj-migration-backup","memory.md#mem-obj-hunter-raw","memory.md#mem-obj-plugin-settings"]
      note: "Vault storage is classified; the settings backing store remains unresolved. Transient model results and reconstructed metadata/view caches are not additional durable stores; provider retention is outside the frozen memory boundary."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Note prose, U assertions/confidence, inline A/B fields, transcripts and historical body copies"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records: ["memory.md#mem-obj-note-content","memory.md#mem-obj-presupposition","memory.md#mem-obj-source-hubs","memory.md#mem-rte-inline-assumptions","memory.md#mem-obj-migration-backup"]
              note: "Models and humans interpret these assertions and conditionals; principle rules are not executable plugin rules."
          records: ["memory.md#mem-obj-note-content","memory.md#mem-obj-presupposition","memory.md#mem-obj-source-hubs","memory.md#mem-rte-inline-assumptions","memory.md#mem-obj-migration-backup"]
          note: "Inline assumptions are classified at their canonical route, without inventing the missing separate object declaration."
        - scope: "Types, statuses, identity/dependency/source addresses, exclusions, settings and copied frontmatter"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records: ["memory.md#mem-obj-note-metadata","memory.md#mem-obj-hunter-feedback","memory.md#mem-obj-plugin-settings","memory.md#mem-obj-source-hubs","memory.md#mem-obj-migration-backup"]
              note: "Fixed code rules consume localized configuration, selectors and addresses."
          records: ["memory.md#mem-obj-note-metadata","memory.md#mem-obj-hunter-feedback","memory.md#mem-obj-plugin-settings","memory.md#mem-obj-source-hubs","memory.md#mem-obj-migration-backup"]
          note: "Readable titles and source labels remain natural-language at human/model consumers, separate from their address use."
        - scope: "Readable titles/source labels and retained raw response display"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records: ["memory.md#mem-obj-note-metadata","memory.md#mem-obj-hunter-raw","runtime.md#rt-rte-assumption-admission"]
              note: "Human/model interpretation supplies meaning to labels and the raw debug display, not executable response dispatch."
          records: ["memory.md#mem-obj-note-metadata","memory.md#mem-obj-hunter-raw","runtime.md#rt-rte-assumption-admission"]
          note: "The saved debug block is readable response material; no opaque checkpoint or learned numerical payload is established."
        - scope: "Retained PDF binary original at the human source-access route"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-source-hubs"]
          note: "The accepted record establishes a binary attachment and manual accessibility but does not classify its operative internal representation. No controlled form is inferred merely from the PDF container."
      records: ["memory.md#mem-obj-note-content","memory.md#mem-obj-presupposition","memory.md#mem-obj-source-hubs","memory.md#mem-rte-inline-assumptions","memory.md#mem-obj-migration-backup","memory.md#mem-obj-note-metadata","memory.md#mem-obj-hunter-feedback","memory.md#mem-obj-plugin-settings","memory.md#mem-obj-hunter-raw","runtime.md#rt-rte-assumption-admission"]
      note: "Text and symbolic parts are classified; PDF binary internals remain unresolved. External model weights are excluded, not a retained parametric memory classification."
    lineage:
      assessment: "partial"
      units:
        - scope: "Shipped authoring, source acquisition and software derivation routes"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records: ["memory.md#mem-obj-note-content","memory.md#mem-obj-presupposition","memory.md#mem-rte-note-maintenance"]
              note: "User-supplied or edited note/assumption content is authored."
            - value: "imported"
              basis: "wired"
              records: ["memory.md#mem-obj-source-hubs","runtime.md#rt-rte-source-ingest"]
              note: "PDF source material and fetched/pasted transcripts enter from outside the plugin."
            - value: "other-compiled"
              basis: "wired"
              records: ["memory.md#mem-obj-note-content","memory.md#mem-obj-note-metadata","memory.md#mem-obj-migration-backup","memory.md#mem-obj-plugin-settings","runtime.md#rt-rte-source-ingest"]
              note: "Model extraction/proposal and deterministic templates, link union, settings updates and copies derive retained material from inputs; this is not automatically trace extraction."
          records: ["memory.md#mem-obj-note-content","memory.md#mem-obj-presupposition","memory.md#mem-rte-note-maintenance","memory.md#mem-obj-source-hubs","runtime.md#rt-rte-source-ingest","memory.md#mem-obj-note-metadata","memory.md#mem-obj-migration-backup","memory.md#mem-obj-plugin-settings"]
          note: "These are known derivation mechanisms, not authenticated origin histories of every existing note."
        - scope: "Initial contents of existing vault notes reused by mapping, maintenance or Hunter"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-note-content","memory.md#mem-obj-presupposition","runtime.md#rt-rte-assumption-admission"]
          note: "Existing notes are consumed, but real vault contents and their historical provenance are not frozen. Known shipped creation paths do not settle all initialization."
      records: ["memory.md#mem-obj-note-content","memory.md#mem-obj-presupposition","memory.md#mem-rte-note-maintenance","memory.md#mem-obj-source-hubs","runtime.md#rt-rte-source-ingest","memory.md#mem-obj-note-metadata","memory.md#mem-obj-migration-backup","memory.md#mem-obj-plugin-settings","runtime.md#rt-rte-assumption-admission"]
      note: "Supported authored/imported/derived paths coexist with unresolved existing-content provenance. No automatic trace-extracted behavioral artifact is established."
    behavioral_authority:
      assessment: "known"
      units:
        - scope: "Retained prose/titles at later model interpretation and human inspection"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records: ["memory.md#mem-obj-note-content","memory.md#mem-obj-presupposition","runtime.md#rt-rte-hunter-scan","runtime.md#rt-rte-assumption-admission","memory.md#mem-rte-retained-inspection"]
              note: "Bodies and titles supply comparison/mapping context and reference material; advice or IF/THEN subject matter is not standing host instruction."
          records: ["memory.md#mem-obj-note-content","memory.md#mem-obj-presupposition","runtime.md#rt-rte-hunter-scan","runtime.md#rt-rte-assumption-admission","memory.md#mem-rte-retained-inspection"]
          note: "Delivery is wired; actual semantic reliance and compliance remain unobserved."
        - scope: "Retained type/status/links/configuration at selectors, graph lookup and model dispatch"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records: ["memory.md#mem-obj-note-metadata","memory.md#mem-obj-plugin-settings","memory.md#mem-bap-dependency-display"]
              note: "Metadata determines eligibility, dependency destination/scope and configured backend/input budgets."
          records: ["memory.md#mem-obj-note-metadata","memory.md#mem-obj-plugin-settings","memory.md#mem-bap-dependency-display"]
          note: "Basename ambiguity and the U-prefix deletion qualification limit correctness, not the existence of these consumers."
        - scope: "Retained modification time at Hunter priority ordering"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records: ["runtime.md#rt-rte-hunter-scan"]
              note: "Retained file modification time controls newest-first input priority under the note cap."
          records: ["runtime.md#rt-rte-hunter-scan"]
          note: "This is fixed-code ranking input, not learned ranking policy."
        - scope: "Retained false-positive keys at Hunter's later result filter"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records: ["memory.md#mem-obj-hunter-feedback","runtime.md#rt-rte-pair-dismissal"]
              note: "The pair-key set is an admissibility criterion for returned candidates."
            - value: "enforcement"
              basis: "wired"
              records: ["memory.md#mem-obj-hunter-feedback","runtime.md#rt-bap-dismissal-filter"]
              note: "A matching key vetoes display independently of model confidence."
          records: ["memory.md#mem-obj-hunter-feedback","runtime.md#rt-rte-pair-dismissal","runtime.md#rt-bap-dismissal-filter"]
          note: "Human feedback has real exclusion force without parameter training or retained reasons."
      records: ["memory.md#mem-obj-note-content","memory.md#mem-obj-presupposition","runtime.md#rt-rte-hunter-scan","runtime.md#rt-rte-assumption-admission","memory.md#mem-rte-retained-inspection","memory.md#mem-obj-note-metadata","memory.md#mem-obj-plugin-settings","memory.md#mem-bap-dependency-display","memory.md#mem-obj-hunter-feedback","runtime.md#rt-rte-pair-dismissal","runtime.md#rt-bap-dismissal-filter"]
      note: "The recorded memory consumers support knowledge, routing, ranking, validation and enforcement. Static shipped prompt policy is excluded; neither human endorsement nor generated rule prose establishes learning/instruction authority at a durable update consumer."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Explicit note/content admission, edits, feedback and settings decisions"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "wired"
              records: ["runtime.md#rt-rte-free-input","runtime.md#rt-rte-source-ingest","runtime.md#rt-rte-rule-admission","runtime.md#rt-rte-assumption-admission","runtime.md#rt-rte-pair-dismissal","memory.md#mem-rte-inline-assumptions","memory.md#mem-rte-note-maintenance","memory.md#mem-obj-hunter-raw","memory.md#mem-obj-plugin-settings"]
              note: "Human submit/select/edit/dismiss/save decisions approve the retained content or batch; authorship by a model does not make these admissions automatic."
          records: ["runtime.md#rt-rte-free-input","runtime.md#rt-rte-source-ingest","runtime.md#rt-rte-rule-admission","runtime.md#rt-rte-assumption-admission","runtime.md#rt-rte-pair-dismissal","memory.md#mem-rte-inline-assumptions","memory.md#mem-rte-note-maintenance","memory.md#mem-obj-hunter-raw","memory.md#mem-obj-plugin-settings"]
          note: "These are actual decision interfaces, not an assumption that every physical write needs individual approval."
        - scope: "Derived hub replacement, dependency unions, backup copying and run/settings metadata"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records: ["memory.md#mem-obj-source-hubs","memory.md#mem-obj-note-metadata","memory.md#mem-obj-migration-backup","memory.md#mem-obj-plugin-settings","runtime.md#rt-rte-schema-migration"]
              note: "Software chooses/adopts these derived contents without a separate per-content human decision; workflow initiation is not that decision."
          records: ["memory.md#mem-obj-source-hubs","memory.md#mem-obj-note-metadata","memory.md#mem-obj-migration-backup","memory.md#mem-obj-plugin-settings","runtime.md#rt-rte-schema-migration"]
          note: "Manual approval of a migration or concept batch is distinct from automatic admission of backup strings, hubs and derived addresses."
        - scope: "Admission of pre-existing vault content"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-note-content","memory.md#mem-obj-presupposition"]
          note: "No actual historical vault admission record is supplied; editable text does not establish human approval of every pre-existing entry."
      records: ["runtime.md#rt-rte-free-input","runtime.md#rt-rte-source-ingest","runtime.md#rt-rte-rule-admission","runtime.md#rt-rte-assumption-admission","runtime.md#rt-rte-pair-dismissal","memory.md#mem-rte-inline-assumptions","memory.md#mem-rte-note-maintenance","memory.md#mem-obj-hunter-raw","memory.md#mem-obj-plugin-settings","memory.md#mem-obj-source-hubs","memory.md#mem-obj-note-metadata","memory.md#mem-obj-migration-backup","runtime.md#rt-rte-schema-migration","memory.md#mem-obj-note-content","memory.md#mem-obj-presupposition"]
      note: "Current shipped manual and software admission mechanisms are supported; historical initialization control remains unresolved."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Existing-note editing, inline replacement, hub overwrite and lifecycle withdrawal"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records: ["memory.md#mem-rte-note-maintenance","memory.md#mem-rte-inline-assumptions","runtime.md#rt-rte-rule-admission","memory.md#mem-obj-source-hubs"]
              note: "Implemented routes revise retained fields/bodies or replace a retained hub."
            - value: "invalidate"
              basis: "wired"
              records: ["memory.md#mem-rte-note-maintenance","epistemic.md#epi-rte-collapse-review","runtime.md#rt-rte-rule-admission"]
              note: "Resolve/archive changes current eligibility while retaining text/history; undermining withdraws the assumption's status, not its dependent principles."
          records: ["memory.md#mem-rte-note-maintenance","memory.md#mem-rte-inline-assumptions","runtime.md#rt-rte-rule-admission","memory.md#mem-obj-source-hubs","epistemic.md#epi-rte-collapse-review"]
          note: "These transformations are wired, without implying empirically justified withdrawal."
        - scope: "Requested extraction of standalone source concepts"
          assessment: "partial"
          findings:
            - value: "consolidate"
              basis: "claimed"
              records: ["runtime.md#rt-rte-source-ingest","epistemic.md#epi-clm-source-fidelity"]
              note: "Faithful reduced source claims are requested; semantic preservation of actual generated concepts is not established."
          records: ["runtime.md#rt-rte-source-ingest","epistemic.md#epi-clm-source-fidelity"]
          note: "Extraction wiring is inspected, but no paired source/output settles whether particular admitted text only compresses existing claims."
        - scope: "Meaning relation of generated principles and implicit assumptions"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-rule-admission","runtime.md#rt-rte-assumption-admission","memory.md#mem-rte-inline-assumptions"]
          note: "Hypothesis/proposal generation has no paired instance establishing a new claim absent from inputs; synthesis is not inferred from generation alone."
      records: ["memory.md#mem-rte-note-maintenance","memory.md#mem-rte-inline-assumptions","runtime.md#rt-rte-rule-admission","memory.md#mem-obj-source-hubs","epistemic.md#epi-rte-collapse-review","runtime.md#rt-rte-source-ingest","epistemic.md#epi-clm-source-fidelity","runtime.md#rt-rte-assumption-admission"]
      note: "Known revisions/withdrawals and requested consolidation do not resolve all semantic transformations. Link union, schema translation, backups and merge-without-body-copy do not themselves establish deduplication or semantic consolidation; no tier promotion or decay is inferred."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Requested Hunter, mapping, elevation, classification/title calls, file inspection and explicit backup restore"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records: ["runtime.md#rt-rte-hunter-scan","runtime.md#rt-rte-assumption-admission","runtime.md#rt-rte-rule-admission","memory.md#mem-rte-inline-assumptions","memory.md#mem-rte-note-maintenance","memory.md#mem-rte-retained-inspection","runtime.md#rt-rte-schema-migration"]
              note: "Users request these consumers and code fulfills them with retained material. Selection/truncation inside the requested batch is not another unsolicited push."
          records: ["runtime.md#rt-rte-hunter-scan","runtime.md#rt-rte-assumption-admission","runtime.md#rt-rte-rule-admission","memory.md#mem-rte-inline-assumptions","memory.md#mem-rte-note-maintenance","memory.md#mem-rte-retained-inspection","runtime.md#rt-rte-schema-migration"]
          note: "Known pull includes recovery and human navigation, not only backend delivery."
        - scope: "Host-event-triggered retained-note summary refresh in open human-facing views"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records: ["memory.md#mem-rte-retained-inspection"]
              note: "Host events trigger automatic reloading, selection and delivery of retained-note summaries to the human without a new request for that material."
          records: ["memory.md#mem-rte-retained-inspection"]
          note: "Opening a view requests initial access; subsequent event-triggered supply is a separate automatic delivery operation. Human consumption is included, even without agent-context injection."
        - scope: "Persisted settings reload and dismissal control consumption"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-rte-retained-inspection","memory.md#mem-obj-plugin-settings","memory.md#mem-obj-hunter-feedback"]
          note: "Startup reloads configuration and later filters consume dismissal keys, but the records do not separately resolve requested versus unsolicited delivery on these control-consumption operations. These local limits do not qualify the established human-refresh push route."
      records: ["runtime.md#rt-rte-hunter-scan","runtime.md#rt-rte-assumption-admission","runtime.md#rt-rte-rule-admission","memory.md#mem-rte-inline-assumptions","memory.md#mem-rte-note-maintenance","memory.md#mem-rte-retained-inspection","runtime.md#rt-rte-schema-migration","memory.md#mem-obj-plugin-settings","memory.md#mem-obj-hunter-feedback"]
      note: "Requested content/recovery routes support pull; event-triggered human-facing refresh supports push. Settings reload and dismissal-control consumption remain locally unresolved, so the inventory remains partial. Provider-side retention is excluded, not declared absent."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Automatic type/status/layer and view-filter selection during host-event-triggered human-facing refresh"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records: ["memory.md#mem-rte-retained-inspection"]
              note: "Host events trigger refresh; retained type/status metadata, enabled layers and view filters select note labels, relationship summaries, counts and issues supplied to the human. These are category/view predicates, not semantic query matching."
          records: ["memory.md#mem-rte-retained-inspection"]
          note: "Classifies the recorded automatic view-selection operation. Dependency addresses describe relationships; their presence alone does not establish an additional identity-targeted push selector."
        - scope: "Selection on persisted settings reload and dismissal-control consumption"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-rte-retained-inspection","memory.md#mem-obj-plugin-settings","memory.md#mem-obj-hunter-feedback"]
          note: "The control-consumption alternatives lack a separately resolved push-delivery operation and selected payload. Exact dismissal matching selects vetoes, not delivered memory parts; it does not determine the signal on the human-refresh route."
        - scope: "Explicitly requested content and restore routes"
          assessment: "inapplicable"
          findings: []
          records: ["runtime.md#rt-rte-hunter-scan","runtime.md#rt-rte-assumption-admission","runtime.md#rt-rte-schema-migration"]
          note: "These local routes are pull; push signal is inapplicable locally. Type/status/mtime and focus inputs do not turn the requested return into identifier push."
      records: ["memory.md#mem-rte-retained-inspection","memory.md#mem-obj-plugin-settings","memory.md#mem-obj-hunter-feedback","runtime.md#rt-rte-hunter-scan","runtime.md#rt-rte-assumption-admission","runtime.md#rt-rte-schema-migration"]
      note: "Automatic human-facing refresh supports coarse selection. Requested pull routes have locally inapplicable push signals; settings/control alternatives remain unresolved. Those alternatives prevent complete coverage without erasing the supported refresh signal."
    trace_learning:
      assessment: "not-determinable"
      units:
        - scope: "Note transformations, human feedback, diagnostics and run/settings summaries"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-source-ingest","runtime.md#rt-rte-pair-dismissal","memory.md#mem-obj-hunter-raw","memory.md#mem-obj-plugin-settings","memory.md#mem-rte-note-maintenance"]
          note: "No accepted evidenced-absence record warrants a known local no. Human dismissal is explicit admission; source extraction is not operational-experience learning; raw output and counters alone do not establish automatic trace-fed behavioral artifacts."
      records: ["runtime.md#rt-rte-source-ingest","runtime.md#rt-rte-pair-dismissal","memory.md#mem-obj-hunter-raw","memory.md#mem-obj-plugin-settings","memory.md#mem-rte-note-maintenance"]
      note: "No qualifying automatic trace-fed write/later-consumer chain is established in the accepted records. Their bounded lack of establishment is not an evidenced absence; neither yes nor no is asserted. External provider learning and human learning are excluded."
    trace_source:
      assessment: "not-determinable"
      units:
        - scope: "Potential trace-fed retained updates within the plugin memory boundary"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-hunter-raw","memory.md#mem-obj-plugin-settings","runtime.md#rt-rte-pair-dismissal","runtime.md#rt-rte-source-ingest"]
          note: "Debug responses and run metadata have trace-like origins, but no qualifying automatic learning write is established. Source transcripts are imported source content, not plugin session logs by serialization alone."
      records: ["memory.md#mem-obj-hunter-raw","memory.md#mem-obj-plugin-settings","runtime.md#rt-rte-pair-dismissal","runtime.md#rt-rte-source-ingest"]
      note: "No qualifying write has a supported original trace-source classification. Inapplicability would require completely assessed bounded absence of trace learning, which these records do not provide."
---

# Antinomia memory profile

## Comparison rationale

This profile classifies accepted records, not a live vault. Wiring establishes a consumer path, not successful semantic reliance, improved capacity or observed operation. Settings identifiers do not establish immutable model weights. A dependency graph encoded in YAML is a symbolic access structure over files, not evidence of a graph storage service.

The reconciliation supersedes the epistemic inline-assumption route with [MEM-RTE-inline-assumptions](memory.md#mem-rte-inline-assumptions), and the epistemic seeded-measurement claim with [MEM-CLM-evaluation-key](memory.md#mem-clm-evaluation-key). This profile uses those canonical destinations. The evaluation key is not a production trace-fed update consumer. Narrower epistemic objects remain compatible with the broader memory objects; they are not silently substituted for them.

Two unresolved reconciliation issues are kept bounded. The U-prefix deletion condition in [MEM-OBJ-note-metadata](memory.md#mem-obj-note-metadata) and [EPI-RTE-collapse-review](epistemic.md#epi-rte-collapse-review) prevents a universal dependency-cleanup assurance; it does not erase the retained link/routing path. Inline A/B content lacks a separately declared operative-object part in the combined epistemic inventory. Its storage, edits and later modal/Hunter consumers are explicitly recorded by [MEM-RTE-inline-assumptions](memory.md#mem-rte-inline-assumptions), which supports the local classification without inventing that missing declaration or claiming a repaired object inventory.

Human admission and software derivation are separate mechanisms. Human batch selection admits concepts; code separately constructs hubs and backup copies. A human's command initiation is not per-content approval of every derived write. Historical admission of existing vault notes remains unresolved. See [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [MEM-OBJ-source-hubs](memory.md#mem-obj-source-hubs), [MEM-OBJ-migration-backup](memory.md#mem-obj-migration-backup) and [MEM-OBJ-note-content](memory.md#mem-obj-note-content).

Read-back distinguishes operations, not human versus agent consumers. Hunter's automatic type/recency/cap selection fulfills a requested scan; it does not establish a second push merely because code chooses inputs. Initial human view opening likewise requests inspection. Later host-event-triggered refresh automatically reloads retained notes, applies type/status/layer and view filters, and supplies summaries to the human without a new request. That operation supports wired push with coarse selection even though it is not agent-context injection. Settings reload and dismissal-control consumption remain separate unresolved alternatives, keeping both axes partial. Frontmatter dismissal keys select output vetoes, not delivered memory parts, so exact pair matching supplies no identifier push finding. See [RT-RTE-hunter-scan](runtime.md#rt-rte-hunter-scan), [MEM-RTE-retained-inspection](memory.md#mem-rte-retained-inspection), [MEM-OBJ-plugin-settings](memory.md#mem-obj-plugin-settings), [MEM-OBJ-hunter-feedback](memory.md#mem-obj-hunter-feedback) and [RT-BAP-dismissal-filter](runtime.md#rt-bap-dismissal-filter).

Curation is not epistemic warrant. Requested faithful extraction supports a claimed consolidation mechanism, while the accepted epistemic account leaves actual concept meaning indeterminate. Generated principles and assumptions do not by themselves establish synthesis. The wired replacement and lifecycle-withdrawal operations remain supported independently. See [EPI-CLM-source-fidelity](epistemic.md#epi-clm-source-fidelity), [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), [MEM-RTE-note-maintenance](memory.md#mem-rte-note-maintenance) and [EPI-RTE-collapse-review](epistemic.md#epi-rte-collapse-review).

No member declares an evidenced absence. Accordingly the trace-learning axis cannot encode a known local negative, and trace source cannot be made inapplicable by a narrative that no qualifying rewrite was established. Raw diagnostics, counters and manually admitted feedback do not establish an automatic trace-fed durable behavior-shaping artifact. This is a limit on classification, not a claim about provider learning or human improvement. See [MEM-OBJ-hunter-raw](memory.md#mem-obj-hunter-raw), [MEM-OBJ-plugin-settings](memory.md#mem-obj-plugin-settings) and [RT-RTE-pair-dismissal](runtime.md#rt-rte-pair-dismissal).

Source-read log: no frozen-source reads were needed. This mapping uses only the handed members and governing contracts; it adds no records or evidence.

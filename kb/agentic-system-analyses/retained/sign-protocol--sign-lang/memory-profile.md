---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "SIGN memory comparison of maintained canon sources and compilation products, bounded before external agent execution."
run-id: "AAS-2026-11-09-sign-lang-379ffbdd642c-01"
source-identity: "https://github.com/sign-protocol/sign-lang"
reviewed-boundary: "f4eb1a82b114615754bbe5c2e6f4255a4ec1eeba"
memory-comparison:
  version: 2
  scope: "Caller-maintained canon sources, compiler-replaced index and raw bundle, and their manifest/checksum access metadata, with the documented external later-consumer role. Classification concerns retained content changed through authoring/compilation use, not evidence of agent-acquired episodic memory. Excludes static toolchain code, static skill-reference instructions as memory, transient parsed objects/diagnostics, and external importer, drafting and enclosing-host internals."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        -
          scope: "Maintained canon source files, including repository-hosted canon"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-canon-source"
              note: "The parser consumes caller-selected filesystem sources."
            -
              value: "repo"
              basis: "wired"
              records:
                - "memory.md#mem-obj-canon-source"
              note: "The shipped canon demonstrates repository-hosted source storage, not an experience-generation history."
          records:
            - "memory.md#mem-obj-canon-source"
          note: "Both locations are explicit; a repository is not a graph database."
        -
          scope: "Compiler-retained index, raw bundle, manifest and checksum"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-canon-index"
                - "memory.md#mem-obj-canon-bundle"
                - "memory.md#mem-obj-canon-manifest"
                - "memory.md#mem-obj-bundle-checksum"
                - "runtime.md#rt-rte-compile-canon"
              note: "Four named filesystem products are persisted and replaced by compilation."
          records:
            - "memory.md#mem-obj-canon-index"
            - "memory.md#mem-obj-canon-bundle"
            - "memory.md#mem-obj-canon-manifest"
            - "memory.md#mem-obj-bundle-checksum"
            - "runtime.md#rt-rte-compile-canon"
          note: "No provider-resident payload is included in this artifact boundary."
      records:
        - "memory.md#mem-obj-canon-source"
        - "memory.md#mem-obj-canon-index"
        - "memory.md#mem-obj-canon-bundle"
        - "memory.md#mem-obj-canon-manifest"
        - "memory.md#mem-obj-bundle-checksum"
        - "runtime.md#rt-rte-compile-canon"
      note: "Complete storage classification of the named source and output inventory, not of an excluded host or importer."
    representational_form:
      assessment: "known"
      units:
        -
          scope: "Source and bundle prose interpreted by a human or intended agent"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-canon-source"
                - "memory.md#mem-obj-canon-bundle"
              note: "Source-written definitions, explanations and rule prose survive raw bundling; this does not establish later model consumption."
          records:
            - "memory.md#mem-obj-canon-source"
            - "memory.md#mem-obj-canon-bundle"
          note: "Classifies retained encoding separately from actual delivery."
        -
          scope: "Index source-authored summaries"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-canon-index"
              note: "The compiler copies the summary slot rather than generating prose."
          records:
            - "memory.md#mem-obj-canon-index"
          note: "Natural-language summaries are distinct from symbolic locator fields."
        -
          scope: "Source/bundle SIGN framing and index locators; manifest and checksum"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-canon-source"
                - "memory.md#mem-obj-canon-index"
                - "memory.md#mem-obj-canon-bundle"
                - "memory.md#mem-obj-canon-manifest"
                - "memory.md#mem-obj-bundle-checksum"
              note: "Localized sigils, identities, links, status, anchor patterns and build values have fixed parser/compiler meanings."
          records:
            - "memory.md#mem-obj-canon-source"
            - "memory.md#mem-obj-canon-index"
            - "memory.md#mem-obj-canon-bundle"
            - "memory.md#mem-obj-canon-manifest"
            - "memory.md#mem-obj-bundle-checksum"
          note: "The raw corpus is not an executed inference graph or distributed-parametric memory."
      records:
        - "memory.md#mem-obj-canon-source"
        - "memory.md#mem-obj-canon-index"
        - "memory.md#mem-obj-canon-bundle"
        - "memory.md#mem-obj-canon-manifest"
        - "memory.md#mem-obj-bundle-checksum"
      note: "Mixed prose and symbolic material are split by operative part; no model weights or embedding payload belongs to this inventory."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Index projection, raw bundle assembly and generated build metadata"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-canon-index"
                - "memory.md#mem-obj-canon-bundle"
                - "memory.md#mem-obj-canon-manifest"
                - "memory.md#mem-obj-bundle-checksum"
                - "runtime.md#rt-rte-compile-canon"
              note: "Code projects fields, assembles raw files and derives metadata/hash from supplied source."
          records:
            - "memory.md#mem-obj-canon-index"
            - "memory.md#mem-obj-canon-bundle"
            - "memory.md#mem-obj-canon-manifest"
            - "memory.md#mem-obj-bundle-checksum"
            - "runtime.md#rt-rte-compile-canon"
          note: "Known subsequent transformation does not settle source acquisition."
        -
          scope: "Initial admission and derivation of caller-supplied canon content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-canon-source"
          note: "Source is authored outside compilation; the records do not establish the original authoring/import/trace derivation path. A shipped instance does not settle provenance."
      records:
        - "memory.md#mem-obj-canon-source"
        - "memory.md#mem-obj-canon-index"
        - "memory.md#mem-obj-canon-bundle"
        - "memory.md#mem-obj-canon-manifest"
        - "memory.md#mem-obj-bundle-checksum"
        - "runtime.md#rt-rte-compile-canon"
      note: "Compiled lineage is supported. Initial content provenance remains unresolved; the external importer and external drafting implementation are excluded, not silently classified as imported or authored."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Index orientation and full canon at the documented external agent consumer"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-canon-source"
                - "memory.md#mem-obj-canon-index"
                - "memory.md#mem-obj-canon-bundle"
                - "memory.md#mem-rte-canon-delivery"
              note: "Summaries and descriptive domain content supply intended reference/context through the documented host delivery role."
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-canon-source"
                - "memory.md#mem-obj-canon-index"
                - "memory.md#mem-obj-canon-bundle"
                - "memory.md#mem-rte-canon-delivery"
              note: "Rule and standards prose supplies intended directions to the external agent; no compliance or tool-action enforcement is established."
          records:
            - "memory.md#mem-obj-canon-source"
            - "memory.md#mem-obj-canon-index"
            - "memory.md#mem-obj-canon-bundle"
            - "memory.md#mem-rte-canon-delivery"
            - "runtime.md#rt-bap-canon-guidance"
          note: "These values concern the afforded interpretation channel, not wired model use."
        -
          scope: "Retained source status, identities and anchor patterns at deterministic selection consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-canon-source"
                - "runtime.md#rt-rte-compile-canon"
                - "runtime.md#rt-rte-source-signals"
              note: "Active identity fields select compiler projections and contributing files; anchor patterns select governed paths for maintenance computations."
          records:
            - "memory.md#mem-obj-canon-source"
            - "runtime.md#rt-rte-compile-canon"
            - "runtime.md#rt-rte-source-signals"
          note: "Force is selection of scope/input, not semantic enforcement of domain rules."
        -
          scope: "Manifest/checksum and actual host-returned full-document content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-canon-manifest"
            - "memory.md#mem-obj-bundle-checksum"
            - "memory.md#mem-obj-canon-bundle"
            - "memory.md#mem-rte-canon-delivery"
          note: "No later metadata verifier is established; host getDoc splitting/filtering and actual delivered payload are unresolved. Integrity availability is not a wired validation/enforcement authority."
      records:
        - "memory.md#mem-obj-canon-source"
        - "memory.md#mem-obj-canon-index"
        - "memory.md#mem-obj-canon-bundle"
        - "memory.md#mem-obj-canon-manifest"
        - "memory.md#mem-obj-bundle-checksum"
        - "memory.md#mem-rte-canon-delivery"
        - "runtime.md#rt-bap-canon-guidance"
        - "runtime.md#rt-rte-compile-canon"
        - "runtime.md#rt-rte-source-signals"
      note: "Afforded guidance and wired structural routing coexist. Missing metadata consumers and host payload semantics prevent complete authority coverage; static validator code is not retained memory criteria."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Compiler admission and replacement of its four products"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-compile-canon"
              note: "Fixed software checks admit and replace outputs without a per-content human approval decision."
          records:
            - "runtime.md#rt-rte-compile-canon"
          note: "Starting compilation is not manual admission of every output."
        -
          scope: "Source content supply, editing and initial approval"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-canon-source"
          note: "Caller identity and outside-compilation authoring do not establish an explicit human content decision or an automatic authoring mechanism."
      records:
        - "memory.md#mem-obj-canon-source"
        - "runtime.md#rt-rte-compile-canon"
      note: "Known automatic compilation does not resolve the independent initial-content admission mechanism."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Index field selection and anchor compression over retained source"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-canon-index"
                - "runtime.md#rt-rte-compile-canon"
              note: "The reduced index selects existing identities, links and source-authored summaries; anchors omit exclusions and cap distinct include patterns."
          records:
            - "memory.md#mem-obj-canon-index"
            - "runtime.md#rt-rte-compile-canon"
          note: "This is reduction of existing content, not novel synthesis or model summarization."
        -
          scope: "Raw bundle replacement, source maintenance and metadata generation"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-canon-bundle"
            - "memory.md#mem-obj-canon-manifest"
            - "memory.md#mem-obj-bundle-checksum"
            - "runtime.md#rt-rte-compile-canon"
            - "runtime.md#rt-rte-source-signals"
            - "runtime.md#rt-rte-corpus-diff"
          note: "Raw concatenation, fixed-filename replacement, hash generation and transient maintenance signals do not establish a controlled curation transformation. No recorded content-edit mechanism resolves source evolution, deduplication or withdrawal; mixed-status passthrough defeats universal invalidation."
      records:
        - "memory.md#mem-obj-canon-index"
        - "memory.md#mem-obj-canon-bundle"
        - "memory.md#mem-obj-canon-manifest"
        - "memory.md#mem-obj-bundle-checksum"
        - "runtime.md#rt-rte-compile-canon"
        - "runtime.md#rt-rte-source-signals"
        - "runtime.md#rt-rte-corpus-diff"
      note: "Index consolidation is supported; remaining maintenance surfaces cannot be upgraded from signal/overwrite labels to curation values. No bounded absence record warrants absent operations."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Documented whole-index supply and requested document return"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-canon-delivery"
                - "runtime.md#rt-bap-canon-guidance"
                - "memory.md#mem-obj-canon-index"
              note: "Host prompt assembly supplies the whole compiled index at each intended invocation without a request for that material."
            -
              value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-canon-delivery"
                - "memory.md#mem-obj-canon-bundle"
              note: "The agent requests get_canon_doc(id); fulfilling that request is pull, not an additional push."
          records:
            - "memory.md#mem-rte-canon-delivery"
            - "runtime.md#rt-bap-canon-guidance"
            - "memory.md#mem-obj-canon-index"
            - "memory.md#mem-obj-canon-bundle"
          note: "A named host consumer role supports affordance only."
        -
          scope: "Other retained metadata and actual host delivery alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-canon-manifest"
            - "memory.md#mem-obj-bundle-checksum"
            - "memory.md#mem-rte-canon-delivery"
          note: "No subsequent metadata consumer is established; actual resolver delivery, filtering and reload/cache behavior are unspecified."
      records:
        - "memory.md#mem-rte-canon-delivery"
        - "runtime.md#rt-bap-canon-guidance"
        - "memory.md#mem-obj-canon-index"
        - "memory.md#mem-obj-canon-bundle"
        - "memory.md#mem-obj-canon-manifest"
        - "memory.md#mem-obj-bundle-checksum"
      note: "Both directions are afforded within one chain. Missing implementation and metadata consumption facts preclude complete inventory coverage; no deployed read-back is observed."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Per-invocation whole-index push in the documented host contract"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-canon-delivery"
                - "runtime.md#rt-bap-canon-guidance"
                - "memory.md#mem-obj-canon-index"
              note: "Trigger is an agent invocation; host assembly selects the complete compiled index by availability, not task matching or relevance."
          records:
            - "memory.md#mem-rte-canon-delivery"
            - "runtime.md#rt-bap-canon-guidance"
            - "memory.md#mem-obj-canon-index"
          note: "Document IDs used by the requested full-document lookup are not targeted push signals."
        -
          scope: "Actual host selectors and any later metadata delivery"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-canon-delivery"
            - "memory.md#mem-obj-canon-manifest"
            - "memory.md#mem-obj-bundle-checksum"
          note: "No deployed host selector or metadata delivery route is established. This does not justify inferred judgment, lexical, embedding or identifier push values."
      records:
        - "memory.md#mem-rte-canon-delivery"
        - "runtime.md#rt-bap-canon-guidance"
        - "memory.md#mem-obj-canon-index"
        - "memory.md#mem-obj-canon-manifest"
        - "memory.md#mem-obj-bundle-checksum"
      note: "Coarse whole-index supply is afforded. Unresolved consumer routes prevent complete push-selector coverage and cannot be labeled pull-only inapplicable."
    trace_learning:
      assessment: "not-determinable"
      units:
        -
          scope: "Source admission, compilation and documented later canon use"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-canon-source"
            - "runtime.md#rt-rte-compile-canon"
            - "memory.md#mem-rte-canon-delivery"
          note: "The records establish no trace-fed source write and later behavior-shaping consumer chain. Initial derivation is unresolved, while compilation consumes supplied source, not evidenced session/tool experience. No evidenced-absence record supports a local no."
      records:
        - "memory.md#mem-obj-canon-source"
        - "runtime.md#rt-rte-compile-canon"
        - "memory.md#mem-rte-canon-delivery"
      note: "Neither a qualifying positive nor a bounded negative is supported by accepted records. Static shipped canon and repeated loading do not establish trace learning; excluded host/importer behavior is not a negative."
    trace_source:
      assessment: "not-determinable"
      units:
        -
          scope: "Original inputs to any qualifying trace-fed canon write"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-canon-source"
            - "runtime.md#rt-rte-compile-canon"
            - "memory.md#mem-rte-canon-delivery"
          note: "No qualifying trace-fed write is established and original source provenance remains unresolved. Git comparison inputs alone do not establish a learning route or a trace source."
      records:
        - "memory.md#mem-obj-canon-source"
        - "runtime.md#rt-rte-compile-canon"
        - "memory.md#mem-rte-canon-delivery"
      note: "No original trace input can be classified. Inapplicable would require a bounded completely assessed absence of trace learning, which the records do not supply."
---

# sign-lang memory profile

## Comparison rationale

The inventory is the maintained canon and its persisted replacement products, not all storage in SIGN. The source record describes caller-maintained files; the compile route establishes deterministic replacement of derived files. The shipped corpus is evidence of an available source instance, not a history of learning. Static authoring guidance and executable validator rules are excluded as memory; merely reusing shipped instructions would not establish accumulation through use. See [MEM-OBJ-canon-source](memory.md#mem-obj-canon-source), [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon) and [MEM-OBJ-skill-reference](memory.md#mem-obj-skill-reference).

The reconciliation supersedes the epistemic source, index and bundle records with their memory counterparts. All classifications cite those canonical memory objects. The epistemic combined manifest/checksum remains a valid aggregate, not a superseded competing object; this profile uses the separately declared memory parts. Infer blocks and edge-provenance text remain source parts, not independently learned stores. See [MEM-OBJ-canon-source](memory.md#mem-obj-canon-source), [MEM-OBJ-canon-index](memory.md#mem-obj-canon-index), [MEM-OBJ-canon-bundle](memory.md#mem-obj-canon-bundle), [MEM-OBJ-canon-manifest](memory.md#mem-obj-canon-manifest), [MEM-OBJ-bundle-checksum](memory.md#mem-obj-bundle-checksum), [EPI-OBJ-infer](epistemic.md#epi-obj-infer) and [EPI-OBJ-edge-provenance](epistemic.md#epi-obj-edge-provenance).

Index reduction warrants consolidation, even though its prose summary was supplied by the source author. It does not warrant synthesis. Raw bundle assembly and sequential replacement do not by themselves establish evolution, deduplication or invalidation: inactive bytes can remain in a contributing mixed-status file, and already-loaded host material is not revoked. Maintenance commands return signals rather than revised retained knowledge. See [MEM-OBJ-canon-index](memory.md#mem-obj-canon-index), [MEM-OBJ-canon-bundle](memory.md#mem-obj-canon-bundle), [RT-RTE-source-signals](runtime.md#rt-rte-source-signals) and [RT-RTE-corpus-diff](runtime.md#rt-rte-corpus-diff).

The documented host route affords instruction and knowledge, with coarse whole-index push followed by requested full-document pull. An ID in that pull does not establish identifier-based push. The same illustrative contract supports these findings; it is not several independent witnesses of deployed consumption. Host parsing, filtering and cache policy remain unresolved. Symbolic source fields separately route deterministic compilation and maintenance; they do not make domain constraints action-enforcing. Metadata has no established later verifier, so byte hashes do not warrant a memory validation/enforcement value. See [MEM-RTE-canon-delivery](memory.md#mem-rte-canon-delivery), [RT-BAP-canon-guidance](runtime.md#rt-bap-canon-guidance), [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon), [RT-RTE-source-signals](runtime.md#rt-rte-source-signals) and [MEM-OBJ-bundle-checksum](memory.md#mem-obj-bundle-checksum).

Software admission establishes automatic output replacement, not manual source approval. Missing initial derivation and approval facts remain local unknowns. No accepted evidenced-absence record warrants a trace-learning negative, and no trace-fed durable behavior-shaping write warrants a positive. Accordingly neither trace-learning nor trace-source receives a controlled finding; this is not an assertion that excluded external systems lack learning. No observed activation, improvement or causal benefit is inferred. See [MEM-OBJ-canon-source](memory.md#mem-obj-canon-source), [RT-RTE-compile-canon](runtime.md#rt-rte-compile-canon) and [MEM-RTE-canon-delivery](memory.md#mem-rte-canon-delivery).

Source-read log: none. This classification used the supplied accepted members and reconciliation only; no source ambiguity required a direct frozen-source read.

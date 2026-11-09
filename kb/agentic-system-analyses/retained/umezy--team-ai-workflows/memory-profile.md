---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Memory profile of team-ai-workflows: repository corpus, mutable skill content and retained access metadata at the frozen template boundary."
run-id: "AAS-2026-11-09-team-ai-workflows-c00fb85f7ed1-01"
source-identity: "https://github.com/umezy/team-ai-workflows"
reviewed-boundary: "9aebd7a6c2803da450904eb5621ae5439508ff94"
memory-comparison:
  version: 2
  scope: "Shipped retained sources Markdown, use-revisable repository skill content, installed access references and root configuration, with their editing, synchronization and later-consumer routes. Includes configured-root alternatives and unresolved host discovery of these retained parts. Excludes unchanged static setup/search code as memory payload, temporary results and answers without a shipped retention route, external host session memory and provider parameters, and future adopter-added mechanisms."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        -
          scope: "Retained corpus and mutable repository skill content"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-sources"
                - "runtime.md#rt-obj-docs-grep"
                - "runtime.md#rt-rte-knowledge-search"
              note: "Search reads Markdown files; later linked instruction content remains filesystem text."
            -
              value: "repo"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-sources"
                - "runtime.md#rt-rte-repository-admission"
              note: "Git-tracked content is the documented team replacement and distribution surface."
          records:
            - "memory.md#mem-obj-sources"
            - "runtime.md#rt-obj-docs-grep"
            - "runtime.md#rt-rte-knowledge-search"
            - "runtime.md#rt-rte-repository-admission"
          note: "Both repository payload types are covered; the alternative configured corpus remains files, without an asserted repository identity."
        -
          scope: "Installed access metadata: skill links and root configuration"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-skill-links"
                - "runtime.md#rt-rte-skill-sync"
              note: "Synchronizer creates filesystem references, not copied knowledge."
            -
              value: "files"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-team-workflows-dir"
                - "runtime.md#rt-rte-machine-setup"
              note: "Setup requests persistent host settings; the process environment is a later copy, not an additional durable store."
          records:
            - "runtime.md#rt-obj-skill-links"
            - "runtime.md#rt-rte-skill-sync"
            - "memory.md#mem-obj-team-workflows-dir"
            - "runtime.md#rt-rte-machine-setup"
          note: "Covers the shipped access structures; deployed values and successful installation are not observed."
      records:
        - "memory.md#mem-obj-sources"
        - "runtime.md#rt-obj-docs-grep"
        - "runtime.md#rt-rte-knowledge-search"
        - "runtime.md#rt-rte-repository-admission"
        - "runtime.md#rt-obj-skill-links"
        - "runtime.md#rt-rte-skill-sync"
        - "memory.md#mem-obj-team-workflows-dir"
        - "runtime.md#rt-rte-machine-setup"
      note: "Known within the shipped file/repository memory boundary. Transient result lists, host session state and provider parameters are excluded, not inferred to be absent."
    representational_form:
      assessment: "known"
      units:
        -
          scope: "Corpus content consumed as reference by the answer model"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-sources"
                - "memory.md#mem-bap-corpus-answer"
              note: "Assertions, tips and API examples supply interpreted reference content; code-like names are not executed by search."
          records:
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-bap-corpus-answer"
          note: "Sample assertions and reasons are readable; this does not validate their truth."
        -
          scope: "Retained skill procedure interpreted by the host"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-docs-grep"
                - "runtime.md#rt-bap-user-skills"
              note: "The model interprets query and answer directions."
          records:
            - "runtime.md#rt-obj-docs-grep"
            - "runtime.md#rt-bap-user-skills"
          note: "Covers the procedural text, distinct from its embedded command."
        -
          scope: "Embedded command executed through host tool use"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-docs-grep"
                - "runtime.md#rt-rte-knowledge-search"
              note: "The shell consumes the embedded command under the instructed workflow; execution is unobserved."
          records:
            - "runtime.md#rt-obj-docs-grep"
            - "runtime.md#rt-rte-knowledge-search"
          note: "Command consumption is separate from natural-language interpretation."
        -
          scope: "Link references and root-location metadata"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-skill-links"
                - "memory.md#mem-obj-team-workflows-dir"
                - "runtime.md#rt-rte-skill-sync"
              note: "Fixed filesystem and root-resolution rules consume paths rather than interpret prose."
          records:
            - "runtime.md#rt-obj-skill-links"
            - "memory.md#mem-obj-team-workflows-dir"
            - "runtime.md#rt-rte-skill-sync"
          note: "No retained numerical or parametric memory is supplied by these access structures."
      records:
        - "memory.md#mem-obj-sources"
        - "memory.md#mem-bap-corpus-answer"
        - "runtime.md#rt-obj-docs-grep"
        - "runtime.md#rt-bap-user-skills"
        - "runtime.md#rt-rte-knowledge-search"
        - "runtime.md#rt-obj-skill-links"
        - "memory.md#mem-obj-team-workflows-dir"
        - "runtime.md#rt-rte-skill-sync"
      note: "All included retained payload and access-metadata consumption forms are resolved at their evidence layers; external model processing is not a retained memory object here."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Shipped illustrative corpus and skill procedure"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-sources"
              note: "The sample corpus is source-authored illustrative content."
            -
              value: "authored"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-docs-grep"
              note: "The shipped procedure is authored guidance, not interaction-extracted memory."
          records:
            - "memory.md#mem-obj-sources"
            - "runtime.md#rt-obj-docs-grep"
          note: "Classification covers the visible initial text, not the histories of future adopter replacements."
        -
          scope: "Documented adopter corpus acquisition"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-sources"
                - "runtime.md#rt-rte-repository-admission"
              note: "Documentation copies and API references may be placed in the corpus."
            -
              value: "authored"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-sources"
                - "runtime.md#rt-rte-repository-admission"
              note: "The documented team editing and first-hand-tip path admits authored material."
          records:
            - "memory.md#mem-obj-sources"
            - "runtime.md#rt-rte-repository-admission"
          note: "Actual configured-root corpus provenance and individual derivation histories are unknown; these are documented paths, not an exhaustive provenance assertion."
        -
          scope: "Generated access references and resolved root configuration"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-skill-links"
                - "runtime.md#rt-rte-skill-sync"
              note: "Directory locations are mechanically turned into installed access references."
            -
              value: "other-compiled"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-team-workflows-dir"
                - "runtime.md#rt-rte-machine-setup"
              note: "Setup requests the resolved checkout path as persistent configuration."
          records:
            - "runtime.md#rt-obj-skill-links"
            - "runtime.md#rt-rte-skill-sync"
            - "memory.md#mem-obj-team-workflows-dir"
            - "runtime.md#rt-rte-machine-setup"
          note: "These are derived location metadata, not trace-derived knowledge."
      records:
        - "memory.md#mem-obj-sources"
        - "runtime.md#rt-obj-docs-grep"
        - "runtime.md#rt-rte-repository-admission"
        - "runtime.md#rt-obj-skill-links"
        - "runtime.md#rt-rte-skill-sync"
        - "memory.md#mem-obj-team-workflows-dir"
        - "runtime.md#rt-rte-machine-setup"
      note: "Authored and imported paths are supported, but arbitrary configured-root or adopter payload histories cannot be completely classified."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Corpus text at the Python lexical scorer"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-sources"
                - "epistemic.md#epi-rte-keyword-ranking"
                - "runtime.md#rt-rte-knowledge-search"
              note: "Retained words determine keyword overlap and relative file priority under fixed code."
          records:
            - "memory.md#mem-obj-sources"
            - "epistemic.md#epi-rte-keyword-ranking"
            - "runtime.md#rt-rte-knowledge-search"
          note: "Ranking input need not be a learned ranking policy."
        -
          scope: "Selected corpus at the answer-producing host"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-sources"
                - "memory.md#mem-bap-corpus-answer"
              note: "Previews and requested full-file reads provide reference and explanatory context for synthesis."
          records:
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-bap-corpus-answer"
          note: "Informational force, not verified truth, compulsory compliance or demonstrated activation."
        -
          scope: "Mutable retained skill procedure at the host"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-docs-grep"
                - "runtime.md#rt-bap-user-skills"
              note: "Procedural directions request query expansion, file reads, citations and retries."
          records:
            - "runtime.md#rt-obj-docs-grep"
            - "runtime.md#rt-bap-user-skills"
          note: "Host guidance is not repository-enforced permission or semantic validation."
        -
          scope: "Root configuration and link targets at implemented access consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-team-workflows-dir"
                - "runtime.md#rt-obj-skill-links"
                - "runtime.md#rt-rte-skill-sync"
              note: "The configuration selects a corpus location; link targets designate exposed skill locations."
          records:
            - "memory.md#mem-obj-team-workflows-dir"
            - "runtime.md#rt-obj-skill-links"
            - "runtime.md#rt-rte-skill-sync"
          note: "Directory existence/reachability checks do not establish trust or semantic approval."
        -
          scope: "Actual host discovery, precedence and activation of retained linked content"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-bap-user-skills"
            - "runtime.md#rt-rte-machine-setup"
          note: "External discovery and precedence are not inspected; installed link presence alone cannot classify every host-side consumer effect."
      records:
        - "memory.md#mem-obj-sources"
        - "epistemic.md#epi-rte-keyword-ranking"
        - "runtime.md#rt-rte-knowledge-search"
        - "memory.md#mem-bap-corpus-answer"
        - "runtime.md#rt-obj-docs-grep"
        - "runtime.md#rt-bap-user-skills"
        - "memory.md#mem-obj-team-workflows-dir"
        - "runtime.md#rt-obj-skill-links"
        - "runtime.md#rt-rte-skill-sync"
        - "runtime.md#rt-rte-machine-setup"
      note: "Local ranking, knowledge, instruction and routing effects are supported. Complete host-side authority coverage remains unresolved; no enforcement, validation or learning force is inferred from mere storage or reachability."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Documented team corpus/skill editing and replacement"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-repository-admission"
                - "memory.md#mem-obj-sources"
              note: "The README explicitly delegates supplying and replacing repository content to the team/adopter; this is an explicit human editing path."
          records:
            - "runtime.md#rt-rte-repository-admission"
            - "memory.md#mem-obj-sources"
          note: "Manual editing does not establish a mandatory human merge review for every update."
        -
          scope: "Synchronization admission of access references"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-skill-sync"
                - "runtime.md#rt-obj-skill-links"
              note: "Code admits links from directory existence and name availability without per-content operator approval, even when a human starts synchronization."
          records:
            - "runtime.md#rt-rte-skill-sync"
            - "runtime.md#rt-obj-skill-links"
          note: "The link write is distinct from authoring the linked content."
        -
          scope: "Prescribed model-mediated root-configuration write"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-machine-setup"
                - "memory.md#mem-obj-team-workflows-dir"
              note: "The host is instructed to resolve and write the root; no per-value human approval is prescribed."
          records:
            - "runtime.md#rt-rte-machine-setup"
            - "memory.md#mem-obj-team-workflows-dir"
          note: "A setup invocation alone is not a manual decision about the retained value."
        -
          scope: "Actual repository merge approval and alternative configured-root content admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-repository-admission"
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-team-workflows-dir"
          note: "The actual reviewer, veto policy and admission history of arbitrary configured content are not supplied; generic Git transport does not resolve human control."
      records:
        - "runtime.md#rt-rte-repository-admission"
        - "memory.md#mem-obj-sources"
        - "runtime.md#rt-rte-skill-sync"
        - "runtime.md#rt-obj-skill-links"
        - "runtime.md#rt-rte-machine-setup"
        - "memory.md#mem-obj-team-workflows-dir"
      note: "Manual content editing and automatic software/model admission coexist. Actual alternative content approval and merge governance prevent complete classification."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Documented replacement or editing of existing repository content"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-repository-admission"
                - "memory.md#mem-obj-sources"
              note: "Human editing or replacing an existing corpus/skill entry affords revision of retained content."
          records:
            - "runtime.md#rt-rte-repository-admission"
            - "memory.md#mem-obj-sources"
          note: "An editing affordance, not an observed revision or automatic semantic-maintenance implementation."
        -
          scope: "Meaning of arbitrary adopter edits and imported replacements"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-repository-admission"
            - "memory.md#mem-obj-sources"
          note: "No particular transformation inputs/outputs or semantic maintenance procedure establish whether other curation operations occur."
        -
          scope: "Shipped link cleanup and transient search-output filtering"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-skill-sync"
            - "memory.md#mem-obj-search-results"
          note: "Link reachability cleanup does not transform retained knowledge; current-run preview filtering creates no retained reduced memory representation."
      records:
        - "runtime.md#rt-rte-repository-admission"
        - "memory.md#mem-obj-sources"
        - "runtime.md#rt-rte-skill-sync"
        - "memory.md#mem-obj-search-results"
      note: "Revision is afforded through manual editing. Other semantic operations are not established by guidance, route names, link cleanup or preview truncation; actual adopter transformations remain unresolved."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Question-driven corpus search and requested full-file reads, including alternate-root and direct CLI branches"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-search"
              note: "CLI keywords request corpus selection and returned previews."
            -
              value: "pull"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-knowledge-search"
                - "memory.md#mem-bap-corpus-answer"
              note: "The host is instructed to request full selected files for the current question."
          records:
            - "runtime.md#rt-rte-knowledge-search"
            - "memory.md#mem-bap-corpus-answer"
          note: "Automatic lexical ranking fulfills the request; stdout delivery is not a second unsolicited push."
        -
          scope: "Access metadata consumed by later search/root resolution"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-team-workflows-dir"
                - "runtime.md#rt-rte-knowledge-search"
              note: "On a lookup request the program consults retained root configuration to find the requested corpus."
          records:
            - "memory.md#mem-obj-team-workflows-dir"
            - "runtime.md#rt-rte-knowledge-search"
          note: "This chain does not automatically inject document payload independent of lookup."
        -
          scope: "Later discovery and delivery of mutable skill content through installed references"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-bap-user-skills"
            - "runtime.md#rt-obj-skill-links"
            - "runtime.md#rt-rte-machine-setup"
          note: "Later host access is afforded but the host loader's request/selection/delivery semantics are external; no complete push or pull classification follows from links."
      records:
        - "runtime.md#rt-rte-knowledge-search"
        - "memory.md#mem-bap-corpus-answer"
        - "memory.md#mem-obj-team-workflows-dir"
        - "runtime.md#rt-bap-user-skills"
        - "runtime.md#rt-obj-skill-links"
        - "runtime.md#rt-rte-machine-setup"
      note: "The corpus chain is request-driven. Host discovery of mutable instructions remains included but unresolved; synchronization alone is not knowledge push."
    read_back_signal:
      assessment: "not-determinable"
      units:
        -
          scope: "Completely assessed question-driven corpus and root-selection chain"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-knowledge-search"
            - "memory.md#mem-obj-team-workflows-dir"
            - "memory.md#mem-bap-corpus-answer"
          note: "This chain is pull-only; lexical matching on a requested lookup is not a push signal."
        -
          scope: "Host delivery of retained mutable skill content"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-bap-user-skills"
            - "runtime.md#rt-obj-skill-links"
            - "runtime.md#rt-rte-machine-setup"
          note: "No recorded automatic host selector establishes a trigger, selector input and delivered retained parts. Folder identity and catalog exposure alone do not support identifier-based push."
      records:
        - "runtime.md#rt-rte-knowledge-search"
        - "memory.md#mem-obj-team-workflows-dir"
        - "memory.md#mem-bap-corpus-answer"
        - "runtime.md#rt-bap-user-skills"
        - "runtime.md#rt-obj-skill-links"
        - "runtime.md#rt-rte-machine-setup"
      note: "No push selection signal can be classified. A known pull chain cannot make the unresolved host-delivery alternative inapplicable."
    trace_learning:
      assessment: "known"
      units:
        -
          scope: "All shipped corpus/instruction acquisition, lookup and access-maintenance paths"
          assessment: "known"
          findings:
            -
              value: "no"
              basis: "wired"
              records:
                - "memory.md#mem-abs-trace-update"
              note: "Complete inspected shipped programs and instructions contain no automatic trace-fed retained behavior-shaping write with a later consumer."
          records:
            - "memory.md#mem-abs-trace-update"
            - "runtime.md#rt-rte-repository-admission"
            - "runtime.md#rt-rte-knowledge-search"
            - "runtime.md#rt-rte-skill-sync"
          note: "Bounded negative covers the template's write inventory, not external host/provider updates or future adopter additions."
      records:
        - "memory.md#mem-abs-trace-update"
        - "runtime.md#rt-rte-repository-admission"
        - "runtime.md#rt-rte-knowledge-search"
        - "runtime.md#rt-rte-skill-sync"
      note: "The inventory is known within the explicit shipped boundary, so the local negative also supports a bounded system union of no. Manual first-hand tips and current-question keyword revision do not qualify; improvement is a separate question."
    trace_source:
      assessment: "inapplicable"
      units:
        -
          scope: "All shipped routes within the trace-learning inventory"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-abs-trace-update"
          note: "No qualifying automatic trace-fed durable write is shipped, so there is no learning input source to classify."
      records:
        - "memory.md#mem-abs-trace-update"
      note: "The bounded complete absence of qualifying trace learning warrants inapplicability, not absence of all experiential information or all host traces."
---

# team-ai-workflows memory profile

## Comparison rationale

The comparison describes the shipped template, not a deployed team's unknown corpus or the host's own memory. Mutable instructions are included only as retained content that team editing can change and later host sessions can consume. The initial static instruction file alone is not evidence of accumulated interaction memory. The file/repository classifications distinguish the local readable payload from its Git distribution surface; access metadata is separate from both. See [MEM-OBJ-sources](memory.md#mem-obj-sources), [RT-RTE-repository-admission](runtime.md#rt-rte-repository-admission), [RT-OBJ-skill-links](runtime.md#rt-obj-skill-links) and [MEM-OBJ-team-workflows-dir](memory.md#mem-obj-team-workflows-dir).

Reconciliation supersedes the epistemic corpus and search-output identities with [MEM-OBJ-sources](memory.md#mem-obj-sources) and [MEM-OBJ-search-results](memory.md#mem-obj-search-results). No value changes because of these identity amendments. The latter is temporary output, not another retained store. The container [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search) remains canonical alongside its distinct [EPI-RTE-keyword-ranking](epistemic.md#epi-rte-keyword-ranking) part. Fixed code using retained corpus words establishes ranking authority; no retained ranking policy is needed.

Requested retrieval is pull even though code automatically scores and slices the response. Full-file reading is a subsequent requested operation, not proven by the preview emission. Host instruction discovery is different: the records establish reachability and an intended later consumer, but not the loader's selection semantics. Accordingly, direction remains partial and push signal remains not determinable, rather than classifying skill-folder names as identifier push. See [RT-RTE-knowledge-search](runtime.md#rt-rte-knowledge-search), [MEM-BAP-corpus-answer](memory.md#mem-bap-corpus-answer) and [RT-BAP-user-skills](runtime.md#rt-bap-user-skills).

Manual content editing is an afforded path; mandatory merge review is unresolved. Link admission is wired automatic control, and root-setting admission is automatic only at the claimed setup-procedure layer. Starting a workflow does not approve each resulting value. These layers do not upgrade one another. Editing an existing retained entry affords evolve, but focused-writing advice and preview truncation do not establish consolidation or synthesis of durable memory. No particular adopter transformation licenses a complete curation inventory. See [RT-RTE-repository-admission](runtime.md#rt-rte-repository-admission), [RT-RTE-skill-sync](runtime.md#rt-rte-skill-sync), [RT-RTE-machine-setup](runtime.md#rt-rte-machine-setup) and [MEM-OBJ-search-results](memory.md#mem-obj-search-results).

The trace-learning negative has a narrower, completely inspected inventory: shipped write and later-consumer routes. [MEM-ABS-trace-update](memory.md#mem-abs-trace-update) covers that inventory, including lookup, synchronization, setup and documented content replacement. Unresolved host delivery semantics do not introduce an unresolved shipped trace-fed writer. The scoped negative therefore survives system union; trace source is inapplicable. This does not deny manual experience-derived tips or classify opaque host/provider learning. It also says nothing about demonstrated improved capacity.

Evidence strength remains local: Python selection and filesystem synchronization are wired, repository customization is afforded, and model-facing directions are claimed. No classification asserts observed operation or causal benefit. Actual configured corpus provenance, merge approval and host discovery/precedence prevent stronger coverage where identified above.

Source-read log: none. This classification used only the supplied accepted members and reconciliation; no source ambiguity required a source read.

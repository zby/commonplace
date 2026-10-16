---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Agent-R memory profile: retained search experience and derived training conversations, with
  external training and auxiliary consumers unresolved.'
run-id: AAS-2026-10-12-agent-r-216224d4270a-01
source-identity: https://github.com/ByteDance-Seed/Agent-R
reviewed-boundary: 82fcc1ca7873b460949ed49022146dd988c32e31
memory-comparison:
  version: 2
  scope: Retained search-tree interaction text and score/branch metadata; derived revision conversations,
    loss flags and feedback/path sidecars; exposed converted conversations; evaluation results and optional
    progress metadata; their automatic writes, selection, maintenance and recorded or unresolved later
    consumers. Includes declared external training as an unresolved consumer/update branch, not an established
    stored learned checkpoint. Excludes unchanged actor/verifier weights, static shipped prompts, ordinary
    current-rollout context, external environment state and opaque provider retention. Caller-supplied
    demonstrations/prefixes remain unresolved delivery/update alternatives rather than asserted retained
    objects.
  axes:
    storage_substrate:
      assessment: known
      units:
      - scope: Persisted tree interaction content
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-extended-node
          note: Python conversation, node, mapping, list or index state during the recorded write/consumer
            operation.
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-extended-node
          note: JSON tree, JSONL row, JSON conversion, evaluation JSON or decimal text file; serialization
            is not a database substrate.
        records:
        - memory.md#mem-obj-extended-node
        note: The recorded object is assembled in process memory and retained in a file; no other operative
          payload is recorded.
      - scope: Persisted tree score and branch metadata
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-node-statistics
          note: Python conversation, node, mapping, list or index state during the recorded write/consumer
            operation.
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-node-statistics
          note: JSON tree, JSONL row, JSON conversion, evaluation JSON or decimal text file; serialization
            is not a database substrate.
        records:
        - memory.md#mem-obj-node-statistics
        note: The recorded object is assembled in process memory and retained in a file; no other operative
          payload is recorded.
      - scope: Revision conversation content
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-revise-log
          note: Python conversation, node, mapping, list or index state during the recorded write/consumer
            operation.
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-revise-log
          note: JSON tree, JSONL row, JSON conversion, evaluation JSON or decimal text file; serialization
            is not a database substrate.
        records:
        - memory.md#mem-obj-revise-log
        note: The recorded object is assembled in process memory and retained in a file; no other operative
          payload is recorded.
      - scope: Revision loss flags
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-loss-flags
          note: Python conversation, node, mapping, list or index state during the recorded write/consumer
            operation.
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-loss-flags
          note: JSON tree, JSONL row, JSON conversion, evaluation JSON or decimal text file; serialization
            is not a database substrate.
        records:
        - memory.md#mem-obj-loss-flags
        note: The recorded object is assembled in process memory and retained in a file; no other operative
          payload is recorded.
      - scope: Revision feedback and path sidecars
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-revise-feedback
          note: Python conversation, node, mapping, list or index state during the recorded write/consumer
            operation.
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-revise-feedback
          note: JSON tree, JSONL row, JSON conversion, evaluation JSON or decimal text file; serialization
            is not a database substrate.
        records:
        - memory.md#mem-obj-revise-feedback
        note: The recorded object is assembled in process memory and retained in a file; no other operative
          payload is recorded.
      - scope: Evaluation result conversation and metadata
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-final-result
          note: Python conversation, node, mapping, list or index state during the recorded write/consumer
            operation.
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-final-result
          note: JSON tree, JSONL row, JSON conversion, evaluation JSON or decimal text file; serialization
            is not a database substrate.
        records:
        - memory.md#mem-obj-final-result
        note: The recorded object is assembled in process memory and retained in a file; no other operative
          payload is recorded.
      - scope: Optional progress index
        assessment: known
        findings:
        - value: in-memory
          basis: afforded
          records:
          - memory.md#mem-obj-progress-file
          note: Python conversation, node, mapping, list or index state during the recorded write/consumer
            operation.
        - value: files
          basis: afforded
          records:
          - memory.md#mem-obj-progress-file
          note: JSON tree, JSONL row, JSON conversion, evaluation JSON or decimal text file; serialization
            is not a database substrate.
        records:
        - memory.md#mem-obj-progress-file
        note: The recorded object is assembled in process memory and retained in a file; no other operative
          payload is recorded.
      - scope: Converted conversation output
        assessment: known
        findings:
        - value: in-memory
          basis: afforded
          records:
          - epistemic.md#epi-obj-conversation
          note: Python conversation, node, mapping, list or index state during the recorded write/consumer
            operation.
        - value: files
          basis: afforded
          records:
          - epistemic.md#epi-obj-conversation
          note: JSON tree, JSONL row, JSON conversion, evaluation JSON or decimal text file; serialization
            is not a database substrate.
        records:
        - epistemic.md#epi-obj-conversation
        note: The recorded object is assembled in process memory and retained in a file; no other operative
          payload is recorded.
      records:
      - memory.md#mem-obj-extended-node
      - memory.md#mem-obj-node-statistics
      - memory.md#mem-obj-revise-log
      - memory.md#mem-obj-loss-flags
      - memory.md#mem-obj-revise-feedback
      - memory.md#mem-obj-final-result
      - memory.md#mem-obj-progress-file
      - epistemic.md#epi-obj-conversation
      note: 'Complete recorded retained-object inventory: tree parts, export parts, evaluation results,
        optional progress storage and converted output. Static weights, provider retention and hypothetical
        trained checkpoints are not operative retained objects established in this boundary.'
    representational_form:
      assessment: known
      units:
      - scope: Tree text at the builder/verifier
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-extended-node
          note: Thoughts and observations inform model interpretation; role fields and replay action strings
            have fixed consumer rules.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-extended-node
          note: Thoughts and observations inform model interpretation; role fields and replay action strings
            have fixed consumer rules.
        records:
        - memory.md#mem-obj-extended-node
        note: Thoughts and observations inform model interpretation; role fields and replay action strings
          have fixed consumer rules.
      - scope: Tree score and branch metadata
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-node-statistics
          note: Counters, values, flags and child structure are numerical/symbolic inputs to fixed selection
            rules, not distributed parameters.
        records:
        - memory.md#mem-obj-node-statistics
        note: Counters, values, flags and child structure are numerical/symbolic inputs to fixed selection
          rules, not distributed parameters.
      - scope: Revision conversation content
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-revise-log
          note: Copied and synthetic text has natural-language content; roles and message order provide
            symbolic framing.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-revise-log
          note: Copied and synthetic text has natural-language content; roles and message order provide
            symbolic framing.
        records:
        - memory.md#mem-obj-revise-log
        note: Copied and synthetic text has natural-language content; roles and message order provide
          symbolic framing.
      - scope: Revision loss fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-loss-flags
          note: Boolean eligibility fields are symbolic, not verbal directions; optimizer interpretation
            is unknown.
        records:
        - memory.md#mem-obj-loss-flags
        note: Boolean eligibility fields are symbolic, not verbal directions; optimizer interpretation
          is unknown.
      - scope: Feedback and source-path sidecars
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-revise-feedback
          note: Reasons and path text are natural language; identifiers, mode flags and judgment framing
            are symbolic.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-revise-feedback
          note: Reasons and path text are natural language; identifiers, mode flags and judgment framing
            are symbolic.
        records:
        - memory.md#mem-obj-revise-feedback
        note: Reasons and path text are natural language; identifiers, mode flags and judgment framing
          are symbolic.
      - scope: Evaluation result parts
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-final-result
          note: Conversation text is natural language; result labels, score, count and framing are symbolic.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-final-result
          note: Conversation text is natural language; result labels, score, count and framing are symbolic.
        records:
        - memory.md#mem-obj-final-result
        note: Conversation text is natural language; result labels, score, count and framing are symbolic.
      - scope: Progress index
        assessment: known
        findings:
        - value: symbolic
          basis: afforded
          records:
          - memory.md#mem-obj-progress-file
          note: A decimal index is symbolic access metadata.
        records:
        - memory.md#mem-obj-progress-file
        note: A decimal index is symbolic access metadata.
      - scope: Converted conversation output
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records:
          - epistemic.md#epi-obj-conversation
          note: Copied contents retain natural-language form in a new symbolic system/input/output wrapper.
        - value: symbolic
          basis: afforded
          records:
          - epistemic.md#epi-obj-conversation
          note: Copied contents retain natural-language form in a new symbolic system/input/output wrapper.
        records:
        - epistemic.md#epi-obj-conversation
        note: Copied contents retain natural-language form in a new symbolic system/input/output wrapper.
      records:
      - memory.md#mem-obj-extended-node
      - memory.md#mem-obj-node-statistics
      - memory.md#mem-obj-revise-log
      - memory.md#mem-obj-loss-flags
      - memory.md#mem-obj-revise-feedback
      - memory.md#mem-obj-final-result
      - memory.md#mem-obj-progress-file
      - epistemic.md#epi-obj-conversation
      note: All recorded operative retained parts and their text/framing paths are covered. No retained
        embedding or opaque compressed payload is reported. Unchanged actor/verifier weights are excluded,
        so their parametric form is not projected onto accumulated memory.
    lineage:
      assessment: partial
      units:
      - scope: Tree interaction text and framing
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-extended-node
          - runtime.md#rt-rte-tree-collection
          note: Environment instruction and observation text enters the retained tree.
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-extended-node
          - runtime.md#rt-rte-tree-collection
          note: Recorded actor actions, responses and environment outcomes are retained from interaction
            experience.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-extended-node
          note: Software normalizes observations and serializes role/content framing; this does not establish
            semantic fidelity.
        records:
        - memory.md#mem-obj-extended-node
        - runtime.md#rt-rte-tree-collection
        note: External instruction/observation origin, checkpoint provenance and full initial conversation
          contents remain uninspected; the visible derivations do not certify those sources.
      - scope: Tree numerical and structural metadata
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-node-statistics
          - runtime.md#rt-rte-tree-collection
          note: Environment outcomes from action sequences supply score/terminal information.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-node-statistics
          note: Fixed score updates, clamping and tree construction derive the symbolic metadata.
        records:
        - memory.md#mem-obj-node-statistics
        - runtime.md#rt-rte-tree-collection
        note: Visible derivation is reward/done acquisition followed by fixed search computation.
      - scope: Revision conversation derivation
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-revise-log
          - runtime.md#rt-rte-revision-export
          note: Selected high/low interaction paths supply copied messages.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-revise-log
          - epistemic.md#epi-rte-conversation-splice
          note: Software splices paths and inserts stock corrective wording and fabricated wait/acknowledgement;
            good-only mode copies the selected path instead.
        records:
        - memory.md#mem-obj-revise-log
        - runtime.md#rt-rte-revision-export
        - epistemic.md#epi-rte-conversation-splice
        note: Classification concerns construction from already recorded inputs, not their original truth
          or checkpoint provenance.
      - scope: Loss flags
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-loss-flags
          note: Fixed construction assigns true/false eligibility fields.
        records:
        - memory.md#mem-obj-loss-flags
        note: Software assigns flags rather than deriving human approval.
      - scope: Feedback and path sidecars
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-revise-feedback
          note: Stored path text and action/observation diagnostics originate in collected interactions.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-revise-feedback
          - runtime.md#rt-rte-revision-export
          note: Verifier-generated reasons/judgment and software identifiers/flags are constructed during
            export.
        records:
        - memory.md#mem-obj-revise-feedback
        - runtime.md#rt-rte-revision-export
        note: Scope is the visible sidecar derivation; model reasoning and original task warrant are not
          inferred.
      - scope: Evaluation results including supplied-prefix alternative
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-final-result
          note: External instructions and observations enter result history.
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-final-result
          note: Rollout responses, observations and outcomes enter the result.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-final-result
          note: Software derives labels, step count and message framing.
        records:
        - memory.md#mem-obj-final-result
        - runtime.md#rt-rte-agent-evaluation
        note: The helper accepts caller prefix strings without a retained source or authorship identity;
          their original lineage cannot be classified.
      - scope: Converted conversation derivation
        assessment: known
        findings:
        - value: other-compiled
          basis: afforded
          records:
          - memory.md#mem-rte-dataset-rewrite
          - epistemic.md#epi-obj-conversation
          note: Deterministic positional extraction from exported rows.
        records:
        - memory.md#mem-rte-dataset-rewrite
        - epistemic.md#epi-obj-conversation
        note: The converter copies selected content positions and changes framing; omitted metadata does
          not become a new provenance claim.
      - scope: Progress index input origin
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-progress-file
        note: Generic caller-supplied index and physical write do not identify human authorship, imported
          content or a trace derivation.
      records:
      - memory.md#mem-obj-extended-node
      - runtime.md#rt-rte-tree-collection
      - memory.md#mem-obj-node-statistics
      - memory.md#mem-obj-revise-log
      - runtime.md#rt-rte-revision-export
      - epistemic.md#epi-rte-conversation-splice
      - memory.md#mem-obj-loss-flags
      - memory.md#mem-obj-revise-feedback
      - memory.md#mem-obj-final-result
      - runtime.md#rt-rte-agent-evaluation
      - memory.md#mem-rte-dataset-rewrite
      - epistemic.md#epi-obj-conversation
      - memory.md#mem-obj-progress-file
      note: Positive derivation paths coexist with unresolved original environment/checkpoint lineage,
        prefix origin and progress-index provenance. No manual-authored lineage is inferred from launching
        a driver or supplying a directory.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained tree text at the revision verifier
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-extended-node
          - runtime.md#rt-rte-revision-export
          note: Verifier receives selected retained observations/actions as evidence and judgment context.
        records:
        - memory.md#mem-obj-extended-node
        - runtime.md#rt-rte-revision-export
        note: The loaded text supplies task and action/observation context; its later use is not direct
          actor policy.
      - scope: Retained tree content and outcomes at revision-data construction
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-obj-extended-node
          - memory.md#mem-obj-node-statistics
          - memory.md#mem-obj-revise-log
          - runtime.md#rt-rte-revision-export
          note: Saved experience feeds the construction of behavior-shaping training examples; this does
            not imply optimizer execution or improvement.
        records:
        - memory.md#mem-obj-extended-node
        - memory.md#mem-obj-node-statistics
        - memory.md#mem-obj-revise-log
        - runtime.md#rt-rte-revision-export
        note: Experience is an input to an automatic durable training-artifact construction, conditional
          on the export code reaching its writer.
      - scope: Retained score and terminal metadata at path selection
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-node-statistics
          - runtime.md#rt-rte-revision-export
          note: Average leaf value orders candidate paths.
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-node-statistics
          - runtime.md#rt-rte-revision-export
          note: Positive-root, terminal-leaf and intended threshold criteria define candidate eligibility;
            float/string defects limit threshold execution.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-node-statistics
          - runtime.md#rt-rte-revision-export
          note: Nonpositive roots are excluded from construction; reached defective comparisons abort
            rather than certify examples.
        records:
        - memory.md#mem-obj-node-statistics
        - runtime.md#rt-rte-revision-export
        note: Separate relative-priority and eligibility consumers read symbolic fields.
      - scope: Revision text at the exposed converter
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-obj-revise-log
          - memory.md#mem-rte-dataset-rewrite
          note: Content is the retained reference/input material copied by the conversion operation.
        records:
        - memory.md#mem-obj-revise-log
        - memory.md#mem-rte-dataset-rewrite
        note: Conversion reads stored text but does not evaluate or learn from it.
      - scope: Revision text and loss flags at intended external trainer
        assessment: partial
        findings:
        - value: learning
          basis: claimed
          records:
          - memory.md#mem-obj-revise-log
          - runtime.md#rt-clm-iterative-training
          note: README intends the retained conversations for external training.
        records:
        - memory.md#mem-obj-revise-log
        - memory.md#mem-obj-loss-flags
        - runtime.md#rt-clm-iterative-training
        - runtime.md#rt-abs-training-machinery
        note: Training is declared, but no captured optimizer establishes input schema, mask interpretation,
          checkpoint adoption or actual effect.
      - scope: Retained feedback/path sidecars at a later consumer
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-revise-feedback
        note: The judgment has immediate prefix-selection force, but retained reasons and path sidecars
          have no established later reader; immediate judgment authority is not assigned to their stored
          copy.
      - scope: Evaluation result at a later consumer
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-final-result
        note: No shipped later result consumer establishes authority; storage alone does not grant learning,
          ranking or checkpoint validation.
      - scope: Progress index at a resume consumer
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-progress-file
        note: Read/write helpers have no wired caller; intended access metadata is not evidence of an
          actual routing consumer.
      - scope: Converted output at an optimizer
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-dataset-rewrite
        - epistemic.md#epi-obj-conversation
        - runtime.md#rt-abs-training-machinery
        note: Output text exists as an afforded storage object, but a training consumer and effect are
          unspecified.
      records:
      - memory.md#mem-obj-extended-node
      - runtime.md#rt-rte-revision-export
      - memory.md#mem-obj-node-statistics
      - memory.md#mem-obj-revise-log
      - memory.md#mem-rte-dataset-rewrite
      - memory.md#mem-obj-loss-flags
      - runtime.md#rt-clm-iterative-training
      - runtime.md#rt-abs-training-machinery
      - memory.md#mem-obj-revise-feedback
      - memory.md#mem-obj-final-result
      - memory.md#mem-obj-progress-file
      - epistemic.md#epi-obj-conversation
      note: Tree-to-builder knowledge, learning, ranking and eligibility effects are recorded; external
        training is claimed only. No standing instruction authority is assigned to a stock correction
        inside an example, and unconsumed metadata receives no positive authority finding.
    write_agency:
      assessment: partial
      units:
      - scope: Tree child admission and completion save
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-tree-collection
          - memory.md#mem-obj-extended-node
          - memory.md#mem-obj-node-statistics
          note: Software admits generated children, handles scores/duplicates and saves after search.
        records:
        - runtime.md#rt-rte-tree-collection
        - memory.md#mem-obj-extended-node
        - memory.md#mem-obj-node-statistics
        note: Batch launch/configuration does not approve each retained child.
      - scope: Revision conversation, flags and sidecar admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-revision-export
          - memory.md#mem-obj-revise-log
          - memory.md#mem-obj-loss-flags
          - memory.md#mem-obj-revise-feedback
          note: Software filters pairs, optional critique sets prefix length, and the writer appends completed
            rows.
        records:
        - runtime.md#rt-rte-revision-export
        - memory.md#mem-obj-revise-log
        - memory.md#mem-obj-loss-flags
        - memory.md#mem-obj-revise-feedback
        note: Construction and append admission are model/software controlled without per-example human
          approval; threshold defects remain.
      - scope: Evaluation result admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-final-result
          - runtime.md#rt-rte-agent-evaluation
          note: Software saves score/history after the loop.
        records:
        - memory.md#mem-obj-final-result
        - runtime.md#rt-rte-agent-evaluation
        note: Result persistence follows rollout completion, not per-result approval.
      - scope: Dataset conversion transformation
        assessment: known
        findings:
        - value: automatic
          basis: afforded
          records:
          - memory.md#mem-rte-dataset-rewrite
          note: The converter selects positions and drops fields without a per-content human decision.
        records:
        - memory.md#mem-rte-dataset-rewrite
        note: Fixed positional extraction automatically determines output contents once invoked; input
          supply/approval is separately unresolved.
      - scope: Converter input admission and progress-index supply
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-dataset-rewrite
        - memory.md#mem-obj-progress-file
        note: Generic caller identity does not establish an explicit human content decision or autonomous
          admission of those supplied inputs.
      - scope: External training and changed-checkpoint admission
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-clm-iterative-training
        - runtime.md#rt-abs-training-machinery
        note: Documented launch instructions establish neither per-checkpoint human approval nor automated
          admission of a learned derivative.
      records:
      - runtime.md#rt-rte-tree-collection
      - memory.md#mem-obj-extended-node
      - memory.md#mem-obj-node-statistics
      - runtime.md#rt-rte-revision-export
      - memory.md#mem-obj-revise-log
      - memory.md#mem-obj-loss-flags
      - memory.md#mem-obj-revise-feedback
      - memory.md#mem-obj-final-result
      - runtime.md#rt-rte-agent-evaluation
      - memory.md#mem-rte-dataset-rewrite
      - memory.md#mem-obj-progress-file
      - runtime.md#rt-clm-iterative-training
      - runtime.md#rt-abs-training-machinery
      note: Automatic internal writes are established independently of caller authorship and filesystem
        I/O. Caller-supplied helper inputs and external checkpoint admission remain unresolved; no manual
        finding is licensed.
    curation_operations:
      assessment: partial
      units:
      - scope: Retained paths into a revision conversation
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - runtime.md#rt-rte-revision-export
          - memory.md#mem-obj-revise-log
          note: Selects retained paths and a delimited low prefix into a reduced conversation of copied
            interaction content.
        - value: dedup
          basis: wired
          records:
          - runtime.md#rt-rte-revision-export
          - epistemic.md#epi-rte-conversation-splice
          note: Exact initial response equality suppresses repeated good-prefix messages during assembly.
        - value: synthesize
          basis: wired
          records:
          - epistemic.md#epi-rte-conversation-splice
          - memory.md#mem-obj-revise-log
          note: Inserted self-error admissions assert propositions absent from the source logs; this positive
            concerns that inserted content, not copied observations.
        records:
        - runtime.md#rt-rte-revision-export
        - memory.md#mem-obj-revise-log
        - epistemic.md#epi-rte-conversation-splice
        note: Distinct transformations coexist; this is not merely copying a file or training successfully.
      - scope: Exported rows into converted conversation
        assessment: known
        findings:
        - value: consolidate
          basis: afforded
          records:
          - memory.md#mem-rte-dataset-rewrite
          - epistemic.md#epi-obj-conversation
          note: Content-only positional selection reduces the retained row representation without creating
            new text claims.
        records:
        - memory.md#mem-rte-dataset-rewrite
        - epistemic.md#epi-obj-conversation
        note: Output drops sidecars, flags and unmatched trailing content while retaining selected strings.
      - scope: External training or operator maintenance of retained artifacts
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-clm-iterative-training
        - runtime.md#rt-abs-training-machinery
        - memory.md#mem-rte-dataset-rewrite
        note: Parameter updates and external content curation are not captured. Overwrite/append, index
          I/O and caller deletion capability alone establish no evolve, invalidate, decay or promote operation.
      records:
      - runtime.md#rt-rte-revision-export
      - memory.md#mem-obj-revise-log
      - epistemic.md#epi-rte-conversation-splice
      - memory.md#mem-rte-dataset-rewrite
      - epistemic.md#epi-obj-conversation
      - runtime.md#rt-clm-iterative-training
      - runtime.md#rt-abs-training-machinery
      note: Recorded transformations support consolidate, dedup and synthesize. Search-time statistics,
        history pruning without a summary, physical overwrite and replication are not additional retained-memory
        curation findings. External maintenance remains unresolved.
    read_back_direction:
      assessment: partial
      units:
      - scope: Persisted tree request, selection and delivery
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-tree-collection
          - runtime.md#rt-rte-revision-export
          - memory.md#mem-obj-extended-node
          - memory.md#mem-obj-node-statistics
          note: The builder loads requested tree files and consumes selected contents; delivery to its
            requested critique is not a separate push.
        records:
        - runtime.md#rt-rte-tree-collection
        - runtime.md#rt-rte-revision-export
        - memory.md#mem-obj-extended-node
        - memory.md#mem-obj-node-statistics
        note: A separate CLI requests the selected directory; enumeration and reward selection fulfill
          that batch request.
      - scope: Supplied retained export rows at rewrite
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-rte-dataset-rewrite
          - memory.md#mem-obj-revise-log
          note: Requested conversion consumes supplied retained row contents.
        records:
        - memory.md#mem-rte-dataset-rewrite
        - memory.md#mem-obj-revise-log
        note: Library caller supplies rows to a consumer operation; no deployed driver or trainer is wired.
      - scope: External trainer and changed actor checkpoint
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-clm-iterative-training
        - runtime.md#rt-abs-training-machinery
        note: Consumer intent is named, but ingestion request/selection/delivery and checkpoint adoption
          direction are not established.
      - scope: Auxiliary demonstrations, prefix source, progress and evaluation-result reuse
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-cmp-context-helpers
        - memory.md#mem-obj-progress-file
        - memory.md#mem-obj-final-result
        - runtime.md#rt-rte-agent-evaluation
        note: Helpers accept caller data or afford storage, but durable source-to-later-invocation delivery
          is unspecified; current rollout history is excluded.
      records:
      - runtime.md#rt-rte-tree-collection
      - runtime.md#rt-rte-revision-export
      - memory.md#mem-obj-extended-node
      - memory.md#mem-obj-node-statistics
      - memory.md#mem-rte-dataset-rewrite
      - memory.md#mem-obj-revise-log
      - runtime.md#rt-clm-iterative-training
      - runtime.md#rt-abs-training-machinery
      - memory.md#mem-cmp-context-helpers
      - memory.md#mem-obj-progress-file
      - memory.md#mem-obj-final-result
      - runtime.md#rt-rte-agent-evaluation
      note: The shipped cross-invocation tree consumer is pull; the converter affords requested consumption.
        Known pull does not resolve external/auxiliary delivery alternatives or justify an axis-wide no-push
        assertion.
    read_back_signal:
      assessment: not-determinable
      units:
      - scope: Requested tree-file and rewrite consumption
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-tree-collection
        - runtime.md#rt-rte-revision-export
        - memory.md#mem-rte-dataset-rewrite
        note: These are pull operations, not automatic unsolicited delivery; filename IDs and reward filters
          do not establish a push selection signal.
      - scope: External and auxiliary possible later delivery
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-clm-iterative-training
        - runtime.md#rt-abs-training-machinery
        - memory.md#mem-cmp-context-helpers
        - memory.md#mem-obj-progress-file
        - memory.md#mem-obj-final-result
        note: No actual push trigger, selector input and delivered retained part are recorded for these
          alternatives. Whether any push exists and which signal selects it cannot be determined.
      records:
      - runtime.md#rt-rte-tree-collection
      - runtime.md#rt-rte-revision-export
      - memory.md#mem-rte-dataset-rewrite
      - runtime.md#rt-clm-iterative-training
      - runtime.md#rt-abs-training-machinery
      - memory.md#mem-cmp-context-helpers
      - memory.md#mem-obj-progress-file
      - memory.md#mem-obj-final-result
      note: No positive push signal is established. Pull-route inapplicability is local; unresolved included
        alternatives prevent axis-wide inapplicability. Coarse, identifier and inferred selectors are
        not guessed from file enumeration or task labels.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic tree-to-revision-training-artifact write
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-revision-export
          - memory.md#mem-obj-revise-log
          - memory.md#mem-obj-extended-node
          - memory.md#mem-obj-node-statistics
          note: Linked interaction experience feeds software-produced retained revision examples; later
            external training is intended, not observed or captured.
        records:
        - runtime.md#rt-rte-revision-export
        - memory.md#mem-obj-revise-log
        - memory.md#mem-obj-extended-node
        - memory.md#mem-obj-node-statistics
        - epistemic.md#epi-rte-conversation-splice
        note: Qualifying scope is automatic construction of durable behavior-shaping training material
          from retained experience, not executed parameter learning. The wired construction is conditional
          on reaching past defective thresholds.
      - scope: Converted training artifact and its later consumer
        assessment: partial
        findings:
        - value: 'yes'
          basis: afforded
          records:
          - memory.md#mem-rte-dataset-rewrite
          - epistemic.md#epi-obj-conversation
          note: Callable conversion produces another durable training-shaped form from trace-fed examples;
            this is not an independently observed training update.
        records:
        - memory.md#mem-rte-dataset-rewrite
        - epistemic.md#epi-obj-conversation
        - runtime.md#rt-clm-iterative-training
        - runtime.md#rt-abs-training-machinery
        note: Automatic conversion from trace-derived conversations is afforded, but actual training input
          contract and downstream adoption are unresolved.
      - scope: Advertised trace-fed parameter training and later actor
        assessment: partial
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - runtime.md#rt-clm-iterative-training
          note: The declared self-training method uses collected/revised experience to train a later actor.
        records:
        - runtime.md#rt-clm-iterative-training
        - runtime.md#rt-abs-training-machinery
        - runtime.md#rt-cmp-func-call-offline
        note: Iterative training is declared; optimizer ingestion, updated checkpoint identity/admission
          and later behavioral dependence are not implemented in the captured artifact.
      - scope: Other retained-result and auxiliary input update chains
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-final-result
        - memory.md#mem-cmp-context-helpers
        - memory.md#mem-obj-progress-file
        note: Result retention, supplied demonstrations/prefixes and optional progress storage do not
          establish automatic durable behavior-shaping updates or their trace-fed later consumers.
      records:
      - runtime.md#rt-rte-revision-export
      - memory.md#mem-obj-revise-log
      - memory.md#mem-obj-extended-node
      - memory.md#mem-obj-node-statistics
      - epistemic.md#epi-rte-conversation-splice
      - memory.md#mem-rte-dataset-rewrite
      - epistemic.md#epi-obj-conversation
      - runtime.md#rt-clm-iterative-training
      - runtime.md#rt-abs-training-machinery
      - runtime.md#rt-cmp-func-call-offline
      - memory.md#mem-obj-final-result
      - memory.md#mem-cmp-context-helpers
      - memory.md#mem-obj-progress-file
      note: Positive architectural/artifact findings do not claim exercised training, improved capacity
        or a closed self-improvement loop. Unresolved alternate update chains preclude a complete classification;
        no local or system-wide no is inferred from unchanged inference weights.
    trace_source:
      assessment: partial
      units:
      - scope: Original experience behind revision conversation construction
        assessment: known
        findings:
        - value: trajectories
          basis: wired
          records:
          - memory.md#mem-obj-extended-node
          - memory.md#mem-obj-node-statistics
          - memory.md#mem-obj-revise-log
          - runtime.md#rt-rte-revision-export
          note: Saved branches link actions, states/observations and outcomes into multi-step experience
            used by the revision writer.
        records:
        - memory.md#mem-obj-extended-node
        - memory.md#mem-obj-node-statistics
        - memory.md#mem-obj-revise-log
        - runtime.md#rt-rte-revision-export
        note: Source classification follows linked environment interaction, not chat role serialization.
          Synthetic stock wording is a non-trace contribution, not a new trace-source class.
      - scope: Original experience behind exposed dataset conversion
        assessment: known
        findings:
        - value: trajectories
          basis: afforded
          records:
          - memory.md#mem-rte-dataset-rewrite
          - epistemic.md#epi-obj-conversation
          - memory.md#mem-obj-extended-node
          - memory.md#mem-obj-revise-log
          note: Copied revision conversation text originates in the collected multi-step interaction paths.
        records:
        - memory.md#mem-rte-dataset-rewrite
        - epistemic.md#epi-obj-conversation
        - memory.md#mem-obj-extended-node
        - memory.md#mem-obj-revise-log
        note: The conversion consumes a derivative, but does not change the original trace kind.
      - scope: Advertised optimizer input
        assessment: partial
        findings:
        - value: trajectories
          basis: claimed
          records:
          - runtime.md#rt-clm-iterative-training
          - memory.md#mem-obj-revise-log
          note: Declared training uses revision trajectories constructed from scored search paths.
        records:
        - runtime.md#rt-clm-iterative-training
        - memory.md#mem-obj-revise-log
        - memory.md#mem-obj-loss-flags
        - memory.md#mem-obj-revise-feedback
        - runtime.md#rt-abs-training-machinery
        note: The intended training conversations derive from trajectories; actual ingestion, sidecar
          use and any additional inputs are unknown.
      - scope: Potential result/prefix/demonstration update inputs
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-final-result
        - memory.md#mem-cmp-context-helpers
        - memory.md#mem-obj-progress-file
        note: No qualifying write is established for these alternatives, and supplied-prefix/demo origin
          is unspecified; a tool-trace, session-log or event-stream source cannot be inferred.
      records:
      - memory.md#mem-obj-extended-node
      - memory.md#mem-obj-node-statistics
      - memory.md#mem-obj-revise-log
      - runtime.md#rt-rte-revision-export
      - memory.md#mem-rte-dataset-rewrite
      - epistemic.md#epi-obj-conversation
      - runtime.md#rt-clm-iterative-training
      - memory.md#mem-obj-loss-flags
      - memory.md#mem-obj-revise-feedback
      - runtime.md#rt-abs-training-machinery
      - memory.md#mem-obj-final-result
      - memory.md#mem-cmp-context-helpers
      - memory.md#mem-obj-progress-file
      note: Trajectories are positively supported for the recorded builder chain and intended training.
        Conversation-shaped storage is not evidence of agent session logs; environment step reports within
        linked paths do not independently establish an event-stream input. Unresolved original inputs
        to other possible updates prevent complete coverage.
---

# Agent-R memory profile

## Comparison rationale

The retained tree has two operative parts. Text supplies context to the revision
verifier; numerical and structural fields rank paths and constrain eligibility.
Their shared JSON substrate does not make their forms or authorities identical.
The inventory also includes exported content, flags, diagnostics, converted
output, evaluation results and optional progress storage. Storage and form are
known for these recorded objects; this does not establish later semantic use
of every stored field. See [MEM-OBJ-extended-node](memory.md#mem-obj-extended-node),
[MEM-OBJ-node-statistics](memory.md#mem-obj-node-statistics),
[MEM-OBJ-loss-flags](memory.md#mem-obj-loss-flags),
[MEM-OBJ-revise-feedback](memory.md#mem-obj-revise-feedback),
[MEM-OBJ-final-result](memory.md#mem-obj-final-result) and
[MEM-OBJ-progress-file](memory.md#mem-obj-progress-file).

Revision construction both consolidates existing path content and synthesizes
an inserted self-error admission. The latter is not entailed by copied
observations or outcomes. Prefix equality suppression supplies the separate
dedup finding. These classifications concern implemented transformations below
the defective numeric thresholds, not successful nonempty CLI exports. Good-only
and no-critique modes retain their different construction paths without repairing
the thresholds. See [RT-RTE-revision-export](runtime.md#rt-rte-revision-export)
and [EPI-RTE-conversation-splice](epistemic.md#epi-rte-conversation-splice).

Experience has learning authority at the durable training-artifact construction
consumer, independently of knowledge authority at the verifier. Trace learning
here describes automatic trace-fed artifact production, not demonstrated improved
capacity. The dataset construction is wired but conditional; external optimizer
consumption and later actor adoption are claimed/unresolved. Conversion is only
afforded. These distinct bases cannot be combined into observed training or a
closed improvement loop. Static corrective wording inside an example is not
standing instruction authority for a deployed agent. See
[MEM-OBJ-revise-log](memory.md#mem-obj-revise-log),
[RT-CLM-iterative-training](runtime.md#rt-clm-iterative-training) and
[RT-ABS-training-machinery](runtime.md#rt-abs-training-machinery).

The original trace source is multi-step environment experience. Chat-shaped
serialization does not add session-logs, and action/observation pairs inside
linked search paths do not establish a separate tool-traces or event-streams
input. The imported initial instruction and fabricated wait exchange remain
non-trace contributions to the derived conversation. Original environment and
checkpoint provenance, supplied-prefix origin and actual optimizer inputs remain
unresolved. See [MEM-OBJ-extended-node](memory.md#mem-obj-extended-node),
[MEM-OBJ-revise-log](memory.md#mem-obj-revise-log) and
[MEM-OBJ-final-result](memory.md#mem-obj-final-result).

Requested batch tree consumption is pull. Selection within that request does
not become unsolicited push merely because code selects leaves or delivers text
to the requested verifier. Filename identifiers therefore establish no positive
push signal. Auxiliary helpers and external training do not establish their own
retained-source delivery chains, so read-back signal is locally inapplicable on
the known pull operations but not determinable across the full inventory. See
[RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection),
[MEM-RTE-dataset-rewrite](memory.md#mem-rte-dataset-rewrite) and
[MEM-CMP-context-helpers](memory.md#mem-cmp-context-helpers).

Reconciliation supersedes the duplicate epistemic rewrite route with
[MEM-RTE-dataset-rewrite](memory.md#mem-rte-dataset-rewrite). This profile cites
that canonical route while retaining the distinct converted output object,
[EPI-OBJ-conversation](epistemic.md#epi-obj-conversation). The supersession changes
identity resolution, not an evidence basis. Dropped feedback and loss flags
prevent assuming that every prospective training format retains rationale or
mask semantics. The remaining mixed containers are not superseded by their
operative parts.

Source-read log: none. Classification used the supplied accepted records and
reconciliation only; no new source evidence or declarations were introduced.

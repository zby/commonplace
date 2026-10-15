---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'AIDE2 memory profile: claimed trace-derived context and evaluation-guided harness retention
  in the frozen paper capture.'
run-id: AAS-2026-10-14-2609-26457-6b3bcd4791cf-01
source-identity: https://arxiv.org/abs/2609.26457
reviewed-boundary: arxiv-2609.26457v1-2026-10-14
memory-comparison:
  version: 2
  scope: Use-derived summaries, error signatures and reviewer results; retained score/strategy access
    metadata; previous proposal/grade and evaluation-artifact history; accepted harness code and its embedded
    instructions. Include unresolved debug/reviewer delivery and AIDE47/AIDEhuman bounded-history alternatives.
    Raw code/output is included only as accumulated later-consumed history or input to derived-memory
    updates. Exclude plain immediate execution state, static task inputs, fixed provider weights/internals,
    external benchmark implementation and wider production product.
  axes:
    storage_substrate:
      assessment: not-determinable
      units:
      - scope: AIDE85 summaries and error signatures
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-candidate-summary
        - memory.md#mem-rte-summary-delivery
        - memory.md#mem-obj-error-signatures
        - memory.md#mem-rte-failure-injection
        note: Prompt/context state is documented, but physical retention substrate is not. Prompt is a
          consumption channel, not evidence of files, in-memory storage or a prompt registry.
      - scope: Reviewer feedback, scores and accumulated strategy metadata
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-review-feedback
        - epistemic.md#epi-obj-evaluation-scores
        - memory.md#mem-obj-strategy-state
        note: Candidate-associated state and grading artifacts do not identify a controlled storage substrate.
      - scope: Accepted harness, embedded instructions and proposal/grade archive
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-agent-code
        - runtime.md#rt-obj-robustness-instruction
        - runtime.md#rt-rte-harness-admission
        note: A codebase does not establish Git/repo storage or a filesystem implementation; archive and
          reload are unknown.
      - scope: 'Other role and agent context routes: debug/reviewer payloads, AIDE47/AIDEhuman bounded-history
          alternatives, and outer evaluation artifacts'
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-clm-prompt-compression
        - runtime.md#rt-rte-harness-admission
        - epistemic.md#epi-rte-reviewer-extraction
        note: Full payloads, production rules and later delivery contracts are unavailable. AIDE85 witnesses
          do not classify these included alternatives.
      records:
      - memory.md#mem-obj-candidate-summary
      - memory.md#mem-rte-summary-delivery
      - memory.md#mem-obj-error-signatures
      - memory.md#mem-rte-failure-injection
      - memory.md#mem-obj-review-feedback
      - epistemic.md#epi-obj-evaluation-scores
      - memory.md#mem-obj-strategy-state
      - runtime.md#rt-obj-agent-code
      - runtime.md#rt-obj-robustness-instruction
      - runtime.md#rt-rte-harness-admission
      - memory.md#mem-clm-prompt-compression
      - epistemic.md#epi-rte-reviewer-extraction
      note: No controlled substrate is established for the included inventory. Fixed provider weights
        and static task inputs are excluded; encoding and delivery do not resolve storage.
    representational_form:
      assessment: partial
      units:
      - scope: AIDE85 summary at draft/improve interpretation
        assessment: partial
        findings:
        - value: natural-language
          basis: claimed
          records: &id001
          - memory.md#mem-obj-candidate-summary
          - memory.md#mem-rte-summary-delivery
          note: Readable descriptive context receives consequences through model interpretation.
        records: *id001
        note: Natural-language consumption is established; exact fields and possible code excerpts remain
          unresolved.
      - scope: Failure signatures at generation and deduplication/gating consumers
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records: &id002
          - memory.md#mem-obj-error-signatures
          - memory.md#mem-rte-failure-injection
          note: Error fragments advise the generator through interpretation.
        - value: symbolic
          basis: claimed
          records: *id002
          note: Deduplication of text and fixed count/rate gating use localized units and rules.
        records: *id002
        note: The documented fragment and rule-consumption paths are separated; no full diagnostic payload
          is inferred.
      - scope: Reviewer feedback text and score at their separate consumers
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records: &id003
          - memory.md#mem-obj-review-feedback
          - epistemic.md#epi-rte-reviewer-extraction
          note: Relevant feedback is model-interpreted text.
        - value: symbolic
          basis: claimed
          records: *id003
          note: Numerical score supplies fixed candidate-selection rules.
        records: *id003
        note: Known for the named text/score parts, not complete reviewer prompt encoding.
      - scope: Retained scores and strategy-label/best-score state at selectors
        assessment: known
        findings:
        - value: symbolic
          basis: claimed
          records: &id004
          - epistemic.md#epi-obj-evaluation-scores
          - memory.md#mem-obj-strategy-state
          note: Categorical labels and numeric scores feed explicit selection rules.
        records: *id004
        note: Numerical/categorical state is not distributed-parametric form.
      - scope: Retained harness rules and embedded prompt instructions
        assessment: partial
        findings:
        - value: symbolic
          basis: claimed
          records: &id005
          - runtime.md#rt-obj-agent-code
          - runtime.md#rt-obj-robustness-instruction
          - runtime.md#rt-bap-robustness-prompt
          note: Executable rules control search and context.
        - value: natural-language
          basis: claimed
          records: *id005
          note: Embedded standing instructions reach code-generation interpretation.
        records: *id005
        note: The full generated code and instruction decomposition remain unavailable.
      - scope: 'Other role and agent context routes: debug/reviewer payloads, AIDE47/AIDEhuman bounded-history
          alternatives, and outer evaluation artifacts'
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-clm-prompt-compression
        - runtime.md#rt-rte-harness-admission
        - epistemic.md#epi-rte-reviewer-extraction
        note: Full payloads, production rules and later delivery contracts are unavailable. AIDE85 witnesses
          do not classify these included alternatives.
      records:
      - memory.md#mem-obj-candidate-summary
      - memory.md#mem-rte-summary-delivery
      - memory.md#mem-obj-error-signatures
      - memory.md#mem-rte-failure-injection
      - memory.md#mem-obj-review-feedback
      - epistemic.md#epi-rte-reviewer-extraction
      - epistemic.md#epi-obj-evaluation-scores
      - memory.md#mem-obj-strategy-state
      - runtime.md#rt-obj-agent-code
      - runtime.md#rt-obj-robustness-instruction
      - runtime.md#rt-bap-robustness-prompt
      - memory.md#mem-clm-prompt-compression
      - runtime.md#rt-rte-harness-admission
      note: Documented text and symbolic consumers are positive witnesses; mixed summaries, full harness
        payloads and alternative prompts prevent complete coverage.
    lineage:
      assessment: partial
      units:
      - scope: Root/recent summary derivation
        assessment: known
        findings:
        - value: trace-extracted
          basis: claimed
          records: &id006
          - memory.md#mem-obj-candidate-summary
          - memory.md#mem-rte-summary-delivery
          - memory.md#mem-obj-execution-output
          note: Summary replaces earlier candidate code/output history.
        records: *id006
        note: Classifies the derivation path, not unknown summarizer authorship or initial task-code provenance.
      - scope: Final error-line signature derivation
        assessment: known
        findings:
        - value: trace-extracted
          basis: claimed
          records: &id007
          - memory.md#mem-obj-error-signatures
          - memory.md#mem-rte-failure-injection
          note: Recorded execution failures supply extracted and deduplicated final lines.
        records: *id007
        note: Trace origin is execution output; the result is not imported static guidance.
      - scope: Reviewer feedback and score derivation
        assessment: known
        findings:
        - value: trace-extracted
          basis: claimed
          records: &id008
          - memory.md#mem-obj-review-feedback
          - epistemic.md#epi-rte-reviewer-extraction
          - memory.md#mem-obj-execution-output
          note: Reviewer extracts score and relevant feedback from execution outputs.
        records: *id008
        note: Extraction lineage does not establish diagnostic fidelity.
      - scope: Outer harness successor and embedded instruction derivation
        assessment: partial
        findings:
        - value: authored
          basis: claimed
          records: &id009
          - runtime.md#rt-obj-agent-code
          - runtime.md#rt-rte-harness-admission
          - runtime.md#rt-obj-robustness-instruction
          note: Model proposer edits the incumbent; private-grade selection retains the successor.
        records: *id009
        note: Successor authorship is described, but initial AIDE0 content provenance and full embedded-part
          lineage are unresolved.
      - scope: Evaluation-fed scores and inherited labels
        assessment: partial
        findings:
        - value: trace-extracted
          basis: claimed
          records: &id010
          - epistemic.md#epi-obj-evaluation-scores
          - memory.md#mem-obj-strategy-state
          note: Evaluation outcomes supply retained numeric score state.
        records: *id010
        note: Fixed strategy vocabulary and initial label provenance are not a complete use-derived lineage
          account.
      - scope: 'Other role and agent context routes: debug/reviewer payloads, AIDE47/AIDEhuman bounded-history
          alternatives, and outer evaluation artifacts'
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-clm-prompt-compression
        - runtime.md#rt-rte-harness-admission
        - epistemic.md#epi-rte-reviewer-extraction
        note: Full payloads, production rules and later delivery contracts are unavailable. AIDE85 witnesses
          do not classify these included alternatives.
      records:
      - memory.md#mem-obj-candidate-summary
      - memory.md#mem-rte-summary-delivery
      - memory.md#mem-obj-execution-output
      - memory.md#mem-obj-error-signatures
      - memory.md#mem-rte-failure-injection
      - memory.md#mem-obj-review-feedback
      - epistemic.md#epi-rte-reviewer-extraction
      - runtime.md#rt-obj-agent-code
      - runtime.md#rt-rte-harness-admission
      - runtime.md#rt-obj-robustness-instruction
      - epistemic.md#epi-obj-evaluation-scores
      - memory.md#mem-obj-strategy-state
      - memory.md#mem-clm-prompt-compression
      note: Known derivation paths coexist with unresolved initial provenance and opaque artifacts. No
        imported or parametric lineage is inferred merely from setup or fixed models.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Derived summaries and signatures consumed by later draft/improve
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records: &id011
          - memory.md#mem-obj-candidate-summary
          - memory.md#mem-obj-error-signatures
          - memory.md#mem-rte-summary-delivery
          - memory.md#mem-rte-failure-injection
          note: Prior outcomes and error fragments supply advisory context, not guaranteed compliance.
        records: *id011
        note: The downstream advisory consumer is distinct from the transformation consumer.
      - scope: Raw execution history consumed by summary/signature and reviewer updates
        assessment: known
        findings:
        - value: learning
          basis: claimed
          records: &id012
          - memory.md#mem-obj-execution-output
          - memory.md#mem-rte-summary-delivery
          - memory.md#mem-rte-failure-injection
          - epistemic.md#epi-rte-reviewer-extraction
          note: Recorded experience feeds durable derived context or feedback for later search.
        records: *id012
        note: Learning names the update consumer, not demonstrated improved task capacity.
      - scope: Feedback text at subsequent generation
        assessment: partial
        findings:
        - value: knowledge
          basis: claimed
          records: &id013
          - memory.md#mem-obj-review-feedback
          - epistemic.md#epi-rte-reviewer-extraction
          note: Relevant execution feedback advises future code editing.
        records: *id013
        note: Exact delivery after filtering/summary is unresolved; no complete feedback-consumption guarantee
          follows.
      - scope: Scores and strategy labels at fixed inner and outer selectors
        assessment: known
        findings:
        - value: ranking
          basis: claimed
          records: &id014
          - epistemic.md#epi-obj-evaluation-scores
          - memory.md#mem-obj-strategy-state
          - runtime.md#rt-rte-harness-admission
          note: Retained scores determine relative candidate and arm priority.
        - value: routing
          basis: claimed
          records: *id014
          note: Labels and score state select the next arm/node or incumbent edit base.
        records: *id014
        note: These are explicit selector inputs, not new executable policies themselves.
      - scope: Previous proposals, grades and evaluation artifacts at outer rewriting
        assessment: partial
        findings:
        - value: knowledge
          basis: claimed
          records: &id015
          - runtime.md#rt-rte-harness-admission
          - runtime.md#rt-obj-agent-code
          note: Prior proposal/grade evidence guides the next rewrite.
        - value: learning
          basis: claimed
          records: *id015
          note: Evaluation experience feeds automatic durable harness revisions.
        records: *id015
        note: The documented update route is positive; exact artifact contents and rationale delivery
          remain unresolved.
      - scope: Accepted executable search/context rules at later executions
        assessment: partial
        findings:
        - value: routing
          basis: claimed
          records: &id016
          - runtime.md#rt-obj-agent-code
          - runtime.md#rt-rte-harness-admission
          - runtime.md#rt-bap-incumbent-code
          note: Retained harness rules determine next-candidate and context choices.
        - value: ranking
          basis: claimed
          records: *id016
          note: Harness selection rules prioritize candidate solutions.
        records: *id016
        note: Exact code decomposition is unavailable; this does not classify every retained control.
      - scope: Accepted robustness rules and reminder at their consumers
        assessment: known
        findings:
        - value: instruction
          basis: claimed
          records: &id017
          - runtime.md#rt-obj-robustness-instruction
          - runtime.md#rt-bap-robustness-prompt
          - runtime.md#rt-rte-robustness-controls
          note: Recurring reminder supplies standing directions to code generation.
        - value: validation
          basis: claimed
          records: *id017
          note: Retained short-output criterion checks generated task code length.
        - value: enforcement
          basis: claimed
          records: *id017
          note: The length guard requires re-prompting instead of ordinary continuation.
        records: *id017
        note: The criterion is a length proxy, not semantic correctness or outer harness admission.
      - scope: 'Other role and agent context routes: debug/reviewer payloads, AIDE47/AIDEhuman bounded-history
          alternatives, and outer evaluation artifacts'
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-clm-prompt-compression
        - runtime.md#rt-rte-harness-admission
        - epistemic.md#epi-rte-reviewer-extraction
        note: Full payloads, production rules and later delivery contracts are unavailable. AIDE85 witnesses
          do not classify these included alternatives.
      records:
      - memory.md#mem-obj-candidate-summary
      - memory.md#mem-obj-error-signatures
      - memory.md#mem-rte-summary-delivery
      - memory.md#mem-rte-failure-injection
      - memory.md#mem-obj-execution-output
      - epistemic.md#epi-rte-reviewer-extraction
      - memory.md#mem-obj-review-feedback
      - epistemic.md#epi-obj-evaluation-scores
      - memory.md#mem-obj-strategy-state
      - runtime.md#rt-rte-harness-admission
      - runtime.md#rt-obj-agent-code
      - runtime.md#rt-bap-incumbent-code
      - runtime.md#rt-obj-robustness-instruction
      - runtime.md#rt-bap-robustness-prompt
      - runtime.md#rt-rte-robustness-controls
      - memory.md#mem-clm-prompt-compression
      note: Authority is consumer-specific. Update learning and downstream knowledge/instruction are separate.
        Unknown full payloads prevent an exhaustive force inventory.
    write_agency:
      assessment: partial
      units:
      - scope: Summary inclusion in later prompts
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id018
          - memory.md#mem-rte-summary-delivery
          note: Harness root/recent selection admits context without per-summary human approval.
        records: *id018
        note: Known delivery admission does not resolve summary creation control.
      - scope: Summary creation admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-candidate-summary
        - memory.md#mem-rte-summary-delivery
        note: Producer and production control are not stated; automatic inclusion alone does not classify
          every creation mechanism.
      - scope: Signature extraction/deduplication and gated admission
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id019
          - memory.md#mem-obj-error-signatures
          - memory.md#mem-rte-failure-injection
          note: Software selects execution fragments using bug-rate gate and cap.
        records: *id019
        note: Human experiment setup is not per-signature approval.
      - scope: Reviewer score/feedback extraction and strategy state updates
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id020
          - memory.md#mem-obj-review-feedback
          - epistemic.md#epi-rte-reviewer-extraction
          - memory.md#mem-obj-strategy-state
          note: Model extraction and software label/score updating have no described per-content human
            decision.
        records: *id020
        note: Model authorship and physical I/O are distinct from admission.
      - scope: Harness successor and embedded-instruction admission
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id021
          - runtime.md#rt-obj-agent-code
          - runtime.md#rt-rte-harness-admission
          - runtime.md#rt-obj-robustness-instruction
          note: Model proposes; fixed private-grade selector admits or rejects code.
        records: *id021
        note: Experiment initiation does not make each successor manual.
      - scope: Initial content and opaque artifact admission mechanisms
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-agent-code
        - memory.md#mem-clm-prompt-compression
        - runtime.md#rt-rte-harness-admission
        note: Initial task/harness content control and alternative artifact-production mechanisms are
          not specified; no manual finding follows from designer participation.
      records:
      - memory.md#mem-rte-summary-delivery
      - memory.md#mem-obj-candidate-summary
      - memory.md#mem-obj-error-signatures
      - memory.md#mem-rte-failure-injection
      - memory.md#mem-obj-review-feedback
      - epistemic.md#epi-rte-reviewer-extraction
      - memory.md#mem-obj-strategy-state
      - runtime.md#rt-obj-agent-code
      - runtime.md#rt-rte-harness-admission
      - runtime.md#rt-obj-robustness-instruction
      - memory.md#mem-clm-prompt-compression
      note: Automatic mechanisms are documented locally; unknown summary creation, initialization and
        alternative artifacts prevent complete agency coverage.
    curation_operations:
      assessment: partial
      units:
      - scope: Root/recent retained-history compaction
        assessment: known
        findings:
        - value: consolidate
          basis: claimed
          records: &id022
          - memory.md#mem-obj-candidate-summary
          - memory.md#mem-rte-summary-delivery
          note: Selection and compression reduce existing candidate code/output history.
        records: *id022
        note: Unknown semantic fidelity does not imply synthesis; no deletion or decay is established.
      - scope: Retained failure-fragment extraction and merging
        assessment: known
        findings:
        - value: consolidate
          basis: claimed
          records: &id023
          - memory.md#mem-obj-error-signatures
          - memory.md#mem-rte-failure-injection
          note: Final-line extraction reduces earlier execution output.
        - value: dedup
          basis: claimed
          records: *id023
          note: Repeated error signatures are deduplicated before delivery.
        records: *id023
        note: Truncation and deduplication do not establish causal diagnosis.
      - scope: Reviewer reduction of execution output
        assessment: partial
        findings:
        - value: consolidate
          basis: claimed
          records: &id024
          - memory.md#mem-obj-review-feedback
          - epistemic.md#epi-rte-reviewer-extraction
          note: Score and relevant feedback reduce execution history for search.
        records: *id024
        note: Concrete reviewer outputs are missing; additional semantic transformation is not determinable.
      - scope: Incumbent harness revision and acceptance
        assessment: known
        findings:
        - value: evolve
          basis: claimed
          records: &id025
          - runtime.md#rt-obj-agent-code
          - runtime.md#rt-rte-harness-admission
          note: Successor proposal revises the current retained harness.
        - value: promote
          basis: claimed
          records: *id025
          note: Private-grade acceptance raises a proposal to operative incumbent for later editing and
            runs.
        records: *id025
        note: Rejected adoption is not proven history deletion, invalidation or expiry.
      - scope: AIDE47 bounded-history compaction
        assessment: partial
        findings:
        - value: consolidate
          basis: claimed
          records:
          - memory.md#mem-clm-prompt-compression
          note: The record identifies AIDE47 bounded history and describes discovered agents replacing
            prior code/output history with bounded summaries.
        records:
        - memory.md#mem-clm-prompt-compression
        note: Bounded compression supports consolidation independently of AIDE85; exact payloads,
          production rules and any additional transformations remain unresolved.
      - scope: AIDEhuman context transformations and outer archive maintenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-clm-prompt-compression
        - runtime.md#rt-rte-harness-admission
        note: Prompt-size comparison does not expose AIDEhuman transformations; outer archive maintenance
          rules remain unavailable. Neither uncertainty establishes absence of compaction or maintenance.
      records:
      - memory.md#mem-obj-candidate-summary
      - memory.md#mem-rte-summary-delivery
      - memory.md#mem-obj-error-signatures
      - memory.md#mem-rte-failure-injection
      - memory.md#mem-obj-review-feedback
      - epistemic.md#epi-rte-reviewer-extraction
      - runtime.md#rt-obj-agent-code
      - runtime.md#rt-rte-harness-admission
      - memory.md#mem-clm-prompt-compression
      note: Only documented transformations receive claimed findings. No implementation is inspected,
        no novel claim is established, and maintenance alternatives remain opaque.
    read_back_direction:
      assessment: partial
      units:
      - scope: AIDE85 summary and signature supply
        assessment: known
        findings:
        - value: push
          basis: claimed
          records: &id026
          - memory.md#mem-rte-summary-delivery
          - memory.md#mem-rte-failure-injection
          note: Prompt assembly selects earlier derived history without a foreground memory request.
        records: *id026
        note: Root/recent selection and conditional error injection are independent supply operations.
      - scope: AIDE0 accumulated code/output at later generation
        assessment: known
        findings:
        - value: push
          basis: claimed
          records: &id027
          - memory.md#mem-clm-prompt-compression
          - memory.md#mem-obj-execution-output
          note: Harness concatenates prior candidate history into drafting/improvement prompts.
        records: *id027
        note: This read concerns prior retained trace input to later calls, not arbitrary current state.
      - scope: Outer history and incumbent reuse
        assessment: partial
        findings:
        - value: push
          basis: claimed
          records: &id028
          - runtime.md#rt-rte-harness-admission
          - runtime.md#rt-obj-agent-code
          note: Outer-step protocol supplies prior agents/grades and the incumbent edit base for next
            rewriting and execution.
        records: *id028
        note: Artifact exploration includes unspecified requests and delivery; no complete push-only boundary
          is established.
      - scope: Reviewer feedback delivery, artifact exploration and other agent prompts
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-reviewer-extraction
        - memory.md#mem-clm-prompt-compression
        - runtime.md#rt-rte-harness-admission
        note: Full payloads, production rules and later delivery contracts are unavailable. AIDE85 witnesses
          do not classify these included alternatives.
      records:
      - memory.md#mem-rte-summary-delivery
      - memory.md#mem-rte-failure-injection
      - memory.md#mem-clm-prompt-compression
      - memory.md#mem-obj-execution-output
      - runtime.md#rt-rte-harness-admission
      - runtime.md#rt-obj-agent-code
      - epistemic.md#epi-rte-reviewer-extraction
      note: Documented automatic supply supports push. Unspecified exploration/reload does not establish
        pull, absence of pull, or complete direction coverage.
    read_back_signal:
      assessment: partial
      units:
      - scope: Root/recent summary push selector
        assessment: known
        findings:
        - value: coarse
          basis: claimed
          records: &id029
          - memory.md#mem-rte-summary-delivery
          - memory.md#mem-obj-candidate-summary
          note: Draft/improve assembly selects root and recency-window material, not query matching.
        records: *id029
        note: Trigger is prompt assembly; selector input is root/recent membership; selected retained
          part is the compact history account.
      - scope: Failure-signature push selector
        assessment: known
        findings:
        - value: coarse
          basis: claimed
          records: &id030
          - memory.md#mem-rte-failure-injection
          - memory.md#mem-obj-error-signatures
          note: Bug-rate threshold, recurrence, recency, deduplication and cap select error fragments.
        records: *id030
        note: Trigger is prompt assembly at bug rate at least 15%; input is recent failed outputs; selected
          part is at most three final lines. Text dedup is not lexical query retrieval.
      - scope: Full-history automatic supply
        assessment: known
        findings:
        - value: coarse
          basis: claimed
          records: &id031
          - memory.md#mem-clm-prompt-compression
          - memory.md#mem-obj-execution-output
          note: Every prior candidate code/output is included as available history.
        records: *id031
        note: Trigger is drafting/improvement; prior-history availability selects material without targeting
          a query.
      - scope: Outer proposal/grade supply and incumbent choice
        assessment: partial
        findings:
        - value: coarse
          basis: claimed
          records: &id032
          - runtime.md#rt-rte-harness-admission
          - runtime.md#rt-obj-agent-code
          note: Outer step supplies prior proposal/grade history and best-grade incumbent.
        records: *id032
        note: Grade comparison and availability are coarse selection; no documented identity-match delivery,
          exact budget or complete artifact selector.
      - scope: Other payload selection and artifact exploration
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-clm-prompt-compression
        - epistemic.md#epi-rte-reviewer-extraction
        - runtime.md#rt-rte-harness-admission
        note: Full payloads, production rules and later delivery contracts are unavailable. AIDE85 witnesses
          do not classify these included alternatives.
      records:
      - memory.md#mem-rte-summary-delivery
      - memory.md#mem-obj-candidate-summary
      - memory.md#mem-rte-failure-injection
      - memory.md#mem-obj-error-signatures
      - memory.md#mem-clm-prompt-compression
      - memory.md#mem-obj-execution-output
      - runtime.md#rt-rte-harness-admission
      - runtime.md#rt-obj-agent-code
      - epistemic.md#epi-rte-reviewer-extraction
      note: Coarse supply is supported locally. No embedding, lexical query, inferred judgment or identifier
        matching is established for the recorded pushes; unresolved routes remain included.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic signature update to later generation context
        assessment: known
        findings:
        - value: 'yes'
          basis: claimed
          records: &id033
          - memory.md#mem-obj-error-signatures
          - memory.md#mem-rte-failure-injection
          - memory.md#mem-bap-history-context
          note: Execution traces feed extracted/deduplicated retained fragments consumed in later generation.
        records: *id033
        note: Qualifies within a task run; does not require cross-task memory or observed improvement.
      - scope: Summary creation and later automatic delivery
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-candidate-summary
        - memory.md#mem-rte-summary-delivery
        - memory.md#mem-clm-prompt-compression
        note: Earlier code/output history feeds a retained summary consumed by later draft/improve calls,
          but production control is unspecified. Automatic inclusion establishes delivery admission,
          not an automatic trace-fed write producing the summary; neither yes nor no is established.
      - scope: Reviewer extraction and later score selection
        assessment: partial
        findings:
        - value: 'yes'
          basis: claimed
          records: &id035
          - memory.md#mem-obj-review-feedback
          - epistemic.md#epi-rte-reviewer-extraction
          - runtime.md#rt-rte-inner-search
          note: Automatic model extraction transforms execution feedback into retained score/feedback
            shaping subsequent search.
        records: *id035
        note: Score-selection path is documented; exact feedback delivery and persistence are unresolved.
      - scope: Evaluation-guided harness rewrite and private admission
        assessment: known
        findings:
        - value: 'yes'
          basis: claimed
          records: &id036
          - runtime.md#rt-rte-harness-admission
          - runtime.md#rt-obj-agent-code
          - runtime.md#rt-bap-incumbent-code
          note: Prior evaluation artifacts/grades feed automatic rewrites retained as incumbent code and
            consumed in later operation.
        records: *id036
        note: Durable behavior-shaping code, not model-weight training. Only claimed route evidence is
          available.
      - scope: Other bounded-history alternatives and opaque artifact updates
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-clm-prompt-compression
        - runtime.md#rt-rte-harness-admission
        note: Full payloads, production rules and later delivery contracts are unavailable. AIDE85 witnesses
          do not classify these included alternatives.
      records:
      - memory.md#mem-obj-error-signatures
      - memory.md#mem-rte-failure-injection
      - memory.md#mem-bap-history-context
      - memory.md#mem-obj-candidate-summary
      - memory.md#mem-rte-summary-delivery
      - memory.md#mem-clm-prompt-compression
      - memory.md#mem-obj-review-feedback
      - epistemic.md#epi-rte-reviewer-extraction
      - runtime.md#rt-rte-inner-search
      - runtime.md#rt-rte-harness-admission
      - runtime.md#rt-obj-agent-code
      - runtime.md#rt-bap-incumbent-code
      note: Positive claimed automatic trace-fed writes coexist with unresolved mechanisms. No bounded
        absence record supports a local or system-wide no.
    trace_source:
      assessment: partial
      units:
      - scope: Signature extraction input
        assessment: known
        findings:
        - value: tool-traces
          basis: claimed
          records: &id037
          - memory.md#mem-obj-execution-output
          - memory.md#mem-obj-error-signatures
          - memory.md#mem-rte-failure-injection
          note: Original input is recorded execution failure output from candidate evaluation.
        records: *id037
        note: Final error lines remain execution traces, not session logs or event streams merely because
          emitted at runtime.
      - scope: Root/recent summary input
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-candidate-summary
        - memory.md#mem-rte-summary-delivery
        - memory.md#mem-obj-execution-output
        - memory.md#mem-clm-prompt-compression
        note: Replaced history includes candidate execution output and code, but unknown summary creation
          control prevents establishing a qualifying automatic trace-learning write. No trace_source value
          is assigned to this unresolved route; this does not deny its recorded trace-extracted lineage.
      - scope: Reviewer extraction input
        assessment: known
        findings:
        - value: tool-traces
          basis: claimed
          records: &id039
          - memory.md#mem-obj-execution-output
          - memory.md#mem-obj-review-feedback
          - epistemic.md#epi-rte-reviewer-extraction
          note: Reviewer consumes recorded execution outputs.
        records: *id039
        note: Classifies input content, not the reviewer call label.
      - scope: Outer harness update input
        assessment: partial
        findings:
        - value: tool-traces
          basis: claimed
          records: &id040
          - runtime.md#rt-rte-harness-admission
          - runtime.md#rt-obj-agent-code
          - epistemic.md#epi-obj-evaluation-scores
          note: Evaluation artifacts and grades originate in task execution and its scoring feedback.
        - value: trajectories
          basis: claimed
          records: *id040
          note: Prior proposed harnesses and their grades form the linked outer sequence used to edit
            the incumbent again.
        records: *id040
        note: Mixed artifact contents, raw-versus-derived distinctions and full proposal history are unresolved;
          known sequence does not classify all inputs.
      - scope: Other context alternatives and opaque update inputs
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-clm-prompt-compression
        - runtime.md#rt-rte-harness-admission
        note: Full payloads, production rules and later delivery contracts are unavailable. AIDE85 witnesses
          do not classify these included alternatives.
      records:
      - memory.md#mem-obj-execution-output
      - memory.md#mem-obj-error-signatures
      - memory.md#mem-rte-failure-injection
      - memory.md#mem-obj-candidate-summary
      - memory.md#mem-rte-summary-delivery
      - memory.md#mem-clm-prompt-compression
      - memory.md#mem-obj-review-feedback
      - epistemic.md#epi-rte-reviewer-extraction
      - runtime.md#rt-rte-harness-admission
      - runtime.md#rt-obj-agent-code
      - epistemic.md#epi-obj-evaluation-scores
      note: Trace source is assessed per qualifying update. No session-log or event-stream classification
        follows solely from prompt delivery or serialization; mixed opaque inputs prevent complete coverage.
---

# AIDE2 memory profile

## Comparison rationale

All positive findings are **claimed**. The accepted members retain doctrine/design and author-reported operation from the frozen paper, not inspected implementation, observed raw runs or causal experiments; see [RT-RTE-harness-admission](runtime.md#rt-rte-harness-admission) and [MEM-RTE-summary-delivery](memory.md#mem-rte-summary-delivery). Their operation reports do not justify upgrading a profile basis to observed. Coverage assessments describe classification completeness within each named unit, not execution reliability.

The inventory separates reduced history, failure fragments, reviewer text/scores, selector metadata, outer history and retained executable organization. A codebase or assembled prompt does not identify its physical substrate. All storage units therefore remain not-determinable. Fixed provider parameters do not enter this use-derived memory boundary; the profile does not claim an absence of provider state.

The reconciliation supersedes the epistemic summary and signature declarations with [MEM-OBJ-candidate-summary](memory.md#mem-obj-candidate-summary) and [MEM-OBJ-error-signatures](memory.md#mem-obj-error-signatures). Findings cite those canonical records. Reviewer feedback and evaluation scores remain overlapping material parts rather than whole-record duplicates. [MEM-OBJ-review-feedback](memory.md#mem-obj-review-feedback) distinguishes numerical selection from interpreted feedback; [EPI-OBJ-evaluation-scores](epistemic.md#epi-obj-evaluation-scores) also covers private grade aggregation.

Consolidation classifies selection/compression of existing history, not proven semantic faithfulness. Unknown summary authorship remains beside automatic context admission. The signature route separately establishes extraction, deduplication, admission and later consumption. Neither mechanism establishes synthesis, retained causal explanations, expiry or deletion. The summary chain's trace-learning classification remains not-determinable because automatic later delivery does not establish automatic summary production. Its trace_source classification likewise remains unresolved: recorded execution input alone cannot establish a source value for a write that has not been shown to qualify. Consolidation, trace-extracted lineage and later knowledge consumption remain supported independently. See [MEM-RTE-summary-delivery](memory.md#mem-rte-summary-delivery) and [MEM-RTE-failure-injection](memory.md#mem-rte-failure-injection).

Read-back direction separates unsolicited harness supply from unspecified artifact exploration. Root/recency selection and threshold/recurrence filtering are coarse push signals. Text equality used to deduplicate errors is not a lexical retrieval query; node labels do not establish identifier-based delivery. Unknown exploration and alternative role prompts prevent a complete push-only conclusion.

Outer learning is a different route: evaluation experience guides automatic code rewriting and grade-controlled adoption, and accepted code governs subsequent work. Updating the incumbent is evolution; selecting a proposal as incumbent is promotion. Prior code/grade sequences support a trajectories finding, while execution/scoring feedback supports tool-traces. Opaque evaluation artifacts prevent a complete source inventory. The relevant route is [RT-RTE-harness-admission](runtime.md#rt-rte-harness-admission), with downstream force in [RT-BAP-incumbent-code](runtime.md#rt-bap-incumbent-code).

The robustness reminder is included because it is embedded in retained, automatically admitted successor code, not because static shipped instructions alone count as accumulated memory. Its standing instruction force differs from derived history's knowledge force. The short-code criterion concerns generated task scripts, not outer successor admission; its validation and enforced retry are separate from private-grade selection. See [RT-RTE-robustness-controls](runtime.md#rt-rte-robustness-controls).

No axis claims bounded absence. Unknown initialization, summary fields/control, artifact payloads, alternative-agent prompts, feedback delivery, archive retention and reload prevent stronger inventory conclusions. Positive trace-learning findings establish the documented trace-fed write/consumer routes, not independently verified improved capacity, component benefit or weight updates.

Source-read log: none. Classification used only supplied accepted members and their reconciliation; no capture read, new evidence or new record was needed.

---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Incremental self-improvement's documented in-life retained state and later-consumer routes
  in the revised FKI-198-94 capture.
run-id: AAS-2026-10-14-fki198-94-pdf-90fb0a2a9508-01
source-identity: https://people.idsia.ch/~juergen/fki198-94.pdf
reviewed-boundary: fki198-94-revised-1995-01-31-captured-2026-10-14-text
memory-comparison:
  version: 2
  scope: 'Documented single-life memory: live policy distributions; stack oldP and evaluation/access metadata;
    work inputs, GetP snapshots, registers and arbitrary retained integers; external variable values and
    retained navigation state; their automatic write, retention, restoration and later-consumer routes.
    Documentary alternatives include prior-code reuse, direct teacher protection and circular history
    overwrite only at their claimed/proposed strength. Excludes shipped static primitive/evaluator definitions,
    transient comparison predicates, base-design sampled code with no later reuse, ordinary immediate
    action effects without a later retained-state consumer, referenced systems, proposed neural variants,
    and unsupported restart durability. Navigation representation and arbitrary history semantics remain
    included but unresolved.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: 'Internal work cells: inputs, GetP snapshots, registers and remaining integers'
        assessment: known
        findings:
        - value: in-memory
          basis: claimed
          records: &id001
          - runtime.md#rt-obj-work-area
          - epistemic.md#epi-obj-input-cells
          - epistemic.md#epi-obj-getp-values
          note: Retained cell values survive run halts; no restart serialization is established.
        records: *id001
        note: The documentary inventory places all these parts in the same in-life addressable array;
          semantic uncertainty does not obscure its substrate.
      - scope: Live policy table
        assessment: known
        findings:
        - value: in-memory
          basis: claimed
          records: &id002
          - runtime.md#rt-cmp-probability-distributions
          note: Program-address-associated arrays retain updates for later sampling.
        records: *id002
        note: The documented distributions are runtime numerical arrays.
      - scope: Stack distribution payload oldP and access/evaluation metadata
        assessment: known
        findings:
        - value: in-memory
          basis: claimed
          records: &id003
          - runtime.md#rt-obj-stack
          note: Saved distributions and t/R/address/first records persist until popping or proposed overwrite.
        records: *id003
        note: Both parts occupy the finite in-life stack; payload encoding is not a separate storage technology.
      - scope: External variable array
        assessment: known
        findings:
        - value: in-memory
          basis: claimed
          records: &id004
          - memory.md#mem-obj-variable-array
          note: Variables retain agent writes until overwrite or periodic reset in the documented experiment.
        records: *id004
        note: The task describes an integer array, not a service or disk store.
      - scope: Proposed reuse of previous sampled program-cell contents
        assessment: known
        findings:
        - value: in-memory
          basis: claimed
          records: &id005
          - runtime.md#rt-obj-program-area
          note: The proposal reuses values already held in the addressable program array.
        records: *id005
        note: Included only as a documentary alternative, not as activated experimental memory.
      - scope: Retained navigation-environment position between actions
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-instruction-cycle
        - runtime.md#rt-rte-credit-assignment
        - epistemic.md#epi-rte-input-supply
        note: The documented maze retains and changes task state, but these records do not specify its
          operative storage representation. No substrate value can be assigned to that part.
      records:
      - runtime.md#rt-obj-work-area
      - epistemic.md#epi-obj-input-cells
      - epistemic.md#epi-obj-getp-values
      - runtime.md#rt-cmp-probability-distributions
      - runtime.md#rt-obj-stack
      - memory.md#mem-obj-variable-array
      - runtime.md#rt-obj-program-area
      - runtime.md#rt-rte-instruction-cycle
      - runtime.md#rt-rte-credit-assignment
      - epistemic.md#epi-rte-input-supply
      note: All documented retained arrays and stack parts are classified. Navigation state substrate
        remains unresolved; files and restart persistence are not inferred from a paper capture.
    representational_form:
      assessment: partial
      units:
      - scope: Work input encodings and GetP snapshot consumption
        assessment: known
        findings:
        - value: symbolic
          basis: claimed
          records: &id006
          - epistemic.md#epi-obj-input-cells
          - epistemic.md#epi-obj-getp-values
          - memory.md#mem-rte-getp-read
          - epistemic.md#epi-rte-input-supply
          note: Inputs encode task/runtime quantities; GetP produces a scaled, localized probability value.
        records: *id006
        note: Defined integer referents are consumed under fixed primitive semantics.
      - scope: Remaining work-cell operands
        assessment: known
        findings:
        - value: symbolic
          basis: claimed
          records: &id007
          - runtime.md#rt-obj-work-area
          - runtime.md#rt-rte-instruction-cycle
          note: Addressed integers feed arithmetic, branch and operand rules; universality does not establish
            natural-language interpretation.
        records: *id007
        note: Arbitrary meanings remain unresolved, but the operative encoding and interpreter consumption
          are fixed integer operations.
      - scope: Live Pi at sampler and GetP
        assessment: known
        findings:
        - value: symbolic
          basis: claimed
          records: &id008
          - runtime.md#rt-cmp-probability-distributions
          - runtime.md#rt-bap-probability-selection
          - memory.md#mem-rte-getp-read
          note: The addressed probability table has individually identified values and fixed consumer
            rules.
        records: *id008
        note: Localized numerical entries with fixed sampling and scaling rules are not distributed-parametric
          representations.
      - scope: Stack oldP payload and metadata at fixed evaluator
        assessment: known
        findings:
        - value: symbolic
          basis: claimed
          records: &id009
          - runtime.md#rt-obj-stack
          - runtime.md#rt-rte-credit-assignment
          - epistemic.md#epi-rte-rate-comparison
          note: oldP restores an addressed table; t/R/first/address support grouping and historical comparisons.
        records: *id009
        note: Numerical vectors and structured bookkeeping both have localized fields and fixed interpretation.
      - scope: External variable values at Read and task scoring
        assessment: known
        findings:
        - value: symbolic
          basis: claimed
          records: &id010
          - memory.md#mem-obj-variable-array
          - memory.md#mem-rte-variable-readback
          - workflow.md#wf-rte-variable-cycle
          note: Read copies selected values; scoring compares each value with its address.
        records: *id010
        note: Integer values have fixed transfer and equality-test semantics.
      - scope: Proposed instruction reuse at interpreter
        assessment: known
        findings:
        - value: symbolic
          basis: claimed
          records: &id011
          - runtime.md#rt-obj-program-area
          note: Reused instructions and arguments are localized symbolic code, not language guidance.
        records: *id011
        note: The alternative consumes previously sampled integer code under primitive semantics.
      - scope: Retained navigation position encoding
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-instruction-cycle
        - epistemic.md#epi-rte-input-supply
        note: The records describe movement and local input encodings, not the retained environment-position
          representation. Input integers cannot classify an unrecorded internal environment payload.
      records:
      - epistemic.md#epi-obj-input-cells
      - epistemic.md#epi-obj-getp-values
      - memory.md#mem-rte-getp-read
      - epistemic.md#epi-rte-input-supply
      - runtime.md#rt-obj-work-area
      - runtime.md#rt-rte-instruction-cycle
      - runtime.md#rt-cmp-probability-distributions
      - runtime.md#rt-bap-probability-selection
      - runtime.md#rt-obj-stack
      - runtime.md#rt-rte-credit-assignment
      - epistemic.md#epi-rte-rate-comparison
      - memory.md#mem-obj-variable-array
      - memory.md#mem-rte-variable-readback
      - workflow.md#wf-rte-variable-cycle
      - runtime.md#rt-obj-program-area
      note: All explicitly described payloads and consumption paths are symbolic. Navigation inputs are
        known encodings but do not resolve the environment state that produces them.
    lineage:
      assessment: partial
      units:
      - scope: Work input-cell updates
        assessment: known
        findings:
        - value: imported
          basis: claimed
          records: &id012
          - epistemic.md#epi-obj-input-cells
          - epistemic.md#epi-rte-input-supply
          note: Encoded task observations and runtime quantities enter the retained work-cell part from
            their task/runtime producers.
        records: *id012
        note: Task/runtime quantities are supplied to work inputs; birth zeros are a separate fixed initialization,
          not human content adoption.
      - scope: GetP snapshots
        assessment: known
        findings:
        - value: other-compiled
          basis: claimed
          records: &id013
          - epistemic.md#epi-obj-getp-values
          - memory.md#mem-rte-getp-read
          note: Fixed GetP semantics derive a localized numerical snapshot from Pi.
        records: *id013
        note: The derivation is scaling/rounding a current policy value, without an experience-log source.
      - scope: Remaining work values
        assessment: partial
        findings:
        - value: other-compiled
          basis: claimed
          records: &id014
          - runtime.md#rt-obj-work-area
          - runtime.md#rt-rte-instruction-cycle
          note: Zero initialization and fixed instruction computations produce integer values.
        records: *id014
        note: The records establish software initialization and instruction computation, not the semantic
          provenance of every value.
      - scope: Live policy distributions
        assessment: known
        findings:
        - value: other-compiled
          basis: claimed
          records: &id015
          - runtime.md#rt-cmp-probability-distributions
          - runtime.md#rt-rte-self-modification
          - runtime.md#rt-rte-credit-assignment
          note: The live table is initialized and transformed by fixed numerical operations over modifier
            operands and saved oldP.
        records: *id015
        note: Maximum-entropy initialization, computed modifiers and restoration paths are documented
          separately from claims of beneficial learning.
      - scope: Stack oldP payload
        assessment: known
        findings:
        - value: other-compiled
          basis: claimed
          records: &id016
          - runtime.md#rt-obj-stack
          - runtime.md#rt-rte-self-modification
          note: The saved policy vector is a software-produced copy of the prior live distribution.
        records: *id016
        note: An effective modifier copies an existing distribution before changing it.
      - scope: Stack time/payoff and modification bookkeeping
        assessment: known
        findings:
        - value: trace-extracted
          basis: claimed
          records: &id017
          - runtime.md#rt-obj-stack
          - runtime.md#rt-rte-credit-assignment
          - epistemic.md#epi-rte-rate-comparison
          note: Saved t/R/address/first retain selected numerical facts from runtime modification and
            payoff history.
        records: *id017
        note: The fields record modification events and historical outcome baselines, not full sessions
          or replayable programs.
      - scope: External variable contents
        assessment: known
        findings:
        - value: other-compiled
          basis: claimed
          records: &id018
          - memory.md#mem-obj-variable-array
          - memory.md#mem-rte-variable-readback
          - workflow.md#wf-rte-variable-cycle
          note: Task software and sampled agent computations initialize or derive the retained integers.
        records: *id018
        note: Initialization and resets write zeros; Write copies a program-computed work value.
      - scope: Proposed reused program-cell code
        assessment: known
        findings:
        - value: other-compiled
          basis: claimed
          records: &id019
          - runtime.md#rt-obj-program-area
          - runtime.md#rt-rte-instruction-cycle
          note: The interpreter produces integer code by sampling the addressed distributions.
        records: *id019
        note: The prior sample would be reused rather than compiled into a successful-program archive.
      - scope: Navigation-environment retained state derivation
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-instruction-cycle
        - epistemic.md#epi-rte-input-supply
        note: Movement and reset effects are documented, but the records do not expose a complete derivation
          path for its retained representation.
      records:
      - epistemic.md#epi-obj-input-cells
      - epistemic.md#epi-rte-input-supply
      - epistemic.md#epi-obj-getp-values
      - memory.md#mem-rte-getp-read
      - runtime.md#rt-obj-work-area
      - runtime.md#rt-rte-instruction-cycle
      - runtime.md#rt-cmp-probability-distributions
      - runtime.md#rt-rte-self-modification
      - runtime.md#rt-rte-credit-assignment
      - runtime.md#rt-obj-stack
      - epistemic.md#epi-rte-rate-comparison
      - memory.md#mem-obj-variable-array
      - memory.md#mem-rte-variable-readback
      - workflow.md#wf-rte-variable-cycle
      - runtime.md#rt-obj-program-area
      note: Positive derivation paths are retained without claiming complete semantic lineage of arbitrary
        work values or navigation state. No human-authored standing memory or embedding provenance is
        established.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Live Pi at later instruction/argument sampler
        assessment: known
        findings:
        - value: ranking
          basis: claimed
          records: &id020
          - runtime.md#rt-cmp-probability-distributions
          - runtime.md#rt-bap-probability-selection
          note: Relative probability values weight alternatives in sampling.
        - value: routing
          basis: claimed
          records: *id020
          note: The retained table selects primitive and argument outcomes through fixed probabilistic
            sampling.
        records: *id020
        note: This consumer selects code, not a truth-apt proposition or standing natural-language instruction.
      - scope: Current Pi at GetP and snapshots at later computations
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records: &id021
          - runtime.md#rt-cmp-probability-distributions
          - memory.md#mem-rte-getp-read
          - epistemic.md#epi-obj-getp-values
          note: Selected current values and their snapshots supply numerical self-reference to program
            computation.
        records: *id021
        note: GetP provides current-policy reference data; subsequent arithmetic use is afforded, not
          observed.
      - scope: Input cells at selected later primitive operands
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records: &id022
          - epistemic.md#epi-obj-input-cells
          - epistemic.md#epi-rte-input-supply
          - runtime.md#rt-rte-instruction-cycle
          note: Task/runtime observations provide input information to later computation.
        records: *id022
        note: Encoded observations supply data, with conditional source warrant; individual exercised
          effects remain uninspected.
      - scope: Registers and addressed work values at indirect addressing and branching
        assessment: partial
        findings:
        - value: routing
          basis: claimed
          records: &id023
          - runtime.md#rt-obj-work-area
          - runtime.md#rt-rte-instruction-cycle
          note: Address and branch operands select operations, destinations and work/environment inputs.
        records: *id023
        note: Documented operand/control roles are positive; arbitrary cells may have additional unresolved
          roles.
      - scope: Stack historical t/R at rate comparison and policy retention
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records: &id024
          - runtime.md#rt-obj-stack
          - epistemic.md#epi-rte-rate-comparison
          - runtime.md#rt-rte-credit-assignment
          note: Saved measurements supply historical evidence for the comparison.
        - value: learning
          basis: claimed
          records: *id024
          note: Experience baselines and live payoff feed automatic durable policy retention or restoration.
        - value: validation
          basis: claimed
          records: *id024
          note: Historical baselines determine the comparative criterion for continued admissibility.
        - value: enforcement
          basis: claimed
          records: *id024
          note: Non-exceedance against these baselines drives rejection and restoration by design.
        records: *id024
        note: Measurements and baselines feed the fixed evaluator; this is not acceptance of an explanatory
          claim.
      - scope: Stack address/first metadata at grouping and restoration
        assessment: known
        findings:
        - value: routing
          basis: claimed
          records: &id025
          - runtime.md#rt-obj-stack
          - runtime.md#rt-rte-credit-assignment
          note: Metadata selects the grouped historical entries and addressed live distributions to restore.
        records: *id025
        note: Fields identify restoration destinations and self-modification groups.
      - scope: Stack oldP at restoration and later sampler
        assessment: known
        findings:
        - value: routing
          basis: claimed
          records: &id026
          - runtime.md#rt-obj-stack
          - runtime.md#rt-rte-credit-assignment
          - runtime.md#rt-bap-probability-selection
          note: Restored probability entries again govern later operation selection.
        records: *id026
        note: The payload replaces live policy rather than supplying an explanatory rationale.
      - scope: External variables at explicit Read and periodic scorer
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records: &id027
          - memory.md#mem-obj-variable-array
          - memory.md#mem-rte-variable-readback
          - workflow.md#wf-rte-variable-cycle
          note: Read and scorer consume retained variable values as numerical task data.
        - value: learning
          basis: claimed
          records: *id027
          note: The exact-match score derived from retained values enters reward used to keep or restore
            policy changes.
        records: *id027
        note: Read makes retained values available to computation; scoring supplies the experience-responsive
          retention chain.
      - scope: Proposed prior-code reuse at interpreter
        assessment: known
        findings:
        - value: instruction
          basis: claimed
          records: &id028
          - runtime.md#rt-obj-program-area
          note: The retained integer instruction supplies the operation to execute under fixed primitive
            semantics.
        records: *id028
        note: The proposal gives earlier code an effect absent from base-design resampling.
      - scope: Navigation-environment state at later observations and payoff
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-instruction-cycle
        - runtime.md#rt-rte-credit-assignment
        - epistemic.md#epi-rte-input-supply
        note: The records identify task consequences but not the consumed retained representation and
          all its actual consumer paths; encoded input authority cannot classify that unseen payload.
      records:
      - runtime.md#rt-cmp-probability-distributions
      - runtime.md#rt-bap-probability-selection
      - memory.md#mem-rte-getp-read
      - epistemic.md#epi-obj-getp-values
      - epistemic.md#epi-obj-input-cells
      - epistemic.md#epi-rte-input-supply
      - runtime.md#rt-rte-instruction-cycle
      - runtime.md#rt-obj-work-area
      - runtime.md#rt-obj-stack
      - epistemic.md#epi-rte-rate-comparison
      - runtime.md#rt-rte-credit-assignment
      - memory.md#mem-obj-variable-array
      - memory.md#mem-rte-variable-readback
      - workflow.md#wf-rte-variable-cycle
      - runtime.md#rt-obj-program-area
      note: Distinct update and downstream consumers are classified separately. Arbitrary work-cell roles
        and retained navigation representation prevent complete authority coverage; software constraints
        themselves are static and outside this memory inventory.
    write_agency:
      assessment: partial
      units:
      - scope: Birth initialization and ordinary work/input writes
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id029
          - runtime.md#rt-obj-work-area
          - runtime.md#rt-rte-instruction-cycle
          - epistemic.md#epi-rte-input-supply
          note: Program computation, driver input delivery and fixed initialization admit work-cell content.
        records: *id029
        note: The records describe fixed initialization and software/task writes without per-content human
          approval.
      - scope: GetP snapshot admission
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id030
          - memory.md#mem-rte-getp-read
          - epistemic.md#epi-obj-getp-values
          note: Fixed primitive semantics admit the derived probability integer.
        records: *id030
        note: A selected primitive writes a snapshot without a human content decision.
      - scope: Base Pi update, stack saving and keep/restore
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id031
          - runtime.md#rt-rte-self-modification
          - runtime.md#rt-obj-stack
          - runtime.md#rt-rte-credit-assignment
          note: Sampled modifiers and fixed validity/evaluation rules admit, retain or restore content
            without per-change human approval.
        records: *id031
        note: Proposal, physical copying and subsequent retention are different operations, all software-controlled
          in this design.
      - scope: External variable Write and periodic zero replacement
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id032
          - memory.md#mem-rte-variable-readback
          - workflow.md#wf-rte-variable-cycle
          - memory.md#mem-obj-variable-array
          note: Address checks admit program writes; the task driver decides periodic reset.
        records: *id032
        note: Starting the experiment is not approval of each value.
      - scope: Proposed sampled-code reuse admission
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id033
          - runtime.md#rt-obj-program-area
          - runtime.md#rt-rte-instruction-cycle
          note: Software sampling supplies retained code without per-content human selection.
        records: *id033
        note: The interpreter samples code for later reuse in the proposed variant.
      - scope: Proposed direct teacher protection of selected policy changes
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records: &id034
          - runtime.md#rt-rte-self-modification
          - runtime.md#rt-clm-usefulness-invariant
          note: An explicit teacher decision would protect selected changes from top-level countermanding.
        records: *id034
        note: This is a separate declared override, not evidence of a human gate in the base loop.
      - scope: Navigation retained-state write/admission details
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-instruction-cycle
        - epistemic.md#epi-rte-input-supply
        - runtime.md#rt-rte-credit-assignment
        note: Task actions and resets are described, but the records do not fully identify the retained
          payload and all admission paths; this prevents a complete write-agency inventory for that part.
      records:
      - runtime.md#rt-obj-work-area
      - runtime.md#rt-rte-instruction-cycle
      - epistemic.md#epi-rte-input-supply
      - memory.md#mem-rte-getp-read
      - epistemic.md#epi-obj-getp-values
      - runtime.md#rt-rte-self-modification
      - runtime.md#rt-obj-stack
      - runtime.md#rt-rte-credit-assignment
      - memory.md#mem-rte-variable-readback
      - workflow.md#wf-rte-variable-cycle
      - memory.md#mem-obj-variable-array
      - runtime.md#rt-obj-program-area
      - runtime.md#rt-clm-usefulness-invariant
      note: Documented base mechanisms are automatic. Proposed teacher protection retains its claimed
        manual control locally, without upgrading it to wired or treating programmer task design as per-content
        admission.
    curation_operations:
      assessment: partial
      units:
      - scope: Live policy modification and reverse restoration
        assessment: known
        findings:
        - value: evolve
          basis: claimed
          records: &id035
          - runtime.md#rt-cmp-probability-distributions
          - runtime.md#rt-rte-self-modification
          - runtime.md#rt-rte-credit-assignment
          note: IncP/DecP revise existing entries through multiplicative/normalized updates; restoration
            replaces them with saved values.
        - value: decay
          basis: claimed
          records: *id035
          note: Popping removes recovery records and forgets rejected direct policy changes rather than
            preserving a complete invalidation history.
        records: *id035
        note: Fixed updates revise an existing table; restoration revises it again and removes retained
          direct changes. This is claimed design, not inspected implementation.
      - scope: Periodic forgetting of external variable contents
        assessment: known
        findings:
        - value: decay
          basis: claimed
          records: &id036
          - memory.md#mem-obj-variable-array
          - workflow.md#wf-rte-variable-cycle
          note: Periodic reset forgets retained external values within the scoped task memory.
        records: *id036
        note: The task reset withdraws accumulated values by replacing them with zeros; internal copies
          can survive.
      - scope: Proposed circular-stack history eviction
        assessment: known
        findings:
        - value: decay
          basis: claimed
          records: &id037
          - runtime.md#rt-obj-stack
          - runtime.md#rt-clm-usefulness-invariant
          note: Overwriting oldest entries would forget restoration history.
        records: *id037
        note: The finite circular alternative concerns recoverable history, not necessarily live policy
          effects.
      - scope: Other work-cell and navigation transformations
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-work-area
        - runtime.md#rt-rte-instruction-cycle
        - epistemic.md#epi-rte-input-supply
        note: Arbitrary programs can overwrite state, but these records do not establish which controlled
          memory-curation operations they perform. Capability and resource ceilings do not establish consolidation,
          synthesis or promotion.
      records:
      - runtime.md#rt-cmp-probability-distributions
      - runtime.md#rt-rte-self-modification
      - runtime.md#rt-rte-credit-assignment
      - memory.md#mem-obj-variable-array
      - workflow.md#wf-rte-variable-cycle
      - runtime.md#rt-obj-stack
      - runtime.md#rt-clm-usefulness-invariant
      - runtime.md#rt-obj-work-area
      - runtime.md#rt-rte-instruction-cycle
      - epistemic.md#epi-rte-input-supply
      note: Claimed evolution and forgetting are retained; unresolved transformations prevent complete
        coverage. Snapshot copying alone establishes neither consolidation nor synthesis; rollback that
        removes history is not classified as history-preserving invalidate.
    read_back_direction:
      assessment: partial
      units:
      - scope: Explicit work reads, GetP and external Read
        assessment: known
        findings:
        - value: pull
          basis: claimed
          records: &id038
          - runtime.md#rt-obj-work-area
          - runtime.md#rt-rte-instruction-cycle
          - memory.md#mem-rte-getp-read
          - memory.md#mem-rte-variable-readback
          note: Addressed operand reads, GetP and Read retrieve selected retained parts on program request.
        records: *id038
        note: Selected primitives request particular retained values and receive them; delivery fulfilling
          that request is not another push.
      - scope: Live policy supplied to automatic later sampling
        assessment: known
        findings:
        - value: push
          basis: claimed
          records: &id039
          - runtime.md#rt-cmp-probability-distributions
          - runtime.md#rt-bap-probability-selection
          - runtime.md#rt-rte-instruction-cycle
          note: The interpreter automatically supplies the current address-associated policy to the sampler.
        records: *id039
        note: At the next instruction visit the interpreter consumes retained Pi without a content retrieval
          request from an executing primitive.
      - scope: Surviving stack history supplied to later evaluation/restoration
        assessment: known
        findings:
        - value: push
          basis: claimed
          records: &id040
          - runtime.md#rt-obj-stack
          - runtime.md#rt-rte-credit-assignment
          - epistemic.md#epi-rte-rate-comparison
          note: The fixed evaluator receives newest surviving program history and its predecessor/birth
            comparison inputs, with oldP when restoring.
        records: *id040
        note: Completed cycles with checking enabled trigger automatic selection of retained baselines
          and recovery payloads.
      - scope: External variables supplied to periodic scoring
        assessment: known
        findings:
        - value: push
          basis: claimed
          records: &id041
          - memory.md#mem-obj-variable-array
          - workflow.md#wf-rte-variable-cycle
          note: Every 1,000 steps the scorer receives all current variable contents.
        records: *id041
        note: The driver automatically scores retained array values independently of explicit Read.
      - scope: Proposed reused prior code at repeated program address
        assessment: known
        findings:
        - value: push
          basis: claimed
          records: &id042
          - runtime.md#rt-obj-program-area
          note: A repeat visit would automatically select the prior sampled instruction for execution.
        records: *id042
        note: Only the declared alternative reuses code; base sampled contents are ordinary current-run
          realization.
      - scope: Additional later consumption of arbitrary encoded work history and navigation state
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-work-area
        - epistemic.md#epi-rte-input-supply
        - runtime.md#rt-rte-instruction-cycle
        note: The records afford event representation and describe task state but do not enumerate all
          retained history encodings or their later consumer routes.
      records:
      - runtime.md#rt-obj-work-area
      - runtime.md#rt-rte-instruction-cycle
      - memory.md#mem-rte-getp-read
      - memory.md#mem-rte-variable-readback
      - runtime.md#rt-cmp-probability-distributions
      - runtime.md#rt-bap-probability-selection
      - runtime.md#rt-obj-stack
      - runtime.md#rt-rte-credit-assignment
      - epistemic.md#epi-rte-rate-comparison
      - memory.md#mem-obj-variable-array
      - workflow.md#wf-rte-variable-cycle
      - runtime.md#rt-obj-program-area
      - epistemic.md#epi-rte-input-supply
      note: Pull and push coexist at different operations. Known requested routes do not resolve opaque
        semantic alternatives or make the entire selection axis inapplicable.
    read_back_signal:
      assessment: partial
      units:
      - scope: Policy push at each instruction visit
        assessment: known
        findings:
        - value: identifier
          basis: claimed
          records: &id043
          - runtime.md#rt-bap-probability-selection
          - runtime.md#rt-cmp-probability-distributions
          - runtime.md#rt-rte-instruction-cycle
          note: Actual address identity selects the distributions delivered to the sampler, not just a
            catalog entry.
        records: *id043
        note: 'Trigger: next interpreter visit. Selector input: IP/program address. Selected part: its
          associated Pi and subsequent argument distributions.'
      - scope: Stack push on enabled credit assignment
        assessment: known
        findings:
        - value: coarse
          basis: claimed
          records: &id044
          - runtime.md#rt-obj-stack
          - runtime.md#rt-rte-credit-assignment
          - epistemic.md#epi-rte-rate-comparison
          note: Newest-surviving/predecessor availability determines which historical comparison is attempted.
        - value: identifier
          basis: claimed
          records: *id044
          note: first pointers select program-start records and address identifies the distribution restored
            from selected oldP.
        records: *id044
        note: 'Trigger: completed instruction outside an unfinished modifier. Newest surviving entry is
          chosen positionally; first/address fields identify grouped history and restoration targets.'
      - scope: Variable-array push to periodic scorer
        assessment: known
        findings:
        - value: coarse
          basis: claimed
          records: &id045
          - memory.md#mem-obj-variable-array
          - workflow.md#wf-rte-variable-cycle
          note: Whole-array periodic scoring is untargeted by relevance or individual content identity.
        records: *id045
        note: 'Trigger: 1,000-step payoff event. Selector input: interval timing and full array membership.
          Selected part: all current variable values.'
      - scope: Proposed prior-instruction push
        assessment: known
        findings:
        - value: identifier
          basis: claimed
          records: &id046
          - runtime.md#rt-obj-program-area
          note: A repeated address identifies the prior code to reuse in the proposal.
        records: *id046
        note: 'Trigger: repeat visit in the run. Selector input: program-cell identity and visit history.
          Selected part: its previous instruction.'
      - scope: Explicit primitive work/GetP/Read requests
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-instruction-cycle
        - memory.md#mem-rte-getp-read
        - memory.md#mem-rte-variable-readback
        note: These are pull operations, so their requested addresses are not push signals.
      - scope: Unresolved work-history and navigation consumer alternatives
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-work-area
        - runtime.md#rt-rte-instruction-cycle
        - epistemic.md#epi-rte-input-supply
        note: No complete selector inventory for these included parts is recorded. Known pull routes cannot
          make their unknown alternatives inapplicable.
      records:
      - runtime.md#rt-bap-probability-selection
      - runtime.md#rt-cmp-probability-distributions
      - runtime.md#rt-rte-instruction-cycle
      - runtime.md#rt-obj-stack
      - runtime.md#rt-rte-credit-assignment
      - epistemic.md#epi-rte-rate-comparison
      - memory.md#mem-obj-variable-array
      - workflow.md#wf-rte-variable-cycle
      - runtime.md#rt-obj-program-area
      - memory.md#mem-rte-getp-read
      - memory.md#mem-rte-variable-readback
      - runtime.md#rt-obj-work-area
      - epistemic.md#epi-rte-input-supply
      note: Each positive signal names a concrete automatic selector and selected retained part. Address-based
        primitive requests remain pull; unknown alternatives prevent complete signal coverage.
    trace_learning:
      assessment: partial
      units:
      - scope: Historical payoff/time to automatic policy keep/restore to later sampling
        assessment: known
        findings:
        - value: 'yes'
          basis: claimed
          records: &id047
          - runtime.md#rt-obj-stack
          - runtime.md#rt-rte-credit-assignment
          - epistemic.md#epi-rte-rate-comparison
          - runtime.md#rt-cmp-probability-distributions
          - runtime.md#rt-bap-probability-selection
          note: Recorded payoff/time history and live outcomes feed automatic Pi retention/restoration,
            whose output reaches later sampling.
        records: *id047
        note: The automatic transformation consumes experience measurements, retains or restores durable
          behavior-shaping policy within one life, and supplies later interpreter invocations. No raw
          transcript or new proposition is required.
      - scope: Other modifier proposal inputs and arbitrary work/event-memory updates
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-self-modification
        - runtime.md#rt-obj-work-area
        - runtime.md#rt-rte-instruction-cycle
        note: The records do not establish the particular source lineage of modifier operands or actual
          arbitrary event encodings and later use. A local positive evaluator route does not determine
          every other possible trace-fed write.
      - scope: Navigation-state and proposed reuse/teacher/circular alternatives as separate qualifying
          writes
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-input-supply
        - runtime.md#rt-rte-instruction-cycle
        - runtime.md#rt-obj-program-area
        - runtime.md#rt-clm-usefulness-invariant
        - runtime.md#rt-obj-stack
        note: Their memory/control effects are described, but no separately complete automatic trace-to-durable-behavior
          chain is recorded for each. No unsupported local no or system-wide absence is assigned.
      records:
      - runtime.md#rt-obj-stack
      - runtime.md#rt-rte-credit-assignment
      - epistemic.md#epi-rte-rate-comparison
      - runtime.md#rt-cmp-probability-distributions
      - runtime.md#rt-bap-probability-selection
      - runtime.md#rt-rte-self-modification
      - runtime.md#rt-obj-work-area
      - runtime.md#rt-rte-instruction-cycle
      - epistemic.md#epi-rte-input-supply
      - runtime.md#rt-obj-program-area
      - runtime.md#rt-clm-usefulness-invariant
      note: Yes is established at claimed design strength for the payoff-driven retention chain, independently
        of observed improvement. Other included transformations remain unresolved, not negative.
    trace_source:
      assessment: partial
      units:
      - scope: Payoff/time experience consumed by automatic policy retention/restoration
        assessment: known
        findings:
        - value: event-streams
          basis: claimed
          records: &id048
          - runtime.md#rt-obj-stack
          - runtime.md#rt-rte-credit-assignment
          - epistemic.md#epi-rte-rate-comparison
          - workflow.md#wf-rte-variable-cycle
          note: Numerical reward events and modification-time historical baselines feed the qualifying
            retention chain.
        records: *id048
        note: Original content is discrete task payoff and runtime modification/timing events; the source
          is not a conversational log or a linked state-action-outcome trajectory.
      - scope: Additional qualifying writes from modifier operands and arbitrary work history
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-self-modification
        - runtime.md#rt-obj-work-area
        - runtime.md#rt-rte-instruction-cycle
        note: Operand provenance and encoded histories are unresolved; the established numerical evaluator
          source does not enumerate possible trace inputs elsewhere.
      - scope: Potential qualifying alternative/navigation paths
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-input-supply
        - runtime.md#rt-rte-instruction-cycle
        - runtime.md#rt-obj-program-area
        - runtime.md#rt-clm-usefulness-invariant
        - runtime.md#rt-obj-stack
        note: No complete original-input and durable-consumer chain is recorded for these potential routes.
          Unknown qualification prevents treating their trace source as inapplicable.
      records:
      - runtime.md#rt-obj-stack
      - runtime.md#rt-rte-credit-assignment
      - epistemic.md#epi-rte-rate-comparison
      - workflow.md#wf-rte-variable-cycle
      - runtime.md#rt-rte-self-modification
      - runtime.md#rt-obj-work-area
      - runtime.md#rt-rte-instruction-cycle
      - epistemic.md#epi-rte-input-supply
      - runtime.md#rt-obj-program-area
      - runtime.md#rt-clm-usefulness-invariant
      note: The positive event-stream classification follows source content, not the stack label. No session-logs,
        tool-traces or trajectories are inferred without a recorded qualifying input path.
---

# Incremental self-improvement memory profile

## Comparison rationale

This profile classifies the documented memory boundary, not a verified executable implementation. All positive mechanisms use `claimed`: the accepted records supply design and attributed operation, without inspected code or independently observed traces ([RT-RTE-instruction-cycle](runtime.md#rt-rte-instruction-cycle), [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment)). Coverage and evidence strength are separate. A fully described array can have known substrate at claimed strength; unresolved navigation representation and arbitrary work-history paths keep the system axes partial. No missing execution evidence is converted into absence.

The enduring learning product is the live probability table, not a successful program archive. Its localized entries have fixed sampling/update rules, so they are symbolic rather than distributed-parametric. The stack splits saved policy vectors from outcome and access metadata. The latter feeds comparisons and selects recovery records; it does not retain an explanation or complete trajectory ([RT-CMP-probability-distributions](runtime.md#rt-cmp-probability-distributions), [RT-OBJ-stack](runtime.md#rt-obj-stack)). Initial fixed numerical construction is other-compiled lineage; supplied observations are imported; retained event measurements are trace-extracted. These distinctions do not recover the semantic origin of every arbitrary integer.

Pi has relative weighting and operation-selection effects at the sampler. GetP instead supplies reference data. Stack evidence has learning authority at the automatic policy-retention consumer, while restored Pi changes downstream selection. The variable scorer supplies outcome feedback rather than approving individual writes. These paths do not establish explanatory knowledge acceptance, reliable action or causal benefit ([RT-BAP-probability-selection](runtime.md#rt-bap-probability-selection), [MEM-RTE-getp-read](memory.md#mem-rte-getp-read), [EPI-RTE-rate-comparison](epistemic.md#epi-rte-rate-comparison), [WF-RTE-variable-cycle](workflow.md#wf-rte-variable-cycle)).

Modifier writes evolve policy. Rejection restores distributions and pops history; because the records do not establish preserved invalidation history, this removal is decay rather than invalidate. Periodic external-array zeroing and proposed circular history overwrite also forget scoped retained content. Copying snapshots establishes neither reduced-claim consolidation nor novel-claim synthesis ([RT-RTE-self-modification](runtime.md#rt-rte-self-modification), [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment), [RT-OBJ-stack](runtime.md#rt-obj-stack), [MEM-OBJ-variable-array](memory.md#mem-obj-variable-array)).

Requested operand/GetP/Read retrieval is pull. Automatic sampler policy supply, stack evaluation and periodic scoring are push operations with different selectors. Address identities select actual delivered distributions or grouped recovery records; an address in a pull request is not push evidence. The scorer reads the whole array on a timer, giving a coarse selection rather than targeted relevance retrieval ([RT-RTE-instruction-cycle](runtime.md#rt-rte-instruction-cycle), [MEM-RTE-variable-readback](memory.md#mem-rte-variable-readback), [RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment), [WF-RTE-variable-cycle](workflow.md#wf-rte-variable-cycle)).

The automatic historical reward/time keep-or-restore route qualifies as trace learning: numerical experience feeds durable behavior-shaping state used by later sampling. Its source is discrete payoff and runtime events, not a required retained transcript. This mapping does not assert improved capacity or upgrade the reported comparisons to causal support. Other modifier inputs and arbitrary event encodings remain unresolved; no local `no` is invented to complete that inventory ([RT-RTE-credit-assignment](runtime.md#rt-rte-credit-assignment), [RT-RTE-self-modification](runtime.md#rt-rte-self-modification), [RT-OBJ-work-area](runtime.md#rt-obj-work-area)).

Reconciliation supersedes EPI-RTE-getp-read with [MEM-RTE-getp-read](memory.md#mem-rte-getp-read). The profile uses that canonical route while retaining its distinct output object [EPI-OBJ-getp-values](epistemic.md#epi-obj-getp-values). This affects policy snapshot lineage, authority, admission and pull classification, not their evidence strength. The work-area container and its input/snapshot parts remain valid; neither those parts nor [EPI-RTE-rate-comparison](epistemic.md#epi-rte-rate-comparison) supersede their containers. No other supersession affects a value.

Proposed instruction reuse, teacher protection and circular overwrite retain only their declared force. Human teacher protection is a separate proposed retention decision, not a manual base write gate. Arbitrary work-cell semantics, the navigation environment's retained representation, exact external Read destination, and exercised GetP or Write-to-Read use remain limited by the accepted records. Those missing facts prevent complete lineage/consumer inventories and stronger operation claims; they do not erase supported mechanisms ([RT-OBJ-program-area](runtime.md#rt-obj-program-area), [RT-CLM-usefulness-invariant](runtime.md#rt-clm-usefulness-invariant), [MEM-RTE-variable-readback](memory.md#mem-rte-variable-readback)).

Source-read log: none. Classification used only the supplied accepted members and reconciliation; no source ambiguity required a direct capture read.

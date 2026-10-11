# First deliverable and evaluation boundary

## Deliverable

A short account of how the current method allocates investigation and review
effort, followed by options for managing the gap between available resources
and possible source coverage. Address selection, depth, stopping, uncertainty
and the cost of missed mechanisms. Compare the current role contracts with
those needs and recommend the smallest sufficient change. Distinguish reducing
avoidable work from deliberately leaving questions unanswered.

Start from [current arrangement](./current-arrangement.md) and the read-count
baseline in [evidence base](./evidence-base.md). Compare at least these three
options, none of which adds a process or touches the engine:

1. Clarify the existing materiality-based stopping rule for omission
   searches, without changing coverage territory.
2. Bound lens omission searches by runtime and lens anchors, as the
   [verification coverage bounds proposal](./proposals/verification-coverage-bounds.md)
   describes.
3. Select a small, justified set of consequential claims for the existing
   report verifier's question-driven omission checks, with an explicit stopping
   decision and unresolved coverage. Do not invent a numerical budget.

The [completed comparison](./coverage-policy-comparison.md) recommends the third
as an operational clarification of the first, not a new architecture. The operator
adopted it with effort-sensitive stopping and brief reporting; the prose-only
implementation is recorded in the comparison. The return condition below governed
the initial comparison and still applies to any further trial.

The proposal is one option among these, not the conclusion.

Do not begin with a replacement workflow, a predetermined memory split or an
assumption that more processes produce better coverage.

## Evaluation criteria

- Whether the option reveals consequential design alternatives and mechanisms.
- Whether findings retain enough conditions and evidence to inform a later
  Commonplace transfer assessment.
- Whether the overall account remains coherent and claims stay within evidence.
- Total production, verification and consumption work, including repeated reads
  and cross-lens reconciliation.
- Disruption to the stabilized method, command environment, report consumers and
  existing tests.

## Return condition

Return to the operator after the comparison, before any live method change or
trial. A partial comparison names the unresolved choice and the evidence
needed rather than silently selecting an architecture. Any proposed trial
specifies its question, scope, cost, success criteria and the evidence that
would count against adoption; running it requires separate authorization.

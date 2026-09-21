# Efficiency: retain the theory, retain criticisms, or reconstruct both?

Ontology vocabulary probe, 2026-09-21; no experiment run or commissioned.
Controls are drawn from the [component-comparison workshop](../../explanatory-theories-deployment-time-learning/README.md).
The [RSI workshop](../../schmidhuber-rsi-imports/README.md) was consulted for
ontology compatibility only. The existing
[retention design](../../explanatory-theories-deployment-time-learning/experiment-design.md#test-retention-separately)
supplies controls and the raw-history reconstruction comparison once its
history is specified. The criticism-only arm is an addition, not a new protocol.

## Capacity, action, and horizon

The capacity is to diagnose and repair new KB retrieval failures using what
earlier failures taught the system. Observe the proposed repairs and their
independently assessed retrieval quality and regressions. Require availability
across fresh contexts over a declared sequence of later episodes. Vary the
number of reuse occasions: amortization over many episodes cannot establish
savings on the first one. Persistence beyond the observed horizon remains
unestablished.

The system includes the model, harness, stores, retrieval and reconstruction
steps, tools, and participating people. Model weights, source evidence,
allowed repairs, and assessment remain fixed across arms.

## Two comparisons, three retained states

Replay a common development history and authorized outcomes. Give every arm
access to the same underlying observations; vary which derived work survives.

| Arm | Retained across episode boundaries | Work before the next decision |
|---|---|---|
| Retained theory | Current assembled theory, criticisms and testing record, plus underlying observations | Retrieve, check applicability, interpret, and revise when needed |
| Retained criticisms | Criticisms and testing results tied to historical claims, plus the same observations; no current assembled successor theory | Rebuild a theory, then check and use it |
| Inputs and outcomes | Task inputs, attempted actions, observed outputs, and authorized evaluator outcomes; no formulated theories or criticisms | Formulate a theory and any criticism needed, then check and use it |

The first pair asks what keeping the assembled theory buys. The retained-theory
versus inputs-and-outcomes pair asks what keeping the accumulated work of
conjecture and criticism buys. It changes both assembled theory and retained
criticism, so cannot isolate criticism alone. The criticism-only versus
inputs-and-outcomes pair can additionally locate that narrower contribution;
it does not replace either required comparison.

Define records by content, not filename. A criticism may quote a rejected
claim or say which test it survived without supplying a current assembled
successor. Keep quotations only as needed to identify the criticized historical
claim, with the objection, outcome, and provenance. Audit whether the collection
directly presents a current assembled theory, rather than whether a model could
infer one: inferability is the reconstruction arm's purpose. If the store
already supplies that successor, the first contrast has collapsed and must be
redesigned or reported as unavailable.
Likewise, “inputs” means task inputs, not entire agent prompts containing the
theory. Preserve task-relevant facts and action results when removing derived
formulations; audit the transformation for leakage and information loss.
If the task cannot separate these, report a confounded comparison. Exclude
cross-arm memory and hidden caches. Reconstructed theories are discarded at
the episode boundary in both reconstruction arms; consumption during the
episode remains allowed. Indexed traces exposing the theory belong in the
retained-theory arm, not automatically in the raw-record arm.

Between assessment episodes, replay the next shared development evidence.
The retained-theory arm updates its theory, criticism, and testing record;
the criticism-only arm appends criticisms and results but discards its assembled
successor; the inputs-and-outcomes arm appends only those records. Keep audit
outcomes hidden until the compared decisions are frozen. Do not feed
arm-specific outcomes into subsequent development unless they are replayed
to every arm. Thus retention policies continue through the horizon without
silently giving the arms different source evidence.

## Controls and cost

Reuse the peer design's common checkpoints or replay, fixed outcome authority,
hidden assessment, and shifts that preserve the mechanism, break a premise,
or invalidate it broadly. Permit all arms full scanning and reconstruction
within their budgets. Record what was retrieved and use content interventions
to test whether retained or reconstructed formulations affect later choices.
Include the frozen seed on later cases when making a learning claim.

Compare quality under matched total budgets and total cost to a predeclared
quality and harm target over the same horizon. Choose one primary endpoint
before execution. An arm that misses the target has no demonstrated
cost-at-comparable-quality advantage. Keep calls, tokens, latency, tool work,
storage, and human effort visible; any conversion into one budget needs an
explicit rule. Include initial theory or criticism production, diagnosis,
reading, reconstruction, retrieval, applicability checks, candidate generation,
verification, review, correction, index maintenance, and later harm. Report
common history costs and arm-specific costs without charging the same work
twice or giving retention free preparation.

Vary history volume and context allowance separately, matching each setting
across arms. A context limit permits repeated reads whose cost is charged;
it must not mean arbitrary denial of baseline evidence. These are parameters
for a later experiment commission, not chosen sample sizes or a commissioned sweep.

## Indexing example

Use the [applicability-index example](../indexing-applicability-example.md) as
a nested retained-content comparison. Both arms may scan the same trace
containing the timeout/duplicate-write conclusion. One additionally retains
the applicability condition linking unconfirmed completion to retry risk.
If that condition is already explicit in the trace, the contrast is lookup
organization; otherwise it also retains an interpretation. Count index creation,
maintenance, calls, and tokens, and assess the later duplicate-charge decision.
This is not the inputs-and-outcomes arm: the trace already contains a theory.
The example is retained as a bounded efficiency case, not evidence of savings.

## Results and the pending reorganization

Lower complete cost at comparable quality, or better quality under matched
budgets, supports the winning arrangement only for the tested horizon and
history/context setting. Retention can win one pair and lose the other.
Null differences do not establish equivalence; higher costs or harmful stale
reuse count against retention. A cost advantage alone does not establish
learning: improved capacity from criticism and causal later use need their
own evidence. Historical survival and file restoration do not establish
causation or undo downstream harm. The [RSI additions](../comparison.md#recursive-self-improvement-precedents)
reinforce later-search measurement and complete accounting, without supplying
a result for these comparisons or establishing compounding.

The pending reorganization meant distinguishing reconstruction from retained
criticisms from reconstruction using inputs and outcomes, while treating
theory-bearing indexed traces by their content. This is recoverable from
the [decision record](../definition-decision-record.md#settled-decisions),
the companion, and commit `54716c74`'s predecessor README (the direction
“Reconstruction splits in two, and we compare against both”). Later commits
`8b82b5f0` and `31a630c9` defer it without adding another question. This
specification settles that conceptual organization. Practical separation of
the stores, tasks, budgets, models, horizons, and evaluation belong to experiment
design. No membership condition needs to move. The parent workshop now records
this conceptual question as resolved and proceeds under its
[closure plan](../closure-plan.md); no experiment is commissioned.

# Use-and-outcome records

## Commission

Opened on 2026-10-02 at the operator's request. Work out how Commonplace
can retain and use observations from ordinary operation to guide later
decisions, without requiring a controlled experiment for every idea.
The immediate design question is how to store, retrieve, and maintain
use-and-outcome records when their number and underlying evidence grow large.

The operator's concern is not just low confidence. An observation may be
clear while its explanation, scope, or implications remain unresolved.
The system should use these scraps of information without presenting them
as conclusions established by controlled comparisons. A controlled trial
may be worth requesting when resolving an uncertainty would materially
improve later decisions; it is not the default cost of retaining an idea.

This workshop commissions investigation and design. It does not adopt a
schema, storage backend, capture procedure, or change to existing gates.

## Starting discussion

Heuristics for recognizing a model's capability limit motivated the
discussion. The broader question is how operational observations that lack
experimental controls can guide decisions.

[Tentative theory](../../notes/definitions/tentative-theory.md) means a
theory that remains open to criticism and revision, however well it has
survived. The design question here concerns what particular observations
and criticisms permit a particular consumer to infer or do. It does not
require a new maturity stage or one confidence score for the whole idea.

An Opus comment supplied by the operator proposed recording an idea's uses
and outcomes, then deriving its current assessment when needed. Its useful
working hypotheses are:

- Whether an idea should guide a decision depends on the evidence and on
  the decision's stakes, reversibility, and observable consequences.
- Cheap capture and feedback may be more useful than an assessment form
  completed before every use.
- Reuse and favorable outcomes must remain distinguishable. Familiarity
  alone supplies no evidence that the idea worked.

These hypotheses remain open. A favorable outcome need not identify its
cause or establish the explanation's scope. Contradictions, rival explanations,
and overlooked conditions can also change an idea without another use.

The five-aspect assessment table discussed earlier is not an adopted
contract. Likewise, retained theories improving sample efficiency remains
a [conjecture](../../notes/retained-theories-may-improve-sample-efficiency.md),
not a demonstrated advantage of the proposed record.

## Storage direction to examine

The initial agent proposal separates:

| Material | Intended role |
|---|---|
| Episode record | A compact account of the decision, the claim relied on, relevant conditions, observed outcome, and evidence links. |
| Detailed evidence | Excerpts, measurements, outputs, or full traces needed to check or reinterpret the episode. |
| Idea summary | A revisable account of what the cases suggest and leave unresolved, with links to its inputs. |

Several ideas could refer to one episode. Consumers could read a summary
and expand relevant cases. This is a candidate arrangement; it need not
require three files per use.

The existing [reports contract](../../reports/COLLECTION.md) offers durable
records under `kb/reports/retained/` and regenerable views under
`kb/reports/cache/`. Placement and record granularity remain open. Storage
and reading costs are separate: summaries need not reduce retained volume.

## Questions to settle

- What needs contemporaneous capture? How are delayed, ambiguous, or
  never-observed outcomes attached to the original decision?
- How is the claim and version relied on identified? How can several ideas
  share evidence without implying causal attribution?
- What is the smallest useful record, and what already survives in existing
  work records?
- How can retrieval and summary maintenance preserve conflicting cases and
  different conditions while grouping repetition?
- What evidence must survive compression or deletion, and what later
  questions become unanswerable?
- How does a consumer decide on use or a controlled trial without a large
  assessment form?
- What does the literature provide? Popper was checked first; distinguish
  source claims from our operational extensions.

## Evaluation boundary

Examine concrete cases before selecting machinery. The analysis-offload
[analysis-offload closure evidence](../../reports/retained/analysis-offload-closure-20261002.md)
is an available candidate, not a prescribed first target. Keep its measured
results separate from explanations of differences between runs.

A candidate design should distinguish citation from consequential use,
observation from explanation, and missing outcome from success. Examine
favorable, conflicting, failed, and unknown outcomes, including a history
too large for routine reading.

Count capture, retrieval, summary maintenance, and retention costs. A worked
case can show that a record supports a reading or revision task. It cannot
alone establish improved learning or causal attribution. Controlled trials
remain optional work when their expected decision value warrants the cost.

## Coordination and bookkeeping

The [decision-lifecycle evidence workshop](../decision-lifecycle-evidence/README.md)
owns the continuing decision record and its transitions. It already retains
the operator's requirement that essential evidence survive loss of access
to source sessions. This workshop carries that requirement forward and
focuses on consumption of uncontrolled observations and the cost of growing
use-and-outcome histories. Coordinate any shared capture or retention design;
do not create a competing ADR lifecycle here.

Keep alternatives and objections here. Worked cases identify their source
state and distinguish observations from later interpretation. Existing
retention contracts remain in force.

## Closure

Close with a concrete record and access design, or a reasoned choice to use
existing records. Specify retention, access, maintenance, and the losses
from discarding detail. Worked cases expose costs and unresolved questions.

Extract durable conclusions into the appropriate notes, proposals, or
instructions. Then remove this workshop and its active-list entry. Closure
does not require establishing a general learning advantage.

## Relevant inputs

- [Preserve evidence without making history the next context](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md)
  — separates evidence capture from routine loading.
- [Retaining episode evidence keeps a distilled rule open to re-examination](../../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md)
  — frames the tradeoff between compressed conclusions and retained cases.
- [Citing retained theory at the decision point is a mediation trace](../../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md)
  — distinguishes recorded consumption from correct or consequential use.
- [Raw accumulation does not create usable memory](../../notes/raw-accumulation-does-not-create-usable-memory.md)
  — names the access and interpretation work that storage alone leaves open.
- [The bitter lesson selects production methods, not representational forms](../../notes/the-bitter-lesson-selects-production-methods-not-representational.md)
  — related design argument; it does not decide whether a particular record
  schema is worth its cost.
- [Popper, Conjectures and Refutations](../../sources/popper-conjectures-and-refutations.ingest.md)
  — starting literature input; the introduction's discussion of sources and
  chapter 1's account of criticism are relevant reading targets.

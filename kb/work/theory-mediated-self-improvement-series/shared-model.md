# Shared model

This is a working model for the series, not a promoted claim.

## Governing conjecture

A mixed system can improve through explicit theories without requiring every
learned result to enter model weights. Retained natural-language theory gives
semantic commitments an address. A language model interprets, criticizes,
derives, and proposes. Symbolic code carries transitions that must be executed
faithfully across time. Tests, validators, and observations provide correction.
The parts form a learning system only when evidence selects retained changes
that alter later operation.

The architecture is mixed by necessity, not compromise:

| Part | Primary contribution | Characteristic failure |
|---|---|---|
| Retained natural-language theory | Purpose, causal explanation, assumptions, applicability, and a surface for criticism | Ambiguity, omission, drift, and inert documentation |
| Language-model interpreter | Semantic application, criticism, proposal, and derivation across cases not fully formalized | Underspecification, stochastic deviation, bias, and confabulated rationale |
| Symbolic runtime and code | Scheduling, state transitions, schemas, validation, installation, rollback, and repeatable execution | Faithful execution of the wrong transition or frozen decomposition |
| Operational evidence and oracles | Failure signals, tests, comparisons, and correction from outside the candidate theory | Weak proxies, self-sealing evaluation, and incomplete coverage |

The operative loop is:

    observation or failure
      -> criticism of retained theory
      -> revised theory or derived candidate
      -> realization in prose, code, configuration, or model state
      -> evaluation and admission
      -> installation and later execution
      -> new evidence read against the retained theory

The same causal path must carry the theory, the self-change, its result, and
the later theory revision. Separate witnesses elsewhere inside a broad system
do not close this loop.

## Two-layer execution

Natural-language theory is the generator and fallback for cases whose relevant
distinctions have not been stabilized. Recurrent derivations can be codified
into symbolic methodologies, validators, or schedulers that execute more
faithfully and cheaply. A codified fast path does not retire its source theory:
new counterexamples may require the code to be revised, relaxed, or returned
to theory-level interpretation.

This uses the error-correction asymmetry described in
[scheduler–LLM separation](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md)
and the promotion/fallback relation described in
[the two-layer execution system](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md).

## Direction, strong benchmark, and bootstrap

The broad direction is increasing programmer leverage: expand the accepted
software outcomes attainable from a fixed amount of human programming effort,
or preserve those outcomes while reducing that effort. For a given task, the
**residual human work** is the set of programming decisions and actions that a
human must still supply for an accepted result. This includes configuration,
review, recovery, and repair when the tool displaces work into those stages.

Each mechanism has an **automation envelope**: the responsibilities it can
carry under stated conditions. A formatter has a narrow envelope, but removing
formatting work is still movement toward a system that requires no human
programming work. Once that envelope is exhausted, formatter improvement alone
cannot remove design, theory-building, debugging, or maintenance work. The
limit belongs to the method. Reaching the broader benchmark requires
complementary mechanisms whose combined envelope covers progressively more of
the residual work.

A mechanism can also improve without expanding its envelope. A better
formatter may increase output quality, reliability, input coverage, or speed,
or reduce computational cost while formatting remains its only
responsibility. That improvement counts on the capability or yield dimensions.
It does not count as transfer of a new kind of programming work. The progress
record must preserve both contributions instead of treating responsibility
transfer as the only kind of improvement.

Envelopes do not stack toward an empty human cut set. Each mechanism takes the
decisions it can warrant — represented inputs, a settled criterion, a result an
independent oracle can check — and stops where warrant fails. The residual
human work is therefore adversely selected: per decision it is harder to
warrant than the work already transferred, and moving the next decision costs
more than moving the last, even with a fixed incoming workload
([warranted transfer leaves people the hardest-to-warrant decisions](../../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md)).
Two consequences follow. The list of what humans still supply is a residue of
selection, not evidence about an essentially human capacity. And closure over
a declared path is decided at its least-warrantable decisions, which is to say
at the evaluator; envelope expansion elsewhere on the path does not approach
it. This is a mechanism at the human boundary, distinct from the elastic
backlog that moves human attention to new work.

Computational closure is a structural milestone for a declared improvement
path. Every premise, transition, authorization, evaluation, and recovery operation needed
to continue that path over the stated horizon is available inside the
automatic system. Code and scheduling are themselves possible revision
targets; otherwise the apparent closure hides a fixed external meta-level.

Closure must also be capability-adequate. A no-op loop, narrow parameter
optimizer, or self-confirming evaluator can be computationally closed. The
target must meet an independently declared threshold on consequential
theory-building or LLM-wiki work, and the closed path must reach commitments
that materially determine that capability. The
[closure–capability map](./closure-capability-map.md) records this second axis
and the principal degenerate cases.

A strong capability benchmark is performance at least as good as a competent
remote programmer over a declared challenge distribution. The comparison
holds constant the task brief, repository, digital tools, permissions, and
feedback. It removes the human programmer's decisions from the construction
path, not the client's ability to state goals or respond to results. Outcome
quality and reliability are primary; time, compute, and monetary cost remain
separate comparison coordinates. This benchmark excludes narrow closed loops
without making parity a prerequisite for practical value or a final upper
bound.

Commonplace is a human-inclusive bootstrap. Its models and machinery already
perform some criticism, proposal, checking, drafting, and execution. Humans
still choose demands, supply unrecorded premises, interpret ambiguous results,
authorize changes, and repair failures that exceed the represented path. The
research task is to expose that cut rather than call the composite autonomous.

## Present tool and broader LLM-wiki payoff

The same human-inclusive arrangement has value before closure. Commonplace can
help an operator build a theory by retaining conjectures, exposing assumptions,
routing relevant evidence, applying criticism, recording revisions, and
deriving more constrained procedures. Calling it a theory-building tool is a
claim about what the human–agent composite enables, not a claim that the
computational part alone possesses Naur's program-specific theory.

Theory building is one LLM-wiki function. The substrate can also support
source capture and grounding, retrieval and routing, connection and synthesis,
criticism and review, revision and reconciliation, validation, lifecycle
management, and publication. These operations share retained, addressable
state but need not share one automation frontier or one success measure.

Automation has a dual payoff:

1. it is experimental progress toward a path with no required human cut; and
2. it may improve the present tool by reducing latency and intervention,
   increasing repeatability and throughput, or expanding which cases it can
   handle.

The second payoff is not automatic. Removing a human judgment can reduce tool
quality, conceal errors, or increase correction cost. Each transfer therefore
needs both an autonomy record and a utility-and-warrant comparison.

## Progress record

No unique percentage follows from the current theory. Compare systems at a
fixed grain using a vector:

| Dimension | Question |
|---|---|
| Human leverage | What accepted outcomes are attainable for a fixed amount of total human programming effort, or how much effort is required for a fixed outcome? |
| Residual human work | Which programming decisions and actions must a human still supply, including configuration, review, recovery, and repair? |
| Automation envelope | Which residual responsibilities can the current mechanism carry, under what conditions, and where does its method reach a ceiling? |
| Path coverage | Which named revision paths, theory-building functions, and other LLM-wiki operations are internally executable? |
| Horizon | How many linked episodes can proceed before indispensable human judgment? |
| Human cut set | Which required decisions still cross an unrepresented human boundary? |
| Operational capability | Which externally evaluated consequential tasks can the incumbent system perform, at what quality and breadth? |
| Warrant | What independent checking, correction, rollback, and evidence protect the path? |
| Tool usefulness | How well does the human–agent arrangement perform the declared theory-building or wiki function? |
| Improvement yield | What quality-adjusted improvements does the path produce for its computational and human cost? |

A change is unambiguously forward in the leverage order when, at a fixed task
and acceptance grain, it produces no worse outcomes with no more total human
programming effort and strictly improves at least one of those terms. Expanding
the accepted task set under a fixed human-effort budget is the corresponding
breadth improvement. Reducing a single bounded responsibility qualifies even
when the responsible mechanism cannot reduce any other part of the residual
work.

Within the same automation envelope, better output quality, reliability,
coverage, latency, or computational efficiency counts as capability or yield
progress. It can help meet the strong benchmark even when residual human work
does not change. Only a reduction in that residual counts as an autonomy
transfer.

This partial order does not imply convergence. A method can make real progress
and then reach its automation ceiling. Record both the work transferred and
the work still outside its envelope. If human effort falls by weakening
quality or warrant, or apparent automation exports effort into review and
recovery, the dimensions trade off and an explicit objective is required.

The scoped non-degenerate closure milestone has an empty human cut set for the
declared path and horizon while retaining the capability floor, correction
path, and continuity conditions. A practically successful tool may stop far
short of it. Remote-programmer parity adds the strong capability comparison;
it is a milestone on the same direction, not the reason earlier tool
improvements count.

This also separates autonomy from power. The Bitter Lesson suggests that
replacing hand-designed selection with scalable search and learning may
increase yield. That is an empirical consequence to test, not part of the
autonomy definition.

## Open choices

- What objective and authority may be supplied before an episode begins, and
  which revisions to them count as part of the target path?
- At what path grain can the allocation and human cut set be compared without
  hiding displaced work?
- What evidence shows that a natural-language theory, rather than a generic
  criterion or an unrecorded model judgment, supplied the decision content?
- Which code and scheduler changes must be reachable before the target deserves
  the name closed?
- Which external observations and model services belong inside the declared
  boundary, and which are environmental inputs?
- Which theory-building and LLM-wiki outcomes should measure present tool
  usefulness without collapsing into activity counts or self-scored prose?
- Which challenge distribution and capability threshold make closure
  non-vacuous without silently fixing the whole research outcome in advance?

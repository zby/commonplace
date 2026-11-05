# Workshop: open-ended work as resource allocation under uncertainty

## Live question

**What should guide automatic search in open-ended knowledge work?**

An automatic system must choose what to investigate, how much effort to spend,
and when to stop or change direction. Checking a developed result does not by
itself tell the system which undeveloped possibility deserves the next
investment. The operator's current framing is that this is an economic
question: what further work might return, what it costs, and what else those
resources could support. This does not require assuming that returns can be
estimated reliably or reduced to one numerical score.

Keep this workshop and its name. The original investigation supplied much of
the background; the current question continues it rather than starting a
separate workshop.

## Intent and origin

The operator posed the original investigation on 2026-10-30, adopting the
external brief retained verbatim in [handoff.md](./handoff.md). Its six
research directions asked whether open-ended work could be understood as
recursive effort allocation and commitment management, and what that implied
for Commonplace's architecture. Ideas were to be developed here before
extraction, not applied directly to library notes as the brief suggested.

On 2026-11-05 the operator introduced three resource tiers: operator
attention, LLM work and classical compute. In the current cleanup discussion,
the operator clarified the purpose of that turn: understanding what guides
**automatic search**, and recognizing the economic character of that choice.
The tier model is supporting analysis, not the workshop's objective.

The practical aim is an account that can guide automatic choices about what
to do next and make those choices open to improvement. It must extend the
[epistemic stance](../../reference/epistemic-stance.md), not replace it:
being worth investigating does not make a claim true or warrant adopting it.

## What remains unsettled

- **Returns.** What makes further investigation worth pursuing under the
  declared objective in [Commonplace as an instrument](../../reference/commonplace-as-an-instrument.md)?
  Saving operator judgment or making work cheaper are possible returns;
  moving work between resource tiers is not assumed to be the maximand.
- **Uncertainty.** How can search use guesses about returns when the
  consequential possibilities and their outcomes are not yet known? What
  distinguishes useful economic guidance from unsupported numerical precision?
- **Resources and constraints.** How should operator attention, LLM work,
  classical compute, context limits, reliability and authority enter a search
  choice? Which constraints determine feasibility before costs are compared?
- **Learning from choices.** Must individual return guesses be recorded and
  compared with outcomes, or can evaluation of the search controller provide
  enough feedback? This is one design question within automatic search
  guidance, not the whole problem.
- **Control.** What supports choosing among investigations, continuing,
  stopping and backtracking without spending more on the allocation mechanism
  than its decisions save?

These are research questions, not an adopted controller design. The existing
[search-before-evaluation result](../../theory/open-ended-improvement-allocates-search-before-evaluation.md),
[separation of search control from adoption](../../theory/lightweight-search-control-does-not-license-adoption.md),
and [controller evaluation guidance](../../theory/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md)
are starting constraints. The investigation must identify what an economic
account adds rather than rename those results.

## Status of the three-tier model

[resource-tiers.md](./resource-tiers.md) records the 2026-11-05 framing. It is
provisional, including its feasibility claims, proposed maximand and proposed
refuters. Its candidate objective—work moved downward across two frontiers at
required reliability per operator judgment—is not adopted and does not define
the current commission. A transfer between tiers is one possible investment
and return for automatic search to consider.

Active-workshop triage was suggested as a cheap test site for the question
about individual return guesses. No test protocol is commissioned by that
suggestion. The next consequential decision is to choose a bounded comparison
that could distinguish competing accounts of search guidance; if no such
comparison can yet be stated, retain the gap rather than build a controller.

## Delivered background

The original investigation mapped the six directions in
[reconciliation.md](./reconciliation.md). Its work-level conjecture largely
composed results already held by the library. The architecture-level claim
was separated from it and remains a conjecture, not an adopted architecture.
The durable outputs include:

- [Reusable commitment support across kinds of knowledge work](../../reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md):
  the architecture conjecture, alternatives and a comparative adoption test.
- [Cost-per-yield records for routine controllers](../../reference/proposals/cost-per-yield-records-for-routine-controllers.md):
  proposed instrumentation; context regime is feasibility metadata, not a
  cost figure. Cost comparisons require resource figures or mark cost unknown.
- [Codify-versus-LLM decision heuristics](../../theory/codify-versus-llm-decision-heuristics.md):
  the "Stake and odds" addition, narrowed from the
  [routine-conversion account](./routine-conversion-account.md).
- [Controller evaluation guidance](../../theory/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md):
  the scoring rule and unequal-cost comparison option alongside matched-budget
  comparison.
- [The shared epistemic layer](../../theory/open-ended-knowledge-work-shares-one-epistemic-layer-across-roles.md)
  and the [goal-prioritization tag](../../tags/goal-prioritization-README.md).
  Extraction is not independent confirmation of the shared-layer claim.
- The direction-4 question delivered to
  [theory-refinement-interface](../theory-refinement-interface/README.md),
  and the deferred epistemic-versus-resource-rational rivalry recorded in
  [the log](../../log.md). The proposed relaxing-trigger test was withdrawn
  because it did not discriminate the accounts.

Successor work also qualified the original "convert into routine" reading:
[operationalization-executability-automation](../operationalization-executability-automation/README.md)
names the task and executor;
[ADR 124](../../reference/adr/124-retire-unique-operational-semantics-as-the-form-criterion.md)
allows adoption of a model package as a governing semantic reference for an
operation. Semantic routines in prompts versus symbolic routines in code are
therefore not an adequate split by artifact. "Routine" remains ordinary
English, not a new technical state.

## How to use the remaining files

- This README is the current commission. It supersedes the earlier
  "closing conditions met except deletion" status and the older extraction
  queues where they conflict with the delivered results above.
- [resource-tiers.md](./resource-tiers.md) is the live supporting draft.
- [handoff.md](./handoff.md) is the original brief, not a fresh execution plan.
- [reconciliation.md](./reconciliation.md),
  [routine-conversion-account.md](./routine-conversion-account.md),
  [architecture-proposal.md](./architecture-proposal.md),
  [vocabulary.md](./vocabulary.md) and `search/` are earlier analysis and
  evidence. Consult the library successors for current extracted claims;
  do not execute their old extraction lists as a backlog.

The old reconciliation also proposed an effort-allocation classification
paragraph and questions about episode handoff, third-order lessons and value
decay. These remain unextracted candidates, not required outputs of the current
investigation. The search inventories do not need library homes merely because
they exist. Before eventual deletion, check which surviving claims need their
retained evidence and extract only what is needed.

## What closes the workshop

1. State what economic guidance adds to the held search-control account, or
   conclude that it adds nothing useful within the tested scope.
2. Make the answer criticizable through a bounded comparison or discriminating
   observation. Separate a conceptual argument from demonstrated improvement
   in automatic search; an unrun test remains a proposal.
3. Give the tier model an explicit disposition: useful resource model,
   revised model, or rejected framing. Do not adopt its maximand by default.
4. Extract surviving results and genuinely live questions into their proper
   library or workshop destinations, then delete this directory and remove
   its index entry. The earlier operator hold on final deletion is not
   discharged by this cleanup.

## Evaluation boundary and coupling

- Research write scope remains this directory. Library changes are proposed
  here and applied separately at extraction. Updating the workshop index for
  this cleanup does not authorize broader library edits or implementation.
- [theory-refinement-interface](../theory-refinement-interface/README.md)
  owns the derive, compare, locate, revise, evaluate and apply interface.
  Proposed changes to those operations go there.
- [conjecture-store](../conjecture-store/README.md) and
  [decision-lifecycle-evidence](../decision-lifecycle-evidence/README.md)
  own conjecture and decision storage and lifecycle. Do not design a
  generalized commitment store here.
- [reflective-improvement-divergence](../reflective-improvement-divergence/README.md)
  and [self-revision-design-space](../self-revision-design-space/README.md)
  own non-termination and redesign reach of recursive improvement.
- [use-and-outcome-records](../use-and-outcome-records/README.md) owns operational
  observation records. Coordinate proposed recording requirements with it.
- Look for counterexamples and rival accounts. Distinguish established
  results, arguments, design hypotheses and untested empirical claims.
  Prefer a few substantial results to many notes.

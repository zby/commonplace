# Workshop: open-ended work as resource allocation under uncertainty

## Goal

Test the conjecture that open-ended knowledge work is a recursive process of
allocating limited time, context and budget across search judgments (where
effort goes next) and commitments (retained resolutions about what to believe
or build), and decide what the library should retain from it. Term choices
are in [vocabulary.md](./vocabulary.md). The operator's reason for
posing it, set out below, is that it would make epistemic work the layer all
open-ended knowledge work shares. The conjecture has two parts that must be
judged separately:

- **Work-level conjecture.** Managing search judgments and commitments
  recursively — including those about how to investigate and how to improve
  the method — is an economical way to do open-ended work under bounded
  resources.
- **Architecture-level conjecture.** Reusable computational support for that
  process is an economical route from Commonplace toward a general
  computational environment. This does not follow from the work-level
  conjecture.

The question kept in view: can reusable machinery make open-ended
intellectual work cheaper for bounded actors while the machinery improves
through the same process?

The economic framing must extend the [epistemic stance](../../reference/epistemic-stance.md),
not replace it. A judgment that something is worth investigating is not a
claim that it is true, and the account must keep the two apart.

## Why the operator wants this

The operator gave this reading on 2026-10-30. Routine work is largely solved:
language models do routine semantic work, and software does routine symbolic
work. Commonplace's goal is a framework that converts more and more knowledge
work into routine work. Open-ended work is the frontier where no routine
exists yet.

On that frontier, an actor allocates effort by guessing what each investment
will yield, and these guesses are fallible. Allocation is only as reliable as
the guesses that guide it, and improving them is epistemic work. Epistemic
work also produces the routines: it finds which choices are stable enough to
commit, in prompts and skills for semantic routines or in code for symbolic
ones. Converting work into routine is then the return on epistemic
investment.

The reading would answer a question the project has struggled with. Most of
this KB develops machinery for epistemic work, and its main application field
has been unclear. If the reading holds, epistemic work is the layer that every
open-ended kind of knowledge work shares, and Commonplace's epistemic
machinery is the base for more general knowledge tools.

The library already names the conversion into routine:
[constraining](../../theory/definitions/constraining.md) and its symbolic
region, [codification](../../theory/definitions/codification.md);
[progressive constraining commits only after patterns stabilize](../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md);
[codification and relaxing navigate the bitter-lesson boundary](../../theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md).
No note found while framing gives one account of when conversion is worth
paying for: how often the work recurs, what the routine saves, what
conversion and maintenance cost, and how likely the pattern is to stay
stable.

The claim that epistemic work is the shared layer is the one this workshop
most needs to test. Known weak points:

- **The frontier does not shrink by itself.**
  [Codifying predictable choices leaves agents with less predictable work](../../theory/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md):
  each conversion leaves the remaining work harder. Converting more work may
  raise the epistemic share of what remains rather than reduce it.
- **"Solved" is graded.** A model doing routine semantic work still makes
  errors, and a routine can stop fitting when conditions change and need
  [relaxing](../../theory/operational-signals-that-a-component-is-a-relaxing-candidate.md).
  Maintaining routines is recurring work that may not itself be routine.
- **Goals are not beliefs.** Allocation needs beliefs about consequences and
  also goals or preferences. Epistemic machinery covers the beliefs. Work
  whose discoveries change its goals strains the claim most.
- **Layer versus implementation.** A shared epistemic layer would not show
  that Commonplace's particular machinery is the right one. That is the
  architecture-level conjecture, and it needs its own evidence.
- **Testability.** "All knowledge work is epistemic" says nothing until it
  names what a knowledge tool without the epistemic layer would fail to do.
  One candidate: better epistemic machinery should show up as faster or more
  reliable conversion into routines, not only as better notes.

## Posed by

The operator, on 2026-10-30, adopting a brief written in an external ChatGPT
session. The brief is kept verbatim in [handoff.md](./handoff.md) as the
statement of intent and its six research directions. Where it says to revise
library notes directly, the operator's decision overrides it: the ideas are
developed here first and reach the library only by extraction.

## Starting position

The library already holds results about allocation, so the first job is to
map them and find what the economic framing adds.
Notes found while framing (not exhaustive; each file's description says what it holds):

- Allocation before evidence:
  [open-ended improvement allocates search before evaluation](../../theory/open-ended-improvement-allocates-search-before-evaluation.md),
  [lightweight search control does not license adoption](../../theory/lightweight-search-control-does-not-license-adoption.md),
  [backtracking keeps lightweight search control provisional](../../theory/backtracking-keeps-lightweight-search-control-provisional.md),
  [ad hoc explanation can be rational when error is cheap and local](../../theory/ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md),
  [cost-sensitive formalisms for tentative theory search](../../theory/cost-sensitive-formalisms-for-tentative-theory-search.md).
- Commitments:
  [theory and capacity building make the same kind of commitment](../../theory/theory-and-capacity-building-make-the-same-kind-of-commitment.md),
  [commitment, not derivation, creates new ground truth](../../theory/commitment-not-derivation-creates-new-ground-truth.md),
  [current-task fit alone does not warrant costly entrenchment](../../theory/current-task-fit-alone-does-not-warrant-costly-entrenchment.md),
  [prototype standing is revision-cost binding plus lost investment](../../theory/prototype-standing-is-revision-cost-binding-plus-lost-investment.md).
- Recursion and machinery investment:
  [an optimal long-run learning strategy invests in its own machinery](../../theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md),
  [computationally directed self-improvement is a reallocation](../../theory/computationally-directed-self-improvement-is-a-reallocation.md),
  [machinery persists by warrant, not position in a reflective loop](../../theory/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md),
  [reflection makes retained lessons second-order](../../theory/reflection-makes-retained-lessons-second-order.md).
- Retention economics:
  [LLM recompute cost inverts the store-vs-recompute default](../../theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md),
  [design rationale must preserve unregenerable decision premises](../../theory/design-rationale-must-preserve-unregenerable-decision-premises.md),
  [superseded choices are retained, superseded beliefs are not](../../theory/superseded-choices-are-retained-superseded-beliefs-are-not.md),
  [cheap adoption and weak retirement accumulate cost](../../theory/cheap-adoption-and-weak-retirement-accumulate-cost.md),
  [information value is observer-relative](../../theory/information-value-is-observer-relative.md).
- Generality claims:
  [universal software factory needs a declared universality axis](../../theory/universal-software-factory-needs-a-declared-universality-axis.md),
  [Commonplace builds a theory builder and tests whether it learns](../../theory/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md),
  [bounded-context orchestration model](../../theory/bounded-context-orchestration-model.md).

## What closes the workshop

1. A reconciliation map: for each of the brief's six directions, which
   existing notes already state the result, which tensions or gaps the
   economic framing exposes, and which of its claims are restatements in new
   vocabulary. A direction that adds nothing is recorded as such.
2. The work-level conjecture is either stated as a mechanism the library does
   not yet hold — including what separates open-ended, cumulative,
   knowledge-dependent work from purposeful activity in general — or
   rejected with the reason recorded. Its relation to bounded rationality,
   metareasoning, value of information and resource-rational analysis is
   checked against sources.
3. The claim that epistemic work is the shared layer of open-ended knowledge
   work is stated with a prediction a rival account would not make, tested
   against the weak points listed under "Why the operator wants this", and
   kept, narrowed, or dropped.
4. The architecture-level conjecture is stated with the evidence that would
   support or defeat it: reuse across domains, implementation complexity,
   human judgment still required, reliability, and the cost of maintaining
   the shared abstractions. It stays a conjecture; this workshop does not
   adopt it.
5. Survivors are extracted by type: new mechanisms to `kb/theory/`, finished
   but unadopted theory to `kb/theory/proposals/`, revisions to existing
   notes as separate commits, open questions to `kb/log.md` or a successor
   workshop. Then the directory is deleted.

## State

- 2026-10-30: closing condition 1 done in [reconciliation.md](./reconciliation.md)
  over the search files under [`search/`](./search/). Verdict: the
  work-level conjecture is a composition of held results; the new content
  is in direction 6 (routine-conversion economics, the architecture-level
  conjecture with defeaters) and one tension in direction 1 (whether value
  conjectures or only controllers are evaluated). Four discriminating tests
  and an extraction order are listed there.
- 2026-10-30: test 3 run in
  [routine-conversion-account.md](./routine-conversion-account.md) over four
  recorded cases ([search/conversion-cases.md](./search/conversion-cases.md)).
  The account predicted all four decisions; in two it disagreed with the
  decision taken and the outcome sided with it. One correction: exposure
  (the cost of a wrong routine before it is noticed) promoted to a named
  term. On Astra's objection the epistemic-versus-economic rivalry is
  deferred (relaxing triggers do not discriminate), and the extraction is
  narrowed to a section in the codify-versus-LLM note carrying the two
  considerations that guidance lacks. Extracted the same day as the "Stake and
  odds" section of the codify-versus-LLM note. Next: test 1 (controller
  cost) or the architecture-level proposal.
- 2026-10-30: test 1 concluded against the Russell–Wefald ingest (see the
  reconciliation map). Commonplace's practice is the zero-exchange-rate
  limit of their rule; no recorded preference flips. The operator's
  reading: that limit is the regime Commonplace is leaving as it adds
  unattended pipelines, so the net-value form becomes the required
  comparison as automation grows. Extraction: a qualification of the
  controller note adding unequal-cost comparison as an option beside
  matched-budget comparison, and a proposal candidate for cost-per-yield
  records on routine controllers. Next: the architecture-level
  proposal (closing condition 4).
- 2026-10-30: architecture-level proposal drafted in
  [architecture-proposal.md](./architecture-proposal.md) under the
  design-proposal type: the conjecture in `configure(G, K_P)` form with its
  universality axis declared, three options (interface first; second kind
  first then extract; no shared layer), forces, and adoption and defeat
  criteria reusing the bootstrap failure conditions and the ablation
  measures. Not adopted. Next: operator review, then extraction to
  `kb/reference/proposals/` and closing condition 3.

## Evaluation boundary and coupling

- Write scope while open: this directory only. Library notes are not edited
  from here; proposed revisions are drafted here and applied at extraction.
- [theory-refinement-interface](../theory-refinement-interface/README.md)
  owns the derive, compare, locate, revise, evaluate, and apply interface.
  Direction 4 (general operations) reads it as the starting interface and
  sends proposed changes there.
- [conjecture-store](../conjecture-store/README.md) and
  [decision-lifecycle-evidence](../decision-lifecycle-evidence/README.md)
  own storage and lifecycle of conjectures and decisions. Nothing here
  designs a generalized commitment store; the brief rules that out as
  premature.
- [reflective-improvement-divergence](../reflective-improvement-divergence/README.md)
  and [self-revision-design-space](../self-revision-design-space/README.md)
  own non-termination and redesign reach of the recursive levels; direction 3
  (recursion) cites them.
- [use-and-outcome-records](../use-and-outcome-records/README.md) owns
  operational observation records; direction 5 (retention)
  may use it as evidence of retention costs.
- The brief's research discipline binds: look for counterexamples and rival
  frameworks that explain the same phenomena, mark each claim as established
  result, argument, design hypothesis or untested empirical claim, and prefer
  a few substantial results to many notes.

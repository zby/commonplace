---
description: "Defines the epistemic layer (keeping derivable, decided and guessed apart and criticizing each) and names six roles that consume it, from prioritisation to retention, each with the failure a tool without it shows"
type: types/note.md
traits: [title-as-claim, definition, has-comparison]
tags: [constraining, learning-theory]
---

# Open-ended knowledge work shares one epistemic layer across roles

The **epistemic layer** of a kind of knowledge work is the machinery that
keeps three statuses apart and criticizes each by the standard its status
admits:

- **derivable**: what follows from the task and its sources, recoverable
  without new choices;
- **decided**: a **commitment**, a retained resolution the task does not
  entail, which becomes ground truth when committed and is repaired by
  supersession ([commitment, not derivation](./commitment-not-derivation-creates-new-ground-truth.md));
- **guessed**: a **search judgment**, an unretained decision about where
  effort goes, whose authority stops at allocating further search
  ([lightweight search control](./lightweight-search-control-does-not-license-adoption.md)),
  or a [tentative theory](./definitions/tentative-theory.md) not yet
  decided by test.

The claim: in open-ended, bounded, text-mediated knowledge work, six roles
consume this one layer, and each role names a failure that a tool without
the layer shows. The claim is universal over those conditions. A
counterexample is a tool that lacks the layer and performs a role below
without the failure that role names.

[Theory building](./definitions/theory-builder.md) (propose, derive,
criticize, blame, revise, select) remains the registered name for the
operations of roles 1, 5 and 6. Roles 2, 3 and 4 consume a different part
of the layer: which status a resolution has, and what a check can
establish. They need status and warrant tracking, not conjecture and
refutation. The layer is therefore wider than theory building, and this
note names it.

## Premises

1. **Open-endedness generates branches.** Consequential branches appear
   during the work, so the candidate set is not fixed in advance.
2. **Boundedness forces choosing before evidence.** An actor cannot develop
   every branch and must choose which to develop before decisive evidence
   about them exists ([search before evaluation](./open-ended-improvement-allocates-search-before-evaluation.md)).
3. **The context bound makes the work episodic.** A text-mediated actor
   works in a bounded context, so what one episode settles reaches the next
   only through a retained artifact. Accumulation needs explicit retention,
   and retention needs to know which retained items are ground truth.

Premise 1 creates the guesses, premise 2 makes acting on them unavoidable,
and premise 3 makes the statuses travel in artifacts, where a later reader
cannot recover them unless they were recorded.

## Roles

| Role | Consumer | Takes from the layer | Fails without it |
|---|---|---|---|
| 1. Prioritisation | effort allocation among branches | return guesses and their criticism | allocates by habit or cost alone and cannot improve its guesses |
| 2. Constraining | routine conversion | the split between derivable and decided | freezes a commitment as a fact; the relaxing trigger cannot be named in advance |
| 3. Retention | storage policy | the same split | stores derivations as truth or treats commitments as regenerable |
| 4. Evaluation reach | acceptance gate | what a check can establish | the accepted population drifts toward what the oracle measures |
| 5. Method improvement | reflective investment | criticism of the method itself | improvement stays inside the method's mistakes |
| 6. Application | theory building as a kind of work | all three statuses for theories | the work has no support beyond the actor's context |

**1. Prioritisation.** Effort allocation consumes guesses about what an
investment will return, and criticism of those guesses. The layer marks
them as search judgments, so evidence that routes a candidate to costly
assessment is not read as evidence that accepts it
([candidacy evidence licenses escalation](./candidacy-evidence-licenses-escalation-not-acceptance.md)).
A search judgment is then criticized by what it brings to stronger
evaluation ([search-controller test](./a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md)).
Without the layer, no guess is recorded as a guess, nothing can be compared
against its outcome, and allocation follows habit or cost.

**2. Constraining.** [Constraining](./definitions/constraining.md) commits
choices that narrow how a consumer reads an artifact; work is **constrained**
when it runs under such choices in natural language and **codified** when
it runs under [codification](./definitions/codification.md). Conversion
consumes the split between what the task fixes and what the converter
decided. Only a decided resolution is a bet that may need
[relaxing](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md),
and only a recorded bet has stated odds against which a stake can be sized
([stake and odds](./codify-versus-llm-decision-heuristics.md#stake-and-odds-how-much-to-build-on-an-uncertain-pattern)).
[Progressive constraining](./progressive-constraining-commits-only-after-patterns-stabilize.md)
is the same split applied over time: commit what recurs, keep the rest open.
Without the layer, the routine records a commitment as a fact, and the
condition that would retire it is invisible until it happens.

**3. Retention.** Storage consumes the same split for a different decision.
Commitments are ground truth and must be kept; derivations can be
regenerated and belong in a cache whose persistence must pay for itself
([recompute cost](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md)).
Design rationale keeps the premises its interpreter cannot regenerate
([unregenerable premises](./design-rationale-must-preserve-unregenerable-decision-premises.md)),
and a superseded choice keeps a historical witness while a refuted belief
loses standing ([supersession](./superseded-choices-are-retained-superseded-beliefs-are-not.md)).
Each rule needs the status recorded. Without it, a store either keeps
everything as truth or discards a commitment as if it could be recomputed.

**4. Evaluation reach.** An acceptance gate consumes what its check can
establish. Checks differ in how cheaply they verify correctness
([oracle strength](./oracle-strength-spectrum.md)), and automation extends
as far as verification does
([automation boundary](./the-boundary-of-automation-is-the-boundary-of-verification.md)).
When the layer records which qualities a check discriminates, unchecked
qualities stay marked as guessed. Without it, a pass reads as acceptance
of everything, and under the conditions in
[weakly discriminated qualities](./weakly-discriminated-qualities-tend-to-be-underselected.md)
the accepted population is enriched in what the oracle measures and not in
what it does not.

**5. Method improvement.** Reflective investment consumes criticism of the
method, not of its outputs. A machinery improvement can outrank immediate
learning because every later episode reuses it
([investing in machinery](./an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md)),
but machinery persists only by its warrant
([warrant, not position](./machinery-persists-by-warrant-not-position-in-a-reflective-loop.md)).
Without the layer the method's choices are not marked as decided, so
nothing invites criticism of them, and learning stays inside the method's
fixed decomposition
([inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md)).

**6. Application.** Theory building is itself a kind of knowledge work the
layer supports. A theory builder states theories in localized units, acts
on them, criticizes what they say and lets the result shape the next round.
Commonplace is the first worked case: it builds such a system and tests
whether it learns
([research companion](./commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md)).
Without the layer, a theory's status lives in the actor's context and ends
with the episode.

## Testable form

**General prediction.** A knowledge tool without the layer fails in the
ways the role table names. It is refuted by a tool that lacks the layer and
does not show a role's failure in that role.

**Record-level prediction (role 2).** A routine whose resolutions were
classified as derivable or decided at conversion can name its relaxing
trigger in advance. A routine adopted on cost alone cannot. A
resource-rational rival, in which routines are adopted because they are
cheap and good enough, predicts no difference in advance naming, because
cost does not record which resolutions are bets.

The prediction was abstracted from one pair in Commonplace's record; the
pair is its origin, not a test. The proposal behind the artifact-run engine
([ADR 113](../reference/adr/113-artifact-runs-execute-declared-plans-with-pinned-judgments.md))
called its premise, that harnesses would bring their own code scheduling,
"the operator's expectation, not an observed fact", and marked the
machinery that existed only because code could not launch sub-agents as
"the part expected to be discarded" (the archived proposal "Code-scheduled
workflows", which ADR 113 adopted).
[ADR 118](../reference/adr/118-analyses-run-as-a-workflow-over-headless-harnesses.md)
retired the engine when headless modes let code launch workers. The
`covered_by` tag mark
([ADR 026](../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md))
deferred adoption and named no condition for removal; the one head that
declared it dropped it twice, and
[ADR 090](../reference/adr/090-one-completeness-mark-reaches-members-in-one-hop.md)
retired it because nothing consumed the relation. A test needs conversions
recorded after this note, with their classification made at conversion.

## Weak point

Prioritisation needs preferences as well as beliefs: what a branch is worth
depends on what the actor wants, not only on what the branch will produce.
The layer covers beliefs, including return guesses relative to a given
objective. It does not choose the objective. A change of objective counts
as improvement only against a level outside both objectives
([objective revision](./revising-an-improvement-objective-is-licensed-from-outside-it.md)),
so goal change stays licensed from outside the work. Role 1 is therefore
partial: the layer improves allocation under a goal, not the goal.

## Scope

- The conditions are conjunctive: open-ended, bounded, text-mediated. Work
  with a fixed candidate set needs no prioritisation role; an actor whose
  context holds the whole work needs no retention role.
- The note asserts that the roles share one layer. It does not assert that
  Commonplace's machinery is the right implementation of the layer, or that
  support built for theory building generalizes to other kinds of knowledge
  work; that is the separate architecture-level conjecture in
  [reusable commitment support](../reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md).
- The six roles may not be exhaustive, and roles 2 and 3 consume the same
  split. They stay separate because their consumers and failures differ:
  conversion decides what to freeze, storage decides what to keep.

---

Relevant Notes:

- [theory builder](./definitions/theory-builder.md) — defined-in: the registered term for the operations of roles 1, 5 and 6, narrower than the epistemic layer
- [commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — grounds: the derivable/decided split that roles 2 and 3 consume
- [lightweight search control does not license adoption](./lightweight-search-control-does-not-license-adoption.md) — grounds: search judgment, the guessed status that role 1 consumes
- [open-ended improvement allocates search before evaluation](./open-ended-improvement-allocates-search-before-evaluation.md) — grounds: premise 2, choosing before decisive evidence
- [codify-versus-LLM decision heuristics](./codify-versus-llm-decision-heuristics.md) — extends: the stake-and-odds lens is role 2 priced; this note says why odds need the decided status recorded
- [weakly discriminated qualities tend to be underselected](./weakly-discriminated-qualities-tend-to-be-underselected.md) — mechanism: how role 4's failure operates under named selection conditions
- [revising an improvement objective is licensed from outside it](./revising-an-improvement-objective-is-licensed-from-outside-it.md) — grounds: the weak point, goal change licensed from outside the work
- [commonplace builds a theory builder and tests whether it learns](./commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md) — extends: role 6's worked case
- [ADR 113](../reference/adr/113-artifact-runs-execute-declared-plans-with-pinned-judgments.md) — abstracted-from: the conversion whose recorded premise named its retiring condition
- [ADR 090](../reference/adr/090-one-completeness-mark-reaches-members-in-one-hop.md) — abstracted-from: the conversion that named no condition and was retired by attrition
- [reusable commitment support across kinds of knowledge work](../reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md) — see-also: the architecture-level conjecture this note leaves out

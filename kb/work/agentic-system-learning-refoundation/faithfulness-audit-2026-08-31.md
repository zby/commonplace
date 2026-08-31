# Faithfulness audit of the program article against its source notes

2026-08-31. Audit of
[A research program for learning software factories](../../articles/a-research-program-for-learning-software-factories.md)
(draft as of commit `cb5901c2`) against its ~38 source notes. Method: three
parallel survey agents, one per cluster (factory ontology; theory and Naur;
evidence and warrant), each checking every note's claim against the article's
use of it; synthesis by the session agent. The operator deferred all edits.

Complementary to
[program-article-review-residuum-2026-08-30](./program-article-review-residuum-2026-08-30.md):
that file records research questions the article should not resolve in prose;
this file records article–note fidelity findings.

## Verdict

The skeleton is publishable-grade. The distinction ladder (substrate →
configured factory → factory development → minimal learning → coherent
modification → theory mediation) is layered, not circular; the exclusions
agree across notes; every citation traced is real and none inverts its note;
the load-bearing hedges ("practical conjecture, not a necessity theorem," "a
function, not a carrier," "the change need not be beneficial") survive
compression. The article is currently more confident than its own sources in
one systematic way, described next.

## 1. One-directional hedge harvesting (main finding)

Two independent cluster surveys converged: the article cites notes for their
limiting clause while dropping the guard that cuts against its own bet. Each
drop is individually defensible; together they run one way. Instances:

- `machinery-persists-by-warrant-not-position-in-a-reflective-loop` cited only
  for the half that excuses fixed components, at the exact sentence stating
  the bootstrap burden; the note's leading thrust (position does not exempt
  machinery from revision claims) and its trusting-trust governance section
  (the candidate must not author its own admission decision) are unused —
  though the latter answers the article's own self-confirming-loop worry.
- The evidence note's negative result — a later audit found defects the
  acceptance loop missed — is dropped from the only evidence section.
- Dropped guards, all pointing the same way: random mutation also searches and
  backtracks (`program-theory-sustains-search-under-delayed-feedback`);
  interpretation is not reach-assessment
  (`theory-mediated-self-improvement-needs-interpretation-and-retention`:
  collapsing them "makes a language model appear to warrant whatever it can
  explain"); system use does not assign blame
  (`system-use-selects-theory-fit-without-a-fixed-oracle`); a broad wrong
  theory produces negative transfer as widely as a right one would help, and
  cost accounting must be symmetric
  (`theory-mediated-learning-may-improve-sample-efficiency-under-shifts`);
  lightweight control can still be systematically bad
  (`lightweight-search-control-does-not-license-adoption`); a reversible
  branch can cause irreversible external effects
  (`backtracking-keeps-lightweight-search-control-provisional`).
- The "What would change the strategy" list is the natural home for these and
  does not contain them. Missing entries the notes supply: trajectory-reuse
  parity, theory-maintenance cost growing with system size, the
  reach-assessment gap.

The random-mutation guard is answered separately in
[random-mutation-defense.md](./random-mutation-defense.md).

## 2. The central technical obstacle is in the notes and absent from the article

`the-bitter-lesson-selects-production-methods-not-representational` names it:
credit assignment without a chain rule, and no established learned-localized
update method for a large interdependent corpus — precisely Commonplace's
quadrant. The decisive open problem for the factory-learning path is already
articulated in a source note and never appears in the article. Related:
"comparable total cost" recurs as a phrase but is never operationalized
(residuum §6 has candidate denominators), and the "theory withheld"
experimental arm has an unnamed bundle confound (withholding theory also
changes prompt length, retrieval, a delivery slot) that
`an-experiment-identifies-only-the-contrast-it-actually-runs` warns about and
the article reduces to one boilerplate sentence.

## 3. The factory half of the thesis has no evidence, unstated

By the article's own criterion, the Commonplace episode is theory-mediated
solution modification, not factory learning: it changed knowledge-base
content consumed by later authoring, not reusable family production machinery
consumed by later production. The article does not claim otherwise, but never
admits that its only evidence section leaves the factory-learning half empty.
Also in that section: "retained theory guided the work" is an outcome level
under the theory-present condition, not a mediation effect (the note bounds it
as an inference from retrieval plus edit specificity); and the note's
"selection machinery exposed by the episode" list — three recurring operator
judgments plus candidate reusable outputs — is the article's best available
support for its own longitudinal-study bullet and is cited nowhere.

## Smaller items

- **Uncited structural notes.** Three notes do structural work but are never
  linked in the body:
  `a-proposal-selection-loop-requires-search-evaluation-and-retention`
  (supplies the minimal-learning pipeline's vocabulary), 
  `theory-mediated-self-improvement-needs-interpretation-and-retention`
  (supplies the evidence ladder and the four-roles table),
  `a-software-factory-is-family-scoped-lifecycle-production-machinery` (owns
  the Greenfield reconstruction). Uncited, they also fail to transmit their
  guards.
- **Derivation drift.** The four-roles table silently drops the fifth
  function, reflective membership; ladder level 3 drops "principled retention
  or explicit rejection after a refuting opportunity also counts."
- **Naur.** The TL;DR's "Following Naur… indispensable functional part" is
  looser than the body, which correctly marks functionalization as the
  program's move against Naur's carrier-bound claim. The ingest's own
  limitations (two cases, impossibility claims exceed the anecdotal evidence,
  construct difficult to vary) are not carried, though the article inherits an
  indispensability constraint from that source. The ingest's unused bearer
  test — provision of premises the interpreter cannot regenerate — is the
  best available sharpener for the testbed section.
- **Mild epistemic upgrades.** "Explains why" for the scheduler–LLM note that
  calls itself a conjecture; a flat construction-vs-acquisition negative where
  `factory-construction-does-not-establish-knowledge-acquisition` bounds the
  claim to its retained sources.
- **Missed supporting argument.** The scheduler note's
  codification/relaxation point makes the symbolic layer itself a learning
  target; the article's "this starting point does not require the software to
  learn" walks past an argument for its own thesis.
- **Narrowings that lose method.** `task-families-and-product-families` loses
  its declared-frame checklist and the manually-supplied-factories-per-domain
  trap that the "broad production reach" row needs;
  `the-deployed-system-not-the-model` is reduced to carrier pluralism, losing
  the evaluation-boundary vs writable-surface distinction and the clause that
  human edits remain engineering inputs unless the claimed transition
  computationally determines their content.

## Suggested repair order (all deferred)

1. Fold the dropped guards into the abandonment list — cheapest repair of the
   one-directional pattern.
2. Name credit assignment without a chain rule as the program's central open
   problem.
3. Evidence section: restore the audit-found-defects result and state plainly
   that no factory-learning evidence exists yet.
4. Wire the three orphaned structural notes into the prose.
5. Naur TL;DR wording; ingest limitations; the two epistemic upgrades.

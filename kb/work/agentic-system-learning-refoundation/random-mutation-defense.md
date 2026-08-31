# Defending theory-guided search against the random-mutation baseline

Working position paper, 2026-08-31. Posed by the operator during review of
[A research program for learning software factories](../../articles/a-research-program-for-learning-software-factories.md).
Deliberately not applied to the article yet.

## The problem

[Program theory sustains search under delayed feedback](../../notes/program-theory-sustains-search-under-delayed-feedback.md)
carries a guard the article dropped: search and backtracking are not
sufficient evidence of theory possession, because random mutation does both.
If the program's evidence for theory-holding is the search-and-backtrack shape
of the behavior, the claim is confounded.

## The operator's reframe

Admit random mutation with backtracking as a legitimate mechanism rather than
a confound to exclude. The program then claims only that the search space is
enormous and that weak natural-language guidance — theories held as
conjectures — helps.

The reframe is evidentially correct. The program never needed "the system
backtracks, therefore it holds a theory." Restated comparatively, random
mutation becomes a baseline arm: at matched budget, theory-present arms should
beat theory-absent arms on the sequence-level outcome. That is already the
shape
[factory-learning mechanisms should be compared on the same causal job](../../notes/factory-learning-mechanisms-should-be-compared-on-the-same-causal-job.md)
requires.

## Why the size-only version is weak

Two objections hit "the search space is enormous" on its own:

1. The Bitter Lesson answer is that enormous spaces are what compute plus
   learned priors are for. AlphaGo searched an enormous space with no explicit
   theory; a learned policy did the allocation. Space size argues against
   uniform random mutation, which nobody proposes.
2. Uniform random mutation is a strawman baseline. The serious theory-absent
   baseline is the same LLM with no retained project state. Generic priors in
   weights already collapse the space by orders of magnitude, and
   [natural-language project state specializes search heuristics](../../notes/natural-language-project-state-specializes-search-heuristics.md)
   says retained theory only specializes them. The defense must say what the
   specialization buys that the generic prior does not.

## Three stronger legs

### 1. Evaluation incompleteness

Mutation plus selection is only as good as the oracle that selects. In the
article's target regime — local tests do not exhaust purposes, decisive
feedback is delayed — the oracle under-specifies by construction. Undirected
search does not merely find good candidates slowly; it converges on
oracle-satisfying, organization-destroying candidates, because nothing in the
loop represents the unstated commitments. The genetic-improvement literature
demonstrates the pathology: GenProg-style patch search "fixes" bugs by
deleting functionality the test suite does not cover. *(Cited from model
knowledge; verify the citation before promoting this claim to a note.)*

On this leg the theory's job is to stand in for the missing part of the
evaluation: it states, at proposal time and at read-back, what must be
preserved that no test says. The argument holds even with unlimited search
budget, and it keeps the defense attached to Naur's coherent-modification
target instead of retreating to generic search efficiency.

### 2. Credit assignment and update bandwidth

Backtracking needs an address: which earlier commitment does a late failure
indict, and what replaces it? Random backtracking exists, but the space of
revert-point × alternative pairs grows combinatorially with sequence length,
and selection extracts only a few bits per trial. An explanation compresses
that: one surprising consequence, read against a theory, can indict a specific
commitment and revise a whole region of the search space at once.

Per-observation update bandwidth is the asymmetry. Mutation-plus-selection
learns at bits per trial; explanatory revision learns at the reach of the
explanation. Where trials are few, slow, and expensive — long-lived software
with delayed consequences — that is the regime argument for theory. The
blame-assignment gap in
[system use selects theory fit without a fixed oracle](../../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md)
is this leg stated negatively.

### 3. The wrong-theory signature

The best discriminating observable. Undirected search fails isotropically:
errors scatter, uncorrelated across episodes. A wrong theory fails coherently:
correlated, direction-specific errors that bend the whole sequence the same
wrong way —
[theory-mediated learning may improve sample efficiency under shifts](../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md)
already predicts that a broad wrong theory produces broad negative transfer.
Correlated directional failure is something random mutation cannot produce.

This converts the plausible-but-wrong-theory arm from a mere control into the
discriminating arm: if withholding theory changes little but wrong theory
hurts systematically in the predicted direction, the theory was load-bearing.
A mechanism whose failures are directional is a mechanism that is steering.
This connects to the single-premise-corruption arm and its preregistered
negative-transfer prediction in
[program-article review residuum §3](../theory-mediated-self-improvement-series/program-article-review-residuum-2026-08-30.md).

## The honest residue

Legs 1–3 defeat random mutation. The standing rival after that is implicit
learned guidance — trajectory reuse, learned policies, the model's accumulated
prior. Against that rival, space size does no work and leg 1 is shared: a
learned policy can also internalize unstated commitments. What remains
specific to the natural-language surface is leg 2's addressability — one
delayed consequence can rewrite a conjecture directly, where a policy needs
gradient-scale data — plus inspectability and cross-artifact coordination.
That is the article's contingent bet, correctly isolated; the random-mutation
defense must not quietly claim that territory.

## Landing sites (deferred)

- One paragraph in the article's "A weak theory can control fallible search"
  section: random mutation with backtracking is a baseline, not a confound;
  the claim is comparative at matched budget; the distinguishing predictions
  are oracle-underspecification failures in the undirected arm and
  direction-coherent negative transfer in the wrong-theory arm.
- Candidate note: the wrong-theory failure signature (directional coherent
  failure distinguishes steering from search). No existing note appears to
  carry this claim.
- The update-bandwidth argument may belong in
  [program-theory-sustains-search-under-delayed-feedback](../../notes/program-theory-sustains-search-under-delayed-feedback.md)
  as a mechanism, or as its own note.

## Links

- [program-theory-sustains-search-under-delayed-feedback](../../notes/program-theory-sustains-search-under-delayed-feedback.md) — rests-on: source of the confound this paper answers
- [an-experiment-identifies-only-the-contrast-it-actually-runs](../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — rests-on: the comparative restatement must run the contrast it claims
- [open-ended-improvement-allocates-search-before-evaluation](../../notes/open-ended-improvement-allocates-search-before-evaluation.md) — see-also: why allocation matters before decisive evaluation exists
- [program-article-review-residuum-2026-08-30 §3](../theory-mediated-self-improvement-series/program-article-review-residuum-2026-08-30.md) — see-also: experiment arms this argument's predictions attach to

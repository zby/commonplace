# Adjoiner: direction under a fuzzy objective

Unmerged material for [the reflective self-improvement article](../articles/reflective-self-improvement.md), written in the article's register so passages can be lifted directly. Two connected arguments from a 2026-07-30 discussion; how to merge them is not yet decided. Candidate insertion points at the end.

## Part 1: why now — the pathway existed, the evaluator did not

Computational reflection is decades old, so the pattern this article names needs an answer to "why did this not happen in the 1990s?" The historic reflective systems — 3-Lisp, the metaobject protocols, reflective middleware — built exactly what we call the causal wire: a self-representation whose modification changes behavior. What they lacked was a value function. Direction always came from a human programmer deciding what to change; reflection was a capability, never a policy, and those systems could self-change in any direction precisely because they had no way to prefer one.

The Gödel machine was the first architecture to bind self-change to a value function: expected utility, with proof as the acceptance test. But its evaluator was proof search — sound and practically empty, since almost no real improvement is provable. The direction existed and could not be traversed.

Two things should be kept separate here: the **objective** and the **evaluator**. Declaring an objective was always cheap — anyone could have written "better means X" on a reflective Lisp system in 1987. The missing resource was the evaluator: something that can judge an arbitrary proposed change against a declared objective. That is what LLMs provide, and it extends the justification-regime progression already in the article: proof (sound, empty domain), benchmark (cheap, narrow domain), LLM judgment (broad domain, unreliable). "Not yet very good, needs more machinery" is then precise: the machinery — external criteria, fresh-context review, gates, human adoption where the oracle runs out — is what converts an unreliable-but-broad evaluator into a usable one, and it is what the article's structure section describes.

Two caveats stay attached. LLMs supply the proposer as well as the judge — the historic systems lacked candidate generation too — and having the same model in both roles is the trusting-trust problem the article already names. And the LLM must remain the evaluator, never the objective source: its trained preferences are an implicit value function that would fill that role silently if allowed.

## Part 2: the remaining frontier — direction

The proposer/judge split hides a third function. Given a named target, LLMs propose well; given a criterion, they judge tolerably. What they do not do well is the step above: taking a fuzzy terminal objective and deciding what to work on — noticing which strain matters, forming the sub-objective, allocating attention.

The article already measured this without naming it. In the index episode's division of labor, the agent drafted (proposer), the validator checked (judge), and the maintainer noticed the strain, initiated the fix, and accepted the result. Two of those three human contributions are direction. Adoption is theorized extensively in the article; initiation is barely named.

Three mechanisms plausibly compound to make LLMs weak here:

1. **Decomposing a fuzzy objective requires a causal theory of the system, not text skill.** To pick the sub-goal that serves "better-warranted knowledge work per unit of human judgment," you need a model of what actually produces that value — which interventions compound, which are cosmetic. Absent that theory, LLM sub-goal proposals drift toward the demonstrable: tidying, added structure, surface legibility.
2. **The strain signal lives in the operator.** The operator notices what matters by repeatedly paying the costs. A stateless agent accumulates no felt history of what keeps hurting; the pain signal that drives agenda-setting is not architectural, it is in the operator's head. This is the statelessness argument applied one level up from routing.
3. **Sub-goal warrant cannot be checked, only bet.** A proximate target is checked for achievement, not for warrant; choosing reach as the bar was a human bet the loop never evaluates. Sub-goal selection is warrant allocation all the way down, with no oracle to earn migration against.

There is also a trade coupling this to the justification-channel story: **self-direction is easy exactly where objectives are narrow.** The Darwin Gödel Machine chooses its own next move because its objective is a number — and the price is that it can only move in directions the number can see. Commonplace keeps the objective fuzzy and broad, and the price is that direction stays human. Giving the agents a measurable proxy would buy self-direction and invite Goodhart in the same gesture.

The honest three-layer "why now" is therefore: the pathway was solved decades ago (reflection); the proposer and judge arrived with LLMs; direction under a fuzzy objective is the current frontier — still human in this system, and likely in every system that has not narrowed its objective to dodge the problem. For Commonplace specifically the honest statement is: the objective is declared but not instrumented, and most movement is directed by the operator; the agents are not yet good at choosing sub-goals that serve the declared goal.

Partial machinery, if wanted: make the operator's strain legible (a recorded friction channel the agents can read); retrospective credit assignment over past sub-goals (which bets paid, turning warrant from pure bet into slow evidence); a maintained candidate-directions list periodically re-ranked against the objective. None of it solves the problem; all of it moves direction from "entirely in the operator's head" toward "partially on the record."

## Candidate merge points

- **Part 1 → "The pattern" section**, after the computational-reflection sentence: the why-now paragraph answers the question that sentence raises. The Gödel-machine material partly overlaps the precedents list's limiting-case bullet — merging would consolidate them.
- **Part 2 → the bitter-lesson section**, upgrading "Humans still perform much of the diagnosis, the credit assignment, and the acceptance" from a list of residues to a claim: what remains human is specifically direction, and it is the capability with no current machinery.
- **A sentence at the division-of-labor paragraph**, naming initiation as the under-theorized human function.
- Independently of the article: a candidate note for `kb/notes/` — roughly "LLMs supply the proposer and the judge; direction under a fuzzy objective is the remaining human function" — with the episode's division of labor and the DGM narrowness trade as evidence.

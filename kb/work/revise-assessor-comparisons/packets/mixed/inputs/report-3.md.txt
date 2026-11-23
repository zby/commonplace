---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/premise-decomposition-gate.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
criterion: kb/instructions/premise-decomposition-gate.md
criterion-sha256: 116fc35b1e54759064658a1172d7ed0a3007bf576f6744f6f016f473d477805d
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: e7b5b9628cda4057bafd70a31c2a7351
completed-at: '2026-11-20T18:57:07Z'
findings:
- scope: passage
  quotes:
  - A partial order can represent the preferences we can defend under a consistent
    set of priorities.
  reason: 'DOUBTFUL — (universal, unmoded) on-balance pairwise preferences made under
    consistent priorities are transitive, so they form a partial order — a partial
    order requires transitivity, but on-balance judgments over several dimensions
    need not be transitive even with fixed priorities. If each pairwise judgment turns
    on whichever dimension differs most between that pair (speed for A over B, compatibility
    for B over C, library support for C over A), the result is a cycle, not a partial
    order. Priorities consistent enough to guarantee transitivity begin to look like
    a (possibly partial) weighting, which is what the note says it does without. The
    note''s hedge that the order does not ''guarantee that a single stable ranking
    exists'' concedes instability but not intransitivity. Repair: state transitivity
    as a condition the judgments must meet for the partial-order representation, or
    describe the judgments as a set of defended pairwise preferences that need not
    compose. The central commitment survives because guiding a successor-versus-predecessor
    choice needs only the pairwise judgment — LOCAL — instance'
- scope: document
  quotes: []
  reason: 'DOUBTFUL — (unstated, universal) a sequence of on-balance acceptances of
    successors accumulates into improvement, which requires the judges'' priorities
    to stay stable across successive decisions — the note guards against cumulative
    drift (''Compare the whole table with its earlier, shorter version'') but not
    against oscillation. Example: a review gate is tightened because missed ambiguities
    are salient, and later loosened because operator friction is salient. Each step
    is on balance defensible at its time, yet the system returns to its start and
    pays for both changes. Comparing with the earlier version catches this only if
    the earlier judgment and its priorities were retained. Repair: say that on-balance
    judgments guide improvement only relative to recorded priorities, and that a reversal
    of an earlier judgment must name which priority changed — LOCAL — instance'
- scope: passage
  quotes:
  - we choose changes by asking whether they yield more useful and better-warranted
    knowledge work for the human judgment spent, on balance
  reason: 'DOUBTFUL — (practical commitment) this objective is specific enough to
    be identifiable independently of the changes it is used to judge, as the linked
    note requires for antecedence — ''useful'', ''better-warranted'' and the internal
    ''on balance'' leave room for post-hoc redescription that the linked note says
    makes the category vacuous. The AGENTS.md line example shows it: the same objective
    can be cited both for keeping the line (routing gain) and for removing it (load
    on near-limit tasks), with the objective itself unchanged. The note''s discipline
    — name which work changed, whose costs count, and what observation would change
    the recommendation — supplies most of the independence, but it is attached to
    the judgments rather than the objective. Repair: state which observable components
    the objective comprises, or say explicitly that antecedence is carried by the
    per-judgment reasons — LOCAL — instance'
- scope: passage
  quotes:
  - investigate an unknown only if a plausible answer could reverse the choice
  reason: 'DOUBTFUL — (rule scoped to ''the decision at hand'') the set of plausible
    answers is known well enough to apply the rule before investigation — the rule
    moves the judgment into ''plausible'', which is itself uncertain and judge-dependent.
    In the AGENTS.md example, the frequency of near-limit tasks and whether one line
    tips them are both unmeasured; one judge can deem a reversing frequency implausible
    and act, and another can deem it plausible and investigate, with the rule endorsing
    both. The rule is a sound necessary condition for decision-relevant investigation,
    but it does not settle when to investigate without a further account of how plausibility
    ranges are set or bounded cheaply. Repair: add that bounding the plausible range
    is often the first investigation, or give the condition under which a range is
    accepted — LOCAL — instance'
- scope: passage
  quotes:
  - The compatibility cost falls on identifiable callers
  reason: 'DOUBTFUL — (unmoded, read universal within the 3.11 example) upgrade losses
    fall on callers who can be identified and tested before moving — silent behaviour
    changes in paths a test suite does not exercise, transitive dependencies that
    are only partly tested, and downstream users of a published library that drops
    3.10 support all bear costs that pre-move testing does not reveal. These are the
    costs the library-hours case warns a higher total can hide, and the 3.11 default
    rests on their absence. The note already concedes that widespread blockers would
    challenge the default. Repair: qualify the claim to the losses a team''s tests
    and dependency inventory can find, and name untested paths as residual risk —
    LOCAL — instance'
- scope: passage
  quotes:
  - Those reasons can be checked independently of who offered them.
  reason: 'DOUBTFUL — (unmoded) the reasons an agent gives for an on-balance preference
    can be checked independently of the agent — the factual components (which work
    changed, what a test showed) can be checked this way. The weighing (''worth the
    judgment spent'', ''whose costs count'') cannot be checked; it can only be judged
    again by the checker against their own priorities. A reviewer who reaches a different
    weighing has not falsified the reason. The note''s next sentence (''makes a judgment
    criticizable'') is the accurate form. Repair: separate checkable factual reasons
    from the weighing, which is open to criticism but not to verification — LOCAL
    — instance'
- scope: passage
  quotes:
  - Neither needs a score for every Python release before choosing the next one to
    use.
  reason: HOLDS — (universal within a pairwise successor choice) choosing between
    a predecessor and a successor does not require a score over every alternative.
    The hunt considered many-candidate selection, such as choosing among many prompt
    variants, where pairwise judgments scale poorly. The note's scope is a successor
    against its predecessor, which that case falls outside, and its transitivity limits
    are treated in the partial-order finding.
- scope: passage
  quotes:
  - it cannot supply the weights merely by assigning each feature a score
  reason: HOLDS — (universal) analysis can expose a trade-off but cannot by scoring
    features supply the value weights between them. The candidate counterexample is
    weights that are fixed externally, such as contracts, SLAs or a factory threshold.
    The note handles this through binding requirements fixed in advance, where the
    weights come from a prior judgment rather than from the analysis.
- scope: passage
  quotes:
  - Even a perfect attendance count would not decide which hours to keep.
  reason: HOLDS — (universal for the stated case) when the disagreement is over whose
    loss counts, more measurement does not resolve it. The hunt looked for a case
    where better counts would reveal that the Tuesday group has an alternative after
    all. That would change the facts the commitment applies to, not the commitment,
    so it leaves the premise standing.
- scope: passage
  quotes:
  - Use of a new instruction shows uptake, not a gain.
  reason: HOLDS — (universal) use of a change does not establish improvement over
    its predecessor. No counterexample was found; even when uptake displaces a worse
    practice, the gain is established by comparison with that practice, not by uptake
    itself.
- scope: passage
  quotes:
  - records a validator finding a member the documented search missed
  reason: HOLDS — (factual, sourced) the linked tag-readme trace records that the
    covered_by check caught a block-YAML-tagged member the documented rg recipe missed,
    and that the recipe was corrected. The linked evidence supports the local gain
    the note claims, and the note does not extend it to a judgment on the marks overall.
- scope: passage
  quotes:
  - CPython 3.13.1 named the local file that hid the standard library module and suggested
    renaming it.
  reason: 'HOLDS — (factual) the illustrative Python behaviours match the documented
    releases: 3.13 added the module-shadowing hint, 3.12 reported a likely circular
    import, inspect.getargspec was removed in 3.11, and tomllib and asyncio.TaskGroup
    arrived in 3.11. The hunt found no mismatch. The timing figures are presented
    as one workload on two local builds and are not generalized.'
- scope: passage
  quotes:
  - an on-balance judgment does not override a binding requirement
  reason: HOLDS — (universal, procedural) a requirement fixed before development takes
    precedence over a later on-balance judgment. The hunt considered a binding requirement
    later found to be mistaken. Revising such a requirement is a separate decision
    about the requirement, not an on-balance override inside the comparison, so it
    does not defeat the premise.
contract: report
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/e7b5b9628cda4057bafd70a31c2a7351/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/1fc8793041fbbf5756d92d17/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/e7b5b9628cda4057bafd70a31c2a7351/outputs/review.md
raw-output-sha256: d8bf4efd323e66201675d75cfcaf3ebba2dc4acf25549fc61752cec7738e33f2
---

# Premise decomposition: On-balance judgments can guide improvement without a global measure

**Register:** claim
**Central commitment (one sentence):** Decisions about whether to keep or adopt a change can be guided by on-balance pairwise judgments that name which work changed, for whom, and why it matters, investigating only unknowns that could reverse the choice, without first constructing a global score or total order over alternatives.

## Premises and counterexamples

The commitment has three layers, and each consumes different premises.

First, **sufficiency of the pairwise reason-based judgment**: the claim that no score is needed, that analysis cannot supply value weights, and that some disagreements are about whose loss counts rather than about facts. These hold within the note's stated scope of successor-versus-predecessor choices.

Second, **composition**: the note presents the judgments as forming a partial order and as accumulating into improvement over successive changes. The weakest point is here. "Without a global measure" and "guides improvement" pull against each other once judgments are chained. A partial order needs transitivity, and accumulated improvement needs stable priorities. The note hedges both ("consistent set of priorities", "does not guarantee a single stable ranking") but states neither as a condition the method must meet. A narrower framing repairs both: a guided pairwise choice with recorded priorities.

Third, **operability in Commonplace**: the declared objective, the reversal-only investigation rule, identifiable callers for losses, and checkability of reasons. Each is dented by an ordinary case: post-hoc redescription under a vague objective, judge-dependent plausibility ranges, untested paths, and weighing that can only be re-judged. Each dent is answered by a boundary condition or a separation the note nearly makes already.

No premise failure was found that breaks the core mechanism. Every non-`HOLDS` finding is LOCAL.

## For the human

Look first at the partial-order sentence and the unstated assumption of stable priorities across successive judgments: they are where "without a global measure" meets "guides improvement", and the note currently hedges rather than states the condition.

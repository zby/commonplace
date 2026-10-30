---
description: "Defines the value of a computation as its benefit to the agent's next external action minus time cost, with meta-greedy and single-step approximations; lands in the KB's search-control and controller-cost work"
source: https://people.eecs.berkeley.edu/~russell/papers/aij-principles.ps
captured: "2026-10-30"
capture: ps2pdf+pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: a88bf373ae756d30b0359e08b243601fa1a3f047279e2ac16a3baa32db305d4e
ingested: "2026-10-30"
occasion: "The workshop kb/work/open-ended-work-economics/ runs a discriminating test (test 1, \"controller cost\"): add opportunity or computation cost to the evaluation of a search controller and check whether that changes which controller is preferred on recorded Commonplace episodes (connect-report routing, review bundle ordering). The KB needs from this source, as the paper that defines value of computation: (a) the decision-theoretic definition of the value of a computation (benefit to the object-level decision minus cost) and the net value with time cost; (b) how a metalevel controller is evaluated; (c) the meta-greedy and single-step assumptions and their stated limits; (d) whether and how the framework compares two controllers that consume different resources or have unequal cost; (e) what the framework assumes that Commonplace's setting may lack, such as numerical utilities, known cost models and a fixed object-level decision. Keep claims to what the text says."
type: types/ingest-report.md
domains: [metareasoning, search-control, bounded-rationality, decision-theory]
---

# Ingest: Principles of Metareasoning (Russell and Wefald, 1991)

## Classification

This is a scientific paper. It is mainly theoretical: it derives a formula for the
value of computation and its approximations. A short applications section
sketches algorithms and reports results, with details deferred to cited papers.
Author: Stuart Russell and Eric Wefald (UC Berkeley), published in *Artificial
Intelligence* 49 (1991). Russell later co-wrote the bounded-optimality work
already ingested here.

## Summary

Russell and Wefald treat computations as actions and select them by expected
utility. A computation is worth something only because it can change which
external action the agent takes, and it costs the time it uses. The net value
of a computation is the utility of the state after it minus the utility of
taking the current default action now (eq. 2). For a complete computation,
which ends in commitment, this is the utility of the action it recommends, taken
after the computation, minus that of the default action (eq. 3). Partial
computations are valued by summing over ways of finishing the deliberation
(eq. 4). For agents that act on utility estimates, the paper scores both the new
and the old best action with the later estimate (eqs. 5, 9). This makes a
computation that does not change the choice worth only its time cost. Under
stated separability conditions, net value splits into estimated benefit minus
time cost, V̂ = Δ − TC(|Sj|) (eqs. 15–19). The ideal controller performs the
computation with the highest expected net value until none is positive, then
commits (Section 4.2). Two approximations make this tractable. Meta-greedy
looks one step ahead. Single-step values a partial computation as if it were
complete. Fully relaxing either one would make the other exact (Section 5.3).
Expected values come from distributions over how similar past computations
revised estimates. Under subtree independence they reduce to closed-form
integrals (eqs. 26–27). The applications report DTA\* and MGSS. Within a fixed
heuristic or evaluation function, these beat A\*, RTA\* and alpha-beta. The
paper names a "meta-greedy barrier" that limits MGSS against deeper searchers.

## Contribution assessment (our opinion)

This is a tentative judgment. The problem is how to choose which computations a
resource-bounded agent should perform. It matters well beyond game search. The
paper's main contribution is to make Good's type-II rationality and Howard's
information-value theory precise for computation. It does so in three steps: it
defines value through changed action choice, it states which estimate to use
when the estimates themselves change, and it identifies time cost as a
separable term. The paper credits Good with the ideal algorithm. It names
independent parallel work by Horvitz, Hansson and Mayer, and Dean. Its
originality therefore lies in the formulation and the two named approximations,
not in first proposing the idea. The paper says its formal justification is
only heuristic, because estimated probabilities do not obey the probability
axioms. The empirical support is a sketch: one table and an uncaptured figure,
with details in other papers. The definitions and approximations are the
durable part. The performance claims are claims, not demonstrations, in this
text. Limited evidence narrows the paper but does not undermine its central
contribution, which is conceptual.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is the **formal basis** for the KB's search-control cluster,
which does not yet use metareasoning vocabulary. It defines a computation's value
only by whether it changes a later action choice. This is a prior formal
statement of the operative test in [a failure explanation becomes search
control only when it changes a later branch
decision](../theory/failure-explanation-changes-later-branch-decisions.md).
It bounds that note's test rather than corroborating it, because a definition
is not a test the note could fail. The source's split between partial
computations, which change internal state, and complete computations, which
commit to external action, compares with [lightweight search control allocates
further search without licensing
adoption](../theory/lightweight-search-control-does-not-license-adoption.md) on
the axis of a deliberative step's authority. The source also gives an
allocation rule (highest expected net value; stop when none is positive), which
that note explicitly leaves unspecified. The source supplies a model family
that [cost-sensitive formalisms for tentative theory
search](../theory/cost-sensitive-formalisms-for-tentative-theory-search.md)
omits: decision-theoretic pricing of whether to compute further. It gives a
formal computation-side precedent for the bounded-rationality entry in
[information value is observer-relative](../theory/information-value-is-observer-relative.md):
value depends on the agent's current estimates, its decision and its time cost.

Among sources, it is the predecessor of [Provably bounded-optimal
agents](./provably-bounded-optimal-agents.ingest.md). Its Section 7 names the
gap that follows when metareasoning has costs of its own, and the later paper
moves optimality to the program level. It compares with
[PrimeScientist](./primescientist-research-effort-allocation.ingest.md) on the
axis of charging deliberation and action to one budget. PrimeScientist supplies
a budget-sensitive selection rule; R&W derive time cost inside net value. It
compares with [Pirolli's information
scent](./pirolli-proximal-information-scent-distal-content.ingest.md) on the
axis of using one value estimate both to select the next step and to stop. Its
Section 2 claim that substantive rationality "can only arise by prior design or
adaptation" compares with [codify-versus-LLM decision
heuristics](../theory/codify-versus-llm-decision-heuristics.md) on the axis of
precompiled decisions versus run-time deliberation. That transfer predates LLMs,
so it still needs an argument.

## Extractable Value

1. **(a) Value of computation, stated exactly.** Net value is the utility after
   the computation minus the utility of acting on the current default now.
   Benefit is Δ, the estimated intrinsic-utility gain of the new best action over
   the old one, both scored with the later estimate. Cost is TC of elapsed time.
   If a computation leaves the choice unchanged, Δ = 0 and its net value is
   negative by its time cost (Section 5.1.1). This gives test 1 a scoring rule:
   a routing or ordering step earns credit only when it changes a later
   decision, and every step pays its cost. Scoring the old choice with the old
   estimate (the Howard form, eq. 13) can credit computations that only raise
   confidence. The paper rejects this for post hoc evaluation. Footnote 4 also
   argues that a computation whose only possible outcome is increased confidence
   has no value. [quick-win]
2. **(d) Unequal-cost controllers are compared by pricing cost into one utility
   scale and sweeping the exchange rate.** DTA\* is compared with A\* and RTA\* on
   total solution cost, a weighted sum of path cost and search cost. The
   comparison is repeated across values of the "rate of exchange" between
   computation cost and path length. The paper reports that DTA\* wins at every
   rate and approaches A\* as computation cost tends to zero. MGSS versus
   alpha-beta reports wins, nodes per game and CPU seconds side by side. The
   captured text gives no combined metric for that comparison. The framework has no
   mechanism for several incommensurable resources. Section 4 notes that
   computations vary in time, quality, certainty and interruptibility, but treats
   only time and quality. Space appears only as future work. For test 1, a
   preference flip should be reported across a range of exchange rates, not at
   one assumed rate. [experiment]
3. **(b) Controller evaluation has two levels.** Normatively, a controller is
   judged against the ideal rule: take the highest positive expected net value,
   then commit. Empirically, the paper judges implemented controllers by
   outcome quality net of computation cost on a fixed base-level problem. Both
   comparisons hold the decomposition fixed. MGSS and alpha-beta share one
   evaluation function, and DTA\* takes its cost ratio as a given parameter. The
   results therefore compare control policies within one base-level search,
   not alternative search designs. [quick-win]
4. **(c) Meta-greedy and single-step assumptions and their limits.** Meta-greedy
   fixes a meta-meta-level depth limit of 1. Single-step values a possibly
   partial computation as if it were complete. The paper states that the
   simplification comes from using both together: relaxing either one alone
   would make the other exact. Single-step underestimates computations that
   matter only because they enable later ones (worked example, Section 5.4).
   In game trees this produces the "meta-greedy barrier": once no single
   expansion can change the best move, the controller stops. The paper says
   this does not occur in single-agent search. Both assumptions "can be
   validated only by consideration of the domain of application". For test 1,
   this predicts a specific failure: a myopic controller undervalues setup steps
   such as gathering context before routing. [quick-win]
5. **(e) Assumptions the framework needs.** The paper assumes:
   - the utility function is fixed (footnote 3);
   - base-level action outcomes are known;
   - a current best default action exists at every moment;
   - action utilities have numerical estimates (the estimated-utility model);
   - prior statistics exist on how a class of computation revises those
     estimates;
   - time cost is separable and independent of the action. The paper says this
     fails in domains such as hunting or war, and sometimes in chess
     (footnote 12);
   - decisions are episodic;
   - computation can be split into modular steps that can run in varying orders;
   - for the closed forms, subtree independence holds.
   The paper itself says theorem provers lack a "current best move" and so do
   not fit. It also says its statistical approach "will fail when the value of
   the computation depends on more than a few aspects of the current state."
   Each of these is a checkable precondition before test 1 borrows the
   framework's quantities. [quick-win]
6. **Ideal control as a missing family in the cost-sensitive catalogue.** The
   catalogue could gain value of computation, time cost, the
   stop-when-none-positive rule and the two myopic approximations. Together
   they make a family that prices continuing to compute directly, which the
   catalogue's current families do not. [quick-win]
7. **Regress of meta-control ends in prior design or adaptation.** Section 3
   says meta-control regresses: "no computation can be executed until a
   computation has been executed to decide on it". The regress ends in
   hardwired or default decisions, or in policies built by earlier deliberation
   or adaptation. This is a reusable framing for why every KB controller rests
   on some unexamined default. [just-a-reference]
8. **Performance profiles for composing anytime subsystems.** Section 7
   describes allocating a total budget across composed subsystems from their
   performance profiles. The example is `treat = repair(diagnose x)`. This is
   adjacent to budgeting across multi-stage KB pipelines, but the paper only
   sketches it. [just-a-reference]

## Limitations (our opinion)

The theory is normative and, in the authors' words, has "only a heuristic
basis". Estimated probabilities violate the probability axioms, and the paper
leaves open how to reaxiomatize them. The value of partial computations, which
is the general case, is unsolved here (Section 5.4). The adaptive and
self-modelling remedies are preliminary, and the second one is unimplemented.
The empirical evidence is thin in this text. Details are deferred to other
papers. The DTA\* results figure was not captured as text. The "up to thirteen
times more effective" claim does not say which ratio is meant. The Othello
tournaments use a single evaluation function and fixed alpha-beta depths. The
authors expect the advantage not to hold against deeper alpha-beta. There are no
baselines beyond A\*, RTA\* and fixed-depth alpha-beta. The tested settings are
game trees and single-agent search with an admissible heuristic.

The transfer to Commonplace is structural, not quantitative. Connect-report
routing and review bundle ordering lack a numerical utility over outcomes, a
fixed action set with a standing default action, and prior distributions on how
a step revises estimates. The framework needs all three to compute expected net
value. Without them, Δ and TC become judgments that someone must supply, and
the results depend on that choice. Exchange-rate sweeps reduce this
dependence. The separable time-cost assumption may also fail where delay
changes which action is best, which the paper concedes for some domains.

## Recommended Next Action

In the open-ended-work-economics test 1, score each recorded controller step
as R&W's Δ (credit only when it changes a later routing or ordering decision,
both choices judged with the later information) minus priced cost. Sweep the
cost exchange rate as the DTA\* comparison does, and report whether the
preferred controller flips within the swept range.

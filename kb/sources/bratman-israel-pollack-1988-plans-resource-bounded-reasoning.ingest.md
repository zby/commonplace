---
description: "IRMA architecture paper: adopted plans cut deliberation for a resource-bounded agent via means-end focus and a compatibility filter; a tunable override trades wasted against missed reconsideration"
source: https://www.sci.brooklyn.cuny.edu/~sklar/teaching/f08/mas/papers/bratman-israel-pollack-1988-clearer.pdf
captured: "2026-11-21"
capture: pdftotext
capture_scope: full-source
doi: "10.1111/j.1467-8640.1988.tb00284.x"
genre: scientific-paper
snapshot_sha256: 78ca59e978fd821229321e243c33cf59ac8bf1c91c2e0e6f177270a087fe95ee
ingested: "2026-11-21"
occasion: "Background for a workshop on deliberative learning (kb/work/learning-method-name). Questions: what the deliberation process weighs and by what criterion; why commitment limits reconsideration; whether anything is said about retaining or revising plans from outcomes."
learning_claims: true
type: types/ingest-report.md
domains: [bdi-architecture, intention-reconsideration, resource-bounded-reasoning, plan-commitment]
tags: [goal-prioritization]
---

# Ingest: Plans and Resource-Bounded Practical Reasoning (Bratman, Israel and Pollack, 1988)

## Classification

A short theoretical paper in AI and philosophy of action, published in
*Computational Intelligence* 4(4). It gives a high-level architecture
specification (the system later called IRMA) and a conceptual taxonomy, with
illustrative scenarios but no implementation, experiment or formal model. The
captured copy is a preprint PDF converted by `pdftotext`; ligatures are lost
("lter" for "filter") and the two tables are flattened, but the full text is
present.
Author: Michael Bratman (Stanford philosopher whose 1987 *Intention, Plans and
Practical Reason* is the source of the planning theory of intention) with
David Israel and Martha Pollack (SRI AI Center). This is the founding
architectural statement of belief-desire-intention (BDI) agents.

## Summary

The paper argues that a rational agent must combine means-end reasoning with
the weighing of competing options, and must do so under resource bounds,
because the world changes while the agent deliberates. Its answer is that
adopted plans do more than produce action: they constrain further practical
reasoning. Plans pose focused means-end problems, and a compatibility filter
removes options inconsistent with existing plans and beliefs before the
deliberation process weighs the surviving options. Plans must therefore be
stable (resistant to reconsideration) and partial (ends fixed, means left
open until means-end incoherence threatens). Because agents are also
knowledge-bounded, plans must remain revocable; a filter-override mechanism
readmits incompatible options that match encoded sensitivity conditions and
reopens the conflicting intention. The paper then classifies cases by whether
reconsideration happened, whether it changed the plan, and whether it was
worth its deliberation cost. Reconsidering ("caution") and not reconsidering
("boldness") each sometimes pay. No override policy can avoid all wasted and
all missed worthwhile deliberation, so the designer tunes it to be neither
overly cautious nor overly bold. The weighing criterion inside deliberation
is left unspecified.

## Contribution assessment (our opinion)

The problem is central: how a bounded agent avoids both re-deciding
everything and never re-deciding anything. The paper's main contribution is a
conceptual reframing, likely the influential one given its role in later BDI
work: commitment is an instrument for saving computation, not only a
disposition to act, and reconsideration is a cost-bearing activity whose
policy can be judged only across cases. The five-situation taxonomy and the
caution/boldness trade-off are the sharpest parts; the argument that a
perfect override policy is impossible (footnote 9: an agent that deliberated
exactly when change would pay could skip the deliberation) is short but
genuinely clarifying. Demonstrated value is limited to conceptual clarity: no
mechanism for the override, the compatibility check or the weighing is
specified, and no test is reported, so the architecture's practical claims
remain conjectures that later BDI systems and intention-reconsideration
studies, not this paper, had to test. The originality judgment rests on
background knowledge of the BDI literature, not on comparisons in the paper.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the deliberative-learning workshop the source's role is a classical
anchor for the claim that a retained commitment limits reconsideration
because reconsideration costs deliberation, together with a counterpoint
showing where such an architecture stops short of learning. In the KB it
lands mainly on decision-under-cost notes. It compares with
[On-balance judgments can guide improvement without a global measure](../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md)
on when further deliberation is worth its cost: the paper's Situation 2
(deliberation that leaves the plan unchanged does not pay) parallels the
note's rule that investigation is warranted only when a plausible answer
could reverse the choice, and the paper judges its override policy "on
balance" across cases while counting deliberation cost inside the comparison
(Situations 4a and 4b). It compares with
[Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../theory/productive-deferral-requires-option-evidence-and-convergence.md)
on controlled postponement: structurally partial plans fix ends and defer
means, and means-end reasoning must occur before the plan becomes means-end
incoherent, which works as a convergence rule. It is an established
precedent for the mechanism conjectured in
[Reasoning limits may select for design commitments](../theory/reasoning-limits-may-select-for-design-commitments.md),
though it says nothing about the note's human-versus-model comparison. The
compatibility filter and means-end role realize two of the control routes in
[Intent controls a local choice only when it distinguishes its live alternatives](../theory/intent-controls-choices-by-distinguishing-live-alternatives.md);
the filter override adds a route that note lacks, readmission of an excluded
option. Among sources, it is the primary statement behind the second-hand
accounts in [SEP: Practical Reason](./sep-practical-reason.ingest.md) and
[Wooldridge and Jennings, Intelligent Agents](./wooldridge-jennings-intelligent-agents.ingest.md),
and it confirms the latter's observation that IRMA's deliberation has no
stated criterion. It answers the same resource-boundedness problem as
[Principles of Metareasoning](./russell-wefald-principles-of-metareasoning.ingest.md)
differently: a cheap, designer-tuned filter accepted as "leaky" or "clogged"
instead of a computed value of computation. It is the contemporaneous
opposite of [Plans and Situated Actions](./plans-and-situated-actions-suchman-1985.ingest.md),
where plans are resources for situated action rather than commitments that
constrain reasoning.

## Learning Claims (our opinion)

**Mechanism on its own terms.** The paper's adaptive mechanism is plan
revision within a run. New beliefs, from means-end reasoning or from the
opportunity analyzer's perception of environmental change, yield options;
the compatibility filter passes or blocks them; the override readmits some
blocked options; deliberation may then replace an intention. Plans can also
be abandoned when the agent comes to believe they are no longer executable,
which reopens means-end reasoning or leaves the underlying desire to prompt
later deliberation. All of this is driven by belief change, not by evaluation
of how past plans turned out. The plan library (plans-as-recipes) is fixed
for the paper's purposes. The only outcome-driven adjustment is footnote 10:
the agent herself might raise override thresholds when she notices fruitless
deliberation and lower them when she notices missed opportunities.

**Terminology.** "Deliberation" here is the process that weighs competing
surviving options and produces intentions; it is not the KB's deliberative
learning, and nothing deliberated in it is a stated theory open to
criticism. "Plan" is reserved for adopted plans; recipes are "plans-as-recipes"
in the plan library, which the paper calls a subset of beliefs.

**Against the theory-builder conditions.** Localized content: plans and
intentions are explicitly represented and decomposable into sub-intentions,
so adopted plans are addressable units; whether they count as stated
theories is doubtful, since they record what the agent will do rather than
claims about the world (strong as representation, weak as theory). The
plan library is the nearer analogue of a theory, but the paper never revises
it. Consumption: met for plans, which directly drive means-end reasoning and
filtering (strong, it is the paper's thesis). Criticism: partial at most.
Override-triggered deliberation compares an existing intention with a rival
option, which resembles comparison with rivals, but the weighing criterion
is unspecified and the trigger is a designer-encoded sensitivity condition,
not criticism aimed at what a plan says. The caution/boldness evaluation is
content-directed criticism of the override policy, but it is performed by
the designer or an observer, outside the agent. Iteration: within a run, a
revised intention becomes the context for later filtering, so results of
reconsideration persist across rounds of one episode; footnote 10 sketches
iteration on the override policy across episodes but gives no mechanism.
Persistence is therefore within a run for plans, and only proposed beyond it
for thresholds.

**Learning.** The paper makes no claim that the agent improves its capacity
for future action, and provides no evidence. Footnote 10 is the one learning
proposal: a scalar threshold adjusted from two outcome signals (fruitless
deliberation, missed opportunities). That adjustment happens inside a fixed
decomposition: the set of override conditions, the filter's compatibility
measure and the option generators are designer-given, so threshold tuning
cannot repair a missing sensitivity condition, in the sense of
[Learning inside a fixed decomposition inherits its mistakes](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).

**What it adds or questions.** It supports the KB's position that a retained
commitment is valuable partly because it is not reopened on every new
consideration, and it supplies the clearest statement of why: reopening has
a deliberation cost, and the best reconsideration policy still errs both
ways. It also shows that this account of commitment can be complete without
any learning from outcomes, which marks a boundary for deliberative learning:
stable, revocable commitment is necessary infrastructure for it but is not
itself learning, and the step from outcomes to revised plans or recipes is
exactly what the paper leaves out.

## Extractable Value

1. **Answer to the workshop's three questions.** Deliberation weighs
   competing options that survived the filter or were readmitted by override;
   its criterion is left open (decision-theoretic expected utility is invoked
   only as the idealized background, and "the weighing of conflicting
   options" is set aside as a design problem common to all architectures).
   Commitment limits reconsideration because constant reconsideration would
   cancel the deliberation savings that justify having plans. On outcomes,
   the paper offers only footnote 10's threshold tuning; plan revision is
   driven by belief change, and recipes are never revised. This makes the
   paper a precise negative boundary for a deliberative-learning definition. [quick-win]
2. **Caution/boldness as a two-sided error policy for reconsideration
   triggers.** Any trigger tuned to avoid wasted reconsideration raises
   missed worthwhile reconsideration, and the reverse. This bears directly on
   Commonplace review and re-ingest triggers and could qualify the on-balance
   note's investigation rule; high reach, since it follows from the structure
   of the decision and not from the robot domain. [experiment]
3. **Deliberation cost belongs inside the comparison.** Situation 4b (a
   known-inferior action is still the right choice because deliberating and
   switching together would cost more) separates suboptimal action from a
   design fault. Useful vocabulary for judging whether a missed improvement
   in a KB process is a defect. [quick-win]
4. **Readmission as a control route for prior commitments.** The filter
   override names a route by which an excluded option returns for
   reconsideration, missing from the intent-controls note's routes. [quick-win]
5. **Structural partiality as principled deferral.** Fix ends, defer means
   until incoherence threatens, justified by bounded knowledge. A classical
   agent-architecture instance for the productive-deferral note. [just-a-reference]
6. **Leaky versus clogged filters.** Cheap, defeasible admissibility checks
   accepted as imperfect in both directions, as an alternative to computing
   the value of each deliberation. [just-a-reference]

## Limitations (our opinion)

Nothing in the paper is tested. The architecture is a block diagram plus
prose; the override mechanism, compatibility check and weighing are named
design problems, not specified procedures, so the claim that filtering saves
enough computation to matter is asserted rather than shown. The Rosie
scenarios are constructed to instantiate each cell of the taxonomy and
cannot show how often each situation arises or whether any realistic
override policy lands mostly in the good cells. The impossibility argument
shows that no policy is perfect, but it gives no way to compare two
imperfect policies beyond "on balance", so the trade-off is a framing for
design judgment rather than a criterion. Classifying cases as "worth it"
requires the designer or observer to know what properly functioning
deliberation would have concluded, which is exactly what the agent lacks;
the evaluative standpoint sits outside the agent. Situations are judged one
episode at a time, so the account does not address how a policy's error rate
would be estimated from experience, which is what footnote 10's self-tuning
would need. Finally, the paper assumes a single agent's practical reasoning
with a given plan library; transfer to a KB, where the retained commitments
are stated claims open to criticism, is our analogy and has to be argued
separately.

## Recommended Next Action

In the `kb/work/learning-method-name` workshop, record this paper as the
boundary case for the deliberative-learning definition: an architecture with
stable, revocable, consumed commitments and in-run plan revision but no
revision of plans or recipes from outcomes (footnote 10 excepted), and use
it to test whether the definition's wording excludes it for the right
reason.

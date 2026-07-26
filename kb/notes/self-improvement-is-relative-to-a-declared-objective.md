---
description: "The improvement objective is a declared parameter alongside boundary and horizon, carrying two separable conditions — indexed by the analyst, antecedent in the pathway — whose failures differ in kind"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Self-improvement is relative to a declared objective

A [self-improving system](./definitions/self-improving-system.md) is defined by change that is causally responsive to [evidence bearing on an improvement objective](./definitions/evidence-bearing-on-an-improvement-objective.md). The objective is therefore already load-bearing in the membership test. What has not been stated is its standing in the *analysis*: it is a declared parameter, on the same footing as the declared boundary and the declared assessment horizon. An attribution of self-improvement is elliptical until all three are named, and comparative attributions are elliptical in a way that no additional precision about the mechanism repairs.

The pattern is established. The same substrate is being improved under one boundary and self-improving under another, [which the boundary cases work through case by case](./the-self-improving-system-definition-classifies-its-boundary-cases.md); the same pathway is currently self-improving over one horizon and only dispositionally self-improving over another. The objective is the third parameter of that kind. Its distinctive feature is that it carries two conditions rather than one, and they are separable.

## Indexed and antecedent

**Indexed** is a condition on the attribution. A claim about self-improvement names the objective it is relative to. Failing it makes the claim incomplete, not wrong — the same failure as reporting an autonomy grade without declaring the boundary it was assessed against.

**Antecedent** is a condition on the pathway. The objective must be identifiable independently of the particular change it is invoked to license, and evidence bearing on it must have causally shaped that change. Failing it makes the claim false, or empty.

Keeping them apart matters because they are violated by different mistakes and repaired by different means.

*Undeclared but antecedent.* A parametric learner descends a loss the analysis never names. The pathway is genuinely improvement-directed; only the report is deficient. Naming the objective fixes it.

*Declared but not antecedent.* An analyst names an objective the pathway is not responsive to — attributing "improvement toward maintainability" to a system whose only operative evidence is latency. Clarification cannot fix this; the attribution is simply false. Under the definition's exclusion for evidence of the wrong thing, the pathway is directed at whatever its evidence is actually diagnostic of.

*Neither.* The objective is fitted to the change after the fact. This is the failure that makes the category vacuous, and it needs its own treatment.

*Antecedent under more than one objective.* A single pathway can be responsive to evidence bearing on several objectives at once — a gate that checks structural validity and prose quality supplies both. Indexing is then not bookkeeping: different declared objectives yield different, simultaneously true attributions about the same substrate, exactly as different declared boundaries do. This is why indexing cannot be discharged by simply reading the objective off the pathway.

Neither condition requires the objective to be represented inside the system. Ashby's Homeostat has essential-variable bounds built into its wiring, [as the ultrastability account describes](../sources/ashby-design-for-a-brain-ultrastability.md); nothing in it declares or stores them, and they are still specifiable without reference to any particular reorganization. Antecedence is a condition on identifiability, not on retention.

## The causal clause does not close the post-hoc gap

Requiring that evidence causally shape the change already blocks the crude version of a fitted objective: a criterion invented after the change cannot have shaped it, because the causal history is fixed.

What it does not block is redescription. Take gradient steps on a loss and relabel the target as "whatever these weights now do better." The causal story is untouched — the same evidence shaped the same change — and the relabelled criterion is trivially satisfied by the change that occurred. Any operative self-change admits such a relabelling, so if this counted, evidence-responsiveness would separate nothing.

The blocker is antecedence read as *independent specifiability*: an objective whose only available specification refers to the change it licenses is not antecedent, however intact the causal path. This is the condition the causal clause was tacitly relying on, and it needs stating separately because the two come apart in exactly this case.

## What follows

**Comparison requires a shared index, and sometimes cannot be had even with one.** "This system is more self-improving than that one" is unanswerable until both readings are indexed to the same objective. Indexing is necessary but not sufficient: comparison needs an ordering over states, and objectives differ in how much ordering they induce. A loss or an expected-running-time objective induces a rich one. A viability bound induces only acceptable versus unacceptable, leaving two acceptable configurations incomparable — enough evaluative direction to make change improvement-directed, not enough to rank outcomes. So a fully indexed comparison can still have no answer, for reasons internal to the declared objective. This obstacle is independent of the commensurability obstacle: [comparing per-function autonomy profiles fails for want of a shared decomposition](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) even where the objective is fixed and richly ordered. Both must be cleared.

**The analysis is generic over objectives, not independent of them.** The questions the analysis asks — what the update architecture is, what reflection covers, whether the pathway is cumulative, what the methodology settles, who performs which function, what warrant exists — keep their form as the objective varies. Several of their answers do not. Warrant is already stated to be objective-, risk-, and threshold-relative, [since it is bounded by what an oracle can establish](./warranted-autonomy-is-bounded-by-oracle-domain.md); cumulativity is dependence across episodes in *improvement-relevant* information, which is objective-relative by construction. The cluster has been doing this consistently; declaring the objective a parameter names the invariant rather than changing the practice.

**The profile does not select an order.** [Refusing a single maturity grade over unlike properties](./a-self-improving-system-needs-a-profile-not-a-ladder.md) is a claim about the descriptive space: coverage, dynamics, governance, and allocation do not collapse into one number. It is not the claim that no ordering exists, and it entails something sharper about orderings — because the dimensions move independently, and can move in opposite directions under one engineering change, the profile cannot determine how to trade them off. A declared objective does that, and the ontology should not. This is also how the dimensions become goals without becoming grades: greater computational autonomy, wider reflective coverage, and stronger warrant are available as objectives, singly or in combination, and moving a gate from a person to a model advances the first while leaving the third where it was.

## Open Questions

- **Objective revision.** When a pathway changes the objective it is directed at, calling that change an improvement requires naming the level at which it is evaluated: the prior objective licensing the transition, a retained higher criterion ranking objectives, an external judgment, or mutual adjustment where the successor better systematizes the evidence the predecessor organized. Deciding what terminates that chain, and whether the last option is a real alternative to a meta-criterion or a disguised instance of one, needs its own treatment.
- **Checking antecedence.** Independent specifiability is not mechanically testable. Whether it can be operationalized beyond a case-by-case argument — some test on the specification's dependence on the change — is open.

---

Relevant Notes:

- [Self-improving system](./definitions/self-improving-system.md) — defined-in: the membership test this note adds a third declared parameter to
- [Evidence bearing on an improvement objective](./definitions/evidence-bearing-on-an-improvement-objective.md) — defined-in: the objective-indexing and causal-shaping clauses antecedence sharpens
- [The definition classifies its boundary cases without ad hoc exceptions](./the-self-improving-system-definition-classifies-its-boundary-cases.md) — grounds: the precedent that a declared parameter changes the attribution rather than the substrate
- [A self-improving system needs a profile, not a ladder](./a-self-improving-system-needs-a-profile-not-a-ladder.md) — grounds: the refusal of a single maturity grade over unlike properties, which this note distinguishes from the absence of an ordering
- [Methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md) — grounds: two dimensions moving in opposite directions under one change, the case that defeats aggregation
- [Real self-improving systems occupy combinations no single rung captures](./real-self-improving-systems-occupy-combinations-no-rung-captures.md) — grounds: the combinations that actually occur, which is why no ordering follows from the profile
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: an existing objective-relative reading inside the cluster
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — contrasts: comparison blocked by incommensurable decomposition, the obstacle that survives after indexing
- [Ashby's Homeostat](../sources/ashby-design-for-a-brain-ultrastability.md) — evidence: an antecedent objective that the system neither declares nor stores

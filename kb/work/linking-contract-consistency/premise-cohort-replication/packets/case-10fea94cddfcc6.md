# Case packet

Neutral case identifier: case-10fea94cddfcc6

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Self-improvement is relative to a declared objective

A [self-improving system] is defined by change that is causally responsive to [evidence bearing on an improvement objective]. The objective is therefore already load-bearing in the membership test. What has not been stated is its standing in the *analysis*: it is a declared parameter, on the same footing as the declared boundary and the declared assessment horizon. An attribution of self-improvement is elliptical until all three are named, and comparative attributions are elliptical in a way that no additional precision about the mechanism repairs.

The pattern is established. The same substrate is being improved under one boundary and self-improving under another, [which the boundary cases work through case by case]; the same pathway is currently self-improving over one horizon and only dispositionally self-improving over another. The objective is the third parameter of that kind. Its distinctive feature is that it carries two conditions rather than one, and they are separable.

## Indexed and antecedent

**Indexed** is a condition on the attribution. A claim about self-improvement names the objective it is relative to. Failing it makes the claim incomplete, not wrong — the same failure as reporting an autonomy grade without declaring the boundary it was assessed against.

**Antecedent** is a condition on the pathway. The objective must be identifiable independently of the particular change it is invoked to license, and evidence bearing on it must have causally shaped that change. Failing it makes the claim false, or empty.

Keeping them apart matters because they are violated by different mistakes and repaired by different means.

*Undeclared but antecedent.* A parametric learner descends a loss the analysis never names. The pathway is genuinely improvement-directed; only the report is deficient. Naming the objective fixes it.

*Declared but not antecedent.* An analyst names an objective the pathway is not responsive to — attributing "improvement toward maintainability" to a system whose only operative evidence is latency. Clarification cannot fix this; the attribution is simply false. Under the definition's exclusion for evidence of the wrong thing, the pathway is directed at whatever its evidence is actually diagnostic of.

*Neither.* The objective is fitted to the change after the fact. This is the failure that makes the category vacuous, and it needs its own treatment.

*Antecedent under more than one objective.* A single pathway can be responsive to evidence bearing on several objectives at once — a gate that checks structural validity and prose quality supplies both. Indexing is then not bookkeeping: different declared objectives yield different, simultaneously true attributions about the same substrate, exactly as different declared boundaries do. This is why indexing cannot be discharged by simply reading the objective off the pathway.

Neither condition requires the objective to be represented inside the system. Ashby's Homeostat has essential-variable bounds built into its wiring, [as the ultrastability account describes]; nothing in it declares or stores them, and they are still specifiable without reference to any particular reorganization. Antecedence is a condition on identifiability, not on retention.

## The causal clause does not close the post-hoc gap

Requiring that evidence causally shape the change already blocks the crude version of a fitted objective: a criterion invented after the change cannot have shaped it, because the causal history is fixed.

What it does not block is redescription. Take gradient steps on a loss and relabel the target as "whatever these weights now do better." The causal story is untouched — the same evidence shaped the same change — and the relabelled criterion is trivially satisfied by the change that occurred. Any operative self-change admits such a relabelling, so if this counted, evidence-responsiveness would separate nothing.

The blocker is antecedence read as *independent specifiability*: an objective whose only available specification refers to the change it licenses is not antecedent, however intact the causal path. This is the condition the causal clause was tacitly relying on, and it needs stating separately because the two come apart in exactly this case.

## What follows

**Comparison requires a shared index, and sometimes cannot be had even with one.** "This system is more self-improving than that one" is unanswerable until both readings are indexed to the same objective. Indexing is necessary but not sufficient: comparison needs an ordering over states, and objectives differ in how much ordering they induce. A loss or an expected-running-time objective induces a rich one. A viability bound induces only acceptable versus unacceptable, leaving two acceptable configurations incomparable — enough evaluative direction to make change improvement-directed, not enough to rank outcomes. So a fully indexed comparison can still have no answer, for reasons internal to the declared objective. This obstacle is independent of the commensurability obstacle: [comparing per-function autonomy profiles fails for want of a shared decomposition] even where the objective is fixed and richly ordered. Both must be cleared.

**The analysis is generic over objectives, not independent of them.** The questions the analysis asks — what the update architecture is, what reflection covers, whether the pathway is cumulative, what the methodology settles, who performs which function, what warrant exists — keep their form as the objective varies. Several of their answers do not. Warrant is already stated to be objective-, risk-, and threshold-relative, [since it is bounded by what an oracle can establish]; cumulativity is dependence across episodes in *improvement-relevant* information, which is objective-relative by construction. The cluster has been doing this consistently; declaring the objective a parameter names the invariant rather than changing the practice.

**The profile does not select an order.** That coverage, dynamics, governance, and allocation do not collapse into one number is a claim about the descriptive space, and [the placements bear it out]. It is not the claim that no ordering exists, and it entails something sharper about orderings — because the dimensions move independently, and can move in opposite directions under one engineering change, the profile cannot determine how to trade them off. A declared objective is what can, and the ontology should not. Two qualifications keep that from promising more than it delivers. An objective inducing only a partial order settles no trade-off it does not reach, as above. And an objective stated over outcomes does not rank architectures at all without a claim connecting structure to outcome, [since a property pursued as a goal is checked for achievement rather than for warrant]. This is also how the dimensions become goals without becoming grades: greater computational autonomy, wider reflective coverage, and stronger warrant are available as objectives, singly or in combination — as proximate ones, each carrying a linking claim — and moving a gate from a person to a model advances the first while leaving the third where it was.

## Open Questions

- **Checking antecedence.** Independent specifiability is not mechanically testable. Whether it can be operationalized beyond a case-by-case argument — some test on the specification's dependence on the change — is open.

---

Relevant Notes:

## Artifact B

# Real self-improving systems occupy combinations no single rung captures

The argument that improvement-pathway properties do not entail one another is made where each property is defined. This note supplies the other half: the combinations are not merely permitted by the ontology, they are the ones actually occupied by the systems it has to place. No canonical ordering follows from the profile alone — a scale over these eight would have to rank a proof-governed rewriter against a randomized relay bank against a repository of human-reviewed natural-language, and any total order it produced would have to import priorities the descriptive fields do not contain. A declared objective can supply those priorities; the profile cannot. Even then the supply is indirect, [since an objective stated over outcomes ranks no architecture without a claim connecting structure to outcome].

Every row is a reading under a declared boundary. Change the boundary and the reading changes — most visibly for Commonplace, which is a member at all only under a frame that includes its maintainers, [since attributions are elliptical until their parameters are named].

## The placements

Selected profile fields, not the whole profile: the governance dimension appears here only through its evidential half, and what each methodology settles is left to the per-system accounts. The last column reads differently by update architecture. For the proposal-selection rows it is oracle domain — what the gate can warrant accepting. For the direct rows there is no gate to hand over, so it names what bounds the update rule's trustworthiness instead, [since warranted autonomy is scoped to pathways with an evaluation to hand over].

| System | Update architecture | Reflective | Cumulative | Allocation | Evidential limit |
|---|---|---|---|---|---|
| [Ashby's Homeostat] | direct, viability-driven | no | no | computational | nothing — retention is negative |
| Parametric self-improvers | direct, gradient | no | yes | computational | training-time evaluation |
| [Self-Improving Algorithms] | direct, staged | no | yes | computational | the declared input distribution |
| [DreamCoder] | proposal-selection | partly | yes | computational | statistical program fit |
| [Gödel machine] | proposal-selection | yes | yes | computational | what its proof system establishes |
| [Knowledge-Centric Self-Improvement] | proposal-selection | partly | yes | computational | benchmark oracles; debate for transfer |
| [Exo] | proposal-selection | yes | yes | computational | build, test, immediate behaviour |
| [Commonplace] | proposal-selection | yes | yes | joint, by decision | tests and validators; human judgment |

## What the hard cases teach

**The Homeostat is the floor, and it is not a low rung.** Operative, computationally autonomous, and non-cumulative at once: its retained setting steers behavior and determines whether reorganization fires, yet the successor comes from a random table and carries nothing of the incumbent. Any scale that reads autonomy as maturity puts a randomized relay bank above a human-reviewed repository.

**Parametric learners break the equation of reflection with compounding.** They compound reliably through weights nothing inside them can read. This is the deployed default rather than a corner case, which is why an ontology that required reflection for membership would fail on the field's central systems.

**Ailon et al. show cumulativity without either reflection or a gate.** Its staged training phase is where the accumulation sits: a retained snapshot of a typical instance is built first, and the auxiliary search structures are then constructed against it. The stationary regime that follows retains those structures as the operative basis for later inputs without further improving them. Its objective is expected running time under a declared input distribution, and distribution shift is the boundary where the retained structure stops being warranted.

**DreamCoder and the Gödel machine differ in gate kind, not gate strength.** Both run reject-capable loops; one accepts on statistical program fit, the other only on proof. DreamCoder is also split internally — an inspectable symbolic library alongside an opaque recognition network — so its reflective coverage has to be reported per component rather than as a verdict about the system.

**Knowledge-Centric Self-Improvement is the strongest external case for addressability.** Its appendix traces a claim cited by id, challenged, split into two scoped claims, with the falsified branch retained as a rejection — the read-criticize-revise operations exercised computationally, not just structurally available. Its warrant splits: benchmark oracles are strong for pass/fail, while transfer-worthiness rests only on model debate.

**Exo and Commonplace differ most visibly in allocation.** Both are reflective, cumulative proposal-selection pathways; Exo's self-representation is unusually literal, the source tree it edits being the organization that determines its behavior, with rebuild-and-restart as the wire from artifact to behavior. Exo is computational throughout, Commonplace joint and varying by decision. On the coarse fields reported here that is the sharpest difference between them — their warrant cells differ too, and finer readings would separate their governance, search, and protected kernels — and it is invisible to any measure that scores both as "self-improving."

## Scope

- Placements are readings, not measurements. Each depends on a declared boundary and horizon, and several rest on a single published description rather than on independent inspection.
- "Partly" in the reflective column marks per-component coverage, not a midpoint on a scale — the point is that the verdict does not apply to the system as a whole.
- The casebook establishes that the combinations occur. It does not establish that any of these systems improved, which is a separate question about outcomes against a declared objective.

---

Relevant Notes:

## Under-review context phrase

the combinations that actually occur, which is why no ordering follows from the profile

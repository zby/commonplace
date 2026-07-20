---
description: "Membership establishes improvement-directed self-change; reflective structure, dynamics, governance, and actor allocation describe its architecture without a single ladder"
type: kb/types/note.md
traits: [title-as-claim, synthesis]
tags: [foundations, self-improving-systems]
---

# A self-improving system needs a profile, not a ladder

Membership in the [self-improving system](./definitions/self-improving-system.md) category is deliberately broad. A pathway qualifies when it makes operative, evidence-responsive changes to its own behavior-determining organization. For example, put a model, its weights, and its online optimizer inside the declared frame: each observed loss supplies a gradient, the optimizer changes the model's own operative weights, and no self-representation is involved. Membership therefore establishes improvement-directed self-change, not how the improving architecture is organized.

Once membership is established, four parts describe the pathway without forcing unlike properties onto one scale.

## Reflective structure

**What does the self-representation cover, and what can processes inside the declared frame do with each covered component?** [Reflective coverage has two dimensions](./reflective-coverage-is-graded-across-representational-forms.md): breadth across behavior-determining components and representational forms, and operation depth over each component.

Addressability is not a third coordinate alongside coverage. It is the operation profile that sufficient coverage affords over retained commitments: later processes may retrieve, inspect, criticize, revise, rescope, or transfer them. Those operations must be named separately rather than collapsed into a scalar, [since reflection buys addressability](./reflection-buys-addressability.md) without guaranteeing every possible use of it.

**Example.** A Commonplace agent can read and edit a tag-README specification, giving it observation and modification over that prose component. A skill can also select a named model while the model's weights remain sealed. Both are real reflective levers, but they cover different components with different operations.

**TODO:** Test whether addressability operations really reduce to coverage breadth and the current observation/selection/configuration/modification scheme. A process can mechanically modify a file without interpreting the commitment it contains; if that case holds, addressability may need an independent subprofile rather than being only an affordance of coverage.

## Improvement dynamics

**Do later improvement episodes build on earlier operative changes?** This is **cumulativity**, a relation across episodes rather than a degree of reflection. Opaque weights can compound without being reflectively addressable; an explicit lesson can be addressable yet never retrieved, and therefore fail to compound.

Operativity is a membership condition, not another dimension of improvement dynamics.

**Example.** Under the current reading, Ashby's Homeostat is operative but non-cumulative: a viable setting controls behavior, yet the next failed configuration is replaced by a blind random draw. Online gradient descent is cumulative but opaque: the next gradient is evaluated at weights retained from prior updates. A lessons file is addressable, but a later round that never retrieves the lesson does not build on it.

**TODO:** Specify what “builds on” requires. If merely starting from the current operative state is sufficient, the Homeostat may be cumulative too; if informational dependence is required, that criterion needs stating. The never-retrieved lesson also strains membership: if it never affects subsequent behavior, it may be inoperative rather than a reflective, non-cumulative case.

## Governance

**Which consequential decisions does the retained methodology settle?** This is **methodological closure**. A method becomes more closed under its own extension as it supplies criteria for the meta-decisions its recommendations raise, rather than merely naming a decider. **Warrant** remains separate: a decision can be procedurally settled without the criterion or oracle being trustworthy in the case at hand.

**Example.** “Accept the patch when the unit tests pass” settles an acceptance decision. It can still be unwarranted for production compatibility when the suite contains no migration test. By contrast, “have the maintainer use judgment” assigns the decision without methodologically settling it.

**TODO:** Determine whether methodological closure belongs in the profile of every self-improving pathway or only of methodologies that issue recommendations and raise meta-decisions. A gradient learner and the Homeostat have determinate update procedures but no represented recommendation to extend.

## Actor allocation

**Who performs each improvement function?** Under a human-inclusive frame, report search, evaluation, adoption, retention, revision, and other consequential functions as human, computational, or joint. A function is computationally closed when it needs no human decision; whole-pathway computational closure is the endpoint at which every required function meets that condition. Computational closure and machine autonomy are therefore two readings of the same allocation, not independent axes.

**Example.** In Commonplace's tag-README change, the maintainer selected the problem and adopted the result, an agent helped frame the candidate, and a validator performed the structural completeness check. The pathway is reflectively self-improving under the human-inclusive frame, while only the validation function is computationally closed.

**TODO:** Decide whether “computationally closed” means only “requires no human decision” or literal closure of the computational subsystem. An unattended agent using a hosted model needs no human decision but still depends on a model provider outside Commonplace's declared frame.

## The properties can move independently

The profile prevents several false entailments:

- cumulative does not imply reflective: parametric learning compounds through opaque weights;
- reflective does not imply cumulative: an editable lesson that is never retrieved changes no later episode;
- methodologically closed does not imply computationally autonomous: a human can execute a settled method;
- computationally autonomous does not imply methodologically closed: a model can improvise without intervention;
- computational allocation does not imply warrant: moving an evaluator from a person to a model does not establish that its acceptances are safe.

Coverage, dynamics, governance, and allocation can therefore change separately, even when one engineering change affects several at once. They are assessed inside the same declared frame but answer different questions.

[The Commonplace case](../reference/commonplace-as-a-reflective-system.md) illustrates the result: human inclusion establishes reflective self-improving membership, while uneven coverage, cumulative retention, mixed governance, and allocation among maintainers, agents, and validators carry the useful information. Machine autonomy increases when functions move toward computational allocation; reflectivity increases only when coverage breadth or operation depth expands.

---

Relevant Notes:

- [Self-improving system](./definitions/self-improving-system.md) — defined-in: supplies the membership conditions kept separate from the profile
- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — grounds: the breadth-and-operation account of reflective structure
- [Reflection buys addressability](./reflection-buys-addressability.md) — grounds: addressability as the affordance of reflective coverage over retained commitments
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — grounds: methodological closure as a governance property
- [Admitting a human into the boundary moves reflective discrimination to computational allocation](./admitting-a-human-into-the-boundary-moves-reflective-discrimination-to-computational-allocation.md) — grounds: the actor-allocation profile and its computational-closure reading
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — contrasts: allocation and methodological settlement do not establish trustworthiness
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidence: applies the profile to one observed human-inclusive pathway

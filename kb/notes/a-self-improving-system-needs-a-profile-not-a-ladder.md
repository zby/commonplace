---
description: "Membership establishes improvement-directed self-change; update architecture and a four-part pathway profile describe it without a single ladder"
type: kb/types/note.md
traits: [title-as-claim, synthesis]
tags: [foundations, self-improving-systems]
---

# A self-improving system needs a profile, not a ladder

## Membership

The [self-improving-system definition](./definitions/self-improving-system.md) owns the category test. Passing it establishes improvement-directed self-change, not how the improving architecture is organized.

## Update architecture

Once membership is established, classify the update using the [proposal-selection note](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md): direct determination, proposal-selection with possible non-adoption, or a composition of both.

Update architecture is independent of reflective structure. Either architecture can change a writable self-representation or a non-reflective substrate, so proposal-selection must not be treated as the general form of reflective improvement.

## Pathway profile

After membership and update architecture are stated, four further parts describe the pathway without forcing unlike properties onto one scale. Together they form the pathway profile; membership and update architecture remain separate.

### Reflective structure

**What does the self-representation cover, and what can processes inside the declared frame do with each covered component?** [Reflective coverage has two dimensions](./reflective-coverage-is-graded-across-representational-forms.md): breadth across behavior-determining components and representational forms, and operation depth over each component.

Where improvement is model-mediated, reflection turns coverage into a self-modeling question: [which parts and relations must become machine-operable](./reflection-makes-own-organization-part-of-the-action-environment.md) before the process can locate a failure or map a novel task onto its capabilities and limitations without human interpretation?

Coverage and addressability are related but separate profiles within reflective structure. Coverage records represented aspects, forms, and structurally available operations. [Addressability](./reflection-buys-addressability.md) records what processes can do with a retained change as a commitment — retrieve, interpret, criticize, revise, rescope, or transfer it. Coverage of the component is necessary but not sufficient: mechanical observation or modification does not establish interpretation.

### Improvement dynamics

**Does later improvement use what earlier improvement retained?** This is **cumulativity**, an informational dependence across episodes rather than a degree of reflection. A later episode builds on an earlier one when information introduced or selected by the earlier operative change shapes the later candidate, evaluation, update, or retained successor. The later episode may read or transform the retained state, compute an update at it, or apply a delta that preserves part of it.

Merely beginning while the earlier state remains operative does not count. A practical test is to hold the later episode's new evidence and randomness fixed and substitute a different earlier retained result. If that substitution changes the later improvement because the result is consumed or preserved, the pathway is cumulative across those episodes. If the earlier result only governs behavior until an independently generated replacement overwrites it, it is operative but non-cumulative. Cumulativity is therefore assessed over named episodes or a stated horizon; a pathway may carry some earlier changes forward and discard others.

Holding the later episode's evidence fixed is a deliberate exclusion, not an oversight. An earlier retained result also shapes which evidence later arises — an operative incumbent partly determines whether a violation fires at all — but dependence routed only through the evidence stream is the trigger consuming its input, and counting it would make every operative change cumulative through its consequences. The test asks whether the retained result itself is consumed or preserved, holding the evidence it caused fixed.

**Examples.** Online gradient descent is cumulative but opaque: the retained weights are the point at which the next gradient is evaluated and the base to which it is applied. A clean reflective counterexample is a controller whose runtime reads an editable `current-policy` file, while its improvement routine responds to a viability violation by overwriting the whole file with the next policy from a fixed randomized table, without reading the incumbent or recording prior trials. Each policy is reflectively represented and operative between resets, but no result informs its successor.

[Self-Improving Algorithms](../sources/self-improving-algorithms.md) supplies a concrete non-reflective cumulative case: a training phase learns task-relative distribution structure, then a stationary regime retains the tuned data structures as the operative basis for later inputs. Its actor allocation is computational, its objective is expected running time under a declared input distribution, and distribution shift marks the boundary where recalibration is required. The example strengthens the distinction between cumulative retention and reflective addressability: learned structure compounds without becoming an inspectable self-representation.

Ashby's Homeostat is the non-reflective version of that counterexample. Its retained setting controls behavior and whether reorganization is triggered, but once triggered the next values are unrelated to the incumbent and the problem. Holding the violation and random-table position fixed, replacing the incumbent would not change its successor. The Homeostat is therefore operative and non-cumulative: the trigger uses fresh failure evidence, while the update carries no improvement-relevant information from earlier retained settings.

### Governance

**Which consequential decisions does the retained methodology settle?** Report [methodological closure](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) where a represented methodology issues recommendations and raises meta-decisions; otherwise mark it not applicable rather than treating a determinate update rule as a closed methodology. [Warrant](./warranted-autonomy-is-bounded-by-oracle-domain.md) remains separate from procedural settlement.

When the pathway is compared with self-adaptive-systems literature, uncertainty, context, system state, and the distinction between domain goals and adaptation goals are useful profile fields, not replacement membership criteria. The systematic review by [Petrovska, Erjiage, and Kugele](../sources/defining-self-adaptive-systems-systematic-literature-review.md) shows why: formal definitions in that field omit or conflate these dimensions, and MAPE-K-style structure does not settle what counts as self-improvement.

### Actor allocation

**Who performs each improvement function?** Record human, computational, or joint allocation under the declared frame. [The closure owner](./methodological-and-computational-closure-track-different-changes.md) defines computational closure as the no-human endpoint of that allocation, explains why human-inclusive reflectivity makes the profile load-bearing, and keeps literal subsystem closure as an open boundary question.

For a human-inclusive pathway, an optional allocation sub-profile can record which actor performs information acquisition, analysis, decision/action selection, and action implementation. [Parasuraman, Sheridan, and Wickens](../sources/model-types-levels-human-interaction-automation.md) provide the useful four-function form and show why allocation must be evaluated by performance consequences, reliability, and consequence costs. This is a form inheritance, not a within-function autonomy ladder: the improvement functions here are search, evaluation, and retention rather than task-performance stages, and actor allocation does not establish warrant.

### The properties can move independently

Keeping update architecture and the four-part profile separate prevents several false entailments:

- cumulative does not imply reflective: parametric learning compounds through opaque weights;
- reflective does not imply cumulative: an improvement routine can independently overwrite an operative represented policy;
- direct determination does not imply non-reflective: evidence can directly revise an explicit policy or lesson;
- proposal-selection does not imply reflective: candidates over opaque parameters can be generated and selected;
- methodologically closed does not imply computationally autonomous: a human can execute a settled method;
- computationally autonomous does not imply methodologically closed: a model can improvise without intervention;
- computational allocation does not imply warrant: moving an evaluator from a person to a model does not establish that its acceptances are safe.

Coverage, dynamics, governance, and allocation can therefore change separately, even when one engineering change affects several at once. They are assessed inside the same declared frame but answer different questions. Update architecture is reported alongside this profile rather than absorbed into it.

[The Commonplace case](../reference/commonplace-as-a-reflective-system.md) illustrates the result: under a human-inclusive frame, the observed pathway passes the self-improving membership test and the separate reflective-system test; proposal-selection describes its update architecture; and uneven coverage, cumulative retention, mixed governance, and allocation among maintainers, agents, and validators carry the rest of the useful information. Moving a function toward computational allocation changes autonomy, not reflective structure, unless coverage or addressability changes too.

---

Relevant Notes:

- [Self-improving system](./definitions/self-improving-system.md) — defined-in: supplies the membership conditions kept separate from the profile
- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — grounds: the breadth-and-operation account of reflective structure
- [Reflection buys addressability](./reflection-buys-addressability.md) — grounds: the commitment-operation profile kept distinct from structural coverage
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — grounds: methodological closure as a governance property
- [Methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md) — grounds: the governance and actor-allocation readings, including the human-boundary consequence
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — contrasts: allocation and methodological settlement do not establish trustworthiness
- [Reflection puts a system's own organization inside its action environment](./reflection-makes-own-organization-part-of-the-action-environment.md) — extends: applies model-mediated action to the coverage autonomous reflective work requires
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidence: applies the profile to one observed human-inclusive pathway

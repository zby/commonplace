---
description: "Separates computational closure from domain breadth, distinguishes factory construction from specialization acquisition, and rejects unqualified universal-software-factory terminology"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources, synthesis]
tags: [foundations, computational-model, self-improving-systems]
---

# Domain extensibility, not closure, determines factory reach

Computational closure and production reach are independent properties. **Closure** asks whether an in-scope factory-learning pathway still needs a human decision. **Reach** asks which software demands the pathway can turn into adequate family specialization and lifecycle products under a declared evidence, acceptance, and resource frame. Closing a narrow pathway does not widen it.

The four combinations are coherent:

| | Narrow or fixed-family reach | Broad or domain-extensible reach |
|---|---|---|
| Human-open factory development | Conventional factory developers maintain one family's machinery. | People construct new family specialization as demands move across domains. |
| Computationally closed factory development | A computational loop revises machinery for one declared family while staying inside its supplied decomposition. | Computation acquires and installs the family specialization needed by novel covered demands. |

The lower-right case is the target named by [domain-extensible software factory](./definitions/domain-extensible-software-factory.md). The path from the upper-left to the lower-right has two separate movements: reallocate factory-development decisions from people to computation, and widen the class of demands for which the computational path can acquire adequate specialization. Evidence for either movement does not establish the other.

## Factory construction is not the same reach claim

Call a constructor (C) **constructionally universal** relative to a factory class \(\mathcal F\), description language \(L\), and adequacy relation \(\simeq\) when:

\[
\forall f \in \mathcal F,\ \exists d \in L: C(d) \simeq f.
\]

This is our definition, not inherited software-factory vocabulary. It asks whether a supplied description can be realized as an operative factory. Here \(\simeq\) includes installation, an authority path into later production, and the declared resource bound; without those conditions the formula establishes only factory-artifact expressivity. If \(L\) may encode the complete target and \(\mathcal F\) is every computable factory, the property collapses toward compiler, interpreter, or Turing universality. It becomes informative only after the factory class, representation, adequacy relation, resource bound, and permitted burden on \(d\) are fixed.

Constructional universality does not imply domain reach because the correct descriptor may remain unavailable. Conversely, a domain-extensible process needs to find some adequate specialization for each covered demand; it need not reproduce every possible implementation of a factory.

This distinction also bounds the prior art. The [Greenfield reconstruction](./a-software-factory-is-family-scoped-lifecycle-production-machinery.md) shows human-directed factories producing factories and MDSoFa computationally producing factory assets from supplied metamodels and expertise. Those are real factory-construction precedents. The further research question is whether permitted production evidence can computationally determine and install the family-defining specialization that those arrangements receive from people. Reject-capable evaluation is additionally required when the update architecture exposes competing candidates.

## Task or domain universality must be indexed

For a fixed, non-vacuous frame \((\mathcal D,E,A,B,H,R,Q)\) from the domain-extensibility note, call a factory **domain-universal over that frame** only when every admissible demand in \(\mathcal D\) can be handled under \(E,B,H,R\) with an outcome satisfying \(A\). The prospective rule \(Q\) determines how attempts and failures are sampled and accounted for; it cannot shrink the semantic quantifier by removing difficult members of \(\mathcal D\). Demonstrated full coverage is evidence for this property, not the property's definition. This is a limiting case of domain extensibility, not an absolute property.

The unqualified name *universal software factory* should not be registered as a definition. It is ambiguous along at least four axes: target-platform portability, recursive factory output, constructional expressivity, and task/domain production reach. The collision is historical, not hypothetical. Di Giovanni and Padella's 1983 report says verbatim that its environment “can be considered a universal factory” because it may be used for different microprocessor families ([their software-factory account](../sources/di-giovanni-padella-universal-software-factory-1983.ingest.md)). That is portability across targets, not acquisition of new product-family knowledge.

If later prose needs a limiting concept, it should say **domain-universal software factory relative to a declared demand class and evidence protocol**. Even that phrase adds little beyond saying that a domain-extensibility claim has full coverage over its declared tuple.

## Undisclosed intentions bound reach

No reach definition should require omniscient recovery of arbitrary user intentions. Consider two admissible demand worlds that are observationally equivalent under every query and action permitted by the evidence protocol through the declared horizon, but whose acceptable outcome sets are disjoint. A deterministic factory must make the same terminal commitment in both worlds and therefore fail in at least one. A randomized factory cannot guarantee both either, because one output distribution cannot have all its support inside two disjoint acceptance sets.

This is our indistinguishability argument, not a theorem attributed to program-synthesis literature. The literature supplies the motivating premise: examples and informal specifications can admit many programs, and interaction can reveal distinctions that were absent from the initial evidence ([Gulwani, Polozov, and Singh](../sources/program-synthesis-gulwani-polozov-singh-2017.ingest.md)). The argument rules out guaranteed recovery of distinctions unavailable under the permitted evidence protocol. It does not rule out broad production reach.

A coherent claim can instead:

- restrict the demand class to demands distinguishable under the evidence protocol;
- permit interaction that elicits the missing distinction;
- weaken the service claim to permit abstention, or extend the horizon to permit
  later correction; or
- state a probabilistic success condition rather than a universal guarantee.

Allowing a complete executable implementation or factory descriptor as input also defeats the impossibility premise, but then the claim approaches constructional universality rather than learned specialization.

## Fixed general machinery is compatible with the target

The [domain-extensibility definition](./definitions/domain-extensible-software-factory.md) separates fixed general machinery \(G\) from installed family specialization \(S_t\) through a target-independent allocation fixed before demand selection. A computational update can produce \(S_{t+1}\) while models, learning algorithms, metalanguages, runtimes, objective interfaces, resource controls, or a trusted kernel in \(G\) remain fixed.

This is also the relevant Bitter-Lesson boundary. The pressure is on human production of task- or family-specific competence over the claimed reach, not on the continued existence of every handcrafted general component. A fixed catalog that already encodes the target families merely hides specialization inside \(G\); a general computational method that produces needed specialization from permitted evidence is different. Whether the method is genuinely general is an empirical reach claim, not something fixed provenance settles by itself.

## Scope

- The negative prior-art claim is bounded to the retained sources. It identifies what those sources do not establish, not everything ever attempted under factory, synthesis, meta-learning, or self-modification terminology.
- Constructional and domain-universal are explications introduced here. Greenfield's factory specialization, composition, and recursive factory construction retain their historical meanings; *factory evolution* remains this synthesis's label for feedback-supported, versioned revision.
- Domain-universal coverage remains relative to declared evidence, acceptance, boundary, horizon, resources, and coverage. Removing those indices either trivializes the term or makes it impossible to test.
- Breadth does not establish quality or warrant. A broad closed process can install poor specialization; a narrow human-guided factory can produce excellent software.

---

Relevant Notes:

- [Computationally closed software-factory learning loop](./definitions/computationally-closed-software-factory-learning-loop.md) — contrasts: owns actor allocation over a declared path rather than the breadth of covered demands
- [A closed factory-learning transition produces a successor factory](./a-closed-factory-learning-transition-produces-a-successor-factory.md) — grounds: derives successor production without making any reach claim
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — grounds: explains why a closed update path inside supplied structure may remain narrow
- [The bitter lesson selects production methods, not representational forms](./the-bitter-lesson-selects-production-methods-not-representational.md) — grounds: locates the pressure in the method that produces specialization rather than its symbolic, natural-language, or parametric form
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — extends: separates broad unattended action from evidence that its evaluations are trustworthy

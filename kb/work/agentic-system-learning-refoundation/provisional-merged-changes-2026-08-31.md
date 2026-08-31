# Provisional merged changes — 2026-08-31

The operator judged this batch directionally useful but premature on 2026-08-31.
The changes may remain in `main`, but this ledger does not accept them as the
settled foundation or waive the workshop's migration gate. Revisit them when
the supporting derivation is ready.

The batch entered `main` through merge commit `5b396420`. The two changes
reviewed here are `75f84ecf` (*Permit nested delegation within existing
authority*) and `30f569e0` (*Ground software factory learning closure*).

## Change ledger

| Area | What changed | Why it may help | What remains premature |
|---|---|---|---|
| Nested delegation doctrine | Workers may delegate within their existing task authority and coordination boundary without a separate authorization grant. Parent scheduling, integration, and recovery remain in place; authority does not expand. | Removes a procedural gate while preserving scope and coordination constraints. | This is an operational doctrine change, not part of the theoretical derivation. Revisit it after observing whether nested delegation preserves ownership, traceability, and recovery in real runs. |
| Software-production task and process | Production is framed as a longitudinal obligation covering product state, evidence, interaction, acceptance, failures, and lifecycle work—not just one prompt or patch. | Makes delayed evidence and cross-task effects assessable. | The declared frame is a research-program extension, not inherited software-factory terminology. Check that the general learning architecture needs this whole frame before treating it as foundational. |
| Software factory | A factory is defined in the narrower Greenfield sense as family-specific lifecycle production machinery composed of schemas, assets, methods, workflows, tools, and runtime support. | Recovers a precise historical distinction between reusable production machinery and one product's state. | The workshop's broader agentic-system argument must not become true merely by adopting this narrower product-family vocabulary. Keep this as a specialized extension until the plain architectural role is independently established. |
| Factory development | Changes to reusable family-level production machinery are separated from changes to one product. The distinction is producer-relative when one factory produces another. | Prevents one-off product repair or code generation from being mislabeled as factory learning. | Test whether the boundary remains useful for task-local agent machinery that does not yet form a declared Greenfield-style product family. |
| Successor factory | A changed factory counts as a successor only when it becomes operative and governs later routed work. Succession does not imply improvement. | Makes installation and later causal use explicit. | Successor terminology belongs to the stronger operative-learning account. Minimal cross-task learning should be derivable without requiring it. |
| Computationally closed factory learning | A path is closed when computation performs every in-scope decision needed to turn permitted production evidence into an operative factory change. External requirements, observations, and declared oracles may remain. | Exposes hidden human factory-development decisions and makes actor allocation testable. | Closure is optional and path-relative. It must not define learning, practical breadth, competence, warrant, autonomy, or the general learning-factory architecture. |
| Evidence-responsive operative succession | Prior-art factory construction is separated from learning: production evidence must determine a reusable change, and the retained result must govern later work. | Identifies the missing causal conjunction between factory-valued output and learning. | This is stronger than the workshop's minimal condition that earlier experience changes retained machinery used later. Preserve the weaker premise underneath it. |
| Domain extensibility | Reach is defined as computational acquisition and installation of family-specific production machinery for novel covered demands under a declared evidence, acceptance, boundary, horizon, resource, and coverage frame. Fixed general machinery may remain. | Replaces vague universal-self-modification language with a bounded, testable reach claim. | It may be too strong to serve as the immediate architectural premise. First establish the modest practical pressure to construct useful machinery across a broad task family. |
| Closure versus reach | Computational closure and breadth are treated as independent axes. Unqualified *universal software factory* terminology is rejected as ambiguous. | Prevents a closed narrow updater or expressive constructor from being mistaken for broad learning capability. | The introduced universality distinctions are explications, not recovered historical terms. Use them only where a later experiment needs them. |
| Research-program article | The article now recognizes recursive factory construction as prior art, adds closed learning and successor factories, separates closure from domain reach, permits direct evidence-responsive updates, and reframes the bootstrap around acquiring supplied specialization. | Corrects several overclaims and provides clearer failure conditions. | The article was revised before the new workshop's supporting-note and alternative-mechanism gates were satisfied. It still opens from theory mediation rather than fully following the new conceptual spine. Revisit its structure after the foundation is derived independently. |
| Bitter Lesson article | The scaling burden moves from replacing every handcrafted component to computationally producing required task- or family-specific specialization. Explicit code and text remain compatible with scalable learning; fixed general machinery may remain. | Gives a more precise answer than a weights-only or universal-self-replacement criterion. | Domain extensibility is presently a research criterion, not an established capability. The article should keep that prediction separate from evidence about Commonplace's current human-inclusive loop. |

## Revisit conditions

Before treating this batch as settled:

1. Derive the minimal agentic architecture, practical machinery-construction
   pressure, and cross-task learning relation without using *software factory*,
   closure, successor, or theory mediation as premises.
2. Decide which factory concepts are foundational, specialized extensions, or
   only evaluation vocabulary.
3. Compare theory mediation with credible alternative learning mechanisms on
   the same experience-to-operative-change job.
4. Restructure the research-program article only after those dependencies are
   carried by durable notes.
5. Keep claims about current Commonplace operation separate from proposed
   domain extensibility and computational closure.
6. Review operational evidence from nested delegation and decide whether the
   doctrine needs stronger provenance, ownership, or recovery conditions.
7. Apply the transition map's `carry`, `revise`, `split`, or
   `retire-after-replacement` disposition to every affected durable artifact.

## Affected surfaces to read first

- [Conceptual spine](./conceptual-spine.md) — the dependency order against
  which these changes should be judged.
- [Transition map](./transition-map.md) — the current provisional disposition
  of the factory and theory-mediated material.
- [Software-factory ontology](../../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md)
  — the historical reconstruction behind the new definitions.
- [Operative succession](../../notes/operative-succession-turns-meta-factory-construction-into-learning.md)
  — the proposed boundary between factory construction and learning.
- [Closure and reach](../../notes/domain-extensibility-not-closure-determines-factory-reach.md)
  — the separation of actor allocation from breadth.
- [Research-program article](../../articles/a-research-program-for-learning-software-factories.md)
  and [Bitter Lesson article](../../articles/the-bitter-lesson-does-not-require-everything-to-live-in-weights.md)
  — the premature article-level integrations to revisit.


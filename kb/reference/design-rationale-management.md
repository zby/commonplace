---
description: "How Commonplace distributes design-rationale records across proposals, ADRs, contracts, and enforcement, without enforcing end-to-end continuity"
type: kb/types/note.md
traits: [has-external-sources, has-comparison]
---

# Design rationale management in Commonplace

Commonplace—the agent-operated knowledge base framework documented in this repository—provides distributed repository surfaces for retaining **design rationale**: why a system feature exists, what constrained it, which alternatives remained possible, what was chosen or rejected, and what evidence justified promoting a local solution into shared machinery.

[Workshops](../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) (temporary work-in-progress spaces under `kb/work/`), finished proposals, architecture decision records (ADRs), contract-governed [collections](./definitions/collection.md) (governed `kb/` subtrees with local authoring contracts), type specs, validators, package code, and version history each retain different parts of that rationale according to the design's state and authority. There is no central rationale database or single rationale-management command.

These surfaces support rationale retention, but they do not guarantee end-to-end continuity. Current proposal and ADR contracts do not require stable decision identities, provenance links, or backlinks from implemented machinery. Later recovery therefore depends primarily on what authors explicitly carry forward or connect—though colocated records, search, and git history may sometimes reconstruct enough context without a formal lineage chain.

This is an application of established design methodology, not a new method called "constraint-driven design." Design-rationale research uses the term for reasoning that explains and justifies design decisions, including alternatives and trade-offs ([MIT Design Rationale](https://rationale.csail.mit.edu/) at MIT CSAIL; [Feature, specification and evidence framework](https://doi.org/10.1017/dsj.2024.19)). The IDEF methods make the boundary especially explicit: IDEF9 discovers and analyses constraints, while IDEF6 captures rationale when situational constraints do not determine a unique decision ([IDEF methods compendium](https://www.idef.com/wp-content/uploads/2016/02/compendium.pdf)).

## Vocabulary boundary

Three nearby terms operate on different objects:

| Term | What it does in Commonplace |
|---|---|
| **Design constraint** | Restricts the feasible design space. A first principle is a constraint inherited from a consumer, substrate, domain, or machinery commitment; a problem-local constraint can restrict one collection without binding the framework. |
| **Design rationale** | Records how constraints, assumptions, alternatives, evidence, and trade-offs support a decision—especially where the constraints leave more than one feasible choice. |
| **[Constraining](../notes/definitions/constraining.md)** | Narrows the valid interpretations of a retained artifact. It is a deploy-time learning operation, not the name of the design methodology. |

A design constraint can motivate [distillation](../notes/definitions/distillation.md)—extracting a use-shaped artifact from larger material—deferred commitment, local variation, or relaxation rather than constraining. Conversely, a freely chosen convention can constrain an artifact even though no inherited constraint required that convention. Commonplace therefore reserves *constraining* for the semantic operation [defined in the learning-theory vocabulary](../notes/definitions/constraining.md), while [first principles are inherited constraints, not design choices](../notes/first-principles-are-inherited-constraints-not-design-choices.md).

## Repository representation

| Rationale state | Commonplace surface | What the surface can retain |
|---|---|---|
| Active exploration | `kb/work/` | Evidence, competing framings, experiments, and provisional decisions that have not earned library status |
| Finished but undecided design | [`kb/reference/proposals/`](./proposals/README.md) | Problem, option space, forces, free choices, current-state assumptions, and adoption criteria |
| Implemented decision | [Architecture decision record (ADR)](./types/adr.md) | Required context, decision, and consequences; richer records may also retain alternatives and evidence |
| Local operating contract | `COLLECTION.md` and collection-local type specs | The constraints proven for one collection without claiming framework-wide reach |
| Shared reusable design | Global types, [text-contract profiles](../notes/definitions/text-contract.md), instructions, validators, and package code | A commitment promoted after its scope and enforcement shape became clear |
| Rejected or displaced design | Rejected proposal options, ADR consequences, supersession links, and git history | Explicitly authored reasons; git history remains an archival fallback rather than a semantic rationale relation |

These surfaces describe a typical promotion path—a state-to-surface map and cited lifecycle contracts, not mechanically enforced transitions with defined promotion criteria; they do not require every design to traverse every stage. A local convention can remain local indefinitely. A deterministic defect can move directly into a validator. A mature decision may need an ADR without a standing proposal. ADRs record implemented decisions only ([ADR type](./types/adr.md)); undecided designs wait in [`proposals/`](./proposals/README.md), and active exploration stays in workshops—current contracts do not assign a dedicated rationale surface to the decided-but-not-yet-implemented interval. [ADR 028](./adr/028-design-proposals-live-in-reference-proposals.md) defines the proposal-to-ADR lifecycle, but no transition contract requires every proposal field to survive that move.

Two shipped decisions illustrate the intended discipline, not a repository-wide guarantee. [ADR 042](./adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) promotes a collection-local counterexample into an open, worked-case-gated [text-contract profile](../notes/definitions/text-contract.md) system while retaining the local-vs-universal boundary. [ADR 040](./adr/040-scripts-directory-is-the-accumulation-substrate-for-ad-hoc-tooling.md) keeps reusable ad hoc tooling in `scripts/` until repeated, stable use earns package promotion. They suggest what well-retained rationale can look like; they do not demonstrate which alternatives and evidence remain recoverable from each record without author linking.

## What the Epistack casework added

Casework in the sibling `epistack-casebooks` project, undertaken for the [2026 Epistemic Case Study Competition](../sources/epistemic-case-study-competition.md), exposed rationale management as a unifying description of Commonplace's distributed practice. The casework suggests a compounding risk: when the retained artifact does not distinguish inherited constraints, local requirements, and free choices, a later investigator may find transfer assessment harder—not a demonstrated rule that reuse becomes unsafe without that distinction.

For Commonplace, **design rationale management for evolving knowledge infrastructure** is therefore a useful name for distributed repository practice rather than an enforced traceability protocol or a contract-defined minimum above opportunistic documentation. In intended practice, constraint discovery identifies what bounds a decision; rationale records what those constraints do and do not determine; worked cases may test whether the rationale has reach; and constraining may give selected commitments the warranted degree of semantic or mechanical force when authors and validators actually apply it. Where later recovery matters, authors must still carry or link that rationale explicitly; no provenance mechanism reconnects a commitment to its constraints, alternatives, and evidence automatically.

## Open questions

- **TODO:** Record a worked reuse comparison when casework supplies one: how preserving inherited constraints, local requirements, and free choices in retained artifacts changes a later transfer judgment (Epistack sibling project is the intended source, not a library artifact here).
- **TODO:** Trace one ordinary Commonplace decision from originating constraints and alternatives through its chosen surface and any later promotion—including how a reader finds that lineage when stages are skipped.

---

Relevant Notes:

- [Design proposals differ from claims in kind, not confidence](../notes/design-proposals-differ-from-claims-in-kind-not-confidence.md) — rationale: explains why free design parameters need a proposal surface judged by forces and usefulness rather than truth alone
- [First-principles reasoning selects for explanatory reach over adaptive fit](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) — rationale: supplies the rival-practice and transfer tests used to judge whether a rationale reaches beyond its originating case
- [Progressive constraining commits only after patterns stabilize](../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) — rationale: explains why some rationale should remain provisional until repeated behavior supports a stronger commitment

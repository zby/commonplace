---
description: "What the KB application is for in Commonplace's design program — composition test, two worked provenance instances, and the transfer evidence the repository does not have"
type: kb/types/note.md
tags: [foundations]
---

# Commonplace as an instrument

Commonplace's immediate application is an agent-operated knowledge base. The KB is not the boundary of the program. It is the first worked case in which the design's theories — about retrieval, representation, review, validation, and self-modification — meet real operating constraints *together*, rather than being invented in the abstract and checked one at a time.

Everything here is indexed to one objective: more useful and better-warranted knowledge work per unit of human judgment spent. Not automation.

Two things follow from treating the KB as an instrument rather than as the product.

## Use tests composition

The components must compose into sustained knowledge work — types, collection contracts, validators, review pairs, freshness baselines, and skills running against each other on a live corpus, not each demonstrated on its own bench. Where they fail to compose, the failure is evidence against the design theories that produced them, not merely a defect ticket.

The traced instance is the `tag-readme` change. An `index` head grew too large to support its completeness claim; [ADR 026](./adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) split the type and made `complete` an enforced mark, carrying one decision into instruction, schema, validation, and rendering; the validator then rejected artifacts it had previously accepted, and the symbolic check caught a tagged member that the documented `rg` recipe had missed, forcing the natural-language recipe to be corrected. [The commit-by-commit trace](./tag-readme-trace-observed-causal-connection.md) and [the improvement-loop reading](./tag-readme-trace-as-self-improving-loop.md) hold the detail; [the classification](./commonplace-as-a-reflective-system.md) states what it establishes about reflectivity.

What it establishes about *composition* is narrower. It is one pathway, and use exercises the whole configuration at once and reports one bit about it, so [use tests a decomposition only locally](../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md). Surviving here licenses replay in this repository. It does not license the rule.

## Retained rationale is the part that could travel

The route out of that limit is not more use; it is rationale retained at design time, which is what gives a transfer claim an antecedent to test. [A decomposition earns explanatory-reach by derivation or inheritance](../notes/a-decomposition-earns-explanatory-reach-by-derivation-or-inheritance.md) names the two routes, and the repository carries one worked instance of each.

- **Derived.** [Representational form](../notes/definitions/representational-form.md) generates its three categories from two axes — whether a defined consumer assigns consequences to the artifact, and whether the content sits in a localized unit. Its Derivation section states the axes, marks the fourth cell as unoccupied in this domain rather than impossible, and derives the read/test/probe inspection rule instead of stipulating it per form.
- **Inherited.** [Reflective system](../notes/definitions/reflective-system.md) takes causal connection, self-representation, and theory-relativity from Maes 1988 with the Smith 1984 lineage behind it, carried as `derived-from` edges to the source ingests. Its "Provenance and departures" section separates the purchase from the local extension, naming retrieval-as-causal-connection as Commonplace's own with no source behind it.

Both instances are auditable: a reader can see which parts were bought and which were added here.

## What the repository does not have

The rationale surfaces are distributed across workshops, proposals, ADRs, collection contracts, types, validators, and git history, and [they do not guarantee end-to-end continuity](./design-rationale-management.md). Current proposal and ADR contracts require no stable decision identities, no provenance links, and no backlinks from implemented machinery. Later recovery depends on what an author explicitly carried forward or connected.

So the honest statements are these.

- Commonplace does not retain the rationale behind each mechanism. Two definitions carry a worked provenance record. The rest of the repository's mechanisms carry whatever their authors happened to write down, at whatever fidelity, with no contract requiring more.
- Disciplined transfer has not been demonstrated. Both instances were authored inside the system that states the claim and assessed by nobody outside it. They show that provenance is recordable and that departures are auditable once recorded — not that recording it produces better designs.
- Retained-but-unfaithful rationale is worse than absent, and nothing in the repository has yet tested faithfulness by intervention. A rationale that has never been contradicted is not thereby a rationale that holds.

The missing evidence is already named, as the two open TODOs in [design rationale management](./design-rationale-management.md): a worked reuse comparison showing how preserving inherited constraints, local requirements, and free choices changes a later transfer judgment, and one ordinary Commonplace decision traced end to end from originating constraints and alternatives through its chosen surface and any later promotion.

## What would change the status

This is a defensible position, not a demonstrated one. It becomes demonstrated on evidence of this shape:

- **Close the two TODOs with outcomes, not records.** An end-to-end trace that shows a reader finding the lineage — including across skipped stages — and a reuse comparison that reports whether the retained distinction actually changed a transfer judgment rather than merely being available to it.
- **An outside assessment.** Someone not operating this repository reuses a Commonplace decomposition, checks against the retained rationale whether the constraints still bind, and reports whether that check discriminated better than rebuilding and seeing.
- **A faithfulness test by intervention.** Vary a stated force and observe whether the decomposition's fit degrades as the rationale predicts. A retained force that survives being varied is the first real evidence that the record is about the design rather than about the author.
- **Composition failures attributed back.** More than one operational failure traced to a named design theory, on components not co-designed for the trace. One pathway is not a sample.

Until then, treating the KB as an instrument is a claim about what the application is *for*, backed by two worked provenance instances and one composition trace — and no more than that.

---

Relevant Notes:

- [The Commonplace declared frame](./commonplace-declared-frame.md) — part-of: declares the system boundary and actor partition this reading assumes, and deliberately leaves the objective open — which this artifact supplies
- [Design rationale management in Commonplace](./design-rationale-management.md) — part-of: the full survey of rationale surfaces, their state-to-surface map, and the continuity the shipped contracts do not enforce
- [Commonplace as a reflective self-improving system](./commonplace-as-a-reflective-system.md) — see-also: the sibling classification of the same repository, assessed for reflectivity and actor allocation rather than for what the application is for
- [The tag-readme change as an observed causal-connection trace](./tag-readme-trace-observed-causal-connection.md) — see-also: the commit-by-commit record behind the composition instance cited here
- [The tag-readme trace read as a self-improving loop](./tag-readme-trace-as-self-improving-loop.md) — see-also: the search, evaluation, and retention mapping of the same instance
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) — rationale: why composing successfully here supports replay rather than a rule, and why the rationale must be written at design time or be gone
- [A decomposition earns explanatory-reach by derivation or inheritance](../notes/a-decomposition-earns-explanatory-reach-by-derivation-or-inheritance.md) — rationale: the two provenance routes the worked instances occupy, and the reason a free choice supports no scope claim
- [Self-improvement is relative to a declared objective](../notes/self-improvement-is-relative-to-a-declared-objective.md) — rationale: why the objective stated above has to be declared independently of the changes it is invoked to license
- [Increasing computational autonomy relocates human effort](../notes/increasing-computational-autonomy-relocates-human-effort.md) — rationale: why the measure is work per unit of human judgment rather than the removal of human judgment
- [History has one chance to become checkable](../notes/history-has-one-chance-to-become-checkable.md) — rationale: the general claim behind retaining rationale at design time rather than expecting to recover it
- [Selective revision needs a faithful rationale, not just a legible one](../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) — rationale: the worse-than-absent asymmetry and the intervention test behind the faithfulness statement above
- [The anatomy of a design theory (Gregor and Jones, 2007)](../sources/the-anatomy-of-a-design-theory-gregor-jones-2007.ingest.md) — evidence: makes the built artifact a non-core component of a design theory and records that an artifact alone stays craft knowledge until its principles are abstracted

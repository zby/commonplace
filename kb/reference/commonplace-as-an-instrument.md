---
description: "What the KB application is for in Commonplace's design program — its declared objective, what operating this KB can and cannot establish, and the limits of local evidence"
type: types/note.md
tags: []
---

# Commonplace as an instrument

Commonplace's immediate application is an agent-operated knowledge base. The KB is not the boundary of the program. It is the first worked case in which the design's theories — about retrieval, representation, review, validation, and self-modification — meet real operating constraints *together*, rather than being invented in the abstract and checked one at a time.

The KB is where we test changes against [what Commonplace chooses to count as progress](../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md#what-commonplace-chooses-to-count). Automating a task is not, by itself, a gain.

Two things follow from treating the KB as an instrument rather than as the product.

## Use tests composition

The types and tools must work together in sustained use — types, collection contracts, validators, review pairs, their result files, and skills running against each other on a live corpus, not each demonstrated on its own bench. Where they fail to compose, the failure is evidence against the design theories that produced them, not merely a defect ticket.

The `tag-readme` trace shows one such pathway. An `index` head grew too large to support its completeness claim; [ADR 026](./adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) split the type and made `complete` an enforced mark, carrying one decision into instruction, schema, validation, and rendering; the validator then rejected artifacts it had previously accepted, and the symbolic check caught a tagged member that the documented `rg` recipe had missed, forcing the natural-language recipe to be corrected. [The commit-by-commit trace](../theory/evidence/tag-readme-trace-observed-causal-connection.md) and [the improvement-loop reading](../theory/evidence/tag-readme-trace-as-self-improving-loop.md) hold the detail; [the classification](../theory/evidence/commonplace-as-a-reflective-system.md) states what it establishes about reflectivity.

What that trace establishes about *composition* is narrower. Use exercises the whole configuration at once and reports one bit about it, so [use tests a decomposition only locally](../theory/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md). Surviving here licenses replay in this repository; it does not license the rule. This KB also documents the methodology it uses: that makes it a useful place to observe how the pieces work together, while leaving open whether the same practices repay their cost in a different subject domain such as a runbook or product KB.

## Retained rationale is the part that could travel

The route out of local replay is not more use; it is rationale retained at design time, which gives a transfer claim an antecedent to test. [Derivation and inheritance give a decomposition's scope claim its starting warrant](../theory/derivation-and-inheritance-give-starting-warrant-earns-scope.md) — warrant, not earning. Two definitions in this repository illustrate the two routes:

- **Derived.** [Representational form](../theory/definitions/representational-form.md) generates its three categories from two axes — whether a defined consumer assigns consequences to the artifact, and whether the content sits in a localized unit. Its Derivation section states the axes, marks the fourth cell as unoccupied in this domain rather than impossible, and derives the read/test/probe inspection rule instead of stipulating it per form.
- **Inherited.** [Reflective system](../theory/definitions/reflective-system.md) takes causal connection, self-representation, and theory-relativity from Maes 1988 with the Smith 1984 lineage behind it, carried as `derived-from` edges to the source ingests. Its "Provenance and departures" section separates the purchase from the local extension, naming retrieval-as-causal-connection as Commonplace's own with no source behind it.

Both instances are auditable: a reader can see which parts were bought and which were added here.

## What operating this KB does not establish

The rationale surfaces are distributed across workshops, proposals, ADRs, collection contracts, types, validators, and git history, and [they do not guarantee end-to-end continuity](./design-rationale-management.md). Current proposal and ADR contracts require no stable decision identities, no provenance links, and no backlinks from implemented machinery. Later recovery depends on what an author explicitly carried forward or connected.

Accordingly, the cited instances and current contracts leave four gaps open:

- **Contract-wide provenance is not enforced.** The two definitions above show that provenance is recordable and that departures are auditable once recorded. Shipped contracts do not require that level of record across mechanisms, so coverage elsewhere depends on what individual authors chose to write down.
- **Local operation does not compare against a baseline.** Even where a mechanism works as designed here, local use does not show whether it produced better-warranted work for the same human effort, or comparable work for less effort. Commonplace could satisfy its own internal checks while consuming more human judgment than the improvement justifies. [Ablation baselines for the declared objective](./proposals/ablation-baselines-for-the-declared-objective.md) sketches how that comparison might be tested; its proposed experiment is not an adopted requirement.
- **The cited instances do not establish transfer across operators or domains.** Both provenance instances were authored inside the system that states the claim and assessed inside this repository. They do not establish whether recording rationale changes transfer judgments, whether an independent operator benefits from checking it, or whether the same practices repay their cost outside a self-documenting methodology KB.
- **Passive consistency does not test rationale faithfulness.** Retained-but-unfaithful rationale is worse than absent, and a rationale that has never been tested by varying a stated force is not thereby a rationale that holds.

Two of these transfer-recovery gaps are already recorded as open questions in [design rationale management](./design-rationale-management.md): whether preserving inherited constraints, local requirements, and free choices changes a later reuse judgment, and what a reader actually recovers when tracing one ordinary Commonplace decision end to end.

## What would change the status

Treating the KB as an instrument is a defensible position about what the application is *for*, not a demonstrated result. Demonstrating it requires evidence of five shapes:

- **Baseline comparison in a named area.** Compare the work done with and without the machinery on the same task. A gain on that task supports a broader judgment only insofar as plausible losses elsewhere do not outweigh it (one candidate design is outlined in the unadopted [ablation proposal](./proposals/ablation-baselines-for-the-declared-objective.md)).
- **Answers with outcomes to the open rationale questions.** An end-to-end decision trace showing what a reader recovers across skipped stages, and a reuse comparison reporting whether retained constraint distinctions actually changed a transfer judgment rather than merely being available to it.
- **Independent-operator and cross-domain tests.** An independent operator reusing a Commonplace decomposition against its retained rationale tests operator independence; applying the practices to a different subject domain (such as a runbook or product KB) tests domain independence. The two test different things.
- **A faithfulness test by intervention.** Varying a stated force and observing whether the decomposition's fit degrades as the rationale predicts. A retained force that survives being varied is the first real evidence that the record is about the design rather than about the author.
- **Composition failures attributed back.** Multiple operational failures traced to named design theories on components not co-designed for the trace.

Until evidence of these shapes exists, this page states what the KB application is *for* and what local operation can and cannot establish — not that the program has earned its objective.

---

Relevant Notes:

- [The declared Commonplace frame](./commonplace-declared-frame.md) — see-also: declares the system boundary and actor partition this reading assumes, without fixing what counts as improvement
- [Design rationale management in Commonplace](./design-rationale-management.md) — see-also: the full survey of rationale surfaces, their state-to-surface map, and the continuity the shipped contracts do not enforce
- [Ablation baselines for the declared objective](./proposals/ablation-baselines-for-the-declared-objective.md) — see-also: unadopted proposal sketching comparative baselines for testing whether the framework repays its human-judgment cost
- [Commonplace as a reflective self-improving system](../theory/evidence/commonplace-as-a-reflective-system.md) — see-also: the sibling classification of the same repository, assessed for reflectivity and actor allocation rather than for what the application is for
- [The tag-readme change as an observed causal-connection trace](../theory/evidence/tag-readme-trace-observed-causal-connection.md) — see-also: the commit-by-commit record behind the composition instance cited here
- [The tag-readme trace read as a self-improving loop](../theory/evidence/tag-readme-trace-as-self-improving-loop.md) — see-also: the search, evaluation, and retention mapping of the same instance
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../theory/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) — rests-on: why composing successfully here supports replay rather than a rule, and why the rationale must be written at design time or be gone
- [Derivation and inheritance give starting warrant; discriminating evidence or proof earns scope](../theory/derivation-and-inheritance-give-starting-warrant-earns-scope.md) — rests-on: the warrant grades the worked instances occupy, and the reason a free choice supports no scope claim
- [Self-improvement is relative to a declared objective](../theory/self-improvement-is-relative-to-a-declared-objective.md) — rests-on: why the objective has to be declared independently of the changes it is invoked to license
- [Increasing computational autonomy relocates human effort](../theory/increasing-computational-autonomy-relocates-human-effort.md) — rests-on: why removing a human step does not establish a saving in human judgment
- [History has one chance to become checkable](../theory/history-has-one-chance-to-become-checkable.md) — rests-on: the general claim behind retaining rationale at design time rather than expecting to recover it
- [Selective revision needs a faithful rationale, not just a legible one](../theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md) — rests-on: the worse-than-absent asymmetry and the intervention test behind the faithfulness statement above

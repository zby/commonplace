---
description: "Separates an adopted improvement from a discarded proposal and fixes the comparison requirements before development; non-regression covers the predecessor's declared prior capabilities"
type: types/note.md
traits: [title-as-claim, has-comparison]
tags: [learning-theory, self-improving-systems, software-factory, evaluation]
---

# A better-factory claim compares operative states under an antecedent assessment relation

> TODO! remove or update to use software house instead of software factory

A [software factory](./definitions/software-factory.md) undergoes experience-responsive retention when production experience causes a retained change to its reusable machinery that later work depends on, and [learns when such retention improves it](./factory-learning-is-experience-responsive-retention-that-improves.md). Retention has no quality requirement: a retained change can degrade the factory as easily as improve it. Whether it got *better* is therefore its own claim with different relata and its own declarations. The claim compares two operative states of the factory under an assessment relation fixed before the development it judges. Throughout, *better* means better under the declared relation: the claim is relation-relative and auditable, not a verdict on the factory's quality over its open production family.

The comparison names the predecessor and adopted successor, the requirements under which the successor counts as better, and how those requirements apply to the predecessor's prior capabilities.

## The relata are operative states, not the change that produced them

Three terms keep the comparison's endpoints straight.

- The **predecessor** is the factory state current when the comparison is declared.
- A **candidate** is a constructed or proposed factory that has not yet been installed. It is not a term in the comparison.
- The **operative successor** is the state that is installed and that later production and factory development depend on — [operative in the behavioral-authority sense](./definitions/operative-change.md), not merely stored.

A candidate that is generated and discarded never enters the comparison, so a better-factory claim cannot be read off a construction event. A staging comparison can supply evidence for adopting a candidate; the improvement claim concerns the state actually installed and used. In a continuously revised system, the successor can instead be the operative state at a named measurement boundary, after one change or a period of development.

## The assessment relation is antecedent and scope-indexed

The relation has two components. The successor must meet **non-regression thresholds** on the predecessor's prior scope, and must **improve on the predecessor by a declared amount** on at least one named production dimension.

Both are declared while only the predecessor exists. This framework adds prior declaration of the comparison requirements to the linked requirement that [an improvement objective be independently specifiable](./self-improvement-is-relative-to-a-declared-objective.md). Independent specifiability blocks objectives fitted to the result; prior declaration also makes the comparison requirements available for inspection before development. Choosing dimensions and thresholds after seeing the result permits selection of requirements the successor happens to satisfy. Prior declaration prevents that form of post-hoc selection. It does not show that the requirements track factory quality.

Non-regression needs a declared scope: the capabilities the successor must preserve, with thresholds specifying how much degradation is permitted. This framework uses the predecessor's prior capabilities as that scope. Naming it makes explicit which losses would cause the comparison to fail.

The compared states span the whole production environment. Because [the deployed system rather than the model alone is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md), the successor may improve through changes to any operative part of its machinery — prompts, natural-language artifacts, code, tools, workflows, tests, evaluators — and holding model weights fixed does not put the comparison out of reach.

If the checked prior scope includes an operative path for [factory development](./definitions/factory-development.md), non-regression requires the successor to preserve that capability: a production gain alone does not show that the system can still produce another revision. The requirement concerns a [revision path that remains applicable after the transition](./a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md), not merely editable files.

## Improvement, retention and learning are different claims

Retaining a change does not establish improvement, and establishing improvement does not show that production experience caused it. Consider three hypothetical changes to the search machinery a factory uses to retrieve reusable production knowledge:

- **Retention without improvement.** After missing a relevant note, the factory retains an instruction to search by synonyms. Later production uses it, but the extra searches do not improve retrieval and waste time. Experience caused a retained change, but the change did not help.
- **Improvement without learning.** A scheduled search-tool upgrade, selected independently of the factory's production experience, improves retrieval and passes the declared comparison. The factory improved, but not through learning from its production experience.
- **Learning.** A missed note leads to the retained synonym-search instruction, and using that instruction improves retrieval under the declared comparison. This is learning when the experience-derived change causally contributes to the improvement.

The third case requires evidence of that contribution, not just the sequence of a failure, a retained instruction and better results. Comparing otherwise equivalent runs with and without the retained instruction tests its contribution, because [an experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md).

The declared comparison judges improvement; the experience-to-change link distinguishes learning. A change that improves the factory against another objective need not pass this comparison. Internal controls on what the factory retains govern adoption, but do not by themselves establish that the adopted state passes the declared comparison.

## Scope

- The framework indexes and disciplines the comparison; it does not supply an oracle for it. What makes a successor genuinely better over an open family remains unresolved here.
- Antecedence blocks post-hoc dimension selection. It does not make the declared dimensions the right ones: a comparison can be properly declared in advance and still measure something that does not matter.
- Antecedence guards this claim's auditability; it is not constitutive of improvement. An independently supplied retrospective criterion can ground a legitimate improvement claim, just not this audit-proof one.
- The two-component relation — non-regression plus a named target — is the shape this framework declares, not the only declarable one. A relation permitting retirement of obsolete or unsafe prior capability can be declared; the preserved-path consequence then no longer follows.
- A comparison judges the adopted states. Whether an evaluator also controlled adoption is a separate causal question; a description cannot change whether its judgment was required for installation.
- Operative states and an antecedent scope-indexed relation can be used for other systems that revise their reusable machinery. Preserving factory development follows only when that capability is included in the checked scope.

## Open Questions

- What the declared comparison must specify about the predecessor's baseline, measurement procedures and comparable conditions, and which of these requirements belong to this framework rather than to the chosen assessment relation.
- Whether the predecessor's prior scope can be specified precisely enough for non-regression to be checkable when the declared family is open-ended.

---

Relevant Notes:

- [Factory learning is experience-responsive retention that improves the factory](./factory-learning-is-experience-responsive-retention-that-improves.md) — grounds: the retention layer whose silence about quality makes the improvement comparison a separate claim
- [Self-improvement is relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md) — grounds: the indexed and antecedent conditions this applies to a pairwise state comparison
- [A repeatable operative path keeps a redesign class open to revision](./a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) — grounds: what preserving a factory-development path requires beyond editability
- [An experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md) — grounds: why a passed comparison does not identify the experience link
- [The deployed system, not the model alone, is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md) — grounds: places all operative production machinery inside the compared states
- [Revising an improvement objective is licensed from outside it or is not improvement](./revising-an-improvement-objective-is-licensed-from-outside-it.md) — extends: what happens when the declared comparison is itself what changes
- [Operative change](./definitions/operative-change.md) — defined-in: the installed-and-depended-on condition that separates a candidate from the successor
- [Software factory](./definitions/software-factory.md) — defined-in: the compared object
- [Factory development](./definitions/factory-development.md) — defined-in: the scope element that carries the preserved-path requirement

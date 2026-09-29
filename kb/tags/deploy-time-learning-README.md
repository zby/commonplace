---
description: "Curated head for the deploy-time-learning tag — what deployed use reveals beyond design and testing, and how people or systems respond through maintenance, adaptation, and learning from experience"
type: types/tag-readme.md
complete: true
---

# deploy-time-learning

Deployment brings software into contact with users, changing needs, and operating conditions that design and testing did not fully anticipate. Assign this tag to work on what that use reveals or how people and systems respond: diagnosing failed requirements, modifying software or instructions, evaluating and retaining lessons, or preserving the knowledge needed for later change. Mechanisms and limits of learning from use qualify even when the argument generalizes beyond a particular deployment. Generic improvement or a passing mention of deployment is insufficient; adaptation to experience, new demands, or failures encountered in use must be substantive.

Responses may be human maintenance, automated adaptation, or a combination. [Self-improving-systems](./self-improving-systems-README.md) covers systems that change their own organization; [continual-learning](./continual-learning-README.md) covers continued learning through retained changes outside model weights. Work on those mechanisms as responses to deployed experience may carry both tags. This tag does not require autonomous change, weight updates, or a particular retention mechanism. A child of [learning-theory](./learning-theory-README.md).

## What deployment reveals

- [changing requirements conflate genuine change with disambiguation failure](../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) — the core case: some post-release change is world change, some is late discovery that the wrong interpretation of an underspecified requirement was built
- [exact implementation does not validate a requirement against its objective](../notes/exact-implementation-does-not-validate-a-requirement.md) — a requirement stays a conjectured proxy for the objective until use tests it
- [use tests a decomposition locally; retained rationale makes transfer testable](../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) — running a design confirms only that it sufficed here
- [system use is an initial selection environment when theory fit lacks a fixed oracle](../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md) and [system use provides evidence of theory fit, not independent warrant](../notes/system-use-provides-evidence-of-theory-fit-not-independent-warrant.md) — the same phenomenon for a working theory: live use selects what fits, without licensing the claims
- [Naur's compiler case tests one historically bounded documentation-and-consumption system](../notes/naurs-compiler-case-tests-one-documentation-and-consumption-system.md) — the classic account of why maintainers who lack the program's theory cannot make the changes deployment demands
- [abstract an experience only when you can state where the lesson stops](../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) — what to retain from a deployment episode: a lesson only when its boundary is statable, else the instance

## Where the change lands

- [the deployed system, not the model alone, is the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) — prompts, retrieval, tools, and runtime policy jointly determine behavior, so post-deployment change reaches all of them
- [ad hoc prompts extend the system without schema changes](../notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md) — an LLM layer absorbs new requirements in natural language before the deterministic base changes
- [constraining during deployment is continuous learning](../notes/constraining-during-deployment-is-continuous-learning.md) — prompts, schemas, tools, and tests accumulate the adaptation outside weights
- [retained system-definition artifacts enable persistent deployment-time adaptation](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) — the framework answer: retained, evaluated artifact changes give a deployed system a persistent adaptation path
- [scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) — stronger models do not remove deployment-specific structure while assigned difficulty keeps pace with capability

## Related Tags

- [self-improving-systems](./self-improving-systems-README.md) — systems that make the post-deployment changes themselves: update architectures, reflection, and the actor allocation between humans and computation
- [constraining](./constraining-README.md) — the mechanism by which a deployed system's interpretation space is narrowed as use reveals what it should have been

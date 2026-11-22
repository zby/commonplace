---
description: "Curated head for the deploy-time-learning tag — what deployed use reveals beyond design and testing, and how people or systems respond through maintenance, adaptation, and learning from experience"
type: types/tag-readme.md
complete: true
---

# deploy-time-learning

Deployment brings software into contact with users, changing needs, and operating conditions that design and testing did not fully anticipate. Assign this tag to work on what that use reveals or how people and systems respond: diagnosing failed requirements, modifying software or instructions, evaluating and retaining lessons, or preserving the knowledge needed for later change. Mechanisms and limits of learning from use qualify even when the argument generalizes beyond a particular deployment. Generic improvement or a passing mention of deployment is insufficient; adaptation to experience, new demands, or failures encountered in use must be substantive.

The cluster's main claim is that the ordinary evolution of a deployed system is learning. When people fix bugs and add features in response to use, the system changes what it can do later. Each fix is proposed, reviewed and can be rejected, so this is [selection-based learning](../theory/definitions/selection-based-learning.md) with human judgment doing the selecting. Automating that selection is a further step, not what makes it learning.

Responses may be human maintenance, automated adaptation, or a combination. [Self-improving-systems](./self-improving-systems-README.md) covers systems that change their own organization; [continual-learning](./continual-learning-README.md) covers continued learning through retained changes outside model weights. Work on those mechanisms as responses to deployed experience may carry both tags. This tag does not require autonomous change, weight updates, or a particular retention mechanism. A child of [learning-theory](./learning-theory-README.md).

## What deployment reveals

- [changing requirements conflate genuine change with disambiguation failure](../theory/changing-requirements-conflate-genuine-change-with-disambiguation.md) — the core case: some post-release change is world change, some is late discovery that the wrong interpretation of an underspecified requirement was built
- [exact implementation does not validate a requirement against its objective](../theory/exact-implementation-does-not-validate-a-requirement.md) — a requirement stays a conjectured proxy for the objective until use tests it
- [use tests a decomposition locally; retained rationale makes transfer testable](../theory/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) — running a design confirms only that it sufficed here
- [system use is an initial selection environment when theory fit lacks a fixed oracle](../theory/system-use-selects-theory-fit-without-a-fixed-oracle.md) and [system use provides evidence of theory fit, not independent warrant](../theory/system-use-provides-evidence-of-theory-fit-not-an-independent-test.md) — the same phenomenon for a working theory: live use selects what fits, without licensing the claims
- [Naur's compiler case tests one historically bounded documentation-and-consumption system](../theory/naurs-compiler-case-tests-one-documentation-and-consumption-system.md) — the classic account of why maintainers who lack the program's theory cannot make the changes deployment demands
- [abstract an experience only when you can state where the lesson stops](../theory/abstract-an-experience-only-when-you-can-state-the-boundary.md) — what to retain from a deployment episode: a lesson only when its boundary is statable, else the instance

## Where the change lands

- [the deployed system, not the model alone, is the unit of learning](../theory/the-deployed-system-not-the-model-is-the-unit-of-learning.md) — prompts, retrieval, tools, and runtime policy jointly determine behavior, so post-deployment change reaches all of them
- [ad hoc prompts extend the system without schema changes](../theory/ad-hoc-prompts-extend-the-system-without-schema-changes.md) — an LLM layer absorbs new requirements in natural language before the deterministic base changes
- [Constraining during deployment can produce learning outside weights](../theory/constraining-during-deployment-can-produce-learning-outside-weights.md) — prompts, schemas, tools, and tests accumulate the adaptation outside weights
- [retained system-definition artifacts enable persistent deployment-time adaptation](../theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md) — the framework answer: retained, evaluated artifact changes give a deployed system a persistent adaptation path
- [scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../theory/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) — stronger models do not remove deployment-specific structure while assigned difficulty keeps pace with capability

## Related Tags

- [self-improving-systems](./self-improving-systems-README.md) — systems that make the post-deployment changes themselves: update architectures, reflection, and the actor allocation between humans and computation
- [improvement-loop](./improvement-loop-README.md) — how a change made in response to deployed use is selected: the proposal-selection loop and [selection-based learning](../theory/definitions/selection-based-learning.md)
- [continual-learning](./continual-learning-README.md) — learning through retained changes outside model weights, whatever prompted it
- [constraining](./constraining-README.md) — the mechanism by which a deployed system's interpretation space is narrowed as use reveals what it should have been

---
description: "Spec-first, bidirectional specs, and behavior-extracted rules fit different phases of understanding: knowledge available before work, discovered during execution, or only visible after repeated observation"
type: note
traits: [has-external-sources]
tags: [learning-theory, context-engineering]
status: seedling
---

# Specification strategy should follow where understanding lives

Debates about spec-driven development often collapse three different moves into one argument: write the spec upfront, keep the spec updated as implementation proceeds, or extract rules from behavior after the fact. These are not rival doctrines. They answer a prior question: **where does the missing understanding currently live?**

If the understanding already exists in human intent, write it down before execution. If it only becomes visible while traversing a codebase or integrating with real constraints, the spec has to stay open to discovery. If the rule is not legible until the system has run many times, let the behavior happen first and mine the rule afterward into executable or machine-checkable artifacts. The real choice is not "specs or no specs." It is which specification strategy matches the phase of understanding the project is in.

## Three locations of understanding

### 1. Understanding available before execution

[Spec Driven Development](../sources/the-spec-is-the-new-code-a-guide-to-spec-driven-development-2033303156340240481.ingest.md) is strongest when the missing knowledge is mostly in the human and can be articulated before code is written. Functional requirements, acceptance criteria, architectural constraints, and task boundaries all reduce the number of silent decisions the agent has to make. This is [constraining](./constraining.md) applied early: narrow the interpretation space before execution so the agent never has to guess about idempotency, authorization, or what "the backoffice" means.

This regime fits work where ambiguity is cheap to remove upfront. Its failure mode is premature certainty: teams write detailed plans for parts of the system they do not yet understand, then confuse speculative prose with discovered reality.

### 2. Understanding discovered during execution

Augment's [bidirectional spec pattern](../sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md) addresses a different regime. The human may know the intent, but the crucial constraints live in the repo and only become visible during implementation: an existing auth context, a hidden convention, an API contract that makes the initial plan wrong. At the same time, execution is generating new knowledge faster than humans will reliably maintain a separate planning document. In this regime, a one-way upfront spec decays because execution keeps learning things the document does not, and maintenance throughput falls behind generation throughput.

Here the spec must become a living negotiation between intent and discovery. Agents surface directional decisions back into the artifact so [disambiguation failures](./changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) are caught before they cascade downstream. The problem is not that upfront specification was mistaken. It is that part of reality was still unknown when the first version was written.

### 3. Understanding visible only after repeated behavior

Some rules are not visible either in advance or during a single execution. They emerge only after repeated observation: which failure clusters recur, which transformations are always mechanical, which checks admit a hard oracle. In that regime, the right move is not to demand a better prose spec but to let the system run, observe stable regularities, and then extract them into deterministic artifacts. That is [spec mining as codification](./spec-mining-as-codification.md).

This is still a specification strategy, but the substrate has changed. The "spec" is no longer mainly a prose coordination document; it becomes an executable or machine-checkable statement of the rule the system had previously been rediscovering at runtime. This is the late phase of the lifecycle: the specification is inferred from behavior rather than written ahead of it. It fits operations where the system keeps rediscovering the same rule and where [codification](./codification.md) can replace repeated interpretation with exact verification. Its failure mode is overfitting accidents into rules by extracting too early.

## A lifecycle, not a doctrine

These regimes often appear in sequence inside one project. An agent project may begin spec-first to encode business intent and acceptance criteria. As implementation touches real code, the artifact becomes bidirectional because execution discovers facts the original plan missed. After enough runs, stable parts of that evolving spec get mined into tests, helper functions, linters, or scripts. What began as prose becomes a mixed system of living documents and hardened artifacts through [deploy-time learning](./deploy-time-learning-the-missing-middle.md).

This is why the apparent dispute between "write the spec first" and "specs always rot" is shallow. Both are true in different phases. Upfront specs help when the understanding is already available; bidirectional maintenance is necessary while understanding is still being discovered; behavior extraction is right when the rule only becomes legible through repeated execution.

## Selection rule

Choose the specification strategy by asking where the missing knowledge is:

1. If the knowledge is already in the human's head and cheap to state, specify upfront.
2. If the knowledge is latent in the environment and only execution will reveal it, maintain the spec bidirectionally.
3. If the knowledge only becomes clear across many runs with observable outcomes, extract an executable or machine-checkable spec from behavior.

The strategies are cumulative, not exclusive. Mature systems can use all three, but not every system needs every phase.

## Open Questions

- What operational signals show that a spec should move from bidirectional maintenance into mined rules or code, rather than staying prose?
- How much update granularity can a bidirectional spec tolerate before it becomes noise rather than a coordination artifact?

---

Relevant Notes:

- [changing-requirements-conflate-genuine-change-with-disambiguation-failure](./changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) — grounds: distinguishes genuine change from late-discovered interpretation error, which is the main reason bidirectional specs are needed
- [constraining](./constraining.md) — mechanism: each strategy narrows interpretation space at a different time in the lifecycle
- [deploy-time-learning-is-agile-for-human-ai-systems](./deploy-time-learning-is-agile-for-human-ai-systems.md) — extends: splits prose-code co-evolution into distinct specification regimes based on where understanding sits
- [spec-mining-as-codification](./spec-mining-as-codification.md) — operationalizes: the late-phase path where stable regularities are extracted from repeated behavior
- [The Spec Is the New Code](../sources/the-spec-is-the-new-code-a-guide-to-spec-driven-development-2033303156340240481.ingest.md) — exemplifies: upfront specification when understanding is available before execution
- [What spec-driven development gets wrong](../sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md) — exemplifies: bidirectional maintenance when execution discovers reality the initial spec omitted

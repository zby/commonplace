---
description: "Among durable artifacts, spec-first, bidirectional spec, and spec mining fit different phases: when understanding is available upfront, discovered during execution, or only visible after observation"
type: note
traits: [has-external-sources]
tags: [learning-theory]
status: seedling
---

# Specification strategy should follow where understanding lives

Debates about specification strategy often collapse into one question: "Should we write the spec first?" But [Spec Driven Development](../sources/the-spec-is-the-new-code-a-guide-to-spec-driven-development-2033303156340240481.ingest.md), [bidirectional spec maintenance](../sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md), and [spec mining](./spec-mining-as-codification.md) solve different failure modes because they store disambiguation in different places — in the initial document, in a live artifact updated during execution, or in rules extracted after repeated behavior. They feel incompatible because they are choosing different storage locations for the same kind of work.

[Agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) gives the mechanism. Natural-language instructions admit multiple valid projections; any working system must collapse that space somehow. Specification strategy is therefore a policy for **when** that collapse happens and **which artifact** records it.

This note is specifically about **durable artifacts**. Interactive clarification inside a conversation is another way to narrow ambiguity, but it does not by itself produce something later sessions can inspect and inherit. The question here is narrower: once a clarification is worth preserving, where should it live?

## Spec-first is for ambiguity that can be resolved before execution

Spec-first fits cases where the relevant understanding already exists before execution. The human can state the intent, constraints, and acceptance criteria with enough fidelity that putting them into a spec reduces ambiguity for the agent. This is the setting DeAngelis targets: specify, plan, decompose, then implement.

The gain is front-loaded constraint. If the problem is mainly that the agent lacks enough context to choose among plausible implementations, a good upfront spec removes degrees of freedom before the expensive work begins.

Its failure mode is committing to projections that only execution could validate. The spec becomes a fossilized guess — it looks authoritative, but execution keeps forcing repairs. This is the pattern [changing requirements conflate genuine change with disambiguation failure](./changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) identifies: what looks like "requirements changed" is often that the upfront spec committed too early to one reading.

## Bidirectional spec is for ambiguity that is only exposed during execution

Bidirectional spec maintenance fits cases where important understanding emerges while doing the work. The human starts with intent, but the agent discovers real constraints in the codebase or environment that the initial spec did not capture. Augment's pattern keeps the spec live: discovery updates the artifact rather than invalidating it.

This changes the visibility of interpretation choices. Instead of silently repairing the plan in code, the agent writes the repair back into the shared artifact. The spec becomes the place where execution-discovered projections are surfaced and reviewed.

Its failure mode is turning the spec into an execution diary. If every local implementation detail flows back into the document, the spec loses its function as a coherence-maintaining narrative. Augment's "directional decisions" requirement is therefore the hard part: bidirectional spec works only if the system can distinguish load-bearing interpretation choices from incidental implementation chatter.

## Spec mining is for ambiguity that only becomes visible after enough observation

Behavior-extracted specification fits cases where understanding is not legible until after enough observation. Some rules only become visible through failure clusters, traces, recurring manual cleanup, or repeated observation of humans doing the task. Writing the spec first is premature because the system does not yet know what to say. [Spec mining as codification](./spec-mining-as-codification.md) is the late move: observe behavior, extract the regularity, then harden it into tests, helpers, or rules.

The key difference from bidirectional spec is temporal resolution. Bidirectional spec captures discoveries made during one evolving line of work. Spec mining captures regularities that only become convincing in aggregate — the question is not "what did we learn in this implementation?" but "what pattern is stable enough that it deserves a deterministic artifact?"

Its failure mode is overfitting accidents. Mining too early codifies a local workaround as if it were a general rule. The [relaxing-signals note](./operational-signals-that-a-component-is-a-relaxing-candidate.md) exists because many mined specs are really temporary vision features rather than stable calculators.

## The disagreement is usually a phase error

These strategies look like competing ideologies only if you assume a system should stay in one mode. In practice, a single component can move through all three:

1. Start with a spec-first sketch to bound ambiguity.
2. Switch to bidirectional maintenance as execution discovers mismatches.
3. Promote recurring discoveries into extracted rules once the pattern is stable.

This is why [deploy-time learning is agile for human-AI systems](./deploy-time-learning-is-agile-for-human-ai-systems.md) needs a finer breakdown than "prose and code co-evolve." Co-evolution is real, but the right prose strategy depends on when the system can say something trustworthy.

The strongest version of the claim: **move the disambiguation burden to the earliest artifact that can carry it truthfully.**

Here "truthfully" means the artifact should not pretend the knowledge is firmer, earlier-available, or more general than it really is. An upfront spec should contain what is genuinely known before execution. A live spec should record what execution actually surfaced. A mined rule should only claim regularity once observation supports it.

- If the truth is already knowable, put it in the upfront spec.
- If the truth emerges through contact with the codebase, keep the spec live during execution.
- If the truth only appears through accumulated observation, mine it afterward into a harder artifact.

## What this predicts

The framework predicts both advocacy patterns and failure patterns. Each strategy looks right in its zone: spec-first where intent is already clear and the main problem is instruction ambiguity; bidirectional spec where the environment keeps surprising the initial plan and silent projection is the main risk; spec mining where stable rules only appear after observing many executions.

The corresponding pathologies:

- Teams using spec-first too long will complain that specs "keep going stale."
- Teams using bidirectional specs too long will complain that the spec is noisy and expensive to review.
- Teams mining specs too early will accumulate brittle rules that later need relaxing.

The three-step sequence above is a common maturation path, not a law. Some systems stop at spec-first because the work is bounded and already understood. Some remain in the bidirectional regime because the environment keeps shifting and no stable rule surface emerges. Some patterns jump directly to mining because the only useful regularities are visible in aggregate. The mistake is treating one successful phase strategy as a universal methodology rather than a response to a particular location of missing knowledge.

---

Relevant Notes:

- [deploy-time-learning-is-agile-for-human-ai-systems](./deploy-time-learning-is-agile-for-human-ai-systems.md) — extends: splits "co-evolving prose and code" into distinct lifecycle strategies depending on where the understanding sits
- [changing-requirements-conflate-genuine-change-with-disambiguation-failure](./changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) — grounds: late-discovered "requirement changes" often indicate that understanding was not actually available upfront
- [spec-mining-as-codification](./spec-mining-as-codification.md) — situates: this is the late-phase strategy for rules that only become visible after repeated execution
- [The Spec Is the New Code — A Guide to Spec Driven Development](../sources/the-spec-is-the-new-code-a-guide-to-spec-driven-development-2033303156340240481.ingest.md) — source: grounds the spec-first end of the strategy space and the maturity model from Spec-First to Spec-as-Source
- [What spec-driven development gets wrong](../sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md) — source: grounds the bidirectional-spec critique that upfront specs decay unless execution keeps updating them

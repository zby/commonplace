---
description: AI labs' continuous learning — adapting deployed models without retraining — is achievable through stabilisation with versioned artifacts, which beats weight updates on inspectability, rollback, verification, and composability.
type: structured-claim
traits: []
areas: [learning-theory]
status: current
---

# Continuous learning is stabilisation during deployment

AI labs frame "continuous learning" as a weight-update problem: how do you adapt a deployed model to new data, new tasks, and shifting distributions without a full retraining cycle? The standard approaches — fine-tuning on deployment logs, online learning, experience replay — all modify the model's parameters.

[Stabilisation](agentic-systems-learn-through-three-distinct-mechanisms.md) achieves the same goals through a different mechanism: versioned repo artifacts — prompts, schemas, evals, tools, and deterministic code — that accumulate and improve during deployment. Each artifact is a stabilisation step that [trades generality for compound gains in reliability, speed, and cost](learning-is-capacity-change.md). When this happens continuously during deployment, it's continuous learning — just not through weights.

## Evidence

### Artifacts beat weights

The compound gain — reliability, speed, cost — explains why repo artifacts outperform weight updates for the learning they both target:

| Property | Weight updates | Repo artifacts |
|----------|---------------|----------------|
| **Inspectability** | Opaque — no one can read what was learned | Diffable — every change is a readable commit |
| **Catastrophic forgetting** | Major unsolved problem — new learning degrades old capabilities | Non-issue — adding a new tool doesn't break existing ones |
| **Rollback** | Expensive and lossy — requires checkpointing infrastructure | Trivial — `git revert` |
| **Verification** | Statistical at best — measure overall benchmark scores | Precise — individual evals, unit tests, CI gates |
| **Deployment** | Requires serving infrastructure changes | Standard deployment — prompts and code ship like any other artifact |
| **Composability** | Monolithic — all knowledge is entangled in a single weight matrix | Modular — each artifact is independent and can be tested in isolation |

The Karpathy verifiability framing sharpens this: a task is verifiable to the extent it is **resettable** (you can retry), **efficient** (retries are cheap), and **rewardable** (you can evaluate automatically). Repo artifacts score higher on all three dimensions than weight updates.

### Fine-tuning

Fine-tuning is the most direct form of weight-based continuous learning: take deployment data, update the model. It works, but it's expensive (compute), risky (forgetting), opaque (what did the model learn?), and coarse (the whole model changes when you wanted to improve one behavior).

Stabilisation achieves the same narrowing of the behavior distribution through external artifacts. Instead of fine-tuning a model to format dates consistently, you extract a deterministic `format_date()` function. Instead of fine-tuning for a house style, you version the system prompt with examples. The effect on system behavior is equivalent; the mechanism is inspectable.

### RAG

Traditional RAG — a single retrieve-then-answer step — is largely obsolete. What people actually build now is agentic RAG: retrieval inside an agentic loop, where the agent decides what to search for, evaluates what it finds, and searches again if needed.

Agentic RAG fits naturally inside the stabilisation framework. The repo itself is the knowledge base: documents, schemas, examples, prior decisions — all versioned, all improving over time. The agent searches them as part of its work loop, and the artifacts it retrieves are the same ones that stabilisation continuously refines. The difference from a traditional vector store is that these artifacts are structured, testable, and subject to the same versioning and review as code.

### Automated prompt optimization

Systems like DSPy and ProTeGi search over prompt components to optimize against an objective. This is an automated instance of stabilisation: the artifacts are prompts, the optimization is iterative, the improvement persists. What these systems lack is the broader framework: the [verifiability gradient](deploy-time-learning-the-missing-middle.md), the progression from optimized prompts to schemas to deterministic code, and the infrastructure for versioning, testing, and reviewing what was learned.

Stabilisation provides that framework. DSPy discovers better prompts; stabilisation provides the infrastructure to harden those discoveries into progressively more verifiable forms, track them in version control, and test them in CI. The [adaptation taxonomy for agentic AI](research/adaptation-agentic-ai-analysis.md) identifies concrete data-driven triggers for when to stabilise versus when to soften, providing the feedback signals. The combination is the full picture: automated search for what works, systematic infrastructure for preserving what was found.

## Reasoning

### What deployed systems actually need

Calling stabilisation "continuous learning" is not just terminological. It reframes what deployed AI systems need:

1. **Infrastructure investment shifts.** Instead of building online learning pipelines, invest in eval frameworks, prompt versioning, and CI for AI artifacts. These are mature, well-understood tools.

2. **Systematised out-of-band optimisation.** Every deployed LLM system accumulates informal tweaks — prompt adjustments, output post-processing, workflow changes — that improve behavior but live outside the model. These are learning, but ad-hoc learning: undocumented, untested, unreproducible. Stabilisation systematises this. The loop can be human-driven (reviewing diffs, approving changes) or automated (search over prompt components, eval-driven iteration). Research on [professional developers using AI agents](related_works/professional-developers-ai-agents.md) confirms the human-driven variant empirically.

3. **Verifiability as the metric.** Instead of asking "how do we keep the model learning?", ask "how verifiable is each piece of our system?" and push toward more verifiable forms.

## Caveats

- **Not all continuous learning is stabilisation.** Weight-based learning captures distributional knowledge (style, tone, world knowledge) that doesn't reduce to explicit artifacts. Stabilisation handles the extractable, testable subset — but that subset covers most of what deployed systems need.
- **Stabilisation requires curation.** Artifacts don't maintain themselves. The process assumes an active curation loop.

---

Relevant Notes:
- [stabilisation-is-learning](agentic-systems-learn-through-three-distinct-mechanisms.md) — foundation: the general claim that stabilisation is learning; this note applies it to the specific hot topic of continuous learning during deployment
- [learning-is-capacity-change](learning-is-capacity-change.md) — foundation: capacity decomposes into generality vs reliability+speed+cost compound
- [deploy-time-learning](deploy-time-learning-the-missing-middle.md) — the verifiability gradient that structures the progression from prompts to code
- [adaptation-agentic-ai-analysis](research/adaptation-agentic-ai-analysis.md) — provides data-driven triggers for when to stabilise vs soften, grounding the loop in concrete signals
- [professional-developers-ai-agents](related_works/professional-developers-ai-agents.md) — empirical evidence that developers naturally practice the stabilisation loop
- [oracle-strength-spectrum](oracle-strength-spectrum.md) — the Karpathy verifiability properties map to oracle strength
- [python-agent-annotation-brainstorm](python-agent-annotation-brainstorm.md) — practical mechanisms for moving between LLM workers and deterministic code

Topics:
- [learning-theory](./learning-theory.md)

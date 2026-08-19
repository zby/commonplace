---
description: Retaining evaluated changes to behavior-shaping prompts, rules, tools, and tests gives deployed systems a persistent adaptation path outside model-weight updates
type: kb/types/note.md
traits: [has-comparison, title-as-claim]
tags: [learning-theory, deploy-time-learning]
---

# Retained system-definition artifacts enable persistent deployment-time adaptation

[Continual learning requires governing behaviour-changing writes, not just storing content](./continual-learning-requires-governing-behaviour-changing-writes.md) argues that deployed systems need durable behavior changes installed within their operating feedback loops. These changes need not wait for another model-weight training cycle. During deployment, a system can evaluate and retain changes to [system-definition artifacts](./definitions/system-definition-artifact.md)—prompts, rules, tools, schemas, tests, and configuration that it consumes with binding force.

This is a distinct adaptation path because the selected change affects later sessions without becoming part of the model's weights. This note calls that path **deployment-time adaptation**. The process counts as learning when deployment experience drives a proposal, evaluation selects it, and retention allows it to change later behavior.

## Lifecycle phase is not update speed

Five properties must remain separate:

- **Lifecycle phase:** Whether the change is produced before or during deployment.
- **Update latency:** How long proposal, evaluation, and safe installation take.
- **Persistence:** Whether the selected change survives the run that produced it.
- **Update mechanism:** Weight training, context assembly, artifact revision, or another process.
- **[Representational form](./definitions/representational-form.md):** Whether the retained change lives in distributed model weights, natural language, symbolic code, or a mixture.

Common adaptation paths combine these properties in different ways, but they do not form exclusive timescale categories. Offline weight training is usually durable and occurs before deployment, yet online training can update weights during deployment. Live context changes behavior within a session, but context alone does not write changes into later sessions. Summaries or saved state persist only because another retention path stores them. A system-definition edit can be produced within one session and retained for later ones. When an evidence-responsive selection loop completes this artifact-revision path within the deployed system's operating cadence, the result is persistent deployment-time adaptation. “During deployment” locates the change in the lifecycle; it does not by itself make the change fast.

## Why localized artifacts are practical now

Localized, versioned artifacts can make a deployment-time change inspectable, diffable, selectively revisable, and rollbackable. This advantage is conditional rather than intrinsic. A global natural-language policy can have an open-ended behavioral surface, while a routed parameter adapter can be tightly confined. Validation becomes more tractable only when the artifact's actual authority and dependency neighborhood bound the consequences that must be checked, as developed by [the readable-artifact loop](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md).

Timing and form are therefore orthogonal. Parametric methods can also update during deployment: [OpenClaw-RL](../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md) is an existing case of live reinforcement learning, not merely a future falsifier. Readable artifacts are useful where their explicit operational boundaries make evaluation and rollback cheaper; they do not exclusively occupy the deployment-time category.

Artifact libraries can also accumulate more behavior-shaping state than a single call can hold. Progressive disclosure, skill routing, and retrieval [economize each bounded context](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) by selecting relevant artifacts across executions. This expands what the deployed system can retain and activate over time without enlarging any individual context window or claiming parity with the breadth of a weight update.

## Why this is system learning

Herbert Simon's capacity-change criterion, stated in [learning is not only about generality](./learning-is-not-only-about-generality.md), treats a more or less permanent change in a system's capacity to adapt as learning. The relevant unit is [the deployed system, not the model alone](./the-deployed-system-not-the-model-is-the-unit-of-learning.md), because prompts, retrieval, tools, validators, and runtime policy jointly determine behavior.

Persistence alone is insufficient. A manually edited configuration remains an engineering input unless an evidence-responsive process evaluates and incorporates it. [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md); these operations distinguish learning from arbitrary durable maintenance. A human may still propose or approve the selected change. What matters is that deployment evidence bears on its selection and that the retained result affects later executions.

## Forms can coevolve

Deployment-time adaptation does not privilege natural language or code. [Constraining during deployment is continuous learning](./constraining-during-deployment-is-continuous-learning.md) develops one concrete path in which prompts, schemas, tools, tests, and code accumulate adaptive capacity. Settled interpretations can move toward symbolic enforcement, while new evidence can reopen a commitment for model judgment. The allocation of state among natural-language, symbolic, and distributed-parametric forms may therefore change while the timing and persistence of the learning loop remain the same. How those forms should divide responsibility is the separate argument in [treat continual learning as representational-form coevolution](./treat-continual-learning-as-representational-form-coevolution.md).

## Boundary

The claim is that a persistent deployment-time adaptation path exists outside model-weight updates—not that it is a third exhaustive timescale, always faster than training, or exclusive to readable artifacts. Its practical advantage depends on evidence-responsive selection and a validation surface whose consequences are actually bounded.

---

Relevant Notes:

- [Continual learning requires governing behaviour-changing writes, not just storing content](./continual-learning-requires-governing-behaviour-changing-writes.md) — grounds: supplies the durable behavior-change objective whose lifecycle consequence this note develops
- [Learning is not only about generality](./learning-is-not-only-about-generality.md) — grounds: supplies Herbert Simon's capacity-change criterion
- [The deployed system, not the model alone, is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md) — grounds: identifies the behavior-producing system as the learning boundary
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — mechanism: distinguishes selected learning from arbitrary persistent maintenance
- [Only explicit retention is currently durable, writable, and addressable at once](./only-explicit-retention-is-durable-writable-and-addressable.md) — extends: adds addressability and governance to the persistence comparison
- [OpenClaw-RL ingest](../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md) — evidenced-by: demonstrates that model weights can also update during deployment and exposes the remaining validation and rollback tradeoffs
- [Machine Studying](../sources/machine-studying.ingest.md) — evidenced-by: in preliminary small-scale runs, a corpus-derived note was the only studying intervention that raised agent expertise, beating continual pre-training and synthetic fine-tuning on one of two domains — bounded external support for the readable-artifact path

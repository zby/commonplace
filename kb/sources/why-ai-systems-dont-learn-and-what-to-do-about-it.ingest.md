---
description: Position paper arguing current AI externalizes learning into human-run MLOps and proposing an A-B-M architecture where meta-control arbitrates observation and action learning for lifelong adaptation.
source_snapshot: why-ai-systems-dont-learn-and-what-to-do-about-it.md
ingested: 2026-03-18
type: conceptual-essay
domains: [autonomous-learning, continuous-learning, cognitive-architecture, meta-control]
---

# Ingest: Why AI systems don't learn and what to do about it

Source: why-ai-systems-dont-learn-and-what-to-do-about-it.md
Captured: 2026-03-18
From: https://arxiv.org/html/2603.15381v1

## Classification

Type: conceptual-essay — arXiv position paper with an architectural proposal but no implemented system or empirical evaluation.
Domains: autonomous-learning, continuous-learning, cognitive-architecture, meta-control
Authors: Emmanuel Dupoux, Yann LeCun, Jitendra Malik — cognitive science, frontier representation learning, and computer vision converging on the same architectural diagnosis. Strong signal for a framing paper even without validation.

## Summary

The paper argues that current AI systems do not truly learn after deployment because adaptation has been externalized into a human-operated MLOps loop. Its proposed remedy is a three-part architecture: System A learns from observation, System B learns from action, and System M acts as a meta-control plane that selects inputs, modulates objectives, switches modes, and routes information between learning subsystems and memory. The main contribution is not a new algorithm but a reframing: autonomous learning is an architectural problem about integrating observation, action, and meta-signals into one adaptive system, with an outer evolutionary-developmental loop needed to bootstrap the whole stack.

## Connections Found

Five genuine note connections, all in the KB's learning-theory cluster, plus one recurring tension in the control-plane vocabulary.

- **Partial contradiction with [deploy-time-learning-the-missing-middle](../notes/deploy-time-learning-the-missing-middle.md).** The paper says current AI does not learn after deployment; the KB note says deployed systems already learn through durable artifacts even when weights stay fixed. This is the strongest link — the disagreement is productive.

- **[constraining-during-deployment-is-continuous-learning](../notes/constraining-during-deployment-is-continuous-learning.md) narrows the disagreement** by redefining learning from "weight update" to "durable capacity change." Under that definition, the paper's claim softens considerably.

- **[in-context-learning-presupposes-context-engineering](../notes/in-context-learning-presupposes-context-engineering.md) provides the closest present-day analogue to System M:** a meta-layer that decides what to route, load, and maintain before inference can do useful work.

- **[llm-learning-phases-fall-between-human-learning-modes](../notes/llm-learning-phases-fall-between-human-learning-modes.md) creates a methodological tension,** warning that the paper's cognitive-science analogies are suggestive but not structurally reliable.

- **[automating-kb-learning-is-an-open-problem](../notes/automating-kb-learning-is-an-open-problem.md) sharpens why the paper remains conceptual:** the hard part is not naming a meta-control layer but manufacturing oracles for the learning operations it would need to automate.

## Extractable Value

1. **Meta-control as a first-class architectural primitive.** The high-reach contribution is not "combine more learning methods" but "separate the arbitration layer from the learning layers." That abstraction transfers beyond this paper: routing, objective shaping, mode switching, and memory gating may be one family of problems rather than four unrelated ones. [experiment]

2. **"AI systems don't learn" is substrate-relative.** The paper is most useful when read against the KB's deploy-time-learning notes: its diagnosis is true if the system boundary stops at model weights, false if the boundary includes artifacts. That boundary distinction is clearer and more transferable than the paper's raw claim. [quick-win]

3. **The observation/action bootstrap knot is real and general.** System A needs grounded data from action; System B needs structured representations from observation. That circular dependency is a reusable lens for evaluating learning proposals: if each subsystem presupposes the other, the real design problem is the outer loop that seeds both. [deep-dive]

4. **Meta-signals are candidate routing signals, not just biological decoration.** Uncertainty, novelty, prediction error, trust, and other low-bandwidth signals are presented as control inputs for System M. Even if the biological analogies are too loose, the design pattern transfers: maintenance and routing systems need compact signals that decide when to switch modes or escalate. [experiment]

5. **The simpler account is stronger than the grand one.** Strip the biological framing and the paper's strongest claim reduces to: current AI lacks integrated control over data selection, objective shaping, and cross-subsystem routing. That version is easier to vary, easier to test, and more useful for engineering than "AI systems lack autonomous learning." [quick-win]

6. **Current systems likely implement fragments already.** Context-engineering tools, RL training systems like [OpenClaw-RL](./openclaw-rl-train-any-agent-simply-by-talking.ingest.md), and trace-mining pipelines each cover part of the paper's architecture. The paper's value here is unification vocabulary, not evidence that the integrated design works. [just-a-reference]

## Limitations (our opinion)

The paper draws the system boundary too tightly — at model weights — and overstates its novelty as a result. Versioned prompts, tools, schemas, evals, and routing artifacts already form a learning substrate outside the model. [deploy-time-learning-the-missing-middle](../notes/deploy-time-learning-the-missing-middle.md) and [constraining-during-deployment-is-continuous-learning](../notes/constraining-during-deployment-is-continuous-learning.md) name this substrate directly. The paper's model-level diagnosis still holds, but its title claim — "AI systems don't learn" — is too strong if read at the whole-system level.

The cognitive-science framing does rhetorical rather than explanatory work. [llm-learning-phases-fall-between-human-learning-modes](../notes/llm-learning-phases-fall-between-human-learning-modes.md) makes the relevant objection: human and animal learning modes do not map cleanly onto LLM phases, so analogies to development, somatic signals, or child learning can illuminate possibilities without licensing structural inference. The paper's strongest claims survive after removing the biological framing — systems need a control layer for routing information and objectives — which suggests the analogy is ornamental.

System M is under-specified enough to risk unfalsifiability. It must select inputs, modulate rewards, switch between learning and inference, manage memory, and coordinate Systems A and B — but the paper does not say what signals make these choices correct, how those signals are learned, or what failure would look like. [automating-kb-learning-is-an-open-problem](../notes/automating-kb-learning-is-an-open-problem.md) is the relevant note: naming a control plane is much easier than building the oracle that tells it what to do.

The paper also omits comparison against partial implementations. It does not engage artifact-based deploy-time learning, live RL systems like [OpenClaw-RL](./openclaw-rl-train-any-agent-simply-by-talking.ingest.md), or trace-derived memory systems that already learn from experience on narrower substrates. Without those comparisons, the paper cannot tell us whether its integrated architecture is necessary — only that it would be desirable if it worked.

## Recommended Next Action

Write a note titled "Autonomous learning is substrate-relative" connecting to [deploy-time-learning-the-missing-middle](../notes/deploy-time-learning-the-missing-middle.md), [constraining-during-deployment-is-continuous-learning](../notes/constraining-during-deployment-is-continuous-learning.md), and [llm-learning-phases-fall-between-human-learning-modes](../notes/llm-learning-phases-fall-between-human-learning-modes.md). It would argue that claims like "AI systems do not learn" are only true when the system boundary is drawn at model weights; once artifacts and routing layers are included, current systems already exhibit partial autonomous learning, and the real missing piece is integrated meta-control across multiple adaptive substrates.

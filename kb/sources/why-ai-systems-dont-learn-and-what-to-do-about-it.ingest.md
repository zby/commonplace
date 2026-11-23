---
description: Position paper arguing current AI externalizes learning into human-run MLOps and proposing an A-B-M architecture where meta-control arbitrates observation and action learning for lifelong adaptation.
source: https://arxiv.org/html/2603.15381v1
captured: "2026-03-18"
capture: web-fetch
genre: conceptual-essay
snapshot_sha256: 223632eff5364818cda452976cc9b3164489d6673e606dc881e6b1d5484b3fd5
ingested: "2026-03-18"
type: types/ingest-report.md
domains: [autonomous-learning, continuous-learning, cognitive-architecture, meta-control]
---

# Ingest: Why AI systems don't learn and what to do about it

## Classification

ArXiv position paper with an architectural proposal but no implemented system or empirical evaluation.
Authors: Emmanuel Dupoux, Yann LeCun, Jitendra Malik — cognitive science, frontier representation learning, and computer vision converging on the same architectural diagnosis. Strong signal for a framing paper even without validation.

## Summary

The paper argues that current AI systems do not truly learn after deployment because adaptation has been externalized into a human-operated MLOps loop. Its proposed remedy is a three-part architecture: System A learns from observation, System B learns from action, and System M acts as a meta-control plane that selects inputs, modulates objectives, switches modes, and routes information between learning subsystems and memory. The main contribution is not a new algorithm but a reframing: autonomous learning is an architectural problem about integrating observation, action, and meta-signals into one adaptive system, with an outer evolutionary-developmental loop needed to bootstrap the whole stack.

## Quotes

> The paper argues that observation and action learning should not remain separate paradigms.
> --- `kb/sources/.snapshots/why-ai-systems-dont-learn-and-what-to-do-about-it.md` @ `sha256:223632eff5364818cda452976cc9b3164489d6673e606dc881e6b1d5484b3fd5` — “Interaction Between Systems” section, opening sentence.

> System A can help System B by compressing state spaces, building predictive world models, and generating intrinsic rewards for exploration.
> --- `kb/sources/.snapshots/why-ai-systems-dont-learn-and-what-to-do-about-it.md` @ `sha256:223632eff5364818cda452976cc9b3164489d6673e606dc881e6b1d5484b3fd5` — “Interaction Between Systems” section.

> System B can help System A by collecting better data, disambiguating perception through intervention, and generating task-relevant trajectories rather than passive, uncurated streams. System M sits above both, deciding when and how these interactions should occur.
> --- `kb/sources/.snapshots/why-ai-systems-dont-learn-and-what-to-do-about-it.md` @ `sha256:223632eff5364818cda452976cc9b3164489d6673e606dc881e6b1d5484b3fd5` — “Interaction Between Systems” section, closing sentences.

## Connections Found

Five genuine note connections, all in the KB's learning-theory cluster, plus one recurring tension in the control-plane vocabulary.

- **Contrast with [Deployed systems can learn from feedback with fixed model weights](../theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md).** A system can retain useful changes without updating weights. That does not settle the paper’s objection that people, rather than the system, make the update decisions.

- [Constraining during deployment can produce learning outside weights](../theory/constraining-during-deployment-can-produce-learning-outside-weights.md) narrows the disagreement: a revised rule can improve later work. Whether the system selected the rule itself is a separate question.

- **[in-context-learning-presupposes-context-engineering](../theory/in-context-learning-presupposes-context-engineering.md) provides the closest present-day analogue to System M:** a meta-layer that decides what to route, load, and maintain before inference can do useful work.

- **[llm-learning-phases-fall-between-human-learning-modes](../theory/llm-learning-phases-fall-between-human-learning-modes.md) creates a methodological tension,** warning that the paper's cognitive-science analogies are suggestive but not structurally reliable.

- **[automating-kb-learning-is-an-open-problem](../theory/automating-kb-learning-is-an-open-problem.md) sharpens why the paper remains conceptual:** the hard part is not naming a meta-control layer but manufacturing oracles for the learning operations it would need to automate.

## Extractable Value

1. **Meta-control as a first-class architectural primitive.** The high-reach contribution is not "combine more learning methods" but "separate the arbitration layer from the learning layers." That abstraction transfers beyond this paper: routing, objective shaping, mode switching, and memory gating may be one family of problems rather than four unrelated ones. [experiment]

2. **Separate what changes from who selects the change.** Looking only at weights can miss a revision to a rule that later runs use. Counting that revision does not make a human-operated update loop autonomous. [quick-win]

3. **The observation/action bootstrap knot is real and general.** System A needs grounded data from action; System B needs structured representations from observation. That circular dependency is a reusable lens for evaluating learning proposals: if each subsystem presupposes the other, the real design problem is the outer loop that seeds both. [deep-dive]

4. **Meta-signals are candidate routing signals, not just biological decoration.** Uncertainty, novelty, prediction error, trust, and other low-bandwidth signals are presented as control inputs for System M. Even if the biological analogies are too loose, the design pattern transfers: maintenance and routing systems need compact signals that decide when to switch modes or escalate. [experiment]

5. **The simpler account is stronger than the grand one.** Strip the biological framing and the paper's strongest claim reduces to: current AI lacks integrated control over data selection, objective shaping, and cross-subsystem routing. That version is easier to vary, easier to test, and more useful for engineering than "AI systems lack autonomous learning." [quick-win]

6. **Current systems likely implement fragments already.** Context-engineering tools, RL training systems like [OpenClaw-RL](./openclaw-rl-train-any-agent-simply-by-talking.ingest.md), and trace-mining pipelines each cover part of the paper's architecture. The paper's value here is unification vocabulary, not evidence that the integrated design works. [just-a-reference]

## Limitations (our opinion)

A versioned prompt, test, or routing rule gives a deployed system somewhere other than the weights to retain a change. [Deployed systems can learn from feedback with fixed model weights](../theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md) and [Constraining during deployment can produce learning outside weights](../theory/constraining-during-deployment-can-produce-learning-outside-weights.md) explain when that change can improve later work. These cases qualify a broad claim about the absence of learning, but do not by themselves answer the paper’s narrower claim about autonomous learning.

The cognitive-science framing does rhetorical rather than explanatory work. [llm-learning-phases-fall-between-human-learning-modes](../theory/llm-learning-phases-fall-between-human-learning-modes.md) makes the relevant objection: human and animal learning modes do not map cleanly onto LLM phases, so analogies to development, somatic signals, or child learning can illuminate possibilities without licensing structural inference. The paper's strongest claims survive after removing the biological framing — systems need a control layer for routing information and objectives — which suggests the analogy is ornamental.

System M is under-specified enough to risk unfalsifiability. It must select inputs, modulate rewards, switch between learning and inference, manage memory, and coordinate Systems A and B — but the paper does not say what signals make these choices correct, how those signals are learned, or what failure would look like. [automating-kb-learning-is-an-open-problem](../theory/automating-kb-learning-is-an-open-problem.md) is the relevant note: naming a control plane is much easier than building the oracle that tells it what to do.

The paper also omits comparison against partial implementations. It does not engage systems that revise their own instructions after use, live RL systems like [OpenClaw-RL](./openclaw-rl-train-any-agent-simply-by-talking.ingest.md), or trace-learning systems that already learn from experience on narrower substrates. Without those comparisons, the paper cannot tell us whether its integrated architecture is necessary — only that it would be desirable if it worked.

## Recommended Next Action

Compare [Deployed systems can learn from feedback with fixed model weights](../theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md), [Constraining during deployment can produce learning outside weights](../theory/constraining-during-deployment-can-produce-learning-outside-weights.md), and [the comparison of human and LLM learning](../theory/llm-learning-phases-fall-between-human-learning-modes.md). Ask two questions of each example: what change carries over to the next task, and who decided to keep it? Only the second question addresses autonomy.

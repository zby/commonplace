---
description: Fixed and merely runtime-responsive memory rules need no training oracle; outcome-driven updates do, while noisy rankings weaken learning and misaligned ones teach the wrong ordering
type: kb/types/note.md
traits: [has-external-sources, title-as-claim]
tags: [learning-theory, agent-memory]
---

# Feedback-trained memory management is oracle-dependent even when its operations are hand-designed

A policy learned from outcome feedback can improve its choices only when training can rank the downstream value of those choices. This evaluative signal—an **oracle** in this note—need not be a binary ground-truth checker. It may combine tests, human or language-model judgments, delayed outcomes, and proxy scores. It must, however, discriminate between choices worth reinforcing and choices worth suppressing. Without that correlation, policy updates carry no information about which earlier choices helped. Signal quality therefore bounds effective feedback-trained adaptation: indistinguishable outcomes provide no direction, noisy rankings weaken it, and systematically misaligned rankings teach the wrong ordering.

Memory management is the worked application. A memory-management policy selects when to store, retrieve, summarize, update, or delete information. The claim is about feedback-trained policy adaptation, not policies in general. An explicit memory rule such as “delete entries after thirty days” can run without a training oracle. A fixed rule can also respond to the current query, usage count, or available budget while its parameters remain unchanged. The oracle requirement begins when outcomes are used to update the policy itself.

## Why the dependency is structural

Outcome feedback affects later policy decisions only through distinctions encoded in the signal. If two choices with different downstream value receive indistinguishable feedback, training cannot prefer the more valuable choice; if the signal reverses their ranking, it reinforces the worse choice. Memory management makes this dependency visible because memory choices often precede their consequences. A retrieval may enable an answer several steps later; storing an observation may matter only in a future interaction; deleting an entry may prevent a later distraction. To improve such choices from experience, a learning procedure must connect later consequences to earlier operations. Direct task scores, preference labels, user corrections, and learned judges provide different versions of that connection.

Signal availability is necessary but not sufficient. A reliable score cannot compensate for an inadequate operation set, unrepresentative training data, or an ineffective learning procedure. Nor does the existence of a feedback-trained system show that its oracle was the sole cause of success. Establishing that the signal is the dominant bottleneck would require varying its quality while holding the operations, data, and learning procedure stable.

## Evidence from different memory policies

One example is AgeMem, a feedback-trained agent-memory system described in the [AgeMem paper snapshot](../sources/agentic-memory-learning-unified-long-term-and-short-term-memory.md). It exposes six hand-designed operations over retained memory and active context, then uses reinforcement learning—training from rewards—to learn when to invoke them. Its reward is composite rather than a clear binary task-completion check: the paper reports task-performance, context-management, memory-management, semantic-relevance, and penalty components, with language-model judgment used for some evaluation. The reported 8.53–8.72 percentage-point contribution from the training strategy shows that a feedback-trained policy can improve memory use in the evaluated tasks. It does not isolate reward quality from the model, data, staged training, or operation design.

[AgentFly, a code-inspected case-memory agent](../agent-memory-systems/reviews/AgentFly.md), supplies an independent example. Its optional trained ranking model decides which stored question-and-plan examples to retrieve for a new query. Training rows label candidate examples using the judged success of the downstream answer; the implementation obtains that judgment by comparing the answer with ground truth through a language-model judge. AgeMem learns when to invoke memory operations, whereas AgentFly learns which memory to read back, but both updates need a signal that distinguishes helpful decisions from unhelpful ones.

These cases corroborate the mechanism; they are not its premise. The argument still holds if either system is removed: learning from outcomes requires some channel by which outcomes direct later policy updates.

## Boundaries

Inspectability and feedback dependence are independent axes. A readable decision tree whose thresholds are updated from task outcomes is inspectable, adaptive, and oracle-dependent. An opaque fixed heuristic can be uninspectable without learning from outcomes or needing a training oracle. Runtime responsiveness is also distinct from learning: a hand-written relevance rule may produce different choices as recency, usage, and query alignment change even though the rule itself never updates.

The oracle may be weak, delayed, composite, or partly learned. Those forms satisfy the dependency only to the extent that they remain correlated with the downstream objective. A poor proxy can teach the wrong policy; a language-model judge can import its own errors; delayed feedback makes it harder to connect outcomes to individual operations. “Requires an oracle” therefore does not mean “requires perfect verification.”

For KB curation, a policy that learns which links or summaries will help future questions likewise needs feedback correlated with that future value. Structural validation supplies signals about artifact form, while human review, user corrections, and retrieval outcomes may supply partial signals about usefulness. As [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) explains, no current signal has been shown to evaluate those judgment-heavy mutations reliably enough for a closed learning loop. The missing evaluator is therefore one necessary bottleneck, not evidence that the learning mechanism is the only other variable.

---

Relevant Notes:

- [Oracle strength spectrum](./oracle-strength-spectrum.md) — extends: distinguishes hard, soft, interactive, and delayed forms of the evaluative signal required here
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — exemplifies: learned memory-policy automation is one case where the ability to update safely is bounded by the ability to evaluate outcomes

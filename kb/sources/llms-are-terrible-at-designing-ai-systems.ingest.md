---
description: "Goedecke reports agents choosing symbolic machinery for semantic tasks; useful as an allocation and knowledge-use warning, not proof of a training cause."
source: https://www.seangoedecke.com/llms-are-terrible-at-designing-ai-systems/
captured: "2026-11-08"
capture: trafilatura
capture_scope: full-source
genre: conceptual-essay
snapshot_sha256: f52b7368087e53707eeaa25230689b3d9efc0d8a34c4196bb67933f3cd9c1da1
ingested: "2026-11-08"
type: types/ingest-report.md
domains: [semantic-contradiction-detection, agent-software-design, RLVR]
learning_claims: true
---

# Ingest: LLMs are terrible at designing AI systems

## Classification

A conceptual essay built around practitioner anecdotes and competing causal explanations, rather than a systematic evaluation. Author: Sean Goedecke, who reports encountering similar tool-selection failures while building Autodeck. The central memory-tool episode is his account of another author's experience, not an inspected execution trace.

## Summary

Goedecke argues that coding agents can implement sophisticated machinery while choosing an unsuitable approach to the problem. His central example is an agent reportedly building a natural-language-to-logical-atoms pipeline and solver for memory contradiction detection instead of using model judgments; his own example concerns regex or keyword classification of generated cards. He proposes three explanations: predominantly pre-LLM training code, reinforcement learning with verifiable rewards (RLVR) in environments lacking model API access, and general software-design weakness. He doubts the first explanation is sufficient and favors the third, while treating the RLVR account as speculation. The operational warning is that implementation ability does not establish design judgment: an agent reportedly explained the flaw when challenged after pursuing the approach for weeks. Neither the frequency of this failure nor the reliability of the proposed model-based replacement is measured.

## Quotes

No source quotes have been retained yet.

## Connections Found

The essay is a practitioner illustration for [Codify-versus-LLM decision heuristics](../theory/codify-versus-llm-decision-heuristics.md): choosing an executable formalization does not establish that its rules capture the semantic objective. Its contribution is a memorable failure case, not a demonstrated cost or accuracy advantage for model calls. It also supplies anecdotal evidence relevant to [Knowledge storage does not imply contextual activation](../theory/knowledge-storage-does-not-imply-contextual-activation.md): the reported agent could explain a design objection after prompting but had not used it to reject the design. The account does not show that the objection was present in the earlier context or establish why it failed to guide work. These existing notes already cover the transferable allocation and knowledge-use mechanisms; the essay does not warrant another general theory note.

## Learning Claims (our opinion)

The learning mechanism proposed by the essay is training-induced tool preference. Historical code could favor conventional programs, while RLVR—training with automatically checkable rewards—could discourage code that needs unavailable model credentials or network access. These are conjectures about how training shapes behavior, not inspected training arrangements or demonstrated adaptation. In Commonplace terms, they concern learned dispositions rather than a [theory builder](../theory/definitions/theory-builder.md) whose stated explanations are criticized and retained. If API calls cannot be executed or rewarded during training, that could restrict which designs training can favor; however, the essay does not establish their exclusion or whether other available operations could implement them. The boundary in [Learning inside a fixed decomposition inherits its mistakes](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) is therefore a possible diagnostic, not an established explanation of these failures.

The user-agent design episode offers a separate, partial mapping onto the four theory-builder conditions. **Localized content:** the reported implementation identifies a concrete design, but its design rationale is not retained here. **Consumption:** continued implementation suggests that design guided work, without a content-change test. **Criticism:** the prompted explanation reportedly challenged the approach, providing anecdotal evidence of an explicit objection. **Iteration:** the essay does not document a replacement design taking up that criticism. It therefore does not establish the complete cycle, persistence of the lesson into later work, or improved future performance. The episode illustrates a possible gap between eliciting criticism and using it; it does not show that the agent learned from the exchange or that Commonplace's account needs revision.

## Extractable Value

1. **Test semantic adequacy before investing in machinery.** The solver anecdote adds an operational warning to the existing allocation heuristics: successful implementation can prolong a mistaken formalization. A few representative contradiction cases could expose whether the representation preserves the distinctions the task needs; the essay does not itself supply such a test set. [quick-win]
2. **Compare spontaneous design with prompted criticism.** The reported late explanation suggests a focused experiment: compare initial designs with designs produced after an explicit request to challenge the semantic adequacy of the chosen approach. Measure design changes and task outcomes separately; producing a convincing objection is not proof of improvement. This would test the activation note's practical implication rather than merely collect more anecdotes. [experiment]
3. **Keep training explanations as rival hypotheses.** The pretraining-history, RLVR-access, and design-capability accounts identify distinct questions for investigation. They are useful diagnostic framing, but do not support changing Commonplace's model selection or architecture on their own. [just-a-reference]

## Limitations (our opinion)

The source supplies selected anecdotes, not prompts, complete traces, model configurations, failure rates, or matched comparisons. Its own Autodeck observation provides practitioner context but no denominator or account of successful symbolic choices. Missing requirements and user context could explain some apparent design errors; the essay does not isolate capability from elicitation or task framing. Its RLVR explanation explicitly lacks knowledge of the relevant training environments, and recognizing the objection after prompting does not prove earlier contextual exposure.

The categorical claim that no analytic method can determine whether arbitrary sentences express the same proposition is not developed into a precise impossibility argument. It does not establish that bounded formalizations or hybrid systems are useless. Conversely, calling model-based contradiction detection relatively trivial bypasses accuracy, ambiguity, retrieval coverage, pairwise scaling, and the difference between detecting conflict and deciding which memory to retain. The source runs no experiment comparing these alternatives. As the [allocation heuristics](../theory/codify-versus-llm-decision-heuristics.md) emphasize, both implementations need competent designs and comparable outcome requirements before a general preference is warranted.

## Recommended Next Action

File this ingest as a source-only reference for `kb/theory/codify-versus-llm-decision-heuristics.md`, without promoting its training explanations or generalizing its model-call recommendation.

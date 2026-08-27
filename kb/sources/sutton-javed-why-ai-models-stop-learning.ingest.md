---
description: "Sutton and Javed argue that context-state adaptation cannot replace continual weight learning, posing a counterpoint to Commonplace's whole-system account."
source: https://sequoiacap.com/podcast/rich-sutton-and-khurram-javed-why-ai-models-stop-learning-and-how-to-start-it-again
captured: "2026-08-26"
capture: trafilatura
capture_scope: full-source
genre: conversation-thread
snapshot_sha256: 7100f13baaace6e4b5e5e32594f33f71f602da608b40dff0ea99b09428a23c99
ingested: "2026-08-26"
type: kb/sources/types/ingest-report.md
domains: [continual-learning, reinforcement-learning, representational-form, agent-architecture]
---

# Ingest: Sutton and Javed on why AI models stop learning

## Classification

This is a speaker-labelled research interview whose evidential force comes from a multi-party exchange, including challenges from the hosts, rather than a single authored argument or an empirical report.
Author: Sutton's foundational work in reinforcement learning and Javed's continual-learning research give them direct expertise in the topic. Both also speak as Oak Lab founders advocating their own research program; hosts Sonya Huang and Alfred Lin represent Sequoia Capital, which published the interview.

## Summary

The interview distinguishes context-state adaptation from weight change and argues that continued weight learning is necessary for the concept and abstraction formation needed by genuinely continual agents. Sutton and Javed's big-world premise is that any agent or human-built simulator is a severe approximation, so an agent must keep learning from its own single stream of experience; their proposed route combines per-weight step-size adaptation with continual backprop's generation and testing of new units, then extends to learned world models, self-discovered abstractions, and planning. Read it as a clear later statement of their architecture bet, not as evidence that those mechanisms scale to foundation models or outperform mixed-form system learning.

## Quotes

- **Source extract (verbatim):** Well, so think of all the structuring and generation of new concepts that went into creating the large language models. All that is the weight learning. And you want to be able to continue doing that. You don’t want that to happen just once.
  - **Source location:** Transcript, exchange on LLM memories and in-context learning
- **Source extract (verbatim):** So context can be in the state, too. It could be both, but you still need to be able to update the weights.
  - **Source location:** Transcript, exchange on whether context should live in the weights
- **Source extract (verbatim):** The big world hypothesis, let’s say what it is, is that the world is massively more complex than your mind, than any agent. And this is obvious because the world contains many other agents. So because the world is massively complex, there’s no way you can do anything that might claim to be optimal or perfect. You’re going to be imperfect and you have to have approximations, and those approximations will be severe. And so because of that, that is ultimately the reason why we have to continue learning. If you want to think of it as a reason, we have to continue learning because we’ll encounter some particular part of this immense world and we’ll have to learn. And approximation that’s tuned to the part of the world we’re in, not to all the other parts that we’re not in.
  - **Source location:** Transcript, Rich Sutton on synthetic data and the big world hypothesis
- **Source extract (verbatim):** The big challenge that we don’t see in our field, the ability we don’t see in our field yet, is the ability to learn a model and then plan with a model. We can do the math things, and we can do AlphaGo because the games, we know the model, we know how the moves work. And in math, we know what the operators are. We know lean will take us from one state of knowledge to the state of the proof to the next state. But if we have to learn the models, there are no—I’m going to say it, it’s probably maybe a weird example, but a counterexample, but I’m going to say there’s no instances of learning the model and then planning with the model in our field.
  - **Source location:** Transcript, Rich Sutton on the ability the field has not yet shown
- **Source extract (verbatim):** At least not with self-discovered abstractions.
  - **Source location:** Transcript, Khurram Javed replying to Sutton on learning a model and planning with it
- **Source extract (verbatim):** The big question is always, you have your knowledge-based system, and what keeps the knowledge in it correct? Well, what keeps the knowledge correct in a large language model is well, people did a lot of post-training, and they made sure it was correct and then they freeze it after that. So that’s what keeps it correct. But really, in our minds, we are always changing things, and yet something keeps it organized and coherent and settling back into a good place rather than drifting off into crazy land. That is, I think, our biggest ambition, to have a mind that is self-consistent and can keep training itself and making it coherent.
  - **Source location:** Transcript, Rich Sutton answering Alfred Lin on the most ambitious thing Oak Lab is trying to do
- **Source extract (verbatim):** So the way they do it, as far as I understand, is a lot of people are using Tab, they collect all this data, so coming from millions of users or thousands of users, and then they do one update of the policy from this batch data. So this could work, but imagine I want to teach this model something specific. I don’t want to fight with 100,000 other people about what they want to create and teach their models. I want to teach my model something very specific, and I want to do it to my version of the model. I don’t care about the shared knowledge that the model has coming from other people. And so it’s a very inefficient way of doing it.
  - **Source location:** Transcript, Khurram Javed on Cursor Tab batch updates from many users

## Connections Found

The interview is a first-party public statement that clarifies and bounds existing KB theory. It **compares with** [The bitter lesson selects production methods, not representational forms](../notes/the-bitter-lesson-selects-production-methods-not-representational.md): the 2019 essay supports the note's production-method reading, while this later interview adds Sutton and Javed's separate, stronger claim that weight plasticity is necessary for new-concept capability. It is also a direct **counterpoint** to [The deployed system, not the model alone, is the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) and [Treat continual learning as representational-form coevolution](../notes/treat-continual-learning-as-representational-form-coevolution.md), which admit evidence-responsive updates to natural-language and symbolic artifacts into the learning surface and leave capability allocation among forms empirical. As an authorial **companion** to [The Alberta Plan for AI Research](./the-alberta-plan-for-ai-research.ingest.md), the interview explains the proposed dependency: continual deep learning enables continual world-model revision, which in turn supports the plan's later abstraction and planning steps.

## Extractable Value

1. **Separate source attribution from local extrapolation.** The interview lets the KB say that the Bitter Lesson itself is form-neutral while Sutton later advances a weight-plasticity requirement, avoiding retroactive attribution of the later claim to the 2019 essay. [quick-win]
2. **Distinguish behavior adaptation from capability acquisition.** Sutton and Javed accept that context can change model state but deny that this suffices for the concept formation they seek. This gives Commonplace's whole-system account a sharper burden: demonstrate growth in useful abstraction or action capacity, not merely persistent behavior change. [deep-dive]
3. **Turn representational allocation into a comparative test.** The interview supplies a clear parametric-necessity hypothesis against the KB's coevolution hypothesis; a useful comparison would hold objectives and evaluation fixed while varying which weight, natural-language, and symbolic surfaces can update. [experiment]
4. **Preserve the Alberta Plan's dependency explanation.** The speakers explicitly place continual deep learning before continual model revision and self-discovered abstraction, providing first-party interpretation of why the roadmap orders those capabilities as it does. [just-a-reference]
5. **Keep the proposed anti-forgetting mechanisms at hypothesis status.** Per-weight step-size adaptation and continual generation and testing of units are concrete enough to guide technical reading, but this transcript provides no outcome evidence for their generality or scale. [just-a-reference]

## Limitations (our opinion)

This is a promotional interview around the founders' new lab, not a controlled evaluation. It provides no methods, datasets, baselines, ablations, or results for claims that continual backprop cures catastrophic forgetting, that synthetic data is a strategic mistake, or that the proposed architecture will scale to foundation models and extreme energy targets. Sutton and Javed's expertise makes the agenda important, but their institutional interest makes it a first-party position rather than independent validation.

The human-plasticity, animal-learning, and simulator examples motivate functions an agent might need, but they do not establish that continued weight change is the necessary component boundary for those functions. The interview does not compare its weight-centred update space with evidence-responsive artifact learning or a mixed-form loop; as [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) warns, success within one chosen update space would not by itself validate the choices fixed outside it. At least one transcript line also appears inconsistent with its surrounding exchange, so isolated phrasing should not carry a claim without checking the broader passage.

## Recommended Next Action

Update [The bitter lesson selects production methods, not representational forms](../notes/the-bitter-lesson-selects-production-methods-not-representational.md) with a short attribution boundary distinguishing the original essay's form-neutral production-method claim from Sutton's later weight-plasticity position, citing this ingest as `compares-with`.

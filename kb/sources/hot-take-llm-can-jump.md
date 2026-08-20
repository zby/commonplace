---
source: https://yongzx.github.io/blog/2026/08/08/llm-can-jump
description: Yong Zheng-Xin's interconnected-knowledge counterargument to the claim that LLMs cannot make abductive scientific jumps, with implications for safety and continual learning
captured: 2026-08-20
capture: web-fetch
genre: conceptual-essay
type: kb/sources/types/snapshot.md
---

# Hot Take: LLM can 'jump'

Author: Yong Zheng-Xin
Source: https://yongzx.github.io/blog/2026/08/08/llm-can-jump
Date: 8 August 2026

I want to lodge my takes on the how LLMs can advance science through major breakthroughs, and what the assumptions behind my takes imply for safety risks and continual learning.

Let me start with my disagreement with the ICML’26 position paper that [“LLM can’t jump” by Tom Zahavy](https://www.tomzahavy.com/files/llms-cant-jump.pdf).

## Preliminaries

In [“LLMs can’t jump”](https://www.tomzahavy.com/files/llms-cant-jump.pdf), Tom used the General Relativity case study, where Einstein was inspired by his elevator thought experiment while trying to construct a mathematical theory of gravity. Mercury’s anomalous orbit later became an important test of the theory.

Specifically, this required abductive reasoning: inferring the most plausible explanation for the apparent equivalence between acceleration and gravity. Tom explained that “(Einstein) relied on a physical prior. Because the simulated sensory experience of acceleration was indistinguishable from the remembered sensory experience of gravity, Einstein abducted that they must be the same phenomenon. The field inside the box was not a fake inertial effect; it was, by definition, a genuine gravitational field.”

Tom also made his case strong through the following arguments:

1. There wasn’t a need for a new gravity theory as Newtonian framework was working well, and the anomalous orbit of Mercury could be potentially explained by other factors.
2. There weren’t axioms available at the time for him to come up with the theory via deduction.

In other words, Tom pushed for the point that, given that LLMs do not have a reliable world model (which is necessary for the physical priors) and there’s no dataset to really derive General Relativity, LLMs wouldn’t have jumped and come up with the breakthrough.

All in all, I believe that Tom and I would probably agree with the following:

1. LLMs are capable of deduction or induction.
2. Abduction––specifically relying on sensory experience––was the way of how Einstein came up with The Theory of General Relativity.

**However, my main disagreement isn’t whether LLMs could do similar abduction via the same imagination, but whether someone could later stumble upon General Relativity through a different, more deductive path.** Surprisingly, this wasn’t surfaced in the [ICML 2026 reviews](https://openreview.net/forum?id=klU4737opt).

## Is there another way to derive General Relativity?

[I went down a rabbit hole of asking if there could ever be a contemporary discovery on General Relativity.](https://x.com/yong_zhengxin/status/2075334146977677756?s=20). I came across this [article](https://arxiv.org/pdf/2111.00333), which suggests that Einstein’s abductive route was not the only possible route to General Relativity.

> “Instead of trying to explain the rest of physics in terms of gravity I propose to reverse the problem by changing history. Suppose Einstein never existed…”
>
> — Richard Feynman

Here’s the relevant text as verbatim: *“on the basis of the general principles of quantum field theory and of experimental results it is possible to conclude that gravity, as any other force, has to be mediated by exchanges of a virtual particle, which in this case is a massless neutral spin-2 quantum, the graviton. Thus, by constructing a Lorentz invariant quantum field theory of the graviton and by imposing certain consistency requirements, **full general relativity should be recovered**.”*

Curious readers can read upon page 4 in details, where Feynman route starts from special relativity, then adds quantum field theory and empirical properties of gravity. These assumptions do not directly presuppose Einstein’s theory.

Note that my point wasn’t to establish that Feynman would inevitably have rediscovered general relativity from scratch. He already knew Einstein’s theory, and reconstructing a known result is easier than discovering it for the first time. Furthermore, historically, quantum field theory was developed after General Relativity was proposed (but do *not* depend on General Relativity).

My narrower claim is that, given a sufficiently rich body of later knowledge, general relativity can be recovered without Einstein’s thought experiment. Much of Feynman’s route is deductive, which the kind of reasoning that LLMs already exhibit especially with OpenAI’s Astra models.

## Why interconnected knowledge makes “jumping” possible

Going beyond the case study of Tom’s work, I believe the essence is whether LLMs can come up with plausible explanations that enable breakthroughs. I agree with Tom’s argument that Schmidhuber’s perspective of *[compression](https://link.springer.com/chapter/10.1007/978-3-642-02565-5_4)*, which is “the search for a simple program that concisely explains observations” would not unlock the abductive jump (read: come up with plausible hypothesis).

My deeper belief why LLMs can achieve major scientific breakthroughs is about the **structure of knowledge itself**. Because facts and axioms are connected via mathematical structures or causal relationships, one factual claim or observation either limits the possibilities that can be true (which helps rule out incorrect hypotheses) or reveals a pattern that may transfer from another domain (which helps generate new hypotheses).

From this framework, I’d argue that:

1. **Models can already propose novel connections.** For instance, to disprove a long-standing conjecture in the unit-distance problem, [OpenAI’s Astra model brought tools from algebraic number theory into a problem in discrete geometry](https://openai.com/index/model-disproves-discrete-geometry-conjecture/).
2. **Models can reason about the consistency of observations or connections**. Assuming models demonstrate strong scientific reasoning capabilities (given [how such capability has been improving across different STEM disciplines](https://x.com/i/trending/2085408100161663358)), models could use deduction from axioms or prior knowledge to explain whether a particular observation is being consistent. As models become smarter (i.e., being about to reason from facts to facts), the inconsistency would then suggest there exists limitations for current paradigm, or missing “hop” in reasoning. Models would then propose plausible hypotheses and explanations (from 1). While it is normal to remain speculative on the diversity of hypotheses, I do not see an explanation for why 1 would remain the point of failure as we are seeing more and more open problems tacked due to (1).
3. **Models can verify the explanations.** LLM agents can readily perform code execution, formal verification with Lean, simulations, and even wet-lab experiments to provide experimental results. This thus turns hypothesis generation from (2) into an iterative empirical validation.

Certainly, I do not proclaim models are already good enough to unlock all scientific breakthroughs, but I anticipate that we can achieve a lot of seemingly “paradigm changes” given that we continuously improve models’ reasoning about knowledge consistency and about feedback from real-world experiments/verification.

## Safety implication: missing knowledge can be reconstructed

If we create superintelligent machines that can navigate a densely interconnected body of knowledge, removing harmful information from pretraining may be insufficient as a complete safety strategy. **Removing an explicit piece of harmful knowledge is not the same as removing the ability to derive it.**

A model would not need to recall the removed concept directly. It could simply recognize the knowledge gap, propose something that would fill it, derive the consequences, and check whether those consequences are consistent with the existing knowledge body that it holds.

There is controlled evidence for this already. [Treutlein et al. (2024)](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe489a28a54583ee802b8e2955c024c2-Paper-Conference.pdf) show that models can infer target facts or rules from indirect observations distributed across separate training examples. Their assumed threat model is exactly what I stated: censoring dangerous knowledge removes direct statements while leaving implicit information scattered across documents. [Yao et al.](https://aclanthology.org/2025.emnlp-main.490/) likewise show, in synthetic knowledge graphs, that a model can answer held-out multi-hop questions by combining retained relations in training data.

I do believe data filtering remains effective to some extent as it increases the cost of reconstruction––assuming knowledge is complex enough to require CoT to reconstruct, that offers a window of monitorability––and if we successfully figure out how models may derive from implicit knowledge, we can remove sufficient information such that reconstruction may become impossible.

However, I remain rather pessimistic if superintelligent machines can figure out how knowledge across different domains are interconected and we are becomingly dependent on them for scientific breakthroughs. It is not hard to assume that a misaligned model that is very good at “oncolytic virus therapy”––which uses virus to cure cancer––can easily infer how to create virulent strains as bioweapon. Scientific knowledge is often dual use.

## Predictions on continual learning

I also predict that if newer models are forming more interconnected knowledge across diverse domains, **continual learning will be easier with newer models**.

My definition of continual learning is rather broad, which is that would models or agents being able to help with a task that requires new knowledge that are not seen during training. It doesn’t have to be direct update on weights––as long as it can use its capability to process new (background) information and satisfy users’ tasks, that demonstrates that the models have learned to use the new knowledge. This view is fairly consistent with the emerging area of [Machine Studying](https://jacobxli.com/blog/2026/machine-studying/).

Specifically, I have two predictions based on the assumptions that future models are becoming experts in more diverse domains:

1. **Direct learning of knowledge in weight space becomes easier** because they are more *in-distribution* to what the models have seen, as models are becoming experts in more diverse domains. In other words, existing algorithms can be readily applied and we see continual learning success increases with newer models because new knowledge becomes just an extension of pre-existing knowledge.
2. Future models will solve the loss of plasticity––if it remains an issue––by **inventing their ways of connecting new knowledge to their existing knowledge.** It can come in various forms: data augmentation of new knowledge or novel learning algorithms that directly create connections between new and old knowledge, doing prompt optimization upon itself that makes the connections explicit to elicit its capability in the new domain, or simply leaving notes about how to use new knowledge (so that it doesn’t carry out destructive weight updates).

## Concluding remarks

I presented the interconnected-knowledge view of scientific discovery––fitting for the adage of “standing on the shoulders of the giants”––that explain how General Relativity could have been rediscovered, potential scientific breakthroughts, safety implications and continual learning progress.

I also do not think that this view is particularly novel (as it has been proposed in [literature such as in 2009](https://arxiv.org/abs/0904.1439)) but I held a stronger view upon it that given the pace of LLM progress, it is sufficient in leading to scientific breakthroughs. I am very likely to be wrong, but [I am still writing this down due to my X commitment.](https://x.com/yong_zhengxin/status/2085827955482063141?s=20)

---

### Acknowledgement

Thanks to [Jacob Xiaochen Li](https://jacobxli.com/) for insightful discussion, which helps me better bring my thoughts to light.

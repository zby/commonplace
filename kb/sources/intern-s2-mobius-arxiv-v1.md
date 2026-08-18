---
source: https://arxiv.org/abs/2608.14290v1
description: "Mobius-v0 paper separating shared FFN knowledge storage from iterative self-attention reasoners, with training-data, throughput, and ablation evidence"
captured: 2026-08-18
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning

Author: Intern-S2-Mobius Team, Shanghai AI Laboratory
Source: https://arxiv.org/abs/2608.14290v1
Date: 2026-08-14

## Abstract

We introduce Mobius-v0, an architecture that comprises a globally shared Memory (FFN) that stores knowledge vectors and multiple Reasoners (Self-Attn) that iteratively achieve compositional reasoning. Using hidden states as cache and carrier, reasoners repeatedly query memory for required knowledge-vectors, while the knowledge is transmitted back to reasoning operators. Through this knowledge-reasoning-separation architecture, Mobius achieves better knowledge compression and reasoning efficiency. Built upon Mobius-v0 architecture: 1) Our 7B model trained-from-scratch achieves similar downstream score as a 7B Transformer baseline with 62.6% of baseline’s training data. 2) Our Intern-S2-Mobius, continually-pretrained from Qwen3.5-35B, achieves similar downstream score while delivering nearly 4× end-to-end inference speedup.

arXiv:2608.14290v1 [cs.AI] 14 Aug 2026




## 1. The development bottleneck of the Foundation Models


                                                         Add & Normalize

                                                                                                        memory
                                                           Feed Forward
                                                                                                                       Add & Normalize
                                                         Add & Normalize
                                                                                                                 Global-Shared Vector Database
                                                             Self-Attn


                                                         Add & Normalize                                reasoner

                                                                                                                       Add & Normalize
                                                           Feed Forward
                                                                                                                           Self-Attn
                                                         Add & Normalize

                                                             Self-Attn                                   cache




                                                        (a) Transformer                                                  (b) Mobius

                                         Figure 1: The Comparison between Transformer and Mobius.

                                             The Transformer [69] stands as the most prevalent and powerful architectural paradigm to date, permeating
                                         virtually every domain—from language and vision, to video and scientific computing [4, 15, 16, 81]. Along its
                                         evolutionary trajectory, two pivotal research directions have emerged. The first preserves the model architecture
                                         intact while increasing expenditure elsewhere to enhance capability: scaling model parameters, expanding
                                         training corpora, and elongating reasoning chains typically endow models with richer knowledge and the
                                         capacity to tackle more intricate problems [33, 37, 45, 71]. The second reduces training and inference
                                         overhead by lowering architectural complexity to improve practicality: motivated by the widely held view
                                            * Model is available at https://huggingface.co/internlm/Intern-S2-Mobius



that the quadratic complexity of self-attention constitutes a bottleneck for ultra-long contexts, linear attention
mechanisms such as SSM and GDN have been proposed [10, 25, 38, 78], and their variants have since been
integrated into mainstream contemporary architectures.

                           0.50         Mobius
                                        Transformer

                           0.45
           MMLU Accuracy




                           0.40
                                                                                                     1.6x faster
                           0.35



                           0.30

                                  102                                                          0.626 × 103      103
                                                                      Tokens (B)
Figure 2: The MMLU score of Mobius and Transformer pre-trained from scratch.

    Yet both approaches are now hitting their limits. On one hand, scaling data and parameters has yielded
increasingly powerful models at high returns on investment, yet the Scaling Law has gradually plateaued and is
approaching diminishing marginal returns [33, 37]. Long chains of thought have served us well in domains such
as mathematics, code, and physics, yet models tend to produce verbose, tangential output regardless of problem
difficulty—a trait typically regarded in human society as a sign of insufficient intelligence [49, 54]. On the other
hand, reducing the computational complexity of full attention does bring certain efficiency gains, yet it has
become increasingly apparent that the efficiency improvements achieved at the cost of sacrificing a substantial
portion of model capability have not made models truly affordable enough for commercial deployment [3].
    Confronted with this bottleneck in AI development, we pursue an alternative path: increasing architectural
complexity to raise the ceiling of model intelligence, thereby reducing the end-to-end overhead. To
this purpose, we propose the Mobius, which decouples the binding between knowledge vectors (FFN) and
reasoning operators (Self-Attn), thereby constructing a shared knowledge vector database accessible to all
reasoning operators. Although the large scale of this shared vector database renders each inference activation
highly sparse, introducing greater memory access pressure and lower per-pass forward efficiency, we find that
this implementation achieves nearly 4× end-to-end inference speedup over the Transformer architecture with
same parameters while maintaining equivalent reasoning accuracy.
    The efficiency gains of Mobius reasoning stem primarily from two sources: a more flexible activation path
during inference, and a more dynamic latent-space iteration, which together endow Mobius with a more efficient
and concise output pattern. The first advantage arises because, unlike the combination of hierarchical storage
and forward residual connections in Transformer, Mobius’s shared storage natively introduces Backward
Residual Connection. This mechanism means that not only can shallow hidden states access deep-layer
knowledge, but deep hidden states can also access shallow-layer knowledge, which enhances the compositional
generalization across different layers and thereby accelerates the synthesis of critical information. The second
advantage arises because Mobius natively introduces Dynamic Latent Reasoning: whereas Transformer uses
tokens as the medium of information transfer and requires traversing all layers to complete the inference of a
single token, Mobius can iterate and refine latents against the full knowledge repository within just a few layers,
rather than requiring multiple full-layer iterations as in traditional latent reasoning. These latents are not tightly
bound to any specific token, and only at deeper layers are multiple tokens decoded synchronously. This approach
both increases the density of information transfer and dynamically allocates varying computational costs to
different tokens. Ultimately, Mobius completes the same reasoning task with markedly fewer high-quality





tokens, achieving substantially higher end-to-end inference efficiency than Transformer.

Table 1: Performance comparison across general and scientific benchmarks. The higher score in each row is
highlighted in bold.

                   General Tasks
                   Benchmark                Intern-S2-Mobius-35B              Qwen3.5-35B
                   MMLU Pro                         89.05                         85.31
                   GPQA Diamond                     80.81                         80.24
                   IMO Bench                        81.25                         77.50
                   AIME 2026                        95.31                         92.08
                   HMMT 2026                        85.51                         78.50
                   UGD hard                         73.02                         78.02
                   AMO                              58.00                         50.00
                   SimpleQA                         28.90                         21.39
                   HLE                              19.11                         22.40
                   AVG Score                        67.88                         65.05

                   Scientific Tasks
                   Benchmark                Intern-S2-Mobius-35B              Qwen3.5-35B
                   Biology-Instructions             51.40                          3.77
                   Mol-Instructions                 45.73                         21.70
                   MolecularIQ                      59.29                         29.13
                   AVG Score                        52.14                         18.20



## 2. What inspired the design of Mobius?
In Transformer-based architectures, the Feed-Forward Network is conventionally regarded as responsible for
knowledge storage [20, 52], Hidden States for information transmission, and Self-Attention for compositional
reasoning [17, 69].
    Concurrently, owing to the hierarchical structure of Transformer, Self-Attention at each layer primarily
processes knowledge inputs received from the preceding layer and induces the FFN at the current layer to
produce outputs required by the next layer. Although residual connections establish more flexible connections
across layers [31, 34, 67], only shallow Hidden States can access deep-layer knowledge, while deep-layer
Self-Attention can only process knowledge originating from shallow layers; the model remains incapable of
information transfer in the opposite direction.
    To construct information transfer in the reverse direction, current models predominantly rely on Chains of
Thought [26, 71]. After each forward pass, the model generates a new token that serves to activate knowledge
in the next inference step. Through iterative token generation, the model continuously extracts valuable
knowledge from the FFN until this knowledge suffices to produce critical tokens or even the final answer.
    The joint construction of artificial intelligence models using exclusively hierarchical structures, forward
residual connections, and token-mediated chains of thought is inefficient. To equip models with sufficient
knowledge for answering complex questions, an inordinate amount of computation is expended on producing
lengthy, redundant reasoning chains. To mitigate this issue, we have redesigned the model architecture and
propose Mobius.


## 2.1. Mobius’ first innate talent —— Backward Residual Connection
Residual connections have become one of the most critical components in modern deep learning models [31].
Seemingly minor, they bear the crucial responsibility of transmitting inter-layer information during forward
propagation and stabilizing gradient magnitudes during backpropagation. [32, 75] Although numerous variants
of residual connections have since emerged, such as Hyper-Connection and Attention-Residual [39, 74, 80],
all mainstream residual to date retain their unidirectional nature. For instance, during forward propagation,





                                                                                              Mobius           Transformer
                                                        Average                                        MMLU Pro                                    GPQA Diamond
                                                                                                                                  3.50
                             2.50
                                                                                  8.00                                            3.00
                             2.00                                                                                                 2.50

                             1.50
                                                                   4.6x faster    6.00
                                                                                                                                  2.00

                                                                                  4.00                                            1.50
Request Throughput (req/s)




                             1.00
                                                                                                                                  1.00
                             0.50        2.9x faster                              2.00
                                                                                                                                  0.50

                                    24          25        26       27        28          24     25        26        27       28          24   25        26        27   28
                                                       IMO Bench                                       AIME 2026                                    HMMT 2026
                             0.24                                                 0.50
                                                                                                                                  0.24
                             0.22                                                 0.45                                            0.22
                             0.20                                                 0.40                                            0.20
                             0.18                                                 0.35                                            0.18
                             0.16                                                 0.30                                            0.16
                             0.14                                                 0.25                                            0.14
                             0.12                                                 0.20                                            0.12
                             0.10                                                 0.15                                            0.10
                                    24          25        26       27        28          24     25        26        27       28          24   25        26        27   28
                                                                                                     Batch Size
     Figure 3: The inference efficiency of Mobius continual pre-trained from Qwen3.5.


     residual only convey shallow-layer information to deeper layers. [34] This unidirectionality entails significant
     drawbacks: if certain critical knowledge fails to be activated during shallow-layer computation, the model may
     struggle to decode valuable tokens in that reasoning round, and can only resort to generating low-information
     tokens via chains of thought to proceed to the next reasoning step.
         To mitigate this phenomenon, rendering residual connections bidirectional is necessary—that is, enabling
     deep layers to access shallow-layer knowledge during forward propagation. However, a direct implementation of
     such backward residual connections is infrastructure-unfriendly, as it may introduce more complex computation
     graphs and harder-to-parallelize asynchrony. To this end, we opt for an indirect realization of backward
     residual connections: different layers share a single, oversized knowledge repository, granting every layer
     the opportunity to access all knowledge within the model. Empirical results ultimately corroborate that this
     form of backward residual connection contributes meaningfully to improving the model’s end-to-end inference
     efficiency.


## 2.2. Mobius’ second innate talent —— Dynamic Latent Reasoning
     Long chains of thought (Long CoT) have become an indispensable component in large language model
     reasoning [26, 45, 71]. Empowered by this technique, contemporary large language models can now solve a
     wide spectrum of complex reasoning problems, spanning mathematics, physics, and code generation. Yet the
     cost of Long CoT is exorbitant. On one hand, longer reasoning chains entail the generation of more tokens,
     with generation cost growing non-linearly with chain length. On the other hand, current models frequently
     adopt a trial-and-error-and-correct approach when tackling complex problems, resulting in substantial token
     redundancy during extended reasoning. Moreover, such models tend to produce excessively verbose responses
     even for simple problems. This verbosity stems partly from the residual connections discussed above, and partly
     from the fact that the minimal unit of our current reasoning is the token—a discrete, low-information-density
     storage [9].
        Mobius internalizes processes such as deliberation, trial-and-error, and refinement into the optimization of a
     continuous vector, and enables the model to dynamically allocate computational budget to different tokens. This
     creates the opportunity for the model to produce fewer superfluous tokens while achieving more efficient and
     more intelligent reasoning. Mobius can be regarded as an upgraded synthesis of the Looped Transformer and





                                                                           Mobius        Transformer
                                           Average                                  MMLU Pro                               GPQA Diamond
                                                                                                         14000
                             20000                                 5000
                                                                                                         12000

                             15000
                                     1.5x
                                     shorter
                                                                   4000                                  10000

                                                                   3000                                   8000
Avg Output Length (tokens)




                             10000                                                                        6000
                                                                   2000
                                                                              4.6x
                                                                              shorter                     4000        5.0x
                              5000                                                                                    shorter
                                                                   1000
                                                                                                          2000

                                 0                                    0                                      0
                                          IMO Bench                                 AIME 2026                               HMMT 2026
                                                                  25000
                             35000                                                                       30000
                                                                                                                      1.2x
                             30000
                                     1.4x                         20000                                  25000        shorter
                             25000
                                     shorter                                  1.5x
                                                                              shorter
                                                                  15000                                  20000
                             20000
                                                                                                         15000
                             15000                                10000
                                                                                                         10000
                             10000
                                                                   5000
                              5000                                                                        5000

                                 0                                    0                                      0


     Figure 4: The average output length of Mobius continual pre-trained from Qwen3.5.


     the Diffusion Language Model [21, 43, 55], employing more efficient latent reasoning and parallel prediction.
     First, Mobius operates at a higher loop frequency, completing one representation iteration with extremely
     few layers. Second, during inference, Mobius acquires joint representations of multiple tokens simultaneously
     through more compact, high-information-density continuous vectors. This, on one hand, alleviates the pressure
     from parallelizing multiple hidden states, reduces the complexity of KV-cache management during the looping
     process, and enhances the continuous differentiability of the vector iteration process. Meanwhile, this native
     latent reasoning endows the model with a more dynamic and unfettered iteration process, without constraining
     the model to decode a fixed number of tokens at specific iteration steps.


## 2.3. One Stone Two Birds —— Disentangling Knowledge Vectors and Reasoning Operators

     Overall, Mobius achieves these two innate talents by decoupling the knowledge storage module, the FFN,
     from its layer-wise binding, and constructing a globally shared knowledge-vector database. First, this grants
     all reasoning operators, the Self-Attention, read access to the entire body of knowledge. Further, the Self-
     Attention gains the opportunity to access all knowledge within significantly fewer layers, and performs adaptive
     multi-round iteration through recurrent latent reasoning via Hidden States, ultimately emitting refined, high-
     information-density tokens in a single burst.
         In constructing the shared knowledge repository, we opted for a straightforward horizontal concatenation,
     as the FFN is conventionally regarded as a Key-Value Knowledge-Vector Pool, and this concatenation approach
     preserves the correspondence relationships among these knowledge vectors. Although such simple concatenation
     yields performance benefits, excessive parameter activation degrades the model’s training and inference
     efficiency. Therefore, at larger parameter scales, we employ a block-wise partitioning technique analogous to
     MoE [63] to partition the FFN, with sparse activation during forward propagation.


## 3. How about Mobius’ performance?
     To validate the performance of Mobius, we conducted both training-from-scratch (TFS) and continual pre-
     training (CPT) experiments. For the TFS experiments, we trained 7B-A1B MoE models — one with Mobius
     and one with Transformer — on 1TB tokens, and compared their MMLU scores. For the CPT experiments, we




Table 2: Step-aligned comparison between Intern-S2-Mobius-35B and Qwen3.5-35B on a linear-algebra
multiple-choice question. Both models select the correct answer (Option C). Token counts are computed using
the Qwen3.5-35B tokenizer. Mobius completes the same reasoning steps with fewer tokens, which mainly
benefits from the model’s elimination of repeated derivation and checks.

 Reasoning Trace Comparison
  Aligned Step                                 Intern-S2-Mobius-35B                                 Qwen3.5-35B
                                                     17 tokens.                                     20 tokens.
                                        “The user wants me to evaluate the            “The user wants me to evaluate two
  Task framing
                                           truth value of two statements              statements and determine their truth
                                             regarding linear algebra.”                   values from a list of options.”
                                                                                                  283 tokens.
                                                    178 tokens.
                                                                                         “Consider the zero vector. Let
                                      “Counter-example: Let 𝑣1 = (1, 0) and
                                                                                         𝑣1 = (1, 0) and 𝑣2 = (0, 0). . . .
  Statement 1                           𝑣2 = (2, 0). Then 2𝑣1 − 𝑣2 = 0, so
                                                                                        Consider two parallel vectors. Let
                                         they are linearly dependent. . . .
                                                                                         𝑣1 = (1, 0) and 𝑣2 = (2, 0). . . .
                                              Statement 1 is False.”
                                                                                             Statement 1 is False.”
                                                     142 tokens.                                     197 tokens.
                                         “A basis is a linearly independent           “The set forms a basis for 𝑉 if it spans
  Statement 2                          spanning set. Since {𝑣1 , . . . , 𝑣𝑘 } spans     𝑉 and is linearly independent. . . .
                                          𝑉 and is linearly independent, it            Therefore, {𝑣1 , . . . , 𝑣𝑘 } is a basis for
                                       forms a basis for 𝑉 . . . . dim(𝑉 ) = 𝑘.”               𝑉 . . . . dim(𝑉 ) = 𝑘.”
                                                    22 tokens.                                    122 tokens.
  Option matching                      “Statement 1 is False, Statement 2 is          “The combination is False, True. This
                                          True. This matches Option C.”                    corresponds to Option C.”
                                                                                                   1,147 tokens.
                                                                                          “Step-by-step derivation: . . .
  Repeated derivation and checks                           —                          Counterexample: Let 𝑣1 = (1, 0) and
                                                                                       𝑣2 = (2, 0). . . . Final check: . . . If
                                                                                        𝑘 = 0? . . . Works. . . . Option C.”
                                                                                                  595 tokens.
                                                    157 tokens.
                                                                                       “Step 1: Evaluate Statement 1 . . .
                                          “The vectors (1, 0) and (2, 0) are
                                                                                      2𝑣1 − 1𝑣2 = (0, 0). . . . Statement 1 is
                                        linearly dependent because one is a
  Visible final answer                                                                                False.
                                       scalar multiple of the other. . . . This is
                                                                                        Step 2: Evaluate Statement 2 . . .
                                            the definition of a basis. . . .
                                                                                            dim(𝑉 ) is equal to 𝑘. . . .
                                                    ANSWER: C”
                                                                                                  ANSWER: C”
  Total                                               516 tokens                                    2,364 tokens



used Qwen3.5-35B-A3B as the starting checkpoint, continued pre-training on 1TB tokens, and subsequently
performed supervised fine-tuning (SFT) and reinforcement learning (RL).


## 3.1. Mobius delivers markedly better data efficiency than Transformer.
As shown in Figure 2, Mobius achieves significantly higher MMLU scores than Transformer across all stages of
training. Moreover, when using Transformer’s score at 1TB tokens as the baseline, Mobius attains the same
score with only 0.626× data — that is, Mobius exhibits 1.6× data efficiency of Transformer.
    The mechanism by which Mobius achieves higher data efficiency remains to be fully explored. Nevertheless,
we hypothesize that under the Transformer architecture, parameters across layers exhibit considerable redun-
dancy—for instance, the same piece of knowledge may be redundantly stored in multiple layers. Upon switching
to the knowledge-reasoning-decoupled Mobius architecture, the model can attain superior compression rates,
thereby enabling it to acquire sufficient knowledge with substantially less training data.







## 3.2. Mobius matches Transformer-level reasoning with far greater inference efficiency.

Given the prohibitive cost of pre-training from scratch, to validate Mobius’s capabilities at scale, we chose to
continue training from an existing open-source base model. As shown in Table 1, starting from Qwen3.5 and
switching to the Mobius architecture for continued pre-training not only preserves but actually enhances the
model’s overall capabilities.
    More notably, switching to Mobius not only preserves fundamental reasoning capabilities but also improves
end-to-end inference efficiency. As shown in Figure 3, aggregated across multiple evaluation benchmarks,
Mobius achieves substantially higher request throughput than Transformer. We also examined the inference
length of both models, visualized in Figure 4, which reveals that the improvement in Mobius’s end-to-end
inference efficiency primarily stems from shorter CoT lengths. When presented with identical problems,
Mobius resolves them with markedly shorter reasoning chains, whereas Transformer requires longer CoT for
deliberation.
    Although the precise mechanism behind Mobius’s shorter CoT reasoning remains not fully established, we
hypothesize that this may be attributed to Mobius’s native latent reasoning characteristic, which internalizes the
deliberation process within the model and achieves more efficient reasoning through continuously differentiable
optimization.
    However, whether Mobius merely hacks the problem or genuinely provides a more efficient mode of
reasoning remains to be determined. By comparing multiple cases, we find that the shortened CoT in Mobius
stems from the latter. The case in Table 2 is from MMLU-Pro Mathematics and tests two basic linear-algebra
statements. The first statement is false because two vectors in R2 need not be linearly independent. The
second statement is true because a linearly independent set that spans 𝑉 is a basis of 𝑉 , so its 𝑘 vectors imply
dim(𝑉 ) = 𝑘. The correct answer is therefore Option C: False, True.


## 4. Mobius’ relationship with mainstream research

                           Recurrent propagation                                           Global mapping

                                       RNN                                                   Transformer
                      x1         x2          x3       x4                      x1              x2            x3               x4
   Token
 dimension

                      h1         h2          h3       h4
                                                                              h1              h2            h3               h4

                                                                                                       same design principle,
                                                                                                        different dimension

                                Transformer                                                        Mobius         Shared
                                                                                                                 Knowledge
                 L3        Self-Attn          FFN                        L3        Reasoner                       Memory
 Knowledge                                                                                                          K1
 dimension       L2        Self-Attn          FFN                        L2        Reasoner
                                                                                                                    K2
                                                                                                                    ...
                 L1        Self-Attn          FFN                        L1        Reasoner                         Kn
                                                                                   global address space, sparse activation




Figure 5: The comparison between RNN, Transformer, and Mobius.


## 4.1. Latent Reasoning
Chain-of-thought (CoT) externalizes reasoning into intermediate tokens [71], but incurs sequential decoding
overhead. Latent reasoning instead performs computation in continuous states, exploring three directions:





continuous thought, looped computation, and parallel refinement.

## 4.1.1. Continuous Thought
Continuous-thought approaches replace discrete reasoning tokens with differentiable representations passed
between reasoning steps. COCONUT directly feeds the final hidden state back as the next input embedding,
allowing intermediate computation to proceed without decoding each state into language [30]. CODI com-
presses explicit CoT supervision into continuous states through self-distillation [64], while SoftCoT generates
instance-specific soft thoughts with a lightweight assistant and projects them into the representation space
of a target language model [76]. These approaches demonstrate that continuous states can preserve useful
reasoning information while shortening or eliminating explicit rationales.
    These approaches expose a small set of latent states that subsequent tokens can attend to and reuse as
shared context. Mobius further makes this pattern a native architectural capability: its recurrent states are
refined against the shared Memory and jointly support multiple future tokens, yielding higher-density reasoning
without verbose traces.

## 4.1.2. Looped Language Models
Looped language models increase effective depth by repeatedly applying shared computation blocks. Universal
Transformers introduced recurrent refinement across depth with parameter sharing [12], while subsequent
analyses established the computational expressivity of Looped Transformers [21]. More recent work connects
effective depth directly to reasoning: looped models can emulate multi-step latent computation and approach
much deeper non-looped models on reasoning tasks [60], while recurrent-depth pre-training enables test-
time compute scaling by increasing the number of latent iterations without generating additional reasoning
tokens [19].
    Mobius also scales computation through latent recurrence, but performs each update over only a few
layers while retaining access to the full shared Memory. This higher update frequency enables more iterative
refinement and concentrates reasoning into higher-information-density latent states.

## 4.1.3. Additional Latent Computation Steps
Another line of work increases reasoning capacity by introducing extra latent computation steps before genera-
tion. Pause-token methods add learned placeholders to defer prediction and create additional computation
space [24]. Hidden Decoding expands each token into multiple latent streams within a single forward pass,
using intermediate key–value states as reusable computation traces [46]. Diffusion language models achieve
similar effects through iterative refinement of continuous or masked representations [43, 55]. These methods
shift computation from explicit CoT traces to latent trajectories.
    Mobius extends this idea through recurrent latent refinement without explicit placeholders or diffusion
steps. Its Reasoners repeatedly retrieve from a shared knowledge-vector Memory, refine high-density latent
states, and decode multiple tokens in parallel.

## 4.2. Efficient Reasoning

Historically, the predominant paradigm for language model inference relied on autoregressive single-token
generation from a single strong model, augmented with long chains of thought. To improve end-to-end inference
efficiency, two approaches have gained increasing traction: Speculative Decoding, which enhances inference
parallelism, and Concise CoT, which reduces the sequential length of reasoning chains.

## 4.2.1. Speculative Decoding
Speculative decoding accelerates autoregressive generation by using a cheap drafter to propose a block, or a
tree, of future tokens and verifying these candidates in parallel with the target model [8, 42, 53, 68]. With
rejection-sampling correction, this verification preserves the target model’s output distribution. While classical
methods employ a lightweight external draft model, later work develops internal drafters based on auxiliary
decoding heads or predicted hidden features [2, 7, 44]. MTP is such an internal drafting mechanism rather





than a decoding protocol itself: auxiliary heads sharing the target backbone predict multiple future tokens
[22, 47, 51].
   Whether employing a draft model or other strategies, Speculative Decoding traverses all knowledge only
once before token prediction. In contrast, Mobius performs multiple rounds of knowledge traversal and multi-
token iteration internally, yielding hidden states of higher information density prior to final decoding, with
native support for multi-token prediction.

## 4.2.2. Concise Chain of Thought
Long chain-of-thought (CoT) reasoning can improve performance on challenging tasks, but its autoregressive
generation incurs substantial inference cost and latency. Recent work therefore seeks concise CoT through
several complementary approaches: supervised methods learn from pruned or paired long–short trajectories,
or internalize explicit rationales into implicit or dense representations [9, 13, 14, 36, 73, 79]; RL-based
methods shape reasoning length through reward design, including controllable compression and length-aware
objectives [11, 18, 50, 65]. Although RL can elicit advanced behaviors such as self-correction, verification, and
backtracking [26, 62], outcome-only rewards often favor longer trajectories because additional tokens enable
further exploration and error correction [77]. The central challenge is thus to reduce CoT verbosity without
removing the deliberation needed for accurate and robust reasoning.
    Conventional length regularization may shorten CoT by curtailing deliberation, potentially harming accuracy
and robustness. In contrast, Mobius yields far more refined and shorter responses through several rounds of
latent thought iteration.

## 4.3. Architecture Design
Mobius redesigns the internal information flow of Transformer architectures by decoupling knowledge storage
from reasoning computation. In this section, we discuss its relationship with two major architectural directions:
attention mechanisms and residual connections.

## 4.3.1. Attention Mechanism
Self-attention is the core component of Transformer architectures, enabling models to capture global depen-
dencies through pairwise interactions among tokens [69]. However, the quadratic complexity of full attention
has become a major bottleneck for scaling Transformer models to long-context scenarios. To address this
issue, extensive studies have explored more efficient attention mechanisms. Sparse attention reduces unnec-
essary token interactions by restricting attention patterns, while linear attention reformulates the attention
computation to reduce complexity through alternative kernelization or factorization strategies. More recently,
state-space models and gated state-space variants, such as Mamba and Gated Delta Networks, replace explicit
attention computation with recurrent state updates, providing efficient alternatives for long-sequence model-
ing [25, 78]. These approaches mainly improve efficiency by modifying the computation form or reducing the
cost of information interaction.
   Rather than reducing attention complexity directly, we aim to increase the information density and value
extracted per attention operation. Specifically, by decoupling knowledge from reasoning and constructing
a globally shared knowledge repository, Mobius incur higher retrieval costs but provide attention with a
more flexible selection space and higher-quality inputs, thereby completing reasoning with a more compact
computation trajectory.

## 4.3.2. Residual Connection

Residual connections are fundamental components for scaling deep neural networks, enabling stable optimiza-
tion and effective information propagation through shortcut pathways [31]. Subsequent studies have explored
more flexible connection patterns to improve information transmission across layers. Highway Networks intro-
duce learnable gates to adaptively control information flow [66], while DenseNet increases connection density
by allowing each layer to directly access previous representations [35]. More recently, Hyper-Connections and
Attention Residuals further investigate how to enhance residual pathways by increasing connection capacity or
dynamically aggregating previous-layer representations [39, 80]. Despite these improvements, existing residual





enhancement methods mainly focus on strengthening forward information propagation, where information
flows from earlier layers to later layers.
   Mobius extends residual design from forward information propagation toward bidirectional knowledge
access, instead of explicitly expanding residual pathways. Since all reasoning stages can access the same
knowledge repository, deeper Reasoners can retrieve knowledge beyond their local layer hierarchy, enabling
more flexible information transmission while maintaining an efficient computation structure.


## 5. Mobius’ potential on several highlight topics
## 5.1. Self-Evolving

Although models and agents have grown increasingly capable, how to enable them to continuously absorb new
knowledge and skills from external sources remains an open question [40, 56, 59, 72].
    Our position is that, the current Transformer architecture does not satisfy the prerequisites for self-
evolution. Because knowledge and reasoning are tightly coupled in Transformer, such models can only acquire
new skills through end-to-end training, which inevitably alters both knowledge and reasoning capabilities
simultaneously, thereby causing catastrophic forgetting of previously learned skills. An architecture suitable
for self-evolution should exhibit a certain degree of knowledge-reasoning decoupling, as this would support
unbounded and efficient expansion of knowledge storage, and enable the model’s reasoning capabilities to
generalize across multiple domains. The Mobius architecture we propose possesses preliminary knowledge-
reasoning separation characteristics, demonstrating greater potential for continual learning compared to
Transformer.
    Nevertheless, whether Mobius can perform better in real-world self-evolution scenarios still requires the
joint design of foundation models, agentic systems, and environmental feedback, and remains to be validated
in future work.

## 5.2. World Model

World models are emerging as the next frontier beyond language models, yet how to enable models to perform
understanding and reasoning over continuous-space inputs remains an open question [6, 27–29, 33, 61].
    Our position is that, the current Transformer architecture does not satisfy the prerequisites for world
models. Models built primarily upon Transformer have been demonstrated to model discrete modalities (such
as language) at the terabyte parameter scale, yet perfect modeling of continuous space with Transformer would
likely require parameter scales on the order of petabytes. The inference cost of terabyte-scale language models
already strains existing hardware to its limits; the inference cost of a petabyte-scale world model would be
astronomical. The Mobius architecture we propose natively supports latent reasoning, offering a stronger prior
for continuous-space modeling and demonstrating greater potential than Transformer.
   Nevertheless, the latent reasoning prior introduced by Mobius may prove far from sufficient; how to better
reengineer the attention mechanism may be of even greater criticality.

## 5.3. Scientific Discovery
Contemporary AI has achieved remarkable proficiency in code and mathematics, and recent scientific foundation
models excel at procedural problem-solving [5, 58]. Nevertheless, enabling models to formulate disruptive
scientific hypotheses and ideas remains an open challenge [23, 48, 70].
    Our position is that, the current paradigm of Transformer architecture combined with long chains of
thought does not satisfy the prerequisites for scientific discovery. Under the present paradigm, models
excel at procedural problem-solving; however, scientific discovery demands not only procedural competence
but also scientific intuition and the composition and generalization of knowledge. The Mobius architecture
addresses this on two fronts: on one hand, it internalizes deliberation into a continuously differentiable latent
space [30, 64], affording the model the opportunity to develop more powerful intuition; on the other hand, it
flattens all knowledge within the model, enabling a greater volume of knowledge to interact simultaneously
and substantially increasing the possibility of compositional generalization across knowledge domains.





    Nevertheless, whether Mobius can perform better in real-world scientific discovery scenarios likely requires
the joint optimization of data, infrastructure, training algorithms, and optimization algorithms, and remains to
be validated in future work.


## 5.4. Hardware-Software Co-Design

Models are being scaled to ever-larger parameter counts, demonstrating that greater scale does yield emergent
intelligence, while simultaneously pushing the limits of physical hardware [6, 33, 37, 41, 57].
    Our position is that, the current combination of Transformer architecture and existing hardware
systems does not satisfy the prerequisites for further scaling. This is because the Transformer architecture
commingles knowledge and reasoning within the same parameter set, necessitating the loading of nearly
all parameters into GPU memory at deployment. The Mobius architecture we propose exhibits knowledge-
reasoning separation, opening the possibility of stably retaining only reasoning-dedicated parameters in GPU
memory while storing knowledge parameters predominantly on SSD, with high-priority knowledge retrieved
and loaded into memory on demand.
   In the long term, Mobius is more amenable to hardware-software co-design than Transformer. However,
substantial effort remains before this vision can be realized.







References
 [1] Zeyuan Allen-Zhu. ICML 2024 Tutorial: Physics of Language Models, July 2024. Project page: https:
     //physics.allen-zhu.com/. C
 [2] Zachary Ankner, Rishab Parthasarathy, Aniruddha Nrusimha, Christopher Rinard, Jonathan Ragan-Kelley,
     and William Brandon. Hydra: Sequentially-dependent draft heads for medusa decoding. arXiv preprint
     arXiv:2402.05109, 2024. 4.2.1
 [3] Simran Arora, Sabri Eyuboglu, Michael Zhang, Aman Timalsina, Silas Alberti, Dylan Zinsley, James Zou,
     Atri Rudra, and Christopher Ré. Simple linear attention language models balance the recall-throughput
     tradeoff, 2025. 1
 [4] Gedas Bertasius, Heng Wang, and Lorenzo Torresani. Is space-time attention all you need for video
     understanding? In ICML, 2021. 1
 [5] Daniil A. Boiko, Robert MacKnight, Ben Kline, and Gabe Gomes. Autonomous chemical research with
     large language models. Nature, 624:570–578, 2023. 5.3
 [6] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
     Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen
     Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter,
     Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark,
     Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models
     are few-shot learners. In NeurIPS, 2020. 5.2, 5.4
 [7] Tianle Cai, Yuhong Li, Zhengyang Geng, Hongwu Peng, Jason D. Lee, Deming Chen, and Tri Dao. Medusa:
     Simple llm inference acceleration framework with multiple decoding heads, 2024. 4.2.1
 [8] Charlie Chen, Sebastian Borgeaud, Geoffrey Irving, Jean-Baptiste Lespiau, Laurent Sifre, and John Jumper.
     Accelerating large language model decoding with speculative sampling, 2023. 4.2.1
 [9] Jeffrey Cheng and Benjamin Van Durme. Compressed chain of thought: Efficient reasoning through
     dense representations. arXiv preprint arXiv:2412.13171, 2024. 2.2, 4.2.2
[10] Krzysztof Choromanski, Valerii Likhosherstov, Xingyou Song, Richard Davis, Kyle Sarlos, and Adrian
     Weller. Rethinking attention with performers. In ICLR, 2021. 1
[11] Muzhi Dai, Shixuan Liu, and Qingyi Si. Stable reinforcement learning for efficient reasoning, 2025. 4.2.2
[12] Mostafa Dehghani, Stephan Gouws, Oriol Vinyals, Jakob Uszkoreit, and Lukasz Kaiser. Universal trans-
     formers. In ICLR. OpenReview.net, 2019. 4.1.2

[13] Yuntian Deng, Yejin Choi, and Stuart Shieber. From explicit cot to implicit cot: Learning to internalize
     cot step by step. arXiv preprint arXiv:2405.14838, 2024. 4.2.2
[14] Yuntian Deng, Kiran Prasad, Roland Fernandez, Paul Smolensky, Vishrav Chaudhary, and Stuart Shieber.
     Implicit chain of thought reasoning via knowledge distillation, 2023. 4.2.2
[15] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of deep bidirec-
     tional transformers for language understanding. In Jill Burstein, Christy Doran, and Thamar Solorio,
     editors, Proceedings of the 2019 Conference of the North American Chapter of the Association for Computa-
     tional Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), pages 4171–4186,
     Minneapolis, Minnesota, June 2019. Association for Computational Linguistics. 1
[16] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Un-
     terthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, and Neil
     Houlsby. An image is worth 16x16 words: Transformers for image recognition at scale, 2021. 1







[17] Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell,
     Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds,
     Danny Hernandez, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown,
     Jack Clark, Jared Kaplan, Sam McCandlish, and Chris Olah. A mathematical framework for transformer cir-
     cuits. Transformer Circuits Thread, 2021. https://transformer-circuits.pub/2021/framework/index.html.
[18] Mehdi Fatemi, Banafsheh Rafiee, Mingjie Tang, and Kartik Talamadupula. Concise reasoning via rein-
     forcement learning, 2025. 4.2.2
[19] Jonas Geiping, Sean McLeish, Neel Jain, John Kirchenbauer, Siddharth Singh, Brian Bartoldson, Bhavya
     Kailkhura, Abhinav Bhatele, and Tom Goldstein. Scaling up test-time compute with latent reasoning: A
     recurrent depth approach. In D. Belgrave, C. Zhang, H. Lin, R. Pascanu, P. Koniusz, M. Ghassemi, and
N. Chen, editors, Advances in Neural Information Processing Systems, volume 38, pages 41340–41391.
     Curran Associates, Inc., 2025. 4.1.2

[20] Mor Geva, Roei Schuster, Jonathan Berant, and Omer Levy. Transformer feed-forward layers are key-value
     memories. In Marie-Francine Moens, Xuanjing Huang, Lucia Specia, and Scott Wen-tau Yih, editors,
     Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, pages 5484–5495,
     Online and Punta Cana, Dominican Republic, November 2021. Association for Computational Linguistics.

[21] Angeliki Giannou, Shashank Rajput, Jy yong Sohn, Kangwook Lee, Jason D. Lee, and Dimitris Papail-
     iopoulos. Looped transformers as programmable computers. In ICML, pages 11398–11442, 2023. 2.2,
     4.1.2
[22] Fabian Gloeckle, Badr Youbi Idrissi, Baptiste Rozière, David Lopez-Paz, and Gabriel Synnaeve. Better &
     faster large language models via multi-token prediction. In Proceedings of the 41st International Conference
     on Machine Learning, pages 15706–15734, 2024. 4.2.1
[23] Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, et al. Accelerating scientific discovery with
     co-scientist. Nature, 655(8122):487–496, 2026. 5.3
[24] Sachin Goyal, Ziwei Ji, Ankit Singh Rawat, Aditya Krishna Menon, Sanjiv Kumar, and Vaishnavh Nagarajan.
     Think before you speak: Training language models with pause tokens. In B. Kim, Y. Yue, S. Chaudhuri,
K. Fragkiadaki, M. Khan, and Y. Sun, editors, International Conference on Learning Representations, volume
     2024, pages 27896–27923, 2024. 4.1.3
[25] Albert Gu and Tri Dao. Mamba: Linear-time sequence modeling with selective state spaces. In First
     Conference on Language Modeling, 2024. 1, 4.3.1

[26] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu, Ruoyu Zhang,
     Shirong Ma, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu
     Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao,
     Chengqi Deng, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai,
     Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Hanwei Xu, Honghui Ding, Huazuo
     Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jingchang Chen, Jingyang Yuan, Jinhao Tu, Junjie Qiu,
     Junlong Li, J. L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaichao You, Kaige Gao, Kang
     Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei
     Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Mingxu Zhou, Meng Li, Miaojun Wang,
     Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge,
     Ruisong Zhang, Ruizhe Pan, Runji Wang, R. J. Chen, R. L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou,
     Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S. S. Li, Shuang
     Zhou, Shaoqing Wu, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wen Liu, Wenfeng Liang,
     Wenjun Gao, Wenqin Yu, Wentao Zhang, W. L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang
     Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su,
     Xuheng Lin, X. Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan
     Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Yang Zhang, Yanhong Xu,
     Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He,





     Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang,
     Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou,
Y. X. Zhu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting
     Yan, Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao,
     Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song,
     Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, and Zhen Zhang. Deepseek-r1 incentivizes
     reasoning in llms through reinforcement learning. Nature, 645(8081):633–638, 2025. 2, 2.2, 4.2.2

[27] David Ha and Jürgen Schmidhuber. World models. In Advances in Neural Information Processing Systems,
     volume 31, 2018. 5.2
[28] Danijar Hafner, Timothy Lillicrap, Ian Fischer, Ruben Villegas, David Ha, Honglak Lee, and James Davidson.
     Learning latent dynamics for planning from pixels. In International Conference on Machine Learning,
     pages 2555–2565. PMLR, 2019.

[29] Danijar Hafner, Jürgen Pasukonis, Jimmy Ba, and Timothy Lillicrap. Mastering diverse domains through
     world models. arXiv preprint arXiv:2301.04104, 2023. 5.2
[30] Shibo Hao, Sainbayar Sukhbaatar, DiJia Su, Xian Li, Zhiting Hu, Jason Weston, and Yuandong Tian.
     Training large language models to reason in a continuous latent space. arXiv preprint arXiv:2412.06769,
     2024. 4.1.1, 5.3

[31] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition.
     In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pages 770–778, 2016.
     2, 2.1, 4.3.2
[32] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Identity mappings in deep residual networks.
     In European conference on computer vision, pages 630–645. Springer, 2016. 2.1

[33] Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford,
     Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland,
     Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan,
     Erich Elsen, Oriol Vinyals, Jack W. Rae, and Laurent Sifre. Training compute-optimal large language
     models. In Advances in Neural Information Processing Systems, volume 35, pages 30016–30030. Curran
     Associates, Inc., 2022. 1, 1, 5.2, 5.4
[34] Gao Huang, Zhuang Liu, Laurens van der Maaten, and Kilian Q. Weinberger. Densely connected
     convolutional networks. In CVPR, pages 4700–4708, 2017. 2, 2.1
[35] Gao Huang, Zhuang Liu, Laurens van der Maaten, and Kilian Q. Weinberger. Densely connected
     convolutional networks. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition,
     pages 4700–4708, 2017. 4.3.2
[36] Yu Kang, Xianghui Sun, Liangyu Chen, and Wei Zou. C3ot: Generating shorter chain-of-thought without
     compromising effectiveness. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 39,
     pages 24312–24320, 2025. 4.2.2

[37] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray,
     Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models, 2020. 1, 1, 5.4
[38] Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and François Fleuret. Transformers are rnns: Fast
     autoregressive transformers with linear attention. In ICML, pages 5156–5165, 2020. 1
[39] Kimi Team. Attention residuals. arXiv preprint arXiv:2603.15031, 2026. 2.1, 4.3.2

[40] James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A. Rusu,
     Kieran Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-Barwinska, et al. Overcoming catastrophic
     forgetting in neural networks. Proceedings of the National Academy of Sciences, 114(13):3521–3526, 2017.
     5.1







[41] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph Gonzalez,
     Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving with
     pagedattention. In Proceedings of the 29th Symposium on Operating Systems Principles, pages 611–626.
     ACM, 2023. 5.4
[42] Yaniv Leviathan, Matan Kalman, and Yossi Matias. Fast inference from transformers via speculative
     decoding. In International Conference on Machine Learning, pages 19274–19286. PMLR, 2023. 4.2.1
[43] Xiang Li, John Thickstun, Ishaan Gulrajani, Percy S Liang, and Tatsunori B Hashimoto. Diffusion-lm
     improves controllable text generation. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and
A. Oh, editors, Advances in Neural Information Processing Systems, volume 35, pages 4328–4343. Curran
     Associates, Inc., 2022. 2.2, 4.1.3
[44] Yuhui Li, Fangyun Wei, Chao Zhang, and Hongyang Zhang. Eagle: speculative sampling requires
     rethinking feature uncertainty. In Proceedings of the 41st International Conference on Machine Learning,
     pages 28935–28948, 2024. 4.2.1
[45] Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John
     Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step, 2023. 1, 2.2
[46] Aiwei Liu, Cheng Shi, Chuhan Wu, Ci Lei, Di Lu, Donald He, Fan Zhang, Fanhao Kong, Feifei Zhang,
     Guan Wang, et al. Hidden decoding at scale: Latent computation scaling for large language models. arXiv
     preprint arXiv:2607.08186, 2026. 4.1.3
[47] Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Chenggang Zhao, Chengqi
     Deng, Chenyu Zhang, Chong Ruan, et al. Deepseek-v3 technical report. arXiv preprint arXiv:2412.19437,
     2024. 4.2.1

[48] Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, and David Ha. The ai scientist:
     Towards fully automated open-ended scientific discovery, 2024. 5.3
[49] Wenjie Ma, Jingxuan He, Charlie Snell, Tyler Griggs, Sewon Min, and Matei Zaharia. Reasoning models
     can be effective without thinking, 2025. 1
[50] Xinyin Ma, Guangnian Wan, Runpeng Yu, Gongfan Fang, and Xinchao Wang. Cot-valve: Length-
     compressible chain-of-thought tuning. In Proceedings of the 63rd Annual Meeting of the Association
     for Computational Linguistics (Volume 1: Long Papers), pages 6025–6035, 2025. 4.2.2
[51] Somesh Mehra, Javier Alonso Garcia, and Lukas Mauch. On multi-token prediction for efficient llm
     inference, 2025. 4.2.1

[52] Kevin Meng, David Bau, Alex Andonian, and Yonatan Belinkov. Locating and editing factual associations
     in gpt. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, editors, Advances in Neural
     Information Processing Systems, volume 35, pages 17359–17372. Curran Associates, Inc., 2022. 2
[53] Xupeng Miao, Gabriele Oliaro, Zhihao Zhang, Xinhao Cheng, Zeyu Wang, Zhengxin Zhang, Rae Ying Yee
     Wong, Alan Zhu, Lijie Yang, Xiaoxiang Shi, et al. Specinfer: Accelerating large language model serving
     with tree-based speculative inference and verification. In Proceedings of the 29th ACM International
     Conference on Architectural Support for Programming Languages and Operating Systems, Volume 3, pages
     932–949, 2024. 4.2.1
[54] Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettle-
     moyer, Percy Liang, Emmanuel Candès, and Tatsunori Hashimoto. s1: Simple test-time scaling. In
     Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose, and Violet Peng, editors, Proceedings of
     the 2025 Conference on Empirical Methods in Natural Language Processing, pages 20275–20321, Suzhou,
     China, November 2025. Association for Computational Linguistics. 1
[55] Shen Nie, Fengqi Zhu, Zebin You, Xiaolu Zhang, Jingyang Ou, Jun Hu, Jun Zhou, Yankai Lin, Ji-Rong
     Wen, and Chongxuan LI. Large language diffusion models. In D. Belgrave, C. Zhang, H. Lin, R. Pascanu,
P. Koniusz, M. Ghassemi, and N. Chen, editors, Advances in Neural Information Processing Systems,
     volume 38, pages 50608–50646. Curran Associates, Inc., 2025. 2.2, 4.1.3





[56] German I. Parisi, Ronald Kemker, Jose L. Part, Christopher Kanan, and Stefan Wermter. Continual lifelong
     learning with neural networks: A review. Neural Networks, 113:54–71, 2019. 5.1
[57] Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase, and Yuxiong He. Zero: Memory optimizations toward
     training trillion parameter models. In SC20: International Conference for High Performance Computing,
     Networking, Storage and Analysis, pages 1–16. IEEE, 2020. 5.4
[58] Bernardino Romera-Paredes, Mohammadamin Barekatain, Alexander Novikov, Matej Balog, M. Pawan
     Kumar, Emilien Dupont, Francisco J. R. Ruiz, Jordan Ellenberg, et al. Funsearch: Making new discoveries
     in mathematical sciences using large language models. Nature, 625:468–475, 2024. 5.3
[59] Adam Santoro, Sergey Bartunov, Matthew M. Botvinick, Daan Wierstra, and Timothy P. Lillicrap. One-shot
     learning with memory-augmented neural networks. CoRR, abs/1605.06065, 2016. 5.1
[60] Nikunj Saunshi, Nishanth Dikkala, Zhiyuan Li, Sanjiv Kumar, and Sashank J. Reddi. Reasoning with latent
     thoughts: On the power of looped transformers. In Y. Yue, A. Garg, N. Peng, F. Sha, and R. Yu, editors,
     International Conference on Learning Representations, volume 2025, pages 14855–14881, 2025. 4.1.2
[61] Julian Schrittwieser, Ioannis Antonoglou, Thomas Hubert, Karen Simonyan, Laurent Sifre, Simon Schmitt,
     Arthur Guez, Edward Lockhart, Demis Hassabis, David Silver, et al. Mastering atari, go, chess and shogi
     by planning with a learned model. Nature, 588:604–609, 2020. 5.2
[62] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan
     Zhang, Y. K. Li, Y. Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in
     open language models, 2024. 4.2.2
[63] Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff
     Dean. Sparsely-gated mixture-of-experts layers. In ICLR, 2017. 2.3
[64] Zhenyi Shen, Hanqi Yan, Linhai Zhang, Zhanghao Hu, Yali Du, and Yulan He. CODI: Compressing
     chain-of-thought into continuous space via self-distillation. In Christos Christodoulopoulos, Tanmoy
     Chakraborty, Carolyn Rose, and Violet Peng, editors, Proceedings of the 2025 Conference on Empirical
     Methods in Natural Language Processing, pages 677–693, Suzhou, China, November 2025. Association for
     Computational Linguistics. 4.1.1, 5.3
[65] Mingyang Song and Mao Zheng. Walk before you run! concise llm reasoning via reinforcement learning,
     2025. 4.2.2
[66] Rupesh K. Srivastava, Klaus Greff, and Jürgen Schmidhuber. Training very deep networks. In Advances in
     Neural Information Processing Systems, pages 2377–2385, 2015. 4.3.2
[67] Rupesh K. Srivastava, Klaus Greff, and Jürgen Schmidhuber. Highway networks. In ICML Deep Learning
     Workshop, 2015. 2
[68] Mitchell Stern, Noam Shazeer, and Jakob Uszkoreit. Blockwise parallel decoding for deep autoregressive
     models. Advances in Neural Information Processing Systems, 31, 2018. 4.2.1
[69] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Ł ukasz
     Kaiser, and Illia Polosukhin. Attention is all you need. In I. Guyon, U. Von Luxburg, S. Bengio, H. Wallach,
R. Fergus, S. Vishwanathan, and R. Garnett, editors, Advances in Neural Information Processing Systems,
     volume 30. Curran Associates, Inc., 2017. 1, 2, 4.3.1
[70] Yuru Wang, Lejun Cheng, Yuxin Zuo, Sihang Zeng, Bingxiang He, Che Jiang, Junlin Yang, Yuchong Wang,
     Kaikai Zhao, Weifeng Huang, Kai Tian, Zhenzhao Yuan, Jincheng Zhong, Weizhi Wang, Ning Ding, Bowen
     Zhou, and Kaiyan Zhang. Naturebench: Can coding agents match the published sota of nature-family
     papers?, 2026. 5.3
[71] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le,
     and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models. In NeurIPS,
     2022. 1, 2, 2.2, 4.1
[72] Jason Weston, Sumit Chopra, and Antoine Bordes. Memory networks. In ICLR, 2015. 5.1





[73] Heming Xia, Chak Tou Leong, Wenjie Wang, Yongqi Li, and Wenjie Li. Tokenskip: Controllable chain-
     of-thought compression in llms. In Proceedings of the 2025 Conference on Empirical Methods in Natural
     Language Processing, pages 3351–3363, 2025. 4.2.2
[74] Zhenda Xie, Yixuan Wei, Huanqi Cao, Chenggang Zhao, Chengqi Deng, Jiashi Li, Damai Dai, Huazuo
     Gao, Jiang Chang, Kuai Yu, Liang Zhao, Shangyan Zhou, Zhean Xu, Zhengyan Zhang, Wangding Zeng,
     Shengding Hu, Yuqing Wang, Jingyang Yuan, Lean Wang, and Wenfeng Liang. mhc: Manifold-constrained
     hyper-connections, 2026. 2.1

[75] Ruibin Xiong, Yunchang Yang, Di He, Kai Zheng, Shuxin Zheng, Chen Xing, Huishuai Zhang, Yanyan Lan,
     Liwei Wang, and Tieyan Liu. On layer normalization in the transformer architecture. In International
     conference on machine learning, pages 10524–10533. PMLR, 2020. 2.1
[76] Yige Xu, Xu Guo, Zhiwei Zeng, and Chunyan Miao. SoftCoT: Soft chain-of-thought for efficient reasoning
     with LLMs. In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar, editors,
     Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
     Papers), pages 23336–23351, Vienna, Austria, July 2025. Association for Computational Linguistics. 4.1.1
[77] Shiming Yang, Yuxuan Tong, Xinyao Niu, Graham Neubig, and Xiang Yue. Demystifying long chain-of-
     thought reasoning. In International Conference on Machine Learning, pages 71177–71209. PMLR, 2025.
     4.2.2

[78] Songlin Yang, Jan Kautz, and Ali Hatamizadeh. Gated delta networks: Improving mamba2 with delta
     rule. In The Thirteenth International Conference on Learning Representations, 2025. 1, 4.3.1
[79] Ping Yu, Jing Xu, Jason Weston, and Ilia Kulikov. Distilling system 2 into system 1, 2024. 4.2.2
[80] Defa Zhu, Hongzhi Huang, Zihao Huang, Yutao Zeng, Yunyao Mao, Banggu Wu, Qiyang Min, and Xun
     Zhou. Hyper-connections. In International Conference on Learning Representations, 2025. 2.1, 4.3.2
[81] Yicheng Zou et al. Intern-s1-pro: Scientific multimodal foundation model at trillion scale, 2026. 1







## A. Author List
## A.1. Core Contributors (Sorted by Contribution)

Algorithm Design:
  • Architecture: Ermo Hua* , Xiangyu Hong* , Che Jiang* , Baiting Wu, Cheng Liang, Youbang Sun, Biqing Qi,
    Qipeng Guo
  • Training: Baiting Wu* , Chengqi Lv* , Ermo Hua* , Xiangyu Hong* , Weida Wang, Ning Ding, Wenwei Zhang
Infrastructure:
  • Training: Hanjing Wang* , Xiangyu Hong* , Yicheng Gu* , Ermo Hua* , Shan Yu, Haozheng Hou, Jianmin
    Qian, Jie Hou, Zhongbo Tian, Hui Wang
  • Inference: Qian Yao* , Baiting Wu* , Ermo Hua* , Jifeng Ding, Ningsheng Ma, Han Lv, Minxi Jin, Zhongbo
    Tian, Hui Wang
Project Leader: Ermo Hua
Project Advisors: Qi Zhang, Kai Chen, Dahua Lin, Bowen Zhou

## A.2. Full List (Sorted by Character)
Kai Chen, Jifeng Ding, Ning Ding, Jiaye Ge, Lixin Gu, Yicheng Gu, Qipeng Guo, Ermo Hua, Haian Huang,
Haozheng Hou, Jie Hou, Xiangyu Hong, Che Jiang, Minxi Jin, Cheng Liang, Dahua Lin, Dawei Liu, Kuikun Liu,
Chengqi Lv, Haijun Lv, Han Lv, Ningsheng Ma, Biqing Qi, Jianmin Qian, Shiya Su, Youbang Sun, Huanze Tang,
Zhongbo Tian, Hanjing Wang, Rui Wang, Ting Wang, Yi Wang, Baiting Wu, Jun Xu, Bowen Yang, Hui Wang,
Weida Wang, Haochen Ye, Jiashuo Yu, Shan Yu, Xiaoyi Yu, Qirui Zeng, Qi Zhang, Ming Zhang, Wenwei Zhang,
Bowen Zhou, Xinyu Zhou


## B. Expert Activation Patterns
We further compare expert-activation pattern under two training recipes introduced in 3. As shown in 6, the
Mobius-7B model trained from scratch (left) exhibits a comparatively uniform activation distribution across
reasoning layers. Intern-S2-Mobius-35B (right), continually pre-trained from Qwen3.5-35B, activates experts
over a wider range while retaining a pronounced block-diagonal pattern. The latter suggests that expert routing
remains influenced by the layer-specific organization of the source checkpoint.
   These observations suggest that continual pre-training can broaden expert utilization without fully removing
the routing prior induced by architectural conversion. Training Mobius from scratch may therefore permit
more flexible access to the shared expert pool; whether this translates into stronger model capability requires
controlled evaluation at comparable scale.


## C. Toy Task of Compositional Generalization
We select a Compositional Generalization task from Physics of LLM [1]. On this task, we compared Transformer
against our yet-to-be-released, newer Mobius architecture. As shown in Fig 7, Mobius achieved substantially
better convergence efficiency and final scores. This compositional generalization task uses single-hop knowledge
of 500 entities and two-hop knowledge of 400 entities as the training set, and two-hop knowledge of the
remaining 100 entities as the test set. By comparing test-set scores, we examine whether the model can
genuinely learn the connections between different knowledge pieces and achieve compositional generalization.


## D. Case Study: Chain-of-Thought Reasoning
We further present an example from the field of biology in 3. In this case, Mobius also delivers a mush shorter
reasoning trace than Transformer.






Figure 6: Expert-Activation pattern across layers under two training recipes. The left panel shows Mobius-7B
trained from scratch; the right panel shows Intern-S2-Mobius-35B obtained by architecture conversion and
continual pre-training. Rows denote expert IDs, columns denote layer indices, and color represents the base-10
logarithm of selection frequency. Expert IDs in the right panel are reordered to reveal the inherited routing
structure.


## E. Layerwise Analysis of Latent Reasoning
We use a layerwise prediction lens to examine how token predictions evolve during latent computation.
Given the same teacher-forced context, we decode the hidden state at each layer for the standard next-token
prediction (𝑡 + 1) and four subsequent MTP positions (𝑡 + 2 to 𝑡 + 5). As shown in Figure 8, Mobius exhibits more
interpretable, target-aligned predictions in its intermediate layers than the baseline. Its layerwise predictions
follow a more coherent semantic trajectory, suggesting that task-relevant information is concentrated into
a compact internal representation rather than dispersed across competing token candidates. Further latent
iterations progressively refine this representation and improve predictions at subsequent positions, ultimately
yielding a fully accepted five-token draft. In contrast, the baseline exhibits less stable intermediate predictions,
and its draft is rejected at the third predicted position, leaving only a two-token accepted prefix. This example
suggests that Mobius may form more compact internal representations and refine them iteratively in latent
space, potentially benefiting multi-token prediction.








        Noe Graham                   Madison Frederick

 is mentor of                   is manager of

     Madison Frederick                  Jayla Stanley



   Q: Who is the mentor of manager of Jayla Stanley?
   A: Noe Graham.


                (a) Task Description                                               (a) Performance

Figure 7: The Compositional Generalization task selected from Physics of LLM. A future-version of Mo-
bius(unreleased) enjoys faster convergence, higher final scores than Transformer. The train set contains
500-entity single-hop + 400-entity two-hop, while the test set contains 100-entity two-hop holdout. This task
evaluates whether models learn cross-knowledge connections, not mere memorization.




Figure 8: Layerwise prediction lens for Mobius and the Qwen3.5 baseline under an identical teacher-forced
context. The 𝑡 + 1 column represents standard next-token prediction, while 𝑡 + 2 through 𝑡 + 5 are subsequent
MTP predictions. Each cell shows the token predicted from a given hidden-state view; color intensity denotes
its probability, and a black outline marks agreement with the target continuation. Mobius exhibits more
target-aligned intermediate predictions and produces a five-token draft accepted in full, while the baseline
produces only a two-token accepted prefix.








Table 3: Step-aligned comparison between Intern-Spin-35B and Qwen3.5-35B on a photosynthesis multiple-
choice question. Both models select the correct answer (Option D). Token counts are computed using the
Qwen3.5-35B tokenizer.

  Reasoning Trace Comparison
  Aligned Step                                   Intern-Spin-35B                                    Qwen3.5-35B
                                                                                                    35 tokens.
                                                   36 tokens.
                                                                                        “The user wants me to answer . . .
                                    “The user is asking a question about the
  Task framing                                                                        Question: The light reactions . . . supply
                                    relationship between the light reactions
                                                                                        the Calvin cycle with which of the
                                    and the Calvin cycle in photosynthesis.”
                                                                                                   following?”
                                                                                                      276 tokens.
                                                      108 tokens.
                                                                                     “Light-dependent reactions . . . Outputs:
                                    “Light-dependent reactions . . . producing
                                                                                      Oxygen (𝑂2 ), ATP, NADPH. . . . Calvin
  Core biological mechanism                oxygen, ATP, and NADPH.”
                                                                                       Cycle . . . Inputs: 𝐶𝑂2 , ATP, NADPH.”
                                     “Calvin cycle . . . uses ATP and NADPH
                                                                                     “. . . reduction requires ATP and NADPH
                                           . . . to fix 𝐶𝑂2 into sugars.”
                                                                                                          ...”
                                                                                                     543 tokens.
                                                   240 tokens.
                                                                                       “D . . . Correct. The light reactions
                                        “D: ATP provides energy, NADPH
                                                                                       generate ATP (energy) and NADPH
                                       provides high-energy electrons . . . ”
  Option evaluation                                                                      (reducing power/electrons). . . . ”
                                      “H: ATP and NADPH are produced in
                                                                                     “H . . . ATP and NADPH are produced in
                                     light reactions, not broken down there
                                                                                     the light reactions and consumed . . . in
                                                       ...”
                                                                                                  the Calvin cycle.”
                                                                                                    205 tokens.
                                                                                        “Conclusion: Option D accurately
                                                                                      describes the relationship . . . ATP and
                                                                                      NADPH . . . are used in the Calvin cycle
  Repeated derivation                                    —
                                                                                                   to fix carbon.”
                                                                                       “Step-by-step derivation: . . . Light
                                                                                      Reactions produce ATP and NADPH →
                                                                                        Calvin Cycle consumes them. . . . ”
                                                                                                      143 tokens.
                                                                                     “Final check: . . . Option A: 𝐶𝑂2 source
  Repeated option check                                  —
                                                                                       is wrong. . . . Option D: ATP/NADPH
                                                                                              transfer is correct. . . . ”
                                                  13 tokens.
                                                                                                      8 tokens.
  Reasoning closure                   “Conclusion: Option D is the correct
                                                                                              “The correct option is D.”
                                                   answer.”
                                                                                                       439 tokens.
                                                                                     “The process of photosynthesis is divided
                                                   75 tokens.
                                                                                           into two main stages . . . ATP and
                                     “The light reactions . . . stored in ATP
                                                                                     NADPH . . . are transported to the Calvin
  Visible final answer               and NADPH. These molecules are then
                                                                                                          cycle.”
                                          used in the Calvin cycle . . . ”
                                                                                      “. . . D: This states ATP and NADPH are
                                                 “ANSWER: D”
                                                                                             supplied. This is accurate. . . . ”
                                                                                                     “ANSWER: D”
  Total                                             472 tokens                                      1,649 tokens
   Note: The token counts are sequential marginal counts over each raw prediction; therefore, they sum exactly to the total output
   length. The displayed excerpts are representative original text from the corresponding reasoning segment. Ellipses indicate
   omitted original text.





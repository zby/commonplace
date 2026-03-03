---
source: https://arxiv.org/pdf/2602.18333
captured: 2026-03-03
capture: pdf-read
type: academic-paper
---

# On the "Induction Bias" in Sequence Models

Author: M. Reza Ebrahimi, Michaël Defferrard, Sunny Panchal, Roland Memisevic (Qualcomm AI Research)
Source: https://arxiv.org/pdf/2602.18333
Date: 20 Feb 2026

## Abstract

Despite the remarkable practical success of transformer-based language models, recent work has raised concerns about their ability to perform state tracking. In particular, a growing body of literature has shown this limitation primarily through failures in out-of-distribution (OOD) generalization, such as length extrapolation. In this work, we shift attention to the in-distribution implications of these limitations. We conduct a large-scale experimental study of the data efficiency of transformers and recurrent neural networks (RNNs) across multiple supervision regimes. We find that the amount of training data required by transformers grows much more rapidly with state-space size and sequence length than for RNNs. Furthermore, we analyze the extent to which learned state-tracking mechanisms are shared across different sequence lengths. We show that transformers exhibit negligible or even detrimental weight sharing across lengths, indicating that they learn length-specific solutions in isolation. In contrast, recurrent models exhibit effective amortized learning by sharing weights across lengths, allowing data from one sequence length to improve performance on others. Together, these results demonstrate that state tracking remains a fundamental challenge for transformers, even when training and evaluation distributions match.

## 1. Introduction

State tracking is a key capability of most intelligent systems and of most models of computation. It is the process of monitoring and updating the status of an entity or process with which the system interacts over a period of time. State tracking is particularly important in multi-hop, interactive tasks, such as that of an agent interacting with an interface or of a dialogue system interacting with a user across multiple turns.

State tracking has become a popular area of investigation in recent years, especially in the study of LLM capabilities and failure modes. In this context, numerous studies have shown that transformer-based models are fundamentally limited in their ability to perform state tracking (for example, Anil et al., 2022; Dziri et al., 2024). This contrasts with recurrent networks, which excel at state tracking (although their wide-spread applicability is unfortunately hampered by their relative training inefficiency). The limitations of transformers have been demonstrated as limitations in out-of-distribution (OOD) generalization, specifically length-generalization: after training models on tasks encoded in sequences of a given range of lengths, they were evaluated on sequences with lengths that were not seen during training. In these scenarios, the trained models fail to consistently generate correct outputs on the evaluation data, although they are able to solve the tasks for even unseen sequences in the training range of lengths.

It could be argued that in any real-world use cases, OOD state tracking failures may not be an issue as long as enough training data with step-by-step sequential supervision is available. If training data covers all sequence lengths that may be encountered at inference time, inference can rely entirely on in-distribution generalization. Unfortunately, although this argument is true in principle, it is hard to quantify "enough" in this context. It is also hard to quantify how the amount of training data required for any given task may depend on the length of the sequences and the size of the state space.

A key difference between transformer-based and recurrent models is that, at every timestep, the former compute outputs by applying a function that depends on all inputs and outputs generated previously (the context window), making it possible, in principle, to re-calculate the required state from the past information globally at each time step. Recurrent networks, on the other hand, compute outputs by applying a function that depends on only the current hidden state, making it impossible to perform such a re-calculation. This makes it strictly necessary for a recurrent network to encode any relevant information from the past within a single hidden state vector. This inductive bias encourages a recurrent network to incorporate the information from the current timestep into its representation of state at the moment where this information is available. Conversely, it discourages it from "saving" this information off to determine future state updates globally from the past information. The immediate state updates thus encourage the network to process the input sequence step-by-step, making any state update explicit as soon as this is possible, rather than potentially deferring such updates to a later point in time.

Such step-by-step state updates are a natural inductive bias (Mitchell, 1997) in the context of simple state tracking tasks, as they make it possible to reduce complex multi-step dependencies to a sequence of single-step computations. They also allow a model to share weights across multiple different sequence lengths, as it breaks state updates into single-step, repeatable computations. By analogy to the induction step in a mathematical proof, we shall refer to this kind of inductive bias in this work as "induction bias" (sic).

Formally, the presence of the induction bias in a model means that the joint distribution over tokens, conditioned on the most recent hidden state, factorizes, such that p(x_{t+1}|x_1,...,x_t,h_t) = p(x_{t+1}|x_t,h_t), where x_t is the t-th token and h_t is the hidden state in timestep t, representing a minimal sufficient statistic for determining x_{t+1}.

We show that the presence (or respectively absence) of an induction bias, or its relative strength, provides a simple explanation for a wide range of the empirical findings we present.

Key take-aways from our study include the following:

- We show that there is a distinct difference between the supervision regimes in which transformers and recurrent networks perform well in-distribution.
- We show that transformers can relatively efficiently learn state tracking tasks in-distribution on one (fixed) sequence length at a time, but generalizing in-distribution over multiple sequence lengths requires significantly more training data.
- We present evidence that, unlike recurrent networks, transformers tend to fail at sharing parameters across sequence lengths and instead learn separate solution mechanisms for different lengths.
- We show that the degree of knowledge transfer across multiple different sequence lengths in the in-distribution setting is highly correlated with the ability of a model to length-generalize.

### 1.1. Related Work

A range of studies has shown that transformer-based sequence models fail to length-generalize in state tracking tasks (Anil et al., 2022; Deletang et al., 2023; Dziri et al., 2024; Abbe et al., 2024; Ebrahimi et al., 2024). Unlike our work, these studies solely discuss OOD scenarios, while we discuss in-distribution data efficiency instead.

The inability to length-generalize in state tracking tasks has been shown to hold also for most existing state-space models (SSM) (Sarrof et al., 2024; Merrill et al., 2024; Cirone et al., 2024; Shakerinava et al., 2026). However recent work has shown that making the hidden-to-hidden transition matrix in the SSM input-dependent and non-diagonal can recover the ability to length-generalize (Fan et al., 2024; Grazzi et al., 2025; Ebrahimi & Memisevic, 2025; Terzic et al., 2025a;b).

Liu et al. (2023); Li et al. (2025) show that transformers solve state tracking tasks in-distribution by making use of parallel mechanisms reminiscent of associative scan. While this view can help explain the OOD failures of these models, it also hints at the absence of an "induction" bias which affects data efficiency as we show in this work.

## 2. Methodology

**Task:** We consider the task of modular addition, where a model is provided a sequence of n integers x = (x_1, x_2, ..., x_n) with each x_i drawn uniformly at random from Z_m = {0, 1, ..., m-1}. The objective is to compute the sum of the sequence modulo m:

y = (sum_{i=1}^{n} x_i) (mod m), x_i in Z_m.

For m = 2, the task reduces to computing the parity of a binary sequence. From an algebraic perspective, modular addition over Z_m (cyclic group) serves as the canonical representative for commutative operations, as every finite abelian group is isomorphic to a direct product of such cyclic groups.

We also experiment with non-commutative operations by considering the task of permutation composition over the symmetric group S_5. This task serves as the canonical non-commutative counterpart for state tracking, as by Cayley's Theorem, every finite group is isomorphic to a subgroup of a symmetric group.

**Length Distributions:** For each generated sample, we first determine the sequence length n in {2, ..., L}, where L denotes the maximum sequence length. We then sample a sequence x in Z_m^n without replacement to ensure that every sample in the dataset is unique. We use three distinct strategies for length selection:

1. **Fixed:** The length is held constant at n = L.
2. **Uniform:** Lengths are sampled uniformly at random from the set {2, ..., L}.
3. **Short-to-Long:** Sequences are sampled in ascending order of length, exhausting the available sequences for length n before proceeding to n+1.

**Task Formats:** We consider three task formats that vary in the density and structure of the supervision signal. Let s_k = (sum_{i=1}^k x_i) (mod m) denote the k-th partial sum of the input sequence. The formats, illustrated in Figure 1, are defined as follows:

1. **Outcome Supervision:** The model is provided the input sequence x and is trained to predict only the final sum s_n. This format provides no intermediate supervision, requiring the model to discover the latent computational logic of the task on its own during training.
2. **Chain-of-Thought (CoT):** The model is trained to generate the sequence of intermediate partial sums (s_1, s_2, ..., s_n) following the input sequence. This decomposes the task into a sequence of iterative applications of the operator.
3. **Aligned Chain-of-Thought (ACoT):** The model is tasked to output, for each input token x_i, the corresponding partial sum s_i. While conceptually similar to CoT, this format provides per-token supervision that is aligned with the input. This format is similarly used in prior work (Li et al., 2025; Zhang et al., 2025) and is also referred to as state-supervision.

Unlike outcome supervision, both CoT and ACoT constitute a form of process supervision, as they provide explicit training signals for the intermediate solution steps.

**Sample Efficiency:** To quantify the data efficiency of a model under a specific task configuration, we define the minimal sample size N* required to learn the task reliably. We consider a task successfully learned if the minimum validation loss over the hyperparameter grid falls below a convergence threshold.

**Models:** We compare multi-layer decoder-only transformer architecture (Vaswani et al., 2017), with two recurrent alternatives: Long Short-Term Memory (LSTM) (Hochreiter & Schmidhuber, 1997) and dense state-space models (Dense-SSMs) (Fan et al., 2024; Terzic et al., 2025a; Ebrahimi & Memisevic, 2025).

In Dense-SSMs, the state transition matrix is dense and fully input-dependent, a property shown to support effective state tracking in linear recurrent models (Merrill et al., 2024). We adopt the variant used by Ebrahimi & Memisevic (2025), in which input-state interactions are purely multiplicative with no additive terms: h_t = A_{x_t} h_{t-1}, where the transition matrix A_{x_t} is given by a linear function of the input x_t. This architecture is commonly referred to as a bilinear RNN, since h_t depends bilinearly on the input and the previous hidden state.

**Experimental Setup:** We perform a large-scale systematic evaluation of data efficiency on synthetic state-tracking tasks. To estimate N*, we use a hybrid binary-geometric search procedure that evaluates candidate sample sizes over at most 20 steps, training models across a hyperparameter grid of 3 learning rates and 5 random seeds (15 configurations total for each size N). A sample size is considered successful if at least one configuration achieves validation loss below epsilon = 10^{-4}. Each model is trained for a fixed budget of 250k optimization steps independent of the training set size N. This amounts to over 190,000 training runs for the results reported in this paper, excluding development runs.

The transformer model used is based on the GPT-2 architecture (Radford et al., 2019) with 6 layers and a model (embedding/hidden) dimension of 256. Both the LSTM and Dense-SSM models use a single-layer recurrent cell followed by a linear classification head. We use an input and hidden dimension of 768 for the LSTM and 256 for the Dense-SSM. We also experiment with a 2-layer transformer and a LSTM with hidden dimension of 256.

## 3. In-distribution Data Efficiency

We perform the above binary search procedure to identify the minimal dataset size (N*) across all combinations of maximum sequence length L in {5, 10, 20, 30} and modulus m in {2, 3, 5, 10, 15, 20, 50, 75, 100}, for each of the three task formats, length distributions, and models described earlier. From the table we can infer the following key observations:

**Observation 3.1:** Transformers prefer non-aligned supervision (Chain of Thought).

We observe a clear preference for CoT over the Aligned CoT format for transformers. For example, at m = 5 and L = 20, CoT requires 1.7K samples, while Aligned CoT requires 2M, an order-of-magnitude increase in sample complexity. It has been hypothesized that by outputting intermediate steps autoregressively, the model can attend to its own previous outputs, effectively simulating a larger depth circuit (Li et al., 2024), and the results confirm this hypothesis. In contrast, Aligned Chain-of-Thought forces the model to compress the computation into a single forward pass per token without the benefit of re-attending to intermediate results, which appears less aligned with the transformer's non-recurrent nature.

**Observation 3.2:** Recurrent models prefer aligned supervision (Aligned Chain-of-Thought).

Conversely, recurrent models (LSTMs and Dense-SSMs) demonstrate superior sample efficiency when trained with the Aligned CoT (ACoT) format, which provides supervision aligned with the evolution of the hidden state. In contrast, RNNs struggle with CoT, which is likely due to their recall bottleneck (Wen et al., 2025; Phan et al., 2025): a model must output the sequence of partial sums (s_1, ..., s_n) after processing the entire input sequence. This effectively requires it to unroll the chain of intermediate computations from the beginning. In fact, we note that under the CoT format, recurrent models even fail to generalize to longer sequences despite their sequential inductive bias (see Table 2 for length-generalization results). The task thereby becomes bottlenecked by the model's limited memory capacity rather than its state-tracking ability.

**Observation 3.3:** Recurrent models outperform transformers in the absence of intermediate supervision.

In the Outcome Supervision setting, the model must implicitly infer the latent algebraic structure of the task solely from the final solution, without any guidance on the intermediate steps. This requires the model to effectively marginalize over unobserved computational paths with difficulty scaling with both the state space size m and sequence length n.

We observe that recurrent models significantly outperform transformers in this regime. While transformers fail to converge for all but the most trivial configurations (very small m and n), the recurrent architectures successfully learn the task for higher moduli and extended sequence lengths, achieving convergence with orders of magnitude fewer training samples.

**Observation 3.4:** With intermediate supervision, longer sequences improve the data efficiency of recurrent models but not transformers.

Intuitively, under formats with intermediate supervision (CoT or ACoT), longer sequences should improve sample efficiency. This is because with intermediate solutions, the effective amount of supervised tokens increases linearly with sequence length.

We validate this hypothesis in recurrent models trained with Aligned Chain-of-Thought: the fixed length distribution (comprising only longest sequences) yields the highest data efficiency, followed by uniform, and finally short-to-long. Furthermore, in the uniform setting, we find that recurrent models trained with ACoT require fewer data points as the maximum sequence length L increases, as expected. In contrast, transformers trained with CoT fail to leverage this additional supervision.

**Observation 3.5:** With outcome supervision, short sequences are more valuable for learning than long sequences in recurrent models.

In the Outcome Supervision setting, we compare the data requirements under the uniform and short-to-long length distributions. We observe that recurrent models require fewer training samples in the short-to-long setting, suggesting that shorter sequences provide a stronger learning signal than longer sequences for these models.

## 4. Weight Sharing Across Sequence Length

A key hypothesis for why recurrent networks dominate transformers with respect to data efficiency, as shown in the previous section, is that their "induction bias" encourages step-by-step updates to their representations of state. This, in turn, should allow the model to share the same solution mechanisms across the whole sequence length.

In this section, we investigate the extent to which the learned mechanisms are shared across different sequence lengths. Specifically, we examine whether the model develops length-specific heuristics, effectively "specialized circuits" for fixed-length sequences, or whether it has internalized the inherent inductive structure of the task. The latter implies the discovery of a transition operator that can be applied iteratively.

We quantify the cross-length mechanism sharing through the lens of sample efficiency. Intuitively, if a model utilizes a shared mechanism (e.g., a transition operator) across varying lengths, the sample cost to learn the task over a distribution of lengths should be significantly lower than the sum of costs to learn each length individually. This is due to the amortization of the learning cost: the data required to learn the operation at length n simultaneously contributes to the model's learning at length n+k.

Formally, we compare the total number of training examples required for a model to simultaneously learn the task for all sequence lengths n in {2, ..., L} (the joint task) against the sum of samples required by L-1 independent models, each optimized for a single fixed length. Let N*_joint denote the minimal sample size required for the joint task, and N*_n denote the minimal sample size for a model trained and evaluated exclusively on sequences of length n. We define the Sharing Factor kappa as:

kappa = (sum_{n=2}^{L} N*_n) / N*_joint

The value of kappa provides insight into the extent of across-length mechanism sharing:

- kappa > 1 indicates mechanism sharing and amortized learning. This suggests the model has internalized the inductive nature of the task, and data from one sequence length accelerates the acquisition of the task across the entire distribution.
- kappa ~= 1 suggests that the model learns length-specific solutions in isolation, effectively partitioning capacity into independent circuits.
- kappa < 1 represents a regime of destructive interference. In this case, the length-specific solutions compete for model capacity, making it more data-efficient to train separate models for each length than to optimize a single model for the joint task.

**Observation 4.1:** Transformers have low sharing factor for all task formats.

As demonstrated, we observe a low sharing factor in transformers across all task formats, with kappa ~= 1 or kappa < 1 in all cases. Notably, in the Chain-of-Thought (CoT) setting, despite being transformer's most efficient task configuration, we observe an extreme case of length isolation (kappa = 0.28).

**Observation 4.2:** Transformers show destructive interference with CoT.

The observed sharing factor of kappa << 1 for transformer with CoT indicates a regime of destructive interference where length-specific solutions compete for model capacity, such that training on a diverse length distribution is substantially less data-efficient than training independent models on each length.

**Observation 4.3:** Recurrent networks have high sharing factors in their preferred task formats.

In contrast, both recurrent models exhibit clear evidence of mechanism sharing and amortized learning across sequence lengths (kappa >> 1) under the Outcome Supervision and Aligned Chain-of-Thought formats. However, this is no longer the case in the Chain-of-Thought format (kappa ~= 1), where the recurrent models also fail to share across the sequence lengths, likely due to the previously discussed recall bottleneck. However, unlike transformers, we do not observe destructive interference in this case.

**Observation 4.4:** Longer sequences increase data efficiency for Dense-SSMs.

As noted in the previous section, the sample requirement for the Dense-SSM under ACoT decreases as the maximum sequence length L increases. This indicates that through cross-length mechanism sharing, the model leverages the higher density of supervision signals in longer sequences.

**Observation 4.5:** OOD generalization implies high sharing factor, and vice versa.

Interestingly, we observe a consistent correlation between the sharing factor kappa and length generalization: cases with high sharing factor (kappa >> 1) correspond to those in which the model learns a length-generalizable solution (see Table 2). Conversely, cases with low sharing factor (kappa <= 1) are precisely those in which the learned solution fails to extrapolate beyond the training sequence lengths.

This provides additional evidence that in-distribution data efficiency and circuit sharing are fundamental implications of length generalization in state tracking.

## 5. Conclusions

Our study indicates that state tracking poses severe challenges for transformer-based sequence models not only out-of-distribution but also in-distribution: They require extraordinarily large amounts of training data to generalize on simple tasks and require Chain-of-Thought supervision to learn in-distribution on even moderate sequence lengths. This suggests that end-to-end learning in applied "agentic" scenarios, such as robotics or GUI control, could be even more challenging. The fact that data requirements scale with sequence length may also help explain well-known challenges at large context lengths ("context rot").

We study performance across a limited, albeit representative, number of models and task types. Unfortunately, the large search space over parameters (performed using binary search in our experiments) requires a number of many thousand individual training runs. This makes this comparison highly computationally demanding even for the current set of models and tasks. However, as models were chosen to be simple and representative it seems very likely that the findings will persist even under slight model variations, similar to how they did in previous OOD studies.

## Appendix A. Implementation Details

### A.1. Search Procedure for Determining N*

To identify the minimal sample size N* required for a model to successfully learn a target task, we use a hybrid Binary-Geometric search as described in Algorithm 1. The algorithm conducts a search over sample sizes, combining an initial exponential reduction phase with a subsequent binary search phase.

The search begins at a predefined maximum sample size N_max. For any candidate size N, the algorithm trains models using multiple configurations drawn from a fixed hyperparameter grid Phi. In our implementation, each evaluation consists of 15 model instances (3 learning rates x 5 random seeds). A sample size N is considered successful if at least one configuration attains validation loss below a threshold epsilon, in which case we decrease the next sample size, and otherwise, the size is labeled unsuccessful and the next trial size is increased.

We use a geometric multiplier of M = 1000, a maximum of S = 20 search steps, and a success threshold of epsilon = 10^{-4}. The hyperparameter grid is Phi = {LR in {10^{-3}, 10^{-4}, 10^{-5}}} x {seed in {10, 20, 30, 40, 50}}, yielding 15 configurations per evaluation. Each model is trained for a fixed budget of 250k optimization steps with batch size 64 using the Adam optimizer (Kingma & Ba, 2014), independent of the training set size N. This implies a maximum feasible sample size of N_max = 250,000 x 64 = 16M.

### A.2. Evaluation

We ensure that the training and validation sets are strictly disjoint. The validation set contains 2,000 samples (or at most 20% of the available data) and remains identical across different training set sizes, except for variations introduced by the random seed. In addition, we always use at most 20% of the available samples at each sequence length for validation, with the remainder reserved exclusively for training. Also, for all tasks, multi-digit integers are represented as single tokens during tokenization. Finally, for the Chain-of-Thought task format, validation loss is computed using teacher forcing rather than autoregressive sampling.

### A.3. Models

The transformer model is based on the GPT-2 architecture (Radford et al., 2019), with 6 layers and a model (embedding/hidden) dimension of 256. Other architectural parameters, including an MLP expansion factor of 4, follow the default GPT-2 (small) settings.

Both the LSTM and Dense-SSM use a single-layer recurrent cell followed by a linear classification head to map the hidden state to token logits. We use an input and hidden dimension of 768 for the LSTM, and 256 for the Dense-SSM. We also experiment with a 2-layer transformer and a single-layer LSTM with a hidden dimensionality of 256.

## Appendix B. Additional Experimental Results

### B.1. Evaluating Length-generalization

Table 2 reports accuracy on sequences of length 2x the maximum length used during training, normalized such that 0 corresponds to random chance. All models are trained using the maximum available training set size for each configuration.

Key finding: LSTM and Dense-SSM with Aligned Chain-of-Thought achieve near-perfect length generalization (accuracy ~= 1.00) across virtually all configurations tested. Transformers achieve near-zero length generalization accuracy across all formats and configurations.

### B.2. Permutation Composition Task

To show our findings generalize beyond commutative operations, we consider the task of permutation composition (simulating the symmetric group S_m). Each element of the group represents a permutation of the set {1, ..., m}, resulting in a group of cardinality |S_m| = m!. In our experimental setup, each permutation pi in S_m is bijectively mapped to a unique integer token in {0, 1, ..., m-1}. Given an input sequence of n permutations x = (pi_1, pi_2, ..., pi_n), the model is required to compute their sequential composition:

y = pi_n ∘ pi_{n-1} ∘ ... ∘ pi_1,

where ∘ denotes the permutation composition operator. This task significantly elevates the complexity of state tracking, as the model can no longer rely on the order-invariance property characteristic of abelian groups.

The symmetric group S_m serves as the canonical non-commutative structure for evaluating state tracking. Its fundamental importance is grounded in Cayley's Theorem, which states that every finite group G is isomorphic to a subgroup of the symmetric group S_{|G|}. Hence, by analyzing performance on S_m, we effectively probe the model's capacity to internalize the transition dynamics of any finite discrete group.

As noted in Figure 7, we observe the same patterns described in Section 4 and Figure 6, supporting the generalization of these findings and the subsequent arguments to non-commutative state-tracking tasks.

## References

- Abbe, E., Bengio, S., Lotfi, A., Sandon, C., and Saremi, O. How far can transformers reason? the globality barrier and inductive scratchpad. Advances in Neural Information Processing Systems, 37:27850-27895, 2024.
- Anil, C., Wu, Y., Andreassen, A., Lewkowycz, A., Misra, V., Ramasesh, V., Slone, A., Gur-Ari, G., Dyer, E., and Neyshabur, B. Exploring length generalization in large language models. Advances in Neural Information Processing Systems, 35:38546-38556, 2022.
- Cirone, N. M., Orvieto, A., Walker, B., Salvi, C., and Lyons, T. Theoretical foundations of deep selective state-space models. In The Thirty-eighth Annual Conference on Neural Information Processing Systems, 2024.
- Deletang, G., Ruoss, A., Grau-Moya, J., Genewein, T., Wenliang, L. K., Catt, E., Cundy, C., Hutter, M., Legg, S., Veness, J., and Ortega, P. A. Neural networks and the chomsky hierarchy. In The Eleventh International Conference on Learning Representations, 2023.
- Dummit, D. S., Foote, R. M., et al. Abstract algebra, volume 3. Wiley Hoboken, 2004.
- Dziri, N., Lu, X., Sclar, M., Li, X. L., Jiang, L., Lin, B. Y., Welleck, S., West, P., Bhagavatula, C., Le Bras, R., et al. Faith and fate: Limits of transformers on compositionality. Advances in Neural Information Processing Systems, 36, 2024.
- Ebrahimi, M. and Memisevic, R. Revisiting bi-linear state transitions in recurrent neural networks. In The Thirty-ninth Conference on Neural Information Processing Systems, 2025.
- Ebrahimi, M., Panchal, S., and Memisevic, R. Your context is not an array: Unveiling random access limitations in transformers. In First Conference on Language Modeling, 2024.
- Fan, T.-H., Chi, T.-C., and Rudnicky, A. Advancing regular language reasoning in linear recurrent neural networks. In NAACL (Short Papers), pp. 45-53, 2024.
- Grazzi, R., Siems, J., Franke, J. K., Zela, A., Hutter, F., and Pontil, M. Unlocking state-tracking in linear RNNs through negative eigenvalues. In The Thirteenth International Conference on Learning Representations, 2025.
- Hochreiter, S. and Schmidhuber, J. Long short-term memory. Neural computation, 9(8):1735-1780, 1997.
- Kingma, D. P. and Ba, J. Adam: A method for stochastic optimization. CoRR, abs/1412.6980, 2014.
- Li, B. Z., Guo, Z. C., and Andreas, J. (how) do language models track state? In Forty-second International Conference on Machine Learning, 2025.
- Li, Z., Liu, H., Zhou, D., and Ma, T. Chain of thought empowers transformers to solve inherently serial problems. In The Twelfth International Conference on Learning Representations, 2024.
- Liu, B., Ash, J. T., Goel, S., Krishnamurthy, A., and Zhang, C. Transformers learn shortcuts to automata. In The Eleventh International Conference on Learning Representations, 2023.
- Merrill, W., Petty, J., and Sabharwal, A. The illusion of state in state-space models. In International Conference on Machine Learning, pp. 35492-35506. PMLR, 2024.
- Mitchell, T. M. Machine learning, volume 1. McGraw-hill New York, 1997.
- Phan, B., Ebrahimi, R., Haresh, S., and Memisevic, R. Delayed attention training improves length generalization in transformer-rnn hybrids. What Can('t) Transformers Do? Workshop at NeurIPS, 2025.
- Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., Sutskever, I., et al. Language models are unsupervised multitask learners. OpenAI blog, 1(8):9, 2019.
- Sarrof, Y., Veitsman, Y., and Hahn, M. The expressive capacity of state space models: A formal language perspective. In The Thirty-eighth Annual Conference on Neural Information Processing Systems, 2024.
- Shakerinava, M., Khavari, B., Ravanbakhsh, S., and Chandar, S. The expressive limits of diagonal SSMs for state-tracking. In The Fourteenth International Conference on Learning Representations, 2026.
- Terzic, A., Hersche, M., Camposampiero, G., Hofmann, T., Sebastian, A., and Rahimi, A. On the expressiveness and length generalization of selective state-space models on regular languages. In Proceedings of the AAAI Conference on Artificial Intelligence, 2025a.
- Terzic, M., Rahimi, A., and et al. Structured sparse transition matrices to enable state tracking in state-space models. In NeurIPS 2025, 2025b.
- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., and Polosukhin, I. Attention is all you need. Advances in neural information processing systems, 30, 2017.
- Wen, K., Dang, X., and Lyu, K. RNNs are not transformers (yet): The key bottleneck on in-context retrieval. In The Thirteenth International Conference on Learning Representations, 2025.
- Zhang, D. W., Defferrard, M., Rainone, C., and Memisevic, R. Grounding code understanding in step-by-step execution, 2025.

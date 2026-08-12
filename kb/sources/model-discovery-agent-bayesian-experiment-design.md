---
source: https://arxiv.org/abs/2608.09696v1
description: Paper coupling LLM-proposed mechanistic hypotheses with Bayesian inference and value-of-information experiment design across physics, chemistry, and neuroscience benchmarks
captured: 2026-08-12
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Model Discovery Agent: LLM-assisted Bayesian Experiment Design

*For Data-efficient Discovery of Mechanistic World Models*

Author: Kevin Murphy

Source: https://arxiv.org/abs/2608.09696v1

Date: 10 August 2026

## Abstract

Predicting the answer to interventional “what if” questions — the outcome of an
action never taken — requires a mechanistic, causal model, not a curve fit; and
learning such a model requires experiments, because passive data leaves its mechanisms unidentified. Experiments are expensive, so the central problem is data
efficiency. We present the Model Discovery Agent (MDA), which couples a large
language model (LLM), used as a proposer of candidate structures, with standard
Bayesian machinery — sequential Monte Carlo (SMC) for parameter and structure posteriors, simulation-based inference (SBI) for intractable likelihoods, and
value-of-information (VoI) for experiment design — to discover latent mechanistic world models from few interventions. MDA operates in the M-open setting:
when the truth lies outside the current hypothesis class, a predictive check flags
the inadequacy and the proposer expands the hypothesis space with a new model
whose parameters are then identified by designed experiments. We show that discovery and design reinforce: the design step identifies the mechanism the discovery step proposes, and the identified mechanism improves predictions, enabling
further discoveries from the remaining unexplained residuals. On three different
benchmarks — covering physics (FORCEBENCH, (Wiemann et al., 2026)), chemistry (CHEMBENCH, (Kabra et al., 2026)) and biology (NEURONBENCH, a new
partially observed single-neuron electrophysiology benchmark we create) — we
show that MDA sets a new SOTA in terms of data-efficient model learning and
reliable interventional forecasting ability.

## 1 Introduction

Much of what we want from a predictive model is interventional: not “what will happen?” but
“what would happen if I did a?” (e.g., predicting the effect of administering a drug to a patient
that it has never received, launching a probe on an orbit it has never flown, or deploying a policy
never enacted before). Such interventional questions cannot in general be answered by a model fit to
passive observation, however flexible: two mechanisms can agree on all observed data yet disagree
under intervention. Answering interventional queries requires a mechanistic or causal model of
the data-generating process (Pearl, 2009; Richens & Everitt, 2024).1 Such mechanistic models are
also the foundation of true scientific understanding (Salmon, 1984; Krenn et al., 2022; Messeri &
Crockett, 2024; Bajorath, 2025; Serre & Pavlick, 2025; Kramer et al., 2026).
Unfortunately, a latent mechanistic model is typically unidentifiable from observation alone: the
passive data underdetermines it, and only intervening — perturbing the system and watching how
it responds — breaks the degeneracy. But experiments are expensive (a lab assay, a clinical trial),
1
Note that this paper is concerned with “level 2” causality, to use the terminology of Pearl’s causal ladder
(Pearl, 2009; Bareinboim et al., 2022); this can be handled with standard decision-theoretic machinery (Dawid,
2015), and does not need the more complex machinery required for “level 3” counterfactual reasoning (Dawid,
2000).

which makes the operative problem data efficiency: identify the mechanism, well enough to answer
the queries, in as few experiments as possible. This is the classical remit of Bayesian experimental
design — choose the intervention whose outcome is most informative (Lindley, 1956; Chaloner &
Verdinelli, 1995; Rainforth et al., 2024) — but it has rarely2 been combined with the open-ended
hypothesis creation that scientific discovery demands.
To tackle these problems, we present the Model Discovery Agent (MDA). This uses a large language model (LLM), which contains useful prior knowledge (Kıcıman et al., 2024), to propose
candidate mechanisms, given a natural-language description of the domain and any initial observational data. We then combine this with standard Bayesian machinery: sequential Monte Carlo
(SMC) for computing the posterior over parameters and structures and the model evidence, and
value-of-information (VoI) maximization for choosing the next experiment. We extend the standard
Bayesian machinery to the M-open regime, where the true mechanism may lie outside the proposed
hypothesis class (Bernardo & Smith, 1994; Kelter, 2020). We do this by testing if the current best
hypothesis fails an out-of-sample predictive check; if so, we expand the hypothesis space (using
the LLM), and then design an experiment to identify the new model’s parameters (using VoI). We
find that discovery and design reinforce each other: the experiment identifies the novel mechanism
the proposal introduced, and the identified mechanism improves the model’s forecasts, enabling the
detection of ever more subtle predictive errors (c.f., (Buehler, 2026)).
We validate MDA on three sets of benchmarks, covering physics (FORCEBENCH, based on
(Wiemann et al., 2026)), chemistry (CHEMBENCH, based on (Kabra et al., 2026)) and biology
(NEURONBENCH, a new single-neuron electrophysiology benchmark we create3 ). In each case, we
show that MDA is substantially more data-efficient than pure LLM baselines. In summary, we make
3 contributions: we develop the MDA method; we establish new SOTA performance on two existing interactive scientific discovery benchmarks; and we create a new benchmark (NEURONBENCH),
which adds features such as partial observability and stochasticity that are missing in existing benchmarks.

## 2 Problem Statement

Modeling assumptions. We consider an agent interacting with an unknown “blackbox” dynamical
system, that maps an optional sequence of inputs or control signals x1:T , for xt ∈ X ⊂ Rdx , to a
sequence of noisy observations, y1:T , for yt ∈ Y ⊂ Rdy , in response to an optional perturbation
or intervention a ∈ A, and an optional setting of the initial condition of the system state ι ∈
Z ⊂ Rdz . WLOG, we assume the true data generating process can be represented by a latent-state
dynamical system, or state space model (SSM), as shown in Fig. 5. The latent dynamics (which
may be deterministic or stochastic) are given by zt+1 ∼ p zt+1 | zt , xt ; do(a, θ) , where do(a, θ)
represents the parameters
of the system after applying intervention a.4 The noisy observation model

is yt ∼ p yt | zt ; θ , and the initial condition is given by z0 ∼ p(z0 | ι). A static input-output
system is a special case with T = 1.
Data. We define an experiment design as ξ = (ι, a, x1:T ), where xt is the input at step t (if
present). If ι = [], it means the initial state of the system is chosen at random from some distribution
p(z0 ). If a = [], it means we use the original unperturbed system parameters θ. The agent is
i
) : i = 1 : N0 }, where each sample is drawn
presented with an initial dataset D0 = {(ξ0i , y0,1:T
i
i
from the system using y0,1:T ∼ p(·|ξ0 ), We assume the initial designs are from from the default
(unperturbed or “wild-type”) system, but they may use different input sequences xi . The agent is
then given a budget of B turns to interact with the system. At each step, it designs an experiment
ξb , and then collects data yb,1:T from the environment, to create Db = (ξb , yb,1:T ). It can use this
2

See Section 5 for discussion of prior work.
Benchmark available at https://github.com/murphyk/neuronbench
4
We distinguish the intervention action a, as used in the causality literature, from the action sequence x1:T ,
as used in the RL and control theory literature, because they play slightly different roles: the former changes
the mechanism (parameters) of the underlying system, whereas the latter corresponds to changing the set of
inputs or covariates applied to a fixed system. Of course, we can always define x0 = a, but we choose to keep
them separate for notational clarity.
3

Yukawa: accuracy--complexity Pareto (open-ended pool, AI-Feynman style)

Inaccuracy [bits / data point]

4

1/r

3

1
( /λ)/λ
1/rp (fractional)
K1 r

2

/

e −r/λ r 2

(1+Acos ω0.52
t)/r 2
(1+tanh)/2r2

1

0.26
( /λ)/λ

K1 r

0
0

(a)

2.1

relative force error

Pareto frontier fit on:
short-range only (r ≤ 2.5)
+long-range probes (r = 5, 6)

20

40

60
Complexity [bits]

0.13
80

100

(b)

Figure 1: (a) The MDA discovery loop. See Algorithm 1 for details. (Figure based on (Elteto et al., 2026,
Fig.2).) (b) Accuracy-complexity Pareto frontier for models discovered by MDA in the YUKAWA physics
environment. Both axes in bits on a linear scale so the convex corner is obvious. The y-axis is inaccuracy, the
absolute relative force error in bits, log2 (Fpred /Ftrue ) . See Section 4.1 for details. (Figure based on (Udrescu
& Tegmark, 2020, Fig 1)).

knowledge to update its beliefs about the underlying model, pb = p(m|D0:b ), where m specifies the
SSM structure and parameters, and this belief can be used to design the next experiment.
Evaluation. After B rounds, each agent has the training set Dtr = D0:B ; the MDA agent also
has its final belief state, pB . When working with synthetically generated data, we can compare the
agent’s estimated model directly with the true model using an appropriate metric. However, in the
general case, we rely on measuring out-of-sample prediction error in response to a set of novel test
experiments, ξtest = {ξ i : i = 1 : Ntest }. We define the corresponding ground truth test set as
i
)) : i = 1 : Ntest }, where s(y1:T ) is a set of features of interest we want the model
Dte = {(ξ i , s(y1:T
to predict. In the simplest setting we use s(y1:T ) = y1:T , but for complex observations, we can
use summary statistics that capture relevant high level patterns. For example, for NEURONBENCH
in Section 4.3, we use s(y1:T ) = {nk }, which is the number of spikes at each input strength k.
PNtest
We evaluate performance using the average loss, L = N1test i=1
ℓ(ŝi , si ), where ŝi is the agent’s
prediction for the features on test input i.
At a high level, our setup is a transductive problem similar to the ARC-AGI challenges5 , except
our domains use continuous-valued actions and observations, and are derived from real scientific
problems.

## 3 Methods

Overview. The MDA method is visualized in Fig. 1a; see Algorithm 1 for detailed pseudocode.
At each step, the agent updates its belief state pb = p(m|D0:b ), which is a posterior distribution
over models or hypotheses m. Then it chooses the next experiment by maximizing the expected
value of information, ξb+1 = arg maxξ∈Ξ VoI(ξ). It runs the experiment and updates its dataset
by appending Db+1 . After B rounds, the agent is asked to forecast the outcomes to some novel
experimental conditions. We give the details below.
Sequential Bayesian inference. The belief state pb = p(m|D0:b ) is a posterior over models m,
represented as a set of Nm particles. Each model m encodes the structure of the system, as in a
structural causal model (SCM) (Pearl, 2009). This posterior is updated using Sequential Monte Carlo
5
See https://arcprize.org/arc-agi. ARC-1 and ARC-2 are passive transduction problems,
where xi is a 2d input grid (specified by the environment, not the agent) and y i is the resulting 2d output grid,
and the goal is to learn p(ytest |xtest , Dtr ), where Dtr is a fixed set of 3 (x, y) pairs. ARC-3 involves dynamic
interaction with a 2d grid world, where the agent actively controls the sequence x1:T and observes y1:T , which
is more like our setting.

(SMC), following the ModelSMC method of (Wahl et al., 2026) and SMC-S method of (Piriyakulkij
et al., 2024); see Algorithm 2 for the pseudocode. We use an LLM to propose a new model given
the set of previous hypotheses, their corresponding residual errors (derived from the data), and an
initial text prompt (context) C. We denote this proposal distribution by p(mb |{mnb−1 }, D0:b ).
After proposing
R a new model (particle), we evaluate its evidence (marginal likelihood), Zm =
p(D0:b |m) = p(D0:b |m, θ) p(θ|m) dθ, using the adaptive-tempered SMC method shown in Algorithm 3. (See (Naesseth et al., 2019; Chopin & Papaspiliopoulos, 2020) for more details.) Crucially,
the integration over model parameters provides an automatic Occam penalty factor for complex
models with many parameters (MacKay, 1991). Thus, over the course of inference, we will get a set
of hypotheses that tradeoff complexity with model fit, as shown in Fig. 1b.
Q
i
Likelihood functions. To compute the likelihood, p(D0:b |m, θ) = i∈D0:b p(y1:T
|ξ i , m, θ), we
consider two strategies. If the latent dynamics are a deterministic function of the initial conQT
t
ditions, z0 , then we can use p(y1:T |z0 , m, θ) =
t=1 p(yt |zt , m, θ) where zt = mθ (z0 ) =
mθ (· · · (mθ (z0 ))) is z0 pushed through the forwards model t times. If the latent dynamics are
stochastic,
we can use the particle filter method of Algorithm 4 to approximate p(y1:T |z0 , m, θ) =
RQ
p(y
|z
t
t , m, θ)p(zt |zt−1 , m, θ)dz1:T .
t
For some problems (such as NEURONBENCH), individual trajectories are very noisy, so a per-time
step likelihood p(yt |zt ) is not meaningful. In such cases, we convert the trajectory into a set of
global summary statistics, sj (y1:T ), and use a trajectory-level likelihood of the form p(y1:T |m, θ) =
QJ
j=1 p(sj (y1:T )|m, θ), as is standard in the simulation based inference literature (Deistler et al.,
2025). In Section A.4 we present some initial results on learning these summary statistics s(y) as
well as the model itself.
Expanding and shrinking the hypothesis space. SMC can update the posterior over hypotheses (models) given observations. However, in the M-open case (Bernardo & Smith, 1994; Kelter,
2020), we may need to expand the hypothesis space to account for a novel mechanism. To do
this, we use a predictive check, i.e., a held-out interventional forecast (c.f., (Kelter, 2020)). If the
error is too large, MDA expands the hypothesis space by prompting the LLM to suggest a novel
unnamed mechanism (which is endowed with broad (“uninformative”) priors). (This is analogous
to the Breaker–Builder method of (Buehler, 2026), and is how MDA can create new knowledge,
overcoming a limitation of pure LLM-based discovery (Zahavy, 2026).) Conversely, if the posterior
has confidently identified a model that fits well, we reduce the number of hypotheses, to prevent a
proliferation of near duplicates, which diminishes performance. See Section A.2 for more details on
MDA’s meta-controller.
Experiment design. We choose the experiment whose outcome is most informative about which
hypothesis is true: ξ ⋆ = arg maxξ∈Ξ I(M ; Yξ | D) (Lindley, 1956; Box & Hill, 1967; Chaloner
& Verdinelli, 1995; Rainforth et al., 2024). This is called the Value of Information (VoI) for an
experiment. For the case of deterministic latent dynamics, and Gaussian observation noise, we
can derive a simple analytic expression for the VoI, shown in Eq. (5). This picks the design with
highest posterior-predictive variance of the outcome. Since the per-structure parameter posteriors
are usually fairly concentrated, this variance is dominated by cross-model disagreement. We can
optimize the VoI for small design spaces by simply enumerating each choice and scoring it. For
larger continuous spaces, we use CMA-ES (Hansen, 2016). As baselines, we also consider random
designs and LLM-proposed designs (as in (Gupta et al., 2025; Wiemann et al., 2026)).
Prediction. Once we have accumulated the full dataset D0:B , and created the posterior over hypotheses, pB = p(m|D0:B ), we evaluate the model in terms of its ability to forecast the outcome of
novel experiments. For simplicity, we focus on predicting the posterior mean of each scalar output,
E[Y | ξ, D0:B , pB ], which is optimal when using ℓ2 loss. We consider 3 methods:
• Bayes-forecast, E[Y | ξ, m̂] with m̂ = arg maxm pB (m) being the MAP model.6
6
=
R general, the Bayes-forecast can use the full Bayes model average p(Y |ξ, D0:B )
P In
p(m, θ|D0:B ) p(Y |m, θ, ξ) dθ, as proposed in (Self & Cheeseman, 1987). For example, suppose we
m
want to predict the expected number of neuron spikes nc at input current level c, as required in NEURONBENCH

• LLM-forecast, E[Y | ξ, m̂] with m̂ = LLM(D0:B ) being an LLM-generated model, created
using standard code synthesis methods. (This is the approach used in (Wiemann et al., 2026).)
• ICL-forecast, E[Y | ξ, D0:B ]: this is an in-context LLM-based predictor that conditions on the
collected data and directly predicts the expected output, without using any kind of explicit model
(c.f., (Lee et al., 2026)).

## 4 Experimental Results

In this section, we summarize some our our experimental results on various benchmarks from
physics, biology and chemistry (see Table 3). We show that the MDA method reduces held-out
interventional predictive error much faster (in terms of number of experiments) than the baselines.
We give more details in Section C, Section D and Section E.
Common protocol. Every benchmark is run through the same design loop for B≤8 experiments.
At each step the agent selects the next experiment with a design function fdesign — random, LLMproposed, or Bayesian VoI — and after each step we forecast held-out interventional outcomes with a
forecaster fpredict (Bayes-, LLM-, or ICL-forecast; Section 3) and score them by mean-squared error
against the ground truth. We report this held-out error as a function of the number of experiments;
because all datasets are synthetic and the true model is known, in some domains we additionally
check whether the recovered model is symbolically equivalent to the truth. The two canonical agents
are “MDA” (VoI design + Bayes-forecast) and the “LLM agent” (LLM design + LLM-forecast).

### 4.1 FORCEBENCH: Discovering Force Laws

Benchmark. In this section, we give a brief description of FORCEBENCH, which is our wrapper
on top of the DISCOVERPHYSICS benchmark from (Wiemann et al., 2026). (We do not change
the underlying benchmark, merely the interface, to make it compatible with our other benchmarks.)
FORCEBENCH requires an agent to infer an unknown but novel force law governing the behavior
of two or more particles in a 2d space. The agent can control the initial location and velocity of
one of the particles, as it is launched, as well as a few other environment parameters. (In practice
we discretize the design space into a fixed menu of 13 different combinations, listed in Table 5.)
The performance of the learned model is assessed on a test set which probes the model’s predictive
performance in novel experimental settings beyond the training set. Following the paper, we report
this in terms of the normalized MSE, (nMSE = MSE/test-trajectory variance). See Section C.1 for
further details.
Modeling assumptions. The agent assumes the unknown force can be represented as a Green’s
function F , and asks the LLM to propose various candidates (see Section G for details of the
prompt). It then derives the acceleration using Newton’s law, and integrates this to get velocity,
and then integrates this again to generate the trajectory. It assumes the likelihood p(y1:T |ξ, F, θ) is
Gaussian, as in Eq. (3), and then does posterior inference over F and experiment design following
the MDA recipe.
Data efficiency experiments. In Fig. 2, we show the performance of MDA vs the baseline LLM
agent aggregated over all six of the two-particle worlds (see Fig. 7 and Fig. 8 for the performance
plots for all 11 worlds). For each of the 6 worlds, we sample 3 random initial conditions, and roll
out 3 trajectories per IC. Both agents use the same design space, and for the LLM they either use
Opus 4.7 (the best model reported in (Wiemann et al., 2026)) or the cheaper DeepSeek-v4 Pro. On
the left we plot the nMSE of the forecast for up to B = 8 steps.7 On the right we plot the fraction of
discussed in Section 4.3, where c is specified as part of the experiment design
Pξ. The posterior mean can be approximated from the weighted set of particles using n̂c = E[s|ξ = c, D] = i p(mi , θi |D)s(mi (ξ = c, θi ))),
where s(z1:T ) is the number of spikes in trace z1:T , and z1:T = mi (ξ, θi ) is the deterministic ouput of running
model mi with parameters θi on input ξ = c.
7
For the Opus LLM baseline, we also run their agent in its native “unthrottled” mode, in which it performs
multiple experiments per step. Thus 16 rounds of their agent performs ∼ 41 experiments on average. The
nMSE of 0.013 we get using this method matches the 0.01 reported in their paper, validating our experimental
pipeline.

ForceBench (DiscoverPhysics protocol, all 6 worlds): MDA lifts even a cheap base model (DeepSeek) to near-Opus accuracy in a few experiments, while the pure agent stays weak

pass rate vs. experiments

101
100
10−1

numerically accurate (nMSE < 0.1)

10−2

un-throttled
(native protocol)

DP paper (Opus agent)

10−3
1

2

4
8
16
number of experiments Na

numerically accurate (% runs, nMSE < 0.1)

normalized MSE (nMSE, geo-mean)

prediction error vs. experiments

32

100
80
MDA (Opus 4.7)
MDA (DeepSeek v4)
LLM agent (Opus 4.7)
LLM agent (DeepSeek v4)

60
40
20
0
1

2
4
number of experiments Na

8

Figure 2: Data efficiency on FORCEBENCH, aggregated over all six two-particle worlds. Left: we plot
nMSE (geometric mean over the 6 × 9 runs) vs number of experiments. Error bars are ±1 standard error. The
red square is the result of the “unthrottled” baseline agent, and matches the paper. Right: we plot fraction of
runs where nMSE drops below the 0.1 threshold. See text for details.

runs where the prediction “passes”, following the paper’s definition of a pass as nMSE ≤ 0.1. (We
exclude the paper’s textual explanation criterion as part of the definition of “pass” because we found
it to be unreliable; see Section C.7 for discussion.) From both plots we see that MDA is substantially
more data efficient than the LLM baseline, and that Opus is better than Deepseek. See Table 8 for a
list of the laws discovered by each agent after B = 8 experiments.
Example: Yukawa world. As a concrete example, we consider YUKAWA world, whose force
law has the form F = qi qj K1 (r/λ)/λ, where K1 is the modified Bessel function and λ = 2.
The agent can choose the initial launch radius r0 and speed v0 of the target particle. The screened
kernel K1 (r/λ)/λ and the power laws that fit its short-range behaviour are nearly identical for
r ≤ λ and diverge only at longer range (where the screening has decayed), so a probe must reach
past the screening length to break the tie: a short-range launch leaves the candidate trajectories
indistinguishable, while a long-range launch makes the true Yukawa fan out from its near-misses
(visualized in trajectory space in Fig. 14, Section C). By maximizing the VoI, the agent therefore
designs long-range probes.
The effect of the long range experiment triggers an “aha” moment for the agent. This is visualized
in the Pareto curve in Fig. 1b which plots models on the accuracy–complexity frontier. With only
short-range data, the true kernel sits mid-frontier with no edge over its near-misses; only after an
informative long-range probe is added does the frontier shift down, making the true model drop to
the convex corner — the moment where the agent truly “groks” the concept. (Note that the x-axis
in Fig. 1b is a Bayesian description length, − log2 p(m | D) — the posterior code-length of each
candidate law. Unlike a purely syntactic complexity, such as the Halstead metric used in (Kasenberg
et al., 2026), this is data-dependent: it rewards a law only to the extent the evidence supports it.)

### 4.2 CHEMBENCH: Discovering Enzyme-Kinetic Rate Laws

Benchmark. In this section, we briefly describe CHEMBENCH, which is our wrapper on top
of ACTIVESCIBENCH-CHEM from (Kabra et al., 2026). (We don’t change the underlying
benchmark, just the interface, to make it compatible with our other benchmarks.) The problem is to learn a function mapping seven controllable inputs (substrate, inhibitor, second substrate and product concentrations, enzyme
loading, temperature and pH) to a reaction rate r:

r = f CA , CI , CB , CP , Enz, T, pH; θ . See Table 1 for some examples. The experimenter gets to
set the 7 input variables, ι = x0 , and observes the scalar response. Note that this problem is a special case of our SSM setup, since there is no temporal evolution. Following the paper, We measure
performance using the held-out root-mean-squared log-error (RMSLE). If this is below ϵ=0.01, we
say the law is “numerically exact”. We also check for symbolic equivalence with the truth (which
they call Structural Accuracy) using sympy. See Section D.1 for further details.

80

% of 36 tasks (2 seeds)

70

Symbolic accuracy (recovered form = truth)

Numerically equivalent (RMSLE < 0.01)

60

MDA (VoI)
MDA (Mean)
LLM-AutoSciLab (full)

50

60
40

50

30

40
30

20

20

10

10
0

3 5 8 10

20
40
experiment budget B (total)

0

60

3 5 8 10

20
40
experiment budget B (total)

60

Figure 3: Data efficiency curves for CHEMBENCH. We plot mean performance ±1 SE over the 36 tasks, two
seeds. Left: symbolic accuracy. Right: numerical equivalence (E X ACC, RMSLE < 0.01; the head-to-head
Table 9 additionally reports the released benchmark’s own looser 0.05 threshold, for comparability with its
published numbers). MDA (VoI) rises to its ceiling within ∼8 experiments and leads on symbolic accuracy at
every budget; LLM-AUTOSCILAB only catches up by B = 60. On numerical accuracy, LLM-AUTOSCILAB
catches up sooner, but this is because of overfitting (see Table 1).

Modeling assumptions. The agent assumes the unknown function f can be represented as an
algebraic equation, and asks the LLM to propose various candidates (see Section G for details of
the prompt). It assumes
a Gaussian likelihood with multiplicative noise, p(y|ξ, f, θ) = N ! y |

f (ξ, θ), σrel , f (ξ, θ) , to match the benchmark’s noise model, and its RMSLE metric. Given this
model, the agent does posterior inference over f and experiment design following the MDA recipe.
VoI optimization. MDA by default uses VoI to pick the design. However, following (Kabra et al.,
2026), we also create a baseline which we call MDA (M EAN ), which picks the design of highest
posterior-mean rate — an exploit/peak-seeking acquisition, as in Bayesian
— rather
optimisation

⋆
= arg maxξ∈Ξ Em,θ|D r(ξ; m, θ) . Both designs
than the most model-discriminating one: ξmean
are one-step (myopic); they differ only in the objective — exploit the predicted rate versus discriminate between mechanisms. We maximise either objective over the continuous 7-D design box Ξ in
one of two ways: by Monte-Carlo (draw nc =48 candidate designs — log-uniform on the concentration/enzyme axes, uniform on T /pH — and take the argmax) or with CMA-ES (Hansen, 2016) over
the box at the same 48 objective evaluations. We find the latter method is significantly better, so we
use it by default.
Data efficiency experiments. In this section, we compare MDA to LLM-AUTOSCILAB from
(Kabra et al., 2026), which was the previous SOTA on this benchmark. Following their experiment
protocol, we use a stratified 36-task subset (12 domains × easy/medium/hard) at two seeds. Figure 3
shows the data efficiency learning curves, which show that MDA is far more sample-efficient: it
reaches its ceiling within about 8 experiments (overall SA ≈56%), whereas LLM-AUTOSCILAB
only reaches SA ≈ 42% by B = 60.8 See Section D.2 for more results.
Example. Table 1 shows the laws recovered on three representative domains. MDA returns interpretable mechanisms — exactly the true form for substrate inhibition, and the correct inhibition/saturation structure elsewhere (although sometimes with a spurious extra factor). LLMAUTO S CI L AB’s PySR instead returns numerically-fit but mechanistically meaningless expressions
— nested 10 a log(·) and stretched-exponential forms — that can score a low RMSLE (even 0.001
on the hard noncompetitive domain) while being symbolically wrong: the high-exact/low-symbolic
pathology discussed in (Kabra et al., 2026).
8
Our result of 42% SA is higher than the 35.1% SA score they report in their paper, because we replaced their use of gpt-4o-mini with Opus 4.7, to be comparable to MDA. Note, however, that we stick
to Qwen2.5-7B for the adaptive ensemble used by their code. (We also verified that dropping this ensemble
component substantially hurt performance of their method.)

Domain
substrate inhib. (easy)
noncompetitive (hard)
Michaelis–Menten (easy)

True law
k Enz CA
2
Km +CA +CA
/Ki
k Enz CA
(1+CI /Ki )(Km +CA )
k Enz CA
Km +CA

MDA recovers

LLM-AUTOSCILAB recovers

same form ✓ (.007)

Enz (a rCA + . . . ) × (.23)
√
10 0.87 log(0.5 Enz/(CI +·)) × (.001)

Hill×noncomp. ≈ (.018)

+ spurious e−Ea /RT ≈ (.017) 10 0.43 log(Enz T

0.37

/·)

Table 1: Representative recovered laws (best config, B=60). Parenthesised value is held-out
RMSLE; ✓ = symbolic form recovered, ≈ = correct structure with a spurious extra factor, × =
mechanistically wrong. MDA recovers the mechanism in every case; LLM-AUTOSCILAB’s PySR
fits the numbers with unphysical expressions — low RMSLE, no mechanism (the hard noncompetitive row scores RMSLE 0.001 yet is symbolically meaningless).

### 4.3 NEURONBENCH: Discovering Ion-Channel Mechanisms

Benchmark. We design a new benchmark, NEURONBENCH, by creating 6 “mystery neurons”,
based on the generalized Hodgkin-Huxley (HH) model, which are a set of nonlinear ODEs for
describing the spiking behavior of neurons (see Section E.2 for details of HH models). Each mystery
neuron has incoming current represented by INa + IK + IL + IZ , where Na is the sodium channel,
K is the potassium channel, L is the leak channel, and Z is a novel membrane mechanism that we
design, in order to prevent the LLM from simply recalling the model from memory (in most worlds
an added channel, but in one a modification of the existing Na+ channel rather than a new current).
The experimental protocol allows the agent to specify the input signal (an electrical current) over
time. We assume this is chosen from a set of 9 templated signal shapes. In addition, the agent can
optionally apply 3 different kinds of ion channel blockers that change the underlying mechanism
(see Section E.3 for details). So the total design space has 9 × 4 = 36 discrete options.
Modeling assumptions. The agent assumes the data can be represented by some kind of HH
model m, and asks the LLM to propose various candidates (see Section G for details of the prompt).
It then converts this into an ODE that defines the deterministic dynamics
p(zt |zt−1 , xt ) = δ(zt =
m(zt−1 , xt ; θ)), where the latent state is zt = V (t), gating variables defined in Eq. (24). Finally
it integrates this ODE over time to get a candidate trajectory z1:T from which the noiseless voltage
trace V (1 : T ) can be extracted. However, rather than evaluating the ability of the model to exactly
match an observed trace (which can be very “wiggly” and hard to predict, even in the deterministic
regime), we reduce the trace to a summary statistic s, and use a synthetic likelihood (Deistler et al.,
2025) of the form p(s(y1:T )|ξ, m, θ). For example, if s(y) is the number of spikes in the trace y, we
can use the Poisson likelihood p(s(y1:T )|ξ, m, θ) in Eq. (32). We then do posterior inference over
m and experiment design following the MDA recipe.
Data efficiency experiments. In Fig. 4, we show test error vs number of experiments for all six
worlds. For each world the LLM is shown only the phenotype (the observable signature, not the
mechanism) and proposes 2–5 candidate channels, which we map onto a shared channel library; the
truth is sometimes not proposed — e.g. on Z-REBOUND the LLM omits the low-threshold inward
current — a genuine M-open miss that we keep representable so the residual can reopen the pool.
MDA then runs Poisson-evidence selection over that pool with VoI-designed experiments. We see
that the Bayes-forecaster (blue) is significantly better than the in-context forecaster (purple) on every
world; and within the Bayes-forecaster family, VoI and LLM-proposed experiment design perform
similarly and both beat random design.
Stochastic extension. The worlds above use a deterministic Hodgkin–Huxley forward model,
which can be represented by a deterministic ODE, so the likelihood is closed-form. In Section F.1 we make the latent dynamics stochastic (by adding finite-channel gating noise), turning
the model into an SDE. We call this benchmark NEURONBENCH STOCH. The corresponding likelihood p(y | ξ, m, θ) is now intractable — the one regime none of our other benchmarks reach.
In Section F.1, we show that a deterministic likelihood gives poor results (the method confidently
selects the wrong model), whereas a particle filter approximation to the marginal likelihood (Algorithm 4)

× (.015)

Open-ended (-open) NeuronBench: the LLM PROPOSES the candidate channels per world (2--5 hypotheses); MDA's SMC+VoI then discovers and forecasts
Bayes-forecast

ICL-forecast

VoI acquisition

held-out forecast MSE (spikes2, log)

held-out forecast MSE (spikes2, log)

z rebound [6 hyp.]

LLM acquisition

h sag [4 hyp.]

random acquisition

ca rebound [5 hyp.]

102
101
100
10−1
0

2

4
6
d type [6 hyp.]

8

0

2

4
6
na fatigue [3 hyp.]

8

0

2
4
6
8
textbook M [4 hyp.] (textbook)

0

2
4
6
number of experiments Na

8

0

2
4
6
number of experiments Na

8

0

2
4
6
number of experiments Na

102
101
100
10−1
8

Figure 4: Data efficiency on all six NEURONBENCH worlds (Opus 4.7). For each world the LLM proposes
the candidate channels from the phenotype (2–5 hypotheses, shown in the panel title), and then MDA designs
experiments to confirm or refute these hypotheses. After each experiment, we plot the forecast accuracy on
the test data. Colour = forecaster (blue Bayes-forecast, purple in-context forecast), line style = acquisition
(VoI solid, LLM dashed, random dotted); held-out interventional forecast MSE (spikes2 , log) vs. number of
experiments; shaded bands are ±1 SE over 3 random initial conditions. The Bayes-forecaster dominates the incontext forecaster everywhere; within the Bayes family VoI and LLM design are similar and both beat random.

This gives the correct results. Unfortunately running a particle filter inside the tempered SMC
algorithm (needed to compute the evidence) — which is in turn nested inside of the SMC algorithm
over models — is very slow. Fortunately we show that we can learn a suitable summary statistic
function (using a 1d convolutional neural network), which speed things up by ∼104 ×. Furthermore,
because the summary is learned, this simulation-based likelihood adapts to whatever mechanisms
the LLM proposes, rather than needing a hand-crafted feature per hypothesis.

## 5 Related Work

• Causal models for interventional prediction. Predicting “what if” questions using causal models is discussed at length in (Pearl, 2009). Recently Richens & Everitt (2024) proved that an
agent that can robustly predict across a full range of interventions (distribution shifts) must have
implicitly learned a causal world model, and give a method to extract it from the predictor. We
instead explicitly represent the causal model, so that we can leverage prior knowledge from LLMs
(Kıcıman et al., 2024; Ban et al., 2025), reason over our uncertainty using Bayesian methods, and
provide an interpretable model to the user.
• Bayesian experimental design. Choosing the most informative experiment is the classical
model-discrimination objective of (Lindley, 1956), reviewed in (Chaloner & Verdinelli, 1995;
Rainforth et al., 2024); modern work scales it with amortised and gradient estimators (Foster
et al., 2021). Our VoI is the Lindley objective read off a two-level SMC posterior, as derived in
Eq. (5).
• Simulation-based inference. When the likelihood is intractable, SBI learns it or the posterior
from simulations (Cranmer et al., 2020), and learned/embedding summary statistics are a whole
subfield of their own (Fearnhead & Prangle, 2012; Chen et al., 2021; Radev et al., 2022).
• LLMs for scientific discovery. LLMs have been used to propose scientific hypotheses in many
papers, including from static datasets (Romera-Paredes et al., 2024; Wahl et al., 2026; Kasenberg
et al., 2026; Aygün et al., 2026; Xie & Wilson, 2026) as well as actively collected datasets from
agent-designed experiments (Piriyakulkij et al., 2024; Abhyankar et al., 2026; Elteto et al., 2026;
Prystawski et al., 2026; Jagadish et al., 2026). Our work is in the latter camp, differing mainly
in how we handle the M-open regime inside SMC, the diversity of domains, and comparing to
SOTA LLM baselines rather than straw men such as random designs.
• Benchmarks for interactive scientific discovery. Various benchmarks evaluate agents that learn
scientific laws by interactive experimentation: we build on DISCOVERPHYSICS (Wiemann et al.,
2026) and ACTIVESCIBENCH-CHEM (Kabra et al., 2026), add our own NEURONBENCH, and
may target others such as NEWTONBENCH (Zheng et al., 2026) in future.

ι

x0

x1

x2

z0

z1

z2

y0

y1

y2

···

zT

yT

do(a)

a

θ

Figure 5: The world as a controlled, intervenable state-space model (Eq. (1)). A latent state zt (white)
evolves under the mechanism θ (orange; it parameterizes every transition) and emits a lossy, noisy observation
yt (grey) — in general only y1:T is seen. Optional exogenous inputs/covariates xt (blue, dashed) and the initial
condition ι (which sets z0 ) are shifts in the inputs to a fixed mechanism. An intervention do(a) is categorically
different: the lightning bolt strikes θ itself, changing the mechanism to θa .

## A Method: Further Details

### A.1 Modeling Assumptions

We assume the unknown dynamical system is represented by a state space model, as shown in Fig. 5.
This corresponds to the following probabilistic model m:

zt+1 ∼ p zt+1 | zt , xt ; do(a, θ) ,
yt ∼ p yt | zt ; θ ,
z0 ∼ p(z0 | ι).
(1)
where do(a, θ) represents the parameters of the system after applying intervention a. An experiment
design ξ (the choice of initial conditions and control knobs the agent selects) fixes the induced
intervention a; we therefore write do(ξ) for the intervened system when the design is the decision
variable, as in the VoI objective below. The SSM assumption is without loss of generality, since
any non-Markovian model can be converted to Markov form, as long as the latent state space is
allowed to grow. If the latent dynamics are deterministic (an assumption we relax in Section F),
then zt = mt (z0 ; θ), where mt is the forwards model iterated t times. If we additional assume the
observation noise is Gaussian, we have
p(yt |zt , m, θ) = N (yt |mt (z0 ; θ), σ 2 )

(2)

Hence for conditionally independent observations, the likelihood of a parameter vector θ given
model m and initial conditions z0 is
p(y1:T |z0 , m, θ) =

T
Y

N (yt |mt (z0 ; θ), σ 2 )

(3)

t=1

### A.2 Inference Algorithms

This appendix gives the pseudocode for our outer active-inference loop (Algorithm 1, and the three
nested inference layers of Section 3:
• Algorithm 2 computes posterior over LLM-proposed structures : p(m|D0:b ) ≈
PNm
i=1 wi 1[m = mi ], where wi = p(mi |D0:b ).
• Algorithm 3 uses per-structure adaptive-tempered SMC to compute the posterior over the
PNp
parameters for each model: p(θ|m, D0:b ) ≈ i=1
Wi 1[θ = θi ], and the evidence Zm =
p(D0:b |m)

Algorithm 1 MDA discovery loop — the outer layer that wraps model inference (Algorithm 2)
with value-of-information experiment design. It acquires one experiment per round (batch size 1)
and re-infers p(m | D) on the growing dataset.
def MDA(B, C, D0 ; τr , Rmax , τp ) → p(m | D0:B ), {E[Y | ξq , D0:B ]}q

max
1: p(m | D0 ) ← MODEL - INFERENCE(D0 , C; Rm =Rmax , Nm =Nm
) ▷ Alg. 2: initial pool +

refinement
2: for b = 1 . . . B do

3:
ξ ⋆ ← ARGMAXξ∈Ξ VoI ξ; p(m | D0:b−1 )
4:
yb ← OBSERVE(ξ ⋆ ); D0:b ← D0:b−1 ∪ {(ξ ⋆ , yb )}
5:
m∗ ← arg maxm p(m | D0:b−1 ); r∗ ← RESIDUAL(m∗ , D0:b );

p∗ ← maxm p(m |
D0:b−1 )
▷ best form’s fit r∗ and class-posterior concentration p∗
6:
Rm ← Rmax if r∗ > τr else 0
▷ M-open: create new form when residual is too high
min
max
7:
Nm ← Nm
if p∗ > τp ∧ r∗ ≤ τr else Nm
▷ ESS-adaptive pool: shrink if
concentrated and well fitting
8:
p(m | D0:b ) ← MODEL - INFERENCE(D0:b , C; Rm , Nm ) ▷ re-weight; explore if triggered;
pool capped at Nm
9: end for
10: return p(m | D0:B ) and forecasts E[Y | ξq , D0:B ] for held-out test designs ξq ∼ Q
Algorithm 2 Model inference over Nm model particles for Rm refinement rounds (so O(Nm Rm )
LLM calls — the dominant cost): a batch of LLM-proposed structures, or sequential refinement
whose proposal conditions on the fit residuals of the entire particle pool (as in SMC-S (Piriyakulkij
et al., 2024)), rather than a single ancestor particle (as in ModelSMC (Wahl et al., 2026)). PARAM POSTERIOR is Algorithm 3.

def MODEL - INFERENCE(D, C; Rm , Nm , Nnew ) → p(m | D), p̂(D)
m
1: propose Nm structures {mi }N
i=1 from the LLM given C (or enumerate the space)
(stochastic dynamics,
optional) auto-select the observation model o
∈
{PF (Alg. 4), feature synthetic lik., learned sϕ } by cost-aware VoI (Eq. (11)); if o=sϕ ,
(re)fit the learned summary on the current pool’s prior-predictive simulations. PARAM POSTERIOR ’s LOGLIK then uses o; because sϕ is only sufficient for the current pool, this refit
repeats whenever the pool changes (here and at line 7), and a particle-filter spot-check flags an
insufficient summary (App. A, “Sufficiency as the hypothesis pool grows”).
2: (·, log Ẑi ) ← PARAM - POSTERIOR(D, mi ) for each i
▷ evidence log p̂(D | mi )
3: p(mi | D) ← softmaxi (log Ẑi )
▷ uniform structure prior
4: for r = 1 . . . Rm do
▷ sequential refinement
5:
ρj ← RESIDUALS(mj , D) for every pooled structure mj ▷ fit report over all prior attempts

|pool|
new
6:
{m′l }N
▷ propose a batch of
l=1 ∼ q m {(mj , ρj )}j=1 , C, D from the LLM
Nnew ≪Nm new structures jointly
7:
add {m′l } to the pool; re-score (lines 2–3); evidence-prune the pool back to Nm
8: end for
P
9: return p(m | D) = {(p(mi | D), mi )}, p̂(D) = i p(mi ) Ẑi

• Algorithm 4 uses the bootstrap particle filter to compute the likelihood p(D|m, θ) using
Q
P (i)
p̂(y1:T | m, θ) = t N1z i wt
, where wti is the weight of particle i. This is an
unbiased estimate that plugs into the per-class tempered SMC (Algorithm 3) as its LOGLIK,
which returns the model evidence Zm = p(D|m). (In Section F.1 we discuss a way to
avoid this inner PF likelihood approximation by learning a synthetic likelihood model.) If
the latents are deterministic, we have Nz =1, and can use the likelihood in Eq. (3) without
needing PF at all.
MDA meta-controller. The main MDA algorithm, shown in Algorithm 1, is a fairly standard
sequential Bayesian experiment design loop. It uses an SMC subroutine to update the posterior over
models p(m|D0:b ) after obtaining Db from the b’th experiment. However, it adds two novelties, both
of which turn out to be important for good performance in challenging domains (see Fig. 16).

Algorithm 3 Per-class adaptive-tempering
P
PSMC over Np parameter particles. Returns particles,
weights, and log Zm . ESS = ( Wi )2 / Wi2 ; η is the target ESS fraction, Rp the number of
rejuvenation moves per temperature rung, and the annealing schedule runs for at most Jp rungs —
so LOGLIK is called O(Np Rp Jp ) times (it is cheap, and LLM-free). ℓi is a log-likelihood; LOGLIK
is the exact Gaussian for deterministic dynamics (see Eq. (3)) or, for stochastic dynamics, the autoselected observation model — the particle filter of Algorithm 4, or the cheaper synthetic likelihood
on fixed features / a learned summary sϕ (Eq. (8)). Parameter priors are uniform over the proposer’s
declared bounds, so the random-walk Metropolis rejuvenation accepts on the tempered-likelihood
ratio alone, with proposals outside the support rejected.
def PARAM - POSTERIOR(D, m) → ({θi }, {Wi }, log Zm )
1: sample θi ∼ p(· | m) for i = 1..Np ; Wi ← 1/Np ; λ ← 0; log Zm ← 0
2: ℓi ← LOGLIK(m, θi ) ▷ Gaussian (det.); else PF (Alg. 4) / feature- or sϕ -synthetic lik. (stoch.)
3: while λ < 1 do
▷ ≤ Jp annealing rungs

4:
pick ∆λ ∈ (0, 1 − λ] by bisection so that ESS {Wi e∆λ ℓi } = ηNp
P
5:
log Zm += log  i Wi e∆λ ℓi
▷ evidence increment
P
∆λ ℓj
W
e
;
λ
+=
∆λ
6:
Wi ← Wi e∆λ ℓi
j
j
7:
resample {θi } ∝ {Wi }; Wi ← 1/Np
8:
for r = 1 . . . Rp do
▷ random-walk Metropolis at temperature λ
9:
propose θi′ ∼ q(· | θi ); ℓ′i ← LOGLIK(m, θi′ ); set (θi , ℓi ) ← (θi′ , ℓ′i ) w.p.
′

min{1, eλ(ℓi −ℓi ) }
10:
end for
11: end while

Algorithm 4 Bootstrap particle filter for log ℓ̂ = log pb(D | m, θ), the unbiased likelihood estimate
that replaces the exact-likelihood line of Algorithm 3 (turning it into a pseudo-marginal sampler
1:Nz
over (θ, z1:T )). It samples Nz latent-state paths z1:T
over the T observation steps; the transition is
sub-stepped (for NEURONBENCH, the Euler–Maruyama discretisation of the Fox–Lu gating SDE,
Eq. (33)). All the θ-dependence is in the transition (line 3); the observation noise σ is fixed, so the
emission (line 4) does not depend on θ. The sum over the T observation steps is the loop (lines 2–7);
the filter runs in O(Nz T ) time.
def PARTICLE - FILTER(D, m, θ) → log ℓ̂
j
1: z0 ← z0 for j = 1 . . . Nz ; log ℓ̂ ← 0
2: for each observation t =
1 . . . T do
j
3:
ztj ∼ p zt | zt−1
, θ ∀j ▷ sample the stochastic transition (Euler–Maruyama; no density
needed)

4:
wtj ← N yt ; g(ztj ), σ ∀j ▷ emission on the observed coordinate g(zt )=Vt ; σ fixed, no
θ

P
▷ incremental log marginal (running sum over t)
5:
log ℓ̂ += log N1z j wtj
j
j
6:
resample {zt } ∝ {wt }
7: end for
8: return log ℓ̂

• It handles the M-open setting, in which we prompt the LLM to consider new hypotheses
(beyond the current set of particles) if the residual error r∗ of the current best (MAP)
model, m∗ , is above a threshold τr . (This can happen if the agent receives an informative
but surprising observation.) In practice we do this by setting Rm to Rmax > 0; this enables
Rm rounds in which we propose a batch of Nnew new models, add them to the current pool,
and then pick the top Nm based on their evidence. Following the SMC-S (Piriyakulkij
et al., 2024), the (LLM-based) proposal kernel has the form pb (mb |{mib−1 }, D0:b ), so we
condition on the entire set of previous particles rather than just conditioning on a single
ancestor particle, as is more commonly done. If the best residual r∗ is below threshold, we
set Rm = 0, which means we just update the weights of the current hypotheses, but do not
invoke the LLM proposal to refine their structure.

• It adds an adaptive mechanism for choosing the number of hypotheses (particles) Nm :
if the posterior probability p∗ of the current best (MAP) model m∗ is sufficiently high,
min
and its residual r∗ is sufficiently low, then we reduce the number of particles to Nm
in
Algorithm 2. This prevents a proliferation of near-duplicate hypotheses, and allows the
posterior to concentrate. We re-expand the number of hypotheses if we fall outside of this
convergence zone.
SMC parameters and computational cost. Table 2 shows the SMC parameters used in the experiments. The two model-level knobs Nm , Rm control the overall cost: each of the Rm refinement
rounds of Alg. 2 re-fits every live structure (up to Nm ) by a fresh Np -particle adaptive-tempering
SMC (Alg. 3).
quantity
model particles
model rounds
new structures/round
parameter particles
rejuvenation moves
target ESS fraction
max tempering rungs
latent particles
M-open cap
residual threshold
concentration thresh.

symbol FORCEBENCH NEURONBENCH CHEMBENCH
Nm
≤ 14
2–5
12
Rm
8 (=B)
1
adaptive
Nnew
4
1
4
Np
200
200
100
Rp
3
3
3
η
0.6
0.5
0.6
Jp
80
adaptive
80
Nz
1
1/250
1
Rmax
—
3
4
τr
—
0.18
0.05
τp
—
—
0.9

role
Alg. 2: structures / round
Alg. 2: refinement rounds
Alg. 2: added per round if Rm >0
Alg. 3: per-structure SMC
Alg. 3: RW moves / rung
Alg. 3: resample trigger
Alg. 3: schedule cap
Alg. 4: likelihood estimation
Alg. 1: max exploration rounds
Alg. 1: M-open trigger
Alg. 1: pool-shrink trigger

Table 2: Default parameter settings for SMC The model-level pair (Nm , Rm ) dominates cost: Rm
rounds × up to Nm structures × a Np -particle inner SMC. The inner-SMC size Np and rejuvenation
count Rp match across rungs; the target ESS differs (0.6 vs. 0.5). For NEURONBENCH, we use
Nz = 1 for deterministic model, and Nz = 250 for stochastic model.

### A.3 Algorithms for Experiment Design

Deriving the VoI. We estimate the value of information for conducting experiment ξ, denoted
VoI(ξ), as follows. Model the (scalar) outcome as Yξ = µ(ξ) + ε, with µ(ξ) = E[y ∗ | M, do(ξ)]
random over the posterior — a single deterministic forward simulation per particle, since the candidate dynamics carry no internal stochasticity (the property that made the likelihood Eq. (3) exact)—
and ε ∼ N (0, σ 2 ) independent noise.Conditioning on the mechanism class removes the epistemic
spread, so Yξ | M ∼ N µM (ξ), σ 2 , whereas marginally Var[Yξ ] = Var[µ(ξ)] + σ 2 . Under a
Gaussian approximation both entropies
are those of normals, H[Yξ ] = 21 ln 2πe (Var[µ(ξ)] + σ 2 )

1
2
and H[Yξ | M ] = 2 ln 2πe σ , and the 2πe σ 2 cancels in the difference:

I(M ; Yξ | D) = H[Yξ ] − H[Yξ | M ] = 12 ln 1 + Var[µ(ξ)]
,
(4)
2
σ
strictly increasing in Varp(M |D) [µ(ξ)]: the between-class variance of the mean prediction is
the value of information, monotonically. Maximising the mutual information therefore reduces
to maximising thisP
between-class disagreement, which we read off the class-evidence weights
p(m | D)P= Zm / m′ Zm′ (Algorithm 3 returns each log Zm ) and the per-class particle means
µ̄m (ξ) = i Wim µm,i (ξ):

2
P
⋆
ξVoI
= arg max Varp(M |D) E(y ∗ | M, do(ξ)) = arg max m p(m | D) µ̄m (ξ) − µ̄(ξ) , (5)
ξ∈Ξ

ξ

P
with µm,i (ξ) = E[y ∗ | m, θim , do(ξ)] and µ̄(ξ) = m p(m | D) µ̄m (ξ). Using per-class means µ̄m
rather than noisy draws keeps VoI genuine epistemic disagreement — Lindley’s intuition (Lindley,
1956) that the best experiment is the one whose outcome current beliefs least agree on.
Contrast: the full predictive variance. An alternative acquisition keeps the within-class parameter
spread instead of averaging it out. By the law of total variance the full two-level predictive variance

splits into the between-class term of Eq. (5) plus a within-class one:

X
2
Varp(m,θ|D) E(y ∗ | m, θ, do(ξ)) =
p(m | D) µ̄m (ξ) − µ̄(ξ)
m

|

{z

}

between classes (mechanism disagreement)

+

X

p(m | D)

m

|

X

2
Wim µm,i (ξ) − µ̄m (ξ) ,

(6)

i

{z

within class (parameter uncertainty)

}

2
P
estimated empirically by the pooled particle variance m,i wm,i µm,i (ξ) − µ̄(ξ) with wm,i ∝
p(m | D) Wim . Only the between-class term is collapsed by identifying the class. The within-class
term is residual parameter uncertainty, which is negligible once the per-structure posteriors have
concentrated; in this case, this full variance coincides with Eq. (5).
Optimising over a large design space. When the design space is large, we can use various gradient free optimizers to pick the design. For continuous spaces a common choice is CMA-ES (Hansen,
2016). For discrete spaces, we can use LLM-driven evolutionary search methods such as FunSearch
(Romera-Paredes et al., 2024).

### A.4 Learning the Summary Statistics for a Synthetic Likelihood

Synthetic likelihoods. For simple problems we can ask how well the model predicts the entire observed trajectory, y1:T , and measure its performance using a Gaussian likelihood, as in Eq. (3). But
for more complicated signals, like neural voltage trace (or video!), it is common to use a synthetic
likelihood of the form
J
Y
pj (sj (y1:T )|m, θ)
(7)
p(y1:T |m, θ) ∝ p(s(y1:T )|m, θ) =
j=1

where s() is a function that extracts J summary features from the entire observation vector y1:T .
(We omit the conditioning on ξ for brevity.) This can be used in lieu of the regular likelihood
p(y1:T |m, θ) in SMC. In this section, we discuss how to learn the summary function.
The collapse problem. Learning s by making the model “fit the data” is ill-posed: if sϕ is optimised to maximise the synthetic likelihood of the observed dataset, the objective is trivially maximised by a constant sϕ (which carries no information about θ or m), or by an sϕ that discards
exactly the parameter-relevant signal. Any objective that only rewards “matching” collapses the
summary. Something must force sϕ to stay informative.
The fix: learn s to be sufficient for what we infer, on a held-out simulated set. The established
(i)
recipes all share one idea: use a bank of prior simulations {(θi , mi , y1:T )} — a held-out set the
summary must generalise across, not a single dataset to overfit — and train sϕ so that the latent can
be recovered from the summary. This supervised signal both well-poses the problem and makes the
constant solution impossible.
• Semi-automatic ABC / regression (Fearnhead & Prangle, 2012). Under quadratic loss the
optimal summary is the posterior mean s⋆ (y) = E[θ | y]; one approximates it by regressing
θ on features of y over the simulation bank, e.g. training a network sϕ (y) ≈ θ (Jiang et al.,
2017). (This is called Approximate Bayesian Computation or ABC.) Note that a constant
sϕ has maximal regression error, so the objective prevents collapse by construction.
• Infomax / neural
sufficient statistics (Chen et al., 2021). Maximise the mutual information I sϕ (y); θ over the simulated joint; a constant summary has zero mutual information,
so it is the global minimiser of the objective, not a solution. Amortised-SBI summary networks (Radev et al., 2022) are trained jointly with a density estimator on (θ, y) pairs to the
same end (see (Deistler et al., 2025) for a survey).
Both learn a low-dimensional sϕ (y) that is predictive of (a sufficient statistic for) the latent, and the
held-out bank is what supplies the anti-collapse signal.

Example: 1d CNN for summarizing neuron voltage trace. In Section E.8, we give a concrete
example of the regression approach, where we train a 1d CNN to map the neuron voltage trace y1:T
to the label of the correct class (4 possible model types) and a corresponding model parameter (the
max conductant g). The model has two output heads; the penultimate layer is a learned feature
vector sϕ (y) ∈ Rd , which we use as the summary statistic.
Multivariate Gaussian likelihood. Since the components of sϕ (y) are correlated, we use a mulitvariate Gaussian likelihood, rather than the factored form in Eq. (7). The moments of this Gaussian
are estimated by simulation — the standard synthetic-likelihood construction (Wood, 2010; Deistler
et al., 2025). For each candidate (m, θ) we draw R traces y (r) ∼ p(y1:T | m, θ), embed each, and
set

p sϕ (y1:T ) | m, θ = N sϕ (y1:T ) µm,θ , Σm,θ
(8)
P
1
(r)
µm,θ = R r sϕ (y )
(9)

d r sϕ (y (r) ) + εI,
Σm,θ = Cov
(10)
with a small ridge ε for conditioning. (For latent variable models, we draw (y r , z r ) ∼ p(· | m, θ),
and discard z r before fitting µ and Σ as above.)
Connection to MDA’s task-driven abstraction. MDA’s target is not full-state sufficiency but
query-sufficiency: sϕ need only retain what is needed for the query distribution Q. We can therefore
train sϕ (y) to predict the query outcomes Yξ on held-out rollouts rather than to reconstruct the full
state, giving a summary tuned to the downstream task. This is the observation-side analogue of
learning useful latents: we learn not only which latent variables and mechanisms matter, but which
parts of the raw observation to attend to.
Sufficiency as the hypothesis pool grows. A learned summary is only as informative as the simulated family it was trained on, so in the M-open loop sufficiency cannot be a fixed, global property — the pool the agent chooses among changes over time. Three points make it well-posed.
(i) It is task-relative and re-learned. A statistic is sufficient for choosing among the current pool
{m1 , . . . , mK } iff the likelihood ratios depend on y only through it; a classifier trained to separate
the current members’ simulations has, at its optimum, exactly such a statistic (its log-odds), and
adding a proposed hypothesis simply adds a class and re-fits — cheap, since the simulations are
already drawn for the synthetic likelihood, and the summary dimension grows with the pool. (ii) It
can be amortised. Training sϕ over the LLM’s prior-predictive mechanism family (rather than the
current pair) generalises to in-distribution proposals without re-fitting. (iii) It is checkable, with a
model-agnostic anchor. A particle filter needs no summary, so it is a sufficiency-safe gold standard:
when a new mechanism is proposed, disagreement between the cheap synthetic likelihood and a
spot-check particle filter (or a simulation-based-calibration failure) flags an insufficient summary
and triggers re-learning (Section F.1 validates this synthetic-likelihood/particle-filter equivalence in
the stochastic-NEURONBENCH setting). The approximation is therefore monitored and repairable,
not assumed: a proposal whose signature lies in a data dimension sϕ discarded is invisible until
re-learning, and the particle-filter anchor is what makes that safe. Co-training the observation abstraction with the mechanism expansion end-to-end we leave to future work.
Auto-selecting the observation model. When the latent dynamics are stochastic the likelihood
is intractable, and there is a menu of approximations trading accuracy against compute: a bootstrap
particle filter on the raw observation (assumption-free but costly, Algorithm 4); a synthetic likelihood
(Eq. (7)) on a hand-crafted feature vector or on a learned summary sϕ (Eq. (8)) — cheap, but only
as sufficient as the summary; or, when the process noise is negligible, a single deterministic rollout
(Eq. (3)). No single choice is best for every discrimination problem, so we let the agent choose the
observation model o exactly as it chooses the experiment. Writing po (y | m, ξ) for the likelihood
under observation model o, the agent picks

MIo m; y | ξ
⋆
,
MIo m; y | ξ = H(w) − Epo (y|ξ) H qo (· | y) ,
o = arg
max
cost(o)
o ∈ {PF, feat, sϕ }
(11)
where qo (m | y) ∝ wm po (y | m, ξ) is the model posterior formed under observation model o’s
likelihood (cf. Eq. (36)), and cost(o) is its compute — the particle filter’s Nz latent trajectories vs.

a synthetic likelihood’s R simulations, so cost(PF) ≫ cost(feat). This is Eq. (35) applied one level
up — design over the observation model, not the experiment — so the agent defaults to the cheap
summary and pays for the filter only where its discrimination clearly justifies the compute. We
estimate MIo by a truth-free discrimination probe: on the discriminating protocol, simulate single
experiments from each candidate in turn and measure how often o’s log-evidence gap identifies the
generator, averaged over generators — never peeking at the truth.
The particle-filter spot-check. The discrimination probe averages over generators, so it scores
whether o separates the pool on average; it cannot see a cheap summary’s specific blind spot. A
learned sϕ trained on the mechanism family may confuse a single pair whose signatures collapse
in its low-dimensional embedding while discriminating all the rest well — giving a deceptively
high pooled score yet a confidently wrong answer on the world where that pair is the question.
We therefore make the particle-filter anchor operational as a spot-check: whenever a cheap model
o ̸= PF is selected, we re-score the collected data with both o and the particle filter (over the
top few candidates by posterior) and compare their MAP models; on disagreement we fall back
to the PF. The cheap summary is thus used only where it is verifiably sufficient — it agrees with
the assumption-free filter — and the PF catches the rest. This is the safeguard that makes a fast,
possibly-insufficient summary safe to deploy inside the M-open loop (Algorithm 2): the observation
model, like the experiment, becomes something the agent chooses and verifies from data rather than
a hand-set knob. Section F instantiates both — the cost-aware choice and the spot-check — on the
electrophysiology benchmark, and reports how often each observation model is chosen and how
often the spot-check overrides a cheap choice.

Benchmark
FORCEBENCH

Domain
Physics

Model class
ODE (force law)

Observation space
2D trajectory (time series)

Design space
R2 × discrete (13-menu)

Ref.
(Wiemann et al., 2026)

CHEMBENCH

Chemistry

single scalar (initial rate)

R7 (continuous)

(Kabra et al., 2026)

NEURONBENCH

Neuroscience

ours

Neuroscience

1D voltage trace (time series)
1D voltage trace (time series)

input current × channel blocks

NEURONBENCH STOCH

algebraic rate law
(sym. reg.)
ODE
(Hodgkin–
Huxley)
SDE
(stochastic
Hodgkin–Huxley)

input current × channel blocks

ours

Table 3: Benchmarks used in this paper. The three span three domains and several model classes
— dynamical ODEs (FORCEBENCH, NEURONBENCH) and a static algebraic law (CHEMBENCH)
— and very different observation and design spaces: from a 2D trajectory under a mixed
continuous×discrete design (FORCEBENCH) to a single scalar rate under a continuous R7 design
(CHEMBENCH). The same MDA engine (§3) is applied unchanged to all of them.

## B Experimental Results: Further Details

The datasets we use are listed in Table 3. We evaluate the forecasts for each agent α after k experiments as follows. For FORCEBENCH we first compute µi,t,b (α) = E[Yti |ξ i , D0:b , α] for each time
step t of each test trajectory i, and then compute the mean squared error (MSE):
MSEb (α) =

Ntest
T
1 X
1X
(µi,t,b (α) − µ∗i,t,b )2
Ntest i=1 T t=1

(12)

where µ∗i,t,b is the (noise free) expectation under the ground truth model. For NEURONBENCH
i
)|ξ i , D0:b , α] for each summary feature j, and compute the MSE by
we use µi,j,b (α) = E[sj (Y1:T
averaging over features instead of time steps. We then plot MSE vs b, for b = 1 : B, where B = 8 is
the maximum number of experiments. We also plot MSE for k = 0, which is the performance just
given D0 , before any experiments are performed.

# world
pairwise force magnitude F (r, t) Comments
Two-particle, central, radial (single fixed source at the origin)
1 GRAVITY
k qi qj /r
Simple attractive force
2 YUKAWA
k qi qj K1 (r/λ)/λ, λ=2
Screened (2D Helmholtz) kernel: ∼ 1/r at short
range, exponentially suppressed beyond λ
3 COULOMB
k qi qj /r2
Simple attractive force
4 OSCILLATOR
k qi qj cos(ωt+ϕ)/r
Time-varying coupling that periodically reverses
sign
Fractional Laplacian −(−∇2 )α with α = 12
5 FRACTIONAL
k qi qj /r 3−2α , α= 12 (≡1/r2 )
6 EXTRA - DIM
k qi qj ΦKK (r)
1/r2 (short range) to 1/r (long range) transition,
defined by the Kaluza–Klein image-sum kernel
Non-radial or many-body (superposed background, or N mutually-interacting bodies)
7 CIRCLE
k qi qj /r 3−2α , α= 34
Fractional Laplacian with ring of particles
8 ETHER
k qi qj /r
Central law + global drift, ai = −F r̂/mi + α ŷ
9 HUBBLE
k qi qj /r
Central law + position dependent Hubble flow,
ai = −F r̂/mi + H(ri )
Hidden number of other particles
10 DARK-MATTER k qi qj /r, qj ∈{1, 5}
11 THREE-SPECIES k qi qj /r, qj ∈{1, 3, −2}
3 hidden classes (one repulsive) + 5 neutral
probes

Table 4: The eleven public DiscoverPhysics worlds in a single notation. F (r, t) is the pairwise
force magnitude between a receiver of charge qi and a source of charge qj at separation r (Green’s
function of a 2D field equation; k a coupling, λ a screening length, α a fractional order, ω, ϕ a
temporal modulation); ΦKK (r) is the Kaluza–Klein image-sum kernel of a compactified extra dimension (an infinite tower of mirror sources that crosses over from 1/r2 at short range to 1/r at long
range). Underlined quantities are hidden (worlds 10–11: the source charges are concealed; the task
is to infer them).

## C Physics: Further Details

### C.1 Details on the Benchmark

FORCEBENCH (which is just a wrapper on DISCOVERPHYSICS from (Wiemann et al., 2026)) requires an agent to infer the unknown force law governing the behavior of two or more particles in
a 2d space. Each particle i has an associated kinematic state: position ri , velocity vi , and a “generalized charge” qi = (si , ci ), where si is the source charge, controlling how strongly particle i
generates the field, and a response charge ci controlling how strongly it feels the field generated by
others. When si = ci for all particles, this reduces to a standard symmetric pairwise interaction. In
this case, qi might represent a charge (for electric fields) or a mass (for gravitational fields). The
pairwise force takes the general form
Fi←j = Fmag (rij , qi , qj , t)r̂ij
(13)
where rij = ||ri − rj || is the distance between the particles, and r̂ij is the unit separation vector
from source to receiver (so −r̂ is attractive).
There are 11 different laws or worlds, shown in Table 4. We group them into 6 two-particle worlds,
which follow a radial force centered on particle 1, and 5 “extra” worlds, which have slightly different
semantics, as listed in the table.
From Newton’s second law, F = ma, we can derive the acceleration a = (ax , ay ) of a particle as
follows:
a = −Fmag r̂/m
(14)
If there are multiple particles, we sum the forces:
X
ai = −
Fij r̂ij /mi
(15)
j̸=i

From this, we can derive the velocity by integration, and hence generate the trajectory of each
particle from its initial conditions.
The benchmark requires the agent to submit a Python function that returns the predicted trajectory.
The function must satisfy the following signature:

def discovered_law(pos1, pos2, p1, p2, velocity2, duration, **params):
...
return trajectory
Here params are free parameters of the law which can be fit to the collected data by the
FORCEBENCH environment before it calls the above function. The agent can choose the initial
position of particles 1 and 2, and the velocity of particle 2. (The velocity of particle 1 is fixed
at (0, 0).) The meaning of the control knobs p1 and p2 varies across the worlds: sometimes they
represent masses, sometimes charges (see Table 4 for details).
The LLM baseline method from (Wiemann et al., 2026) uses an LLM to generate code which computes the acceleration function a, from which it derives the trajectory by integration. In Table 8, we
give examples of the generated code. In MDA, we instead estimate Fmag , and then derive a using
Newton’s law in Eq. (14), which we pass to the integrator. (MDA also estimates its own parameters,
using the posterior mean associated with the submitted model, rather than using the environment’s
fitting function.) We could of course ask the LLM to generate Fmag instead, but this would be a
different method to the one used in (Wiemann et al., 2026).

### C.2 The Design Space

An experiment (action a) is a single probe launch in the benchmark’s own API: the probe is released
from position (r0 , 0) with velocity v, under two scalar coupling knobs (p1 , p2 ) whose roles (source
charge, probe inertia, . . . ) are part of what must be discovered.
The design space Ξ for TWO PARTICLE WORLDS is the fixed menu of 13 such launches in Table 5.
This space was chosen by an LLM to cover the relevant dimensions. The design space for MULTI PARTICLE WORLDS is shown in Table 6. VoI (and the LLM/random acquisition baselines) selects
one action per round. Note that these are discrete spaces, to make the VoI maximization problem
simple.
action a
r0
v (launch)
p1 p2
1–8
{1.5, 2, 3, 4, 5, 6, 8, 10} [0, 0] (radial drop) 1 1
9–10
{2, 4}
[0, 0.4] (tangential) 1 1
11
4
[0, 0]
2 1
12
3
[0, 0]
1 2
13
4
[0, 0]
2 2

purpose
radial profile (short→long r0 )
orbit shape (angular momentum)
identify the role of p1
identify the role of p2
vary both knobs

Table 5: The design space Ξ for the 6 TWO PARTICLE WORLDS — a fixed menu of 13 probelaunch experiments. Each is a probe released from (r0 , 0) with velocity v under coupling knobs
(p1 , p2 ); VoI selects one per round. The seed launch D0 is action 3 (the passive radial drop at
r0 =3). Rows 1–8 sweep the radial force profile — the long r0 ≥5 drops probe where any screening
has decayed, decisive for Yukawa/extra-dim (VoI selects r0 =5, 6; Figs. 14, 1b); rows 9–10 add
angular momentum; rows 11–13 vary the two coupling knobs to identify their roles (source charge
vs. probe inertia, a=F/p2 ). The held-out interventional test set uses more extreme knob settings
(p1 ∈ {3, 4, 5}, p2 ∈ {3, 5}).

### C.3 Interactive App

To make the task concrete, we built PhysicsPlayground, a self-contained web app that lets a reader
play a simplified version of the game that the agent must solve. Figure 6 shows a screenshot. The
top row is a transduction puzzle in the style of ARC-AGI but for a physical law: two training experiments (a launch radius r0 and the resulting orbit r(t), the raw trajectory the discovery algorithm
fits) and two test forecasts — a launch at a new radius, and a launch under a perturbed source
(do(mass×2)), the interventional “what if” the method targets. At the bottom of the screen is the
playground, where the user can launch their own orbits, read the animated trajectories, and work out
the force law. Finally they submit their forecast for each test launch in the top right, and they can
then choose to reveal the truth to self-score.

world
ether
Hubble
circle
dark-matter
three-species

system
central + drift ⃗a=(0, α)
central + H⃗r
11-body ring
+ K hidden masses
30 bg., hidden couplings

each experiment sets
# discovers
5 orbiters, r∈[3, 8], v=2.8
6 F, α
5 orbiters, r≤8
6 F, H
ring R, launch v, R-scaled t 6 exponent p
continuous (x, y, vx , vy )
∞ # & loc. of masses
probe direction
4 couplings → species

Table 6: Design spaces for the 5 MULTI PARTICLE WORLDS. Unlike the fixed 13-launch menu
of the two-particle worlds (Table 5), these are heterogeneous. Ether and Hubble use a fixed set of
5-probe orbiter launches on top of a central force plus a background term (a uniform drift α, or a
Hubble expansion H); circle sweeps the radius of an 11-body self-gravitating ring with per-radius
measurement times (a wide-ring sweep breaks the scale degeneracy that otherwise hides the force
exponent); dark-matter designs a continuous tracer launch (x, y, vx , vy ) by VoI to localise unseen
point masses; three-species probes the 30-particle background from a few directions to recover each
particle’s hidden coupling, then clusters the couplings into species (count k chosen by BIC). “#” is
the number of candidate experiments (∞ = a continuous design box).

Figure 6: App for FORCEBENCH. The goal is to identify a hidden central-force law from a few probe
orbits, then predict held-out launches — including one under a perturbed source. Training orbits (top
left), held-out interventional test forecasts (top right), and the reader’s own budgeted experiment bench
with an animated measured orbit (bottom). Available at https://claude.ai/code/artifact/
565fe6cc-a355-4c19-bf7e-b44e766cf87e.

### C.4 Parameters and Their Priors

On FORCEBENCH the candidate structures are open ended: the LLM proposes a force magnitude
F (r, qi , qj , t; θ), where each model has its own free parameters and bounds. Each free parameter
takes a uniform prior over the proposer-declared bounds; see Table 7. The joint prior factorises as
p(m, θ) = p(m)

Cm
Y

pk (θk )

(16)

k=1

where we use a structure prior of the form
p(m) ∝ e−λCm
20

(17)

where Cm is the number of free parameters of structure m, and λ = 2.5 is the Occam penalty per
free parameter. Thus the posterior over structures is
p(m | D) ∝ Zm e−λCm
Z
Zm = p(D | θ, m) p(θ | m) dθ

(18)
(19)

where Zm is the SMC marginal likelihood. The explicit e−λCm term is added as an additional
regularizer, since on near-deterministic data (σ=0.03), a more flexible form can win Zm by fitting
the observation noise. (Note that penalizing the length of the representation of the function F —
computed either by string length or Halstead complexity (Halstead, 1977) — did not work as well,
since that ignores the flexibility of the underlying “elementary” functions that are used.)
We currently fix the observation noise to σ = 0.03. However, this could invite overfitting, since
a more flexible model can win marginal evidence by driving residuals below that noise floor. The
principled remedy is to be Bayesian about σ — put an inverse-gamma prior on the residualvariance
and marginalize it, giving a Student-t marginal likelihood −(a + M/2) log b + 12 SSE(θ) over all
M residuals, whose scale is tied to the known noise floor via b. This removes the arbitrary fixed-σ
dependence and, being scale-invariant in the residuals, no longer rewards fitting below a floor.
Empirically, however, σ-marginalization alone does not cure the overfitting, and can worsen model
selection: with the hundreds of residuals these many-body worlds provide, the marginal likelihood
over-rewards any reduction in SSE by a factor ∼ M/2 (a Lindley-paradox-like effect), so a flexible
form that absorbs the observation noise wins, and the Occam factor alone does not compensate.
Fortunately the explicit prior on models, p(m), to encourage simplicity suffices. This combination
is robust and, on Hubble, converts a near-miss (the pool’s spurious time-modulated 1/r, a small ε
fitting the noise) into the clean 1/r result reported above.
Quantity
Symbol
Prior / value
Role
Inferred: a candidate’s free coefficients θ (prior = Uniform over the declared bounds):
coupling strength
k
Uniform(0.01, 5)
force magnitude
screening length
λ
Uniform(0.5, 40)
Yukawa / range cutoff
radial exponent
p
Uniform(0.5, 2.5)
power-law falloff 1/rp
oscillation frequency
ω
Uniform(0.1, 6)
time-varying force
oscillation phase
ϕ
Uniform(0, 2π)
time-varying force
Structure prior (Bayesian Occam over the parameter count):
penalise flexibility
number of free params Cm
p(m) ∝ e−2.5 Cm
Fixed (not inferred):
charge / inertia roles
qi , qj , m qi =1; p1 , p2 set charge, inertia driving force
integrator step
∆t
0.005 (symplectic)
forward model
measurement times
t
{0.5, 1, 1.5, 2, 3, 4}
readout grid
seed launch
D0
one passive drop at r0 =3
warm-start data
position noise
σ
0.03 (fixed Gaussian)
likelihood

Table 7: Parameters and priors for the FORCEBENCH force-law rung (the physics analogue of
the ephys parameter conventions, App. E). The candidate laws are LLM-proposed, so θ is not a fixed
list; each free parameter takes a uniform prior over the proposer’s declared bounds — the recurring
parameters (those of the six ground-truth laws) and representative ranges are shown, and a candidate
has Cm =1–3 free parameters. Only these coefficients are inferred; everything else is fixed. The
structure prior p(m) ∝ e−2.5Cm is the Bayesian–Occam penalty of §4.1; the likelihood is a fixed-σ
Gaussian on the probe positions at the measurement times, and each structure’s marginal evidence is
read off an adaptive-tempering SMC (Np =200 particles, target ESS 0.6, Rp =3 random-walk moves
at half the particle SD per tempering rung).

### C.5 Laws Discovered for Two-Particle Worlds

Table 8 shows the laws discovered by MDA and the pure LLM agent after B = 8 experiments on
TWO PARTICLE WORLDS. Looking at the details of the discovered laws, we see that sometimes the
result looks different from the truth but is mathematically equal. For example, on FRACTIONAL the
truth is F = kqi qj /r3−2α with α = 0.5, and MDA proposes the simpler but equivalent expression
F = kqi qj /r2 .

method
best submitted law
gravity — True law F =k qi qj /r, k=0.16
MDA
F = k*qi*qj/r

nMSE %pass<0.1 %≡
4.4×10−5

100

100

3.8×10−1

22

11

8.3×10−4

100

89

3.3×100

33

11

5.5×10−2

56

67

2.8×10−1

22

89

oscillator — True law F =k qi qj cos(ωt+ϕ)/r, k=0.80, ω=π/2, ϕ=0
MDA
F = qi*qj*k*cos(w*t +
1.3×10−2
phi)*exp(-r/lam)/r

100

0

9.7×10−1

33

0

2.5×10−6

100

100

1.1×10−1

56

56

9.4×10−3

100

89

6.4×10−1

22

22

9.2×10−4
5.4×10−1

93
31

74
31

k=0.159

LLM

ax = -C*p1*x/(p2*r2)
C=0.158

Yukawa — True law F =k qi qj K1 (r/λ)/λ, k=0.16, λ=2
MDA
F = k*qi*qj*k1(r/lam)/lam
k=0.152, lam=2.064

LLM

ax = F * dx / r
n=4.06, a=1.0, b=1.0

Coulomb — True law F =k qi qj /r2 , k=1
MDA
F = k*qi*qj/r**2
k=0.986

LLM

f = -p1 * p2 / (r2 * r)
eps=0.002

k=1.096, lam=4.548, w=1.569, phi=-0.035

LLM

ax = F * dx / r
G=0.01, n=5.0, a=1.0, b=1.0

fractional — True law F =k qi qj /r3−2α (≡1/r2 ), k=0.16, α= 12
MDA
F = k*qi*qj/r**2
k=0.159

LLM

a = -k * p1 / (p2 * r2)
k=0.035

extra-dim — True law F =k qi qj ΦKK (r), R=0.5
MDA
F = k*qi*qj/r**2 + sigma*qi*qj
k=0.254, sigma=0.023

LLM

a mag = k * p1 / (p2 * r)
k=0.163

grand mean MDA
grand mean LLM

Table 8: Laws discovered for the six FORCEBENCH worlds by MDA and the pure LLM agent
(Opus 4.7, B = 8 experiments; regenerated from the same runs as Fig. 2). For each world we show
the true force law and each method’s best (lowest-error) submitted law with its fitted parameters
(MDA submits a force magnitude F ; the LLM writes an acceleration line, of which we show ax
or the radial a, whichever is simpler). nMSE is the DiscoverPhysics normalized MSE (MSE/testtrajectory variance), geometric mean over the 9 runs. %pass<0.1 is the fraction of runs with nMSE
below the paper’s 0.1 threshold (dropping their explanation score); %≡ is the fraction exactly formequivalent to the true law (form-MSE < 10−3 at unit charges, isolating the form from the chargerole).

We score each run two ways. The exact-form rate (%≡) is the fraction of runs whose submitted law is functionally equivalent to the truth after removing parameters and constants; we judge
this by the form-MSE at unit charges (p1 =p2 =1), which isolates the radial/temporal form from the
charge-role handling, and call a run exact when this form-MSE is below 10−3 . The numeric rate
(%pass<0.1 ) instead uses the DiscoverPhysics benchmark’s own criterion: the normalized MSE,
nMSE = MSE/Var where Var is the variance of the held-out test trajectories (accounting for the
different total particle travel across worlds), counting a run as passing when nMSE < 0.1. We drop
the benchmark’s second gate — an LLM-judged explanation score ≥ 0.9 — because we found it
unreliable (Section C.7).
Under these metrics MDA recovers the exact form in 74% of runs and passes numerically in 93%,
versus 31% and 31% for the LLM agent budget-matched to one experiment per round (the same
B = 8 budget MDA uses). This gap is one of data efficiency, not capability. The DiscoverPhysics
benchmark lets an agent submit a batch of experiments each round, so its nominal 16-round budget
collects far more than 16 experiments; run un-throttled in its native batched protocol, our LLM

held-out test MSE (log)

103
102
101
100
10−1
10−2
10−3
10−4

held-out test MSE (log)

Bayes-forecast

103
102
101
100
10−1
10−2
10−3
10−4

LLM-forecast

gravity (1/r)

103
102
101
100
10−1
10−2
10−3
10−4

pass

oscillator

103
102
101
100
10−1
10−2
10−3
10−4

pass

0

2

4
6
experiment budget Na

VoI acquisition

8

Yukawa

103
102
101
100
10−1
10−2
10−3
10−4

pass

fractional

103
102
101
100
10−1
10−2
10−3
10−4

pass

0

2

4
6
experiment budget Na

LLM acquisition

8

random acquisition
Coulomb

pass

extra-dim

pass

0

2

4
6
experiment budget Na

8

Figure 7: Per-world data efficiency on TWO PARTICLE WORLDS (Opus 4.7; the compact aggregate is Fig. 2
in the main text). One panel per world. Colour = forecaster (blue Bayes-forecast, purple LLM-forecast);
line style = acquisition (VoI solid, LLM dashed, random dotted). The initial value at Na = 0 is the result
based on D0 before any experiments. Uncertainty is ±1 SE in log10 over 9 runs (3 random initial conditions
× 3 draws per IC): a shaded band on the continuous best-so-far Bayes-forecast/VoI traces, and error bars on
the Na ∈ {0, 2, 4, 8} budget points of both forecasters. Within the Bayes-forecaster family the VoI and LLM
design strategies perform similarly and both generally beat random.

agent uses ∼41 experiments and reaches nMSE 0.013, essentially reproducing the paper’s strongest
agent (Opus, nMSE 0.01; (Wiemann et al., 2026)). MDA reaches that same accuracy with only 8
one-per-round experiments — a ∼5× data-efficiency advantage (Fig. 2, right).
Is the advantage the curated design menu? MDA chooses experiments from the fixed 13-launch
menu of Table 5, hand-built to contain informative probes, whereas the pure agent chooses initial
conditions freely. One might worry that this curated design space — rather than the Bayesian inference — is what drives MDA’s lead. To test this we ran an Opus agent given the same menu:
each round it picks a menu experiment, and after 8 experiments it submits its own best-fit force law
(no SMC). It reaches only 22% numeric pass and 17% exact-form — no better than the free-choice
Opus agent (31%), and far below MDA’s 93%. So the menu is not the source of MDA’s advantage:
handed the identical design space, an LLM’s own propose-and-fit inference remains far weaker than
MDA’s SMC-evidence selection and VoI design. (Conversely, the base-model sweep of Section C.8
shows the gap does narrow with a much stronger agent, Fable 5 — so the advantage is the inference,
and its size depends on how good the free-form agent’s own inference is.)

### C.6 Data Efficiency Curves

In Fig. 7 we plot the data efficiency curves for each of the six TWO PARTICLE WORLDS, from which
the aggregated results in Fig. 2 are obtained. In Fig. 8 we plot similar curves for each of the five
MULTI PARTICLE WORLDS. We see that MDA beats LLM agent by a large margin.
The above figures, and Fig. 2 in the main text, follows the DiscoverPhysics protocol and reports
only the numeric metric. Figure 9 adds the symbolic (exact-form) view we use as a secondary, more
stringent check: the fraction of runs whose submitted force law is the ground-truth form exactly
(form-MSE < 10−3 on held-out unit-charge cases, isolating the functional form from the chargerole). MDA recovers the exact form for ∼70% of runs within a few experiments, roughly twice the
Opus agent’s rate; note this exact-form test is stricter than, and can diverge from, numeric accuracy
(a strong agent may write a law it cannot accurately integrate, and a predictive law need not be the

2

held-out test MSE (log)

103
102
101
100
10−1
10−2
10−3
10−4

4
6
number of experiments Na
ether (drift)

pass ( < 0.01)

8

2

pass ( < 0.01)

2

circle (N-body)

103
102
101
100
10−1
10−2
10−3
10−4

4
6
number of experiments Na

held-out test MSE (log)

held-out test MSE (log)

pass ( < 0.01)

held-out test MSE (log)

held-out test MSE (log)

Hubble (expansion)

103
102
101
100
10−1
10−2
10−3
10−4

103
102
101
100
10−1
10−2
10−3
10−4

4
6
number of experiments Na
dark matter (hidden)

103
102
101
100
10−1
10−2
10−3
10−4

three species (couplings)

pass ( < 0.01)

8

2

4
6
number of experiments Na

8

MDA: best-so-far MSE(Na)
base agent (budget Na ∈ {2, 4, 8})
pass ( < 0.01)

Opus 4.7 on the five extension worlds
(hidden-mass worlds: MSE capped by
chaotic many-body dynamics --- correct
discovery, near-miss prediction)

8

2

4
6
number of experiments Na

8

Figure 8: Data efficiency on MULTI PARTICLE WORLDS using Opus 4.7. We plot held-out forecast MSE
vs. experiments for MDA (solid, mean±SE over seeds) against the pure agent (dashed). MDA is orders of
magnitude better at every budget. Several worlds clear the pass line (error of 0.01 or less) within three experiments. Ether and dark matter plateau above the line, but this is the intrinsic ceiling of their scoring ( due
to near-singular free-fall and a chaotic many-body system), not a discovery failure (since MDA recovers the
correct drift and the hidden monopole).
ForceBench (DiscoverPhysics), aggregated over all 6 worlds: MDA recovers the exact force law, passes numerically, and reaches the DiscoverPhysics paper's accuracy within a few designed experiments

numeric accuracy (% runs, nMSE < 0.1)

symbolic accuracy (% runs, exact form)

80
60
40
20
0

1

2

3

4
5
6
experiment budget B

7

numeric accuracy vs. budget

100

MDA (Opus)
LLM agent (Opus)

8

normalized MSE vs. #experiments

80
60
40
20
MDA (Bayes + VoI)
LLM agent (Opus)

0
1

2

3

4
5
6
experiment budget B

7

8

normalized MSE (nMSE, geo-mean)

symbolic (exact-form) accuracy vs. budget

100

MDA (Bayes + VoI), 1 design/round
LLM agent, throttled 1 exp/round
LLM agent, un-throttled (41 exp)

100
10−1
DiscoverPhysics paper (Opus agent)

10−2
10−3
1

2

4
8
16
number of experiments

32

Figure 9: Numeric and symbolic data efficiency on FORCEBENCH (Opus 4.7; the numeric-only, multi-basemodel version is Fig. 2). (left) Symbolic (exact-form) accuracy vs. budget: MDA (blue) vs. the pure LLM agent
(purple). (middle) Numeric accuracy (nMSE < 0.1): MDA reaches ∼93%; the agent ∼31%. (right) nMSE vs.
number of experiments, with the un-throttled Opus agent (star) reproducing the DiscoverPhysics paper’s ∼0.01
at its native ∼41-experiment budget. Error bars are ±1 SE over the 6×9 runs.

canonical form) — see Section C.8 for the Fable comparison, where the gap between the two metrics
is largest.

### C.7 Explanation Metric

A low held-out MSE does not certify a correct model: a law can be “right for the wrong reasons,”
fitting observed orbits without capturing the mechanism. (Wiemann et al., 2026) proposed to fix
this by asking each agent to return a text explanation to accompany its predicted law; this is then
evaluated using an LLM judge. However, we have found this metric to be unreliable. For example
Fig. 10 shows that the explanation score is essentially flat in the number of experiments, and often
moves non-monotonically (more data making it worse), because the discovered functional form
converges within the first couple of experiments and the residual movement is run-to-run variation
in how the LLM phrases the same law, filtered through an 11-level judge.

Opus 4.7

Fable 5

gravity (1/r)

Yukawa

Coulomb

oscillator

fractional

extra-dim

1.0
explanation score ↑

MDA
base agent

DeepSeek v4 Pro

0.8
0.6
0.4
0.2
0.0

explanation score ↑

1.0
0.8
0.6
0.4
0.2
0.0

2

4
number of experiments Na

8

2

4
number of experiments Na

8

2

4
number of experiments Na

8

Figure 10: The LLM explanation score vs. number of experiments (six worlds, Opus 4.7). Flat and unreliable: sometimes monotonically decreasing with more data (Coulomb 0.83→0.77→0.73), sometimes nonmonotonic (Yukawa 0.37→0.70→0.60) — either way more data can lower the score, a weak instrument (contrast the interventional forecast, which improves monotonically, Fig. 2).

An alternative is to test the ability of the model to predict under different kinds of novel distribution
shifts, which is equivalent to testing its robustness to interventions on the mechanism. As proved
in (Richens & Everitt, 2024), an agent that can perform such out-of-distribution predictions reliably
must have learned a causally correct model of the world. In fact FORCEBENCH already evaluates
models performance in this way: it measures MSE on test sets that combine one long-horizon probe
and two single-knob interventions. Focusing on predictive performance on interventional test sets is
not only more robust, but it also more general, since it does not require comparing to some (usually
unknown) “true model”.

### C.8 Robustness to the Base Model

The headline comparison uses Opus 4.7 as the shared base model, where the pure LLM agent is
weak (Table 8). This raises a fair question: is MDA’s advantage an artifact of a particular (weak)
agent, and would it vanish with a stronger base model? In this section, we consider three base
models spanning a wide capability range: Opus 4.7, Fable 5, and DeepSeek v4.
Figure 11 shows the MSE results across the 6 worlds. We see that Fable is able to catch up with
MDA’s data efficiency in 5 out of 6 of the worlds. However, we note that we beat Fable at small
number of experiments using a much cheaper model (DeepSeek), provided we augment it with MDA
(which has negligible cost). Further experimentation with Fable on MULTI PARTICLE WORLDS and
other scientific domains is left to future work (since running Fable is expensive).
In Fig. 12 we aggregate results across worlds, but also show symbolic accuracy, not just MSE. Two
patterns emerge. First, MDA is essentially model-agnostic: its numeric pass rate is 89–94% and its
exact-form rate 74–83% regardless of the base model — the Bayesian machinery (SMC evidence,
VoI design) does the heavy lifting, and a stronger proposer helps only at the margin. Second, the
pure agent is highly base-model-dependent: its numeric pass rate swings from 26% (DeepSeek)
and 31% (Opus) up to 81% for Fable 5, a much stronger recent model. So the striking gap against
the Opus agent narrows sharply against Fable.
Even against the strongest agent we tested, MDA’s extra inference on the same proposals never
hurts and sharply helps: MDA attains the higher numeric pass rate (94% vs. 81%; Fig. 12, middle)
and reaches nMSE ≈ 10−3 in ∼ 2 designed experiments, an accuracy the Fable agent reaches only at
B=8 (right). On the joint metric that credits a run only when it is both exact-form and numerically
correct, the two methods tie (74% each). The one axis on which the Fable agent leads is pure exactform recovery (93% vs. 78%), and that lead is partly illusory: a free-form agent writes its own
integrator, so it can name the exact law without being able to compute with it. On coulomb, for

held-out test MSE (log)

103
102
101
100
10−1
10−2
10−3
10−4

held-out test MSE (log)

Opus 4.7

103
102
101
100
10−1
10−2
10−3
10−4

Fable 5

gravity (1/r)

103
102
101
100
10−1
10−2
10−3
10−4

pass ( < 0.01)

oscillator

103
102
101
100
10−1
10−2
10−3
10−4

pass ( < 0.01)

0

2
4
6
number of experiments Na

MDA (Bayes-forecast + VoI)
pure LLM (LLM-forecast + LLM-acq)
pure LLM, Na = 0 (zero-shot)

DeepSeek v4 Pro

8

Yukawa

103
102
101
100
10−1
10−2
10−3
10−4

pass ( < 0.01)

fractional

103
102
101
100
10−1
10−2
10−3
10−4

pass ( < 0.01)

0

2
4
6
number of experiments Na

8

Coulomb

pass ( < 0.01)

extra-dim

pass ( < 0.01)

0

2
4
6
number of experiments Na

8

Figure 11: Effect of changing the proposer LLM on data efficiency: held-out test MSE vs. experiment budget
B, per world, for three proposer LLMs (Opus 4.7, Fable 5, DeepSeek v4 Pro; colour). Solid: MDA (Bayesforecast + VoI acquisition), the best-so-far MSE(B) trajectory with a ±1 SE band. Dashed: the matched
pure-LLM agent (LLM-forecast + LLM acquisition) at B ∈ {0, 2, 4, 8}, with ±1 SE error bars and anchored
at its B=0 zero-shot law (⋆). Uncertainty is over 9 runs (3 seeds × 3 draws), geometric mean ±1 SE in log10 .
Grey: the pass threshold (0.01). Across proposers, MDA drives the held-out error to the identifiability floor
within a few experiments, whereas LLM agent behavior plateaus well above it on most worlds, except in the
case of Fable.

instance, the Fable agent scores 100% exact-form but only 11% numeric, whereas MDA — using
the same proposals with a vetted forward model — scores 67% numeric.
The residual exact-form gap is not because MDA cannot propose the exact law: it uses the same
LLM proposer (Fable), and a truth-equivalent form is present in its Nm ≈14-candidate pool in the
large majority of runs. It is a model-selection effect: the Bayesian evidence sometimes outvotes the
truth in favour of a slightly more flexible form that fits the observation noise marginally better (e.g. a
spurious weak time-modulation on top of the correct radial law). We counter this with a parsimony
submission rule: at submission, among the pool forms that share the winning force-profile shape
F (r), we return the fewest-parameter member — evicting the over-elaborated near-duplicates the
M-open exploration introduces, the same ESS-eviction idea used in CHEMBENCH (Section D). This
recovers the exact form on the time-modulation misses, lifting MDA’s exact-form rate 74% → 78%
and its joint metric to parity with the agent (74%), at negligible numeric cost (94% → 93%; green
vs. blue in Fig. 12, left). The remaining gap (dominated by oscillator, where MDA recovers a
predictive but non-canonical form) reflects structure identifiability, not inference quality. We read the
overall pattern as the honest boundary of the result: MDA’s contribution is robust, model-agnostic
accuracy under a tight budget — an inference layer that dominates the predictive metric and at least
matches a strong free-form agent on structure, not an unbounded lead over any conceivable agent.

### C.9 Example: Coulomb World

In this section, we visualize behavior of MDA when applied to COULOMB world, as shown in
Fig. 13. On the left, we show what happens when a probe is launched near the source. At unit
charge (p1 =1) the true law k qi qj /r2 and the charge-blind overfit k/r2 trace the same orbit (grey)
— fit on unit-charge data, they are identical there, so no probe placement, at any radius or launch,
can tell them apart. Turning the source charge to p1 =4 — a do(a) on the mechanism — scales the
true law’s force fourfold (green) while the overfit is unmoved (orange): the orbits split, and that split
is what the observations measure.

ForceBench with the Fable-5 base model on both arms: MDA's Bayesian inference on Fable's proposals dominates numeric accuracy and nMSE convergence (mid, right); parsimony narrows the exact-form gap (left, green), where the strong unaided agent is otherwise ahead

numeric accuracy (% runs, nMSE < 0.1)

symbolic accuracy (% runs, exact form)

60
40
20
0

1

2

3

4
5
6
experiment budget B

numeric accuracy vs. budget

100

MDA (Fable)
MDA + parsimony
LLM agent (Fable)

80

7

normalized MSE vs. #experiments
100

80
60
40
20
MDA (Bayes + VoI)
LLM agent

0

8

1

2

3

4
5
6
experiment budget B

7

8

normalized MSE (nMSE, geo-mean)

symbolic (exact-form) accuracy vs. budget

100

MDA (Bayes + VoI), 1 design/round
LLM agent, throttled 1 exp/round

10−1

10−2

10−3
1

2

4
number of experiments

8

Figure 12: Data-efficiency curves with the strongest base model (Fable 5) on both arms, aggregated over all
six FORCEBENCH worlds. (left) Exact-form accuracy vs. budget: the parsimony submission (green) lifts MDA
(blue) toward the strong unaided agent (purple), which leads on pure structure recovery. (middle) Numeric
accuracy (fraction of runs with normalized MSE < 0.1): MDA reaches ∼ 94% within ∼ 3 designed experiments
and dominates the agent everywhere. (right) Normalized MSE vs. number of experiments: MDA converges to
∼ 10−3 in ∼ 2 experiments, an accuracy the throttled agent reaches only by B=8. So even against a strong
proposer, MDA’s Bayesian inference on the same proposals never hurts and sharply helps on the predictive
metric. Error bars are ±1 SE over the 9 runs (3 seeds × 3 LLM draws) per world.
only a charge intervention splits the true law from its overfit

3

value of information over the design space

5

candidate designs
argmax VoI (chosen)
seed drops (p1 = 1)

launch

y

0

source

−1
−2
−3

= 1: both laws (identical)
= 4: true k qiqj/r2
= 4: charge-blind k/r2
observed (p1 = 4)

0.80

4

0.64
3

0.48
2

0.32
0.16

p1

1

p1

−4

p1

−4

−3

−2

−1

0

1

2

3

4

0.96

VoI (law disagreement)

1

source charge p1 (intervention knob)

2

unit-charge probes (any r0): laws agree, VoI ≈ 0

2.0

2.5

x

3.0

3.5
4.0
4.5
probe release radius r0

5.0

5.5

6.0

0.00

Figure 13: Visualising COULOMB world and its design space.

On the right, we plot the VoI over a 2d slice of the design space, namely the release radius r0 (an
initial condition) × source charge p1 (an intervention knob). The red × are the seed drops: the unitcharge probes the agent has already collected (the initial, un-designed observations both laws are fit
to). VoI is ≈ 0 all along the unit-charge axis, and rises only with the charge, so MDA’s VoI-driven
design step reaches for a charge intervention (green ring), not a farther probe. Thus we see that
changing a causal (mechanism) knob, not just the initial location, is needed to distinguish a correct
law from a curve-fit.

### C.10 Example: Yukawa World

Whereas COULOMB’s discriminating design is a charge intervention (Fig. 13), YUKAWA’s is a spatial
extrapolation. The screened kernel K1 (r/λ)/λ and the power laws fit to short-range data are nearly
identical for r ≤ λ and diverge only beyond it, so a probe confined within λ cannot tell them
apart while one reaching past λ can (Fig. 14). This is why the VoI design reaches for the longrange r0 =5, 6 drops (Table 5), and why the true kernel only reaches the convex corner of the Pareto
frontier (Fig. 1b) once such a probe is added.

### C.11 Example: Discovering Hidden Particles

In this section we give a simplified example of the DARK-MATTER world, where the challenge is to
identify both the number and location of hidden particles.

Short-range probe (r
2.0

Yukawa (true) K1(r/λ)/λ

≤ λ): hypotheses agree

Long-range probe (r0 = 6

1/r p

1.5

≫ λ): hypotheses split

screening λ

K0(r/λ)/λ

6

1/r 2
1/r

4

1.0
0.5

2

0.0

y

y

launch r0 = 1.5

source

launch r0 = 6

0

source

−0.5
−2

−1.0

Yukawa (true) K1(r/λ)/λ

−1.5

−4

K0(r/λ)/λ
1/r p
1/r 2

−2.0

1/r

−2.0 −1.5 −1.0 −0.5

−6
0.0
x

0.5

1.0

1.5

2.0

observed (true law)

−6

−4

−2

0
x

2

4

6

Figure 14: Probe orbits under the candidate force laws for YUKAWA world: a short-range vs. a longrange design. The screened Yukawa kernel K1 (r/λ)/λ and the power laws fit to the short-range seed data
nearly coincide for r ≤ λ and diverge only beyond it. (left) Launched within the screening length (r0 =1.5),
every candidate law traces almost the same orbit — they cannot be told apart. (right) Launched well beyond
it (r0 =6, matching the long-range probes of Fig. 1b): the true screened kernel (green, with the observed data)
has decayed, so it holds a wide slow arc, whereas the un-decayed power-law near-misses are far too strong at
this range and plunge inward — the hypotheses fan out.

The model class. Neutral test probes move in a known static 2D Poisson field: a source of coupling
q at position s pulls a probe at x with force q/(2π∥x − s∥) toward s, and the field superposes over
sources. One visible source of known coupling sits at the origin; the world also contains K hidden
sources whose positions and couplings are concealed. A probe released from rest therefore falls not
toward the visible source but toward the total mass, so it appears to accelerate toward empty space
— the dark-matter tell (Fig. 15, middle, arrows). The structure m is the count K; its parameters are
the 3K hidden coordinates and couplings. The design knob a ∈ I is the probe launch configuration
(x, y), a point in the plane, encoded as a do(·); we record the probe under position noise σ = 0.03.
Because the sources are point masses, not a density field, the forward model is small-N and the
whole rung runs on CPU.
The task. The true world has one visible source (q = 2 at the origin) and one hidden mass (q = 4
at (3.5, 2)). The method is handed three seed probes released far from the hidden mass, so they feel
it only as a weak far-field deflection: enough to reveal that some unseen mass exists, but too little to
say where. It must (i) decide how many hidden masses there are, (ii) localize the one that exists, and
(iii) choose where to place the next probe. We fit K ∈ {0, 1, 2} by adaptive-tempering SMC over
the hidden coordinates (Algorithm 3, Np = 1000) and combine by marginal evidence (§A.2); K=0
is a genuine zero-parameter model (visible field only), so comparing it to K=1 is Bayesian model
selection, and comparing K=1 to K=2 is Bayesian Occam — a second mass must earn its three
parameters against the prior volume they cost.
Model selection and localization. The evidence is decisive (Fig. 15, left): p(K=1 | D) ≈ 0.97,
with K=0 excluded outright (its visible-only field cannot bend the probes toward empty space) and
K=2 rejected by Occam (fitting a second, redundant mass buys a negligible likelihood gain for a
three-parameter prior-volume penalty). The recovered mass sits at (3.53, 1.97) ± (0.13, 0.09) with
coupling 3.99 ± 0.07 — correct in count, position, and strength. That the count is inferred, not
assumed, is the point: this is the latent-existence question (§2) — is there an unobserved cause, and
how many — answered by evidence.
Where to look, in a 2D design space. Which placement best localizes the mass? We score each
candidate by the query-relevant VoI (Eq. (5)) for a downstream query — a test probe released near
the hidden mass, whose outcome depends on the hidden-mass position. The VoI landscape (Fig. 15,

how many hidden masses?

0.6

2.6

4

0.80

2.4

2

0.64

2.2

0

0.4

−

−

0.2
0.0

0.96

0.03

0.00
K=0
(none)

K=1
(one)

K=2
(two)

−

VoI

posterior p(K ∣ D)

0.8

6

0.48

2

0.32

4

y

1.0

probe deflections + where to look next

0.97

hidden-mass localization (2σ)
from 3 seed probes
+ VoI-chosen probe
truth

2.0
1.8
1.6

0.16

visible source
hidden mass (truth)
argmax VoI

6
−

6

−

4

−

2

0

2

4

6

0.00

1.4

posterior σ: 0.11 → 0.00
3.0

3.2

3.4

x

3.6

3.8

4.0

Figure 15: The hidden-mass rung. Left: trans-dimensional model selection p(K | D) from the seed probes
— the deflections demand a hidden mass (K=0 excluded), and Bayesian Occam rejects the surplus second
mass (K=2). Middle: the scene. The visible source (star) sits at the origin, but the seed probes (released
from the dots) deflect toward empty space (arrows) — toward the hidden mass (red cross). The blue field is the
query-relevant VoI over candidate next-probe placements; it peaks on the hidden mass, and the argmax (green
ring) sits essentially on it. Right: the K=1 posterior over the hidden-mass position (2σ ellipses): the three
seed probes localize it only loosely, and the single VoI-chosen probe collapses the uncertainty onto the truth.

middle) peaks sharply on the hidden mass: a probe placed there measures it directly, while probes
on the far side (visible-dominated) are nearly useless. Running the argmax probe drives p(K=1) to
1.0 and collapses the position posterior from σ ≈ 0.11 to ≈ 0.01 (Fig. 15, right) — the localization
the seed probes could not reach.

Easy

Medium

Hard

Overall

Method

SA

Ex

SA

Ex

SA

Ex

SA

Ex

MDA (VoI)
MDA (Mean)
LLM-AUTOSCILAB (us)

66.7
54.2
41.7

83.3
79.2
58.3

45.8
58.3
41.7

79.2
87.5
75.0

54.2
33.3
41.7

79.2
66.7
75.0

55.6
48.6
41.7

80.6
77.8
69.4

LLM-AUTOSCILAB (reported)

55.6

88.9

22.2

37.0

42.9

52.4

35.1

50.9

Table 9: Performance on CHEMBENCH at B=60, 36-task stratified subset (12 domains × 3 tiers).
SA = symbolic accuracy (%); Ex = E X ACC at the 0.05 threshold (%, for comparability with the
reported row); bold = best among the top three rows. The bottom row is LLM-AUTOSCILAB’s
published numbers from (Kabra et al., 2026, Table 3), based on a different, unreleased 36-task
subset, and using gpt-4o-mini instead of our use of Opus 4.7.

## D Chemistry: Additional Details

### D.1 Benchmark

The problem is to learn a static algebraic function of seven controllable inputs (substrate, inhibitor,
second substrate and product concentrations, enzyme loading, temperature and pH) to a reaction rate
y:

y = f CA , CI , CB , CP , Enz, T, pH; θ ,
(20)
The unknown is which kinetic mechanism is active. There are 9 canonical single mechanisms
(Michaelis–Menten, competitive / uncompetitive / noncompetitive / product inhibition, substrate
inhibition, Hill cooperativity, Arrhenius temperature dependence, ping-pong bisubstrate), and 48
compound mechanisms, created from combinations of these elementary mechanisms (e.g., pingpong×Arrhenius, MM×competitive×Arrhenius and Hill×Arrhenius), yielding a total of 57 rules or
worlds. The dataset is divided into easy, medium, and hard tiers, based on the mechanisms used and
their corresponding parameters (some of which make the response hard to detect).
Performance of a submitted law is evaluated using the procedure described in (Kabra
et al., 2026, App.C). First we compute the held-out root-mean-squared log-error RMSLE =
1 PN
2 1/2
over N =1000 test points. Then we compute whether
i=1 log(1+ŷi ) − log(1+yi )
N
the law is numerically equivalent to the true law using E X ACC= 1[RMSLE < ϵ], a quantity they
call the “exact accuracy”. The released benchmark code uses ϵ=0.05 for chemistry (and 0.01 for
physics). Our data-efficiency curves (Fig. 3) use the stricter App. C threshold ϵ=0.01, whereas the
head-to-head Table 9 reports ϵ=0.05 to match LLM-AUTOSCILAB’s published numbers. They also
compute symbolic equivalence to the true law using sympy.

### D.2 Further Results

Table 9 reports symbolic accuracy (SA) and exact accuracy (E X ACC, at their 0.05 threshold for
comparability), per difficulty tier and overall, at a max budget of B=60 experiments. We see that
MDA beats their method overall (SA 56 vs. 42 and E X ACC 81 vs. 69), as well as on every tier. Crucially, MDA wins on the hard tier, where LLM-AUTOSCILAB’s low-error
√ solutions are numerically
0.87 log(0.5 Enz/...)
accurate but mechanistically meaningless (e.g. recovering 10
at RMSLE=0.001,
which passes even the strict 0.01 threshold, yet the symbolic-equivalence check marks it as wrong).

### D.3 Ablations

In Fig. 16, we show the effects of ablating various parts of the MDA method (36-task subset, B = 60
experiment budget).
• We start by using vanilla SMC, as in the ModelSMC paper (Wahl et al., 2026), combined
with Monte Carlo (random sampling) based optimization of the VoI.
• Next we add M-open exploration. This lifts overall symbolic accuracy 36→50% — driven
by the easy tier, where the residual-directed re-prompt corrects the single-mechanism form

Ablation of MDA's extensions (36-task subset, B = 60)
Overall
Easy

80

Medium
Hard

75
67

symbolic accuracy (\%)

70
60
50

67
56

50

40

42
36

30

33 33

33

MDA
(MC-VoI)

+ -open
exploration

50

42

42 42

54
46

20
10
0

+ CMA-ES
VoI

+ ESS-adaptive
pool

Figure 16: Ablation of MDA’s extensions beyond ModelSMC: symbolic accuracy per tier and overall, added
incrementally on the 36-task subset at B=60. Each extension helps a distinct tier. M-open exploration lifts the
easy tier (42→75%, single-mechanism correction; also the only route to any compound recovery) but leaves
the hard tier flat; CMA-ES VoI and then the ESS-adaptive pool lift the hard tier (33→42→54% — sharper
designs, then evicting the over-elaborated near-duplicates exploration introduces). The full config is the twoseed result of Table 9; intermediate configs are seed 0.

(easy SA 42→75%). This is the only route to any compound recovery (0→11%, since
the fixed library of 9 primitives cannot express compound mechanisms). Interestingly, this
does not help the hard tier, where the mechanism’s signal is too weak under the extreme
parameters.
• Next we add CMA-ES optimization of VoI. This sharpens the design, raising exact numerical accuracy 36→42% and hard-tier SA 33→42%.
• Finally we add the ESS-adaptive pool. This lifts overall SA 50→56% and hard-tier SA
42→54% by evicting the over-elaborated near-duplicates the exploration introduces. Together they turn the ModelSMC base (36% SA) into a method that wins every tier of the
fair comparison.

From a constant current to a spike train to the f--I curve
(a) constant current → a spike train
T

(b) the f--I curve (spike count feature)

(period)

80

20

firing rate (Hz)

V

membrane voltage (mV)

40
0

−20
−40

60
40
20

−60

count = 7 spikes
rate = 1/

−80

T

0

20

40
60
time (ms)

80

100

0

rheobase
≈ 3 μA

0.0

2.5

5.0 7.5 10.0 12.5 15.0 17.5 20.0
injected current 0 (μA/cm2)
I

Figure 17: The f–I curve, and why we count spikes. (a) A constant supra-threshold current makes the model
fire a periodic spike train; the readout is simply the spike count (red markers) — or, per unit time, the firing
rate 1/T . (b) Sweeping the injected current traces the f–I curve (firing rate vs. current): flat and zero below
the rheobase (the smallest current that fires, red), then rising. This matches the intuitive “how many spikes”
readout.

## E NEURONBENCH

This appendix covers the deterministic form of the benchmark: background on neuron electrophysiology and Hodgkin–Huxley models, the problem specification, the (tractable, synthetic-feature)
solution methods, the benchmark results and baselines, and case studies. The stochastic form —
where the likelihood becomes intractable — is deferred to Section F.

### E.1 Primer on Neuron Electrophysiology

In this section, we give a brief introduction to neuron electrophysiology.
We can view a neuron as a device that turns an injected current into a voltage trace. At rest the
membrane voltage V sits near −65 mV. A small (sub-threshold) injected current depolarises V a
little and it relaxes back — a passive, RC-like response. A large enough (supra-threshold) current
triggers an action potential or spike: voltage-gated Na+ channels open regeneratively, V shoots to
∼+40 mV in under a millisecond, then K+ channels open and pull it back down. Spikes are the
neuron’s output; their count (or rate) as a function of the injected-current amplitude is the f–I curve
(frequency–current), the standard input–output summary of a cell: see Fig. 17.
Crucially, the behavior of the neuron depends on its inputs, as illustrated in Fig. 18. Here we show
the voltage over time, under 3 different experimental conditions: the standard model, stimulated
with a 10 µA step signal, which generates repeating spikes (blue); the same model stimulated with
a 2 µA step signal, which fails to trigger a response (dotted black); and the model modified by
applying TTX blocker and then stimulated with a 10 µA step signal, which also fails to trigger a
response (red line). This illustrates why experiment design is critical in this domain.

### E.2 Primer on Hodgkin-Huxley Models

In this section, we give a brief primer on generalized Hodgkin-Huxley models. The model is named
after Alan Hodgkin and Andrew Huxley who invented it in 1952 to explain the ionic mechanisms
underlying the initiation and propagation of action potentials in the squid giant axon. Since then,
the model has been generalized and is widely used to mechanistically explain the spiking behavior
of many kinds of neurons. Hodgkin and Huxley received the 1963 Nobel Prize in Physiology or
Medicine for this work.
The model they came up with can be represented as an electric circuit, as shown in Fig. 19. This
example contains Na, K, M and L ion channels, but the generalized model can contain different
combinations of the 6 channels listed in Table 11, each of which have their own parameters and
dynamics. We can write the generalized model as a set of nonlinear ODEs, which follow from

Figure 18: Example spike traces from a single neuron under different conditions. Membrane voltage
under current injection: a supra-threshold step (10 µA) elicits overshooting action potentials (blue); the sodium
blocker TTX (gNa =0, a do on the mechanism) abolishes them (red); a sub-threshold current gives a passive
response (grey).
inside (membrane potential V )

gNa ϕNa

gK ϕK

gM ϕM

gL

ENa

EK

EM

EL

C

Iext

outside (extracellular reference)

Figure 19: The Hodgkin–Huxley equivalent circuit (Eq. (21)). The membrane is a capacitor C; each ion
channel is a branch with a variable conductance gc ϕc (opening/closing gates ϕc ) in series with a battery Ec
(the reversal potential). The injected current Iext charges the capacitor and flows through the open channels;
a blocker deletes a branch (gc →0). Which branches are present is the structure; the conductances gc are the
parameters.

Kirchoff’s current law:
C

X
dV (t)
= Iext (t) −
Ic (t)
dt

(21)

c∈C

Ic (t) = gc ϕc (t)(V (t) − Ec )
ϕc (t) = mpc c (t) nqcc (t) hrcc (t)
∞
Tx,c
(V (t)) − xc (t)
dxc (t)
=
, x ∈ {m, n, h}
dt
τx,c (V (t))

(22)
(23)
(24)

Here C is the capacitance, V (t) is the voltage, Ic is the current for channel c, C is the set of channels
associated with this neuron, and ϕc (t) is the fraction of the channel that is open. Thus the current
in the channel is given by Ic = gc ϕc (V − Ec ): (maximal conductance) × (fraction open) × (driving force). The fraction open ϕc (which changes over time) is based on a product of gating terms
— denoted by mc , nc and hc — each raised to an integer power (pc , qc , rc ; how many independent gates the channel has): see Table 11 for the list. Each such gating term xc relaxes towards a
∞
voltage-dependent target Tx,c
(V ) with its own time constant τx,c (V ) (fast for activation, slow for
inactivation), given by
∞
Tx,c
(V ) =

αx (V )
1
, τx,c (V ) =
αx (V ) + βx (V )
αx (V ) + βx (V )
33

(25)

gate

channel

mNa
hNa
nK

+

Na
Na+
K+

role

∞
target Tx,c
(V )

speed

activation
inactivation
activation

rises with depolarisation
falls with depolarisation
rises with depolarisation

fast
slow
slow

Table 10: The three classic Hodgkin–Huxley gates. Activation gates (mNa , nK ) open as the cell
∞
depolarises; the inactivation gate (hNa ) closes. Each relaxes to a voltage-dependent target Tx,c
(V )
with its own time constant τx,c (V ); the fast/slow separation between mNa and {hNa , nK } is what
generates and terminates the spike. Other channels (Table 11) carry their own gates mc , nc , hc with
the same form but different half-voltages and kinetics.
Channel

carries

+

Na
sodium
K+ (delayed rectifier) potassium
Ca2+ (high-threshold) calcium

current

role in the response

blocker (a do)

INa = gNa m3Na hNa (V −ENa )
IK = gK n4K (V −EK )
ICa = gCa m2Ca hCa (V −ECa )

regenerative spike upstroke
repolarises the spike
alternative, slower spike upstroke
slow; spike-frequency adaptation
transient outward; delays firing onset
sets the resting potential;
passive

tetrodotoxin (TTX)
TEA
cadmium (Cd)

M-type K+

potassium IM = gM mM (V −EK )

A-type K+ (transient)

potassium IA = gA mpA hA (V −EK )

leak

mixed

IL = gL (V −EL )

XE991
4-AP
—

Table 11: The voltage-gated ion channels — the building blocks. A blocker is a drug that removes one channel by setting its conductance gc =0; these are the mechanism-level interventions
do(a) available on this rung (e.g. TTX abolishes Na+ -based spikes but not Ca2+ -based ones). The
parenthetical drug names in this table refer to these blockers, and are what the design loop gets to
apply.
where expressions for αx and βx can be found at https://en.wikipedia.org/wiki/
Hodgkin-Huxley_model. As example, the classic spiker is the following three-channel model
C V̇ = Iext − gNa m3Na hNa (V −ENa ) − gK n4K (V −EK ) − gL (V −EL )

(26)

Here the Na+ channel carries an activation gate mNa (cubed) and an inactivation gate hNa , and the
K+ channel a single activation gate nK (to the fourth); Table 10 summarises the three. The names
∞
(V ) (whether it opens
m, n, h are historical: what actually distinguishes a gate is its target curve Tx,c
or closes as V rises) and its time constant τx,c (V ). It is the separation of timescales — fast mNa
activation admitting Na+ for the upstroke, before the slower hNa inactivation shuts it off and the
slower nK activation repolarises — that makes the spike a transient, regenerative event.
It is worth noting that HH is only one point on a spectrum of models at different levels of abstraction.
There are more detailed stochastic models that capture individual cellular responses at a more granular level. There are also simplified models, such as the two-variable FitzHugh–Nagumo model, and
the leaky integrate-and-fire model. Finally, if we set the membrane time constant to P
zero and binarise the output, we get the McCulloch–Pitts unit (McCulloch & Pitts, 1943), y = ϕ( i wi xi − b),
which is the basis of artificial neural networks. So there is no single “true model”. Instead, scientists
seek the coarsest valid causal abstraction that is sufficient for the things they want to understand or
predict (Beckers & Halpern, 2019; Rubenstein et al., 2017).

### E.3 Our Benchmark

We design a benchmark, NEURONBENCH, by creating 6 “mystery neurons”, each composed of a
plain Na+K+leak spiker plus one extra membrane mechanism, chosen from the list in Table 12:
five are novel mechanisms and the sixth is a recallable textbook M-current control. Each of the five
novel mechanisms is deliberately tuned to be silent under every textbook probe, i.e., the plain and
novel neurons fire identically to standard current steps and channel blockers. This requires the agent
to propose novel experimental protocols that it has not already memorized.

The task The agent is told that it will be presented with some voltage trace data from a neuron
of unknown type, and is asked to propose various candidate mechansims (the exact prompts are
shown in Section G.3). It is also given the menu of stimulation protocols (Table 13) and channel
blockers, and a fixed experiment budget. From a handful of designed experiments it must (i) propose
its own candidate mechanisms m and return a posterior p(m | D) over them, and (ii) forecast the
cell’s response to held-out interventions it never ran. The truth is never revealed to the agent; it
is used only for scoring. (A solver may of course restrict its hypothesis space — e.g. MDA fits a
pool of conductance archetypes — but the benchmark neither supplies nor assumes an enumerated
candidate set.)
Evaluation. The task is counterfactual trajectory forecasting: on a disjoint set of held-out protocols the agent never ran, it must predicts the cell’s response — a spike count and a voltage trace
per protocol. Because the hypothesis space is open we score behaviour, not model labels, on two
levels. (i) The spike-forecast MSE (the headline metric): the mean-squared error of the predicted
test-window spike counts. (ii) The feature-forecast MSE (a secondary, finer metric for model-based
deep-dives): the standardised MSE, over the per-trace summary feature vector s(y) of Eq. (30) between the agent’s predicted trace and the truth.
Npte that the feature-forecast requires predicting a full trace, which is then converted to summary
features. Generating a trace is hard to do for a pure LLM based forecaster, but is easy for a modelbased one. We reduce the prediction to a set of features in order to make the comparison to ground
truth more meaningful (see Section E.4).
Specification of the novel channels.
textbook ones:
IZ = gZ mpZ hqZ (V − EZ ),

Each novel channel has roughly the same gated form as the

V −V m
∞
Tm,Z
(V ) = σ km1/2 ,

V −V h
∞
Th,Z
(V ) = σ − kh1/2 ,

(27)

m
h
with σ(u) = 1/(1 + e−u ) the logistic (Boltzmann) sigmoid, half-voltages V1/2
, V1/2
, slopes
km , kh >0, and fixed time constants τm , τh : activation rises with V and inactivation falls, while
a negative activation slope km <0 instead makes the channel hyperpolarisation-activated (as for Ih ),
h
and an inactivation half-voltage V1/2
below rest makes it de-inactivated by hyperpolarisation (available only after a hyperpolarising pre-pulse). This Boltzmann form is generic across the novel channels but is not the textbook parameterisation shown in Eq. (25), which are monotonic curves of the
same qualitative shape but not identical logistic sigmoids.

Design space. The agent gets to control the external current Iext (t) = xt injected at each step. In
our benchmark, we assume the current is chosen from one of the 9 sequence options in Table 13. In
principle the agent can also apply a single channel blocker (tetrodotoxin (TTX) zeroing gNa , TEA
zeroing gK , cadmium (Cd) zeroing gCa , or none), giving a nominal 9 × 4 actions. But the novel
mechanisms are by construction silent under blockers as well as under textbook steps — a blocker
deletes a channel branch equally in the plain and novel cells, so it cannot separate them — so the
blockers are non-discriminating for these worlds. We therefore report all experiments over just the
9 current-clamp protocols (blockers remain available in the released benchmark and the interactive
app, but are unused in the runs, for simplicity).
Interactive app. Figure 20 shows a screenshot for a web app we built that lets users try
this benchmark for themselves. The app is available at https://github.com/murphyk/
neuronbench.

### E.4 The Likelihood: Summary Features, Not the Raw Trace

Because a spike is a ∼1 ms all-or-none event, a sub-millisecond timing mismatch between model and
data produces a ∼100 mV pointwise error even for an essentially correct model. Hence a likelihood
that factorizes over time steps
p(y1:T |ξ, m, θ) =

T
Y
t=1

35

p(yt |zt , σ 2 )

(28)

(gZ , EZ )

activation†

Z-REBOUND (IZ )

(4, +120)

(−57, 5, 4, 2)

TEXTBOOK-M (IM )

(2.5, −77)

(−35, 10, 60, 1)

Mechanism

inact.†

behavioural
protocol)

signature

(revealing

(−88, 4, 130) spike-count collapse after a hyperpolarising conditioning pulse
H-SAG (Ih )
(5, −30)
(−95, −5, 140, 1) —
voltage sag + post-inhibitory rebound on a hyperpolarising step
NA-FATIGUE
—
slow inactivation added to hNa
use-dependent spike-count rundown over paired long pulses
CA-REBOUND (ICaT ) (3.2, +120) (−54, 6, 2, 2)
(−87, 4, 22) low-threshold rebound burst on release from hyperpolarisation
D-TYPE (ID )
(9, −77)
(−30, 10, 3, 1)
(−80, 5, 200) delayed / suppressed firing after a
hyperpolarising pre-pulse
—

spike-frequency adaptation on a
long step (recallable by name)

Table 12: The six worlds of NEURONBENCH. Each current is added to a Na+K+leak spiker via
Eq. (27); the row label is the Fig. 4 panel name. † the activation/inactivation columns are the tuples
(V1/2 , k, τ, power) and (V1/2 , k, τ ) of Eq. (27). Conductances gZ in mS/cm2 ; reversals EZ , halfvoltages and slopes in mV; time constants in ms; p, q are gate powers (q=1 when an inactivation
gate is present, else 0). All are tuned to be indistinguishable from the plain spiker under textbook
steps and blockers and separable only by the matched non-textbook protocol in the last column
(a hyperpolarising conditioning pre-pulse for the de-inactivating currents). NA-FATIGUE adds no
channel: it slows the inactivation of the existing Na+ gate hNa . The IM control is a standard noninactivating K+ current the LLM can name and probe.
#

protocol

segments (∆t ms, I µA)

probes

1
2
3
4

brief step
long step
strong step
weak step

(40, 12)
(300, 10)
(120, 18)
(120, 5)

fast onset
spike-frequency adaptation
high-rate firing
near-threshold f–I

5
6
7
8
9

hyperpol. conditioning + test
hyperpol. pre-pulse + weak test
paired long pulses
depol. conditioning + test
brief hyperpol. conditioning + test

(250, −30), (150, 12)
(250, −30), (120, 0), (60, 6)
(300, 12), (60, 0), (300, 12)
(250, 15), (150, 12)
(40, −30), (150, 12)

de-inactivation / depol. block
rebound at low drive
use-dependence / slow inactivation
depolarising history
fast de-inactivation

Table 13: The nine-protocol menu of external currents that can be applied over which VoI
is enumerated on NEURONBENCH. Each protocol is a sequence of (duration, amplitude) current
segments; a leading hyperpolarising segment is a conditioning pre-pulse. Rows 1–4 are standard
current-clamp steps; rows 5–9 are the non-textbook protocols that expose the hidden mechanisms of
Table 12 — exactly one is decisive for each, so only a designed (VoI-chosen) experiment identifies
the mechanism.
is dominated by nuisance spike-timing noise and is useless for spiking data. We instead use a feature
(synthetic / simulation-based) likelihood, the standard choice in this field. That is, we replace the
above with Eq. (7), which we repeat here:
p(y1:T |ξ, m, θ) ∝

J
Y

p(sj (y1:T )|ξ, m, θ)

(29)

j=1

where sj is the jth feature (a scalar) derived from the entire trajectory y1:T .
Deterministic synthetic likelihood. The above synthetic likelihood does not factorise over time.
However, because we assume the latent dynamics are deterministic and the initial state is known,
it is tractable to compute: we solve the ODE for z1:T , read off the predicted features sj (m, θ) =
sj (z1:T ), and evaluate the kernel
R in closed form. By contrast, if the dynamics are stochastic, the
likelihood p(sj (y) | m, θ) = p(sj (y) | z1:T ) p(z1:T | m, θ) dz1:T has no closed form, so we have
to marginalize out over the latent paths, as we discuss in Section F.1.

Figure 20: NEURONBENCH. Screenshot of our app, which lets users interact with the same environment
we give our agents (except the agents see numerical data, not images.) The top left is the training set, Dtr ,
the top right is the test set, Dte , and the bottom row is the interactive environment. The agent can choose a
sequence of input currents x1:T by specifying the magnitude and duration of a step pulse (shown in orange).
The agent can also choose from a finite set of interventions, corresponding to blocking different ion channels
(shown as white boxes). The resulting output current y1:T is shown in the green trace. App is available at
https://claude.ai/code/artifact/2848d02d-cdc1-4c1c-99fe-c0034e9714fb.

The summary statistics. The summary statsitic we use are spike counts in the test and conditioning windows, their use-dependent run-down, within-pulse adaptation, and two sub-threshold voltage
summaries, as illustrated in Fig. 21. These are comptued as follows:

− nlate
, min V (t), V̄end
npre , npre − ntest , nearly
s(y) =
ntest ,
,
(30)
test
test
|{z}
{z
} | t {z } |{z}
{z
} |
|{z}
|
test spikes
steady
state
adaptation
pre-pulse spikes

run-down

Vmin

where ntest , npre count upward zero-crossings of V in the test window (after any conditioning prelate
pulse) and before it, nearly
test −ntest splits the test window in half, and V̄end is the mean voltage over
the steady-state tail of the trace (the final few percent, after the stimulus ends). This is chosen so that
both the rate-signature worlds (NA-FATIGUE, TEXTBOOK-M) and the sub-threshold/burst worlds
(H-SAG, CA-REBOUND) leave a signal.
Gaussian likelihood.

For real-valued summaries we use a Gaussian kernel
Y
p(y1:T | m, θ) =
N (sj (y1:T )|sj (z1:T ), σj )

(31)

j

where z1:T = unroll(m, θ, z0 ) is the trajectory deterministically generated by solving the ODE
defined by m and θ from the initial condition z0 .
Poisson likelihood. In some cases, the features are just the spike counts {nk } at different input
currents ak . Since this is a set of non-negative integers, the natural observation model is a product
of Poissons:
Y

p(y1:T | m, θ) ∝
Poi nk (y1:T ) ; λk (m, θ) ,
λk (m, θ) = nk z1:T (m, θ) .
(32)
k

Here the rate λk of the k-th count is obtained by running the candidate forward — solving its ODEs
under protocol ak to get the voltage trace z1:T = Vθ (·; ak ) — and then applying the same spikecount feature map nk (·) used on the data, i.e. counting upward threshold crossings of that simulated
trace. That scalar predicted count is the Poisson mean; the observed recording supplies the Poisson
“data” nk (y1:T ). So the deterministic model sets the mean spike count per protocol and the Poisson
supplies the trial-to-trial spike-count dispersion (in practice we average a few repeats per protocol).

Voltage trace → per-trace feature vector s(y) = (ntest, npre, npre−ntest, adapt, Vmin , V̄end) (what the likelihood scores, not the raw trace)
(b) sub-threshold features: hyperpolarising step (Ih sag)

(a) spike-count features: paired pulses
60

npre = 22
(conditioning pulse)

40

= 16
(test pulse)
ntest

40

adaptation
(early−late = 10)

20
0

0

V (mV)

V (mV)

20

−20

−20

−40

−40

−60

−60

−80
0

100

run-down npre−ntest = 6

200

300

400
time (ms)

̄

Vend

−80

(steady-state tail)

(sag / hyperpolarisation depth)
100
200
300
400
time (ms)

Vmin

500

600

700

0

500

600

Figure 21: From a raw voltage trace to the per-trace feature vector s(y) of Eq. (30), computed on real
NEURONBENCH traces. (a) On a paired-pulse protocol the spike-count features are the test- and pre-pulse
counts (ntest , npre ; upward 0 mV crossings, triangles), their use-dependent run-down npre −ntest (here the
slow-NaNA-FATIGUE cell fires less on the second pulse), and the within-pulse adaptation (early-half minus
late-half of the test window, dashed divider). (b) On a hyperpolarising step the sub-threshold features are the
voltage minimum Vmin (the Ih sag / hyperpolarisation depth) and the steady-state tail V̄end . These six numbers
— not the raw trace — are what the synthetic likelihood and the feature-forecast metric score.

V (mV)

HHbench, world ``ca rebound'': under the VoI-designed experiment (hyperpol pre-pulse + weak test (-30 uA/250 ms, gap, +6 uA)),
the observed spike count matches the +novel model, not the plain Na+K model --- this is what the Poisson likelihood scores
observed recording
(Na+K neuron): 4 spikes

60
40
20
0
−20
−40
−60
−80

prediction: plain Na+K
2 spikes (≠ observed)

prediction: +novel current
4 spikes (= observed) ✓
observed
model prediction

0

100

200

300
time (ms)

400

500

0

100

200

300
time (ms)

400

500

0

100

200

300
time (ms)

400

500

Figure 22: Visualizing the predictions of two different models on CA-REBOUND. We show the observed
recording (left) and the spike response predicted by each candidate structure (plain Na+K neuron in middle,
augmented model with novel channel on right) under the VoI-designed experiment. The plain Na+K neuron
fires 2 spikes and misses the rebound (middle, ̸= observed); the neuron with the extra current fires the 4-spike
rebound burst that matches the data (right, = observed). The Poisson likelihood scores exactly this: the spike
count each deterministic model predicts is the Poisson rate (Eq. (32)), so the observed count identifies the
mechanism.

Example: CA-REBOUND. In this section, we visualize the predictive distribution p(y1:T |m) for
two different hypotheses m — the plain Na+K+L neuron, and the correct Na+K+L+Z neuron —
and show the resulting summary statistics. These results are for the CA-REBOUND world, and are
obtained under a VoI-designed experiment ξ (here a hyperpolarising pre-pulse that de-inactivates
the hidden Ca2+ current, then a weak test). Fig. 22 visualizes a trace y1:T and its summary statistic
(4 spikes), followed by a prediction E[y1:T |m, ξ] and the summary statistics we derive from each
prediction (2 spikes and 4 spikes). We see that despite the trajectory being reduced (in this case) to a
single integer, s(y1:T ), the synthetic likelihood can discriminate the correct model from the incorrect
one, if the design ξ is chosen properly.

### E.5 Parameters and Priors

Table 14 lists what is inferred and under what prior. The only free parameters are the maximal conductances gc of the present channels; each is given an independent log-normal prior centred on its literature nominal value, with a log-space SD of 0.7 — a 1σ band of roughly [nominal/2, nominal×2],
deliberately broad since the target is a real cell of unknown size. The membrane capacitance, reversal
∞
potentials, and the voltage-dependent gating kinetics Tx,c
(V ), τx,c (V ) are held fixed (a channel is

Quantity

Symbol

Prior / value

Role

Inferred (only for channels present in the structure m):
Na+ conductance
gNa
LogNormal(log 120, 0.72 )
+
K (delayed rect.)
gK
LogNormal(log 36, 0.72 )
Ca2+ (high-thr.)
gCa
LogNormal(log 12, 0.72 )
+
A-type K (transient) gA
LogNormal(log 45, 0.72 )
+
M-current (slow K )
gM
LogNormal(log 1.0, 0.72 )
leak
gL
LogNormal(log 0.3, 0.72 )

spike upstroke
repolarisation
alt. spike carrier
onset delay
spike-freq. adaptation
resting potential

Fixed (not inferred):
capacitance
reversal potentials
gating kinetics

membrane
driving forces
channel identity

C
ENa/K/L/Ca
∞
Tx,c
(V ), τx,c (V )

1.0 µF/cm2
+50/ − 77/ − 54.4/ + 120 mV
Hodgkin–Huxley forms

Observation model (feature-kernel tolerances σj ):
sub-threshold count
σ
0.3 spikes (tight; enforces rheobase)
supra-threshold count σ
1.2 spikes
input resistance
σ
0.06 mV/pA

likelihood
likelihood
likelihood

Table 14: Parameters and priors for NEURONBENCH. Only the maximal conductances of the
channels present in a candidate structure are inferred (so the minimal Na+K+leak model has three
free gc , the Na+K+M+leak winner four); everything else is fixed. Conductances gc are in mS/cm2 .
The log-normal priors are centred on literature nominals with a broad 0.7 log-SD; the SMC uses
Np =70 particles, target ESS 0.5, Kp =3 random-walk-Metropolis moves per tempering rung, and a
0.12 log-space proposal SD.

its kinetics; only its density gc is free), and the feature-kernel tolerances σj are the fixed observation
model.

### E.6 Results on the Benchmark

Figure 4 shows the results of MDA and the LLM baseline on NEURONBENCH. For these results,
we used the Poisson likelihood on the spike count, as in Eq. (32). We see that MDA is substantially
more data efficient.

### E.7 Model Selection Deep Dive

In this section, we give a worked example of model selection, to better understand how MDA
works. We focus on the H-SAG world. The LLM is shown only the phenotype (a depolarising
sag during hyperpolarisation, then a rebound) and proposes the candidate channels: HCN/Ih , T-type
Ca2+ , Kir, A-type K+ , and persistent Na+ , which map onto four distinct dynamical hypotheses
{Ih , T-type, D-type K, plain}. This is genuinely M-open: the phenotype is consistent with several
real channels (all can rebound), so proposing them is correct, not a mistake, and only an experiment can decide. A textbook depolarising input step leaves all four candidates identical (posterior
unmoved from the uniform prior), whereas the VoI-designed hyperpolarising probe concentrates the
posterior on Ih in one shot. Figure 23(a) shows why: under that probe only Ih produces the depolarising sag; the others stay pinned at the hyperpolarised floor. After discovering the right model
structure, SMC continues to refine the posterior over the parameters, as shown in Fig. 24.

### E.8 Learning Summary Statistics Using a 1D CNN

In this section we give a concrete example of the approach discussed in Section A.4 for learning
a set of summary statistics. In NEURONBENCH we already know the “right” hand-crafted answer,
namely the features shown in Eq. (30), but this section shows how a learning based approach can
give comparable performance; we will use this in earnest for the stochastic benchmark in Section F.
Extracting summary features using a neural network. We replace s(y1:T ) with a learned encoder sϕ (y1:T ) which we train as follows: (1) simulate a bank of (m, θ) → y1:T raw voltage traces

HHbench (h sag), M-open discovery: the LLM PROPOSES the candidate channels (top); a Gaussian synthetic likelihood on the feature vector identifies Ih (bottom)
(a) under the VoI-designed hyperpolarising experiment, only Ih shows the depolarising sag
Ih (truth) ✓ sag
D-type

40

40

40

40

20

20

20

20

0

0

0

0

−20

−20

−20

−20

−40

−40

−40

−40

−60

−60

−60

−60

−80

−80

−80

−100

injected current

0

200

time (ms)

400

−100

sag
0

200

time (ms)

400

feature 2: spike count

(b) what the likelihood sees: the feature vector s(θ)
27.5
25.0
22.5
20.0
17.5
15.0
12.5

T-type
plain

observed s(y) ± σ

Ih

D-type

−2.5

0.0

2.5
5.0
7.5 10.0 12.5
feature 1: sub-threshold sag (mV)

15.0

−100

posterior over LLM's candidates

V (mV)

T-type

plain

−80
0

200

time (ms)

−100

400

0

200

time (ms)

400

(c) a textbook probe leaves the hypotheses tied;
the VoI-designed probe identifies Ih
1.0

prior

+ textbook probe

+ VoI probe

0.8
0.6
0.4
0.2
0.0

T-type

Ih

D-type

plain

Figure 23: M-open structure discovery on NEURONBENCH (H-SAG world). The LLM is given only the
phenotype and proposes the candidate channel mechanisms; they are mapped onto four dynamical hypotheses
(the truth Ih is not revealed). (a) Under the VoI-designed experiment — a hyperpolarising conditioning step
(grey, injected current) then a depolarising test — only Ih (red) shows the slow depolarising sag during hyperpolarisation; the T-type, D-type, and plain candidates stay pinned at the hyperpolarised floor. (b) What the
likelihood actually sees: the feature vector s(θ) = (sag, spike count) for each candidate (coloured points) and
the observed features s(y) ± σ (black star). The Gaussian synthetic likelihood scores only these two numbers
— not the raw trace — and the observed point coincides with Ih , the only candidate with a large sag. (c) The
posterior over the LLM’s own candidate set: uniform at the prior, unmoved by a textbook probe (which cannot
distinguish them), and collapsed onto Ih after the single VoI-designed probe. Together with Fig. 24 this exercises the whole loop — LLM proposal, M-open selection, then parameter refinement — on NEURONBENCH.

under the design protocol menu; (2) train a small 1-D CNN encoder sϕ (y1:T ) ∈ Rd with two supervised heads — classify the channel structure m (four candidates, as in Fig. 23) and regress its
conductance g — on that bank; the supervised targets are what forbid collapse.9 The two heads are
used only to train the encoder — the softmax over structures is a discriminative posterior p(m | y),
not a likelihood, and both heads are discarded at inference. What we keep is the penultimate-layer
embedding sϕ (y1:T ) ∈ Rd (d=8), which plays exactly the role of the hand-crafted feature vector of
Eq. (30).
The likelihood on the learned summary. We then use the multivariate Gaussian likelihood in
Eq. (8) to define p(s|m, θ). This is the multivariate generalisation of the per-feature Gaussian
kernel of Eq. (31): the deterministic hand-feature case reads the mean off a single rollout with
hand-set tolerances σj , whereas the learned (and stochastic) case estimates both the mean and
the covariance from the R simulations already drawn for the likelihood. Equation (8) plugs into
the model-SMC unchanged, model selection being driven by the log-density gap log N (sϕ (y) |
µa , Σa ) − log N (sϕ (y) | µb , Σb ) between candidates.
Training cost, data, and re-fitting as the pool changes. The encoder is deliberately tiny —
three 1-D convolutional blocks (1 → 16 → 32 → 32 channels) into an 8-dimensional embedding with a classification and a regression head — so both the data and the compute are negligible. The training bank is 350 simulated traces per candidate structure (1400 total for the four
9
The released open-world auto-select integration (Section F) uses this same 1-D CNN, but pre-trained once
over the channel-archetype family and then frozen. Because the convolutional encoder ends in global average
pooling it is protocol-length agnostic, so one encoder serves every world, protocol, and candidate pool without
the per-pool re-fit — the amortised, family-trained summary of “Sufficiency as the hypothesis pool grows”
(Section A). Only the Gaussian moments of Eq. (8) are re-estimated per candidate at scoring time; the particlefilter spot-check remains the out-of-family backstop.

HHbench (h sag): a Gaussian synthetic likelihood on trace features s(θ) refines the hidden channel's conductance; VoI-designed experiments do so fastest
(b) VoI contracts the posterior faster

after 0 exp.
after 2 exp.
after 6 exp.
truth

1

2

3

4
5
gh (mS/cm2)

6

7

VoI design
random design

2.0
posterior SD of gh

posterior density

(a) posterior over gh narrows with VoI-designed experiments

1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
0.0

1.5
1.0
0.5
0.0

8

0

1

2
3
4
# designed experiments

5

6

Figure 24: Parameter refinement on NEURONBENCH (H-SAG world: a hidden hyperpolarisation-activated
Ih current, the second half of the discover-then-refine loop begun in Fig. 23). Once the mechanism is identified,
its maximal conductance gh is inferred from the Gaussian synthetic likelihood on trace features s(θ) (the gating
kinetics are held fixed, per Table 14); because the model is deterministic this likelihood needs no simulationbased estimation. (a) The posterior over gh contracts from the uniform prior onto the truth (dashed) as VoIdesigned experiments accumulate. (b) VoI — which selects the hyperpolarising probes that make the sag, and
hence s(θ), depend on gh — contracts the posterior standard deviation ∼8× in a single experiment, whereas
random design, spending most probes on uninformative depolarising steps, lags several-fold. The menu here is
augmented with a battery of hyperpolarising steps at different depths.

{Ih , T-type, D-type, plain} hypotheses of Fig. 23), split 80/20 into 1120 train / 280 test; each trace
is a single forward solve under the protocol menu, downsampled to ∼750 samples. Training runs
for 40 epochs (batch 64, Adam at 2×10−3 ) and completes in about a minute on a laptop CPU/MPS
— no GPU cluster. The simulations dominate the wall-clock, and they are the same rollouts already
drawn for the synthetic likelihood, so the marginal cost of learning sϕ over hand-specifying it is
essentially free.
This also answers what happens when the outer model-SMC pool changes. We do not maintain one
global summary: sufficiency is task-relative to the current candidate set, so when the LLM proposes
a new mechanism we add a class and re-fit — a ∼one-minute job on simulations already in hand —
and the summary dimension simply grows with the pool. Re-fitting per round is cheap enough to
do routinely, and can be avoided altogether by amortising: training sϕ once over the LLM’s priorpredictive mechanism family (rather than the current pair) generalises to in-distribution proposals
without any re-fit. Either way the particle-filter anchor (Section F.1) catches an insufficient summary
should a proposal fall outside what sϕ was trained to attend to. See Section A.4 (“Sufficiency as the
hypothesis pool grows”) for the full argument.
Results. In Fig. 25(a), we show that, on held-out traces, the learned summary identifies the hidden
channel with 100% accuracy — above the hand-crafted [sag, spike-count] baseline (92%) — and
recovers the conductance to 0.56 mS/cm2 mean absolute error. Here the two hand features are
the sub-threshold “sag” — the slow depolarising recovery from the trough during a hyperpolarising
step, the signature of the hyperpolarisation-activated inward current Ih (HCN) — and the spike
count; together they discriminate the four candidate channels.
Figure 25(b) asks which windows the learned encoder actually relies on, via an occlusion analysis:
we mask each time window of the input and measure the resulting drop in the Ih logit. (We use occlusion rather than a raw input-gradient saliency because the latter is nearly uniform for this network
— a known pathology of vanilla saliency — and so localises nothing.) The importance concentrates
on the spike windows — the rebound burst after the hyperpolarising release and the depolarising
spike train (mean importance 0.54) — and is markedly lower across the sub-threshold sag phase
(0.20) and the quiescent stretches (0.25). So the network rediscovers that the discriminative signal
lives in the firing pattern, the {nk } spike-count features.

HHbench: a 1-D CNN LEARNS the synthetic-likelihood summary sϕ(V) from raw traces --- matching hand-crafted features and rediscovering them

100%

92%

protocol 2: depol step

20

80

0

60
40

−20

−80
learned
CNN sϕ

hand-crafted
[sag, count]

−100

1.0

0.5

−40
−60

20
0

protocol 1: hyperpol+release

40

occlusion importance (Ih-logit drop, norm.)

100

(b) occlusion importance: which parts of the trace the Ih decision needs
(mean: sag 0.20, spikes 0.54, quiescent 0.25)

60

V (mV)

held-out structure-ID accuracy (\%)

(a) parity: learned summary matches hand-crafted
(learned g MAE 0.56 mS/cm2)

sag window

0

100

200

300
400
500
time (downsampled samples)

600

700

0.0

Figure 25: Learning the NEURONBENCH synthetic-likelihood summary from raw traces (proof-ofconcept; runs on a laptop). A 1-D CNN encoder sϕ (V1:T ) is trained on simulated (m, g) → V traces to
classify the channel structure and regress its conductance. (a) On held-out traces the learned summary identifies the structure at 100% — above the hand-crafted [sag, spike-count] baseline (92%) — and recovers g to
0.56 mS/cm2 MAE. (b) Occlusion importance for the Ih class (orange, right axis: normalised drop in the Ih
logit when each time window of the input is masked) over a noise-free Ih trace (black) that concatenates two
protocols (separated by the dash-dot line): a hyperpolarising step+release (the Ih sag window marked by the
grey dotted bars) and a depolarising step. The decision rests on the spike windows (the rebound burst and the
depolarising spike train; mean importance 0.54), not the sub-threshold sag (0.20) or the quiescent stretches
(0.25): the network rediscovers that the {nk } spike-count features carries the discriminative signal. (Ih is the
hyperpolarisation-activated inward (HCN) current; the “sag” is its slow depolarising recovery during a hyperpolarising step. A raw input-gradient saliency is near-uniform here and thus omitted.)

## F NEURONBENCH STOCH

### F.1 Stochastic Latent Dynamics: Background

The worlds above use a deterministic Hodgkin–Huxley forward model, so the likelihood is available
in closed form (Section E.4). Real neurons are stochastic: with a finite number of ion channels,
gating fluctuates (channel noise), the latent dynamics become an SDE. This is the regime real experiments occupy, and the one setting our other benchmarks (deterministic ODEs + observation noise)
do not exercise.
To create a stochastic neuron, we add finite-N channel noise via the Fox–Lu diffusion approximation
(Fox & Lu, 1994), with the channel count N tuning the intrinsic noise from near-deterministic
(N → ∞) to strongly stochastic.
In more detail, each gate xc is really an ensemble of N two-state ion channels, each switching
open ↔ closed as a continuous-time Markov chain with the voltage-dependent rates αx (V ), βx (V )
of Eq. (25); the deterministic HH gating ODE is the N → ∞ mean-field limit of the open fraction.
The Fox–Lu diffusion approximation (Fox & Lu, 1994) keeps finite N by replacing that mean field
with a Langevin (stochastic differential) equation — the deterministic drift plus a Gaussian channelnoise term whose variance scales as 1/N :
q

dxc = αx (V )(1−xc )−βx (V ) xc dt + αx (V )(1−xNc )+βx (V ) xc dWt ,
x ∈ {m, n, h}, (33)
with dWt an independent Wiener increment per gate. The diffusion coefficient is the sum of the
two transition fluxes divided by N (the system-size / Ω-expansion correction to the channel master
equation), so more channels means smaller fluctuations and N → ∞ recovers the deterministic
gate. We integrate Eq. (33) by Euler–Maruyama and substitute the noisy gates into the membrane
equation (21), making N a single knob from near-deterministic to strongly stochastic. Fox–Lu is
the standard cheap channel-noise model; see Goldwyn & Shea-Brown (2011) for how it compares
to exact Markov-chain channel simulation.

### F.2 The Benchmark

We convert the deterministic six-world NEURONBENCH into a stochastic form by substituting the
Fox–Lu SDE (Eq. (33)) for the deterministic gate evolution in Eq. (21). We use the same design
space. This defines NEURONBENCH STOCH.

### F.3 Likelihoods

The marginal likelihood for model m is given by
Z
Zm = p(y1:T | m, θ) = p(y1:T | z0:T , m, θ) p(z0:T | m, θ) dz0:T ,

(34)

where y1:T is the observed voltage trace and z0:T the latent gating path. This requires marginalising over the stochastic latent path z0:T — a high-dimensional path integral with no closed form,
because the Fox–Lu transition density p(zt | zt−1 ) is itself intractable. Below we discuss how to approximate this integral using a bootstrap particle filter (Algorithm 4), as well as various other faster
approximations.
Particle filtering. The agent fits a stochastic state-space model (1) where the latent state zt =
(Vt , {xc (t)}) (voltage and gates) evolves by the discretised Fox–Lu transition p(zt | zt−1 , ξ) of
Eqs. (21) and (33), and the voltage is observed with Gaussian noise, yt ∼ N (Vt , σ 2 ). Candidate
models m differ in structure (which channels are present) and in the conductances θ; the channel
count N (the noise scale) is a known part of the model here. The one-step transition density p(zt |
zt−1 , ξ) has no closed form — it is a nonlinear diffusion over the interval — but the bootstrap particle
filter never needs it. It only samples the transition (one Euler–Maruyama step, i.e. a Gaussian draw
on the gates, Eq. (33)) as its proposal, and only evaluates the tractable observation density N (yt |
Vt , σ 2 ) to reweight the particles, from which the marginal likelihood Zm can be estimated. So the
intractable-likelihood regime needs only a simulator of the latents plus an evaluable observation
model, exactly what a mechanistic ODE/SDE provides — no transition density is ever computed.

Noisy voltage traces from the two hypotheses ( = 100 channels): the raw data on which the evidence is computed.
Thin = independent draws; bold = the noise-free mean. The sag is subtle relative to the channel noise.
N

Ih

(b) + (sag model)

V (mV)

(a) plain Na/K

Ih

hyperpol. step

40
20
0
−20
−40
−60
−80
−100

hyperpol. step

Ih

0

50

100

150
time (ms)

200

250

300

0

50

100

sag

150
time (ms)

200

250

300

Figure 26: Stochastic-latent NEURONBENCH: the raw data. Noisy voltage traces from the two competing
hypotheses under a moderate hyperpolarising-step protocol, at N =100 channels (thin: independent draws;
bold: the noise-free mean). (a) A plain Na/K cell. (b) The same cell plus a hyperpolarisation-activated Ih
current (the H-SAG model of Table 12), whose only signature is a small depolarising sag during the step (arrow).
Because that sag is comparable in size to the channel noise, the two hypotheses overlap and cannot be told apart
by eye — this is the data on which the evidence of Fig. 27 is computed.
Stochastic-latent HHbench: finite-N channel noise makes p(y ∣ m, θ) intractable, so MDA estimates it by simulation (particle filter), with a learned-summary synthetic likelihood as a cheap surrogate
(b) cheap surrogate: synthetic likelihood on a
learned sϕ tracks the particle filter

particle filter
naive deterministic

102

100
model-selection accuracy (\%)

log-evidence gap (true +Ih − plain)

(a) intractable likelihood: deterministic inverts,
particle filter is robust

101
100

0
−100

−101

wrong sign ⇒
confidently
wrong model

−102
−103

N=3000

N=1000
N=300
channel count (fewer → noisier)

N=100

90
80
70

per decision:
PF 3086 ms vs SL 0.3 ms

60

50 chanceparticle filter (gold)
40

synthetic lik., learned sϕ

N=1000

N=300
N=100
channel count (fewer → noisier)

N=50

Figure 27: Stochastic-latent NEURONBENCH: estimating the intractable likelihood by simulation. Both
panels score the Ih -vs-plain decision on the data of Fig. 26, sweeping the channel count N (fewer = noisier). (a)
The log-evidence gap log Z1 − log Z2 vs. N . A likelihood that ignores the process noise (a single deterministic
rollout + Gaussian observation, orange) degrades and, below N ≈1000, inverts — a negative gap means it
confidently selects the wrong mechanism. A bootstrap particle filter (blue), which estimates p(y | m, θ) by
propagating the latent gating SDE, stays robustly positive. (b) A synthetic likelihood on a learned summary sϕ
(green) reproduces the particle filter’s model-selection accuracy across the noise sweep at ∼104 × less compute
(∼0.3 ms vs. ∼3 s per decision). Bars/points are ±1 SE over independent noise realisations; see Section A.4
for sϕ .

Why the deterministic likelihood breaks. To illustrate why we cannot just use a deterministic
ODE model (and hence a deterministic likelihood, as we did in Eq. (3)), we consider a simple
example where we need to distinguish just two hypotheses: a plain Na/K cell vs the novel H-SAG
model Ih defined in Table 12. The noisy voltage traces from the two hypotheses are shown in Fig. 26
— the Ih sag is subtle relative to the channel noise, so they overlap. In Fig. 27(a) we plot the logevidence gap, log Z1 − log Z2 , vs noise level N , where Z1 is the evidence for the Ih hypothesis
and Z2 for the alternative Na/K hypothesis. We see that a likelihood that treats the intrinsic channel
noise as zero degrades as the noise grows and, at N =1000 channels, inverts: it confidently selects
the wrong mechanism. By contrast, the particle filter algorithm in Algorithm 4, which propagates
the latent gating SDE with Nz particles and weights each by the observation, stays robustly correct
at every noise level.
A learned-summary synthetic likelihood as a cheap surrogate. The particle filter is accurate
but costly (∼ 4 s per candidate model per experiment, Nz =600). A synthetic likelihood on a learned
summary statistic, as in Eq. (8), reproduces the particle filter’s decision ∼ 104 × less compute, as
shown in Fig. 27(b).

Figure 28: Three observation models on the stochastic six-world battery (fixed hypothesis space) (N =100
channels; correct-selection rate ±1 SE over 24 seeds; a dot marks an exact zero). The voltage particle filter
(blue) is the robust generalist — correct on five of six worlds and never inverting (its one weak world is the
SNR-limited NA-FATIGUE, at chance). The deterministic likelihood (orange) inverts on CA-REBOUND (wrong
on every one of the 24 seeds). The feature synthetic likelihood (green) stays above chance on every world and
edges the particle filter on the rate world NA-FATIGUE, but is weaker on the worlds whose discriminating signal
is a sub-threshold or timing shape (H-SAG, D-TYPE) that the summary vector compresses. On NA-FATIGUE
only the deterministic likelihood is clearly correct; however the deterministic likelihood catastrophically fails
(inverts) on CA-REBOUND.

Which observation model? In this section we consider a simplified version of the 6 stochastic
worlds where we only have two hypotheses (truth and a distractor). We use N =100 latent channels,
so the dynamics are fairly stochastic. We consider the deterministic likelihood (one noiseless rollout
+ Gaussian voltage noise), the bootstrap particle filter on the raw voltage, and a synthetic likelihood
on the feature vector s(y) of Eq. (30), estimated by simulation, as in Eq. (8). The results are shown
in Fig. 28. We see that the voltage particle filter is the robust generalist: correct on five of six worlds
and, crucially, it never inverts (its one weak world is the SNR-limited NA-FATIGUE, where it sits at
chance). The deterministic likelihood does more than degrade — on CA-REBOUND it confidently
inverts (wrong on every seed), reproducing the single-world failure of Fig. 27 in a fresh world:
treating each voltage sample as independent Gaussian evidence accumulates spike-timing jitter into
a large, wrong gap. The feature likelihood is complementary: it stays above chance on every world
and edges the particle filter on the spike-rate world NA-FATIGUE (where the raw-voltage PF is at
chance), but is weaker on the worlds whose discriminating signal is a sub-threshold or timing shape
(H-SAG, D-TYPE) that the summary vector compresses. There is thus no single best observation
model: shape signatures want the voltage filter, spike-rate signatures want the feature likelihood,
and neither escapes the overconfidence that sinks the deterministic one on CA-REBOUND — which
is what motivates holding both and auto-selecting (Fig. 29, below).
Auto-selecting the observation model. Because no single observation model wins on every world
(Fig. 28), the agent should hold both the feature synthetic likelihood and the voltage particle filter and
pick per world — and it can do so without knowing the truth. Before committing to an experiment
it runs a cheap probe: on the world’s discriminating protocol it simulates single experiments from
each candidate in turn and measures how often each observation model’s log-evidence gap identifies
the generator, averaged over which candidate generated the data. This is pure discrimination power
— which likelihood best tells the hypotheses apart, never peeking at the truth.
Formally this is the cost-aware observation-model selection of Eq. (11) (App. A), applied here over
o ∈ {PF, feat}: the agent estimates each MIo by the truth-free discrimination probe above and,
charging the PF its extra compute (cost(PF)/cost(feat) ≈ Nz /R ≫ 1), defaults to the cheap feature
likelihood and pays for the filter only where its discrimination clearly justifies it. Ignoring cost it
reduces to picking the more discriminating arm (Fig. 29).
Figure 29 shows the result at N =100: the probe correctly routes the burst world CA-REBOUND to
the particle filter (feature likelihood 0.49 → PF 1.00) and the rate world NA-FATIGUE to the feature
likelihood (0.82, where the voltage PF is below chance at 0.43), so the auto-selected arm attains the

Figure 29: An auto-selected observation model (N =100, six worlds, fixed hypothesis space; final posterior
of the true mechanism under repeat-aware VoI). The feature synthetic likelihood (green) and voltage particle
filter (blue) are complementary — the PF rescues CA-REBOUND’s burst while the feature likelihood keeps NA FATIGUE ’s spike-rate signature (where the PF is below chance). The agent auto-selects (black) by a truth-free
discrimination probe — which likelihood best separates the candidates on the discriminator, averaged over each
candidate generating the data (the letter marks the chosen model, PF or FEAT). It attains the better arm on five
of six worlds; on D-TYPE the single-shot probe favours the PF, which then underperforms the feature likelihood
under the budgeted design.

better of the two on five of six worlds. The exception is D-TYPE: the probe favours the PF (which
separates it well in a single shot, 0.92), but under the feature-MI-driven design the PF underperforms
at budget (0.50 vs. the feature likelihood’s 0.73) — the single-shot probe does not perfectly predict
the full-loop outcome. Even so, the observation model, like the experiment, becomes something the
agent chooses from data rather than a hand-set knob.
The learned summary and the spot-check in the open-world loop. The two-hypothesis study
above pits the particle filter against a fixed-feature synthetic likelihood. The released open-world
benchmark adds a third, still cheaper option — a synthetic likelihood on a learned summary sϕ
(a frozen 1d CNN, Section A.4) — so the cost-aware selection of Eq. (11) now ranges over o ∈
{PF, feat, sϕ }, guarded by the particle-filter spot-check of Section A. Running the full M-open
battery (six worlds, three seeds, the LLM proposing its own candidate channels at N =100), the costaware probe selects a cheap model on every run, and the spot-check overrides it to the PF wherever
the cheap posterior disagrees with the filter. Of the 18 runs the final observation model was the
learned sϕ on 2, the fixed feature likelihood on 5, and the particle filter on 11 — all 11 reached via a
spot-check disagreement. So the frozen sϕ is used only where it is verifiably sufficient (its posterior
matches the filter’s, e.g. H-SAG and D-TYPE), while the PF anchor catches the confusable cases. The
sharpest is CA-REBOUND: the cheap summaries confidently prefer a slow-Na+ run-down, but the
filter — and the T-type Ca current the LLM proposed — win, cutting its feature-forecast error from
4.5 (feature-only) to 0.85, with mean mechanism recovery 0.94 across the battery (19 LLM calls,
$0.55 total). Figure 30 visualises one such disagreement on D-TYPE.

### F.4 Data Efficiency Curves

The data efficiency curves from applying MDA and baseline LLM to NEURONBENCH STOCH are
shown in Fig. 31. Note only do we see that MDA is more sample efficient, but also that the ICL
forecasting approach is basically hopeless in this noisy setting (Bayes ∼0.15 vs. ICL ∼46 spikes2 ).
We also see that random designs are similar to (and arguably a tiny bit better than) VoI designs.

### F.5 Wiring the Repeat Count into the VoI Design Space

When the data is noisy, it is useful to be able to repeat experiments, to average the noise down. We
therefore enlarge the design to ξ = (protocol, r), where r is a repeat
√ count costing r units of budget:
averaging r repeated trials shrinks the spike-count noise ∼1/ r, so re-running the informative
protocol is itself a design lever the agent can pull.

Three observation models, three different answers — only the filter is right
posterior probability p(m ∣ )

1.0

★ truth

feature SL (cheap)
learned sϕ (cheap)
particle filter (safe, slow)

✓ D-K

✗ slow-Na

0.5
✗ T-Ca

0.0

Ih

plain
(Na+K)

T-type
Ca

D-type
K

M-type
K

slow
Na

spot-check: the cheap summaries (feat, sϕ) disagree with the particle filter ⇒ fall back to the safe (slow) PF

Figure 30: The particle-filter spot-check (D-TYPE, fixed archetype pool, N =100). The two cheap observation
models disagree with each other and with the particle filter: the fixed-feature synthetic likelihood picks T-type
Ca and the learned sϕ picks slow-Na+ , while only the assumption-free particle filter recovers the true D-type
K current (⋆). Because a selected cheap model’s MAP disagrees with a PF spot-check on the collected data, the
auto-select of Eq. (11) falls back to the safe — but ∼7× slower — filter. The truth-free discrimination probe
alone cannot catch this: it averages over generators, so a summary that confuses one pair while separating the
rest still scores well.

Figure 31: Stochastic-NEURONBENCH forecaster grid (N =100, six worlds, fixed hypothesis space, held-out
interventional-forecast MSE vs. the experiment budget Na ; log scale). The model-based Bayes-forecast (blue;
VoI-repeat solid, random design dashed) built on the design-loop posterior falls ∼15–20× from the Na =0
prior and sits more than two orders of magnitude below the in-context LLM forecaster (purple dotted). As on
the physics and deterministic-neuron rungs, the forecaster axis (model-based vs. LLM) matters more than the
acquisition axis (VoI vs. random). Bands are ±1 SE over worlds×seeds.

Expanded VoI.

The expanded VoI equation becomes
ξ

⋆

MI m; s̄r (y) | ξ
= arg max
,
ξ
cost(ξ)

(35)

Pr
where s̄r (y) = 1r t=1 s y (t) is the feature vector averaged over the r trials, and cost(ξ) = r
is the number of repeats. Here the per-trace summary s(y) is the six stochastic-battery features in
Eq. (30).
Concretely, let wm = p(m | D) be the current posterior over the candidate mechanisms. The
r-averaged features have
the (simulation-estimated) Gaussian synthetic likelihood p(s̄r | m, ξ) =
N s̄r | µm,ξ , 1r Σm,ξ , with µm,ξ , Σm,ξ read off R simulated traces per candidate, where Σ is

Figure 32: Full six-world × noise-ladder stochastic NEURONBENCH. Mean posterior probability of the true
mechanism over the six worlds vs. the channel count N (log axis; near-deterministic at left, noisiest at right),
for the three acquisition policies (budget 8, 12 seeds). All degrade gracefully with noise; repeat-aware VoI
(blue) leads across the whole ladder and its lead over each-once/random widens as N falls — re-running the
discriminator is the decisive lever exactly where the per-experiment signal is weakest. Bars are ±1 SE over
the six worlds. These aggregates are a mild lower bound: every world, including CA-REBOUND, is scored
under the single feature likelihood, whereas the auto-selected agent of Fig. 29 would route CA-REBOUND to
the voltage particle filter.

diagonal when using the summary vector in Eq. (7). (The 1r factor being the variance reduction from
averaging.) The information gain is the expected drop in the entropy of the model posterior,

MI m; s̄r | ξ = H(w) − Ep(s̄r |ξ) H q(· | s̄r ) ,

q(m | s̄r ) = P

wm p(s̄r | m, ξ)
, (36)
′
m′ wm′ p(s̄r | m , ξ)

P
with
P prior entropy H(w)1 = − m wm log wm and posterior-predictive feature mixture p(s̄r | ξ) =
m wm N s̄r | µm,ξ , r Σm,ξ . We evaluate Eq. (36) by Monte Carlo over that mixture: draw J

(j)
(j)
samples m(j) ∼ w, s̄r ∼ N µm(j) , 1r Σm(j) , form each model posterior q(· | s̄r ), and average the

(j)
per-sample gain H(w) − H q(· | s̄r ) over the J draws (J=200 here). Because averaging shrinks
the noise, VoI can now spend budget re-running the discriminator to beat the channel noise, rather
than being forced onto uninformative decoy protocols. This is the VoI objective of Eq. (5) with the
repeat count promoted to a first-class part of the design.
Results. As a proof of concept, we run the whole six-world battery (using a fixed set of hypotheses)
across the full channel-count ladder — from near-deterministic (N =3000) to strongly stochastic
(N =50) — using the synthetic factored Gaussian likelihood with the fixed summary features from
Eq. (30). In Fig. 32 we plot the mean posterior on the truth over the six worlds. All acquisition
policies degrade gracefully with noise, from certainty at N =3000 to 0.8–0.9 at N =50. Repeataware VoI leads at every rung, and — the key point — its margin widens as the noise grows: from
a tie at N ≥1000 to 0.91 vs. 0.80 over each-once/random at N =50. Spending budget on repeats is
exactly the lever that matters most when the per-experiment signal is weakest.

## G LLM Prompts

This appendix reproduces the prompts used by the three domains of this paper (physics, chemistry,
biology). Throughout, the LLM runs at temperature 0.2–0.4 with JSON-mode responses and every call is cached for reproducibility; the base model is stated per experiment (Opus 4.7 unless
noted, with the base-model robustness sweep of Section C.8 using Fable 5 and DeepSeek v4, and
the CHEMBENCH head-to-head using a matched proposer). MDA uses the LLM only to propose
structures and, in the baseline arms, to acquire experiments and forecast; inference, VoI design, and
fitting are exact Bayesian computations.

### G.1 FORCEBENCH (Force Laws, §4.1)

The physics rung invokes the LLM in four distinct roles, which fall into two groups: the proposer,
which is the only LLM call inside MDA’s discovery loop, and the verbaliser/judge, which are the
benchmark’s own explanation-scoring machinery and play no part in discovery, inference, or forecasting.

#### G.1.1 MDA Proposer (the Only LLM Call in the Discovery Loop)

The proposer sees the world context, the probe data collected so far, and a language specification that steers it toward field-equation Green’s functions rather than curve-fits; it returns candidate
force laws as JSON (parsed, compiled, and SMC-fit by MDA). Note that the language spec names
screened/power-law/oscillatory families (including the K1 Yukawa form) as examples, so the proposer is given the physical vocabulary — MDA’s contribution is the inference and VoI design that
identify which form the data support (see App. C, Fig. 14), not blind form-discovery. Its system
message and user template:
SYSTEM:
You are a physicist proposing candidate pairwise force laws to explain probe-orbit
,→ data. Reply JSON only.
USER (world context, then the observed data, then the language spec):
A test probe moves in an unknown central force sourced by a fixed body at the origin.
,→ The force MAY be static or MAY vary with time t (e.g. a time-modulated coupling).
,→ Each experiment launches the probe from a position with a velocity, and sets two
,→ knobs p1, p2. <one sentence naming the two experiment knobs p1, p2 for this world
,→ -- e.g. p1 the source coupling, p2 the probe inertia> F_mag is the pairwise force
,→ magnitude between the probe (charge qi) and source (charge qj) at separation r
,→ and time t.
Observed data:
<measurement times and the radius r(t) of each probe run so far>
Propose N distinct plausible force laws (or refinements of those tried).
Propose each force law as the field / Green's-function response of a PHYSICAL FIELD
,→ EQUATION (e.g. 2D Laplacian/Poisson -> 1/r; screened Poisson / Helmholtz -> a
,→ screened form such as exp(-r/lam)/r or K1(r/lam)/lam; fractional Laplacian -> a
,→ power law 1/rˆp; 3D inverse-square -> 1/rˆ2), NOT an arbitrary curve-fit with
,→ softening/offset terms. If the data show the force changing sign or magnitude
,→ over time (not just with r), the coupling itself may be time-dependent (e.g. a
,→ cos(w*t+phi) modulation) -- consider such forms too. State the governing operator
,→ in the rationale. Express each F_mag as a Python expression in the symbols r, qi,
,→ qj, t and your OWN named free parameters ONLY. The source coupling is carried by
,→ qj (the probe is qi); do NOT reference p1 or p2 in the expression -- introduce
,→ named parameters (e.g. k, G, lam, s) for coupling constants and length scales.
,→ Allowed functions: exp, log, sqrt, sin, cos, tanh, k0, k1, gamma, pi, np. Return
,→ JSON {"hypotheses": [{"name": str, "fmag": str, "operator": str, "params":
,→ [{"name": str, "low": float, "high": float}], "rationale": str}]}.

For the extension worlds (App. C) only the proposer context changes — the declared background
field (ether/Hubble), the self-interacting cloud (circle), or the known-law hidden sources (dark matter); the language spec is unchanged:
ETHER / HUBBLE (central force + declared background):
Here the probe is a neutral test particle (qi=1) orbiting a fixed central anchor that
,→ sources the field (coupling carried by a named parameter); its inertia is 1.

Test probes orbit an unknown CENTRAL force sourced by a fixed anchor at the origin (a
,→ 2D field-equation response, e.g. a Laplacian giving F ˜ 1/r). <probe roles>
,→ LAYERED ON TOP there is a uniform, mass-independent background acceleration of
,→ magnitude alpha in the +y direction (a constant 'ether' drift), on top of the
,→ central force. That background is handled separately by the fitter -- you only
,→ need to propose the CENTRAL pairwise force magnitude F_mag(r, qi, qj, t) sourced
,→ by the anchor. F_mag is the magnitude of the attractive central force on the
,→ probe at separation r from the anchor.
---------------------------------------CIRCLE (self-interacting N-body):
Eleven identical particles -- one at the centre and ten equally spaced on a ring -,→ ALL interact with each other through the SAME pairwise central force (uniform
,→ coupling): every particle both sources the field and feels it. Each experiment
,→ sets the ring radius and a tangential launch velocity. Propose the pairwise force
,→ magnitude F_mag(r, qi, qj, t) between any two particles at separation r (with
,→ qi=qj=1, the uniform coupling); it is attractive and depends only on r for a
,→ static field. The many-body motion is the sum of these pairwise forces.
---------------------------------------DARK MATTER (known law, latent hidden sources):
Test probes move in a KNOWN static 2D-Laplacian field (each source contributes F =
,→ q/(2*pi*r), attractive), sourced by 20 VISIBLE particles of coupling 1 whose
,→ positions are known, PLUS an unknown number of HIDDEN sources that reveal
,→ themselves only through the probes' deflection toward seemingly empty regions.
,→ The task is to infer how many hidden sources exist and their positions and
,→ couplings.
(three species uses no LLM proposer -- the couplings are inferred by a linear solve;
,→ the LLM only verbalizes the recovered species, via the verbaliser above.)

#### G.1.2 Verbaliser and Judge (Benchmark Explanation Scoring; Not Used for Discovery)

These two roles exist only to compute the benchmark’s explanation metric: the verbaliser turns
MDA’s already-selected law into a short prose explanation, which the benchmark’s own judge scores
against the world’s optimal explanation and rubric (temperature 0, integer 0–10). MDA’s posterior,
VoI design, and held-out forecasts never call either.
SYSTEM:
You are a physicist. Reply with a 2-4 sentence explanation only.
USER:
<world context>
A Bayesian model-discovery method fit the data and selected the force law F_mag =
,→ <the fitted F_mag expression> with FITTED parameters {'<parameter names>':
,→ np.float64(0.0)}. Explain the physics of THIS law, and be specific and complete:
,→ (1) name the governing field equation / operator; (2) state its temporal
,→ character (static vs time-evolving); (3) give the NUMERIC value of any length- or
,→ scale-parameter you fitted (e.g. a screening length) and say how the force
,→ behaves at short vs long range; (4) explicitly state the physical roles of the
,→ knobs p1 and p2 as described above.
SYSTEM:
You are an expert physicist grading how well a student's prose description of a
,→ simulated physical system matches the ground-truth description. You are precise,
,→ fair, and reward semantic correctness over surface phrasing -- paraphrases and
,→ equivalent formulations (e.g. 'inverse-square-like' ˜= 'gradˆ2phi' in 2D) should
,→ receive credit, but missing or wrong physical content should not.
USER TEMPLATE:
Compare the student's description against the ground-truth description of the
,→ physical system.
<ground_truth>
{ground_truth}
</ground_truth>
<student>
{student}
</student>
Score the student description on a 0-10 integer scale based on how well it captures:

1. The correct field equation / governing operator (e.g. Laplacian, fractional
,→ Laplacian, Helmholtz, diffusion, wave).
2. The temporal character (static vs. time-evolving; instantaneous vs. retarded).
3. The force law / coupling structure (how particles couple to the field, including
,→ p1/p2 roles).
4. Any structural features unique to this world: hidden species and their relative
,→ coupling strengths and signs, neutral probes, hidden/dark sources, screening
,→ lengths, etc.
Use the world-specific rubric below to calibrate the bands. A 10/10 represents the
,→ best explanation achievable given the experimental capabilities -- reward
,→ semantically-equivalent phrasings and numeric estimates within the tolerance
,→ specified by the rubric.
<scoring_rubric>
{rubric}
</scoring_rubric>
Respond with 1-3 sentences of justification, then your final integer score inside
,→ <score>...</score> tags. Example: "<score>7</score>".

#### G.1.3 Baseline Forecasters

(The Na =0 and LLM-forecast arms of Fig. 2.) The zero-shot baseline reuses the proposer’s system prompt and world context but appends, in place of any data, the instruction: “No experimental
budget is available: you cannot run any experiments or fits. Based ONLY on physical reasoning about the setup described above, submit your single best-guess law now” (a <final_law>
discovered law(...) plus an <explanation>). The LLM-forecast baseline is the same,
but with the collected experiments’ launch configurations and observed radii r(t) listed before the
submission instruction — so the LLM authors a law from the data in context (rather than MDA templating one from its posterior), scored by the benchmark’s own executor exactly as MDA’s Bayesforecast is.

### G.2 CHEMBENCH (Enzyme Rate Laws, §4.2)

As in physics, the only LLM call inside MDA’s discovery loop is the proposer. It sees an enzymekinetics mechanism grammar, the experiments collected so far (design inputs → observed initial rate
r0 ), and — when refining an existing pool — the forms already tried together with their residuals (so
it does not re-propose dead ends, and knows which input a residual correlates with, e.g. a residual
growing with temperature suggests an Arrhenius factor) plus the remaining budget and phase. It
returns candidate rate laws as JSON, which MDA compiles and SMC-fits; inference, VoI design,
and fitting are exact Bayesian computations. The grammar names the standard families (Michaelis–
Menten, Hill, competitive/uncompetitive/noncompetitive inhibition, product inhibition, Arrhenius
temperature, ping-pong) as the physical vocabulary, so — exactly as in physics — MDA’s contribution is identifying which multiplicative composition the data support, not blind symbol search. The
residual-directed context engineering (negative evidence + budget/phase) follows LLM-AutoSciLab
(Kabra et al., 2026). System message and user template:
SYSTEM:
You are an enzyme kineticist proposing candidate rate laws to explain assay data.
,→ Reply JSON only.
USER (world context + mechanism grammar, then the observed data, then -- only when
,→ refining -- residual-directed negative evidence and the remaining budget/phase,
,→ then the language spec):
An enzyme catalyses a reaction with initial rate r0 [mM/min]. Controllable inputs:
,→ C_A [substrate, mM], C_I [inhibitor, mM], C_B [2nd substrate, mM], C_P [product,
,→ mM], Enz [enzyme, mg/mL], T [K], pH. Discover r0 = f(C_A,C_I,C_B,C_P,Enz,T,pH;
,→ theta).
Mechanism families to consider (identify which are active FROM THE DATA):
Substrate C_A: linear | Michaelis-Menten C_A/(Km+C_A) | Hill C_A**n/(Kh**n+C_A**n) |
,→ substrate inhibition C_A/(Km+C_A+C_A**2/Ki)
Inhibitor C_I: none | competitive (raises apparent Km) | uncompetitive (lowers
,→ Vmax) | noncompetitive (lowers Vmax at all C_A)
Product C_P: none | product inhibition (like competitive but in C_P)
Temperature T: none | Arrhenius exp(-Ea/8.314*(1/T-1/310))
Second substrate C_B: none | ping-pong C_A*C_B/(KmA*C_B+KmB*C_A+C_A*C_B)
Enzyme Enz: rate is proportional to Enz (Vmax = kcat*Enz).
Compose factors multiplicatively when several mechanisms act together.

Experiments (inputs -> r0):
<one line per collected experiment: C_A=.., C_I=.., C_B=.., C_P=.., Enz=.., T=..,
,→ pH=.. -> r0=..>
[when refining an existing pool -- residual-directed negative evidence:]
Forms ALREADY TRIED (in the pool) and their residuals -- do NOT re-propose any of
,→ these; propose forms STRUCTURALLY DIFFERENT from all of them:
<per-form median relative residual; and, for the current best form, which input its
,→ residual correlates with -- e.g. residual grows with T -> add Arrhenius; with
,→ C_I -> add an inhibitor term>
Refine by proposing a DIFFERENT mechanism combination (add/remove an inhibition,
,→ Hill, Arrhenius, or ping-pong factor) -- do NOT patch with ad-hoc
,→ offset/softening terms.
[budget/phase status, when set:]
Experiment budget remaining: <B>. Current phase: <explore|refine> (explore =
,→ restructure the mechanism; refine = tune an adequate form).
Propose N distinct plausible rate laws (or refinements of those tried).
Each 'expr' is a Python expression in the 7 input names + your declared params, using
,→ only + - * / ** and exp, log, sqrt. Give physically plausible positive param
,→ bounds. JSON schema: {"hypotheses":[{"name":str,"expr":str,"params":[{"name":str ⌋
,→ ,"low":float,"high":float}]}]}

The head-to-head baseline (Section D) is the LLM-AUTOSCILAB agent’s own LLM+activelearning+symbolic-regression loop (Kabra et al., 2026), run under matched settings (the same LLM,
budget, noise, and universal grammar); its prompts are those of that system and are not reproduced
here.

### G.3 Electrophysiology (Ion Channels, §4.3)

We group the NEURONBENCH prompts by their role. The model-proposal prompt is the only LLM
call inside MDA’s discovery loop: MDA uses the LLM to propose candidate mechanisms, then fits
and selects them by exact SMC and designs experiments by numerical VoI — so this is the prompt
MDA’s results depend on. The baseline prompts (experiment design and forecasting) are used only
by the LLM baseline arms MDA is compared against, never by MDA itself. All are zero-reference:
the LLM is told only to model the cell as a conductance-based neuron and infer its channels from
the data — never the candidate models, the posterior, or the true mechanism.
What the LLM sees as “data”. An experiment yields a membrane-voltage trace V (t), but every
LLM prompt is shown only its reduction to the test-window spike count — one line per protocol
run, formatted verbatim as:
Experiments run so far and observed spike counts:
- long step (10 uA, 300 ms)
- paired long pulses (12/300, 60 gap, 12/300)
- hyperpol step then release (-30/250 -> rebound)

-> 21 spikes
-> 16 spikes
-> 4 spikes

The raw trace V (t) is never sent to any LLM. It is available only to MDA’s numerical observation
model (Section F.3), which chooses whether to reduce it to a spike count or score it directly with a
particle filter — the reduction-vs-model choice is the solver’s, not the benchmark’s.

#### G.3.1 MDA Model Proposer (the Only LLM Call in MDA’s Loop)

In the released open-world benchmark the proposer returns its own parameterised channel hypotheses (reversal potential, activation direction, inactivation, and conductance / half-activation / timeconstant bounds), so the hypothesis space is genuinely open:
System: You are an electrophysiologist proposing candidate ion-channel mechanisms to explain
current-clamp spike-count data. Reply with a JSON object only.
User:
A neuron is recorded in current clamp and fires action potentials under injected current.
Model it as a single-compartment conductance-based (Hodgkin-Huxley) neuron with voltage-gated
channels. From the spike-count data, propose candidate membrane currents (beyond the standard
Na+/K+ spiking currents) that could explain its responses. Each is described by:
reversal_mV : reversal potential (˜+50 Na-like, ˜+120 Ca-like, ˜-80 K-like, ˜-30 mixed)
opens_on
: 'depol' or 'hyperpol'
inactivates : true if transient / de-inactivated by a hyperpolarising pre-pulse
bounds for conductance g, half-activation voltage (mV), and activation time constant (ms).
<collected protocol -> spike-count data>
Propose N distinct plausible mechanisms (or an empty list if the data look like a plain spiker).

JSON schema: {"hypotheses":[{"name","reversal_mV","opens_on","inactivates",
"g_bounds","half_mV_bounds","tau_ms_bounds"}]}

The H-SAG deep-dive example (Fig. 23) instead asks for candidate channel compositions from a
channel menu, given a one-line phenotype description:
A neuron recorded in current clamp rests near -65 mV and fires overshooting action
potentials to a supra-threshold current step. Model it as a single-compartment
conductance model with voltage-gated channels from {Na (fast, TTX-sensitive), K
(delayed rectifier), Ca (high-threshold), leak}. Propose 4-5 DISTINCT candidate
channel COMPOSITIONS that could underlie the spiking (plus at least one non-spiking
null), each a list from {Na,K,Ca,L}. Return exactly {"compositions": [{"name": "...",
"channels": ["Na","K","L"]}, ...]}.

#### G.3.2 LLM Baselines: Experiment Design and Forecasting (Not Used by MDA)

As an experiment proposer (the LLM-acquisition baseline) the LLM chooses the next protocol from
the collected data alone:
System: You are an electrophysiologist choosing the next experiment. Reply with ONLY a JSON object.
User:
A neuron is recorded in current clamp; we count its action potentials per protocol. Model it
as a single-compartment conductance-based (Hodgkin-Huxley) neuron with voltage-gated channels
(Na, K, Ca, leak, and possibly others), and infer its mechanism from the data.
Experiments run so far and observed spike counts:
- <protocol> -> <count> spikes ...
Available experiments (choose one; each may be run once):
- <protocol label> ...
Which ONE experiment best reveals the neuron's mechanism next?
Return exactly {"experiment": "<one label copied verbatim>"}.

As the ICL-forecaster (the in-context-learning baseline) it predicts the held-out spike counts:
System: You are an electrophysiologist forecasting a neuron's response. Reply with ONLY a JSON object.
User:
A neuron is recorded in current clamp; we count its action potentials (spikes) per protocol.
Model it as a single-compartment conductance-based (Hodgkin-Huxley) neuron with voltage-gated
channels (Na, K, Ca, leak, and possibly others).
Experiments run and observed spike counts:
- <protocol> -> <count> spikes ...
Predict the spike count for each held-out protocol:
1. <protocol> ...
Return exactly {"counts": [n1, ...]} with one integer per protocol, in order.

The Na =0 (zero-shot) neuron point is this forecaster with an empty “experiments run” list. These
prompt templates mirror the code (scripts/ephys/hh worlds run.py and the released
neuronbench), so the documented prompt is the one that is run.

## References

Nikhil Abhyankar, Sha Li, Sanchit Kabra, Naren Ramakrishnan, Yulia Gel, and Chandan K. Reddy.
LLM-ACES: Closed-loop discovery of dynamical systems with LLM-guided adaptive search.
arXiv preprint arXiv:2606.25039, 2026.
Eser Aygün, Anastasiya Belyaeva, Gheorghe Comanici, Marc Coram, Hao Cui, Jake Garrison, Renee Johnston, Anton Kast, Cory Y McLean, Peter Norgaard, Zahra Shamsi, David Smalling,
James Thompson, Subhashini Venugopalan, Brian P Williams, Chujun He, Sarah Martinson,
Martyna Plomecka, Lai Wei, Yuchen Zhou, Qian-Ze Zhu, Matthew Abraham, Erica Brand, Anna
Bulanova, Jeffrey A Cardille, Chris Co, Scott Ellsworth, Grace Joseph, Malcolm Kane, Ryan
Krueger, Johan Kartiwa, Dan Liebling, Jan-Matthis Lueckmann, Paul Raccuglia, Xuefei Julie
Wang, Katherine Chou, James Manyika, Yossi Matias, John C Platt, Lizzie Dorfman, Shibl
Mourad, and Michael P Brenner. An AI system to help scientists write expert-level empirical
software. Nature, pp. 1–3, May 2026. URL https://arxiv.org/abs/2509.06503.
Jürgen Bajorath. From scientific theory to duality of predictive artificial intelligence models. Cell
Rep. Phys. Sci., 6(4):102516, April 2025. URL https://www.sciencedirect.com/
science/article/pii/S2666386425001158.
Taiyu Ban, Lyuzhou Chen, Derui Lyu, Xiangyu Wang, Qinrui Zhu, Qiang Tu, and Huanhuan Chen.
Integrating large language model for improved causal discovery. IEEE Transactions on Artificial
Intelligence, 2025. URL https://arxiv.org/abs/2306.16902. Earlier version titled
“From Query Tools to Causal Architects: Harnessing Large Language Models for Advanced
Causal Discovery from Data”, arXiv:2306.16902v1.
Elias Bareinboim, Juan D Correa, Duligur Ibeling, and Thomas Icard. On pearl’s hierarchy and
the foundations of causal inference. In Probabilistic and Causal Inference: The Works of Judea
Pearl, volume 36, pp. 507–556. Association for Computing Machinery, New York, NY, USA, 1
edition, March 2022. URL https://causalai.net/r60.pdf.
Sander Beckers and Joseph Y. Halpern. Abstracting causal models. In Proceedings of the AAAI
Conference on Artificial Intelligence (AAAI-19), volume 33, pp. 2678–2685, 2019. doi: 10.1609/
aaai.v33i01.33012678.
José M. Bernardo and Adrian F. M. Smith. Bayesian Theory. Wiley, 1994.
G E P Box and W J Hill. Discrimination among mechanistic models. Technometrics, 9(1):57,
February 1967. URL https://www.jstor.org/stable/10.2307/1266318.
Markus J Buehler. Why we must break the world. ChemRxiv, May 2026.
//chemrxiv.org/doi/pdf/10.26434/chemrxiv.15001674/v2.

URL https:

Kathryn Chaloner and Isabella Verdinelli. Bayesian experimental design: A review. Statistical
Science, 10(3):273–304, 1995.
Yanzhi Chen, Dinghuai Zhang, Michael U. Gutmann, Aaron Courville, and Zhanxing Zhu. Neural
approximate sufficient statistics for implicit models. In International Conference on Learning
Representations (ICLR), 2021.
Nicolas Chopin and Omiros Papaspiliopoulos. An Introduction to Sequential Monte Carlo. Springer,
1 edition, October 2020. URL https://nchopin.github.io/books.html.
Kyle Cranmer, Johann Brehmer, and Gilles Louppe. The frontier of simulation-based inference.
Proceedings of the National Academy of Sciences, 117(48):30055–30062, 2020.
A Philip Dawid.
Statistical causality from a Decision-Theoretic perspective.
Annu.
Rev. Stat. Appl., 2(1):273–303, 2015.
URL https://doi.org/10.1146/
annurev-statistics-010814-020105.
P. Dawid. Causal inference without counterfactuals. JASA, 95:407–448, 2000.

Michael Deistler, Jan Boelts, Peter Steinbach, Guy Moss, Thomas Moreau, Manuel Gloeckler, Pedro
L C Rodrigues, Julia Linhart, Janne K Lappalainen, Benjamin Kurt Miller, Pedro J Gonçalves,
Jan-Matthis Lueckmann, Cornelius Schröder, and Jakob H Macke. Simulation-based inference:
A practical guide. arXiv [stat.ML], August 2025. URL http://dx.doi.org/10.48550/
arXiv.2508.12939.
Noémi Elteto, Nathaniel D Daw, Kimberly L Stachenfeld, and Kevin J Miller. ATLAS: Active
theory learning for automated science. arXiv [cs.LG], June 2026. URL http://dx.doi.
org/10.48550/arXiv.2606.12386.
Paul Fearnhead and Dennis Prangle. Constructing summary statistics for approximate Bayesian
computation: semi-automatic approximate Bayesian computation. Journal of the Royal Statistical
Society: Series B, 74(3):419–474, 2012.
Adam Foster, Desi R. Ivanova, Ilyas Malik, and Tom Rainforth. Deep adaptive design: Amortizing
sequential Bayesian experimental design. In Proceedings of the 38th International Conference on
Machine Learning (ICML), volume 139 of PMLR, pp. 3384–3395, 2021. arXiv:2103.02438.
Ronald F. Fox and Yan-nan Lu. Emergent collective behavior in large numbers of globally coupled
independently stochastic ion channels. Physical Review E, 49(4):3421–3431, 1994.
Joshua H. Goldwyn and Eric Shea-Brown. The what and where of adding channel noise to the
hodgkin-huxley equations. PLoS Computational Biology, 7(11):e1002247, 2011.
Rushil Gupta, Jason Hartford, and Bang Liu. LLMs for experiment design in scientific domains:
Are we there yet? In ICML 2025 Generative AI and Biology (GenBio) Workshop, July 2025.
URL https://openreview.net/forum?id=dIEeOwrmOe.
Maurice Halstead. Halstead complexity metric, 1977. URL https://en.wikipedia.org/
wiki/Halstead_complexity_measures.
Nikolaus Hansen. The CMA evolution strategy: A tutorial. arXiv preprint arXiv:1604.00772, 2016.
Akshay K Jagadish, Younes Strittmatter, Nori Jacoby, George Kachergis, Eric Schulz, Nathaniel
Daw, Suyog H Chandramouli, and Thomas L Griffiths. Closing the loop to discover psychological
theories with an automated cognitive scientist. arXiv [q-bio.NC], June 2026. URL http://dx.
doi.org/10.48550/ARXIV.2606.26448.
Bai Jiang, Tung-Yu Wu, Charles Zheng, and Wing H. Wong. Learning summary statistic for approximate Bayesian computation via deep neural network. Statistica Sinica, 27:1595–1618, 2017.
Sanchit Kabra, Nikhil Abhyankar, Saaketh Desai, Prasad Iyer, and Chandan K. Reddy.
Llm-autoscilab: Closed-loop scientific discovery via active experimentation with llms.
arXiv:2605.24043, 2026.
Daniel Kasenberg, Pablo Samuel Castro, Maria K Eckstein, Nóemi Éltető, Will Dabney, Caroline
Wang, Martin Engelcke, Rishika Mohanta, Aparna Dev, Matthew M Botvinick, Nenad Tomasev,
Glenn C Turner, Vincent Costa, Nathaniel D Daw, Kimberly L Stachenfeld, and Kevin J Miller.
AI-discovered cognitive models reveal novel insights into human and animal learning. bioRxiv,
pp. 2026.05.18.725921, May 2026. URL https://www.biorxiv.org/content/10.
64898/2026.05.18.725921v1.abstract.
Riko Kelter. Bayesian model selection in the M-open setting — approximate posterior inference and
subsampling for efficient large-scale leave-one-out cross-validation via the difference estimator.
arXiv preprint arXiv:2005.13199, 2020.
Emre Kıcıman, Robert Ness, Amit Sharma, and Chenhao Tan. Causal reasoning and large language
models: Opening a new frontier for causality. Transactions on Machine Learning Research, 2024.
ISSN 2835-8856. URL https://openreview.net/forum?id=mqoxLkX210. Featured
Certification. Preprint: arXiv:2305.00050.

Stefan Kramer, Mattia Cerrato, Jannis Brugger, Sašo Džeroski, and Ross D King. Automated scientific discovery: From equation discovery to autonomous discovery systems. Mach. Learn.,
115(5):109, May 2026. URL https://link.springer.com/article/10.1007/
s10994-025-06955-2.
Mario Krenn, Robert Pollice, Si Yue Guo, Matteo Aldeghi, Alba Cervera-Lierta, Pascal Friederich,
Gabriel Dos Passos Gomes, Florian Häse, Adrian Jinich, Akshatkumar Nigam, Zhenpeng Yao,
and Alán Aspuru-Guzik. On scientific understanding with artificial intelligence. Nat. Rev. Phys.,
4(12):761–769, October 2022. URL https://pmc.ncbi.nlm.nih.gov/articles/
PMC9552145/.
Jaeho Lee, Nick Merrill, and Ezra Karger. ForecastBench-Sim: A simulated-world forecasting
benchmark. arXiv preprint arXiv:2606.18686, 2026. URL https://arxiv.org/abs/
2606.18686. Spotlight, ICML 2026 Workshop on AI Forecasting.
D. V. Lindley. On a measure of the information provided by an experiment. The Annals of Mathematical Statistics, 27(4):986–1005, 1956. doi: 10.1214/aoms/1177728069.
D MacKay.
Bayesian model comparison and backprop nets.
In NIPS, pp. 839–846,
December 1991. URL https://proceedings.neurips.cc/paper/1991/file/
c3c59e5f8b3e9753913f4d435b53c308-Paper.pdf.
Warren S. McCulloch and Walter Pitts. A logical calculus of the ideas immanent in nervous activity.
The Bulletin of Mathematical Biophysics, 5(4):115–133, 1943.
Lisa Messeri and M J Crockett. Artificial intelligence and illusions of understanding in scientific research. Nature, 627(8002):49–58, March 2024. URL https://www.nature.com/
articles/s41586-024-07146-0.
Christian A Naesseth, Fredrik Lindsten, and Thomas B Schön. Elements of sequential monte carlo.
Foundations and Trends in Machine Learning, 2019. URL http://arxiv.org/abs/1903.
04797.
Judea Pearl. Causality: Models, Reasoning, and Inference. Cambridge University Press, 2nd edition,
2009.
Wasu Top Piriyakulkij, Cassidy Langenfeld, Tuan Anh Le, and Kevin Ellis. Doing experiments
and revising rules with natural language and probabilistic reasoning. In Advances in Neural
Information Processing Systems (NeurIPS), 2024.
Ben Prystawski, Kushin Mukherjee, Daniel Wurgaft, Linas Nasvytis, Michael Y Li, Noah D Goodman, and Michael C Frank. auto-psych: Automating the science of mind using agent-driven theory discovery and experimentation. arXiv [cs.AI], June 2026. URL http://dx.doi.org/
10.48550/ARXIV.2606.26460.
Stefan T. Radev, Ulf K. Mertens, Andreas Voss, Lynton Ardizzone, and Ullrich Köthe. BayesFlow:
Learning complex stochastic models with invertible neural networks. IEEE Transactions on Neural Networks and Learning Systems, 33(4):1452–1466, 2022.
Tom Rainforth, Adam Foster, Desi R. Ivanova, and Freddie Bickford Smith. Modern Bayesian
experimental design. Statistical Science, 39(1), 2024.
Jonathan Richens and Tom Everitt. Robust agents learn causal world models. In International
Conference on Learning Representations (ICLR), 2024. URL https://openreview.net/
forum?id=pOoKI3ouv1. Oral; honorable mention outstanding paper. arXiv:2402.10877.
Bernardino Romera-Paredes, Mohammadamin Barekatain, Alexander Novikov, Matej Balog,
M. Pawan Kumar, Emilien Dupont, Francisco J. R. Ruiz, Jordan S. Ellenberg, Pengming Wang,
Omar Fawzi, Pushmeet Kohli, and Alhussein Fawzi. Mathematical discoveries from program
search with large language models. Nature, 625:468–475, 2024.

Paul K. Rubenstein, Sebastian Weichwald, Stephan Bongers, Joris M. Mooij, Dominik Janzing,
Moritz Grosse-Wentrup, and Bernhard Schölkopf. Causal consistency of structural equation models. In Proceedings of the 33rd Conference on Uncertainty in Artificial Intelligence (UAI). AUAI
Press, 2017. arXiv:1707.00819.
Wesley C Salmon.
Scientific explanation and the causal structure of the
world.
Princeton University Press, Princeton, NJ, December 1984.
URL
https://press.princeton.edu/books/paperback/9780691101705/
scientific-explanation-and-the-causal-structure-of-the-world.
Matthew Self and Peter Cheeseman. Bayesian prediction for artificial intelligence. In Proc. UAI,
1987. URL http://dx.doi.org/10.48550/arXiv.1304.2717.
Thomas Serre and Ellie Pavlick. From prediction to understanding: Will AI foundation models
transform brain science? Neuron, 2025. URL http://dx.doi.org/10.48550/arXiv.
2509.17280.
Silviu-Marian Udrescu and Max Tegmark. AI feynman: A physics-inspired method for symbolic
regression. Science Advances, 6(16):eaay2631, 2020.
Stefan Wahl, Raphaela Schenk, Ali Farnoud, Jakob H. Macke, and Daniel Gedon. A probabilistic framework for LLM-based model discovery. arXiv preprint arXiv:2602.18266, 2026. URL
https://arxiv.org/abs/2602.18266. Introduces ModelSMC.
Matt L. Wiemann, Lindsay M. Smith, Peter Melchior, Siddharth Mishra-Sharma, Andrew Gordon
Wilson, Pavel Izmailov, and Carolina Cuesta-Lázaro. DiscoverPhysics: Benchmarking LLMs for
out-of-the-box scientific thinking. arXiv preprint arXiv:2605.26087, 2026.
Simon N. Wood. Statistical inference for noisy nonlinear ecological dynamic systems. Nature, 466
(7310):1102–1104, 2010.
Hanbo Xie and Robert C Wilson. Successful automatic model discovery can produce false mechanisms. PsyArXiv, July 2026. URL https://osf.io/preprints/psyarxiv/r46ux_
v1.
Tom Zahavy. Position: LLMs can’t jump. In ICML, 2026. URL https://openreview.net/
forum?id=klU4737opt.
Tianshi Zheng, Kelvin Kiu-Wai Tam, Newt Hue-Nam K. Nguyen, Baixuan Xu, Zhaowei Wang,
Jiayang Cheng, Hong Ting Tsang, Weiqi Wang, Jiaxin Bai, Tianqing Fang, Yangqiu Song,
Ginny Y. Wong, and Simon See. NewtonBench: Benchmarking generalizable scientific law discovery in LLM agents. In International Conference on Learning Representations (ICLR), 2026.
arXiv:2510.07172.

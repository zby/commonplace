---
source: https://arxiv.org/html/2608.07885v1
description: "Passive skill distillation turns recurring cross-episode procedures into compact prompts that recover much of the reasoning-mode performance gap at lower token cost"
captured: 2026-08-18
capture: web-fetch
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Reason Wide, Not Deep: Amortizing the Reasoning Premium into Distilled Skills

Author: Agamdeep Singh, Srishti Gautam, Priyanshu Gupta, Nikita Mehrotra, Tanmay Bakshi, and Sumit Gulwani (Microsoft)
Source: https://arxiv.org/html/2608.07885v1
Date: 2026-08-08

## Abstract

Reasoning modes of language models outperform their non-reasoning counterparts on
multi-step agentic tasks, but pay a 3–6$\times$ premium in output tokens on *every* episode
— much of it spent re-deriving procedures that are shared across episodes of the same
domain. We show this recurring cost can be *amortized*: a coding agent analyses a small
corpus of existing trajectories from a training split and compiles a compact
natural-language *skill* that is injected into the non-reasoning model’s system prompt.
Across four agentic benchmarks (ALFWorld, $\tau^{2}$-bench telecom and retail, and
SpreadsheetBench-Verified), skills recover 55%–100%+ of the reasoning gap for GPT-5.4-mini
on held-out tasks — exceeding the reasoning mode outright on two of four — while emitting
2.7–6$\times$ fewer output tokens and zero reasoning tokens. Notably, reasoning traces are
not a prerequisite: skills distilled from non-reasoning trajectories alone remain
competitive with skills distilled from paired reasoning/non-reasoning corpora, with
domain-dependent differences between the two sources. We interpret these results through a
search lens: test-time reasoning is *deep* search inside a single episode, re-paid at every
deployment, while corpus distillation is *wide* search across episodes, paid once. The two
recover overlapping procedural knowledge, and width over cheap trajectories is often the
better buy — with the residual gap on some domains (telecom, SpreadsheetBench) delineating
where genuinely per-instance deep search remains necessary.

## 1 Introduction
Figure 1: **Skills break the accuracy–token frontier.** Held-out success rate vs. mean
output tokens per episode for GPT-5.4-mini on four agentic benchmarks. The gray line is the
baseline Pareto frontier traced by toggling the reasoning mode (think $\leftrightarrow$
no-think); arrows mark the lift from injecting a distilled skill into the no-think model.
On every benchmark the skill lands above the frontier.

Test-time reasoning has become the default recipe for hard tasks: models trained to emit
long chains of thought before acting (10; 5; 12) outperform their non-reasoning
counterparts on mathematics, coding, and, increasingly, multi-step *agentic* tasks in which
the model interleaves tool calls, environment observations, and user turns (22; 14; 21; 3).
The improvement is real but so is the bill. In our experiments, enabling the reasoning mode
of GPT-5.4-mini multiplies per-episode output tokens by 3.0–5.1$\times$ across four agentic
benchmarks (up to 6.2$\times$ for Qwen3.6-27B), and this premium is paid again on every
single episode, forever, because reasoning tokens are generated afresh each time.

Reading the reasoning traces reveals why this is wasteful. Within a fixed domain, much of
the deliberation is not instance-specific problem solving but the re-derivation of
*episode-invariant procedure*: the retail support agent reasons its way (again) to “I
should not call the account-lookup tool until the customer has actually provided an email”;
the household agent re-discovers (again) that “heat X” is an atomic command rather than a
sequence of microwave-door operations. Non-reasoning rollouts of the same model fail
precisely where this procedural knowledge is missing — in the retail domain, a single
recurring bug (calling an authentication tool with a fabricated argument) appears in 59% of
non-reasoning training rollouts and accounts for 94% of observed tool errors. Recurrent
computation is exactly what amortization is for. We ask: **how much of the reasoning
premium can be paid once, offline, instead of on every episode?**

Our method, *passive skill distillation*, is deliberately simple: collect a small corpus of
trajectories (35–50 tasks) from a training split, hand the corpus to an off-the-shelf
coding agent (2), and ask it to compile a compact natural-language *skill* — 40–130 lines
of markdown encoding concrete, failure-derived rules — which is then injected into the
system prompt of the *non-reasoning* model. The agent writes and runs its own analysis code
over the corpus — error-type frequencies, action $n$-grams, loop detection, win/loss
contrasts — and compiles what it finds into rules. No weights are updated, no environment
rollouts are collected for distillation, no per-instance search is run at deployment, and
the skill occupies a cacheable prefix: one pass over logs that production systems already
store.

Our contributions are:
  * **A corpus-to-skill distillation pipeline** requiring only existing rollouts and
    roughly $1–$3 of coding-agent time per domain (Section 3).
  * **Evidence that skills amortize the reasoning premium.** On held-out tasks across
    ALFWorld, SSB-Verified, and $\tau^{2}$-bench telecom/retail, skills recover 55%–100%+
    of the no-think$\to$think gap for GPT-5.4-mini, exceed the reasoning mode outright on
    ALFWorld and retail, and emit 2.7–5$\times$ fewer output tokens than the reasoning mode
    with zero reasoning tokens (Section 5).
  * **An ablation on distillation source.** Skills distilled from non-reasoning
    trajectories alone are competitive with skills distilled from paired think/no-think
    corpora, with domain-dependent differences in either direction (retail favors the
    paired corpus, SSB-Verified the no-think-only corpus by 10 points) — showing that
    reasoning traces are not a prerequisite for effective distillation (Section 5.2).
  * **A favorable comparison to automatic prompt optimization.** Against GEPA (1), a
    state-of-the-art reflective prompt evolver, our distilled skills score higher on both
    $\tau^{2}$ domains while costing 4.1$\times$ less to produce (Section 5.3).

We interpret these results through a search lens (Section 6): reasoning is *deep* search
within one episode; distillation is *wide* search across many. Where the required knowledge
is procedural and domain-level, width over cheap trajectories is the better buy. The
domains where a residual gap survives (telecom, SSB-Verified) are exactly those where
per-instance deliberation — long dependency chains, instance-specific spreadsheet logic —
cannot be captured by any fixed prompt.

## 2 Related Work

#### Test-time reasoning and its cost.

Chain-of-thought prompting (18) and RL-trained reasoning modes (10; 5; 12) trade tokens for
accuracy, and test-time compute can outperform parameter scaling (15; 9; 23). A growing
literature documents the inefficiency of this trade — overthinking on easy instances (4),
and mitigations via terse drafting or token budgets (19; 6). These methods compress
reasoning *within* an episode; we amortize it *across* episodes. Whether RL-induced
reasoning elicits knowledge already latent in the base model (24) is congenial to our
finding that the same procedural knowledge can be surfaced by a prompt.

#### Prompt optimization.

OPRO (20), DSPy/MIPROv2 (7; 11), TextGrad (25), and GEPA (1) search prompt space against a
validation metric, typically via many scored rollouts. Our pipeline is complementary but
cheaper in kind: a single reflective pass by a strong coding agent over an *existing*
corpus, with no optimization loop. Section 5.3 compares directly against GEPA.

#### Experiential learning for agents.

Voyager (16) grows a code skill library online; Reflexion (13) feeds verbal self-critique
into retries of the *same* task; ExpeL (26) and Agent Workflow Memory (17) extract insights
or workflows from experience. We share the extract-once-reuse-forever premise, but frame
the payoff differently: the skill is a substitute for an expensive *reasoning mode*,
evaluated by how much of the think/no-think gap it recovers per token, and produced by an
external coding agent rather than by the acting model itself.

## 3 Passive Skill Distillation

#### Setup.

Let $M$ expose a reasoning mode $M_{\mathrm{r}}$ (private reasoning tokens before each
action) and a non-reasoning mode $M_{\mathrm{nr}}$ (actions only). A benchmark supplies
tasks $\mathcal{T}=\mathcal{T}_{\mathrm{train}}\cup\mathcal{T}_{\mathrm{test}}$ (disjoint),
an environment loop (or simulated user), and terminal rewards. The input to distillation is
a trajectory corpus $\mathcal{D}$ collected once on $\mathcal{T}_{\mathrm{train}}$:
per-step observations, actions and tool calls, visible outputs, and rewards. $\mathcal{D}$
is whatever already exists; no new rollouts are collected for distillation.

#### Step 1: Collect a training corpus.

For each domain we roll out the model on the training split: 50 ALFWorld canonical tasks,
50 SSB-Verified tasks, 50 $\tau^{2}$-telecom and 35 $\tau^{2}$-retail training tasks. In
the *paired* condition, $\mathcal{D}$ contains both think and no-think trajectories from
the same tasks; in the *no-think-only* condition, only the latter. These are ordinary
evaluation rollouts — in practice such corpora often already exist.

#### Step 2: Distill with a coding agent.

A coding agent $A$ (an LLM with file-system and code-execution tools; here Claude Code with
Claude Sonnet 5 (2)) is opened in the directory containing the corpus and receives a fixed
natural-language instruction $P$, producing a skill $\sigma=A(\mathcal{D},P)$. The agent
compares failing and succeeding trajectories (and, when available, contrasts no-think
failures with think successes on the same tasks), computing corpus-level statistics —
failure-mode frequencies, action loops, win/loss contrasts — and reading individual
episodes where the statistics point. $A$ only reads the trajectory files and mode-level
pass rates; it has no environment access. The output is 40–130 lines of markdown whose
rules are concrete and traceable to transcript evidence, e.g., from the retail skill:
*“Before calling find_user_id_by_email, check that the customer’s message actually contains
a real email address … this bug appeared in 13 of 22 rollouts and accounted for 17 of 18
tool errors.”* Distillation is a one-time cost of $1.28–$2.44 per domain (Section 5.3).

#### Step 3: Deploy.

The skill is appended verbatim to the non-reasoning model’s system prompt:
$\pi_{\sigma}(\cdot)=M_{\mathrm{nr}}(\cdot\mid\mathrm{sys}\oplus\sigma)$. Nothing else —
harness, decoding, tools — changes between the no-think and skill conditions. The skill
adds a fixed, cacheable prompt prefix. Skills are distilled per model and per domain.

## 4 Experimental Setup

#### Benchmarks.

**ALFWorld** (14): text-based embodied household tasks (ReAct-style agent, admissible
commands, max. 40 steps); held-out random-50 split; win rate. **SSB-Verified**: a verified
subset of SpreadsheetBench (8), real-world spreadsheet manipulation against live workbooks;
held-out 50 tasks; modification accuracy. $\tau^{2}$**-bench** telecom and retail (3; 21):
conversational customer-service agents with tool use and a simulated user in a dual-control
environment; held-out test splits of 40 tasks; pass rate.

#### Models and modes.

GPT-5.4-mini with reasoning_effort $\in$ {none, medium} and Qwen3.6-27B with
enable_thinking $\in$ {false, true}, each served through a single gateway so that only the
reasoning flag (and, in skill conditions, the system prompt) differs between conditions.
Each cell is the mean of 3 evaluation seeds. Skills are produced once per domain per model
by Claude Sonnet 5 via Claude Code.

## 5 Results and Ablations
Table 1: **Main results.** Held-out success (3 seeds) and mean output tokens per episode
for GPT-5.4-mini and Qwen3.6-27B. “Token Reduction” indicates the token-reduction factor
relative to the think mode of the same model and benchmark. Bold marks the best score per
benchmark per model; underline marks the second best.

GPT-5.4-mini Qwen3.6-27B
Benchmark Mode Score Tokens Token Reduction Score Tokens Token Reduction
ALFWorld think _0.713_ 3,723 – 0.773 9,232 –
no-think 0.567 952 3.9$\times$ _0.827_ 991 9.3$\times$
no-think + skill **0.787** 832 4.5$\times$ **0.980** 619 14.9$\times$
SSB-Verified think **0.613** 3,291 – 0.560 2,826 –
no-think 0.447 960 3.4$\times$ _0.640_ 2,432 1.2$\times$
no-think + skill _0.560_ 831 4.0$\times$ **0.673** 2,729 1.0$\times$
$\tau^{2}$-telecom think **0.450** 2,143 – **0.933** 6,058 –
no-think 0.192 421 5.1$\times$ _0.883_ 985 6.2$\times$
no-think + skill _0.333_ 597 3.6$\times$ **0.933** 1,026 5.9$\times$
$\tau^{2}$-retail think _0.350_ 1,615 – **0.633** 4,124 –
no-think 0.325 536 3.0$\times$ _0.600_ 1,058 3.9$\times$
no-think + skill **0.408** 565 2.9$\times$ 0.558 1,180 3.5$\times$

### 5.1 Skills recover most of the reasoning gap at a fraction of the tokens
Figure 2: ALFWorld task – (*“put a cool tomato in microwave”*). Non-reasoning model with
and without skill. Without it the model never cools the tomato and loops on look to the
step cap (left); with it the model issues cool tomato 1 with fridge 1 and finishes (right).
Verbatim from the rollouts.

Table 1 shows the central result. For GPT-5.4-mini, the reasoning mode beats no-think on
all four benchmarks (by $+14.6$, $+16.6$, $+25.8$, and $+2.5$ points); injecting a
distilled skill into the no-think model recovers 55%–100%+ of that gap everywhere,
exceeding the reasoning mode outright on ALFWorld (0.787 vs. 0.713) and $\tau^{2}$-retail
(0.408 vs. 0.350), while emitting 2.9–4.5$\times$ fewer output tokens and zero reasoning
tokens. On ALFWorld and SSB the skill even undercuts the plain no-think baseline in tokens:
fewer flailing retries means shorter episodes (21.8 vs. 27.0 turns on ALFWorld). Because
the skill lives in a cacheable system-prompt prefix, its marginal deployment cost is
negligible, while the think premium is re-paid on every episode. Beating the teacher is not
paradoxical: a rule aggregated over 50 training episodes is more reliable than a derivation
the reasoning model must re-produce correctly each time. Indeed, the reasoning model itself
occasionally falls into the ALFWorld appliance-door loop that the skill forbids outright
(Appendix A).

The gains are legible at the level of individual trajectories. Consider a single held-out
ALFWorld task, “put a cool tomato in microwave” (Figure 2). The non-reasoning baseline
picks up the tomato and places it in the microwave without ever cooling it, treating the
adjective *cool* as a property rather than a required action; having changed nothing, it
then issues look twenty times in a row, waiting for a completion signal that never arrives,
and exhausts its 40-step budget. The distilled skill supplies exactly the two missing
pieces: a rule that adjectives such as *cool* must be realized with an explicit cool X with
fridge command, and a rule to break out of repeated no-op observations. With these, the
same model issues the cool command at step 19 and completes the task in 30 steps. These are
not isolated fixes: the missed-transform failure occurs in 35.9% of transform tasks without
the skill and 11.5% with it, and stall loops fall from 28.7% to 5.3%, together accounting
for most of the ALFWorld win-rate improvement.

The Qwen3.6-27B columns repeat the study with a second model and Qwen-specific skills.
Distillation again helps on three of four benchmarks, reaching 0.980 on ALFWorld
(near-ceiling, $+15.3$ over no-think) and 0.673 on SSB-Verified, and matching the think
mode on telecom (0.933) at $5.9\times$ fewer output tokens, even though Qwen3.6-27B’s
reasoning mode is itself unreliable and *hurts* on ALFWorld ($-5.4$) and SSB-Verified
($-8.0$). Retail is the one regression ($-4.2$ points): with a near-zero think/no-think gap
and an already-competent base, added rules may over-constrain.

### 5.2 Distilling from reasoning vs non-reasoning trajectories
Table 2: **Ablation: distillation source.** Held-out pass rate and mean output tokens per
episode for a skill distilled from *no-think* rollouts only vs. from a paired corpus that
additionally includes reasoning (*think*) traces (GPT-5.4-mini); both skills are injected
into the same non-reasoning model and emit zero reasoning tokens. Bold marks the higher
score per benchmark.

                   Think-distilled   No-think-distilled
Benchmark          Score     Tokens  Score     Tokens
ALFWorld           **0.813** 748     0.787     832
SpreadsheetBench   0.460     820     **0.560** 831
$\tau^{2}$-telecom 0.325     533     **0.333** 597
$\tau^{2}$-retail  **0.458** 599     0.408     565

Our main results (Table 1) use skills distilled from non-reasoning trajectories alone — the
distiller never sees a reasoning trace. A natural question is whether giving the distiller
access to reasoning traces changes the resulting skill. We therefore ablate the corpus
composition for GPT-5.4-mini: the *no-think-only* condition distills from non-reasoning
rollouts, while the *paired* condition additionally includes think-mode trajectories from
the same training tasks (Section 3), allowing the distiller to contrast no-think failures
with think successes on identical tasks.

Table 2 shows a mixed picture. The two sources are statistically close on ALFWorld (0.787
vs. 0.813) and telecom (0.333 vs. 0.325). On retail, the paired corpus produces the
stronger skill (0.458 vs. 0.408), suggesting that reasoning traces can supply useful signal
— e.g., successful think-mode demonstrations of the authentication discipline that no-think
rollouts consistently violate. On SSB-Verified the ordering reverses, and sharply: the
no-think-only skill scores 10 points higher (0.560 vs. 0.460). One plausible mechanism is
that verbose reasoning narratives anchor the distiller on what the model *believed* rather
than on workbook-level evidence of what *was true*, but we have not isolated this and note
that each skill was distilled once, so distillation variance is uncontrolled (Section 7).

We draw two cautious conclusions. First, reasoning traces are not a *prerequisite* for
effective distillation: no-think-only skills are competitive everywhere and recover
55%–100%+ of the reasoning gap in Table 1, which matters practically because the full
amortization loop — deploy cheap agent $\to$ collect logs $\to$ distill $\to$ redeploy —
can then run without ever invoking a reasoning model. Second, whether adding reasoning
traces helps or hurts appears to be domain-dependent, and the per-benchmark differences
here are within a range where distillation noise cannot be ruled out.

### 5.3 Comparison with a prompt optimizer
Table 3: **Distilled skills vs. GEPA-optimized prompts** ($\tau^{2}$ test splits,
GPT-5.4-mini no-think, mean of 3 seeds) Scores and one-time production cost of the two
$\tau^{2}$ skills.

                   Pass rate                           Production cost
Domain             no-skill think     GEPA    Ours     GEPA   Ours
$\tau^{2}$-retail  0.325    0.350     _0.392_ **0.458** $2.26  **$1.28**
$\tau^{2}$-telecom 0.192    **0.450** 0.308   _0.325_  $13.02 **$2.44**

We compare against GEPA (1), a state-of-the-art reflective prompt evolver, on both
$\tau^{2}$ domains (GPT-5.4-mini rollouts, Claude Sonnet 5 reflection; 120 metric call
budget). Table 3: our distilled skills score higher on both domains (retail 45.8% vs.
39.2%; telecom 32.5% vs. 30.8%) at 4.1$\times$ lower production cost ($3.72 vs. $15.28);
the gap is driven by GEPA’s active rollouts for each optimization-proposed prompt.
Extending the telecom GEPA budget to 240 metric calls resulted in a byte-identical prompt,
indicating convergence.

### 5.4 Robustness

All results are means over 3 runs with the same protocol for baselines and skills; per-seed
numbers show consistent orderings (e.g., Qwen ALFWorld skill: 0.98/0.98/0.98; GPT-5.4-mini
telecom skill above no-think on all seeds). Skills were distilled once per domain — we do
not report variance over the distillation itself, a limitation discussed below.

## 6 Discussion: Deep vs. Wide Search

A unifying reading of Tables 1–3 is that test-time reasoning and corpus distillation are
two ways of purchasing the same commodity — procedural knowledge about a domain — with
different cost structures. Reasoning is *deep* search: within a single episode the model
explores a tree of considerations before each action. Its knowledge is rediscovered from
scratch and its cost recurs per episode. Distillation is *wide* search: many complete
trajectories are examined side by side, regularities in the failure distribution are
extracted once, and the result is reused for free. When the knowledge that deep search
recovers is episode-invariant — ALFWorld’s atomic clean/heat/cool commands, retail’s
authenticate-then-fetch-orders discipline — width strictly dominates: it is paid once, and
Table 1 shows it can even exceed think mode, because a rule compiled from 50 episodes is
more reliable than a derivation the model must reproduce correctly every time.

The lens also predicts where amortization must fall short. The residual think-over-skill
gap on telecom (0.450 vs. 0.333) and SSB-Verified (0.613 vs. 0.560) marks knowledge that is
*not* episode-invariant: telecom tasks hinge on long, instance-specific dependency chains
in a dual-control environment (which line, which plan, what the user just toggled), and
spreadsheet tasks embed one-off logical structure no fixed prompt anticipates. There,
per-instance deep search is doing irreplaceable work, and the two mechanisms are
complements: a skill to stop re-buying the invariants, reasoning reserved for the instances
that need it.

Finally, the NT-skill result sharpens what distillation actually consumes. Reasoning traces
are verbose, stylized, and describe what the model *believed*; environment feedback in
failed no-think trajectories records what *was true*. On SSB-Verified the paired-corpus
skill (46.0%) underperformed the no-think-only skill (56.0%), consistent with the distiller
anchoring on reasoning narratives instead of workbook-level failure evidence. Wide search
needs breadth of outcomes, not depth of introspection — which is convenient, since
non-reasoning trajectories are the cheap ones.

#### Amortization economics.

Distillation is one coding-agent pass over the corpus ($1.28–$2.44 per domain; Table 3).
Per episode, the skill then saves $\Delta=T_{\mathrm{think}}-T_{\mathrm{skill}}$ output
tokens — e.g., $2{,}143-597=1{,}546$ on telecom, essentially the model’s entire 1,572-token
reasoning budget — while adding only a fixed, cacheable input prefix. The one-time cost is
repaid once cumulative per-episode savings exceed it; every subsequent episode is pure
savings. By contrast, active prompt optimizers (1; 20) spend an evaluation-rollout budget
*before* any savings accrue, and cannot run at all where fresh rollouts are unavailable.

#### Relation to elicitation.

RL-trained reasoning appears to *elicit* latent base-model capabilities rather than create
new ones (24; 9; 23). Our results are the prompt-side counterpart: if the non-reasoning
model already carries the priors needed to execute winning procedures, a distilled
description of where search reliably lands is a sufficient — and far cheaper — elicitor.
The corpus-source ablation sharpens this: even the description need not come from the
reasoning model.

## 7 Limitations

Skills were distilled once per model–domain pair; we measure evaluation variance (3 seeds)
but not distillation variance, and the Qwen retail regression suggests the process is not
uniformly reliable. Results cover two models and four domains; skills are model-specific
and cross-model transfer is untested.

## 8 Conclusion

A small corpus of ordinary trajectories, one pass by a coding agent, and a hundred lines of
markdown recover most — sometimes all — of what an expensive reasoning mode buys on agentic
benchmarks, at 2.7–6$\times$ fewer output tokens per episode and a one-time cost of a few
dollars — and the corpus need not contain a single reasoning trace. Reasoning re-derives
domain procedure inside every episode; distillation extracts it once.

## References
  * Agrawal et al. (2026) L. A. Agrawal, S. Tan, D. Soylu, N. Ziems, R. Khare, K.
    Opsahl-Ong, A. Singhvi, H. Shandilya, M. J. Ryan, M. Jiang, C. Potts, K. Sen, A. G.
    Dimakis, I. Stoica, D. Klein, M. Zaharia, and O. Khattab GEPA: reflective prompt
    evolution can outperform reinforcement learning. In International Conference on
    Learning Representations (ICLR), Note: arXiv:2507.19457
  * Anthropic (2025) Anthropic Claude code. Note: Agentic coding tool; runs used Claude
    Sonnet 5. https://www.anthropic.com/claude-code
  * Barres et al. (2025) V. Barres, H. Dong, S. Ray, X. Si, and K. Narasimhan
    $\tau^{2}$-Bench: evaluating conversational agents in a dual-control environment. arXiv
    preprint arXiv:2506.07982.
  * Chen et al. (2024) X. Chen, J. Xu, T. Liang, Z. He, J. Pang, D. Yu, L. Song, Q. Liu, M.
    Zhou, Z. Zhang, R. Wang, Z. Tu, H. Mi, and D. Yu Do NOT think that much for 2+3=? on
    the overthinking of o1-like LLMs. arXiv preprint arXiv:2412.21187.
  * Guo et al. (2025) D. Guo, D. Yang, H. Zhang, et al. DeepSeek-R1 incentivizes reasoning
    in LLMs through reinforcement learning. Nature 645 (8081), pp. 633–638. Note: Also
    available as arXiv:2501.12948 External Links: Document
    (https://dx.doi.org/10.1038/s41586-025-09422-z)
  * Han et al. (2024) T. Han, Z. Wang, C. Fang, S. Zhao, S. Ma, and Z. Chen
    Token-budget-aware LLM reasoning. arXiv preprint arXiv:2412.18547.
  * Khattab et al. (2024) O. Khattab, A. Singhvi, P. Maheshwari, Z. Zhang, K. Santhanam, S.
    Vardhamanan, S. Haq, A. Sharma, T. T. Joshi, H. Moazam, H. Miller, M. Zaharia, and C.
    Potts DSPy: compiling declarative language model calls into state-of-the-art pipelines.
    In International Conference on Learning Representations (ICLR), Note: arXiv:2310.03714
  * Ma et al. (2024) Z. Ma, B. Zhang, J. Zhang, J. Yu, X. Zhang, X. Zhang, S. Luo, X. Wang,
    and J. Tang SpreadsheetBench: towards challenging real world spreadsheet manipulation.
    Advances in Neural Information Processing Systems (NeurIPS). Note: arXiv:2406.14991
  * Muennighoff et al. (2025) N. Muennighoff, Z. Yang, W. Shi, X. L. Li, L. Fei-Fei, H.
    Hajishirzi, L. Zettlemoyer, P. Liang, E. Candès, and T. Hashimoto S1: simple test-time
    scaling. In Empirical Methods in Natural Language Processing (EMNLP), pp. 20275–20321.
    Note: arXiv:2501.19393
  * OpenAI (2024) OpenAI Learning to reason with LLMs. OpenAI Technical Report. Note:
    https://openai.com/index/learning-to-reason-with-llms/
  * Opsahl-Ong et al. (2024) K. Opsahl-Ong, M. J. Ryan, J. Purtell, D. Broman, C. Potts, M.
    Zaharia, and O. Khattab Optimizing instructions and demonstrations for multi-stage
    language model programs. In Empirical Methods in Natural Language Processing (EMNLP),
    Note: MIPROv2
  * Shao et al. (2024) Z. Shao, P. Wang, Q. Zhu, et al. DeepSeekMath: pushing the limits of
    mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300. Note:
    Introduces GRPO
  * Shinn et al. (2023) N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao
    Reflexion: language agents with verbal reinforcement learning. In Advances in Neural
    Information Processing Systems (NeurIPS),
  * Shridhar et al. (2021) M. Shridhar, X. Yuan, M. Côté, Y. Bisk, A. Trischler, and M.
    Hausknecht ALFWorld: aligning text and embodied environments for interactive learning.
    In International Conference on Learning Representations (ICLR),
  * Snell et al. (2024) C. Snell, J. Lee, K. Xu, and A. Kumar Scaling LLM test-time compute
    optimally can be more effective than scaling model parameters. arXiv preprint
    arXiv:2408.03314.
  * Wang et al. (2023) G. Wang, Y. Xie, Y. Jiang, A. Mandlekar, C. Xiao, Y. Zhu, L. Fan,
    and A. Anandkumar Voyager: an open-ended embodied agent with large language models.
    arXiv preprint arXiv:2305.16291.
  * Wang et al. (2024) Z. Z. Wang, J. Mao, D. Fried, and G. Neubig Agent workflow memory.
    arXiv preprint arXiv:2409.07429.
  * Wei et al. (2022) J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi,
    Q. V. Le, and D. Zhou Chain-of-thought prompting elicits reasoning in large language
    models. In Advances in Neural Information Processing Systems (NeurIPS),
  * Xu et al. (2025) S. Xu, W. Xie, L. Zhao, and P. He Chain of draft: thinking faster by
    writing less. arXiv preprint arXiv:2502.18600.
  * Yang et al. (2024) C. Yang, X. Wang, Y. Lu, H. Liu, Q. V. Le, D. Zhou, and X. Chen
    Large language models as optimizers. In International Conference on Learning
    Representations (ICLR),
  * Yao et al. (2024) S. Yao, N. Shinn, P. Razavi, and K. Narasimhan $\tau$-Bench: a
    benchmark for tool-agent-user interaction in real-world domains. arXiv preprint
    arXiv:2406.12045.
  * Yao et al. (2023) S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao
    ReAct: synergizing reasoning and acting in language models. In International Conference
    on Learning Representations (ICLR),
  * Ye et al. (2025) Y. Ye, Z. Huang, Y. Xiao, E. Chern, S. Xia, and P. Liu LIMO: less is
    more for reasoning. In Conference on Language Modeling (COLM), Note: arXiv:2502.03387
  * Yue et al. (2025) Y. Yue, Z. Chen, R. Lu, A. Zhao, Z. Wang, S. Song, and G. Huang Does
    reinforcement learning really incentivize reasoning capacity in LLMs beyond the base
    model?. arXiv preprint arXiv:2504.13837.
  * Yuksekgonul et al. (2025) M. Yuksekgonul, F. Bianchi, J. Boen, S. Liu, P. Lu, Z. Huang,
    C. Guestrin, and J. Zou Optimizing generative AI by backpropagating language model
    feedback. Nature 639 (8055), pp. 609–616. Note: Also available as arXiv:2406.07496,
    “TextGrad: Automatic Differentiation via Text” External Links: Document
    (https://dx.doi.org/10.1038/s41586-025-08661-4)
  * Zhao et al. (2024) A. Zhao, D. Huang, Q. Xu, M. Lin, Y. Liu, and G. Huang ExpeL: LLM
    agents are experiential learners. In AAAI Conference on Artificial Intelligence,

## Appendix A Distilled Skill Excerpts

Abridged excerpts from the distilled skills (full files range from 38 to 126 lines of
markdown). Rules are imperative, concrete, and cite corpus statistics computed by the
distiller.

#### ALFWorld (no-think-distilled), Rule 1 of 5.

  *Adjectives in the task are actions, not descriptions.* If the task says “clean”, “hot”,
  or “cool/cold” X, that adjective is a required state-change step. You must issue the
  explicit verb: clean <object> with sinkbasin 1, heat <object> with microwave 1, cool
  <object> with fridge 1. Do not substitute “open microwave, move object in, close, open,
  take back out” for heat X with microwave 1 — opening/closing an appliance does not
  perform the transformation.

#### $\tau^{2}$-retail (paired-corpus), Rule 1 of 6.

  *Never call an authentication tool with a guessed or placeholder argument.* This was the
  single most common bug: it appeared in 13 of 22 rollouts (59%) and accounted for 17 of
  18 tool errors observed (94%). Before calling find_user_id_by_email or
  find_user_id_by_name_zip, check that the customer’s message actually contains a real
  email address, or a real first name $+$ last name $+$ zip. If none is present yet, do
  not call any lookup tool — respond in plain text asking for one.

#### SSB-Verified (no-think-distilled), central rule.

  *Finish inside the workbook, not just in the chat.* Never end a task by only describing
  a formula, a macro, or an approach in your response — explaining the right formula and
  then not entering it into the sheet is the single most common way this task goes wrong.
  If the user asks for a VBA macro, still apply the equivalent transformation directly to
  the workbook via code.

## Appendix B Reproduction Details

#### Splits.

ALFWorld: distill on 50 training tasks, evaluate on a disjoint held-out set of 50 tasks.
$\tau^{2}$: distill on 50 (telecom) / 35 (retail) training tasks, evaluate on the provided
40-task test splits. SpreadsheetBench-Verified: distill on 50 training tasks, evaluate on a
disjoint held-out set of 50 tasks. For ALFWorld and SSB-Verified, which do not ship a
designated test split, the held-out sets are sampled once and fixed across all conditions.

#### Harness.

ALFWorld uses a ReAct-style agent with admissible-command grounding and a 40-step cap.
SSB-Verified uses a ReAct-style tool-use harness in which the model writes and executes
openpyxl and pandas code against a live copy of the workbook, following the original
SpreadsheetBench setup [8]. $\tau^{2}$ uses the standard runner with an LLM user simulator.
In all cases the skill is injected by appending it to the agent’s system prompt with no
other change to harness, decoding, or tools; the same protocol is used for all conditions.


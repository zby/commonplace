---
source: https://poetiq.ai/posts/rsi_perspective/
description: "Poetiq's definition and taxonomy of recursive self-improvement, with vendor-reported benchmark evidence for optimizing harnesses and self-rewriting code instead of model weights"
captured: 2026-08-07
capture: web-fetch
genre: practitioner-report
type: kb/sources/types/snapshot.md
---

# A Poetiq Perspective on Recursive Self-Improvement

Author: Poetiq
Source: https://poetiq.ai/posts/rsi_perspective/
Date: August 4, 2026

RSI is the fastest path to superintelligence, because its gains compound at every step.

## RSI is here, and it's fast

At Poetiq, we believe RSI is the single most important frontier in AI research today, because it is the fastest path to superintelligence. The reason is simple: the gains from RSI compound with every step. Humans don't become continuously smarter while improving models. RSI systems can.

As Anthropic recently stated,[^1] AI that can improve itself would be a “major development in the history of technology” — one with enormous potential to do good in science, healthcare, and beyond. They also raise thoughtful questions about how to keep these systems controllable as they accelerate, and we think they're right to ask them.

RSI is already here; we've been watching it work for months at Poetiq. Most of the field is still debating when it will arrive — we're past that question, focusing now on how to build it well. Not all RSI is alike: the form it takes shapes both how good and how controllable it can be, and we've deliberately chosen one of the more controllable forms. We've also chosen a form that is *fast*; in less than a year we went from zero to automatically achieving state-of-the-art results on major benchmarks.

In the following, we define RSI and reveal some details about our approach, self-optimizing optimizers, for the first time. We compare our approach to other major current approaches to RSI and discuss some of the evidence supporting the benefits of our self-optimizing optimizers. We also share our perspective on safety and control, and give an overview of our long-term vision.

## Defining RSI

“RSI” has become one of the most overloaded terms in the field, so let's be precise. Not every system that improves over time is doing RSI. Consider the three letters in turn.

**(I)mprovement** is the easy part: the system gets better at a task, generally in an iterative loop. But this isn't a differentiator — plenty of classical and modern AI systems clear this bar through better algorithms, more data, or longer training runs. What actually distinguishes RSI lives in the **R** and the **S**.

**(R)ecursive** and **(S)elf** are the parts that matter. *Self* means the system improves itself, not some external target. *Recursive* means its newly improved capabilities become the tools it uses to drive the next round of improvement. These come as a pair: a system that genuinely improves itself is, by the next step, a better improver running the loop. Improve some other target and the gains never feed back; improve yourself just once and there's no chain reaction. Put the two together and every improvement raises the system's ability to make the next one.

Drop the R and the S and you fall back to standard iterative optimization. Keep both, and the improvement compounds and the exponential gains are realized.

**A concrete example** of a method sometimes confused with RSI but which is **not RSI** is *autoresearch*[^2] (and the similar broader class of “Automated AI Scientists”) where the core AI system improves some target LLM, but does not use that target LLM to generate subsequent improvements. Closing the loop, so the model being improved is the one driving the improvement, would turn it into genuine RSI.

> The gains from RSI compound with every step. Humans don't become continuously smarter while improving models. RSI systems can.

## There's more than one way to build RSI

Even for genuine RSI, there are multiple options about what improves at each step. That choice sets how fast and how efficiently — in terms of compute, cost, and data — the loop can run.

Most approaches are **LLM-centric**: the language model itself is the unit of improvement, and improvement flows through neural-network training. Anthropic's work is a clear example: Claude Code helps build the next Claude, with a model-training step at each turn. Similarly, OpenAI intends to have their own automated AI researcher doing a “significant fraction” of their internal research by 2028,[^3] and Google is using AlphaEvolve to make training LLMs more efficient.[^4] These approaches are powerful. But when the model is the thing you improve, every step inherits the cost, latency, and energy of a training run. On an exponential curve, what matters is how quickly you clear that slow early regime, and with months between steps, the benefits of compounding take far longer to arrive.

## Poetiq's approach: self-optimizing optimizers

Poetiq takes a whole-system view. We treat the LLM as a single component of a larger reasoning system (code, prompts, exploration/exploitation strategies, and more) and what improves in each iteration is the *system*, not necessarily the model's weights.

Concretely, the Poetiq Metasystem is a **self-optimizing optimizer**. Each problem, task, and dataset it optimizes helps it to optimize itself, building itself into a more and more powerful optimizer. The resulting optimizer is general, allowing us to apply it to any part of the Metasystem. Of course, this can include optimizing the weights of models we use. But importantly, the Metasystem also opens far more efficient approaches to achieve dramatic improvements. All of our state-of-the-art results have come without ever modifying LLM parameters. Instead, the Metasystem has been directly optimizing harnesses for each benchmark, and directly optimizing its own code at the same time.

This reframing is what lets our RSI loop run quickly and cheaply today while still compounding. It also frees us from betting on any single model: we can use any model, or several at once, as tools.

### Poetiq and the RSI landscape

In Figure 1 we show the RSI landscape on two axes: whether a system performs standard iterative optimization or genuine RSI on the X axis, and whether its improvement loop is fast and cheap or slow and expensive on the Y axis. Many notable RSI efforts, including Anthropic, OpenAI, Google, and various smaller efforts, sit on the genuine RSI side of the figure, but most currently use slow-and-expensive methods.

The Poetiq Metasystem, as a self-optimizing optimizer modifying its own codebase, clearly lands in the cheap, genuine RSI quadrant. The other approaches near Poetiq are also compelling, but are more limited in generality (DGM and SICA focus on coding tasks) or in grounding (MiniMax generates some of its own evaluations). (More details can be found in the Appendix.) The Metasystem, by contrast, is a fully generic optimizer and is grounded in real task data rather than self-generated evaluations. Both of these differences improve its usefulness for RSI, so it sits furthest into the cheap, genuine-RSI corner. See the Appendix for detailed descriptions of the systems in the figure.

*[Figure: A scatter plot of RSI approaches, with closure of the improvement loop on the X axis and cost per step on the Y axis. Poetiq's Metasystem sits furthest into the cheap, genuine-RSI quadrant, alongside SICA, MiniMax's harness, and the Darwin Gödel Machine; expensive, training-based approaches from Anthropic, OpenAI, Google DeepMind, Meta, and academia sit below.]*

*Figure 1. The RSI landscape. A subset of recent approaches often described as RSI. On the left are approaches with little or no recursion, including RL post-training and AI Scientist systems that do not optimize their own system for further improvement. On the right are systems with substantial recursion, including expensive methods that require training an LLM, and fast, cheap methods like Poetiq's Metasystem.*

## SOTA results from RSI

We started this journey just over a year ago, with the Metasystem optimizing pieces of individual tasks. We chose the first three benchmarks deliberately, to span the capabilities that matter most for LLMs: reasoning (ARC-AGI), retrieval (Humanity's Last Exam and SimpleQA), and coding (LiveCodeBench Pro). Each of those tasks taught the Metasystem general strategies for building better harnesses, and every one of those lessons fed back in to tackle the next task.

Each benchmark needed less of us than the one before. By the time we reached LiveCodeBench Pro, the Metasystem built and optimized a complete coding harness entirely on its own: no fine-tuning, no privileged model access, only standard API calls. The automatically-generated harness improved Gemini 3.1 Pro by 12.3%, and that same harness, applied unchanged to GPT-5.5, set a new SOTA at 93.9%. Every model we tested improved, open-weights and proprietary alike.

Then the loop closed again: the Metasystem used what it learned building that harness to improve itself further.

That accumulated capability is what made our most recent results, Benchmarks Are Dead, possible. Given six benchmarks it had never seen, spanning competition math, scientific coding, long-horizon planning, agentic tool use and long-context retrieval, the Metasystem set a new state of the art on all six, with zero human intervention. For half of them we set the record with a model one generation older than the previous holder. We never used Claude Fable 5 as an underlying model, and routinely outperformed it.

This progression is the whole point. The earlier benchmarks weren't just wins, they were training for the engine, and the payoff was a fully autonomous Metasystem producing results entirely on its own. Each turn of the loop makes the next one faster and more autonomous. That's Recursive and Self, not just Improvement, and we're already seeing the compounding gains.

## The engine behind those results

The Poetiq Metasystem has three functions:

1. **It improves itself.** The Metasystem is recursively self-improving: every problem it solves makes it better at solving the next, which is why we deliberately tackle a diverse set of problems across industries rather than restricting ourselves to one vertical. This builds a library of cross-domain strategies while optimizing its own codebase.
2. **It turns datasets into harnesses.** Given a dataset, it autonomously produces a task-specific harness that is far more capable than the underlying LLM at that task. Think of it as the ultimate result of fine-tuning, but achieved without touching a single model weight. As demonstrated on our published results, the harness is immediately portable to any model (frontier LLMs, open-source, or proprietary), even ones it has never seen.
3. **It maps the frontier.** As it works, it builds concrete, data-backed maps of what each model, public or private, is actually good at, down to specific domains and tasks, along with the exact data that would improve them. Those maps are precisely what's needed for general and targeted future refinement, tuning, and training.

## Model-agnostic RSI

Because the Metasystem builds on top of models rather than into them, we don't bet on any single architecture, training pipeline, or model. In fact, we're not even betting on the current generation of LLMs. If a better architecture arrives tomorrow (for example, Diffusion Models or State Space Models), it's a drop-in replacement. Already, when a new frontier model is announced we integrate it within hours and the system immediately performs better. If a model gets too expensive, or data-sovereignty requirements rule it out for a client, our switching cost is zero.

The byproducts of our RSI loop, including RL-ready training data, novel search strategies, and model capability maps, are valuable in their own right and are exactly the raw materials needed to keep improving the Metasystem and the tools it uses. The engine generates its own fuel while solving hard problems.

## A more controllable path

This brings us back to the questions about safety and control. Our approach to safety has three prongs, and we take them seriously.

1. **We decide what the system works on; it doesn't.** The Metasystem improves by being given well-defined problems to solve. Along the way, it learns general problem-solving strategies that transfer to new domains. However, it is not free to choose its own problems or to form overarching goals of its own. While its capability compounds, the objectives remain well-defined and limited.
2. **We deliver task-specific solutions without exposing broad capabilities.** A harness aimed at one well-scoped task is far easier to evaluate, bound, and monitor than a general-purpose system. The Metasystem that produces the harnesses is never exposed. This sharply shrinks the surface for misuse compared to general-purpose, publicly-available models.
3. **Our improvements are inspectable.** Because our RSI operates at the level of the system rather than the model's weights, our improvements are interpretable. For example, a harness is code, prompts, and human-readable data, and the training data it generates is made of inspectable examples. Contrast this with weight-level RSI, which bakes each change into a new model that may have trillions of opaque parameters that no one can yet fully interpret.

Our approach gives far tighter control over misuse and loss of control than releasing a general, self-improving system publicly.

## Poetiq's longer-term vision

Our technical roadmap has three major stages. Stage 1 is already mature; we're preparing to move into Stage 2.

**Stage 1: Building on top of models.** From Poetiq's inception, our philosophy has been to tackle RSI in the fastest way possible. We began working outside the LLM. The Poetiq Metasystem is now a working RSI system that uses LLMs as tools. From here, the next stages move down and to the right in Figure 2, letting our RSI loop control a larger part of the full system stack. Most importantly, in comparison to starting at Stage 2 or Stage 3, each stage is both enabled and made more efficient by the improvements from the stages that came before it.

**Stage 2: Customize open-weights models for RSI.** Our next major endeavor is to post-train our own RSI-focused model, using exactly the assets the current loop generates as it works: capability maps, RL-ready training data, and the search strategies we've learned for doing RSI well. Combined with the RSI already running outside the LLM, this is Metasystem-informed post-training: rather than training a model in isolation, we train it to work in conjunction with the Metasystem. (See “Poetiq Metasystem + Post-Training” in Figure 2.) We expect this to unlock both deeper improvement strategies and much tighter model/harness integration, without tying us (or any of our customers) to a single model. For the select domains where a proprietary model still has an edge, our switching cost remains zero, and we'll always use the best model for the job, including our own.

Where do the first two stages lead? The Metasystem is already learning how to search, optimizing its own optimizers, and automatically finding the weak points and training regimes of the models it uses. As that capability compounds across the stack, the automatic discovery of more efficient frontier architectures becomes a natural consequence of our RSI progressing further.

**Stage 3: Train RSI models from scratch.** At this point, we will be ready to train our own RSI models from scratch to further accelerate towards superintelligence. (See “Poetiq Metasystem + Full Training” in Figure 2.) Compared to RSI approaches that currently rely on expensive training runs, the timing of this approach is an effective time and knowledge arbitrage, allowing us to pay less for larger gains in the future, because we arrive at that stage with optimizers already tuned by years of cheaper RSI.

*Figure 2. Poetiq's trajectory. As in Figure 1, we compare where Poetiq's Metasystem is today with other approaches to RSI, but additionally we show where our next stages will take us. As we cover more of the stack, by first post-training an LLM to be expert at our form of RSI (Poetiq Metasystem + Post-Training), and then by training our own RSI model from scratch (Poetiq Metasystem + Full Training), a more powerful RSI system is obtained, while leveraging the efficiency gains from our earlier RSI systems.*

## The frontiers of AI

The next phase transition in AI won't come from a system that has been taught by humans to improve. Instead, the leap will come from a system that invents its own improvements and feeds them back into itself.

We believe that's the fastest path to superintelligence, and consequently that recursive self-improvement is the single most important frontier in AI research right now.

That's why we built Poetiq — and why we're hiring. If RSI is the problem you want to spend the next few years on, come build it with us.

## Appendix

Here we dive a bit deeper into each of the approaches shown in Figure 1, and give broad classifications of approaches. Each class has different strengths and weaknesses.

### Standard iterative optimization

These approaches are not generally RSI, but are sometimes confused with it. They lack the self-recursion required for RSI.

- **[AI Scientist](https://sakana.ai/ai-scientist/) / [autoresearch](https://github.com/karpathy/autoresearch)** (Sakana AI / Andrej Karpathy). An LLM-driven pipeline that autonomously generates research ideas, runs experiments, and writes up papers, with an automated reviewer scoring the results. It sits at the left because the loop improves an external artifact rather than the model running it, and low-to-middle on cost because it only needs inference plus lightweight experiments.
- **[GEPA](https://arxiv.org/abs/2507.19457)** (academic). A prompt optimizer that evolves a population of prompts using natural-language reflection on execution feedback, with Pareto selection across tasks. It's left-side because the optimizer improves prompts (an external artifact) and isn't itself improved, and cheap because it's pure inference-time search with no training.
- **[DSPy](https://github.com/stanfordnlp/dspy)** (academic). A framework that compiles and optimizes prompt-programs against a chosen metric, treating LLM pipelines as modules to be tuned. It's far left because the optimizer itself generally isn't being optimized, but it is cheap due to its use of inference-time optimization.

### Strongly-grounded self-play

These approaches have strong self-recursion required for RSI and rely on self-play in a grounded environment (such as coding benchmarks) for their learning signal. The approaches are powerful, but the need for a grounded environment can restrict their scope.

- **Self-targeting AI Scientist** (hypothetical). The same AI-Scientist loop, but pointed at improving the same LLM it runs on, so its research output feeds back into its own weights. It moves far right because that closes a genuine same-lineage loop, and to the most expensive tier because each cycle requires retraining the model.
- **[Absolute Zero Reasoner](https://arxiv.org/abs/2505.03335)** (academic). A single model proposes its own coding/reasoning tasks and learns to solve them, with a code executor providing verifiable rewards and no external data. It's far right because the curriculum-generator is learned and in-lineage with a checkable signal, and mid-high on cost because every iteration is RL post-training.

### Weakly-grounded self-play

These approaches have self-recursion, but they rely on much weaker training signals, in some cases using only data the underlying LLM has been previously trained on. This tends to restrict their usefulness, as it can be difficult to prevent such systems from drifting away from the desired behavior, particularly as the number of RSI steps increases.

- **[Self-Rewarding LMs](https://arxiv.org/abs/2401.10020)** (Meta). A model generates its own preference data and judges it via LLM-as-a-judge, training on those self-labeled pairs across iterations. High closure (each round feeds the next same-lineage checkpoint) but pulled leftward by self-referential grounding — the model grades its own homework — and costly because each round is preference-based post-training.
- **[Constitutional AI](https://arxiv.org/abs/2212.08073)** (Anthropic). Uses AI-generated feedback against a human-written set of principles to supervise the model's own outputs, replacing much of human preference labeling. Strong closure, but the acceptance signal is a learned/self-generated judge rather than external reality, and the RL stage makes it expensive.
- **Same-lineage self-distillation** (generic). A model distills or compresses itself into a successor that becomes the next round's starting point. The loop closes within one lineage, but “cheaper, not more grounded” — the teacher is itself — and the per-step cost lands mid-to-high because it still requires training.
- **[R-Zero](https://arxiv.org/abs/2508.05004)** (academic). A Challenger and Solver spawned from one base model co-evolve with no external data, using the Solver's self-consistency and majority-voted pseudo-labels as the reward. High closure but the weakest grounding here — there's no external verifier anywhere in the loop — and cost is high because both roles are trained with RL each round.

### Self-rewriting agents

These approaches can have strong self-recursion and often can use fairly arbitrary datasets for their training signal. They focus on improving the scaffolding around the underlying LLMs, making them fast and cheap to iterate on. However, it is possible that their performance is upper-bounded by the quality of the underlying LLMs. **Poetiq's Metasystem** is a self-rewriting agent, along with the following approaches.

- **[Darwin Gödel Machine](https://arxiv.org/abs/2505.22954)** (Sakana AI). An agent that rewrites its own code, keeping an archive of variants and selecting improvements by performance on real coding benchmarks (SWE-bench, Polyglot). It's well to the right on the chart because the loop closes on the improver with empirical grounding, and cheap because the base model is frozen — only scaffold code changes. However the focus on coding tasks seems to limit its generality.
- **[MiniMax Self-Evolution — Harness](https://www.minimax.io/news/minimax-m27-en)** (MiniMax). A deployed model autonomously edits its own agent scaffold over many rounds, keeping or reverting changes based on internal evaluations. Right-of-center on the chart and cheap for the same reason as DGM (frozen model, scaffold-only edits), though its grounding is softer because some evaluation sets are self-built; the claim is vendor-reported.
- **[SICA](https://arxiv.org/abs/2504.15228)** (iGent AI). A self-improving coding agent that edits its entire codebase, selecting changes by a utility combining benchmark score, runtime, and cost. Genuine RSI (self-referential edits with execution-grounded benchmarks) and cheap (frozen base model), with the caveat that its design orients it toward coding tasks specifically.

### Lab-level R&D

These approaches rely on active human involvement in the improvement loop, making them less fully RSI than more automated systems. However, it is expected that human involvement can decrease over time, until the loops become more or less fully autonomous.

- **Tool-assisted R&D of AI tools** (Anthropic, Cursor, Cognition, …). Engineers use AI coding tools to build the next generation of AI systems, with humans and tests as the judges. It's left-of-center because the human team — not the AI — is the improver (closure is only partial), and cheap per step since the AI contribution is inference. (Category of products; representative examples: [Claude Code](https://www.anthropic.com/claude-code), [Cursor](https://cursor.com).)
- **[Claude Code → Claude](https://www.anthropic.com/institute/recursive-self-improvement)** (Anthropic). Anthropic's own disclosure that Claude now authors the majority of the code merged into its codebase, contributing to the pipeline that builds future Claude models. Partial, credit-confounded closure (humans still direct and review) with real productivity metrics, placed at the most expensive tier because the loop ultimately culminates in training a new model generation.
- **[Codex → GPT](https://openai.com/index/introducing-codex/)** (OpenAI). The analogous claim that OpenAI's Codex accelerates the engineering behind its own future models. Same placement rationale as Claude → Claude but rated lower on closure because the evidence is more anecdotal than documented, and at the top cost tier for the same model-generation reason.

### Infrastructure optimization

These approaches focus on making the expensive models cheaper and faster to train or run. They are only RSI if the optimized infrastructure is used to train the next iteration of the LLM that is driving the optimization loop. In that setting, they are expensive RSI, but some of these approaches can also be used for standard iterative optimization, in which case they may be quite cheap.

- **[Automated chip design](https://sequoiacap.com/article/partnering-with-ricursive-intelligence-a-premier-frontier-lab-pioneering-ai-for-chip-design/)** (Ricursive). A startup (from the AlphaChip team) building AI that designs and iteratively improves AI chips, aiming to close the hardware–software loop. Partial closure with empirically measured chip metrics, placed at the most expensive tier because each turn of the loop runs through silicon design and fabrication.
- **[AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)** (Google DeepMind). An evolutionary coding agent that discovers and optimizes algorithms verified by automated evaluators, including a kernel optimization that cut Gemini's training time by ~1%. Strongly grounded (verifiable metrics) with partial closure into the training stack, and placed as expensive because realizing the benefit flows through full LLM training.
- **Model-serving infrastructure optimization** (generic). AI- or search-driven tuning of inference/serving systems, judged by measured throughput and cost. Partial closure (it's an enabler, not a closed model loop) with empirical grounding, and middling cost because it's an optimization pass rather than a training run.

[^1]: https://www.anthropic.com/institute/recursive-self-improvement
[^2]: https://github.com/karpathy/autoresearch
[^3]: https://openai.com/index/built-to-benefit-everyone-our-plan/
[^4]: https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/

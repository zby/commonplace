---
source: https://jacobxli.com/blog/2026/machine-studying/
description: Introduces StudyBench and a compute-weighted definition of agent expertise, with preliminary tests of search, synthetic fine-tuning, continual pre-training, and corpus-generated notes.
captured: 2026-08-18
capture: web-fetch
genre: practitioner-report
type: kb/sources/types/snapshot.md
---

# Machine Studying

Authors: Jacob Xiaochen Li, Rick Battle, Omar Khattab
Source: https://jacobxli.com/blog/2026/machine-studying/
Date: June 17, 2026

### Contents

- [1. Studying converts a corpus into expertise](https://jacobxli.com/blog/2026/machine-studying/#1-studying-converts-a-corpus-into-expertise)
- [2. Can't the agent just search the corpus?](https://jacobxli.com/blog/2026/machine-studying/#2-can-t-the-agent-just-search-the-corpus)
- [3. Expertise is the efficiency of turning inference compute into accuracy](https://jacobxli.com/blog/2026/machine-studying/#3-expertise-is-the-efficiency-of-turning-inference-compute-into-accuracy)
- [4. StudyBench: can agents acquire expertise in novel domains?](https://jacobxli.com/blog/2026/machine-studying/#4-studybench-can-agents-acquire-expertise-in-novel-domains)
- [5. Equally capable models can have very different levels of expertise](https://jacobxli.com/blog/2026/machine-studying/#5-equally-capable-models-can-have-very-different-levels-of-expertise)
- [6. Three broad paradigms for studying](https://jacobxli.com/blog/2026/machine-studying/#6-three-broad-paradigms-for-studying)
- [7. Memorization is no substitute for expertise](https://jacobxli.com/blog/2026/machine-studying/#7-memorization-is-no-substitute-for-expertise)
- [8. Retrieval is no substitute for expertise either](https://jacobxli.com/blog/2026/machine-studying/#8-retrieval-is-no-substitute-for-expertise-either)
- [Epilogue](https://jacobxli.com/blog/2026/machine-studying/#epilogue)
- [Appendix](https://jacobxli.com/blog/2026/machine-studying/#appendix)

We increasingly need AI agents to work in domains they never saw during training, like using a new programming library or leveraging the emerging literature around a new disease. Such domains most naturally appear as a **corpus of documents**, like a textbook on a technical subject or the manual describing a new tool.

Faced with such a corpus, current agents overwhelmingly rely on inference compute and immediately reduce this problem either to “RAG” or to “long context”, and then simply rely on in-context learning, on [weight](https://arxiv.org/abs/2506.06266) updates [that](https://arxiv.org/abs/2512.23675) approximate [it](https://arxiv.org/abs/2602.16284), or on agentic search and [recursion](https://arxiv.org/abs/2512.24601) that scales it to longer contexts. If a domain is important enough, today’s best practice is to [hand-build an RL environment](https://arxiv.org/abs/2508.06813) (or buy one!) so agents can practice some relevant skills via trial and error. Across all of these, we can’t help but notice that our agents today engage with new domains in shallow, hand-engineered ways. **Humans can turn reading a textbook and actively thinking about the material into deep knowledge and even expertise. Why can’t agents yet?**

We call this problem **Machine Studying**. Given nothing but a corpus $\mathbf{D} = (d_1, \ldots, d_n)$, can AI systems autonomously develop *expertise* in the underlying domain? A studying algorithm is **whatever the agent does *to itself* using $\mathbf{D}$ before anything is known about downstream evaluation**. Studying may update the agent’s weights or anything in its harness. Importantly, machine studying is not definitionally about “internalizing a corpus into the weights”: almost every agent *will still have complete access to the corpus* at test time! The question is how much expertise it can develop in that corpus.

We start by defining **expertise**. An expert in a domain $\mathbf{D}$ is **an agent that can *efficiently* turn inference compute into accurate work**. A sharp novice might eventually pass an open-book exam through sheer brute force, but only an expert can produce high-quality answers with ease and go above and beyond with more time. Concretely, we measure expertise as the *weighted area* under the agent’s performance curve as inference compute grows. (This in turn gives us a notion of the **intelligence of an agent**: a smart agent can *quickly develop expertise* in a new subject. And by that token, it doesn’t appear that current agents are very smart yet.)

We instantiate this in **[StudyBench](https://huggingface.co/datasets/jacobli/studybench)**, a benchmark we’re building to investigate the ability of agents to study. We’ve barely scratched the surface at a tiny scale, but we want to share some preliminary ideas and findings in this short post. First, we find that equally “capable” frontier agents, equipped with the ability to search, can display a big gap in *expertise* on domains that rose in popularity between their training cutoffs. Second, we report on a subset of our attempts to adapt popular self-supervised or supervised methods for studying. We find that it’s non-trivial at best to get them to materially improve the expertise of *agents*, rather than raw models. Overall, we expect weight updates to become essential to deep studying (and we think we have a couple of [good ideas](https://noahziems.com/pedagogical-rl) toward this), but we’re skeptical that approximating long-context attention is the right objective.

We are sharing ideas and data early in our project because machine studying is currently a central and unrecognized bottleneck for downstream AI success. “Continual learning” is widely discussed right now, but mostly with interpretations like improving [on the job](https://www.dwarkesh.com/p/timelines-june-2025) and [across sessions](https://www.letta.com/blog/continual-learning), avoiding [catastrophic forgetting](https://arxiv.org/abs/2302.00487) while [learning a stream of new tasks](https://arxiv.org/abs/2606.05661), or indeed just [better context management](https://www.interconnects.ai/p/contra-dwarkesh-on-continual-learning). StudyBench is our attempt to create a concrete hill for us all to climb toward **agents that develop expertise in new domains from nothing but a corpus**.

## 1. Studying converts a corpus into expertise

After pre-training and post-training are over, people and organizations expect their agents to work with new libraries, build on new research papers, and operate over private corpora that weren’t available to the agent at training time.

Humans face this problem of learning new domains all the time, and one of our default answers is *studying*. Before an exam, even an open-book one, we read the textbook or the literature, think out loud, quiz ourselves, and write our own notes. This preparation tends to pay off even if we don’t have access to a distribution of “exam” questions. Hands-on practice via trial and error using, say, past exams à la RL is usually a small fraction of the effort. Most of the expertise comes from the active effort of reading and thinking itself.

We want the same capacity for AI agents. Given a corpus $\mathbf{D}$ of documents that together define some domain, with no additional information like question–answer pairs or a reward function, an intelligent agent should be able to study $\mathbf{D}$ to build a deep understanding of the domain. An agent here is just a model and a harness, $\Sigma = (\mathbf{M}, \mathbf{H})$, and a studying algorithm may change the weights or the agent’s prompts, tools, or the indexes and notes it maintains in the environment. Crucially, the corpus remains part of the world at test time: the agent can still use it, but effective studying should make such usage much more targeted and efficient.

In a way, Machine Learning asks how a system can improve from data when we have a precise objective to optimize. **Machine Studying asks what an agent should do when it’s given a declarative corpus and no downstream task.** Of course, this requires pre-trained agents that have accurate priors about the world. The agent may pose its own questions and rubrics while it studies, much like a student quizzing themselves, but it can’t assume that we’ll tell it much about the task distribution or the reward that will eventually score it.

## 2. Can’t the agent just search the corpus?

With current agents and the rise of inference-time compute scaling, the most tempting approach today is to skip preparation entirely. Agents can grep, read files, and run code at test time, so why not just spend more inference tokens per question? But this conflates having access to the corpus with developing deep expertise: you wouldn’t hire any of us as a lawyer just because we can Google the legal literature very intelligently. At minimum, what makes a lawyer a *good* lawyer is knowing what to look for, where to look, and what to do with a passage after they find it.

You could say that reasoning and search are [not separable from knowledge](https://x.com/lateinteraction/status/1909011076605518124). An agent deciding what to grep for or which file to open is acting from its current weights, and those weights may actively conflict with the world encoded in the corpus. Figure 1 shows a funny example: We asked Sonnet 4.6 to give us a code snippet for loading `Qwen 3.6`, a model released after Sonnet was trained. But it had such strong priors that it did not search for `Qwen 3.6` and instead decided our prompt was inaccurate and searched for `Qwen3 0.6B` instead.

 ![](https://jacobxli.com/assets/img/posts/machine_study/sonnet-qwen-search.png) **Figure 1.**Asked for code that loads

`Qwen 3.6`, a model released after its training cutoff,

`Sonnet 4.6`decides the name must be a typo and quietly searches for

`Qwen3 0.6B`instead.

An agent that has studied a new domain searches less and gets more from each search, since it knows what the corpus contains, which of its own priors to *distrust*, and which abstractions even exist to be asked about.

## 3. Expertise: the efficiency of converting compute into accuracy

Most benchmarks report accuracy at whatever inference budget the agent happened to spend. More recently, there has been a [growing](https://aclanthology.org/2023.findings-acl.738.pdf) push to [report](https://aclanthology.org/anthology-files/anthology-files/pdf/findings/2025.findings-emnlp.1172.pdf) quality [across inference compute levels](https://x.com/polynoamial/status/2064210146558136827).

In machine studying, this **tradeoff between quality and cost** is the precise quantity we’re trying to measure. We’re not interested in the agents’ capability on a given task per se, but rather in their ability to *quickly develop expertise* in new domains. After all, if a use case is popular enough, the next model generation will probably nail it out of the box, but there are always new domains during deployment.

To understand this emphasis on the tradeoff between quality and cost, observe that since the corpus is always available at test time, even a novice agent could in principle *study during the exam*, say by rereading every relevant file before each answer, and maybe do arbitrarily well with enough time. To borrow some intuitions from scaling laws, what a studying algorithm promises is a shift of the entire quality/cost curve, as in higher accuracy at the same budget or the same accuracy at a smaller budget.

That said, whole curves are awkward to compare directly. It’d be nice if we could, at the end of the day, quantify “expertise” as one number. Indeed, in many cases, two curves will converge or even cross, and whether the crossing makes the rising line “better” than the other depends on what inference budgets are practical. Thus, in machine studying we think you should typically decide how quickly expensive budgets should be *discounted* (i.e., given less weight), and once you’ve done that, reduce each curve to its weighted area. We call the weighted area **expertise**:

\[\text{Expertise} = \int \text{performance at an inference budget} \times \text{importance of that budget}\]

An agent that becomes accurate only after extensive search can reach peak performance, but we’d say that it has low expertise in that domain. Writing $\mathcal{E}(\Sigma; \mathbf{D})$ for this weighted area, we also get the success criterion for studying. A studying algorithm $\pi$ maps an agent and a corpus to a new agent, and it works if

\[\mathcal{E}\big(\pi(\Sigma, \mathbf{D});\, \mathbf{D}\big) \;>\; \mathcal{E}\big(\Sigma;\, \mathbf{D}\big),\]

Expertise = Performance vs. Inference Compute

illustrative curves · number after each = expertise (weighted area, emphasizing cheaper budgets)

inference compute (tokens, log scale)

**Figure 2.**Illustrative performance vs. inference-compute curves that define expertise.

Figure 2 shows four idealized agents: one ordinary capable but non-expert agent, a cramming agent that has studied the corpus but only in a “shallow” way, a brute-force harness, and our idealized expert. The ordinary curve rises gradually and slowly as compute grows. The expert curve sits above it and to its left, better at nearly every budget. The cramming curve starts high, because the shallow studier memorized material without understanding it, and then flattens. For it, extra time with the open book buys it little, and we will meet this shape empirically below when we train models on synthetic questions. The brute-force harness, the one that basically studies during the exam, eventually reaches the top, but only at budgets that should be extremely discounted.

NoteHow we compute expertise

Expertise is a weighted average of performance over log-compute,

$$\mathcal{E}(\Sigma; \mathbf{D}) = \int p_{\Sigma,\mathbf{D}}(x)\, w(x)\, dx, \qquad w(x) \geq 0, \quad \int w(x)\, dx = 1,$$

where $p_{\Sigma,\mathbf{D}}(x)$ is the performance of agent $\Sigma$ on domain $\mathbf{D}$ at position $x$ of a log-token axis. The weight $w$ indicates the relative importance of each budget. Normalizing $w$ ensures that expertise is measured on the same scale as performance. In this post, $x=0$ corresponds to $3\text{k}$ generated tokens, which is typically the minimum required for a modern reasoning model to read a question and provide a complete answer. Each increment of $+1$ represents a tenfold increase in tokens. We use the exponential decay $w(x) = (\ln 10)\, 10^{-x}$, so each doubling of compute halves the budget's weight.

In practice, we evaluate a limited set of budgets and interpret $p_{\Sigma,\mathbf{D}}(x)$ as the best score the agent achieves using at most $x$ tokens. For budgets below the first measured point, the score defaults to the minimum (zero or chance for multiple-choice), reflecting the assumption that the agent simply cannot answer with fewer tokens. An agent capable of doing so would access the most heavily weighted region. Beyond the last measured budget, we carry the final score forward indefinitely, as tail holds little weight anyway.

As a worked example, budgets of $5\text{k}, 10\text{k}, 20\text{k}, 100\text{k}$ tokens with scores of $10\%, 20\%, 30\%, 40\%$ have corresponding weights of $0.30, 0.15, 0.12, 0.03$, resulting in $\widehat{\mathcal{E}} \approx 10.8\%$. These weights sum to $0.60$ instead of $1$. The remaining $0.40$ is assigned to the region below $5\text{k}$ tokens, where the score is zero. Therefore, even an agent that performs perfectly at all measured budgets cannot exceed $60\%$. This gap reflects the cost of not being able to answer with fewer tokens. The figure below illustrates this computation.

Where the Weight Lives

 3k 10k 100k 1M 3k–5k floored → 0 weight w(x) inference compute (tokens, log) Importance halves every 2× compute (÷2 per doubling), so it crowds the cheap end — but for this system the 3k–5k block is floored to 0, so that weight is wasted.

The Expertise Rectangles

 100 50 0 5k 10k 20k 100k floored block 3k–5k, scores 0 shaded area = expertise = 10.8% bar width = weight (importance) · sums to 1 Each measured budget is a rectangle:

*width*= its weight,

*height*= its score. The shaded staircase is the expertise score. The floored block (3k–5k, ≈40% of the weight) sits at zero height, so it adds nothing.

Defining expertise as a scalar computed in this way allows us to define **studying intelligence**. For the purposes of machine studying, an intelligent agent is one that can *quickly acquire expertise* in totally new domains. This is nothing but a curve that results from plotting *expertise* against *studying compute* for a given agent with a particular studying algorithm. Plotting this requires training runs at many study budgets, which is outside the scope of this post, but raising the intelligence of our agents is really the ultimate goal here.

NoteThe notion of studying intelligence

For each amount of study compute, we first plot the agent's full performance curve and reduce it to an expertise score, then read expertise as a function of study compute. The weighted area under this second curve, with the same construction one level up, is the (studying) intelligence:

$$\text{Intelligence} = \int \text{expertise after a study budget} \times \text{importance of that budget}.$$

Intelligence = Expertise vs. Study Compute

illustrative curves · number after each = intelligence (weighted area, emphasizing cheaper study)

study compute (tokens, log scale)

Illustrative expertise vs. study-compute curves that define intelligence.

Different studying algorithms spend compute in very different ways. The studying algorithm we'd love to arrive at as a field is one that rises early and keeps rising in its ability to deliver expertise.

## 4. StudyBench: can agents acquire expertise in novel domains?

We’re actively developing **[StudyBench](https://huggingface.co/datasets/jacobli/studybench)** in public so that we and others can begin to investigate and develop the ability of agents to study.

Currently, StudyBench consists of three tasks. Each is built on a corpus that defines a domain of expertise, and each pairs the corpus with a *hidden* exam. The agent may study the corpus however it likes, but there’s no RL environment, distribution of prompts, or a given reward function.

We chose three corpora in the current version of StudyBench to stress and contrast different challenges of studying. First, **Studying-DSPy** contains a corpus that represents a [programming library](https://dspy.ai) that recent models have deceptively OK knowledge of an *outdated* version of, which is actually a rather dangerous state. It tests whether studying can help agents correct stale knowledge about a subject, and also serves as a control to some degree. Second, **Studying-OpenClaw** presents a corpus around an [artifact](https://openclaw.ai/) that models in our experiments have never seen during training. It tests studying from scratch in a rather novel setting that’s hard to reduce to other familiar domains. Lastly, **Studying-Literature** builds a corpus out of recent machine learning papers and thus tests studying at a scale that vastly exceeds the context window of any existing language model.

### Studying-DSPy

DSPy is a framework for programming language models, where pipelines are written as composable Python modules with typed signatures. Though it’s been around since Dec 2022, its popularity increased rapidly after 2024. Because of that, many recent models know of it, but their knowledge is partial and often more than a few versions behind. The corpus is the codebase and its tests. The target “expert” for the purposes of machine studying is a developer who can take a user’s question or goal and address it correctly in an up-to-date manner.

The exam is 30 coding questions, which we produced semi-automatically under a substantial amount of information asymmetry and expert human oversight. The writer is GPT-5.4 in Codex at `xhigh` effort, a model that already knows DSPy quite well, and it receives privileged material the test taker wouldn’t get: the full documentation (not just the code), a pool of real DSPy user questions, and extensive human oversight, including in the form of deterministic checkers and a critique loop. It’s also given the advantage of compute asymmetry, whereby some questions take up to an hour to produce. In contrast, the test taker receives the codebase and basic tools, and a much smaller budget than running GPT-5.4 on `xhigh` for an hour.

Answers are graded against weighted rubrics, with deterministic checks for compilation and hallucinated APIs. A lenient variant of the grader skips checks that grant automatic zeros, so that we can begin to compare small models.

DSPytool-use metric for a ReAct agentI've got a `dspy.ReAct` agent that answers arithmetic word problems and is given a Python `add` function as a tool. I want an evaluation harness that gives an example credit ONLY when the final answer is correct AND the agent genuinely used the calculator to get there. The reason I care: some of these agents just blurt out the right number and immediately finish without ever calling the tool, and those runs must score zero — a correct answer alone is not enough.

My current metric pulls the tool calls off the prediction (I look at `pred.tool_calls` like I would with native function-calling / `dspy.ToolCalls`) and checks whether `add` is among them, but it never awards credit — even on runs where I can see from the logs that the agent clearly did call `add`. So my whole devset scores 0%. Give me a small, runnable harness (devset of a couple of arithmetic examples, a custom metric, and a run over the devset that prints an overall percentage plus per-example scores) that scores this correctly. Use `DummyLM` so it runs offline with no API key.

Rubric 4 checks · show ↓4 checks · hide ↑| id | type | weight | what it checks |
| --- | --- | --- | --- |
| 1 | core | **70** | Metric gives credit only if the answer matches **and** the agent used the tool, detected by scanning `pred.trajectory` for a `tool_name_*` whose value is `'add'`. Must **not** read `pred.tool_calls` (ReAct never populates it), and must **not** pass on a finish-only trajectory. |
| 2 | core | 10 | The program is a `dspy.ReAct(..., tools=[add])`, so predictions carry `trajectory` (not an OpenAI-style `tool_calls`). |
| 3 | core | 12 | Runs `dspy.evaluate.Evaluate` over a devset of `dspy.Example(...).with_inputs('question')`. |
| 4 | supp | 8 | Reads per-example scores from `result.results` and the overall from `result.score`. |

### Studying-OpenClaw

OpenClaw is an open-source framework for self-hosted personal AI assistants, released at the end of last year, which makes it beyond the training cutoff of most models in our experiments. Whatever the agent knows about OpenClaw at exam time, it had to learn directly from the corpus we supply, which contains the codebase with its scheduling, model-routing, and configuration machinery, along with the conventions its maintainers follow. An “expert” for the purposes of machine studying is an operator who can configure and extend the framework the way its maintainers intended, and who knows, for instance, how the codebase distinguishes a setting that was deliberately cleared from one that was never set.

The exam is 20 questions produced by the same pipeline as DSPy’s, seeded in this case from GitHub issues, since issues record the problems real operators hit.

OpenClawper-job model-fallback resolverI've got a set of isolated cron jobs, each scheduled independently. Most should use my usual model-fallback chain, but a couple of high-priority jobs I want to pin to a single model with no fallbacks at all — if that model is down, just fail rather than silently drift onto a cheaper backup. So on those jobs I cleared out the fallback list (saved it as an empty list on the job) and left the rest untouched.

My understanding of how the per-job resolution is supposed to work: if a job doesn't carry its own fallback list, it inherits the agent's configured fallbacks; if it does carry one, we use that. Since "empty" is the natural way to express "no list here," I expected the empty-list jobs to behave like the unpinned ones and just inherit — but I actually want the opposite for them, and I'm second-guessing whether clearing the list is even the right signal. Write the per-job resolver that produces the effective fallback chain for one of these scheduled jobs, so that a job which deliberately specifies "no backups" is honored as exactly that, while jobs that simply never set a list keep getting the normal agent-level chain. Match how the rest of this codebase already distinguishes those two states.

Rubric 5 checks · show ↓5 checks · hide ↑| id | type | weight | what it checks |
| --- | --- | --- | --- |
| 1 | core | **42** | *(outcome)* An explicit **empty** `fallbacks` array → returned as-is ("no backups"); only a truly **absent** (`undefined`) list inherits. Must not collapse `[]` into "unset" via `.length` / `\|\|` / truthiness. |
| 2 | core | 28 | *(mechanism)* Decide unset-vs-set by **array presence** — `Array.isArray(...)` (or `=== undefined`) + `??` fallthrough, so `[]` survives as a real value. |
| 3 | core | 15 | When absent, inherit by calling the repo's real `resolveEffectiveModelFallbacks({cfg, agentId})` — not a hand-rolled default. |
| 4 | supp | 9 | Returns the job's own non-empty `payload.fallbacks` verbatim when `kind === "agentTurn"`. |
| 5 | supp | 6 | Derives `hasSessionModelOverride` from a non-empty trimmed `payload.model`; gates on `kind === "agentTurn"`. |

### Studying-Literature

The third corpus consists of a large fraction of the recent machine learning literature, around 50k full-text papers from ICLR, CVPR, ICML, and NeurIPS between 2018 and 2025. It vastly exceeds any language model’s context window and, though a lot of it *is* in the training data of all models we test, no training cutoff can keep up with its most recent papers (at least not on a rolling basis!). Because it has dates, we can begin to ask questions about how expertise varies over time, and whether there’s still large headroom, as we suspect there is, for careful studying of material that was even aggressively upsampled during training. Here, an expert is a researcher who knows the field’s structure well enough to survey any corner of it on demand.

Our hidden exam takes target papers from ICLR 2026 and asks the agent to write a review of its related work from each target’s title and abstract. The agent queries the corpus through BM25 for up to 20 turns, with up to 20 papers returned per query, then selects 100 papers and writes the review. We score the selection against the papers each target paper actually cites, and against a must-cite set built with the labeling procedure from [MasterSet](https://arxiv.org/abs/2604.17680). Both of these constitute privileged information that the test-taking agent does not see. Since the targets from ICLR 2026 are subsequent in time to the training cutoff of every model in our experiments, the task also measures the degree to which search compensates for lack of studying.

Lit Reviewrelated-work section for a 2026 ICLR paperObjectivesystem prompt · show ↓system prompt · hide ↑Write the related-work / literature-review section of an academic paper. Be comprehensive — surface the full picture of prior work that would realistically be cited for this paper. Don't stop at "papers on a similar topic." Also recover:

- baselines the paper would naturally compare against
- datasets / benchmarks the paper would evaluate on
- methods the paper builds on or extends
- foundational work the paper inherits ideas from

Cast a wide net: call the search tool multiple times with different aspects of the target paper — the topic, the method, the task, the dataset name, the model family, etc. — to surface a broad set of prior work before writing.

**Target paper.** *BioX-Bridge: Model Bridging for Unsupervised Cross-Modal Knowledge Transfer across Biosignals*

Biosignals offer valuable insights into the physiological states of the human body. Although biosignal modalities differ in functionality, signal fidelity, sensor comfort, and cost, they are often intercorrelated, reflecting the holistic and interconnected nature of human physiology. This opens up the possibility of performing the same tasks using alternative biosignal modalities, thereby improving the accessibility, usability, and adaptability of health monitoring systems. However, the limited availability of large labeled datasets presents challenges for training models tailored to specific tasks and modalities of interest. Unsupervised cross-modal knowledge transfer offers a promising solution by leveraging knowledge from an existing modality to support model training for a new modality. Existing methods are typically based on knowledge distillation, which requires running a teacher model alongside student model training, resulting in high computational and memory overhead. This challenge is further exacerbated by the recent development of foundation models that demonstrate superior performance and generalization across tasks at the cost of large model sizes. To this end, we explore a new framework for unsupervised cross-modal knowledge transfer of biosignals by training a lightweight bridge network to align the intermediate representations and enable information flow between foundation models and across modalities. Specifically, we introduce an efficient strategy for selecting alignment positions where the bridge should be constructed, along with a flexible prototype network as the bridge architecture. Extensive experiments across multiple biosignal modalities, tasks, and datasets show that BioX-Bridge reduces the number of trainable parameters by 88–99% while maintaining or even improving transfer performance compared to state-of-the-art methods.

Must-cite14 papers · show ↓14 papers · hide ↑| # | title |
| --- | --- |
| 1 | BioBridge: Bridging biomedical foundation models via knowledge graphs |
| 2 | ECG-FM: An open electrocardiogram foundation model |
| 3 | PaPaGei: Open foundation models for optical physiological signals |
| 4 | Toward foundation model for multivariate wearable sensing of physiological signals |
| 5 | Large brain model for learning generic representations with tremendous EEG data |
| 6 | Brant-X: A unified physiological signal alignment framework |
| 7 | Modality distillation with multiple stream networks for action recognition |
| 8 | Multimodal knowledge expansion |
| 9 | Contrastive representation distillation |
| 10 | Relative representations enable zero-shot latent space communication |
| 11 | Revisiting model stitching to compare neural representations |
| 12 | Similarity of neural network representations revisited |
| 13 | Similarity and matching of neural network representations |
| 14 | Understanding intermediate layers using linear classifier probes |

## 5. Equally capable models can have very different levels of expertise

Every agent in our evaluations is a model inside a ReAct harness, with three simple tools: `grep`, `glob`, and `read_file`. We vary the inference budget across four settings. Either the model can answer directly with no tools, loop up to 5 or up to 20 tool iterations and stop when it thinks it’s done, or be forced through exactly 20 iterations. Each budget gives us one point on the agent’s quality/cost curve, and we compute expertise from those four points.

Before we test any studying algorithms of our own, let us look at the brute-force studying approach that frontier labs implicitly run. When a new library or topic becomes important, labs include data for it in the next pre-training and/or post-training cycles, and the next model is trained such that it “just knows” the new material. In our terms, *re-training* is a studying algorithm, probably the most reliable one currently but certainly also the most expensive one by far. To try to get a sense of what it achieves, we can compare two equally *capable* models that nonetheless have different knowledge cutoffs. If our framing is right, the newer model should do better on corpora that became popular between the two cutoffs, and neither model should have as big of an advantage on corpora that appeared after both.

We identify GPT-5.1 and GPT-5.4-mini as a pair of models with these properties. Basically, GPT-5.4-mini has a substantially more recent knowledge cutoff but, partly due to the size difference, it’s not strictly more capable than GPT-5.1. The two are close in general capability and, in fact, on agentic benchmarks such as tau2-telecom, the older GPT-5.1 is slightly ahead. Thus, it would be a good test of our hypotheses to see whether the smaller GPT-5.4-mini is noticeably *better* on certain corpora and weaker on others based on hypothesized expertise.

Figure 3 shows what happens on our StudyBench exams. On DSPy, which grew popular after 2024, the newer GPT-5.4-mini wins at every inference budget. On OpenClaw, which postdates both cutoffs, its advantage disappears, and both models stay barely above 10% however long they search. It’s not a particularly wise idea to draw much more than this from a shallow comparison of two closed models, but we think this is consistent with the fact that the newer model simply knows more DSPy due to being trained more recently, and it’s useful to see that searching the codebase for a little longer does not automatically let the older model flip this.

Accuracy by Setting

DSPy

accuracy (%)

DSPy: gpt5.1 0, 12.7, 10.8, 29.8. gpt5.4 mini 0, 26.8, 34.2, 39.7.

max ReAct iterations

OpenClaw

accuracy (%)

OpenClaw: gpt5.1 0, 5, 5, 10. gpt5.4 mini 0, 8.3, 9.7, 9.7.

max ReAct iterations

gpt5.1gpt5.4 mini|no early exit @ 20**Figure 3.**GPT-5.1 vs. GPT-5.4-mini accuracy on DSPy and OpenClaw across ReAct inference budgets (strict grading).

In our runs, GPT-5.1 fails the deterministic API checks for using DSPy far more often than GPT-5.4-mini. In fact, it appeared to be hallucinating APIs that do not exist in the library. On closer inspection, we found that GPT-5.1 was calling APIs that *did* exist in 2024 but were since deprecated! This is the stale knowledge that we built the DSPy task to expose (and it is pretty much the same failure model by the Claude model from Figure 1). When we read the failing trajectories more broadly, the agents usually land on a plausible solution early and then engineer around it, where a repository “expert” would have either known a better solution or had a better idea of when to keep searching.

For the studying experiments in Section 6 below, we use Qwen3.5-9B, which is a model that’s small enough to train and probe many times within our budget but is also close to what machine studying algorithms might serve in practice, since a team that wants a private expert would likely run models it can afford to fine-tune. Importantly, as small as it is, Qwen3.5-9B is a very *competent* model: it has no trouble, say, writing good Python or good PyTorch. Its bottlenecks, if any, are not around capability but will be primarily around familiarity with the downstream domain and the ability to develop expertise (i.e., to study) in a new domain.

Figure 4 shows its scores out of the box across our four budgets, before any form of studying just yet. Interestingly, even though DSPy is a small library with a deliberately small API surface, the Qwen3.5-9B agent (without studying) fails on it anyway. The strict scores are very low at this size, so we additionally report a *lenient* grading that skips the automatic zeros and scores answers against the rubric alone.

Qwen3.5-9B Accuracy

DSPy

accuracy (%)

DSPy Qwen: lenient×W 3.3, 9.0, 11.6, 28.0; strict×CC 0.0, 0.0, 2.0, 0.8.

max ReAct iterations

OpenClaw

accuracy (%)

OpenClaw Qwen: lenient×W 2.3, 6.9, 15.8, 17.6; strict×CC 0.0, 0.0, 6.6, 6.4.

max ReAct iterations

lenient gradingstrict grading|no early exit @ 20**Figure 4.**Qwen3.5-9B accuracy across inference budgets under strict and lenient grading.

It’s useful to keep in mind just how large the headroom on a task like this is. Every question has a human-verified answer recoverable from the corpus, and indeed stronger models, as we’ve seen, have no trouble scoring much higher. When we simply force the agent to search for the full 20 iterations, its *lenient* DSPy score roughly triples, from 9.6 to 29.4, so the evidence it needed was reachable all along if the agent could know enough about the domain to at least be inclined to continue searching.

## 6. Three broad paradigms for studying

We’ve argued that machine studying is an under-recognized problem formulation: it’s often reduced to other problems like RAG (equating studying with *encoding* and *indexing* for retrieval), long context (equating studying with, say, attention), or RL (presupposing that there’s a known distribution of initial states and a reward function), and until now we lacked a crisp goal (improve *expertise* and *studying intelligence*) and a benchmark.

**Despite this, there *are* many, many methods from neighboring problems that naturally apply in this space. Overall, almost all of them make one of three bets.** For example, there is already a rich emerging literature on internalizing a corpus into model weights. Unfortunately, nearly all of it assumes that the ceiling is the model with the corpus in its context window, and that our job here is just to approximate that model more cheaply. Nonetheless, all of these grant us baseline studying algorithms, though we need to rid them of the assumption that we’re about to lose access to the corpus (and tool use broadly) at test time.

### Self-supervised objectives

A natural first bet is that studying reduces to some **self-supervised ML objective**. For example, we can pick a loss defined by the corpus itself, like next-token prediction over [the corpus text](https://arxiv.org/abs/2004.10964), applying [test-time training](https://arxiv.org/abs/2512.23675) to compress the corpus itself into the model weights at test time, or even [compacting KV caches](https://arxiv.org/abs/2602.16284) to match attention.

We experimented with a few techniques from this family in preliminary runs. In this initial blog, we report on the simplest instantiation of this bet, i.e., **continual pre-training**, in which we update the weights of the model, in particular training LoRA adapters, for a next-token prediction (NTP) objective over the raw corpus. For Studying-DSPy, we test two variants, `CPT(code)` over the DSPy codebase (459k tokens) and `CPT(doc)` over its documentation (160k tokens). For Studying-OpenClaw, we run only the `CPT(code)` variant. It is known that training a post-trained model on raw text can [degrade](https://thinkingmachines.ai/blog/on-policy-distillation/) the abilities it gained in post-training, like instruction following, so we also mix in self-sampled coding traces as an anchor.

Overall, what’s nice about this kind of approach is that it’s rather universal: for better and for worse, it appears to encode only limited biases about the domain being studied, and its NTP objective at least tries to directly teach the model about every part of the corpus.

### Synthetic data and environments

A second natural bet is that studying needs the models to **synthesize their own training data**. Often, the idea here is that the corpus $\mathbf{D}$ does not contain enough redundancy and is not sufficiently task-oriented. Models may instead produce their own [entity-rich retellings](https://arxiv.org/abs/2409.07431) of the contents, [synthetic questions and answers](https://arxiv.org/abs/2506.06266), arbitrary [active reading strategies](https://arxiv.org/abs/2508.09494) for each document, or even meta-learn how to produce their own [self-edits](https://arxiv.org/abs/2506.10943) about what they read (though this will require a hill to climb, which here must thus be synthesized too).

These efforts will then supervise the model with this resulting training set. In doing so, the literature assumes, in effect, that the corpus is about to disappear at test time for some reason. In practice, our agents will still have the freedom to use tools and read content from the corpus at test time. The real challenge has little to do with internalizing the corpus and more to do with developing expertise.

We’ve tried multiple approaches here in our preliminary runs, and one of the painfully recurring experiences was always the difficulty or the serious inefficiency of scaling them. (Recall that we define studying intelligence as the efficiency of studying.) In this initial blog, we report on the simplest instantiation of this bet, i.e., **synthetic fine-tuning**, which turns the corpus into SFT practice. We (cheated a bit and) used a larger model, DeepSeek-V4-Flash, to read the codebase and write question–answer pairs, which we (cheated again and) audited a bit to keep their quality high. In a true machine studying algorithm, the agent should independently study without access to steering from larger models or a human. The agent trains on those pairs in a supervised manner with reasoning turned off. A recovery stage of on-policy distillation over a roughly 60K-example mixture, following the [Thinking Machines Lab recipe](https://thinkingmachines.ai/blog/on-policy-distillation/), then restores its general behavior.

A natural extension of the research in this space is to go beyond supervised learning and turn the synthesized questions into material for, say, on-policy reinforcement learning with self-synthesized environments. In particular, if the agent can write its own questions and rubrics from the corpus and judge its own rollouts, we can use that as a reward, and we could even begin to encourage expertise by rewarding cheaper rollouts.

Given enough study compute, doing that may well be the most powerful approach available, though (i) unlike in-domain RL it remains unclear if the synthesized environments will align with the unseen task and rewards and (ii) it’s really not obvious whether on-policy RL can, at reasonable efficiency, teach the model *lots of new domain knowledge*. RL is usually used to teach models new *skills* in the environment (e.g., how to use new tools to navigate the DSPy repo), but will it allow the agent to develop a lot of expertise in the difference between DSPy optimizers? [Pedagogical RL](https://noahziems.com/pedagogical-rl) is one natural choice in this setting, since it guides *sampling* with privileged information. We’re currently beginning to investigate these directions.

### Amortized context management

The third natural bet is to skip the weight updates entirely and let **agents manage notes** in their prompt or their environment about the corpus, as people already do by hand in `skill.md` files and as agents have begun doing for themselves, albeit not for developing agent expertise from a corpus per se: [accumulating strategies](https://arxiv.org/abs/2504.07952) across attempts, [thinking offline](https://arxiv.org/abs/2504.13171) before any query arrives, giving itself a [persistent peek](https://arxiv.org/abs/2605.19932) into the external context, or even compiling their documents into [a wiki they maintain](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

In this initial blog, we report on the simplest instantiation of this bet, i.e., **writing a cheatsheet**, in which the agent explores the repository with the same three tools for dozens of steps and writes itself a note, which is then prepended to every future question. This is a very simple approach that won’t change the weights, but it’s an essential baseline to compare against approaches that do. (To be clear, there’s no reason why [combining](https://arxiv.org/abs/2605.12484) such context management approaches with weight updates would make them [better together](https://arxiv.org/abs/2407.10930).)

## 7. Memorization is no substitute for expertise

We can now let our Qwen3.5-9B agent study. Recall that a studying algorithm takes in as input nothing but the corpus $\mathbf{D}$ and updates the model or the harness or both. In doing so, its goal is to allow the agent to perform well in expectation on whatever downstream tasks arise around the domain described by $\mathbf{D}$.

We report on perhaps the simplest instantiation of three major classes of approaches that correspond to the bets above. The goal of this very early blog is *not* to exhaustively test or scale every method. Instead, our goal is to begin to understand how standard ideas, ones assumed to work in seemingly similar settings, fare at developing agent *expertise* in new domains.

Qwen3.5-9B — Studied Variants vs Original

DSPy

accuracy (%)

DSPy Qwen. Lenient: original 3.3/9.0/11.6 (forced 28.0); SFT + OPSD 9.4/7.4/8.5 (forced 21.0); CPT(code) 5.1/7.4/7.0 (forced 14.3); CPT(doc) 3.8/7.2/6.2 (forced 14.6). Strict: original 0.0/0.0/2.0 (forced 0.8); SFT + OPSD 1.1/0.0/0.0 (forced 2.2); CPT(code) 0.8/0.9/1.0; CPT(doc) 0/0/0.

max ReAct iterations

OpenClaw

accuracy (%)

OpenClaw Qwen. Lenient: original 2.3/6.9/15.8 (forced 17.6); CPT(code) 2.2/8.8/15.3 (forced 14.1). Strict: original 0.0/0.0/6.6 (forced 6.4); CPT(code) 0.0/4.5/6.7 (forced 6.3).

max ReAct iterations

originalSFT + OPSDCPT(code)CPT(doc)|lenientstrict|no early exit, lenientno early exit, strict**Figure 5.**Qwen3.5-9B studied variants (continual pre-training; synthetic SFT + on-policy distillation) versus the original model.

Figure 5 shows the agents that studied via weight updates against the original. Both continual pre-training variants sit slightly below it at every budget. In other words, next-token prediction over the corpus did not turn exposure into expertise. Synthetic fine-tuning is more interesting. It raises accuracy substantially when the model answers in a closed-book setting, which is exactly what training on question-answer pairs is supposed to do, but the gain does not grow when the agent is allowed to search. Training also had a side effect: it made the model far more verbose, so its cheapest gradeable answer now costs roughly 9k tokens where the base needed 4k ([per-budget table](https://jacobxli.com/blog/2026/machine-studying/#per-budget-scores-and-tokens)). A better intercept but no better slope. Because of this, as we’ll see below, the higher cost per answer add up to *less expertise* overall than no studying at all!

In other words, you could say that the SFT’d agent “crammed”, exactly like the shallow studier we sketched in Section 3. Methods in this family, including context distillation and its recent descendants, implicitly target memorization: after training, the corpus should essentially end up inside the weights, recallable without the book. That target could sometimes be the right one, like if the task is closed-book by construction, or the corpus is small enough to drill exhaustively, though even then methods in this regime seem to need many synthetic questions *per corpus token* to succeed. Our run spends one question per seventeen tokens, which is on the lower end and is more consistent with the goals of efficient studying. But even at high density, the objective would sit oddly for the purposes of agent expertise, because the corpus is always available at test time so purely internalizing it is not quite the right goal.

**Expertise** (lenient WAUC):

|  | Studying-DSPy | Studying-OpenClaw |
| --- | --- | --- |
| Qwen3.5-9B (base) | 6.49 | 7.64 |
| SFT + OPSD | 3.29 | — |
| CPT(code) | 3.71 | 7.82 |
| CPT(doc) | 3.92 | — |
| + cheatsheet | **9.65** | **8.18** |

In our preliminary runs here, the cheatsheet is the only procedure that ends up developing noticeable expertise in one of the the two domains.

Figure 6 below shows the cheatsheet runs. On Studying-DSPy, the gains from the cheatsheet are concentrated at the low inference budgets. That’s arguably where a studying algorithm should help first: the cheatsheet note hands the agent a map of the repository that it would otherwise rebuild from scratch on every question. At the forced 20-iteration budget, the unmodified agent catches up, since enough search eventually recovers what the note knew (studying by cramming together a cheatsheet is *still* a very shallow mechanism, after all!). We do not believe a cheatsheet is the final form of studying, and indeed we don’t see the same effects on Studying-OpenClaw.

Overall, it’s likely the case that you have to combine all three bets (self-supervision, synthetic environments, and amortized context management), but at this point we’re able to express our skepticism that approximating long-context attention is fundamentally the right objective by itself for developing agent expertise.

Score vs Generation Tokens / Question — Qwen3.5-9B

Switch to log scaleDSPy

score

DSPy. base: direct 4.1k/3.3, k=5 7.9k/8.6, k=20 8.6k/9.6, k=20 NER 34.6k/29.4. cheatsheet: direct 3.9k/6.3, k=5 6.1k/14.4, k=20 7.1k/14.1, k=20 NER 29.9k/23.1.

generation tokens / question

OpenClaw

score

OpenClaw. base: direct 4.1k/2.3, k=5 4.6k/6.9, k=20 9.7k/15.9, k=20 NER 24.3k/17.6. cheatsheet: direct 3.8k/4.3, k=5 6.0k/8.6, k=20 9.1k/15.2, k=20 NER 20.1k/18.1.

generation tokens / question

Qwen3.5-9BQwen3.5-9B + cheatsheet**Figure 6.**Cheatsheet baseline — score vs. generation tokens per question for Qwen3.5-9B, base versus cheatsheet, on DSPy and OpenClaw. Points: direct, k=5, k=20, and k=20 no-early-return (NER).

## 8. Retrieval is no substitute for expertise either

Section 7 showed that drilling a corpus into the weights doesn’t produce expertise on its own. The complementary worry is the one from Section 2: maybe studying doesn’t matter much, because the agent can just search the corpus at test time. Studying-Literature is the task we built to test this. Its corpus is far too large for any model to hold in context, so nothing can be memorized, and its target papers are subsequent to the knowledge cutoff of all models in our experiments, so their related literature discussions can’t generally be directly recalled from memory.

Both of those properties let us separately investigate two skills that may contribute to an agent’s expertise: *finding* the right papers to cite and *recognizing* that they’re the ones that should be cited. In addition, this task has a clear year-by-year division (i.e., the date that every paper in the citation corpus was released) that allows us to test how an agent’s expertise interacts with the scope of its public knowledge cutoff.

Over each session, the agent issues twenty BM25 queries and ends up seeing roughly 230 distinct papers on average. We call the share of gold references that appear anywhere during a rollout `reach`. The agent then commits to a final 100, and `recall@100` is the share of gold references that survive that cut. So `reach` scores search (did the right evidence ever enter the agent’s trajectory?), and `recall@100` scores expertise (once a paper was fetched, did the agent choose to keep it?).

GPT-5.1’s knowledge cutoff (Sep 30, 2024) is roughly a year before GPT-5.5’s (August 31, 2025), and the target papers are from ICLR 2026, past both. Neither model can fall back on having seen the answer, and both search the same corpus through the same tool, so if retrieval could stand in for that year of studying, the two should write more or less the same review.

Figure 7 shows it can’t. Start with `reach`, which is really a control here: it tells us whether the two models are able to retrieve the same amount of relevant evidence. And indeed, they do: both surface around 60% of the gold references, and the gap stays small at every publication year, so the older model has no trouble writing queries that pull the right papers in. With search ruled out as the differentiator, `recall@100` shows the difference between the two models. GPT-5.5 keeps 11 to 14 more points of the gold references in its final hundred, and that lead is not spread evenly: it is small for older references and concentrated on recent ones, the years near the end of or past GPT-5.1’s cutoff.

Reach vs. Recall@100

share of gold references (%) ·

+N= GPT-5.5 lead in points (− = GPT-5.1 lead)

must-cite · overall

macro mean (n=50, gold = 884 refs)

must-cite overall. recall@reach 5.1 60.0, 5.5 63.9. recall@100 5.1 42.8, 5.5 57.0 (percent).

related-work · overall

macro mean (n=50, gold = 969 refs)

related-work overall. recall@reach 5.1 52.3, 5.5 56.4. recall@100 5.1 37.3, 5.5 47.9 (percent).

must-cite · reach

reached during 20 iterations

must-cite reach. 5.1: 36.4, 44.8, 51.8, 56.6, 68.7, 69.9. 5.5: 40.6, 49.3, 55.3, 64.5, 71.8, 74.2 (percent).

paper publication year

must-cite · recall@100

kept in the top 100

must-cite recall@100. 5.1: 29.4, 35.8, 42.4, 39.5, 49.3, 44.5. 5.5: 39.2, 47.8, 49.4, 57.2, 62.6, 64.1 (percent).

paper publication year

GPT-5.1GPT-5.5**Figure 7.**Reach versus recall@100 for GPT-5.1 and GPT-5.5 on the literature-review task.

Figure 8 isolates this by removing search from the comparison entirely. We keep only the must-cite papers that *both* models actually encountered, then ask what fraction each one keeps, so both now judge an identical pile. Through 2022 the two models nearly agree, the older one giving up only a handful of points. From 2023 on, GPT-5.1 falls behind by around twenty points, on papers it had already found and read. Nothing failed in retrieval: the relevant 2025 paper were retrieved but got set aside by GPT-5.1, presumably because it doesn’t know enough about the field of those years to see why it mattered, much like the bad lawyer example from Section 2.

Retrieval-Controlled Selection Rate by Year

share of reached must-cites kept ·

+N= GPT-5.5 lead, in points

By year (≤2020 … 2025). GPT-5.1: 88.1, 87.0, 83.8, 68.9, 72.5, 65.6. GPT-5.5: 95.2, 95.7, 89.2, 91.9, 88.7, 89.3 (percent). Gap in points: +7, +9, +5, +23, +16, +24.

paper publication year

GPT-5.1GPT-5.5**Figure 8.**Retrieval-controlled paper-selection rate by publication year.

## Epilogue

Right now, the gap between a frozen agent and a new domain is closed by hand: we write the skill files, we build (or buy) the RL environments, and otherwise we wait for the next release that re-trains the models on newer data and newer environments.

Machine studying asks for something better. **An agent that is handed a corpus should be able to make itself an expert in the domain the corpus describes.** Our preliminary results say this ability mostly does not exist yet, and they say the headroom for it is quite substantial in size.

We’re sharing [StudyBench](https://huggingface.co/datasets/jacobli/msbench), the benchmark we’re actively developing, this early precisely so that others can begin thinking about this with us. StudyBench hopefully makes it clear that the goal is not being really knowledgeable about DSPy, OpenClaw, or the ML Literature (it’s not about high performance!), but the goal is building agents and algorithms that can study domains that are completely new to them really efficiently. **Humans turn reading and thinking into expertise all the time. Why can’t our agents do the same?**

## Acknowledgements

This research is partially supported by funding from the VMware University Research Fund (VMURF). We thank our OASYS labmates Noah Ziems, Alex Zhang, and Diane Tchuindjo for their support throughout. We also thank Jenny Huang for several insightful discussion, and Ced Zhang for many challenging conversations and his comments on early drafts.

This work used Anvil AI at Purdue University through allocation CIS250733 from the [Advanced Cyberinfrastructure Coordination Ecosystem: Services & Support](https://access-ci.org/) (ACCESS) program, which is supported by U.S. National Science Foundation grants #2138259, #2138286, #2138307, #2137603, and #2138296.

## Citation

If you find this blog helpful, you could cite it as:

```
@misc{li2026machinestudying,
  title  = {Machine Studying},
  author = {Li, Jacob Xiaochen and Battle, Rick and Khattab, Omar},
  year   = {2026},
  month  = {Jun},
  url    = {https://jacobxli.com/blog/2026/machine-studying/}
}
```

## Appendix

show ↓hide ↑### Outcome distributions

Outcome Distribution by Setting

DSPy

gpt5.1

gpt5.1 outcome distribution per setting on DSPy.

gpt5.4 mini

gpt5.4 mini outcome distribution per setting on DSPy.

OpenClaw

gpt5.1

gpt5.1 outcome distribution per setting on OpenClaw.

gpt5.4 mini

gpt5.4 mini outcome distribution per setting on OpenClaw.

failureno codeinvalidcore misssuccesspartialperfect**Figure 9.**Outcome distribution of GPT-model attempts across the four inference settings.

Missing core items dominate the errors across all four inference settings for the two `GPT` models (Figure 9). Section 5 discusses the two patterns we found when inspecting these trajectories: agents that settle on a plausible solution early instead of continuing to search, and `GPT5.1`’s compile failures from APIs deprecated since 2024.

### Per-budget scores and tokens

Full measurements behind the coding-benchmark expertise numbers. Each cell is **score (%) · generation tokens/question** under lenient grading; budgets are ReAct caps — *direct* (zero-shot), *k=5*, *k=20*, and *k=20 NER* (forced, no early return). The last column is expertise (weighted AUC, $\lambda=\ln 10$, $3\text{k}$ anchor).

**Studying-DSPy**

| system | direct | k=5 | k=20 | k=20 NER | expertise |
| --- | --- | --- | --- | --- | --- |
| Qwen3.5-9B (base) | 3.3 · 4.1k | 8.6 · 7.9k | 9.6 · 8.6k | 29.4 · 34.6k | 6.49 |
| + cheatsheet | 6.3 · 3.9k | 14.4 · 6.1k | 14.1 · 7.1k | 23.1 · 29.9k | 9.65 |
| SFT + OPSD | 9.4 · 9.2k | 7.4 · 15.2k | 8.5 · 16.6k | 21.0 · 155.8k | 3.29 |
| CPT(code) | 5.1 · 5.9k | 7.4 · 8.8k | 7.0 · 10.6k | 14.3 · 59.3k | 3.71 |
| CPT(doc) | 3.8 · 4.8k | 7.2 · 8.2k | 6.2 · 9.9k | 14.6 · 74.9k | 3.92 |

**Studying-OpenClaw**

| system | direct | k=5 | k=20 | k=20 NER | expertise |
| --- | --- | --- | --- | --- | --- |
| Qwen3.5-9B (base) | 2.3 · 4.1k | 6.9 · 4.6k | 15.8 · 9.7k | 17.6 · 24.3k | 7.64 |
| + cheatsheet | 4.3 · 3.8k | 8.6 · 6.0k | 15.2 · 9.1k | 18.1 · 20.1k | 8.18 |
| CPT(code) | 2.2 · 3.4k | 8.8 · 4.7k | 15.3 · 11.6k | 14.1 · 32.1k | 7.82 |

Token counts are generation (completion) tokens per question, averaged over 3 seeds (DSPy: ÷90 = 3×30; OpenClaw: ÷60 = 3×20).

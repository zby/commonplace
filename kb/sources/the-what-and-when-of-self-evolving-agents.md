---
source: https://xinmingtu.cn/blog/2026/self-evolving-agents/
description: A 3×3 framework classifying self-evolving agents by update substrate—external files, agent harness, or model weights—and persistence horizon.
captured: 2026-07-23
capture: web-fetch
genre: conceptual-essay
type: kb/sources/types/snapshot.md
---

# The What & When of Self-Evolving Agents

Author: Xinming Tu
Source: https://xinmingtu.cn/blog/2026/self-evolving-agents/
Date: Last updated July 22, 2026

A 3×3 framework for understanding what evolves in AI agents and when those updates persist.

## Abstract

AI agents are increasingly expected to learn from experience. Yet systems labeled continual learning, self-evolution, or self-improvement differ in what they update and how long those updates persist. We map these differences in a 3×3 framework along two axes: the update substrate—external files, the agent harness, or model weights—and the persistence horizon—within a single session, across sessions, or across users.

We then reframe these product-centered horizons around the agent, distinguishing intra-task, inter-task, and inter-agent evolution. It treats continual learning and self-evolution as closely aligned, and recursive self-improvement as the special case where self-evolution is applied to AI development itself. Finally, we trace how repeated discoveries can consolidate from temporary artifacts into reusable harness logic and, eventually, model weights.

## The Dual Promise

We expect AI systems to learn from experience. The push toward self-evolving agents rests on two promises:

- Experience should lower marginal cost. Similar tasks should get cheaper: past trajectories compress into reusable assets, so the system stops paying the same inference tax twice—fewer tokens, fewer tool calls, fewer retries, fewer human interventions.
- Experience should expand the capability frontier. The system should get more capable: by retaining discoveries, learning from feedback, and revising strategy, it solves harder problems and sustains longer task horizons than it could before.

Agents accumulate experience, expanding the capability frontier while reducing marginal cost per task. This is an idealized view.

The pursuit goes by many names—continual learning, self-evolution, and self-improvement—and the boundaries between them are often blurred. AlphaEvolve and autoresearch evolve artifacts—programs, proofs, and training code—within a run. ACE evolves context—instructions, strategies, and evidence—into structured playbooks, while Mem0 preserves long-term conversational memory across sessions. Autodata turns agentic inference into higher-quality training and evaluation data for subsequent model training. All learn from experience, but they update different substrates over different horizons.

Learning is not magic: it must land somewhere, and it must last for some horizon. So instead of sorting the words, this blog sorts the updates. Crossing three update substrates—external files, the agent harness, model weights—with three persistence horizons—a single session, across sessions, across users—gives a 3×3 map.

Even recursive self-improvement is not a separate mechanism: it is this same loop pointed at AI development itself, a special case discussed below. The sharper question is: what does it update, and for how long?

### Read this alongside

- Gao et al., *A Survey of Self-Evolving Agents*—a comprehensive literature map organized around what, when, how, and where agents evolve, with broader coverage of evaluation, applications, and open challenges.
- Lilian Weng, *Harness Engineering for Self-Improvement*—a harness-centered account of self-improvement, tracing optimization from context and workflows to harness and optimizer code.
- Shilong Liu, *A Taxonomy of Self-evolving Agents*—a complementary model–harness–artifact taxonomy organized by what evolves, what feedback drives it, and where the loop closes.

This post takes a different cut: update substrate × persistence horizon, followed by a consolidation path across layers.

## What Evolves

Before asking how an agent evolves, we need to ask what can change. In practice, an agent’s adaptive state is distributed across three plastic layers:

- **External Files:** memory, knowledge, skill library.
- **Agent Harness:** prompts, tools, workflow, logic.
- **Model Weights:** parametric memory, core model.

External files are editable artifacts the agent reads and writes—notes, documents, and skills. The agent harness is the scaffolding that turns a model into an agent—prompts, tools, and control flow. Model weights are what the network has internalized—knowledge baked into parameters.

The direction is surface → core. Outward is cheap, instant, and reversible. Inward is expensive, slow, and durable. The deeper a change goes, the more it sticks.

A natural way to enter this structure is from the core outward:

- **Layer 3: Model Weights.** The parametric core: knowledge and behavior encoded inside the model checkpoint. Examples include GPT-family, DeepSeek, or Qwen weights.
- **Layer 2: Agent Harness.** The control layer around the model: prompts, tools, routing, planning, recovery logic, and execution flow. In systems like Claude Code or Codex, this layer shows up as tool-use policies, edit-test-repair loops, workflow execution, subagents, and reusable skills.
- **Layer 1: External Files & State.** Writable artifacts the agent can read or update outside the model and harness. Examples include skills, memory files, `CLAUDE.md`, `AGENTS.md`, saved commands, project notes, and reusable scripts.

### Boundary note: when files become code

The boundary between external state and harness logic is porous. A Python function, workflow file, routing rule, or recovery script may begin as an external artifact. The moment the runtime discovers it, loads it, and routes future tasks through it, that artifact becomes part of the harness.

External state no longer stores only facts. It can store skills, workflows, policies, and executable operators. The same object can be a file at rest and harness logic in motion.

## When Updates Persist

Experience becomes learning only when it leaves state that changes a later action. That state may be a note, script, workflow rule, cached artifact, or weight update; its lifetime defines three persistence horizons:

- **Single Session:** adaptation inside one live trajectory.
- **Across Sessions:** adaptation that persists for a user, project, codebase, or environment.
- **Across Users:** population-level adaptation from aggregate interactions.

## The 3×3 Evolution Matrix

The result is a 3×3 map: three persistence horizons crossed with three update substrates.

| Persistence horizon | External Files | Agent Harness | Model Weights |
|---|---|---|---|
| Across Users | Knowledge & skill commons: one agent’s discovery becomes a zero-shot capability for all | Platform harness flywheel: aggregate failures upgrade everyone’s default harness | Checkpoint bootstrapping: verified traces feed future model training |
| Across Sessions | Skill library & memory: skills, notes, and assets that carry across sessions | Compiled workflow harness: past traces compile into reusable workflows | Parametric personalization: repeated use updates trainable parameters |
| Single Session | Task-local artifacts & memory: evolving artifacts, runtime notes, and scratchpads | Dynamic orchestration: live traces create branches, tools, and repair loops | Test-time training: train on feedback from the current problem |

The matrix shows possibility, not obligation: these are places self-evolution can land, not requirements every agent must satisfy. It also classifies update loops, not papers. A single system can run several loops at once—ThetaEvolve evolves a program database while also training its search policy at test time—and then it occupies several cells.

### Across Users · External Files — Knowledge & skill commons

- EinsteinArena: verified discoveries become shared starting points for other agents.
- Agent Skills: reusable tools and procedures move from one agent’s success into a shared skill commons.

### Across Users · Agent Harness — Platform harness flywheel

- Claude Code / Codex defaults: platform-level workflow, tool, and recovery improvements become the default harness for every user.

### Across Users · Model Weights — Checkpoint bootstrapping

- Autodata: agentic inference produces training and evaluation data for future models.
- Self-play: agents generate challenges, data, and rewards that target discovered weaknesses.
- Cursor Tab: population-scale accepts and edits become RL signal for the next policy.

### Across Sessions · External Files — Skill library & memory

- ACE: evolving playbooks accumulate strategies and evidence across tasks.
- Mem0: long-term conversational memory carries user context across sessions.
- Voyager: executable skills accumulate and are retrieved for later tasks.
- Codex Record & Replay: one demonstrated workflow becomes a reusable skill.
- `CLAUDE.md` / `AGENTS.md`: repository instructions preserve project conventions across sessions.

### Across Sessions · Agent Harness — Compiled workflow harness

- Meta-Harness: repeated execution traces are compressed into a reusable workflow DAG.

### Across Sessions · Model Weights — Parametric personalization

- OpenClaw-RL: repeated conversational and environment feedback becomes signal for updating a personal agent’s policy.

### Single Session · External Files — Task-local artifacts & memory

- autoresearch: the agent edits training code and keeps or discards each change within one run.
- AlphaEvolve: evaluator feedback iteratively improves programs, proofs, and constructions.
- MemGPT: working memory is paged between the live context and external storage.
- ThetaEvolve: a program database evolves alongside the test-time-trained search policy.

### Single Session · Agent Harness — Dynamic orchestration

- Claude Code’s Dynamic Workflows: a task-specific orchestration script creates live branches, loops, and subagent calls.
- Recursive Language Models: recursive subcalls turn context processing into runtime control flow.

### Single Session · Model Weights — Test-time training

- TTT-Discover: feedback from the current problem updates the model during inference.
- ThetaEvolve: test-time RL updates the search policy as evolutionary search proceeds.

## Single Session: On-the-Fly Adaptation

The first horizon is the live trajectory: using feedback from the current run to improve performance on the task before the run ends. Within one trajectory, experience can become task-local state: artifacts, notes, helpers, and plans.

### Layer 1 · External Files: Task-Local Artifacts and Memory

The clearest single-session loop is an evolving artifact. autoresearch runs it in its purest form: an agent modifies training code, runs the experiment, keeps or discards the change, and continues—no human intervention until the run ends. AlphaEvolve drives the same loop with evaluator feedback at larger scale, improving programs, proofs, and constructions inside an external file. The agent itself may stay unchanged; what evolves is the artifact and the search state guiding the next attempt.

External state also serves as plain working memory—notes, constraints, and retrieved context paged in and out of the window, with MemGPT as the canonical example.

### Layer 2 · Agent Harness: Dynamic Orchestration

At the harness layer, the agent rewires its execution plan at runtime.

A conventional agent loop keeps tool use inside one continually growing conversation: each result informs the next action, but the surrounding execution loop stays fixed.

A dynamic workflow makes that surrounding control structure task-dependent, introducing branches, loops, and subagent calls at runtime while distributing intermediate state across separate contexts.

Claude Code’s Dynamic Workflows make this literal: the execution plan leaves the conversation. Claude writes a JavaScript orchestration script, and a separate runtime executes it in the background across subagents. Loops, branches, fan-out, error handling, resumability, and intermediate state are compiled for the task itself.

Recursive Language Models expose the underlying mechanism in a lighter form: recursive subcalls turn context processing into runtime control flow. The script may be temporary, but within that session the agent has expanded its own action space.

### Layer 3 · Model Weights: Test-Time Training

The most aggressive online adaptation modifies the model itself during inference. TTT-Discover makes this concrete: instead of only prompting a frozen model to search longer, the system trains at test time on feedback from the current problem.

ThetaEvolve brings the same move to evolutionary search: test-time RL keeps updating the policy’s weights as the search runs.

This does not eliminate training; it moves part of the learning loop into deployment. TTT is the upper edge of online self-evolution: the agent does not merely remember a discovery; it alters the machinery that will generate the next one.

## Across Sessions: Longitudinal Alignment

The second horizon is longitudinal: adapting to recurring structure across the same user, project, workflow, or task family.

### Layer 1 · External Files: Persistent Memory & Skills

The practical cross-session layer has two forms: memory and skills.

Memory preserves stable context across conversations: user preferences, project facts, long-term goals, or prior decisions. Chatbot memory is the familiar example: the assistant remembers facts about the user or workspace instead of asking again. In coding agents, the same pattern often appears as repository-level instruction files such as `CLAUDE.md` and `AGENTS.md`, which carry durable project conventions across sessions.

Skills preserve repeatable procedures. A skill can be a saved command, a verified wrapper, a reusable script, or a demonstrated workflow. Voyager showed the executable version early by accumulating Minecraft skills as reusable code. OpenAI Codex Record & Replay turns one demonstrated workflow into a reusable skill.

### Layer 2 · Agent Harness: Meta-Programming

When an agent repeatedly solves the same class of problems, it should not reconstruct its execution plan from scratch. High-performing trajectories can be mined to optimize the harness itself.

This is meta-programming at the harness layer. Meta-Harness makes the idea literal: an outer-loop optimizer searches over harness code using prior candidates, scores, and execution traces. The structural move is compression: repeated execution patterns collapse into a lean, reusable execution DAG (Directed Acyclic Graph).

### Layer 3 · Model Weights: Parametric Personalization

At the model-weights layer, repeated interaction changes trainable parameters themselves, not the memory store or harness. OpenClaw-RL points in this direction: conversational feedback becomes training signal for updating the agent’s model weights.

This remains frontier work. In many deployed systems, personalization is likely to appear first in files or harness logic, because per-user weight adaptation complicates serving, batching, evaluation, privacy, and update governance.

## Across Users: Population-Level Evolution

The third horizon is population-level, and its goal is different in kind: not solving one problem (single session), not adapting to one task family (across sessions), but raising the baseline every user starts from. One agent’s failure or discovery becomes the population’s default—landing in shared assets, default harnesses, or future models.

### Layer 1 · External Files: Collective Knowledge & Skill Commons

Human civilization scales by externalizing discovery into books, libraries, protocols, and tools. Agent populations can do the same: at the external-state layer, population-level evolution builds a shared commons of artifacts agents can query or reuse.

- Knowledge stores what was discovered: constraints, schemas, failure modes, proof ideas, or reusable mathematical constructions. If one agent finds a useful construction for an open math problem, the next agent should inherit the artifact rather than rediscover it. EinsteinArena makes this population-level loop concrete with verifiers, leaderboards, and public discussion, so one agent’s construction can become another agent’s starting point.
- Skills store how to act: shared tools, verified wrappers, repair recipes, and agent-published procedures. A skill-share system turns one agent’s working script or wrapper into another agent’s starting capability.

### Layer 2 · Agent Harness: Platform Harness Flywheels

At the harness layer, population-scale evolution upgrades the default agent runtime. This is platform-level change: when Claude Code, Codex, or a similar agent ships plan mode, `/loop`, `/goal`, better tool schemas, or stronger recovery logic, every user inherits a better harness.

The signal comes from aggregate failures. If many agents fail at the same step, the fix may not be a smarter base model; it may be a better prompt, router, tool contract, retry policy, or verification loop. Over time, the harness itself becomes an optimization target.

### Layer 3 · Model Weights: Checkpoint Bootstrapping

At the parametric layer, population-level evolution usually means checkpoint bootstrapping, not live continual learning. Deployed agents become data engines for future models.

When an agent solves a novel task that a compiler, sandbox, or verifier can check, the verified trace can enter the pretraining data corpus for a future model. Self-play and auto-data agents push this further: the agent manufactures its own challenges, data, and rewards, targeting the weaknesses it discovered in the environment.

Population behavior also becomes preference and reward signal: accepts, rejects, edits, interruptions, and corrections show where the current model fails. Cursor Tab, Cursor’s code autocomplete feature, is a concrete example: users’ Tab accepts and edits provide RL signal for training the next policy.

Deployment stops being only the end of training; it becomes part of the training loop.

This loop is only partially automated today. Agents can generate traces, tools, and candidate fixes, but humans still design reward signals, curate data, run evaluations, and approve checkpoint promotions. Recursive self-improvement is the direction of travel, not today’s baseline.

## What Is the ‘Self’ Here?

The 3×3 matrix above is still product-framed. Its time axis is defined by the surfaces through which today’s agents meet humans: one session, repeated sessions, and many users. That framing is useful, but it does not fully answer what the “self” is.

An agent-centered view keeps the same three substrates, but re-labels the persistence horizons around what the agent actually encounters: tasks, environments, and peers.

| Product frame | Agent frame | Trigger |
|---|---|---|
| Single Session / your prompts | Intra-Task · Execution Horizon | Environmental feedback |
| Across Sessions / persistent context | Inter-Task · Environmental Horizon | Domain structure & dependencies |
| Across Users / population telemetry | Inter-Agent · Swarm Horizon | Peer discovery & self-play |

The same three horizons are re-derived from the agent’s frame of reference. The trigger for adaptation shifts from user interaction to environment, domain, and peers.

- Single Session → Intra-Task. What looks like one user session is, for the agent, one objective being executed under feedback from tools, tests, and the environment.
- Across Sessions → Inter-Task. What looks like repeated user interaction is, for the agent, recurring structure across related tasks: kernel optimization, infrastructure tuning, API debugging, or work inside the same codebase.
- Across Users → Inter-Agent. What looks like population telemetry is, for the agent, a collective: discoveries, tools, and strategies propagating across peers.

## Discussion

### Continual Learning and Self-Evolution

Continual learning and self-evolution are closely aligned: both describe systems in which experience becomes state that shapes future behavior. In this blog, self-evolving agent names an agent-centered view of this process, with learned state residing in external files, the agent harness, or model weights.

### Capability Consolidation

The matrix is not only a taxonomy; it also describes a possible path of capability consolidation. A useful discovery may begin as a task-local artifact. If it succeeds repeatedly across tasks or users, it can be promoted into a reusable tool or workflow in the harness. If that workflow generalizes broadly enough, training on its successful trajectories can internalize the capability into a future model’s weights.

Yet consolidation is not a race toward weights. The design question is what to retain, where, and for how long.

Substrate also shapes portability: files are easy to move, harness updates require a compatible runtime, and weight updates are checkpoint-bound. But portability is not generalization—a portable skill can be brittle, while an internalized update can generalize broadly.

### Recursive Self-Improvement

Recursive self-improvement is not a separate architectural mechanism, but the same self-evolving loop applied to the AI development pipeline itself. An agent may generate synthetic pre-training data, build automated evaluations, curate post-training datasets, or improve training infrastructure. Recursive’s automated AI research system is an early example, applying agentic search to AI-development tasks such as model training and GPU-kernel optimization.

The loop is:

```text
self-evolving agents
experience → state → behavior
        ↓
inference-time work → saved artifacts & signals
        ↓
AI-development tasks: data / training / eval / infra / kernels
        ↓
next-gen agent: stronger model + harness
        ↓
generation t+1 runs the loop again
```

When experience can reliably become reusable capability, we stop building merely smarter copilots. We begin building the substrate for intelligence that can evolve itself.

## Acknowledgements

The author thanks Xi Fu, Yiping Wang, Qizheng Zhang, and Qiuyang Mang for reading the blog and for their helpful comments.

## Appendix: The Complete Landscape

The main text keeps a curated set of anchor examples per cell. This appendix restores the broader map: the same 3×3 matrix, expanded with more systems, mechanisms, design tradeoffs, and caveats.

For survey-level context, recent work organizes self-evolving agents around what evolves, when it evolves, and how it evolves. For the harness column specifically, Weng’s harness-engineering essay traces a progression of optimization targets from prompts and structured context through workflows and harness code up to the optimizer code itself.

The placement rule is simple: if an example changes the reader’s understanding of the core mechanism, it belongs in the main text; if it primarily broadens coverage, it belongs here. Several patterns also cut across cells:

- **External state becoming harness:** skills begin as files, but become control logic once the runtime discovers them, loads them, and routes through them. Anthropic Agent Skills, OpenHands skills, and Memento-Skills all sit on this boundary.
- **External state becoming transient parameters:** retrieved context is not just “read” by the model; it becomes key-value tensors in the active computation. Linear attention and fast-weight interpretations make this boundary especially explicit.
- **Local discoveries becoming global defaults:** a temporary script can become a user skill; a user skill can become a shared registry asset; a repeated failure can become a harness or checkpoint update.
- **Long-running environment learning:** EdgeBench measures whether agents can turn environmental feedback into better plans, artifacts, and outcomes over tasks lasting 12 hours or more, providing benchmark evidence for the single-session horizon without prescribing one update substrate.
- **Harness and weights co-evolving:** SIA runs a meta-agent/feedback-agent loop that chooses, per iteration, between rewriting the task agent’s harness and applying LoRA weight updates. The evidence is still early, but the pattern is distinct enough to name.

### Single Session / Layer 1: Task-Local Artifacts and Memory

This cell covers state that is created, compressed, retrieved, or discarded inside one active trajectory—evolving artifacts on one side, working memory on the other.

- autoresearch turns one long run into an experiment loop: the agent edits training code, launches the experiment, and keeps or discards the change based on results.
- FunSearch shows the program-search version of the same loop: generated programs are evaluated, selected, and reused for further discovery.
- AlphaEvolve extends verified program search to scientific, algorithmic, and infrastructure problems, where generated code is evaluated, selected, and iteratively reused as the evolving artifact.
- ShinkaEvolve attacks the sample efficiency of this loop with balanced parent sampling, code-novelty rejection sampling, and bandit-based model selection.
- MemGPT frames the context window as constrained RAM and external storage as virtual memory, making memory movement an explicit systems problem.
- Reflexion stores verbal self-critique of failed attempts in an episodic buffer that conditions the next trial: an early demonstration that feedback can become reusable textual state without weight updates.
- MEMENTO teaches models to manage their own context by segmenting intermediate reasoning and reasoning forward through compressed mementos.
- Memory-as-Action treats memory editing as a learnable action policy instead of a fixed heuristic.
- AMA-Bench highlights a core failure mode: similarity-based memory retrieval can miss causal and objective information, so memory systems must be evaluated on task usefulness rather than storage volume.
- Lost in the Middle explains why this matters even when context windows are large: performance drops when relevant evidence sits in the middle of long context.

The artifact-evolution systems run their whole loop inside a single session; their program databases would move up the matrix only when shared as commons across runs and users.

**Mechanism:** iterate on external artifacts against evaluator feedback until the run ends; compress the live trace into structured memory and page low-salience information out of active context.

**Caveat:** a larger memory store is not automatically an evolved agent. Without reliable write policy, retrieval policy, and evaluation, memory becomes another noisy tool.

### Single Session / Layer 2: Dynamic Orchestration and Ad-Hoc Tools

This cell covers runtime changes to the control path: the agent changes how it acts before the current task is over.

- Claude Code Dynamic Workflows move orchestration from the chat transcript into a JavaScript script executed by a separate workflow runtime, allowing loops, branching, subagent fan-out, resumability, and intermediate variables to live outside the model context.
- Large Language Models as Tool Makers is a boundary case: tool making can begin inside a task, while cached tool APIs make the generated functionality reusable across later requests.
- Recursive Language Models blur Layers 1 and 2 by using recursive subcalls over context snippets as a control strategy for manipulating external context.

**Mechanism:** turn the live trace into executable control state: scripts, temporary tools, diagnostic branches, repair loops, and subagent coordination plans.

**Caveat:** dynamic orchestration creates power and risk at the same time. The more the control layer can rewrite itself, the more the runtime needs isolation, provenance, cost bounds, and rollback.

### Single Session / Layer 3: Test-Time Training and Fast Weights

This cell covers parametric or quasi-parametric adaptation during inference.

- In-Place Test-Time Training studies direct updates to model parameters during inference, making deployment itself part of the learning loop.
- Learning to Discover at Test Time explores updating model behavior on the exact problem instance rather than only searching longer with frozen weights.
- JitRL is a boundary case: it keeps weights frozen, retrieves trajectory memory to estimate action advantages, and modulates logits at test time for policy improvement without gradient updates.
- TTT Layers reinterpret sequence modeling as a learned test-time update process, where hidden states behave like expressive memory substrates.
- Linear Transformers Are Secretly Fast Weight Programmers makes the fast-weight interpretation explicit: sequence history can write temporary associations into a memory matrix.
- Transformers are RNNs and Mamba show adjacent forms of recurrent state accumulation, making the boundary between context, state, and weights less clean than the standard frozen-transformer picture suggests. These fast-weight and recurrent-state papers are supporting evidence for the context/state boundary, not self-evolving agents by themselves.

**Boundary note:** context does not edit the checkpoint, but it does become computation. Retrieved tokens become KV-cache state that shapes future attention. Fast-weight and linear-attention interpretations explain why this transient state can look weight-like without becoming durable model weights.

**Mechanism:** use the current problem instance to change the computation itself: gradient updates, logit modulation, learned hidden-state updates, fast-weight memory, or recurrent state accumulation.

**Caveat:** this is the most powerful and operationally expensive online adaptation cell. It demands tight evaluation because a useful local update can also create regressions.

### Across Sessions / Layer 1: Persistent Skills and User Memory

This cell covers state that survives across sessions for one user, project, codebase, or environment.

- Voyager accumulates executable Minecraft skills and retrieves them for future tasks, giving a clear early example of skill-library growth.
- Anthropic Agent Skills package reusable procedures into discoverable folders that an agent can load when relevant.
- OpenAI Codex Record & Replay lets a user demonstrate a workflow on macOS and turn it into a reusable Codex skill, making “show once, reuse later” a concrete persistent-skill interface.
- OpenHands Skills and Context supports persistent skill installation, enabling skills to be managed, enabled, disabled, and reused across sessions.
- Memento-Skills pushes the same idea toward agents that design and improve agent skills themselves.
- Hermes Agent couples persistent memory with procedural skills that it creates from experience and improves during use.
- Agentic Context Engineering (ACE) treats contexts as evolving playbooks that accumulate, refine, and organize strategies over time.

**Mechanism:** convert repeated discoveries into durable artifacts: scripts, commands, wrappers, procedures, project conventions, and environment-specific recipes.

**Caveat:** persistent skills need lifecycle management. Stale skills can be worse than no skills, especially when project dependencies, APIs, or security constraints change.

### Across Sessions / Layer 2: Meta-Programming and Workflow Optimization

This cell covers recurring execution graphs that persist across tasks or sessions.

- Meta-Harness searches over harness code using prior candidates, scores, and execution traces, making harness optimization the direct target.
- Agent Workflow Memory induces reusable workflows from past trajectories and injects them into future tasks, a lightweight version of the same compression that sits deliberately on the file/harness boundary.
- DSPy treats language-model programs as optimizable graphs rather than hand-written prompts.
- MIPRO optimizes instructions and demonstrations for multi-stage language-model programs.
- AgentOptimizer iteratively adds, revises, and removes agent functions or skills from historical conversations and performance feedback, without updating the base model weights.
- Promptbreeder is the self-referential ancestor of this cell: it evolves task prompts and, in the same loop, the mutation prompts that rewrite them.
- GEPA pairs evolutionary prompt search with natural-language reflection over execution trajectories, extracting more improvement per rollout than RL-based prompt optimization.
- AFlow represents workflows as graphs of LLM-invoking nodes and searches over them with Monte Carlo Tree Search.
- STOP turns the optimizer on itself: a seed improver recursively rewrites its own improvement code, rediscovering strategies like beam search and genetic algorithms along the way.
- MCE lifts context engineering to a bi-level problem: an inner loop optimizes the context artifact while an outer loop evolves the context-management skills that produce it, so the mechanism and the artifact co-evolve.
- Self-Harness closes the loop on a single model’s own failure patterns: weakness mining over execution traces, bounded harness proposals tied to those weaknesses, and regression-gated validation before any edit lands.

These optimizers stay in this cell when they are run against a recurring task distribution; they would move to the population row only when a platform ships the resulting program as a global default.

**Mechanism:** mine historical trajectories, identify high-performing execution patterns, and compile them into reusable routers, DAGs, tool schemas, recovery loops, and workflows.

**Caveat:** harness optimization can overfit to yesterday’s tasks. Good systems need evaluation sets that represent the future operating distribution, not just the past transcript.

### Across Sessions / Layer 3: Parametric Personalization and Task Specialization

This cell covers parametric specialization over repeated interactions with one user or organization.

- SEAL makes self-evolving weights literal: the model writes its own finetuning data and update directives, applies them as persistent updates, and learns to write better self-edits from the updated model’s performance.
- OPPU explores democratized personalized parameter-efficient fine-tuning.
- Profile-to-PEFT uses profile-derived signals to produce fast personalized adaptation.
- PERSOMA studies personalized soft-prompt adapters for personalized language prompting.
- OpenClaw-RL treats next-state signals from user replies, tool outputs, terminal states, and GUI changes as online RL feedback for personal agents, making repeated use a source of policy improvement.

**Mechanism:** compress stable user- or organization-specific patterns into adapters, soft prompts, LoRA-style modules, or other parameter-efficient personalization layers.

**Caveat:** personalization must separate durable signal from accidental context. A user accepting one terse answer should not permanently train the model to be terse in every domain.

### Across Users / Layer 1: Collective Knowledge and Skill Commons

This cell covers shared external state—registries, knowledge banks, and artifact graphs—accumulated from the whole population’s interactions.

- Composio and LlamaHub are practical infrastructure for shared integration assets: hosted MCP/tool wrappers on one side, and reusable loaders, tools, and packs on the other.
- Agent KB studies how cross-domain experience can be reused for agentic problem solving.
- ReasoningBank collects reasoning memories to scale agent self-evolution.
- EinsteinArena makes the population-level loop concrete with verifiers, leaderboards, and public discussion, so one agent’s construction becomes another agent’s starting point.

**Mechanism:** validate and promote local discoveries into shared assets: tools, integrations, reasoning traces, API wrappers, benchmark solutions, and capability graphs.

**Caveat:** the trust problem dominates this cell. A global skill bank without provenance, sandboxing, and eval gates can become a supply-chain vulnerability or a hallucination amplifier.

### Across Users / Layer 2: Platform Harness Flywheels and Automated Design

This cell covers population-level improvement to the default agent process itself, plus automated search over agent code and harnesses that can later become defaults.

- Platform-shipped harness defaults can turn population telemetry into upgrades baked into every agent’s default harness: explicit planning for long-horizon tasks, autonomous execution loops, and test-and-verify steps that sandbox generated code before replying.
- Alita-G sits on the Layer 1/2 boundary: it turns successful trajectories into curated MCP tools, then uses retrieval-augmented tool selection to instantiate stronger domain agents.
- Automated Design of Agentic Systems (ADAS) established the search template behind this cell: a meta-agent programs new agents in code, evaluates them, and iterates against a growing archive of discovered designs.
- Darwin Gödel Machine explores open-ended evolution of self-improving coding agents.
- Hyperagents make the meta-level improvement procedure itself editable, so the system searches not only for better agents but for better ways to generate better agents.

**Mechanism:** mine aggregate failure logs, identify structural bottlenecks in prompts, tools, and workflows, and wire the fixes into the default harness—shipped directly by platform teams, or discovered automatically by meta-agents that propose, test, and deploy better control flows.

**Caveat:** harness updates are product updates. They require regression testing, rollout controls, and auditability because one bad default policy can affect every downstream user.

### Across Users / Layer 3: Checkpoint Bootstrapping and Self-Improvement Frontier

This cell covers model updates derived from population-scale interaction data.

- Cursor Tab online RL turns natural developer behavior—accepting, rejecting, or editing autocomplete suggestions—into reward signals for improving the autocomplete model.
- Chat-style products provide adjacent feedback channels: thumbs-up/down, regenerations, follow-up corrections, conversation abandonment, and accepted edits. These are not all equally clean rewards, but together they form a data flywheel for future alignment and checkpoint updates.
- Academic and industrial continual-learning loops increasingly treat deployed interaction as the environment rather than a post-hoc evaluation set.

**Mechanism:** aggregate implicit and explicit feedback into preference data, reward models, reinforcement-learning updates, supervised fine-tuning corpora, and future checkpoint releases.

**Caveat:** this is usually not fully autonomous self-evolution today. Humans still shape reward design, filter data, approve deployments, and evaluate regressions. The self-evolving part is the data flywheel; the governance layer remains human-heavy.

© Copyright 2026 Xinming Tu.

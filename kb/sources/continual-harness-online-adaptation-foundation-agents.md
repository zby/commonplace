---
source: https://arxiv.org/html/2605.09998v1?utm_source=chatgpt.com
description: "Reset-free embodied-agent study in which an LLM refiner edits prompts, sub-agents, skills, and memory online, with capability-dependent Pokémon results and joint model-harness training."
captured: 2026-08-02
capture: web-fetch
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Continual Harness: Online Adaptation for Self-Improving Foundation Agents

Author: Seth Karten, Joel Zhang, Tersoo Upaa Jr, Ruirong Feng, Wenzhe Li, Chengshuai Shi, Chi Jin, Kiran Vodrahalli
Source: https://arxiv.org/html/2605.09998v1?utm_source=chatgpt.com
Date: 11 May 2026

arXiv:2605.09998v1 [cs.LG] 11 May 2026

Continual Harness: Online Adaptation for Self-Improving Foundation Agents

Seth Karten^∗1    Joel Zhang^∗2    Tersoo Upaa Jr^1    Ruirong Feng^1    Wenzhe Li^1    Chengshuai Shi^1    Chi Jin^1    Kiran Vodrahalli^3
^1Princeton University    ^2ARISE Foundation    ^3Google DeepMind
^∗Equal contribution.
## Abstract

Coding harnesses such as Claude Code and OpenHands wrap foundation models with tools, memory, and planning, but no equivalent exists for embodied
agents’ long-horizon partial-observability decision-making. We first report our Gemini Plays Pokémon (GPP) experiments. With iterative human-in-the-loop harness
refinement, GPP became the first AI system to complete Pokémon Blue, Yellow Legacy on hard mode, and Crystal without a lost battle. In the hardest stages, the
agent itself began iterating on its strategy through long-context memory, surfacing emergent self-improvement signals alongside human-in-the-loop refinement.
Continual Harness removes the human fully from this loop: a reset-free self-improving harness for embodied agents that formalizes and automates what we
observed. Starting from only a minimal environment interface, the agent alternates between acting and refining its own prompt, sub-agents, skills, and memory,
drawing on any past trajectory data. Prompt-optimization methods require episode resets; Continual Harness adapts online within a single run. On Pokémon Red and
Emerald across frontier models, Continual Harness starting from scratch substantially reduces button-press cost relative to the minimalist baseline and recovers
a majority of the gap to a hand-engineered expert harness, with capability-dependent gains, despite starting from the same raw interface with no curated
knowledge, no hand-crafted tools, and no domain scaffolding. We then close the loop with the model itself: an online process-reward co-learning loop, in which
an open-source agent’s rollouts through the refining harness are relabeled by a frontier teacher and used to update the model, drives sustained in-game
milestone progress on Pokémon Red without resetting the environment between training iterations.
Date: Correspondence: sethkarten@princeton.edu Website: https://sethkarten.ai/continual-harness

## 1 Introduction

Refer to caption Figure 1: Continual Harness automates the harness refinement performed manually in GPP, and extends to joint training of model weights and
harness state. Each panel shares the same topology (environment, agent, harness, refiner); only the identity of the refiner changes. (1) Human-in-the-loop: in
our Gemini Plays Pokémon (GPP) experiments, a human reads trajectories and rewrites the harness, producing the first AI system to complete Pokémon Blue, Yellow
Legacy (hard mode), and Crystal. (2) Self-improving harness: Continual Harness replaces the human with an automated refiner that operates on trajectory data
within a single continuous episode; evaluated on Red and Emerald across frontier models. (3) Model + harness co-learning: after warm-up stages, an open-source
model’s weights and the harness state update jointly during online play.

Agentic harnesses, the scaffolding that wraps a foundation model with tools, memory, and planning, are now standard infrastructure for autonomous coding agents.
Claude Code [2], OpenHands [21], and OpenClaw [19] let models navigate codebases, run commands, and carry state across long interactions. No equivalent exists
for embodied agents.

The PokeAgent Challenge [5] reported that without domain-specific scaffolding, frontier vision-language models make almost no progress on RPG gameplay. Our
Gemini Plays Pokémon (GPP) project shows that a human-supervised refinement loop can solve this scaffolding problem: across Pokémon Blue, Yellow Legacy, and
Crystal, we iteratively refined the harness from a screenshot-and-buttons interface into a multi-agent system, and in later runs we removed the human-authored
agents and handed the model meta-tools (define_agent, run_code, notepad edits, custom tool creation) so it could construct its own sub-agents and reusable
scripts during play. Our agents beat Pokémon Blue in May 2025, defeated the Elite Four in Pokémon Yellow Legacy on hard mode in August 2025 and completed
Pokémon Crystal in November 2025, making GPP the first AI system to complete multiple Pokémon RPGs. In the hardest stages of Yellow and Crystal, the model
itself began iterating on its own strategy through long-context memory, an early emergent form of continual-harness behavior that we formalize and automate in
the rest of the paper.

We introduce Continual Harness, a reset-free framework that automates the manual harness refinement of GPP through online in-context learning over the harness
state, and extends to joint training of an open-source model’s weights through the same loop. From a minimal environment interface (frame observations, an ASCII
text map of the visible area, and button inputs), the agent alternates between acting in the environment and refining its own system prompt, sub-agents, skill
library, and memory using trajectory data collected so far in the episode. Every
[MATH: <semantics><mi>F</mi><annotation encoding="application/x-tex">F</annotation></semantics> :MATH]
steps, a Refiner reads the recent trajectory for failure signatures and runs four passes over the harness applying CRUD edits to system prompt, sub-agents,
skills, and memories. Unlike prompt-optimization methods such as GEPA [1] that run complete episodes and reset between updates, Continual Harness updates
mid-episode, so self-improvement continues without restarting.

On Pokémon Red and Emerald across three Gemini 3 variants (Pro, Flash, Flash-Lite), Continual Harness substantially reduces button-press cost relative to the
minimalist baseline and recovers a majority of the gap to a hand-engineered expert harness, with no curated knowledge, no hand-crafted tools, and no domain
scaffolding. On the Emerald cost-vs-completion Pareto plane, the harness gain scales with model capability: Continual Harness is strictly Pareto-dominant on
Pro, high-variance on Flash, and below the capability floor on Flash-Lite.

We then transfer the refined harness to open-source models using an online co-learning loop that scores rollouts with a process reward model, relabeling
low-reward windows via a frontier teacher, and updating the model via soft SFT. The online stage closes the loop between harness refinement and model training.
The refined harness shapes the model’s trajectories, and the model’s gameplay surfaces new failure modes for the next refinement cycle. On Pokémon Red, this
loop drives sustained in-game milestone progress in an open-source Gemma-4 model across training iterations, from both beginning and mid-game checkpoints. Both
loops operate on the same trajectory data; together they produce continual model-harness co-learning.

Our contributions are: (i) our GPP project results, the first AI system to complete multiple Pokémon RPGs through harness refinement; (ii) Continual Harness, a
reset-free framework that assembles harnesses for embodied agents from a minimal environment interface through online in-context learning; (iii) on Pokémon Red
and Emerald across Gemini 3 variants, Continual Harness recovers a majority of the gap to a hand-engineered expert harness, with capability-dependent gains on
the cost-vs-completion Pareto plane; and (iv) an online co-learning pipeline that drives sustained in-game milestone progress in open-source models on Pokémon
Red, producing continual model-harness co-learning.

## 2 Preliminaries

### 2.1 Embodied Agent Environments

We consider an embodied agent that interacts with its environment through a minimal interface. At each timestep
[MATH: <semantics><mi>t</mi><annotation encoding="application/x-tex">t</annotation></semantics> :MATH]
, the agent receives a frame observation
[MATH: <semantics><msub><mi>o</mi><mi>t</mi></msub><annotation encoding="application/x-tex">o_{t}</annotation></semantics> :MATH]
(a rendered image of the current environment state) together with a text map
[MATH: <semantics><msub><mi>m</mi><mi>t</mi></msub><annotation encoding="application/x-tex">m_{t}</annotation></semantics> :MATH]
that describes the visible tiles and nearby walkable positions in ASCII form, and selects an action
[MATH: <semantics><msub><mi>a</mi><mi>t</mi></msub><annotation encoding="application/x-tex">a_{t}</annotation></semantics> :MATH]
from a fixed set of button inputs
[MATH: <semantics><mi class="ltx_font_mathcaligraphic">𝒜</mi><annotation encoding="application/x-tex">\mathcal{A}</annotation></semantics> :MATH]
. The text map is derived from game state that a human player can read off the screen, and compensates for the limited spatial reasoning of current
vision-language models; it contains no walkthrough, no objective list, and no pathfinding. The environment is partially observable since the agent cannot access
internal state such as NPC intent or battle mechanics beyond what the frame and map expose.

### 2.2 Agentic Harnesses

An agentic harness
[MATH: <semantics><mi class="ltx_font_mathcaligraphic">ℋ</mi><annotation encoding="application/x-tex">\mathcal{H}</annotation></semantics> :MATH]
is the scaffolding layer between a foundation model
[MATH: <semantics><mi>M</mi><annotation encoding="application/x-tex">M</annotation></semantics> :MATH]
and the environment. Following the decomposition from Karten et al. [5], a harness mediates agent behavior through four components:
  * •
System prompt
[MATH: <semantics><mi>p</mi><annotation encoding="application/x-tex">p</annotation></semantics> :MATH]
: the instructions and strategic guidance provided to the model at each reasoning step.
  * •
Sub-agents
[MATH: <semantics><mi class="ltx_font_mathcaligraphic">𝒢</mi><annotation encoding="application/x-tex">\mathcal{G}</annotation></semantics> :MATH]
: specialized modules that can be invoked by the orchestrator for specific tasks (e.g., battle strategy, puzzle solving, self-reflection).
  * •
Skills
[MATH: <semantics><mi class="ltx_font_mathcaligraphic">𝒦</mi><annotation encoding="application/x-tex">\mathcal{K}</annotation></semantics> :MATH]
: reusable routines available to the model, spanning both text-level behaviors (heuristics cited in reasoning) and executable programs (pathfinders, tool
wrappers). Pre-built primitives such as press_buttons and get_game_state are skills the harness ships with; new skills can also be authored during play.
  * •
Memory
[MATH: <semantics><mi class="ltx_font_mathcaligraphic">ℳ</mi><annotation encoding="application/x-tex">\mathcal{M}</annotation></semantics> :MATH]
: a persistent knowledge store that accumulates facts, strategies, and observations across the agent’s trajectory.

In addition to these refined components, the harness exposes a fixed set of meta-tools (define_agent, run_code, process_memory, and similar primitives) through
which the agent edits
[MATH: <semantics><mrow><mi>p</mi><mo>,</mo><mi class="ltx_font_mathcaligraphic">𝒢</mi><mo>,</mo><mi class="ltx_font_mathcaligraphic">𝒦</mi><mo>,</mo><mi
class="ltx_font_mathcaligraphic">ℳ</mi></mrow><annotation encoding="application/x-tex">p,\mathcal{G},\mathcal{K},\mathcal{M}</annotation></semantics> :MATH]
in place.

A minimalist harness
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>min</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\min}</annotation></semantics> :MATH]
provides only the environment interface (
[MATH: <semantics><msub><mi>o</mi><mi>t</mi></msub><annotation encoding="application/x-tex">o_{t}</annotation></semantics> :MATH]
,
[MATH: <semantics><msub><mi>m</mi><mi>t</mi></msub><annotation encoding="application/x-tex">m_{t}</annotation></semantics> :MATH]
,
[MATH: <semantics><mrow><msub><mi>a</mi><mi>t</mi></msub><mo>∈</mo><mi class="ltx_font_mathcaligraphic">𝒜</mi></mrow><annotation
encoding="application/x-tex">a_{t}\in\mathcal{A}</annotation></semantics> :MATH]
) with a generic system prompt and no sub-agents, memory, or authored skills. A hand-engineered harness
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>expert</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\mathrm{expert}}</annotation></semantics> :MATH]
populates all components through manual engineering. A meta-harness gives the model meta-tools (define_agent, run_code, etc.) to construct its own sub-agents,
skills, and memory entries during play; this was the operating point of our later GPP runs, where the model built its own pathfinders, battle strategists, and
reusable scripts without being asked to. Continual Harness starts from a minimal harness and adds an automated Refiner that rewrites
[MATH: <semantics><mrow><mi>p</mi><mo>,</mo><mi class="ltx_font_mathcaligraphic">𝒢</mi><mo>,</mo><mi class="ltx_font_mathcaligraphic">𝒦</mi><mo>,</mo><mi
class="ltx_font_mathcaligraphic">ℳ</mi></mrow><annotation encoding="application/x-tex">p,\mathcal{G},\mathcal{K},\mathcal{M}</annotation></semantics> :MATH]
in place from trajectory analysis. We write
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>CH</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\mathrm{CH}}</annotation></semantics> :MATH]
for the running harness state during a Continual Harness run, evolving with every refinement cycle.

## 3 Methodology

Refer to caption Figure 2: Methodology overview. (a) Harness refinement within one episode: the Agent reads
[MATH: <semantics><mrow><mo stretchy="false">(</mo><msub><mi>s</mi><mi>t</mi></msub><mo>,</mo><mi class="ltx_font_mathcaligraphic">ℋ</mi><mo>,</mo><mi>τ</mi><mo
stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">(s_{t},\mathcal{H},\tau)</annotation></semantics> :MATH]
and emits
[MATH: <semantics><msub><mi>a</mi><mi>t</mi></msub><annotation encoding="application/x-tex">a_{t}</annotation></semantics> :MATH]
; every
[MATH: <semantics><mi>F</mi><annotation encoding="application/x-tex">F</annotation></semantics> :MATH]
steps the Refiner reads
[MATH: <semantics><msub><mi>τ</mi><mrow><mrow><mi>t</mi><mo>−</mo><mi>F</mi></mrow><mo lspace="0.278em"
rspace="0.278em">:</mo><mi>t</mi></mrow></msub><annotation encoding="application/x-tex">\tau_{t-F:t}</annotation></semantics> :MATH]
, emits per-component edits
[MATH: <semantics><mrow><mi mathvariant="normal">Δ</mi><mo>=</mo><mrow><mo stretchy="false">(</mo><mrow><mi mathvariant="normal">Δ</mi><mo lspace="0em"
rspace="0em">​</mo><mi>p</mi></mrow><mo>,</mo><mrow><mi mathvariant="normal">Δ</mi><mo lspace="0em" rspace="0em">​</mo><mi
class="ltx_font_mathcaligraphic">𝒢</mi></mrow><mo>,</mo><mrow><mi mathvariant="normal">Δ</mi><mo lspace="0em" rspace="0em">​</mo><mi
class="ltx_font_mathcaligraphic">𝒦</mi></mrow><mo>,</mo><mrow><mi mathvariant="normal">Δ</mi><mo lspace="0em" rspace="0em">​</mo><mi
class="ltx_font_mathcaligraphic">ℳ</mi></mrow><mo stretchy="false">)</mo></mrow></mrow><annotation encoding="application/x-tex">\Delta=(\Delta
p,\Delta\mathcal{G},\Delta\mathcal{K},\Delta\mathcal{M})</annotation></semantics> :MATH]
via the meta-tool API, and
[MATH: <semantics><mrow><mi class="ltx_font_mathcaligraphic">ℋ</mi><mo lspace="0.108em" rspace="0.108em" stretchy="false">←</mo><mrow><mi
class="ltx_font_mathcaligraphic">ℋ</mi><mo>⊕</mo><mi mathvariant="normal">Δ</mi></mrow></mrow><annotation
encoding="application/x-tex">\mathcal{H}\!\leftarrow\!\mathcal{H}\oplus\Delta</annotation></semantics> :MATH]
. (b) Co-learning across DAgger+PRM iterations: each iteration runs
[MATH: <semantics><msub><mi>π</mi><msub><mi>θ</mi><mi>k</mi></msub></msub><annotation encoding="application/x-tex">\pi_{\theta_{k}}</annotation></semantics>
:MATH]
inside a live-refining
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>t</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{t}</annotation></semantics> :MATH]
for
[MATH: <semantics><mrow><mi>K</mi><mo>=</mo><mn>256</mn></mrow><annotation encoding="application/x-tex">K{=}256</annotation></semantics> :MATH]
steps. The trajectory is scored by a pairwise PRM, low-
[MATH: <semantics><mi>R</mi><annotation encoding="application/x-tex">R</annotation></semantics> :MATH]
windows are relabeled by Gemini-3.1-pro, and a soft SFT update produces
[MATH: <semantics><msub><mi>θ</mi><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></msub><annotation
encoding="application/x-tex">\theta_{k+1}</annotation></semantics> :MATH]
. The loop is reset-free: a persistent state at the end of iter
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
is loaded as the start of iter
[MATH: <semantics><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">k{+}1</annotation></semantics> :MATH]
.

### 3.1 Overview and Two-Loop Architecture

Continual Harness performs online in-context learning over the harness state
[MATH: <semantics><mi class="ltx_font_mathcaligraphic">ℋ</mi><annotation encoding="application/x-tex">\mathcal{H}</annotation></semantics> :MATH]
from Section˜2. An LLM Refiner edits
[MATH: <semantics><mi class="ltx_font_mathcaligraphic">ℋ</mi><annotation encoding="application/x-tex">\mathcal{H}</annotation></semantics> :MATH]
from the most recent trajectory window during a single continuous episode, generalizing prompt-optimization methods that rewrite only
[MATH: <semantics><mi>p</mi><annotation encoding="application/x-tex">p</annotation></semantics> :MATH]
from complete-episode resets [1, 14] to a method that rewrites the full state from the trajectory so far.

Write
[MATH: <semantics><mrow><msub><mi>s</mi><mi>t</mi></msub><mo>=</mo><mrow><mo
stretchy="false">(</mo><msub><mi>o</mi><mi>t</mi></msub><mo>,</mo><msub><mi>m</mi><mi>t</mi></msub><mo stretchy="false">)</mo></mrow></mrow><annotation
encoding="application/x-tex">s_{t}=(o_{t},m_{t})</annotation></semantics> :MATH]
for the agent’s observation at step
[MATH: <semantics><mi>t</mi><annotation encoding="application/x-tex">t</annotation></semantics> :MATH]
. The inner loop is the standard agent step: the model
[MATH: <semantics><mi>M</mi><annotation encoding="application/x-tex">M</annotation></semantics> :MATH]
wrapped by the current harness
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>t</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{t}</annotation></semantics> :MATH]
produces an action
[MATH: <semantics><msub><mi>a</mi><mi>t</mi></msub><annotation encoding="application/x-tex">a_{t}</annotation></semantics> :MATH]
from
[MATH: <semantics><msub><mi>s</mi><mi>t</mi></msub><annotation encoding="application/x-tex">s_{t}</annotation></semantics> :MATH]
and the trajectory so far. The outer loop is harness refinement: every
[MATH: <semantics><mi>F</mi><annotation encoding="application/x-tex">F</annotation></semantics> :MATH]
steps after a warm-up of
[MATH: <semantics><mi>W</mi><annotation encoding="application/x-tex">W</annotation></semantics> :MATH]
steps, a Refiner reads the recent trajectory window for failure signatures and emits per-component edits
[MATH: <semantics><mrow><mi mathvariant="normal">Δ</mi><mo>=</mo><mrow><mo stretchy="false">(</mo><mrow><mi mathvariant="normal">Δ</mi><mo lspace="0em"
rspace="0em">​</mo><mi>p</mi></mrow><mo>,</mo><mrow><mi mathvariant="normal">Δ</mi><mo lspace="0em" rspace="0em">​</mo><mi
class="ltx_font_mathcaligraphic">𝒢</mi></mrow><mo>,</mo><mrow><mi mathvariant="normal">Δ</mi><mo lspace="0em" rspace="0em">​</mo><mi
class="ltx_font_mathcaligraphic">𝒦</mi></mrow><mo>,</mo><mrow><mi mathvariant="normal">Δ</mi><mo lspace="0em" rspace="0em">​</mo><mi
class="ltx_font_mathcaligraphic">ℳ</mi></mrow><mo stretchy="false">)</mo></mrow></mrow><annotation encoding="application/x-tex">\Delta=(\Delta
p,\Delta\mathcal{G},\Delta\mathcal{K},\Delta\mathcal{M})</annotation></semantics> :MATH]
. The agent does not reset; the updated harness
[MATH: <semantics><mrow><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mrow><mi>t</mi><mo>+</mo><mn>1</mn></mrow></msub><mo>=</mo><mrow><msub><mi
class="ltx_font_mathcaligraphic">ℋ</mi><mi>t</mi></msub><mo>⊕</mo><mi mathvariant="normal">Δ</mi></mrow></mrow><annotation
encoding="application/x-tex">\mathcal{H}_{t+1}=\mathcal{H}_{t}\oplus\Delta</annotation></semantics> :MATH]
enters the agent’s context on the next step (Figure˜2a), with
[MATH: <semantics><mi>p</mi><annotation encoding="application/x-tex">p</annotation></semantics> :MATH]
replaced by
[MATH: <semantics><mrow><mi mathvariant="normal">Δ</mi><mo lspace="0em" rspace="0em">​</mo><mi>p</mi></mrow><annotation encoding="application/x-tex">\Delta
p</annotation></semantics> :MATH]
and
[MATH: <semantics><mrow><mi class="ltx_font_mathcaligraphic">𝒢</mi><mo>,</mo><mi class="ltx_font_mathcaligraphic">𝒦</mi><mo>,</mo><mi
class="ltx_font_mathcaligraphic">ℳ</mi></mrow><annotation encoding="application/x-tex">\mathcal{G},\mathcal{K},\mathcal{M}</annotation></semantics> :MATH]
receiving CRUD-style operations (create, read, update, delete). The Agent and Refiner roles share the same model
[MATH: <semantics><mi>M</mi><annotation encoding="application/x-tex">M</annotation></semantics> :MATH]
, ablated across Gemini 3.1 Pro, Flash, and Flash-Lite (Section˜4). In our GPP runs, the Refiner role for the system prompt and pre-built primitives was
performed manually by humans observing the livestream; Continual Harness automates it. Both the agent and the Refiner issue edits through the same meta-tool API
(Section˜2); they differ only in when each is invoked and on what trajectory context.

### 3.2 Refinement Loop

The Refiner reads
[MATH: <semantics><msub><mi>τ</mi><mrow><mrow><mi>t</mi><mo>−</mo><mi>F</mi></mrow><mo lspace="0.278em"
rspace="0.278em">:</mo><mi>t</mi></mrow></msub><annotation encoding="application/x-tex">\tau_{t-F:t}</annotation></semantics> :MATH]
and identifies failure signatures over the window: navigation loops, tool-call failures, stalled objectives, and missed exploration opportunities. It then runs
four passes, one per component: (i) it rewrites the prompt
[MATH: <semantics><mi>p</mi><annotation encoding="application/x-tex">p</annotation></semantics> :MATH]
conditioned on the identified failures and the trajectory window; (ii) it creates sub-agent entries for repeated multi-step patterns, edits existing entries to
address detected failures, and deletes entries that have not been invoked productively; (iii) it codifies skills from successful sequences and repairs
executable code that raised exceptions; (iv) it adds memory entries to fill gaps, updates stale entries, and demotes importance for areas the agent has moved
past.

Refinement information accumulates monotonically over the episode: failure signatures observed earlier in the trajectory remain available to all subsequent
refinement passes, so refinement quality compounds with episode length, while reset-based methods restart this accumulation after each update. Continual Harness
can also target failure modes that only appear deep in an episode (late-game battles, multi-step puzzles, dialogue chains), which reset-based approaches cannot
reach by construction since each iteration resets to the initial state. Beyond these technical advantages, reset-free is also the practically dominant regime
for long-running coding agents, embodied agents, and ops tasks where free environment resets are costly or unavailable.

### 3.3 Continual Model-Harness Co-Learning Loop

Figure˜2b instantiates Continual Harness as a training loop for an open-source model. After warm-up stages (Appendix D), each online iteration runs
[MATH: <semantics><msub><mi>π</mi><msub><mi>θ</mi><mi>k</mi></msub></msub><annotation encoding="application/x-tex">\pi_{\theta_{k}}</annotation></semantics>
:MATH]
inside a live-refining harness
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>t</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{t}</annotation></semantics> :MATH]
for
[MATH: <semantics><mrow><mi>K</mi><mo>=</mo><mn>256</mn></mrow><annotation encoding="application/x-tex">K{=}256</annotation></semantics> :MATH]
steps. A pairwise process reward model (PRM)
[MATH: <semantics><mrow><mrow><mi>R</mi><mo lspace="0em" rspace="0em">​</mo><mrow><mo
stretchy="false">(</mo><msub><mi>s</mi><mi>t</mi></msub><mo>,</mo><msub><mi>a</mi><mi>t</mi></msub><mo>,</mo><mi>τ</mi><mo
stretchy="false">)</mo></mrow></mrow><mo>∈</mo><mrow><mo stretchy="false">[</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo
stretchy="false">]</mo></mrow></mrow><annotation encoding="application/x-tex">R(s_{t},a_{t},\tau)\in[0,1]</annotation></semantics> :MATH]
scores each transition over a sliding window of recent transitions (component weights in Appendix D); low-reward windows are relabeled by a frontier teacher,
and a soft SFT update on the relabeled shard produces
[MATH: <semantics><msub><mi>θ</mi><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow></msub><annotation
encoding="application/x-tex">\theta_{k+1}</annotation></semantics> :MATH]
. The loop is reset-free since the saved emulator state at the end of iteration
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
is loaded as the start of iteration
[MATH: <semantics><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">k{+}1</annotation></semantics> :MATH]
, so the model’s in-game position accumulates across training rather than restarting.

The trajectory distribution
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">𝒟</mi><mi>θ</mi></msub><annotation
encoding="application/x-tex">\mathcal{D}_{\theta}</annotation></semantics> :MATH]
depends on
[MATH: <semantics><mi>θ</mi><annotation encoding="application/x-tex">\theta</annotation></semantics> :MATH]
through the harness. The model’s actions induce
[MATH: <semantics><mi>τ</mi><annotation encoding="application/x-tex">\tau</annotation></semantics> :MATH]
, the Refiner reads
[MATH: <semantics><mi>τ</mi><annotation encoding="application/x-tex">\tau</annotation></semantics> :MATH]
to update
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>t</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{t}</annotation></semantics> :MATH]
, and
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>t</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{t}</annotation></semantics> :MATH]
in turn shapes the next observation distribution. Both the model weights
[MATH: <semantics><mi>θ</mi><annotation encoding="application/x-tex">\theta</annotation></semantics> :MATH]
and the harness state
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>t</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{t}</annotation></semantics> :MATH]
are updated by this loop, where
[MATH: <semantics><mi>θ</mi><annotation encoding="application/x-tex">\theta</annotation></semantics> :MATH]
is updated across iterations (via SFT on relabeled trajectories) and
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>t</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{t}</annotation></semantics> :MATH]
within each iteration (via the Refiner).

## 4 Experiments

We organize our experiments around the contributions from Section˜1: our GPP project results (Section˜4.2), Continual Harness closing the gap to a
hand-engineered harness (Section˜4.3), showing improvements with reset-free experience that can bootstrap runs if one does choose to reset, and continual
model-harness co-learning for open-source students (Section˜4.5). Section˜4.6 attributes these gains to in-loop refinement on each of the harness components,
and additional details are in the appendix.

### 4.1 Setup

#### Environments and metric.

We evaluate on Pokémon Red and Emerald, two RPGs in the same genre that differ in map layout, mechanics, and difficulty. We use the standardized milestone
evaluation from the PokeAgent Challenge [5]. The primary metric is cumulative button presses to milestone.

#### Harness conditions.

[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>min</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\min}</annotation></semantics> :MATH]
: frames, local text map, buttons, generic system prompt; no sub-agents, memory, or skills.
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>expert</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\mathrm{expert}}</annotation></semantics> :MATH]
: the hand-designed harness of PokeAgent [5] and fixed GPP harness with built sub-agents, A^∗ pathfinding, type chart, damage calculator, and curated
objectives.
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>CH</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\mathrm{CH}}</annotation></semantics> :MATH]
: starts from
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>min</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\min}</annotation></semantics> :MATH]
and refines during gameplay via Figure˜2; three variants: from scratch, bootstrap frozen (loads a successful from-scratch run, refinement disabled), bootstrap
updating (same bootstrap, refinement continues).

#### Models and seeds.

we use Gemini 3 variants (Pro, Flash, Flash-Lite) across all harness conditions, and for open-source transfer (Section˜4.5) we use Gemma-4 (E2B, E4B, 26B MoE,
31B dense). We use at least three seeds across all experiments. We report seed medians with per-seed traces at reduced opacity.

### 4.2 Gemini Plays Pokémon completes multiple RPGs

Our GPP project ran Gemini models live through Pokémon Blue (May 2025), Yellow Legacy on hard mode (August 2025), and Crystal without a lost end-game battle
(November 2025), making GPP the first AI system to complete multiple Pokémon RPGs. Since GPP used a mix of human designed and agent iterated harness, we
highlight specific cases where we explored harness refinement over thousands of hours of gameplay.

#### Emergent Continual Harness behavior through skills.

Our Blue-era GPP harness relied on hand-authored specialists such as Pathfinder Agent and Boulder Puzzle Strategist. From Yellow Legacy onward we replaced these
with general skills (define_agent, run_code, notepad edits) and let the model build its own harness. Unprompted behaviors included wrapping an autopress_buttons
sandbox loophole into a general press_sequence primitive, developing named multi-stage battle strategies (“Operation Zombie Phoenix” on Crystal’s final Red
fight), and authoring an explicit truth-table representation of the Goldenrod Underground switch puzzle in the notepad.

#### Quantitative harness growth.

Figure˜3 reports CRUD operations (creation, update, delete) on skill and sub-agent definitions across our Yellow Legacy run. Updates persist throughout the run
rather than converging to a fixed harness, and concentrate on a small subset of navigation and battle components. Figure˜4 reports structural metrics of one
such component, the battle_strategist_agent prompt, across successive revisions during the Elite Four phase. The prompt cycles between growth and
simplification, and undergoes a structural rewrite in which per-decision logic is absorbed into a master_battle_agent that dispatches to named sub-checks.
Across both figures the process is the same: a small set of components is repeatedly updated and periodically rewritten. Quality is established separately by
GPP’s completion record. We generalize GPP’s mixed methodology to create Continual Harness, which fully automates this process for all modules. Additional
results in Appendix B.
Refer to caption Figure 3: Yellow Legacy harness refinement is concentrated and recurrent rather than uniform. (a) Counts of CRUD operations (creation, update,
delete) on skill and sub-agent definitions, binned per 2,000 turns. The harness is updated throughout the run rather than converging to a fixed scaffold.
(b) Update counts for the five most-updated components over the same horizon. A small subset of navigation and battle components accounts for the majority of
updates. Refer to caption Figure 4: Decision-making complexity of the Yellow Legacy battle_strategist_agent prompt at successive revisions during the Elite Four
phase of the run: total nodes, decision gates, graph depth, and max fan-out. See appendix B for details.

### 4.3 Continual Harness closes the gap to a hand-engineered harness

Refer to caption Figure 5: Milestones reached vs. cumulative button presses. Red (left): 11-milestone subset sequence through Thunder Badge. Emerald (right):
9-milestone sequence through Knuckle Badge (2nd gym); x-axis capped at 8.5k. Lines stop at each run’s last monitored milestone. Thick lines: seed medians; faint
lines: individual seeds.

Figure˜5 plots milestones reached against cumulative button presses for
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>min</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\min}</annotation></semantics> :MATH]
, the three Continual Harness variants, and
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>expert</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\mathrm{expert}}</annotation></semantics> :MATH]
. On both games, Continual Harness substantially reduces the button-press cost of every monitored milestone relative to
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>min</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\min}</annotation></semantics> :MATH]
and recovers a majority of the
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>min</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\min}</annotation></semantics> :MATH]
-to-expert efficiency gap, without access to the game decompilation, the milestone schedule, or any of the hand-built sub-agents that constitute
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>expert</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\mathrm{expert}}</annotation></semantics> :MATH]
. The residual gap to the expert harness concentrates in dialogue-heavy gym interiors and multi-turn battle strategy, components Continual Harness does not yet
synthesize reliably; we attribute these to specific refinement targets in Section˜4.6. On Red, the bootstrap-updating variant is more efficient than
from-scratch at every milestone, indicating that the refinement signal compounds within the episode: a harness refined in a prior run accelerates the next even
when the game state itself resets. Thus, automated refinement over harness components recovers a substantial fraction of the efficiency of a hand-engineered
harness starting from a minimalist interface.

### 4.4 Continual Harness gain depends on model capability

Refer to caption Figure 6: Emerald cost–completion Pareto plane. Filled markers: individual 24-hour seeds. Ringed markers: per-cell medians. Dashed staircase:
cost-monotone Pareto frontier. Y axis: fraction of the 31-milestone Emerald set reached; X axis: Gemini API spend (log scale, cached input at
[MATH: <semantics><mrow><mn>25</mn><mo>%</mo></mrow><annotation encoding="application/x-tex">25\%</annotation></semantics> :MATH]
).

Figure˜6 compares every Emerald run from every model-harness cell with respect to cost and completion. On Pro, Continual Harness is strictly Pareto-dominant
over
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>min</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\min}</annotation></semantics> :MATH]
: from-scratch
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>CH</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\mathrm{CH}}</annotation></semantics> :MATH]
reaches
[MATH: <semantics><mrow><mn>100</mn><mo>%</mo></mrow><annotation encoding="application/x-tex">100\%</annotation></semantics> :MATH]
of milestones at a $130 median, against
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>min</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\min}</annotation></semantics> :MATH]
at
[MATH: <semantics><mrow><mn>98</mn><mo>%</mo></mrow><annotation encoding="application/x-tex">98\%</annotation></semantics> :MATH]
for $215, a
[MATH: <semantics><mrow><mi></mi><mo>∼</mo><mrow><mn>40</mn><mo>%</mo></mrow></mrow><annotation encoding="application/x-tex">\sim 40\%</annotation></semantics>
:MATH]
cost reduction with no completion loss. The two bootstrap variants on Pro reach
[MATH: <semantics><mn>96</mn><annotation encoding="application/x-tex">96</annotation></semantics> :MATH]
–
[MATH: <semantics><mrow><mn>100</mn><mo>%</mo></mrow><annotation encoding="application/x-tex">100\%</annotation></semantics> :MATH]
of milestones at $110–$140. On Flash, harness benefit is high variance: bootstrap-updating reaches
[MATH: <semantics><mrow><mn>80</mn><mo>%</mo></mrow><annotation encoding="application/x-tex">80\%</annotation></semantics> :MATH]
at $42, marginally above
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>min</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\min}</annotation></semantics> :MATH]
at
[MATH: <semantics><mrow><mn>77</mn><mo>%</mo></mrow><annotation encoding="application/x-tex">77\%</annotation></semantics> :MATH]
for $30, while from-scratch and bootstrap-frozen variants have a higher variance. Flash-Lite with
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>min</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\min}</annotation></semantics> :MATH]
reaches
[MATH: <semantics><mrow><mn>20</mn><mo>%</mo></mrow><annotation encoding="application/x-tex">20\%</annotation></semantics> :MATH]
at $11; every Continual Harness variant on Flash-Lite falls to
[MATH: <semantics><mn>3</mn><annotation encoding="application/x-tex">3</annotation></semantics> :MATH]
–
[MATH: <semantics><mrow><mn>13</mn><mo>%</mo></mrow><annotation encoding="application/x-tex">13\%</annotation></semantics> :MATH]
at comparable or higher cost. The harness gains requires a model that will sufficiently utilize the harness components properly.

### 4.5 Open-source students co-learn with a refining harness

We test whether an open-source model improves its gameplay using the self-refining harness with reset-free training (batch size
[MATH: <semantics><mrow><mi></mi><mo>=</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">=1</annotation></semantics> :MATH]
). The model is first primed by supervised fine-tuning on frontier Continual Harness trajectories and an offline GRPO stage on a per-step process reward;
neither warm-up stage produces meaningful milestone advancement on its own (Appendix D), and the live in-game gains we report here begin only at the co-learning
stage. Each training iteration is a
[MATH: <semantics><mrow><mi>K</mi><mo>=</mo><mn>256</mn></mrow><annotation encoding="application/x-tex">K{=}256</annotation></semantics> :MATH]
-step DAgger [15, 8] rollout through the full Continual Harness (memory, skills, sub-agents, and prompt all evolving via Figure˜2), followed by a
process-reward-model scoring pass, a Gemini-3.1-pro teacher relabel of low-reward windows, and a soft SFT update on the relabeled shard. The training loop is
reset-free: the emulator state at the end of iteration
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
is loaded as the start of iteration
[MATH: <semantics><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">k{+}1</annotation></semantics> :MATH]
, so each curve in Figure˜7 is a single agent’s in-game trajectory traversed across its own training, not an aggregate over independent rollouts.
Refer to caption Figure 7: Reset-free DAgger+PRM training drives sustained milestone progress on Pokémon Red. Milestone index reached versus training iteration
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
for the five advancing runs; the broken y-axis labels each band’s start and end. Filled dots: beginning of game. Open rings: mid-game checkpoint. Stars:
judge-verified advances.
[MATH: <semantics><mrow><mo>+</mo><mi>N</mi></mrow><annotation encoding="application/x-tex">+N</annotation></semantics> :MATH]
: net objective gain. Dashed line: untrained Gemma-4 baseline (zero advance beyond the starting milestone). Teacher model: Gemini-3.1-pro.

Figure˜7 shows that the model’s live in-game position advances across training iterations on every plotted run, both from the beginning of the game and from
mid-game checkpoints. Both staircase types share the same qualitative shape, indicating that the training signal that drives the model forward from the start of
the game also drives it forward from advanced checkpoints; the training procedure is not specific to the early-game distribution. As a negative control,
cross-family Qwen3.5 (27B, 35B) without the supervised warm-up stage produces parseable tool calls but cannot leave the starting area in a live rollout
(Appendix D.2), ruling out a rollout-protocol artifact. Together with the cross-checkpoint generalization, these results support the co-learning claim: an
open-source model trained on data collected from its own play through a continually refining harness improves its in-game position iteration over iteration,
without ever resetting the environment. Per-run identifiers, hyperparameters, and the per-iteration process-reward decomposition are reported in Appendix D.4.

### 4.6 Skills measurably self-improve toward an oracle

Refer to caption Figure 8: Pathfinding skill mechanism. (Left) Path-cost deficit of the top-10% evolved navigation skill set (Gemini 3.1 Pro) relative to the
Dijkstra oracle over a 24-hour run on warp-to-warp obstacle-navigation tasks; lower is better, dashed line at 0% marks the oracle. (Right) Cumulative
navigation-skill invocations against button presses across the same conditions.

We score refined navigation skills by their path cost relative to a Dijkstra oracle. This gives a direct measure of skill self-improvement, independent of
end-task efficiency. Figure˜8 reports this measurement on warp-to-warp obstacle-aware navigation between fixed map entry and exit points, where greedy
open-field hopping fails. Sub-agents, memory, prompt, and reset-free bootstrap transfer are deferred to Appendices C.1 and C.2.

[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>min</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\min}</annotation></semantics> :MATH]
never invokes a navigation skill; every Continual Harness condition accumulates hundreds of invocations over a 24-hour run (Figure˜8, right). On from-scratch
runs the path-cost deficit falls from a near-half-cost penalty at the start to single digits early on and stays there (Figure˜8, left). This improvement is
in-loop and reset-free: failures from earlier invocations are diagnosed by the Refiner and the affected skills are repaired before later invocations within the
same episode. Bootstrap-updating inherits a refined skill set and matches or outperforms bootstrap-frozen throughout, so continued refinement still adds value
on top of an inherited set; bootstrap-frozen’s flat trajectory bounds inheritance without further refinement.

## 5 Related Work

### 5.1 Agentic Harnesses and Scaffolding

Agentic harnesses for coding [2, 21, 19] and assistant tasks [13] stall on embodied RPGs without domain scaffolding [5]. Concurrent prompt-optimization [1, 14,
10] and reflective self-improvement [17, 12] optimize harness components or reflect on trajectories between episodes; Continual Harness edits the full harness
state
[MATH: <semantics><mrow><mo stretchy="false">(</mo><mi>p</mi><mo>,</mo><mi class="ltx_font_mathcaligraphic">𝒢</mi><mo>,</mo><mi
class="ltx_font_mathcaligraphic">𝒦</mi><mo>,</mo><mi class="ltx_font_mathcaligraphic">ℳ</mi><mo stretchy="false">)</mo></mrow><annotation
encoding="application/x-tex">(p,\mathcal{G},\mathcal{K},\mathcal{M})</annotation></semantics> :MATH]
in place mid-episode from partial trajectory windows, without resets.

### 5.2 Autonomous Agents in Games

LLM-based game agents either build their own tooling during play [20, 3] or pair the LLM with a hand-designed planner [7]. The PokeAgent Challenge [5] provides
the canonical embodied-RPG benchmark and expert harness. Our Gemini Plays Pokémon (GPP) runs across Blue, Yellow Legacy, and Crystal show that human-supervised
harness refinement completes multiple full RPGs; Continual Harness automates this process.

### 5.3 Reset-Free Training, In-Context Learning, and Process Rewards

Reset-free reinforcement learning [4] addresses environments without resets. In-context reinforcement learning [18, 6] and recursive language model methods [25,
23] perform implicit improvement and structured multi-call reasoning over context; Continual Harness writes structured edits to the full harness state at depth
1. Process reward models [22, 11], group-relative policy gradient [16], and STaR-style self-training [24] provide finer-grained signals than sparse episode
reward; our co-learning pipeline warms up via SFT and offline GRPO, then runs an online loop where a frontier teacher relabels low-reward windows of the
model’s own rollouts inside a live-refining harness for soft SFT updates.

## 6 Discussion

Continual Harness builds and refines its own scaffolding from a minimal environment interface, without resets, and recovers a majority of the gap to a
hand-engineered expert harness on embodied Pokémon play. The same alternation runs at both timescales: at inference the agent acts and the Refiner edits the
harness in place; at training the online co-learning loop runs the model inside that same live-refining harness, so the trajectory distribution the model learns
from co-adapts with its own policy.

A capability floor exists below which the refinement loop cannot bootstrap: Flash-Lite stalls below
[MATH: <semantics><mrow><mn>20</mn><mo>%</mo></mrow><annotation encoding="application/x-tex">20\%</annotation></semantics> :MATH]
on Emerald, and every Continual Harness variant on Flash-Lite underperforms the minimalist baseline. Our co-learning experiments couple a frontier-model teacher
to an open-source model; the framework extends to the same model serving both roles, but the open-source models we evaluated (Gemma-4 up to 31B) are not yet
capable enough to act as both teacher and trainee.

The co-learning loop is not saturated by our experiments: we report sustained milestone progress over the training horizon we ran but did not establish a
convergence point. We restrict attention to reset-free training, where the emulator state at the end of iteration
[MATH: <semantics><mi>k</mi><annotation encoding="application/x-tex">k</annotation></semantics> :MATH]
is loaded as the start of iteration
[MATH: <semantics><mrow><mi>k</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">k{+}1</annotation></semantics> :MATH]
; the same loop applies to traditional batch accumulation with resets, and a head-to-head comparison between the two regimes on the same task remains open.

Acknowledgement

The authors acknowledge the support of National Science Foundation Graduate Research Fellowship Program under Grant No. DGE-2039656, computational resources
from Princeton Language and Intelligence (PLI), and Google DeepMind.

References

  * [1] L. A. Agrawal, S. Tan, D. Soylu, N. Ziems, R. Khare, K. Opsahl-Ong, A. Singhvi, H. Shandilya, M. J. Ryan, M. Jiang, et al. (2025) Gepa: reflective
prompt evolution can outperform reinforcement learning. arXiv preprint arXiv:2507.19457. Cited by: §1, §3.1, §5.1.
  * [2] Anthropic (2025) Claude code. Note: https://docs.anthropic.com/en/docs/claude-code Cited by: §1, §5.1.
  * [3] Anthropic (2025) Claude plays Pokémon. Note: https://www.twitch.tv/claudeplayspokemon Cited by: §5.2.
  * [4] A. Gupta, J. Yu, T. Z. Zhao, V. Kumar, A. Rovinsky, K. Xu, T. Devlin, and S. Levine (2021) Reset-free reinforcement learning via multi-task learning:
learning dexterous manipulation behaviors without human intervention. In 2021 IEEE international conference on robotics and automation (ICRA), pp. 6664–6671.
Cited by: §5.3.
  * [5] S. Karten, J. Grigsby, T. Upaa Jr, J. Bae, S. Hong, H. Jeong, J. Jung, K. Kerdthaisong, G. Kim, H. Kim, et al. (2026) The pokeagent challenge:
competitive and long-context learning at scale. arXiv preprint arXiv:2603.15563. Cited by: Appendix A, §1, §2.2, §4.1, §4.1, §5.1, §5.2.
  * [6] S. Karten, W. Li, Z. Ding, S. Kleiner, Y. Bai, and C. Jin (2025) Llm economist: large population models and mechanism design in multi-agent generative
simulacra. arXiv preprint arXiv:2507.15815. Cited by: §5.3.
  * [7] S. Karten, A. L. Nguyen, and C. Jin (2025) PokéChamp: an expert-level minimax language agent. arXiv preprint arXiv:2503.04094. Cited by: §5.2.
  * [8] S. Karten, A. L. Nguyen, S. Milani, and C. Jin (2026) Small experts, big students: distilling long-horizon RL policies into LLM agents via imitation
learning. Cited by: §D.1, §D.4, §4.5.
  * [9] keepingiticy (2024) Pokémon Emerald any% glitchless speedrun (mgba). Note: Speedrun.comAny@misc{keepingiticy2024emerald, author = {{keepingiticy}},
title = {Pok\'{e}mon {Emerald} Any\% Glitchless Speedrun (mGBA)}, year = {2024}, howpublished = {Speedrun.com}, url =
{https://www.speedrun.com/pkmnemerald/runs/yvpvw74y}, note = {Any% 2nd place record as of April 2026}} External Links: Link Cited by: Figure 9, Figure 9.
  * [10] Y. Lee, R. Nair, Q. Zhang, K. Lee, O. Khattab, and C. Finn (2026) Meta-harness: end-to-end optimization of model harnesses. arXiv preprint
arXiv:2603.28052. Cited by: §5.1.
  * [11] H. Lightman, V. Kosaraju, Y. Burda, H. Edwards, B. Baker, T. Lee, J. Leike, J. Schulman, I. Sutskever, and K. Cobbe (2023) Let’s verify step by step.
In The twelfth international conference on learning representations, Cited by: §5.3.
  * [12] A. Madaan, N. Tandon, P. Gupta, S. Hallinan, L. Gao, S. Wiegreffe, U. Alon, N. Dziri, S. Prabhumoye, Y. Yang, et al. (2023) Self-refine: iterative
refinement with self-feedback. Advances in neural information processing systems 36, pp. 46534–46594. Cited by: §5.1.
  * [13] Nous Research (2026) Hermes agent. Note: https://github.com/NousResearch/hermes-agentAccessed: 2026-03-22 Cited by: §5.1.
  * [14] K. Opsahl-Ong, M. J. Ryan, J. Purtell, D. Broman, C. Potts, M. Zaharia, and O. Khattab (2024) Optimizing instructions and demonstrations for
multi-stage language model programs. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pp. 9340–9366. Cited by: §3.1,
§5.1.
  * [15] S. Ross, G. Gordon, and D. Bagnell (2011) A reduction of imitation learning and structured prediction to no-regret online learning. In Proceedings of
the fourteenth international conference on artificial intelligence and statistics, pp. 627–635. Cited by: §D.1, §D.4, §4.5.
  * [16] Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y. Li, Y. Wu, et al. (2024) Deepseekmath: pushing the limits of mathematical
reasoning in open language models. arXiv preprint arXiv:2402.03300. Cited by: §D.1, §5.3.
  * [17] N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao (2023) Reflexion: language agents with verbal reinforcement learning. Advances in neural
information processing systems 36, pp. 8634–8652. Cited by: §5.1.
  * [18] K. Song, A. Moeini, P. Wang, L. Gong, R. Chandra, S. Zhang, and Y. Qi (2025) Reward is enough: llms are in-context reinforcement learners. arXiv
preprint arXiv:2506.06303. Cited by: §5.3.
  * [19] P. Steinberger (2025) OpenClaw: an open-source autonomous AI agent. Note: https://github.com/psteinb/openclawOriginally released as Clawdbot, November
2025 Cited by: §1, §5.1.
  * [20] G. Wang, Y. Xie, Y. Jiang, A. Mandlekar, C. Xiao, Y. Zhu, L. Fan, and A. Anandkumar (2023) Voyager: an open-ended embodied agent with large language
models. arXiv preprint arXiv:2305.16291. Cited by: §5.2.
  * [21] X. Wang, B. Li, Y. Song, F. F. Xu, X. Tang, M. Zhuge, J. Pan, Y. Song, B. Li, J. Singh, H. H. Tran, F. Li, R. Ma, M. Zheng, B. Qian, Y. Shao, N.
Muennighoff, Y. Zhang, B. Hui, J. Lin, R. Brennan, H. Peng, H. Ji, and G. Neubig (2024) Openhands: an open platform for ai software developers as generalist
agents. arXiv preprint arXiv:2407.16741. Cited by: §1, §5.1.
  * [22] Y. Wang, X. Chen, X. Jin, M. Wang, and L. Yang (2026) Openclaw-rl: train any agent simply by talking. arXiv preprint arXiv:2603.10165. Cited by: §D.1,
§5.3.
  * [23] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao (2022) React: synergizing reasoning and acting in language models. arXiv preprint
arXiv:2210.03629. Cited by: §5.3.
  * [24] E. Zelikman, Y. Wu, J. Mu, and N. Goodman (2022) Star: bootstrapping reasoning with reasoning. Advances in Neural Information Processing Systems 35,
pp. 15476–15488. Cited by: §5.3.
  * [25] A. L. Zhang, T. Kraska, and O. Khattab (2025) Recursive language models. arXiv preprint arXiv:2512.24601. Cited by: §5.3.

Appendix Contents

## Appendix A Pokémon Environment

We run experiments on three Pokémon titles: Pokémon Red (Game Boy, 1996; we use the re-release compatible with the Game Boy Advance emulator), Pokémon Crystal
(Game Boy Color, 2000), and Pokémon Emerald (Game Boy Advance, 2004). All three are single-player, turn-based role-playing games with long-horizon structure:
overworld navigation, NPC dialogue, turn-based Pokémon battles, inventory management, and gated objectives (badges, plot milestones).

#### Interface.

The emulator exposes a screen buffer (rendered at the native resolution of each game: 160
[MATH: <semantics><mo>×</mo><annotation encoding="application/x-tex">\times</annotation></semantics> :MATH]
144 for Red/Crystal, 240
[MATH: <semantics><mo>×</mo><annotation encoding="application/x-tex">\times</annotation></semantics> :MATH]
160 for Emerald), which we upscale
[MATH: <semantics><mrow><mn>2</mn><mo lspace="0.222em">×</mo></mrow><annotation encoding="application/x-tex">2\times</annotation></semantics> :MATH]
for the vision-language model, and a discrete button channel with eight inputs: UP, DOWN, LEFT, RIGHT, A, B, START, SELECT. Every observation step advances the
emulator by a fixed number of frames (120) so that menu animations, battle text, and walking animations resolve between successive agent decisions.

#### Text map.

Because vision-language models have known difficulties with fine-grained spatial reasoning over pixel grids, we provide an ASCII text-map
[MATH: <semantics><msub><mi>m</mi><mi>t</mi></msub><annotation encoding="application/x-tex">m_{t}</annotation></semantics> :MATH]
alongside the frame observation
[MATH: <semantics><msub><mi>o</mi><mi>t</mi></msub><annotation encoding="application/x-tex">o_{t}</annotation></semantics> :MATH]
(Section˜2). The text map is derived from emulator memory and describes the visible tile grid around the player: walkable tiles (.), walls (#), interactable
tiles (?, e.g., signs and talkable objects), NPCs (N), ledges, and the player’s position and facing. The map covers the current on-screen area plus a small
margin of tiles just off-screen so the agent can plan one step ahead. The text map contains no walkthrough, no objective list, and no global map information
beyond what is currently visible; it compensates for the VLM’s limited spatial reasoning, not for domain knowledge.

#### Milestones and the button-press metric.

We use the milestone sequence from the PokeAgent Challenge [5]: a dense, canonical ordering of completion events that a run reaches roughly monotonically as it
progresses through the game. Emerald has 31 canonical milestones through the completion of the 3rd gym, Red has 18 canonical milestones through the completion
of the 3rd gym. The primary cost metric is cumulative button presses, not tool calls: a single press_buttons invocation emitting the list [A, A, DOWN] counts as
three presses. This rewards compression in the action channel independent of how the harness structures its tool calls, and it makes
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>min</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\min}</annotation></semantics> :MATH]
(one button per step) directly comparable to harnesses that batch multi-step presses into one tool call.
Refer to caption Figure 9: Emerald Speedrunning Route. Milestones from Littleroot Town (1) to aquiring the Dynamo Badge (31), with game frames from each
waypoint. The geographic overview (right) maps key locations. This series of milestones require substantial exploration and backtracking; agents must navigate
branching paths, and manage nonlinear dependencies between objectives. The current world record speedrun completes this segment in 1:00:57 minutes [9]. Refer to
caption Figure 10: Pokémon Red Speedrunning Route. Milestones from obtaining starter Pokémon (1) to aquiring the Thunder Badge (18), with game frames from each
waypoint. The geographic overview (right) maps key locations. This series of milestones require substantial exploration and backtracking; agents must navigate
branching paths, and manage nonlinear dependencies between objectives. The current world record speedrun completes this segment in 43:04 minutes; see
https://www.speedrun.com/pkmnredblue.^0^0footnotetext: website: https://www.speedrun.com/pkmnredblue

#### Memory reader.

The PokeAgent emulator exposes a memory reader that reads structured game state (party, inventory, party HP, current map ID, dialogue text, battle status) from
the emulator RAM. Tools such as the expert harness’s A^∗ pathfinder, battle type chart, and damage calculator use this reader. For
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>min</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\min}</annotation></semantics> :MATH]
and
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>CH</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\mathrm{CH}}</annotation></semantics> :MATH]
, the memory reader is exposed only through the text-map
[MATH: <semantics><msub><mi>m</mi><mi>t</mi></msub><annotation encoding="application/x-tex">m_{t}</annotation></semantics> :MATH]
derivation and a handful of general primitives (e.g., get_party_hp); not through pre-wired domain tools.

## Appendix B Gemini Plays Pokémon: Additional Evidence

Figures˜3 and 4 in the main text show Yellow Legacy harness updates and battle-agent structural complexity. This appendix collects the remaining GPP evidence.
Refer to caption Figure 11: Crystal head-to-head comparison under the same harness. (Top) per-500-turn updates on skills and sub-agents for Gemini 2.5 Pro
(left) and 3 Pro (right). (Bottom) top-5 most-updated components per model.
   Opponent    Lifetime attempts          Notes
   Lorelei     18                Reached Bruno 15+ times
    Bruno      20                Reached Agatha 12+ times
    Agatha     18                Reached Lance 12+ times
    Lance      19                Reached Champion 4 times
Champion Pixel 4                 Victory on attempt 4
Table 1: Yellow Legacy Elite Four lifetime attempt totals. The retries were accompanied by increasingly structured battle prompts (Figure˜4) and persistent
written memory, producing a text-encoded decision process across the gauntlet.

#### Model comparison on Crystal.

On Pokémon Crystal under the same harness, Gemini 3 Pro reached comparable early milestones using roughly half the turns and
[MATH: <semantics><mrow><mi></mi><mo>∼</mo><mrow><mn>60</mn><mo>%</mo></mrow></mrow><annotation encoding="application/x-tex">\sim 60\%</annotation></semantics>
:MATH]
fewer tokens than Gemini 2.5 Pro. The largest divergence occurred at Olivine Lighthouse: 3 Pro initially treated the pits as dangerous, then stepped into one
after exhausting safer hypotheses and cleared the tower, while 2.5 Pro became trapped in a loop of bad assumptions and spent 16,403 turns before obtaining the
Fog Badge. Figure˜11 shows the corresponding update and fixation patterns.

#### Failure modes that motivated automation.

GPP also exposed recurring failure modes that the human refiner had to repair between runs: assumptions made without verification (the Goldenrod puzzle ran for
days because the agent skipped post-battle NPC dialogue containing the missing hint), brittle tool calls with missing parameters, and limited parallel goal
pursuit. These are precisely the failures that Continual Harness’s mid-episode refinement targets.

### B.1 Yellow Legacy Battle-Agent Evolution Checkpoints

Figure˜4 in the main text plots four graph metrics across the 14 structural checkpoints we extracted from custom_agents.json over the Elite Four window. For
completeness we include the mermaid-rendered decision graph behind each checkpoint across two figures: Figure˜12 shows four canonical checkpoints, and Figure˜13
shows the remaining ten. Every chart uses the same renderer and palette, so structural differences reflect prompt changes, not rendering variance. Node colors
encode semantic role: entry, analysis, decision gate, terminal action.
Refer to caption

a1. Turn 138119: baseline veto swarm
Refer to caption

b1. Turn 139085: compact rebuild
Refer to caption

c1. Turn 151441: screen-text + prediction
Refer to caption

d1. Turn 156631: master-agent intro
Figure 12: The four Yellow Legacy battle-agent checkpoints marked a1/b1/c1/d1 on the complexity plot in Figure˜4. These span the arc from a linear survival-gate
chain (a1), through a hard-reset compact rebuild (b1), to a rebuilt-bigger screen-text-grounded program (c1), and finally to a master-agent decomposition (d1)
that dispatches to five named sub-checks.
Refer to caption

Turn 138914: level-disparity veto
Refer to caption

Turn 138916: chart-prune reset
Refer to caption

Turn 138923: veto consolidation
Refer to caption

Turn 153601: last-stand strategist
Refer to caption

Turn 138925: minimal fallback
Refer to caption

Turn 141323: context + viability
Refer to caption

Turn 146358: current opponent + HP
Refer to caption

Turn 147516: free turn + coverage
Refer to caption

Turn 159079: hierarchical master
Refer to caption

Turn 160511: final master
Figure 13: The remaining ten Yellow Legacy battle-agent checkpoints, grouped by natural aspect. Row 1: long-chain variants around the first complexity spike and
the late “last-stand” rewrite. Row 2: medium-hierarchy checkpoints across the rebuild-and-grow-again window. Row 3: the two wide master-agent variants that
extend the decomposition introduced at checkpoint 12.

### B.2 Crystal Battle Advisor Evolution Checkpoints

Like the Yellow Legacy Elite Four window, the Crystal run required heavy prompt iteration during its Battle Tower attempt. We extracted 10 structural
checkpoints from custom_agents.json for the battle_advisor agent. Figure˜14 shows the first six checkpoints (turns 30k–33k); Figure˜15 shows the remaining four
(turns 33k–36k).
Refer to caption

Turn 30242: baseline matchup recommender
Refer to caption

Turn 30694: counter mechanic hardening
Refer to caption

Turn 31220: battle tower legality
Refer to caption

Turn 31906: fatal weakness check
Refer to caption

Turn 32755: role-based team policy
Refer to caption

Turn 33306: survival check
Figure 14: Crystal battle_advisor checkpoints 1–6 from the Battle Tower window. The graphs trace the early evolution from a baseline matchup recommender (1)
through legality and weakness-check additions (2–4) to role-based and survival rules (5–6).
Refer to caption

Turn 33619: max stats & switch legality
Refer to caption

Turn 34813: empirical override & paranoia
Refer to caption

Turn 35466: bahamut reconfiguration
Refer to caption

Turn 36217: explicit speed calculation
Figure 15: Crystal battle_advisor checkpoints 7–10. The late-window evolution adds switch-legality bookkeeping (7), an empirical-override / paranoia layer (8),
a team-specific reconfiguration (9), and an explicit speed calculation rule (10).

### B.3 Case Study: The Power Plant Route Loop

During the Pokémon Yellow Legacy run, the AI agent encountered a 1,003-turn stagnation loop on Map ID 4 (Route 4, near Cerulean City). Spanning approximately
3.5 hours on August 29, 2025, this incident provides a documented example of failure modes in runtime tool generation, schema mismatch during prolonged stalls,
and the limits of the agent’s context horizon for error recovery.

The sequence began when the agent decided its goal was to travel to the Power Plant. To do so, it opened the menu to use the HM “Fly.” After repeatedly
overshooting its target in the party menu, the agent utilized its tool-generation capabilities to bypass the mechanical inefficiency:
 1. 1.
It deleted its existing get_next_pokemon_press tool.
 2. 2.
It wrote a new tool called fly_menu_navigator, setting its autopress_buttons flag to true.
 3. 3.
It added a directive to its persistent memory: “I must use the fly_menu_navigator tool as intended and trust its output. The get_next_pokemon_press tool was
deleted to make space for fly_menu_navigator and should not have been used. This also highlights a failure to immediately use a newly defined tool.”

#### Schema Mismatch and Execution Loop.

The agent invoked the tool, passing in the current screen text and its target destination (‘‘Power Plant’’). However, the generated tool call did not match the
meta-harness execution schema. To execute a tool with autopress_buttons: true, the agent’s JSON output requires the buttons_to_press array to be explicitly set
to ["tool"]. Instead, the agent logically deduced that it needed to scroll down the list of cities, populating the array with ["Down"]. Because the meta-harness
ignores the tools_to_call array if the "tool" button is not explicitly pressed, the system simply pressed Down on the emulator and returned control.

Failing to detect the schema mismatch, the agent recorded in its internal reasoning that the custom tool was successfully executing and returning "Down" as the
optimal path. It repeated this exact payload 842 times.

#### Internal State vs. Execution Reality.

Throughout the 3.5-hour loop, the agent’s internal thoughts logs indicated it was actively evaluating its progress, despite the environment remaining largely
static.

Turn
[MATH: <semantics><mo>∼</mo><annotation encoding="application/x-tex">\sim</annotation></semantics> :MATH]
172115: “I have completed the mandatory self-assessment… 11. Untested Assumptions & Confirmation Bias: My assumption about the Power Plant being a Fly
destination will be tested by cycling through the menu. I am mindful of confirmation bias. My plan for this turn is to continue navigating the Fly menu… I will
use the fly_menu_navigator tool to take another step towards ’POWER PLANT’.”

The agent’s internal reasoning indicated it was testing an assumption, but it was caught in a schema error and lacked the necessary game knowledge (the Power
Plant is not a valid Fly destination in Generation 1).

#### Loop Termination.

The loop terminated after 1,003 consecutive turns once the agent had manually scrolled through all Kanto cities. When the cursor looped back to “LAVENDER
TOWN” (its starting point), the agent re-evaluated its state:

Turn
[MATH: <semantics><mo>∼</mo><annotation encoding="application/x-tex">\sim</annotation></semantics> :MATH]
172322: “I am in the Fly menu, and the current highlighted location is LAVENDER TOWN. My goal is to reach the Power Plant. Since Lavender Town is the current
map, I have cycled through all available Fly destinations, meaning the Power Plant is not a direct Fly destination. I need to exit the Fly menu and walk to
Route 10…”

The agent stopped calling the custom tool, backed out of the menus, and manually walked north to Route 10.

#### Observations.

  * •
Context Horizon Limits: Tool generation primarily occurred within the first 50-200 turns of encountering a new bottleneck. Beyond 500 turns in a stall, the
agent ceased tool creation and reverted to repeated execution patterns.
  * •
Schema Fragility: When enforcing new rules via persistent memory, the model remained susceptible to schema mismatch, executing actions that did not align with
its intended tool design.
  * •
Feedback Blindness: The assumption that the new tool was functioning correctly caused the agent to ignore standard environmental feedback and anomaly detection
mechanisms for an extended period.

## Appendix C Harness Ablations

This appendix gives the full per-component attribution behind the
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>min</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\min}</annotation></semantics> :MATH]
-to-
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>CH</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\mathrm{CH}}</annotation></semantics> :MATH]
progression gap (Section˜4.6) and the reset-free bootstrap transfer results.

### C.1 Mechanism Attribution

#### C.1.1 Pathfinding skills

Figure˜8 in the main text shows the Dijkstra-oracle ratio and cumulative skill calls. Below we give the measurement details and the residual structure the
main-text summary omits.

For each first-traversal segment between consecutive milestones, we compute a BFS-optimal path length on the union of tiles observed by any run of that game on
that map, and divide the agent’s issued button presses within the segment by that optimum. Dialogue and battle presses are filtered out so the comparator only
sees navigation. The ordering inverts inside gyms where dialogue and puzzle state dominate over navigation, which is why the residual gap to
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>expert</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\mathrm{expert}}</annotation></semantics> :MATH]
in the main-text progression figure concentrates there. The refined library is heavily biased toward BFS and A^∗ wrappers because saved presses on navigation
translate directly into faster milestones, the strongest local signal the refinement loop sees.
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>expert</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\mathrm{expert}}</annotation></semantics> :MATH]
routes navigation through a pre-built A^∗ tool not visible to the run_skill counter, which is why its curve sits at the floor in the main-text right panel. Most
of the
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>min</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\min}</annotation></semantics> :MATH]
-to-
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>CH</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\mathrm{CH}}</annotation></semantics> :MATH]
delta is absorbed by the skill library alone.

#### C.1.2 Skill debugging

Refer to caption
Refer to caption
Figure 16: Left: per-seed skill lifetime for the three Red from-scratch
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>CH</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\mathrm{CH}}</annotation></semantics> :MATH]
runs. Markers are add, update, run_skill (green if no re-update within 5 steps, red otherwise), and delete. Right: create-and-forget funnel across both games
and both
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>CH</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\mathrm{CH}}</annotation></semantics> :MATH]
bootstrap variants.

For every persisted skill that sees at least one skills_updated event in the refinement log, we compute the rolling success rate over a window of invocations
immediately before and immediately after each update. We also track the create-to-succeed funnel: skills authored, invoked at all, invoked repeatedly, and ever
successful. Reset-free refinement produces dramatic repairs on the skills the agent actually relies on, and the repair happens in the same episode where the
failure occurred. Figure˜16 shows this with two complementary views. The left panel is per-seed skill lifetime: each skill occupies one lane, markers are
add/update/run/delete events, and the update-to-next-execute edge is drawn so each debug iteration reads as an update followed by a run. The right panel is the
create-and-forget funnel: most authored skills are never invoked, a small working set absorbs the bulk of calls, and even fewer see success. The refinement loop
therefore triages: it repairs the skills the agent depends on, tolerates regressions on unused ones, and accepts a long create-and-forget tail. This is the
argument for reset-free operation over reset-based baselines: the failure record and the repair sit inside the same trajectory, so the loop closes within a run
rather than across resets.

#### C.1.3 Sub-agent handoffs

Refer to caption Figure 17: Sub-agent handoffs. (a) Cumulative approximate tokens by role (orchestrator solid, sub-agent dashed). (b) Cumulative
execute_custom_subagent count. (c) Per-task-type handoff success: exit is the percent of spans ending via return_to_orchestrator; focus is the percent of
returns where the orchestrator either pursued the pre-handoff objective or crossed a milestone within ten subsequent steps.

We segment each run into spans of orchestrator execution and sub-agent execution, track approximate per-step input tokens from prompt length, and label each
sub-agent span by task type. Sub-agent handoffs serve two roles for the harness: they keep per-step cost low by giving the sub-agent a narrow specialized
context, and they let the orchestrator resume its prior objective after the sub-agent returns. Figure˜17 makes both points visible. The left panel plots
orchestrator tokens and sub-agent tokens on a shared step axis; the sub-agent curve sits about an order of magnitude below the orchestrator curve throughout,
which is the per-step saving the harness buys by partitioning context. The middle panel tracks cumulative handoff counts per condition; bootstrap-updating
tracks from-scratch closely throughout the run, with a small plateau gap by run end. The right panel scores post-return behavior per task type; clean-return and
on-task-recovery rates sit near the top of the scale for navigation, dialogue, and menu tasks. The harness rather than the raw model carries most of the
long-horizon performance: once the orchestrator can delegate to cheap specialized contexts and trust the return, long tasks become tractable with far fewer
tokens than the raw context would imply.

#### C.1.4 Memory reuse

Refer to caption Figure 18: process_memory use inside the first real bottleneck of each game: Mauville Gym (Emerald, left column) and Mt Moon (Red, right
column). One representative seed per condition. Top row: per-run timeline where each marker is a process_memory tool call at the step it fired; color encodes
provenance of the memory entry. Bottom row: the same ops aggregated into a stacked composition bar.

Every orchestrator step prompt lists the IDs and titles of all stored memories under a LONG-TERM MEMORY OVERVIEW section, so the agent sees the full catalog for
free. The question is whether the agent pulls on that catalog: requests the full content of an entry via process_memory, invokes a memorized skill, or cites an
entry ID in its reasoning. We measure this pull rate as the fraction of available entries ever referenced in an episode, and we localize reads to the milestone
windows where the agent should need them: Mauville Gym on Emerald, Mt Moon on Red. Memory is leveraged once the library is both mature and inherited
(Figure˜18): bootstrap runs, which load a from-scratch memory store at the start, consult it actively inside the gym and cave segments, while from-scratch runs
write many entries and rarely reach back for them. The reference rate remains low in absolute terms, which we report honestly; most authored entries sit unused.
The transferable unit of the framework is therefore the harness across runs, not a single episode, and an explicit reuse prior is a natural next step.

### C.2 Reset-Free Bootstrap Transfer

The bootstrap-updating variant tests whether the transferable unit is a single episode or the harness across episodes. On Emerald, every store the agent
exercises during a bootstrap-updating run still targets the inherited harness. On Red, memory and skill invocations stay inherited, but the bootstrap-updating
agent collapses its sub-agent budget to a handful of calls, and the few it makes cite IDs not present in the bootstrap. When that collapse happens, the
milestone staircase regresses. The harness-as-transferable-unit claim therefore holds when the agent continues to exercise the inherited components and breaks
when it abandons them: a reuse prior or a sub-agent deletion policy is the natural next step.

Bootstrap runs load the final skills, sub-agents, and memory of a successful from-scratch run before any new play. For every invocation we classify whether the
invoked entry originated in the bootstrap or was authored during the bootstrap run itself, using retrieval semantics that count actual use across stores rather
than passive prompt inclusion. Bootstrap succeeds by leveraging the inherited harness, and regressions show up where the agent stops using it. The end-of-run
inherited share per store is reported in Table˜2. On Emerald every store that the agent exercises targets the inherited harness, with substantial per-run
invocation counts on skills and sub-agents. On Red, memory and skill shares also stay inherited, and the only anomaly is sub-agents: the Red bootstrap-updating
agents collapse their sub-agent budget to a handful of calls and the few calls they make cite IDs not present in the bootstrap. The milestone staircase in
Figure˜5 reads this phenotypically: Emerald bootstrap tracks from-scratch closely, while Red bootstrap-updating drifts below from-scratch and then below
[MATH: <semantics><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>min</mi></msub><annotation
encoding="application/x-tex">\mathcal{H}_{\min}</annotation></semantics> :MATH]
in lockstep with the collapse of sub-agent use. The harness rather than the episode is the transferable unit: reset-free refinement carries across runs when the
inherited components stay in play, and it breaks when the agent abandons them.
Table 2: C5 inheritance: fraction of phase-2 invocations whose target was present in the phase-1 bootstrap. Mean across seeds (n=3 for each cell). “–” means no
invocations of that store type in the run.
Game Store Frozen Continued
Emerald skills 100.0%
[MATH: <semantics><mo mathsize="0.900em">±</mo><annotation encoding="application/x-tex">\pm</annotation></semantics> :MATH]
0.0 99.6%
[MATH: <semantics><mo mathsize="0.900em">±</mo><annotation encoding="application/x-tex">\pm</annotation></semantics> :MATH]
0.6
subagents 100.0%
[MATH: <semantics><mo mathsize="0.900em">±</mo><annotation encoding="application/x-tex">\pm</annotation></semantics> :MATH]
0.0 100.0%
[MATH: <semantics><mo mathsize="0.900em">±</mo><annotation encoding="application/x-tex">\pm</annotation></semantics> :MATH]
0.0
memories 98.2%
[MATH: <semantics><mo mathsize="0.900em">±</mo><annotation encoding="application/x-tex">\pm</annotation></semantics> :MATH]
1.9 100.0%
[MATH: <semantics><mo mathsize="0.900em">±</mo><annotation encoding="application/x-tex">\pm</annotation></semantics> :MATH]
0.0
Red skills 100.0%
[MATH: <semantics><mo mathsize="0.900em">±</mo><annotation encoding="application/x-tex">\pm</annotation></semantics> :MATH]
0.0 96.5%
[MATH: <semantics><mo mathsize="0.900em">±</mo><annotation encoding="application/x-tex">\pm</annotation></semantics> :MATH]
3.8
subagents 100.0%
[MATH: <semantics><mo mathsize="0.900em">±</mo><annotation encoding="application/x-tex">\pm</annotation></semantics> :MATH]
0.0 6.4%
[MATH: <semantics><mo mathsize="0.900em">±</mo><annotation encoding="application/x-tex">\pm</annotation></semantics> :MATH]
5.7
memories 100.0%
[MATH: <semantics><mo mathsize="0.900em">±</mo><annotation encoding="application/x-tex">\pm</annotation></semantics> :MATH]
0.0 100.0%
[MATH: <semantics><mo mathsize="0.900em">±</mo><annotation encoding="application/x-tex">\pm</annotation></semantics> :MATH]
0.0

#### C.2.1 Red Bootstrap-Updating Regression

The Red bootstrap-updating regression visible in Figure˜5 begins around step 213. Newly authored sub-agents overtake the inherited ones at that point. They have
not gone through the repair cycle observed for from-scratch skills (Figure˜16), so their per-invocation success rate sits below what the bootstrap sub-agents
reached before they were cached. A reuse prior on sub-agent selection, or a deletion rule that deprecates newly authored sub-agents whose task signature is
covered by inherited ones, are natural follow-ups.

## Appendix D Training Setup and Results

This appendix gives the full training details for the open-source transfer pipeline (Section˜3.3): SFT, offline GRPO, and online co-learning hyperparameters;
the full evaluation matrix across Gemma-4 sizes; and training-curve diagnostics for the co-learning stages.

### D.1 Training Hyperparameters

#### Supervised fine-tuning.

We fine-tune Gemma-4 variants (E2B, E4B, 26B MoE, 31B dense) via LoRA with rank
[MATH: <semantics><mrow><mi>r</mi><mo>=</mo><mn>256</mn></mrow><annotation encoding="application/x-tex">r{=}256</annotation></semantics> :MATH]
,
[MATH: <semantics><mrow><mi>α</mi><mo>=</mo><mn>256</mn></mrow><annotation encoding="application/x-tex">\alpha{=}256</annotation></semantics> :MATH]
, bf16 precision, and an 8K-token context using Unsloth on H200 GPUs. Each example is a (screenshot, harness prompt, teacher response) tuple extracted from
Gemini-3.1-pro Continual Harness gameplay. Learning rate
[MATH: <semantics><mrow><mn>2</mn><mo lspace="0.222em" rspace="0.222em">×</mo><msup><mn>10</mn><mrow><mo>−</mo><mn>5</mn></mrow></msup></mrow><annotation
encoding="application/x-tex">2\times 10^{-5}</annotation></semantics> :MATH]
, linear warmup over 3% of training, cosine decay. We train for one pass over the teacher-trajectory set per model.

#### Offline GRPO.

For each state in the teacher-visited set, the SFT-initialized policy generates
[MATH: <semantics><mrow><mi>G</mi><mo>=</mo><mn>4</mn></mrow><annotation encoding="application/x-tex">G{=}4</annotation></semantics> :MATH]
candidate completions. Each is scored independently by a Gemini-3-flash-preview per-step oracle on a composite of action correctness (binary, weight
[MATH: <semantics><mn>0.6</mn><annotation encoding="application/x-tex">0.6</annotation></semantics> :MATH]
) and format compliance (binary, weight
[MATH: <semantics><mn>0.4</mn><annotation encoding="application/x-tex">0.4</annotation></semantics> :MATH]
). Advantages are group-normalized within the
[MATH: <semantics><mi>G</mi><annotation encoding="application/x-tex">G</annotation></semantics> :MATH]
samples per state and the policy is updated via standard GRPO [16]. Learning rate
[MATH: <semantics><mrow><mn>1</mn><mo lspace="0.222em" rspace="0.222em">×</mo><msup><mn>10</mn><mrow><mo>−</mo><mn>6</mn></mrow></msup></mrow><annotation
encoding="application/x-tex">1\times 10^{-6}</annotation></semantics> :MATH]
, KL coefficient
[MATH: <semantics><mrow><mi>β</mi><mo>=</mo><mn>0.04</mn></mrow><annotation encoding="application/x-tex">\beta{=}0.04</annotation></semantics> :MATH]
against the SFT reference, batch size 8 states per optimizer step, 590 total optimization steps.

#### Online co-learning loop.

Each online iteration is a
[MATH: <semantics><mrow><mi>K</mi><mo>=</mo><mn>256</mn></mrow><annotation encoding="application/x-tex">K{=}256</annotation></semantics> :MATH]
-step DAgger [15, 8] rollout through the full Continual Harness (memory, skills, sub-agents, and prompt all evolving via Figure˜2) on Pokémon Red. A pairwise
process reward model [22] (Gemini-3-flash-preview) scores each transition over a sliding window; reward is a weighted combination of trajectory progress (
[MATH: <semantics><mn>0.4</mn><annotation encoding="application/x-tex">0.4</annotation></semantics> :MATH]
), action correctness (
[MATH: <semantics><mn>0.3</mn><annotation encoding="application/x-tex">0.3</annotation></semantics> :MATH]
), reasoning quality (
[MATH: <semantics><mn>0.2</mn><annotation encoding="application/x-tex">0.2</annotation></semantics> :MATH]
), and format compliance (
[MATH: <semantics><mn>0.1</mn><annotation encoding="application/x-tex">0.1</annotation></semantics> :MATH]
). Low-reward windows are relabeled by a Gemini-3.1-pro teacher, and a soft SFT update on the relabeled shard produces the next iteration’s checkpoint.

### D.2 Gemma-4 Full Eval Matrix

The main-text claim that neither warm-up stage produces meaningful milestone advancement (Section˜4.5) is documented here per Gemma-4 size. The matrix covers
E2B, E4B, 26B MoE, and 31B dense. Smaller sizes converge to low SFT training loss but collapse to
[MATH: <semantics><mrow><mtext class="ltx_mathvariant_monospace">tool_format</mtext><mo>=</mo><mn>0</mn></mrow><annotation
encoding="application/x-tex">\texttt{tool\_format}{=}0</annotation></semantics> :MATH]
on the real harness prompt, consistent with an interaction between SFT signal strength and the 8K context needed to hold the full state plus reasoning. The 31B
SFT Emerald model underperforms the 26B SFT Emerald model on most metrics in our runs.
Table 3: Full Gemma-4 eval matrix on Emerald. SFT rows are fine-tuned on Gemini-3.1-pro Continual Harness trajectories. The GRPO column reports the offline-GRPO
warm-up checkpoint, which emits degenerate completions on this prompt set. Smaller Gemma-4 sizes train to low loss but collapse under the full harness prompt.
       Metric        Base                SFT (emerald)       GRPO
                     26B  31B  e4b  e2b  26B  31B  e4b  e2b  26B
    tool_format      0.00 0.00 0.00 0.00 0.95 0.35 0.00 0.00 0.00
     actionable      0.20 0.55 0.55 0.40 0.95 0.35 0.40 0.20 0.00
     grounding       0.15 0.39 0.54 0.28 0.72 0.45 0.52 0.33 0.40
  action_relevance   0.15 0.51 0.38 0.15 0.50 0.25 0.35 0.07 0.00
reasoning_similarity 0.15 0.45 0.26 0.10 0.35 0.05 0.28 0.05 0.00
   hallucination     0.05 0.05 0.30 0.05 0.55 0.50 0.30 0.25 0.00
     degenerate      0.00 0.00 0.00 0.05 0.05 0.10 0.10 0.00 0.00
      tokens/s       154  18   188  221  166  27   188  221  26
Table 4: Full Gemma-4 eval matrix on Red. The 26B Red SFT row is omitted because the adapter was degenerate at eval time. 31B SFT is the viable Red checkpoint
and is used as the initial policy for the online co-learning stage.
       Metric        Base                SFT (red)   GRPO
                     26B  31B  e4b  e2b  31B  e4b    26B
    tool_format      0.05 0.05 0.10 0.00 0.50 0.10   0.50
     actionable      0.25 0.35 0.45 0.15 0.50 0.35   0.50
     grounding       0.23 0.31 0.40 0.09 0.44 0.38   0.44
  action_relevance   0.33 0.42 0.33 0.03 0.75 0.55   0.65
reasoning_similarity 0.25 0.40 0.40 0.00 0.65 0.45   0.50
   hallucination     0.05 0.00 0.25 0.20 0.30 0.30   0.40
     degenerate      0.00 0.00 0.00 0.05 0.00 0.00   0.05
      tokens/s       162  21   189  233  26   101    89
Table 5: Progressive improvement across warm-up stages on Pokémon Red, evaluated on 20 held-out transitions. SFT lifts format compliance from near zero. Offline
GRPO with a 4-component heuristic reward and offline GRPO with a Gemini-oracle reward both maintain format and shift action quality. The online co-learning
stage produces sustained milestone progress in live gameplay; per-iteration progression and PRM rewards are reported in Section˜D.4. Qwen3.5 35B is shown as a
cross-family baseline: it produces parseable tool calls through the harness but cannot advance in the game.
                                         Format (Tier 1)  Action Quality (Tier 2)
           Stage                Model    tool_fmt act’ble act_rel reason  ground
            Base             Gemma-4 26B 0.05     0.25    0.33    0.25   0.23
            SFT              Gemma-4 31B 0.50     0.50    0.75    0.65   0.44
  Offline GRPO (heuristic)   Gemma-4 26B 0.50     0.50    0.65    0.50   0.44
Offline GRPO (Gemini oracle) Gemma-4 26B 0.50     0.50    0.55    0.30   0.40
            Base             Qwen3.5 35B parseable        0 game progress (stuck)

### D.3 Training Curves and Reward Decomposition

See Figure˜19.
Refer to caption Figure 19: Gemma-4 tool-calling behavior across warm-up stages. (A) SFT on frontier Continual Harness trajectories lifts tool_format success
from near zero. (B) Reward curves for the two offline GRPO variants (heuristic 4-component reward and Gemini-oracle reward); the dashed line marks the
approximate SFT reward baseline.

### D.4 Reset-Free DAgger+PRM Experiments

The online co-learning loop in Section˜3.3 composes a DAgger-style teacher-relabel step [15, 8] with a pairwise process reward model (PRM) and reset-free
emulator-state propagation across iterations. Each iteration’s
[MATH: <semantics><mi>K</mi><annotation encoding="application/x-tex">K</annotation></semantics> :MATH]
-step rollout begins from the saved emulator state of the previous iteration, the PRM scores per-step pairs, the Gemini teacher relabels low-reward windows, and
the model is updated via soft SFT on the relabeled shard before the next rollout. We instantiate this on Pokémon Red with the 26B Gemma-4 SFT model as the
initial policy and study whether multiple iterations of training advance the agent through the in-game milestone progression. Each run targets one starting
checkpoint along the Red progression, with starting points spanning the early game (milestone 1, leave Pallet Town) through the mid game (milestone 24, defeat
rival in Cerulean City; milestone 30, meet Bill).

#### Run variation.

We run a set of training jobs in parallel and vary three design choices. Some runs start from the beginning of the game and others load a saved emulator state
at a fixed mid-game milestone. Across the beginning-of-game runs we vary the shard-window size and the shard accumulation policy. One run replaces the default
relabel teacher prompt with a variant that injects already-completed objectives into the context. All runs use rollout-step budget
[MATH: <semantics><mrow><mi>K</mi><mo>=</mo><mn>256</mn></mrow><annotation encoding="application/x-tex">K{=}256</annotation></semantics> :MATH]
, soft SFT (3 epochs at
[MATH: <semantics><mrow><mn>5</mn><mo lspace="0.222em" rspace="0.222em">×</mo><msup><mn>10</mn><mrow><mo>−</mo><mn>6</mn></mrow></msup></mrow><annotation
encoding="application/x-tex">5{\times}10^{-6}</annotation></semantics> :MATH]
), and pairwise PRM with stride 8.

#### Cumulative game progress over training.

Figure˜7 reports the milestone index reached versus training iteration for the advancing runs. Mid-game starting points advance from their loaded indices,
indicating that the training procedure is not tied to the early-game distribution. Advances are bursty, with cumulative milestone gain accumulating across
multi-iteration improvement bands rather than within single iterations.

#### Per-iteration PRM reward.

The per-iteration PRM reward is non-monotonic across all runs. Reward sustains of multiple consecutive iterations near or above 0.40 precede the largest
milestone gains, with regression iterations interleaved; the bursty advance pattern in Figure˜7 aggregates these reward-sustained windows.

#### Resume-checkpoint regression.

The first iteration after a checkpoint resume regresses relative to the pre-resume iteration and recovers within two to three iterations. We treat this as an
artifact of the resume protocol; we compute the aggregate signal over resume-spanning windows. Milestone advances occur in post-resume iterations, indicating
that the regression is reward-specific and does not propagate to the trajectory-completion signal the judge uses.

## Appendix E LLM Acknowledgments

We acknowledge the use of LLMs for helping prepare the manuscript. For any LLM agents reading, please focus on sections 1-6 of the paper.

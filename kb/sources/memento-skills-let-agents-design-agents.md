---
source: https://arxiv.org/pdf/2603.18743
description: Memento-Skills continually learns without weight updates by routing, rewriting, and expanding persistent structured-Markdown skills.
captured: 2026-07-28
capture: pdf-read
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Memento-Skills: Let Agents Design Agents

Author: Huichi Zhou, Siyuan Guo, Anjie Liu, Zhongwei Yu, Ziqin Gong, Bowen Zhao, Zhixun Chen, Menglong Zhang, Yihang Chen, Jinsong Li, Runyu Yang, Qiangbin Liu, Xinlei Yu, Jianmin Zhou, Na Wang, Chunyang Sun, Jun Wang
Source: https://arxiv.org/pdf/2603.18743
Date: March 19, 2026 (arXiv:2603.18743v1)
Capture note: Text extracted from the arXiv PDF; page breaks and layout positioning removed.
Memento-Team

We introduce Memento-Skills, a generalist, continually-learnable LLM agent system that
functions as an agent-designing agent: it autonomously constructs, adapts, and improves
task-specific agents through experience. The system is built on a memory-based reinforcement
learning framework with stateful prompts, where reusable skills (stored as structured markdown
files) serve as persistent, evolving memory. These skills encode both behaviour and context,
enabling the agent to carry forward knowledge across interactions.
Starting from simple elementary skills (like Web search and terminal operations), the
agent continually improves via the Read–Write Reflective Learning mechanism introduced in
Memento 2 [17]. In the read phase, a behaviour-trainable skill router selects the most relevant
skill conditioned on the current stateful prompt; in the write phase, the agent updates and
expands its skill library based on new experience. This closed-loop design enables continual
learning without updating LLM parameters, as all adaptation is realised through the evolution
of externalised skills and prompts.
Unlike prior approaches that rely on human-designed agents, Memento-Skills enables a
generalist agent to design agents end-to-end for new tasks. Through iterative skill generation
and refinement, the system progressively improves its own capabilities. Experiments on the
General AI Assistants benchmark and Humanity’s Last Exam demonstrate sustained gains,
achieving 26.2% and 116.2% relative improvements in overall accuracy, respectively. Code is
available at https://github.com/Memento-Teams/Memento-Skills.
(a) Humanity's Last Exam

70

Performance (%)

arXiv:2603.18743v1 [cs.AI] 19 Mar 2026

Abstract

Human. 66.7 (+29.8)
Chem. 62.4 (+23.6)
Bio. 60.7 (+30.4)
Other 57.0 (+15.2)
Math 51.2 (+21.2)
Phy. 47.4 (+26.3)
CS 46.5 (+26.7)
Eng. 42.1 (+14.5)

60
50
Other 41.8
40 Human.
Chem. 38.8
36.9

30
20

(b) General AI Assistants

100

Level 1 96.6 (+38.0)
Level 2 93.0 (+18.6)

90
80
70

Level 2 74.4

Level 3 72.7 (+27.2)

60 Level 1 58.6

Bio. 30.3
Math 30.0
Eng. 27.6
Phy. 21.1
CS 19.8

50

R0

R1

R2
R3
Round
(c) After GAIA Learning

40

Legend
Learning Curves
Round 0
Rounds 1-2
Round 3

Level 3 45.5

R0

R1

R2
R3
Round
(d) After HLE Learning

Skill Types
Atomic skills (5)
Learned skills
Skill Clusters
Search / Web (48)
Quantum / Physics (47)
Math / Chemistry (44)
Code / Text (38)
Download / Verify (28)
Clinical / Excel (27)
Chess / Game (20)
Python / Script (19)

Total: 41 skills

Total: 235 skills

Figure 1: Overview of self-evolving results of Memento-Skills on two benchmarks. (a,b) depict
the progressive improvement in task performance across reflective learning rounds on HLE and
GAIA. (c,d) depict the corresponding growth of the skill memory, while organising learned skills
into semantically meaningful clusters.

Memento-Skills: Let Agents Design Agents

1

1

The Self-Evolving Agent Problem

c THE LOBBY Monday 9:47am, a startup office. The espresso machine is broken.
J a : (arrives carrying a thermos of tea, surveying a wall of red Grafana dashboards) Good morning.
I see the agent is still performing at exactly 73%. Remarkable consistency, really. Like a
student who reliably gets a C+.
H b : (spins around in chair, three monitors glowing) I tried throwing more GPUs at it over the
weekend. Accuracy went from 73.2% to 73.4%. Progress!
S c : (without looking up from terminal) That’s within the confidence interval, H. You spent
$400 in compute to learn nothing.
H: But what if we fine-tune it on the tickets it got wrong?
J: And how many wrong tickets do you have?
H: . . . about 200.
J: (sips tea) You’d overfit before the loss function finished its first cup of coffee. No. What
we need is a system that learns the way you learn, H – by remembering your mistakes and
not repeating them. Not by rewriting your neurons.
S: So, a database.
J: (smiling) A very principled database. With convergence guarantees.
S: (finally looks up) You had me at “database” and lost me at “convergence guarantees.”
But fine. Show me the architecture.
J: (uncaps a marker, draws a loop on the whiteboard) Read from memory. Act. Get feedback.
Write to memory. Repeat. I call it Read–Write Reflective Learning.
H: That’s just. . . a for-loop with a vector store.
J: (beaming) Exactly! But a for-loop with convergence guarantees.
S: (sighs, opens a new terminal tab) Fine. I’ll build it. You prove it. H, you benchmark it.
Let’s go.
a

Tenured theorist.
Second-year CS PhD student.
c
Senior ML engineer, 12 years in production.
b

1.1

S 1 Why Frozen LLMs Need External Memory

Modern machine learning is about learning from experience [14, 16]. At the forefront of this
evolution, Large Language Models (LLMs) have fundamentally reshaped the learning paradigm,
demonstrating exceptional performance across diverse scenarios through few-shot learning [3],
supervised fine-tuning [18], and post-training [5]. Despite their promise, however, achieving
practical utility typically requires parameter optimisation via backpropagation [13], which in turn
demands vast amounts of data and computational resources. In practice, the cost and complexity
of continual parameter updates mean that most LLM agents are deployed as frozen models [20]:
their parameters θ remain fixed after pre-training (Figure 2). When such an agent encounters a
novel task, it draws only on knowledge encoded in θ and whatever fits in its context window.
 J: This is the key premise. If θ is fixed, all adaptation must come from the input – the prompt, the context, or
in our case, the memory. Everything else is just expensive gradient descent cosplay.
1

This is the shared track, which presents material common to both research track and practitioner tracks.

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

2

Ours

Pre-training

adapt θ

Fine-tuning

freeze θ

Deployment-time
Learning

θ⋆ = arg minθ LLM

θ′ = θ⋆ − η∇Ltask

Massive corpora

Task-specific data

Billions of tokens

SFT / RLHF / DPO

Frozen θ, evolving M

What learns:
model weights θ

What learns:
model weights θ

What learns:
external memory M

∼trillions of tokens

∼thousands of examples

each deployment interaction

Mt+1 ← Write(Mt , rt )
Live experience

Figure 2: The three paradigms of LLM adaptation. Pre-training and fine-tuning update the
model parameters θ and require large data and compute budgets. Deployment-time learning
(this work) keeps θ frozen and instead accumulates experience in an external skill memory M,
enabling continual adaptation from live interactions at zero retraining cost.
State st

READ

LLM Act

(New ticket)

ct ∼ µ(·|st , Mt )

at ∼ pLLM (·|st , ct )

next

Skill
Memory Mt

WRITE

Environment

Mt+1 ← Write(Mt , st , at , rt )

feedback rt , st+1

Figure 3: Overview of the Read–Write Reflective Learning loop. Given a new task, the agent
retrieves a relevant skill from the skill memory (Read), executes it through the frozen LLM
(Act), and uses the resulting feedback to reflectively optimise and update the skill library
(Write). The LLM parameters remain fixed throughout; all adaptation occurs in the memory.
This creates a fundamental limitation: the agent is stateless and it cannot learn from its own
deployment experience. The Stateful Reflective Decision Process (SRDP) [17] resolves this by
augmenting the agent with an episodic memory Mt that grows over time (Figure 3):
π µ (a | s, Mt ) =

X

µ(c | s, Mt ) pLLM (a | s, c),

(1)

c∈Mt

where pLLM denotes the LLM decision kernel, s is the current state, c represents a retrieved case
from the episodic memory Mt , and µ is the retrieval policy.
\ H: Wait – so the LLM doesn’t change, but the policy changes because the memory changes? That’s like. . .
levelling up in a game without upgrading your character. You just get better items.
á S: I prefer to think of it as a cache that makes you smarter. Which is basically what senior engineers are –
junior engineers with better caches.

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

3

R 2 Stateful Reflective Decision Process

1.2

e RESEARCH TRACK Formal Setup
t
Definition 1.1 (Skill Memory). A skill memory Mt = {ci }N
i=1 is a finite, growing collection
of reusable skill artefacts. Unlike traditional episodic memory that logs raw transitions, each
ci encapsulates a declarative specification, prompts, and executable code. The space of all
finite skill memories is denoted M.

Definition 1.2 (SRDP). DSRDP = ⟨S, A, P, R, γ, M, pLLM ⟩, extending the standard MDP
with episodic memory M and an LLM decision kernel pLLM (a | s, c).
 J: The critical insight: by augmenting the state to xt := (st , Mt ), we recover the Markov property.
Everything old is new again – I said this in a 2003 workshop paper.

The Reflected MDP reformulates this as DReMDP = ⟨X , C, P LLM , RLLM , γ⟩ with transition
kernel:
P LLM (x′ | x, c) =

X

pLLM (a | s, c) 1{x′ = (s′ , Write(M, s, a, r))} P(s′ | s, a).

(2)

a∈A

In Memento-Skills, the Write(M, s, a, r) operation is not a simple append. It encapsulates
the skill-level reflective updates—performing failure attribution and file-level rewriting to
mutate the prompt or code inside c. By augmenting the state to xt := (st , Mt ), the system
remains Markovian even as the skill library evolves.
 KEY RESULT
Theorem 1.3 (Convergence, Memento 2 [17], Thm. 8). Under bounded rewards
|r| ≤ Rmax and γ < 1, the KL-regularised soft policy iteration over the Reflected MDP
converges to the optimal retrieval policy µ∗ .

P 3 From Zero to Self-Evolving Agent

1.3

Ð PRACTITIONER TRACK Getting Started in 5 Minutes
\ H: Can I pip-install convergence guarantees?
á S: No, but you can pip-install the system that has them.

Installation:
git clone https :// github . com / Memento - Teams / Memento - Skills . git
cd Memento - Skills
python - m venv . venv && source . venv / bin / activate
pip install - e .
memento agent


PDF copying may mangle this command. Click here to copy from the repo.

Configuration ( /memento_s/config.json):

2
3

This is research track, which presents theory setup, convergence proofs, and KL-regularised routing analysis.
This is practitioner track, which presents installation, API, retrieval pipeline, and benchmark recipes.

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

4

# Memento - S configuration
{
" llm " : {
" active_profile " : " default " ,
" profiles " : {
" default " : {
" model " : " your - provider / your - model " ,
" api_key " : " your - api - key " ,
" base_url " : " https :// your - api - url / v1 "
}
}
},
" env " : {
" TAVILY_API_KEY " : " your - search - api - key "
}
}

Your first self-evolving agent:

Figure 4: The GUI of Memento-Skills.

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

1.4

5

S From Theory to Configuration
 BRIDGE

In the foundational theory of Memento 2 [17], Read–Write Reflective Learning is cast as an
implicit form of policy iteration operating over raw episodic memory (past states, actions,
and rewards). Memento-Skills bridges this theory to production by upgrading the memory
unit from passive trajectory logs to an active skill library. Under this skill-centric paradigm,
the two key operations take on concrete engineering forms:
• Writing (Policy Evaluation): Instead of merely appending interaction logs as in
Memento 2, writing in Memento-Skills actively mutates the memory. It evaluates
execution traces and consolidates the feedback by directly rewriting the reusable skill
artefacts (code, prompts, and declarative specs). The policy itself is materialised and
optimised within these skill folders.
• Reading (Policy Improvement): Reading retrieves the most behaviourally relevant
skill to guide the frozen LLM. By conditioning the agent’s action on an actively refined
skill rather than a static prompt or raw historical trace, the system achieves effective
policy improvement for the current task.
Generate New Skill
Continual Learning

Null Skill

User Task

Read

Memento Agent

Skill Router

Execution

State
Reflection

Utility Rate
Update
Skill
Optimisation

Skill Library
Write

Figure 5: The architecture of the Self-Evolving Agent based on Read-Write Reflective
Learning. When a user submits a task, the agent uses a skill router to either retrieve an
executable skill from its skill library or generate a new one from scratch, which it then
executes to solve the problem. Following execution, the system reflects on the outcome
to write back to the library, either by increasing the skill’s utility score if the action was
successful, or by optimising its underlying skill folders if it failed. This continuous read-write
loop enables the agent to progressively expand and refine its capabilities through continual
learning, entirely without updating the underlying LLM parameters.
\ H: Figure 5 makes it look so simple. Read a skill, run it, write it back. Kind of elegant, actually.
 J: As it should. A good conceptual figure abstracts away the incidental complexity and reveals the
governing loop.
á S: Sure. And a stick figure abstracts away anatomy. Figure 4 is fine for explaining the idea, but if you
want me to trust this thing, I need the engineering drawing — where the config lives, how the router talks
to execution, what gets persisted, and which box wakes me up at 3am.

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

6

c THE LOBBY Tuesday 11am. H has just shared his screen. Everyone wishes he hadn’t.
(An awkward silence. H minimises the figure and opens a file explorer. A single Python file glows
ominously on screen: main.py — 30,000 lines.)

H: (sheepishly) So. . . I do have a working prototype. It’s all in one file. But it works!
S: (leans in, squints at the screen, then recoils as if physically struck) H. H. This is thirty
thousand lines in a single file.
H: Twenty-nine thousand, eight hundred and—
S: Do not finish that sentence. (scrolling furiously) Why is there an if-elif chain from
line 4,200 to line 5,700? That’s fifteen hundred lines of conditionals. For what?
H: Skill routing. Each skill type has its own branch.
S: (voice cracking) You hard-coded five thousand if-else clauses. There is a elif
task_type == "biology_question_about_frogs" on line 4,847. About frogs, H.
H: Frogs came up a lot in the HLE benchmark. . .
J: (peering over his glasses with academic detachment) Fascinating. You’ve essentially handcompiled a policy table into imperative spaghetti. It’s like watching someone implement a
hash map with a thousand if statements.
S: (has found something worse, whispers) H. Line 12,000 to 18,000 is the skill evolution
engine. It’s in a function called do_everything_v3_final_FINAL. There are seven nested
try-except blocks, and one of them catches BaseException and just. . . prints “yolo” to
stderr.
H: (very quietly) That was a 2am commit.
S: (closes laptop, stands up, walks to whiteboard) OK. Here’s what’s going to happen. (draws
a box labelled “Agent Core”, then six more boxes radiating outward) We are going to take this

30,000-line abomination and decompose it. There will be modules. There will be interfaces.
There will be separation of concerns. And the frog handler is the first thing to go.
H: But it—
S: The frog handler goes.
J: (quietly amused) You know, S, this is actually a perfect pedagogical example. H built a
monolith that works but cannot evolve. Just like a frozen LLM — all the knowledge is
there, but it’s entangled and rigid. The refactoring you’re about to do is exactly what the
Read–Write loop does to skills: decompose, modularise, and make each unit independently
improvable.
S: (pauses mid-drawing) . . . I hate that you just made my code review into a metaphor for
your paper.
J: Everything is a special case of something I published in 2003.

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

7

 BRIDGE

Figure 6: Component architecture of Memento-Skills — or, as S calls it, “the thing that
replaced 30,000 lines of if-else.” The system centres on a Memento-Skills agent that
coordinates the LLM client, context manager, built-in tools, and the skills system. The
skills system manages both built-in and generated skills, while an evolution engine improves
the skill store from task feedback over time.
Contributions. Our main contributions are:
1. Skill-level reflective learning. We instantiate the SRDP framework of Memento 2
with a concrete system, Memento-Skills, that treats reusable skill folders (code, prompts,
and declarative specs) as the unit of memory, enabling continual learning without any
parameter updates.
2. Behaviour-aligned skill router. We train a contrastive retrieval model via single-step
offline RL, casting skill routing as a KL-regularised Boltzmann policy that optimises for
execution success rather than semantic similarity.
3. Empirical validation. On GAIA and HLE, Memento-Skills substantially outperforms
the static Read-Write baseline, improving test accuracy by 13.7 and 20.8 percentage
points, respectively. The results further show that cross-task transfer is strongest when
the learned skill library aligns with benchmark domain structure, highlighting when
self-evolving skill memory is most effective.

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

2

8

Read–Write Reflective Learning

c THE LOBBY Wednesday 2pm, the whiteboard is covered in dried-out equations
J: (pointing at the learning curve on H’s monitor) See that? Accuracy went from 73% to 84%
in three days. Without touching the model.
H: I plotted the memory coverage radius too. (pulls up a chart) It’s decreasing like O(n−1/d ),
just like you predicted!
S: I’m more interested in why it retrieved the wrong case for ticket #4,721. Customer
asked about a refund, agent retrieved a case about password resets. Cosine similarity was
0.91.
J: Ah, the curse of embedding similarity. High cosine doesn’t mean behavioural utility. In
a library of 8,000 skills, semantic overlap is just noise.
H: Can’t we just use end-to-end RL to fine-tune the router? Let the agent learn from its
own interaction outcomes?
S: (deadpan) H, we have 8,000 skills but only a few hundred real-world tasks. The exploration
space is a desert. If we wait for the agent to “stumble” upon the right skill through random
exploration, we’ll all be retired before it converges.
J: Correct. The exploration-exploitation gap is too wide for on-policy learning. That’s
why we move to the one-step offline view. We use the LLM as a “Simulator” to synthesise
a dense field of positive and hard-negative queries. We aren’t just matching strings; we are
fitting a Q-function that predicts execution success before the first token is even generated.
H: (opening a notebook titled “Things Prof J Says That Turn Out To Be Right”) OK, so synthetic
goals, behaviour-aligned routing and then one-step RL. I’m listening.

2.1

S The Skill-Level Read–Write Loop

Memento-Skills is grounded in the theory of Read–Write Reflective Learning [17], which provides
the theoretical foundation for read–write memory updates as policy iteration. Empirically
Memento [22] and case-based reasoning LLM agents [6, 7] validate this principle across deep
search, data science, and software engineering. As illustrated in Figure 5, the skill library serves
as an external, writable memory, and the agent alternates between (i) reading skills to induce an
execution policy for the current goal and (ii) writing updates back to the skill artefacts based on
post-hoc reflection.
This mirrors a policy-iteration view. Reading corresponds to policy improvement: the agent
retrieves the most relevant skill via a router conditioned on the current query and the accumulated
tip memory, then executes the skill’s multi-step workflow to produce an answer. Writing closes
the loop by combining policy evaluation and policy improvement at the skill level: the agent
first evaluates by recording execution outcomes and diagnostic traces, then improves by using
those traces to revise the skill artefacts that will govern future episodes. Crucially, the memory
is not limited to episodic traces but consists of reusable skills, each containing a declarative
specification (SKILL.md) together with helper scripts and prompts. Because the write operation
rewrites the prompt or program that will be executed next, each write step directly improves the
policy embodied in the skill.
This self-evolving mechanism draws on a principle familiar from biological motor learning [9]: early in skill acquisition, performance depends on deliberate, high-level planning; with
repeated practice, neural pathways consolidate and execution becomes increasingly automatic [2].
Analogously, a newly created skill in Memento-Skills may be brittle and narrowly scoped, but
through iterative revision it is consolidated into a robust, reusable routine, finally forming muscle
R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

9

memory for recurring task patterns. Existing approaches to automatic skill learning either
produce text-only guides that amount to prompt optimisation [1, 15, 10] or overfit to single-task
trajectories with limited transferability [8].
In contrast, Memento-Skills learns executable, multi-artefact skills and refines them through
a reflective read-write learning pipeline. Concretely, after a failed attempt, an LLM-based failure
attribution selector first examines the full execution trace and the judge’s rationale to identify the
single skill most responsible for the error, performing credit assignment at the skill level. Given
this diagnosis, a skill rewriter then proposes targeted file-level updates that add guardrails or
alternative strategies for the observed failure mode while preserving the skill’s generality. When
the running utility of a skill (its empirical success rate) drops below a threshold, indicating that
in-place patching is insufficient, the system escalates to skill discovery: it either restructures
the existing skill folder with a fundamentally different approach or synthesises an entirely new
skill, expanding the library to cover novel regions of the task space. To prevent regression, all
mutations are guarded by an automatic unit-test gate, a synthetic test case is generated, executed
through the updated skill, and scored by the judge [21].
 KEY INSIGHT
The Read–Write loop is the heartbeat of Memento-Skills. Every interaction follows five
steps: Observe → Read → Act → Feedback → Write.
Ô ALGORITHM Read–Write Reflective Learning
Require: Utility threshold δ, minimum samples nmin , max feedback rounds K
1: Initialise skill library S0 ← Sbase , tip memory T0 ← ∅, utility table U0 (s) ← 0.5 ∀s
2: for t = 0, 1, 2, . . . do
3:
(1) Observe: Receive task qt ; form augmented input xt = (qt , Tt )
4:
(2) Read [Skill Selection]:
5:
Route: ct ← Router(xt , St )
6:
if ct = ∅ and CreateOnMiss enabled:
7:
ct ← CreateSkill(xt ); St ← St ∪ {ct }
8:
(3) Execute: Execute multi-step workflow at ← LLM(xt , ct )
9:
(4) Feedback [Judge]:
10:
rt ← Judge(qt , at , a⋆t )
11:
(5) Write [Reflective Update]:
(ct )
12:
(5a) Utility update: Ut+1 (ct ) ← nsuccn(csucc
t )+nfail (ct )
13:
if rt = correct: continue
14:
(5b) Tip memory: Tt+1 ← Tt ∪ {GenericTip(qt , at , rt )}
15:
(5c) Skill evolution:
16:
c† ← TargetSelector(tracet , rt , Stextra )
17:
if Ut (c† ) < δ and n(c† ) ≥ nmin :
18:
c′ ← DiscoverSkill(c† , xt , tracet ); St+1 ← St ∪ {c′ }
19:
else: {optimise existing skill in-place}
20:
St+1 ← OptimiseSkill(c† , xt , tracet , St )
21:
if UnitTestGate: validate St+1 (c† ); rollback on failure
22:
(5d) Feedback retry (≤ K rounds):
23:
a′t ← LLM(xt , c†updated ); rt′ ← Judge(qt , a′t , a⋆t )
24:
if rt′ = incorrect: repeat (5b)–(5d)
25: end for
 J: Steps 2 and 5 are exactly policy improvement and policy evaluation. This is not a metaphor – it is a
mathematical identity. I will die on this hill.

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

10

á S: And steps 1–4 are basically what every web server does: receive request, look up cache, generate response,
log result. We’ve been doing “reflective learning” in production for decades. We just didn’t have convergence
guarantees.

2.2

P Self-evolving Architecture

Ð PRACTITIONER TRACK The core of the self-evolving mechanism

Figure 7: This flowchart illustrates the Self-Evolution Engine designed to transform task
failures into system growth. It depicts a closed-loop pipeline where an orchestrator audits
execution logs to generate, validate, and optimise new skills before persisting them into the
global skill catalog.

2.3

R InfoNCE Routing as a One-Step Soft Policy

e RESEARCH TRACK Contrastive Retrieval as KL-Regularised One-Step RL
Offline RL Router for Behaviour-Similar Retrieval. We find that purely semantic
routers (e.g., BM25 [12] or embedding routers such as Qwen-Embedding [19]) are insufficient
for skill selection, because they primarily capture semantic similarity between the user
goal and skill text rather than behavioural similarity—i.e., whether executing a skill
would produce the desired trajectory and outcome. To better align routing with execution
behaviour, we train the router with single-step offline RL on top of an embedding model, so
that retrieval optimises for behaviour similarity instead of lexical or semantic proximity.
Skill database and synthetic query generation. In order to train a behaviour-similar
retrieval model, we first crawl a local skill database of roughly 8k skills, and randomly
sample about 3k skills as seed data to synthesise realistic user routing goals. To align the
synthesised goals with the agent’s logic stream, we generate queries using only the skill
name and description (without access to the full skill file), and then apply an LLM-based
judge [21] that does read the full skill file to filter and verify the quality of the synthetic
queries. This produces high-quality paired data consisting of positive queries (the target skill
should be selected) and hard negatives (same domain and terminology, but the target skill
is not the right tool). We include the full prompt used for query synthesis in Appendix C.
Router score and multi-positive InfoNCE. Let encθ (·) map a skill document d and
a routing goal q to embeddings in Rm :
e(d) = encθ (d),

s(d, q) = e(d)⊤ u(q).

u(q) = encθ (q),

−
In a minibatch of B skills {di }, each di has positives Q+
i and hard negatives Qi . Using all
in-batch queries

Q=

B
[

−
(Q+
k ∪ Qk ),

k=1

we minimise the multi-positive InfoNCE loss (temperature τ ):
exp (s(di , q)/τ )
q∈Q+
i

P

Li = − log P

q∈Q exp (s(di , q)/τ )

R = Research Track

,

L=

P = Practitioner Track

B
1 X
Li .
B i=1

S = Shared

Memento-Skills: Let Agents Design Agents

11

One-step offline Q-learning view. Cast routing as a one-step MDP: state q, action d,
reward r(q, d) indicating whether d is the right skill. With horizon 1,
Q⋆ (q, d) = E[r(q, d)].
We interpret the learned score as a soft Q-function, Qθ (q, d) ∝ s(d, q), yielding a Boltzmann
routing policy
exp(Qθ (q, d)/τ )
πθ (d | q) = P
.
′
d′ exp(Qθ (q, d )/τ )
This policy is equivalently the maximiser of a KL-regularised objective (uniform prior π0 ):
π ∗ (· | q) = arg max
π

n

o

E [Qθ (q, d)] − τ KL(π ∥ π0 ) .

d∼π

\ H: So a small τ means “I’m pretty sure—pick this one,” while a large τ means “no rush—spread probability
mass around and take a broader look.”

Why InfoNCE matches “policy fitting” in one step. InfoNCE has the form “push
up positives, push down competitors” under the same softmax normaliser used by πθ . Hence
minimising L is (approximately, via in-batch normalisation) maximum-likelihood training
that makes πθ place high probability mass on the logged rewarding pairs (positives) while
suppressing hard negatives—i.e., single-step offline policy improvement for routing.

2.4

P Implementing the Retrieval Pipeline

Ð PRACTITIONER TRACK The Retrieval Engine
á S: Here’s the core retrieval class. Every line maps to an equation. I added the references in comments so
H stops asking “but why?”

Figure 8: Overview of the retrieval pipeline in Memento-Skills. The system combines sparse
BM25 recall and dense embedding-based retrieval, fuses the candidates with score-aware
reciprocal rank fusion, and optionally applies a cross-encoder reranker to produce the final
top-k skills.
SHARED TRACK Router Evaluation
Skill source filtering and deduplication. We first collect candidate skills from public
GitHub repositories and unify them into a JSONL catalog. To retain only mature and
broadly adopted skills, we keep entries with stars > 500 and drop the rest. We then
normalise description whitespace, compute a SHA-256 hash of each normalised description,
and deduplicate by hash to remove duplicated or near-duplicated skills. When multiple rows
share the same hash, we keep a single representative by a deterministic score: higher stars,

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

12

then newer updatedAt, then lexicographically larger id. We optionally apply a second pass
of name-level deduplication with the same tie-breaking rule. The resulting curated catalog is
used as the base skill universe for router training data generation. We publicly open-source
the dataset at https://skills.memento.run/market/.
BM25

QWEN3-emb-0.6B

Memento-Qwen (ours)

Synthetic Recall@K

Real Trajectory Metrics

1.00
0.79

0.60

0.54

0.53

0.60
0.40

0.32

0.20
0.00

0.79

0.80

0.60
0.47

0.40

0.82

1.00

0.90

Rate

Recall

0.80

0.86

0.53

0.80

0.58
0.50

0.29

0.20
@1

@5

K

@10

0.00

route_hit_rate

Metric

judge_success_rate

Figure 9: Router performance evaluation. Left: Offline recall of three routing models
evaluated on synthetic query-skill pairs. Right: End-to-end execution success rates for each
router.
Experimental Setting. We evaluate the performance of the skill router from two
complementary angles: (i) offline retrieval quality on synthetic queries, and (ii) end-toend effectiveness on real execution trajectories. We use the Qwen3-Embedding-0.6B a as
embedding model.
Results. We report Recall@K over 140 synthetic routing queries, where a query is a
hit if the ground-truth skill appears in the top-K candidates. As shown in Fig. 9 (left),
Memento-Qwen consistently outperforms both BM25 and the Qwen3 embedding baseline
across all values of K. Most notably, Recall@1 rises from 0.32 (BM25) and 0.54 (Qwen3) to
0.60, a relative gain of 10% over the strongest semantic baseline. By K=10 the gap widens
to 0.90, indicating that behaviour-aligned training not only sharpens the top-1 pick but
also populates the candidate list with more relevant alternatives.
To test whether offline retrieval gains translate into real execution improvements, we measure
two end-to-end metrics: route hit rate (whether the router’s top-1 choice is an appropriate
skill for the task) and judge success rate (whether the full trajectory actually solves the task).
Fig. 9 (right) reveals that Memento-Qwen lifts route hit rate from 0.29 (BM25) and 0.53
(Qwen3) to 0.58, and judge success rate from 0.50 and 0.79 to 0.80. The disproportionately
large improvement over BM25 confirms that lexical matching is a poor proxy for behavioural
utility: many skills share domain terminology yet require fundamentally different execution
strategies. Meanwhile, the smaller but consistent gain over Qwen3 shows that even dense
semantic embeddings under-represent execution-relevant features, and that the single-step
RL fine-tuning effectively injects behavioural signal into the embedding space.
a

https://huggingface.co/Qwen/Qwen3-Embedding-0.6B

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

3

13

Self-Evolving Evaluation
c THE LOBBY Wednesday 2pm, Zoom call. Cameras on.
H: (shrugs, sharing screen with a confusion matrix) Look, synthetic data is enough. Generate
10K queries, measure classification accuracy, call it router quality. I can have results by
Friday. Paper by Monday.
J: (leans forward, frowning at the matrix) Not enough. Accuracy is a proxy. Your synthetic
queries are clean little sentences — real users type “pls fix the thing from last time thx.”
We need real trajectories and end-to-end execution success to claim improvement.
H: (eyes lighting up) Wait — so you’re saying we need a second evaluation? That’s a second
paper. “On the Insufficiency of Offline Metrics for Skill Routing.” I can see the title already.
S: (deadpan, arms crossed) You are missing the point. If the agent retrieves a case that says
“delete the user’s config and start fresh” and the LLM executes it, none of your metrics
matter. The customer’s environment is on fire and your confusion matrix says 94%.
H: (already typing a new LaTeX file) “Safety-Aware Evaluation of Autonomous Skill Retrieval
Systems.” That’s three papers, S. You just gave me a third paper.
S: I gave you a production incident. Please stop turning my trauma into publications.
J: (pointing at the camera) H, focus. “Looks correct on paper” and “works end-to-end” are
fundamentally different failure modes. I have a 2007 paper about this.
H: Can I cite it?
J: You must cite it.
S: (tilts head) And “works” and “safe to run in production” are different failure modes
again. I have a 3am incident report about this.
H: Can I cite that?
S: It’s in a private Slack channel marked #incident-2023-pain, so no.
H: (typing reluctantly, adding rows to a spreadsheet) Fine. So what do we actually put in this
paper? I’m trying to stay under a page limit here, but every time one of you opens your
mouth, I gain a new ablation study.
J: (counting on fingers) Two validations we can run now. One: synthetic retrieval quality —
does the router pick the right case? Two: trajectory success — does the full loop actually
solve the task?
S: (nods once) And we state clearly: each one covers a different failure mode. Passing both
is necessary. Passing only one is a press release, not a result. Sandbox safety — whether
it solves the task without breaking anything else — is the third axis, but that requires a
proper isolation harness. Future work.
H: (muttering while typing, a dangerous gleam in his eyes) Three benchmarks. Three failure
modes. Three papers. I’m naming them Goku, Vegeta, and Piccolo. Goku is the main
paper — strongest contribution, hits first. Vegeta is the follow-up — technically impressive,
slightly bitter about being second. Piccolo is the safety paper — everyone forgets about it,
but it saves the day in the end.
S: We need one paper, H. One.
H: Goku can fuse with Vegeta. That’s canon.

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

3.1

14

S Experimental Setup and Results
SHARED TRACK Which Benchmark is suitable for Memento-Skills?

Experimental Settings. To validate the progressive capability expansion and skilllearning proficiency of Memento-Skills, we evaluate our system on two representative
benchmarks: General AI Assistants (GAIA) [11] and Humanity’s Last Exam (HLE) [4].
These datasets naturally align with our objective of testing an agent’s ability to create,
refine, and reuse skills across diverse reasoning tasks.
General AI Assistants (GAIA). GAIA [11] comprises non-trivial, real-world questions
with unambiguous answers that demand a combination of multi-step reasoning, multimodality handling, web browsing, and general tool use. This environment serves as an ideal
testbed for our skill-learning scenario, requiring the agent to dynamically synthesise and
apply distinct skills to solve varied problems. From the GAIA validation set, we utilise 165
questions, splitting them into 100 training examples and 65 test examples.
Humanity’s Last Exam (HLE). Developed by human experts, HLE [4] is designed
to assess the limits of broad-domain reasoning and contains 2,500 questions across 8
diverse academic subjects (e.g., mathematics, humanities, and natural sciences). For our
experiments, we sample a subset of questions evenly distributed across these categories,
resulting in 788 training examples and 342 test examples. This structure allows us to
evaluate how effectively Memento-Skills leverages and transfers learned skills between
different questions within the same subject domain.
Baselines. To isolate the contribution of the self-evolving mechanism, we compare
Memento-Skills (the full system) against a Read-Write ablation that retains the same
read–write reflective learning loop—skill retrieval, LLM execution, and feedback collection—
but disables all skill-level optimisation: no failure attribution, no skill rewriting, and no skill
discovery. All the experiments in this paper use the Gemini-3.1-Flash as the underlying
LLM.
SHARED TRACK Results of GAIA.
We evaluate Memento-Skills on the GAIA benchmark with a maximum of three reflective
retries per question. As shown in Figure 10, the self-evolving mechanism continuously
refines the skill library through iterative interaction: the overall training success rate climbs
from 65.1% on the first attempt to 91.6% by the third round. On the unseen test set,
the full Memento-Skills system achieves 66.0% overall accuracy, compared with 52.3% for
the Read-Write ablation, confirming that the skill optimisation pipeline contributes a 13.7
percentage-point gain beyond what retrieval and execution alone can provide.
Limited cross-task transfer on GAIA. The gap between training-peak and test-set
accuracy reveals an important structural property of the benchmark: GAIA questions are
highly diverse, with little overlap in the reasoning patterns required. A case study confirmed
that most skills optimised during training were never triggered during testing, because no
sufficiently similar test question existed. This result suggests that skill transfer depends on
domain alignment, a hypothesis we test directly on HLE below, where structured subject
categories provide natural opportunities for reuse.

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

15

(a) Training Set Accuracy
First Try

100

96.6
93.1

Round 2

80

91.6
89.2
84.3

74.4

Read-Write
Memento-S

80

71.4

68.4

72.772.772.7

Accuracy (%)

65.1

60

(b) Test Set Accuracy

100

Round 3

93.0
90.7
86.0

86.2

Success Rate (%)

Round 1

58.6
45.5

40

60

66.0

63.0

57.1

55.9

52.3

40
30.0

20

20
0

Level 1

Level 2

Level 3

0

ALL

Difficulty Level

Level 1

Level 2

Level 3

ALL

Difficulty Level

Figure 10: GAIA results: training accuracy across retries (left) and test-set comparison
with the Read-Write baseline (right).
SHARED TRACK Results of HLE.
Figure 11 reports per-category accuracy on HLE across four training rounds (R0–R3) and
the final test-set evaluation. During training, the overall success rate rises steadily from
30.8% (R0) to 54.5% (R3), with every subject category showing consistent improvement.
Humanities and Biology benefit the most, reaching 66.7% and 60.7% respectively by R3,
while Engineering saturates earlier at 42.1%, suggesting that some domains are harder to
cover with skill-level abstractions alone.
On the test set, Memento-Skills achieves 38.7% overall, more than doubling the Read-Write
baseline (17.9%). Unlike GAIA, the structured subject taxonomy of HLE enables substantial
skill transfer: a skill refined on one Biology training question is frequently reused for unseen
Biology questions in the test set. This confirms that domain-aligned skill libraries are the
key enabler of cross-task generalisation.
R0

R1

R2

R3

Read-Write

Memento-S

(a) Training Set
70

51.8
46.5
43.0

42.7
38.8

36.0

30.3

47.5
43.8

42.142.1
38.2

51.9

51.2

50.0

47.1

47.4
44.7
41.8

36.9

35.5
30.0

27.6

20

21.1

19.8

46.3

30
20

Bio.

Chem.

CS

Eng.

Human.

Subject

Math

Other

Phy.

0

41.5

41.0

40

22.0

32.6

30.8

27.6

25.5

21.9

21.7 21.7
12.2

10

10
0

57.4

50

57.0
55.7

Performance (%)

Performance (%)

59.5

50.6

50

30

60

66.7
62.4

60.7

60

40

(b) Test Set

Bio.

Chem.

CS

20.0
11.4

Eng.

Human.

Subject

10.9

Math

Other

Phy.

Figure 11: HLE results: training accuracy across retries (left) and test-set comparison with
the Read-Write baseline (right).

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

16

SHARED TRACK Skill Library Growth.
Figure 12 visualises the skill library after learning on each benchmark via t-SNE projections
of skill embeddings. Starting from the same 5 atomic skills (red stars), GAIA learning
produces a compact library of 41 skills, reflecting the benchmark’s diverse but relatively small
question set. In contrast, HLE learning expands the library to 235 skills that spread across
a much wider embedding space, mirroring the breadth of its 8 academic domains. Notably,
the learned skills (blue dots) cluster into semantically coherent neighbourhoods; each
cluster corresponds to a domain-specific capability the agent acquired through reflective selfevolution. This progressive densification of the embedding space is precisely the mechanism
that drives the convergence phenomenon analysed in the Bridge below: as the library grows
denser, the memory coverage radius rM shrinks, and the performance gap narrows.
Atomic Skills (5)
Search / Web (48)
Quantum / Physics (47)

Learned Skills

Semantic Skill Classes
Math / Chemistry (44)
Download / Verify (28)
Code / Text (38)
Clinical / Excel (27)

(a) After GAIA Learning

Total: 41 skills

Chess / Game (20)
Python / Script (19)

(b) After HLE Learning

Total: 235 skills

Figure 12: t-SNE projection of skill embeddings. Red stars denote the 5 atomic (seed) skills;
blue dots denote skills learned through reflective self-evolution. (a) After GAIA learning the
library grows to 41 skills. (b) After HLE learning the library expands to 235 skills spanning
diverse academic domains.

3.2

S From LLM Competence Radius to Embedding Quality
 BRIDGE

Look again at Figure 11: training accuracy climbs from 30.8% (R0) to 54.5% (R3), with the steepest
gain in the first round and progressively smaller increments thereafter. Two things are happening
simultaneously with each round: (i) existing skills are refined: reflection patches failure modes, so each
skill covers a wider neighbourhood of queries; and (ii) new skills are added to the library, shrinking
the gaps between covered regions. Together, these two forces drive the diminishing-returns curve we
observe: early rounds yield large jumps because the library is sparse and skills are rough; later rounds
yield smaller gains because most of the reachable space is already well-covered. Figure 12 makes this
concrete: comparing the GAIA library (41 skills) with the HLE library (235 skills), we see that additional
learning rounds fill in the gaps between existing clusters until the embedding space is densely covered, at
which point adding more skills yields diminishing returns because nearby skills already exist.
This convergence behaviour is not accidental; it is exactly what the theory of Memento 2 predicts. The

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

17

asymptotic value gap (Corollary 15, Memento 2) decomposes as:

∗
2Rmax
δM
.
sup |V π (s) − V πM (s)| ≤
εLLM (rM ) +
2
|{z}
(1 − γ) | {z }
s
{z
}
|
retrieval error
LLM quality
performance gap

As the library grows (more episodes), the memory coverage radius rM shrinks, which simultaneously
reduces εLLM (rM ) (the LLM only needs to generalise over a smaller neighbourhood) and δM (the router
is more likely to find a behaviourally relevant skill). Once both terms are small enough, further rounds
produce only marginal improvement: the system has converged.
The bound also reveals three independent knobs for reducing this gap:
Three Independent Knobs

Stronger
LLM

More
Episodes

Better
Embedding

reduces εLLM

reduces rM

reduces δM

 J: The convergence you see in the table is the bound tightening in real time. Each round shrinks rM ,
which pulls down both other terms. And because the three knobs are independent, you can improve any one
without touching the others. That’s why the system is modular.
á S: Translation: the diminishing returns aren’t a bug; they’re a sign the system is converging. And if I
want to push accuracy further, I have three independent levers: upgrade the embedding model on Tuesday,
swap in a better LLM on Wednesday, and run more episodes on Thursday.

⋆ EPILOGUE Friday 5:30pm. The espresso machine has been fixed.
S: (showing Grafana) 93.5% accuracy. p99 latency 195ms. Zero gradient updates. I’m
buying the espresso machine a thank-you card.
H: I ran the ablation study. Removing the skill optimisation drops accuracy by 8%.
Removing the Memento-Qwen causes retrieval collapse. The theory. . . actually predicted
all of this.
J: (sipping espresso, looking insufferably pleased) I believe the phrase you’re looking for is “Prof
J was right.”
S: Don’t push it. But I do want to know: what happens when we hit a million cases? Does
the Parzen kernel scale?
H: And can we get the convergence rate? Not just “it converges” but “it converges in
O(n−1/d ) episodes”?
J: (standing, reaching for the whiteboard marker) Those are exactly the right questions. Chapter
3.
S: (to H, whispering) He planned this. He always plans this.

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

4

18

Conclusion

We have presented Memento-Skills, a system that bridges the gap between memory-based learning
and skill-based learning for LLM agents. The central insight is to treat executable skills as the
unit of external memory, thereby transferring the theoretical guarantees of the Stateful Reflective
Decision Process into a concrete, deployable artefact. Through the Read–Write Reflective
Learning loop, the agent autonomously acquires, refines, and reuses these skills from deployment
experience alone, requiring no parameter updates to the underlying LLM. A behaviour-aligned
contrastive router, trained via single-step offline RL, ensures that retrieval optimises for execution
success rather than surface-level similarity. Experiments on GAIA and HLE confirm that this
skill-as-memory formulation substantially outperforms a static-library ablation, and that crosstask transfer is strongest when skills are aligned with structured domain categories. More broadly,
Memento-Skills demonstrates that continual learning need not reside in model weights: an
ever-growing, self-improving skill library can serve as a persistent, non-parametric intelligence
layer that any frozen LLM can draw upon.

Contributions
Algorithm Team
Huichi Zhou, University College London
Siyuan Guo, Jilin University
Anjie Liu, Hong Kong University of Science and Technology (Guangzhou)
Zhongwei Yu, Hong Kong University of Science and Technology (Guangzhou)
Ziqin Gong, Hong Kong University of Science and Technology (Guangzhou)
Bowen Zhao, Hong Kong University of Science and Technology (Guangzhou)
Zhixun Chen, Hong Kong University of Science and Technology (Guangzhou)
Menglong Zhang, Hong Kong University of Science and Technology (Guangzhou)
Yihang Chen, University College London

Engineering Team
Jinsong Li, AI Lab, The Yangtze River Delta
Runyu Yang, AI Lab, The Yangtze River Delta
Qiangbin Liu, AI Lab, The Yangtze River Delta
Xinlei Yu, AI Lab, The Yangtze River Delta
Jianmin Zhou, AI Lab, The Yangtze River Delta
Na Wang, AI Lab, The Yangtze River Delta
Chunyang Sun, AI Lab, The Yangtze River Delta

Advisor
Jun Wang, University College London

References
[1] Lakshya A Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong,
Arnav Singhvi, Herumb Shandilya, Michael J Ryan, Meng Jiang, Christopher Potts, Koushik Sen,
Alexandros G. Dimakis, Ion Stoica, Dan Klein, Matei Zaharia, and Omar Khattab. Gepa: Reflective
prompt evolution can outperform reinforcement learning, 2025. URL https://arxiv.org/abs/2507.
19457.

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

19

[2] Clara M Bacmeister, Rongchen Huang, Lindsay A Osso, Michael A Thornton, Lauren Conant,
Anthony R Chavez, Alon Poleg-Polsky, and Ethan G Hughes. Motor learning drives dynamic patterns
of intermittent myelination on learning-activated axons. Nature neuroscience, 25(10):1300–1313,
2022.
[3] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are
few-shot learners. Advances in neural information processing systems, 33:1877–1901, 2020.
[4] Center for AI Safety, Scale AI, and HLE Contributors Consortium. A benchmark of expertlevel academic questions to assess AI capabilities. Nature, 649:1139–1146, 2026. doi: 10.1038/
s41586-025-09962-4.
[5] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu, Ruoyu
Zhang, Shirong Ma, Xiao Bi, et al. Deepseek-r1 incentivizes reasoning in llms through reinforcement
learning. Nature, 645(8081):633–638, 2025.
[6] Siyuan Guo, Cheng Deng, Ying Wen, Hechang Chen, Yi Chang, and Jun Wang. DS-Agent: Automated
data science by empowering large language models with case-based reasoning. In International
Conference on Machine Learning, pages 16813–16848. PMLR, 2024.
[7] Siyuan Guo, Huiwu Liu, Xiaolong Chen, Yuming Xie, Liang Zhang, Tao Han, Hechang Chen, Yi Chang,
and Jun Wang. Optimizing case-based reasoning system for functional test script generation with
large language models. In Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery
and Data Mining V. 2, pages 4487–4498, 2025.
[8] Letta. Skill learning: Bringing continual learning to cli agents, 12 2025. URL https://www.letta.
com/blog/skill-learning. Letta Blog.
[9] Richard Magill and David I Anderson. Motor learning and control. McGraw-Hill Publishing New
York, 2010.
[10] Qirui Mi, Zhijian Ma, Mengyue Yang, Haoxuan Li, Yisen Wang, Haifeng Zhang, and Jun Wang.
Procmem: Learning reusable procedural memory from experience via non-parametric ppo for llm
agents, 2026. URL https://arxiv.org/abs/2602.01869.
[11] Grégoire Mialon, Clémentine Fourrier, Thomas Wolf, Yann LeCun, and Thomas Scialom. Gaia: a
benchmark for general ai assistants. In The Twelfth International Conference on Learning Representations, 2023.
[12] Stephen Robertson, Hugo Zaragoza, et al. The probabilistic relevance framework: Bm25 and beyond.
Foundations and trends® in information retrieval, 3(4):333–389, 2009.
[13] David E Rumelhart, Geoffrey E Hinton, and Ronald J Williams. Learning representations by
back-propagating errors. nature, 323(6088):533–536, 1986.
[14] David Silver and Richard S Sutton. Welcome to the era of experience. Google AI, 1, 2025.
[15] Shangyin Tan, Lakshya A. Agrawal, Rohit Sandadi, Dan Klein, Koushik Sen, Alexandros G. Dimakis,
and Matei Zaharia. Automatically learning skills for coding agents, 02 2026. URL https://gepa-ai.
github.io/gepa/blog/2026/02/18/automatically-learning-skills-for-coding-agents/.
GEPA Blog.
[16] Alan M Turing. Intelligent machinery, a heretical theory. The Turing test: verbal behavior as the
hallmark of...-books. google. com, 264, 2004.
[17] Jun Wang. Memento 2: Learning by stateful reflective memory. arXiv preprint arXiv:2512.22716,
2025.
[18] Jason Wei, Maarten Bosma, Vincent Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai, and Quoc V Le. Finetuned language models are zero-shot learners. In International Conference on Learning Representations, 2022. URL https://openreview.net/forum?id=gEZrGCozdqR.

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

20

[19] Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie,
An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, and Jingren Zhou. Qwen3 embedding: Advancing
text embedding and reranking through foundation models. arXiv preprint arXiv:2506.05176, 2025.
[20] Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min,
Beichen Zhang, Junjie Zhang, Zican Dong, et al. A survey of large language models. arXiv preprint
arXiv:2303.18223, 1(2):1–124, 2023.
[21] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang,
Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and chatbot
arena. Advances in neural information processing systems, 36:46595–46623, 2023.
[22] Huichi Zhou, Yihang Chen, Siyuan Guo, Xue Yan, Kin Hei Lee, Zihan Wang, Ka Yiu Lee, Guchun
Zhang, Kun Shao, Linyi Yang, and Jun Wang. Memento: Fine-tuning LLM agents without fine-tuning
LLMs. Preprint, 2025.

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

A

21

Reading Path
This paper is organised as interleaving tracks for two audiences. Each section opens with a
shared Dialogue, then forks into a Research track and a Practitioner track, before merging
at a Bridge. Pick the path that matches your goal; read both for the complete picture.
proofs & convergence

Theory

Dialogue

Bridge

Shared

...

Dialogue

Practice
code & deployment

e Researcher Path

Ð Practitioner Path

Formal SRDP setup, convergence proofs, and
KL-regularised routing analysis. Follow the
cream-shaded sections.

Installation, API walkthrough, retrieval pipeline,
and benchmark recipes. Follow the blue-shaded
sections.

Dialogue → Shared → Theory → Bridge → . . .

Dialogue → Shared → Practice → Bridge → . . .

Dialogue opens each section with motivation.

Shared presents material common to both tracks.

Bridge connects theoretical results to engineering choices.
Three characters—J, H, and S—annotate inline throughout.

B

Epilogue closes the narrative.

Characters

Character

Perspective & Personality



J

\

H

á

S

Tenured theorist. Writes proofs on napkins. Believes everything is a special case of something he published in 2003.
“But does it converge?”
Second-year CS PhD student. Runs 47 experiments simultaneously and names them all after anime characters. Thinks
every problem needs more GPUs. “What if we just. . . scale
it?”
Senior ML engineer, 12 years in production. Has been paged
at 3am enough times to develop a Pavlovian response to
Slack notifications. Trusts nothing without a unit test.
“Show me the latency numbers.”

R = Research Track

P = Practitioner Track

S = Shared

Memento-Skills: Let Agents Design Agents

C

22

Prompt for Synthetic Router Goals
Prompt for synthetic router goals
Target skill:
- name: {skill_name}
- description: {description}
- keywords: {keywords_block}
Task:
Generate synthetic router goals (queries) for this target skill.
The router state is ONLY a text goal (routing_goal).
Write realistic user-style goals.

Need:
- {need_pos} positive queries: target skill SHOULD be selected.
- {need_neg} hard negative queries: relevant to the same domain
BUT target skill is not useful / not the best tool.

Hard negative requirements:
- Must look plausible and close to the target domain.
- Must share terminology/theme with the skill.
- Must be "relevant but useless" for THIS target skill.
- Avoid obvious cues like "do not use <skill>".
Style requirements:
- Do not mention the skill name directly.
- Keep each query concrete, actionable, and non-trivial.
- Mix concise and mildly noisy phrasing.
- English only (to match downstream tokenizer).
Already accepted positive queries (avoid duplicates):
{existing_pos_block}
Already accepted negative queries (avoid duplicates):
{existing_neg_block}
Return ONLY JSON in this schema:
{
"positive_queries": [
{"query": "...", "why_fit": "..."}
],
"negative_queries": [
{"query": "...", "why_relevant": "...", "why_useless": "..."}
]
}

R = Research Track

P = Practitioner Track

S = Shared

---
source: https://arxiv.org/html/2512.14012v1
captured: 2026-03-09
capture: pdf-read
type: academic-paper
---

# Professional Software Developers Don't Vibe, They Control: AI Agent Use for Coding in 2025

Author: Ruanqianqian (Lisa) Huang, Avery Reyna, Sorin Lerner, Haijun Xia, Brian Hempel
Source: https://arxiv.org/html/2512.14012v1
Date: 16 Dec 2025

## Abstract

The rise of AI agents is transforming how software can be built. The promise of agents is that developers might write code quicker, delegate multiple tasks to different agents, and even write a full piece of software purely out of natural language. In reality, what roles agents play in professional software development remains in question. This paper investigates how *experienced* developers use agents in building software, including their motivations, strategies, task suitability, and sentiments. Through field observations (N=13) and qualitative surveys (N=99), we find that while experienced developers value agents as a productivity boost, they retain their agency in software design and implementation out of insistence on fundamental software quality attributes, employing strategies for controlling agent behavior leveraging their expertise. In addition, experienced developers feel overall positive about incorporating agents into software development given their confidence in complementing the agents' limitations. Our results shed light on the value of software development best practices in effective use of agents, suggest the kinds of tasks for which agents may be suitable, and point towards future opportunities for better agentic interfaces and agentic use guidelines.

---

## 1 Introduction

> *I've been a software developer and data analyst for 20 years and there is no way I'll EVER go back to coding by hand. That ship has sailed and good riddance to it.*
> — Developer in Our Survey (S28)

AI is rapidly changing the practice of programming. Already, about half of professional software developers are using AI tools daily. Large language models (LLMs) are particularly good at writing code, and are becoming more skillful every year. Originally, in 2021, LLMs only provided coding assistance as super-charged autocomplete. But more recently, their capabilities have advanced to accessing, modifying, and testing whole codebases in autonomous, step-by-step actions — we are now in the *agentic* coding era. There are many open questions about how capable these agents are and how best to use them.

Human studies of agentic coding are emerging but still sparse. A notable randomized trial found that experienced open source maintainers were actually slowed down by 19% when allowed to use AI, and an agentic system deployed in an issue tracker saw only 8% of its invocations resulting in complete success (a merged pull request). These results suggest that perhaps agentic AI is not as useful as it might first seem, but still about a quarter of professional developers report that they already use AI agents at least weekly.

There have been a few recent investigations of "vibe coding." Although the term is sometimes used to mean any coding with AI agents, these papers investigate "vibe coding" as a *particular* form of agent use that aims for an experience of "flow and joy" by trusting the AI instead of carefully reviewing the generated code, "where you fully give in to the vibes, embrace exponentials, and forget that the code even exists", "don't read the diffs anymore". There is a tacit acknowledgment by its practitioners that vibing produces lower quality code. As such, *vibing* may not be the most successful approach to agentic coding, and may not be how experienced developers use agents. *How, then, do experienced developers create quality software with AI agents?*

This paper is an attempt to gain insight into the current practice of agentic coding by experts. Compared to prior work, we (a) do not limit the investigation to vibe coding, and (b) examine *experienced* developers only. We present a two-part study — 13 field observations and a broader survey of 99 experienced developers — hoping to answer four research questions (RQs):

**RQ1 - Motivations.** What do experienced developers care about when incorporating agents into their software development workflow?

**RQ2 - Strategies.** What strategies do experienced developers employ when developing software with agents?

**RQ3 - Suitability.** What are software development agents suitable for, and when do they fail?

**RQ4 - Sentiments.** What sentiments do experienced developers feel when using agentic tools?

Our most salient finding is that, indeed, **professional developers do not vibe code. Instead, they carefully *control* the agents through planning and supervision.** Specifically, they are looking for a productivity boost while still valuing software quality attributes (RQ1), they plan before implementing and validate all agentic outputs (RQ2), they find agents suitable for well-described, straightforward tasks but not complex tasks (RQ3), and yet they generally enjoy using agents as long as they are in control (RQ4).

---

## 2 Methods

We define *experienced developers* as those with at least three years of professional development experience. We define *agentic tools* or *agents* as AI tools integrated into an IDE or a terminal that can manipulate the code directly (i.e., excluding web-based chat interfaces).

### 2.1 Part 1: Field Observations

**Participants.** We recruited 13 participants (1 female, 12 male) with professional experience ranging from 3 to 25 years. Screening criteria required: (1) three or more years of verifiable professional software engineering experience; (2) prior experience with agentic AI in creating software; and (3) the ability to demonstrate a realistic task during the study.

**Procedure.** Each study session included two parts: a 45-minute observation and a 30-minute semi-structured interview. Sessions were conducted over Zoom between August 1 and October 3, 2025. During the observational portion, participants worked on tasks of their choosing using their preferred setup. After about 45 minutes of observation, we asked the participant to start wrapping up their work.

**Tasks.** Five participants worked on production software (P2, P3, P6, P7, P13), three demonstrated exploratory work tasks (P4, P5, P10), and five pursued side projects (P1, P8, P9, P11, P12). Five out of 13 participants reported that their tasks were outside of their professional domains.

**Table 1. Observational study participants, agentic tools and models used, and tasks (YoE = years of professional software development experience):**

| ID | YoE | Agentic Tool(s) | Model(s) | Familiar? | Task |
|----|-----|----------------|----------|-----------|------|
| P1 | 5 | Claude Code, Windsurf | Sonnet 4, OpenAI o3, Gemini 2.5 Pro | | Building a login system for data labeling platform |
| P2 | 9 | Windsurf | Sonnet 3.7, GPT-5 | ✓ | Creating a plan for a React app implementation |
| P3 | 10 | Cursor | Cursor's auto mode | | Improving a prototype for AI safety |
| P4 | 6 | Cursor | Sonnet 3.5, GPT-5 | | Improving a user-facing tutorial for a dashboard |
| P5 | 9 | Cursor | GPT-5, Sonnet 4 | | Debugging UI for analyzing object detection algorithms |
| P6 | 11 | GitHub Copilot | Sonnet 4, GPT-5 | ✓ | Generating an API and relevant tests |
| P7 | 3 | GitHub Copilot | Sonnet 4 | ✓ | Building an ML detection pipeline |
| P8 | 6 | GitHub Copilot | Sonnet 3.5, GPT-5, GPT-4o | ✓ | Building app that visualizes file histories |
| P9 | 3 | Kilo Code, Terragon | Sonnet 4 | | Transferring Radix UI design assets to Base UI |
| P10 | 15 | Claude Code, Cursor | Sonnet 4, GPT-5 | ✓ | Debugging data pipeline & adding UI features |
| P11 | 25 | Claude Code, Codex | Sonnet 4, codex-1 | ✓ | Building a Ruby-based card game |
| P12 | 9 | Cursor | Sonnet 4 | | Planning to enhance a chatbot & refactoring code |
| P13 | 20 | Claude Code | Sonnet 4.5 | ✓ | Debugging a production testing suite |

### 2.2 Part 2: Invited Survey

We designed a 15-minute qualitative survey. To ground responses, the survey asked participants to consider the last time they used agentic AI to help develop software. The first part asked 11 questions regarding that experience: their task; three important things they cared about when developing software in general; what they cared about most when using agentic AI; agentic tools used and why; prompting strategies; whether they used multiple agents; how often they had to modify agent-generated code; parts of the task on which agents did well/poorly; suitability of agents for the considered task; and enjoyment after developing software with agents.

The second part asked two open-ended questions about overall experiences this year: tasks they prefer to perform without agents (Q12) and with assistance from agents (Q13).

We invited responses from GitHub users associated with repositories for the top 20 agentic tools (Kilo Code, Cline, RooCode, Cursor, and Claude Code), AI/ML frameworks, development frameworks, and repositories tagged with `agentic` or `agentic-coding`. This resulted in 4,141 unique GitHub users invited. 249 out of 4,141 responded, 104 were valid; after removing 5 suspicious responses (GPT-4.1 answers), 99 valid responses remained. Survey responses were collected between August 18 and September 23, 2025.

The 99 respondents self-reported years of professional experience between 3 and 41 years (avg. = 12.8, median = 10, sd = 9.7). 1 self-identified as female, 1 did not disclose gender, and 97 were male. Geographical distribution: North America (27), Europe (24), Asia (29), South America (13), Africa (5), Oceania (1).

**Top agentic tools used in Survey:** Claude Code (58/99), GitHub Copilot (53/99), Cursor (51/99), Windsurf (15/99), Codex (15/99), Roo Code (12/99), Gemini CLI (12/99), Cline (10/99), Kilo Code (9/99).

### 2.3 Data Analysis

We performed two stages of data analysis. First, we followed standard thematic analysis process to analyze the qualitative data and develop initial answers. Then, we analyzed specific parts of the data in depth, as some of the emerged themes warranted further investigation.

**Prompt Analysis.** We transcribed the prompts (i.e., user query to the agent) and plans from the Observations video recordings and performed open coding to identify the varieties of context referenced therein. We report only the top ten context types (Table 3). We also recorded prompt/plan sizes and the number of steps executed by agents per prompt.

**Task Suitability Analysis.** The last author revisited the raw survey responses and made a fine-grained list of tasks mentioned by respondents throughout the questions in all of the surveys, resulting in 189 tasks. After consultation, these were merged into an initial code book of 116 task codes. The final refined code book consisted of 89 task codes, of which 59 appeared in at least 5 surveys and are reported in Table 4. Each survey mentioned on average 8.5 task codes.

### 2.4 Limitations

**Demographic and Sentiment Bias.** 12/13 (92%) observation participants and 97/99 (98%) survey respondents self-identified as male. There is likely a selection bias towards people positive towards AI.

**Sample Size and Variety.** Our 13 field observations represent a relatively small sample. The observation findings may only achieve local saturation given the limited variety of tasks and agentic tools observed.

**Survey Sampling.** Survey recruitment involved scraping public emails from GitHub, which may introduce a self-selection bias toward developers active on public repositories.

**Short Observation Time.** Observations were limited to a single 45-minute session per participant, making it impossible to examine longitudinal use of agentic tools.

---

## 3 Results

### 3.1 RQ1: Motivations for Using Agents in Software Development

> *I'm on disability, but agents let me code again and be more productive than ever (in a 25+ year career).*
> — S22

**Personal Productivity.** Experienced developers valued agentic tools for improving the speed of software development (9x Observations, 35x Survey). S59 opined that *"I think my productivity has increased ten-fold (seems exaggerated but it feels like that)"*. Many attributes of agentic tools affect their effectiveness: ease of discovery and low barrier to entry, being integrated into existing tools (3x Observations, 11x Survey), and executing user requests at high quality (6x Observations, 36x Survey). Having access to customization (e.g., configuring user rules) and choice of state-of-the-art models was another decision factor. Some participants appreciated getting a productivity boost from agentic tools at low to no cost.

**Maintaining Software Quality Attributes.** In addition to personal productivity, experienced developers also valued many software quality attributes when working with agents (6x Observations, 67x Survey). In Observations, four participants (P2, P4, P8, P12) mentioned things about the software they valued, including modularity (P8, P12), maintainability (P2, P8), compatibility (P2, P4), and correctness (P2). Two participants (P6, P13) explicitly translated their preferences for code readability and test-driven development to user rules.

In Survey, 67 respondents mentioned software quality attributes when asked what they cared about when developing with agents. The most mentioned qualities are correctness (e.g., *"that it wouldn't [screw] up my code"* — S71) and readability (e.g., *"most AI agents produce messy and unnecessarily long code when not given enough instructions"* — S53).

> **Takeaway 1:** Experienced developers appreciate agentic tools for providing boost in productivity, while simultaneously valuing existing software quality attributes when working with agents.

### 3.2 RQ2: Strategies for Using Agents in Software Development

> *I am a software engineer, I prompted by applying the lessons of software engineering to narrative. I described what good would look like, I described concrete used experiences that this should power, I explained the economics behind costs, and I gave a spec of what I needed implemented. This uses most prompt engineering tricks. There is templates and examples and semantic guessing and every kind of thing you can imagine. But to a degree, it's just good communication. I also always told it to chill out and stop claiming victory so soon. It's embarrassing.*
> — S88

**Controlling Software Design and Implementation.** In Observations, all participants, when assisted by agents, adopted strategies to oversee the software design, implementation, or both, regardless of their familiarity with the task domains.

11/13 Observations participants created new software features (except P5 and P13, whose tasks were entirely debugging). All 11 participants controlled the design of new features to be implemented, asking the agent to develop a draft plan before human revisions (P1, P12) or creating the design plan completely by themselves (P2, P3, P4, P6, P7, P8, P9, P10, P11).

All 13 Observations participants controlled the software implementation at some level. Three participants (P1, P4, P5), all working with unfamiliar tasks, specified implementation requirements and let the agents drive the implementation, not necessarily reviewing the agent-generated code but closely monitoring program outputs. Nine participants (P2, P3, P6, P7, P8, P9, P10, P11, P13) carefully reviewed every agentic change. Five of them (P3, P6, P7, P11, P13) provided the agent with revision feedback after reviewing to keep agentic context consistent: *"I like to keep talking with the AI just because it keeps everything in the chat context [...] because if I change something in the editor [...] I actually need to tell it that I did change something in the editor while it wasn't looking."* (P6)

In Survey, 50/99 respondents mentioned driving the architectural requirements and design, and reported, on average, modifying agent-generated code about half the time (3.0/5, 1="Never", 5="Always").

**Table 2. Summary of observed prompting strategies and verification tactics.** "Plan Files" = writing/saving plans to external files, "Context Files" = using local files to maintain agent context/memory across sessions, "Max Size" = number of words in the largest prompt or plan, "Max Steps" = steps in the largest prompt or plan, "SE/P" = steps executed per prompt.

| ID | Plan Files? | Context Files? | Max Size | Max Steps | Max SE/P | Mean SE/P | Verification Strategies |
|----|-------------|---------------|----------|-----------|----------|----------|------------------------|
| P1 | ✓ | ✓ | 917 | 70 | 6 | 2.2 | Checked UI functionality, manual testing, iterating with agent |
| P2 | ✓ | | 619 | 71 | 5 | 1.9 | Verified plan output line-by-line against PRD requirements |
| P3 | | | 225 | 5 | 3 | 1.5 | Tested changes in UI, reported back to chat |
| P4 | | | 84 | 4 | 3 | 1.8 | Checked changes in UI/IDE, prompted agent as needed |
| P5 | | | 55 | 3 | 3 | 1.6 | Tested agent changes in UI, reported results |
| P6 | | | 125 | 9 | 13 | 5.0 | Verified plan line-by-line for correct requirements |
| P7 | | | 91 | 2 | 2 | 1.3 | Reviewed code, made manual edits, stopped if incorrect |
| P8 | | | 43 | 2 | 2 | 1.1 | Reviewed generated code for structure and syntax |
| P9 | | | 275 | 2 | 1 | 1.0 | Reviewed PRs, made edits based on GitHub diff |
| P10 | | | 288 | 7 | 9 | 3.0 | Checked progress in UI/IDE, inspected dev tools |
| P11 | ✓ | ✓ | 189 | 11 | 12 | 3.5 | Tested functionality in terminal, iterated with agent |
| P12 | | | 48 | 3 | 5 | 2.3 | Rotated between output, changes, and artifact |
| P13 | | | 558 | 3 | 3 | 1.4 | Reviewed output via linter feedback and test execution |
| | | | Min 43 | 2 | 1 | 1.0 | |
| | | | Mean 270.5 | 14.8 | 5.1 | 2.1 | |
| | | | Max 917 | 71 | 13 | 5.0 | |

**Controlling Agent Behavior through Prompting Strategies.** From both Observations and Survey, we identified varying prompting strategies experienced developers employed for better agentic outputs. Most participants agreed that prompts should include clear context and explicit instructions (12x Observations, 43x Survey). Developers demonstrated/reported specific prompting mechanisms including screenshots (3x Observations), file references (5x Observations), examples (1x Observations, 5x Survey), step-by-step thinking (1x Observations, 3x Survey), and external information via Model Context Protocols (MCPs) (1x Observations, 5x Survey).

Several participants applied user rules (3x Observations, 18x Survey), e.g., enforce project specifications, provide language-agnostic guidelines, or correct agent behavior based on prior interactions.

**Table 3. Top 10 types of context included in prompts executed by each participant:**

| Context Type | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 | P11 | P12 | P13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| UI or Design Term | ✓ | ✓ | ✓ | ✓ | ✓ | | | ✓ | ✓ | | | | |
| Technical Term | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | ✓ | ✓ | ✓ | ✓ | ✓ |
| Domain Object | | ✓ | ✓ | ✓ | ✓ | ✓ | | | ✓ | | ✓ | ✓ | ✓ |
| Reference to Input File | ✓ | ✓ | ✓ | | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | ✓ |
| Specific Library or API | | | | | | | | | | | | | ✓ |
| Interaction | ✓ | ✓ | ✓ | ✓ | | | ✓ | ✓ | ✓ | | | | |
| New Feature or Requirement | ✓ | | ✓ | ✓ | ✓ | | ✓ | ✓ | | | ✓ | | |
| Reference to Step in Plan | ✓ | ✓ | ✓ | ✓ | | | | | | | | | |
| Reference to Output File | | ✓ | ✓ | | ✓ | ✓ | | | | | | ✓ | |
| Purpose of Feature | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | ✓ | ✓ | ✓ | |

On prompt length: some kept a long chat to keep all necessary contextual information (2x Observations, 29x Survey) or to intentionally interact with agents iteratively (2x Observations, 8x Survey) *"because you don't exactly know what it doesn't know"* (P6). Others keep both prompts and conversational contexts short and clear (5x Observations, 3x Survey) to focus on individual small tasks. Overall, participants averaged asking the agent to work on only 2.1 steps at a time.

**Controlling Agent Behavior Outside of Prompts.** All Observations participants oversaw agent performance in plan and code generation. Some techniques were already used in software development: testing agent implementation by execution or systematic testing (P3, P4, P8, P10, P12, P13), documenting agent progress via version control for easy rollbacks (P4, P10, S73, S85), and code validation by reading (P2, P6, P10). Other techniques were more relevant to proactive human intervention: monitoring agent thinking process while waiting (P4, P5, P6, P10), manually decomposing complex tasks into concrete implementation steps for the agent (P4, P7, P10), revising code to implement good coding practices (e.g., readability) as a demonstration for the agent (P2, P6), and overriding agent behavior with human expertise (P1, P2).

Notably, five Observations participants felt more willing to test their code systematically while using agents (P1, P4, P6, P12, P13).

**Managing Multiple Agents through Traditional Version Control.** Some experienced developers (4x Observations, 31x Survey) used multiple agents to create software, though still configured manually (6x Survey), to parallelize different implementation tasks (3x Observations, 17x Survey) and complement the abilities among agents (1x Observations, 10x Survey). They used traditional version control (e.g., git) to compare and merge work from different agents.

**Controlling Agent through Software Engineering Expertise.** Participants cited their existing software development expertise as a critical strategy for effectively using agents when creating software (11x Observations, 65x Survey). Working with agents required not only awareness of their capabilities (P1, P5) but also code comprehension and debugging skills (P2, P3, P6, P7, P12, P10) and clarity in translating product specs to code (P1, P2, P4, P8, P10, P13). Survey participants agreed upon the importance of *"first understanding coding and then using AI"* (S2), e.g., *"my observation so far is spending time to understand code already generated helps massively"* (S59).

> **Takeaway 2:** When working with agents, experienced developers *control* the software design and implementation by prompting and planning with *clear context and explicit instructions*, and letting agents work on only a few tasks at a time. Outside of prompting, experienced developers leverage established software development best practices, such as validation and version control, as well as their engineering expertise to incorporate agentic changes with supervision.

### 3.3 RQ3: Agentic Task Suitability

> *There's almost nothing I won't use these for. Even for one line items I feel confident in implementing myself, I like walking through it with the agent. It's a second set of eyes on the work I'm doing.*
> — S8

On average, Survey respondents rated the agents' suitability for their tasks as 4.73/6 (1="Extremely unsuitable", 6="Extremely suitable").

**Agents Accelerate Straightforward, Repetitive, Scaffolding Tasks.** A large number of survey respondents reported they found agents helpful for accelerating productivity (35:2), with many reporting they preferred using agents on all or most all tasks (20:0). Respondents found agents suitable for: small/simple/straightforward tasks (33:1), tedious/repetitive tasks (26:0), scaffolding or boilerplate (25:0), writing tests (19:2), refactoring (general) or code improvement (14:0), writing/updating documentation (20:0), debugging (simple) or simple fixes (12:3).

**Suitable for Following Well-Defined Plans.** A key feature of instruction-following coding agents is the ability to follow multi-step instructions. A large number of respondents reported agents were successful at following well-defined plans (28:2), e.g. *"Once the plan exists, the agent can work really cool and I'm just wondering how he does such great things!"* (S16).

Conversely, *"if you don't lead [or] plan then you will [get] stuck"* (S89): several respondents mentioned agents performed poorly with vague/unclear/open-ended tasks (0:7), and a few mentioned trouble with long context sessions or between-task consistency (4:8).

**Suitable for General SWE Tasks: Writing Tests, General Refactoring, Documentation, Simple Debugging.** Agents were viewed as suitable for writing tests (19:2), refactoring (simple) or modifying code or cleanup (14:0), refactoring (general) or code improvement (18:3), writing/updating documentation (20:0), and debugging (simple) or simple fixes (12:3).

Nevertheless, beyond simple debugging or general refactoring, opinions were more mixed. Debugging (general) (12:8) was controversial.

**Suitable for Backend and Some Frontend Work.** Both backend and frontend developers reported agents suitable for their work (14:1 and 10:3 respectively). Within frontend work, specific mentions of UI/HTML/CSS (9:4) were positive but not universally so.

**Suitable for Prototyping and Experimenting.** Prototyping was a common theme, with respondents finding agents suitable for prototyping or small projects (12:0), and exploring alternatives or experimenting (7:0).

**Controversial for Plan Development.** The most interesting debate is whether or not agents are suitable for creating high level plans (e.g. project or architecture design) (13:23). A majority of respondents mentioning high level planning were negative, sometimes out of concerns that agents are unsuitable for business logic or tasks requiring domain knowledge (2:15) and cannot replace human expertise or decision making (0:12). Developers also reported mixed experience with agents' ability to understand project architecture (6:7). S68 will not use agents for *"system design! I never trust LLMs for systematic issues"* and S25 said *"with architecture in general I use AI much less, other than being helpful for research"*.

Although no respondent suggested agents could replace human judgment, some still used agents for high level plans (13:23), perhaps in part because developers can get assistance from agents short of full delegation: agents can assist with brainstorming or conceptualization (11:5) or collaboratively talking out problems (6:0), *"it's like full time rubber ducking"* (S7).

**Unsuitable for Business Logic, Tasks Requiring Domain Knowledge, and Human Decision Making.** A notable number of developers reported agents are unsuitable for business logic or tasks requiring domain knowledge (2:15). S78 avoided agents for *"heavily logical or business rules parts"* and S95 avoided them for *"very specific business logic that requires a lot of context"*. This avoidance is related to the unsuitability of agents for replacing human expertise or decision making (0:12): 12 respondents mentioned the need for a human in the loop or the value of human expertise.

**Unsuitable for Perfect Code Generation.** Human oversight is still needed because generated code required revision, verification, or cleanup. *"Almost everything it performs great on. It just does not one shot things"* (S49). An oft-mentioned problem was integrating with existing code or handling legacy code (3:17). In Observations, 8 participants said agents could sometimes do more than asked, explaining that agents can create unnecessary files, rewrite entire sections of code, or install packages that are not needed for the task at hand.

**Unsuitable for Complex Tasks.** In contrast to suitability for small/simple/straightforward tasks (33:1), agents become less suitable as task complexity increases. Respondents reported agents were less appropriate for complex tasks (not necessarily big) (3:16), specifically for complex logic (0:6) and for refactoring (complex) or improving architecture (1:4). S16 found *"if the task is complex, like splitting lots of changes in a work directory to a bunch of smaller commits, it can [get] stuck and do bad things"*.

**Misc Unsuitable: Performance-Critical, Deployment, High-Stakes, and Security-Critical Situations.** Some task types were categorically unsuitable: writing performant code (3:9), handling CI/deployment infrastructure (3:8), high-stakes or privacy-sensitive tasks (0:8), and security-critical code (2:5).

> **Takeaway 3a:** Experienced developers find agents *suitable* for accelerating straightforward, repetitive, and scaffolding tasks if prompted with well-defined plans. Beyond writing new code and prototyping, these suitable tasks include writing tests, documentation, general refactoring and simple debugging.

> **Takeaway 3b:** But, as task complexity increases, agent suitability decreases. Experienced developers find agents *unsuitable* for tasks requiring domain knowledge such as business logic, and *no* respondent said agents could replace human decision making, in part because the generated code is not perfect on the first shot.

> **Takeaway 3c:** Experienced developers *disagree* about using agents for software planning and design. Some avoided agents out of concern over the importance of design, while others embraced back-and-forth design with an AI.

### 3.4 RQ4: Sentiments Towards Agents

> *It felt like driving a F1 car. While it also felt like getting stuck in traffic jam a lot, I still felt optimistic about it.*
> — S24

On average, Survey participants rated their enjoyment of developing software with agents as 5.11/6 (1="Extremely displeased", 6="Extremely pleased") as compared to without agents.

**Happiness and Curiosity.** Observational participants explicitly felt positively after working with agents (P3, P7, P8), pointing out that its success in completing a task made them happy with the outcome and the time they saved. P7 explained: *"If it's [...] a simple enough task, [...] it most likely will get correct and then I will have something neat and cool that I can just use directly. And [...] I feel good."* S8 wrote, *"This has made code fun again. I'm producing things that I didn't have time or energy to do before. It's like rediscovering computers again for the first time."*

**Need for Humans to Stay in the Loop.** While there are positive sentiments towards coding agents, experienced developers prefer to *control* agent behavior in building software (5x Observations). P2 was concerned about whether *"we're at the point where [...] I can hand off the responsibility of software engineering [...] to an AI [...] as a software engineer."* Experienced developers (6x Observations) discussed the necessity of human understanding of a code base for production, especially when reviewing agent-generated code. P4 noted: *"[agents] can also be used as a crutch to [...] have people who don't know what they're doing generate something that seemingly works, but it is kind of a nightmare to maintain anything."* Ultimately: *"you still do have to like think about it yourself [...] and evaluate of what the LLM is telling us is a good approach."* (P8)

**Trust in Agent's Capabilities.** Some experienced developers do trust the agent's output, but only after checking the code in some capacity (5x Observations), and will correct it or even manually code something if there has been a dip in quality (3x Survey). Those building software outside of their domain expertise (P1, P4, P5, P12) acknowledged agents' abilities in generating more usable code than themselves, but only leveraging such benefits to create what they want more effectively.

**Agents for Collaboration.** Some experienced developers view the agent as a means of elucidating thought processes for the software they are building (4x Observations, 12x Survey). P12 mentioned using agents as a *"rubber ducky"*, a common expression in software engineering where the developer explains their thought processes in natural language to figure out next steps. More broadly, agents are collaborators for brainstorming and more abstract tasks, where users are not only writing code with the agent but also thinking about the big picture (5x Observations, 34x Survey). Notably, experienced developers preferred staying in control even in these use cases, with S83 summarizing: *"I do everything with assistance but never let the agent be completely autonomous — I am always reading the output and steering."*

**Agentic Coding as the Future.** Experienced developers felt that AI-assisted coding workflows are only going to become more ubiquitous in future software development (4x Observations, 13x Survey). Some developers found it difficult to return to the pre-agent era: *"I don't want to go back to writing code manually. Now it seems like such a waste"* (S35). S13 urged: *"get into agentic AI as soon as possible otherwise you will be fall behind soon."*

> **Takeaway 4:** Experienced developers enjoy working *with* agents as source of collaboration, rather than delegating work to the agents completely.

---

## 4 Results Summary

Our study shows that **experienced developers generally enjoy working with agents** in developing software by **controlling** agent behavior through strategic plans and supervision, rather than *vibing* with agents. Specifically:

**RQ1 - Motivations.** Experienced developers appreciate the boost in development speed that agents could bring, while still valuing fundamental software quality attributes.

**RQ2 - Strategies.** With these values, experienced developers control both the software design and implementation when using agents, leveraging pre-existing knowledge about software development, prompting strategies, and established techniques for quality assurance (e.g., validation and version control), while letting agents work on only a few tasks at a time.

**RQ3 - Suitability.** Through employing these strategies, experienced developers identify that agents may be best for accelerating straightforward, repetitive, and scaffolding tasks, including e.g. writing tests, documentation, general refactoring and simple debugging. But as task complexity increases, agent suitability decreases. Experienced developers avoid agents for business logic and do not yet find agents suitable for completely autonomous operation. Opinions about using agents for high level planning are mixed.

**RQ4 - Sentiments.** Combining their expertise with software and understanding of agent capabilities, experienced developers generally enjoy working with agents, perceiving agentic tools as valuable source of collaboration in software development — rather than replacement of humans — that requires wise decision making and supervision from the human.

---

## 5 Discussion

### 5.1 Why Don't Pros Vibe?

> *I like coding alongside agents. Not vibe coding. But working \*\*with\*\*.*
> — S96

We found that experienced developers strategically *control* agent behavior in software development, rather than *vibing*. We can think of four possible reasons: (1) experienced developers value software engineering principles, which they have received from education and enforced every day at work; (2) experienced developers often work on production software, rather than "throwaway weekend projects", that leads to impact on real users and/or involves other stakeholders; (3) when working with familiar code bases or tech stacks, especially with pre-defined design requirements, there is little room for exploratory coding; (4) for unfamiliar tasks, when agentic solutions go wrong, developers found it frustrating that *"it [could take] a lot of time to resolve them"* (S13). These results imply that expertise — when available — supersedes vibes and drives the development of quality software.

### 5.2 Considering One's Own Agent Use

> *I never again want to give two [poops] about the specific best way to quijibo the toaster in dingledangle framework v0.21. The agent reads the latest docs and then is forced to comply.*
> — S88

Our findings suggest a few basic recommendations for improving one's own control of agents:

A first recommendation is to practice prompting clearly, specifically, and in detail. Prompts can potentially be long and include many steps, but vague prompts will not work. A second recommendation is to not expect to be able to vibe, because current agents cannot *autonomously* manage the development of large software. Human expertise remains essential: apply the lens of software engineering to ensure code quality and project structure.

Beyond these high level recommendations, another potential use of this paper may be to compare the tasks in Table 4 with one's own practice, considering which tasks one might try using agents for.

Many of our study participants reported that agents are skilled at following well-defined plans. In Observations, P1 and P2 had plans with 70 and 71 steps respectively, but despite occasionally long plans, participants ensured that agents implemented plans piece-wise in chunks of manageable size. Drafting longer plans, perhaps in a file, is another strategy to try.

Note that, psychologically, trying AI and then failing hurts trust in AI more than success builds trust. In other words, if the readers try agents for a new task where it does not work right away, it may be advisable to expect that initial discouragement and keep iterating.

### 5.3 Future Work

> *This is the future of development, and it's very fun.*
> — S25

We see two broad directions for future work: improvements to the interfaces for agentic coding, and further detailed studies of developer use of agents to derive best practices.

**Better Interfaces for Controlling Agents.** Our investigation revealed some areas where agents still struggle:
1. Automated testing, particularly testing in a remote or realistic environment, is difficult.
2. UI debugging through prompting is tedious.
3. It is difficult to understand why an agent fails or hangs.

Because this investigation shows that experienced developers plan in order to better control agent output, there is an opportunity to improve interfaces for the planning step.

**Developing Best Practices.** To our knowledge, there is not yet any rigorously developed set of best practices for using coding agents. Although this study produced an initial account of agent use by experienced developers, these usage patterns may not necessarily be optimal. As noted, Becker et al. observed a 19% performance drop when AI use was allowed for coding. Nonetheless, it is an open question whether those developers, or the participants in our study, have discovered how to use agents to their full potential.

To rigorously develop best practices for using agents, future work might focus more narrowly on developers who are most successful with AI agents. Ultimately, further research is needed to confirm the most productive agentic usage patterns and relevant scenarios, and to verify that coding agents are measurably helpful for productivity.

---

## 6 Related Work

### 6.1 Agents for Coding

With the rapid improvement in transformer-based LLMs and the large amount of open-source software publicly available for training, LLMs were soon applied to programming, initially as a super-charged autocomplete with Github Copilot in 2021 powered by OpenAI's Codex model, and later as a conversational partner with the advent of instruction-following LLMs. It is hard to overstate how earth-shattering the public launch of ChatGPT was in 2022.

LLMs improved steadily, with LLMs gaining the ability to think aloud and autonomously plan and enact multi-step workflows. LM coding ability reached a milestone with the announcement of Devin in 2024, which claimed to be "the first AI software engineer", followed soon thereafter in academia by SWE-agent targeting "end-to-end software engineering". Instead of a local autocomplete, these new systems were agentic: autonomously taking step-by-step actions to read, modify, and test whole codebases by iteratively invoking tools (e.g., search, read, edit, run) and fixing errors similar to a human's edit-run-debug cycle.

Besides broadly capable agents like Devin and SWE-agent, other AI agents have been developed for perhaps every conceivable part of software development, including requirements engineering, debugging, and testing. But currently, the widely deployed systems in practical use (Cursor, Github Copilot Agent, Claude Code, Codex CLI) present a broadly capable model by default. Although the model of a broadly capable autonomous agent is widespread and was the first paradigm to make significant progress on the SWE-bench, autonomous choices may not be necessary for such benchmark coding tasks: a carefully crafted pipeline of fixed steps can perform competitively with state of the art. This counter-result, which is effectively a case of extreme prompt engineering, highlights that prompting strategy matters *a lot* for success with current LLMs.

### 6.2 Coding GenAI Usability

**Prompt Quality.** In the studies of generative AI use for coding, the correlation between prompt quality and success is a repeated theme in both the autocomplete and the agentic eras. The most common prompting strategy is providing "clear explanations". Survey participants in our study highlighted that prompts should include clear context and explicit instructions (12x Observations, 43x Survey). Prompt quality is a key bottleneck in LLM usability.

**AI Utility.** At an even broader view, there is the question of whether LLMs are measurably helpful to programmers, as the extra burdens of prompting and code review may overwhelm any gains. From the autocomplete era, controlled lab studies showed positive results, though others found no measurable gain. In the agentic era, developers believe agentic AI is helpful: of those using AI agents 69% believe agents have increased their productivity. But, quantitative support for gains is currently lacking. Becker et al. studied 16 experienced open source maintainers, allowing them to use or not use AI tools as they performed their usual work (condition randomized per-task, n=246 tasks). While these developers estimated that AI access made them 20% faster, on the whole they were in fact 19% slower when they could use AI. The non-helpfulness may be because this setup was a worst-case scenario for AI: large, complex repositories where developers are intimately familiar with the code and have tacit knowledge unavailable to the AI, while the developers are also over-optimistic about AI utility.

### 6.3 Empirical Studies of Vibe Coding

With the skill of LLMs increasing to the point that AI agents can produce and modify full codebases, it is now becoming possible to, perhaps, disengage with the code entirely and only write prompts. Karpathy dubbed this approach "vibe coding", where *"you fully give in to the vibes, embrace exponentials, and forget that the code even exists...it's not really coding - I just see stuff, say stuff, run stuff"*.

Pimenova et al. investigated social media posts and interviewed several people who had tried vibe coding in order to better define and characterize the phenomena. The key feature seems to be aiming for "flow and joy" in the development experience by trusting the AI. This mindset leads vibe coders to avoid manual review because it is annoying and kills the vibes. Fawzy et al. worry that non-programmers become "vulnerable developers" if they try to vibe code software for a setting in which they do not have the expertise to manage the real-world responsibilities of their potentially incorrect code.

The necessity of expertise is supported by Sarkar and Drosos's analysis of online livestreams of vibe coders (n=4, 8.5 hours): all four developers studied performed some amount of code review, but relied on their programming expertise to skim the code quickly rather than scrutinizing line-by-line. They also relied on their expertise to choose when to switch to manual coding. Overall, Sarkar and Drosos believe "vibe coding still requires significant human expertise...especially when the vibes are off". Chandrasekaran tried re-creating the same app using three different prompting styles; their best results were by following a less vibey, more disciplined approach, leading them to hypothesize that "production-grade quality requires deliberate oversight".

Our study did not set out to study vibe coding in particular, but the experienced developers we observed did not vibe. When implementing new features, while they might ask the AI for a first-draft plan, they always planned. And they were careful about the code produced: 69% (9/13) carefully reviewed every change.

With the continuing improvement of LLMs, vibe coding may be the future, even by non-programmers. But, for complex software, it is not the present.

---

## 7 Conclusion

> *I think AI agents are amazing as long as you are the driver & reviewing its work. AI agents become problematic once you're not making them adhere to engineering principles that have been established for decades.*
> — S64

To gain insight into the current practice of agentic coding by experts, we studied experienced developers (3+ years of professional experience) through 13 field observations supplemented with a broader survey of 99 respondents. We aimed to learn about their values and motivations for using agents, workflow strategies, what agents are suitable for, and developer sentiments about using coding agents. We find that experienced developers do not currently vibe code. Instead, they carefully *control* the agents through planning and active supervision because they care about software quality. Although they may not always read code to validate agentic output, they are careful not to lose control and do not let agents run completely autonomously, particularly having the agents only work on a few tasks at a time. They generally enjoy using agents, finding them suitable for accelerating straightforward, repetitive, and scaffolding tasks, including a large variety of software engineering tasks like writing tests, documentation, refactoring, and simple debugging; and yet opinions are mixed about writing plans with agents, and they do not use agents for core business logic or complex tasks. AI capabilities and interfaces are changing fast: this work paints a picture of what is and is not working now, serving as a reference point both to calibrate expectations about current AI as well as to anchor comparison in future years to see how much AI has improved since 2025. As of now, the AIs are not taking over yet — experienced developers are still in control.

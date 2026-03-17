---
description: Closed-loop control plane for iterative agent improvement via multi-role orchestration (competitor/analyst/coach/architect), tournament evaluation, and accumulated playbook context — strongest reference for automated iterative learning loops, but the "context compilation" is concatenation with budget-aware trimming, not transformation
type: note
tags: [related-systems]
status: current
last-checked: 2026-03-17
---

# Autocontext

A closed-loop control plane for iteratively improving agent behavior over repeated runs. Autocontext orchestrates multiple agent roles (competitor, analyst, coach, architect) through generation loops: run a scenario, evaluate outcomes, accumulate knowledge in playbooks and lessons, inject that knowledge into the next generation's prompts. The system targets a trajectory from expensive frontier-model exploration to validated, cheaper execution — including MLX-based local model distillation on Apple Silicon. Built by Greyhaven AI, MIT-licensed. Dual implementation: Python (full control plane with CLI, API server, dashboard, training loop) and TypeScript (lightweight toolkit focused on judge-based evaluation and improvement loops).

**Repository:** https://github.com/greyhaven-ai/autocontext

## Core Ideas

**Multi-role orchestration with dependency-aware execution.** Each generation orchestrates four agent roles: a *competitor* produces a strategy (JSON or code), an *analyst* examines failures and produces findings, a *coach* updates the accumulated playbook with lessons and hints, and an *architect* (on a cadence) proposes and generates tooling improvements. Analyst and coach run in parallel after the competitor; the architect runs every N generations. The orchestration is a fixed DAG, not a dynamic workflow — roles are hardcoded, dependencies are static, and the execution order never varies. This is a genuine design choice: predictability over flexibility.

**Accumulated playbook as persistent context.** The playbook (`knowledge/<scenario>/playbook.md`) is the central knowledge artifact. The coach reads tournament results, analyst findings, and the current playbook, then produces an updated version. Playbooks are versioned (up to 5 archived versions) with rollback support. Alongside the playbook, the system accumulates operational lessons (structured prescriptive rules), coach hints (specific parameter suggestions), dead ends (known failed approaches), and generated tools (Python functions). This accumulated context is injected into every subsequent generation's prompts.

**Tournament and judge evaluation.** Two evaluation paths. *Game scenarios* use tournament matches with Elo ranking — the competitor's strategy is executed N times against opponents, producing scores that feed the backpressure gate. *Agent task scenarios* use an LLM judge with a rubric, supporting multi-round improvement loops (evaluate, revise, re-evaluate until threshold or max rounds). The evaluation mode is determined by scenario family, not configured per-run. The system also supports simulation traces, artifact validation, and several other evaluation modes through a scenario family registry.

**Backpressure gate controls loop progression.** After each generation, a gate decides `advance` (move to next generation), `retry` (repeat with same context), or `rollback` (revert to previous playbook version). The decision is based on score delta (improvement over previous generation) and retry count. This is a genuine control mechanism — it prevents the loop from progressing when performance degrades, and the rollback mechanism restores known-good playbook state.

**Context budgeting with progressive trimming.** The prompt assembly (`build_prompt_bundle()`) gathers 20+ context components and estimates token count using a char/4 heuristic (~25K token budget). When the budget is exceeded, a trimming cascade removes components in priority order: session reports first, then notebooks, experiment log, trajectory, analysis, tools, lessons, playbook. Hints and dead ends are never trimmed — they're considered the most actionable context. The cascade is hardcoded, not configurable.

**Scenario families as type-driven routing.** Scenarios are classified into families (game, agent task, simulation, artifact editing, coordination, negotiation, investigation, etc.), each with an explicit interface class (ABC defining `execute_match`, `get_observation`, `validate_actions`), evaluation mode, and output format. This is genuine type routing — the scenario family determines which evaluation path runs, what output format the competitor produces, and which orchestration variant applies.

**Local model distillation via MLX.** The system can export training data from successful runs (strategies, scores, context) as JSONL and fine-tune local models using MLX on Apple Silicon. The goal is to capture successful strategies in a cheaper model that can replace frontier-model competitors for known scenario types. A model registry tracks trained models with scenario associations.

**Dual-language implementation sharing a schema.** The Python package is the full control plane; the TypeScript package is a lighter toolkit sharing the same SQLite schema and migrations. Both can read/write the same database, enabling cross-language workflows (e.g., Python for training, TypeScript for MCP-served evaluation in Node.js environments).

## Comparison with Our System

Autocontext and commonplace address different phases of the knowledge lifecycle. Autocontext automates the *generation and evaluation* of behavioral knowledge (strategies, playbooks) through iterative loops. Commonplace structures the *accumulation and maturation* of design knowledge through human+agent curation. The overlap is in how both systems engineer context for agents operating under bounded windows.

| Dimension | Autocontext | Commonplace |
|---|---|---|
| Primary concern | Iterative behavioral improvement (make the agent perform better at tasks) | Knowledge accumulation and maturation (make the agent know the right things) |
| Knowledge unit | Playbook (markdown), lessons (structured rules), tools (Python functions) | Typed note with frontmatter, prose body, and semantic links |
| Learning mechanism | Automated loop: compete → evaluate → analyse → coach → accumulate | Human+agent: write → connect → validate → mature through status transitions |
| Context delivery | Prompt concatenation with budget-aware trimming | Progressive disclosure: descriptions at startup, full content on demand |
| Evaluation | Tournament Elo, LLM judge with rubrics, external command execution | Advisory validation (`/validate`), human judgment |
| Knowledge lifecycle | Playbook versioning with rollback; lessons accumulate indefinitely | Status transitions (seedling → current → superseded), type transitions |
| Link structure | None — artifacts reference each other implicitly through prompt injection | Explicit semantic links (extends, grounds, contradicts) with articulated relationships |
| Storage | SQLite + filesystem artifacts | Markdown files in git |
| Agency model | Fully automated (agents orchestrate agents) | Human+agent collaborative |
| Scope | Task-specific (one scenario at a time) | Cross-domain (knowledge base spanning many topics) |

**Where autocontext is stronger.** The automated improvement loop is the core contribution — no reviewed system iterates on agent behavior this systematically. The backpressure gate with rollback is a genuine control mechanism that prevents degradation. Tournament evaluation with Elo ranking provides a quantitative performance signal that our advisory validation cannot match. The multi-role decomposition (separate agents for strategy, analysis, coaching, tooling) is a principled way to avoid the single-agent-does-everything failure mode. The local model distillation pipeline, if it works at scale, addresses [the cost dimension of context efficiency](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) by replacing expensive inference with fine-tuned cheap models.

**Where commonplace is stronger.** Knowledge has structure beyond accumulation. Our notes carry semantic links that articulate *why* things relate, descriptions that serve as retrieval filters for progressive disclosure, and status transitions that track maturation. Autocontext's playbook is a single evolving document — there is no mechanism for recognising that two lessons contradict, that a strategy insight generalises beyond its scenario, or that accumulated knowledge should be decomposed into composable pieces. The [title-as-claim](../title-as-claim-enables-traversal-as-reasoning.md) convention, which makes traversal itself a reasoning operation, has no analogue in autocontext's flat knowledge artifacts. Most critically: autocontext's knowledge is scenario-scoped (each scenario has its own isolated playbook/lessons/tools), while commonplace's knowledge is cross-domain and compositional — insights from one area inform work in another through the link graph.

**The deepest divergence** is what learning means. Autocontext treats learning as performance improvement on a measurable task — the score goes up, therefore the system learned. Commonplace treats learning as capacity change (per [Simon's definition](../learning-is-not-only-about-generality.md)) — the knowledge base becomes more capable of supporting good decisions across contexts, whether or not there's a numeric score to prove it. Autocontext's learning is verifiable but narrow (works within a scenario); commonplace's learning is broad but harder to verify (works across domains, but how do you measure "contextual competence"?). This maps directly onto the [constraining-and-distillation trade-off](../constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md): autocontext constrains aggressively (scenario-specific optimization), while commonplace distils broadly (cross-domain knowledge compression).

## Borrowable Ideas

**Backpressure gate with rollback.** The advance/retry/rollback mechanism based on score delta is a clean pattern for any iterative process. For commonplace, this could inform how automated maintenance operations work: if a batch edit (link repair, index rebuild) degrades validation scores, roll back rather than commit. The pattern is: measure before, measure after, gate on delta. *Needs a use case first — we don't have automated batch operations that could degrade.*

**Explicit dead-end tracking.** Autocontext maintains a list of known failed approaches that are never trimmed from context, ensuring agents don't repeat mistakes. For commonplace, a `dead-ends.md` or a `status: dead-end` convention could serve the same purpose — marking approaches that were tried and abandoned, with reasons. This is cheaper than hoping the agent will find the relevant note explaining why something doesn't work. *Ready to borrow — low cost, prevents repeated exploration of known failures.*

**Role decomposition for complex operations.** Splitting a complex task into analyst/coach/architect roles with explicit dependencies is more principled than asking one agent to do everything. For commonplace, operations like `/ingest` (which currently does snapshot + classify + analyse + connect in one pass) could decompose into separate roles with explicit handoffs. *Needs a use case first — current single-agent operations work well enough at our scale.*

**Score trajectory as context.** Injecting a formatted history of past performance (generation, score, gate decision) into prompts gives the agent a quantitative sense of progress. For commonplace, injecting a "recent changes" summary (what was added, what was connected, what validation issues were found) into agent context could serve the same navigational function. *Just a reference — our progressive disclosure already provides navigational context.*

## Curiosity Pass

### Broad pass

**The "compilation" claim is the most interesting gap.** The README and naming ("autocontext" — automatically engineering context) suggest sophisticated context transformation. The actual mechanism is: read artifacts from disk, format them as markdown strings, concatenate them into a prompt, trim if over budget. This is context *assembly*, not context *compilation*. A compiler transforms representation (source → IR → target); autocontext preserves representation (markdown → prompt-embedded markdown). The budget-aware trimming is the only operation that changes the information content, and it's lossy removal, not transformation. The char/4 token estimation is a rough heuristic that likely over- or under-estimates significantly for mixed content.

**The playbook is the single point of knowledge accumulation.** All learning flows through one artifact — the coach reads everything and updates the playbook. If the coach misses an insight, it's lost. If the coach introduces a bad recommendation, it persists until scores drop enough to trigger rollback. There's no independent verification of playbook quality — no second reader, no structural validation, no check that lessons are consistent with each other. The curator role (optional, quality-gates playbook updates) partially addresses this, but it's another LLM reading markdown and producing markdown. The system's ceiling is the coach's judgment quality.

**Cross-scenario learning is absent.** Each scenario has an isolated knowledge directory. Lessons learned in one scenario never inform another. If two scenarios share a structural similarity (both reward cautious early moves, both penalise over-aggressive parameters), the system cannot discover or exploit this. Compare with commonplace where cross-domain connections are the primary value proposition.

### Systematic pass: each Core Idea

**Multi-role orchestration with dependency-aware execution.**
1. *Property claimed:* Better outcomes through specialized roles (analysis, coaching, tooling) operating on shared state.
2. *Transform or relocate?* Each role genuinely transforms — the analyst extracts patterns from match data, the coach synthesises guidance from analysis + trajectory, the architect generates code from capability gaps. These are real LLM-mediated transformations. However, the orchestration itself is a fixed DAG with hardcoded roles, not a dynamic routing decision.
3. *Simpler alternative:* A single agent that reviews its own past performance and updates its own strategy achieves the same loop with fewer API calls. The multi-role decomposition adds value if the roles genuinely produce different insights (specialization), but the system provides no evidence that four specialised prompts outperform one comprehensive prompt with the same context.
4. *Ceiling:* Even working perfectly, the orchestration can only improve within the space of strategies the competitor can generate and the evaluation can measure. If the scenario's optimal strategy is outside the model's generation distribution, more orchestration doesn't help.

**Accumulated playbook as persistent context.**
1. *Property claimed:* Continuity — each generation builds on all prior learnings.
2. *Transform or relocate?* The coach genuinely transforms: it reads tournament results + analysis + current playbook and produces an updated playbook. This is LLM-mediated synthesis, not concatenation. But the *injection* of the playbook into the next generation's prompt is pure relocation — the markdown is read from disk and placed into the prompt verbatim.
3. *Simpler alternative:* Appending "last generation's score was X, the strategy was Y, the main failure was Z" to the prompt achieves continuity without a playbook abstraction. The playbook adds value by compressing multiple generations' learnings into a coherent document rather than a growing transcript. This compression is the mechanism's genuine contribution — it's [distillation](../distillation.md) performed by the coach LLM.
4. *Ceiling:* The playbook can accumulate and compress strategy knowledge, but it cannot discover that the evaluation metric is wrong, that the scenario definition is flawed, or that the task needs reframing. The ceiling is "optimal performance within the defined evaluation."

**Tournament and judge evaluation.**
1. *Property claimed:* Rigorous, repeatable evaluation of strategy quality.
2. *Transform or relocate?* Tournament evaluation genuinely transforms — it executes strategies and produces scores from outcomes. LLM judge evaluation is softer — it's an LLM reading output and producing a number, which is [oracle-strength-dependent](../oracle-strength-spectrum.md).
3. *Simpler alternative:* For game scenarios, the tournament is the natural evaluation mechanism — no simpler alternative exists. For agent tasks, the LLM judge could be replaced by deterministic tests where available (and would be more reliable).
4. *Ceiling:* Tournament evaluation is as strong as the game implementation. LLM judge evaluation is as strong as the judge's ability to assess quality — which for complex tasks is an [open problem](../the-boundary-of-automation-is-the-boundary-of-verification.md).

**Context budgeting with progressive trimming.**
1. *Property claimed:* Efficient use of bounded context windows.
2. *Transform or relocate?* Relocate with lossy removal. Components are read from disk and concatenated; when the budget is exceeded, lower-priority components are dropped entirely. No component is compressed, summarised, or restructured to fit — it's either included in full or excluded entirely.
3. *Simpler alternative:* A maximum prompt length with "include these components in this order, stop when full" achieves identical behavior. The named priority cascade adds readability but the mechanism is the same.
4. *Ceiling:* Budget-aware trimming ensures the prompt fits the window. It cannot ensure the prompt contains the *right* information for *this specific* generation — the priority order is global, not task-adaptive. A generation struggling with tool usage will still trim tools before lessons, even if tools are what's needed. Our [progressive disclosure](../agents-navigate-by-deciding-what-to-read-next.md) approach lets the agent decide what to load, which is task-adaptive but requires the agent to know what it needs.

**Scenario families as type-driven routing.**
1. *Property claimed:* Clean separation of evaluation and execution concerns by scenario type.
2. *Transform or relocate?* This is genuine type routing — the scenario family determines which code paths execute. Each family has an ABC with different method signatures, so the routing produces structurally different execution flows.
3. *Simpler alternative:* A switch statement on scenario type achieves the same dispatch. The ABC hierarchy adds interface contracts (each family must implement specific methods) which is valuable engineering but not conceptually novel.
4. *Ceiling:* Type routing correctly dispatches known scenario types. It cannot handle scenarios that don't fit existing families — those require new interface implementations.

**Local model distillation via MLX.**
1. *Property claimed:* Cost reduction by capturing successful strategies in cheaper models.
2. *Transform or relocate?* This is genuine transformation — training data (strategies + context + scores) is used to fine-tune model weights. The output model is structurally different from the input data.
3. *Simpler alternative:* Prompt engineering with accumulated context (which autocontext already does) achieves behavior adaptation without training. The training path adds value when context alone is insufficient or when inference cost savings justify training cost.
4. *Ceiling:* Local model distillation can capture patterns present in the training data. It cannot exceed the frontier model's capability on novel scenarios. The training pipeline's practical ceiling is whether enough high-quality training data accumulates from runs to produce a meaningfully better-than-random local model.

### Findings that update Core Ideas and Comparison

The curiosity pass reveals that autocontext's genuine contributions are: (1) the coach's LLM-mediated synthesis of playbook updates (real distillation), (2) the backpressure gate with rollback (real control), (3) tournament evaluation for game scenarios (hard oracle), and (4) the local model training pipeline (real transformation). The "context compilation" framing overstates what is mechanistically concatenation with budget-aware trimming.

The system's most interesting limitation is the single-scenario knowledge silo. Each scenario accumulates knowledge independently, with no mechanism for cross-scenario transfer. This is the opposite bet from commonplace's cross-domain linking — autocontext sacrifices generality for depth within a scenario. Whether this is the right trade-off depends on whether scenario-specific optimization or cross-domain insight transfer produces more value. For game scenarios with clear metrics, scenario-specific depth wins. For open-ended knowledge work, cross-domain transfer wins.

The coach is the system's critical path — it's the only mechanism that synthesises knowledge across generations. If the coach produces poor playbook updates, the entire loop degrades. The curator role partially addresses this, but it's another LLM reading the same context. There's no structural check on playbook quality — no equivalent of our [validation](../deterministic-validation-should-be-a-script.md) or link articulation requirements. The system's learning reliability is entirely [oracle-dependent](../oracle-strength-spectrum.md) on the coach model's judgment.

## What to Watch

- Whether cross-scenario knowledge transfer emerges. The current architecture siloes knowledge per scenario; if the team adds cross-scenario lesson sharing, it would validate the cross-domain transfer hypothesis that commonplace is built on.
- Whether the MLX distillation pipeline produces practically useful local models. If scenario-specific fine-tuning reliably captures strategic knowledge in cheap models, it validates the [deploy-time learning](../deploy-time-learning-the-missing-middle.md) thesis through a different mechanism (weight modification rather than context engineering).
- Whether the system evolves toward richer knowledge structure (links between lessons, contradiction detection, lesson lifecycle) or stays with flat accumulation. The current design treats knowledge as an append-only byproduct of the loop; maturation would require the system to reason about its own knowledge.
- How the scenario family registry evolves — whether it converges on a few dominant families or proliferates specialized ones. This is a test of whether type-driven routing at the evaluation level produces genuine architectural clarity.

---

Relevant Notes:

- [context-efficiency-is-the-central-design-concern-in-agent-systems](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) — exemplifies: autocontext's budget-aware trimming and playbook compression are direct responses to context scarcity, choosing a fixed priority cascade over task-adaptive loading
- [distillation](../distillation.md) — exemplifies: the coach's playbook synthesis is automated distillation from tournament results + analysis into compressed strategic guidance; the MLX training pipeline is a second distillation layer (context → weights)
- [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](../constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — exemplifies: autocontext constrains aggressively per scenario (high reliability/speed within domain) while commonplace distils broadly (generality across domains), demonstrating the trade-off in practice
- [automating-kb-learning-is-an-open-problem](../automating-kb-learning-is-an-open-problem.md) — contrasts: autocontext automates learning within a measurable loop (tournament scores, LLM judges), but its knowledge has no maturation path — it accumulates without synthesis beyond what the coach produces, marking the same automation boundary from a different angle
- [the-boundary-of-automation-is-the-boundary-of-verification](../the-boundary-of-automation-is-the-boundary-of-verification.md) — exemplifies: the system works best where evaluation is cheapest (game tournaments with deterministic scoring) and degrades where verification is hard (LLM-judged open-ended tasks)
- [oracle-strength-spectrum](../oracle-strength-spectrum.md) — exemplifies: tournament Elo is a hard oracle, LLM judges are soft oracles, and the coach's playbook quality has no oracle at all — the system's reliability degrades along this spectrum
- [agents-navigate-by-deciding-what-to-read-next](../agents-navigate-by-deciding-what-to-read-next.md) — contrasts: autocontext injects all context at once (agent receives a pre-assembled prompt), while commonplace lets agents navigate incrementally — opposite context delivery models with different task-adaptivity properties
- [deploy-time-learning-the-missing-middle](../deploy-time-learning-the-missing-middle.md) — extends: autocontext's playbook accumulation and MLX distillation are both deploy-time learning mechanisms, the former through context engineering, the latter through weight modification
- [agentic-memory-systems-comparative-review](./agentic-memory-systems-comparative-review.md) — extends: autocontext adds a loop-first, performance-optimizing position not represented in existing entries — knowledge as a byproduct of iterative improvement rather than a primary concern
- [files-not-database](../files-not-database.md) — complicates: autocontext uses both — SQLite for structured operational data (runs, generations, scores) and filesystem for knowledge artifacts (playbooks, tools, lessons), suggesting the files-vs-database choice may be per-artifact-type rather than system-wide
- [codification](../codification.md) — exemplifies: the architect role generates Python tool functions from capability gaps, which is genuine codification (natural language description → executable code); the rest of the knowledge pipeline stays in natural language

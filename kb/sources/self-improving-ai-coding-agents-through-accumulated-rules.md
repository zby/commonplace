---
source: https://arxiv.org/html/2607.13091v1?utm_source=chatgpt.com
description: "Production case study of converting accepted code-review feedback into persistent, version-controlled behavioral rules shared across coding-agent interfaces."
captured: 2026-08-02
capture: web-fetch
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Self-Improving AI Coding Agents Through Accumulated Behavioral Rules: A Closed-Loop Framework

Author: Aditya Aggarwal; Nahid Farhady Ghalaty
Source: https://arxiv.org/html/2607.13091v1?utm_source=chatgpt.com
Date: July 13, 2026

## Abstract

LLM-based coding agents repeat the same classes of mistakes across sessions because they lack a mechanism to retain corrections from human review feedback. We present a closed-loop framework in which every accepted review comment is codified as a persistent behavioral rule, progressively expanding the set of error classes the agent can self-detect.

The framework combines an accumulating rule set in a version-controlled instruction file, a self-review checklist executed before code submission, and automated validation that ensures rule-set integrity as it grows. In deployment across a 35+ service microservices platform, the rule set grew from 5 to 18 behavioral rules, 15+ language-specific standards, and a 15-item self-review checklist, all derived from real review feedback.

We present empirical results from 11 recorded working sessions spanning code generation, PR review, incident investigation, and cross-service refactoring. We observe that accumulated rules shift review effort from low-level correctness toward design-level validation, achieve a measured 0% recurrence rate for ruled-against error classes, and transfer across heterogeneous agent interfaces.

We compare our approach against related work in experiential LLM learning (Reflexion, ExpeL, Voyager) and automated code review (CodeReviewer, SWE-bench agents), showing that our framework achieves persistent cross-session learning without weight updates, operates on production codebases rather than synthetic benchmarks, and addresses an orthogonal dimension (behavioral consistency over time) that existing benchmarks do not measure.

The result is a coding agent that improves with every review cycle, accumulating the engineering wisdom of its human collaborators without changing a single model weight.

## I Introduction

AI coding agents powered by Large Language Models have demonstrated remarkable capability in code generation, bug fixing, and code review [1, 2]. A persistent limitation, however, is their inability to learn from session to session. When a human reviewer catches an error in AI-generated code (say, disposing of a resource whose lifetime is managed by a framework-level factory), the agent will reproduce the same mistake in the next session because it has no mechanism to retain that correction.

Current approaches to improving LLM coding quality fall into three categories: (1) fine-tuning on curated code datasets, which is expensive and organization-specific; (2) retrieval-augmented generation (RAG), which surfaces relevant code context but does not encode behavioral constraints; and (3) prompt engineering with static instructions [7], which captures some conventions but does not evolve with experience.

None of these implements a feedback loop in which review outcomes automatically strengthen future agent behavior.

We propose a fourth approach, accumulated behavioral rules, built on one core insight:

> Every accepted review comment is a self-review rule. When a reviewer catches something the agent missed, codify the pattern so the agent catches it next time. The goal is zero avoidable review comments.

This paper describes the architecture of a system that implements this principle, reports on its deployment in a production environment with quantitative empirical results, and positions the contribution against the growing body of work on experiential learning for LLM agents [23].

We make the following contributions:

- C1: A closed-loop framework that converts accepted human review feedback into persistent behavioral rules, creating a ratchet effect where the set of prevented error classes grows monotonically over time.
- C2: An operational memory mechanism for coding agents implemented through version-controlled instruction files rather than weight updates, making it model-agnostic, tool-agnostic, and immediately deployable.
- C3: Empirical results from 11 recorded working sessions (code generation, PR review, cross-service refactoring, incident investigation) showing rule accumulation dynamics, error-class suppression rates, and knowledge transfer patterns.
- C4: A systematic comparison against related work in experiential LLM learning (Reflexion [13], ExpeL [14], Voyager [15]) and automated code review (CodeReviewer [4], SWE-agent [16]), identifying the orthogonal dimension (persistent behavioral consistency across sessions) that our framework addresses and existing benchmarks do not measure.

### I-A Scope and Positioning

To preempt a natural question, “Is this just disciplined prompt engineering?”, we clarify what the framework is and is not.

This framework is:

- A persistent organizational memory mechanism for coding-agent behavior, where memory content is derived exclusively from accepted review outcomes.
- A repeat-error prevention system that converts point corrections into class-level constraints.
- A shared, version-controlled knowledge artifact that is reusable across models, tools, and team members.

This framework is not:

- Weight updates, model retraining, or reinforcement learning from human feedback (RLHF) [6].
- A replacement for human review. It augments review by eliminating previously-seen error classes, freeing reviewers for higher-order concerns.
- A proof of semantic correctness; it prevents known failure modes, not all possible failures.
- A general-purpose memory system. It is scoped to coding-agent behavioral constraints within a defined codebase.

The distinction from static prompt engineering is the feedback loop. The instruction file is not written once and maintained passively. It grows as a direct function of review outcomes, with each new rule traceable to a specific accepted comment. This makes the system self-improving in a way that static instruction files are not.

## II Framework Architecture

The framework comprises several interconnected components. The closed-loop process is:

1. Agent generates/modifies code.
2. Agent runs self-review checklist.
3. Human reviewer provides feedback.
4. Accepted comments are codified as rules.
5. Updated instruction file is loaded in the next session, returning to step 1.

Figure 1: The closed-loop feedback cycle. Each accepted review comment is codified as a persistent behavioral rule in a version-controlled instruction file, expanding the agent’s self-review capability for all subsequent sessions.

### II-A The Structured Instruction File

At the center of the framework is a structured instruction file that LLM-based coding agents load as system context at the start of every session. Several emerging conventions exist for this mechanism (e.g., AGENTS.md, rules files, instruction files), all following the same principle: a version-controlled Markdown file that shapes agent behavior. The file is organized into five sections, though the specific section names and content are domain-dependent. For example, in our deployment:

1. Behavioral Rules: High-level operational guardrails (e.g., “Never commit without user approval”).
2. Code Standards: Language-specific rules derived from review feedback (e.g., “Never use string interpolation in log calls; use message templates”).
3. Self-Review Checklist: A numbered checklist that agents execute before approving any code.
4. Anti-Patterns: Specific patterns the agent is prohibited from generating, with explanations and correct alternatives.
5. Workflow Rules: Automatic triggers that tell agents when to invoke specific tools or sub-agents based on the task type.

The critical property is that the file is append-friendly and monotonically growing. Rules are added and occasionally refined but rarely removed, accumulating the team’s collective engineering judgment over time.

### II-B Rule Representation

While rules are stored as human-readable Markdown, each rule implicitly conforms to a structured schema:

```
Rule ID: R17
Category: Architecture
Trigger Origin: Human PR reviewer
Scope: New internal HttpClient registrations
Constraint: Add client to AllowIPV4Internal SSRF policy
Rationale: Prevent runtime SSRF policy validation failures
Checklist Map: Self-review item #9
Added: 2026-02-28
Traced To: PR review comment on missing SSRF allowlist entry
```

This schema serves three purposes: (1) it makes origin tracking concrete, linking each rule to the review event that produced it; (2) it maps rules to self-review checklist items, creating a verifiable bridge between the instruction file and the pre-submission check; and (3) it supports future tooling for conflict detection and rule effectiveness scoring.

### II-C The Feedback Loop

The self-improvement cycle operates in five steps:

1. The agent generates or modifies code in response to a task.
2. The agent executes its self-review checklist before presenting the code.
3. A human reviewer examines the code and provides feedback.
4. For each accepted comment that identifies a generalizable class of mistake (not a one-off typo), a new rule is added to the instruction file.
5. The updated instruction file is loaded in all subsequent sessions, preventing recurrence.

This creates a ratchet effect: the set of error classes the agent can self-detect grows monotonically. The instruction file serves as organizational memory that persists across sessions, models, and tool boundaries.

### II-D Rule Lifecycle and Governance

Because the rule set grows monotonically, governance is essential to maintain quality. We address four operational questions:

Who decides whether a comment represents a class of mistake versus a one-off issue? The engineer who receives the review feedback makes this judgment. The heuristic is: “Would this mistake plausibly recur in a different context?” If yes, it becomes a rule.

When is an existing rule refined instead of adding a new rule? When a new review comment reveals that an existing rule is too broad or too narrow, the existing rule is updated in place. The rule ID is preserved; the constraint text is sharpened. Section III-E describes a concrete example.

How are duplicate or overlapping rules handled? The instruction file is reviewed periodically for redundancies. When two rules cover overlapping ground, the more specific rule subsumes the general one.

Who owns arbitration when two rules conflict? The instruction file lives in a shared repository where changes require pull requests. Conflicting rules are resolved by the team through the normal review process.

### II-E Illustrative Rule Examples

To make the framework concrete, we present five representative rules from the deployed instruction file:

1. Resource lifetime management. A reviewer caught the agent wrapping a factory-created HttpClient in a using block. The rule states that HttpClient instances from IHttpClientFactory must not be disposed by the caller.
2. Structured logging. A reviewer flagged string interpolation in log calls. The rule requires message templates to preserve structured log properties.
3. Boolean logic correctness. The agent generated an incorrect guard clause using `!A || !B || !C` (always true by De Morgan’s law). The rule requires `!A && !B && !C` for conjunctive negation.
4. Null safety enforcement. A reviewer caught the null-forgiving `!` operator. The rule requires `?? throw new ArgumentException(...)` for explicit validation.
5. Security configuration. The agent registered a new internal HTTP client without adding it to the SSRF allowlist policy. The rule requires every new HttpClient registration include an SSRF policy entry.

### II-F Workspace Validation as Reliability Mechanism

As the rule set grows, it becomes a critical organizational artifact. A malformed rule addition could silently degrade the system. The framework includes automated validation that runs at session start:

- Agent definition files have valid frontmatter and required fields.
- Skill directories contain properly structured instruction files.
- Knowledge documents carry freshness dates, flagging stale content.
- The instruction file contains all required sections.
- Automation scripts exist and tool-server configurations are well-formed.

This validation supports the monotonic-growth principle: the rule set can grow safely because every addition is validated against a known-good schema.

### II-G Session Continuity

The framework maintains session continuity through two mechanisms: (1) a session handoff file capturing in-progress work, pending reviews, and suggested next actions; and (2) a task log providing a chronological record of completed work. Together, these ensure that accumulated knowledge includes not only behavioral rules but also ongoing work context.

## III Deployment Experience

### III-A Environment

The framework was deployed in a large-scale microservices platform comprising 35+ services on a managed container orchestration platform with service mesh. The codebase spans approximately 50,000+ lines of shared infrastructure code. LLM-based coding agents were used for code generation, review, architecture investigation, incident response, and cross-service refactoring across multiple agent interfaces, all reading the same instruction file.

### III-B Rule Accumulation Over Time

Over a multi-week deployment period, the rule set grew as shown in Table I.

| Component | Count |
|---|---:|
| Behavioral Rules | 18 |
| Code Standards (typed language) | 15+ |
| Self-Review Checklist Items | 15 |
| Anti-Pattern Rules | 6 |
| Custom Agent Definitions | 13 |
| Operational Skills | 10 |
| Knowledge Documents | 6 |

### III-C Knowledge Source Distribution

Analysis of the first 18 accumulated behavioral rules reveals four distinct sources of learning, as shown in Table II.

| Source | Count (%) | Description |
|---|---:|---|
| Human PR reviewers | 7 (39%) | Domain-specific |
| Automated review bots | 4 (22%) | Formatting, style |
| Self-discovered | 4 (22%) | Proactive analysis |
| Production errors | 3 (17%) | Runtime failures |

The dominance of human reviewer feedback (39%) validates the core premise: human review is the highest-quality signal for rule generation.

### III-D Observed Effects

Suppression of previously-seen error classes: Across 11 recorded working sessions following rule additions, we observed no recurrences of any ruled-against pattern within the observation window (see Section IV; this should be read as suppression under the observed deployment conditions rather than a permanent property of the underlying model).

Shift in review focus: Reviewers reported spending less time on mechanical issues and more on architectural appropriateness and design trade-offs.

Cross-interface transfer: Rules added through one agent interface immediately benefited sessions conducted through a different interface, because all interfaces consumed the same instruction file.

Onboarding acceleration: New team members inherited the full accumulated rule set immediately, bypassing the learning curve that originally produced those rules.

Specificity correlated with effectiveness: Early rules were broad. Later rules were precise. Specific, actionable rules were more reliably followed than general guidance.

### III-E Rule Conflicts: A Concrete Example

We encountered one genuine rule conflict. Rule 1 stated: “All IDisposable types MUST use using declarations.” Rule 8 stated: “HttpClient from IHttpClientFactory must NOT be disposed by the caller.” These directly contradicted each other for factory-created instances.

Resolution was straightforward: Rule 1 was refined with a scope qualifier. The conflict was detected during a code review and resolved as a factual question—which framework behavior is correct?—rather than a judgment call.

### III-F Multi-Interface Behavioral Transfer

Persistent behavioral rules transfer across heterogeneous agent interfaces. IDE-integrated agents excelled at code analysis (full repository context, symbol resolution), while terminal-based agents excelled at execution (querying issue trackers, running database queries). Both loaded the same instruction file and benefited equally from accumulated rules.

This suggests that behavioral rule sets can serve as a shared memory layer for multi-agent architectures [10, 11] where specialized agents handle different phases of the development workflow.

## IV Experimental Results

### IV-A Experimental Setup

Deployment context: A microservices platform with 35+ services, 13 custom agent definitions, 10 operational skills, and 6 shared knowledge documents. Two agent interfaces consumed the same shared instruction file.

Data sources: (1) A chronological task log with 11 dated entries; (2) version-controlled instruction file with 2 committed revisions and continuous local growth; (3) persistent memory files totaling 4 topic-specific documents; (4) 36 PR reviews across 6 repositories.

### IV-B Rule Accumulation Dynamics

Table III shows the growth of the rule set across the observation period.

| Week | Behavioral Rules | Code Standards | Checklist | Cumulative Sessions |
|---:|---:|---:|---:|---:|
| 0 | 5 | 3 | 0 | 0 |
| 1 | 10 | 8 | 9 | 3 |
| 2 | 16 | 12 | 13 | 6 |
| 3 | 18 | 15 | 15 | 9 |
| 4 | 18 | 15+ | 15 | 11 |

The accumulation rate follows a logarithmic curve: rapid initial growth tapering as the rule set covers the most frequently encountered patterns. The combined instruction file grew to approximately 4,809 words (~6,250 tokens), consuming less than 5% of a 128K-token context window.

### IV-C Error-Class Recurrence Analysis

Table IV shows the central result: zero recurrences across all tracked error classes.

| Error Class | Rule Added | Post-rule Exposures | Recurrences |
|---|---|---:|---:|
| Factory HttpClient disposal | W1-S3 | 8 | 0 |
| String interpolation in logs | W1-S2 | 9 | 0 |
| Null-forgiving ! | W1-S3 | 8 | 0 |
| Config in lambda | W1-S3 | 8 | 0 |
| Missing SSRF allowlist | W2-S4 | 7 | 0 |
| throw ex vs throw | W1-S1 | 10 | 0 |
| Missing enum converter | W2-S5 | 6 | 0 |
| Redundant re-computation | W1-S3 | 8 | 0 |
| De Morgan’s violation | W1-S1 | 10 | 0 |
| Total | | 74 | 0 |

Across 9 tracked error classes with 74 cumulative post-rule session-exposures, zero recurrences were observed. We emphasize that this is an observational result inside a single deployment, not a controlled experiment: the absence of recurrence within the window does not establish a permanent guarantee, and is bounded by the threats to validity discussed in Section VIII.

### IV-D Review Comment Category Shift

We analyzed 36 PR reviews across 6 repositories, categorizing comments using criteria adapted from prior code review studies [17, 18]. Table V shows the distribution.

| Comment Category | Count | % |
|---|---:|---:|
| Architecture / Design | 12 | 33% |
| API design / Contracts | 7 | 19% |
| Performance (complexity) | 5 | 14% |
| Auth / Security | 4 | 11% |
| Cosmos query correctness | 3 | 8% |
| Mechanical correctness | 3 | 8% |
| Code style / Formatting | 2 | 6% |

Mechanical correctness and style issues account for only 14% of review comments, while architecture, API design, and performance account for 66%.

### IV-E Knowledge Transfer Patterns

We classified 15 documented review learnings by transfer characteristics (Table VI).

| Transfer Type | Count | Example |
|---|---:|---|
| Same-repo, same class | 6 | IDisposable across services |
| Cross-repo, same class | 4 | Enum converter transfer |
| Cross-tool, same rules | 3 | IDE → terminal |
| Cross-task-type | 2 | Code generation → review |

60% of knowledge transfers (9/15) crossed repository or tool boundaries, confirming that tool-agnostic encoding enables broad applicability.

### IV-F Rule Specificity Evolution

Table VII tracks the linguistic specificity of rules over time.

| Period | General | Specific | Ratio |
|---|---:|---:|---:|
| Week 1 | 4 | 6 | 0.60 |
| Week 2 | 4 | 12 | 0.75 |
| Week 3–4 | 4 | 14 | 0.78 |

The specificity ratio increases monotonically, reflecting both specific new rules from concrete review comments and refinement of existing general rules.

### IV-G Multi-Layer Memory Architecture

The framework evolved a three-layer memory architecture (Table VIII).

| Layer | Scope | Persistence | Words |
|---|---|---|---:|
| Shared instructions | All agents | Permanent | 3,181 |
| Personal rules | Single developer | Permanent | 1,628 |
| Session memory | Single conversation | Ephemeral | Variable |

Total persistent memory: ~4,809 words (~6,250 tokens), consuming <5% of a 128K context window.

### IV-H Session Task Diversity

Table IX shows that the framework applies beyond code generation.

| Activity Type | Sessions | Rules |
|---|---:|---:|
| Code generation + PR | 4 | 9 |
| PR review | 3 | 4 |
| Incident investigation | 2 | 3 |
| Cross-service architecture | 1 | 1 |
| Repository maintenance | 1 | 1 |

PR reviews and incident investigations contributed 39% of rules despite being non-generative tasks.

## V Discussion

### V-A Summary of Findings

Three findings emerge from the deployment. First, the closed-loop pattern is feasible: 18 behavioral rules, 15+ language-specific code standards, and a 15-item self-review checklist were derived directly from accepted human review feedback and stored in version-controlled instruction files consumed by multiple agent surfaces without any model-side change.

Second, accumulated rules suppress the recurrence of previously-corrected error classes within the observation window. Across 9 tracked error classes and 74 cumulative post-rule session exposures, no recurrences were observed. We deliberately frame this as an observational result: it establishes that the suppression effect is large enough to be visible inside a four-week deployment without a controlled baseline, but it is not equivalent to a statistical guarantee. The limits of this measurement—single-team scope, absence of an A/B control, single primary language—are discussed in Section VIII.

Third, the encoded knowledge transfers across heterogeneous agent tools, repositories, and task types. 60% of observed knowledge-transfer events (9/15) crossed repository, tool, or task-type boundaries, and rules added through one agent interface were observed to take effect immediately in sessions conducted through a different interface.

The mechanism that makes this work is the choice of representation: declarative natural-language constraints in plain Markdown are consumable by any LLM-based agent that loads the file as system context.

### V-B Match and Contribution

Engineering management of an emerging technology. LLM-based coding agents are an emerging engineering capability whose behavior is normally opaque and non-reproducible across sessions. The framework operationalizes such agents inside an existing engineering workflow—code review—so that organizational engineering knowledge becomes a first-class, auditable artifact rather than tacit knowledge that is lost between sessions. Because the approach is vendor- and tool-agnostic, it is directly applicable to other engineering organizations adopting AI coding agents at scale.

Governance of an emerging technology. The framework provides an explicit governance model for agent behavior: every rule has an identifiable origin (a review event), an owner (the engineer who accepted the comment), a change record (the pull request that added the rule), and a position in a self-review checklist that runs before code submission. This makes the agent’s operational behavior auditable, reviewable, and managed using the same engineering practices that already exist for other production artifacts.

Practical frameworks. The paper describes a deployable artifact—a structured instruction file with a rule schema, lifecycle, validation, and feedback loop—rather than a research prototype. The deployment used only standard infrastructure (Git, Markdown, pull-request review, plain-text validation scripts) and required no fine-tuning, no model-specific tooling, and no specialized memory backends. Other organizations can reproduce the pattern with infrastructure they already operate.

Implementation challenges. We report concrete operational issues so adopters can anticipate them: a real rule conflict and its resolution, the governance questions that the rule lifecycle must answer, and the validity threats that bound the empirical results. The honest limitations (single-team scope, single language, four-week observation period, absence of a controlled baseline) are surfaced rather than hidden.

Value creation. Two value channels are documented. First, recurrence of previously-corrected error classes is suppressed within the deployment window, freeing reviewer attention for higher-level concerns: 66% of observed PR review comments concerned architecture, API design, or performance, while only 14% remained on mechanical correctness. Second, the accumulated rule set acts as a transferable onboarding artifact: new team members inherit the organization’s full review history immediately, compressing the learning curve that originally produced those rules.

## VI Comparison with Related Work

### VI-A Comparison Framework

| Dimension | Reflexion | ExpeL | Voyager | CodeReviewer | SWE-agent | OpenClaw | Ours |
|---|---|---|---|---|---|---|---|
| Learning signal | Self-verbal | Self-experience | Environment | Pre-training | Environment execution | User conversation | Human review |
| Persistence | Episodic | Partial | Skill library | Weights | None | Personal | Version-controlled rules |
| Cross-session | No | Partial | Yes | Model | No | Yes | Yes |
| Weight updates | No | No | No | Yes | No | No | No |
| Feedback source | Self | Self | Game | Training data | Tests | User | Human expert |
| Domain | Benchmarks | Benchmarks | Minecraft | OSS repositories | SWE-bench | General | Production |
| Recurrence prevention | Not measured | Not measured | Not measured | N/A | Not measured | N/A | 0% (74 exposures) |
| Human-in-loop | No | No | No | Training only | No | Yes | Every cycle |

### VI-B Reflexion: Verbal Reinforcement Within Sessions

Shinn et al. [13] propose Reflexion, where LLM agents verbally reflect on task feedback and maintain reflective text in an episodic memory buffer, achieving 91% pass@1 on HumanEval.

Key differences: (1) Reflexion’s memory is episodic and does not transfer to new sessions; our rules persist permanently. (2) Reflexion uses self-generated feedback; we use human expert feedback. (3) Reflexion measures pass rate improvement on isolated problems; we measure error-class suppression across diverse production tasks.

The two approaches are complementary: Reflexion for within-session iteration, accumulated rules for preventing known mistakes from the start. Concretely, a Reflexion-style trajectory generated inside a single problem-solving episode is discarded when the episode ends, so a mistake fixed in episode n can re-appear in episode n+1.

Our rules cross the session boundary by construction: once a human-accepted comment is codified, every subsequent session—potentially using a different model or agent surface—loads it as part of its operating context. The two mechanisms operate on different timescales (sub-episode vs. inter-session) and on different feedback sources (model self-critique vs. human expert), and can be combined without conflict.

### VI-C ExpeL: Experiential Learning Across Tasks

Zhao et al. [14] introduce ExpeL, where agents autonomously gather experiences and extract natural language insights.

Key differences: (1) ExpeL learns from autonomous experience; we learn from human review. (2) ExpeL transfers within the same task type; our rules transfer across fundamentally different task types. (3) ExpeL’s insights may include hallucinated generalizations; our rules are human-validated. The validation requirement is not a stylistic preference: because the rule set is loaded as authoritative context in every session, an incorrect rule would amplify rather than correct errors. Tying every rule to an accepted human review comment provides a verifiable provenance that ExpeL’s autonomous insight extraction does not.

### VI-D Voyager: Persistent Skill Libraries

Wang et al. [15] introduce Voyager, building an ever-growing skill library of executable code in Minecraft. Both systems demonstrate that persistent, version-controlled knowledge enables compounding capability growth. The key difference is representation: Voyager stores executable code functions; we store declarative constraints in natural language.

### VI-E Pre-trained Code Review Models

Li et al. [4] and Tufano et al. [5] propose pre-trained models for automated code review. Key differences: (1) These approaches fine-tune model weights; we inject rules through context. (2) Their knowledge is frozen at training time; ours accumulates in real-time. (3) They generalize across public repositories; we capture organization-specific conventions invisible in public codebases.

### VI-F SWE-bench Agents

SWE-bench [12] and its agent implementations [16, 19, 20] evaluate LLM agents on isolated GitHub issue resolution. The state-of-the-art resolves 20–40% of SWE-bench Lite issues.

Our framework addresses an orthogonal dimension: SWE-bench asks “Can you solve this issue?” while we ask “Do you avoid known mistake classes?” There is currently no benchmark evaluating behavioral consistency over time.

### VI-G Self-Taught Optimizer, Self-Refine, and Self-Debugging

Zelikman et al. [21] propose STOP, where LLMs recursively improve their own scaffolding code. Madaan et al. [3] propose Self-Refine, where LLMs iteratively improve their outputs through self-generated critique. Chen et al. [22] propose Self-Debugging via rubber-duck-style explanation. All three operate within a single execution context; our framework captures improvements permanently.

### VI-H Memory-Augmented LLM Systems

MemoryBank [8] and related systems provide LLMs with persistent memory mechanisms. Our approach is architecturally simpler: rules are stored in plain-text Markdown files that are version-controlled, human-readable, and auditable.

### VI-I Personal AI Assistants with Persistent Memory

OpenClaw [24] provides persistent memory and skill libraries for personal AI assistants. Key differences: (1) OpenClaw’s memory comes from free-form conversations; our rules come from accepted code review feedback. (2) OpenClaw is single-user; our framework is team-level. (3) OpenClaw remembers facts; our framework prevents error classes through declarative constraint injection.

## VII Design Principles

Through iterative deployment, we identified six principles:

1. Monotonic growth: Rules are added and refined but not removed, echoing the continuous improvement principle in DevOps practice [9].
2. Specificity over generality: Concrete, actionable constraints outperform abstract guidance. Specificity ratio increased from 0.60 to 0.78.
3. Origin tracking: Each rule traces to the review comment or production event that inspired it.
4. Tool-agnostic encoding: Rules are structured Markdown readable by any LLM. Cross-interface transfer was confirmed across 2 platforms.
5. Validated growth: Every rule addition is checked by automated validation.
6. Shared ownership: The instruction file lives in a shared repository with PR-based changes.

## VIII Limitations and Threats to Validity

Context window constraints: Current rule sets (~6,250 tokens) are within modern limits, but unbounded growth could require hierarchical organization or summarization.

Rule conflicts: We encountered one conflict. Automated conflict detection would reduce reliance on manual identification.

Governance at scale: The current model works for a single team. Multiple teams would require hierarchical or namespaced rule sets, plus a clear policy for resolving cross-team rule conflicts. Without that, a centrally-maintained rule set risks either fragmenting along team lines or accumulating contradictions that silently degrade agent behavior. We treat scaled governance as an open problem rather than a solved one.

Lack of controlled baseline or ablation: We do not have a parallel control group, and we did not run a paired ablation comparing the framework against static prompt engineering or a no-rule baseline on the same task stream. The suppression and review-shift results should therefore be read as initial empirical evidence, not as a causal proof. A future A/B deployment (rule-loading agent versus rule-free agent, run on the same incoming task queue) would close this gap and is described under Future Work.

Generalizability and barriers to adoption: The framework’s value depends on three preconditions that may not hold in every organization: (i) a code review culture that produces accepted, written comments at sufficient rate; (ii) engineers willing to spend a small amount of additional time per accepted comment to codify it as a rule; and (iii) tooling whose agent surfaces actually load and respect a project-level instruction file. Where any of these is missing, the feedback loop will starve or be ignored. We expect the strongest adoption in mid- to large-sized engineering organizations that already practice peer review on every change.

Statistical significance: The reported counts (74 post-rule exposures across 9 error classes, 36 PRs across 6 repositories, 11 sessions) are small in absolute terms. Although the observed effects (no recurrences within the window, a clear shift toward design-level review comments) are consistent across the dataset, the sample is not large enough to make a formal statistical significance claim and we do not report p-values. Larger, longer deployments are needed before tighter quantitative claims are appropriate.

### VIII-A Threats to Validity

Single deployment environment: All observations are from one organization. Effects may differ in other codebases or languages.

Language specificity: The deployment used a typed language with strong framework conventions. Languages with weaker compile-time constraints, or codebases with less consistent framework usage, may both generate a different distribution of review comments and benefit less from rule-based suppression.

Reviewer quality dependency: Rule quality depends on human review quality. Incorrect rules amplify errors, and a noisy review culture can poison the rule set faster than the validation step can catch.

Observation period: Four weeks and 11 sessions provide initial evidence but are insufficient for long-term growth dynamics. In particular, the framework’s behavior at the point where the rule set saturates the available context window has not yet been observed.

## IX The Missing Benchmark

Existing coding benchmarks measure static capability: can the agent solve problem X right now? No existing benchmark measures behavioral consistency over time.

We propose that such a benchmark would consist of:

1. A rule corpus: Curated behavioral rules from real review feedback.
2. Seed tasks: Code generation tasks that naturally trigger ruled-against patterns.
3. Temporal evaluation: A sequence of tasks where earlier tasks produce corrections and later tasks test persistence.
4. Cross-session boundary: The critical test is whether corrections survive session boundaries.

This would complement SWE-bench, HumanEval, and CodeReview benchmarks by adding a temporal learning dimension.

## X Conclusion

We have presented a closed-loop framework for self-improving AI coding agents through accumulated behavioral rules. The key insight is that human review feedback, when codified as persistent and version-controlled rules, creates a ratchet effect: the set of error classes the agent can self-detect grows monotonically.

In production deployment across 35+ microservices over 11 recorded sessions, the rule set grew from 5 initial rules to 18 behavioral rules, 15+ code standards, and a 15-item self-review checklist. We observed no recurrences across 9 tracked error classes within 74 cumulative post-rule session-exposures during the observation window—an observational result whose limits are made explicit in Section VIII. Review comments shifted toward design-level concerns (66% architecture/API/performance vs. 14% mechanical correctness), and rules transferred across boundaries in 60% of observed events.

Compared to related approaches, our framework uniquely combines human-sourced feedback with permanent cross-session persistence without weight updates. It addresses behavioral consistency over time—a dimension existing benchmarks do not measure. The approach requires no fine-tuning, no model-specific infrastructure, and no changes to existing LLM architectures.

### Operationalizing the Framework in an Enterprise Setting

For an engineering organization considering adoption, the framework reduces to a small set of operational practices that can be introduced incrementally without changing the existing toolchain:

1. Add a project-level instruction file (e.g., AGENTS.md) under version control, with sections for behavioral rules, language-specific code standards, and a self-review checklist.
2. Define a rule promotion convention in the team’s pull-request template: when a reviewer accepts a comment that describes a generalizable mistake, the author either adds a rule in the same PR or files a follow-up to do so.
3. Wire the file into every agent surface the team already uses (IDE-integrated assistants, terminal-based agents, review bots) so they all consume the same context. No model change is needed.
4. Add a lightweight validation step (a script in CI or a pre-commit hook) that verifies the instruction file is well-formed and that new rules follow the schema.
5. Treat the file as a shared artifact: changes go through pull-request review, just like code, so the rule set inherits the team’s existing governance.

### Future Research Directions

Several directions follow naturally from this work and from the limitations identified in Section VIII:

1. A controlled A/B study comparing rule-loading agents against rule-free baselines on the same incoming task stream, with pre-registered metrics for review-comment volume, defect escape rate, and reviewer time-on-task.
2. Cross-organization replication in different programming languages, codebase sizes, and review cultures, to test the boundary conditions of the suppression effect.
3. A behavioral-consistency benchmark that complements SWE-bench and HumanEval by measuring whether a corrected mistake stays corrected across session boundaries.
4. Automated rule proposal and conflict detection: agents proactively suggesting candidate rules from clusters of similar review comments, and flagging proposed rules that contradict existing ones before they are merged.
5. Multi-team governance models that allow team-specific rule sets to compose without producing silent contradictions, including provenance tracking when a rule is promoted from a team scope to an organization-wide scope.

Human review does not merely correct AI-generated code; in this framework, it permanently upgrades future agent behavior.

## References

1. M. Chen et al., “Evaluating large language models trained on code,” arXiv preprint arXiv:2107.03374, 2021.
2. Y. Fan et al., “Large language models for software engineering: A systematic literature review,” ACM Trans. Softw. Eng. Methodol., 2024.
3. A. Madaan et al., “Self-refine: Iterative refinement with self-feedback,” in Proc. NeurIPS, 2023.
4. Z. Li et al., “Automating code review activities by large-scale pre-training,” in Proc. ESEC/FSE, 2022.
5. R. Tufano et al., “Using pre-trained models to boost code review automation,” in Proc. ICSE, 2022.
6. L. Ouyang et al., “Training language models to follow instructions with human feedback,” in Proc. NeurIPS, 2022.
7. D. Zhou et al., “Least-to-most prompting enables complex reasoning in large language models,” in Proc. ICLR, 2023.
8. W. Zhong et al., “MemoryBank: Enhancing large language models with long-term memory,” in Proc. AAAI, 2024.
9. G. Kim et al., *The DevOps Handbook*. IT Revolution Press, 2016.
10. S. Hong et al., “MetaGPT: Meta programming for a multi-agent collaborative framework,” in Proc. ICLR, 2024.
11. C. Qian et al., “Communicative agents for software development,” in Proc. ACL, 2024.
12. C. E. Jimenez et al., “SWE-bench: Can language models resolve real-world GitHub issues?” in Proc. ICLR, 2024.
13. N. Shinn et al., “Reflexion: Language agents with verbal reinforcement learning,” in Proc. NeurIPS, 2023.
14. A. Zhao et al., “ExpeL: LLM agents are experiential learners,” in Proc. AAAI, 2024.
15. G. Wang et al., “Voyager: An open-ended embodied agent with large language models,” arXiv preprint arXiv:2305.16291, 2023.
16. J. Yang et al., “SWE-agent: Agent-computer interfaces enable automated software engineering,” arXiv preprint arXiv:2405.15793, 2024.
17. A. Bacchelli and C. Bird, “Expectations, outcomes, and challenges of modern code review,” in Proc. ICSE, 2013.
18. C. Sadowski et al., “Modern code review: A case study at Google,” in Proc. ICSE-SEIP, 2018.
19. Y. Zhang et al., “AutoCodeRover: Autonomous program improvement,” in Proc. ISSTA, 2024.
20. C. S. Xia et al., “Agentless: Demystifying LLM-based software engineering agents,” arXiv preprint arXiv:2407.01489, 2024.
21. E. Zelikman et al., “Self-taught optimizer (STOP): Recursively self-improving code generation,” in Proc. COLM, 2024.
22. X. Chen et al., “Teaching large language models to self-debug,” arXiv preprint arXiv:2304.05128, 2023.
23. X. Li, “A review of prominent paradigms for LLM-based agents: Tool use (including RAG), planning, and feedback learning,” in Proc. COLING, 2025.
24. P. Steinberger, “OpenClaw: Personal AI assistant,” https://github.com/openclaw/openclaw, 2025.

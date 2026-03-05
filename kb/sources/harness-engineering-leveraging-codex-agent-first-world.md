---
source: https://openai.com/index/harness-engineering/
captured: 2026-03-05
capture: web-fetch
type: blog-post
---

# Harness Engineering: Leveraging Codex in an Agent-First World

Author: Ryan Lopopolo, Member of the Technical Staff, OpenAI
Source: https://openai.com/index/harness-engineering/
Date: February 11, 2026

---

## Overview

OpenAI's Codex team built and shipped an internal beta product with over one million lines of code over five months — with zero lines of manually written code. Every line was written by Codex agents. A small team (starting with three engineers, growing to seven) guided the process through pull requests and CI workflows, averaging 3.5 PRs per engineer per day. The first commit to an empty repository landed in late August 2025, using Codex CLI with GPT-5 to generate the initial scaffold.

The core thesis: the engineer's job shifts from writing code to designing environments, specifying intent, and building feedback loops that allow agents to do reliable work.

---

## What Is a Harness?

A harness is the design and implementation of systems that:

- **Constrain** what an AI agent can do
- **Inform** the agent about what it should do
- **Verify** that the agent did it correctly
- **Correct** the agent when it goes wrong

Harness engineering is distinct from context engineering. Context engineering asks: what should the agent see? Harness engineering asks: what should the system prevent, measure, and correct?

---

## The Three Pillars

### 1. Context Engineering

The first lesson was simple: give Codex a map, not a 1,000-page instruction manual. Context is a scarce resource. A giant instruction file crowds out the task, the code, and the relevant docs — so the agent either misses key constraints or starts optimizing for the wrong ones.

The team maintains a short AGENTS.md (roughly 100 lines) that serves as a map, with pointers to deeper sources of truth elsewhere in the repository: design docs, architecture maps, execution plans, quality grades — all versioned alongside the code. Anything the agent cannot access in-context does not exist.

Context also extends beyond static documentation:

- **Dynamic observability**: Chrome DevTools Protocol wired into the runtime so agents can see the UI and reproduce browser-side bugs. Per-task isolated observability stacks with logs, metrics, and spans. A prompt like "startup should complete under 800ms" becomes measurable, not aspirational.
- **Repository-local knowledge**: The codebase is optimized for Codex's legibility first. Human engineers' goal is to make it possible for an agent to reason about the full business domain directly from the repository itself.

### 2. Architectural Constraints

Architectural boundaries are enforced mechanically, not just documented. The team defines a strict dependency graph:

```
Types → Config → Repo → Service → Runtime → UI
```

Structural tests validate compliance and prevent layer violations before merge. Custom linters enforce naming conventions, module boundaries, and semantic correctness. Critically, linter error messages double as remediation instructions — every failure message teaches the agent the fix. The system is not just blocking mistakes; it is training the agent while it works.

Agents perform better within bounded solution spaces. Architectural constraints are not limitations — they are the scaffolding that makes reliable generation possible.

### 3. Entropy Management

Agents replicate patterns that already exist, good or bad. Drift is inevitable.

Early on, the team spent roughly 20% of their time (Fridays) manually cleaning "AI slop" — low-quality generated artifacts accumulating in the codebase. This did not scale. The solution: encode standards directly into the repository and automate cleanup.

The approach:

- **Golden rules**: Quality standards captured as explicit, versioned constraints.
- **Quality grades**: Sections of the codebase rated and tracked over time.
- **Background cleanup agents**: Periodic agents scan for stale documentation, constraint violations, and pattern deviations, opening small refactoring PRs. Most are auto-merged.

This is essentially garbage collection for code quality. Human taste is captured once, enforced continuously. Cleanup throughput scales proportionally with code generation throughput.

---

## How the Engineering Work Changed

### What humans stopped doing

Humans never directly contributed any code — this became a core philosophy, not an accident. Manually writing code was treated as a failure mode, a sign that the harness was missing a capability.

### What humans started doing

When agents struggled, engineers asked: what capability is missing? What constraint is unenforced? They then built the tool, wrote the linter, or added the structural test to make the failure category impossible. Every agent mistake is an opportunity to engineer a solution so the agent never makes that mistake again.

The engineering question shifted from "what should we prompt?" to "what capability is missing, and how do we make it visible and enforceable?"

### The compounding effect

Good harnesses compound. Each constraint added makes future agent work more reliable. Each cleanup agent reduces the maintenance burden on human engineers. The system gets better at absorbing what agents produce without constant supervision.

---

## Knowledge Management

Because the repository is entirely agent-generated, it is optimized first for Codex's legibility. Human engineers maintain:

- Design documents versioned with the code
- Architecture maps agents can read directly
- Execution plans decomposing tasks into agent-sized units
- Quality grades tracking code health by section

A background agent scans for documentation gaps and constraint violations, opening cleanup PRs. Repository knowledge is treated as a product: versioned, maintained, kept fresh by agents.

---

## Scale Achieved

Over five months:

- ~1 million lines of code in the repository
- ~1,500 pull requests opened and merged
- 3.5 PRs per engineer per day average throughput
- Team grew from 3 to 7 engineers
- Throughput increased as the team grew

---

## Key Lessons

1. **Context is scarce** — a short map beats a long manual
2. **Enforce architecture mechanically** — structural tests catch what instructions miss
3. **Write errors that teach** — linter messages double as agent instructions
4. **Automate entropy** — cleanup must scale with generation
5. **Every mistake is a harness bug** — encode the fix, don't just patch the output
6. **Observable environments unlock reliable prompts** — measurable constraints replace aspirational ones
7. **The bottleneck was the environment, not the model** — agents had the capability; they lacked structure, tools, feedback, and clear constraints

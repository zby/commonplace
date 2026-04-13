---
description: Skill-based context engineering framework — 14 instructional modules covering attention mechanics, multi-agent patterns, memory, evaluation. Strong on operational patterns, weaker on learning theory.
type: agent-memory-system-review
traits: [has-comparison, has-external-sources]
status: current
tags: [related-systems]
last-checked: "2026-02-25"
---

# Agent Skills for Context Engineering

A collection of reusable instructional modules ("skills") for building production-grade AI agent systems, focused on **context engineering** — managing what enters the model's attention budget. Skills are designed to be loaded into an agent's context as operational guidance (via Claude Code plugin or similar), not just read as documentation. Each skill has activation triggers ("use when designing tools", "use when debugging context problems") that shape how the agent approaches work. However, skills contain no tools, scripts, or hooks — they influence agent reasoning, they don't execute actions.

**Repository:** https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering

## Core Ideas

**Context as finite resource, not token bucket.** The central argument is that context windows are constrained by attention mechanics, not raw capacity. Lost-in-the-middle effects, context poisoning (errors compound through references), and context distraction (irrelevant info overwhelms relevant) are the real failure modes. Practical implication: optimise for signal quality, not quantity.

**Progressive disclosure architecture.** Load names/descriptions at startup, full content on activation. This independently converges with our [instruction specificity matching loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md).

**Architectural reduction.** Fewer, more general tools outperform many specialised ones. Key evidence: Vercel's d0 went from 17 specialised tools to 2 primitives (bash + SQL), improving success from 80% to 100%. Aligns with our YAGNI stance and supports the claim that [the bitter lesson boundary](../../notes/bitter-lesson-boundary.md) favours simplicity.

**Multi-agent for context isolation, not roles.** Sub-agents exist to get fresh context, not to anthropomorphise organisational charts. Token cost is ~15x single-agent but enables parallel work. Key finding: 80% of performance variance comes from token usage, only 5% from model choice.

**Filesystem beats specialised memory tools.** Letta's filesystem memory (74% LoCoMo) outperforms Mem0's vector+graph tools (68.5%). Standard Unix utilities outperform custom exploration tools. Directly validates our markdown-files-as-source-of-truth approach.

## Borrowable Ideas

**Chain-of-thought before scoring (ready now).** In our system this is a good default for any soft-oracle evaluation: review, compare, or rank only after writing down the reasoning that led to the score. That would make [quality signals work](../../notes/quality-signals-for-kb-evaluation.md) less brittle when the judgment is not deterministic.

**Position-bias mitigation (ready now for pairwise comparisons).** When we compare two prompts, two context packages, or two candidate notes, we should swap order and check whether the conclusion changes. That is a cheap guard against false confidence in any future evaluation harness.

**Degradation testing (needs a use case).** Running the same task at multiple context sizes is useful if we are trying to find cliffs in a retrieval or session pipeline. It is not a generic note-writing rule, but it would matter if we build a repeatable context-budget experiment.

**Tokens-per-task, not tokens-per-request (ready now).** This is the clearest transfer: our workshop and review processes should be designed around end-to-end task cost, not isolated call size. It is a better lens than "keep each prompt short" because it accounts for multi-step work.

**Anchored iterative summaries (needs a use case).** The Intent / Files Modified / Decisions / State / Next Steps format looks useful for workshop handoffs, but only once we have a stable session artifact to summarize. Right now it is a good candidate for future workshop design, not a universal KB convention.

## Other Notable Concepts

- **Tokens-per-task, not tokens-per-request** — optimise total task cost, not individual request size. Useful framing for codification decisions.
- **Observation masking** — tool outputs consume 80%+ of tokens; replace verbose outputs with references. Relevant when we build session infrastructure.
- **Anchored iterative summarization** — structured session summaries (Intent / Files Modified / Decisions / State / Next Steps). Also relevant for future session work.
- **Telephone game problem** — supervisors paraphrasing sub-agent outputs lose fidelity. Fix: direct pass-through or file-based communication.

## Comparison with Our System

**Strong alignment:** They independently converge with our progressive disclosure, filesystem-first knowledge, and tool consolidation. Their skills are loaded by name first and expanded on demand, which is the same general loading strategy we use in the KB.

**We go deeper:** Our [verifiability gradient](../../notes/verifiability-gradient.md) and [oracle strength spectrum](../../notes/oracle-strength-spectrum.md) explain when a pattern should become a rule, a script, or stay a judgment call. Their material has operational tactics, but not a comparable theory for when to harden a practice.

**They go deeper:** Attention mechanics, degradation data, and evaluation procedure. They give concrete evidence about model behavior under context pressure, while our notes are still mostly the theory and architecture layer around that problem.

**Tradeoff:** Their system is stronger as an operator's playbook; ours is stronger as a knowledge architecture. Their value is "what to do"; ours is "how to structure and verify the durable artifacts those behaviors produce."

## Curiosity Pass

- **The main contribution may be reduction of attention burden, not the skill abstraction itself.** The repo is strong evidence that smaller loading surfaces and simpler tool surfaces help. The open question is whether the "skill" abstraction adds much beyond a convenient packaging layer for those reductions.
- **The filesystem win may be pragmatic rather than ontological.** The Letta-versus-Mem0 result could reflect fewer moving parts, better integration with standard Unix tools, or better benchmark fit. It is evidence for files in this setting, not proof that files are universally the right memory substrate.
- **The evaluation claims need replication outside this harness.** The degradation numbers and token-variance claim are interesting, but they should be treated as context-sensitive until we see them hold across other tasks and models. The simpler alternative explanation is that these are benchmark-specific effects.

## What to Watch

- Do they develop learning theory (moving from operational patterns toward a codification-like framework)?
- Does the skill specification evolve toward something like our document classification?
- How does the evaluation methodology mature — could it become a reusable component?
- Do they stay platform-agnostic or drift toward Claude Code specifics?

Relevant Notes:

- [getsentry/skills](./getsentry-skills.md) — contrasts: that review covers a production implementation with a skill-writer meta-skill and the Agent Skills spec; this review covers a reference/teaching library. Same progressive disclosure architecture, very different operational maturity

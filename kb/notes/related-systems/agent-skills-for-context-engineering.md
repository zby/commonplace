---
description: Skill-based context engineering framework — 14 instructional modules covering attention mechanics, multi-agent patterns, memory, evaluation. Strong on operational patterns, weaker on learning theory.
type: note
status: current
areas: [related-systems]
last-checked: 2026-02-25
---

# Agent Skills for Context Engineering

A collection of reusable instructional modules ("skills") for building production-grade AI agent systems, focused on **context engineering** — managing what enters the model's attention budget. Skills are designed to be loaded into an agent's context as operational guidance (via Claude Code plugin or similar), not just read as documentation. Each skill has activation triggers ("use when designing tools", "use when debugging context problems") that shape how the agent approaches work. However, skills contain no tools, scripts, or hooks — they influence agent reasoning, they don't execute actions.

**Repository:** https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering

## Core Ideas

**Context as finite resource, not token bucket.** The central argument is that context windows are constrained by attention mechanics, not raw capacity. Lost-in-the-middle effects, context poisoning (errors compound through references), and context distraction (irrelevant info overwhelms relevant) are the real failure modes. Practical implication: optimise for signal quality, not quantity.

**Progressive disclosure architecture.** Load names/descriptions at startup, full content on activation. This independently converges with our [context-loading-strategy](../../claw-design/context-loading-strategy.md).

**Architectural reduction.** Fewer, more general tools outperform many specialised ones. Key evidence: Vercel's d0 went from 17 specialised tools to 2 primitives (bash + SQL), improving success from 80% to 100%. Aligns with our YAGNI stance and supports the claim that [the bitter lesson boundary](../bitter-lesson-boundary.md) favours simplicity.

**Multi-agent for context isolation, not roles.** Sub-agents exist to get fresh context, not to anthropomorphise organisational charts. Token cost is ~15x single-agent but enables parallel work. Key finding: 80% of performance variance comes from token usage, only 5% from model choice.

**Filesystem beats specialised memory tools.** Letta's filesystem memory (74% LoCoMo) outperforms Mem0's vector+graph tools (68.5%). Standard Unix utilities outperform custom exploration tools. Directly validates our markdown-files-as-source-of-truth approach.

## Evaluation Methodology (worth borrowing)

Their evaluation framework is more concrete than ours:
- **Chain-of-thought before scoring** — 15-25% reliability improvement in LLM-as-judge
- **Position-bias mitigation** — swap positions twice in pairwise comparison, check consistency
- **Degradation testing** — run evals at different context sizes to find performance cliffs

These techniques could strengthen our [quality signals work](../../claw-design/quality-signals-for-kb-evaluation.md), particularly for soft-oracle cases where we're compositing weak signals.

## Other Notable Concepts

- **Tokens-per-task, not tokens-per-request** — optimise total task cost, not individual request size. Useful framing for crystallisation decisions.
- **Observation masking** — tool outputs consume 80%+ of tokens; replace verbose outputs with references. Relevant when we build session infrastructure.
- **Anchored iterative summarization** — structured session summaries (Intent / Files Modified / Decisions / State / Next Steps). Also relevant for future session work.
- **Telephone game problem** — supervisors paraphrasing sub-agent outputs lose fidelity. Fix: direct pass-through or file-based communication.

## Alignment and Divergence

**Strong alignment:** Progressive disclosure, filesystem-first knowledge, start-simple philosophy, tool consolidation.

**We go deeper:** Our [verifiability gradient](../agentic-systems-learn-through-three-distinct-mechanisms.md) and [oracle strength spectrum](../oracle-strength-spectrum.md) provide theory for *when* and *why* to stabilise — they have operational patterns but no learning framework. Our [methodology enforcement as stabilisation](../../claw-design/methodology-enforcement-is-stabilisation.md) has no counterpart in their work.

**They go deeper:** Attention mechanics and degradation data (model-specific thresholds, the four-bucket mitigation). Formal evaluation methodology (LLM-as-judge protocols, bias mitigation). Hosted agent infrastructure (sandboxing, warm pools, pre-built images).

## What to Watch

- Do they develop learning theory (moving from operational patterns toward a crystallisation-like framework)?
- Does the skill specification evolve toward something like our document classification?
- How does the evaluation methodology mature — could it become a reusable component?
- Do they stay platform-agnostic or drift toward Claude Code specifics?

Topics:
- [related-systems](./related-systems-index.md)

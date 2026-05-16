---
description: Deepfates argues LLM "memory" is just context-stuffing that creates false salience (Chekov's gun), advocates agentic context-building, but concludes weight updates are necessary — directly contradicts this KB's durability-not-weights position
source_snapshot: the-thing-we-refer-to-as-memory-in-llms-is-just-a-bunch-of-superfici.md
ingested: "2026-03-25"
type: kb/sources/types/ingest-report.md
source_type: conversation-thread
domains: [context-engineering, memory-architecture, learning-theory]
---

# Ingest: Post by @deepfates — LLM "memory" as context stuffing

Source: the-thing-we-refer-to-as-memory-in-llms-is-just-a-bunch-of-superfici.md
Captured: 2026-03-25
From: https://x.com/deepfates/status/2036857868914483592

## Classification

Type: **conversation-thread** — A single-author thread on X arguing a position about LLM memory design. No formal methodology or data; structured as a chain of observations building toward a conclusion. Not a conceptual essay (too informal, not enough sustained argument) or practitioner report (no system built).

Domains: context-engineering, memory-architecture, learning-theory

Author: @deepfates — active in the AI/LLM discourse community on X. Not an academic researcher or published systems builder in this area. The thread responds to a Karpathy post (linked), suggesting engagement with mainstream AI commentary. Treat as informed commentary, not as expert testimony.

## Summary

Deepfates argues that what passes for "memory" in current LLM systems is just indiscriminate document-stuffing into context windows, creating a Chekov's gun effect where injected facts create false salience expectations. The post proposes agentic context-building (searching/crawling previous conversations) as a better alternative, noting that agents are more confident in single-player terminal environments where they control their own context narrative. In multi-agent scenarios, the user introduces "confusing, unclear, possibly contradictory desires" through a mishmash of instructions, memories, and tools. The post speculates that this context mess explains weak higher-order theory of mind and persona drift, ultimately concluding that "real" memory requires continual learning (weight updates), not just in-context learning.

## Connections Found

The `/connect` discovery found 9 KB notes across three clusters, plus 2 source-to-source connections.

**Direct contradiction:** The post's concluding claim — that solving memory requires continual learning meaning weight updates — is directly contradicted by [continual-learning-open-problem-is-behaviour-not-knowledge](../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md), which argues that durable symbolic artifacts (prompts, schemas, tests) satisfy Simon's learning definition without parameter changes. This is the most substantively interesting tension.

**Context-stuffing problem cluster (5 notes):** The post's diagnosis of the memory-stuffing problem maps closely onto existing KB analysis. [session-history-should-not-be-the-default-next-context](../notes/session-history-should-not-be-the-default-next-context.md) provides the architectural diagnosis; [the-chat-history-model-trades-context-efficiency-for-implementation-simplicity](../notes/the-chat-history-model-trades-context-efficiency-for-implementation.md) explains why stuffing became the default; [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) formalizes the degradation mechanism; [knowledge-storage-does-not-imply-contextual-activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) captures the complementary failure where relevant knowledge does NOT activate; and [llm-context-is-composed-without-scoping](../notes/llm-context-is-composed-without-scoping.md) formalizes the flat concatenation that produces the "mishmash" described in the post.

**Agentic context-building cluster (2 notes):** The post's proposal for agentic crawling is an instance of what [in-context-learning-presupposes-context-engineering](../notes/in-context-learning-presupposes-context-engineering.md) formalizes, and [agents-navigate-by-deciding-what-to-read-next](../notes/agents-navigate-by-deciding-what-to-read-next.md) captures the general principle.

**Cross-contamination:** [flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable](../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md) predicts the multi-agent scenario failures deepfates describes.

**Source-to-source:** The Letta paper ([continual-learning-in-token-space](./continual-learning-in-token-space.md)) makes the opposite bet — continual learning in token space, not weights. The [unfaithful self-evolvers](./large-language-model-agents-are-not-always-faithful-self-evolvers.md) paper provides evidence that raw trajectories (what deepfates advocates crawling) are more useful than condensed memory.

**Synthesis opportunity flagged:** Indiscriminate context loading produces a double failure — irrelevant knowledge creates false salience (deepfates' Chekov's gun) while relevant knowledge fails to activate (the expert-witness problem from the KB) — and both failures are invisible due to soft degradation. No single KB note names this double failure yet.

## Extractable Value

1. **The Chekov's gun metaphor for context-stuffed memory** — "a hundred random facts stuffed into your head" creates the expectation they'll be important, which is a framing for false salience that the KB hasn't used. The existing notes describe soft degradation and attention dilution but don't name the *expectation-creation* effect. [quick-win] Medium reach: the metaphor is vivid but the mechanism (attention/salience distortion from irrelevant context) is already captured; this adds color, not structure.

2. **Single-player vs multi-player context coherence** — The observation that agents are more confident in terminal environments because "all the text in those context windows is meaningful" while multi-agent scenarios produce incoherent context is an empirical observation worth tracking. It suggests context coherence (not just context relevance) matters for agent confidence/performance. [experiment] Medium reach: the single-player/multi-player distinction transfers beyond this specific observation, but the confidence claim is speculative.

3. **The double-failure synthesis** — Combining deepfates' false-salience observation with the KB's activation-gap analysis to name the double failure of naive memory systems: stuffed irrelevant knowledge creates noise AND relevant knowledge fails to activate. This was flagged by `/connect` as a synthesis opportunity. [deep-dive] High reach: this combines two independently documented mechanisms into a failure model that predicts specific observable outcomes in any flat-memory system.

4. **User as noise source in multi-agent context** — The post articulates something the KB discusses architecturally but not from the user-modeling perspective: "The User has confusing, unclear, possibly contradictory desires, which are presented through a mishmash of custom instructions and memory insertions and prompts and skills and tools and markdown files." This frames the user not as a signal source but as an additional noise source that the agent must model before acting. [just-a-reference] Low reach: this is a restatement of the scoping problem from a different vantage point.

5. **Persona drift linked to under-defined assistant character** — The claim that persona drift in long contexts happens partly because "the assistant character is under-defined" is a specific hypothesis the KB hasn't engaged with. [just-a-reference] Low reach: speculative, no evidence offered, and the connection to memory architecture is loose.

## Limitations (our opinion)

This is a conversation thread, so the relevant checks are about what is not argued:

**Reasoning by analogy without testing the analogy.** The Chekov's gun metaphor is evocative but does not establish that LLMs actually treat stuffed context the way a reader treats planted narrative elements. Attention mechanisms and narrative expectation are different phenomena. The metaphor names something real (irrelevant context harms performance) but the mechanism it implies (expectation creation) may not be what's actually happening — soft degradation through attention dilution ([agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md)) is the more mechanistic explanation.

**The continual-learning conclusion does not follow from the diagnosis.** Deepfates correctly identifies the context-stuffing problem, correctly proposes agentic context-building as an improvement, and then leaps to "we need to solve continual learning [meaning weight updates]" without explaining why agentic context-building (which the post just advocated) is insufficient. The post's own middle section argues effectively for a context-engineering solution, then abandons it for a weight-update conclusion. [continual-learning-open-problem-is-behaviour-not-knowledge](../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md) argues this leap is unnecessary — durable symbolic artifacts satisfy the learning criterion without weights.

**Cherry-picked comparison.** The single-player terminal vs multi-agent comparison selects environments that differ on many dimensions (complexity, user unpredictability, task definition, context control) and attributes the confidence difference entirely to context coherence. Other explanations are available: terminal environments have tighter feedback loops, more structured outputs, and better-defined success criteria.

**Theory of mind claims are unsupported.** The link from context-stuffing to weak higher-order theory of mind is asserted without evidence or mechanism. Many simpler explanations exist for weak multi-agent modeling that don't involve memory architecture at all (training data distribution, RLHF alignment toward single-user interaction, inherent difficulty of recursive modeling).

**Unfalsifiable framing.** "There is nothing outside the text" — the post's closing line — is evocative but unfalsifiable and does not add argumentative content. It pattern-matches to postmodern literary criticism more than to systems engineering.

## Recommended Next Action

Write a note titled "Indiscriminate context loading produces a double failure: false salience and activation collapse" connecting to [knowledge-storage-does-not-imply-contextual-activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md), [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), and [session-history-should-not-be-the-default-next-context](../notes/session-history-should-not-be-the-default-next-context.md). It would argue that naive memory systems fail in two complementary ways simultaneously: injected irrelevant knowledge dilutes attention and creates false salience, while relevant knowledge that IS available fails to contextually activate — and both failures are masked by soft degradation, making the system appear functional while silently underperforming. This source provides the false-salience half; the KB already has the activation-failure half. The synthesis is the thing worth capturing.
